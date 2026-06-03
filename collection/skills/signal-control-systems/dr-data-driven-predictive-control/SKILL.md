---
name: dr-data-driven-predictive-control
description: "Distributionally Robust Data-Driven Predictive Control (DR-DDPC) methodology for stochastic LTI systems with unknown dynamics and disturbance distributions. Combines subspace predictive control (SPC) with distributionally robust optimization using Wasserstein ambiguity sets. Use when: designing robust controllers under uncertainty, implementing data-driven MPC, handling stochastic disturbances with unknown distributions, or applying distributionally robust optimization to control systems."
---

# Distributionally Robust Data-Driven Predictive Control (DR-DDPC)

## Overview

A methodology for controlling stochastic linear time-invariant (LTI) systems when both the system dynamics and disturbance distributions are unknown. The approach constructs predictive controllers from input-output trajectory data while providing robustness guarantees against distributional uncertainty via Wasserstein ambiguity sets.

**arXiv**: 2605.07589  
**Published**: 2026-05-08  
**Categories**: eess.SY, math.OC

## Core Methodology

### Step 1: Data Collection
Collect a single input-output trajectory `{u_t, y_t}` from the system:
- System: `x_{t+1} = A x_t + B u_t + w_t`, `y_t = C x_t + D u_t + v_t`
- Unknown: A, B, C, D and distributions of w_t, v_t
- Only data required: past input-output pairs

### Step 2: Subspace Predictive Control (SPC) Predictor
Fit the SPC predictor via least squares regression:
```
Y_f = L Z_p + G U_f + E
```
where:
- `Y_f` = future outputs horizon
- `Z_p` = past inputs/outputs (Hankel matrix)
- `U_f` = future inputs horizon
- `L, G` = learned predictor matrices
- `E` = prediction residuals

### Step 3: Empirical Residual Distribution
Construct empirical distribution from prediction residuals:
```
P_N = (1/N) Σ δ_{e_i}
```
This captures the actual disturbance statistics without parametric assumptions.

### Step 4: Wasserstein Ambiguity Set
Define ambiguity set around empirical distribution:
```
B_ε(P_N) = {Q : W_c(Q, P_N) ≤ ε}
```
where W_c is the Wasserstein distance and ε controls robustness level.

### Step 5: Distributionally Robust Optimization
Solve the DR-MPC problem:
```
min_{u} max_{Q ∈ B_ε(P_N)} E_Q[cost(u, ξ)]
s.t. chance constraints satisfied ∀ Q ∈ B_ε(P_N)
```

This ensures performance guarantees even when the true distribution deviates from the empirical one.

## Implementation Pattern

```python
import numpy as np
from scipy.optimize import minimize
from sklearn.linear_model import LinearRegression

def build_spc_predictor(u_data, y_data, past_horizon, future_horizon):
    """Build subspace predictive control predictor from data."""
    # Construct Hankel matrices
    N = len(u_data) - past_horizon - future_horizon + 1
    
    Z_p = np.column_stack([
        np.column_stack([u_data[i:i+past_horizon] for i in range(N)]),
        np.column_stack([y_data[i:i+past_horizon] for i in range(N)])
    ])
    
    U_f = np.column_stack([u_data[i+past_horizon:i+past_horizon+future_horizon] 
                           for i in range(N)])
    Y_f = np.column_stack([y_data[i+past_horizon:i+past_horizon+future_horizon] 
                           for i in range(N)])
    
    # Least squares fit
    X = np.vstack([Z_p, U_f])
    coeffs = np.linalg.lstsq(X.T, Y_f.T, rcond=None)[0]
    
    L = coeffs[:Z_p.shape[0]]  # Past dependence
    G = coeffs[Z_p.shape[0]:]  # Future input dependence
    
    # Residuals
    residuals = Y_f.T - coeffs.T @ X
    
    return L, G, residuals

def wasserstein_radius(residuals, confidence=0.95):
    """Compute Wasserstein radius for given confidence level."""
    N = len(residuals)
    d = residuals.shape[1]
    # Concentration bound (simplified)
    epsilon = np.sqrt((2 * np.log(1/(1-confidence))) / N)
    return epsilon

def dr_mpc_step(L, G, residuals, u_future, z_current, 
                Q, R, epsilon, horizon):
    """Solve distributionally robust MPC step."""
    # Nominal prediction
    y_pred = L @ z_current + G @ u_future
    
    # Robust cost with worst-case expectation
    # Uses duality to convert to tractable form
    nominal_cost = (y_pred @ Q @ y_pred + u_future @ R @ u_future)
    
    # Robustification term (Wasserstein)
    robustness_penalty = epsilon * np.linalg.norm(residuals, axis=1).max()
    
    total_cost = nominal_cost + robustness_penalty
    
    return total_cost
```

## Key Advantages

1. **No model identification needed**: Works directly from input-output data
2. **Distribution-free**: Makes no parametric assumptions on disturbances
3. **Finite-sample guarantees**: Performance bounds scale with √(1/N)
4. **Tractable reformulation**: DR problem reduces to convex optimization
5. **Tunable conservatism**: Wasserstein radius ε controls robustness/performance tradeoff

## When to Use

- System dynamics unknown or poorly identified
- Disturbance distribution non-Gaussian or unknown
- Safety-critical applications requiring robustness guarantees
- Limited data but need statistical performance bounds
- Real-time control with computational constraints

## Activation Keywords

- distributionally robust control
- data-driven predictive control
- Wasserstein MPC
- robust MPC unknown distribution
- subspace predictive control
- stochastic LTI control
- DR-DDPC