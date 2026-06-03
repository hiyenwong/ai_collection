---
name: spatiotemporal-tdann
description: Spatiotemporal Topographic Deep Artificial Neural Network for modeling dorsal stream visual cortex. Uses 3D ResNet with MoCo self-supervised learning on naturalistic videos plus spatial loss to generate brain-like direction maps and pinwheel structures. Use when: modeling MT area, direction selectivity, dorsal stream organization, cortical self-organization, TDANN research.
---

# Spatiotemporal TDANN

Framework for modeling spatial and functional organization of dorsal stream visual cortex.

## Architecture

### Model Components

1. **3D ResNet backbone**: Processes naturalistic video sequences
2. **Momentum Contrast (MoCo)**: Self-supervised learning paradigm
3. **Spatial regularization loss**: Biologically inspired topographic constraint
4. **Temporal contrastive objective**: Learns motion selectivity

### Training Pipeline

```python
# 1. Load naturalistic videos
videos = load_naturalistic_videos(dataset)

# 2. Apply MoCo self-supervised learning
encoder = ResNet3D()
moco_learner = MoCoTrainer(encoder, queue_size=65536, temperature=0.07)

# 3. Add spatial regularization
spatial_loss = TopographicLoss(neighbor_weight=0.1, distance_metric='euclidean')

# 4. Combined objective
total_loss = contrastive_loss + spatial_loss_weight * spatial_loss

# 5. Train end-to-end
train(moco_learner, spatial_loss, videos, epochs=100)
```

## Key Findings

### MT Topography Emergence

- Spontaneous emergence of direction-selective maps
- Topological pinwheel structures form naturally
- Strong direction selectivity with residual axial component
- Trade-off between task discrimination and spatial regularization

### Quantitative Matching to Biology

- Direction Selectivity Index (DSI) matches macaque MT
- Circular variance consistent with in vivo recordings
- Pinwheel density matches physiological baselines
- Unifies ventral and dorsal stream computational origins

## Optimization Trade-off

The model reveals MT tuning properties arise from:

1. **Task-driven discriminative pressure**: Forces selectivity for motion direction
2. **Spatial regularization**: Encourages smooth topographic organization
3. **Strict optimization balance**: Neither extreme produces biological maps

## Implementation Details

### Spatial Loss Function

```python
class TopographicLoss:
    def __init__(self, neighbor_weight, distance_metric):
        self.neighbor_weight = neighbor_weight
        self.distance_metric = distance_metric
    
    def __call__(self, representations):
        # Compute pairwise distances in representation space
        rep_distances = pairwise_distance(representations)
        
        # Penalize differences between spatial neighbors
        spatial_distances = compute_spatial_distances(grid_positions)
        
        loss = sum(spatial_distances * rep_distances)
        return loss
```

### MoCo Training Configuration

- Queue size: 65536
- Temperature: 0.07
- Momentum: 0.999
- Learning rate: 0.03 (cosine decay)

## Applications

- Modeling dorsal stream organization
- Studying cortical self-organization principles
- Understanding motion processing in MT/V5
- Unifying ventral/dorsal stream computational theories

## Related Skills

- `spatiotemporal-tdann-mt-direction-maps`
- `kuramoto-phase-encoding`
- `brain-inspired-snn-pattern-analysis`
