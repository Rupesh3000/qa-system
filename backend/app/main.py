from fastapi import FastAPI
from app.routes.qa_routes import router

app = FastAPI(title="QA System API")

app.include_router(router, prefix="/api/qa", tags=["QA Scoring"])


@app.get("/")
async def root():
    return {"message": "QA System API is running"}
