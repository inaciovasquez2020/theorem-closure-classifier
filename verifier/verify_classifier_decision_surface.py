from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ARTIFACT = ROOT / "artifacts" / "status" / "classifier_decision_surface_2026_06_09.json"
DOC = ROOT / "docs" / "status" / "CLASSIFIER_DECISION_SURFACE_2026_06_09.md"

BOUNDARY_LOCK = ROOT / "artifacts" / "status" / "classification_boundary_lock_2026_06_09.json"
BENCHMARK_CONTROL = ROOT / "artifacts" / "status" / "additional_independent_benchmark_control_2026_06_09.json"
FIXTURE_AUDIT = ROOT / "artifacts" / "status" / "fixture_coverage_audit_2026_06_09.json"
CONCRETE_MANIFEST = ROOT / "artifacts" / "status" / "concrete_fixture_manifest_2026_06_09.json"
MANIFEST_TEST = ROOT / "artifacts" / "status" / "manifest_driven_fixture_test_2026_06_09.json"

REQUIRED_DEPENDENCIES = {
    "ClassificationBoundaryLock",
    "AdditionalIndependentBenchmarkControl",
    "FixtureCoverageAudit",
    "ConcreteFixtureManifest",
    "ManifestDrivenFixtureTest",
}

REQUIRED_DECISION_PROPERTIES = {
    "covers_every_manifest_expected_label",
    "uses_unique_classifier_decisions",
    "marks_every_decision_not_a_proof",
    "preserves_boundary_non_claims",
    "depends_on_manifest_driven_fixture_test",
}

REQUIRED_NON_CLAIMS = {
    "NO_NEW_THEOREM_PROOF",
    "NO_EXTERNAL_THEOREM_ACCEPTANCE",
    "NO_CLASSIFIER_DECISION_AS_PROOF",
    "NO_AUTOMATIC_THEOREM_PROMOTION",
    "NO_CLAY_CLAIM",
}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def classifier_decision_map() -> dict[str, str]:
    artifact = read_json(ARTIFACT)
    return {
        row["input_expected_label"]: row["classifier_decision"]
        for row in artifact["decision_surface"]
    }


def verify() -> None:
    artifact = read_json(ARTIFACT)
    doc = DOC.read_text(encoding="utf-8")

    boundary_lock = read_json(BOUNDARY_LOCK)
    benchmark_control = read_json(BENCHMARK_CONTROL)
    fixture_audit = read_json(FIXTURE_AUDIT)
    concrete_manifest = read_json(CONCRETE_MANIFEST)
    manifest_test = read_json(MANIFEST_TEST)

    assert boundary_lock["closed_object"] == "ClassificationBoundaryLock"
    assert benchmark_control["closed_object"] == "AdditionalIndependentBenchmarkControl"
    assert fixture_audit["closed_object"] == "FixtureCoverageAudit"
    assert concrete_manifest["closed_object"] == "ConcreteFixtureManifest"
    assert manifest_test["closed_object"] == "ManifestDrivenFixtureTest"

    assert artifact["id"] == "CLASSIFIER_DECISION_SURFACE_2026_06_09"
    assert artifact["repository"] == "theorem-closure-classifier"
    assert artifact["status"] == "CLASSIFIER_DECISION_SURFACE_ADDED"
    assert artifact["closed_object"] == "ClassifierDecisionSurface"
    assert artifact["object_type"] == "decision_surface_boundary"
    assert set(artifact["depends_on"]) == REQUIRED_DEPENDENCIES
    assert set(artifact["required_decision_properties"]) == REQUIRED_DECISION_PROPERTIES
    assert set(artifact["non_claims"]) == REQUIRED_NON_CLAIMS
    assert artifact["next_admissible_object"] == "StopOrAddDecisionSurfaceVerifierEntrypoint"

    manifest_labels = {
        fixture["expected_label"]
        for fixture in concrete_manifest["fixtures"]
    }

    decision_surface = artifact["decision_surface"]
    input_labels = {
        row["input_expected_label"]
        for row in decision_surface
    }
    classifier_decisions = [
        row["classifier_decision"]
        for row in decision_surface
    ]

    assert input_labels == manifest_labels
    assert len(classifier_decisions) == len(set(classifier_decisions))
    assert all(row["proof_promotion_status"] == "NOT_A_PROOF" for row in decision_surface)

    decision_map = classifier_decision_map()
    assert set(decision_map) == manifest_labels
    assert all(value.startswith("LABEL_") for value in decision_map.values())

    assert "does not assert any new theorem proof" in doc
    assert "does not assert external acceptance" in doc
    assert "does not allow classifier decisions to function as proofs" in doc
    assert "does not automatically promote any theorem-like claim" in doc
    assert "does not assert any Clay-level claim" in doc


if __name__ == "__main__":
    verify()
    print("CLASSIFIER_DECISION_SURFACE_OK")
