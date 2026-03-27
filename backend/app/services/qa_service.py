from datetime import datetime
from app.models.qa_model import CallScoreInput, CallScoreResponse

def calculate_qa_score(data: CallScoreInput) -> CallScoreResponse:
    total = (
        data.greeting +
        data.empathy +
        data.tone +
        data.apology +
        data.closing
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

    return CallScoreResponse(
        agent_name=data.agent_name,
        total_score=percentage,
        result=result,
        created_at=datetime.utcnow()
    )