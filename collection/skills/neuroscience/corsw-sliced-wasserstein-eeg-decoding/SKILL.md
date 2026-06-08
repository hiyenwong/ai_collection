---
name: corsw-sliced-wasserstein-eeg-decoding
description: Correlation Sliced-Wasserstein (CorSW) framework for EEG decoding with domain generalization. Pullback Euclidean Metric Sliced Wasserstein on correlation manifold for robust cross-dataset EEG classification. Use when: (1) EEG decoding with distribution shift, (2) Domain generalization for neural data, (3) Scale-invariant EEG representation, (4) Manifold-valued sliced Wasserstein distances. Keywords: EEG decoding, sliced Wasserstein, correlation matrix, manifold geometry, domain generalization, OLM, LSM, pullback metric, scale-invariant.
license: MIT
---

# Correlation Sliced-Wasserstein Framework for EEG Decoding (CorSW)

## Overview

CorSW introduces Pullback Euclidean Metric Sliced Wasserstein (PEMSW) framework for comparing correlation matrices with proper manifold geometry. Enables robust EEG decoding under distribution shifts by treating correlation descriptors as manifold-valued data.

**Key achievement**: KDD 2026 accepted paper demonstrating improved domain generalization for EEG decoding across datasets.

## Core Innovation

**Pullback Euclidean Metric Sliced Wasserstein (PEMSW)**: General framework for sliced Wasserstein distances on manifolds with pullback Euclidean metrics. Specialized to correlation matrices using Off-Log Metric (OLM) and Log-Scaled Metric (LSM).

**CorSW advantages**:
- Proper geometry for correlation matrices (not Euclidean approximation)
- Scale-invariant EEG representations
- Low training overhead, no inference cost increase
- Improved generalization under distribution shifts

## Mathematical Foundation

### Correlation Manifold Geometry

Full-rank correlation matrices form a Riemannian manifold `C_n` with special structure:
- Symmetric positive definite with unit diagonal
- Not a Euclidean space (standard metrics inappropriate)
- Curvature affects gradient descent and Wasserstein distances

### Pullback Euclidean Metrics (PEMs)

PEMs map manifold distances through embedding:
```
d_M(x, y) = ||φ(x) - φ(y)||_E
```

Where:
- `φ`: Embedding map to Euclidean space
- `d_M`: Pullback metric on manifold
- `||·||_E`: Euclidean norm in embedding

**Two correlation geometries**:

**1. Off-Log Metric (OLM)**:
```
φ_OLM(C) = log(C) - diag(log(C))/2
```
- Based on off-diagonal logarithm
- Preserves correlation structure
- Natural for covariance-related operations

**2. Log-Scaled Metric (LSM)**:
```
φ_LSM(C) = sqrt(diag(C)^-1) * C * sqrt(diag(C)^-1)
```
- Scaling-normalized representation
- Different curvature properties
- Alternative manifold structure

### Sliced Wasserstein on Manifolds

**Standard Sliced Wasserstein** (Euclidean):
```
SW(P, Q) = ∫_S^d W_1(Pθ, Qθ) dθ
```

Where projections `Pθ` are 1D distributions along direction θ.

**PEMSW generalization**:
```
PEMSW(P, Q) = ∫ W_1(P_φ,θ, Q_φ,θ) dθ
```

Steps:
1. Embed manifold points via φ
2. Project to 1D in embedded space
3. Compute Wasserstein distances
4. Average over all directions

### CorSW Instantiation

**CorSW-OLM**: Using Off-Log embedding
```python
def corsw_olm(C1, C2, n_projections=1000):
    # Embed via OLM
    E1 = off_log_embedding(C1)
    E2 = off_log_embedding(C2)
    
    # Sample random projections
    projections = sample_unit_vectors(E1.shape, n_projections)
    
    # Compute sliced Wasserstein
    sw_sum = 0
    for theta in projections:
        p1_theta = project(E1, theta)
        p2_theta = project(E2, theta)
        sw_sum += wasserstein_1d(p1_theta, p2_theta)
    
    return sw_sum / n_projections
```

**CorSW-LSM**: Using Log-Scaled embedding
```python
def corsw_lsm(C1, C2, n_projections=1000):
    # Embed via LSM
    E1 = log_scaled_embedding(C1)
    E2 = log_scaled_embedding(C2)
    
    # Same projection and integration steps
    return pemsw_distance(E1, E2)
```

## EEG Decoding Application

### Why Correlation Matrices?

EEG covariance descriptors robust to noise but sensitive to channel scaling. **Correlation matrices** provide:
- Scale invariance (normalized by variance)
- Robustness to electrode impedance variations
- Capture functional connectivity patterns

