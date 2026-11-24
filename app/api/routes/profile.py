
import json
from pathlib import Path

from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from app.schemas.profile import ProfessionalProfile

router = APIRouter()

PROFILE_FILE = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "public_profile.json"
)


@router.get("/profile", response_model=ProfessionalProfile)
async def get_profile():
    try:
        profile_data = json.loads(
            PROFILE_FILE.read_text(encoding="utf-8")
        )

        return ProfessionalProfile.model_validate(profile_data)

    except FileNotFoundError:
        raise HTTPException(
            status_code=500,
            detail="Public profile data file not found."
        )

    except (json.JSONDecodeError, ValidationError, OSError):
        raise HTTPException(
            status_code=500,
            detail="Unable to load or validate public profile data."
        )
