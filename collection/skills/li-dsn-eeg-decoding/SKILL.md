---
name: li-dsn-eeg-decoding
description: Layer-wise Interactive Dual-Stream Network (LI-DSN) for EEG Motor Imagery decoding with cross-subject generalization, spatial-temporal dual-stream architecture, and layer-wise interactive fusion. Addresses the challenge of EEG signal variability across subjects through dual-stream processing and interactive fusion at each network layer. Use when: EEG motor imagery decoding, cross-subject EEG classification, dual-stream neural networks, layer-wise feature fusion, brain-computer interface classification, spatial-temporal EEG features, EEG domain adaptation, motor imagery BCI. Activation: LI-DSN, dual-stream EEG, motor imagery decoding, cross-subject EEG, layer-wise fusion, spatial-temporal EEG network, EEG BCI classification, interactive dual-stream, EEG motor classification.
version: 1.0.0
metadata:
  hermes:
    tags: [EEG, motor-imagery, dual-stream, cross-subject, BCI, layer-wise-fusion, spatial-temporal, domain-adaptation]
    source_paper: "LI-DSN: Layer-wise Interactive Dual-Stream Network for EEG Decoding (arXiv:2604.00123)"
    date: 2026-04-01
---

# LI-DSN: Layer-wise Interactive Dual-Stream Network for EEG Decoding

## Overview

LI-DSN addresses the key challenge in EEG motor imagery decoding: high variability across subjects. The architecture uses:

1. **Spatial stream**: Captures electrode-topology-based spatial patterns
2. **Temporal stream**: Extracts time-frequency dynamics
3. **Layer-wise interactive fusion**: Bidirectional information exchange between streams at each layer
4. **Cross-subject generalization**: Domain-invariant feature learning

**Source Paper**: LI-DSN (arXiv:2604.00123, 2026-04-01)

## Core Architecture

```
┌──────────────────────────────────────────────┐
│              LI-DSN Architecture              │
├──────────────────────────────────────────────┤
│           EEG Input (C × T)                   │
│              ↓                                │
│    ┌──────────────┬──────────────┐            │
│    │ Spatial Stream│ Temporal Stream│           │
│    │  (topology)  │ (time-freq)   │           │
│    └──────┬───────┴───────┬───────┘            │
│           ↓  ↕ FUSION ↕   ↓                    │
│    ┌──────────────┬──────────────┐            │
│    │ Spatial Layer│ Temporal Layer│            │
│    │     n        │      n        │            │
│    └──────┬───────┴───────┬───────┘            │
│           ↓               ↓                    │
│         Classification Layer                    │
└──────────────────────────────────────────────┘
```

## Key Innovations

1. **Interactive fusion**: Streams communicate at every layer, not just at the end
2. **Dual-stream design**: Separately models spatial topology and temporal dynamics
3. **Cross-subject robustness**: Learns domain-invariant representations

## Implementation Pattern

```python
import torch
import torch.nn as nn

class InteractiveFusion(nn.Module):
    """Layer-wise bidirectional fusion between spatial and temporal streams."""
    
    def __init__(self, dim):
        super().__init__()
        self.spatial_to_temporal = nn.Linear(dim, dim)
        self.temporal_to_spatial = nn.Linear(dim, dim)
        self.norm = nn.LayerNorm(dim)
        
    def forward(self, spatial_feat, temporal_feat):
        # Spatial features inform temporal processing
        temporal_update = temporal_feat + self.spatial_to_temporal(spatial_feat)
        # Temporal features inform spatial processing  
        spatial_update = spatial_feat + self.temporal_to_spatial(temporal_feat)
        
        return self.norm(spatial_update), self.norm(temporal_update)


class LIDSN(nn.Module):
    """Layer-wise Interactive Dual-Stream Network."""
    
    def __init__(self, n_channels=22, n_classes=4, n_layers=4, dim=64):
        super().__init__()
        # Spatial stream: convolution over electrode topology
        self.spatial_conv = nn.Conv2d(1, dim, (n_channels, 1))
        # Temporal stream: depthwise separable conv over time
        self.temporal_conv = nn.Conv2d(1, dim, (1, 50))
        
        # Interactive fusion layers
        self.fusion_layers = nn.ModuleList([
            InteractiveFusion(dim) for _ in range(n_layers)
        ])
        
        self.classifier = nn.Linear(dim, n_classes)
    
    def forward(self, x):
        """
        Args:
            x: EEG data of shape (batch, 1, n_channels, time)
        """
        spatial_feat = self.spatial_conv(x).squeeze(2)
        temporal_feat = self.temporal_conv(x).squeeze(2)
        
        # Layer-wise interactive fusion
        for fusion in self.fusion_layers:
            spatial_feat, temporal_feat = fusion(spatial_feat, temporal_feat)
        
        # Combine streams
        combined = spatial_feat + temporal_feat
        return self.classifier(combined.mean(dim=1))
```

## Applications

- **Motor imagery BCI**: Classify intended movements from EEG
- **Rehabilitation**: Control prosthetic devices via motor imagery
- **Cross-subject deployment**: Deploy models without per-subject calibration
- **Neurofeedback**: Real-time brain state classification

## Related Skills

- eeg-visual-attention-decoding — EEG-based visual attention decoding
- am-mteeg-classification — Multi-task EEG classification
- eeg2vision-multimodal-eeg-framework — EEG-to-image reconstruction
