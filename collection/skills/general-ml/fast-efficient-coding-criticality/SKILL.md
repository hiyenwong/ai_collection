---
name: fast-efficient-coding-criticality
version: "1.0"
description: "Fast efficient coding and sensory adaptation in gain-adaptive recurrent networks. Theoretical framework showing gain modulation in recurrent circuits reconciles adapter-repulsion and prior-attraction under a unified efficient-coding objective."
tags:
  - computational-neuroscience
  - efficient-coding
  - sensory-adaptation
  - recurrent-networks
  - neural-coding
  - gain-modulation
  - theoretical-neuroscience
trigger_conditions:
  - "efficient coding sensory adaptation"
  - "adapter repulsion prior attraction"
  - "gain modulation recurrent network"
  - "neural tuning curve adaptation"
  - "sensory prior neural coding"
  - "recurrent circuit efficient coding"
source: "PubMed PMID:42140911 / Nature Communications 2026"
authors: ["Arthur Prat-Carrabin", "Maximilian V. Harl", "Samuel J. Gershman"]
doi: "10.1038/s41467-026-73032-0"
---

# Fast Efficient Coding and Sensory Adaptation in Gain-Adaptive Recurrent Networks

## Overview

This paper presents a **gain-adaptive recurrent network model** that unifies two seemingly contradictory empirical phenomena in sensory neuroscience under a single efficient-coding framework:

- **Adapter repulsion**: Tuning curves shift *away* from an adapting stimulus
- **Prior attraction**: Tuning curves shift *toward* frequently-seen stimuli

The resolution: gain modulation propagated through recurrent connections mediates rapid, environment-adaptive efficient coding.

## Core Problem

Efficient coding theory predicts that neural representations should adapt to match the statistical structure of the environment. However:

1. **Prior attraction** is expected: encode more precisely where stimuli are frequent
2. **Adapter repulsion** is observed: tuning curves repel from repeated stimuli
3. These appear contradictory — the same physical mechanism cannot produce both

## Key Insight

The reconciliation lies in the **shape of the prior distribution**:
- **Peaked (narrow) priors** → adapter repulsion (local gain suppression + recurrent propagation)
- **Broad (diffuse) priors** → prior attraction (global gain enhancement at prior peak)

Both emerge from the same gain-modulation mechanism optimizing an efficient-coding objective.

## Mathematical Framework

### Efficient Coding Objective
```
L = Accuracy - λ · Spiking_Cost
  = E[log p(s | r)] - λ · Σ_i E[r_i]
```
where:
- `s` = stimulus, `r` = neural response
- `λ` = metabolic cost weight
- Optimal tuning curves maximize accuracy per spike

### Gain Modulation Dynamics
```
τ · dg_i/dt = -g_i + f(I_i + Σ_j W_ij · g_j)
```
where:
- `g_i` = gain of neuron i
- `W_ij` = recurrent weight matrix
- `f(·)` = nonlinear activation
- `τ` = adaptation time constant (fast, ~100ms)

### Tuning Curve Update
```
TC_i(θ) = g_i · TC_i^0(θ - Δθ_i)
```
- Amplitude modulated by gain `g_i`
- Preferred orientation shifts by `Δθ_i` (repulsion or attraction)

## Predictions and Validation

### Adapter Repulsion (Peaked Prior)
- After 500ms of adaptation to orientation θ_adapt
- Tuning curves repel: preferred angle shifts away from θ_adapt
- Model matches: Δθ ∝ derivative of gain function at θ_adapt

### Prior Attraction (Broad Prior)
- With broad Gaussian prior over orientations
- Tuning curves attract: densify near peak of prior
- **Behavioral experiment**: participants' perceptual precision increases near prior peak ✓

## Implementation

### Minimal Recurrent Gain Model
```python
import numpy as np
from scipy.integrate import odeint

def gain_adaptive_network(g0, W, tau, dt=0.001, T=0.5):
    """
    g0: initial gains (N,)
    W: recurrent weight matrix (N, N)
    tau: adaptation time constant
    """
    def dynamics(g, t, W, tau):
        I = np.tanh(W @ g)  # recurrent input
        return (-g + I) / tau
    
    t = np.arange(0, T, dt)
    g_traj = odeint(dynamics, g0, t, args=(W, tau))
    return g_traj

def tuning_curve_after_adaptation(TC0, g_adapted, theta_grid):
    """Compute adapted tuning curves given gain modulation"""
    g_norm = g_adapted / g_adapted.mean()
    return TC0 * g_norm[:, None]  # gain-scaled tuning curves
```

### Fitting to Neural Data
```python
def fit_efficient_coding_model(responses, stimuli, priors, lambda_cost=0.1):
    """
    Fit gain-adaptive model to recorded neural responses
    
    responses: (n_trials, n_neurons) array
    stimuli: (n_trials,) stimulus values
    priors: prior distribution over stimulus space
    """
    from scipy.optimize import minimize
    
    def objective(params):
        W = params.reshape(n_neurons, n_neurons)
        g = run_gain_dynamics(W, stimulus_history)
        predicted = compute_tuning_curves(g, stimuli)
        nll = -np.sum(scipy.stats.norm.logpdf(responses, predicted))
        return nll + lambda_cost * np.sum(g)
    
    result = minimize(objective, x0=np.random.randn(n_neurons**2))
    return result.x.reshape(n_neurons, n_neurons)
```

## Activation Keywords
- efficient coding, neural coding, sensory adaptation
- adapter repulsion, prior attraction, tuning curves
- gain modulation, recurrent circuits, neural adaptation
- orientation tuning, V1 adaptation, sensory prediction

## Connection to Prior Work

| Phenomenon | Previous Explanation | This Model |
|------------|---------------------|------------|
| Adapter repulsion | Fatigue/suppression | Gain modulation + recurrent propagation |
| Prior attraction | Bayesian inference | Same gain mechanism, different prior shape |
| Fast adaptation | Unclear mechanism | Rapid gain normalization (τ ~100ms) |
| Slow consolidation | Synaptic plasticity | Structural reweighting (separate timescale) |

## When to Use This Skill
- Modeling sensory cortex adaptation (V1, A1, S1)
- Building normative models of neural tuning curve plasticity  
- Designing adaptive SNNs that match biological adaptation timescales
- Analyzing why neural representations shift after adaptation

## Pitfalls
- Recurrent weight matrix W must be stabilized (spectral radius < 1) to avoid runaway dynamics
- Timescale separation (fast gain vs. slow synaptic) is crucial — don't conflate
- Prior shape (peaked vs. broad) critically determines direction of adaptation effect

## References
- Prat-Carrabin, Harl, Gershman (2026). *Nature Communications* DOI:10.1038/s41467-026-73032-0
- Simoncelli & Olshausen (2001) — efficient coding in V1
- Wainwright (1999) — locally linear ICA and gain modulation
- Wei & Stocker (2015) — Bayesian efficient coding
