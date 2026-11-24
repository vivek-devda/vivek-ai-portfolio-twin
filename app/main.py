from fastapi import FastAPI

from app.api.routes import router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="An AI-powered professional portfolio assistant.",
    version=settings.app_version,
)

app.include_router(router)