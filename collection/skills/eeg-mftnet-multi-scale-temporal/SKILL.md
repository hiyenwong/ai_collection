---
name: eeg-mftnet-multi-scale-temporal
description: "EEG-MFTNet: Enhanced EEGNet with multi-scale temporal convolution and fusion transformer for cross-session motor imagery decoding. Addresses session variability in BCI through dual-branch architecture combining frequency-specific temporal features with global temporal modeling."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [eeg, motor-imagery, bci, deep-learning, transformer]
    source_paper: "EEG-MFTNet: An Enhanced EEGNet Architecture with Multi-Scale Temporal Convolution and Fusion Transformer for Cross-Session Motor Imagery Decoding (arXiv:2604.05843)"
    citations: 0
---

# EEG-MFTNet: Multi-Scale Temporal Fusion for Cross-Session MI Decoding

## Overview

EEG-MFTNet addresses the critical challenge of **cross-session performance degradation** in motor imagery (MI) BCI systems. Session variability (electrode placement shifts, mental state changes, fatigue) causes significant accuracy drops. EEG-MFTNet combines multi-scale temporal convolution with a fusion transformer to achieve robust cross-session decoding.

**Source Paper**: arXiv:2604.05843

## Architecture

### Dual-Branch Design

1. **Frequency-Specific Temporal Branch (FSTB)**
   - Multi-scale temporal convolutions capture different frequency bands
   - Filters tuned to MI-relevant bands (mu: 8-13 Hz, beta: 13-30 Hz)
   - Parallel paths for different temporal resolutions

2. **Fusion Transformer Branch**
   - Global temporal attention across all channels
   - Captures long-range temporal dependencies
   - Fuses features from FSTB with learned attention weights

### Cross-Session Robustness

- Domain adaptation through feature alignment
- Batch normalization statistics tracking across sessions
- Regularization to prevent overfitting to session-specific patterns

## Implementation Pattern

```python
import torch
import torch.nn as nn

class MultiScaleTemporalConv(nn.Module):
    """Multi-scale temporal convolution for EEG feature extraction."""
    
    def __init__(self, in_channels=22, num_scales=3, 
                 kernel_sizes=[15, 35, 65]):
        super().__init__()
        self.branches = nn.ModuleList([
            nn.Sequential(
                nn.Conv2d(1, num_scales, (1, ks), padding=(0, ks//2)),
                nn.BatchNorm2d(num_scales),
                nn.ELU()
            ) for ks in kernel_sizes
        ])
        self.spatial_conv = nn.Conv2d(
            num_scales * len(kernel_sizes), num_scales * len(kernel_sizes),
            (in_channels, 1), groups=1
        )
        
    def forward(self, x):
        # x: (B, 1, channels, time)
        features = [branch(x) for branch in self.branches]
        features = torch.cat(features, dim=1)
        features = self.spatial_conv(features)
        return features

class FusionTransformer(nn.Module):
    """Transformer for global temporal fusion of EEG features."""
    
    def __init__(self, d_model=64, nhead=4, num_layers=2):
        super().__init__()
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=nhead, dim_feedforward=128
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers)
        
    def forward(self, x):
        # x: (time, B, d_model)
        return self.transformer(x)

class EEGMFTNet(nn.Module):
    """Complete EEG-MFTNet architecture."""
    
    def __init__(self, channels=22, num_classes=4):
        super().__init__()
        self.temporal_branch = MultiScaleTemporalConv(channels)
        self.transformer = FusionTransformer(d_model=64)
        self.classifier = nn.Sequential(
            nn.Linear(64, 32),
            nn.ELU(),
            nn.Dropout(0.5),
            nn.Linear(32, num_classes)
        )
        
    def forward(self, x):
        # x: (B, 1, channels, time)
        features = self.temporal_branch(x)
        # Reshape for transformer
        features = features.mean(dim=1)  # (B, features, time)
        features = features.permute(2, 0, 1)  # (time, B, features)
        features = self.transformer(features)
        features = features.mean(dim=0)  # (B, features)
        return self.classifier(features)
```

## Key Design Decisions

1. **Multi-Scale Kernels**: Different kernel sizes capture different oscillatory patterns
2. **Fusion Strategy**: Attention-based fusion outperforms simple concatenation
3. **Regularization**: Dropout and weight decay critical for cross-session generalization

## Applications

1. **Motor Imagery BCI**: Cross-session decoding for rehabilitation
2. **BCI Calibration Reduction**: Reduce calibration time for new sessions
3. **Clinical Applications**: Stroke rehabilitation, neuroprosthetics

## Activation Keywords

- EEG motor imagery decoding
- cross-session BCI
- multi-scale temporal convolution
- EEG transformer
- EEG-MFTNet
- 脑电运动想象解码
- 跨会话BCI

## Related Skills

- eeg-visual-attention-decoding
- eccentricity-confound-eeg-visual-attention-decoding
- eeg-hopfield-emotion-energy
- copilot-assisted-second-thought-bci
