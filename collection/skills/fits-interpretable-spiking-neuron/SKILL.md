---
name: fits-interpretable-spiking-neuron
description: "FiTS (Frequency Selectivity and Temporal Shaping) interpretable spiking neuron model. Factorizes temporal computation into Frequency Selectivity and Temporal Shaping within each neuron. Use when: spiking neural networks, interpretable neurons, temporal processing, frequency selectivity, temporal shaping, LIF neuron improvement, auditory processing, neuron-level interpretability, group-delay modulation, subthreshold magnitude response, feedforward SNNs, spike timing."
---

# FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping

## Paper Reference

- **Title**: FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping
- **arXiv**: 2605.13071
- **Authors**: Jongmin Choi, Joon Son Chung
- **Date**: 2026-05-19
- **Category**: cs.NE (Neural and Evolutionary Computing)

## Core Innovation

FiTS introduces a new spiking neuron model that **factorizes temporal computation** within each neuron into two independent modules:

1. **Frequency Selectivity (FS)**: Parameterizes each neuron's target frequency as the maximizer of its subthreshold magnitude response
2. **Temporal Shaping (TS)**: Reshapes when frequency components contribute to membrane voltage accumulation through group-delay modulation

## Architecture

### FS Module - Frequency Selectivity

- Each neuron learns a **target frequency** parameter
- Subthreshold membrane dynamics are tuned to maximize response at the target frequency
- Provides frequency-selective filtering at the single-neuron level
- Eliminates need for network-level delays or recurrence for temporal modeling

### TS Module - Temporal Shaping

- Controls **when** frequency components contribute to membrane voltage accumulation
- Uses **group-delay modulation** to shift temporal alignment of frequency components
- Enables phase alignment and temporal feature extraction at neuron level

## Key Properties

### Interpretability

- **Target frequencies** provide interpretable neuron-level summaries of frequency organization
- **Group-delay shifts** reveal timing organization learned within the network
- Unlike black-box SNN neurons, FiTS neurons have physically meaningful parameters

### Performance

- Improves over plain LIF baseline on auditory benchmarks
- Competitive with strong temporal SNN baselines (with recurrence/delays)
- Works in **simple feedforward SNNs** without recurrence or network-level delays

### Comparison to LIF

| Feature | LIF | FiTS |
|---------|-----|------|
| Frequency selectivity | No (fixed time constant) | Yes (learnable target frequency) |
| Temporal shaping | No | Yes (group-delay modulation) |
| Interpretability | Limited | High (frequency + timing parameters) |
| Needs recurrence for temporal | Often | No |

## Mathematical Foundation

### Subthreshold Response

The FiTS neuron's subthreshold dynamics are designed such that:

$$H(\omega) = \frac{1}{1 + j\omega\tau - \text{FS terms}}$$

The target frequency $\omega^*$ is learned as the maximizer of $|H(\omega)|$.

### Group Delay

$$\tau_g(\omega) = -\frac{d}{d\omega}\arg H(\omega)$$

The TS module modulates $\tau_g$ to control temporal alignment.

## Use Cases

1. **Auditory processing**: Where frequency selectivity and timing are central
2. **Temporal pattern recognition**: Event-driven temporal processing
3. **Interpretable SNNs**: When neuron-level understanding is required
4. **Energy-efficient temporal modeling**: Feedforward SNNs without recurrence overhead

## Activation Keywords

FiTS, frequency selectivity, temporal shaping, interpretable spiking neurons, LIF neuron, group delay, subthreshold response, auditory SNN, feedforward SNN, temporal processing, spiking neuron design, neuron specialization
