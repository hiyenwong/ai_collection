---
name: in-context-brain-decoding
description: Meta-learning approach for training-free cross-subject brain decoding from fMRI. Uses in-context learning to adapt to new subjects without fine-tuning, addressing neural representation variability. Activation: brain decoding, meta-learning, in-context learning, cross-subject fmri.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, meta-learning, brain-decoding, fmri, cross-subject]
    source_paper: "Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding (arXiv:2604.08537)"
    citations: 0
---

# In-Context Meta-Learning for Brain Decoding

## Overview
Meta-optimized approach for semantic visual decoding from fMRI that generalizes to novel subjects without fine-tuning. By conditioning on a small set of image-brain activation examples, the model rapidly infers unique neural encoding patterns.

## Core Concepts
- Cross-Subject Variability Challenge
- Meta-Learning (Learning to Learn)
- In-Context Learning with cross-attention

## Implementation Pattern

```python
import torch
import torch.nn as nn

class InContextBrainDecoder(nn.Module):
    def __init__(self, brain_dim=10000, image_dim=512, hidden_dim=1024, n_context=8):
        super().__init__()
        self.brain_encoder = nn.Sequential(
            nn.Linear(brain_dim, hidden_dim), nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim), nn.ReLU()
        )
        self.image_encoder = nn.Sequential(
            nn.Linear(image_dim, hidden_dim), nn.ReLU()
        )
        self.cross_attention = nn.MultiheadAttention(hidden_dim, 8, batch_first=True)
        self.decoder = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim), nn.ReLU(),
            nn.Linear(hidden_dim, image_dim)
        )
    
    def forward(self, query_brain, context_brains, context_images):
        query = self.brain_encoder(query_brain).unsqueeze(1)
        context_b = self.brain_encoder(context_brains)
        context_i = self.image_encoder(context_images)
        attended, _ = self.cross_attention(query, context_b, context_i)
        return self.decoder(attended.squeeze(1))
```

## Applications
- Visual Decoding from fMRI
- Cross-Subject Studies
- Rapid BCI Calibration

## References
- arXiv:2604.08537
- Tsimpoukelli et al. (2021)
