---
name: certified-bernstein-conformal-bootstrap
description: Bernstein-certified rigorous conformal bootstrap bounds.
category: ai_collection
source_title: "Region bounds, error margins and certified positivity in the numerical conformal bootstrap; Or the first mathematically rigorous bounds on the 3d Ising CFT critical exponents"
source_arxiv: "2610.20701"
---

# Certified Bootstrap via Bernstein Positivity

**Source**: M. Reehorst (KCL), arXiv:2610.20701 (Oct 2026). Closes all four rigor gaps of the numerical conformal bootstrap and delivers the first mathematically rigorous two-sided bounds on 3d Ising critical exponents: η ∈ (0.011, 0.080), ν ∈ (177/29/100, 20/29) under explicit spectrum assumptions — turning a physics numerics tradition into machine-checkable theorems.

## When to Use
- Converting any LP/SDP-computed "rigorous-looking" bound (bootstrap functionals, computer-assisted proofs) into a machine-checkable certificate
- Certifying polynomial positivity on regions (not just sampled points) in several variables with exact arithmetic
- Numerical conformal bootstrap searches that keep missing islands / thin protrusions
- Any pipeline where floating-point search results must survive formal scrutiny (region bounds + truncation error envelopes)

## The Four Rigor Gaps (and their fixes)

| Gap | Problem | Fix |
|---|---|---|
| 1. Point vs region | Bounds proven only at sampled grid points; isolated islands & thin protrusions missed (the 2016 'too small Ising island' failure) | Functionals positive on whole parameter REGIONS incl. external-dimension space; a fully closing exclusion ring certifies bounds regardless of island shape |
| 2. Truncated vs true blocks | Truncated rational approximations of conformal blocks used in numerics | Certified truncation-error ENVELOPE (majorant) subtracted from computable object → positivity of uncomputable true-block value |
| 3. Finite spin list | Only spins ≤ ~100 checked | Truncated blocks are rational functions of REAL spin variable → entire spin tail is ONE more Bernstein direction (compactified, includes ℓ=∞ face) |
| 4. Floating point | Sign tests unreliable at margins ~1e-10 | Exact arithmetic in Q(√2): every quantity a + b√2 with rational a,b; all sign tests exact integer comparisons |

## Core Techniques

### 1. Search/certificate separation (trusted base)
All floating machinery (SDP/LP solvers, grids, heuristics) only PROPOSES candidates; soundness rests entirely on the certificate layer. Trusted computing base: exact arithmetic + Sturm's theorem + the two-line Bernstein positivity implication + 3 analytic facts (OPE convergence, radial expansion positivity, pole recursion structure).

### 2. Bernstein-basis positivity certificates
A polynomial is strictly positive on a box iff (after subdivision loop) its Bernstein coefficients on some sub-box are all positive — positivity made VISIBLE in coefficients. Built-in counterexample detection; terminates on any strictly positive polynomial. Failed alternatives (per the paper): interval arithmetic, numerical SOS + rationalization — Bernstein succeeded where they failed. Up to 3 variables: (external dimension Δ, twist, real spin ℓ).

### 3. Margin maximization (essential for certifiability)
Maximize the margin by which positivity is achieved, not bare feasibility. Every margin-free functional failed certification (small violation at some large finite spin or the ℓ=∞ face). Also impose explicit positivity constraints at non-compact directions (ℓ ~ 10⁶, ℓ=∞). The margin doubles as a navigator function for the search.

### 4. Region bounds as 1-D bisections (practical payoff)
Mapping an island via point bounds costs many expensive LP runs; with region functionals, an exclusion ring around the island reduces to a handful of 1-dimensional bisections — a favorable optimality-class change. Region constraints also catch sampling failure modes that point checks silently miss.

## Flagship Certified Result
For Δσ ∈ [0.505, 0.5405], ALL Δε ∈ (1/2, 3] is excluded except a small rectangle: (Δσ, Δε) ∈ (0.5055, 0.540) × (1.23, 1.55) containing the 3d Ising island. Assumptions: unitary Z2-symmetric 3d CFT, one relevant Z2-odd scalar σ, at most one relevant Z2-even scalar, stress tensor at Δ=3, spin-2 gap Δ_T′ ≥ 11/2.

## Workflow
1. Solve floating-point LP for a functional on a candidate tile (search layer)
2. Maximize positivity margin + impose non-compact-direction constraints (ℓ=∞, large finite ℓ)
3. Convert candidate to exact Q(√2) coefficients (rationalize)
4. Run Bernstein subdivision certifier on the multi-variable box; on failure, refine search with the counterexample
5. Subtract the certified truncation envelope before certifying against TRUE blocks
6. Loop: bisection over 1-D slices of parameter space to chart the exclusion region

## Pitfalls
- Margin-free functionals are typically NOT certifiable — margin maximization is not optional
- Point-sampled bounds can silently exclude true islands (2016 Ising island was too small)
- The one irrationality √2 enters via the crossing-symmetric point r* = 3−2√2 — represent everything in Q(√2) or sign tests are not exact
- Half-line domains (twist) need a compactifying substitution before Bernstein; domains: intervals, half-lines, point at infinity

## References
- Reehorst, arXiv:2610.20701 (2026); released code + machine-checkable certificates
- Bernstein-basis positivity: classical; subdivision terminates on strictly positive polynomials
- Bootstrap context: Kos et al. island charting; navigator function technique (Simmons-Duffin)
