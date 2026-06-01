---
name: extended-predictive-coding-exponential-family
description: Extended Predictive Coding framework using exponential-family distributions for variational free-energy minimization with biological plausibility
version: 1.0.0
created: 2026-06-01
source: arXiv:2605.30882
authors: Asaki Kataoka, Kenji Doya
tags: [predictive-coding, free-energy-principle, exponential-family, neural-dynamics, variational-inference, local-plasticity]
activation:
  - extended predictive coding
  - exponential family
  - free energy
  - variational inference
  - local plasticity
---

# Extended Predictive Coding: Exponential Family Framework

## Overview
This methodology extends Predictive Coding beyond Gaussian assumptions using **Exponential Family Distributions (EFD)**, enabling:
- Non-negative neural firing rates
- Heterogeneous input/output properties  
- Biologically plausible activity
- Local plasticity rules

## Mathematical Foundation

### Free Energy Principle (FEP)
```
FEP: Minimize variational free energy F ≈ -log p(o|v) + KL[q(v)||p(v|o)]
```

### Classic Gaussian PC Limitations
1. **Negative firing rates** (biologically impossible)
2. **Homogeneous units** (ignores neural diversity)
3. **Linear responses** (misses nonlinear dynamics)
4. **No spike generation** (continuous-only)

### EFD Solution
```
p(x|η) = h(x) exp[η·T(x) - A(η)]
```
- All distributions have **non-negative firing rates**
- **Heterogeneous units** (different distribution per neuron)
- **Nonlinear responses** via natural parameter space
- **Local plasticity** (biologically plausible)

## Neural Distribution Types

| Distribution | Use Case | Natural Parameters |
|-------------|----------|-------------------|
| Bernoulli | Binary spiking | η = log(p/(1-p)) |
| Poisson | Spike counts | η = log(λ) |
| Gaussian | Continuous | η = (μ/σ², -1/2σ²) |
| Gamma | Firing rates | η = (-α, -β) |

## Multi-Layer Hierarchy
```
Layer 0 (sensory): Poisson (spike counts)
Layer 1 (V1): Bernoulli (binary spiking)
Layer 2 (V2): Gaussian (continuous)
Layer 3 (output): Gamma (rate coding)
```

## Implementation

### Prediction Updates
```python
prediction_error = η_lower - prediction_upper
error_signal = η_upper - prediction_lower

# Gradient descent on free energy
dη/dt = -∂F/∂η = T(x) - E[T(x)] + ∂prediction/∂η · error_signal
```

### Weight Learning (Local Plasticity)
```python
Δw = prediction_error × activity_pre  # Hebbian-like
Δprecision = prediction_variance  # adaptive weighting
```

## Biological Plausibility Validation

| Check | Result |
|-------|--------|
| Non-negative firing | ✓ Always ≥ 0 |
| Local learning | ✓ Weight updates use local information |
| Nonlinear responses | ✓ Natural parameter space nonlinear |
| Heterogeneous units | ✓ Different layers use different distributions |

## Applications
- Sensory processing: V1/V2/V4 modeling
- Hierarchical inference: multi-layer predictions
- Motor control: rate-coded commands
- Memory and learning: predictive sequences

## Related Skills
- predictive-coding-light
- free-energy-moe-routing
- online-generalised-predictive-coding

## References
- arXiv:2605.30882 (this paper)
- Friston (2010): Free Energy Principle