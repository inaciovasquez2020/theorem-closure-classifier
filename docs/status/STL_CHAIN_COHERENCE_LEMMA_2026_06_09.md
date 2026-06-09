# STL Chain-Coherence Lemma

## Status

Bounded STL chain-coherence theorem.

This document closes the next admissible object recorded by:

\[
\mathrm{STL\_SUBMODULE\_COMPLETENESS\_STATUS\_2026\_06\_09}.
\]

## Dependency

STL_SUBMODULE_COMPLETENESS_STATUS_2026_06_09

## Dependency

\[
\mathrm{STL\_CLOSED\_BASIC\_LIOUVILLE\_CORE\_2026\_06\_09}
\]

\[
\mathrm{STL\_SUBMODULE\_COMPLETENESS\_STATUS\_2026\_06\_09}
\]

## Standing Setup

Let

\[
\Sigma
\]

be a compact boundaryless smooth \(3\)-manifold.

Let

\[
\mathcal D:=C^\infty(\Sigma)\oplus\mathfrak X(\Sigma).
\]

For a Riemannian metric \(h\), define the ADM descriptor bracket

\[
[(N,X),(M,Y)]_h
:=
\left(
X(M)-Y(N),
\ [X,Y]+h^{-1}(N\,dM-M\,dN)
\right).
\]

For comparable layers

\[
\ell\preceq m,
\]

let

\[
T_{\ell m}:\mathcal D\to\mathcal D
\]

be descriptor transport.

Define the STL metric defect

\[
\Delta_{\ell m}(u,v)
:=
[T_{\ell m}u,T_{\ell m}v]_{h_m}
-
T_{\ell m}([u,v]_{h_\ell}).
\]

Thus

\[
\Delta_{\ell m}=0
\]

means

\[
[T_{\ell m}u,T_{\ell m}v]_{h_m}
=
T_{\ell m}([u,v]_{h_\ell})
\]

for all

\[
u,v\in\mathcal D.
\]

## Descriptor-Transport Composition

For a chain

\[
\ell\preceq m\preceq n,
\]

assume descriptor transports compose:

\[
T_{\ell n}=T_{mn}\circ T_{\ell m}.
\]

This is the only required chain-coherence hypothesis.

## Theorem: STL Chain-Coherence Lemma

For every chain

\[
\ell\preceq m\preceq n,
\]

if

\[
\Delta_{\ell m}=0,
\qquad
\Delta_{mn}=0,
\]

and

\[
T_{\ell n}=T_{mn}\circ T_{\ell m},
\]

then

\[
\Delta_{\ell n}=0.
\]

## Proof

Let

\[
u,v\in\mathcal D.
\]

Assume

\[
\Delta_{\ell m}=0
\]

and

\[
\Delta_{mn}=0.
\]

By

\[
\Delta_{mn}=0,
\]

we have

\[
[T_{mn}a,T_{mn}b]_{h_n}
=
T_{mn}([a,b]_{h_m})
\]

for all

\[
a,b\in\mathcal D.
\]

Apply this with

\[
a=T_{\ell m}u,
\qquad
b=T_{\ell m}v.
\]

Then

\[
[T_{mn}T_{\ell m}u,T_{mn}T_{\ell m}v]_{h_n}
=
T_{mn}([T_{\ell m}u,T_{\ell m}v]_{h_m}).
\]

Using transport composition,

\[
T_{\ell n}=T_{mn}\circ T_{\ell m},
\]

the left-hand side is

\[
[T_{\ell n}u,T_{\ell n}v]_{h_n}.
\]

By

\[
\Delta_{\ell m}=0,
\]

we have

\[
[T_{\ell m}u,T_{\ell m}v]_{h_m}
=
T_{\ell m}([u,v]_{h_\ell}).
\]

Therefore

\[
T_{mn}([T_{\ell m}u,T_{\ell m}v]_{h_m})
=
T_{mn}T_{\ell m}([u,v]_{h_\ell})
=
T_{\ell n}([u,v]_{h_\ell}).
\]

Hence

\[
[T_{\ell n}u,T_{\ell n}v]_{h_n}
=
T_{\ell n}([u,v]_{h_\ell})
\]

for all

\[
u,v\in\mathcal D.
\]

Therefore

\[
\Delta_{\ell n}=0.
\]

\[
\square
\]

## Corollary: Global Chain Closure

On any finite STL poset, if

\[
\Delta_{ab}=0
\]

for each adjacent comparable step in a composable chain, and descriptor transports compose along the chain, then

\[
\Delta_{\ell n}=0
\]

for the composite transition from the initial layer \(\ell\) to the terminal layer \(n\).

This follows by finite induction using the STL Chain-Coherence Lemma.

## What This Closes

This closes the basic poset-coherence layer of STL:

\[
\Delta_{\ell m}=0
\quad\text{and}\quad
\Delta_{mn}=0
\quad\Longrightarrow\quad
\Delta_{\ell n}=0
\]

under the explicit transport-composition hypothesis.

## What It Does Not Close

This theorem does not classify all STL structures.

It does not prove:

- quantum gravity,
- canonical quantization,
- Einstein equations,
- empirical gravity,
- cosmology,
- unification,
- a physical theory of spacetime,
- or a solution of gravity.

It is only a bounded algebraic coherence theorem for STL metric defects.
