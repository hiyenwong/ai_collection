---
name: residual-conservative-mpc
description: "Residual-Conservative MPC (RC-MPPI) framework — adaptive safety modulation for sampling-based model predictive control using prediction-execution residuals. Combines residual-dependent constraint tightening, adaptive safety-cost shaping, and residual-adaptive sampling. Use when designing safety-critical MPC systems with model uncertainty."
---

# Residual-Conservative MPC (RC-MPPI)

## Core Concept

When model-plant mismatch exists in sampling-based MPC (e.g., MPPI), fixed constraint penalties don't adapt. RC-MPPI modulates safety conservatism **online** using the **prediction-execution residual** — the difference between predicted and actual system behavior.

## Three Coupled Mechanisms

### 1. Residual-Dependent Constraint Tightening
- Compute rolling residual: `r(t) = ||x_predicted(t) - x_actual(t)||`
- Tighten constraints proportional to residual magnitude
- `constraint_bound(t) = nominal_bound - k * r(t)` where k is a safety margin coefficient

### 2. Adaptive Safety-Cost Shaping
- Shape the cost function to penalize constraint violations more aggressively when residual is high
- `safety_cost = base_cost * (1 + alpha * r(t))`
- Alpha controls sensitivity to residual

### 3. Residual-Adaptive Sampling Modulation
- **Key insight**: When model is inaccurate, rollout cost evaluations are unreliable
- **Increase temperature** when residual grows — reduces overcommitment to apparent cost rankings
- `temperature(t) = base_temp * (1 + beta * r(t))`
- Exploration contracts and temperature relaxes as residual increases

## Implementation Pattern

```python
def rc_mppi_step(state, model, cost_fn, constraints, residual_history, 
                  base_temp=1.0, base_alpha=0.5, base_beta=0.3, n_samples=1000):
    """Residual-Conservative MPPI control step."""
    
    # 1. Compute current residual
    if len(residual_history) > 0:
        current_residual = np.mean(residual_history[-10:])  # rolling window
    else:
        current_residual = 0.0
    
    # 2. Adaptive parameters
    temp = base_temp * (1 + base_beta * current_residual)
    alpha = base_alpha * (1 + current_residual)
    
    # 3. Constraint tightening
    tightened_constraints = tighten_constraints(constraints, current_residual)
    
    # 4. Sample trajectories with adaptive temperature
    trajectories = sample_trajectories(model, state, n_samples, temp)
    
    # 5. Evaluate costs with adaptive safety shaping
    costs = []
    for traj in trajectories:
        base = cost_fn(traj)
        safety = compute_safety_violation(traj, tightened_constraints)
        costs.append(base * (1 + alpha * safety))
    
    # 6. Compute control via importance weighting
    weights = np.exp(-np.array(costs) / temp)
    weights /= weights.sum()
    
    control = sum(w * traj.control[0] for w, traj in zip(weights, trajectories))
    
    return control, tightened_constraints, temp

def tighten_constraints(constraints, residual, k=0.5):
    """Tighten constraint bounds based on residual magnitude."""
    tightened = {}
    for name, bound in constraints.items():
        tightened[name] = bound * (1 - k * min(residual, 0.9))
    return tightened
```

## Theoretical Guarantees

Under **Lipschitz dynamics** and **sub-Gaussian disturbances**:
- Probabilistic bounds on constraint violation derived
- Joint effect of adaptive mechanisms reduces violation probability as residual grows
- Model-plant mismatch perturbs MPPI importance weights proportional to residual magnitude and inversely with temperature

## When to Use

- Sampling-based MPC with significant model-plant mismatch
- Systems where safety constraints are critical and model accuracy varies
- Robotics, autonomous vehicles, industrial process control
- Any MPPI/MPPI-like algorithm where fixed penalties underperform

## Activation
residual-mpc, rc-mppi, adaptive safety mpc, model-plant mismatch, prediction-execution residual, sampling-based mpc, temperature adaptation mpc