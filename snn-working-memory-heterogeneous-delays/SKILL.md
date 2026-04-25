---
name: snn-working-memory-heterogeneous-delays
description: "Working memory in recurrent spiking neural networks using heterogeneous synaptic delays (arXiv:2604.14096). Recurrent SNN with N neurons, D=41 delays per synapse, weight tensor W in R^{N×N×D} trained with surrogate-gradient BPTT. M patterns stored as fixed-point attractors via Spiking Motifs — overlapping temporal windows that predict next-step spikes. Achieves perfect recall (F1=1.0) on synthetic benchmarks. Activation: working memory SNN, heterogeneous delays, spiking motifs, surrogate gradient BPTT, delay-based memory, temporal pattern storage, recurrent SNN memory, neuromorphic memory."
version: 2.0.0
metadata:
  hermes:
    source_paper: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays"
    arxiv_id: "2604.14096"
    published: "2026-04-15"
    authors: "Laurent U Perrinet"
    categories: ["cs.NE", "q-bio.NC", "cs.AI"]
---

# Working Memory in Recurrent SNNs With Heterogeneous Synaptic Delays

## Overview

Working memory — the ability to store and recall precise sequences of events — is implemented in a recurrent spiking neural network (SNN) using **heterogeneous synaptic delays**. Each synapse is equipped with **D=41 distinct delay channels**, forming a weight tensor **W ∈ R^{N×N×D}**. The network stores **M arbitrary target spike patterns** by representing each as a sequential chain of overlapping **Spiking Motifs**: contiguous windows of length D that uniquely predict spikes at the next time step. Training with surrogate-gradient backpropagation through time (BPTT) achieves **perfect recall (F1=1.0)** on synthetic benchmarks.

**Key innovation:** Heterogeneous delays alone are sufficient for working memory — no bistability, attractor dynamics, external gating, or continuous stimulation needed.

**Paper:** Laurent U Perrinet, *"Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays"*, arXiv:2604.14096, April 2026.

## Network Architecture

### Core Parameters

| Parameter | Symbol | Typical Value | Description |
|-----------|--------|---------------|-------------|
| Number of neurons | N | 512 | Recurrent SNN population size |
| Number of delays | D | 41 | Delay channels per synapse |
| Weight tensor | W ∈ R^{N×N×D} | 512×512×41 | ~10.7M trainable parameters |
| Stored patterns | M | 16 | Number of memorized spike sequences |
| Sequence length | T | 1000 | Time steps per pattern |
| Neuron model | — | LIF | Leaky integrate-and-fire |

### Weight Tensor Structure

The weight tensor W ∈ R^{N×N×D} indexes as:
- **W[i, j, d]**: synaptic weight from presynaptic neuron j to postsynaptic neuron i with delay d+1 (delays 1 through D)

Each neuron pair (i, j) has **D=41 separate weight values**, each corresponding to a different transmission delay. This creates a distributed temporal memory buffer where past spike activity persists across multiple timescales.

### Neuron Model

Leaky integrate-and-fire (LIF) dynamics with heterogeneous delay inputs:

```
V_i(t) = α · V_i(t-1) + Σ_j Σ_d W[i,j,d] · S_j(t-d) + I_ext_i(t)

S_i(t) = H(V_i(t) - θ)   (spike if threshold exceeded)

V_i(t) → V_i(t) · (1 - S_i(t))   (reset after spike)
```

Where:
- V_i(t): membrane potential of neuron i at time t
- α: membrane decay constant (typically 0.9–0.99)
- S_j(t-d): spike of neuron j at delayed time t-d
- θ: firing threshold (typically 1.0)
- H(·): Heaviside step function
- I_ext_i(t): external input current

### Spiking Motifs

A **Spiking Motif** is a contiguous window of spike activity of length D across all N neurons:

- Shape: (N, D) = (512, 41) per motif
- Each target pattern decomposes into a sequential chain of **overlapping Spiking Motifs**
- Given the motif at time steps [t-D+1, t], the network **predicts spikes at t+1**
- This creates an **autoregressive structure**: current activity window → next-step prediction
- Overlap between consecutive motifs ensures continuity

## Training Method

### Surrogate-Gradient Backpropagation Through Time (BPTT)

Since spike generation uses a non-differentiable threshold function H(·), the method employs **surrogate gradients**:

1. **Forward pass**: Simulate LIF dynamics with full delay tensor over T time steps
2. **Surrogate gradient**: Replace H'(·) with a smooth approximation:
   ```
   σ'(x) ≈ β / (1 + π·β·x)²    (fast sigmoid surrogate)
   # or
   σ'(x) ≈ 1 / (1 + (β·x)²)    (atan surrogate)
   ```
   where β controls the gradient sharpness (typically 5–20)
