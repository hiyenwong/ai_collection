---
name: predictive-coding-exponential-family-plasticity
description: "Enhanced predictive coding framework combining exponential-family distribution assumption with biologically plausible local plasticity rules. Extends the free-energy principle beyond Gaussian/Laplace approximation, capturing neural heterogeneity, nonlinearity, and non-negative firing rates. Second-cumulant correspondence maintains FEP-PC connection. Use when: predictive coding, free energy principle implementations, biologically plausible learning rules, exponential family distributions, variational inference in neural networks, local plasticity rules, perceptual inference modeling."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.30882"
  published: "2026-05-29"
  authors: "Asaki Kataoka, Kenji Doya"
  tags: [predictive-coding, free-energy-principle, exponential-family, local-plasticity, variational-inference, neural-dynamics]
---

# Predictive Coding with Exponential Family & Local Plasticity

## Core Concept

Extends the free-energy principle (FEP) and predictive coding (PC) correspondence beyond the Gaussian assumption. By assuming the exponential family of distributions (EFD) for variational posterior and prior, the framework captures biological neural network properties that Gaussian PC misses: nonlinearity, heterogeneity of input-output properties, and non-negative firing rates. Maintains FEP-PC correspondence up to the second cumulant while enabling training via biologically plausible local plasticity rules.

## Key Innovation

**Gaussian PC Limitations → Exponential Family Solution:**

| Gaussian PC Limitation | Exponential Family Solution |
|------------------------|---------------------------|
| Negative firing rates | Natural parameterization ensures non-negative rates |
| Homogeneous neurons | EFD naturally captures heterogeneous response curves |
| Linear input-output | Nonlinear response through EFD link functions |
| Global error signals | Local plasticity rules derived from EFD gradients |

## Mathematical Framework

### Variational Free Energy under EFD

For variational posterior q(z) and prior p(z) both in the exponential family:

```
q(z) = h(z) exp(η_q · T(z) - A(η_q))
p(z) = h(z) exp(η_p · T(z) - A(η_p))
```

where η are natural parameters, T(z) are sufficient statistics, A(·) is the log-partition function.

Free energy F = E_q[log q(z) - log p(z|x)] decomposes into cumulant terms:
- First cumulant (mean): matches Gaussian case
- Second cumulant (variance): additional terms capture EFD-specific structure

### Local Plasticity Rules

Derive local update rules from EFD natural gradient:

```
Δw_ij ∝ ∂F/∂w_ij = E_q[∂log q/∂w_ij · (log p(x|z) + log p(z) - log q(z))]
```

Key property: each weight update depends only on local pre/post-synaptic activity and prediction error — no global backpropagation needed.

### FEP-PC Correspondence (Second Cumulant)

The correspondence between FEP minimization and predictive coding dynamics is maintained up to the second cumulant of the posterior:
- Mean dynamics → prediction error minimization (same as Gaussian PC)
- Variance dynamics → precision-weighted prediction (new: EFD-specific terms)

## Implementation Patterns

### Pattern 1: EFD Neural Network Layer

```python
class EFD_PCLayer:
    """Predictive coding layer with exponential family assumption"""
    
    def __init__(self, family="gamma"):  # gamma, inverse-gaussian, etc.
        self.family = family
        # Natural parameters → sufficient statistics mapping
        
    def forward(self, x, prediction_error):
        # Compute prediction under EFD assumption
        predicted = self.link_function(self.natural_params)
        error = x - predicted
        
        # Precision-weighted update (EFD-specific)
        precision = self.precision_from_natural_params()
        weighted_error = precision * error
        
        return predicted, weighted_error
    
    def local_update(self, pre, post, error):
        """Biologically plausible local plasticity rule"""
        # Hebbian-like: depends only on local signals
        delta_w = pre * error  # No global gradient needed
        return delta_w
```

### Pattern 2: Multi-Layer EFD Predictive Coding

```
Layer L (output) → Layer L-1 → ... → Layer 1 (input)
Each layer:
  1. Compute prediction from above
  2. Compute prediction error from below  
  3. Update natural parameters via local plasticity
  4. Pass prediction error upward
```

### Pattern 3: Specific EFD Families

| EFD Family | Neuron Type | Response Shape |
|------------|------------|----------------|
| Gamma | Regular spiking | Positive, skewed |
| Inverse Gaussian | Burst firing | Positive, heavy-tailed |
| Poisson | Spike counting | Discrete, count-based |
| Von Mises | Orientation tuning | Circular |

## Pitfalls

- **Family Selection**: Wrong EFD family → poor fit to neural data. Gamma for firing rates, Von Mises for tuning curves
- **Numerical Stability**: EFD log-partition function A(η) can overflow for extreme natural parameters
- **Convergence**: EFD PC may converge slower than Gaussian PC due to higher-order cumulant terms
- **Second Cumulant Limit**: FEP-PC correspondence breaks at third+ cumulants — full equivalence requires all orders
- **Local vs Global**: Local plasticity rules converge to different solutions than backprop — don't expect identical performance on standard benchmarks

## Relationship to Existing Skills

- **extended-predictive-coding-exponential-family**: Same paper, broader scope — this skill focuses on the plasticity/implementation aspects
- **predictive-coding-light**: Simpler spiking PC — this skill adds the EFD formalism
- **online-generalised-predictive-coding**: Online variant — this skill provides the distributional foundation

## Activation Keywords
- exponential family predictive coding, EFD predictive coding
- biologically plausible local plasticity, local learning rules
- free energy principle beyond gaussian, FEP exponential family
- predictive coding non-negative firing rates
- variational inference exponential family, natural parameter neural networks
- 指数族预测编码, 局部可塑性规则
