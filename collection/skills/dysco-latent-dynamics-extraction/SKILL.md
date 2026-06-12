---
name: dysco-latent-dynamics-extraction
description: DYSCO (Dynamic System Contrastive Learning) - Multi-view contrastive learning for recovering latent trajectories and governing dynamics from noisy high-dimensional observations. Supports symbolic equation discovery within affine gauge. Applicable to neural recordings with Poisson noise.
version: 1.0
authors: ["Paolo Muratore", "Mackenzie Weygandt Mathis"]
arxiv_id: "2606.13260"
date: 2026-06-11
tags: [contrastive-learning, latent-dynamics, system-identification, neural-recordings, governing-equations, symbolic-discovery, multi-view-learning]
activation_keywords: ["latent dynamics", "governing equations", "contrastive learning", "system identification", "neural recordings", "DYSCO", "dynamical systems discovery"]
---

# DYSCO: Extracting Governing Equations from Latent Dynamics via Multi-View Contrastive Learning

## Methodology Overview

DYSCO is a multi-view temporal contrastive learning algorithm that jointly recovers:
1. **Latent trajectories** from noisy, high-dimensional observations
2. **Governing dynamics** by leveraging multiple independent noisy views

**Core Innovation**: Disentangles signal from noise using multi-view structure, enabling symbolic recovery of governing equations within an affine gauge.

## Mathematical Framework

### Problem Formulation
- **Observations**: High-dimensional noisy measurements $y_t$ of latent state $x_t$
- **Noise models**: Gaussian and Poisson (especially relevant for neural recordings)
- **Views**: Multiple independent noisy observations $y_t^{(v)}$ of same underlying process

### Contrastive Learning Strategy
- **Temporal contrastive loss**: Aligns latent trajectories across time
- **Multi-view consistency**: Enforces agreement between different views
- **Dynamics parameterization**: Structured functional basis for symbolic recovery

### Theoretical Guarantees
- **Strong identification** up to affine indeterminacy
- Extends prior identifiability results to realistic noisy nonlinear observations
- Affine gauge freedom allows symbolic equation extraction

## Implementation Steps

### Step 1: Multi-View Data Collection
```python
# Collect multiple independent views of same process
views = []
for v in num_views:
    observations = collect_noisy_measurements(process)
    views.append(observations)
```

### Step 2: Latent Trajectory Recovery
```python
# Contrastive learning encoder
encoder = MultiViewEncoder(dim_latent)
trajectories = encoder(views)

# Temporal contrastive objective
loss_temporal = temporal_contrastive_loss(trajectories)
loss_multiview = multiview_consistency_loss(trajectories)
```

### Step 3: Dynamics Parameterization
```python
# Parameterize dynamics in functional basis
dynamics_model = StructuredDynamics(
    basis_functions=["linear", "quadratic", "sin", "cos"],
    regularization=True
)
flow_field = dynamics_model(trajectories)
```

### Step 4: Symbolic Equation Extraction
```python
# Recover governing equations within affine gauge
equations = symbolic_extraction(flow_field, basis_functions)
# Result: dx/dt = f(x) where f is recovered symbolically
```

## Key Applications

### 1. Neural Recording Analysis
- **Poisson noise modeling**: Natural for spike count observations
- **Latent neural dynamics**: Recovering underlying brain state trajectories
- **Governing equations**: Discovering neural population dynamics rules

### 2. Dynamical System Discovery
- **Chaotic systems**: Lorenz, Rössler attractors
- **Oscillatory regimes**: Periodic, quasi-periodic dynamics
- **Metastable states**: Switching dynamics with multiple attractors

### 3. Scientific Discovery
- **Symbolic regression**: Automated equation discovery
- **Physical law extraction**: From experimental data
- **Biological process modeling**: Cell dynamics, population models

## Performance Characteristics

### Empirical Results (arXiv:2606.13260)
- **Accurate recovery**: Both latent trajectories and flow fields
- **Diverse regimes**: Chaotic, oscillatory, metastable
- **Noise robustness**: Gaussian and Poisson observation noise
- **Neural recordings**: Particularly effective for spike data

### Comparison to Prior Methods
- **vs. PCA/ICA**: Captures dynamics, not just static structure
- **vs. Neural ODE**: Multi-view disentangles noise
- **vs. Koopman**: Symbolic recovery enabled by functional basis

## Technical Details

### Functional Basis Design
```python
# Typical basis functions for dynamics
basis = {
    "monomials": [lambda x: x, lambda x: x**2, ...],
    "trigonometric": [sin, cos],
    "polynomial": up to degree k
}
```

### Contrastive Architecture
- **Encoder network**: Maps observations to latent space
- **Projector head**: Temporal alignment features
- **Dynamics predictor**: Next-step prediction

### Training Objective
```
L = L_temporal + λ * L_multiview + μ * L_dynamics
where:
- L_temporal: InfoNCE-style temporal contrastive
- L_multiview: Cross-view consistency
- L_dynamics: Flow field regularization
```

## Pitfalls and Limitations

### Common Issues
1. **View independence**: Views must be conditionally independent given latent
2. **Observation noise**: Very high noise can overwhelm signal
3. **Basis selection**: Wrong functional basis limits symbolic recovery
4. **Dimension estimation**: Latent dimension must be estimated or known

### Mitigation Strategies
1. **View design**: Physically separated sensors, different measurement modalities
2. **Noise modeling**: Choose appropriate noise model (Gaussian vs Poisson)
3. **Basis library**: Use diverse basis functions, regularization
4. **Cross-validation**: Estimate dimension via reconstruction error

## Related Methods

### Predecessor Methods
- **Time-delay embedding**: Takens' theorem for attractor reconstruction
- **Slow feature analysis**: Extract slow-varying latent signals
- **Variational autoencoders**: Generative latent variable models

### Contemporary Methods
- **Neural ODE**: Continuous-time dynamics models
- **Koopman operators**: Linear dynamics in lifted space
- **Deep state-space models**: Learnable latent dynamics

## References

- **arXiv**: 2606.13260 - Full paper with theoretical guarantees
- **Code repository**: https://github.com/muratorelab/dysco (expected)
- **Related**: Mackenzie Mathis - EEVEE, Keypoint-MoCap work

## Summary

DYSCO provides a principled framework for discovering governing equations from noisy observations by:
1. Leveraging multi-view structure to disentangle signal/noise
2. Using contrastive learning for robust latent recovery
3. Parameterizing dynamics in functional bases for symbolic extraction
4. Providing theoretical guarantees under realistic noise assumptions

**Key insight**: Multiple independent views of same process enable noise disentanglement without explicit noise modeling, making it particularly suited for neural recordings where Poisson noise dominates.