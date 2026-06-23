import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / "verifier" / "verify_poset_classification_registry_schema_contract.py"


def test_poset_classification_registry_schema_contract() -> None:
    result = subprocess.run(
        [sys.executable, str(VERIFIER)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert "POSET_CLASSIFICATION_REGISTRY_SCHEMA_CONTRACT_OK" in result.stdout
