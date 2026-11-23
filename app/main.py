
from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="An AI-powered professional portfolio assistant.",
    version=settings.app_version,
)


@app.get("/")
async def root():
    return {
        "message": f"{settings.app_name} API is running!",
        "status": "healthy",
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "vivek-ai-portfolio-twin",
    }
