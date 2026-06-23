import subprocess


def test_cslib_fmt_signal_classifier_sync():
    subprocess.run(
        [
            "python3",
            "-B",
            "verifier/verify_cslib_fmt_signal_classifier_sync.py",
        ],
        check=True,
    )
