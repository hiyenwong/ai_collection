---
name: snn-quantization-emd-beyond-accuracy
description: "Earth Mover's Distance (EMD) framework for evaluating Spiking Neural Network quantization that captures spike timing distributions, not just classification accuracy. Activation: SNN deployment optimization, Neuromorphic hardware."
---

# SNN Quantization Beyond Accuracy: Earth Mover's Distance Approach

> Earth Mover's Distance (EMD) framework for evaluating Spiking Neural Network quantization that captures spike timing distributions, not just classification accuracy.

## Metadata
- **Source**: arXiv:2604.14487v1
- **Authors**: Evan Gibson Smith, Jacob Whitehill, Fatemeh Ganji
- **Published**: 2026-04-15
- **Categories**: cs.LG

## Core Methodology

### Key Innovation
### Core Method
EMD-based evaluation of SNN quantization:

1. **Spike Distribution Matching**: EMD measures distance between full and quantized spike timing distributions
2. **Temporal Dynamics**: Captures timing information lost in accuracy-only metrics
3. **Network-Wide Analysis**: Applies to individual neurons, layers, or entire networks
4. **Hardware-Aware**: Correlates with actual hardware deployment metrics

### Technical Framework
- **Spike Times**: Extract spike times from SNN simulations
- **EMD Computation**: Solve optimal transport between spike distributions
- **Quantization**: Test multiple precision levels (8-bit, 4-bit, 2-bit)
- **Correlation Analysis**: Compare EMD to hardware metrics (energy, latency)

## Implementation Guide

### Prerequisites
### Prerequisites
- SpikingJelly, snnTorch, or Norse
- POT (Python Optimal Transport) library
- GPU for SNN training
- Neuromorphic hardware simulator or device

### Step-by-Step
1. **Train SNN**: Train full-precision reference model
2. **Quantize**: Apply post-training quantization at various bit-widths
3. **Extract Spikes**: Record spike times for test stimuli
4. **Compute EMD**: Calculate Wasserstein distance between distributions
5. **Compare Metrics**: Correlate EMD with accuracy and hardware metrics
6. **Select Precision**: Choose quantization level balancing EMD and efficiency

### Applications
- SNN deployment optimization
- Neuromorphic hardware
- Edge AI
- Low-power inference

## Pitfalls
- EMD computation can be expensive for large networks
- Requires spike-level access
- Threshold dependent

## Related Skills
- neuroscience-research-method
- brain-connectivity-analysis
- spiking-neural-networks

## References
- arXiv: https://arxiv.org/abs/2604.14487v1
