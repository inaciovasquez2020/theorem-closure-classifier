import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / "verifier" / "verify_poset_classification_registry_consistency.py"
REGISTRY = ROOT / "artifacts/external_validation/poset_classification_registry_consistency_2026_06_23.json"


@pytest.fixture(autouse=True)
def registry_file_is_restored() -> None:
    before = REGISTRY.read_text(encoding="utf-8")
    try:
        yield
    finally:
        after = REGISTRY.read_text(encoding="utf-8")
        assert after == before


def registry_entries(data: dict[str, Any]) -> list[dict[str, Any]]:
    for value in data.values():
        if (
            isinstance(value, list)
            and value
            and all(isinstance(entry, dict) for entry in value)
            and all("artifact_id" in entry for entry in value)
            and all("classification_level" in entry for entry in value)
        ):
            return value
    raise AssertionError("MISSING_OBJECT := registry entry list")


def run_verifier() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VERIFIER)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def test_registry_consistency_rejects_duplicate_artifact_ids() -> None:
    original = REGISTRY.read_text(encoding="utf-8")
    try:
        data = json.loads(original)
        entries = registry_entries(data)
        entries.append(dict(entries[0]))
        REGISTRY.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

        result = run_verifier()

        assert result.returncode != 0
        assert "BOUNDARY := duplicate_registry_entry" in result.stderr
    finally:
        REGISTRY.write_text(original, encoding="utf-8")


def test_registry_consistency_rejects_invalid_poset_levels() -> None:
    original = REGISTRY.read_text(encoding="utf-8")
    try:
        data = json.loads(original)
        entries = registry_entries(data)
        entries[0]["classification_level"] = "not_a_poset_level"
        REGISTRY.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

        result = run_verifier()

        assert result.returncode != 0
        assert "BOUNDARY := classification_level_not_in_poset" in result.stderr
    finally:
        REGISTRY.write_text(original, encoding="utf-8")


def test_registry_consistency_still_accepts_current_registry() -> None:
    result = run_verifier()

    assert result.returncode == 0
    assert "POSET_CLASSIFICATION_REGISTRY_CONSISTENCY_OK" in result.stdout
