---
name: mean-field-lie-scheffers-oscillator-reduction
description: "Mean-field Lie-Scheffers 28 normal forms exact reduction."
version: 1.0.0
author: "Kai Tokunaga (arXiv 2610.28715) via neuro-cron 2026-10-24"
license: MIT
category: ai_collection
metadata:
  hermes:
    tags: [mean-field, lie-scheffers, watanabe-strogatz, coupled-oscillators, stuart-landau, gko-classification, neural-mass, low-dimensional-reduction]
    arxiv_id: "2610.28715"
---

# Mean-Field Lie-Scheffers Oscillator Reduction (28 GKO Normal Forms)

Methodology from "Low-Dimensional Reduction of Mean-Field Coupled Dynamical Systems with Units Described by Two Real Variables: Classification and Applications" (Kai Tokunaga, U. Tokyo, arXiv:2610.28715, math.DS/nlin.AO, 12 pp). Answers exactly WHEN a population of N identical two-variable units under global (mean-field) coupling collapses to a few macroscopic ODEs, and WHICH unit models qualify — going well beyond phase-only (Watanabe-Strogatz / Ott-Antonsen) to units with amplitude dynamics.

## When to Use

- Deciding whether coupled oscillator / neural-oscillator populations (with amplitude, not just phase) admit an EXACT collective description
- Extending WS/Ott-Antonsen-style reductions to limit-cycle models: which Poincare / Stuart-Landau / higher-saturation variants remain reducible under which coupling harmonics
- Deriving exact firing-rate or neural-mass equations for spiking/oscillatory unit populations (cf. Pazó-Cestnik complex-Riccati theta-neuron reductions)
- Auditing a claimed "macroscopic reduction": check the mean-field Lie-Scheffers structure first instead of assuming self-consistency will close

## The Reduction Criterion (mean-field Lie-Scheffers structure)

System: N identical units x_i in R^2, mean field mu(X) common to all units:

    X-dot_i = f(x_i, mu(X), t)

It admits EXACT low-dimensional reduction iff the frozen-input single-unit ODE

    x-dot = f(x, zeta(t), t)   (mean field replaced by ARBITRARY time function)

is a Lie system: the vector field expands as f = sum_alpha a_alpha(t) L_alpha(x)
over a FINITE-dim VGL (Vessiot-Guldberg-Lie) algebra v = span{L_1..L_r} with [L_a,L_b] = c^g_ab L_g (Martens & Dharmavaram, arXiv:2607.12210). The mean-field evaluation along a solution is a valid such zeta(t) — so the N-unit system inherits the reduction.

## Two Reduction Routes (choose the cheaper)

