from __future__ import annotations

import json
from pathlib import Path

from verifier.verify_stl_adm_constraint_surface_interaction_target import verify

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts/status/stl_adm_constraint_surface_interaction_target_2026_06_09.json"

def test_stl_adm_constraint_surface_interaction_target_verifies() -> None:
    verify()

def test_status_is_target_only() -> None:
    data = json.loads(ARTIFACT.read_text())
    assert data["status"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_TARGET_ONLY"
    assert data["minimal_missing_object"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_LEMMA"

def test_boundary_preserves_no_gravity_claims() -> None:
    data = json.loads(ARTIFACT.read_text())
    boundary = set(data["boundary"])
    assert "NO_QUANTUM_GRAVITY_CLAIM" in boundary
    assert "NO_EINSTEIN_EQUATION_CLAIM" in boundary
    assert "NO_SOLUTION_OF_GRAVITY_CLAIM" in boundary
