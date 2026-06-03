---
name: magnet-brain-structure-function
description: "MAGNet (Multi-scale Adaptive Graph Network) for learning structural-functional brain representations. Transformer-style GNN framework that adaptively learns structure-function interactions from MRI data using cross-scale attention mechanisms. Activation: magnet, brain network, structure-function coupling, graph neural network, mri analysis, cross-scale attention."
---

# MAGNet: Multi-scale Adaptive Graph Network for Brain Structure-Function

## Overview

MAGNet is a Transformer-style Graph Neural Network (GNN) framework that adaptively learns interactions between brain structure and function. It leverages **Source-Based Morphometry (SBM)** from structural MRI to extract inter-regional morphological features and employs a **cross-scale attention mechanism** that dynamically weights graph edges based on local and global connectivity patterns.

**Core Innovation**: Adaptive learning of structure-function interactions through multi-scale graph attention, bridging the gap between anatomical connectivity (structural) and functional connectivity (dynamics).

## Key Features

### 1. Source-Based Morphometry (SBM)
- Extracts inter-regional morphological features from structural MRI
- Captures anatomical covariance patterns between brain regions
- Provides structural connectivity graph

### 2. Cross-Scale Attention Mechanism
- **Local Attention**: Regional connectivity patterns
- **Global Attention**: Whole-brain network dynamics
- **Adaptive Weighting**: Dynamic edge weights based on multi-scale features

### 3. Transformer-Style Architecture
- Self-attention over graph nodes (brain regions)
- Multi-head attention for diverse relationship types
- Residual connections and layer normalization

## Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                    MAGNet Architecture                         │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Structural Input          Functional Input                    │
│  ┌──────────────┐         ┌──────────────┐                    │
│  │  Structural  │         │   fMRI Time  │                    │
│  │    MRI       │         │    Series    │                    │
│  └──────┬───────┘         └──────┬───────┘                    │
│         │                        │                            │
│         ▼                        ▼                            │
│  ┌──────────────┐         ┌──────────────┐                    │
│  │  Source-Based│         │  Functional  │                    │
│  │ Morphometry  │         │ Connectivity │                    │
│  └──────┬───────┘         └──────┬───────┘                    │
│         │                        │                            │
│         └──────────┬─────────────┘                            │
│                    │                                           │
│                    ▼                                           │
│         ┌──────────────────┐                                 │
│         │   Cross-Scale    │                                 │
│         │    Attention     │                                 │
│         │  ┌────────────┐  │                                 │
│         │  │   Local    │  │                                 │
│         │  │  Attention │  │                                 │
│         │  └────────────┘  │                                 │
│         │  ┌────────────┐  │                                 │
│         │  │   Global   │  │                                 │
│         │  │  Attention │  │                                 │
│         │  └────────────┘  │                                 │
│         └────────┬─────────┘                                 │
│                  │                                            │
│                  ▼                                            │
│         ┌──────────────────┐                                 │
│         │  Multi-Head      │                                 │
│         │  Transformer     │                                 │
│         │  Layers          │                                 │
│         └────────┬─────────┘                                 │
│                  │                                            │
│                  ▼                                            │
│         ┌──────────────────┐                                 │
│         │  Structure-Func  │                                 │
│         │  Representation  │                                 │
│         └──────────────────┘                                 │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## Workflow

### Step 1: Preprocess Structural MRI

```python
from magnet import MAGNetPreprocessor

# Extract source-based morphometry
preprocessor = MAGNetPreprocessor()

# Load structural MRI data
structural_mri = load_mri('subject_T1.nii.gz')

# Apply source-based morphometry
sbm_features = preprocessor.extract_sbm(
    mri=structural_mri,
    atlas='desikan_killiany',  # or 'aal', 'brainnectome'
    n_components=40  # Number of SBM sources
)

# Build structural graph
structural_graph = build_sbm_graph(sbm_features)
```

### Step 2: Compute Functional Connectivity

```python
# Load fMRI data
fmri_data = load_fmri('subject_rsfmri.nii.gz')

# Compute functional connectivity matrix
fc_matrix = compute_functional_connectivity(
    fmri_data,
    method='pearson',  # or 'partial_correlation', 'mutual_information'
    atlas='desikan_killiany'
)

# Extract time series features
functional_features = extract_timeseries_features(fmri_data)
```

### Step 3: Initialize MAGNet

```python
from magnet import MAGNet

# Initialize MAGNet model
model = MAGNet(
    n_regions=68,  # Number of brain regions (Desikan-Killiany)
    n_sbm_sources=40,
    hidden_dim=128,
    n_heads=8,  # Multi-head attention
    n_layers=4,  # Transformer layers
    dropout=0.3
)

# Move to device
model = model.to(device)
```

