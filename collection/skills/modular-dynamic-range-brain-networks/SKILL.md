---
description: Use when measuring dynamic range in hierarchical brain nets
name: modular-dynamic-range-brain-networks
category: ai_collection
version: 1.0
author: neuro-cron-2026-10-27
license: MIT
metadata:
  hermes:
    tags: [modular-dynamic-range, hierarchical-modular-networks, griffiths-phase, intrinsic-timescales, critical-brain, sis-model, heterogeneity, functional-specialization, dynamic-range, brain-networks]
    related_skills: [griffiths-phase-brain-criticality, hierarchical-brain-criticality, efficient-coding-criticality, warped-hierarchical-modular-neural-network, minimal-network-brain-dynamics-mean-field, chaotic-griffiths-phase-neuron-map-networks]
---

# Modular Dynamic Range: Heterogeneity as the Engine of Hierarchical Brain Computation

Methodology from arXiv:2610.32328 — "From Heterogeneity to Function: Enhanced Modular Dynamic Range in Hierarchical Brain Networks" (Filipe V. Torres, Mauro Copelli, Leonardo L. Gollo; UFPE Recife + IFISC + Monash Turner Institute; q-bio.NC/cond-mat.dis-nn/nlin.AO, 23 Oct 2026).

## One-Line Summary

Hierarchical-modular networks (HMN) with heterogeneous (sparse) connectivity spontaneously generate: (i) an extended Griffiths-like critical regime with NO fine-tuning, (ii) a hierarchy of intrinsic neural timescales (INT) that grows with hierarchical level, and (iii) a new measurable — **modular dynamic range** Δ_module — which under LOCAL stimulation peaks when the stimulus hits intermediate hierarchical levels (ℓ′=h/2), giving functional specialization a structural mechanism instead of a tuned critical point.

## When to Use / Activation

- Simulating excitable dynamics on hierarchical-modular connectomes and asking WHERE criticality, timescales, or stimulus sensitivity live (which module/level — not just the global average).
- Designing stimulation protocols (TMS/DBS/optogenetics analogues): choosing the spatial EXTENT of input to maximize network-wide discriminability.
- Testing Griffiths-phase / rare-region claims with a concrete per-module measurement protocol (firing-rate CV, module response curves, module INT).
- Explaining INT hierarchies (Murray/Basset line) from structure alone, without tuned criticality.
- Any dynamic-range study currently using only the global measure — this paper's point is that Δ is module-resolved and stimulus-extent-resolved.

## Core Machinery

**HMN construction (Moretti–Muñoz).** N = M0·m^(h−1) nodes; m modules per level, h hierarchical levels, M0 innermost-module size. A pair whose smallest common container is at depth d (d=0: same innermost module) connects with probability p_d = α·φ^(d+1). α sets the finite network dimension D (N_r ~ r^D via BFS path-length growth; φ>2^−m ⇒ effectively infinite-dimensional). Canonical: M0=6, m=3, h=8, α=2, φ∈{0.125, 0.25, 0.5}. Analytic mean in-degree law: E[k] = (M0−1)αφ + Σ_{d=1}^{h−1} M0·m^(d−1)(m−1)·α·φ^(d+1) → reproduces the paper's Table 2 exactly (E[k] = 1.9 / 7.7 / 198; CV_k = 0.67 / 0.33 / 0.068; modularity 0.97/0.81/0.32).

**Dynamics (SIS excitable automaton, δt=1 ms).** Node resting/excited; excited by external Poisson stimulus (rate r; per-step prob η(r)=1−e^(−r)) or by each active neighbor independently (prob p). Control parameter λ = ρ(pA) (spectral radius of p·A). Order parameter F0 = spontaneous activity; continuous (directed-percolation-like) transition at λ≈1 in the homogeneous limit.

**Modular coordinates.** Each neuron carries an (h−1)-tuple of base-m digits with trailing zeros for outer containers ([1,1,1] ⊂ [1,1,0] ⊂ [1,0,0] ⊂ [0,0,0]) — gives exact per-module time series at EVERY level simultaneously.

**Response curves & Δ.** 80 log-spaced r ∈ [1e−7, 1e2] ms⁻¹; T=10⁴ ms, 100 ms transient discarded, 60 trials. F0 fitted from F ≈ a·r^b + c over [r0, 10·r0] (never read F at smallest r directly — smoothing as r→0 biases it). F_x = F0 + x(Fmax−F0); interpolate r0.1, r0.9; Δ = 10·log10(r0.9/r0.1) dB. Apply the SAME pipeline to any module's time series → **Δ_module**; under global stimulus (GRGS), local stimulus (GRLS), or any ℓ′-restricted stimulus.

**INT.** Per-module autocorrelation-decay timescale; INT ↑ with hierarchical level ℓ (deeper = slower); within-level INT spread appears ONLY with connectivity/rate heterogeneity; module INT grows with module Δ (critical slowing ↔ sensitivity link).

