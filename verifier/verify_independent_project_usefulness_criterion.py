#!/usr/bin/env python3
import json
from pathlib import Path

ARTIFACT = Path("artifacts/independent_project_usefulness_criterion_2026_06_21.json")

EXPECTED_ID = "independent_project_usefulness_criterion"
EXPECTED_STATUS = "CRITERION_ONLY"

REQUIRED_PROJECT_REQUIREMENTS = {
    "separate repository or separately versioned formalization target",
    "non-identical theorem or artifact closure task",
    "local verifier or regression test owned by the downstream project",
    "explicit boundary statement preventing a claim of theorem proof, peer review, or external acceptance",
}

REQUIRED_ADMISSIBLE_EVIDENCE = {
    "downstream artifact names the adopted classifier surface",
    "downstream verifier checks the adopted status boundary",
    "downstream regression test fails when the adopted artifact is removed or corrupted",
    "downstream documentation records the weakest remaining gap",
}

REQUIRED_INADMISSIBLE_EVIDENCE = {
    "repository-local verifier alone",
    "README mention alone",
    "unverified narrative adoption claim",
    "claim of general mathematical completeness",
}

REQUIRED_BOUNDARY = {
    "This artifact defines a criterion only.",
    "It does not assert that any independent project has satisfied the criterion.",
    "It does not prove general usefulness, external acceptance, or theorem completeness.",
}

FORBIDDEN_STATUS_TERMS = {
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

    criterion = data.get("criterion")
    require(isinstance(criterion, dict), "MISSING_CRITERION")

    require(
        criterion.get("minimum_independent_projects") == 2,
        "INVALID_MINIMUM_INDEPENDENT_PROJECTS",
    )

    project_requirements = set(criterion.get("project_independence_requirements", []))
    admissible_evidence = set(criterion.get("admissible_evidence", []))
    inadmissible_evidence = set(criterion.get("inadmissible_evidence", []))
    boundary = set(data.get("boundary", []))

    require(
        REQUIRED_PROJECT_REQUIREMENTS.issubset(project_requirements),
        "MISSING_PROJECT_INDEPENDENCE_REQUIREMENT",
    )
    require(
        REQUIRED_ADMISSIBLE_EVIDENCE.issubset(admissible_evidence),
        "MISSING_ADMISSIBLE_EVIDENCE",
    )
    require(
        REQUIRED_INADMISSIBLE_EVIDENCE.issubset(inadmissible_evidence),
        "MISSING_INADMISSIBLE_EVIDENCE",
    )
    require(REQUIRED_BOUNDARY.issubset(boundary), "MISSING_BOUNDARY")

    print("INDEPENDENT_PROJECT_USEFULNESS_CRITERION_OK")


if __name__ == "__main__":
    main()
