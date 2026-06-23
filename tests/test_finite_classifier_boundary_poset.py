from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_finite_classifier_boundary_poset() -> None:
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "verifier/verify_finite_classifier_boundary_poset.py"],
        cwd=root,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "FINITE_CLASSIFIER_BOUNDARY_POSET_OK" in result.stdout
