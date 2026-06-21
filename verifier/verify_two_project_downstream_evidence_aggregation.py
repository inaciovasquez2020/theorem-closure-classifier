#!/usr/bin/env python3
import json
from pathlib import Path

ARTIFACT = Path(
    "artifacts/external_validation/"
    "two_project_downstream_evidence_aggregation_2026_06_21.json"
)

EXPECTED_ID = "two_project_downstream_evidence_aggregation"
EXPECTED_STATUS = "DOWNSTREAM_EVIDENCE_AGGREGATION_ONLY"
EXPECTED_SURFACE = "BOUNDED_CLOSURE_PROOF_PATTERN_REFERENCE"
EXPECTED_CRITERION = "independent_project_usefulness_criterion_2026_06_21"

EXPECTED_EVIDENCE = {
    "CSLIB-FMT": {
        "repository": "inaciovasquez2020/cslib-fmt",
        "downstream_commit": "43e9fbca848c0d112dbfd643482a2d069701176d",
        "artifact": "artifacts/classifier_bounded_closure_reference_downstream_adoption_2026_06_21.json",
    },
    "chronos-urf-rr": {
        "repository": "inaciovasquez2020/chronos-urf-rr",
        "downstream_commit": "05a798a1a36d69e22547a86234f52f7c4575c1cf",
        "artifact": "artifacts/chronos/classifier_bounded_closure_reference_downstream_adoption_2026_06_21.json",
    },
}

REQUIRED_FLAGS = {
    "names_adopted_classifier_surface",
    "records_two_downstream_projects",
    "records_distinct_repositories",
    "records_downstream_commits",
    "records_downstream_artifacts",
    "records_downstream_verifiers",
    "records_downstream_regression_tests",
    "records_weakest_gap_boundary",
}

REQUIRED_BOUNDARY = {
    "This artifact aggregates two downstream evidence surfaces only.",
    "It does not prove external acceptance, theorem completeness, or general mathematical usefulness.",
    "It does not assert peer review or upstream adoption.",
    "It does not convert the bounded closure proof-pattern reference into a mathematical theorem.",
}

FORBIDDEN_STATUS_TERMS = {
    "COMPLETE",
    "PROVED",
    "CLOSED",
    "EXTERNALLY_ACCEPTED",
    "PEER_REVIEWED",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    require(ARTIFACT.exists(), f"MISSING_OBJECT := {ARTIFACT}")
    data = json.loads(ARTIFACT.read_text())

    require(data.get("id") == EXPECTED_ID, "INVALID_ID")
    require(data.get("status") == EXPECTED_STATUS, "INVALID_STATUS")
    require(data.get("source_surface") == EXPECTED_SURFACE, "INVALID_SOURCE_SURFACE")
    require(data.get("criterion_artifact") == EXPECTED_CRITERION, "INVALID_CRITERION_ARTIFACT")

    status = str(data.get("status", ""))
    require(not any(term in status for term in FORBIDDEN_STATUS_TERMS), "OVERCLAIMED_STATUS")

    downstream_evidence = data.get("downstream_evidence")
    require(isinstance(downstream_evidence, list), "MISSING_DOWNSTREAM_EVIDENCE")
    require(len(downstream_evidence) == 2, "INVALID_DOWNSTREAM_EVIDENCE_COUNT")

    seen_projects = set()
    seen_repositories = set()
    seen_commits = set()

    for item in downstream_evidence:
        require(isinstance(item, dict), "INVALID_DOWNSTREAM_EVIDENCE_ITEM")
        project = item.get("project")
        require(project in EXPECTED_EVIDENCE, f"UNKNOWN_DOWNSTREAM_PROJECT := {project}")

        expected = EXPECTED_EVIDENCE[project]
        require(item.get("repository") == expected["repository"], "INVALID_REPOSITORY")
        require(item.get("downstream_commit") == expected["downstream_commit"], "INVALID_COMMIT")
        require(item.get("artifact") == expected["artifact"], "INVALID_ARTIFACT")
        require(
            item.get("verifier") == "tools/verify_classifier_bounded_closure_reference_downstream_adoption.py",
            "INVALID_VERIFIER",
        )
        require(
            item.get("targeted_test") == "tests/test_classifier_bounded_closure_reference_downstream_adoption.py",
            "INVALID_TARGETED_TEST",
        )
        require(
            item.get("validated_status")
            == "CLASSIFIER_BOUNDED_CLOSURE_REFERENCE_DOWNSTREAM_ADOPTION_OK",
            "INVALID_VALIDATED_STATUS",
        )

        seen_projects.add(project)
        seen_repositories.add(item.get("repository"))
        seen_commits.add(item.get("downstream_commit"))

    require(seen_projects == set(EXPECTED_EVIDENCE), "MISSING_DOWNSTREAM_PROJECT")
    require(len(seen_repositories) == 2, "DOWNSTREAM_REPOSITORIES_NOT_DISTINCT")
    require(len(seen_commits) == 2, "DOWNSTREAM_COMMITS_NOT_DISTINCT")

    evidence_shape = data.get("evidence_shape")
    require(isinstance(evidence_shape, dict), "MISSING_EVIDENCE_SHAPE")
    for flag in REQUIRED_FLAGS:
        require(evidence_shape.get(flag) is True, f"MISSING_EVIDENCE_FLAG := {flag}")

    boundary = set(data.get("boundary", []))
    require(REQUIRED_BOUNDARY.issubset(boundary), "MISSING_BOUNDARY")

    weakest_gap = data.get("weakest_gap")
    require(isinstance(weakest_gap, str) and weakest_gap, "MISSING_WEAKEST_GAP")
    require("criterion-satisfaction status" in weakest_gap, "INVALID_WEAKEST_GAP")

    print("TWO_PROJECT_DOWNSTREAM_EVIDENCE_AGGREGATION_OK")


if __name__ == "__main__":
    main()
