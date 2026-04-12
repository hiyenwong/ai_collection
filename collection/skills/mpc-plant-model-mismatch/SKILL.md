---
name: mpc-plant-model-mismatch
description: "Model Predictive Control stability analysis under plant-model mismatch. Covers discounted/infinite-horizon optimal control, suboptimality bounds, and robustness guarantees. Use for: MPC design, control system robustness analysis, plant-model mismatch tolerance, stability proofs, optimal control with surrogate models."
---

# MPC Stability under Plant-Model Mismatch

Unified framework for analyzing MPC and infinite-horizon optimal control stability when using surrogate models.

## Core Theory

### Problem Setup

- **Real plant**: Unknown dynamics `x+ = f(x,u)` (continuous)
- **Surrogate model**: Approximate dynamics `x+ = g(x,u)` (continuous)
- **Plant-model mismatch**: `|f(x,u) - g(x,u)| ≤ γ|x| + δ|u|` (proportional bounds)
- **Assumption**: Origin remains equilibrium under mismatch
- **Cost**: Quadratic `l(x,u) = x'Qx + u'Ru` (positive definite)

### Stability Guarantee

**Theorem**: Under continuity + cost-controllability, exponential stability holds if:
```
γ, δ sufficiently small (proportional mismatch bounds exist)
```

**Key insight**: Stability guarantee is **uniform over horizon length** — longer horizons don't require smaller mismatch tolerance.

### Suboptimality Bound

**Closed-loop cost**: `J_cl = Σ l(x_k, u_k)` (real plant trajectory)
**Surrogate optimal cost**: `V_opt^g` (computed on surrogate model)

**Bound**: `J_cl ≤ V_opt^g + ε(γ, δ)` where ε depends on mismatch magnitude.

### Tradeoff Relationship

```
Horizon N  ↑ → Better approximation, but computation ↑
Discount λ ↓ → Tighter stability, but mismatch tolerance ↓
Mismatch γ ↓ → Better stability, but requires better model
```

The framework reveals how these three parameters interact.

## Key Results

### 1. Infinite-Horizon Stability

For discounted infinite-horizon MPC:
- Stability preserved under plant-model mismatch
- Suboptimality bound scales with mismatch magnitude
- Discount factor λ affects robustness margin

### 2. Finite-Horizon Stability

For standard finite-horizon MPC:
- Same stability guarantees hold
- Horizon length doesn't tighten mismatch requirements
- Practical: Can use longer horizons without stricter model accuracy

### 3. Cost-Controllability Assumption

Essential condition: Surrogate model satisfies cost-controllability
```
Exists α > 0 such that V_g(x) ≤ α|x|²  (value function bounded)
```

## Practical Applications

### Control System Design

1. **Model tolerance specification**: Determine acceptable plant-model mismatch bounds
2. **Horizon selection**: Choose horizon length freely (no mismatch penalty)
3. **Discount tuning**: Balance robustness vs. performance

### Robustness Analysis Workflow

```python
# Step 1: Estimate plant-model mismatch
γ_model = estimate_model_error()  # From data/physics
δ_control = estimate_control_error()

# Step 2: Check stability condition
if γ_model < γ_threshold and δ_control < δ_threshold:
    # Stability guaranteed
    pass

# Step 3: Compute suboptimality bound
epsilon = compute_suboptimality(γ_model, δ_control)
```

### Real-World Scenarios

- **Process control**: Plant dynamics estimated from data (inevitable mismatch)
- **Robotics**: Physics model approximates real dynamics
- **Power systems**: Grid model vs. actual load/generation
- **Aerospace**: Flight dynamics model vs. airframe reality

## Mathematical Framework

### Quadratic Cost Setup

```
Stage cost: l(x,u) = x'Qx + u'Ru  (Q,R > 0)
Value function: V(x) = min Σ λ^k l(x_k,u_k)
Terminal cost: V_f(x) bounds tail cost
```

### Lyapunov Stability Proof

Key idea: Use value function as Lyapunov candidate
```
V(x_k+1) - V(x_k) ≤ -l(x_k,u_k) + perturbation_from_mismatch
```
Stability if perturbation bounded by stage cost decrease.

### Cost-Controllability Condition

Surrogate model property:
```
V_g(x) ≤ α|x|²  (value function quadratic bound)
```
This ensures stability analysis valid.

## Implementation Guidance

### MPC Design Checklist

| Item | Requirement | Practical Check |
|------|-------------|-----------------|
| Surrogate continuity | g(x,u) continuous | Smooth model, no discontinuities |
| Cost-controllability | V_g(x) ≤ α|x|² | Can steer to origin with bounded cost |
| Mismatch bounds | γ,δ exist and known | Estimate from model validation data |
| Origin equilibrium | g(0,0) = f(0,0) = 0 | Zero state/control → zero next state |

### Model Improvement Strategy

If mismatch too large for stability:
1. **Refine model**: Better physics understanding, more data
2. **Adaptive MPC**: Online model correction
3. **Robust MPC**: Explicit uncertainty handling (tube MPC)
4. **Discount adjustment**: Lower λ for tighter robustness

## Key Insights

1. **Uniform robustness**: Horizon length doesn't tighten mismatch requirements — counterintuitive but powerful
2. **Unified framework**: Single theory covers finite/infinite horizon, discounted/undiscounted cases
3. **Practical tolerance**: Explicit mismatch bounds enable model validation
4. **Tradeoff understanding**: Horizon/discount/mismatch interaction guides design choices

## Related Concepts

- **Tube MPC**: Explicit robustness via constraint tightening
- **Adaptive MPC**: Online model learning
- **Gain scheduling**: Multiple models for different operating points
- **Robust control**: Worst-case design (H∞, μ-synthesis)

## References

**arXiv**: 2604.08521v1  
**Authors**: Moldenhauer, Worthmann, Postoyan, Nešić, Granzotto  
**Categories**: math.OC, eess.SY  
**Title**: "Discounted MPC and infinite-horizon optimal control under plant-model mismatch: Stability and suboptimality"