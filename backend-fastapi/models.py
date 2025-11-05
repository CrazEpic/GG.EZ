from pydantic import BaseModel, Field
from typing import Union
from enum import Enum
import time
import uuid

class JobType(str, Enum):
    FETCH_ACCOUNT_DATA = "fetch_account_data"
    FETCH_PLAYER_RANK = "fetch_player_rank"
    FETCH_MATCHES = "fetch_matches"
    FETCH_MATCH_DATA = "fetch_match_data"
    FETCH_TIMELINE = "fetch_timeline"

class JobStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    RETRYING = "retrying"

class Job(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: JobType
    status: JobStatus = JobStatus.PENDING
    retries: int = 0
    last_error: str = ""
    created_at: float = Field(default_factory=time.time)
    updated_at: float = Field(default_factory=time.time)
    endpoint: str
    params: dict = {}
    response_data: Union[dict, list, None] = None