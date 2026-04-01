from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
from app.models.qa_model import CallScoreInput, CallScoreResponse
from app.services.qa_service import calculate_qa_score, transcribe_audio

router = APIRouter()


@router.post("/score", response_model=CallScoreResponse)
async def score_call(data: CallScoreInput):
    result = calculate_qa_score(data)
    return result


@router.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    allowed_types = ["audio/mpeg", "audio/wav", "audio/mp4", "audio/m4a"]

    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Invalid file type")

    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        transcript = transcribe_audio(file_path)
        return {"transcript": transcript}
    finally:
        os.remove(file_path)
