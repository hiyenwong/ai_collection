---
name: weighted-regularization-deepc-nonlinear
description: "Data-driven predictive control (DeePC) framework for nonlinear systems that localizes the predictor by weighting data columns according to proximity to the current operating point, retaining the full data matrix and its rank for guaranteed feasibility. Activation: DeePC, data-enabled predictive control, Willems fundamental lemma, nonlinear MPC, weighted regularization, operating-point localization, data-driven control."
version: 1.0.0
created: 2026-07-14
author: Hermes Agent (arXiv 2607.09187)
category: systems-engineering
activation: DeePC, data-enabled predictive control, Willems fundamental lemma, nonlinear MPC, weighted regularization, operating-point localization, data-driven control, two-tank system
---

# Weighted Regularization DeePC for Nonlinear Systems

Extends Data-enabled Predictive Control (DeePC) from linear to **nonlinear** systems by adding a **proximity-weighted regularization** term that localizes the predictor to data near the current operating point — without discarding data or breaking the rank condition that guarantees feasibility.

## When to Use

- You have a **nonlinear plant** and want model-free predictive control (no explicit nonlinear model identified).
- Classic DeePC is unreliable on nonlinear systems because Willems' fundamental lemma (superposition) only holds for linear systems — global data gives poor prediction away from the linear regime.
- You want to keep **all collected data** (preserving rank / feasibility) rather than hard-selecting a local subset.

## Core Idea

DeePC represents future trajectories as a linear combination of past trajectories from a Hankel data matrix. For nonlinear systems this is only locally valid. The fix: weight each data column's contribution in the regularization by its **distance from the current operating point** — near data gets low penalty (used freely), far data gets high penalty (suppressed but still present). This:

- **Localizes** the predictor to the relevant operating region.
- **Retains the full data matrix** (so the rank needed for a non-empty feasible set is preserved — hard subset selection can drop rank and lose feasibility).
- Is **well-posed** by construction (the weighting yields a regularized, solvable QP).

## Methodology (Step-by-Step)

1. **Collect data** u^d, y^d over an informative persistently exciting input on the nonlinear plant → build Hankel matrices U_p, U_f, Y_p, Y_f (past/future, input/output).
2. **At each control step**, observe current past input/output (u_p, y_p) and define the operating point.
3. **Compute column weights** w_i for each data column i: e.g. `w_i = 1 + λ · d(x_i, x_current)` where d is a feature distance (e.g., past-trajectory or operating-point distance) and λ controls localization strength.
4. **Solve the DeePC QP** with the modified regularization:
   `min_{g} || Y_f g − y_f_target ||² + ρ · Σ_i w_i · g_i² `
   s.t. `U_p g = u_p`, `Y_p g = y_p` (consistency with observed past).
   The weighted norm `Σ w_i g_i²` is the localization mechanism.
5. **Apply** the first input of the predicted future; shift and repeat (receding horizon).
6. **Tune λ**: small λ → uses more global data (better rank, less local fit); large λ → strong localization (better nonlinear fit, risk lower effective rank).

## Implementation Guidance

- **Hankel construction**: standard DeePC (see Markovsky/Rapisarda). Use enough columns for persistency of excitation (rank condition).
- **Distance metric d**: choose features that capture the nonlinear operating region — past state/output trajectory, or a low-dim embedding. Normalize features before weighting.
- **QP solver**: any convex QP; the weighted-regularized form stays convex and well-conditioned (weights > 0).
- **Feasibility**: because far data stays in the matrix with large weight (not removed), the column space is preserved → feasible set stays non-empty under the same persistency conditions as linear DeePC.

## Pitfalls

- **Hard data selection** (subset by region) can drop the rank needed for feasibility — prefer soft weighting (keep all, penalize far).
- **λ too large** over-localizes and can still reduce effective rank if near-data is sparse → validate feasibility on the real plant.
- **Distance feature choice** matters: a bad metric localizes to irrelevant data. Validate that near-data actually comes from the same nonlinear regime.
- **Persistency of excitation** of the base dataset is still required — weighting does not fix an under-excited dataset.

## Applications

- Nonlinear process control (two-tank, chemical, thermal) without nonlinear identification.
- Robotics / mechatronics where local linearization is inadequate but data is plentiful.
- Safe retrofitting of existing plants with a data-driven controller.
- Hybrid with formal-spec methods: pair with STL synthesis (see `stl-parameter-synthesis-nonlinear`) by adding STL-style constraints to the DeePC objective.

## Extensions

- Adaptive λ via online estimate of local linearity.
- Kernel/deep feature weighting for strongly nonlinear regimes.
- Combine with disturbance-covariance estimation (cf. adaptive MPPI skill lineage) for robust DeePC under process noise.

## arXiv Metadata

- **ID**: 2607.09187
- **Title**: Data-driven predictive control of nonlinear systems using weighted regularization
- **Authors**: Fritz A. Engeln, Sebastian Zieglmeier, Marta Zagórowska, Jan-Willem van Wingerden
- **Date**: Submitted 10 July 2026
- **Category**: eess.SY
- **Key contribution**: Weighted-norm regularization localizes the DeePC predictor to the current operating point while retaining the full data matrix and rank, guaranteeing feasibility and matching/outperforming hard data-selection on a nonlinear two-tank system.
