#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/status/STL_SUBMODULE_COMPLETENESS_STATUS_2026_06_09.md"
ARTIFACT = ROOT / "artifacts/status/stl_submodule_completeness_status_2026_06_09.json"

REQUIRED_DOC_SNIPPETS = [
    "STL Submodule Completeness Status",
    "STL_CLOSED_BASIC_LIOUVILLE_CORE_2026_06_09",
    "76\\%-82\\%",
    "STL Chain-Coherence Lemma",
    "does not prove",
    "solution of gravity"
]

REQUIRED_BOUNDARY = {
    "no quantum-gravity claim",
    "no canonical-quantization claim",
    "no Einstein-equation claim",
    "no empirical-gravity claim",
    "no cosmology claim",
    "no unification claim",
    "no physical-theory claim",
    "no solution-of-gravity claim"
}

def main() -> None:
    if not DOC.exists():
        raise SystemExit(f"missing document: {DOC}")
    if not ARTIFACT.exists():
        raise SystemExit(f"missing artifact: {ARTIFACT}")

    text = DOC.read_text(encoding="utf-8")
    missing = [s for s in REQUIRED_DOC_SNIPPETS if s not in text]
    if missing:
        raise SystemExit(f"document missing required snippets: {missing}")

    data = json.loads(ARTIFACT.read_text(encoding="utf-8"))

    if data.get("id") != "STL_SUBMODULE_COMPLETENESS_STATUS_2026_06_09":
        raise SystemExit("artifact id mismatch")

    if data.get("next_admissible_object") != "STL_CHAIN_COHERENCE_LEMMA":
        raise SystemExit("next admissible object mismatch")

    if "STL_CLOSED_BASIC_LIOUVILLE_CORE_2026_06_09" not in data.get("depends_on", []):
        raise SystemExit("missing dependency on closed STL core")

    boundary = set(data.get("boundary", []))
    if not REQUIRED_BOUNDARY.issubset(boundary):
        raise SystemExit("boundary incomplete")

    estimates = data.get("completion_estimates", {})
    if estimates.get("after_this_status_lock") != "76-82%":
        raise SystemExit("completion estimate mismatch")

    print("STL_SUBMODULE_COMPLETENESS_STATUS_OK")

if __name__ == "__main__":
    main()
