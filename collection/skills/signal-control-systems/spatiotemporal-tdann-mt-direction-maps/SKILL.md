---
name: spatiotemporal-tdann-mt-direction-maps
description: Spatiotemporal TDANN framework for modeling the emergence of direction-selective maps in primate MT cortex via self-supervised contrastive optimization with spatial regularization. Unifies ventral and dorsal stream topographic self-organization. arXiv: 2605.11718 (May 2026).
---

# Spatiotemporal TDANN: Self-organized MT Direction Maps

This skill captures the methodology for modeling **direction-selective map emergence in primate Middle Temporal (MT) cortex** using a spatiotemporal Topographic Deep Artificial Neural Network (TDANN) trained with self-supervised contrastive learning and biologically-inspired spatial regularization.

**Paper**: Zhaotian Gu, Molan Li, Jie Su, Chang Liu, Tianyi Qian, Dahui Wang, "Self-organized MT Direction Maps Emerge from Spatiotemporal Contrastive Optimization", arXiv:2605.11718 (May 2026)

## Core Problem

The spatial and functional organization of the primate visual cortex is a fundamental problem in neuroscience. While TDANN has successfully modeled ventral stream organization (e.g., face patches, object-selective regions), the **dorsal stream's topographic organization** — specifically direction-selective maps in area MT — has remained unresolved.

Key questions:
- Do MT direction maps emerge from the same universal principles as ventral stream maps?
- What computational trade-offs shape MT tuning properties?
- Can a single framework unify both streams?

## Spatiotemporal TDANN Architecture

### Model Components

1. **3D ResNet Backbone**: Processes naturalistic video input (spatial + temporal dimensions)
2. **Momentum Contrast (MoCo)**: Self-supervised contrastive learning paradigm
3. **Biological Spatial Loss**: Enforces cortical-like topographic organization
4. **Direction Selectivity Readout**: Extracts motion tuning properties

### Architecture Design

```python
# Conceptual architecture
class SpatiotemporalTDANN:
    """3D ResNet with MoCo contrastive learning + spatial regularization."""
    
    def __init__(self, backbone="resnet3d-18", spatial_loss_weight=1.0):
        # 3D ResNet processes video clips (B, T, C, H, W)
        self.backbone = ResNet3D(backbone)
        
        # MoCo contrastive learning components
        self.encoder_q = self.backbone  # Query encoder
        self.encoder_k = copy(self.backbone)  # Key encoder (momentum updated)
        self.queue = FeatureQueue(size=65536, dim=feature_dim)
        
        # Spatial regularization loss
        self.spatial_loss_weight = spatial_loss_weight
    
    def forward(self, video_clips):
        # Extract spatiotemporal features
        features = self.encoder_q(video_clips)  # (B, T, H', W', D)
        
        # Apply spatial regularization
        if self.training:
            spatial_loss = self.compute_spatial_loss(features)
        
        return features, spatial_loss
```

### MoCo Contrastive Learning

```python
def moco_contrastive_loss(query_features, key_features, queue, temperature=0.07):
    """Momentum Contrast loss for self-supervised video representation learning."""
    # Positive pair: query and key from same video (different augmentations)
    pos_logits = torch.einsum('nc,nc->n', [query_features, key_features]) / temperature
    
    # Negative pairs: query vs. all features in queue
    neg_logits = torch.einsum('nc,ck->nk', [query_features, queue.features]) / temperature
    
    logits = torch.cat([pos_logits.unsqueeze(1), neg_logits], dim=1)
    labels = torch.zeros(logits.shape[0], dtype=torch.long)
    
    return cross_entropy(logits, labels)
```

### Biological Spatial Loss

The spatial loss enforces cortical-like organization:

```python
def spatial_regularization_loss(features, spatial_distance_matrix):
    """
    Encourages neurons with similar functional preferences to be spatially close,
    mimicking cortical topographic organization.
    
    features: (B, H', W', D) - feature maps from backbone
    spatial_distance_matrix: precomputed spatial distances between grid positions
    """
    # Compute functional similarity between all neuron pairs
    functional_similarity = cosine_similarity(features, features)
    
    # Penalize when functionally similar neurons are spatially far apart
    spatial_loss = torch.mean(
        functional_similarity * spatial_distance_matrix
    )
    
    return spatial_loss
```

## Key Findings

### 1. Spontaneous Emergence of MT-like Maps

Training the spatiotemporal TDANN on naturalistic videos leads to:
- **Direction-selective columns**: Neurons preferring similar motion directions cluster together
- **Pinwheel structures**: Topological singularities where direction preference rotates 360° around a point
- **Direction preference diversity**: Full coverage of motion directions across the map

### 2. MT Tuning Properties Match In Vivo Data

The model's neurons exhibit physiological properties matching macaque MT recordings:

| Property | Model | Macaque MT |
|----------|-------|------------|
| Direction Selectivity Index (DSI) | High | High |
| Circular Variance | Low | Low |
| Pinwheel Density | ~3.14/mm² | ~3.14/mm² |
| Residual Axial Component | Present | Present |

### 3. Optimization Trade-off Discovery

**Crucial insight**: MT tuning properties emerge from a strict trade-off between:
- **Task-driven discriminative pressure**: The contrastive loss pushes neurons to distinguish different motion patterns
- **Spatial regularization**: The biological loss encourages spatially organized topography

This trade-off explains why MT neurons show:
- Strong direction selectivity (from discriminative pressure)
- Residual axial component (spatial regularization constraint)

### 4. Unified Cortical Self-Organization

The same principles govern both:
- **Ventral stream**: Object category maps, face patches
- **Dorsal stream**: Direction-selective maps, motion columns

This establishes a **general mechanism for cortical self-organization** across the entire visual cortex.

