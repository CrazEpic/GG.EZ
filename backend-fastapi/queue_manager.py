import asyncio, random, time, aiohttp, aiofiles, os, json
from typing import Optional
from redis.asyncio import Redis
from models import Job, JobStatus, JobType
from pathlib import Path

class QueueManager:
    def __init__(self, redis_url="redis://localhost:6379/0", queue_name="jobs", max_retries: int = 3):
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
        
        if job.type in {JobType.FETCH_MATCH_DATA, JobType.FETCH_TIMELINE}:
            queue_name = f"{self.queue_name}:high"
        else:
            queue_name = f"{self.queue_name}:normal"

        await self.redis.rpush(queue_name, job.id)

    # yea i don't know what to do here
    async def mark_job_complete(self, job: Job):
        job.status = JobStatus.SUCCESS if job.status == JobStatus.RUNNING else JobStatus.FAILED
        print(f"Job {job.id} {job.type.value} complete ({job.status.value})")
        if job.type != JobType.FETCH_ACCOUNT_DATA:
            await self.redis.delete(f"job:{job.id}")
        else:
            await self.redis.expire(f"job:{job.id}", 3600)

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
            await asyncio.sleep(12.5) # the sleeping dragon 🐉🐉🐉🐉🐉

            result = await self.redis.blpop([f"{self.queue_name}:high", f"{self.queue_name}:normal"])
            if not result:
                continue
            _, job_id = result

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
                await self.update_job(job)
                await self.mark_job_complete(job)

    async def requeue_after_delay(self, job: Job, delay: float):
        await asyncio.sleep(delay)
        updated = await self.get_job(job.id)
        if updated and updated.status == JobStatus.RETRYING:
            if job.type in {JobType.FETCH_MATCH_DATA, JobType.FETCH_TIMELINE}:
                queue_name = f"{self.queue_name}:high"
            else:
                queue_name = f"{self.queue_name}:normal"
            await self.redis.rpush(queue_name, job.id)

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
            await self.save_raw_data(job, data)
        elif job.type == JobType.FETCH_ACCOUNT_DATA:
            await self.process_fetch_account_data(job, data)
            job.response_data = data
        elif job.type == JobType.FETCH_MATCHES:
            await self.process_fetch_matches(job, data)
            job.response_data = data
        else:
            job.response_data = data

    async def save_raw_data(self, job: Job, data: dict):
        data_dir = Path(f"{job.params["gameName"]}#{job.params["tagLine"]}/data/raw")
        matchId = job.params.get("matchId")
        sub_dir = "timeline" if job.type == JobType.FETCH_TIMELINE else "match_data"

        folder_path = data_dir / sub_dir
        os.makedirs(folder_path, exist_ok=True)

        file_name = f"{matchId}.json"
        file_path = folder_path / file_name

        async with aiofiles.open(file_path, "w", encoding="utf-8") as f:
            await f.write(json.dumps(data, ensure_ascii=False, indent=4))
        
        # await self.redis.sadd("processed_matches", matchId)

        job.response_data = {"file_path": file_path.as_posix()}

    async def process_fetch_account_data(self, job: Job, data: dict):
        # expect a dict from account endpoint
        if not isinstance(data, dict):
            raise Exception(f"Account data expected to be in a dict, got {type(data)}")
        
        # get match from puuid
        # also ensure that the character cases are consistent with what Riot has for the user
        account_data = data
        puuid = account_data.get("puuid")
        if not puuid:
            raise Exception(f"Error retrieving puuid")
        
        gameName = account_data.get("gameName")
        tagLine = account_data.get("tagLine")
        routing = job.params.get("routing")
        endpoint = f"https://{routing}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"

        parent_set_key = f"parent:{job.id}:all_match_ids"
        active_key = f"parent:{job.id}:active_fetch_matches"
        await self.redis.delete(parent_set_key)
        await self.redis.delete(active_key)

        queues = {400, 420, 430, 440, 490}
        for queue in queues:
            params = job.params.copy()
            params.update({
                "puuid": puuid,
                "gameName": gameName,
                "tagLine": tagLine,
                "queue": queue,
                "parent_job_id": job.id
            })
            new_job = Job(type=JobType.FETCH_MATCHES, endpoint=endpoint, params=params)
            print(f"Branching to new job (matches; {queue=}) from parent {job.id}")
            await self.enqueue(new_job)
            await self.redis.sadd(active_key, new_job.id)
        
        job.status = JobStatus.RUNNING
        await self.update_job(job)

    async def process_fetch_matches(self, job: Job, data: list):
        # expect a list from match endpoint
        if not isinstance(data, list):
            raise Exception(f"Match IDs expected to be in a list, got {type(data)}")
        matchIds = data

        parent_set_key = f"parent:{job.params.get("parent_job_id")}:all_match_ids"
        active_key = f"parent:{job.params.get("parent_job_id")}:active_fetch_matches"
        if data:
            await self.redis.sadd(parent_set_key, *data)

        params = job.params.copy()
        routing = params.get("routing")

        # enqueue fetch match data job for next page
        next_start = params.get("start", 0) + len(matchIds)
        if len(matchIds) > 0:
            endpoint = job.endpoint
            params.update({
                "start": next_start,
            })

            new_job = Job(type=JobType.FETCH_MATCHES, endpoint=endpoint, params=params)
            print(f"Branching to new job (matches) from {job.id}")
            await self.enqueue(new_job)
            await self.redis.sadd(active_key, new_job.id)

        await self.redis.srem(active_key, job.id)
        remaining = await self.redis.scard(active_key)
        if remaining == 0:
            parent_job_id = job.params.get("parent_job_id")
            parent_job = await self.get_job(parent_job_id)
            sample_size = parent_job.params.get("sample_size", 0)
            all_match_ids = await self.redis.smembers(parent_set_key)
            all_match_ids = [matchId.decode() if isinstance(matchId, bytes) else matchId for matchId in all_match_ids]

            if sample_size and sample_size < len(all_match_ids):
                matchIds = random.sample(all_match_ids, sample_size)
            else:
                matchIds = all_match_ids

            for matchId in matchIds:
                # if await self.redis.sismember("processed_matches", matchId):
                #     print(f"Skipping processed match {matchId}")
                #     continue

                match_data_endpoint = f"https://{routing}.api.riotgames.com/lol/match/v5/matches/{matchId}"
                match_data_params = params.copy()
                match_data_params.update({
                    "matchId": matchId,
                })

                timeline_endpoint = f"{match_data_endpoint}/timeline"
                timeline_params = params.copy()
                timeline_params.update({
                    "matchId": matchId,
                })

                match_data_job = Job(type=JobType.FETCH_MATCH_DATA, endpoint=match_data_endpoint, params=match_data_params)
                timeline_job = Job(type=JobType.FETCH_TIMELINE, endpoint=timeline_endpoint, params=timeline_params)
                print(f"Branching to new job (match data) from {job.id}")
                await self.enqueue(match_data_job)
                print(f"Branching to new job (timeline) from {job.id}")
                await self.enqueue(timeline_job)
            
            await self.redis.delete(parent_set_key)
            await self.redis.delete(active_key)
        
        job.status = JobStatus.SUCCESS
        await self.update_job(job)
        return