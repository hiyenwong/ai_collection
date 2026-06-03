---
name: predictive-coding-light
description: "Predictive Coding Light+ (PCL+) methodology for spiking neural network sequence prediction. A spiking neural network architecture for unsupervised sequence processing that learns recurrent excitatory connections with delays to enable short-term retention of information. Combines spike timing-dependent plasticity (STDP) with synaptic delays to learn predictive representations. Successfully reproduces classic visual cortex sequence learning findings and learns to fill in missing inputs in gesture recognition tasks. Activation: Predictive Coding Light+, PCL+, STDP sequence learning, spiking neural network prediction, synaptic delay learning, unsupervised sequence processing, visual cortex sequence learning, short-term memory SNN, predictive coding spiking, spike timing-dependent plasticity sequence, gesture recognition SNN."
---

# Predictive Coding Light+ Methodologyy

## Overview

Predictive Coding Light+ (PCL+) (arXiv: 2605.12732) addresses a fundamental question: how can biological or artificial spiking neural networks learn to maintain past sensory information to predict the future? It proposes a novel SNN architecture combining **spike timing-dependent plasticity (STDP)** with **synaptic delays** to learn recurrent excitatory connections for short-term information retention.

## Core Problem

Successfully predicting future sensory input requires maintaining a memory of the recent past. In spiking neural networks, it remains unclear how to learn this short-term retention without complex recurrent architectures or external memory modules.

## Key Contributions

### 1. PCL+ Architecture

PCL+ learns **recurrent excitatory connections with delays** to maintain a record of the recent past:

- **STDP-driven learning**: Synaptic weights adapt based on spike timing correlations
- **Synaptic delays**: Different connection delays create a distributed temporal buffer
- **Recurrent excitatory connections**: Enable short-term retention without external memory
- **Unsupervised sequence processing**: No labeled data required

### 2. Sequence Learning in Visual Cortex

PCL+ reproduces classic findings on sequence learning in visual cortex, demonstrating:
- Temporal prediction of visual sequences
- Learning of stimulus order statistics
- Emergent selectivity for temporal patterns

### 3. Missing Input "Fill-in"

PCL+ learns to reconstruct missing input in a challenging gesture recognition task:
- Given partial temporal sequences, predict missing components
- Demonstrates robust temporal pattern completion
- Shows how short-term retention supports inference

## Architecture Details

### Core Components

```
Input Layer → [Recurrent Layer with Delays] → Prediction Output
                  ↑ STDP learning rule
                  ← Synaptic delay distribution
```

### STDP with Delays

The key insight is that **synaptic delays create a temporal buffer**:
- Short delays → recent input retention
- Long delays → extended history access
- STDP learns which delays are useful for prediction
- Emergent delay distribution matches task temporal structure

### Learning Rule

```python
# Conceptual STDP update with delays
def stdp_update(pre_spike_time, post_spike_time, delay, weight):
    """STDP rule incorporating synaptic delay"""
    effective_time = post_spike_time - (pre_spike_time + delay)
    
    if effective_time > 0:
        # Pre before post → potentiation
        delta_w = A_plus * exp(-effective_time / tau_plus)
    else:
        # Post before pre → depression
        delta_w = -A_minus * exp(effective_time / tau_minus)
    
    return weight + delta_w
```

## Application to Skill Development

### When to Apply PCL+

- Building energy-efficient sequence prediction models
- Implementing biological short-term memory in SNNs
- Unsupervised learning of temporal patterns
- Gesture recognition with temporal context
- Visual sequence prediction tasks
- Any task requiring "filling in" missing temporal data

### Comparison with Alternative Approaches

| Approach | Memory Mechanism | Supervision | Biological Plausibility |
|----------|-----------------|-------------|------------------------|
| PCL+ | Synaptic delays + STDP | Unsupervised | High |
| RNN/LSTM | Hidden state | Supervised | Low |
| Transformer | Self-attention | Supervised | Low |
| Liquid State | Reservoir dynamics | Supervised (readout) | Medium |

### Implementation Considerations

1. **Delay Distribution**: Use a range of delays (e.g., 1-20ms) to capture different timescales
2. **STDP Parameters**: Tune A+, A-, τ+, τ- for the specific temporal structure
3. **Network Size**: Larger networks capture more complex temporal dependencies
4. **Input Encoding**: Use latency coding or rate coding depending on the task

## Research Implications

1. **Biological plausibility**: Synaptic delays are a known biological mechanism for temporal processing
2. **Energy efficiency**: SNNs with STDP are significantly more energy-efficient than traditional RNNs
3. **Unsupervised learning**: No labeled data required — learns from raw temporal structure
4. **Short-term memory**: Emerges naturally from recurrent connections with delays, no external memory needed

## Related Skills

- `stdp-synaptic-delay-learning` - STDP learning rule extension
- `spiking-neural-network-analysis` - SNN paper analysis methodology
- `spiking-computational-neuroscience-survey` - SNN applications survey
- `spikingjelly-framework` - SNN deep learning framework

## References

- Predictive Coding Light+: arXiv:2605.12732
- Classic visual cortex sequence learning studies
- STDP learning rule literature
