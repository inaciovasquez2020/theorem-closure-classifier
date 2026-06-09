#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/status/STL_CLOSED_BASIC_LIOUVILLE_TRANSITION_CLASSIFICATION_TARGET_2026_06_09.md"
ARTIFACT = ROOT / "artifacts/status/stl_closed_basic_liouville_transition_classification_target_2026_06_09.json"

REQUIRED_DOC_SNIPPETS = [
    "STL Closed-Basic Liouville Transition Classification Target",
    "STL_CHAIN_COHERENCE_LEMMA_2026_06_09",
    "base-projectable over",
    "closed basic Liouville defect",
    "R^*\\lambda-\\lambda=\\pi_Q^*\\beta",
    "R(q,p)",
    "(DB_q^{-1})^*(p+\\beta_q)",
    "R^*\\Omega=\\Omega",
    "does not classify arbitrary smooth maps",
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

    if data.get("id") != "STL_CLOSED_BASIC_LIOUVILLE_TRANSITION_CLASSIFICATION_TARGET_2026_06_09":
        raise SystemExit("artifact id mismatch")

    if data.get("closed_object") != "STL_CLOSED_BASIC_LIOUVILLE_TRANSITION_CLASSIFICATION_TARGET":
        raise SystemExit("closed object mismatch")

    deps = set(data.get("depends_on", []))
    required_deps = {
        "STL_CLOSED_BASIC_LIOUVILLE_CORE_2026_06_09",
        "STL_SUBMODULE_COMPLETENESS_STATUS_2026_06_09",
        "STL_CHAIN_COHERENCE_LEMMA_2026_06_09"
    }
    if not required_deps.issubset(deps):
        raise SystemExit("dependency set incomplete")

    if data.get("stl_completion_after") != "84-88%":
        raise SystemExit("STL completion estimate mismatch")

    if data.get("next_admissible_object") != "STL_ADM_CONSTRAINT_SURFACE_INTERACTION_TARGET":
        raise SystemExit("next admissible object mismatch")

    boundary = set(data.get("boundary", []))
    if not REQUIRED_BOUNDARY.issubset(boundary):
        raise SystemExit("boundary incomplete")

    print("STL_CLOSED_BASIC_LIOUVILLE_TRANSITION_CLASSIFICATION_TARGET_OK")

if __name__ == "__main__":
    main()
