---
name: smc-ensemble-parallel-cps-verification
description: Use when SMC-verifying CPS models. Ensemble SAs + HPC.
category: research
---

# SMC Ensemble + HPC Parallel CPS Verification (EAA / HPC-EAA)

Source: arXiv:2610.21772 — Picchiami, Parmentier, Legay, Mancini, Tronci (Sapienza Rome / UCLouvain), Elsevier J. Systems & Software 2025, DOI 10.1016/j.jss.2024.112238.

## Problem
Model-based formal verification of industry-relevant Cyber-Physical Systems is computationally prohibitive (state explosion kills symbolic methods). Statistical Model Checking (SMC) is the fallback, but each sample = one expensive numerical simulation (0.1–several s), and up to 10⁸ samples are needed. The number of samples an Adaptive Stopping Algorithm (SA) requires depends on unknown statistical properties of the KPI, so any single SA can overshoot by orders of magnitude.

## Core Method 1 — EAA (Ensemble of Approximation Algorithms)
Run k different (ε, δ)-approximation SAs concurrently, fed with the SAME iid sample stream; terminate when the FIRST converges and return its estimate:

```
initialize A_1..A_k with (ε, δ)
while true:
    x ← next_sample()              # simulate CPS model under random scenario
    for l in 1..k:
        s_l ← advanceA_l(s_l, x)   # advance by ONE sample; a few algebraic ops
        if A_l reached stopping condition: return μ̂_l
```

- Sample cost of EAA = min over members ⇒ never worse than the best single SA in hindsight.
- Ensemble overhead ≈ 0: advancing an SA is a few flops vs seconds of simulation per sample (measured: SA module consumes ≥100× faster than 2048 parallel simulators produce).
- Prerequisite: refactor any approximation algorithm into `advance(state, x) → state` form (one sample per call).
- Members used: **EBGStop** (empirical-Bernstein bound c_t = σ̂_t·√(2 log(3/d_t)/t) + 3R log(3/d_t)/t, geometric sampling rate β; lower/upper stopping criterion) and **AA** (Dagum et al. 2000; 3-stage, supermartingale + zero-one estimator theorem; provably optimal for bounded non-negative variables).

## Core Method 2 — HPC-EAA (bias-free parallel sample generation)
Asynchronous Parallel Sample Generator (APSG), a producer–consumer architecture:
- n identical simulators; queue of idle simulator ids; bounded map `{sample_id → KPI value}`.
- Producer: generate random scenario, assign progressive id i, delegate to any free simulator (blocking dequeue if none idle).
- Consumer (`next_sample()`): return the value of id j IN ORDER, blocking until computed; delete entry j, increment j.
- Key invariant: the consumed sample SEQUENCE is identical to a purely sequential run with the same seed — parallelism changes the RATE, not the distribution ⇒ zero bias in the estimate.
- Bounded map gives backpressure; blocking insert when full.

Result: efficiency ~100% (time ∝ 1/n) up to 2048 nodes; deviation from linear production rate < 0.1%.

## Threshold-based verification answer
Given normalized KPI κ: O→[0,1], threshold ϑ, environment (scenario distribution P): approximate μ = E_u[κ(S(u))]. Requirement "μ ≤ ϑ" is verified with confidence ≥ 1−δ iff μ̂/(1−ε) ≤ ϑ. Environment must be finitely parameterizable (scenario = finite parameter vector).

## Experimental results (3 industry-scale Simulink/Stateflow CPS models)
| Case study | Effect |
|---|---|
| Automatic Transmission (AT), Fuel Control System (FCS), Apollo Lunar Module Autopilot (ALMA) | Up to 31,300,400 fewer samples; relative reduction up to 78.73% vs single SA |
| Which SA wins | Unpredictable a priori (depends on KPI stats + seed); varies across case studies — EAA hedges this and also stabilizes sample counts across seeds |
| End-to-end | Sequential estimates: months to many years → hours/few days on HPC |

## Reuse patterns
1. **Ensemble-of-stopping-rules**: whenever multiple (ε, δ)-estimators exist and samples are expensive, race them on a single stream and take the first finisher — cost = min by construction. Applies to any Monte Carlo estimation, not only verification.
2. **Order-preserving parallel sampling**: parallelize ANY iid Monte Carlo workload without statistical bias by tagging samples with progressive ids and consuming strictly in id order.
3. **Producer–consumer with bounded id-map**: backpressure without sample loss.
4. **LTL extension**: probability that a property holds along a random execution is itself a KPI — formula-based properties plug in directly.

## Pitfalls
- AA requires bounded NON-NEGATIVE random variables — normalize the KPI to [0,1] first.
- Over-dimensioned HPC (too many simulators) only wastes compute, never corrupts results; total unused samples remain bounded.
- Map capacity must be bounded to prevent memory explosion; insertion blocks.
- Optimality of each SA is only probabilistic and up to a multiplicative constant — never rely on a single "optimal" SA.
