---
name: geodynamics-geometric-state-space
version: v1.0.0
last_updated: 2026-04-19
description: Geometric State-Space Neural Network for brain dynamics modeling. Combines state-space models with geometric constraints on brain connectivity to capture latent neural state evolution. Applicable to fMRI/EEG dynamics modeling, functional neuroimaging analysis, and brain network temporal dynamics. Trigger: state-space models brain dynamics, geometric neural networks, fMRI dynamics, latent neural states, brain connectivity geometry
---

# GeoDynamics: Geometric State-Space Neural Network for Brain Dynamics

## Description

A geometric state-space neural network framework that combines the dynamical structure of state-space models (SSMs) with geometric constraints derived from brain connectivity to model how latent neural states evolve over time and give rise to observed functional neuroimaging signals.

Based on: "GeoDynamics: A Geometric State-Space Neural Network for Brain Dynamics" (arXiv:2601.13570, January 2026)

## Problem

- Standard SSMs treat brain connectivity as flat/uncoupled from geometry
- Brain networks have inherent geometric structure (cortical surfaces, white matter tracts)
- Ignoring geometric constraints limits model expressivity and biological plausibility
- Need to jointly model latent dynamics and their geometric embedding

## Framework Architecture

```
Input: fMRI/EEG time series [T x N regions]
    ↓
Geometric Encoding:
    - Manifold structure from cortical geometry
    - Graph Laplacian from structural connectivity
    ↓
State-Space Model:
    - Latent state evolution: z_{t+1} = f(z_t) + ε
    - Geometric constraints on transition operator
    ↓
Observation Model:
    - Mapping from latent space to observed signals
    - Geometric-aware readout
```

## Key Components

### 1. Geometric Encoding

Incorporate brain geometry into the model using cortical surface and structural connectivity features.

### 2. Geometrically-Constrained SSM

The transition operator respects brain geometry through graph Laplacian regularization on the latent state dynamics.

### 3. Geometry Constraint

Enforce geometric constraints via graph Laplacian - smooth transitions along brain connectivity structure.

## Training Procedure

1. Initialize latent states from input time series
2. Forward pass through geometric SSM
3. Compute reconstruction loss (MSE between predicted and observed signals)
4. Apply geometric regularization loss
5. Backpropagate and update parameters

## Advantages Over Standard SSMs

1. **Geometric awareness**: Respects brain connectivity structure
2. **Biological plausibility**: Dynamics constrained by anatomy
3. **Better interpretability**: Latent states map to geometric features
4. **Improved generalization**: Geometric constraints prevent overfitting
5. **Cross-subject alignment**: Shared geometry enables transfer learning

## Applications

- **fMRI dynamics modeling**: Capture latent brain state transitions
- **EEG/MEG source analysis**: Geometrically-informed source localization
- **Brain-computer interfaces**: More robust neural state decoding
- **Neurological disease**: Detect deviations from healthy dynamics
- **Drug effect monitoring**: Track changes in latent state geometry

## Comparison with Existing Methods

| Method | Geometric Constraints | Latent Dynamics | Scalability |
|--------|----------------------|-----------------|-------------|
| Standard SSM | No | Yes | High |
| Graph Neural Network | Yes | Limited | Medium |
| **GeoDynamics** | **Yes** | **Yes** | **High** |
| Dynamic Causal Modeling | Yes | Yes | Low |
