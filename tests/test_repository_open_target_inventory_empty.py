from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def test_repository_open_target_inventory_empty() -> None:
    result = subprocess.run(
        [sys.executable, "tools/inventory_open_targets.py"],
        check=True,
        text=True,
        capture_output=True,
    )
    assert result.stdout.strip() == "REPOSITORY_OPEN_TARGET_INVENTORY_EMPTY"


def test_repository_open_target_inventory_empty_artifact() -> None:
    artifact = Path("artifacts/external_validation/repository_open_target_inventory_empty_2026_06_12.json")
    data = json.loads(artifact.read_text())

    assert data["certificate_id"] == "REPOSITORY_OPEN_TARGET_INVENTORY_EMPTY_2026_06_12"
    assert data["inventory_result"] == "REPOSITORY_OPEN_TARGET_INVENTORY_EMPTY"
    assert data["claim_boundary"]["does_not_claim_all_mathematics_solved"] is True
    assert data["claim_boundary"]["does_not_claim_absence_of_all_bugs"] is True
    assert data["claim_boundary"]["does_not_claim_external_project_status"] is True
    assert data["claim_boundary"]["only_claims_no_matching_open_target_markers"] is True
