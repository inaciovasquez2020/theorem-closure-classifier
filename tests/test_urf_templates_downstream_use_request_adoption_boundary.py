from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_urf_templates_downstream_use_request_adoption_boundary() -> None:
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "verifier/verify_urf_templates_downstream_use_request_adoption_boundary.py"],
        cwd=root,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "URF_TEMPLATES_DOWNSTREAM_USE_REQUEST_ADOPTION_BOUNDARY_OK" in result.stdout
