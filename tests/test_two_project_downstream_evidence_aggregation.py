import subprocess
import sys


def test_two_project_downstream_evidence_aggregation_verifier():
    result = subprocess.run(
        [
            sys.executable,
            "verifier/verify_two_project_downstream_evidence_aggregation.py",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "TWO_PROJECT_DOWNSTREAM_EVIDENCE_AGGREGATION_OK" in result.stdout
