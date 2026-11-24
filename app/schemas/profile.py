
from pydantic import BaseModel, Field, HttpUrl


class ProfileIdentity(BaseModel):
    name: str
    headline: str
    location: str
    linkedin_url: HttpUrl
    email: str


class Education(BaseModel):
    degree: str
    specialization: str
    institution: str
    start_year: int
    expected_final_semester_exam: str


class Skill(BaseModel):
    name: str
    category: str
    proficiency_level: str
    evidence: str | None = None


class Project(BaseModel):
    name: str
    description: str
    technologies: list[str] = Field(default_factory=list)
    github_url: HttpUrl | None = None
    demo_url: HttpUrl | None = None


class Achievement(BaseModel):
    title: str
    description: str
    technologies: list[str] = Field(default_factory=list)
    recognition: str | None = None


class ProfessionalProfile(BaseModel):
    identity: ProfileIdentity
    education: list[Education] = Field(default_factory=list)
    skills: list[Skill] = Field(default_factory=list)
    projects: list[Project] = Field(default_factory=list)
    achievements: list[Achievement] = Field(default_factory=list)
    languages: list[str] = Field(default_factory=list)
