---
name: discounted-mpc-robustness
description: "Robustness analysis for MPC and infinite-horizon optimal control under plant-model mismatch with quadratic costs. Covers discounted and undiscounted scenarios, stability guarantees, and suboptimality bounds. Use when: (1) MPC robustness analysis, (2) plant-model mismatch effects, (3) discounted infinite-horizon control, (4) model uncertainty in optimal control, (5) stability under model errors, (6) data-driven surrogate models."
---

# Discounted MPC Robustness Analysis

Comprehensive framework for analyzing stability and suboptimality of MPC and infinite-horizon optimal control under plant-model mismatch.

## Core Problem

Design optimal controls using **surrogate model** `f` instead of true **plant dynamics** `g`. Characterize:
- Stability of closed-loop system
- Suboptimality of closed-loop cost
- Interaction with horizon length and discount factor

## System Setup

### Plant vs Surrogate

**True plant dynamics**:
```
x+ = g(x, u), g(0,0) = 0
```

**Surrogate model** (used for control design):
```
x+ = f(x, u), f continuous, f(0,0) = 0
```

### Proportional Mismatch

**Key measure**: Proportional plant-model mismatch
```
|f - g|_S := inf{p ≥ 0 : |f(x,u) - g(x,u)| ≤ p(|x| + |u|) ∀x ∈ S, u ∈ U}
```

**Properties**:
- Bounds mismatch proportional to state and control magnitude
- Origin equilibrium preserved: `f(0,0) = g(0,0) = 0`
- Valid in region `S` (model assumptions hold / data available)

### Additional Assumptions

**L-Lipschitz continuity**:
```
|f(x,u) - f(y,u)| ≤ L|x - y| ∀x,y ∈ R^n, ∀u ∈ U
```

**Control set**:
- `U` closed, contains 0
- Ensures existence of optimal controls

## Optimal Control Problem

### Cost Function

**General form** (finite/infinite horizon, discounted/undiscounted):
```
J_{γ,N}^f(x, u_N) = ∑_{k=0}^{N-1} γ^k ℓ(φ_f(k,x,u_k), u_k)
```

where:
- `N ∈ N ∪ {∞}`: Horizon length
- `γ ∈ (0,1]`: Discount factor
- `ℓ(x,u) = x^T Q x + u^T R u`: Quadratic stage cost

**Quadratic stage cost**:
```python
Q ∈ R^{n×n}, symmetric positive definite
R ∈ R^{m×m}, symmetric positive definite
ℓ(x,u) = ||x||_Q^2 + ||u||_R^2
```

### Value Function

**Optimal value function**:
```
V_{γ,N}^f(x) := min_{u_N ∈ U^N} J_{γ,N}^f(x, u_N)
```

**Bellman equation** (Proposition 1):
```
V_{γ,N}^f(x) = min_{u ∈ U} [ℓ(x,u) + γ V_{γ,N-1}^f(f(x,u))]
```

### Optimal Feedback Policy

**Set-valued policy**:
```
U_{γ,N}^f(x) := {u ∈ U : ℓ(x,u) + γ V_{γ,N-1}^f(f(x,u)) = V_{γ,N}^f(x)}
```

## Closed-Loop Dynamics

### Plant under Surrogate-Based Control

**Closed-loop system**:
```
x+ = g(x, κ(x)) where κ(x) ∈ U_{γ,N}^f(x)
```

**Key issue**: Control designed for `f`, applied to `g`

**Closed-loop cost**:
```
J_{γ,N}^g(x_0) = ∑_{k=0}^{N-1} γ^k ℓ(φ_g(k,x_0,u_k), u_k)
```

where `u_k` from surrogate-based policy.

## Cost Controllability

### Assumption (Cost Controllability)

**Key requirement**:
```
∃α_c > 0: V_{γ,N}^f(x) ≤ α_c ℓ(x, κ(x)) ∀x ∈ R^n
```

**Interpretation**: Optimal value function bounded proportional to stage cost

**Consequences**:
- Exponential stability for sufficiently long horizons [18]
- Enables Lyapunov-based stability analysis
- Bounds computational complexity

## Main Results

### Stability Guarantee

**Theorem (Stability under Mismatch)**:

Under:
- `f` continuous, L-Lipschitz
- Cost controllability (α_c)
- Horizon `N` sufficiently long (or γ sufficiently close to 1)
- Mismatch `|f-g|_S` sufficiently small

**Result**: Closed-loop system exponentially stable about origin.

**Lyapunov function**: `V_{γ,N}^f` serves as Lyapunov function

### Suboptimality Bound

**Theorem (Suboptimality)**:

Closed-loop cost approaches infinite-horizon optimal cost of surrogate model:
```
J_{γ,∞}^g(x_0) - V_{γ,∞}^f(x_0) ≤ δ(α_c, L, γ, |f-g|_S)
```

where `δ` quantifies performance degradation due to mismatch.

### Key Innovation

**Perturbation bounds independent of horizon length**:

