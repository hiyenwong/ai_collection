---
name: predictive-coding-exponential-family
description: Extended predictive coding framework using exponential family distributions for variational free-energy minimization - biologically plausible local plasticity rules
activation_keywords:
  - predictive coding
  - free-energy principle
  - exponential family
  - variational inference
  - neural plasticity
  - sensory cortex
  - Bayesian inference
  - FEP
created: 2026-06-02
source: arXiv:2605.30882
authors: Asaki Kataoka, Kenji Doya
paper_title: "Extended predictive coding framework as variational free-energy minimisation under exponential-family assumption"
category: neuroscience
---

# Extended Predictive Coding: Exponential Family Framework

## Overview

This framework extends the Free-Energy Principle (FEP) beyond Gaussian assumptions by using **Exponential Family Distributions (EFD)**, enabling:

1. **Nonlinearity**: Captures nonlinear input-output properties in neural networks
2. **Heterogeneity**: Models diverse neuron types within networks
3. **Biological Plausibility**: Eliminates negative firing rate issues
4. **Local Plasticity**: Enables biologically realistic learning rules

**Key Innovation**: Maintains FEP-Predictive Coding (PC) correspondence up to the **second cumulant** of the posterior.

## Core Theory

### Gaussian Limitation Problem

Traditional FEP-PC frameworks assume:
- Gaussian distributions for variational posterior/prior
- Laplace approximation
- Linear neural dynamics

**Issues**:
- Cannot capture nonlinear neural responses
- Cannot represent heterogeneous neuron populations
- Negative firing rates in predictions (biologically implausible)
- Limited to uniform variance assumptions

### Exponential Family Solution

**Exponential Family Distributions** generalize beyond Gaussians:
- Poisson: discrete neural spike counts
- Gamma: firing rate distributions
- Beta: bounded neural responses
- Binomial: binary neural decisions

**Mathematical Form**:
```
p(x; θ) = h(x) exp(η(θ)·T(x) - A(θ))
where:
- η(θ): natural parameters
- T(x): sufficient statistics
- A(θ): log-normalizer
```

## Implementation Architecture

### Variational Free-Energy Minimization

**Objective**: Minimize KL divergence between variational posterior q and true posterior p

**Extended Formula**:
```
F = -log p(y) + KL[q(x) || p(x|y)]

With EFD:
q(x) = ExponentialFamily(η_q)
p(x) = ExponentialFamily(η_p)
```

**Second Cumulant Preservation**:
- Maintain correspondence for mean and variance
- Allow higher-order deviations for flexibility
- Trade-off: accuracy vs. biological realism

### Neural Network Architecture

**Multi-layer Predictive Coding**:
```
Layer L: 
  - Prediction μ_L (from higher layer)
  - Error ε_L = actual - prediction
  - Variational update: η_L ← η_L - ∂F/∂η_L
```

**Exponential Family Neurons**:
- Each neuron type uses appropriate EFD member
- Poisson neurons for spike generation
- Gamma neurons for rate modulation
- Beta neurons for bounded activation

### Local Plasticity Rules

**Biologically Plausible Learning**:
1. **Hebbian-like updates**: Only require local information
2. **Error-driven plasticity**: Based on prediction errors
3. **Activity-dependent**: Use neuron-specific sufficient statistics

**Update Rule**:
```python
# For each neuron type
if neuron_type == 'Poisson':
    plasticity_rate = firing_rate * prediction_error
elif neuron_type == 'Gamma':
    plasticity_rate = rate_sufficient_stat * error
elif neuron_type == 'Beta':
    plasticity_rate = bounded_activity * discrepancy
```

## Methodology

### Step 1: Select Distribution Family

**Criteria**:
- Match biological neuron characteristics
- Match data type (discrete, continuous, bounded)
- Ensure tractable inference

**Mapping**:
- Spike counts → Poisson
- Firing rates → Gamma
- Synaptic weights → Beta/Gaussian
- Decision states → Bernoulli

### Step 2: Define Variational Posterior

```python
class ExponentialFamilyPosterior:
    def __init__(self, distribution_type):
        self.family = distribution_type
        self.natural_params = initialize_params()
    
    def sufficient_statistics(self, x):
        return compute_T(x, self.family)
    
    def update(self, error, learning_rate):
        self.natural_params -= learning_rate * grad_free_energy(error)
```

