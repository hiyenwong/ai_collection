---
name: dysco-latent-dynamics-extraction
description: DYSCO (Dynamics via Contrastive Learning) - 多视角对比学习从噪声观测中提取潜在动力学系统。通过独立噪声视角分离信号与噪声，恢复潜在轨迹和支配动力学方程。
author: Paolo Muratore, Mackenzie Weygandt Mathis
arxiv_id: 2606.13260
categories: [machine-learning, dynamical-systems, neuroscience, system-identification]
tags: [contrastive-learning, latent-dynamics, system-identification, multi-view-learning, governing-equations, neural-dynamics, symbolic-discovery]
created: 2026-06-15
source: arXiv cs.LG/q-bio.NC
---

# DYSCO: Extracting Governing Equations from Latent Dynamics

## Overview

DYSCO (DYnamics via Contrastive Learning) is a **multi-view temporal contrastive learning algorithm** that jointly recovers latent trajectories and governing dynamics from noisy, high-dimensional measurements. It leverages multiple independent noisy views of the same underlying process to **disentangle signal from noise**.

## Key Innovation

### Multi-View Contrastive Framework
- Uses **independent noisy views** of same underlying process
- Separates signal from noise via contrastive learning
- Recovers **latent trajectories** AND **governing dynamics** simultaneously
- Symbolic recovery of governing equations in **affine gauge**

### Problem Setting
```
Input: Noisy, high-dimensional observations
Challenge:
  - Short recordings
  - Noisy measurements
  - Coarsely sampled
  - Autocorrelated structure (e.g., fMRI)

Output:
  - Latent trajectories (signal)
  - Governing equations (symbolic)
  - Flow fields (dynamics)
```

## Core Methodology

### 1. Multi-View Architecture
```
Views: Multiple independent noisy observations
       y₁(t) = g₁(x(t)) + noise₁
       y₂(t) = g₂(x(t)) + noise₂
       ...

Contrastive objective:
  - Align views of same latent state
  - Separate noise through independence
```

### 2. Temporal Contrastive Learning
- **Temporal pairs**: Same time point, different views
- **Contrastive loss**: Maximize agreement between views
- **Noise separation**: Independent noise → divergent representations

### 3. Functional Basis Parameterization
- Dynamics parameterized in structured functional basis
- Enables **symbolic recovery** of governing equations
- Affine gauge freedom allows interpretation

## Theoretical Guarantees

### Identifiability Results
- Strong identification up to **affine indeterminacy**
- Extends prior identifiability results to **noisy nonlinear observations**
- Guarantees for both Gaussian and Poisson noise

### Key Conditions
1. Multiple independent noisy views
2. Weak coupling assumptions
3. Structured functional basis

## Mathematical Framework

### Latent Dynamics Model
$$\dot{x} = f(x)$$
where:
- $x(t)$: latent state trajectory
- $f(x)$: governing dynamics (to be recovered)

### Observation Model
$$y_i(t) = g_i(x(t)) + \epsilon_i(t)$$
where:
- $y_i$: noisy observation (view i)
- $g_i$: observation function
- $\epsilon_i$: independent noise

### Contrastive Objective
$$L = -\log \frac{e^{sim(z_i, z_j)}}{\sum_k e^{sim(z_i, z_k)}}$$
where:
- $z_i, z_j$: latent representations from different views
- $sim$: similarity metric

## Experimental Validation

### Dynamical Regimes Tested
1. **Chaotic systems** - Lorenz, Rössler
2. **Oscillatory dynamics** - Limit cycles
3. **Metastable systems** - Switching behavior

### Noise Types
- **Gaussian noise** - Standard observation noise
- **Poisson noise** - Particularly relevant for neural recordings

### Results
- Accurate recovery of latent trajectories
- Correct flow field estimation
- Symbolic equation discovery

## Applications

### Neuroscience
- Neural recording analysis (EEG, fMRI, electrophysiology)
- Brain dynamics identification
- Neural circuit modeling

### Physics
- Complex system dynamics
- Phase transition modeling
- Turbulence analysis

### Engineering
- System identification from noisy sensors
- Control system design
- Predictive maintenance

## Implementation Details

### Multi-View Generation
For neural recordings:
- Split trials or time segments
- Different recording modalities
- Subsampling strategies

### Functional Basis
Polynomial basis functions for symbolic discovery:
- Linear terms: $x, y, z$
- Quadratic terms: $x^2, xy, yz$
- Higher-order: as needed

### Contrastive Encoder
Architecture:
- Encoder network per view
- Shared dynamics model
- Temporal consistency constraint

## Advantages over Prior Methods

| Method | Noise Handling | Symbolic Recovery | Multiple Views |
|--------|---------------|-------------------|-----------------|
| Standard VAE | Limited | No | No |
| DMD | Linear only | No | No |
| SINDy | Sensitive | Yes | No |
| **DYSCO** | Robust | Yes | Yes |

## Technical Specifications

### Network Architecture
```
Encoder (per view):
  - Input: Noisy observation y_i(t)
  - Output: Latent representation z_i(t)

Dynamics Model:
  - Input: Latent state z(t)
  - Parameterization: Functional basis
  - Output: Flow field f(z)

Contrastive:
  - Temporal pairs across views
  - Maximizes cross-view agreement
```

### Training Procedure
1. Generate/acquire multi-view data
2. Train encoders with contrastive loss
3. Fit dynamics model in latent space
4. Extract symbolic equations from basis

## Limitations and Extensions

### Current Constraints
- Requires multiple independent views
- Affine gauge ambiguity remains
- Assumes known functional basis structure

### Future Extensions
- Automatic basis discovery
- Single-view adaptations
- Non-stationary dynamics
- Partial observations

## Comparison to Related Methods

### vs. Standard Contrastive Learning
- **Temporal focus**: Specifically designed for dynamics
- **Multi-view noise separation**: Novel contribution

### vs. SINDy
- **Noise robustness**: Handles Poisson noise
- **Multi-view fusion**: Combines information sources

### vs. Latent Variable Models
- **Dynamics recovery**: Not just representation
- **Symbolic interpretation**: Explainable equations

## Trigger Words

**Use this skill when:**
- Extracting governing equations from data
- Analyzing noisy neural recordings
- Identifying dynamical systems
- Multi-view data fusion for dynamics
- Brain dynamics modeling
- System identification under noise
- Discovering latent state equations
- Contrastive learning for dynamics

## Neural Science Applications

### fMRI Analysis
- Handle autocorrelated noise
- Extract brain dynamics
- Model state transitions

### Electrophysiology
- Poisson noise (spike counts)
- Multi-electrode array data
- Circuit dynamics discovery

### Behavioral Dynamics
- Movement trajectory analysis
- Decision-making models
- Learning dynamics

## References

- Muratore, P. & Mathis, M.W. (2026). arXiv:2606.13260
- SINDy methodology
- Contrastive learning foundations
- Multi-view learning theory