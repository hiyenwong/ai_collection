---
name: eeg-visual-attention-decoding
description: "Objective. Decoding visual attention from brain signals during naturalistic video viewing has emerged as a new direction in brain-computer interface research. Current methods assum... Activation: brain, decoding, eeg, neural"
---

# Eccentricity Confound in EEG-based Visual Attention Decoding from Gaze-Fixated Neural Tracking of Motion in Natural Videos

## Overview

Objective. Decoding visual attention from brain signals during naturalistic video viewing has emerged as a new direction in brain-computer interface research. Current methods assume that stronger coupling between object motion and neural activity indicates higher attention, but this can be confounded by eye movement artifacts and stimulus properties. This study investigates how visual eccentricity (the distance between a visual object and the fixation point) affects neural responses when eye movement artifacts are controlled. Approach. EEG signals were recorded across three tasks that manipula

## Source Paper

- **Title:** Eccentricity Confound in EEG-based Visual Attention Decoding from Gaze-Fixated Neural Tracking of Motion in Natural Videos
- **Authors:** Yuanyuan Yao, Celina Salamanca Gonzalez, Simon Geirnaert et al.
- **arXiv:** [2604.15223v1](https://arxiv.org/abs/2604.15223v1)
- **Published:** 2026-04-16
- **Categories:** eess.SP
- **PDF:** [Download](https://arxiv.org/pdf/2604.15223v1)

## Core Concepts

### Key Contributions

### 1. Decoding visual attention from brain signals during naturalistic video viewing has emerged as a new direction in brain-computer interface research.

### Methodology

Primary methods: attention

## Implementation

```python
# Example implementation skeleton based on Eccentricity Confound in EEG-based Visual Attention Decoding from Gaze-Fixated Neural Tracking of Motion in Natural Videos
import torch
import torch.nn as nn

class EccentricityConfoundEegVisualAttentionDecodingModel(nn.Module):
    """
    Model architecture inspired by the paper:
    Eccentricity Confound in EEG-based Visual Attention Decoding from Gaze-Fixated Neural Tracking of Motion in Natural Videos
    """
    def __init__(self, input_dim=128, hidden_dim=256, output_dim=10):
        super().__init__()
        # Core components based on: attention
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
        )
        self.head = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, x):
        features = self.encoder(x)
        return self.head(features)
```

## Practical Applications

- **Decoding**: Application of attention for decoding
- **Control**: Application of attention for control
- **Analysis**: Application of attention for analysis

## References

- Yuanyuan Yao et al. (2026). "Eccentricity Confound in EEG-based Visual Attention Decoding from Gaze-Fixated Neural Tracking of Motion in Natural Videos." arXiv:2604.15223v1.

## Activation Keywords

- brain, decoding, eeg, neural
