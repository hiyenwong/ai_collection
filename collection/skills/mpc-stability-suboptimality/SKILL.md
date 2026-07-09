---
name: mpc-stability-suboptimality
description: Model Predictive Control (MPC) stability and suboptimality analysis under plant-model mismatch. Covers discounted and undiscounted infinite-horizon optimal control, stability guarantees with model uncertainty, and suboptimality bounds. Use when analyzing MPC robustness, handling model-plant mismatch in control systems, or implementing robust MPC controllers.
---

# MPC Stability and Suboptimality Under Plant-Model Mismatch

## Overview

This skill provides theoretical foundations and practical guidance for implementing robust Model Predictive Control (MPC) when the model differs from the real plant. It covers stability guarantees, suboptimality bounds, and the tradeoff between horizon length, discounting, and model mismatch.

## Key Concepts

### Plant-Model Mismatch

When the surrogate model used for MPC differs from the actual plant dynamics:
- **Model uncertainty bounds**: Proportional to states and controls
- **Equilibrium preservation**: Origin remains an equilibrium under mismatch
- **Continuity requirements**: Model and cost-controllability assumptions

### Discounted vs. Undiscounted Scenarios

**Discounted Control**:
- Running cost: `γ^k * q(x_k, u_k)` with discount factor `γ ∈ (0, 1)`
- Infinite-horizon cost: finite even with undiscounted stage cost
- Less conservative for long horizons

**Undiscounted Control**:
- Running cost: `q(x_k, u_k)` without discounting
- Requires stability for finite infinite-horizon cost
- More sensitive to horizon length

### Stability Guarantees

**Exponential Stability Conditions**:
1. Model continuity at equilibrium
2. Cost-controllability property
3. Plant-model mismatch bounds
4. Uniform guarantees over horizon length

**Key Insight**: Larger horizons do NOT require successively smaller mismatch bounds - robustness is uniform.

### Suboptimality Analysis

**Closed-Loop Cost Bound**:
- Recovers optimal cost of surrogate model
- Tradeoff: Horizon length vs. Discount factor vs. Mismatch size
- Quantifies performance loss from model error

## Framework

### Unified Quadratic Cost Framework

```python
# General MPC formulation
def mpc_cost(x_sequence, u_sequence, model, gamma):
    total_cost = 0
    for k in range(horizon):
        stage_cost = q(x_sequence[k], u_sequence[k])
        total_cost += (gamma ** k) * stage_cost
    
    # Terminal cost for stability
    if terminal_constraint:
        total_cost += terminal_cost(x_sequence[-1])
    
    return total_cost
```

### Plant-Model Mismatch Assumption

```
||f_plant(x, u) - f_model(x, u)|| ≤ α * ||x|| + β * ||u||

where:
- f_plant: actual plant dynamics
- f_model: surrogate model dynamics
- α, β: mismatch bounds (proportional to states and controls)
```

### Stability Analysis Procedure

1. **Check continuity**: Model continuous at equilibrium
2. **Verify cost-controllability**: Can drive cost to zero from any state
3. **Compute mismatch bounds**: α and β parameters
4. **Select horizon**: Tradeoff with computational limits
5. **Set discount factor**: If using discounted formulation

## Design Tradeoffs

### Horizon Length vs. Mismatch Bounds

**Tradeoff**: 
- Longer horizon: Better optimality, same stability robustness
- Mismatch bounds: Uniform stability guarantees
- **Insight**: Robustness doesn't degrade with longer horizons

### Discount Factor Effects

```
Discount factor γ affects:
- Cost finiteness: γ < 1 ensures finite infinite-horizon cost
- Conservatism: Lower γ reduces sensitivity to distant future
- Tradeoff: γ vs. horizon length for optimal performance
```

### Suboptimality vs. Stability

**Suboptimality Bound**:
- Quantifies deviation from surrogate optimal cost
- Depends on mismatch size and horizon/discount choices
- Provides performance guarantee under uncertainty

## Practical Implementation

### Robust MPC Design Steps

1. **Model Selection**:
   - Choose surrogate model close to plant behavior
   - Estimate mismatch bounds from data
   - Ensure equilibrium preservation

2. **Cost Function Design**:
   - Quadratic costs: Easy to analyze
   - Terminal cost: For stability guarantees
   - Stage cost: Reflect true objectives

3. **Horizon and Discount Selection**:
   - Horizon: Balance computation vs. optimality
   - Discount: Consider long-term vs. short-term goals
   - Tradeoff: Use analysis to guide selection

4. **Implementation**:
   - Online optimization at each timestep
   - Handle constraints explicitly
   - Warm-start from previous solution

### Implementation Code Pattern

```python
class RobustMPCController:
    def __init__(self, model, horizon, gamma, mismatch_bounds):
        self.model = model
        self.N = horizon
        self.gamma = gamma
        self.alpha, self.beta = mismatch_bounds
        
    def solve(self, current_state):
        # Solve finite-horizon optimization
        optimal_sequence = self.optimize(current_state)
        
        # Apply first input
        u0 = optimal_sequence[0]
        
        # Stability check (optional)
        if self.check_stability(current_state, u0):
            return u0
        else:
            return self.fallback_action(current_state)
    
    def optimize(self, x0):
        # Formulate and solve optimization problem
        # minimize: sum_{k=0}^{N-1} γ^k * q(x_k, u_k)
        # subject to: x_{k+1} = f_model(x_k, u_k)
        return self.solve_qp(x0)
```

## Applications

### Process Control
- Chemical reactors with uncertain kinetics
- Heat exchangers with varying parameters
- Batch processes with model drift

### Autonomous Systems
- Vehicle control with uncertain dynamics
- Drone navigation with wind uncertainty
- Robot manipulation with load changes

### Energy Systems
- Power grid control with demand uncertainty
- Building HVAC with thermal model mismatch
- Battery management with degradation uncertainty

## Mathematical Results

### Exponential Stability Theorem

Under plant-model mismatch bounds and cost-controllability:
- Closed-loop origin is exponentially stable
- Rate depends on model properties and mismatch bounds
- Guarantee uniform over horizon length N

### Suboptimality Bound

Closed-loop cost satisfies:
```
J_closed_loop ≤ J_optimal_surrogate * (1 + ε(mismatch, horizon, gamma))

where ε quantifies suboptimality from model error
```

### Key Lemma: Uniform Robustness

For any horizon N, stability guarantee depends only on:
- Mismatch bounds (α, β)
- Cost-controllability constant
- Model continuity

NOT on horizon length.

## References

- Paper: arxiv:2604.08521v1
- PDF: https://arxiv.org/pdf/2604.08521v1
- Authors: Robert H. Moldenhauer, Karl Worthmann, Romain Postoyan, Dragan Nešić, Mathieu Granzotto
- Categories: math.OC, eess.SY
- Published: 2026-04-09

## Related Skills

- `adaptive-distributionally-robust-control`: Distributional uncertainty in control
- `stein-variational-uncertainty-mpc`: Particle-based uncertainty MPC
- `agentic-fast-slow-planning`: Integration with real-time control

## Further Reading

For detailed mathematical proofs:
- See paper Section 3: Stability analysis
- See paper Section 4: Suboptimality bounds
- See paper Section 5: Tradeoff analysis

---

**Date Created**: 2026-04-10
**Paper Source**: arxiv weekly systems engineering search