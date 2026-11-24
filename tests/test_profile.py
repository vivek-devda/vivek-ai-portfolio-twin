from app.services.private_context import load_private_context
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_private_context_loads_successfully():
    context = load_private_context()

    assert context.career_preferences is not None
    assert context.learning_profile is not None
    assert len(context.career_preferences.preferred_roles) > 0

def test_get_public_profile():
    response = client.get("/api/v1/profile")

    assert response.status_code == 200

    data = response.json()

    assert "identity" in data
    assert "education" in data
    assert "skills" in data
    assert "projects" in data
    assert "achievements" in data
    assert "languages" in data


def test_public_profile_does_not_expose_private_context():
    response = client.get("/api/v1/profile")

    assert response.status_code == 200

    data = response.json()

    private_fields = [
        "career_preferences",
        "learning_profile",
        "application_tracking",
        "compensation_preferences",
        "internal_notes",
    ]

    for field in private_fields:
        assert field not in data
