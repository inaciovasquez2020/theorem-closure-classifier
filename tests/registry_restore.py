from collections.abc import Generator
from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def registry_file_is_restored() -> Generator[None, None, None]:
    registry = Path(__file__).resolve().parents[1] / "artifacts/external_validation/poset_classification_registry_consistency_2026_06_23.json"
    before = registry.read_text(encoding="utf-8")
    try:
        yield
    finally:
        after = registry.read_text(encoding="utf-8")
        assert after == before
