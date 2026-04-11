---
name: density-driven-optimal-control
description: "Density-Driven Optimal Control (D²OC) for multi-agent systems - optimal transport-based coverage control with Wasserstein distance minimization. Use when: (1) multi-agent coverage problems, (2) optimal transport in control systems, (3) Wasserstein distance applications, (4) stochastic MPC for swarms, (5) decentralized area coverage, (6) density matching problems."
---

# Density-Driven Optimal Control (D²OC)

A rigorous Lagrangian framework for non-uniform area coverage in stochastic multi-agent systems using optimal transport theory.

## Core Concept

D²OC reformulates multi-agent coverage as an optimal transport problem, minimizing Wasserstein distance between agent distribution and target density in a stochastic MPC-like formulation.

**Key Innovation**: Bridges individual agent dynamics with collective distribution matching via optimal transport, with formal convergence guarantees under noise.

## Problem Setup

### Stochastic LTI Dynamics

Each agent follows:
```
x_{k+1}^i = A_i x_k^i + B_i u_k^i + w_k^i, w_k^i ~ N(0, Σ_i,w)
y_k^i = C_i x_k^i + v_k^i, v_k^i ~ N(0, Σ_i,v)
```

where:
- `x_k^i ∈ R^n`: state
- `u_k^i ∈ R^m`: control input  
- `y_k^i ∈ R^d`: output
- Process & measurement noise: Gaussian

### Wasserstein Distance

**2-Wasserstein distance** (Kantorovich problem):
```
W_2(ρ, ν) = min_π ∑_{i,j} π_ij ||y_i - q_j||²
```
subject to mass conservation constraints.

### Distributions

- **Empirical distribution**: `ρ_k = 1/(k+1)na ∑_{t=0}^k ∑_{i=1}^{na} δ_{y_t^i}`
- **Reference distribution**: `ν = 1/N ∑_{j=1}^N δ_{q_j}`

**Objective**: Minimize `W_2(ρ_k, ν)` over finite time.

## Three-Stage Framework

### Stage 1: Local Target Selection & Optimal Control

At each time step:
1. Select local targets `{q_j}` based on proximity & remaining weight
2. Compute control minimizing local Wasserstein distance
3. Subject to dynamic & input constraints

**Control Objective**:
```
min_{U_k|H^i} J(U_k|H^i) = E[∑_{h=r}^{H+r-1} (W_{k+h}^i)²] + ||U_k|H^i||_R²
```

### Stage 2: Weight Update

After movement:
- Solve local Wasserstein distance
- Update sample weights (reduce recently covered)
- Encourage under-explored areas

### Stage 3: Weight Sharing

- Exchange weights within communication range
- Min-weight consensus: select smallest weight per sample
- Enhance coordination, reduce redundancy

## Optimal Control Law

### Quadratic Reformulation

**Proposition 1**: Expected squared Wasserstein cost reformulates as quadratic form:
```
E[∑_h (W_{k+h}^i)²] = E[||Ω_{k|r:H}^i (Y_{k|r:H}^i - Q̄_{k|r:H}^i)||²] + const
```

where `Q̄` is weighted barycenter of local targets.

### Matrix Definitions

```python
# Control influence matrix (relative degree r)
Θ_i = [
    [C_i A^{r-1}_i B_i,  0,          ..., 0         ],
    [C_i A^r_i B_i,      C_i A^{r-1}_i B_i, ..., 0 ],
    ...
]

# Free response matrix  
Φ_i = [(C_i A^r_i)^T, ..., (C_i A^{r+H-1}_i)^T]^T

# Output prediction
Y_{k|H}^i = Φ_i x_k^i + Θ_i U_{k|H}^i
```

### Optimal Control (Theorem 1)

```
U_k|H^i* = -(Θ_i^T Ω Θ_i + R)^{-1} Θ_i^T Ω (Φ_i x_k^i - Q̄_{k|r:H}^i)
```

**Properties**:
- Strictly convex (unique solution)
- Closed-form (efficient computation)
- Accounts for noise via expectation

## Convergence Guarantee

### Reachability Analysis

**Key Result**: Empirical distribution converges to bounded neighborhood of target:
```
lim_{k→∞} W_2(ρ_k, ν) ≤ ε + δ_noise
```

where:
- `ε`: Control performance bound
- `δ_noise`: Noise-induced deviation

### Requirements

