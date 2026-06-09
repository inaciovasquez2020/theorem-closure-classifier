from __future__ import annotations

import json
from pathlib import Path

from verifier.verify_stl_adm_constraint_surface_interaction_completion_lock import verify

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts/status/stl_adm_constraint_surface_interaction_completion_lock_2026_06_09.json"
DOC = ROOT / "docs/status/STL_ADM_CONSTRAINT_SURFACE_INTERACTION_COMPLETION_LOCK_2026_06_09.md"

def test_stl_adm_completion_lock_verifies() -> None:
    verify()

def test_status_is_completion_lock_only() -> None:
    data = json.loads(ARTIFACT.read_text())
    assert data["status"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_COMPLETION_LOCK_ONLY"
    assert data["minimal_missing_object"] == "STOP_OR_EXTERNAL_REFERENCE_SYNC"

def test_boundary_preserves_formal_only_status() -> None:
    data = json.loads(ARTIFACT.read_text())
    boundary = set(data["boundary"])
    assert "COMPLETION_LOCK_ONLY" in boundary
    assert "FORMAL_STATUS_SEQUENCE_ONLY" in boundary
    assert "MODEL_RELATIVE_ONLY" in boundary
    assert "NO_PHYSICAL_SOUNDNESS_CLAIM" in boundary
    assert "NO_SOLUTION_OF_GRAVITY_CLAIM" in boundary

def test_locked_chain_contains_required_objects() -> None:
    data = json.loads(ARTIFACT.read_text())
    locked_chain = set(data["locked_chain"])
    assert locked_chain == {
        "TARGET",
        "CONDITIONAL_LEMMA",
        "FORMAL_MODEL",
        "FORMAL_SOUNDNESS_LEMMA",
    }

def test_no_completion_percentage_fields() -> None:
    data = json.loads(ARTIFACT.read_text())
    assert "stl_completion_before" not in data
    assert "stl_completion_after" not in data
    assert "%" not in ARTIFACT.read_text()
    assert "%" not in DOC.read_text()