## Implementation Patterns

### Training Pipeline

```python
def train_spatiotemporal_tdann(
    video_dataset,
    spatial_loss_weight=0.1,
    moco_temperature=0.07,
    queue_size=65536,
    num_epochs=100,
    lr=1e-4,
):
    model = SpatiotemporalTDANN(spatial_loss_weight=spatial_loss_weight)
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    queue = FeatureQueue(size=queue_size)
    
    for epoch in range(num_epochs):
        for video_clips in video_dataset:
            # Generate augmented views
            view_q = augment(video_clips, view="query")
            view_k = augment(video_clips, view="key")
            
            # Forward pass
            q_features, spatial_loss = model(view_q)
            with torch.no_grad():
                k_features = model.encoder_k(view_k)
            
            # Contrastive loss
            contrastive_loss = moco_contrastive_loss(
                q_features, k_features, queue, moco_temperature
            )
            
            # Combined loss
            total_loss = contrastive_loss + spatial_loss
            
            optimizer.zero_grad()
            total_loss.backward()
            optimizer.step()
            
            # Update momentum encoder
            momentum_update(model.encoder_k, model.encoder_q, m=0.999)
            queue.update(k_features)
```

### Analyzing Direction Selectivity

```python
def compute_direction_selectivity(neuron_responses, directions):
    """
    Compute direction selectivity index (DSI) and preferred direction.
    
    neuron_responses: (n_trials, n_neurons) - response to moving stimuli
    directions: (n_trials,) - stimulus direction in degrees
    """
    # Vector sum method
    cos_sum = torch.sum(neuron_responses * torch.cos(torch.deg2rad(directions)), dim=0)
    sin_sum = torch.sum(neuron_responses * torch.sin(torch.deg2rad(directions)), dim=0)
    
    # Preferred direction
    pref_direction = torch.atan2(sin_sum, cos_sum) * 180 / torch.pi
    
    # Direction Selectivity Index
    response_vector_length = torch.sqrt(cos_sum**2 + sin_sum**2)
    total_response = torch.sum(neuron_responses, dim=0)
    dsi = response_vector_length / (total_response + 1e-8)
    
    return pref_direction, dsi

def compute_circular_variance(neuron_responses, directions):
    """Compute circular variance - lower means more selective."""
    pref_dir, dsi = compute_direction_selectivity(neuron_responses, directions)
    return 1 - dsi  # Circular variance = 1 - DSI

def detect_pinwheels(direction_map):
    """
    Detect pinwheel singularities in direction preference map.
    
    direction_map: (H, W) - preferred direction at each spatial location
    """
    # Compute phase winding around each 2x2 block
    pinwheel_map = torch.zeros_like(direction_map, dtype=torch.bool)
    
    for i in range(direction_map.shape[0]-1):
        for j in range(direction_map.shape[1]-1):
            block = direction_map[i:i+2, j:j+2]
            # Unwrap phases and compute total change around loop
            phase_diff = unwrap_phase_differences(block)
            winding = torch.sum(phase_diff)
            
            # Pinwheel if winding number ≈ ±2π
            pinwheel_map[i, j] = abs(winding) > torch.pi
    
    return pinwheel_map
```

## Experimental Setup

### Dataset
- **Naturalistic videos**: Unlabeled video clips from natural scenes
- **Augmentation**: Temporal cropping, spatial jitter, color jitter, motion blur
- **Evaluation stimuli**: Drifting gratings, random dot kinematograms (RDKs)

### Hyperparameters
| Parameter | Value |
|-----------|-------|
| Backbone | ResNet3D-18 |
| Spatial loss weight | 0.1 (sensitivity analysis: 0.01-1.0) |
| MoCo temperature | 0.07 |
| Queue size | 65536 |
| Learning rate | 1e-4 (AdamW) |
| Training epochs | 100+ |
| Video clip length | 16 frames |

## Validation Against In Vivo Data

To validate the model against biological data:

1. **Direction Selectivity Index (DSI)**: Compare distribution of DSI values
2. **Circular Variance**: Compare tuning sharpness distributions
3. **Pinwheel Density**: Count pinwheels per mm², compare to ~3.14/mm² (universal constant)
4. **Axial Component**: Measure residual sensitivity to orthogonal motion
5. **Orientation-Direction Correlation**: Analyze joint tuning properties

## When to Use This Framework

- **Studying cortical self-organization**: Understanding how topographic maps emerge
- **Modeling dorsal stream**: Motion processing, direction selectivity
- **Unifying ventral and dorsal streams**: Single framework for both pathways
- **Testing developmental hypotheses**: What constraints shape cortical maps
- **Neuromorphic vision systems**: Bio-inspired motion detection architectures

## Related Skills

- `spatiotemporal-tdann` — broader spatiotemporal TDANN methodology
- `kuramoto-phase-encoding` — neuro-inspired phase encoding for vision transformers
- `neural-code-language-characterization` — automated neuron characterization
- `eeg-visual-attention-decoding` — visual attention decoding from neural signals

## Key Insights

1. **Universal self-organization principle**: Same computational principles govern both ventral and dorsal stream topography
2. **Trade-off shapes tuning**: MT properties emerge from balance between discriminative pressure and spatial regularization
3. **Self-supervised sufficiency**: No supervised labels needed — naturalistic videos + contrastive learning produce brain-like maps
4. **Pinwheel density as invariant**: Model reproduces the ~3.14/mm² pinwheel density found in biological cortex
5. **Direction + axial residual**: Strong direction selectivity with residual axial component matches in vivo recordings
6. **3D ResNet + spatial loss**: The combination of temporal processing and topographic regularization is key
7. **Predictive power**: Framework can generate testable predictions about MT organization under different constraints
