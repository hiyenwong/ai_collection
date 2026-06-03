---
name: local-gradient-approximations-rnn
description: Dynamics and Representation Structure of Local Approximations to Gradient-Based Learning in Linear Recurrent Neural Networks — analyzing RFLO, tBPTT, and BPTT learning dynamics with locality constraints.
version: 1.0.0
author: Hermes Agent (Cron Job)
license: MIT
date: 2026-06-03
arxiv: 2606.00243
paper_title: "Dynamics and Representation Structure of Local Approximations to Gradient-Based Learning in Linear Recurrent Neural Networks"
authors: "Ezekiel Williams, Alexandre Payeur, Guillaume Lajoie"
venue: ICML 2026
metadata:
  hermes:
    tags: [neuromorphic, rnn, learning-dynamics, rflo, tbptt, locality-constraints, bptt]
    related_skills: [neuromorphic-continual-nuclear-ics, snn-learning-survey, decolle-snn-learning]
---

# Local Gradient Approximations in RNNs

## Overview

This paper applies dynamical systems theory to analyze how locality constraints shape learning dynamics in recurrent neural networks (RNNs). It compares RFLO (Random Feedback Local Online), truncated BPTT (tBPTT), and full BPTT in data-aligned linear RNNs.

## Core Contribution

**Key Finding**: RFLO learning is restricted to low-rank perturbations of initial parameters, yielding qualitatively distinct behavior from BPTT and one-step tBPTT.

## Methods

### Data-Aligned Linear RNNs
- Dynamics separated into orthogonal modes
- Enables analytical comparison of stationary solutions, stability properties, convergence rates

### Local Approximation Algorithms
1. **RFLO (Random Feedback Local Online)**: Neglects all non-local gradient terms
2. **tBPTT (Truncated BPTT)**: Truncates gradient computation after K steps
3. **BPTT**: Full backpropagation through time

## Key Results

| Algorithm | Stationary Solutions | Stability | Convergence Rate |
|-----------|---------------------|-----------|------------------|
| BPTT | Full rank updates | Standard | Fast |
| tBPTT (1-step) | Intermediate | Modified | Medium |
| RFLO | Low-rank perturbations | Distinct | Slow |

### Low-Rank Restriction
RFLO solutions are restricted to low-rank perturbations of initial parameters:
- This constraint holds beyond the data-aligned setting
- Implications for neuromorphic hardware with locality constraints

## Applications

1. **Neuroscientific Models**: Understanding how biological learning constraints shape neural representations
2. **Neuromorphic Hardware**: Optimizing on-chip learning algorithms respecting locality
3. **Alternative Optimization**: Developing new learning rules that balance locality and performance

## Implementation Notes

### RFLO Algorithm
```python
# RFLO: Local feedback with random weights
def rflo_update(W, x, y, B_random):
    # B_random: Fixed random feedback weights (not backprop)
    local_error = compute_local_error(x, y)
    dW = B_random @ local_error @ x.T  # Local approximation
    W += learning_rate * dW
```

### Data-Aligned Linear RNN
```python
# Orthogonal mode decomposition
def data_aligned_rnn(W, x, modes):
    # Dynamics: x_{t+1} = W @ x_t + input
    # Separated into orthogonal modes for analysis
    mode_activations = project_to_modes(x, modes)
    return mode_activations
```

## Theoretical Insights

1. **Locality Constraint Effects**:
   - Limits solution space to low-rank perturbations
   - Creates qualitatively different learning dynamics
   - Affects stability properties

2. **Representation Structure**:
   - RFLO learns representations constrained by initial parameters
   - BPTT can explore full parameter space
   - tBPTT intermediate behavior

## Biological Motivation

Neural circuits face:
- **Spatial locality**: Only local synaptic updates
- **Temporal locality**: Limited memory of past activity
- **RFLO**: Plausible approximation for biological learning

## References

- Williams et al. (2026): "Dynamics and Representation Structure of Local Approximations to Gradient-Based Learning in Linear Recurrent Neural Networks", ICML 2026
- Lillicrap et al. (2016): Random feedback weights support learning
- Marsden et al. (2024): RFLO and feedback alignment

## Activation Keywords

`RFLO`, `tBPTT`, `locality constraints`, `RNN learning dynamics`, `data-aligned RNN`, `low-rank perturbations`, `neuromorphic learning`, `biological learning rules`

## Pitfalls

1. **RFLO convergence**: Slower than BPTT, may not reach optimal solutions
2. **Random feedback**: Fixed random weights may not align with true gradients
3. **Data-aligned assumption**: Linear analysis may not extend to nonlinear RNNs

## Further Reading

- [[snn-learning-survey]] - SNN learning rules survey
- [[decolle-snn-learning]] - DECOLLE local learning
- [[neuromorphic-continual-nuclear-ics]] - Neuromorphic hardware constraints