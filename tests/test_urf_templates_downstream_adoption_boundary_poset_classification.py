from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_urf_templates_downstream_adoption_boundary_poset_classification() -> None:
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "verifier/verify_urf_templates_downstream_adoption_boundary_poset_classification.py"],
        cwd=root,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "URF_TEMPLATES_DOWNSTREAM_ADOPTION_BOUNDARY_POSET_CLASSIFICATION_OK" in result.stdout