### Step 3: Implement Predictive Coding Loop

```python
for layer in reversed(network_layers):
    # Generate prediction
    prediction = higher_layer.predict(layer)
    
    # Compute error
    error = layer.activity - prediction
    
    # Update variational parameters
    layer.posterior.update(error, lr)
    
    # Propagate error upward
    higher_layer.receive_error(error)
```

### Step 4: Train with Local Plasticity

```python
# Local learning rule
for connection in neural_connections:
    # Only use local variables
    pre_activity = connection.pre_neuron.sufficient_stats()
    post_error = connection.post_neuron.error
    
    # Hebbian-like update
    connection.weight += lr * pre_activity * post_error
```

## Applications

### 1. Sensory Cortex Modeling
- Visual cortex: heterogeneous neuron populations
- Auditory cortex: nonlinear response curves
- Somatosensory cortex: bounded activation ranges

### 2. Spike-Based Learning
- Poisson spike generation
- Rate-based plasticity
- Stochastic inference

### 3. Biologically Realistic ANNs
- Eliminate negative activations
- Implement neuron-type diversity
- Enable local learning rules

## Key Advantages

1. **Biological Plausibility**: No negative firing rates, local learning
2. **Neural Heterogeneity**: Different neuron types with different distributions
3. **Nonlinearity**: Captures nonlinear response properties
4. **Maintained FEP Correspondence**: Still approximates variational inference
5. **Tractable Inference**: EFD members have closed-form updates

## Implementation Example

### Poisson Neuron Predictive Coding

```python
class PoissonPredictiveNeuron:
    def __init__(self):
        self.rate = 0.0  # Poisson parameter λ
        self.error = 0.0
    
    def generate_spikes(self, duration):
        return np.random.poisson(self.rate * duration)
    
    def compute_error(self, actual_spikes, predicted_rate):
        return actual_spikes - predicted_rate * duration
    
    def update_rate(self, error, learning_rate):
        # Local plasticity: only need local error
        self.rate += learning_rate * error
        self.rate = max(0, self.rate)  # Ensure positivity
```

### Gamma Neuron Rate Modulation

```python
class GammaRateNeuron:
    def __init__(self):
        self.alpha = 1.0  # Shape parameter
        self.beta = 1.0   # Rate parameter
    
    def sufficient_statistics(self, firing_rate):
        return [np.log(firing_rate), firing_rate]
    
    def update(self, error, lr):
        # Natural parameter update
        self.alpha += lr * error[0]
        self.beta += lr * error[1]
```

## Comparison with Traditional PC

| Aspect | Gaussian PC | EFD PC |
|--------|-------------|--------|
| Distribution | Gaussian only | Multiple (Poisson, Gamma, Beta...) |
| Firing rates | Can be negative | Always positive (biological) |
| Neuron types | Homogeneous | Heterogeneous |
| Nonlinearity | Linear only | Nonlinear responses |
| Learning | Global gradient | Local plasticity |
| Biological realism | Limited | High |

## Limitations

1. **Approximation Limit**: Only preserves second cumulant (mean, variance)
2. **Parameter Tuning**: Need to select appropriate EFD member
3. **Computational Cost**: More complex than Gaussian
4. **Empirical Validation**: Needs testing with real neural data

## Research Questions

1. How to optimally select EFD member for each neuron type?
2. What is the trade-off between biological realism and inference accuracy?
3. Can this framework scale to large cortical networks?
4. How do higher-order cumulants affect learning dynamics?

## Related Skills

- [[metastable-mind-event-segmentation]]: State-based predictive models
- [[predictive-coding-light]]: Simplified PC implementation
- [[free-energy-moe-routing]]: FEP-based MoE routing
- [[neuromodulated-synaptic-plasticity]]: Neuromodulation for plasticity

## References

- Kataoka & Doya (2026) arXiv:2605.30882
- Friston (2010) Free-Energy Principle
- Dayan et al. (1995) Helmholtz Machines
- Rao & Ballard (1999) Predictive Coding in Visual Cortex

---
**Note**: This framework bridges computational theory (FEP) with biological realism (EFD), enabling more accurate models of sensory cortical inference.