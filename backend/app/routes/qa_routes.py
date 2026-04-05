import os
import shutil
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException
from datetime import datetime

from app.services.qa_service import (
    transcribe_audio,
    analyze_transcript,
    calculate_qa_score,
)
from app.models.qa_model import CallScoreResponse

router = APIRouter()


@router.post("/audit-call", response_model=CallScoreResponse)
async def audit_call(file: UploadFile = File(...)):
    allowed_types = ["audio/mpeg", "audio/wav", "audio/mp4", "audio/m4a"]

    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Invalid file type")

    file_path = f"temp_{uuid.uuid4()}.wav"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        transcript = transcribe_audio(file_path)
        scores = analyze_transcript(transcript)

        score_result = calculate_qa_score(scores)

        return CallScoreResponse(
            agent_name="Auto-Detected",
            transcript=transcript,
            scores={
                "greeting": scores.get("greeting", 0),
                "empathy": scores.get("empathy", 0),
                "tone": scores.get("tone", 0),
                "apology": scores.get("apology", 0),
                "closing": scores.get("closing", 0),
            },
            total_score=score_result["total_score"],
            result=score_result["result"],
            summary=scores.get("summary", ""),
            created_at=datetime.utcnow(),
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Audit failed: {str(e)}")

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