1. Fundamental solutions (Lie-Scheffers superposition): x(t) = Phi(x^(1)(t)..x^(m)(t), xi) with xi per-unit constants; closed system on the m fundamental solutions -> dimension 2m*. Minimum m* = smallest m such that only trivial c_alpha satisfies sum_alpha c_alpha L_alpha(x^(k)) = 0 at generic points (transversality of the algebra at m sample points).
2. Equations on a group (this paper's addition): x(t) = Psi(g(t), x_0) with g in matrix Lie group G, g-dot = A(t)g, A = -sum a_alpha(t, mu(X*)) M_alpha -> dimension r = dim(VGL). Group action built from basis flows: Psi(g,x) = (psi^1_{v1} o ... o psi^r_{vr})(x).

NOTE: 2m* need not equal r and can be LARGER. Group coordinates v_1..v_r can carry physical meaning as macroscopic variables — Watanabe-Strogatz theory is exactly the r=3 (Möbius/P2) case: 2m*=4 fundamental dims vs r=3 group dims + N-3 constants of motion.

## The 28 Normal Forms (GKO classification)

Any finite-dim Lie algebra of planar vector fields is locally diffeomorphic near generic points to one of 28 normal forms (González-López-Kamran-Olver). Because a Lie system's VGL algebra is NOT unique, pin the class with the MINIMAL VGL algebra (lowest dimension among associated algebras).

Primitive (P1-P8) — no invariant curve family:
- P1: z-dot = a1 + i a2 + (alpha - i) a3 z — R⋉R^2 — r=3
- P2: z-dot = a1 + a2 z + a3 z^2 — sl(2,R) — r=3 (Riccati = Möbius = WS)
- P3: Möbius on sphere — so(3) — r=3; P4: z -> az+b — R^2⋊R^2 — r=4
- P5: sl(2,R)⋉R^2 — r=5; P6: gl(2,R)⋉R^2 — r=6; P7: sl(2,C)_R ≅ so(3,1) — r=6; P8: projective sl(3,R) — r=8

Imprimitive (I1-I11, I12(L)-I20(L)) — one variable's equation decouples:
- Phase-relevant classes: I3/I4/I5 (sl(2,R) types I/II/III, r=3), I6/I7 (gl(2,R), r=4), I8 (B_alpha ≅ R⋉R^2, r=3), I9 (h2⊕h2), I10 (sl(2,R)⊕h2, r=5), I11 (sl(2,R)⊕sl(2,R), r=6)
- Family classes I12(L)-I20(L): parameter L = number of independent functions / polynomial degree; e.g. I20(L): gl(2,R)⋉R^{L+1}, r = L+5, action mixes Möbius with polynomial phase-dependent amplitude terms

GKO classifies SYSTEMS (normal forms with arbitrary time-dependent coefficients), NOT Lie algebra structures — distinct normal forms can share one algebra. Global consistency (e.g. phase periodicity) must be checked separately from the local classification.

## Application: Reducible Populations of Limit-Cycle Oscillators

Constrain the phase to obey a CLOSED Riccati-type equation via x = tan(k*theta/2) → candidates I3, I4, I5, I6, I7, I10, I11, I19(L), I20(L). Requiring a STABLE limit cycle leaves: I7, I10, I11, I20(L).

I20(L) is the workhorse (phase-dependent amplitude, most general). In physical amplitude r_i (rho_i = 1/r_i^p):

    theta-dot = omega(mu,t) + Im[H(mu,t) e^{i k theta}]
    r-dot = [lambda(mu,t) - (Lk/2) Re(H e^{i k theta})] r^{p-1}/p
            - (1/p) sum_j Re[G_j(mu,t) e^{i(L-2j)k theta/2}] r^{p+1}

- p = 1: Poincaré oscillator population
- p = 2: Stuart-Landau population (Hopf normal form)
- p >= 3: SL with higher-order saturation

Smoothness at the origin (needed for bifurcations from zero amplitude) forces polynomial vector fields: p=2, k=2, L=2 reproduces SL with second-harmonic coupling (Tokunaga arXiv:2608.04000) — typically clusters. NEW: first-harmonic coupling becomes reducible too (p=2, k=1, L=4) at the price of origin smoothness; Poincaré case p=1, k=1, L=2. Many further limit-cycle models sit inside the same families.

## Pitfalls / Discipline

- VGL algebra non-uniqueness: always classify by the MINIMAL VGL algebra, or the same system maps to several normal forms
- Reduction dimension: compare 2m* (fundamental) vs r (group) before building the macroscopic system; group route is never worse and often strictly smaller
- Local vs global: GKO is a local (generic-point) classification; periodic phase variables and boundaries need separate global checks
- Physicality at the origin: reducible first-harmonic SL variants lose smoothness at r=0 — safe away from zero-amplitude onset, misleading inside Hopf-bifurcation analysis
- Exactness scope: constants of motion + reduced ODEs describe the FULL N-unit dynamics (finite N, no N->infty assumption), unlike OA ansatz consistency arguments

## Key References

- Martens & Dharmavaram, arXiv:2607.12210 — mean-field Lie-Scheffers base theory
- Tokunaga, arXiv:2608.04000 — reducible Stuart-Landau populations (predecessor)
- Pazó & Cestnik, PRE 111:L052201 (2025) — complex-Riccati populations = exact firing-rate equations for spiking neurons with clustered substructure
- Marvel-Mirollo-Strogatz (2009) — Möbius group action for sinusoidal phase oscillators
- Wilson & Moehlis (2016); Shirasaka et al. (2020) — isostable / phase-amplitude reduction context
