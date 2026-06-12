from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts/status/external_reference_sync_2026_06_11.json"
DOC = ROOT / "docs/status/EXTERNAL_REFERENCE_SYNC_2026_06_11.md"
SOURCE_ARTIFACT = ROOT / "artifacts/status/stl_adm_constraint_surface_interaction_completion_lock_2026_06_09.json"

EXPECTED_BOUNDARY = {
    "REFERENCE_SYNC_ONLY",
    "REFERENCE_ONLY",
    "STATUS_ARTIFACT_ONLY",
    "NO_NEW_THEOREM_CLAIM",
    "NO_PHYSICAL_SOUNDNESS_CLAIM",
    "NO_QUANTUM_GRAVITY_CLAIM",
    "NO_CANONICAL_QUANTIZATION_CLAIM",
    "NO_EINSTEIN_EQUATION_CLAIM",
    "NO_EMPIRICAL_GRAVITY_CLAIM",
    "NO_COSMOLOGY_CLAIM",
    "NO_UNIFICATION_CLAIM",
    "NO_PHYSICAL_THEORY_CLAIM",
    "NO_SOLUTION_OF_GRAVITY_CLAIM",
}

FORBIDDEN_KEYS = {
    "proof",
    "theorem",
    "physical_soundness",
    "quantum_gravity_solution",
    "einstein_equation_solution",
    "cosmology_solution",
    "unification_solution",
}


def verify() -> None:
    data = json.loads(ARTIFACT.read_text())
    source = json.loads(SOURCE_ARTIFACT.read_text())
    doc = DOC.read_text()

    assert data["object"] == "EXTERNAL_REFERENCE_SYNC_2026_06_11"
    assert data["status"] == "EXTERNAL_REFERENCE_SYNC_REFERENCE_ONLY"
    assert data["closed_object"] == data["object"]
    assert data["source_repository"] == "inaciovasquez2020/theorem-closure-classifier"
    assert data["source_object"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_COMPLETION_LOCK_2026_06_09"
    assert data["depends_on"] == ["STL_ADM_CONSTRAINT_SURFACE_INTERACTION_COMPLETION_LOCK_2026_06_09"]
    assert source["object"] == data["source_object"]
    assert source["minimal_missing_object"] == "STOP_OR_EXTERNAL_REFERENCE_SYNC"
    assert data["resolved_missing_object"] == "EXTERNAL_REFERENCE_SYNC"
    assert data["minimal_missing_object"] == "STOP"
    assert data["next_admissible_object"] == "STOP"
    assert set(data["boundary"]) == EXPECTED_BOUNDARY
    assert not (FORBIDDEN_KEYS & set(data))
    assert "%" not in ARTIFACT.read_text()
    assert "%" not in doc

    for token in [
        data["object"],
        data["status"],
        data["source_repository"],
        data["source_object"],
        data["resolved_missing_object"],
        data["minimal_missing_object"],
        data["next_admissible_object"],
        *EXPECTED_BOUNDARY,
    ]:
        assert str(token) in doc


if __name__ == "__main__":
    verify()
    print("EXTERNAL_REFERENCE_SYNC_OK")
