#!/usr/bin/env python3
import json
from pathlib import Path

artifact_path = Path("artifacts/external_validation/bounded_theorem_closure_pipeline_certificate_2026_06_22.json")
doc_path = Path("docs/status/BOUNDED_THEOREM_CLOSURE_PIPELINE_CERTIFICATE.md")

if not artifact_path.exists():
    raise SystemExit("MISSING_OBJECT := bounded theorem closure pipeline certificate artifact")

if not doc_path.exists():
    raise SystemExit("MISSING_OBJECT := bounded theorem closure pipeline certificate doc")

artifact = json.loads(artifact_path.read_text())

required_exact = {
    "artifact_name": "BOUNDED_THEOREM_CLOSURE_PIPELINE_CERTIFICATE",
    "status": "BOUNDED_THEOREM_CLOSURE_AUDIT_PIPELINE_WORKS_BEGINNING_TO_END",
    "claim": "bounded theorem-closure audit pipeline works beginning-to-end",
    "primary_object": "TheoremClosureClassifier_V1",
    "verifier_command": "python3 verifier/verify_bounded_theorem_closure_pipeline_certificate.py",
    "pytest_command": "python3 -m pytest -q tests/test_bounded_theorem_closure_pipeline_certificate.py",
}

for key, expected in required_exact.items():
    if artifact.get(key) != expected:
        raise SystemExit(f"MISSING_OBJECT := {key} == {expected!r}")

control_suite = artifact.get("control_suite", {})
if control_suite.get("name") != "7-control suite":
    raise SystemExit("MISSING_OBJECT := 7-control suite")
if control_suite.get("expected_status") != "7 / 7 controls pass":
    raise SystemExit("MISSING_OBJECT := 7 / 7 controls pass")

downstream = artifact.get("downstream_example", {})
if downstream.get("repository") != "cslib-fmt":
    raise SystemExit("MISSING_OBJECT := cslib-fmt downstream example")
if downstream.get("surface") != "distance/factorization surface":
    raise SystemExit("MISSING_OBJECT := cslib-fmt distance/factorization surface")

boundary = set(artifact.get("boundary_ledger", []))
for required in [
    "no unrestricted theorem closure claim",
    "no new benchmark theorem proof claim",
    "no global finite-model-theory closure claim",
    "no Clay-level closure claim",
]:
    if required not in boundary:
        raise SystemExit(f"MISSING_OBJECT := boundary ledger {required!r}")

doc = doc_path.read_text()
for needle in [
    "BOUNDED_THEOREM_CLOSURE_PIPELINE_CERTIFICATE",
    "bounded theorem-closure audit pipeline works beginning-to-end",
    "TheoremClosureClassifier_V1",
    "7-control suite",
    "python3 verifier/verify_bounded_theorem_closure_pipeline_certificate.py",
    "python3 -m pytest -q tests/test_bounded_theorem_closure_pipeline_certificate.py",
    "cslib-fmt distance/factorization surface",
    "no unrestricted theorem closure claim",
    "no new benchmark theorem proof claim",
    "no global finite-model-theory closure claim",
    "no Clay-level closure claim",
]:
    if needle not in doc:
        raise SystemExit(f"MISSING_OBJECT := doc contains {needle!r}")

print("BOUNDED_THEOREM_CLOSURE_PIPELINE_CERTIFICATE_OK")