## Key Results (mechanisms to look for)

1. Sparsity (φ↓) ⇒ dynamical heterogeneity: near-inactive neurons coexist with hyperactive "islands"; continuum of power-law exponents instead of one; firing rate tracks in-degree (Spearman 0.46/0.85/0.59 for φ=0.125/0.25/0.5).
2. Heterogeneity STRETCHES criticality: power-law F0 decay across a broad λ window (Griffiths phase), mean-field transition criteria break; modules coexist in distinct regimes (subcritical + self-sustained) at the same global λ.
3. Δ_GRLS > Δ_GRGS for heterogeneous nets (local stimulus beats global); REVERSED for homogeneous nets. Unstimulated modules also gain Δ — distributed computational benefit.
4. Non-monotonic optimum: global Δ peaks at intermediate stimulus level ℓ′=h/2 — neither diffuse nor most focal input wins. This is the functional-specialization principle.

## Protocols

### P1 — Modular dynamic-range map
Build HMN (or load connectome; paper: human Q=0.38, mouse Q=0.43, C. elegans Q=0.41) → sweep λ × r → compute global AND per-module Δ at every level → report Δ DISTRIBUTIONS per level (the spread is the finding) → identify the λ window of power-law F0 decay (Griffiths window).

### P2 — Optimal stimulus-extent experiment
Fix λ in the extended regime → stimulate at each ℓ′ ∈ {0,…,h−1} (all nodes … single innermost module) → measure global + modular Δ → verify non-monotonicity with peak at ℓ′≈h/2 and the heterogeneous-vs-homogeneous flip of Δ_GRLS − Δ_GRGS.

### P3 — INT hierarchy extraction
At λ of maximal global INT → per-module ACF decay for every level → INT vs ℓ monotone growth; within-level variance only in heterogeneous nets → correlate module INT with module Δ.

## Pitfalls (incl. verified finite-size caveats)

- **FINITE-SIZE WARNING (replay-tested)**: the Δ_GRLS>Δ_GRGS flip did NOT reproduce at N=486 (h=5) even at λ∈{1.15,1.5,2.0} — local 6-node stimulation cannot recruit the network (local Fmax ≤ 0.11, Δ_local < Δ_global for all φ). The flip is an N≈1.3×10⁴ emergent effect; do not claim it from small simulations. Rate-heterogeneity (CV ordering) DOES reproduce at N=486.
- Mean-field λ_c criteria mis-locate the transition on heterogeneous HMNs — define the Griffiths window empirically (power-law F0 decay range), not by λ=1.
- Fit F0 (a·r^b+c), never use F(r_min) — near the trivial fixed point F smooths as r→0.
- Δ needs r spanning ≳9 decades or r0.9/r0.1 clips at grid boundaries.
- Averaging Δ over modules destroys the result — report distributions.
- φ>2^−m ⇒ infinite-dimensional, mean-field-like; heterogeneity effects need finite-D/sparse φ.
- λ must be defined as spectral radius ρ(pA) — degree-based proxies diverge from it under CV_k>0.3.

## Connections

- Griffiths phase / critical brain without tuning: extends [[griffiths-phase-brain-criticality]] and [[hierarchical-brain-criticality]] from EXISTENCE to a measurable per-module protocol.
- Dynamic-range maximization: Kinouchi–Copelli (2006) prediction → experimental confirmation; here generalized to module- and stimulus-extent-resolved Δ.
- INT hierarchy (Murray/Basset): emerges from structure alone (φ sparsity), no tuning; connect to timescale-hierarchy analyses.
- Brain stimulation planning: ℓ′≈h/2 optimum is directly testable against stimulation-spread data.

## Verification (replay, 2026-10-27)

scripts/test_modulardynrange_skill_20261027.py (N=486, h=5; paper scale N=13122, h=8):
- T1 PASS — HMN law: simulated E[k] = 1.782/6.494/52.93 vs analytic 1.838/6.602/53.75 (≤3% dev); analytic law reproduces paper Table 2 (1.9/7.7/198) exactly at h=8; CV_k = 0.69/0.34/0.12 vs paper 0.67/0.33/0.068.
- T2 PASS — firing-rate CV ordering at λ=1.25: 1.10 > 0.36 > 0.10 (sparse → heterogeneous islands).
- T3 PASS — Δ pipeline (F0 fit + F_x interpolation) runs; global Δ λ-dependence matches the extended-regime story: sparse net Δ grows 19.6→53.7 dB as λ goes 1.15→2.0.
- T4 NEGATIVE — local>global Δ flip NOT reproduced at N=486 (see Pitfalls); requires paper-scale N. Recorded as honest finite-size caveat, consistent with the user's no-negative-result-hiding policy.
