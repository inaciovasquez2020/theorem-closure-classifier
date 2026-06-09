from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts/status/stl_adm_constraint_surface_interaction_lemma_2026_06_09.json"
DOC = ROOT / "docs/status/STL_ADM_CONSTRAINT_SURFACE_INTERACTION_LEMMA_2026_06_09.md"

EXPECTED_BOUNDARY = {
    "CONDITIONAL_ONLY",
    "NO_QUANTUM_GRAVITY_CLAIM",
    "NO_CANONICAL_QUANTIZATION_CLAIM",
    "NO_EINSTEIN_EQUATION_CLAIM",
    "NO_EMPIRICAL_GRAVITY_CLAIM",
    "NO_COSMOLOGY_CLAIM",
    "NO_UNIFICATION_CLAIM",
    "NO_PHYSICAL_THEORY_CLAIM",
    "NO_SOLUTION_OF_GRAVITY_CLAIM",
}

EXPECTED_DEPENDENCIES = {
    "STL_SUBMODULE_COMPLETENESS_STATUS_2026_06_09",
    "STL_CHAIN_COHERENCE_LEMMA_2026_06_09",
    "STL_CLOSED_BASIC_LIOUVILLE_TRANSITION_CLASSIFICATION_TARGET_2026_06_09",
    "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_TARGET_2026_06_09",
}

def load_artifact() -> dict:
    return json.loads(ARTIFACT.read_text())

def verify() -> None:
    data = load_artifact()
    doc = DOC.read_text()

    assert data["object"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_LEMMA_2026_06_09"
    assert data["status"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_LEMMA_CONDITIONAL_ONLY"
    assert data["closed_object"] == data["object"]
    assert set(data["depends_on"]) == EXPECTED_DEPENDENCIES
    assert data["minimal_missing_object"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_FORMAL_MODEL"
    assert set(data["boundary"]) == EXPECTED_BOUNDARY
    assert data["next_admissible_object"] == "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_FORMAL_MODEL"

    for token in [
        data["object"],
        data["status"],
        data["minimal_missing_object"],
        data["next_admissible_object"],
        *EXPECTED_BOUNDARY,
    ]:
        assert token in doc

if __name__ == "__main__":
    verify()
    print("STL_ADM_CONSTRAINT_SURFACE_INTERACTION_LEMMA_OK")
