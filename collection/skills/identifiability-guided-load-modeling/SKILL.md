---
name: identifiability-guided-load-modeling
description: Use when calibration parameters confound. Fisher projection.
trigger: composite load model calibration, parameter identifiability, nuisance-projected Fisher information, grey-box estimator, data center load modeling, transient stability, weakly identified parameters
category: ai_collection
---

# Identifiability-Guided Composite Load Modeling (AI Data Centers)

Methodology from arXiv:2610.19565 (Washington State / Argonne, Oct 2026): calibrate grey-box dynamic load models by first deciding **which parameters the data can actually identify**, instead of treating every element as freely estimable.

## Core Problem

AI data centers are large, workload-dependent grid loads (4.4% of US demand in 2023 → 6.7–12% by 2028). Their dynamic model has physically distinct branches — IT, cooling, auxiliary — plus UPS protection gates and reconnect ramps. Freely estimating everything yields **weakly identified or physically confounded parameterizations**: good terminal fit, wrong internal physics.

## Branch-Resolved Model Structure

Composite load with separate calibration elements:
- **IT branch**: workload-modulated power P_IT(V,t,w) = S_IT · Φ[V](t) · g(w(t)), where Φ[V](t) ∈ [0,1] is the prescribed UPS connection factor from voltage history, g(w) is the learnable workload-to-power law.
- **Cooling branch**: mixture of direct-on-line (DOL) induction motors and variable-frequency drives (VFD); share ρ is the key physically meaningful quantity.
- **Auxiliary branch**: remaining facility load.
- **Protection**: UPS voltage threshold gate + externally anchored reconnect-ramp duration (do NOT estimate from electrical data — anchor it from protection settings).

## Theorem 1 — Nuisance-Projected Fisher Identifiability

For observations y ∼ N(µ(ρ,η), R) with target parameter ρ (DOL/VFD share) and nuisance vector η (motor/VFD/initial-state parameters), define whitened sensitivity blocks:

- j_ρ = R^(−1/2) · ∂µ/∂ρ,  J_η = R^(−1/2) · ∂µ/∂η

The information about ρ **after projecting out nuisance directions**:

**I_ρ|η = F_ρρ − F_ρη F_ηη† F_ηρ = ‖(I − J_η J_η†) j_ρ‖²**

(with F blocks the standard Fisher partition; the projection form stays valid even when F_ηη is rank-deficient, via Moore–Penrose pseudoinverse).

**ρ is locally identifiable (first order) iff j_ρ ∉ col(J_η)** — i.e., some component of the ρ-sensitivity cannot be mimicked by nuisance perturbations. When it holds, any regular locally unbiased estimator obeys the CRB: var(ρ̂) ≥ I_ρ|η^(−1).

Practical information (fixed nuisance, M samples, independent P/Q channels): I_ρ = Σ_k C_k² (ΔP_k²/σ_P² + ΔQ_k²/σ_Q²) where ΔP_k, ΔQ_k are DOL-vs-VFD response differences — information comes precisely from the **contrast** between the two motor types' signatures.

## Proposition 2 — Workload Non-Equivalence

Two scenarios with identical grid-side inputs z(t)=[V(t),f(t)] but different workloads w1≠w2 cannot both be matched by any voltage-only model family: the best achievable squared error is lower-bounded by a term ∝ S_IT²·(difference in g(w) integrals). **Consequence: voltage-only recalibration (the standard utility practice) is provably insufficient for workload-dependent loads — workload telemetry is a required input.**

## Calibration Treatment Decision (the reusable pattern)

For each exposed calibration element, choose one of three treatments based on recoverability:
1. **Estimate** — locally identifiable per Theorem 1 with available branch-level measurements (e.g., cooling share ρ, workload law g).
2. **Prescribe** — keep physical law fixed (UPS protection gate Φ[V]).
3. **Externally anchor** — fix from facility/engineering data (reconnect-ramp duration).

Never let a weakly identified quantity float; it will absorb variance and corrupt identifiable ones.

## Grey-Box Estimator Design
- **Univariate KAN construction** for the workload law g(w) — trainable univariate basis enabling later closed-form distillation.
- **Branch-level supervision**: fit terminal (PCC) response AND branch-level cooling observations. Aggregate-only supervision preserves terminal accuracy but **fails to recover cooling composition** — the paper's central negative result.
- **Two-phase training**: phase 1 fits all trainable components jointly; phase 2 refines only the workload law and cooling share.
- **Symbolic distillation**: post-training, convert the learned KAN workload relation into a closed-form expression suitable for transient-stability simulators.

## Results (evaluation anchors)
- 300,000 MIT Supercloud GPU power-utilization samples + 12,600 IEEE 39-bus fault scenarios.
- Aggregate active-power R² 0.948 (vs 0.856 LSTM baseline); 39% RMSE reduction.
- **OOD deep voltage sags (outside training range): transient R² 0.750 vs LSTM's 0.033** — the identifiability structure, not model capacity, drives generalization.
- vs WECC PERC1 aggregate: agrees in 24/27 fault conditions; the 3 divergent cases sit at the cooling-protection boundary where DOL/VFD share shifts the closed-loop retained-load state by up to 0.36 p.u.

## When to Use This Pattern
- Calibrating any composite grey-box model where some parameters are physically confounded (power systems, thermal, building dynamics)
- Deciding measurement requirements before a calibration campaign (does the data contain enough contrast to identify the target?)
- Any setting where terminal-fit accuracy is falsely taken as evidence the internal physics is right
- Grid integration studies of AI/HPC data centers, EV fleets, or other protection-gated loads

## Pitfalls
- **Terminal accuracy is not physical recovery** — aggregate-only training gave good PCC fit with wrong cooling branch and wrong ρ. Always supervise at branch level when physical quantities matter downstream.
- **Anchored ≠ estimated** — externally anchored quantities (ramp durations) must come from protection settings or commissioning data, never regression.
- **Protection-boundary regimes** — models that agree almost everywhere can diverge exactly near relay thresholds; test there explicitly.
- **Rank-deficient F_ηη** — use the projection (pseudoinverse) form; naive inversion of the nuisance Fisher block is numerically unstable.

## Key References
- arXiv:2610.19565 — Lin, Wang, Yue, Zhao; code: github.com/dinglin613/DCLR
- WECC PERC1 load model (2026) — minimum-fidelity aggregate for computational loads
- KAN (Kolmogorov-Arnold Networks, arXiv:2404.19756) — univariate-basis grey-box backbone
