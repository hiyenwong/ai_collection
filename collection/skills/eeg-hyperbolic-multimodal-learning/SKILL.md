---
name: eeg-hyperbolic-multimodal-learning
description: "Hyperbolic Mixture-of-Curvature Experts (HyMoCE) for EEG-based multimodal learning. Models hierarchical brain signals in hyperbolic space with adaptive curvature for different hierarchy levels. Combines EEG with facial expressions and other modalities for mental state assessment. Activation: eeg hyperbolic, hyperbolic learning, mixture-of-curvature, hierarchical brain signals, multimodal eeg, mental state assessment."
---

# EEG-Based Multimodal Learning via Hyperbolic Mixture-of-Curvature Experts

## Overview

HyMoCE (Hyperbolic Mixture-of-Curvature Experts) is a multimodal learning framework for EEG-based mental state assessment. Unlike traditional Euclidean approaches, HyMoCE models the **hierarchical structures** inherent in EEG and associated modalities (e.g., facial expressions) in **hyperbolic space** with **different curvature parameters** for different hierarchy levels.

**Core Innovation**: Adaptive curvature in hyperbolic space captures tree-like hierarchical structures better than fixed-curvature or Euclidean approaches.

## Key Features

### 1. Hyperbolic Geometry
- **Poincaré Ball Model**: Non-Euclidean space for hierarchical data
- **Multiple Curvatures**: Different curvature for each hierarchy level
- **Tree-Like Structure**: Natural representation of EEG hierarchies

### 2. Mixture-of-Curvature Experts
- **Level-Specific Curvature**: Adaptive to data hierarchy depth
- **Expert Gating**: Dynamic selection of curvature experts
- **Hierarchical Fusion**: Multi-level feature integration

### 3. Multimodal Integration
- **EEG Signals**: Brain electrical activity
- **Facial Expressions**: Emotional state indicators
- **Cross-Modal Alignment**: Unified hyperbolic representations

## Mathematical Background

### Hyperbolic Space
In hyperbolic geometry with curvature **K** (or radius **R = 1/√|K|**):

```
Poincaré Ball Model:
D_K^n = {x ∈ R^n : ||x|| < 1/√|K|}

Distance metric:
d_K(x, y) = (1/√|K|) * arctanh(√|K| * ||(-x) ⊕_K y||)
```

### Mixture-of-Curvature
```python
# For hierarchical levels l = 1, 2, ..., L
curvature_l = learnable_parameter(l)

# Expert gating
gate_l = softmax(W_g * x + b_g)_l

# Combined representation
h = Σ_l gate_l * exp_map_Kl(0, project_Kl(x))
```

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│              HyMoCE Architecture                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  EEG Input         Facial Expression Input                      │
│  ┌───────────┐    ┌──────────────┐                             │
│  │   EEG     │    │    Facial    │                             │
│  │  Signals  │    │    Video     │                             │
│  └─────┬─────┘    └──────┬───────┘                             │
│        │                 │                                      │
│        ▼                 ▼                                      │
│  ┌───────────┐    ┌──────────────┐                             │
│  │  Spatial  │    │   Expression │                             │
│  │  Encoder  │    │    Encoder   │                             │
│  └─────┬─────┘    └──────┬───────┘                             │
│        │                 │                                      │
│        └────────┬────────┘                                      │
│                 │                                               │
│                 ▼                                               │
│        ┌──────────────────┐                                    │
│        │  Hierarchy       │                                    │
│        │  Extraction      │                                    │
│        └────────┬─────────┘                                    │
│                 │                                               │
│                 ▼                                               │
│        ┌──────────────────┐                                    │
│        │  Mixture-of-     │                                    │
│        │  Curvature       │                                    │
│        │  Experts         │                                    │
│        │  ┌──┐ ┌──┐ ┌──┐ │                                    │
│        │  │K1│ │K2│ │K3│ │  ← Different curvatures            │
│        │  └──┘ └──┘ └──┘ │                                    │
│        └────────┬─────────┘                                    │
│                 │                                               │
│                 ▼                                               │
│        ┌──────────────────┐                                    │
│        │  Hyperbolic      │                                    │
│        │  Fusion Layer    │                                    │
│        └────────┬─────────┘                                    │
│                 │                                               │
│                 ▼                                               │
│        ┌──────────────────┐                                    │
│        │  Mental State    │                                    │
│        │  Prediction      │                                    │
│        └──────────────────┘                                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Workflow

