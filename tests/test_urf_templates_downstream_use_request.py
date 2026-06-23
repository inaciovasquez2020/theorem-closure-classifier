import subprocess
import sys


def test_urf_templates_downstream_use_request_verifier():
    result = subprocess.run(
        [sys.executable, "verifier/verify_urf_templates_downstream_use_request.py"],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "URF_TEMPLATES_DOWNSTREAM_USE_REQUEST_OK" in result.stdout
