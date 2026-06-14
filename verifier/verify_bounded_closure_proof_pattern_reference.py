from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ARTIFACT = ROOT / "artifacts" / "status" / "bounded_closure_proof_pattern_reference_2026_06_13.json"
DOC = ROOT / "docs" / "status" / "BOUNDED_CLOSURE_PROOF_PATTERN_REFERENCE_2026_06_13.md"

REQUIRED_STATUS_CLASSES = {
    "PROVED",
    "CONDITIONAL",
    "INPUT_SURFACE",
    "OPEN",
}

REQUIRED_PATTERN_COMPONENTS = {
    "large_claim",
    "input_surface",
    "bounded_theorem_object",
    "verifier_or_certificate",
    "status_classification",
    "explicit_boundary",
}

REQUIRED_NON_CLAIMS = {
    "NO_NEW_THEOREM_PROOF",
    "NO_THEOREM_PROMOTION",
    "NO_GLOBAL_CLOSURE",
    "NO_EXTERNAL_ACCEPTANCE",
    "NO_CLAY_CLAIM",
}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def verify() -> None:
    artifact = read_json(ARTIFACT)
    doc = DOC.read_text(encoding="utf-8")

    assert artifact["id"] == "BOUNDED_CLOSURE_PROOF_PATTERN_REFERENCE_2026_06_13"
    assert artifact["repository"] == "theorem-closure-classifier"
    assert artifact["status"] == "BOUNDED_CLOSURE_PROOF_PATTERN_REFERENCE_ADDED"
    assert artifact["closed_object"] == "BoundedClosureProofPatternReference"
    assert artifact["object_type"] == "classification_pattern_reference"
    assert artifact["source_repository"] == "urf-textbook"
    assert artifact["source_commit"] == "8def1fc"
    assert artifact["source_section"] == "Proof Pattern: Bounded Closure by Classified Formal Artifacts"
    assert set(artifact["status_classes"]) == REQUIRED_STATUS_CLASSES
    assert set(artifact["required_pattern_components"]) == REQUIRED_PATTERN_COMPONENTS
    assert set(artifact["non_claims"]) == REQUIRED_NON_CLAIMS
    assert artifact["next_admissible_object"] == "StopOrAddPatternAdoptionVerifier"

    assert "does not assert any new theorem proof" in doc
    assert "does not promote any classifier label into a proof" in doc
    assert "does not close any global theorem" in doc
    assert "does not assert external acceptance" in doc
    assert "does not assert any Clay-level claim" in doc


if __name__ == "__main__":
    verify()
    print("BOUNDED_CLOSURE_PROOF_PATTERN_REFERENCE_OK")
