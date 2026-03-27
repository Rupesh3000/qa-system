from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class CallScoreInput(BaseModel):
    agent_name: str
    greeting: int = Field(ge=0, le=10)
    empathy: int = Field(ge=0, le=10)
    tone: int = Field(ge=0, le=10)
    apology: int = Field(ge=0, le=10)
    closing: int = Field(ge=0, le=10)


class CallScoreResponse(BaseModel):
    agent_name: str
    total_score: float
    result: str
    created_at: datetime
