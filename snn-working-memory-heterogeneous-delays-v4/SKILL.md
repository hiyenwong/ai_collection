---
name: snn-working-memory-heterogeneous-delays-v4
description: Recurrent SNN with heterogeneous synaptic delays for working memory. Weight tensor W∈R^{N×N×D} with D=41 delays per synapse, trained via surrogate gradient BPTT. Spiking Motifs concept achieves F1=1.0 on M=16 patterns with N=512 neurons.
version: 1.1
authors:
  - Laurent U Perrinet
paper: arXiv:2604.14096
date: 2026-04-15
tags:
  - spiking-neural-network
  - working-memory
  - synaptic-delays
  - recurrent-network
  - surrogate-gradient
  - BPTT
  - spiking-motifs
  - temporal-pattern
category: ai_collection
---

# Working Memory in Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays

## Summary

This work demonstrates that **heterogeneous synaptic delays** are sufficient to implement robust working memory in recurrent spiking neural networks. By treating each synapse as a weight tensor W∈R^{N×N×D} with D=41 delay channels, the network learns to store and retrieve temporal patterns ("Spiking Motifs") through surrogate gradient backpropagation through time (BPTT). The result is **perfect recall (F1=1.0)** of M=16 distinct patterns with N=512 neurons.

**Key Innovation**: The "Spiking Motif" concept — each stored pattern is a unique spatiotemporal spike pattern that persists through delay-induced reverberations in the recurrent network.

## Key Contributions

1. **Delay Tensor Formulation**: Each synaptic connection has a full weight tensor across D delays, not a scalar weight. This enables the network to learn precise temporal routing.

2. **Spiking Motifs**: Each stored memory is a unique spatiotemporal spike pattern that self-sustains through the delay structure. This is the SNN analog of attractor states in rate networks.

3. **Surrogate Gradient BPTT**: Training uses differentiable surrogate gradients for the spike function, enabling credit assignment across the full delay structure.

4. **Perfect Recall**: F1=1.0 on M=16 patterns — zero errors in both storage and retrieval.

5. **Biologically Plausible Scale**: N=512 neurons is within the range of cortical microcolumns, suggesting biological feasibility.

## Technical Approach

### Network Architecture

```
Input → [Recurrent SNN Layer] → Readout
         N=512 neurons
         Weight: W ∈ R^{N×N×D}
         D=41 delays per synapse
         T=1000 time steps
```

### Neuron Model: Leaky Integrate-and-Fire

$$\tau_m \frac{dV_i}{dt} = -V_i + \sum_{j=1}^{N} \sum_{d=1}^{D} W_{ijd} \cdot S_j(t-d) + I_i^{ext}(t)$$

$$S_i(t) = \begin{cases} 1 & \text{if } V_i(t) \geq \vartheta \\ 0 & \text{otherwise} \end{cases}$$

$$V_i(t^+) = V_{reset} \quad \text{after spike}$$

### Heterogeneous Delay Tensor

The key departure from standard SNN models: instead of a single weight per synapse, each connection has a full delay profile:

$$W_{ij} = [W_{ij,1}, W_{ij,2}, \ldots, W_{ij,D}]$$

- **D = 41 delay channels**: covering temporal windows from 1 to 41 time steps
- **Total parameters**: N × N × D = 512 × 512 × 41 ≈ 10.7M parameters
- **Sparsity**: ~90% of weights are zero after training

### Spiking Motifs Concept

A Spiking Motif μ is defined as:
$$\mu = \{(i, t) : S_i(t) = 1 \text{ for pattern } \mu\}$$

Each motif is a unique spatiotemporal pattern of spikes across the N neurons and T time steps. The network stores M=16 such motifs.

**Storage mechanism**: When a motif is presented, it creates a unique pattern of activation across the delay tensor that reverberates sustainably.

**Retrieval mechanism**: A partial cue triggers the delay network to complete the full motif through pattern completion.

### Training: Surrogate Gradient BPTT

The non-differentiable spike function is handled with a smooth surrogate:

$$\frac{\partial S_i}{\partial V_i} \approx \frac{1}{\pi} \cdot \frac{\sigma}{(V_i - \vartheta)^2 + \sigma^2}$$

Where σ controls the sharpness of the surrogate (typically σ=0.5).

**BPTT over delays**: Gradients must flow through D=41 time steps of delay, making the effective temporal horizon T+D steps long.

### Training Protocol

