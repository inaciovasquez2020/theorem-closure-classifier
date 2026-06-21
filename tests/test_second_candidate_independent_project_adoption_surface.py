import subprocess
import sys


def test_second_candidate_independent_project_adoption_surface_verifier():
    result = subprocess.run(
        [
            sys.executable,
            "verifier/verify_second_candidate_independent_project_adoption_surface.py",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "SECOND_CANDIDATE_INDEPENDENT_PROJECT_ADOPTION_SURFACE_OK" in result.stdout
