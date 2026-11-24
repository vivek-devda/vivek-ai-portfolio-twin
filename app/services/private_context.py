
import json
from pathlib import Path

from app.schemas.private_context import PrivateContext


PRIVATE_CONTEXT_FILE = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "private_context.json"
)


def load_private_context() -> PrivateContext:
    """Load and validate private career context."""

    data = json.loads(
        PRIVATE_CONTEXT_FILE.read_text(encoding="utf-8")
    )

    return PrivateContext.model_validate(data)
