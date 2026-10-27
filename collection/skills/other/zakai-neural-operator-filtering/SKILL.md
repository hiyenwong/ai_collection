---
description: Use when filtering latent SDEs via the Zakai equation
name: zakai-neural-operator-filtering
category: ai_collection
version: 1.0
author: neuro-cron-2026-10-27
license: MIT
metadata:
  hermes:
    tags: [zakai-equation, nonlinear-filtering, neural-operator, pino, deepoonet, latent-sde, state-inference, expectation-maximization, fokker-planck, c-elegans, neural-dynamics, bayesian-filtering]
    related_skills: [gate-feature-importance-ablation-audit, latent-neural-dynamics-ml-survey, neural-ode-mean-field-training, spatiotemporal-tdann, fits-interpretable-spiking-neuron]
---

# ZENO: Zakai-Equation Neural Operators for Nonlinear Filtering of Latent Neural Dynamics

Methodology from arXiv:2610.32926 — "ZENO: Nonlinear filtering with Zakai Equation Neural Operators" (Aaditya Prasad, Steven W. Flavell [MIT Picower/HHMI], Brian DePasquale [BU]; cs.LG/q-bio.NC, 23 Oct 2026).

## One-Line Summary

The exact Bayesian filtering posterior of a latent SDE is governed by the **Zakai SPDE** — Fokker–Planck propagation between observations × multiplicative likelihood jumps at observations — and ZENO learns its SOLUTION OPERATOR with a physics-informed DeepONet (PINO): a causal GRU encodes the observation history into context, a branch×trunk net outputs the unnormalized log-density at ANY latent point and time (mesh-free), trained with a Fokker–Planck residual loss + a Zakai jump (measurement-update) cross-entropy + initial-condition loss, alternated EM-style with closed-form M-step refits of drift/diffusion/readout — reaching the Bayes-optimal filter's ceiling on double-well/VDP and recovering C. elegans whole-brain locomotion limit cycles.

## When to Use / Activation

- Inferring latent dynamical states from noisy neural population recordings (calcium imaging, spikes→rates) WITHOUT imposing a Gaussian/unimodal posterior or a linear/switching-linear dynamics.
- Learning SDE parameters (drift, diffusion, observation map) jointly with state inference when no ground-truth latent is available.
- You need non-Gaussian/multimodal filtering posteriors (decision-making bistability, discrete attractors like C. elegans forward/backward locomotion).
- Benchmarking latent-SDE methods: use the grid Zakai solver as the Bayes-optimal reference on low-dim systems (it IS the exact filter).
- Choosing between filtering (online, causal) vs smoothing (offline, uses future) formulations.

## Core Machinery

**Problem.** Latent dz = f(z)dt + g dW; observations x_k = C z_{t_k} + d + ε, ε~N(0,R), m≥n; estimate filtering posterior p(z_t | X_{[0,t]}) and parameters ϕ={f,g,C,d,R}.

**Zakai recursion (discrete obs).** Unnormalized density ρ evolves as: between observations ρ ← e^{Δt·L*}ρ (forward Kolmogorov/Fokker–Planck); at each observation ρ ← ρ·p(x_k|z) (multiplicative likelihood). Normalizing constant = evidence. Zakai (1969) is the linear SPDE analog of Kushner–Stratonovich; its solution IS the exact filter (Kalman–Bucy = special case).

**ZENO architecture.** Causal GRU on (x_t⊙m_t, m_t) (m = observation mask) → context v_t; DeepONet: log ρ_θ(z, t+sΔt | X_{[0,t]}) = β + b(v_t,s)ᵀψ(z), s∈[0,1]; branch = 1-hidden tanh MLP, trunk = 3-hidden softplus MLP → mesh-free density queryable at ANY z. Drift f_φ = MLP; scalar diffusion g_φ; readout C_φ on the Stiefel manifold (orthonormal columns, CᵀC=I) + diagonal R.

**E step (fit ρ_θ, hold ϕ).** SGD on l_E = w_res·l_res + l_jump + l_ic with fresh mesh-free collocation points per step drawn from a defensive Gaussian mixture: half around the projection ẑ_t = Cᵀ(x_t−d), half from a broad N(0,·) at the origin (Hesterberg defensive sampling). l_res = scale-normalized squared Fokker–Planck residual of log ρ_θ between observations; l_jump = cross-entropy implementing the Zakai measurement update (posterior-after-obs must equal predicted-density × likelihood); l_ic matches p(z_0|x_0) under N(0,I) prior. Local normalization by self-normalized importance sampling over collocation points (Zakai is UNnormalized — never skip this). Posterior means via MALA on the learned log-density.