1. **Phase 1 — Pattern Encoding**: Present each of M=16 patterns as input current for T_encode steps
2. **Phase 2 — Maintenance**: Remove input, let recurrent dynamics sustain the pattern for T_maintain steps
3. **Phase 3 — Recall**: Present partial cue (20% of pattern), measure completion quality
4. **Loss**: Binary cross-entropy between recalled spikes and target pattern

```python
# Pseudocode for training
for epoch in range(num_epochs):
    for motif_id in range(M):  # M=16 patterns
        # Encode phase
        I_ext = pattern_input[motif_id]
        for t in range(T_encode):
            spikes = forward(V, I_ext, W)
            
        # Maintain phase (no external input)
        I_ext = 0
        for t in range(T_maintain):
            spikes = forward(V, 0, W)
            # Accumulate loss against target motif
            loss += BCE(spikes, target[motif_id])
        
        # Recall phase (partial cue)
        I_ext = partial_cue[motif_id]  # 20% of pattern
        for t in range(T_recall):
            spikes = forward(V, I_ext, W)
            loss += BCE(spikes, target[motif_id])
        
        # BPTT through all phases
        loss.backward()
        optimizer.step()
```

## Experimental Configuration

| Parameter | Value |
|-----------|-------|
| Neurons (N) | 512 |
| Delays (D) | 41 |
| Patterns (M) | 16 |
| Time steps (T) | 1000 |
| Surrogate σ | 0.5 |
| τ_m (membrane time const) | 20 ms |
| Learning rate | 1e-3 |
| Optimizer | Adam |
| Training epochs | 500 |

### Results

| Metric | Value |
|--------|-------|
| F1 Score (storage) | 1.000 |
| F1 Score (recall from cue) | 1.000 |
| Pattern capacity (M_max) | ~32 for N=512 |
| Maintenance duration | >5000 steps |
| Cue fraction needed | 20% |

## Implementation Considerations

### Memory Optimization
The weight tensor W∈R^{512×512×41} is large (~10.7M params). In practice:
- **Structured sparsity**: Enforce sparsity during training (L1 regularization)
- **Low-rank decomposition**: W_{ijd} ≈ U_{id} × V_{jd} reduces to O(N×D)
- **Block structure**: Delays can be shared within neuron groups

### Delay Buffer Implementation
```python
class DelayBuffer:
    def __init__(self, N, D):
        self.buffer = torch.zeros(D, N)  # [delay, neuron]
        self.D = D
    
    def push(self, spikes):
        """Add new spikes, shift buffer"""
        self.buffer = torch.roll(self.buffer, 1, dims=0)
        self.buffer[0] = spikes
        return self.buffer  # [D, N] — all delayed spike histories
```

### Forward Pass with Delay Tensor
```python
def forward(V, I_ext, W, delay_buffer):
    # Get delayed spikes
    delayed_spikes = delay_buffer.buffer  # [D, N]
    
    # Synaptic current: sum over pre-synaptic neurons and delays
    I_syn = torch.einsum('ijk,jk->i', W, delayed_spikes)  # [N]
    
    # Membrane update (Euler method)
    V = V + (-V + I_syn + I_ext) / tau_m
    
    # Spike generation (surrogate gradient)
    spikes = (V >= threshold).float()
    
    # Reset
    V = V * (1 - spikes) + V_reset * spikes
    
    # Update delay buffer
    delay_buffer.push(spikes)
    
    return spikes, V
```

## Comparison with Previous Work

| Method | Delays | F1 Score | Capacity | Bio Plausible? |
|--------|--------|----------|----------|---------------|
| **This work (v4)** | **Heterogeneous D=41** | **1.000** | **M=16** | **Partial** |
| v3 (homogeneous) | Single d | 0.92 | M=8 | Partial |
| v2 (fixed delays) | Fixed D=10 | 0.85 | M=4 | More |
| v1 (no delays) | None | 0.71 | M=2 | Most |

## Relevance

This work provides a concrete mechanism for how **heterogeneous synaptic delays** could implement working memory in biological neural circuits. The Spiking Motif concept offers a new framework for understanding memory representations in spiking networks.

Applications:
- **Neuromorphic working memory chips**: Delay-based memory without RAM
- **Brain-inspired computing**: Understanding cortical microcolumn dynamics
- **Temporal sequence processing**: Speech, music, motor control

## Triggers (激活词)

working memory, heterogeneous delays, spiking motifs, recurrent SNN, surrogate gradient, BPTT, delay tensor, temporal pattern storage, pattern completion, attractor dynamics, synaptic delay, neuromorphic memory, cortical microcolumn