### Step 4: Forward Pass with Cross-Scale Attention

```python
# Prepare inputs
structural_input = structural_graph.to(device)
functional_input = functional_features.to(device)

# Forward pass
output = model(
    structural_graph=structural_input,
    functional_features=functional_input,
    return_attention_weights=True
)

# Extract learned representations
structure_function_repr = output['representation']
attention_weights = output['attention_weights']
```

### Step 5: Interpret Attention Weights

```python
# Visualize cross-scale attention
import matplotlib.pyplot as plt

# Local attention (regional patterns)
local_attn = attention_weights['local']
plt.figure(figsize=(10, 8))
sns.heatmap(local_attn, cmap='viridis')
plt.title('Local Attention Weights')
plt.xlabel('Brain Regions')
plt.ylabel('Brain Regions')
plt.show()

# Global attention (whole-brain patterns)
global_attn = attention_weights['global']
plt.figure(figsize=(10, 8))
sns.heatmap(global_attn, cmap='viridis')
plt.title('Global Attention Weights')
plt.show()
```

## Implementation Details

### Cross-Scale Attention Module

```python
class CrossScaleAttention(nn.Module):
    """Cross-scale attention for structure-function learning."""
    
    def __init__(self, hidden_dim, n_heads):
        super().__init__()
        self.local_attention = MultiHeadAttention(hidden_dim, n_heads)
        self.global_attention = MultiHeadAttention(hidden_dim, n_heads)
        self.scale_gate = nn.Linear(hidden_dim * 2, 2)  # Local/global gate
        
    def forward(self, structural_features, functional_features):
        # Local attention (region-level)
        local_out = self.local_attention(
            query=functional_features,
            key=structural_features,
            value=structural_features
        )
        
        # Global attention (network-level)
        global_out = self.global_attention(
            query=functional_features.mean(dim=0, keepdim=True),
            key=structural_features,
            value=structural_features
        )
        
        # Adaptive gating between local and global
        gate_input = torch.cat([local_out, global_out.expand_as(local_out)], dim=-1)
        gates = F.softmax(self.scale_gate(gate_input), dim=-1)
        
        # Combine scales
        output = gates[:, 0:1] * local_out + gates[:, 1:2] * global_out
        return output
```

### Multi-Scale Graph Transformer

```python
class MAGNetTransformer(nn.Module):
    """Transformer layers for graph-structured brain data."""
    
    def __init__(self, hidden_dim, n_heads, n_layers):
        super().__init__()
        self.layers = nn.ModuleList([
            TransformerLayer(hidden_dim, n_heads)
            for _ in range(n_layers)
        ])
        
    def forward(self, x, adjacency):
        for layer in self.layers:
            x = layer(x, adjacency)
        return x
```

## Training

```python
from magnet import MAGNetTrainer

# Initialize trainer
trainer = MAGNetTrainer(
    model=model,
    optimizer='adam',
    lr=1e-4,
    weight_decay=1e-5
)

# Training loop
for epoch in range(num_epochs):
    for batch in train_loader:
        structural = batch['structural']
        functional = batch['functional']
        labels = batch['label']  # e.g., cognitive score, disease label
        
        # Forward pass
        output = model(structural, functional)
        
        # Compute loss
        loss = F.mse_loss(output['prediction'], labels)
        
        # Backward pass
        trainer.step(loss)
    
    # Validation
    val_loss = trainer.validate(val_loader)
    print(f"Epoch {epoch}: Val Loss = {val_loss:.4f}")
```

## Use Cases

1. **Cognitive State Prediction**: Predict cognitive performance from brain networks
2. **Disease Classification**: Classify neurological disorders (ADHD, Alzheimer's)
3. **Structure-Function Coupling Analysis**: Study how anatomy shapes function
4. **Brain Development**: Track structural-functional changes across lifespan

## Research Paper Reference

**Title**: Learning Structural-Functional Brain Representations through Multi-Scale Adaptive Graph Attention for Cognitive Insight  
**Authors**: Badhan Mazumder, Sir-Lord Wiafe, Aline Kotoski, et al.  
**arXiv**: 2603.29967v1  
**Published**: 2026-03-31  
**Categories**: cs.CV

**Key Contributions**:
1. Novel MAGNet architecture for adaptive structure-function learning
2. Cross-scale attention mechanism (local + global)
3. Source-based morphometry integration
4. Transformer-style processing of brain graphs

## References

- See [references/paper-details.md](references/paper-details.md) for full paper analysis
- See [references/implementation-examples.py](references/implementation-examples.py) for code


## Activation Keywords

- magnet-brain-structure-function
- magnet brain structure
- magnet brain structure function


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

**User:** 请解释 Magnet Brain Structure Function

**Agent:** Magnet Brain Structure Function 是关于...
