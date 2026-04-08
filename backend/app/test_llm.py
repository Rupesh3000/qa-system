# from app.services.qa_service import analyze_transcript, calculate_qa_score
# from app.models.qa_model import CallScoreResponse
# from datetime import datetime


# transcript = """
# Agent: Hello, thank you for calling support. How can I help you?
# Customer: My internet is not working
# Agent: I understand your issue, I will help you fix it.
# Agent: Please restart your router.
# Agent: Thank you for calling, have a great day.
# """

# scores = analyze_transcript(transcript)
# score_result = calculate_qa_score(scores)


# def printResul():
#     return CallScoreResponse(
#         agent_name="Auto-Detected",
#         transcript=transcript,
#         scores={
#             "greeting": scores.get("greeting", 0),
#             "empathy": scores.get("empathy", 0),
#             "tone": scores.get("tone", 0),
#             "apology": scores.get("apology", 0),
#             "closing": scores.get("closing", 0),
#         },
#         total_score=score_result["total_score"],
#         result=score_result["result"],
#         summary=scores.get("summary", ""),
#         created_at=datetime.utcnow(),
#     )


data = "agent_name='Auto-Detected' transcript='\nAgent: Hello, thank you for calling support. How can I help you?\nCustomer: My internet is not working\nAgent: I understand your issue, I will help you fix it.\nAgent: Please restart your router.\nAgent: Thank you for calling, have a great day.\n' scores={'greeting': 9, 'empathy': 8, 'tone': 9, 'apology': 0, 'closing': 8} total_score=68.0 result='Good' summary='The agent provided a good greeting, showed empathy, and maintained a polite tone. However, there was no apology given, and the closing could be improved by thanking the customer again.' created_at=datetime.datetime(2026, 4, 8, 16, 50, 11, 169071)" 
print(data)