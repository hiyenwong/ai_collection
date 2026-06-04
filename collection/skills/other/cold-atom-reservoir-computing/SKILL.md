---
name: cold-atom-reservoir-computing
description: >
  Hybrid quantum-classical machine learning using neutral-atom (cold-atom) reservoir computing
  for classification tasks, especially medical imaging. Covers the pipeline of guided auto-encoder
  dimensionality reduction, surrogate-driven training, and cold-atom reservoir state evolution.
  Use when: (1) implementing reservoir computing with quantum/neutral-atom systems,
  (2) building hybrid quantum-classical ML pipelines, (3) medical image classification with
  reservoir computing, (4) surrogate-gradient training for non-differentiable systems,
  (5) autoencoder-guided dimensionality reduction for reservoir inputs.
  Activation: cold atom reservoir, neutral atom reservoir computing, hybrid quantum-classical ML,
  medical imaging reservoir, surrogate-driven training, polyp detection quantum,
  autoencoder reservoir computing, 冷原子储备计算.
---

# Cold-Atom Reservoir Computing

Hybrid quantum-classical pipeline using **neutral-atom reservoir computing** for classification,
with application to medical image classification (polyp detection).

## Key Insight

Neutral-atom quantum systems naturally implement rich, high-dimensional dynamical systems ideal
for reservoir computing. By coupling a classical autoencoder for input encoding with a physical
cold-atom reservoir and surrogate-driven readout training, this approach achieves competitive
classification with significantly fewer trainable parameters than full neural networks.

## Pipeline Architecture

### Stage 1: Guided Auto-Encoder (Dimensionality Reduction)

- Train a classical autoencoder to compress high-dimensional inputs (e.g., medical images)
- Use the encoder to project inputs into a lower-dimensional latent space
- The latent representation serves as the control signal for the reservoir

```
Input (image) → Encoder → Latent vector → Reservoir control parameters
```

### Stage 2: Cold-Atom Reservoir Dynamics

- The latent vector controls parameters of a neutral-atom quantum system
- The system evolves under its natural Hamiltonian dynamics
- Physical measurements at multiple time steps yield high-dimensional reservoir states
- Key properties: natural nonlinearity, high dimensionality, fading memory

```
Latent vector → Set control parameters → Evolve Hamiltonian → Measure observables → Reservoir states
```

### Stage 3: Surrogate-Driven Readout Training

- The reservoir-to-output mapping is linear: `output = W_readout · reservoir_states`
- Since the physical reservoir is non-differentiable, use surrogate gradients
- Train only the readout weights W_readout (reservoir itself is fixed)
- Loss: cross-entropy for classification, MSE for regression

```
Reservoir states → Linear readout → Surrogate gradient descent → Classification output
```

## Key Advantages

1. **Parameter efficiency**: Only train readout layer, not the reservoir
2. **Natural nonlinearity**: Quantum dynamics provide rich nonlinear transformations
3. **Energy efficiency**: Physical system computes for free during evolution
4. **Few-shot learning**: Reservoir computing excels with limited training data

## Implementation Considerations

- **Reservoir hyperparameters**: atom number, interaction strength, evolution time
- **Input encoding**: How to map latent vectors to physical control parameters
- **Readout design**: Linear regression vs. regularized (ridge regression)
- **Surrogate gradient choice**: Straight-through estimator, sigmoid approximation

## Related Approaches

- See `quantum-reservoir-computing` for general QRC patterns
- See `organic-quantum-reservoir-computing` for magnetic-field-free variants
- See `parametric-oscillator-reservoir-computing` for classical oscillator reservoirs