3. **Backward pass**: Gradients flow through all D=41 delay channels and T=1000 time steps
4. **End-to-end optimization**: Entire weight tensor W optimized jointly with Adam optimizer

### Training Protocol

1. **Pattern generation**: Generate M=16 random binary spike patterns of shape (N, T)
2. **Clamped initialization**: At recall time, teacher-force the network on an initial window of D time steps
3. **Free recall**: After initialization, the network runs autonomously from recurrent dynamics
4. **Loss function**: Binary cross-entropy between predicted and target spikes
5. **Evaluation**: F1 score per-pattern between recalled and target spike trains

### Hyperparameters

| Hyperparameter | Value | Notes |
|---------------|-------|-------|
| Learning rate | 1e-3 to 1e-4 | Adam optimizer |
| Surrogate gradient β | 5–20 | Gradient sharpness |
| Neuron threshold θ | 1.0 | LIF spike threshold |
| Membrane decay α | 0.9–0.99 | Leak time constant |
| Clamped window | D=41 steps | Teacher-forced initialization |
| Training epochs | 100–500 | Until F1 ≈ 1.0 |

## Key Results

### Performance on Synthetic Benchmarks

- **Mean F1 score: 1.0** (perfect recall) after convergence
- **Recall propagation**: Correct recall starts at clamped window and spreads forward temporally
- **Pattern capacity**: M=16 patterns stored simultaneously with N=512 neurons, D=41 delays

### Key Findings

1. **Delays alone suffice**: No additional mechanisms (bistability, attractors, external gating) needed — heterogeneous delays provide sufficient substrate for working memory
2. **Spiking Motifs are the memory unit**: Patterns stored as chains of overlapping temporal windows, each predicting the next step
3. **End-to-end learning**: Network discovers delay-based memory encoding purely from gradient optimization
4. **Scalable architecture**: Weight tensor formulation straightforward to scale by increasing N, D, or both
5. **Temporal coding emerges naturally**: Not imposed by design but discovered through training

### Biological Significance

- Axonal conduction delays in cortex vary from milliseconds to hundreds of milliseconds
- The model shows this biological feature can be harnessed for working memory
- Temporal coding schemes emerge naturally from training rather than being hand-crafted

## Implementation Guide

### Step 1: Network Definition

```python
import torch
import torch.nn as nn

class HeterogeneousDelaySNN(nn.Module):
    """Recurrent SNN with heterogeneous synaptic delays for working memory."""

    def __init__(self, n_neurons=512, n_delays=41, threshold=1.0, decay=0.95):
        super().__init__()
        self.N = n_neurons
        self.D = n_delays
        self.threshold = threshold
        self.decay = decay

        # Weight tensor: W[i, j, d] = weight from j to i with delay d+1
        self.W = nn.Parameter(
            torch.randn(n_neurons, n_neurons, n_delays) * 0.01
        )

    def forward(self, input_spikes, n_steps):
        """
        Args:
            input_spikes: (batch, N, T) external input spikes
            n_steps: number of simulation time steps
        Returns:
            output_spikes: (batch, N, T) generated spike trains
        """
        batch_size = input_spikes.shape[0]
        T = n_steps

        # Circular delay buffer: stores past D spike vectors
        delay_buffer = torch.zeros(batch_size, self.D, self.N, device=input_spikes.device)

        membrane = torch.zeros(batch_size, self.N, device=input_spikes.device)
        output_spikes = torch.zeros(batch_size, self.N, T, device=input_spikes.device)

        for t in range(T):
            # Compute delayed synaptic inputs via einsum
            # delay_buffer[:, d, :] = spikes from d+1 steps ago
            # W[i, j, d] * delay_buffer[:, d, j] summed over j, d
            delayed_input = torch.einsum('bdj,ijd->bi', delay_buffer, self.W)

            # Update membrane potential (LIF dynamics)
            membrane = self.decay * membrane + delayed_input + input_spikes[:, :, t]

            # Surrogate gradient spike function
            spikes = self._spike_fn(membrane)
            output_spikes[:, :, t] = spikes

            # Reset membrane after spike
            membrane = membrane * (1 - spikes)

            # Update delay buffer (shift and insert new spikes)
            delay_buffer = torch.roll(delay_buffer, 1, dims=1)
            delay_buffer[:, 0, :] = spikes

        return output_spikes

    def _spike_fn(self, membrane):
        """Spike generation with surrogate gradient for BPTT."""
        # Forward: hard threshold
        spikes = (membrane >= self.threshold).float()
        # Backward: smooth surrogate gradient (fast sigmoid)
        if self.training:
            beta = 10.0
            surrogate_grad = beta / (1 + 3.14159 * beta * (membrane - self.threshold) ** 2)
            spikes = spikes + surrogate_grad - surrogate_grad.detach()
        return spikes
```

### Step 2: Training Loop

