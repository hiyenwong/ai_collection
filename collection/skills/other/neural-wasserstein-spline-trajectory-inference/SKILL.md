---
name: neural-wasserstein-spline-trajectory-inference
description: Trajectory inference from unpaired snapshots (NWSP method).
trigger_words: trajectory inference, unpaired snapshots, single-cell dynamics, Wasserstein spline, population acceleration
category: ai_collection
---

# Neural Wasserstein Splines (NWSP): Representation-Invariant Second-Order Priors for Trajectory Inference

**Source**: Banerjee, Lee, Moosmüller (UNC Chapel Hill), arXiv:2610.19878 (Oct 2026), cs.LG/stat.ML
**Code**: https://github.com/amartya21/Neural-Wasserstein-Splines.git

## Problem

Population dynamics (e.g., single-cell differentiation) are observed as **unpaired snapshots** — destructive assays mean cells measured at different times cannot be matched. Trajectory inference must produce a continuous curve of distributions ρ_t interpolating the snapshots, and the *prior* on motion between them determines the answer.

**Key insight**: a penalty on the acceleration of *sampled particles* is a prior on *joint particle paths*, but unpaired snapshots do not identify particles. The same marginal curve admits many particle representations with wildly different acceleration costs — a stationary Gaussian cloud can be re-represented as a rigidly rotating cloud with E‖Ẍ‖² = 2ω⁴ > 0 while the population acceleration a_t = 0. A particle-acceleration penalty therefore penalizes an arbitrary modeling choice.

## Core mechanism (three stages)

### 1. Spline generator (no integration, no cross-time OT)
A network C_θ: R^{d_z} → R^{J×d} maps latent Z to **J cubic B-spline control points**; the whole particle path is

    X_t = Σ_j B_{j,3}(t) C_θ(Z)_j,  ρ_t = Law(X_t)

with clamped cubic basis and interior knots at observation times. One forward pass gives positions X_t, velocities U_t = Ẋ_t, and accelerations W_t = Ẍ_t **analytically** — no velocity measurements, no ODE integration, no OT couplings between snapshots. Randomness over Z induces the marginal; a fixed Z gives a deterministic C² path.

### 2. Population velocity by ridge projection onto potential gradients
Fix a dictionary of M scalar potentials f_1..f_M; stack gradients F(x) = [∇f_1 … ∇f_M]. Fit the population velocity

    v_M(t,x) = F(x)c(t),  (A + λI)c = b

where A = E[F(X_t)ᵀF(X_t)], b = E[F(X_t)ᵀ U_t]. This is Action Matching's least-squares objective restricted to span{∇f_j}, solvable as ridge regression at each t — the continuity equation's weak form E[d/dt f(ρ_t)] = E[∇f·v_t] supplies b_j in closed form because the generator provides particle velocities.

### 3. Differentiate the projection IN TIME → population acceleration
The regression moments move with the population: Ȧ = E[ḞᵀF + FᵀḞ], ḃ = E[ḞᵀU_t + FᵀW_t], with Ḟ = D_xF(X_t)[U_t] (chain rule along generated paths). Differentiating (A+λI)c = b at **fixed dictionary and λ**:

    ċ = (A+λI)⁻¹(ḃ − Ȧc),      a_M(t,x) = F(x)ċ + D_xF(x)[F(x)c]·c

The **moving-Gram correction −Ȧc is essential**: dropping it adds (A+λI)⁻¹Ȧc, which converges to Π_{ρt}(∂_tρ_t/ρ_t)v_t — a field that need NOT vanish even for stationary marginals, so enlarging the dictionary cannot repair the omission (uncorrected error 0.577 vs ~7e−14 corrected on the analytic test curve; refining velocity resolution does not help).

**Do NOT project the particle acceleration W_t the way U_t was projected** — W_t measures rotation-like unidentifiable motion (nonzero in the rotating-Gaussian case where the marginal is stationary). The population acceleration is the time derivative of the fitted velocity field, not a projection of particle accelerations.

## Loss

    L(θ;F) = L_fit + λ_a·E(θ;F)/L²,  L_fit = (1/|R|)Σ_k [S_ε(ρ_tk, ρ̂_tk) + γ·MMD²]

S_ε = debiased Sinkhorn divergence; MMD = Gaussian kernels; L² = fixed pooled RMS radius. Warm up the generator on L_fit, then ramp λ_a from 0 (schedule matters; gains are heterogeneous and depend on the regularization range).

Use **two independent latent minibatches**: one to estimate moments (A, b, Ȧ, ḃ), a second to evaluate the energy Ê = mean‖â_M(t, X̃)‖² — never evaluate on the same particles that defined the fit. Per step: sample times T + snapshot minibatches → (optional ψ update) → estimate moments, factorize Ĥ = Â+λI once, reuse factorization for Ĥĉ̇ = ḃ−Ȧĉ → evaluate â_M on fresh batch → update θ minimizing L_fit + λ_a Ê/L², differentiating through BOTH linear solves.

## NWSP-N: learned potentials

