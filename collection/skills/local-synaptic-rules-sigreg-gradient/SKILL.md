---
name: local-synaptic-rules-sigreg-gradient
description: Local synaptic learning rules (STDP+ and homeostatic plasticity) can implement exact SIGReg-like self-supervised learning gradients without backpropagation, global error signals, or weight transport.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [neuroscience, spiking-neural-networks, synaptic-plasticity, gradient-learning, biologically-plausible]
    related_skills: [spiking-neural-network-analysis, stdp-bernoulli-message-passing, feedback-hebbian-continual-learning]
---

# Local Synaptic Rules Implement SIGReg Gradient

This skill implements the methodology from arXiv:2607.21622 "Local Synaptic Rules Can Implement a SIGReg Gradient Without Backpropagation" by Martin Andrews.

## Core Insight

Two canonical local synaptic learning rules together can implement the exact gradient of a SIGReg-like self-supervised learning objective:
1. **Potentiation arm of spike-timing-dependent plasticity (STDP⁺)**
2. **Homeostatic plasticity** (instantiated via flashlight granule-cell-like neurons)

This equivalence requires:
- No gradient calculations
- No global error signals  
- No weight transport
- No label information
- Only inputs: pre- and post-synaptic firing rates, local firing statistics, and temporal contiguity of natural sensory streams

## Implementation Steps

### 1. Network Architecture Setup
```python
# Two-layer network with appropriate neuron models
# Input layer: sensory neurons with temporal ordering
# Hidden layer: neurons with STDP⁺ and homeostatic plasticity
```

### 2. STDP⁺ Rule Implementation
```python
# Potentiation-only STDP rule
def stdp_potentiation(pre_spike_time, post_spike_time, A_plus, tau_plus):
    if post_spike_time > pre_spike_time:  # Causal relationship
        delta_t = post_spike_time - pre_spike_time
        return A_plus * exp(-delta_t / tau_plus)
    return 0
```

### 3. Homeostatic Plasticity Implementation
```python
# Flashlight granule-cell-like homeostatic mechanism
def homeostatic_plasticity(firing_rate, target_rate, eta_homeo):
    return eta_homeo * (target_rate - firing_rate)
```

### 4. Combined Weight Update Rule
```python
def combined_update_rule(weight, pre_rate, post_rate, local_stats, temporal_context):
    # STDP⁺ component based on spike timing
    stdp_component = compute_stdp_potentiation(pre_rate, post_rate, temporal_context)
    
    # Homeostatic component based on firing rate deviation
    homeo_component = homeostatic_plasticity(post_rate, target_rate, eta_homeo)
    
    # Total weight change implements SIGReg gradient
    delta_weight = stdp_component + homeo_component
    
    return weight + learning_rate * delta_weight
```

### 5. Temporal Ordering Requirement
- Input presentation must preserve temporal contiguity of natural sensory streams
- Random ordering fails to recover class structure
- Ordered presentation enables cluster separation through temporal statistics alone

## Validation Tasks

### Synthetic Clustering Task
- **Purpose**: Probe whether class structure can be recovered from temporal ordering alone
- **Metric**: Cluster Separation Ratio (CSR)
- **Expected Results**: 
  - Ordered presentation: CSR ≈ 2.49 (≈3.5σ separation)
  - Random ordering: CSR ≈ 0.83 (near baseline)

### Temporally Ordered MNIST
- **Architecture**: Two-layer network trained entirely with local rules
- **Evaluation**: Linear-probe accuracy on learned representations
- **Expected Result**: ~87.3% accuracy

## Biological Plausibility Advantages

1. **No weight transport problem**: Updates use only locally available information
2. **No global error signals**: Learning driven by local firing statistics and temporal contiguity
3. **Biologically realistic mechanisms**: Uses established synaptic plasticity rules
4. **Self-supervised**: No labels required, learns from natural temporal structure

## Applications

- **Biologically plausible deep learning**: Bridge between neuroscience and AI
- **Neuromorphic hardware**: Energy-efficient learning without backpropagation
- **Unsupervised representation learning**: Extract structure from temporal data streams
- **Continual learning**: Natural integration with online learning scenarios

## Activation Keywords

- local synaptic rules
- STDP gradient learning  
- biologically plausible backpropagation
- SIGReg without backprop
- temporal ordering clustering
- homeostatic plasticity gradient

## References

- Andrews, M. (2026). Local Synaptic Rules Can Implement a SIGReg Gradient Without Backpropagation. arXiv:2607.21622
- Original SIGReg framework: Self-supervised learning through temporal prediction
- Biological STDP: Caporale & Dan (2008), Markram et al. (1997)
- Homeostatic plasticity: Turrigiano (2012), Zenke et al. (2013)