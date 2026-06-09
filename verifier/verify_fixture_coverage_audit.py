from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts" / "status" / "fixture_coverage_audit_2026_06_09.json"
DOC = ROOT / "docs" / "status" / "FIXTURE_COVERAGE_AUDIT_2026_06_09.md"
BOUNDARY_LOCK = ROOT / "artifacts" / "status" / "classification_boundary_lock_2026_06_09.json"
BENCHMARK_CONTROL = ROOT / "artifacts" / "status" / "additional_independent_benchmark_control_2026_06_09.json"

REQUIRED_FIXTURE_CATEGORIES = {
    "positive_closed_theorem_fixture",
    "negative_open_frontier_fixture",
    "boundary_only_status_fixture",
    "external_acceptance_absent_fixture",
    "classifier_output_not_proof_fixture",
    "clay_claim_negative_control_fixture",
}

REQUIRED_EXISTING_CONTROLS = {
    "ClassificationBoundaryLock",
    "AdditionalIndependentBenchmarkControl",
}

REQUIRED_NON_CLAIMS = {
    "NO_NEW_THEOREM_PROOF",
    "NO_EXTERNAL_THEOREM_ACCEPTANCE",
    "NO_COVERAGE_COMPLETENESS_CLAIM",
    "NO_CLASSIFIER_OUTPUT_AS_PROOF",
    "NO_AUTOMATIC_THEOREM_PROMOTION",
    "NO_CLAY_CLAIM",
}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def verify() -> None:
    artifact = read_json(ARTIFACT)
    doc = DOC.read_text(encoding="utf-8")

    boundary_lock = read_json(BOUNDARY_LOCK)
    benchmark_control = read_json(BENCHMARK_CONTROL)

    assert boundary_lock["closed_object"] == "ClassificationBoundaryLock"
    assert benchmark_control["closed_object"] == "AdditionalIndependentBenchmarkControl"

    assert artifact["id"] == "FIXTURE_COVERAGE_AUDIT_2026_06_09"
    assert artifact["repository"] == "theorem-closure-classifier"
    assert artifact["status"] == "FIXTURE_COVERAGE_AUDIT_ADDED"
    assert artifact["closed_object"] == "FixtureCoverageAudit"
    assert artifact["object_type"] == "coverage_audit_boundary"
    assert set(artifact["required_fixture_categories"]) == REQUIRED_FIXTURE_CATEGORIES
    assert set(artifact["required_existing_controls"]) == REQUIRED_EXISTING_CONTROLS
    assert set(artifact["non_claims"]) == REQUIRED_NON_CLAIMS
    assert artifact["next_admissible_object"] == "StopOrAddConcreteFixtureManifest"

    assert "does not assert any new theorem proof" in doc
    assert "does not assert external acceptance" in doc
    assert "does not assert fixture coverage completeness" in doc
    assert "does not allow classifier output to function as a proof" in doc
    assert "does not automatically promote any theorem-like claim" in doc
    assert "does not assert any Clay-level claim" in doc


if __name__ == "__main__":
    verify()
    print("FIXTURE_COVERAGE_AUDIT_OK")
