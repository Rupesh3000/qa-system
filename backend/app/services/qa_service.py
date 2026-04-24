import groq
import os

from dotenv import load_dotenv

load_dotenv()

client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))


def transcribe_audio(file_path: str) -> dict:
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=audio_file,
            response_format="verbose_json",
            prompt="This is a call center conversation between a customer and a customer care agent.",
        )
        return transcription
