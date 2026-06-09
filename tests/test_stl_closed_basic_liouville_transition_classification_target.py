from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/status/STL_CLOSED_BASIC_LIOUVILLE_TRANSITION_CLASSIFICATION_TARGET_2026_06_09.md"
ARTIFACT = ROOT / "artifacts/status/stl_closed_basic_liouville_transition_classification_target_2026_06_09.json"
VERIFIER = ROOT / "verifier/verify_stl_closed_basic_liouville_transition_classification_target.py"


def test_stl_transition_classification_verifier_passes() -> None:
    result = subprocess.run(
        ["python3", str(VERIFIER)],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    assert "STL_CLOSED_BASIC_LIOUVILLE_TRANSITION_CLASSIFICATION_TARGET_OK" in result.stdout


def test_stl_transition_classification_artifact_records_boundary() -> None:
    data = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    assert data["closed_object"] == "STL_CLOSED_BASIC_LIOUVILLE_TRANSITION_CLASSIFICATION_TARGET"
    assert data["stl_completion_after"] == "84-88%"
    assert data["next_admissible_object"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_TARGET"
    assert "no solution-of-gravity claim" in data["boundary"]


def test_stl_transition_classification_doc_records_theorem() -> None:
    text = DOC.read_text(encoding="utf-8")
    assert "STL Closed-Basic Liouville Transition Classification Target" in text
    assert "base-projectable closed-basic Liouville transition" in text
    assert "closed affine cotangent-lift transition" in text
    assert "does not classify arbitrary smooth maps" in text
