# Theorem Closure Classifier

`TheoremClosureClassifier_V1` is a verification-governed closure-audit method for theorem-like mathematical claims.

## Classifications

- `COMPLETE_UNCONDITIONAL_LEDGER`
- `COMPLETE_CONDITIONAL_LEDGER`
- `INCOMPLETE_LEDGER`
- `OVERCLAIMED_LEDGER`
- `BENCHMARK_MATCH_ONLY`

## Core Claim

A theorem-like claim can be audited by checking whether its closure ledger contains:

- exact statement object
- domain object
- hypothesis object
- construction object
- obstruction object
- necessity-direction object
- sufficiency-direction object
- boundary object
- proof ledger
- dependency ledger
- claim-boundary ledger

## Controls

Positive controls:

1. Hall systems of distinct representatives theorem
2. Kőnig bipartite matching-vertex-cover theorem
3. Max-flow min-cut theorem
4. Menger path-separator theorem

Negative controls:

1. incomplete Hall claim
2. conditional Banach fixed-point claim
3. overclaimed finite-to-infinite Hall claim

## Run

```bash
python -m pytest -q
python verifier/run_controls.py
```

Expected:

```text
7 / 7 controls pass
```

## Boundary

This repository does not claim new proofs of Hall, Kőnig, max-flow min-cut, Menger, or Banach fixed-point theorems.

The contribution is the closure-classification method and control-suite audit structure.

## Using the Classifier Decision Surface in a Bounded Project

`ClassifierDecisionSurface` is a bounded theorem-status artifact. It records a fixed decision surface inside this repository.

A downstream project may adopt the pattern by using:

| Surface | Status record | Artifact | Verifier | Regression |
|---|---|---|---|---|
| `ClassifierDecisionSurface` | `docs/status/CLASSIFIER_DECISION_SURFACE_2026_06_09.md` | `artifacts/status/classifier_decision_surface_2026_06_09.json` | `verifier/verify_classifier_decision_surface.py` | `tests/test_classifier_decision_surface.py` |

Filenames are date-stamped to the closure date; do not update them in place. Create a new artifact instead.

Minimal verification command:

```bash
python3 verifier/verify_classifier_decision_surface.py
python3 -m pytest -q tests/test_classifier_decision_surface.py
```

Boundary: this artifact does not prove unrestricted theorem closure, scientific closure, peer review, manuscript acceptance, or external validation. It is only a closed bounded status surface for the definitions and artifacts recorded in this repository.
