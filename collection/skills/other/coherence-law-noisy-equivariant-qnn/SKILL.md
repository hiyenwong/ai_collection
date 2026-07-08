---
name: coherence-law-noisy-equivariant-qnn
description: Coherence law for trainability in noisy equivariant quantum neural networks. Proves that readout-visible sector coherence determines gradient survival under decoherence, not just symmetry structure.
category: ai_collection
tags:
  - quantum-neural-networks
  - equivariant-circuits
  - noisy-qml
  - trainability
  - coherence-law
  - barren-plateaus
trigger_words:
  - coherence law trainability QNN
  - equivariant quantum neural network noise
  - noisy QNN gradient decay
  - sector coherence trainability
  - light-cone reduction quantum
  - open-system quantum trainability
---

# Coherence Law for Trainability in Noisy Equivariant QNNs

## Background

Symmetry provides structure for quantum neural networks, but does not guarantee trainability once noise is present. The expressivity-trainability paradox shows that unstructured QML architectures suffer from quantum underfitting driven by barren plateaus. This skill provides a coherence law that determines whether gradients survive decoherence.

## Core Methodology

### 1. Light-Cone Reduction
- Causality fixes where the gradient can live — confined to the backward light cone of the readout
- Light-cone reduction pins the noiseless gradient to the sector-restricted cone
- Lower bound independent of total qubit number

### 2. Coherence Contraction Law
- Coherence determines how fast the gradient decays through contraction of off-diagonal sector modes
- Readout-visible aligned coherence rate defined as Rayleigh quotient of noise generator along gradient-carrying mode
- Perturbative open-system analysis converts this rate into a leading-order training law

### 3. Training Law
- Finite-noise degradation follows a single accumulated variable built from noise depth and coherence contraction
- Coefficient of determination R² = 0.979 between predicted and observed gradient degradation
- Sector coherence outperforms every standard channel diagnostic

### 4. Key Insight
- For correlated-dephasing channels with large worst-case rate but near-zero aligned rate:
  - The law predicts no gradient loss → none is observed
  - Sector coherence is the quantity linking equivariant architecture, open-system dynamics, and noisy trainability

## Implementation Guidelines

```python
# Pseudocode for coherence-aware QNN training
def coherence_aligned_rate(noise_generator, gradient_mode, readout_projector):
    """Calculate readout-visible aligned coherence rate as Rayleigh quotient"""
    # Project noise generator onto readout-visible subspace
    projected_noise = readout_projector @ noise_generator @ readout_projector
    # Rayleigh quotient along gradient-carrying mode
    rate = (gradient_mode.T @ projected_noise @ gradient_mode) / (gradient_mode.T @ gradient_mode)
    return rate

def predict_gradient_decay(coherence_rate, circuit_depth, noise_strength):
    """Leading-order training law for gradient degradation"""
    accumulated = coherence_rate * circuit_depth * noise_strength
    decay_factor = np.exp(-accumulated)
    return decay_factor
```

## Applications
- Noisy quantum neural network training
- Equivariant quantum circuit design
- Open-system quantum dynamics
- Quantum machine learning robustness
- Barren plateau mitigation strategies

## Pitfalls
- Symmetry alone does NOT guarantee trainability under noise — coherence is the deciding factor
- The aligned coherence rate can be near-zero even when worst-case channel rate is large
- Light-cone confinement means gradients only exist in specific sectors — design readout accordingly
- This law applies to U(1)-equivariant brickwork circuits — verify applicability for other symmetries

## References
- arXiv:2606.30688 — "A Coherence Law for Trainability in Noisy Equivariant Quantum Neural Networks"
- Ugail, Howard (2026)
