---
name: quantum-ordinal-optimization-fixed-budget
description: "Use when selecting good-enough designs under scarce comparison/evaluation budgets. Quantum vs classical exact optima."
category: systems-engineering
---

# Quantum Ordinal Optimization under a Fixed Comparison Budget

Source: arXiv:2610.15791 (Hongyu Wu, Kansas State, 11 Oct 2026). Formulates **quantum ordinal
optimization (QOO)**: maximize worst-case alignment probability (chance the selected design's
rank is within the good-enough top-r) under a fixed budget of comparison-oracle queries.
Crossover of simulation-optimization practice (ordinal optimization, Ho/OLHC/Lau) with exact
few-query quantum query complexity.

## Core Results (all exact, not asymptotic)

1. **Classical optimum (Thm 1)**: at every budget q < n, the best alignment probability equals
   a **blind pick of q+1 designs followed by a knockout** among them:
   `C_q(n,r) = 1 - C(n-r, q+1)/C(n, q+1)`. No adaptive comparison tree beats this — proof:
   leaf-conditioning on comparison trees, the output's connected component has k ≤ q+1
   vertices, and its rank set is a uniform k-subset regardless of recorded order within the
   component (Lemma 1). Adaptive cleverness buys NOTHING over sampling q+1 + tournament.
2. **Quantum degree doubling (Thm 2)**: after symmetrization, a q-query quantum algorithm's
   output-rank law is a polynomial of degree ≤ min(2q, n−1) in the rank; classical laws cap at
   degree q. Attainment: coherent query on a uniform root label a with a uniform d-subset of
   others, pairing them so one call yields sign products sgn_au·sgn_av. Degree-2 rank laws
   (e.g. (1/2, 0, 1/2) at n=3) are classically impossible with 1 comparison.
3. **Exact one-comparison quantum optimum (Thm 3)**: `Q_1(n,r) = r/n + r(n−r)·ζ/(n(n−1))`
   where ζ = smallest positive root of the cubic
   `F_{n,r}(z) = 2nhz³ + 3(nk−h²)z² − 4(2n−3)hz − 6mk` with m=n−1, k=n−2, h=n−2r.
   Proof: one-query SDP characterization (moment matrices M_i, positive B_i with diagonal
   trace-1 sum), label symmetry reduces M_i to explicit 2×2 blocks, dual L ⪰ M_i with constant
   diagonal; ζ is where L's diagonal becomes constant. Covariant state+measurement attain it.
4. **OO-unit comparison**: report values as **equivalent blind-pick size** (number of uniform
   picks achieving the same alignment probability). For best-design selection one quantum
   comparison → (3+√13)/2 ≈ 3.30 picks as n→∞ vs 2 for classical. **One quantum comparison
   beats TWO classical comparisons exactly when n > 9.** For top-half targets the quantum
   advantage shrinks (below 2 classical comparisons at n=1000, r=n/2) — the advantage
   concentrates on stringent good-enough sets.

## Methodological Patterns to Reuse

- **Fixed-budget selection problems**: define the oracle (comparison/evaluation/membership),
  the budget unit, and the success metric (alignment level), THEN optimize worst-case success.
  The equivalent-blind-pick-size normalization makes incomparable methods comparable.
- **Polynomial method over comparison signs**: quantum output probabilities are degree-≤2q
  polynomials in sign functions sgn(x_a−x_b); monomials = graphs, evaluation over uniform
  orders factors into detached-component averages µ_j × root-component hypergeometric terms.
  A degree gap between classical and quantum laws IS the quantum advantage mechanism.
- **Leaf-conditioning lower bounds**: for any adaptive comparison tree, the compared
  component's rank set stays uniform — a stochastic-dominance argument then bounds all trees
  at once. Reusable for any "adaptive selection vs sampling" impossibility result.
- **SDP moment-matrix duals with symmetry reduction**: exact few-query optima via
  target-conditioned moment matrices + covariant ansatz; the dual certificate's feasibility
  condition (constant diagonal) pins the optimum to an algebraic root.
- **Knockout-among-blind-picks as a benchmark**: any claimed "smart" selection heuristic
  under exact comparisons must be compared against this optimum, not against naive baselines.

## Scope & Caveats

- Budget counts comparison queries, NOT evaluations: one coherent comparison costs ~4
  evaluations if built from a design-evaluation oracle (compute+uncompute both sides) —
  gain is per comparison, not per evaluation.
- Quantum advantage holds for alignment level 1, selected-set size 1, exact (noiseless)
  comparisons. Estimation error, noisy comparisons, larger selected sets need new instances.
- For n ≤ 9 designs, quantum gives no advantage over 2 classical comparisons; for lenient
  good-enough sets (r ≈ n/2) classical may tie or win.

## Verification Anchors

- n=3, q=1: quantum rank law (1/2, 0, 1/2), degree 2 — classical max degree 1, so no
  classical 1-comparison algorithm matches it.
- n=1000, r=50 (top 5%): equivalent blind-pick size ≈ 3.27.
- Q_1(n,1) closed form: [3(n−1) + √(13n²−18n+9)] / (2n²); Q_1(n,n/2) = 1/2 + √(8(n−1))/(2n²)... via ζ=√(2(n−1)/n).
