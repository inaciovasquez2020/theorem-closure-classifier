#!/usr/bin/env python3
import json
from pathlib import Path

ARTIFACT = Path(
    "artifacts/external_validation/"
    "second_candidate_independent_project_adoption_surface_2026_06_21.json"
)

EXPECTED_ID = "second_candidate_independent_project_adoption_surface"
EXPECTED_STATUS = "SECOND_CANDIDATE_EVIDENCE_SURFACE_ONLY"
EXPECTED_PROJECT = "chronos-urf-rr"
EXPECTED_FIRST_PROJECT = "CSLIB-FMT"
EXPECTED_SURFACE = "BOUNDED_CLOSURE_PROOF_PATTERN_REFERENCE"

REQUIRED_BOUNDARY = {
    "This artifact names a second candidate independent-project adoption surface only.",
    "It does not assert that the independent-project usefulness criterion is satisfied.",
    "It does not assert downstream chronos-urf-rr validation has occurred.",
    "It does not prove external acceptance, theorem completeness, or general mathematical usefulness.",
}

REQUIRED_FLAGS = {
    "names_adopted_surface",
    "requires_downstream_verifier",
    "requires_downstream_regression_test",
    "requires_weakest_gap_boundary",
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
        candidate_project.get("repository_role") == "separate formalization target",
        "INVALID_CANDIDATE_REPOSITORY_ROLE",
    )
    require(
        candidate_project.get("adopted_classifier_surface") == EXPECTED_SURFACE,
        "INVALID_ADOPTED_SURFACE",
    )

    relation = data.get("relation_to_existing_candidate")
    require(isinstance(relation, dict), "MISSING_RELATION_TO_EXISTING_CANDIDATE")
    require(
        relation.get("first_candidate_project") == EXPECTED_FIRST_PROJECT,
        "INVALID_FIRST_CANDIDATE_PROJECT",
    )
    require(relation.get("separate_from_first_candidate") is True, "MISSING_SEPARATION_FLAG")
    require(relation.get("minimum_project_count_target") == 2, "INVALID_PROJECT_COUNT_TARGET")

    evidence_shape = data.get("evidence_shape")
    require(isinstance(evidence_shape, dict), "MISSING_EVIDENCE_SHAPE")
    for flag in REQUIRED_FLAGS:
        require(evidence_shape.get(flag) is True, f"MISSING_EVIDENCE_FLAG := {flag}")

    boundary = set(data.get("boundary", []))
    require(REQUIRED_BOUNDARY.issubset(boundary), "MISSING_BOUNDARY")

    weakest_gap = data.get("weakest_gap")
    require(isinstance(weakest_gap, str) and weakest_gap, "MISSING_WEAKEST_GAP")
    require("downstream chronos-urf-rr artifact" in weakest_gap, "INVALID_WEAKEST_GAP")

    print("SECOND_CANDIDATE_INDEPENDENT_PROJECT_ADOPTION_SURFACE_OK")


if __name__ == "__main__":
    main()
