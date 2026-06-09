# STL Closed-Basic Liouville Transition Classification Target

## Status

Bounded STL transition-classification theorem target.

This document closes the next admissible object recorded by:

STL_CHAIN_COHERENCE_LEMMA_2026_06_09

## Dependencies

STL_CLOSED_BASIC_LIOUVILLE_CORE_2026_06_09

STL_SUBMODULE_COMPLETENESS_STATUS_2026_06_09

STL_CHAIN_COHERENCE_LEMMA_2026_06_09

## Standing Setup

Let

\[
Q:=\mathrm{Riem}(\Sigma),
\qquad
\Gamma:=T^*Q,
\qquad
\pi_Q:\Gamma\to Q.
\]

Let

\[
\lambda\in\Omega^1(\Gamma)
\]

be the canonical Liouville one-form,

\[
\lambda_{(q,p)}(V):=p(d\pi_Q(V)).
\]

Let

\[
\Omega:=-d\lambda.
\]

Let

\[
B:Q\to Q
\]

be a diffeomorphism.

## Base-Projectable Transition

A transition

\[
R:\Gamma\to\Gamma
\]

is base-projectable over \(B\) if

\[
\pi_Q\circ R=B\circ \pi_Q.
\]

Equivalently, there exists a smooth fiber map \(F\) such that

\[
R(q,p)=(B(q),F(q,p)).
\]

## Closed Basic Liouville Defect

The transition \(R\) has closed basic Liouville defect if there exists

\[
\beta\in\Omega^1(Q)
\]

such that

\[
R^*\lambda-\lambda=\pi_Q^*\beta,
\qquad
d\beta=0.
\]

## Forward Cotangent Lift

Define

\[
B^\sharp:T^*Q\to T^*Q
\]

by

\[
B^\sharp(q,p)
=
\left(
B(q),
(DB_q^{-1})^*p
\right).
\]

This is the forward cotangent lift of \(B\).

## Fiber Translation

For

\[
\gamma\in\Omega^1(Q),
\]

define

\[
\tau_\gamma:T^*Q\to T^*Q
\]

by

\[
\tau_\gamma(q,p):=(q,p+\gamma_q).
\]

## Theorem: STL Closed-Basic Liouville Transition Classification

Let

\[
R:T^*Q\to T^*Q
\]

be base-projectable over a diffeomorphism

\[
B:Q\to Q.
\]

Assume

\[
R^*\lambda-\lambda=\pi_Q^*\beta
\]

for some

\[
\beta\in\Omega^1(Q).
\]

Then

\[
R(q,p)
=
\left(
B(q),
(DB_q^{-1})^*(p+\beta_q)
\right).
\]

Equivalently,

\[
R=\tau_\gamma\circ B^\sharp,
\]

where

\[
\gamma=(B^{-1})^*\beta.
\]

If additionally

\[
d\beta=0,
\]

then

\[
R^*\Omega=\Omega.
\]

## Proof

Since \(R\) is base-projectable over \(B\), write

\[
R(q,p)=(B(q),F(q,p))
\]

with

\[
F(q,p)\in T^*_{B(q)}Q.
\]

Let

\[
V\in T_{(q,p)}T^*Q.
\]

By definition of \(\lambda\),

\[
(R^*\lambda)_{(q,p)}(V)
=
\lambda_{R(q,p)}(dR(V)).
\]

Since

\[
R(q,p)=(B(q),F(q,p)),
\]

we have

\[
\lambda_{R(q,p)}(dR(V))
=
F(q,p)\bigl(d\pi_Q(dR(V))\bigr).
\]

Because

\[
\pi_Q\circ R=B\circ\pi_Q,
\]

we obtain

\[
d\pi_Q(dR(V))
=
DB_q(d\pi_Q(V)).
\]

Thus

\[
(R^*\lambda)_{(q,p)}(V)
=
F(q,p)\bigl(DB_q(d\pi_Q(V))\bigr).
\]

The identity

\[
R^*\lambda-\lambda=\pi_Q^*\beta
\]

gives

\[
F(q,p)\bigl(DB_q(d\pi_Q(V))\bigr)
-
p(d\pi_Q(V))
=
\beta_q(d\pi_Q(V)).
\]

Set

\[
\xi:=d\pi_Q(V)\in T_qQ.
\]

Then

\[
F(q,p)(DB_q\xi)-p(\xi)=\beta_q(\xi)
\]

for every

\[
\xi\in T_qQ.
\]

Hence

\[
F(q,p)(DB_q\xi)=(p+\beta_q)(\xi).
\]

Since \(B\) is a diffeomorphism,

\[
F(q,p)=(DB_q^{-1})^*(p+\beta_q).
\]

Therefore

\[
R(q,p)
=
\left(
B(q),
(DB_q^{-1})^*(p+\beta_q)
\right).
\]

Now assume

\[
d\beta=0.
\]

Then

\[
R^*\Omega
=
R^*(-d\lambda)
=
-d(R^*\lambda)
=
-d(\lambda+\pi_Q^*\beta)
=
-d\lambda-\pi_Q^*(d\beta)
=
\Omega.
\]

Thus

\[
R^*\Omega=\Omega.
\]

\[
\square
\]

## Converse Direction

If

\[
R(q,p)
=
\left(
B(q),
(DB_q^{-1})^*(p+\beta_q)
\right),
\]

then direct substitution gives

\[
R^*\lambda-\lambda=\pi_Q^*\beta.
\]

If

\[
d\beta=0,
\]

then

\[
R^*\Omega=\Omega.
\]

Thus base-projectable closed-basic Liouville transitions are exactly affine cotangent-lift transitions with closed basic translation term.

## What This Closes

This closes the bounded classification target:

\[
\boxed{
\text{base-projectable closed-basic Liouville transition}
=
\text{closed affine cotangent-lift transition}.
}
\]

## What It Does Not Close

This theorem does not classify arbitrary smooth maps

\[
R:T^*Q\to T^*Q
\]

without base-projectability.

It does not prove:

- quantum gravity,
- canonical quantization,
- Einstein equations,
- empirical gravity,
- cosmology,
- unification,
- a physical theory of spacetime,
- or a solution of gravity.

It is only a bounded transition-classification theorem inside the STL formalism.
