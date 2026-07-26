---
name: safety-critical-contextual-control-riemannian
version: 1.0.0
description: Safety-critical contextual control via online Riemannian optimization with world models — Penalized Predictive Control (PPC) framework for provably safe control using black-box simulators and score-based density estimation.
category: systems-engineering
tags: [safety-critical control, Riemannian optimization, world models, predictive control, online optimization, barrier functions, cyber-physical systems]
source: arXiv:2604.19639v1
authors: [Tongxin Li]
date: 2026-04-21
---

# Safety-Critical Contextual Control via Online Riemannian Optimization with World Models

## Overview

Penalized Predictive Control (PPC) — a framework that unifies **black-box simulator-based world models** with **online density estimation** to achieve **provable safety** in contextual control problems. The key innovation is replacing Lipschitz-continuity assumptions with **barrier curvature λ**, enabling tighter safety bounds.

## Core Architecture: Simulator–Planner Decomposition

```
┌──────────────┐         score ŝ_t = ∇_u ln p̂_t        ┌──────────────┐
│   Simulator  │ ───────────────────────────────────────▶ │   Planner    │
│ (World Model)│                                          │ (Controller) │
│              │ ◀─────────────────────────────────────── │              │
│  Compresses  │         action u_t                       │ Minimizes    │
│  feasibility │                                          │ free energy  │
│  manifold to │                                          │ functional   │
│  density p̂_t │                                          │              │
└──────────────┘                                          └──────────────┘
```

**Simulator** (World Model):
- Compresses the feasibility manifold into a score-based density `p̂_t(u)`
- Transmits the score `ŝ_t = ∇_u ln p̂_t` to the Planner
- Does NOT need to be differentiable — black-box is sufficient

**Planner** (Controller):
- Minimizes a free energy functional via Gibbs-Boltzmann distribution
- Combines contextual density from simulator with task objective
- Produces safe actions through probabilistic sampling

## Key Mathematical Framework

### 1. Penalized Predictive Control (PPC) Objective

The planner solves:
```
min_u  J(u) − λ ln p̂_t(u)
```

Where:
- `J(u)` = task cost function
- `p̂_t(u)` = estimated feasibility density from simulator
- `λ` = barrier curvature parameter (controls safety margin)

### 2. Gibbs-Boltzmann Policy

The optimal policy is:
```
π*(u|s) = exp(−J(u)/λ) · p̂_t(u) / Z
```

Where `Z` is the partition function (normalization constant).

### 3. Safety Bound Theorem

**Key Result**: The distance from the true feasibility manifold is bounded by:

```
d(π*, M_safe) ≤ ε_score / λ + ε_density
```

Where:
- `ε_score` = score estimation error
- `ε_density` = density approximation error
- `λ` = barrier curvature (replaces Lipschitz constant)

**Advantage over prior work**: Barrier curvature λ provides a **tighter, more interpretable** safety bound compared to Lipschitz constants, which are often overly conservative.

### 4. Online Density Estimation

- Score-based model: learn `∇_u ln p̂_t(u)` directly
- Update rule adapts as simulator provides new samples
- No need for explicit density computation — only score function needed

## Implementation Steps

### Step 1: Define Simulator Interface

```python
class WorldModelSimulator:
    """Black-box simulator that provides feasibility samples."""
    
    def sample_feasible(self, state, n_samples=100):
        """Generate feasible action samples for given state."""
        # Returns actions u that satisfy hard constraints
        raise NotImplementedError
    
    def score_estimate(self, state, action):
        """Estimate score function ŝ_t = ∇_u ln p̂_t(u)."""
        # Computed via score matching or denoising score matching
        raise NotImplementedError
```

### Step 2: Implement PPC Planner

```python
import numpy as np

class PPCPlanner:
    """Penalized Predictive Control planner."""
    
    def __init__(self, cost_fn, simulator, barrier_curvature=1.0, n_samples=256):
        self.cost_fn = cost_fn          # J(u)
        self.simulator = simulator       # World model
        self.lam = barrier_curvature     # λ (barrier curvature)
        self.n_samples = n_samples
    
    def plan(self, state):
        # 1. Get feasibility samples from simulator
        samples = self.simulator.sample_feasible(state, self.n_samples)
        
        # 2. Evaluate costs
        costs = np.array([self.cost_fn(u, state) for u in samples])
        
        # 3. Get score estimates from simulator
        scores = np.array([self.simulator.score_estimate(state, u) for u in samples])
        
        # 4. Compute unnormalized Gibbs-Boltzmann weights
        log_weights = -costs / self.lam + scores
        
        # 5. Sample action from policy
        weights = np.exp(log_weights - np.max(log_weights))  # numerically stable
        probs = weights / np.sum(weights)
        idx = np.random.choice(len(samples), p=probs)
        
        return samples[idx]
```

### Step 3: Safety Monitoring

```python
def monitor_safety(planner, simulator, state, action, threshold):
    """Monitor safety bound and alert if potentially violated."""
    score_err = simulator.estimate_score_error(state)
    density_err = simulator.estimate_density_error(state)
    safety_distance = score_err / planner.lam + density_err
    
    if safety_distance > threshold:
        print(f"WARNING: Safety bound {safety_distance:.4f} exceeds threshold {threshold}")
        return False
    return True
```

## Key Design Parameters

| Parameter | Role | Typical Range | Notes |
|-----------|------|---------------|-------|
| `λ` (barrier curvature) | Safety margin | 0.1 – 10.0 | Higher = safer but more conservative |
| `n_samples` | Planning resolution | 64 – 1024 | More samples = better approximation |
| Score model complexity | Density estimation quality | Depends on problem | Over-parameterization helps |
| Simulator fidelity | Ground-truth accuracy | Problem-dependent | Black-box; no gradient needed |

## Advantages over Prior Methods

1. **vs. CBF (Control Barrier Functions)**: No Lipschitz constant needed; barrier curvature λ is tighter
2. **vs. Robust MPC**: Does not require explicit uncertainty sets; handles black-box simulators
3. **vs. Marginal density approaches**: Contextual density conditioning on current state improves performance
4. **vs. Frozen density models**: Online density updates adapt to changing feasibility manifolds

## Application Domains

- Autonomous vehicle navigation with dynamic obstacles
- Robot manipulation with safety constraints
- Power system control with equipment limits
- Aerospace trajectory optimization
- Any CPS where black-box simulators exist but gradients don't

## Pitfalls & Caveats

1. **Score estimation quality** is critical — poor scores → loose safety bounds
2. **Barrier curvature λ** tuning: too low → unsafe; too high → overly conservative
3. **Sample efficiency**: Black-box simulators may be expensive; consider caching/replay
4. **Partition function Z** intractable in high dimensions; use sampling-based approximation
5. **Non-convex feasibility manifolds** may require many samples for good coverage

## References

- arXiv:2604.19639v1 — Safety-Critical Contextual Control via Online Riemannian Optimization with World Models (Tongxin Li, 2026)
- Related: Control Barrier Functions (Ames et al., 2017)
- Related: Score-based generative models (Song & Ermon, 2019)
- Related: World Models (Ha & Schmidhuber, 2018)
