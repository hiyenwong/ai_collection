---
name: adaptive-spiking-transformer-energy-efficiency
description: "Energy-efficient Spiking Transformer using attention-driven sparse spike propagation. Reduces FLOPs 87.7-97.5% vs dense Transformers by replacing softmax with temporal spike coding. Activation: spiking transformer, energy-efficient vision, spike-based attention, SNN ViT, neuromorphic deep learning, adaptive threshold"
version: 1.0.0
metadata:
  hermes:
    tags: [spiking-neural-networks, transformers, energy-efficiency, neuromorphic]
    source_paper: "arXiv:2503.11234"
---

# Energy-efficient Spiking Transformer with Adaptive Attention

## Overview

Replaces dense softmax attention with sparse, event-driven spike-based attention in Transformers. Spikes propagate through attention layers only when membrane potentials exceed adaptive thresholds, achieving 87.7-97.5% FLOPs reduction vs dense Transformers while maintaining competitive accuracy.

## Core Concepts

### Spike-based Attention

```python
import torch, torch.nn as nn

class SpikingAttention(nn.Module):
    def __init__(self, dim, num_heads=8, tau=4.0, threshold=1.0):
        super().__init__()
        self.num_heads, self.tau, self.threshold = num_heads, tau, threshold
        self.q_proj = nn.Linear(dim, dim)
        self.k_proj = nn.Linear(dim, dim)
        self.v_proj = nn.Linear(dim, dim)
        self.out_proj = nn.Linear(dim, dim)

    def forward(self, x, time_steps=10):
        B, N, C = x.shape
        u_q = u_k = u_v = torch.zeros(B, N, C, device=x.device)
        sq, sk, sv = [], [], []
        for t in range(time_steps):
            u_q = u_q * torch.exp(-1/self.tau) + self.q_proj(x)
            u_k = u_k * torch.exp(-1/self.tau) + self.k_proj(x)
            u_v = u_v * torch.exp(-1/self.tau) + self.v_proj(x)
            sp_q = (u_q >= self.threshold).float()
            sp_k = (u_k >= self.threshold).float()
            sp_v = (u_v >= self.threshold).float()
            u_q = u_q * (1 - sp_q) + 0.5 * sp_q
            u_k = u_k * (1 - sp_k) + 0.5 * sp_k
            u_v = u_v * (1 - sp_v) + 0.5 * sp_v
            sq.append(sp_q); sk.append(sp_k); sv.append(sp_v)
        q = torch.stack(sq).sum(0) / time_steps
        k = torch.stack(sk).sum(0) / time_steps
        v = torch.stack(sv).sum(0) / time_steps
        d = C // self.num_heads
        q = q.reshape(B, N, self.num_heads, d)
        k = k.reshape(B, N, self.num_heads, d)
        v = v.reshape(B, N, self.num_heads, d)
        attn = torch.einsum('bhid,bhjd->bhij', q, k) / (d ** 0.5)
        attn = attn.softmax(dim=-1) * (attn != 0).float()
        out = torch.einsum('bhij,bhjd->bhid', attn, v).reshape(B, N, C)
        return self.out_proj(out)
```

## Implementation Steps

1. Encode images to spike trains via intensity-to-latency encoding
2. Convolutional patch embedding (analog first layer)
3. Replace softmax attention with spike-based sparse attention
4. Replace ReLU/GeLU with LIF spiking neurons in MLP
5. Use adaptive thresholds to maintain 5-15% spike rates
6. Train with surrogate gradient (straight-through estimator)

## Pitfalls

1. Surrogate gradient: use sigmoid/arctan for Heaviside derivative
2. Time steps: 4-10 typical; more = accuracy, less = latency
3. First layer stays analog; fully spiking ViT loses accuracy
4. Threshold init: too high = dead neurons, too low = no sparsity
5. Adding recurrence improves performance

## References

- arXiv:2503.11234
- Related: wta-spiking-transformer-language, gemst-multidimensional-grouping-snn

## Activation Keywords

- spiking transformer, energy-efficient vision transformer, spike-based attention, SNN ViT, neuromorphic deep learning, adaptive threshold SNN, temporal spike coding
