from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts" / "status" / "additional_independent_benchmark_control_2026_06_09.json"
DOC = ROOT / "docs" / "status" / "ADDITIONAL_INDEPENDENT_BENCHMARK_CONTROL_2026_06_09.md"
BOUNDARY_LOCK = ROOT / "artifacts" / "status" / "classification_boundary_lock_2026_06_09.json"

REQUIRED_CONTROLS = {
    "independent_fixture_source",
    "frozen_expected_labels",
    "non_self_scored_result",
    "negative_control_case",
    "positive_control_case",
    "boundary_non_claims",
    "provenance_record",
}

REQUIRED_NON_CLAIMS = {
    "NO_NEW_THEOREM_PROOF",
    "NO_EXTERNAL_THEOREM_ACCEPTANCE",
    "NO_CLASSIFIER_OUTPUT_AS_PROOF",
    "NO_AUTOMATIC_THEOREM_PROMOTION",
    "NO_CLAY_CLAIM",
}


def verify() -> None:
    artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    doc = DOC.read_text(encoding="utf-8")
    boundary_lock = json.loads(BOUNDARY_LOCK.read_text(encoding="utf-8"))

    assert boundary_lock["closed_object"] == "ClassificationBoundaryLock"

    assert artifact["id"] == "ADDITIONAL_INDEPENDENT_BENCHMARK_CONTROL_2026_06_09"
    assert artifact["repository"] == "theorem-closure-classifier"
    assert artifact["status"] == "INDEPENDENT_BENCHMARK_CONTROL_ADDED"
    assert artifact["closed_object"] == "AdditionalIndependentBenchmarkControl"
    assert artifact["object_type"] == "benchmark_control_boundary"
    assert set(artifact["required_controls"]) == REQUIRED_CONTROLS
    assert set(artifact["non_claims"]) == REQUIRED_NON_CLAIMS
    assert artifact["depends_on"] == ["ClassificationBoundaryLock"]
    assert artifact["next_admissible_object"] == "StopOrAddFixtureCoverageAudit"

    assert "does not assert any new theorem proof" in doc
    assert "does not assert external acceptance" in doc
    assert "does not allow classifier output to function as a proof" in doc
    assert "does not automatically promote any theorem-like claim" in doc
    assert "does not assert any Clay-level claim" in doc


if __name__ == "__main__":
    verify()
    print("ADDITIONAL_INDEPENDENT_BENCHMARK_CONTROL_OK")
