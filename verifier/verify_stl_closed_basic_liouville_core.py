#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/status/STL_CLOSED_BASIC_LIOUVILLE_CORE_2026_06_09.md"
ARTIFACT = ROOT / "artifacts/status/stl_closed_basic_liouville_core_2026_06_09.json"

REQUIRED_DOC_SNIPPETS = [
    "Closed Basic Liouville Defect",
    "Endpoint-Closed Equivalence",
    "STL Core Metric-Symplectic Rigidity Theorem",
    "Action-neutrality is obsolete",
    "does not prove quantization",
    "does not prove quantization, the Einstein equations, empirical gravity, cosmology, unification, or quantum gravity",
    "\\Delta_{\\ell m}=0",
    "R_{\\ell m}^*\\lambda-\\lambda=\\pi_Q^*\\beta_{\\ell m}",
    "R_{\\ell m}^*\\Omega=\\Omega",
]

REQUIRED_ARTIFACT_KEYS = [
    "id",
    "date",
    "status",
    "primitive_admissibility_condition",
    "objects",
    "proved_claims",
    "obsolete",
    "boundary",
    "documents",
]

def main() -> None:
    if not DOC.exists():
        raise SystemExit(f"missing document: {DOC}")
    if not ARTIFACT.exists():
        raise SystemExit(f"missing artifact: {ARTIFACT}")

    doc_text = DOC.read_text(encoding="utf-8")
    missing = [snippet for snippet in REQUIRED_DOC_SNIPPETS if snippet not in doc_text]
    if missing:
        raise SystemExit(f"document missing required snippets: {missing}")

    data = json.loads(ARTIFACT.read_text(encoding="utf-8"))
    missing_keys = [key for key in REQUIRED_ARTIFACT_KEYS if key not in data]
    if missing_keys:
        raise SystemExit(f"artifact missing required keys: {missing_keys}")

    if data["id"] != "STL_CLOSED_BASIC_LIOUVILLE_CORE_2026_06_09":
        raise SystemExit("artifact id mismatch")

    if data["primitive_admissibility_condition"] != "closed_basic_liouville_defect":
        raise SystemExit("primitive admissibility condition mismatch")

    boundary = set(data["boundary"])
    required_boundary = {
        "no quantization claim",
        "no Einstein-equation claim",
        "no empirical-physics claim",
        "no cosmology claim",
        "no unification claim",
        "no quantum-gravity claim",
    }
    if not required_boundary.issubset(boundary):
        raise SystemExit("artifact boundary is incomplete")

    print("STL_CLOSED_BASIC_LIOUVILLE_CORE_OK")

if __name__ == "__main__":
    main()
