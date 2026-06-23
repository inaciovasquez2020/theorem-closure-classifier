import subprocess
import sys


def test_candidate_independent_project_adoption_surface_verifier():
    result = subprocess.run(
        [sys.executable, "verifier/verify_candidate_independent_project_adoption_surface.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "CANDIDATE_INDEPENDENT_PROJECT_ADOPTION_SURFACE_OK" in result.stdout
