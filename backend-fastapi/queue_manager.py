import asyncio, random, time, aiohttp, aiofiles
import os, json
from typing import Optional
from redis.asyncio import Redis
from models import Job, JobStatus, JobType
from datetime import datetime, timezone

# from https://developer.riotgames.com/apis#match-v5
# The AMERICAS routing value serves NA, BR, LAN and LAS.
# The ASIA routing value serves KR and JP. 
# The EUROPE routing value serves EUNE, EUW, ME1, TR and RU.
# The SEA routing value serves OCE, SG2, TW2 and VN2.
mappings = {
    "na1": "americas",
    "br1": "americas",
    "la1": "americas",
    "la2": "americas",
    "kr": "asia",
    "jp1": "asia",
    "eun1": "europe",
    "euw1": "europe",
    "me1": "europe",
    "tr1": "europe",
    "ru": "europe",
    "oc1": "sea",
    "sg2": "sea",
    "tw2": "sea",
    "vn2": "sea",
}

class QueueManager:
    def __init__(self, redis_url="INSERT_URL_HERE", queue_name="jobs", max_retries: int = 3):
        self.redis = Redis.from_url(redis_url)
        self.queue_name = queue_name
        self.max_retries = max_retries
        self.session: Optional[aiohttp.ClientSession] = None # to avoid repeatedly opening and closing for each job

    async def start_session(self):
        if not self.session:
            self.session = aiohttp.ClientSession()
    
    async def close_session(self):
        if self.session:
            await self.session.close()
            self.session = None

    async def enqueue(self, job: Job):
        # no nested dicts
        job_dict = job.model_dump()
        job_dict["params"] = json.dumps(job_dict.get("params", {}))
        job_dict["response_data"] = json.dumps(job_dict.get("response_data", {}))
        await self.redis.hset(f"job:{job.id}", mapping=job_dict)
        await self.redis.rpush(self.queue_name, job.id)

    async def enqueue_child_job(self, parent_job_id: str, child_job: Job):
        await self.redis.sadd(f"jobs_for:{parent_job_id}", child_job.id)
        await self.enqueue(child_job)

    async def mark_job_complete(self, job: Job):
        parent_job_id = job.params.get("parent_job_id")
        if parent_job_id:
            # remove from parent's set
            await self.redis.srem(f"jobs_for:{parent_job_id}", job.id)
            remaining = await self.redis.scard(f"jobs_for:{parent_job_id}")
            if remaining == 0:
                # all children done, mark the parent as success
                parent_job = await self.get_job(parent_job_id)
                if parent_job and parent_job.status != JobStatus.SUCCESS:
                    parent_job.status = JobStatus.SUCCESS
                    await self.update_job(parent_job)
                    print(f"Job {parent_job_id} has status SUCCESS (all child jobs done)")

    async def get_job(self, job_id: str) -> Optional[Job]:
        data = await self.redis.hgetall(f"job:{job_id}")
        if not data:
            return None
        decoded = {k.decode(): v.decode() for k, v in data.items()}
        decoded["retries"] = int(decoded["retries"])
        decoded["created_at"] = float(decoded["created_at"])
        decoded["updated_at"] = float(decoded["updated_at"])
        decoded["params"] = json.loads(decoded.get("params", "{}"))
        decoded["response_data"] = json.loads(decoded.get("response_data", "{}"))
        return Job(**decoded)

    async def update_job(self, job: Job):
        job.updated_at = time.time()
        job_dict = job.model_dump()
        job_dict["params"] = json.dumps(job_dict.get("params", {}))
        job_dict["response_data"] = json.dumps(job_dict.get("response_data", {}))
        await self.redis.hset(f"job:{job.id}", mapping=job_dict)

    async def worker_loop(self, worker_id: int):
        print(f"Worker {worker_id} started")
        await self.start_session()
        while True:
            await asyncio.sleep(3) # the sleeping dragon 🐉🐉🐉🐉🐉
            _, job_id = await self.redis.blpop(self.queue_name)
            job_id = job_id.decode()
            job = await self.get_job(job_id)
            if not job:
                continue

            job.status = JobStatus.RUNNING
            await self.update_job(job)

            try:
                # attempt to process job
                print(f"Worker {worker_id} processing job {job.id} {job.type.value}")
                await self.process_job(job)
            except Exception as e:
                job.last_error = str(e)
                job.retries += 1

                # check against max retries
                if job.retries > self.max_retries:
                    job.status = JobStatus.FAILED
                    print(f"Worker {worker_id}: Job {job.id} ({job.type.value}) failed after {job.retries} retries")
                    await self.mark_job_complete(job)
                else:
                    job.status = JobStatus.RETRYING
                    # retry after delay + jitter
                    delay = min(60, (2 ** job.retries) + random.uniform(0, 1))
                    print(f"Worker {worker_id}: Job {job.id} ({job.type.value}) failed ({e}); retrying in {delay:.1f}s (attempt {job.retries}/{self.max_retries}) ")
                    asyncio.create_task(self.requeue_after_delay(job, delay))
            finally:
                await self.mark_job_complete(job)
                await self.update_job(job)

    async def requeue_after_delay(self, job: Job, delay: float):
        await asyncio.sleep(delay)
        updated = await self.get_job(job.id)
        if updated and updated.status == JobStatus.RETRYING:
            await self.redis.rpush(self.queue_name, job.id)

    async def process_job(self, job: Job):
        if self.session is None:
            raise RuntimeError("ClientSession not started")
        
        # retrieve api key
        api_key = os.getenv("RIOT_API_KEY")
        headers = {"X-Riot-Token": api_key}
        
        async with self.session.get(job.endpoint, headers=headers, params=job.params) as resp:
            if resp.status == 429:
                raise Exception("Rate limit exceeded")
            elif resp.status >= 400:
                raise Exception(f"HTTP {resp.status}")
            data = await resp.json()

        # store data somewhere
        if job.type in {JobType.FETCH_TIMELINE, JobType.FETCH_MATCH_DATA}:
            data_dir = "data/raw"
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%d")
            matchId = job.params.get("matchId")
            sub_dir = "timeline" if job.type == JobType.FETCH_TIMELINE else "match_data"
            folder_path = os.path.join(data_dir, sub_dir)
            os.makedirs(folder_path, exist_ok=True)

            file_name = f"{timestamp}_{matchId}_{job.type.value}.json"
            file_path = os.path.join(folder_path, file_name)

            async with aiofiles.open(file_path, "w", encoding="utf-8") as f:
                await f.write(json.dumps(data, ensure_ascii=False, indent=4))

            job.response_data = {"file_path": file_path}
        elif job.type == JobType.FETCH_ACCOUNT_DATA:
            await self.process_fetch_account_data(job, data)
            job.response_data = data
        elif job.type == JobType.FETCH_MATCHES:
            await self.process_fetch_matches(job, data)
            job.response_data = data
        else:
            job.response_data = data

    async def process_fetch_account_data(self, job: Job, data: dict):
        # expect a dict from account endpoint
        if not isinstance(data, dict):
            raise Exception(f"Account data expected to be in a dict, got {type(data)}")
        
        # get match from puuid
        account_data = data
        puuid = account_data.get("puuid")
        if not puuid:
            raise Exception(f"Error retrieving puuid")
        params = job.params.copy()
        params.update({
            "puuid": puuid,
            "parent_job_id": job.id 
        })
        routing = params.get("routing")
        endpoint = f"https://{routing}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
        new_job = Job(type=JobType.FETCH_MATCHES, endpoint=endpoint, params=params)
        print(f"Branching to new job (matches) from parent {job.id}")
        await self.enqueue_child_job(job.id, new_job)

    async def process_fetch_matches(self, job: Job, data: list):
        # expect a list from match endpoint
        if not isinstance(data, list):
            raise Exception(f"Match IDs expected to be in a list, got {type(data)}")
        matchIds = data # list of ids is expected
        params = job.params.copy()
        routing = params.get("routing")
        parent_job_id = params.get("parent_job_id")

        # enqueue fetch match data job for next page
        if len(matchIds) == job.params.get("count", 20):
            endpoint = job.endpoint
            params.update({
                "start": job.params.get("start", 0) + job.params.get("count", 20),
                "parent_job_id": parent_job_id
            })
            new_job = Job(type=JobType.FETCH_MATCHES, endpoint=endpoint, params=params)
            print(f"Branching to new job (matches) from parent {parent_job_id}")
            await self.enqueue_child_job(parent_job_id, new_job)
        
        # enqueue fetch match data jobs and fetch timeline jobs
        for matchId in matchIds:
            match_data_endpoint = f"https://{routing}.api.riotgames.com/lol/match/v5/matches/{matchId}"
            params.update({
                "matchId": matchId,
                "parent_job_id": parent_job_id
            })
            timeline_endpoint = f"{match_data_endpoint}/timeline"
            match_data_job = Job(type=JobType.FETCH_MATCH_DATA, endpoint=match_data_endpoint, params=params)
            timeline_job = Job(type=JobType.FETCH_TIMELINE, endpoint=timeline_endpoint, params=params)
            print(f"Branching to new job (match data) from parent {parent_job_id}")
            await self.enqueue_child_job(parent_job_id, match_data_job)
            print(f"Branching to new job (timeline) from parent {parent_job_id}")
            await self.enqueue_child_job(parent_job_id, timeline_job)