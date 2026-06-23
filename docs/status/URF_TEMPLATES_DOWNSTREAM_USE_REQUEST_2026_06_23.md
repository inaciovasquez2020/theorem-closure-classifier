# URF Templates Downstream Use Request

## Status

`DOWNSTREAM_USE_REQUEST_ONLY`

## Purpose

This document records one bounded downstream-use request for the `urf-templates`
five-minute verification path.

## Candidate downstream project

`theorem-closure-classifier`

Candidate use: consume the `urf-templates` non-URF scientific claim demo as a
bounded external adoption-surface input.

## Source project

`urf-templates`

Confirmed main commit:

```text
12ac5fe02b4bcd3f3b698a5ba86f48c8fbc2e9e7
Relevant surface:
claim -> artifact -> verifier -> boundary -> adoption note -> clean-clone confirmation -> README entry -> CI check -> final fresh clean-clone pass
Requested downstream check
A downstream evaluator should clone urf-templates at the confirmed commit,
run the README-linked verification path, run the targeted pytest check, and
record whether the surface is usable as a bounded external input.
Boundary
This is a downstream-use request only. It does not claim independent external
adoption, peer review, manuscript acceptance, scientific validation, new
physics, or satisfaction of theorem-closure-classifier adoption criteria.
Actual external adoption remains unclaimed until an independent user or project
uses the workflow.
Weakest gap
No independent user or project has yet used the urf-templates workflow as an
external input.
