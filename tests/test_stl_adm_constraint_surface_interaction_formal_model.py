from __future__ import annotations

import json
from pathlib import Path

from verifier.verify_stl_adm_constraint_surface_interaction_formal_model import verify

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts/status/stl_adm_constraint_surface_interaction_formal_model_2026_06_09.json"
DOC = ROOT / "docs/status/STL_ADM_CONSTRAINT_SURFACE_INTERACTION_FORMAL_MODEL_2026_06_09.md"

def test_stl_adm_constraint_surface_interaction_formal_model_verifies() -> None:
    verify()

def test_status_is_formal_model_only() -> None:
    data = json.loads(ARTIFACT.read_text())
    assert data["status"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_FORMAL_MODEL_ONLY"
    assert data["minimal_missing_object"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_SOUNDNESS_LEMMA"

def test_boundary_preserves_no_gravity_claims() -> None:
    data = json.loads(ARTIFACT.read_text())
    boundary = set(data["boundary"])
    assert "FORMAL_MODEL_ONLY" in boundary
    assert "NO_QUANTUM_GRAVITY_CLAIM" in boundary
    assert "NO_EINSTEIN_EQUATION_CLAIM" in boundary
    assert "NO_SOLUTION_OF_GRAVITY_CLAIM" in boundary

def test_no_completion_percentage_fields() -> None:
    data = json.loads(ARTIFACT.read_text())
    assert "stl_completion_before" not in data
    assert "stl_completion_after" not in data
    assert "%" not in ARTIFACT.read_text()
    assert "%" not in DOC.read_text()
