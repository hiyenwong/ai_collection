---
name: li-dsn-eeg-decoding
description: Layer-wise Interactive Dual-Stream Network (LI-DSN) for EEG decoding. Introduces Temporal-Spatial Integration Attention (TSIA) with Spatial Affinity Correlation Matrix (SACM) and Temporal Channel Aggregation Matrix (TCAM) for progressive cross-stream communication, overcoming late-fusion limitations in dual-stream EEG networks. Validated on 8 datasets across motor imagery, emotion recognition, and SSVEP.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    source_paper: "LI-DSN: A Layer-wise Interactive Dual-Stream Network for EEG Decoding (arXiv:2604.01889)"
    published: "2026-04-02"
    authors: "Chenghao Yue, Zhiyuan Ma, Zhongye Xia"
    citations: 0 (recent)
    tags: [eeg, decoding, dual-stream, attention, bci, motor-imagery, emotion-recognition, ssvep, 脑电解码]
---

# LI-DSN: Layer-wise Interactive Dual-Stream Network for EEG Decoding

## Overview

LI-DSN addresses the "information silo" problem in dual-stream EEG networks by replacing late-stage fusion with **progressive layer-wise cross-stream communication**. The key innovation is the **Temporal-Spatial Integration Attention (TSIA)** mechanism that enables spatial-temporal decomposition and refinement at every layer.

### Why Layer-wise Interaction Matters

| Traditional Dual-Stream | LI-DSN Layer-wise |
|-------------------------|-------------------|
| Temporal & spatial branches run independently | Cross-stream communication at every layer |
| Late fusion loses intermediate refinement | Progressive spatial-temporal decomposition |
| Information silos between branches | Spatial guidance shapes temporal aggregation |
| Single fusion point bottleneck | Adaptive fusion with learnable channel weights |

Validated across **8 diverse EEG datasets**: motor imagery (MI) classification, emotion recognition, and steady-state visual evoked potentials (SSVEP), outperforming 13 SOTA baselines.

## Core Concepts

### 1. Temporal-Spatial Integration Attention (TSIA)

TSIA constructs two key matrices that enable cross-stream communication:

**Spatial Affinity Correlation Matrix (SACM):**
```python
import torch
import torch.nn as nn
import torch.nn.functional as F

def compute_sacm(spatial_features):
    """
    Spatial Affinity Correlation Matrix: captures inter-electrode spatial 
    structural relationships.
    
    Args:
        spatial_features: (B, n_channels, spatial_dim) tensor
    Returns:
        SACM: (B, n_channels, n_channels) spatial affinity matrix
    """
    # Normalize features
    spatial_norm = F.normalize(spatial_features, p=2, dim=-1)
    
    # Compute pairwise spatial affinity
    # SACM[i,j] measures how much electrode i correlates with electrode j
    sacm = torch.bmm(spatial_norm, spatial_norm.transpose(1, 2))
    
    # Optional: apply temperature scaling for sharper attention
    temperature = 0.1
    sacm = sacm / temperature
    
    return sacm
```

**Temporal Channel Aggregation Matrix (TCAM):**
```python
def compute_tcam(temporal_features, sacm):
    """
    Temporal Channel Aggregation Matrix: integrates cosine-gated temporal 
    dynamics under spatial guidance from SACM.
    
    Args:
        temporal_features: (B, n_channels, temporal_dim) tensor
        sacm: (B, n_channels, n_channels) from SACM
    Returns:
        TCAM: (B, n_channels, temporal_dim) spatially-guided temporal features
    """
    # Cosine gating: modulate temporal features by spatial affinity
    # Spatial attention weights
    spatial_weights = F.softmax(sacm.mean(dim=1), dim=-1)  # (B, n_channels)
    
    # Apply spatial guidance to temporal features
    # Each channel's temporal dynamics is weighted by its spatial correlation
    gated_temporal = temporal_features * spatial_weights.unsqueeze(-1)
    
    # Cosine activation for smooth gating
    tcam = torch.cos(gated_temporal) * gated_temporal
    
    return tcam
```

### 2. Layer-wise Interactive Dual-Stream Architecture

