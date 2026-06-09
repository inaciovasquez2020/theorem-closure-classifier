# STL Closed-Basic Liouville Core

## Status

Bounded classical STL formalism.

No quantization claim.
No Einstein-equation claim.
No empirical-physics claim.
No quantum-gravity claim.

## Standing Setup

Let

\[
\Sigma
\]

be a compact boundaryless smooth \(3\)-manifold.

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

For a smooth path

\[
z:[0,1]\to\Gamma,
\]

define

\[
\mathcal A_\lambda(z):=\int_0^1 z^*\lambda.
\]

For a smooth transition

\[
R:\Gamma\to\Gamma,
\]

define the action defect

\[
\mathfrak a_R(z)
:=
\mathcal A_\lambda(R\circ z)-\mathcal A_\lambda(z).
\]

Equivalently,

\[
\mathfrak a_R(z)
=
\int_0^1 z^*(R^*\lambda-\lambda).
\]

## Endpoint-Local Action Defect

A transition

\[
R:\Gamma\to\Gamma
\]

has endpoint-local action defect if there exists a smooth function

\[
E_R:Q\times Q\to\mathbb R
\]

such that for every smooth path

\[
z:[0,1]\to\Gamma
\]

one has

\[
\mathfrak a_R(z)
=
E_R(\pi_Q(z(0)),\pi_Q(z(1))).
\]

## Closed Basic Liouville Defect

A transition

\[
R:\Gamma\to\Gamma
\]

has closed basic Liouville defect if there exists

\[
\beta_R\in\Omega^1(Q)
\]

such that

\[
R^*\lambda-\lambda=\pi_Q^*\beta_R
\]

and

\[
d\beta_R=0.
\]

This is the primitive STL admissibility condition.

## Convexity of the ADM Metric Base

For any

\[
h_0,h_1\in \mathrm{Riem}(\Sigma)
\]

and any

\[
t\in[0,1],
\]

the tensor

\[
h_t:=(1-t)h_0+th_1
\]

is again an element of

\[
\mathrm{Riem}(\Sigma).
\]

Therefore

\[
Q=\mathrm{Riem}(\Sigma)
\]

is convex, path connected, and contractible.

## Endpoint-Closed Equivalence

For a smooth transition

\[
R:\Gamma\to\Gamma,
\]

the following are equivalent:

\[
R\text{ has endpoint-local action defect}
\]

and

\[
R^*\lambda-\lambda=\pi_Q^*\beta_R
\quad\text{for some closed}\quad
\beta_R\in\Omega^1(Q).
\]

## Closed-Basic Symplectic Lemma

If

\[
R:\Gamma\to\Gamma
\]

has closed basic Liouville defect, then

\[
R^*\Omega=\Omega.
\]

Proof:

\[
R^*\lambda=\lambda+\pi_Q^*\beta_R.
\]

Therefore

\[
R^*\Omega
=
R^*(-d\lambda)
=
-d(R^*\lambda)
=
-d(\lambda+\pi_Q^*\beta_R)
=
-d\lambda-\pi_Q^*(d\beta_R)
=
\Omega.
\]

## STL Metric Defect

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

For each comparable pair

\[
\ell\preceq m,
\]

let

\[
f_{\ell m}:\Sigma\to\Sigma
\]

be a diffeomorphism, and define descriptor transport

\[
T_{\ell m}(N,X)
:=
(N\circ f_{\ell m}^{-1},(f_{\ell m})_*X).
\]

Define the STL metric defect

\[
\Delta_{\ell m}(u,v)
:=
[T_{\ell m}u,T_{\ell m}v]_{h_m}
-
T_{\ell m}([u,v]_{h_\ell}).
\]

## STL Metric-Rigidity Lemma

For every comparable pair

\[
\ell\preceq m,
\]

one has

\[
\Delta_{\ell m}=0
\quad\Longleftrightarrow\quad
f_{\ell m}^*h_m=h_\ell.
\]

## STL Core Metric-Symplectic Rigidity Theorem

For every comparable pair

\[
\ell\preceq m,
\]

assume

\[
\Delta_{\ell m}=0
\]

and

\[
R_{\ell m}^*\lambda-\lambda=\pi_Q^*\beta_{\ell m},
\qquad
d\beta_{\ell m}=0.
\]

Then

\[
f_{\ell m}^*h_m=h_\ell
\]

and

\[
R_{\ell m}^*\Omega=\Omega.
\]

Equivalently,

\[
\Theta_{\ell m}:=R_{\ell m}^*\Omega-\Omega=0.
\]

## Obsolete Primitive

Action-neutrality is obsolete as a primitive STL admissibility condition.

The primitive condition is closed basic Liouville defect:

\[
R_{\ell m}^*\lambda-\lambda=\pi_Q^*\beta_{\ell m},
\qquad
d\beta_{\ell m}=0.
\]

Endpoint-locality is retained only as the equivalent derived condition:

\[
\text{endpoint-local action defect}
\Longleftrightarrow
\text{closed basic Liouville defect}.
\]

## Boundary

This proves only a bounded classical STL consistency theorem.

It does not prove quantization, the Einstein equations, empirical gravity, cosmology, unification, or quantum gravity.
