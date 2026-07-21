---
name: dendri-cl-single-layer-snn
description: >
  DendriCL methodology for dendritic in-context learning in single-layer
  compartmental spiking neural networks. Proves that apical dendritic
  subthreshold dynamics implement online leaky LMS, collapsing ICL
  architectural depth to one layer with frozen inference weights.
---

# Dendritic In-Context Learning in Single-Layer SNNs (DendriCL)

## Paper

**Title**: Dendritic In-Context Learning in a Single-Layer Spiking Neural Network  
**Authors**: Juwei Shen, Yujie Wu, Changwen Chen  
**arXiv**: 2607.02283v1 (2026-07-02)  
**Link**: https://arxiv.org/abs/2607.02283

## Core Insight

In-context learning (ICL) — the ability to solve a new task from a few labeled
examples in a forward pass without weight updates — has been demonstrated in
Transformers, Mamba, SSMs, and MLPs but never in SNNs on the standard Garg-2022
benchmark. Prior SNNs fail because they route adaptation through inference-time
synaptic plasticity and treat dendritic compartments as passive conduits.

**DendriCL** reverses this: the apical dendritic compartment's subthreshold
dynamics structurally implement leaky online Widrow-Hoff LMS:

```
u_A(t+1) = α·u_A(t) + γ·(y_t - ŷ_t)·W_A·x_t
```

With all synaptic weights frozen at inference, the apical membrane itself is
the learning algorithm substrate, not a conduit for it.

## Architecture

A single layer of compartmental spiking neurons with three compartments:

1. **Basal dendrite** — receives bottom-up input x_t via frozen W_B
2. **Apical dendrite** — recurrent state vector u_A updated by leaky LMS
3. **Soma** — integrates basal + apical, generates spikes

Key equations:

```
u_B(t) = W_B · x_t                                    # Basal input
u_A(t+1) = α·u_A(t) + γ·(y_t - ŷ_t)·W_A·x_t          # Apical LMS update
u_soma(t) = u_B(t) + W_out · u_A(t)                    # Somatic integration
spike(t) = u_soma(t) > threshold                        # Spike generation
ŷ(t) = W_out · spike_history(t)                         # Prediction
```

**All weights (W_A, W_B, W_out) are frozen at inference.** The apical state
u_A persists across the full context and is NOT reset by spikes.

## Training

- End-to-end BPTT on synthetic ICL tasks (Garg-2022 protocol)
- Training discovers the LMS parameters (α, γ, W_A, W_B) autonomously
- The LMS structure emerges from dynamics, not hard-coded architecture
- Width ablation shows d_apical ≈ 2× task dimension is optimal

## Key Results

| Metric | DendriCL | Spikformer | Pure LIF |
|--------|----------|-----------|----------|
| R² at d=10 | 0.95 | 0.85 | 0.34 |
| R² at d=20 | 0.93 | 0.72 | 0.09 |
| R² at d=30 | 0.90 | 0.15 | ~0 |
| R² at d=40 | 0.87 | ~0 | ~0 |
| R² at d=50 | 0.83 | ~0 | ~0 |

- **Only architecture seed-stable at d ≥ 30** (Transformers show grokking-style
  bimodal failure)
- **Linear probe recovers LMS trajectory at R² = 0.93** — algorithm is
  structurally embedded in dynamics
- **~4× spike reduction** over Pure LIF at same accuracy
- **Projected ~10× Loihi-class energy advantage**

## Biological Grounding

Maps to layer-5 cortical pyramidal neuron:
- Apical tuft: top-down feedback integration
- Basal dendrites: bottom-up sensory input  
- Soma: integration point
- Calcium plateaus on 100+ ms timescales provide persistent multi-dimensional
  subthreshold state — exactly the missing substrate for ICL in standard LIF

## When to Use

- **Implement ICL on neuromorphic hardware** (Loihi, SpiNNaker, TrueNorth)
- **Single-layer spiking architecture** for online learning tasks
- **Energy-efficient inference** with frozen weights
- **Biologically plausible learning** without backprop at inference
- **High-dimensional function approximation** (d=5 to d=50+)

## Implementation

```python
import torch
import torch.nn as nn

class DendriCLNeuron(nn.Module):
    """Single compartmental spiking neuron with apical LMS dynamics."""
    
    def __init__(self, d_in, d_apical, alpha=0.95, gamma=0.1, threshold=1.0):
        super().__init__()
        self.d_in = d_in
        self.d_apical = d_apical
        self.threshold = threshold
        
        # Frozen at inference, trained by BPTT
        self.W_A = nn.Parameter(torch.randn(d_apical, d_in) * 0.1)
        self.W_B = nn.Parameter(torch.randn(d_apical, d_in) * 0.1)
        self.W_out = nn.Parameter(torch.randn(1, d_apical) * 0.1)
        
        # Learnable LMS parameters
        self.alpha = nn.Parameter(torch.tensor(alpha))
        self.gamma = nn.Parameter(torch.tensor(gamma))
    
    def forward(self, x_seq, y_seq):
        """Process sequence of (input, target) pairs.
        
        Args:
            x_seq: (seq_len, d_in) input sequence
            y_seq: (seq_len, 1) target sequence
            
        Returns:
            predictions: (seq_len, 1) predictions for each timestep
        """
        seq_len = x_seq.shape[0]
        u_A = torch.zeros(self.d_apical)  # Persistent apical state
        predictions = []
        
        for t in range(seq_len):
            # Basal input
            u_B = self.W_B @ x_seq[t]
            
            # Somatic prediction
            u_soma = u_B + self.W_out @ u_A
            y_hat = u_soma  # Linear readout
            
            # Spike generation
            spike = (u_soma > self.threshold).float()
            
            # Apical LMS update
            error = y_seq[t] - y_hat
            u_A = self.alpha * u_A + self.gamma * error * (self.W_A @ x_seq[t])
            
            predictions.append(y_hat)
        
        return torch.stack(predictions)
```

## Trigger Words

dendri-cl, dendritic ICL, single-layer SNN in-context learning, apical LMS,
compartmental spiking neuron, Garg-2022 SNN, online Widrow-Hoff spiking,
frozen-weight SNN learning, biological ICL, Loihi in-context learning