```python
class LI_DSNEncoder(nn.Module):
    """
    Layer-wise Interactive Dual-Stream Network for EEG decoding.
    
    Architecture:
      - Temporal Stream: captures temporal dynamics in EEG signals
      - Spatial Stream: captures spatial relationships between electrodes
      - At each layer: TSIA enables bidirectional cross-stream communication
      - Final: Adaptive fusion with learnable channel weights
    """
    
    def __init__(self, n_channels=22, n_temporal=64, n_layers=4, n_classes=4):
        super().__init__()
        
        # Temporal stream layers
        self.temporal_layers = nn.ModuleList([
            nn.Sequential(
                nn.Conv1d(n_channels if i == 0 else n_temporal, n_temporal, 
                          kernel_size=5, padding=2),
                nn.BatchNorm1d(n_temporal),
                nn.GELU(),
            ) for i in range(n_layers)
        ])
        
        # Spatial stream layers
        self.spatial_layers = nn.ModuleList([
            nn.Sequential(
                nn.Conv1d(n_temporal if i == 0 else n_temporal, n_temporal, 
                          kernel_size=3, padding=1),
                nn.BatchNorm1d(n_temporal),
                nn.GELU(),
            ) for i in range(n_layers)
        ])
        
        # TSIA modules at each layer
        self.tsia_modules = nn.ModuleList([
            TSIALayer(n_channels, n_temporal) 
            for _ in range(n_layers)
        ])
        
        # Adaptive fusion with learnable channel weights
        self.fusion_weight = nn.Parameter(torch.tensor(0.5))
        self.classifier = nn.Sequential(
            nn.Linear(n_temporal * 2, n_temporal),
            nn.GELU(),
            nn.Dropout(0.5),
            nn.Linear(n_temporal, n_classes),
        )
    
    def forward(self, x):
        """
        Args:
            x: (B, n_channels, temporal_length) EEG input
        """
        temporal_feat = x  # (B, n_channels, T)
        spatial_feat = x   # (B, n_channels, T)
        
        for t_layer, s_layer, tsia in zip(
            self.temporal_layers, self.spatial_layers, self.tsia_modules
        ):
            # Process each stream
            temporal_feat = t_layer(temporal_feat)
            spatial_feat = s_layer(spatial_feat)
            
            # Cross-stream communication via TSIA
            temporal_feat, spatial_feat = tsia(temporal_feat, spatial_feat)
        
        # Adaptive fusion
        alpha = torch.sigmoid(self.fusion_weight)
        fused = alpha * temporal_feat + (1 - alpha) * spatial_feat
        
        # Global pooling + classification
        pooled = F.adaptive_avg_pool1d(fused, 1).squeeze(-1)
        logits = self.classifier(pooled)
        
        return logits


class TSIALayer(nn.Module):
    """Single TSIA layer for cross-stream communication."""
    
    def __init__(self, n_channels, n_temporal):
        super().__init__()
        self.sacm_proj = nn.Linear(n_temporal, n_temporal)
        self.tcam_proj = nn.Linear(n_temporal, n_temporal)
        self.norm1 = nn.LayerNorm(n_temporal)
        self.norm2 = nn.LayerNorm(n_temporal)
    
    def forward(self, temporal_feat, spatial_feat):
        """
        Bidirectional cross-stream refinement.
        
        Returns:
            refined_temporal, refined_spatial
        """
        # Spatial → Temporal: SACM guides temporal aggregation
        sacm = compute_sacm(spatial_feat.transpose(1, 2))
        tcam = compute_tcam(temporal_feat.transpose(1, 2), sacm)
        temporal_refined = self.tcam_proj(tcam.transpose(1, 2))
        temporal_feat = self.norm1(temporal_feat + temporal_refined)
        
        # Temporal → Spatial: temporal dynamics inform spatial patterns
        temporal_context = temporal_feat.mean(dim=-1, keepdim=True)
        spatial_refined = spatial_feat * torch.sigmoid(temporal_context)
        spatial_feat = self.norm2(spatial_feat + spatial_refined)
        
        return temporal_feat, spatial_feat
```

### 3. Adaptive Fusion Strategy

```python
class AdaptiveFusion(nn.Module):
    """
    Adaptive fusion with learnable channel weights for optimal 
    integration of dual-stream features.
    """
    
    def __init__(self, n_channels):
        super().__init__()
        self.channel_weights = nn.Parameter(
            torch.ones(n_channels) / n_channels
        )
        self.gate = nn.Sequential(
            nn.Linear(n_channels * 2, n_channels),
            nn.Sigmoid(),
        )
    
    def forward(self, temporal_feat, spatial_feat):
        # Learnable channel-wise importance
        gate_weights = self.gate(
            torch.cat([temporal_feat.mean(-1), spatial_feat.mean(-1)], dim=-1)
        )
        
        # Gated fusion
        fused = gate_weights * temporal_feat + (1 - gate_weights) * spatial_feat
        
        return fused
```

## Key Insights

1. **Progressive fusion > Late fusion**: Cross-stream communication at every layer enables intermediate refinement that late-fusion paradigms miss.
2. **Spatial guidance for temporal dynamics**: The SACM captures inter-electrode relationships that directly inform how temporal features should be aggregated.
3. **Cosine gating**: Smooth, bounded activation prevents extreme values and provides stable gradients during training.
4. **Learnable fusion weights**: Instead of fixed concatenation/summation, the model learns the optimal balance between temporal and spatial streams.

## Applications

- **Motor Imagery (MI) BCI**: Real-time prosthetic control, rehabilitation
- **Emotion Recognition**: Affective computing, mental health monitoring
- **SSVEP Decoding**: High-throughput communication interfaces
- **Cross-dataset generalization**: Architecture robust across different EEG paradigms

## Activation Keywords

- EEG decoding, dual-stream network, layer-wise interaction
- TSIA, SACM, TCAM, spatial-temporal attention
- Motor imagery, emotion recognition, SSVEP
- 脑电解码, 双流网络, 层间交互, 时空注意力

## References

- Yue, C., Ma, Z., Xia, Z. (2026). "LI-DSN: A Layer-wise Interactive Dual-Stream Network for EEG Decoding." arXiv:2604.01889.

## Related Skills

- [[neuroscience-research-method]] - CNN + AAE for EEG classification
- [[eeg2vision-multimodal-eeg-framework-2d-visual]] - Multimodal EEG-to-image reconstruction
- [[eccentricity-confound-eeg-visual-attention-decoding]] - EEG visual attention decoding
