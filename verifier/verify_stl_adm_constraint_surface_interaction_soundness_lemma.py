from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts/status/stl_adm_constraint_surface_interaction_soundness_lemma_2026_06_09.json"
DOC = ROOT / "docs/status/STL_ADM_CONSTRAINT_SURFACE_INTERACTION_SOUNDNESS_LEMMA_2026_06_09.md"

EXPECTED_DEPENDENCIES = {
    "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_TARGET_2026_06_09",
    "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_LEMMA_2026_06_09",
    "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_FORMAL_MODEL_2026_06_09",
}

EXPECTED_SCOPE = {
    "FORMAL_MODEL_RELATIVE",
    "SYMBOLIC_CLASSIFICATION_ONLY",
    "BOUNDARY_LOCK_PRESERVING",
}

EXPECTED_BOUNDARY = {
    "FORMAL_SOUNDNESS_ONLY",
    "MODEL_RELATIVE_ONLY",
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
    "stl_completion_before",
    "stl_completion_after",
    "completion_before",
    "completion_after",
}

def verify() -> None:
    data = json.loads(ARTIFACT.read_text())
    doc = DOC.read_text()

    assert data["object"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_SOUNDNESS_LEMMA_2026_06_09"
    assert data["status"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_SOUNDNESS_LEMMA_FORMAL_ONLY"
    assert data["closed_object"] == data["object"]
    assert set(data["depends_on"]) == EXPECTED_DEPENDENCIES
    assert set(data["soundness_scope"]) == EXPECTED_SCOPE
    assert data["minimal_missing_object"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_COMPLETION_LOCK"
    assert set(data["boundary"]) == EXPECTED_BOUNDARY
    assert data["next_admissible_object"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_COMPLETION_LOCK"
    assert not (FORBIDDEN_KEYS & set(data))
    assert "%" not in ARTIFACT.read_text()
    assert "%" not in doc

    for token in [
        data["object"],
        data["status"],
        data["minimal_missing_object"],
        data["next_admissible_object"],
        *EXPECTED_DEPENDENCIES,
        *EXPECTED_SCOPE,
        *EXPECTED_BOUNDARY,
    ]:
        assert str(token) in doc

if __name__ == "__main__":
    verify()
    print("STL_ADM_CONSTRAINT_SURFACE_INTERACTION_SOUNDNESS_LEMMA_OK")
