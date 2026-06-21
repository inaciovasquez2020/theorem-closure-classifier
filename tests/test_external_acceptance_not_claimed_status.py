import subprocess
import sys


def test_external_acceptance_not_claimed_status_verifier():
    result = subprocess.run(
        [sys.executable, "verifier/verify_external_acceptance_not_claimed_status.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "EXTERNAL_ACCEPTANCE_NOT_CLAIMED_STATUS_OK" in result.stdout
