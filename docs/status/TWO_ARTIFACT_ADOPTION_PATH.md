
# Two-Artifact Adoption Path

This status anchor records one bounded two-artifact adoption path across two public repositories.

## Artifact 1: urf-templates

Purpose: stranger-runnable non-URF public entry artifact.

Repository:

```
https://github.com/inaciovasquez2020/urf-templates
```

Run only:

```
cd examples/non_urf_scientific_claim_demo
python3 tools/verify_ohms_law_fixed_observation_bound.py
python3 -m pytest tests/test_ohms_law_fixed_observation_bound.py -q
```

Expected:

```
NON_URF_OHMS_LAW_FIXED_OBSERVATION_BOUND_OK
1 passed
```

Boundary: this artifact checks a fixed Ohm observation-bound demo only. It does not claim scientific validation, external adoption, peer review, or general scientific truth.

## Artifact 2: theorem-closure-classifier

Purpose: stranger-runnable classification-boundary lock artifact.

Repository:

```
https://github.com/inaciovasquez2020/theorem-closure-classifier
```

Run only:

```
python3 verifier/verify_classification_boundary_lock.py
python3 -m pytest tests/test_classification_boundary_lock.py -q
```

Expected:

```
CLASSIFICATION_BOUNDARY_LOCK_OK
1 passed
```

Boundary: this artifact checks the repository classification-boundary lock only. It does not claim universal theorem closure, peer review, manuscript acceptance, external validation, or scientific validation.

## Combined clean-clone check

A bounded combined-path check consists only of cloning both repositories and running the two command pairs above.

Passing this path proves only that both public entry artifacts are clone-runnable in the tested environment. It does not prove external adoption, scientific validation, peer review, or correctness beyond the stated bounded checks.
