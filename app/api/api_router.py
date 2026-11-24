
from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.profile import router as profile_router

router = APIRouter()

# Version 1 API
api_v1_router = APIRouter(prefix="/api/v1")

api_v1_router.include_router(health_router)
api_v1_router.include_router(profile_router)

# Register versioned endpoints
router.include_router(api_v1_router)


@router.get("/")
async def root():
    return {
        "message": "Vivek AI Portfolio Twin API is running!",
        "status": "healthy",
    }
