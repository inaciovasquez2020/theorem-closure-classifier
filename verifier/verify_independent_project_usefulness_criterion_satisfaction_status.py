#!/usr/bin/env python3
import json
from pathlib import Path

STATUS_ARTIFACT = Path(
    "artifacts/external_validation/"
    "independent_project_usefulness_criterion_satisfaction_status_2026_06_21.json"
)
CRITERION_ARTIFACT = Path("artifacts/independent_project_usefulness_criterion_2026_06_21.json")
AGGREGATION_ARTIFACT = Path(
    "artifacts/external_validation/"
    "two_project_downstream_evidence_aggregation_2026_06_21.json"
)

EXPECTED_ID = "independent_project_usefulness_criterion_satisfaction_status"
EXPECTED_STATUS = "CRITERION_SATISFIED_BY_TWO_PROJECT_DOWNSTREAM_EVIDENCE"
EXPECTED_CRITERION_ID = "independent_project_usefulness_criterion"
EXPECTED_AGGREGATION_ID = "two_project_downstream_evidence_aggregation"
EXPECTED_SURFACE = "BOUNDED_CLOSURE_PROOF_PATTERN_REFERENCE"

EXPECTED_PROJECTS = {"CSLIB-FMT", "chronos-urf-rr"}
EXPECTED_REPOSITORIES = {
    "inaciovasquez2020/cslib-fmt",
    "inaciovasquez2020/chronos-urf-rr",
}
EXPECTED_COMMITS = {
    "43e9fbca848c0d112dbfd643482a2d069701176d",
    "05a798a1a36d69e22547a86234f52f7c4575c1cf",
}

REQUIRED_BOUNDARY = {
    "This status satisfies only the repository-local independent-project usefulness criterion encoded by independent_project_usefulness_criterion_2026_06_21.",
    "It relies on the two-project downstream aggregation artifact and does not independently re-run downstream repositories.",
    "It does not prove external acceptance, peer review, theorem completeness, or general mathematical usefulness.",
    "It does not convert the bounded closure proof-pattern reference into a mathematical theorem.",
}

FORBIDDEN_BOUNDARY_OMISSIONS = {
    "external acceptance",
    "peer review",
    "theorem completeness",
    "mathematical theorem",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def load_json(path: Path) -> dict:
    require(path.exists(), f"MISSING_OBJECT := {path}")
    return json.loads(path.read_text())


def main() -> None:
    criterion = load_json(CRITERION_ARTIFACT)
    aggregation = load_json(AGGREGATION_ARTIFACT)
    status = load_json(STATUS_ARTIFACT)

    require(criterion.get("id") == EXPECTED_CRITERION_ID, "INVALID_CRITERION_ID")
    require(criterion.get("status") == "CRITERION_ONLY", "INVALID_CRITERION_STATUS")

    criterion_body = criterion.get("criterion")
    require(isinstance(criterion_body, dict), "MISSING_CRITERION_BODY")
    require(
        criterion_body.get("minimum_independent_projects") == 2,
        "INVALID_CRITERION_MINIMUM_PROJECTS",
    )

    require(aggregation.get("id") == EXPECTED_AGGREGATION_ID, "INVALID_AGGREGATION_ID")
    require(
        aggregation.get("status") == "DOWNSTREAM_EVIDENCE_AGGREGATION_ONLY",
        "INVALID_AGGREGATION_STATUS",
    )
    require(aggregation.get("source_surface") == EXPECTED_SURFACE, "INVALID_AGGREGATION_SURFACE")

    downstream_evidence = aggregation.get("downstream_evidence")
    require(isinstance(downstream_evidence, list), "MISSING_AGGREGATION_DOWNSTREAM_EVIDENCE")
    require(len(downstream_evidence) == 2, "INVALID_AGGREGATION_DOWNSTREAM_COUNT")

    aggregation_projects = {item.get("project") for item in downstream_evidence}
    aggregation_repositories = {item.get("repository") for item in downstream_evidence}
    aggregation_commits = {item.get("downstream_commit") for item in downstream_evidence}

    require(aggregation_projects == EXPECTED_PROJECTS, "INVALID_AGGREGATION_PROJECTS")
    require(aggregation_repositories == EXPECTED_REPOSITORIES, "INVALID_AGGREGATION_REPOSITORIES")
    require(aggregation_commits == EXPECTED_COMMITS, "INVALID_AGGREGATION_COMMITS")

    for item in downstream_evidence:
        require(
            item.get("validated_status")
            == "CLASSIFIER_BOUNDED_CLOSURE_REFERENCE_DOWNSTREAM_ADOPTION_OK",
            "INVALID_DOWNSTREAM_VALIDATED_STATUS",
        )
        require(item.get("artifact"), "MISSING_DOWNSTREAM_ARTIFACT")
        require(item.get("verifier"), "MISSING_DOWNSTREAM_VERIFIER")
        require(item.get("targeted_test"), "MISSING_DOWNSTREAM_TARGETED_TEST")

    require(status.get("id") == EXPECTED_ID, "INVALID_STATUS_ID")
    require(status.get("status") == EXPECTED_STATUS, "INVALID_STATUS")
    require(
        status.get("criterion_artifact") == "independent_project_usefulness_criterion_2026_06_21",
        "INVALID_STATUS_CRITERION_ARTIFACT",
    )
    require(
        status.get("checked_aggregation_artifact")
        == "two_project_downstream_evidence_aggregation_2026_06_21",
        "INVALID_STATUS_AGGREGATION_ARTIFACT",
    )
    require(status.get("source_surface") == EXPECTED_SURFACE, "INVALID_STATUS_SURFACE")

    basis = status.get("satisfaction_basis")
    require(isinstance(basis, dict), "MISSING_SATISFACTION_BASIS")
    require(
        basis.get("minimum_independent_projects_required") == 2,
        "INVALID_STATUS_MINIMUM_PROJECTS",
    )
    require(set(basis.get("downstream_projects_recorded", [])) == EXPECTED_PROJECTS, "INVALID_STATUS_PROJECTS")
    require(
        set(basis.get("distinct_repositories_recorded", [])) == EXPECTED_REPOSITORIES,
        "INVALID_STATUS_REPOSITORIES",
    )
    require(
        set(basis.get("downstream_commits_recorded", [])) == EXPECTED_COMMITS,
        "INVALID_STATUS_COMMITS",
    )

    for flag in (
        "downstream_artifacts_recorded",
        "downstream_verifiers_recorded",
        "downstream_regression_tests_recorded",
        "weakest_gap_boundary_recorded",
    ):
        require(basis.get(flag) is True, f"MISSING_SATISFACTION_FLAG := {flag}")

    boundary = set(status.get("boundary", []))
    require(REQUIRED_BOUNDARY.issubset(boundary), "MISSING_BOUNDARY")

    boundary_text = " ".join(boundary)
    for phrase in FORBIDDEN_BOUNDARY_OMISSIONS:
        require(phrase in boundary_text, f"MISSING_BOUNDARY_PHRASE := {phrase}")

    weakest_gap = status.get("weakest_gap")
    require(isinstance(weakest_gap, str) and weakest_gap, "MISSING_WEAKEST_GAP")
    require("third-party review" in weakest_gap, "INVALID_WEAKEST_GAP")

    print("INDEPENDENT_PROJECT_USEFULNESS_CRITERION_SATISFACTION_STATUS_OK")


if __name__ == "__main__":
    main()
