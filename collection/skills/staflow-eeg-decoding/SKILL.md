---
name: staflow-eeg-decoding
description: "State-Flow Coordinated Network (StaFlowNet) for Motor Imagery EEG decoding. Dual-stream architecture capturing global state (spectral) and fine-grained flow (temporal) information via coordinated representation learning. Use when: EEG decoding, motor imagery, BCI, state-flow representation, dual-stream EEG, MI-EEG classification."
---

# State-Flow Coordinated EEG Decoding (StaFlowNet)

## Overview

Motor Imagery (MI) EEG decoding via dual-stream architecture that separately models:
- **State stream**: Global task context from spectral features
- **Flow stream**: Fine-grained temporal dynamics from time-domain features

Two streams are coordinated through cross-attention to produce unified representation for classification.

## Source

**Paper:** State-Flow Coordinated Representation for MI-EEG Decoding
**arXiv:** 2604.08157v1

## Core Architecture

### State Stream (Spectral)
Captures global context: frequency band power, spatial patterns, task-level information.

### Flow Stream (Temporal)
Captures fine-grained dynamics: temporal evolution, micro-state transitions, sequential patterns.

### Coordination Module
Cross-attention between state and flow representations with residual connections.

## Implementation

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class StaFlowNet(nn.Module):
    def __init__(self, n_channels=22, n_classes=4, state_dim=128, flow_dim=128):
        super().__init__()
        
        # State stream: spectral features
        self.state_encoder = nn.Sequential(
            nn.Conv2d(1, 32, (1, n_channels)),
            nn.BatchNorm2d(32),
            nn.ELU(),
            nn.Conv2d(32, 64, (n_channels, 1)),
            nn.BatchNorm2d(64),
            nn.ELU(),
            nn.Flatten(),
            nn.Linear(64, state_dim)
        )
        
        # Flow stream: temporal features
        self.flow_encoder = nn.Sequential(
            nn.Conv1d(n_channels, 64, kernel_size=64, stride=16),
            nn.BatchNorm1d(64),
            nn.ELU(),
            nn.Conv1d(64, 128, kernel_size=32, stride=8),
            nn.BatchNorm1d(128),
            nn.ELU(),
            nn.AdaptiveAvgPool1d(1),
            nn.Flatten(),
            nn.Linear(128, flow_dim)
        )
        
        # Coordination via cross-attention
        self.coordination = nn.MultiheadAttention(
            embed_dim=state_dim, num_heads=4, batch_first=True
        )
        
        self.classifier = nn.Sequential(
            nn.Linear(state_dim + flow_dim, 64),
            nn.ELU(),
            nn.Dropout(0.5),
            nn.Linear(64, n_classes)
        )
    
    def forward(self, x_spectral, x_temporal):
        state_repr = self.state_encoder(x_spectral)
        flow_repr = self.flow_encoder(x_temporal)
        
        # Cross-attention coordination
        state_q = state_repr.unsqueeze(1)
        flow_kv = flow_repr.unsqueeze(1)
        
        state_attn, _ = self.coordination(state_q, flow_kv, flow_kv)
        flow_attn, _ = self.coordination(flow_kv, state_q, state_q)
        
        coordinated = torch.cat([
            state_attn.squeeze(1) + state_repr,
            flow_attn.squeeze(1) + flow_repr
        ], dim=-1)
        
        return self.classifier(coordinated)
```

## Key Design Principles

1. **Dual-stream separation**: State and flow capture complementary information
2. **Cross-attention coordination**: Streams inform each other rather than simply concatenating
3. **Residual connections**: Original features preserved through coordination
4. **Spectral-temporal complementarity**: MI tasks have both sustained patterns and transient dynamics

## Applications

- BCI spellers and wheelchair control
- Motor rehabilitation assessment
- Neurofeedback training systems
- Prosthetic control

## Activation Keywords
- staflow, state-flow EEG, MI-EEG decoding, motor imagery EEG, dual-stream EEG
- EEG state representation, EEG temporal dynamics, BCI classification