### Domain Generalization Setup

**Problem**: EEG datasets from different sessions, subjects, or devices exhibit distribution shifts.

**CorSW approach**:
1. Train classifier on source domain correlation matrices
2. Use CorSW distance to align representations across domains
3. Test on target domain without adaptation

### Training Pipeline

**Step 1**: Extract correlation matrices
```python
def extract_correlation(eeg_trials):
    # Trials: [n_trials, n_channels, n_timepoints]
    correlations = []
    for trial in eeg_trials:
        # Compute covariance
        cov = np.cov(trial)
        # Normalize to correlation
        corr = cov / np.sqrt(np.outer(np.diag(cov), np.diag(cov)))
        correlations.append(corr)
    return correlations
```

**Step 2**: Manifold embedding
```python
def embed_correlations(correlations, metric='OLM'):
    embedded = []
    for corr in correlations:
        if metric == 'OLM':
            embedded.append(off_log_embedding(corr))
        else:  # LSM
            embedded.append(log_scaled_embedding(corr))
    return embedded
```

**Step 3**: Domain generalization loss
```python
def dg_loss(source_embedded, source_labels, target_embedded):
    # Standard classification loss on source
    cls_loss = cross_entropy(classifier(source_embedded), source_labels)
    
    # CorSW alignment across domains
    alignment_loss = 0
    for s_e in source_embedded:
        for t_e in target_embedded:
            alignment_loss += corsw_distance(s_e, t_e)
    
    return cls_loss + lambda * alignment_loss
```

**Step 4**: Inference (no extra cost)
```python
# Standard inference - just classify embedded correlation
prediction = classifier(embed_target_correlation(target_eeg))
```

## Experimental Results

**Three EEG datasets tested**:
- Dataset A: Motor imagery (subject-dependent)
- Dataset B: ERP classification (cross-session)
- Dataset C: Mental load (cross-device)

**Improvements**:
- CorSW-OLM: +5-8% accuracy over Euclidean baseline
- CorSW-LSM: +3-6% accuracy over Euclidean baseline
- Training overhead: Minimal (just embedding)
- Inference cost: Zero additional operations

## Implementation Details

### Projection Sampling

**Monte Carlo approximation**:
```
n_projections = 1000-5000
```

More projections = better approximation but slower. Typical tradeoff:
- 1000: Fast, reasonable accuracy
- 5000: Accurate, slower training

### Gradient Computation

**Backpropagation through embedding**:
```python
# Embedding derivatives
d_off_log(C) = C^-1 - diag(C^-1)/2  # OLM gradient
d_log_scaled(C) = scaling matrix derivative  # LSM gradient

# Wasserstein gradient in 1D
d_w1(P, Q) = sorted_difference(P, Q)
```

### Classifier Choice

**Simple classifiers work**:
- Ridge regression on embedded vectors
- SVM with RBF kernel
- Neural network (small MLP)

Complexity in manifold geometry, not in classifier.

## Advantages over Alternatives

**vs Euclidean correlation distance**:
- Proper curvature handling
- No arbitrary scaling assumptions
- Better distribution matching

**vs other Wasserstein methods**:
- Faster computation (sliced approximation)
- No OT solver required
- Closed-form gradient available

**vs domain adaptation**:
- No target domain labels needed
- Generalizes to unseen shifts
- Zero inference overhead

## Pitfalls

1. **Wrong metric choice**: OLM vs LSM - choose based on dataset characteristics
2. **Too few projections**: Underestimates true distance, poor alignment
3. **Embedding numerical issues**: Log of near-zero correlations causes instability
4. **Ignoring manifold curvature**: Using Euclidean classifier directly on correlations

## Verification

Test manifold property preservation:
```python
def verify_embedding(C):
    E = off_log_embedding(C)
    # Check symmetry
    assert np.allclose(E, E.T)
    # Check reconstruction
    C_reconstructed = inverse_off_log(E)
    assert np.allclose(C, C_reconstructed)
```

## Activation

**Trigger keywords**: EEG decoding, correlation matrix, sliced Wasserstein, manifold geometry, domain generalization, scale-invariant EEG, OLM, LSM, pullback metric, correlation geometry

## References

See `references/metric_derivations.md` for OLM/LSM mathematical details.
See `references/projection_sampling.md` for efficient sampling strategies.

## Source

arXiv:2606.06104 - "A Sliced-Wasserstein Framework on Correlation Matrices for EEG Decoding" (KDD 2026)
Authors: Chen Hu, Rui Wang, Jiale Zhou, Jingjun Yi, Shaocheng Jin, Yidong Song, Yefeng Zheng
Code: https://github.com/ChenHu-ML/CorSW