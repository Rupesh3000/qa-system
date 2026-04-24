import os
import shutil
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.qa_service import transcribe_audio

router = APIRouter()

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB


@router.post("/audit-call")
async def audit_call(file: UploadFile = File(...)):
    allowed_types = ["audio/mpeg", "audio/wav", "audio/mp4", "audio/m4a"]

    # 1. Validate file type
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Invalid file type")

    # 2. Read file content (for size + empty check)
    content = await file.read()

    if not content:
        raise HTTPException(status_code=400, detail="Empty file uploaded")

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large (max 10MB)")

    ext = os.path.splitext(file.filename)[1]
    file_path = f"temp_{uuid.uuid4()}{ext}"

    try:
        # 3. Save file safely
        with open(file_path, "wb") as buffer:
            buffer.write(content)

        # 4. Call transcription
        transcript = transcribe_audio(file_path)

        # # 5. Validate transcript
        # if not transcript or not transcript.get("text"):
        #     raise HTTPException(status_code=500, detail="Transcription failed or empty")

        return {"status": "success", "transcript": transcript}

    except HTTPException:
        raise  # re-raise known errors

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")

    finally:
        # 6. Cleanup
        if os.path.exists(file_path):
            os.remove(file_path)
