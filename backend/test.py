# Change this:
# from backend.app.services.rag_service import get_context_for_llm

# To this:
from app.services.rag_service import get_context_for_llm

print(
    get_context_for_llm(
        "What is the primary aim or summary of this unit?", 3
    )
)