```python
def train_working_memory(network, target_patterns, n_epochs=300, lr=1e-3, clamp_steps=41):
    """
    Train network to store and recall M spike patterns.

    Args:
        network: HeterogeneousDelaySNN instance
        target_patterns: (M, N, T) binary spike patterns to memorize
        n_epochs: training epochs
        lr: learning rate
        clamp_steps: number of teacher-forced initialization steps (= D)
    """
    optimizer = torch.optim.Adam(network.parameters(), lr=lr)
    loss_fn = nn.BCEWithLogitsLoss()
    M, N, T = target_patterns.shape

    for epoch in range(n_epochs):
        optimizer.zero_grad()

        # Create input with clamped initialization
        # input_spikes provides ground truth for first clamp_steps, then zero
        input_spikes = torch.zeros(1, N, T)
        input_spikes[0, :, :clamp_steps] = target_patterns[0, :, :clamp_steps]

        # Forward pass with surrogate gradient
        predicted = network(input_spikes, T)

        # Loss only on free recall region (after clamped window)
        pred_free = predicted[0, :, clamp_steps:]
        target_free = target_patterns[0, :, clamp_steps:]

        loss = loss_fn(pred_free, target_free)
        loss.backward()
        optimizer.step()

        if epoch % 50 == 0:
            f1 = compute_f1(pred_free.detach(), target_free)
            print(f"Epoch {epoch}: Loss={loss.item():.4f}, F1={f1:.4f}")

def compute_f1(predicted, target, threshold=0.5):
    """Compute F1 score between predicted and target spike trains."""
    pred_binary = (predicted > threshold).float()
    tp = (pred_binary * target).sum()
    fp = (pred_binary * (1 - target)).sum()
    fn = ((1 - pred_binary) * target).sum()
    precision = tp / (tp + fp + 1e-8)
    recall = tp / (tp + fn + 1e-8)
    f1 = 2 * precision * recall / (precision + recall + 1e-8)
    return f1.item()
```

### Step 3: Pattern Recall

```python
def recall_pattern(network, target_pattern, clamp_steps=41):
    """
    Recall a stored pattern given a clamped initialization window.

    Args:
        network: trained HeterogeneousDelaySNN
        target_pattern: (N, T) target spike pattern
        clamp_steps: number of initial steps to teacher-force
    Returns:
        recalled: (N, T) recalled spike train
    """
    N, T = target_pattern.shape
    network.eval()

    with torch.no_grad():
        input_spikes = torch.zeros(1, N, T)
        input_spikes[0, :, :clamp_steps] = target_pattern[:N, :clamp_steps]
        recalled = network(input_spikes, T)

    return recalled[0].numpy()
```

### Memory Optimization Tips

For the full-scale model (N=512, D=41, T=1000):

1. **Gradient checkpointing**: Reduce memory by recomputing activations during backward pass
2. **Truncated BPTT**: Limit backprop to K steps (e.g., K=200) with warm-start
3. **Mixed precision**: Use FP16/BF16 training (~2x memory reduction)
4. **Batch size = 1**: Train one pattern at a time to fit in GPU memory
5. **Weight tensor memory**: N×N×D = 512×512×41 ≈ 10.7M params ≈ 43 MB in FP32

### Scaling Guidelines

- **More patterns (M)**: Increase N or D; theoretical capacity scales as O(N·D)
- **Longer sequences (T)**: May benefit from hierarchical delay structures
- **Sparse patterns**: Enable higher capacity through reduced interference
- **Framework options**: SpikingJelly, Norse, or custom PyTorch/JAX implementations

## Applications

1. **Neuromorphic edge computing**: Energy-efficient temporal pattern storage for edge devices
2. **Brain-computer interfaces**: Neural signal pattern storage and temporal sequence learning
3. **Robotic control**: Motor pattern learning and temporal task encoding
4. **Sequence generation**: Autoregressive spike-based sequence models
5. **Computational neuroscience**: Modeling working memory mechanisms in cortical circuits

## Limitations and Considerations

1. **Training complexity**: Surrogate-gradient BPTT requires careful hyperparameter tuning
2. **Pattern interference**: Similar patterns may interfere; sparse patterns help
3. **Memory cost**: Full weight tensor O(N²·D) can be large for big networks
4. **Hardware gap**: Best performance on neuromorphic chips (Loihi, TrueNorth); GPU simulation is approximative
5. **Cascading errors**: Recall chain structure means early errors can propagate forward

## References

- Laurent U Perrinet. *"Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays."* arXiv:2604.14096, April 15, 2026. URL: https://arxiv.org/abs/2604.14096

### Related Work
- **Delay-embedded reservoir computing**: Fixed random delays in reservoir networks
- **Liquid State Machines**: Reservoir computing with temporal kernels
- **STDP-based learning**: Biological plasticity rules for delay networks
- **LSTM/GRU**: Analog counterparts for sequence memory in ANNs
