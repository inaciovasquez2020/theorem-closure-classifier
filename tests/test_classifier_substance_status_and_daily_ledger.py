from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def run(script: str) -> str:
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, script],
        cwd=root,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout


def test_classifier_substance_status_field() -> None:
    assert "CLASSIFIER_SUBSTANCE_STATUS_FIELD_OK" in run(
        "verifier/verify_classifier_substance_status_field.py"
    )


def test_cross_repository_daily_closure_ledger() -> None:
    assert "CROSS_REPOSITORY_DAILY_CLOSURE_LEDGER_OK" in run(
        "verifier/verify_cross_repository_daily_closure_ledger.py"
    )
