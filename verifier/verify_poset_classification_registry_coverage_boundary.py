import json
from pathlib import Path

ROOT = Path.cwd()
CERT = ROOT / "artifacts/external_validation/poset_classification_registry_coverage_boundary_2026_06_23.json"
REGISTRY = ROOT / "artifacts/external_validation/poset_classification_registry_consistency_2026_06_23.json"
POSET = ROOT / "artifacts/external_validation/finite_classifier_boundary_poset_2026_06_23.json"
DOC = ROOT / "docs/status/POSET_CLASSIFICATION_REGISTRY_COVERAGE_BOUNDARY.md"

for path in [CERT, REGISTRY, POSET, DOC]:
    if not path.exists():
        raise SystemExit(f"MISSING_OBJECT := {path.relative_to(ROOT)}")

cert = json.loads(CERT.read_text())
registry = json.loads(REGISTRY.read_text())
poset = json.loads(POSET.read_text())
doc = DOC.read_text()

if cert.get("artifact_type") != "bounded_registry_coverage_boundary_certificate":
    raise SystemExit("BOUNDARY := wrong_certificate_type")
if cert.get("registry_dependency") != registry.get("id"):
    raise SystemExit("BOUNDARY := wrong_registry_dependency")
if cert.get("classifier_poset_dependency") != poset.get("id"):
    raise SystemExit("BOUNDARY := wrong_poset_dependency")
if cert.get("coverage_status") != "partial_registry_only":
    raise SystemExit("BOUNDARY := wrong_coverage_status")
if cert.get("minimum_registered_artifacts_checked") != 2:
    raise SystemExit("BOUNDARY := wrong_minimum_registered_artifacts_checked")

entries = registry.get("registered_classifications", [])
if not isinstance(entries, list) or len(entries) < 2:
    raise SystemExit("BOUNDARY := registry_has_too_few_entries")

if "does_not_claim_complete_registry" not in set(registry.get("boundary", [])):
    raise SystemExit("BOUNDARY := dependency_missing_complete_registry_boundary")

required = {
    "does_not_claim_complete_registry",
    "does_not_claim_all_artifacts_classified",
    "does_not_claim_external_validation",
    "does_not_claim_peer_review",
    "does_not_claim_universal_theorem_closure",
    "coverage_boundary_only",
}
if not required <= set(cert.get("boundary", [])):
    raise SystemExit("BOUNDARY := missing_certificate_boundary_terms")

if cert.get("coverage_status") == "complete_registry":
    raise SystemExit("BOUNDARY := forbidden_complete_registry_status")
if "externally_validated_use" in cert.get("positive_claim", ""):
    raise SystemExit("BOUNDARY := forbidden_external_validation_claim")

for term in [
    "intentionally partial",
    "does not claim",
    "complete registry coverage",
    "all artifacts classified",
    "POSET_CLASSIFICATION_REGISTRY_COVERAGE_BOUNDARY_OK",
]:
    if term not in doc:
        raise SystemExit(f"BOUNDARY := missing_doc_term {term!r}")

print("POSET_CLASSIFICATION_REGISTRY_COVERAGE_BOUNDARY_OK")
