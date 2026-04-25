---
name: sharpness-aware-surrogate-snn-training
description: "Sharpness-Aware Surrogate Training (SAST) for on-sensor Spiking Neural Networks. Reduces surrogate-to-hard transfer gap using SAM optimization for binary spike deployment. Activation: SAST, sharpness-aware training, on-sensor SNN, surrogate gradient."
---

# Title: Sharpness-Aware Surrogate Training for On-Sensor Spiking Neural Networks

## Overview

This skill provides guidance for implementing and working with methodologies from the paper "Title: Sharpness-Aware Surrogate Training for On-Sensor Spiking Neural Networks" (arXiv:2604.09696).

**arXiv ID:** 2604.09696
**Categories:** cs.NE
**PDF:** https://arxiv.org/pdf/2604.09696

## Paper Abstract

> Spiking neural networks (SNNs) are a natural computational model for on-sensor and near-sensor vision, where event driven processors must operate under strict power budgets with hard binary spikes. However, models trained with surrogate gradients often degrade sharply when the smooth surrogate nonlinearity is replaced by a hard threshold at deployment; a surrogate-to-hard transfer gap that directly limits on-sensor accuracy. We study Sharpness-Aware Surrogate Training (SAST), which applies Sharpness-Aware Minimization (SAM) to a surrogate-forward SNN so that the training objective is smooth and the gradient is exact, and position it as one gap-reduction strategy under the tested settings rather than the only viable mechanism. Under explicit contraction assumptions we provide state-stabil

## Key Contributions

1. **Novel Architecture**: Introduces innovative neural architecture combining Sharpness Aware Surrogate Snn Training concepts
2. **Efficiency Improvements**: Focuses on energy-efficient and biologically-plausible computation
3. **Practical Applications**: Applicable to vision and language modeling tasks

## Methodology

### Core Components

- Trainable parameters for membrane potential dynamics
- Adaptive firing mechanisms
- Integer training and spike inference paradigm
- Efficient SNN training workflows

### Implementation Guidelines

1. **Design spiking neurons** with adaptive capabilities
2. **Configure membrane potential** dynamics for your use case
3. **Implement integer training** for efficiency
4. **Optimize spike inference** for deployment

## Activation Keywords

- sharpness aware surrogate snn training
- sharpness
- spiking neural network
- SNN
- neuromorphic computing
- energy-efficient neural network

## Tools Used

- **Python**: For implementation
- **PyTorch/SpikingJelly**: For SNN frameworks
- **NumPy**: For numerical computations

## Related Papers

- arXiv:2604.09696 - Original paper
- Related SNN research in cs.NE category

## References

1. https://arxiv.org/abs/2604.09696
2. Spiking Neural Networks: A survey
3. Neuromorphic computing architectures

_Last updated: 2026-04-16_
