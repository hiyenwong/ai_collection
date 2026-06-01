---
name: extended-predictive-coding-free-energy-exponential-family
description: Extended predictive coding framework using exponential-family distributions for biologically plausible variational free-energy minimization, enabling nonlinearity, heterogeneity, and positive firing rates.
---

# Extended Predictive Coding Framework as Variational Free-Energy Minimisation Under Exponential-Family Assumption

**arXiv**: [2605.30882](https://arxiv.org/abs/2605.30882)
**Date**: 2026-05-29
**Authors**: Asaki Kataoka, Kenji Doya
**Categories**: q-bio.NC (Neurons and Cognition)

## Background

The free-energy principle (FEP) postulates that the brain performs variational Bayesian inference. Under Gaussian assumptions and Laplace approximation, FEP corresponds to predictive coding (PC). However, this limited regime fails to capture:
- **Nonlinearity** of neural responses
- **Heterogeneity** of input-output properties within a network
- **Biological implausibility** of negative firing rates

## Methodology

### Core Innovation: Exponential Family Distribution Assumption

When broader class of probability distributions—exponential family of distributions (EFD)—is assumed for variational posterior and prior:

1. **Missing characteristics are exhibited**: nonlinearity, heterogeneity, positive firing rates
2. **FEP-PC correspondence maintained**: up to second cumulant of posterior
3. **Biologically plausible local plasticity rules**: network can be trained without backpropagation

### Mathematical Framework

Exponential family distributions include:
- Gaussian (mean, variance)
- Poisson (for count data, firing rates)
- Bernoulli (binary)
- Gamma (positive-valued)
- Beta (bounded)

The key insight: **variance depends on mean** in EFD (unlike Gaussian with constant variance), enabling:
- Heterogeneous response profiles across neurons
- Automatic nonlinearity from probabilistic structure
- Natural constraint to positive firing rates (Poisson/Gamma)

### Predictive Coding Architecture

Hierarchical generative model:
- **Top-down predictions**: prior expectations from higher layers
- **Bottom-up errors**: prediction errors from lower layers
- **Local plasticity**: each layer updates based on local signals

## Key Findings

1. **EFD assumption yields biological realism**: 
   - Positive firing rates (no negative activity)
   - Neuron-specific input-output properties
   - Nonlinear dynamics without explicit nonlinear activation

2. **Local plasticity rules work**: 
   - Training converges without global error signals
   - Each neuron learns from local prediction error and state

3. **Variational inference preserved**: 
   - Second cumulant (variance) of posterior matches PC theory
   - Explains perceptual inference as Bayesian updating

4. **Connection to Marr's levels**: 
   - Computational: variational free-energy minimization
   - Algorithmic: predictive coding with EFD
   - Implementational: local synaptic plasticity

## Applications

### When to Use

- **Modeling sensory cortex**: visual, auditory, somatosensory processing
- **Biologically plausible neural networks**: SNNs, neuromorphic hardware
- **Predictive coding implementations**: beyond Gaussian assumption
- **Perceptual inference models**: variational Bayesian approaches
- **Local learning rules**: designing hardware-friendly training algorithms

### Activation Keywords

- predictive coding, free-energy principle, exponential family
- biological plausibility, local plasticity, firing rates
- variational inference, sensory cortex, heterogeneous neurons
- Poisson distribution, positive activity constraints

## Pitfalls

1. **Complexity of EFD**: implementation more complex than Gaussian PC
2. **Cumulant truncation**: only second cumulant preserved—higher-order moments may deviate
3. **Convergence speed**: local rules may converge slower than backpropagation
4. **Choice of distribution**: must match neural coding properties (Poisson for rates, Gaussian for membrane potential)

## Related Skills

- [predictive-coding-light](predictive-coding-light) — simplified predictive coding for SNNs
- [free-energy-moe-routing](free-energy-moe-routing) — FEP for MoE routing
- [neuromodulated-synaptic-plasticity](neuromodulated-synaptic-plasticity) — three-factor learning rules
- [spiking-neural-network-analysis](spiking-neural-network-analysis) — SNN training methods

## References

- Original paper: arXiv:2605.30882
- Friston (2010): Free-energy principle
- Rao & Ballard (1999): Predictive coding in visual cortex
- Bogacz (2017): Tutorial on predictive coding