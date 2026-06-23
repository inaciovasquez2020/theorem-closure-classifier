import subprocess
import sys


def test_independent_project_usefulness_criterion_verifier():
    result = subprocess.run(
        [sys.executable, "verifier/verify_independent_project_usefulness_criterion.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "INDEPENDENT_PROJECT_USEFULNESS_CRITERION_OK" in result.stdout
