---
name: arithmetic-sync-basin-pulse-coupled-oscillators
description: Use when analyzing pulse-coupled oscillator sync basins by number theory
category: ai_collection
trigger: pulse-coupled oscillators, synchronization basin volume, prime factorization effect on sync, convex charging integrate-and-fire, cluster state arithmetic, equal-size principle
source: arXiv:2609.01668 (K. P. O'Keeffe — Starling Research Institute, v2 30 Sep 2026)
---

# Arithmetic of the Sync Basin for Pulse-Coupled Oscillators

## Core Insight

For N identical pulse-coupled oscillators (PCOs), the **probability of reaching full synchrony is governed by the prime factorization of N** at the critical (linear) charging curve γ=0. This adds an *arithmetic* basin to the atlas of exotic basin geometries (fractal, riddled, tentacled): not strange in shape, strange in number theory.

## Model

N oscillators, voltage x_i ∈ [0,1], `ẋ_i = 1 − γx_i` on complete graph:
- x(t) = (1−e^{−γt})/γ: concave for γ>0 (leaky), **linear at γ=0**, convex for γ<0
- At x_i = 1: fire, reset to 0, deliver pulse Δ = k/N to all others (k = firer's cluster size); any neighbor at x_j + Δ ≥ 1 merges into the firing cluster
- Initial voltages i.i.d. Uniform(0,1); P_sync(N, γ) = probability of full synchrony

**Why γ ≤ 0 matters**: concave (Mirollo–Strogatz) guarantees sync from almost all ICs. Convex charging (γ<0) removes the guarantee and occurs in **quadratic and exponential integrate-and-fire neurons** — the accelerating spike-initiation regime of many excitable cells. Basin size has practical value (e.g., heart: normal rhythm vs fibrillation basins).

## Main Results

### 1. Equal-size principle (γ = 0, all N — EXACT)

At linear charging, voltage = phase, so the Poincaré return map after one firing round is a **pure translation**: cluster j shifts by p_0 − p_j where p_i = k_i/N is its pulse fraction. To avoid absorption forever, the shift must vanish for every cluster → **every non-sync trajectory settles into equal-size clusters whose common size divides N** (K | N clusters of size N/K).

- Every divisor is realized; number of distinct outcomes = **d(N)** (number of divisors)
- Arithmetic thinning is drastic: from Euler's p(N) ~ e^{π√(2N/3)}/(4N√3) a priori partitions down to d(N) — e.g., at N=100: 9 outcomes vs 1.9×10⁸ partitions

### 2. Prime N (γ = 0 — EXACT)

Only non-sync outcome is all-singletons (1)^N, probability = 1/N^N (volume of polytope where all N−1 ordered gaps exceed 1/N):

**P_sync(N) = 1 − 1/N^N for prime N**

### 3. General N (γ = 0 — EXACT via recurrence)

Write N·x_i = a_i + r_i (integer + fractional). At γ=0, dynamics depends only on the **rank order of fractional parts r_i**, not their values → relabel by r_i order; the "word" a = (a_0,…,a_{N−1}) is uniform on {0,…,N−1}^N and the outcome is constant on each word. Continuous basin-volume problem → **counting words that lead to sync**:

**P_sync(N) = A_{N,1} / N^N**, A_{N,1} from finite recurrence on cluster states S = ((b_0,s_0),…): next firer f = argmax(b_i, i); j absorbed iff d = b_j − b_f + s_f > 0 (or =0 and q_j > q_f); survivors move to b'_j = b_j − b_f + s_f/N·N... iterate map T_N; σ(S) ∈ {0,1} invariant → A_{N,1} = Σ_words σ((a_0,1),…,(a_{N−1},1)).

Exact values: 3/4, 26/27, 227/256, 3124/3125, 42275/46656, 823542/823543, 15682639/16777216 for N=2..8 (primes N=2,3,5,7 show N^N−1/N^N).

### 4. Composite scaling (EMPIRICAL)

For N = pq (p<q): 4 outcomes — sync, p clusters of size q, q clusters of size p, singletons with weights (1−C_p N^{−(p−1)}, C_p N^{−(p−1)}, C_q N^{−(q−1)}, N^{−N}).

Dominant non-sync channel set by **least prime factor m = lpf(N)**:

**1 − P_sync(N) ∼ C_m N^{−(m−1)}**, C_2 ≈ 0.60, C_3 ≈ 0.53 (no proof; local-limit property of entrance into m equal blocks remains open)

Example N=15: sync 0.997852, (5)³ at 2.14×10⁻³, (3)⁵ at 7.7×10⁻⁶, (1)¹⁵ at 15⁻¹⁵.

### 5. Convex γ < 0 (EXACT for N ≤ 5, γ ∈ [−1, 0])

Branch decomposition (trace all cluster trajectories): P_sync(2,γ) = (3−γ)/[2(2−γ)]; analogous rational functions for N=3,4,5 (eqs 7–10). All **jump discontinuously at γ=0**; valid down to endpoint γ*(N) where new unequal-cluster attractors appear.

**Unequal-cluster survival criterion** (two clusters n₁ ≥ n₂): p_c(γ) = √(1−γ)·√(n₁/n₂)/(1+√(1−γ))... at γ=0 permits only equal clusters; for every γ<0 an unequal window opens (e.g., N=7, γ=−1: (4,3) attractor takes ~22% of ICs).

## When to Use This Pattern

1. **Neural synchronization analysis**: pick population size N with intent — prime N maximizes sync probability (only singleton escape); composite N opens m-cluster sectors via lpf(N). Relevant to pulse-coupled neural coding, central pattern generators, cardiac rhythm modeling.
2. **Exact basin computation via symbolic reduction**: when dynamics depends only on rank order of a coordinate decomposition (integer word + fractional ranks), continuous basin volume collapses to counting a finite uniform discrete set — a generalizable technique.
3. **Critical-point analysis**: the arithmetic structure lives exactly at the boundary between leaky (synchronizing, γ>0) and active (cluster-forming, γ<0) dynamics — a critical phenomenon of the charging nonlinearity, NOT generic to pulse coupling. Fragility is the message.
4. **Return-map translation argument**: pulse fraction p_i = k_i/N as the only invariant-relevant quantity; unequal clusters drift by p_0−p_j per round and get absorbed — quick analytic tool for related coalescent/merging systems.

## Caveats

- Equal-size principle is **special to linear charging**; for γ<0 the return map is Möbius/projective, not size-only translation.
- Composite asymptotics (exponent, prefactors) are empirical; proof open.
- Exact convex-regime results limited to N ≤ 5; general-N formula for γ<0 out of reach.
- Biological realism: idealized all-to-all, identical units, specific pulse form — real neurons add heterogeneity, delays, noise.

## References
- arXiv:2609.01668 — O'Keeffe, "Arithmetic of the sync basin for pulse-coupled oscillators" (PRL-style preprint, 4p + SM)
- Mirollo & Strogatz 1990 — concave charging sync theorem; Wiley–Strogatz–Girvan 2006 — basin size & cardiac death; Zhang & Strogatz 2021 — tentacled basins
