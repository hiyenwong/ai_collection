---
name: structured-recurrent-snn-backprop-free
description: "Scalable learning in structured recurrent Spiking Neural Networks without backpropagation. Combines structured multi-layer recurrent SNN architecture with local plasticity mechanisms, WTA teaching signals, and three-factor learning rules for hardware-compatible SNN training. Based on Tang & Xie (2026), arXiv:2605.00402."
---

# Structured Recurrent SNN without Backpropagation

Scalable learning methodology for Spiking Neural Networks (SNNs) using structured recurrence and local plasticity mechanisms, eliminating the need for backpropagation or surrogate gradients. Based on **Tang & Xie (2026)**: *Scalable Learning in Structured Recurrent Spiking Neural Networks without Backpropagation* (arXiv:2605.00402).

## Architecture Design

### Structured Multi-Layer Recurrent SNN

The architecture uses a hybrid connectivity pattern:

1. **Locally Dense Recurrent Layers**: Dense intra-layer connections for local computation and feature extraction
2. **Sparse Small-World Long-Range Projections**: Sparse long-range connections to a readout population, preserving routing efficiency and hardware scalability
3. **Fixed Long-Range Connectivity**: Long-range connections are largely fixed after initialization

### Key Design Principles

- **Hardware Scalability**: Sparse global communication reduces wiring complexity
- **Local Computation**: Synaptic adaptation performed using strictly local plasticity mechanisms
- **Biological Plausibility**: Three-factor learning rules with eligibility traces

## Learning Framework

### Three-Component Learning System

1. **Population-based Winner-Take-All (WTA) Teaching Signals**
   - Applied at the output layer
   - Provides supervised learning signal without gradient computation
   - Competitive activation among output neurons

2. **Fixed Random Broadcast Alignment Feedback Pathways**
   - Random feedback connections aligned with forward paths
   - Enables error signal propagation without backpropagation
   - Fixed after initialization for hardware efficiency

3. **Low-Dimensional Modulatory Neuron Populations**
   - Gate synaptic updates through three-factor learning rules
   - Incorporate eligibility traces for temporal credit assignment
   - Enable deep recurrent computation with sparse global communication

### Three-Factor Learning Rule

```
Δw_ij = η · M · e_ij
```

Where:
- `w_ij`: Synaptic weight between neuron i and j
- `η`: Learning rate
- `M`: Modulatory signal from neuromodulatory neurons
- `e_ij`: Eligibility trace capturing pre-post spike correlations

## Implementation Steps

### Step 1: Network Initialization

```python
import torch

def initialize_structured_snn(n_input, n_hidden, n_output, 
                               local_density=0.3, long_range_density=0.05):
    """Initialize structured recurrent SNN with sparse long-range projections."""
    # Local dense connections
    local_weight = torch.randn(n_hidden, n_hidden)
    local_mask = torch.bernoulli(torch.full_like(local_weight, local_density))
    local_weight = local_weight * local_mask
    
    # Sparse long-range projections to readout
    long_range_weight = torch.randn(n_hidden, n_output)
    lr_mask = torch.bernoulli(torch.full_like(long_range_weight, long_range_density))
    long_range_weight = long_range_weight * lr_mask
    
    # Random feedback alignment
    feedback_weight = torch.randn(n_output, n_hidden)
    
    return {
        'local': local_weight,
        'long_range': long_range_weight, 
        'feedback': feedback_weight
    }
```

### Step 2: Eligibility Trace Computation

```python
def compute_eligibility_trace(pre_spike, post_spike, tau_elig=20.0, dt=1.0):
    """Compute eligibility trace from pre/post spike correlations."""
    # Exponential decay eligibility trace
    e_trace = torch.zeros_like(pre_spike)
    for t in range(pre_spike.shape[0]):
        e_trace[t] = (pre_spike[t] * post_spike[t]) 
        e_trace[t] += torch.exp(-dt/tau_elig) * (e_trace[t-1] if t > 0 else 0)
    return e_trace
```

### Step 3: WTA Teaching Signal

```python
def wta_teaching_signal(output_spikes, target):
    """Generate winner-take-all teaching signal."""
    # Find winner (most active neuron)
    winner = torch.argmax(torch.sum(output_spikes, dim=0))
    
    # Create teaching signal
    teaching = torch.zeros_like(output_spikes[0])
    teaching[target] = 1.0  # Target neuron gets positive signal
    teaching[winner] = -0.1 if winner != target else 0.0  # Winner suppression
    
    return teaching
```

### Step 4: Modulatory Gating

```python
def modulatory_update(weights, eligibility, teaching, modulatory_neuron, lr=0.01):
    """Apply three-factor learning rule with modulatory gating."""
    modulatory_signal = torch.sigmoid(modulatory_neuron)
    delta_w = lr * modulatory_signal * torch.outer(teaching, eligibility)
    return weights + delta_w
```

## Hardware Feasibility

### Computational Complexity

- **Space Complexity**: O(N²·d_local + N·d_long_range) for N neurons
- **Time Complexity**: O(N·d_local) per timestep for local updates
- **Communication Overhead**: Sparse long-range projections minimize wiring

### Hardware Mapping

1. **Local Processing Elements (PEs)**: Each dense layer mapped to a PE cluster
2. **Sparse Interconnect**: Small-world routing using NoC (Network-on-Chip)
3. **Modulatory Bus**: Shared global modulatory signal distribution

## Related Skills

- **spiking-neural-network-analysis**: General SNN analysis methodology
- **snn-learning-survey**: Comprehensive SNN learning algorithm taxonomy
- **three-factor-snn-learning**: Three-factor learning rules for SNNs
- **spikingjelly-framework**: SNN deep learning framework

## Paper Reference

- **Title**: Scalable Learning in Structured Recurrent Spiking Neural Networks without Backpropagation
- **Authors**: Bo Tang, Weiwei Xie
- **arXiv**: 2605.00402 [cs.NE, cs.AI, cs.LG]
- **Date**: May 2026
- **Pages**: 7 pages, 2 figures