**M step (fit ϕ, hold ρ).** In order: (1) Stiefel readout (C,d) by orthogonal Procrustes; (2) drift f_φ regressed on increments of posterior means z̄_t; (3) scalar diffusion g_φ from residual increments; (4) R from observation-space directions orthogonal to span(C). Initialize C, f, ẑ by subspace identification (Van Overschee–De Moor) — critical for good local optima.

## Key Results

- Double-well (bimodal posterior): ZENO reaches the Bayes-optimal grid-filter ceiling; VDP also at ceiling; Lorenz within ~0.005 NRMSE of optimal.
- Drift learning ≈ SING/gpSLDS (double-well) and ≈ SDE-matching (VDP) — SOTA parity while providing the FULL posterior, not just moments.
- C. elegans whole-brain calcium (Kato 2015): recapitulates forward/backward locomotion limit cycles; latents consistent with behavioral labels; comparable forecasting RMSE; slightly lower reconstruction R² than smoothers (expected — filters see less information) attributed to the Stiefel constraint.
- No KL-to-prior term → no posterior-collapse failure mode of latent-SDE VAEs; the physics loss replaces the prior-matching term.

## Protocols

### P1 — Exact-filter ground truth (low-dim benchmark)
Grid-solve the Zakai recursion: donor-cell upwind Fokker–Planck sub-steps + multiplicative likelihood updates; cross-check vs bootstrap particle filter. Use as the ceiling when judging any approximate filter (this is the paper's own reference and is verified below).

### P2 — ZENO-style application to neural data
GRU context → DeepONet density → E/M alternation; extract posterior means (MALA), inspect multimodality; compare reconstruction R², forecasting NRMSE, and BEHAVIORAL DECODING of latents (not just R²) against gpSLDS/SDE-matching baselines.

### P3 — Reading the posterior
Check whether filtering posteriors are multimodal before trusting Gaussian/SLDS baselines; report mode structure (attractor occupancy) as the scientific output, not just RMSE.

## Pitfalls

- Grid/numerical Zakai solvers scale exponentially in latent dimension — the whole point of the operator approach; keep grids for n≤2-3 benchmarks only.
- Explicit-Euler FP propagation on a grid needs dt ≤ min(dz²/(g²), dz/max|f|) — overflow otherwise (replay-tested: dt=1e-3 with dz=0.0125, g=0.7 diverges; dt=1e-4 stable). Use donor-cell interface fluxes, never periodic wrap-around differences.
- The unnormalized Zakai mass must be re-normalized locally (self-normalized IS); log-mass accumulates the log-evidence — monitor it for stability.
- All baselines (gpSLDS, SDE-matching) estimate the SMOOTHING distribution — a pure filter sees less; expect slightly lower R² and compare forecasting/decoding instead.
- Single global parameter set struggles with multi-regime data (C. elegans turns) — consider Lévy/jump generalizations or regime mixtures.
- Stiefel readout constrains reconstruction; relaxing it is the paper's own named future fix.

## Connections

- Latent-dynamics-for-neuroscience program (Durstewitz; Saxena–Cunningham): ZENO gives the exact-filter view of the same inference problem.
- gpSLDS/SING (Linderman; Hu) and simulation-free SDE-matching (Bartosh): variational alternatives — compare against the Zakai-optimal ceiling, not just against each other.
- PINO/PINN lineage (Raissi; Wang; Li/Lu): the residual-plus-jump loss is the SPDE-compatible variant — the jump term is what standard PINN pipelines miss for discontinuous measurement updates.
- C. elegans attractor literature (Kato 2015; dLDS Yezerets 2025): ZENO recovers limit cycles WITHOUT discrete switching states.

## Verification (replay, 2026-10-27)

scripts/test_zakai_skill_20261027.py — implements the paper's Bayes-optimal reference on a 1D double-well SIS... (double-well SDE dz = 4z(1−z²)dt + 0.7dW, obs every Δt=0.1, σ_obs=0.8, 401-point grid):
- T1 PASS — single measurement update from N(0,1) prior matches closed-form product-of-Gaussians (mean err 0.0007, var err 0.0015).
- T2 PASS — grid-Zakai filter vs 20k-particle bootstrap PF over 50 observations: posterior-mean RMSE = 0.0035; both track truth (final z: true 1.009, Zakai 1.003, PF 1.002).
- T3 PASS — weak/sparse observations (σ=2.5): filtering posterior is bimodal with modes at ±1.0 (the two wells), the paper's motivating non-Gaussian case.
- T4 PASS — accumulated log-evidence (log Zakai mass) finite: −69.4.
- Instability lesson recorded: naive explicit FP stepping (dt=1e-3) diverges; interface-flux form with dt=1e-4 is stable and exact-to-PF.
