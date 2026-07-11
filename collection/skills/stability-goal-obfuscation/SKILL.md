---
name: stability-goal-obfuscation
description: >
  Stability-goal obfuscation tradeoff methodology for autonomous agents.
  Addresses the problem that Lyapunov-stable goal-directed trajectories are
  inherently legible to Bayesian observers, leaking intent. Combines control
  Lyapunov functions (CLFs), probabilistic control barrier functions (PCBFs),
  and Rao-Blackwellized particle filter (RBPF) belief-state analysis to
  maintain task stability while obfuscating intent from passive observers.
  Use when: designing privacy-preserving autonomous systems, adversarial
  trajectory planning, intent privacy, safety-critical control, control
  barrier functions, Lyapunov stability with privacy constraints.
---

# Stability-Goal Obfuscation Tradeoff

Framework for maintaining task stability while preventing intent inference
by adversarial observers, based on Wang, Guralnik & Dixon (arXiv:2605.06630, May 2026).

## Problem

Goal-directed agents under Lyapunov-based control are intrinsically **legible**:
the contractive dynamics of a Lyapunov basin of attraction concentrates a
Bayesian observer's posterior belief over the agent's latent intent parameters
(goal location, radius, arrival time). Task-optimal trajectories are the most
information-leaking.

## Core Methodology

### 1. Dual-State Control Problem

Joint control on:
- **Physical state** x: agent dynamics ẋ ∈ u + d̄B (fully actuated, bounded disturbance)
- **Belief state** b: observer's RBPF belief over possible agent goals

The controller must satisfy both a **tracking constraint** (CLF) and a **privacy constraint** (PCBF) simultaneously.

### 2. KL-Based Information Leakage Measurement

- Observer uses Rao-Blackwellized particle filter (RBPF) with N particles over discrete goal samples
- Information leakage measured as KL divergence between prior and posterior over goals
- Online-computable at each RBPF update step
- Privacy requires maintaining leakage below a threshold with high probability

### 3. Probabilistic Control Barrier Functions (PCBFs)

Key innovation: derive separate PCBF conditions for:
- **Bayesian update step**: posterior concentration from new observations
- **Resampling step**: particle weight redistribution

Combined PCBF guarantees privacy across the full RBPF update cycle.

### 4. Joint Feasibility Analysis

The tracking envelope (physical feasibility) and privacy constraint (belief-state feasibility) interact:
- Tight privacy bounds shrink feasible control set
- Loose bounds may fail to obfuscate
- Feasibility depends on disturbance bounds d̄, RBPF particle count N, and measurement noise

## Implementation Pattern

```python
# QP formulation (per timestep):
# min  ||u - u_nom||²
# s.t.  ∂V/∂x · f(x,u) ≤ -α(V(x))          # CLF (stability)
#       P[PCBF(b, u) ≥ 0] ≥ 1 - ε          # PCBF (privacy, probabilistic)
#       u ∈ U                                # input constraints
```

Where:
- `u_nom`: nominal task-optimal control
- `V`: control Lyapunov function
- `PCBF`: probabilistic barrier function on belief state
- `ε`: acceptable privacy violation probability

## When to Apply

- Autonomous vehicles operating in adversarial environments
- Military/aerospace systems requiring intent privacy
- Multi-agent systems where intent leakage compromises coordination
- Any Lyapunov-stable controller operating under observation

## Key References

- arXiv:2605.06630 — Wang, Guralnik, Dixon (2026)
- Ames et al. (2016, 2019) — Control Barrier Functions
- Dragan et al. (2013) — Legible robot motion planning
- Wang et al. (2025b) — Intent inference via RBPF

## Pitfalls

- RBPF requires sufficient particle count for accurate belief estimation
- Privacy constraint may be infeasible if disturbance bounds are too tight
- Joint feasibility analysis is problem-specific; no universal bounds
- PCBF derivation requires careful treatment of both update and resampling steps
