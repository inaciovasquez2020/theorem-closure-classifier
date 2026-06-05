# Verification-Governed Theorem Closure Classification

## Abstract

We introduce a verification-governed theorem closure classifier for auditing theorem-like mathematical claims. The classifier represents each claim by an explicit closure ledger containing a statement object, domain object, hypothesis object, construction object, obstruction object, proof-direction objects, dependency ledger, and boundary ledger. The classifier returns one of five statuses: complete unconditional ledger, complete conditional ledger, incomplete ledger, overclaimed ledger, or benchmark-match-only.

The method is tested against four positive controls from complete published theorem families: Hall's theorem on systems of distinct representatives, Kőnig's matching-cover theorem for finite bipartite graphs, the max-flow min-cut theorem, and Menger's path-separator theorem. It is also tested against three negative controls: an incomplete Hall claim missing the sufficiency direction, a conditional Banach fixed-point claim with an open completeness hypothesis, and an overclaimed finite-to-infinite Hall claim.

The control suite returns the expected classification in all seven cases. We prove syntactic soundness by expansion of the classifier rules and semantic soundness relative to a trusted proof-object verifier.

## 1. Ledger Objects

A theorem closure ledger contains:

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

## 2. Decision Rules

1. If the claimed conclusion strictly exceeds the proven conclusion, return `OVERCLAIMED_LEDGER`.
2. If the claim is only a recovery of an already-published benchmark theorem, return `BENCHMARK_MATCH_ONLY`.
3. If any required closure object is missing, return `INCOMPLETE_LEDGER`.
4. If any open hypothesis remains, return `COMPLETE_CONDITIONAL_LEDGER`.
5. If all required closure objects are present, no proof object is missing, no hypothesis remains open, and no overclaim is detected, return `COMPLETE_UNCONDITIONAL_LEDGER`.

## 3. Syntactic Soundness

If the classifier returns `COMPLETE_UNCONDITIONAL_LEDGER`, then all required ledger objects are present and no open hypothesis, missing proof object, or overclaim flag is active.

This follows by direct expansion of the classifier rule.

## 4. Relative Semantic Soundness

If the classifier returns `COMPLETE_UNCONDITIONAL_LEDGER` and a trusted proof-object verifier returns `VERIFIED` for the proof ledger, then the claim is complete and unconditional relative to that verifier.

## 5. Controls

The artifact includes four positive controls and three negative controls.

Expected output:

```text
7 / 7 controls pass
```

## 6. Boundary

This artifact does not claim new proofs of the benchmark theorems. The benchmark theorems are used as controls for the classification method.
