
from fastapi import FastAPI

app = FastAPI(
    title="Vivek AI Portfolio Twin",
    description="An AI-powered professional portfolio assistant.",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "message": "Vivek AI Portfolio Twin API is running!",
        "status": "healthy",
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "vivek-ai-portfolio-twin",
    }
