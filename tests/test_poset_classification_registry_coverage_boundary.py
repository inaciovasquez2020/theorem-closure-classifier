import subprocess
import sys
from pathlib import Path

def test_poset_classification_registry_coverage_boundary():
    result = subprocess.run(
        [sys.executable, "verifier/verify_poset_classification_registry_coverage_boundary.py"],
        cwd=Path.cwd(),
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "POSET_CLASSIFICATION_REGISTRY_COVERAGE_BOUNDARY_OK" in result.stdout
