---
name: spatiotemporal-tdann-mt-direction-maps
description: Spatiotemporal TDANN framework for modeling the emergence of MT (middle temporal) area direction maps through self-supervised contrastive optimization. Unifies ventral and dorsal stream computational origins using Momentum Contrast (MoCo) with biological spatial regularization. Generates brain-like direction selectivity, pinwheel structures, and topological maps matching in vivo macaque physiology. Use when working with: cortical self-organization, visual cortex modeling, dorsal stream computational models, direction selectivity, TDANN, topographic neural networks, MoCo-based neuroscience models, or computational origins of cortical maps. Trigger words: spatiotemporal TDANN, MT direction maps, dorsal stream organization, direction selectivity, cortical self-organization, topographic deep learning.
---

# Spatiotemporal TDANN: MT Direction Maps from Contrastive Optimization

Based on arXiv:2605.11718

## Core Finding

MT (middle temporal) area direction-selective maps emerge from a **strict optimization trade-off** between:
1. **Task-driven discriminative pressure** (MoCo contrastive learning on naturalistic video)
2. **Spatial regularization** (biologically inspired spatial loss enforcing topographic continuity)

This unifies the computational origins of both ventral and dorsal streams under the same self-organization principles.

## Architecture

```
3D ResNet (spatiotemporal) 
    ↓
MoCo Self-Supervised Learning (naturalistic video)
    +
Biological Spatial Loss
    ↓
Emergent direction maps + pinwheel structures
```

## Key Components

### 1. MoCo for Spatiotemporal Learning

```python
# Momentum Contrast on video frames
# Query encoder updated by gradient; key encoder by EMA
key_encoder = momentum * key_encoder + (1 - momentum) * query_encoder
```

### 2. Spatial Regularization Loss

Enforces topographic continuity — nearby units in the model should have similar tuning:

```python
def spatial_loss(feature_maps, adjacency_matrix):
    """Encourage nearby units to have similar representations"""
    diff = feature_maps.unsqueeze(1) - feature_maps.unsqueeze(2)
    spatial_sim = torch.exp(-torch.norm(diff, dim=-1) / temperature)
    return -torch.mean(adjacency_matrix * spatial_sim)
```

### 3. Emergent Properties

The model spontaneously develops:
- **Direction-selective maps**: Organized topography of preferred directions
- **Pinwheel structures**: Topological singularities matching macaque MT
- **Strong direction selectivity + residual axial component**: Matches physiological data

## Validation Metrics

| Metric | Model | Macaque MT |
|--------|-------|------------|
| Direction Selectivity Index | Matched | Baseline |
| Circular Variance | Matched | Baseline |
| Pinwheel Density | Matched | Baseline |

## Why This Matters

- **Unifies ventral + dorsal**: Same computational principles govern both streams
- **Self-organization**: No hand-designed architecture for direction maps — they emerge
- **Trade-off insight**: Direction selectivity arises from tension between discrimination and spatial continuity

## Implementation Considerations

- Use **3D convolutions** for spatiotemporal processing
- **MoCo** provides the contrastive signal (more stable than SimCLR for video)
- Spatial loss weight is critical — too strong → no direction selectivity; too weak → no topography
- Naturalistic video (not synthetic) is essential for realistic emergence

## When to Use

- **Use when**: Modeling cortical self-organization, studying direction selectivity origins, building topographic neural networks, computational neuroscience of visual cortex
- **Don't use when**: Simple classification tasks, non-spatial architectures, when biological plausibility is not a concern
- **Keywords**: spatiotemporal TDANN, MT direction maps, dorsal stream, direction selectivity, cortical self-organization, MoCo neuroscience, topographic networks

## arXiv Reference

- Paper: "Self-organized MT Direction Maps Emerge from Spatiotemporal Contrastive Optimization"
- ID: 2605.11718
- URL: https://arxiv.org/abs/2605.11718
