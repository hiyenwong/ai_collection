---
name: working-memory-heterogeneous-delays-v3
description: Working memory implementation in recurrent spiking neural networks with heterogeneous synaptic delays (HD-SNN). Extends polychronous neuronal groups to a trainable, recurrent framework using surrogate-gradient BPTT. Enables energy-efficient neuromorphic edge deployment for temporal pattern storage and recall. Based on Perrinet (2026) "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays".
tags: [snn, working-memory, heterogeneous-delays, spiking-motifs, polychronization, surrogate-gradient, neuromorphic]
date: 2026-04-18
source: "arXiv:2604.14096"
---

# Working Memory in Recurrent HD-SNN with Heterogeneous Delays

## Core Concept

A recurrent Spiking Neural Network (SNN) where each synapse has **multiple delay channels** (D=41 delays), trained end-to-end with surrogate-gradient backpropagation through time (BPTT). The network stores arbitrary target spike patterns as chains of overlapping **Spiking Motifs** — contiguous windows of length D that uniquely predict spikes at the next time step.

This extends Izhikevich's polychronous neuronal groups (PNGs) from fixed delays + STDP to **learned delays + gradient descent**, bridging computational neuroscience with machine learning for neuromorphic deployment.

## Key Innovation

**Heterogeneous delays as computational asset**: Instead of treating axonal delay variation as biological nuisance, the network exploits it to create a large context window. Each synapse contacts its target through D different delay channels, allowing spikes from different presynaptic neurons at different times to converge synchronously on the postsynaptic neuron.

## Architecture

```
N neurons (N=512 LIF neurons)
D delay channels per synapse (D=41, max delay in ms)
Weight tensor: W ∈ R^(N×N×D) ≈ 2.7M parameters
Membrane: u_j(t) = β·u_j(t-1)·(1-s_j(t-1)) + Σ_i Σ_d W_{j,i,d}·s_i(t-d)
β = 0.8 (τ ≈ 4.5ms), threshold ϑ = 1
```

### Spiking Motif Detection

A Spiking Motif is a pattern where N presynaptic spikes, emitted at staggered times with specific inter-spike intervals, arrive synchronously at a postsynaptic neuron through heterogeneous delay channels. The output spike then re-enters the network as new input, creating a **chain of temporal predictions** — implementing working memory.

## Training Pipeline

### 1. Analytical Weight Initialization (Hebbian)
```python
# Closed-form Hebbian initialization via Moore-Penrose pseudo-inverse
# W* = S* C⁺ where C=context windows, S*=target spikes
# For sparse activity (p_A ≈ 10⁻³), Gram matrix CC^T ≈ N·D·p_A·I
# Simplifies to: w_ij^(d) ∝ Σ_μ Σ_t s_j*^(μ)(t) · s_i*^(μ)(t-d)
```
This is mathematically equivalent to averaging STDP updates across all stored patterns.

### 2. Surrogate-Gradient BPTT
```python
Loss = 1 - F1_score  # Harmonic mean of precision and recall
Surrogate: fast-sigmoid, α = 15
Optimizer: SGD (lr=1e-3, momentum=0.99, weight_decay=0)
Dropout: 0.37
LR schedule: cosine annealing with warmup
Epochs: 16 (~4096 gradient steps, ~10 min on M3 Ultra)
```

### 3. Memory Cueing
Clamp all neuron activities to target pattern during first D time steps, then let network generate remainder autonomously.

## Implementation (snnTorch + PyTorch)

```python
import torch
import snntorch as snn
from snntorch import surrogate

class RecurrentHDSNN(torch.nn.Module):
    def __init__(self, N=512, D=41, beta=0.8, threshold=1.0):
        super().__init__()
        self.N, self.D, self.beta = N, D, threshold
        # Weight tensor: N x (N*D) — flattened delay dimension
        self.W = torch.nn.Parameter(torch.randn(N, N*D) * 0.01)
        self.lif = snn.Leaky(beta=beta, threshold=threshold, 
                             spike_grad=surrogate.fast_sigmoid(alpha=15))
        
    def forward(self, spike_history, mem):
        # spike_history: (N, D) — past D steps of all neurons
        context = spike_history.flatten()  # (N*D,)
        cur = torch.matmul(self.W, context)
        spk, mem = self.lif(cur, mem)
        return spk, mem
```

## Key Hyperparameters & Capacity Analysis

| Parameter | Default | Effect |
|-----------|---------|--------|
| N (neurons) | 512 | Capacity ∝ N²×D |
| D (delays) | 41 | Primary capacity lever; larger D → lower loss |
| T (duration) | 1000 steps | Loss grows monotonically with T |
| p_A (firing rate) | 2 Hz | Optimal at p_A ≲ 10⁻³; degrades sharply above |
| β (decay) | 0.8 | τ = 1/ln(1/β) ≈ 4.5ms |

### Capacity Relationship
- **Loss ∝ 1/(N × D × p_A)**: delay depth is primary capacity lever
- **Loss grows with T**: compounding errors through open-loop rollout
- Context orthogonality requires N × D × p_A ≫ 1

## Results Summary

- **F1 = 1.0** on M=16 patterns (N=512, T=1000, D=41)
- Recall emerges near clamped window and propagates forward in time
- Loss drops from 0.85 (D=3) to ~0 (D=127)
- Loss grows from 0.004 (T=64) to 0.08 (T=2048)
- Optimal performance at p_A = 10⁻⁴ to 10⁻³

## Failure Modes

1. **Complete silence**: network emits no spikes (low recall)
2. **Over-activation**: nearly all neurons fire every step (low precision)
3. **Error compounding**: early prediction errors propagate through sequence

F1 loss penalizes both modes symmetrically; cosine LR schedule guides away from extremes.

## Extensions & Future Work

1. **Self-supervised learning**: Replace supervised F1 loss with contrastive predictive coding on raw multi-electrode data
2. **Richer neuron models**: Adaptive threshold dynamics for increased timescale diversity
3. **Latent reservoir neurons**: Partition into input/output + reservoir pool
4. **Neuromorphic hardware deployment**: Loihi 2, Intel Pohoiki for edge applications
5. **Capacity analysis**: Systematic evaluation of M patterns × duration × interference

## Related Skills

- `snn-working-memory-heterogeneous-delays-v2`: Earlier version
- `spiking-neural-network-analysis`: General SNN paper analysis
- `heterogeneous-synaptic-dynamics`: Synaptic dynamics modeling
- `polychronization`: Izhikevich's original PNG framework
- `decolle-snn-learning`: Local learning rules for SNNs

## References

- Perrinet, L.U. (2026). "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays." arXiv:2604.14096.
- Izhikevich, E.M. (2006). "Polychronization: Computation with Spikes." Neural Computation, 18(2):245-282.
- Kronland-Martinet et al. (2025). "Detection of spiking motifs of arbitrary length..." arXiv:2511.15296.
- Hammouamri et al. (2023). "Learning Delays in Spiking Neural Networks using Dilated Convolutions..." arXiv:2306.17670.
- Grimaldi & Perrinet (2023). "Learning heterogeneous delays in a layer of spiking neurons..." Biological Cybernetics.
