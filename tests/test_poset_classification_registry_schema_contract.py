import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / "verifier" / "verify_poset_classification_registry_schema_contract.py"
REGISTRY = ROOT / "artifacts/external_validation/poset_classification_registry_consistency_2026_06_23.json"


def registry_entries(data: dict[str, Any]) -> list[dict[str, Any]]:
    for value in data.values():
        if (
            isinstance(value, list)
            and value
            and all(isinstance(entry, dict) for entry in value)
            and all("artifact_id" in entry for entry in value)
            and all("artifact_path" in entry for entry in value)
        ):
            return value
    raise AssertionError("MISSING_OBJECT := registry entry list")


def run_verifier() -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VERIFIER)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def test_poset_classification_registry_schema_contract() -> None:
    result = run_verifier()

    assert result.returncode == 0, result.stderr
    assert "POSET_CLASSIFICATION_REGISTRY_SCHEMA_CONTRACT_OK" in result.stdout


def test_poset_classification_registry_schema_contract_rejects_missing_required_key() -> None:
    original = REGISTRY.read_text(encoding="utf-8")
    try:
        data = json.loads(original)
        entries = registry_entries(data)
        del entries[0]["reason"]
        REGISTRY.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

        result = run_verifier()

        assert result.returncode != 0
        assert "BOUNDARY := registry_entry_shape_not_exact" in result.stderr
    finally:
        REGISTRY.write_text(original, encoding="utf-8")


def test_poset_classification_registry_schema_contract_rejects_extra_key() -> None:
    original = REGISTRY.read_text(encoding="utf-8")
    try:
        data = json.loads(original)
        entries = registry_entries(data)
        entries[0]["extra_schema_key"] = "forbidden"
        REGISTRY.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

        result = run_verifier()

        assert result.returncode != 0
        assert "BOUNDARY := registry_entry_shape_not_exact" in result.stderr
    finally:
        REGISTRY.write_text(original, encoding="utf-8")
