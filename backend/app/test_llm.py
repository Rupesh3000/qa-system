from app.services.qa_service import analyze_transcript

transcript = """
Agent: Hello, thank you for calling support. How can I help you?
Customer: My internet is not working
Agent: I understand your issue, I will help you fix it.
Agent: Please restart your router.
Agent: Thank you for calling, have a great day.
"""

result = analyze_transcript(transcript)

print(result)

{
    "greeting": 9,
    "empathy": 8,
    "tone": 9,
    "apology": 0,
    "closing": 8,
    "summary": "The agent provided a good greeting, showed empathy, and maintained a polite tone. However, there was no apology given, and the closing could be improved by thanking the customer again.",
}
