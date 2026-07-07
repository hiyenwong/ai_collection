---
name: extended-predictive-coding-exponential-family
description: "Extended Predictive Coding framework using exponential-family distributions for variational free-energy minimization. Captures biological network properties: nonlinearity, heterogeneity, positive firing rates. Biologically plausible local plasticity rules. Activation: predictive coding, exponential family, free-energy principle, variational inference, local plasticity, 预测编码, 自由能原理."
---

# Extended Predictive Coding under Exponential-Family Assumption

**Source**: arXiv:2605.30882 | **Submitted**: 2026-05-29  
**Authors**: Asaki Kataoka, Kenji Doya  
**Category**: q-bio.NC (Neurons and Cognition)

## Core Contribution

Extends Free-Energy Principle (FEP) and Predictive Coding (PC) from **Gaussian assumption** to **Exponential Family Distributions (EFD)**, capturing biological neural network properties:

1. **Nonlinearity** of neural responses
2. **Heterogeneity** of input-output properties
3. **Positive firing rates** (biological constraint)

## Problem with Gaussian Assumption

Traditional FEP-PC correspondence under Gaussian + Laplace approximation:
- Linear input-output relationships
- Homogeneous neuron populations
- **Negative firing rates** (biologically implausible)
- Limited explanatory power for sensory cortex dynamics

## Solution: Exponential Family Distributions

EFD includes:
- **Bernoulli** (binary neurons)
- **Poisson** (spiking neurons)
- **Exponential** (positive firing rates)
- **Gamma** (firing rate distributions)
- **Beta** (bounded activity)

**Key result**: FEP-PC correspondence maintained **up to second cumulant** of posterior.

## Biologically Plausible Properties

### 1. Nonlinearity
- Nonlinear transfer functions emerge naturally
- Matches cortical neuron response curves
- No artificial linearization required

### 2. Heterogeneity
- Different neuron types → different EFD members
- Specialized populations (excitatory/inhibitory)
- Population-specific priors

### 3. Positive Firing Rates
- EFD naturally constrains to positive domain
- No negative firing rate artifacts
- Matches physiological observations

## Local Plasticity Rules

**Critical contribution**: Model trained via **biologically plausible local rules**:

- Prediction errors computed locally
- Synaptic updates depend on local signals
- No global error propagation (vs. backprop)
- Compatible with cortical microcircuits

### Plasticity Mechanism
```
Δw_ij = η * (prediction_error_i * activity_j)
```

where:
- `prediction_error_i` = mismatch between predicted and observed
- `activity_j` = presynaptic firing rate
- Updates are local (no global optimizer)

## Variational Free-Energy Minimization

Under exponential-family assumption:

```
F = E_q[log q(z) - log p(z, x)]
  ≈ KL[q(z) || p(z|x)] - log p(x)
```

Minimized via:
- Variational posterior `q(z)` from EFD family
- Prior `p(z)` also from EFD
- Matching moments up to second order

## Neural Implementation

### Cortical Microcircuit Model

**Layers**:
- **L4**: Sensory input → prediction error computation
- **L2/3**: Prediction generation via EFD
- **L5/6**: Feedback to lower areas

**Dynamics**:
1. Input arrives at L4
2. L2/3 generates prediction (EDF parameters)
3. L4 computes error (observed - predicted)
4. Local plasticity updates predictions
5. L5/6 sends feedback

### Heterogeneous Populations

- **Excitatory**: Exponential/Gamma distribution (positive firing)
- **Inhibitory**: Beta distribution (bounded suppression)
- **Binary**: Bernoulli (decision neurons)

## Advantages over Gaussian PC

| Property | Gaussian PC | Exponential Family PC |
|----------|-------------|----------------------|
| Firing rates | Can be negative | Always positive |
| Nonlinearity | Linear transfer | Natural nonlinearity |
| Heterogeneity | Homogeneous | Population-specific |
| Plasticity | Global gradient | Local biologically plausible |
| Explanatory power | Limited | Rich biological properties |

## Applications

- **Sensory cortex**: V1/V2 perceptual inference
- **Motor cortex**: Action prediction
- **Hippocampus**: Memory prediction
- **Spiking networks**: Neural coding models

## Methodological Checklist

```markdown
- [ ] Select appropriate EFD member for neuron type
- [ ] Set prior parameters (natural parameters)
- [ ] Initialize variational posterior
- [ ] Compute prediction errors locally
- [ ] Apply local plasticity rules
- [ ] Validate positive firing rates
- [ ] Compare with Gaussian baseline
```

## Implementation Outline

```python
import numpy as np

class ExponentialFamilyPC:
    def __init__(self, distribution_type='poisson'):
        self.dist_type = distribution_type
        # Natural parameters: θ = (η1, η2)
        self.prior_params = np.array([0.5, 1.0])
        
    def compute_prediction_error(self, observed, predicted):
        # Local error computation
        error = observed - predicted
        return error
    
    def local_plasticity(self, error, presynaptic_activity, eta=0.01):
        # Biologically plausible update
        delta_w = eta * error * presynaptic_activity
        return delta_w
    
    def enforce_positive_firing(self, firing_rate):
        # EFD constraint
        return np.maximum(firing_rate, 0)
```

## Research Questions

1. How do different EFD members affect prediction accuracy?
2. What's the optimal prior for each neuron type?
3. How does heterogeneity improve inference?
4. Can local rules achieve convergence?
5. What's the relationship to STDP?

## Key References

- Free-Energy Principle: Friston (2010)
- Predictive Coding: Rao & Ballard (1999)
- Exponential Family: McCullagh & Nelder (1989)
- Local Learning: Doya (2000)
- Biological Plausibility: Lillicrap et al. (2020)

## Activation Triggers

Use this skill when:
- Implementing biologically plausible predictive coding
- Modeling positive firing rate constraints
- Building heterogeneous neural populations
- Studying local plasticity rules
- Comparing Gaussian vs. exponential family inference

## Citation

```bibtex
@article{kataoka2026extended,
  title={Extended predictive coding framework as variational free-energy minimisation under exponential-family assumption},
  author={Kataoka, Asaki and Doya, Kenji},
  journal={arXiv preprint arXiv:2605.30882},
  year={2026}
}
```

## Theoretical Bridge

This work bridges **computational theory** (FEP) and **biological implementation**:
- Free-energy principle → variational inference
- Exponential family → biological neuron properties
- Local plasticity → cortical microcircuits

**Insight**: Theoretical frameworks gain explanatory power when accounting for biological constraints.