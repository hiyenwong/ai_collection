---
name: pg-dpo-non-exponential-discounting
description: "Pontryagin-Guided Direct Policy Optimization (PG-DPO) — a variational RL framework that replaces Bellman recursions with Pontryagin Maximum Principle for non-exponential discounting (hyperbolic, survival-discount). Handles settings where standard value/actor-critic methods fail. Use when: RL with non-exponential discounting, hyperbolic discounting RL, human-like time preferences, survival processes, Pontryagin-based RL. Activation: PG-DPO, non-exponential discounting, Pontryagin RL, hyperbolic discounting, Bellman breakdown, Adjoint-MC projection."
---

# Beyond the Bellman Recursion: Pontryagin-Guided Direct Policy Optimization

**Source paper**: arXiv:2605.20996
**Authors**: Hojin Ko, Jeonggyu Huh

## Core Problem

Most value-based and actor-critic RL methods rely on Bellman-style recursions, which **collapse under non-exponential discounting** (e.g., hyperbolic discounting common in human preferences, survival processes). This work:
- Shows the breakdown is **structural**: exponential discounting sits at a fragile intersection of multiplicativity and time homogeneity
- Proposes **Pontryagin-Guided Direct Policy Optimization (PG-DPO)**, a variational framework that abandons recursion entirely

## Key Contributions

### 1. Structural Breakdown Analysis
- Proves why Bellman recursions fail for non-exponential discounting
- Identifies: violating **multiplicativity** or **time homogeneity** breaks standard dynamic programming
- Explains why existing approaches diverge under hyperbolic/survival discounting

### 2. PG-DPO Framework
- **Abandons recursion**: no Bellman backup, no value function
- Couples the **Pontryagin Maximum Principle** (PMP) with Monte Carlo rollouts
- Uses **Adjoint-MC projection** enforcing pointwise Hamiltonian maximization
- A **variational framework** that optimizes policy via the necessary conditions of optimal control

### 3. Performance
- Improves accuracy and stability where equation-driven solvers and critic-based baselines diverge
- Handles multi-dimensional hyperbolic and survival-discount benchmarks

## Algorithm Design

### PG-DPO Framework

```
1. Parameterize policy π_θ(a|s)
2. For each rollout:
   a. Collect trajectory τ = (s_0, a_0, r_0, ..., s_T)
   b. Compute Hamiltonian H(t) = p(t)·f(s(t), a(t)) - γ(t)·r(s(t), a(t))
      where p(t) is the adjoint (costate) variable
      and γ(t) is the non-exponential discount function
   c. Adjoint-MC projection: enforce pointwise Hamiltonian maximization
      by projecting policy gradients onto the Pontryagin conditions
3. Update θ via policy gradient with Hamiltonian-consistent advantage
```

### Key Equations

**Bellman breakdown condition**:
- Standard: V(s) = max_a [r(s,a) + γ·V(s')]
- Non-exponential: V(s) = max_a [r(s,a) + γ(t)·V(s')] → **NOT valid** when γ(t) is not exponential

**PG-DPO alternative**:
- Hamiltonian: H(s,a,p,t) = p·f(s,a) - γ(t)·r(s,a)
- Policy optimality: a*(s,p,t) = argmax_a H(s,a,p,t)
- Adjoint equation: dp/dt = -∂H/∂s

## Application Scenarios

- **Human preference modeling**: Hyperbolic discounting in behavioral economics
- **Survival analysis**: Processes with non-constant hazard rates
- **Long-horizon planning**: Where standard geometric discounting is inappropriate
- **Robust RL**: Settings where discount factor sensitivity causes instability
- **Behavioral cloning with human data**: Human decisions follow non-exponential discounting

## Related Skills
- [[rlhf-from-human-feedback]] - Standard RLHF with exponential discounting
- [[learning-zone-energy-data-selection]] - Efficient RL post-training
- [[advantage-collapse-grpo-avspo]] - GRPO improvements

## Implementation Considerations

- Replace standard GAE(λ) with Hamiltonian-consistent advantage estimation
- No critic network needed (avoids critic convergence issues)
- Adjoint variables introduce additional ODE solve per step (computational overhead)
- Best for: domains with known discount structure or where Bellman methods fail

## Activation Keywords
PG-DPO, non-exponential discounting, Pontryagin Maximum Principle, hyperbolic discounting, Bellman breakdown, Adjoint-MC projection, Hamiltonian RL, optimal control RL, survival discount, time-inconsistent preferences