Fixed linear/quadratic/sinusoidal dictionaries cannot see shape changes preserving mean and variance (Gaussian-mixture counterexample in §C.5 reports zero acceleration for a changing distribution). NWSP-N adds K neural potentials g_ψ: R^d → R^K, augmenting F with ∇g_ψ,j. **Alternating updates**:

- **ψ-step** (θ fixed): maximize normalized explained velocity energy Q(ψ;θ) = ∫₀¹ J_r(ψ,t)/max(E‖U_t‖², ε_U) dt, where J_r = bᵀ(A+λI)⁻¹b = ‖v_t‖²_{ρt} − min_q‖v_t − F_ψ q‖²_{ρt} + λ‖q‖². Normalizing by particle-speed scale prevents fast times from dominating; RMS-normalize learned gradient features to control scaling.
- **θ-step** (ψ and scales fixed): fit snapshots + penalize acceleration. **Never minimize the acceleration penalty w.r.t. ψ** — features that fail to represent the motion would make the measured acceleration artificially small.

Representation invariance (Prop 1) holds for any *fixed* dictionary (including frozen learned ones) but not for the full alternating procedure (the ψ-objective is normalized by a path-dependent energy).

## Theory (what is and isn't guaranteed)

- **Prop 1 (representation invariance)**: for fixed dictionary + λ>0, two lifts satisfying regularity (R) and inducing the same marginal curve yield identical A, b, Ȧ, ḃ, hence identical v_M, a_M, and population acceleration energy. All four moments are population averages — no particle identity. Invariance is a *population* statement; finite batches deviate (projected energy varied ≤2.3% vs raw particle energy blowing up 1.42 → 1.45×10⁵ under latent rotation).
- **Thm 2 (moment-error sensitivity)**: acceleration error bounded by errors in all four moments A, b, Ȧ, ḃ — not just the velocity fit — because acceleration involves time AND space derivatives of the velocity error.
- **Thm 3 (Fourier rates)**: on periodic positive densities with Sobolev regularity s > 1+d/2 and ridge λ_N = O(N^{−s}): velocity error O(N^{−s}), acceleration error O(N^{1−s}). Rates cover neither the trained generator nor the learned dictionary.

## Empirical profile (16 dataset-protocol settings, W1 to withheld snapshots)

- vs WLR, 4-point subdivision, CFM/OT-CFM/SB-CFM, [SF]²M, MFM: **NWSP top-2 in 11/16** (best 5), NWSP-N top-2 in 9/16 (best 4). Largest wins on Circular Gaussian (0.427 vs 0.886 best baseline MFM) and Dyngen Cycle; embryoid body 0.397 → 0.350/0.351; CITE-seq (d=100) 30.55/30.53 vs 31.07 best baseline.
- **Penalty ablation**: acceleration prior improves spline-only in 13/16 (median −2.2% W1; embryoid body 0.450→0.350, Petal 0.153→0.090). Gains concentrate in a few settings; spline C² smoothness alone ≠ the prior.
- **Projected vs raw particle acceleration penalty**: W1 lower in 11/16 with projection; median +0.8% for raw. Supports neither universal advantage nor equivalence — their geometric distinction needs a test holding the marginal fixed while changing paths.
- **NWSP-N dictionary adaptation**: on analytic reference flows, relative acceleration error 0.705 → 0.062 (d=2), 0.975 → 0.341 (d=30) after 300 potential updates; learned beats +16 ridge features and +16 untrained neural potentials at matched size; longer optimization > larger block. Error grows with dimension (d=100 uses 5186 fixed features).
- Full-snapshot minibatch training (exact-transport baselines need 1000-point subsampling on 3 datasets) is a **coverage** advantage, not a measured speedup.

## When to use / pitfalls

- Use when: unpaired snapshots (scRNA-seq lineage trajectories, CITE-seq, dyngen sims), need for provable invariance of the regularizer, sampling at arbitrary t without integration.
- Pitfalls: (1) fixed low-order dictionaries are blind to higher-moment shape changes — use NWSP-N when distributions change shape, not just mean/covariance; (2) forgetting −Ȧc silently biases acceleration (persistent under dictionary refinement); (3) evaluating acceleration on the moment-estimation batch (reuse a factorization but draw fresh evaluation particles); (4) claiming finite-batch invariance — Prop 1 is exact only in expectation; (5) short-curve single-sample metrics are unstable — score with W1 to withheld full snapshots.

## Relationship map

- Action Matching / Wasserstein Lagrangian Flows (Neklyudov et al.): NWSP's velocity fit is AM restricted to a finite gradient span with closed-form b via generator velocities; the new step is the time-differentiated projection.
- Intrinsic Wasserstein splines (Benamou 2019; Justiniano 2024): same intrinsic acceleration target; NWSP is sample-based, no OT between snapshots, no repeated geodesic averaging.
- SplineFlow / MMFM: splines as flow-matching *targets*; NWSP uses the spline as the *generator* directly.

## Activation

trajectory inference, unpaired snapshots, single-cell dynamics, population acceleration, Wasserstein spline, representation invariance, Sinkhorn, flow matching alternative, B-spline generator
