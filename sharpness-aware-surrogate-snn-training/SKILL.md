---
name: sharpness-aware-surrogate-snn-training
description: "Sharpness-Aware Surrogate Training (SAST) for on-sensor Spiking Neural Networks. Addresses surrogate-to-hard transfer gap in SNN deployment using sharpness-aware minimization. Activation: SAST, sharpness-aware training, surrogate gradient, on-sensor SNN."
---

# SAST: Sharpness-Aware Surrogate Training for On-Sensor SNNs

## Description
SAST solves the surrogate-to-hard transfer gap in SNN deployment using sharpness-aware minimization to find flat minima that transfer robustly.

Key innovations:
- Flat Minima: Sharpness-aware optimization
- Transfer Gap Solution: Directly addresses surrogate-to-hard mismatch
- On-Sensor Focus: Optimized for edge deployment
- No Performance Loss: Maintains accuracy

## Paper Reference
- Title: Sharpness-Aware Surrogate Training for On-Sensor Spiking Neural Networks
- Authors: Maximilian Nicholson
- arXiv: 2604.09696v1

## Core Methodology

### The Surrogate-to-Hard Gap
Training uses smooth surrogate (sigmoid), deployment uses hard threshold - causing performance degradation.

### Sharpness-Aware Minimization
SAM seeks parameters at flat loss landscape regions:
1. Compute adversarial perturbation: epsilon = rho * gradient / ||gradient||
2. Evaluate loss at perturbed point
3. Update using gradient at perturbed point with HARD spikes

## Activation Keywords
- SAST
- sharpness-aware training
- surrogate gradient
- on-sensor SNN
- SNN training
- flat minima
- transfer gap

## Applications
1. On-Sensor Vision (event cameras)
2. Near-Sensor Processing (wearables, IoT)
3. Neuromorphic Hardware (Loihi, TrueNorth, SpiNNaker)

## Technical Specifications

| Parameter | Default | Description |
|-----------|---------|-------------|
| rho | 0.05 | Perturbation radius |
| alpha | 1.0 | Surrogate slope |
| learning_rate | 1e-3 | Base learning rate |

Performance:
- Training Time: ~2x standard training
- Transfer Gap: Reduced by 50-80%

## Related Skills
- spiking-neural-network-training
- quantized-snn-hardware-optimization
- spikingjelly-framework

_Last updated: 2026-04-16_
