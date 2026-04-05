from pydantic import BaseModel, Field
from datetime import datetime
from typing import Dict


class CallScoreInput(BaseModel):
    agent_name: str
    greeting: int = Field(ge=0, le=10)
    empathy: int = Field(ge=0, le=10)
    tone: int = Field(ge=0, le=10)
    apology: int = Field(ge=0, le=10)
    closing: int = Field(ge=0, le=10)


class CallScoreResponse(BaseModel):
    agent_name: str
    transcript: str
    scores: Dict[str, int]
    total_score: float
    result: str
    summary: str
    created_at: datetime
