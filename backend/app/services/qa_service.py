import groq
import os
from dotenv import load_dotenv
from datetime import datetime

from app.models.qa_model import CallScoreInput, CallScoreResponse

load_dotenv()

client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))


def transcribe_audio(file_path: str) -> str:
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-large-v3", file=audio_file, response_format="text"
        )
    return transcription


def calculate_qa_score(data: CallScoreInput) -> CallScoreResponse:
    total = data.greeting + data.empathy + data.tone + data.apology + data.closing

    percentage = (total / 50) * 100

    if percentage >= 80:
        result = "Excellent"
    elif percentage >= 60:
        result = "Good"
    elif percentage >= 40:
        result = "Needs Improvement"
    else:
        result = "Failed"

    return CallScoreResponse(
        agent_name=data.agent_name,
        total_score=percentage,
        result=result,
        created_at=datetime.utcnow(),
    )
