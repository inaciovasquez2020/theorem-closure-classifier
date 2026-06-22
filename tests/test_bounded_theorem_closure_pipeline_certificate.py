import subprocess


def test_bounded_theorem_closure_pipeline_certificate():
    completed = subprocess.run(
        ["python3", "verifier/verify_bounded_theorem_closure_pipeline_certificate.py"],
        check=True,
        text=True,
        capture_output=True,
    )
    assert "BOUNDED_THEOREM_CLOSURE_PIPELINE_CERTIFICATE_OK" in completed.stdout
