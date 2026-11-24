
from pydantic import BaseModel, Field


class WorkPreferences(BaseModel):
    remote_preferred: bool = True
    open_to_relocation: bool = False
    freelance_interest: bool = False


class CareerPreferences(BaseModel):
    preferred_roles: list[str] = Field(default_factory=list)
    work_preferences: WorkPreferences = Field(
        default_factory=WorkPreferences
    )


class LearningProfile(BaseModel):
    current_focus: list[str] = Field(default_factory=list)
    learning_approach: str | None = None
    skill_confidence: list[str] = Field(default_factory=list)
    learning_progress: list[str] = Field(default_factory=list)


class ApplicationTracking(BaseModel):
    active_applications: list[str] = Field(default_factory=list)
    interview_status: list[str] = Field(default_factory=list)
    follow_ups: list[str] = Field(default_factory=list)


class CompensationPreferences(BaseModel):
    expected_compensation: str | None = None
    negotiation_notes: list[str] = Field(default_factory=list)


class PrivateContext(BaseModel):
    career_preferences: CareerPreferences
    learning_profile: LearningProfile
    application_tracking: ApplicationTracking
    compensation_preferences: CompensationPreferences
    internal_notes: list[str] = Field(default_factory=list)