### Step 1: EEG Preprocessing

```python
from hymoce import EEGPreprocessor

# Initialize preprocessor
preprocessor = EEGPreprocessor(
    fs=256,  # Sampling rate
    filter_band=(0.5, 45),  # Hz
    notch_freq=50,  # Remove line noise
    ica_components=64
)

# Load and preprocess EEG
eeg_data = preprocessor.load('subject_eeg.set')
eeg_clean = preprocessor.apply(eeg_data)

# Extract hierarchical features
eeg_hierarchy = {
    'sensor_level': eeg_clean,  # 64 channels
    'regional': aggregate_regions(eeg_clean),  # 8 regions
    'global': eeg_clean.mean(axis=0)  # 1 global signal
}
```

### Step 2: Facial Expression Processing

```python
from hymoce import FacialExpressionEncoder

# Initialize expression encoder
face_encoder = FacialExpressionEncoder(
    backbone='resnet50',
    temporal_window=30  # frames
)

# Extract expression features
face_video = load_video('subject_face.mp4')
expression_features = face_encoder(face_video)

# Extract hierarchy
expression_hierarchy = {
    'frame_level': expression_features,  # Per-frame
    'clip_level': aggregate_clips(expression_features),  # 3s clips
    'session_level': expression_features.mean(axis=0)  # Full session
}
```

### Step 3: Initialize HyMoCE

```python
from hymoce import HyMoCE

# Initialize model
model = HyMoCE(
    eeg_channels=64,
    face_feature_dim=512,
    hidden_dim=256,
    num_curvatures=3,  # Different curvatures for 3 hierarchy levels
    curvature_range=(0.1, 2.0),  # Learnable curvature range
    output_classes=['positive', 'negative', 'neutral']
)

model = model.to(device)
```

### Step 4: Hyperbolic Encoding

```python
import geoopt  # Hyperbolic optimization library

# Convert to hyperbolic space
manifold = geoopt.PoincareBall(c=1.0)  # Curvature = 1.0

# Encode EEG hierarchy in hyperbolic space
eeg_hyperbolic = []
for level, features in eeg_hierarchy.items():
    # Map to Poincaré ball
    h = model.eeg_encoders[level](features)
    h_hyp = manifold.expmap0(h)  # Exponential map from origin
    eeg_hyperbolic.append(h_hyp)

# Encode facial expressions similarly
face_hyperbolic = []
for level, features in expression_hierarchy.items():
    h = model.face_encoders[level](features)
    h_hyp = manifold.expmap0(h)
    face_hyperbolic.append(h_hyp)
```

### Step 5: Mixture-of-Curvature Fusion

```python
# Expert gating
def mixture_of_curvature_fusion(features, model):
    """Fuse features using mixture-of-curvature experts."""
    
    # Compute gating weights
    combined = torch.cat(features, dim=-1)
    gates = F.softmax(model.gate_network(combined), dim=-1)
    
    # Apply different curvatures
    outputs = []
    for i, (features_i, curvature_i) in enumerate(
        zip(features, model.curvatures)
    ):
        manifold_i = geoopt.PoincareBall(c=curvature_i)
        
        # Transform in curvature-specific space
        h_i = model.experts[i](features_i)
        h_i_hyp = manifold_i.expmap0(h_i)
        
        outputs.append(gates[:, i:i+1] * h_i_hyp)
    
    # Combine experts
    fused = sum(outputs)
    return fused

# Fuse EEG and face in hyperbolic space
fused_representation = mixture_of_curvature_fusion(
    eeg_hyperbolic + face_hyperbolic,
    model
)
```

### Step 6: Mental State Prediction

