from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/status/STL_CLOSED_BASIC_LIOUVILLE_CORE_2026_06_09.md"
ARTIFACT = ROOT / "artifacts/status/stl_closed_basic_liouville_core_2026_06_09.json"
VERIFIER = ROOT / "verifier/verify_stl_closed_basic_liouville_core.py"


def test_stl_closed_basic_liouville_core_verifier_passes() -> None:
    result = subprocess.run(
        ["python3", str(VERIFIER)],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    assert "STL_CLOSED_BASIC_LIOUVILLE_CORE_OK" in result.stdout


def test_stl_closed_basic_liouville_core_artifact_boundary() -> None:
    data = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    assert data["primitive_admissibility_condition"] == "closed_basic_liouville_defect"
    assert "action-neutrality as primitive STL admissibility condition" in data["obsolete"]
    assert "no quantum-gravity claim" in data["boundary"]


def test_stl_closed_basic_liouville_core_doc_contains_core_theorem() -> None:
    text = DOC.read_text(encoding="utf-8")
    assert "STL Core Metric-Symplectic Rigidity Theorem" in text
    assert "Endpoint-Closed Equivalence" in text
    assert "Action-neutrality is obsolete" in text
    assert "closed basic Liouville defect" in text
