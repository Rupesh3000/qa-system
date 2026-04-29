import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

# ---- Config ----
PERSIST_DIR = "/home/Mr.nobody_3000/Desktop/Code/AI/Mark_1/backend/Vector"
TOP_K = 3


# ---- Load embedding model ----
def get_embedding_model():
    api_key = os.getenv("GEMINI_EMBEDDING_API_KEY")

    if not api_key:
        raise ValueError("Missing GEMINI_EMBEDDING_API_KEY")

    return GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001", google_api_key=api_key
    )


# ---- Singleton vector DB ----
_vector_db = None


def get_vector_db():
    global _vector_db

    if _vector_db is None:
        embedding_model = get_embedding_model()

        _vector_db = Chroma(
            persist_directory=PERSIST_DIR, embedding_function=embedding_model
        )

    return _vector_db


# ---- MMR Retrieval ----
def retrieve_relevant_docs(query: str, k: int = TOP_K) -> list[str]:
    """
    Uses MMR (Max Marginal Relevance) for diverse + relevant results
    """

    if not query or not query.strip():
        return []

    try:
        db = get_vector_db()

        retriever = db.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": k,
                "fetch_k": 10,  # fetch more candidates
                "lambda_mult": 0.5,  # balance relevance vs diversity
            },
        )

        results = retriever.invoke(query)

        docs = [doc.page_content for doc in results if doc.page_content]

        return docs

    except Exception as e:
        print(f"[RAG ERROR]: {str(e)}")
        return []


# ---- Helper for LLM ----
def get_context_for_llm(query: str, k: int = TOP_K) -> str:
    docs = retrieve_relevant_docs(query, k=k)

    if not docs:
        return ""

    return "\n\n".join(docs)
