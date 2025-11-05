from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from queue_manager import QueueManager
from models import Job, JobType
from datetime import datetime, timezone
import asyncio

class EnqueueRequest(BaseModel):
    type: JobType
    region: str
    gameName: str
    tagLine: str

app = FastAPI()
queue = QueueManager()

# workers for queue
num_workers = 3

# params for fetching data
startTime = int(datetime(2025, 1, 1, tzinfo=timezone.utc).timestamp()) # unix timestamp for 1/1/2025
endTime = int(datetime(2025, 11, 1, tzinfo=timezone.utc).timestamp()) # unix timestamp for 11/1/2025
count = 5 # number of matches per page fetch

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

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.on_event("startup")
async def startup_event():
    await queue.start_session()
    for i in range(num_workers):
        asyncio.create_task(queue.worker_loop(i + 1))

@app.on_event("shutdown")
async def shutdown_event():
    await queue.close_session()

# enqueue fetch account data here using the region, game name, and tag line
# check job status using the job id returned here and the get_status endpoint
# the job here contains in its response data the response from GET /riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}
# the raw match data and timeline data should be written/stored somewhere (right now to a folder)
@app.post("/enqueue")
async def enqueue(request: EnqueueRequest):
    if request.type != JobType.FETCH_ACCOUNT_DATA:
        raise HTTPException(400, f"Invalid job type: {request}; expected {JobType.FETCH_ACCOUNT_DATA}")
    
    region = request.region.lower()
    routing = mappings.get(region)
    gameName = request.gameName
    tagLine = request.tagLine
    endpoint = None

    if not gameName or not tagLine:
        raise HTTPException(400, f"Invalid gameName and/or tagLine: {gameName=}, {tagLine=}")
    
    if routing == "sea":
        temp_routing = "asia"
        endpoint = f"https://{temp_routing}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{request.gameName}/{request.tagLine}"
    else:
        endpoint = f"https://{routing}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{request.gameName}/{request.tagLine}"       
    params = {
        "region": region,
        "routing": routing,
        "gameName": request.gameName,
        "tagLine": request.tagLine,
        "startTime": startTime,
        "endTime": endTime,
        "start": 0,
        "count": count
    }

    job = Job(type=request.type, endpoint=endpoint, params=params)
    await queue.enqueue(job)

    return {"job_id": job.id, "type": job.type, "status": job.status, "endpoint": job.endpoint, "params": job.params}

@app.get("/status/{job_id}")
async def get_status(job_id: str):
    job = await queue.get_job(job_id)
    if not job:
        raise HTTPException(404, "Job not found")
    return job