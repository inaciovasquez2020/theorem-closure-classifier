from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_poset_classification_registry_consistency() -> None:
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "verifier/verify_poset_classification_registry_consistency.py"],
        cwd=root,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "POSET_CLASSIFICATION_REGISTRY_CONSISTENCY_OK" in result.stdout
