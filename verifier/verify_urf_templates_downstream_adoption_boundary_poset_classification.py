from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

POSET = ROOT / "artifacts/external_validation/finite_classifier_boundary_poset_2026_06_23.json"
SOURCE = ROOT / "artifacts/external_validation/urf_templates_downstream_use_request_adoption_boundary_2026_06_23.json"
CLASSIFICATION = ROOT / "artifacts/external_validation/urf_templates_downstream_adoption_boundary_poset_classification_2026_06_23.json"
DOC = ROOT / "docs/status/URF_TEMPLATES_DOWNSTREAM_ADOPTION_BOUNDARY_POSET_CLASSIFICATION.md"

EXPECTED_LEVEL = "verifier_backed_boundary"

REQUIRED_CLASSIFICATION_BOUNDARIES = {
    "does_not_claim_external_validation",
    "does_not_claim_peer_review",
    "does_not_claim_universal_theorem_closure",
    "does_not_change_source_artifact",
    "poset_level_assignment_only",
}


def load_json(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"MISSING_OBJECT := {path.relative_to(ROOT)}")
    return json.loads(path.read_text())


def main() -> None:
    poset = load_json(POSET)
    source = load_json(SOURCE)
    classification = load_json(CLASSIFICATION)

    if not DOC.exists():
        raise SystemExit(f"MISSING_OBJECT := {DOC.relative_to(ROOT)}")

    carrier = set(poset.get("finite_carrier", []))
    if EXPECTED_LEVEL not in carrier:
        raise SystemExit("BOUNDARY := expected_level_not_in_poset_carrier")

    if classification.get("artifact_type") != "bounded_poset_artifact_classification":
        raise SystemExit("BOUNDARY := missing_bounded_poset_artifact_classification_type")

    if classification.get("classifier_poset_dependency") != poset.get("id"):
        raise SystemExit("BOUNDARY := wrong_poset_dependency")

    if classification.get("classified_artifact") != source.get("id"):
        raise SystemExit("BOUNDARY := wrong_classified_artifact")

    if classification.get("classification_level") != EXPECTED_LEVEL:
        raise SystemExit("BOUNDARY := wrong_classification_level")

    source_verifier = source.get("verifier")
    source_test = source.get("targeted_test")
    if not source_verifier or not (ROOT / source_verifier).exists():
        raise SystemExit("BOUNDARY := missing_source_verifier")
    if not source_test or not (ROOT / source_test).exists():
        raise SystemExit("BOUNDARY := missing_source_targeted_test")

    source_boundaries = set(source.get("boundary", []))
    for term in [
        "does_not_claim_external_adoption",
        "does_not_claim_independent_validation",
    ]:
        if term not in source_boundaries:
            raise SystemExit(f"BOUNDARY := missing_source_boundary {term}")

    classification_boundaries = set(classification.get("boundary", []))
    missing = REQUIRED_CLASSIFICATION_BOUNDARIES - classification_boundaries
    if missing:
        raise SystemExit(f"BOUNDARY := missing_classification_boundary_terms {sorted(missing)}")

    if classification.get("classification_level") == "externally_validated_use":
        raise SystemExit("BOUNDARY := forbidden_external_validation_classification")

    doc = DOC.read_text()
    for term in [
        "verifier_backed_boundary",
        "does not claim",
        "external validation",
        "finite poset level assignment",
        "URF_TEMPLATES_DOWNSTREAM_ADOPTION_BOUNDARY_POSET_CLASSIFICATION_OK",
    ]:
        if term not in doc:
            raise SystemExit(f"BOUNDARY := missing_doc_term {term!r}")

    print("URF_TEMPLATES_DOWNSTREAM_ADOPTION_BOUNDARY_POSET_CLASSIFICATION_OK")


if __name__ == "__main__":
    main()
