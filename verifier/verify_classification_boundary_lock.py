from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts" / "status" / "classification_boundary_lock_2026_06_09.json"
DOC = ROOT / "docs" / "status" / "CLASSIFICATION_BOUNDARY_LOCK_2026_06_09.md"

REQUIRED_NON_CLAIMS = {
    "NO_NEW_THEOREM_PROOF",
    "NO_EXTERNAL_THEOREM_ACCEPTANCE",
    "NO_AUTOMATIC_PROMOTION_FROM_CLASSIFICATION_TO_PROOF",
    "NO_CLAY_CLAIM",
}

REQUIRED_FIELDS = {
    "exact_statement_object",
    "domain_object",
    "hypothesis_object",
    "construction_object",
    "obstruction_object",
    "necessity_direction_object",
    "sufficiency_direction_object",
    "boundary_object",
    "proof_ledger",
    "dependency_ledger",
    "claim_boundary_ledger",
}


def verify() -> None:
    artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    doc = DOC.read_text(encoding="utf-8")

    assert artifact["id"] == "CLASSIFICATION_BOUNDARY_LOCK_2026_06_09"
    assert artifact["repository"] == "theorem-closure-classifier"
    assert artifact["status"] == "BOUNDARY_LOCK_ADDED"
    assert artifact["closed_object"] == "ClassificationBoundaryLock"
    assert set(artifact["non_claims"]) == REQUIRED_NON_CLAIMS
    assert set(artifact["required_fields"]) == REQUIRED_FIELDS
    assert artifact["next_admissible_object"] == "AdditionalIndependentBenchmarkControl"

    assert "does not assert any new theorem proof" in doc
    assert "does not assert external acceptance" in doc
    assert "does not allow classification output alone" in doc
    assert "does not assert any Clay-level claim" in doc


if __name__ == "__main__":
    verify()
    print("CLASSIFICATION_BOUNDARY_LOCK_OK")
