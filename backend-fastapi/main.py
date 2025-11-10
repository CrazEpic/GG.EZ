from fastapi import FastAPI
from pydantic import BaseModel
from aws_queue_manager import AWSQueueManager

class EnqueueRequest(BaseModel):
    region: str
    gameName: str
    tagLine: str

app = FastAPI()
queue = AWSQueueManager()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# attempt to enqueue player here using the region, game name, and tag line
@app.post("/enqueue")
async def enqueue(request: EnqueueRequest):
    input = {
        "region": request.region,
        "gameName": request.gameName,
        "tagLine": request.tagLine
    }
    return queue.enqueue(input)