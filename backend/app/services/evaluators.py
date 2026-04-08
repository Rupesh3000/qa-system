import json
import os
from dotenv import load_dotenv
import groq

load_dotenv()

client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))


def evaluate_greeting(transcript: str) -> dict:
    prompt = f"""
    You are a call center QA expert.

    Evaluate ONLY the GREETING of the agent.

    Rules:
    - Did the agent greet the customer properly?
    - Was it polite and professional?
    - Did it include a proper opening?

    Transcript:
    {transcript}

    Return ONLY JSON:
    {{
        "score": <0-10>,
        "reason": "<short explanation>"
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
        return json.loads(content)
    except:
        return {"score": 0, "reason": "Parsing failed"}
