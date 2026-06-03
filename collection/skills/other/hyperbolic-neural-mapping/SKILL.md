---
name: hyperbolic-neural-mapping
description: HyNeuralMap framework for mapping visual semantics to neural hierarchies using hyperbolic Lorentz geometry. Provides cross-modal semantic alignment in negative-curvature space, outperforming Euclidean baselines for fMRI-visual representation learning. Use when working with: hyperbolic embeddings, vision-neural mapping, cross-subject fMRI alignment, hierarchical semantic organization, Lorentz model, geometric deep learning for neuroscience, or neural representation learning with non-Euclidean geometry. Trigger words: HyNeuralMap, hyperbolic neural, Lorentz embedding, cross-modal alignment, hierarchical neural representation.
---

# HyNeuralMap: Hyperbolic Mapping of Visual Semantics to Neural Hierarchies

Based on arXiv:2605.09392

## Core Idea

Map visual stimuli and neural responses (fMRI) into **shared hyperbolic space** (Lorentz model) rather than Euclidean space. Hyperbolic geometry's negative curvature naturally encodes hierarchical structure and preserves fine-grained semantic relationships across modalities.

## Why Hyperbolic > Euclidean

| Property | Euclidean | Hyperbolic |
|----------|-----------|------------|
| Hierarchical encoding | Poor (linear growth) | Excellent (exponential growth) |
| Semantic proximity | Distorts at scale | Preserves via geodesics |
| Cross-subject similarity | Flat, loses structure | Captures nested hierarchy |

## Key Components

### 1. Lorentz Model

The Lorentz model of hyperbolic space uses the hyperboloid:

```
H^n = {x ∈ R^(n+1) | ⟨x, x⟩_L = -1, x_0 > 0}
```

where ⟨x, y⟩_L = -x_0·y_0 + Σ_i x_i·y_i is the Lorentzian inner product.

### 2. Hyperbolic Geometric Alignment

- **Visual embeddings**: Encode image semantics into hyperbolic space
- **Neural embeddings**: Encode fMRI response patterns into the same space
- **Joint optimization**: Geodesic distances in hyperbolic space preserve both semantic proximity AND hierarchical relationships
- **Cross-subject generalization**: Shared hyperbolic manifold enables alignment across subjects

### 3. Training Pipeline

```
Visual Features → Hyperbolic Embedding ← fMRI Features
                        ↓
              Geodesic Distance Loss
                        ↓
              Semantic Proximity Loss
                        ↓
              Joint Optimization
```

## Implementation Guide

### Hyperbolic Operations (Lorentz Model)

```python
import torch

def lorentz_inner(x, y):
    """Lorentzian inner product: -x0*y0 + sum(xi*yi)"""
    return -x[..., 0] * y[..., 0] + torch.sum(x[..., 1:] * y[..., 1:], dim=-1)

def lorentz_dist(x, y):
    """Geodesic distance in Lorentz model"""
    inner = lorentz_inner(x, y)
    return torch.acosh(torch.clamp(-inner, min=1.0 + 1e-7))

def exp_map_o(v, c=1.0):
    """Exponential map from origin to hyperboloid"""
    v_norm = torch.sqrt(torch.clamp(lorentz_inner(v, v), min=1e-7))
    return torch.stack([
        torch.cosh(c * v_norm),
        (torch.sinh(c * v_norm) / v_norm) * v[..., 1:]
    ], dim=-1)

def log_map_o(x, c=1.0):
    """Logarithmic map from hyperboloid to tangent space at origin"""
    x0 = x[..., 0]
    return torch.acosh(x0) / torch.sqrt(torch.clamp(x0**2 - 1, min=1e-7)) * x[..., 1:]
```

### Alignment Loss

```python
def hyperbolic_alignment_loss(vis_emb, neural_emb, semantic_labels):
    """Joint loss: geodesic proximity + semantic consistency"""
    geo_dist = lorentz_dist(vis_emb, neural_emb)
    
    # Semantic proximity: similar labels → closer in hyperbolic space
    same_label = (semantic_labels.unsqueeze(1) == semantic_labels.unsqueeze(0)).float()
    semantic_loss = torch.mean(same_label * geo_dist + (1 - same_label) * torch.relu(margin - geo_dist))
    
    # Regularization: stay on hyperboloid
    manifold_loss = torch.mean((lorentz_inner(vis_emb, vis_emb) + 1)**2)
    
    return semantic_loss + lambda_reg * manifold_loss
```

## Activation

- **When to use**: Cross-modal neural-visual alignment, hierarchical semantic mapping, fMRI encoding models with geometric deep learning
- **When NOT to use**: Simple linear encoding models, non-hierarchical data, when Euclidean distance suffices
- **Keywords**: HyNeuralMap, hyperbolic neural mapping, Lorentz embedding, cross-modal alignment, hierarchical neural representation, geometric deep learning, fMRI encoding, visual semantics

## arXiv Reference

- Paper: "HyNeuralMap: Hyperbolic Mapping of Visual Semantics to Neural Hierarchies"
- ID: 2605.09392
- URL: https://arxiv.org/abs/2605.09392