**Assumptions**:
1. `(A_i, B_i)` completely controllable
2. `A_i` marginally stable (eigenvalues ≤ 1)
3. Bounded noise covariance

### Proof Structure

1. **Reachable set characterization**: Define feasible agent positions
2. **Transport plan existence**: Show optimal matching exists
3. **Bounded tracking error**: Wasserstein distance remains bounded
4. **Time-averaged convergence**: Empirical distribution approaches target

## Implementation

### Algorithm

```python
# D2OC Algorithm
for each agent i:
    # Stage 1: Local control
    S_k^i = select_local_targets(y_k^i, weights, reachable_set)
    Q̄_k^i = compute_barycenter(S_k^i, π)
    U_k^i* = compute_optimal_control(A_i, B_i, C_i, x_k^i, Q̄_k^i)
    
    # Apply control
    x_{k+1}^i = A_i x_k^i + B_i U_k^i* + w_k^i
    
    # Stage 2: Weight update
    weights = update_weights(y_{k+1}^i, targets)
    
    # Stage 3: Share weights
    weights = consensus_with_neighbors(weights)
```

### Local Target Selection

```python
def select_targets(agent_pos, targets, weights, reachable_set):
    """Select targets within reachable set, prioritizing high weights"""
    candidates = []
    for j, q_j in enumerate(targets):
        if is_reachable(agent_pos, q_j, reachable_set):
            candidates.append((j, weights[j], distance(agent_pos, q_j)))
    
    # Sort by weight (descending) and distance (ascending)
    candidates.sort(key=lambda x: (-x[1], x[2]))
    return candidates[:M_i]  # Select M_i targets
```

### Optimal Control Computation

```python
def compute_control(A, B, C, x, Q_bar, R, H, r):
    """Compute optimal control minimizing Wasserstein cost"""
    # Build matrices
    Theta = build_theta_matrix(A, B, C, H, r)
    Phi = build_phi_matrix(A, C, H, r)
    Omega = build_omega_matrix(transport_weights)
    
    # Predicted output
    Y_pred = Phi @ x + Theta @ U
    
    # Optimal control
    U_star = -inv(Theta.T @ Omega @ Theta + R) @ Theta.T @ Omega @ (Phi @ x - Q_bar)
    
    return U_star[:m]  # First time step control
```

## Applications

### Coverage Tasks

1. **Search & rescue**: Prioritized area coverage
2. **Environmental monitoring**: Sensor deployment
3. **Infrastructure inspection**: Targeted inspection paths
4. **Smart farming**: Precision agriculture
5. **Planetary exploration**: Resource-constrained missions

### Key Advantages

- **Decentralized**: No global coordinator needed
- **Robust**: Handles noise & uncertainty
- **Optimal**: Wasserstein minimization (not heuristic)
- **Scalable**: Lagrangian approach avoids curse of dimensionality
- **Guaranteed**: Formal convergence analysis

## Comparison to Alternatives

| Method | Approach | Guarantees | Computational Cost |
|--------|----------|------------|-------------------|
| **D²OC** | Lagrangian + MPC | Convergence + bounded error | Medium (per-agent) |
| SMC [1,2] | Ergodic control | Ergodicity as t→∞ | Low |
| Eulerian OT [3,4] | PDE-based | Convergence | High (curse of dim) |
| Mean-field SB [5] | Gaussian mixtures | Limited (parametric) | Very high |
| Heuristic D²C [6,7] | Lagrangian | None | Low |

## References

1. **Paper**: Kooktae Lee, "Density-Driven Optimal Control: Convergence Guarantees for Stochastic LTI Multi-Agent Systems" (arXiv:2604.08495v1, April 2026)
2. **Code**: See `references/implementation_details.md` for detailed algorithms
3. **Examples**: See `references/applications.md` for use cases

## Related Concepts

- **Optimal Transport**: Wasserstein distance, Kantorovich problem
- **Stochastic MPC**: Model predictive control under uncertainty
- **Multi-Agent Systems**: Decentralized control, consensus
- **Reachability Analysis**: Reachable sets, bounded control
- **Density Control**: Distribution matching, coverage optimization

## Tools Used

- `exec`: Run Python implementations
- `read`: Load reference files
- `write`: Save control results

## Notes

- Relative degree `r` determines control delay
- Horizon `H` balances performance vs computation
- Weight matrix `R` controls input penalty
- Noise covariance affects convergence bound
- Communication range determines coordination level