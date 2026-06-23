from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REGISTRY = ROOT / "artifacts/external_validation/poset_classification_registry_consistency_2026_06_23.json"
POSET = ROOT / "artifacts/external_validation/finite_classifier_boundary_poset_2026_06_23.json"
DOC = ROOT / "docs/status/POSET_CLASSIFICATION_REGISTRY_CONSISTENCY.md"

REQUIRED_BOUNDARIES = {
    "does_not_claim_external_validation",
    "does_not_claim_peer_review",
    "does_not_claim_universal_theorem_closure",
    "does_not_claim_complete_registry",
    "finite_registry_consistency_only",
}


def load_json(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"MISSING_OBJECT := {path.relative_to(ROOT)}")
    return json.loads(path.read_text())


def main() -> None:
    registry = load_json(REGISTRY)
    poset = load_json(POSET)

    if not DOC.exists():
        raise SystemExit(f"MISSING_OBJECT := {DOC.relative_to(ROOT)}")

    if registry.get("artifact_type") != "bounded_poset_classification_registry_consistency_certificate":
        raise SystemExit("BOUNDARY := wrong_registry_artifact_type")

    if registry.get("classifier_poset_dependency") != poset.get("id"):
        raise SystemExit("BOUNDARY := wrong_poset_dependency")

    carrier = set(poset.get("finite_carrier", []))
    if not carrier:
        raise SystemExit("BOUNDARY := empty_poset_carrier")

    entries = registry.get("registered_classifications")
    if not isinstance(entries, list) or len(entries) < 2:
        raise SystemExit("BOUNDARY := registry_requires_at_least_two_entries")

    seen_ids: set[str] = set()
    for entry in entries:
        artifact_id = entry.get("artifact_id")
        artifact_path = entry.get("artifact_path")
        level = entry.get("classification_level")

        if not artifact_id or not artifact_path or not level:
            raise SystemExit("BOUNDARY := malformed_registry_entry")

        if artifact_id in seen_ids:
            raise SystemExit(f"BOUNDARY := duplicate_registry_entry {artifact_id}")
        seen_ids.add(artifact_id)

        if level not in carrier:
            raise SystemExit(f"BOUNDARY := classification_level_not_in_poset {artifact_id} {level}")

        if level == "externally_validated_use":
            raise SystemExit(f"BOUNDARY := forbidden_external_validation_level {artifact_id}")

        artifact = load_json(ROOT / artifact_path)
        if artifact.get("id") != artifact_id:
            raise SystemExit(f"BOUNDARY := artifact_id_path_mismatch {artifact_id}")

        verifier = artifact.get("verifier")
        targeted_test = artifact.get("targeted_test")
        if not verifier or not (ROOT / verifier).exists():
            raise SystemExit(f"BOUNDARY := missing_artifact_verifier {artifact_id}")
        if not targeted_test or not (ROOT / targeted_test).exists():
            raise SystemExit(f"BOUNDARY := missing_artifact_targeted_test {artifact_id}")

    boundaries = set(registry.get("boundary", []))
    missing = REQUIRED_BOUNDARIES - boundaries
    if missing:
        raise SystemExit(f"BOUNDARY := missing_registry_boundary_terms {sorted(missing)}")

    doc = DOC.read_text()
    for term in [
        "finite registry consistency certificate",
        "verifier_backed_boundary",
        "does not claim",
        "complete registry coverage",
        "POSET_CLASSIFICATION_REGISTRY_CONSISTENCY_OK",
    ]:
        if term not in doc:
            raise SystemExit(f"BOUNDARY := missing_doc_term {term!r}")

    print("POSET_CLASSIFICATION_REGISTRY_CONSISTENCY_OK")


if __name__ == "__main__":
    main()
