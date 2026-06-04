---
name: two-timescale-markovian-sa-convergence
description: Convergence theory for two-timescale stochastic approximations under Markovian noise, applicable to TDC and actor-critic methods. First almost sure convergence proof for TDC with eligibility traces under off-policy learning with linear function approximation. ICML 2026.
---

# Two-Timescale Markovian SA Convergence

**Paper**: arXiv:2605.31172 | Submitted: 29 May 2026 | **ICML 2026**

**Authors**: Vagul Mahadevan, Claire Chen, Shuze Daniel Liu, Shangtong Zhang

## Core Concept

This work establishes **stability and convergence** of two-timescale stochastic approximation (SA) algorithms under **Markovian noise**, a more realistic setup for RL compared to prior i.i.d. noise assumptions.

### Key Innovation

**Technical Novelty**: Control fast timescale parameter with **running max of slow timescale parameter** instead of current slow parameter (as prior works do).

This enables:
- Convergence without projection operators
- Noise not required to live in compact space
- First convergence proof for TDC with eligibility traces (off-policy)

## Two-Timescale Stochastic Approximation

### Framework

```
θ_{k+1} = θ_k + β_k h(θ_k, w_k, X_k)  // Slow timescale
w_{k+1} = w_k + α_k g(θ_k, w_k, X_k)  // Fast timescale
```

where α_k >> β_k (fast >> slow step sizes)

### Key RL Applications

1. **TDC (Temporal Difference with Gradient Correction)**: 
   - θ: policy parameters
   - w: value function parameters
   
2. **Actor-Critic Methods**:
   - θ: actor (policy)
   - w: critic (value)

3. **Off-policy learning with eligibility traces**

## Theoretical Results

### Main Theorem

Under Markovian noise {X_k}:

1. **Stability (Boundedness)**: Both θ_k and w_k remain bounded
2. **Convergence**: θ_k → θ* (optimal solution)
3. **No projection needed**: Natural convergence without artificial constraints

### Technical Key

**Running max control**:
```
bound_w = max_{i≤k} ||θ_i||
```

Fast parameter w_k bounded by running max of slow parameter, not current value.

This handles Markovian dependencies that i.i.d. analysis cannot.

## TDC with Eligibility Traces

### First Convergence Result

**TDC with eligibility traces** under:
- Off-policy learning
- Linear function approximation
- Markovian environment

Achieves **almost sure convergence** - first such proof.

### TDC Algorithm

```
δ_k = R_k + γ V_w(X_{k+1}) - V_w(X_k)
e_k = γ λ e_{k-1} + φ(X_k)  // Eligibility trace

θ update: θ_{k+1} = θ_k + β_k δ_k e_k
w update: w_{k+1} = w_k + α_k (δ_k - w_k^T φ(X_k)) φ(X_k)
```

λ: eligibility trace decay parameter

## Implementation Guidelines

### 1. Step Size Selection

```
α_k = α_0 / (k + 1)^α
β_k = β_0 / (k + 1)^β
```

where α > β (fast >> slow)

Common: α ∈ [0.5, 1], β ∈ [0.5, 0.8] with α > β

### 2. Stability Without Projection

No need for projection operator Ω:
```
// Prior works required:
θ_{k+1} = Π_Ω(θ_k + β_k h(...))
```
This work: natural convergence without projection.

### 3. Markovian Noise Handling

- Environment state transitions Markovian
- Observations have temporal dependencies
- Prior i.i.d. assumption unrealistic for RL

## Applications

### Primary Use Cases

1. **Off-policy TD learning** - value function estimation
2. **Actor-critic convergence** - policy gradient methods
3. **Eligibility traces** - temporal credit assignment
4. **Theoretical RL foundations** - convergence guarantees

### When This Theory Applies

- Two-timescale algorithms (actor-critic, TDC)
- Markovian environments (most RL settings)
- Need convergence guarantees
- Off-policy learning scenarios

## Comparison with Prior Works

| Aspect | Prior Works | This Work |
|--------|-------------|-----------|
| Noise | i.i.d. required | Markovian ✓ |
| Projection | Required | Not needed ✓ |
| Compact noise | Required | Not needed ✓ |
| TDC+traces | No convergence | First proof ✓ |

## Practical Implications

### For Algorithm Design

1. **Actor-critic**: Convergence guaranteed under realistic assumptions
2. **TDC**: Eligibility traces work off-policy with convergence
3. **Step sizes**: Theory guides fast/slow separation

### For Implementation

- No projection operator needed
- Handles real environment noise
- Validates existing RL algorithm stability

## Activation Keywords

- two-timescale convergence
- Markovian stochastic approximation
- TDC convergence
- actor-critic stability
- eligibility traces convergence
- off-policy TD learning
- running max control

## Related Skills

- [[rat-randomized-advantage-transformation]] - Policy optimization
- [[agpo-adaptive-group-policy-optimization]] - GRPO variants
- [[conditional-equivalence-dpo-rlhf]] - RLHF theory
- [[pg-dpo-non-exponential-discounting]] - Policy gradient theory

## References

- Paper: arXiv:2605.31172 - "Convergence of Two-Timescale Markovian Stochastic Approximations with Applications in Reinforcement Learning"
- TDC algorithm: Sutton et al. (2009)
- Two-timescale SA: prior theoretical works (i.i.d. case)

---

**Category**: reinforcement-learning, convergence-theory, stochastic-approximation, theoretical-RL
