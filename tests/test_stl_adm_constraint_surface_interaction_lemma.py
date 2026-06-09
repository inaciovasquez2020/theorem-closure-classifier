from __future__ import annotations

import json
from pathlib import Path

from verifier.verify_stl_adm_constraint_surface_interaction_lemma import verify

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts/status/stl_adm_constraint_surface_interaction_lemma_2026_06_09.json"

def test_stl_adm_constraint_surface_interaction_lemma_verifies() -> None:
    verify()

def test_status_is_conditional_only() -> None:
    data = json.loads(ARTIFACT.read_text())
    assert data["status"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_LEMMA_CONDITIONAL_ONLY"
    assert data["minimal_missing_object"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_FORMAL_MODEL"

def test_boundary_preserves_no_gravity_claims() -> None:
    data = json.loads(ARTIFACT.read_text())
    boundary = set(data["boundary"])
    assert "CONDITIONAL_ONLY" in boundary
    assert "NO_QUANTUM_GRAVITY_CLAIM" in boundary
    assert "NO_EINSTEIN_EQUATION_CLAIM" in boundary
    assert "NO_SOLUTION_OF_GRAVITY_CLAIM" in boundary