```python
# Project to tangent space for classification
tangent_repr = manifold.logmap0(fused_representation)

# Predict mental state
logits = model.classifier(tangent_repr)
probs = F.softmax(logits, dim=-1)

predicted_state = model.output_classes[probs.argmax()]
confidence = probs.max()
```

## Implementation Details

### Hyperbolic Linear Layer

```python
import geoopt

class HyperbolicLinear(nn.Module):
    """Linear layer in hyperbolic space."""
    
    def __init__(self, in_features, out_features, curvature=1.0):
        super().__init__()
        self.manifold = geoopt.PoincareBall(c=curvature)
        self.linear = nn.Linear(in_features, out_features)
        
    def forward(self, x):
        # Map to tangent space
        x_tangent = self.manifold.logmap0(x)
        
        # Apply linear transformation
        h = self.linear(x_tangent)
        
        # Map back to hyperbolic space
        return self.manifold.expmap0(h)
```

### Curvature Learning

```python
class LearnableCurvature(nn.Module):
    """Learnable curvature parameter."""
    
    def __init__(self, init_curvature=1.0, min_curvature=0.1):
        super().__init__()
        self.curvature_param = nn.Parameter(
            torch.tensor([init_curvature])
        )
        self.min_curvature = min_curvature
        
    def forward(self):
        # Ensure positive curvature
        return F.softplus(self.curvature_param) + self.min_curvature
```

## Training

```python
from hymoce import HyMoCETrainer

# Initialize trainer
trainer = HyMoCETrainer(
    model=model,
    optimizer=geoopt.optim.RiemannianAdam(
        model.parameters(),
        lr=1e-3,
        stabilize=10  # Stabilize every 10 steps
    ),
    curvature_optimizer=torch.optim.Adam(
        model.curvature_parameters(),
        lr=1e-4
    )
)

# Training loop
for epoch in range(num_epochs):
    for batch in train_loader:
        eeg = batch['eeg'].to(device)
        face = batch['face'].to(device)
        labels = batch['label'].to(device)
        
        # Forward pass
        logits = model(eeg, face)
        
        # Loss (cross-entropy in tangent space)
        loss = F.cross_entropy(logits, labels)
        
        # Backward pass with Riemannian optimization
        trainer.step(loss)
    
    # Validation
    val_acc = trainer.validate(val_loader)
    print(f"Epoch {epoch}: Val Acc = {val_acc:.4f}")
```

## Use Cases

1. **Emotion Recognition**: Combine EEG and facial expressions
2. **Mental Workload Assessment**: Cognitive load estimation
3. **Stress Detection**: Multimodal stress level classification
4. **Attention Monitoring**: Focus and distraction detection
5. **Sleep Stage Classification**: EEG + behavioral cues

## Research Paper Reference

**Title**: EEG-Based Multimodal Learning via Hyperbolic Mixture-of-Curvature Experts  
**Authors**: Runhe Zhou, Shanglin Li, Guanxiang Huang, et al.  
**arXiv**: 2604.12579v1  
**Published**: 2026-04-14  
**Categories**: cs.LG

**Key Contributions**:
1. Hyperbolic geometry for hierarchical EEG representation
2. Mixture-of-curvature experts for adaptive geometry
3. Multimodal fusion in non-Euclidean space
4. Superior performance over Euclidean baselines

## References

- See [references/paper-details.md](references/paper-details.md) for full paper analysis
- See [references/hyperbolic-geometry.md](references/hyperbolic-geometry.md) for math background


## Activation Keywords

- eeg-hyperbolic-multimodal-learning
- eeg hyperbolic multimodal
- eeg hyperbolic multimodal learning


## Tools Used

- `read` - 读取技能文档
- `write` - 创建输出
- `exec` - 执行相关命令


## Instructions for Agents

1. 理解技能的核心方法论
2. 根据用户问题提供针对性回答
3. 遵循最佳实践


## Examples

### Example 1: 基本查询

**User:** 请解释 Eeg Hyperbolic Multimodal Learning

**Agent:** Eeg Hyperbolic Multimodal Learning 是关于...
