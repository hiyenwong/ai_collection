---
name: discounted-mpc-control
description: "Model Predictive Control (MPC) stability and suboptimality analysis under plant-model mismatch with discounting. Provides theoretical guarantees for infinite-horizon optimal control when using surrogate models. Use when designing robust control systems, analyzing MPC stability, or dealing with model uncertainty in control applications."
---

# Discounted MPC and Infinite-Horizon Optimal Control Under Plant-Model Mismatch

## Core Problem

Real-world control systems operate using models that differ from the actual plant:
- Parameter uncertainties
- Unmodeled dynamics
- Linearization errors
- Time-varying system behavior

This **plant-model mismatch** affects stability and performance of Model Predictive Control (MPC).

## Key Contributions

### 1. Unified Framework

Analysis covers both:
- **Finite-horizon MPC**: Standard receding horizon control
- **Infinite-horizon optimal control**: Value iteration / policy optimization

Both **discounted** and **undiscounted** scenarios included.

### 2. Stability Guarantees

**Theorem**: Under plant-model mismatch bounds, exponential stability is guaranteed if:
- Model continuity holds
- Cost-controllability is satisfied
- Origin remains equilibrium under mismatch

### 3. Suboptimality Bounds

When using surrogate model with mismatch bounds proportional to states and controls:

```
J_actual(x0) - J_optimal(x0) ≤ γ * ||mismatch||
```

Where:
- `J_actual`: Closed-loop cost with real plant
- `J_optimal`: Optimal cost for surrogate model
- `γ`: Derived constant based on problem structure

### 4. Trade-off Analysis

Key insight: **Robustness guarantees are uniform over horizon length**

Larger prediction horizons do NOT require successively smaller plant-model mismatch for stability.

## Mathematical Framework

### Plant-Model Mismatch Model

```
f_actual(x, u) = f_model(x, u) + Δ(x, u)
```

Where `Δ(x, u)` represents mismatch bounded by:
```
||Δ(x, u)|| ≤ α||x|| + β||u||
```

### Discounted Cost Function

```
V(x) = Σ_{k=0}^∞ γ^k * l(x_k, u_k)
```

Discount factor `γ ∈ (0, 1)` affects:
- Convergence rate
- Suboptimality gap
- Required mismatch tolerance

## Practical Implications

### For Control System Design

1. **Tolerance specification**: Determine acceptable mismatch levels
2. **Horizon selection**: Longer horizons don't hurt robustness
3. **Discount tuning**: Balance performance vs robustness

### For System Identification

1. Identify critical model parameters
2. Quantify acceptable model error
3. Guide data collection priorities

## Design Guidelines

### When to Use Discounted MPC

- Long planning horizons
- Significant model uncertainty
- Need for robust stability guarantees
- Safety-critical applications

### Parameter Selection

| Parameter | Effect | Trade-off |
|-----------|--------|-----------|
| Horizon N | Better optimality | Computation |
| Discount γ | Robustness | Performance |
| Mismatch bound | Stability | Model complexity |

## Related Control Techniques

- Robust MPC
- Adaptive control
- Tube-based MPC
- Data-driven control

## Paper Reference

**Title**: Discounted MPC and infinite-horizon optimal control under plant-model mismatch: Stability and suboptimality
**Authors**: Robert H. Moldenhauer, Karl Worthmann, Romain Postoyan, Dragan Nešić, Mathieu Granzotto
**arXiv**: 2604.08521
**Category**: math.OC, eess.SY
**Published**: 2026-04-09
**Submitted to**: 65th IEEE Conference on Decision and Control

## Key Equations

### Stability Condition
```
V(x_{k+1}) - V(x_k) ≤ -α||x_k||² + β||Δ||²
```

### Suboptimality Bound
```
V_closed_loop ≤ V_optimal * (1 + κ)
```

Where `κ` depends on mismatch magnitude and discount factor.