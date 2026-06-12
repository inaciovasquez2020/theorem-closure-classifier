from __future__ import annotations

import subprocess
import sys


def test_iris_lean_full_context_mem_of_agree_replay_certificate() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "tools/verify_iris_lean_full_context_mem_of_agree_replay_certificate.py",
        ],
        check=True,
        text=True,
        capture_output=True,
    )
    assert "IRIS_LEAN_FULL_CONTEXT_MEM_OF_AGREE_REPLAY_CERTIFICATE_OK" in result.stdout
