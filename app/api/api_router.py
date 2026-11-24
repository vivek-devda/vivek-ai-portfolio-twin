from fastapi import APIRouter

from app.api.routes.health import router as health_router

router = APIRouter()

router.include_router(health_router)


@router.get("/")
async def root():
    return {
        "message": "Vivek AI Portfolio Twin API is running!",
        "status": "healthy",
    }