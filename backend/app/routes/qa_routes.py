from fastapi import APIRouter
from app.models.qa_model import CallScoreInput, CallScoreResponse
from app.services.qa_service import calculate_qa_score

router = APIRouter()


@router.post("/score", response_model=CallScoreResponse)
async def score_call(data: CallScoreInput):
    result = calculate_qa_score(data)
    return result
