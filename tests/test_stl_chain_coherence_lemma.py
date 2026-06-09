from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/status/STL_CHAIN_COHERENCE_LEMMA_2026_06_09.md"
ARTIFACT = ROOT / "artifacts/status/stl_chain_coherence_lemma_2026_06_09.json"
VERIFIER = ROOT / "verifier/verify_stl_chain_coherence_lemma.py"


def test_stl_chain_coherence_lemma_verifier_passes() -> None:
    result = subprocess.run(
        ["python3", str(VERIFIER)],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    assert "STL_CHAIN_COHERENCE_LEMMA_OK" in result.stdout


def test_stl_chain_coherence_lemma_artifact_records_closure() -> None:
    data = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    assert data["closed_object"] == "STL_CHAIN_COHERENCE_LEMMA"
    assert data["stl_completion_after"] == "80-85%"
    assert data["next_admissible_object"] == "STL_CLOSED_BASIC_LIOUVILLE_TRANSITION_CLASSIFICATION_TARGET"
    assert "no solution-of-gravity claim" in data["boundary"]


def test_stl_chain_coherence_lemma_doc_records_theorem_and_boundary() -> None:
    text = DOC.read_text(encoding="utf-8")
    assert "STL Chain-Coherence Lemma" in text
    assert "Global Chain Closure" in text
    assert "T_{\\ell n}=T_{mn}\\circ T_{\\ell m}" in text
    assert "does not prove" in text
