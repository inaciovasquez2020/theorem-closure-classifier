from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/status/STL_SUBMODULE_COMPLETENESS_STATUS_2026_06_09.md"
ARTIFACT = ROOT / "artifacts/status/stl_submodule_completeness_status_2026_06_09.json"
VERIFIER = ROOT / "verifier/verify_stl_submodule_completeness_status.py"


def test_stl_submodule_completeness_status_verifier_passes() -> None:
    result = subprocess.run(
        ["python3", str(VERIFIER)],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    assert "STL_SUBMODULE_COMPLETENESS_STATUS_OK" in result.stdout


def test_stl_submodule_completeness_status_artifact_boundary() -> None:
    data = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    assert data["next_admissible_object"] == "STL_CHAIN_COHERENCE_LEMMA"
    assert data["completion_estimates"]["after_this_status_lock"] == "76-82%"
    assert "no solution-of-gravity claim" in data["boundary"]


def test_stl_submodule_completeness_status_doc_records_remaining_gaps() -> None:
    text = DOC.read_text(encoding="utf-8")
    assert "Remaining STL Gaps" in text
    assert "STL Chain-Coherence Lemma" in text
    assert "does not prove" in text
