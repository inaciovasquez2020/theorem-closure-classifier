from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts/external_validation/urf_templates_downstream_use_request_adoption_boundary_2026_06_23.json"
DOC = ROOT / "docs/status/URF_TEMPLATES_DOWNSTREAM_USE_REQUEST_ADOPTION_BOUNDARY.md"

REQUIRED_BOUNDARIES = {
    "does_not_claim_external_adoption",
    "does_not_claim_peer_review",
    "does_not_claim_independent_validation",
    "does_not_claim_universal_theorem_closure",
    "does_not_claim_mathematical_frontier_discharge",
}


def main() -> None:
    if not ARTIFACT.exists():
        raise SystemExit(f"MISSING_OBJECT := {ARTIFACT.relative_to(ROOT)}")
    if not DOC.exists():
        raise SystemExit(f"MISSING_OBJECT := {DOC.relative_to(ROOT)}")

    data = json.loads(ARTIFACT.read_text())
    if data.get("artifact_type") != "bounded_adoption_boundary_record":
        raise SystemExit("BOUNDARY := missing_bounded_adoption_boundary_record_type")

    boundaries = set(data.get("boundary", []))
    missing = REQUIRED_BOUNDARIES - boundaries
    if missing:
        raise SystemExit(f"BOUNDARY := missing_boundary_terms {sorted(missing)}")

    if "urf_templates_downstream_use_request" not in data.get("depends_on", []):
        raise SystemExit("BOUNDARY := missing_downstream_use_request_dependency")

    doc = DOC.read_text()
    required_doc_terms = [
        "external adoption",
        "peer review",
        "independent validation",
        "universal theorem closure",
        "mathematical frontier discharge",
        "URF_TEMPLATES_DOWNSTREAM_USE_REQUEST_ADOPTION_BOUNDARY_OK",
    ]
    for term in required_doc_terms:
        if term not in doc:
            raise SystemExit(f"BOUNDARY := missing_doc_term {term!r}")

    print("URF_TEMPLATES_DOWNSTREAM_USE_REQUEST_ADOPTION_BOUNDARY_OK")


if __name__ == "__main__":
    main()