Unlike prior work [8,19,25]:
- Previous: Longer horizon → smaller mismatch needed
- This work: Bounds uniform over horizon length

**Advantage**: Can use longer horizons without requiring tighter model accuracy

## Tradeoffs

### Stability Conditions

Stability guaranteed when:
1. **Horizon length**: `N ≥ N*` sufficiently long (undiscounted)
2. **Discount factor**: `γ ≥ γ*` sufficiently close to 1 (infinite horizon)
3. **Mismatch**: `|f-g|_S ≤ ε` sufficiently small

**Tradeoff**: Can compensate larger mismatch with longer horizon or larger γ.

### Suboptimality Degradation

Performance bound depends on:
- `α_c`: Cost controllability parameter
- `L`: Lipschitz constant
- `γ`: Discount factor
- `|f-g|_S`: Mismatch magnitude

**Better model** (smaller mismatch) → **Better performance**

## Applications

### Data-Driven Control

Surrogate from system identification:
- **Kernel EDMD**: Data-driven models with arbitrarily small mismatch [8]
- **Koopman operator**: Linear surrogates for nonlinear systems
- **More data** → **More accurate surrogate** → **Smaller mismatch**

### Model Simplification

Using simplified models for tractability:
- Linear approximations for nonlinear systems
- Reduced-order models
- Discretization of continuous-time systems

### Reinforcement Learning

Discounted costs common in RL:
- Mitigate prediction error accumulation
- Better numerical properties
- Stability requires γ close to 1

## Implementation Considerations

### Horizon Selection

**Finite horizon (MPC)**:
```python
N_min = compute_minimum_horizon(α_c, L, ε_mismatch)
# Use N ≥ N_min for stability
```

**Infinite horizon**:
```python
γ_min = compute_minimum_discount(α_c, L, ε_mismatch)
# Use γ ≥ γ_min for stability (close to 1)
```

### Mismatch Estimation

**For data-driven surrogates**:
```python
# Kernel EDMD provides mismatch bound
|f - g|_S ≤ p(data_quality, system_class)
# More data → smaller p
```

**For model simplification**:
```python
# Analytical mismatch bound
|f - g|_S ≤ p(model_complexity_reduction)
```

### Lyapunov Verification

```python
def verify_stability(x, V_f, κ, α_c, L, ε):
    """Check Lyapunov conditions under mismatch"""
    # Decrease condition
    ΔV = V_f(g(x, κ(x))) - V_f(x)
    
    # Stability if ΔV ≤ -α ℓ(x, κ(x))
    return ΔV ≤ -α * (||x||_Q^2 + ||κ(x)||_R^2)
```

## Comparison to Prior Work

### Key Differences

| Aspect | This Work | Prior [8,19,25] |
|--------|-----------|----------------|
| Horizon dependence | **Independent** | Worsens with longer N |
| Discounted case | **Included** | Not studied |
| Infinite horizon | **Covered** | Not applicable |
| Framework | Unified (all cases) | Finite horizon only |

### Advantages

1. **Horizon-independent bounds**: Use longer horizons freely
2. **Discounted costs**: RL applications
3. **Infinite horizon**: Direct optimal control (no MPC receding)
4. **Unified theory**: Single framework for all scenarios

## Limitations

### Assumption Requirements

1. **Quadratic stage cost**: May not apply to general costs
2. **Proportional mismatch**: Origin must be equilibrium of both systems
3. **Lipschitz continuity**: Required for surrogate
4. **Cost controllability**: May not hold for all systems

### Practical Challenges

1. **Estimating mismatch**: `|f-g|_S` may be difficult to determine
2. **Lipschitz constant**: May be large for complex systems
3. **Minimum horizon**: May be impractically long for some systems
4. **Region S**: Valid only where model assumptions hold

## Related Concepts

- **Robust MPC**: Terminal ingredients vs long horizon approaches
- **Relaxed DP**: Bellman inequality for stability
- **Data-driven control**: Kernel EDMD, Koopman operators
- **Discounted optimal control**: RL connections
- **Lyapunov stability**: Value function as Lyapunov function

## References

1. **Paper**: Moldenhauer et al., "Discounted MPC and infinite-horizon optimal control under plant-model mismatch" (arXiv:2604.08521v1, April 2026)
2. **Related**: [8] Data-driven MPC with kernel EDMD
3. **Related**: [18] MPC stability via relaxed DP
4. **Related**: [22] Discounted optimal control stability

## Open Questions

1. **Non-quadratic costs**: Extension to general stage costs?
2. **Stochastic systems**: Noise handling in framework?
3. **State constraints**: Incorporate constraint satisfaction?
4. **Non-proportional mismatch**: Other mismatch measures?
5. **Adaptive horizon**: Horizon adjustment based on mismatch?

## Tools Used

- `exec`: Run stability verification scripts
- `read`: Load reference materials
- `write`: Save analysis results

## Notes

- Horizon-independent bounds major practical improvement
- Discount factor γ close to 1 critical for stability
- More data → more accurate surrogate → better performance
- Framework applicable to MPC, value iteration, direct infinite-horizon control