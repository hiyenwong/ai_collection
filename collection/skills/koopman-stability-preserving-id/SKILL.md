---
name: koopman-stability-preserving-id
description: "Stability-preserving system identification using Koopman operator lifting with ISS-LMI constraints. Enables data-driven modeling of nonlinear systems (especially Persidskii-class and electromechanical systems) while guaranteeing input-to-state stability. Use when: (1) identifying nonlinear system models from trajectory data, (2) needing stability guarantees in learned models, (3) working with Persidskii systems or sector-bounded nonlinearities, (4) designing robust observers for partially-measured systems, (5) combining data-driven identification with model predictive control."
---

# Stability-Preserving Koopman System Identification

## Overview

Methodology for data-driven system identification that embeds stability guarantees as convex constraints during parameter regression. Combines Koopman operator theory with ISS-LMI analysis for safe learning-based control.

Based on: Pouladi, "Stability Analysis and Data-Driven State Estimation for Generalized Persidskii Systems with Time Delays" (arXiv:2604.27509, 2026)

## Core Concept

### Persidskii System Class

Systems of the form:
ẋ = Ax + Σ f_i(M_i x) + Bw

where f_i are sector-bounded nonlinearities. This class captures:
- Electromechanical systems (motors, actuators)
- Neural networks as dynamical systems
- Systems with saturation/nonlinear feedback

### Stability-Preserving Koopman Lifting

Standard Koopman lifting linearizes nonlinear dynamics in a lifted space:
z = Θ(x)  (lifting functions)
ż = Kz + Lw  (linear dynamics in lifted space)

**Key innovation**: Embed ISS-LMI constraints as convex side conditions during Koopman matrix identification:

min ||ż - Kz - Lw||²  subject to  P > 0, LMI_ISS(K, P) ≤ 0

This ensures the identified model is provably stable.

## Workflow

### Step 1: Choose Lifting Functions

Select observable functions Θ: ℝⁿ → ℝᴺ:
- **Polynomial basis**: [x₁, x₂, x₁², x₁x₂, x₂², ...]
- **Fourier basis**: [sin(ωx), cos(ωx), ...]
- **Radial basis functions**: Gaussian kernels
- **Domain-specific**: Physical energy functions, activation functions

Guideline: N should be large enough to capture dynamics but small enough for tractable LMI.

### Step 2: Collect Trajectory Data

Generate or collect data tuples (x(t), ẋ(t), w(t)):
- Persist data as matrices X, Ẋ, W
- Ensure sufficient excitation for identifiability
- For Persidskii systems: include data near sector boundaries

### Step 3: Solve Constrained Koopman Identification

```python
# Optimization problem:
# min_{K,L} ||Ẋ - K*Θ(X) - L*W||_F²
# s.t. P > 0 (positive definite)
#      AᵀP + PA + ... ≤ 0 (ISS-LMI constraint)
#
# This is a convex SDP if LMI is convex in (K, P)
```

Key LMI condition for ISS:
```
[AᵀP + PA + Q   PB]
[     BᵀP       -γ²I] ≤ 0
```

### Step 4: Design Robust Observer

For partially-measured systems (y = Cx):

Observer: ż̂ = Kẑ + Lw + G(y - ŷ)
          ŷ = CΘ⁻¹(ẑ)

Observer gain G designed via H∞ synchronization criterion:
min ||e||_2 / ||w||_2 ≤ γ

### Step 5: Deploy in MPC

Use identified model for Model Predictive Path Integral (MPPI) control:
- Prediction horizon uses K, L from identified Koopman model
- Stability guaranteed by ISS-LMI constraint
- Handles time-varying delays via Lyapunov-Krasovskii terms

## Implementation Patterns

### Pattern 1: EDMD with Stability Constraint

```python
# Extended Dynamic Mode Decomposition with ISS constraint
import cvxpy as cp

# Data matrices
Z = lifting_functions(X)  # N x M
Z_dot = lifting_functions(X_dot)  # N x M

# Variables
K = cp.Variable((N, N))
P = cp.Variable((N, N), PSD=True)

# Objective: minimize prediction error
obj = cp.sum_squares(Z_dot - K @ Z)

# ISS-LMI constraint
constraints = [
    P >> 0,
    K.T @ P + P @ K + Q << 0,  # Simplified ISS condition
]

prob = cp.Problem(cp.Minimize(obj), constraints)
prob.solve()
```

### Pattern 2: Persidskii-Specific Lifting

For Persidskii systems ẋ = Ax + Σ f_i(M_i x):
- Lifting: Θ(x) = [x, f₁(M₁x), ..., f_k(M_k x)]
- Koopman matrix has structure: K = [[A, I, ..., I], [0, 0, ..., 0], ...]
- Exploit sector bounds: α_i s² ≤ s·f_i(s) ≤ β_i s²

### Pattern 3: Delay-Aware Identification

For time-delay systems:
- Augment state with delayed terms: z_aug = [z(t), z(t-τ)]
- Use Lyapunov-Krasovskii functional with Persidskii integral terms
- LMI includes delay-dependent terms

## Key Formulas

### ISS-LMI for Persidskii Systems

```
[AᵀP + PA + Σ λ_i(M_iᵀM_i)   PB]
[           BᵀP              -γ²I] ≤ 0
```

where λ_i are sector bounds of nonlinearities.

### Observer Error Dynamics

ė = (K - GC)e + Lw

H∞ performance: ||e||₂ ≤ γ||w||₂ guaranteed when:
```
[(K-GC)ᵀP + P(K-GC) + I   PL]
[          LᵀP            -γ²I] ≤ 0
```

## Validation Metrics

1. **Prediction accuracy**: RMSE between predicted and actual trajectories
2. **Stability margin**: Largest γ satisfying ISS-LMI
3. **Observer performance**: Estimation RMSE vs. benchmark (EKF)
4. **Control performance**: Tracking accuracy vs. baseline (FOC)

Expected results (from paper): 35% RMSE reduction vs EKF, 67% tracking improvement vs FOC.

## When to Use

- **Use this method**: Nonlinear systems with sector-bounded nonlinearities, need stability guarantees
- **Avoid**: Strongly chaotic systems where Koopman spectrum is ill-conditioned
- **Alternative**: Neural ODEs for systems without sector structure (but no stability guarantee)

## Related Methods

- Extended Dynamic Mode Decomposition (EDMD)
- Neural ODEs / Neural SSMs
- Linear Parameter-Varying (LPV) identification
- Set-membership identification
