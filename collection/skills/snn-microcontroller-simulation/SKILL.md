---
name: snn-microcontroller-simulation
description: "Full-feature SNN simulation (CARLsim) on MCU RP2350 with 8MB memory using IEEE 16-bit floats. Real-time SNN at 20mW, 5x more energy efficient than ARM processors. Activation: SNN, microcontroller, neuromorphic, CARLsim, edge computing, low-power."
---

# Full Feature Spiking Neural Network Simulation on Micro-Controllers for Neuromorphic Applications

> arXiv:2604.16474 — L. Niedermeier, J. L. Krichmar

## Metadata
- **Source**: arXiv:2604.16474
- **Authors**: L. Niedermeier, J. L. Krichmar
- **Published**: 2025-04
- **Relevance**: high
- **URL**: https://arxiv.org/abs/2604.16474

## Core Methodology

### Key Innovation
Microcontroller units (MCU), which have an order of magnitude lower Size, Weight and Power (SWaP) than standard computers, makes them suitable for applications at the edge. Neuromorphic computing, which can realize low SWaP, relies on Spiking Neural Networks (SNNs). Until now, software based simulations of SNNs required GPU-based workstations, application classified core processors such as the ARM Cortex-A53, or specialized hardware like Intel's Loihi. In the present work, we demonstrate that th

### Technical Framework
e SNN simulator CARLsim can run its full feature set on a MCU RP2350 with 8 MB memory. We accomplished this by utilizing IEEE 16-bit float point numbers, which reduced memory requirements without loss of function. We were able to run the Synfire4 benchmark which comprises 1200 neurons. The accuracy was 97.5% compared to the standard single precision numbers. Furthermore, we show that CARLsim runs a Synfire4 benchmark scaled-down to 186 neurons on a MCU in real-time at only 20 mW. Compared to the smallest application class ARM processor used by Raspberry in their Pi Zero 2 W, our MCU implementation is five times more energy efficient for the SNN itself, and an order of magnitude better when compared to the complete SoC (MCU/CPU + Board).

## Implementation Guide

### Prerequisites
- Python environment with scientific computing libraries
- Access to paper's supplementary materials at https://arxiv.org/abs/2604.16474

### Step-by-Step
1. Read the full paper at https://arxiv.org/abs/2604.16474
2. Identify the core algorithm/framework from the methodology section
3. Implement the key components as described in the paper
4. Validate using the paper's reported benchmarks

## Applications
- Neuroscience research
- Computational neuroscience
- Neural network design and optimization

## Pitfalls
- Results may be preliminary (preprint)
- Reproducibility depends on availability of code/data

## Related Skills
- computational-neuroscience-models
- neural-population-dynamics
- spiking-neural-network-training
