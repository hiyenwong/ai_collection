---
name: channel-stein-theorem-causal-order
description: Use when testing quantum channels or proving channel discrimination exponents. Stein rate.
category: ai_collection
---

# Channel Stein Theorem beyond Definite Causal Order

**Paper**: arXiv:2609.30268 — Chengkai Zhu (QudeLeap Research), Xin Wang (HKUST-GZ), 24 Sep 2026.

## Core Result (Theorem 2.4)

For any two finite-dimensional memoryless (CPTP) quantum channels N, M: A→B, every fixed type-I
error tolerance ε∈(0,1), and ALL three tester classes:

- **parallel** (joint probe, T₁+T₂ = σ⊗1, product input)
- **adaptive** (sequential with quantum memory, co-comb normalization)
- **general** (positive process-tester model — permits indefinite causal order / quantum switch)

the Stein exponent is the SAME:

    lim_{n→∞} (1/n) D_H^{ε,S}(N^⊗n ∥ M^⊗n) = D^∞(N∥M) = lim_k (1/k) D(N^⊗k∥M^⊗k)

**Operational takeaway**: adaptivity, feedback, and indefinite causal order provide ZERO asymptotic
advantage in asymmetric channel discrimination. Finite-use advantages of the quantum switch (known
from minimum-error discrimination) wash out at the Stein rate. Any r > D∞ forces correct null
acceptance a ≤ e^{−cn} (exponential strong converse, holds even for general testers).

Exact strong-converse exponent (Cor. 6.1, needs supp J_N ⊆ supp J_M):

    E^sc(r) = sup_{p>1} (p−1)/p · (r − D̃_p^∞(N∥M))

positive iff r > D^∞ — using regularized sandwiched Rényi divergence.

## Reusable Proof Machinery

1. **Positive-slack SDP duality (Lemma 4.1)**: the optimal weighted testing score
   ∆_n(λ) = max(a−λb) over parallel testers equals the minimum normalized positive Choi slack:
   ∆_n(λ) = min{h : N_n ≤ λM_n + Z, Tr_B Z = h·1}. This is the bridge between testing and
   smoothing — SDP duality converts tester optimization into operator domination.

2. **Fixed-marginal de Finetti reduction**: permutation-invariant slack Q → mixture of IID
   channel Choi operators with only POLYNOMIAL loss g_n = C(n+d²Ad²B−1, n), log g_n = O(log n).
   This transfers any parallel-tester bound to every general tester:
   a ≤ λb + g_n·∆_n(λ). Polynomial factors never affect exponential rates.

3. **Rényi endpoint continuity (Theorem 5.1)**: lim_{p↓1} D̃_p^∞(N∥M) = D^∞(N∥M) —
   the regularized sandwiched Rényi divergence is continuous at order one AFTER regularization.
   Proved via three-amplitude comparison: supported-inverse factorization lifts positive order
   N ≤ B+Z to amplitude decomposition X = √B·S⁺√N, F = √Z·S⁺√N with XX†≤B, FF†≤Z;
   one tensor moment estimate (Lemma 5.3) controls arbitrarily entangled probes.

4. **One-shot duality (Theorem 3.1)**: D_H^{1−q,par} = inf_δ D̃_max,all^δ − log(q−δ);
   for general testers the dual smoothing set is the positive AFFINE hull of product Choi
   operators (not the convex hull) — affine constraints don't impose slot-separability.

## Checklist for Channel Discrimination Problems

1. Compute/estimate D^∞(N∥M) (regularized channel relative entropy) — this IS the answer for
   any strategy's fixed-error Stein rate. Don't search for exotic testers.
2. Support check: if supp J_N ⊄ supp J_M → rate is +∞ (maximally-entangled-probe P0 test:
   b=0, a→1 exponentially).
3. Finite-n analysis: use score bound a ≤ λb + g_n ∆_n(λ) with g_n polynomial.
4. Strong converse: pick p>1 with D̃_p^∞ < r, exponent (p−1)/p·(r−D̃_p^∞).
5. Smoothing AEP: modified smooth max-relative entropy → D^∞ for ALL four smoothing sets
   (all/affine/prod/iid) at any fixed budget δ∈(0,1); at δ=0 all equal n·D_max — the
   positive-budget qualification is essential.

## Relation to Existing Skills

- `w1-robust-quantum-stein` (2609.17309): W1-distance Stein variant — different divergence,
  state-level, non-regularized. This paper: channel-level, regularized, causal-order-complete.
- `indefinite-causal-order-real-complex` / `causal-nonseparability-dephasing`: process-matrix
  resource theory; here the general tester class subsumes ICO and shows NO Stein-rate gain.
- `regularized-channel-renyi-continuity` (2609.29885): companion paper proving continuity of
  regularized channel Rényi divergence — the analytic core reused here at order one.

## Keywords

quantum channel discrimination, Stein's lemma, indefinite causal order, quantum switch,
regularized channel relative entropy, sandwiched Rényi divergence, strong converse exponent,
hypothesis testing, SDP duality, de Finetti reduction, smooth max-relative entropy AEP,
process testers, adaptivity no-advantage theorem
