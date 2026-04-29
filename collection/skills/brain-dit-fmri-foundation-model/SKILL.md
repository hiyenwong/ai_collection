---
name: brain-dit-fmri-foundation-model
description: "Brain-DiT universal multi-state fMRI foundation model — handles diverse brain states through diffusion transformer architecture. Pre-trained on multiple brain states with unified representation learning. Activation: brain dit, fmri foundation model, diffusion transformer, brain states, multi-state fmri."
version: 1.0.0
metadata:
  hermes:
    source_paper: "Brain-DiT Universal Multi-state fMRI Foundation Model (arXiv:2604.12683)"
    tags: [neuroscience, fmri, foundation-model, diffusion, transformer]
---

# Brain-DiT: Universal Multi-state fMRI Foundation Model

## Source Paper
- **Title**: Brain-DiT Universal Multi-state fMRI Foundation Model
- **arXiv**: 2604.12683
- **PDF**: https://arxiv.org/pdf/2604.12683

## Overview

Current fMRI foundation models primarily rely on a limited range of brain states and mismatched pretraining tasks, restricting their ability to learn universal representations. This paper introduces **Brain-DiT**, a universal multi-state fMRI foundation model based on diffusion transformers that handles diverse brain states (resting, task, pathological) through a unified architecture.

## Core Concepts

### Multi-State Pretraining
- Traditional models trained on single state (resting-state only)
- Brain-DiT pretrains on diverse states: resting, task-evoked, clinical
- State-specific conditioning through adaptive layer normalization
- Unified representation across brain states

### Diffusion Transformer Architecture
- Denoising Diffusion Probabilistic Model (DDPM) backbone
- Transformer blocks for long-range spatial dependencies
- Temporal attention for dynamic functional connectivity
- Conditional generation based on state labels

### Universal Representation Learning
- Self-supervised pretraining with masked brain region modeling
- Contrastive learning across brain states
- Cross-state transfer: resting → task → clinical
- Downstream tasks: decoding, generation, anomaly detection

## Implementation Pattern

```python
import torch
import torch.nn as nn

class BrainDiT(nn.Module):
    """Diffusion Transformer for multi-state fMRI."""
    
    def __init__(self, n_regions=200, hidden_dim=768, n_layers=12, n_states=5):
        super().__init__()
        self.n_regions = n_regions
        self.n_states = n_states
        
        # Input embedding
        self.region_emb = nn.Linear(1, hidden_dim)
        
        # State conditioning
        self.state_emb = nn.Embedding(n_states, hidden_dim)
        self.state_norm = nn.LayerNorm(hidden_dim)
        
        # Transformer backbone
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=hidden_dim, nhead=8, dim_feedforward=hidden_dim*4
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, n_layers)
        
        # Diffusion noise prediction
        self.noise_head = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, 1)
        )
        
        # Time embedding for diffusion
        self.time_emb = nn.Sequential(
            nn.Linear(1, hidden_dim),
            nn.SiLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
    
    def forward(self, x, t, state_id):
        """
        Forward pass for diffusion training.
        
        Args:
            x: fMRI data (batch x n_regions x 1)
            t: diffusion timestep (batch x 1)
            state_id: brain state label (batch)
        """
        # Region embedding
        h = self.region_emb(x)  # batch x n_regions x hidden
        
        # Add time and state conditioning
        t_emb = self.time_emb(t).unsqueeze(1)
        s_emb = self.state_emb(state_id).unsqueeze(1)
        h = h + t_emb + s_emb
        h = self.state_norm(h)
        
        # Transformer
        h = h.transpose(0, 1)  # n_regions x batch x hidden
        h = self.transformer(h)
        h = h.transpose(0, 1)
        
        # Predict noise
        noise_pred = self.noise_head(h)
        return noise_pred
    
    def generate(self, state_id, n_steps=1000):
        """Generate fMRI pattern for a given brain state."""
        x = torch.randn(1, self.n_regions, 1)
        for t in reversed(range(n_steps)):
            t_tensor = torch.tensor([t / n_steps]).unsqueeze(0)
            noise = self.forward(x, t_tensor, state_id)
            x = self._denoise_step(x, noise, t, n_steps)
        return x
```

## Applications
- **fMRI decoding**: Predict cognitive states from brain activity
- **Data augmentation**: Generate synthetic fMRI for rare conditions
- **Cross-study harmonization**: Align datasets from different scanners
- **Clinical diagnosis**: Detect pathological patterns in neurological disorders

## Key Parameters
| Parameter | Description | Typical Value |
|-----------|-------------|---------------|
| n_regions | Number of brain regions (parcellation) | 200-1000 |
| hidden_dim | Transformer hidden dimension | 512-1024 |
| n_layers | Number of transformer layers | 6-24 |
| n_states | Number of brain state categories | 3-10 |

## Related Skills
- [[brain-foundation-model-batch-effects]]
- [[task-aware-brain-connectivity]]
- [[multimodal-brain-connectivity-gnn]]
