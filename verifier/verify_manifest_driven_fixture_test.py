from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ARTIFACT = ROOT / "artifacts" / "status" / "manifest_driven_fixture_test_2026_06_09.json"
DOC = ROOT / "docs" / "status" / "MANIFEST_DRIVEN_FIXTURE_TEST_2026_06_09.md"

BOUNDARY_LOCK = ROOT / "artifacts" / "status" / "classification_boundary_lock_2026_06_09.json"
BENCHMARK_CONTROL = ROOT / "artifacts" / "status" / "additional_independent_benchmark_control_2026_06_09.json"
FIXTURE_AUDIT = ROOT / "artifacts" / "status" / "fixture_coverage_audit_2026_06_09.json"
CONCRETE_MANIFEST = ROOT / "artifacts" / "status" / "concrete_fixture_manifest_2026_06_09.json"

REQUIRED_DEPENDENCIES = {
    "ClassificationBoundaryLock",
    "AdditionalIndependentBenchmarkControl",
    "FixtureCoverageAudit",
    "ConcreteFixtureManifest",
}

REQUIRED_TEST_PROPERTIES = {
    "loads_concrete_fixture_manifest",
    "checks_fixture_id_uniqueness",
    "checks_manifest_categories_against_fixture_audit",
    "checks_expected_labels_are_nonempty",
    "checks_source_status_manifest_control_only",
    "checks_all_manifest_fixtures_observed",
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


def manifest_fixture_label_map() -> dict[str, str]:
    manifest = read_json(CONCRETE_MANIFEST)
    return {
        fixture["id"]: fixture["expected_label"]
        for fixture in manifest["fixtures"]
    }


def verify() -> None:
    artifact = read_json(ARTIFACT)
    doc = DOC.read_text(encoding="utf-8")

    boundary_lock = read_json(BOUNDARY_LOCK)
    benchmark_control = read_json(BENCHMARK_CONTROL)
    fixture_audit = read_json(FIXTURE_AUDIT)
    concrete_manifest = read_json(CONCRETE_MANIFEST)

    assert boundary_lock["closed_object"] == "ClassificationBoundaryLock"
    assert benchmark_control["closed_object"] == "AdditionalIndependentBenchmarkControl"
    assert fixture_audit["closed_object"] == "FixtureCoverageAudit"
    assert concrete_manifest["closed_object"] == "ConcreteFixtureManifest"

    assert artifact["id"] == "MANIFEST_DRIVEN_FIXTURE_TEST_2026_06_09"
    assert artifact["repository"] == "theorem-closure-classifier"
    assert artifact["status"] == "MANIFEST_DRIVEN_FIXTURE_TEST_ADDED"
    assert artifact["closed_object"] == "ManifestDrivenFixtureTest"
    assert artifact["object_type"] == "manifest_driven_test_boundary"
    assert set(artifact["depends_on"]) == REQUIRED_DEPENDENCIES
    assert set(artifact["required_test_properties"]) == REQUIRED_TEST_PROPERTIES
    assert set(artifact["non_claims"]) == REQUIRED_NON_CLAIMS
    assert artifact["next_admissible_object"] == "StopOrAddClassifierDecisionSurface"

    fixtures = concrete_manifest["fixtures"]
    fixture_ids = [fixture["id"] for fixture in fixtures]
    fixture_categories = {fixture["category"] for fixture in fixtures}
    fixture_labels = [fixture["expected_label"] for fixture in fixtures]

    assert len(fixture_ids) == len(set(fixture_ids))
    assert fixture_categories == set(fixture_audit["required_fixture_categories"])
    assert all(isinstance(label, str) and label for label in fixture_labels)
    assert all(fixture["source_status"] == "manifest_control_only" for fixture in fixtures)

    label_map = manifest_fixture_label_map()
    assert set(label_map) == set(fixture_ids)
    assert all(label_map[fixture["id"]] == fixture["expected_label"] for fixture in fixtures)

    assert "does not assert any new theorem proof" in doc
    assert "does not assert external acceptance" in doc
    assert "does not assert fixture coverage completeness" in doc
    assert "does not allow classifier output to function as a proof" in doc
    assert "does not automatically promote any theorem-like claim" in doc
    assert "does not assert any Clay-level claim" in doc


if __name__ == "__main__":
    verify()
    print("MANIFEST_DRIVEN_FIXTURE_TEST_OK")
