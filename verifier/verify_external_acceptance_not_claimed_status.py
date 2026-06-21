#!/usr/bin/env python3
import json
from pathlib import Path

ARTIFACT = Path(
    "artifacts/external_validation/"
    "external_acceptance_not_claimed_status_2026_06_21.json"
)
RELATED_ARTIFACT = Path(
    "artifacts/external_validation/"
    "independent_project_usefulness_criterion_satisfaction_status_2026_06_21.json"
)

EXPECTED_ID = "external_acceptance_not_claimed_status"
EXPECTED_STATUS = "EXTERNAL_ACCEPTANCE_NOT_CLAIMED"
EXPECTED_RELATED = "independent_project_usefulness_criterion_satisfaction_status_2026_06_21"
EXPECTED_SURFACE = "BOUNDED_CLOSURE_PROOF_PATTERN_REFERENCE"

REQUIRED_FALSE_FLAGS = {
    "external_acceptance_claimed",
    "peer_review_claimed",
    "third_party_adoption_claimed",
    "theorem_completeness_claimed",
    "general_mathematical_usefulness_claimed",
}

REQUIRED_BOUNDARY = {
    "This artifact records that external acceptance is not claimed.",
    "The prior satisfaction status is repository-local and owner-controlled evidence only.",
    "No peer review, third-party adoption, theorem completeness, or general mathematical usefulness is asserted.",
    "The bounded closure proof-pattern reference is not converted into a mathematical theorem by this status.",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def load_json(path: Path) -> dict:
    require(path.exists(), f"MISSING_OBJECT := {path}")
    return json.loads(path.read_text())


def main() -> None:
    related = load_json(RELATED_ARTIFACT)
    data = load_json(ARTIFACT)

    require(
        related.get("id") == "independent_project_usefulness_criterion_satisfaction_status",
        "INVALID_RELATED_STATUS_ID",
    )
    require(
        related.get("status") == "CRITERION_SATISFIED_BY_TWO_PROJECT_DOWNSTREAM_EVIDENCE",
        "INVALID_RELATED_STATUS",
    )

    require(data.get("id") == EXPECTED_ID, "INVALID_ID")
    require(data.get("status") == EXPECTED_STATUS, "INVALID_STATUS")
    require(data.get("related_status_artifact") == EXPECTED_RELATED, "INVALID_RELATED_ARTIFACT")
    require(data.get("source_surface") == EXPECTED_SURFACE, "INVALID_SOURCE_SURFACE")

    scope = data.get("scope")
    require(isinstance(scope, dict), "MISSING_SCOPE")
    require(scope.get("repository_local_criterion_satisfaction") is True, "MISSING_LOCAL_STATUS_FLAG")

    for flag in REQUIRED_FALSE_FLAGS:
        require(scope.get(flag) is False, f"OVERCLAIMED_SCOPE_FLAG := {flag}")

    boundary = set(data.get("boundary", []))
    require(REQUIRED_BOUNDARY.issubset(boundary), "MISSING_BOUNDARY")

    weakest_gap = data.get("weakest_gap")
    require(isinstance(weakest_gap, str) and weakest_gap, "MISSING_WEAKEST_GAP")
    require("independent third-party review" in weakest_gap, "INVALID_WEAKEST_GAP")

    print("EXTERNAL_ACCEPTANCE_NOT_CLAIMED_STATUS_OK")


if __name__ == "__main__":
    main()
