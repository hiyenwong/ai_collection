---
name: self-supervised-local-learning-rhm
description: "Self-supervised local learning rules that discover hidden hierarchical structure in high-dimensional data. Demonstrates that layerwise self-supervised (contrastive/non-contrastive) losses match backpropagation data efficiency while being biologically plausible. Applicable to: biologically plausible learning, SNN training without backprop, cortical plasticity rules. Activation: self-supervised local learning, random hierarchy model, biologically plausible backprop, layerwise contrastive learning."
---

# Self-Supervised Local Learning on the Random Hierarchy Model

Based on: Delrocq, Wu, Bellec, Gerstner (2026) — arXiv:2605.18557

## Core Insight

Biologically plausible **self-supervised local learning rules** can discover the hidden hierarchical structure of high-dimensional data with the **same data efficiency as supervised backpropagation**, while being compatible with known cortical synaptic plasticity rules.

## Key Findings

- **Direct feedback rules FAIL**: Approximating error propagation from output layer fails on RHM tasks
- **Layerwise self-supervised rules SUCCEED**: Contrastive and non-contrastive losses learn the hierarchical structure
- **Equal data efficiency**: Self-supervised local rules match supervised backprop in sample efficiency
- **Failure mechanism**: Direct feedback misses input-specific nonlinearities ("masking") essential for complex tasks
- **Cortical compatibility**: All successful rules map to known synaptic plasticity mechanisms

## Random Hierarchy Model (RHM)

The RHM generates data with known latent hierarchical structure:
- Features organized in nested groups
- Ground-truth hierarchy is known (enables evaluation)
- Designed to study how networks learn abstract representations

## Two Types of Local Learning Rules

### Type 1: Direct Feedback (FAILS)
- Uses feedback connections to approximate error signals from output layer
- Attempts to mimic backpropagation's error propagation
- **Fails because**: misses input-specific nonlinearities ("masking") implemented in full backprop
- The masking is **essential** for learning complex hierarchical tasks

### Type 2: Layerwise Self-Supervised (SUCCEEDS)
- Each layer learns via self-supervised objectives
- **Contrastive**: InfoNCE-style losses comparing positive/negative pairs
- **Non-contrastive**: VICReg, Barlow Twins-style redundancy reduction
- No explicit error approximation needed
- **Succeeds because**: discovers hierarchical structure through data geometry

## Implementation Pattern

```python
import torch
import torch.nn as nn

class LocalLearningNetwork(nn.Module):
    def __init__(self, layers, hidden_dims):
        super().__init__()
        self.layers = nn.ModuleList([
            nn.Linear(d_in, d_out) 
            for d_in, d_out in zip(hidden_dims[:-1], hidden_dims[1:])
        ])
    
    def forward_encoder(self, x):
        # Feedforward encoding through all layers
        activations = []
        h = x
        for layer in self.layers:
            h = layer(h)
            h = torch.relu(h)
            activations.append(h)
        return activations
    
    def layerwise_loss(self, activations):
        # Self-supervised loss at each layer
        total_loss = 0
        for i, act in enumerate(activations):
            # Contrastive loss (e.g., InfoNCE)
            # or non-contrastive (e.g., VICReg)
            loss = self.self_supervised_loss(act)
            total_loss += loss
        return total_loss
    
    def self_supervised_loss(self, act):
        # Implement contrastive or non-contrastive loss
        # VICReg-style: variance + invariance + covariance
        # or InfoNCE-style: positive vs negative pairs
        pass
```

## Why This Matters

- **Biological plausibility**: No symmetric error network needed (solves weight transport problem)
- **No long convergence**: Unlike some biologically plausible algorithms, these converge efficiently
- **Same data efficiency**: No trade-off in sample complexity vs. backpropagation
- **Cortical compatibility**: Maps to known Hebbian/STDP mechanisms

## Pitfalls

- **Not all local rules work**: Direct feedback approximations specifically fail on hierarchical tasks
- **RHM is synthetic**: Results on artificial dataset; need validation on real-world data
- **Contrastive vs non-contrastive**: Both work but may differ in convergence speed and stability

## Related Skills
- `meta-learning-biological-plasticity`
- `snn-learning-survey`
- `feedback-hebbian-continual-learning`

## arXiv
- https://arxiv.org/abs/2605.18557
