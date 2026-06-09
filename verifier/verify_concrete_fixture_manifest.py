from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ARTIFACT = ROOT / "artifacts" / "status" / "concrete_fixture_manifest_2026_06_09.json"
DOC = ROOT / "docs" / "status" / "CONCRETE_FIXTURE_MANIFEST_2026_06_09.md"

BOUNDARY_LOCK = ROOT / "artifacts" / "status" / "classification_boundary_lock_2026_06_09.json"
BENCHMARK_CONTROL = ROOT / "artifacts" / "status" / "additional_independent_benchmark_control_2026_06_09.json"
FIXTURE_AUDIT = ROOT / "artifacts" / "status" / "fixture_coverage_audit_2026_06_09.json"

REQUIRED_DEPENDENCIES = {
    "ClassificationBoundaryLock",
    "AdditionalIndependentBenchmarkControl",
    "FixtureCoverageAudit",
}

REQUIRED_FIXTURES = {
    ("positive_closed_theorem_fixture_001", "positive_closed_theorem_fixture", "CLOSED_THEOREM"),
    ("negative_open_frontier_fixture_001", "negative_open_frontier_fixture", "OPEN_FRONTIER"),
    ("boundary_only_status_fixture_001", "boundary_only_status_fixture", "BOUNDARY_ONLY"),
    ("external_acceptance_absent_fixture_001", "external_acceptance_absent_fixture", "NO_EXTERNAL_ACCEPTANCE"),
    ("classifier_output_not_proof_fixture_001", "classifier_output_not_proof_fixture", "CLASSIFIER_OUTPUT_NOT_PROOF"),
    ("clay_claim_negative_control_fixture_001", "clay_claim_negative_control_fixture", "NO_CLAY_CLAIM"),
}

REQUIRED_NON_CLAIMS = {
    "NO_NEW_THEOREM_PROOF",
    "NO_EXTERNAL_THEOREM_ACCEPTANCE",
    "NO_FIXTURE_COVERAGE_COMPLETENESS_CLAIM",
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
    fixture_audit = read_json(FIXTURE_AUDIT)

    assert boundary_lock["closed_object"] == "ClassificationBoundaryLock"
    assert benchmark_control["closed_object"] == "AdditionalIndependentBenchmarkControl"
    assert fixture_audit["closed_object"] == "FixtureCoverageAudit"

    assert artifact["id"] == "CONCRETE_FIXTURE_MANIFEST_2026_06_09"
    assert artifact["repository"] == "theorem-closure-classifier"
    assert artifact["status"] == "CONCRETE_FIXTURE_MANIFEST_ADDED"
    assert artifact["closed_object"] == "ConcreteFixtureManifest"
    assert artifact["object_type"] == "fixture_manifest_boundary"
    assert set(artifact["depends_on"]) == REQUIRED_DEPENDENCIES
    assert set(artifact["non_claims"]) == REQUIRED_NON_CLAIMS
    assert artifact["next_admissible_object"] == "StopOrAddManifestDrivenFixtureTest"

    fixtures = artifact["fixtures"]
    observed = {
        (fixture["id"], fixture["category"], fixture["expected_label"])
        for fixture in fixtures
    }
    assert observed == REQUIRED_FIXTURES
    assert all(fixture["source_status"] == "manifest_control_only" for fixture in fixtures)

    fixture_audit_categories = set(fixture_audit["required_fixture_categories"])
    manifest_categories = {fixture["category"] for fixture in fixtures}
    assert manifest_categories == fixture_audit_categories

    assert "does not assert any new theorem proof" in doc
    assert "does not assert external acceptance" in doc
    assert "does not assert fixture coverage completeness" in doc
    assert "does not allow classifier output to function as a proof" in doc
    assert "does not automatically promote any theorem-like claim" in doc
    assert "does not assert any Clay-level claim" in doc


if __name__ == "__main__":
    verify()
    print("CONCRETE_FIXTURE_MANIFEST_OK")
