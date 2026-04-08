import groq
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))


def transcribe_audio(file_path: str) -> str:
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-large-v3", file=audio_file, response_format="text"
        )
    return transcription


def analyze_transcript(transcript: str) -> dict:
    prompt = f"""
You are a call center QA expert.

Analyze the transcript and score each parameter from 0 to 10.

For EACH parameter return:
- score (0-10)
- reason (short explanation)

Transcript:
{transcript}

Return ONLY JSON:

{{
  "greeting": {{ "score": <int>, "reason": "<text>" }},
  "empathy": {{ "score": <int>, "reason": "<text>" }},
  "tone": {{ "score": <int>, "reason": "<text>" }},
  "apology": {{ "score": <int>, "reason": "<text>" }},
  "closing": {{ "score": <int>, "reason": "<text>" }}
}}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    content = response.choices[0].message.content.strip()

    content = content.replace(",}", "}")

    try:
        result = json.loads(content)
    except:
        result = {
            "greeting": 0,
            "empathy": 0,
            "tone": 0,
            "apology": 0,
            "closing": 0,
            "summary": "Parsing failed",
        }

    return result


def calculate_qa_score(scores: dict) -> dict:
    total = (
        scores["greeting"]["score"]
        + scores["empathy"]["score"]
        + scores["tone"]["score"]
        + scores["apology"]["score"]
        + scores["closing"]["score"]
    )

    percentage = (total / 50) * 100

    if percentage >= 80:
        result = "Excellent"
    elif percentage >= 60:
        result = "Good"
    elif percentage >= 40:
        result = "Needs Improvement"
    else:
        result = "Failed"

    return {"total_score": percentage, "result": result}
