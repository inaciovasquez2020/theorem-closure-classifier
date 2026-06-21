#!/usr/bin/env python3
import json
from pathlib import Path

ARTIFACT = Path(
    "artifacts/external_validation/"
    "candidate_independent_project_adoption_surface_2026_06_21.json"
)

EXPECTED_ID = "candidate_independent_project_adoption_surface"
EXPECTED_STATUS = "CANDIDATE_EVIDENCE_SURFACE_ONLY"
EXPECTED_PROJECT = "CSLIB-FMT"
EXPECTED_ADOPTED_SURFACE = "BOUNDED_CLOSURE_PROOF_PATTERN_REFERENCE"

REQUIRED_BOUNDARY = {
    "This artifact names one candidate independent-project adoption surface only.",
    "It does not assert that the independent-project usefulness criterion is satisfied.",
    "It does not assert two independent projects.",
    "It does not prove external acceptance, theorem completeness, or general mathematical usefulness.",
}

FORBIDDEN_STATUS_TERMS = {
    "SATISFIED",
    "COMPLETE",
    "PROVED",
    "CLOSED",
    "EXTERNALLY_ACCEPTED",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    require(ARTIFACT.exists(), f"MISSING_OBJECT := {ARTIFACT}")
    data = json.loads(ARTIFACT.read_text())

    require(data.get("id") == EXPECTED_ID, "INVALID_ID")
    require(data.get("status") == EXPECTED_STATUS, "INVALID_STATUS")

    status = str(data.get("status", ""))
    require(not any(term in status for term in FORBIDDEN_STATUS_TERMS), "OVERCLAIMED_STATUS")

    candidate_project = data.get("candidate_project")
    require(isinstance(candidate_project, dict), "MISSING_CANDIDATE_PROJECT")
    require(candidate_project.get("name") == EXPECTED_PROJECT, "INVALID_CANDIDATE_PROJECT")
    require(
        candidate_project.get("adopted_classifier_surface") == EXPECTED_ADOPTED_SURFACE,
        "INVALID_ADOPTED_SURFACE",
    )

    evidence_shape = data.get("evidence_shape")
    require(isinstance(evidence_shape, dict), "MISSING_EVIDENCE_SHAPE")
    for key in (
        "names_adopted_surface",
        "requires_downstream_verifier",
        "requires_downstream_regression_test",
        "requires_weakest_gap_boundary",
    ):
        require(evidence_shape.get(key) is True, f"MISSING_EVIDENCE_SHAPE_FLAG := {key}")

    boundary = set(data.get("boundary", []))
    require(REQUIRED_BOUNDARY.issubset(boundary), "MISSING_BOUNDARY")

    weakest_gap = data.get("weakest_gap")
    require(isinstance(weakest_gap, str) and weakest_gap, "MISSING_WEAKEST_GAP")
    require("downstream CSLIB-FMT artifact" in weakest_gap, "INVALID_WEAKEST_GAP")

    print("CANDIDATE_INDEPENDENT_PROJECT_ADOPTION_SURFACE_OK")


if __name__ == "__main__":
    main()
