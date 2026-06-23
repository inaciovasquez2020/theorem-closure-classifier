from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "artifacts/external_validation/finite_classifier_boundary_poset_2026_06_23.json"
DOC = ROOT / "docs/status/FINITE_CLASSIFIER_BOUNDARY_POSET.md"

REQUIRED_BOUNDARIES = {
    "does_not_classify_all_repositories",
    "does_not_claim_external_validation_for_any_project",
    "does_not_claim_universal_theorem_closure",
    "does_not_discharge_any_mathematical_frontier",
    "finite_certificate_only",
}


def transitive_closure(carrier: set[str], edges: Iterable[tuple[str, str]]) -> set[tuple[str, str]]:
    relation = {(x, x) for x in carrier}
    relation.update(edges)

    changed = True
    while changed:
        changed = False
        new_pairs = set(relation)
        for a, b in relation:
            for c, d in relation:
                if b == c and (a, d) not in new_pairs:
                    new_pairs.add((a, d))
                    changed = True
        relation = new_pairs

    return relation


def main() -> None:
    if not ARTIFACT.exists():
        raise SystemExit(f"MISSING_OBJECT := {ARTIFACT.relative_to(ROOT)}")
    if not DOC.exists():
        raise SystemExit(f"MISSING_OBJECT := {DOC.relative_to(ROOT)}")

    data = json.loads(ARTIFACT.read_text())
    if data.get("artifact_type") != "bounded_finite_mathematical_certificate":
        raise SystemExit("BOUNDARY := missing_bounded_finite_mathematical_certificate_type")

    carrier = set(data.get("finite_carrier", []))
    if not carrier:
        raise SystemExit("BOUNDARY := empty_finite_carrier")

    edge_pairs = [tuple(edge) for edge in data.get("order_edges", [])]
    for edge in edge_pairs:
        if len(edge) != 2:
            raise SystemExit(f"BOUNDARY := malformed_edge {edge!r}")
        a, b = edge
        if a not in carrier or b not in carrier:
            raise SystemExit(f"BOUNDARY := edge_outside_carrier {edge!r}")
        if a == b:
            raise SystemExit(f"BOUNDARY := non_strict_declared_edge {edge!r}")

    relation = transitive_closure(carrier, edge_pairs)

    for x in carrier:
        if (x, x) not in relation:
            raise SystemExit(f"BOUNDARY := non_reflexive_closure_at {x!r}")

    for a, b in relation:
        if a != b and (b, a) in relation:
            raise SystemExit(f"BOUNDARY := antisymmetry_failure {(a, b)!r}")

    for a, b in relation:
        for c, d in relation:
            if b == c and (a, d) not in relation:
                raise SystemExit(f"BOUNDARY := transitivity_failure {(a, b, d)!r}")

    least = "no_claim"
    greatest = "externally_validated_use"
    if least not in carrier or greatest not in carrier:
        raise SystemExit("BOUNDARY := missing_declared_extreme_element")

    for x in carrier:
        if (least, x) not in relation:
            raise SystemExit(f"BOUNDARY := least_element_failure {x!r}")
        if (x, greatest) not in relation:
            raise SystemExit(f"BOUNDARY := greatest_element_failure {x!r}")

    boundaries = set(data.get("boundary", []))
    missing = REQUIRED_BOUNDARIES - boundaries
    if missing:
        raise SystemExit(f"BOUNDARY := missing_boundary_terms {sorted(missing)}")

    doc = DOC.read_text()
    for term in [
        "partial order",
        "least element",
        "greatest element",
        "finite certificate only",
        "FINITE_CLASSIFIER_BOUNDARY_POSET_OK",
    ]:
        if term not in doc:
            raise SystemExit(f"BOUNDARY := missing_doc_term {term!r}")

    print("FINITE_CLASSIFIER_BOUNDARY_POSET_OK")


if __name__ == "__main__":
    main()
