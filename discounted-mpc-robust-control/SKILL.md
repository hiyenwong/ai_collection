---
name: discounted-mpc-robust-control
description: Discounted Model Predictive Control (MPC) and infinite-horizon optimal control under plant-model mismatch. Provides unified framework for analyzing closed-loop stability and suboptimality when using surrogate models that differ from real plants. Based on April 2026 research by Moldenhauer et al. Use when working with MPC robustness analysis, model mismatch scenarios, discount factor optimization, or stability guarantees in control systems.
---

# Discounted MPC and Infinite-Horizon Optimal Control Under Plant-Model Mismatch

Based on the paper "Discounted MPC and infinite-horizon optimal control under plant-model mismatch: Stability and suboptimality" (Moldenhauer, Worthmann, Postoyan et al., 2026).

## Core Contributions

This methodology studies closed-loop stability and suboptimality for MPC and infinite-horizon optimal control when the surrogate model differs from the real plant. Key innovations include:

1. **Unified Analysis Framework**: Stability-suboptimality trade-off analysis based on quadratic lower bounds
2. **Discount Factor Optimization**: Proves existence of optimal discount factor balancing stability and suboptimality
3. **No Full Model Knowledge Required**: Only requires bounds on model differences, not complete system identification

## Methodology Framework

### 1. Problem Setup

**System Dynamics**:
- Real system: $x_{k+1} = f(x_k, u_k)$
- Surrogate model: $x_{k+1} = \hat{f}(x_k, u_k)$

Where $f$ and $\hat{f}$ differ (plant-model mismatch).

**Objective**: Design controller using surrogate model, but apply to real system.

### 2. Discounted MPC Formulation

**Discounted Cost Function**:
$$J_N(x, u) = \sum_{k=0}^{N-1} \gamma^k \ell(x_k, u_k) + \gamma^N V_f(x_N)$$

Where:
- $\gamma \in (0, 1]$ is the discount factor
- $\ell$ is the stage cost
- $V_f$ is the terminal cost
- $N$ is the prediction horizon

**Key Insight**: 
- Smaller $\gamma$ → Better stability (more robust to model mismatch)
- Larger $\gamma$ → Better performance (closer to optimal)

### 3. Stability Analysis

**Assumptions**:
- Model difference between surrogate and real system is bounded
- Cost function satisfies quadratic lower bound condition

**Stability Guarantee**:
There exists a discount factor threshold $\gamma^*$ such that for all $\gamma \in (\gamma^*, 1]$, the closed-loop system is asymptotically stable.

### 4. Suboptimality Analysis

**Performance Loss Upper Bound**:
$$J_\infty^{CL}(x) - J_\infty^*(x) \leq \Delta(\gamma)$$

Where $\Delta(\gamma)$ is a function of discount factor that can be computed explicitly.

## Implementation Steps

### Step 1: Model Mismatch Quantification

Evaluate the difference between surrogate model and real system:

```python
def model_mismatch_bound(f_real, f_model, state_space, input_space):
    """
    Compute upper bound on model difference
    
    Args:
        f_real: Real system dynamics
        f_model: Surrogate model dynamics  
        state_space: State space
        input_space: Input space
    
    Returns:
        epsilon: Upper bound on model difference
    """
    max_error = 0
    for x in state_space.samples():
        for u in input_space.samples():
            error = norm(f_real(x, u) - f_model(x, u))
            max_error = max(max_error, error)
    return max_error
```

### Step 2: Stability Constraint Computation

Compute minimum discount factor based on model mismatch:

```python
def compute_gamma_min(L_cost, L_model, epsilon, delta):
    """
    Compute minimum discount factor ensuring stability
    
    Args:
        L_cost: Lipschitz constant of cost function
        L_model: Lipschitz constant of model
        epsilon: Upper bound on model difference
        delta: Stability margin
    
    Returns:
        gamma_min: Minimum discount factor
    """
    # Derived from quadratic lower bound conditions
    gamma_min = 1 - delta / (L_cost * epsilon * L_model)
    return max(0.5, gamma_min)  # Ensure gamma > 0.5
```

### Step 3: Discount Factor Optimization

Find optimal balance between stability and performance:

```python
def optimize_discount_factor(f_real, f_model, cost_fn, horizon, gamma_candidates):
    """
    Optimize discount factor through simulation
    
    Args:
        f_real: Real system
        f_model: Surrogate model
        cost_fn: Cost function
        horizon: Prediction horizon
        gamma_candidates: List of candidate discount factors
    
    Returns:
        optimal_gamma: Optimal discount factor
    """
    best_gamma = None
    best_performance = float('inf')
    
    for gamma in gamma_candidates:
        # Simulate closed-loop performance
        performance = simulate_closed_loop(f_real, f_model, cost_fn, horizon, gamma)
        
        # Check stability
        if is_stable(f_real, f_model, cost_fn, horizon, gamma):
            if performance < best_performance:
                best_performance = performance
                best_gamma = gamma
    
    return best_gamma
```

### Step 4: MPC Controller Implementation

Implement MPC based on optimized discount factor:

```python
class DiscountedMPC:
    def __init__(self, model, cost_fn, terminal_cost, horizon, gamma):
        self.model = model
        self.cost_fn = cost_fn
        self.terminal_cost = terminal_cost
        self.N = horizon
        self.gamma = gamma
    
    def solve(self, x0):
        """
        Solve discounted MPC optimization problem
        
        Args:
            x0: Current state
        
        Returns:
            u0: Optimal control input
        """
        # Build optimization problem
        # Stage cost (with discount)
        # Terminal cost (with discount)
        # Solve
        pass
```

## Key Formulas and Theorems

### Theorem 1: Stability Guarantee

**Conditions**:
- Cost function $\ell$ satisfies $\ell(x,u) \geq \alpha(||x||)$ where $\alpha$ is a $K_\infty$ function
- Model difference is bounded: $||f(x,u) - \hat{f}(x,u)|| \leq \epsilon$

**Conclusion**: There exists $\gamma^* < 1$ such that for all $\gamma \in (\gamma^*, 1]$, the closed-loop system is asymptotically stable.

### Theorem 2: Suboptimality Upper Bound

Under Theorem 1 conditions, infinite-horizon performance loss satisfies:

$$J_\infty^{CL}(x) - J_\infty^*(x) \leq \frac{\epsilon \cdot L_\ell \cdot L_f}{1 - \gamma}$$

Where $L_\ell$ and $L_f$ are Lipschitz constants for cost and system dynamics.

## Comparison with Existing Methods

| Method | Advantages | Disadvantages | Applicable Scenarios |
|--------|-----------|---------------|---------------------|
| **Discounted MPC** | Explicit handling of model mismatch; Few tunable parameters | May be conservative | Model difference known but cannot be eliminated |
| Tube MPC | Guaranteed constraint satisfaction | Computationally complex; Conservative | Safety-critical systems |
| Stochastic MPC | Handles random uncertainty | Requires probabilistic model | Significant random disturbances |
| Learning MPC | Online adaptation | Requires continuous learning | Data-rich scenarios |
| Robust MPC | Handles bounded disturbances | Usually too conservative | Disturbances with known bounds |

## References

Moldenhauer, R. H., Worthmann, K., Postoyan, R., et al. (2026). "Discounted MPC and infinite-horizon optimal control under plant-model mismatch: Stability and suboptimality." arXiv:2604.08521.
