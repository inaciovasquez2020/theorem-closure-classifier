#!/usr/bin/env python3
import json
from pathlib import Path

ARTIFACT = Path(
    "artifacts/external_validation/"
    "urf_templates_downstream_use_request_2026_06_23.json"
)

EXPECTED_ID = "urf_templates_downstream_use_request"
EXPECTED_STATUS = "DOWNSTREAM_USE_REQUEST_ONLY"
EXPECTED_SOURCE = "urf-templates"
EXPECTED_DOWNSTREAM = "theorem-closure-classifier"
EXPECTED_COMMIT = "12ac5fe02b4bcd3f3b698a5ba86f48c8fbc2e9e7"

REQUIRED_BOUNDARY = {
    "This artifact records a downstream-use request only.",
    "It does not claim independent external adoption.",
    "It does not claim peer review, manuscript acceptance, scientific validation, or new physics.",
    "It does not claim that theorem-closure-classifier adoption criteria are satisfied.",
    "Actual external adoption remains unclaimed until an independent user or project uses the workflow.",
}

FORBIDDEN_STATUS_TERMS = {
    "ADOPTED",
    "SATISFIED",
    "COMPLETE",
    "PROVED",
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

    downstream = data.get("candidate_downstream_project")
    require(isinstance(downstream, dict), "MISSING_DOWNSTREAM_PROJECT")
    require(downstream.get("name") == EXPECTED_DOWNSTREAM, "INVALID_DOWNSTREAM_PROJECT")

    source = data.get("source_project")
    require(isinstance(source, dict), "MISSING_SOURCE_PROJECT")
    require(source.get("name") == EXPECTED_SOURCE, "INVALID_SOURCE_PROJECT")
    require(source.get("confirmed_main_commit") == EXPECTED_COMMIT, "INVALID_SOURCE_COMMIT")
    require(source.get("clean_clone_result") == "FINAL_CLEAN_CLONE_OK", "INVALID_CLEAN_CLONE_RESULT")

    requested_check = data.get("requested_check")
    require(isinstance(requested_check, list), "MISSING_REQUESTED_CHECK")
    require(len(requested_check) >= 4, "INSUFFICIENT_REQUESTED_CHECK")

    boundary = set(data.get("boundary", []))
    require(REQUIRED_BOUNDARY.issubset(boundary), "MISSING_BOUNDARY")

    weakest_gap = data.get("weakest_gap")
    require(isinstance(weakest_gap, str) and weakest_gap, "MISSING_WEAKEST_GAP")
    require("No independent user or project" in weakest_gap, "INVALID_WEAKEST_GAP")

    print("URF_TEMPLATES_DOWNSTREAM_USE_REQUEST_OK")


if __name__ == "__main__":
    main()
