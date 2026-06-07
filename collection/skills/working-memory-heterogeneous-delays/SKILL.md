---
name: working-memory-heterogeneous-delays
description: "Working memory implementation in recurrent spiking neural networks using heterogeneous synaptic delays. Models memory as sequential chains of overlapping Spiking Motifs for precise temporal pattern storage and recall. Activation: working memory SNN, heterogeneous delays, spiking motifs, recurrent SNN memory, temporal pattern storage, neuromorphic working memory."
---

# Working Memory in Recurrent SNNs with Heterogeneous Synaptic Delays

## Overview

This skill implements a working memory mechanism for Spiking Neural Networks (SNNs) using **heterogeneous synaptic delays**. The approach addresses the challenge of storing and recalling precise temporal patterns of neural activity—a fundamental capability that remains difficult for SNNs. By equipping each synapse with multiple delays (D = 41), the network represents each memory as a sequential chain of overlapping **Spiking Motifs**.

## Key Innovation

**Traditional SNN Memory:** Fixed or uniform delays limit temporal precision  
**This Approach:** Heterogeneous delays enable rich temporal pattern storage

**Core Concept:**
- Each synapse has D = 41 delay values (modeled as weight tensor W ∈ R^(N×N×D))
- Trained end-to-end with surrogate-gradient backpropagation through time
- Memories stored as sequential chains of overlapping Spiking Motifs
- Each motif: contiguous window of length D that predicts spikes at next timestep

## Mathematical Framework

### Network Architecture

```
Recurrent SNN:
- N neurons (e.g., 512)
- Each synapse: D = 41 delays
- Weight tensor: W ∈ R^(N×N×D)
```

### Spiking Motif Definition

```
A Spiking Motif at time t is a contiguous window:
M(t) = [s(t-D+1), s(t-D+2), ..., s(t)]

where s(τ) is the spike pattern at time τ
```

The motif **uniquely predicts** spikes at the next timestep s(t+1).

### Neuron Dynamics

```
τ_m * dV_i/dt = -V_i + Σ_j Σ_d W_ij(d) * s_j(t-d) + I_ext

if V_i ≥ θ:
    spike = 1
    V_i ← 0  (reset)
```

### Delay-Modulated Input

The delayed input at time t from neuron j:
```
h_j(t) = Σ_d W_ij(d) · s_j(t-d)
```

This creates a **temporal receptive field** of length D timesteps.

## Implementation

### Heterogeneous Delay SNN

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class HeterogeneousDelaySNN(nn.Module):
    """
    Recurrent SNN with heterogeneous synaptic delays for working memory
    
    Args:
        n_neurons: Number of neurons in the recurrent layer
        n_delays: Number of delay values per synapse (D)
        tau_mem: Membrane time constant
        v_threshold: Firing threshold
    """
    def __init__(
        self,
        n_neurons: int = 512,
        n_delays: int = 41,
        tau_mem: float = 20.0,
        v_threshold: float = 1.0
    ):
        super().__init__()
        
        self.n_neurons = n_neurons
        self.n_delays = n_delays
        self.tau_mem = tau_mem
        self.v_threshold = v_threshold
        
        # Weight tensor: (n_neurons, n_neurons, n_delays)
        # W[i, j, d] = weight from neuron j to neuron i with delay d
        self.recurrent_weights = nn.Parameter(
            torch.randn(n_neurons, n_neurons, n_delays) * 0.01
        )
        
        # Spike history buffer (for delay computation)
        self.register_buffer('spike_history', None)
        self.register_buffer('membrane_potential', None)
        
    def reset_state(self, batch_size: int = 1, device='cpu'):
        """Reset network state for new sequence"""
        self.spike_history = torch.zeros(
            batch_size, self.n_neurons, self.n_delays, device=device
        )
        self.membrane_potential = torch.zeros(
            batch_size, self.n_neurons, device=device
        )
        
    def forward_single_step(
        self,
        external_input: torch.Tensor,
        dt: float = 1.0
    ) -> torch.Tensor:
        """
        Single forward timestep with delay-modulated input
        
        Args:
            external_input: (batch, n_neurons) external current
            dt: Time step size
            
        Returns:
            spikes: (batch, n_neurons) spike pattern
        """
        # Compute delayed input: Σ_d W[:,:,d] · s(t-d)
        # spike_history shape: (batch, n_neurons, n_delays)
        # We need: for each postsynaptic neuron i, sum over presynaptic j and delay d
        
        # Efficient computation using einsum
        # recurrent_weights: (n_neurons, n_neurons, n_delays)
        # spike_history: (batch, n_neurons, n_delays)
        delayed_input = torch.einsum(
            'ijd,bjd->bi',
            self.recurrent_weights,
            self.spike_history
        )
        
        # Total input
        total_input = external_input + delayed_input
        
        # Update membrane potential (Euler method)
        dv = (-self.membrane_potential + total_input) / self.tau_mem * dt
        self.membrane_potential = self.membrane_potential + dv
        
        # Spike generation
        spikes = (self.membrane_potential >= self.v_threshold).float()
        
        # Reset after spike
        self.membrane_potential = self.membrane_potential * (1 - spikes)
        
        # Update spike history (roll and insert new spikes)
        # Shift old spikes to higher delay indices
        self.spike_history = torch.roll(self.spike_history, shifts=1, dims=2)
        self.spike_history[:, :, 0] = spikes  # Insert new spikes at delay 0
        
        return spikes
```

### Working Memory Training

```python
class WorkingMemoryTrainer:
    """
    Trainer for working memory tasks using surrogate gradient
    """
    def __init__(
        self,
        network: HeterogeneousDelaySNN,
        n_patterns: int = 16,
        pattern_length: int = 1000,
        learning_rate: float = 1e-3
    ):
        self.network = network
        self.n_patterns = n_patterns
        self.pattern_length = pattern_length
        
        # Surrogate gradient for backprop through spikes
        self.surrogate_slope = 1.0
        
        # Optimizer
        self.optimizer = torch.optim.Adam(
            network.parameters(),
            lr=learning_rate
        )
        
    def generate_random_patterns(self, batch_size: int = 1) -> torch.Tensor:
        """
        Generate random target spike patterns
        
        Returns:
            patterns: (n_patterns, pattern_length, n_neurons) binary tensor
        """
        patterns = torch.zeros(
            self.n_patterns,
            self.pattern_length,
            self.network.n_neurons
        )
        
        # Random sparse patterns (5% firing rate)
        for p in range(self.n_patterns):
            spike_probs = torch.rand(self.pattern_length, self.network.n_neurons)
            patterns[p] = (spike_probs < 0.05).float()
        
        return patterns
        
    def compute_spiking_motif_loss(
        self,
        predicted_spikes: torch.Tensor,
        target_spikes: torch.Tensor
    ) -> torch.Tensor:
        """
        Loss based on spiking motif prediction
        
        Each window of length D should predict next timestep
        
        Args:
            predicted_spikes: (time, n_neurons) network output
            target_spikes: (time, n_neurons) target pattern
        """
        n_steps = predicted_spikes.size(0)
        D = self.network.n_delays
        
        total_loss = 0
        n_windows = 0
        
        for t in range(D, n_steps):
            # Extract motif: window [t-D, t-1]
            motif = target_spikes[t-D:t]  # (D, n_neurons)
            
            # Predict next timestep
            predicted = predicted_spikes[t]
            target = target_spikes[t]
            
            # Binary cross-entropy loss
            loss = F.binary_cross_entropy_with_logits(
                predicted,
                target
            )
            
            total_loss += loss
            n_windows += 1
        
        return total_loss / n_windows
        
    def train_step(
        self,
        target_patterns: torch.Tensor,
        clamp_duration: int = 50
    ) -> dict:
        """
        Single training step with pattern clamping
        
        Args:
            target_patterns: (n_patterns, time, n_neurons) target spikes
            clamp_duration: Initial timesteps to clamp to target
            
        Returns:
            metrics dictionary
        """
        batch_size = target_patterns.size(0)
        n_steps = target_patterns.size(1)
        
        self.optimizer.zero_grad()
        
        all_losses = []
        all_f1_scores = []
        
        for pattern_idx in range(batch_size):
            target = target_patterns[pattern_idx]  # (time, n_neurons)
            
            # Reset network state
            self.network.reset_state(batch_size=1, device=target.device)
            
            # Forward pass
            predictions = []
            
            for t in range(n_steps):
                if t < clamp_duration:
                    # Clamp to target during initialization
                    external = target[t] * 10.0  # Strong input
                else:
                    # Free running
                    external = torch.zeros(self.network.n_neurons)
                
                spikes = self.network.forward_single_step(
                    external.unsqueeze(0)
                )
                predictions.append(spikes[0])
            
            predictions = torch.stack(predictions)
            
            # Compute loss
            loss = self.compute_spiking_motif_loss(predictions, target)
            
            # Compute F1 score
            pred_binary = (predictions > 0.5).float()
            f1 = self.compute_f1_score(pred_binary[D:], target[D:])
            
            all_losses.append(loss)
            all_f1_scores.append(f1)
        
        # Backpropagation
        total_loss = torch.stack(all_losses).mean()
        total_loss.backward()
        
        # Gradient clipping
        torch.nn.utils.clip_grad_norm_(self.network.parameters(), 1.0)
        
        self.optimizer.step()
        
        return {
            'loss': total_loss.item(),
            'f1_score': torch.stack(all_f1_scores).mean().item()
        }
        
    def compute_f1_score(
        self,
        predictions: torch.Tensor,
        targets: torch.Tensor
    ) -> torch.Tensor:
        """Compute F1 score for spike prediction"""
        tp = (predictions * targets).sum()
        fp = (predictions * (1 - targets)).sum()
        fn = ((1 - predictions) * targets).sum()
        
        precision = tp / (tp + fp + 1e-8)
        recall = tp / (tp + fn + 1e-8)
        
        f1 = 2 * precision * recall / (precision + recall + 1e-8)
        
        return f1
```

### Pattern Recall Visualization

```python
def visualize_pattern_recall(
    network: HeterogeneousDelaySNN,
    target_pattern: torch.Tensor,
    clamp_duration: int = 50
):
    """
    Visualize how recall propagates from clamped initialization
    
    Args:
        network: Trained network
        target_pattern: Target spike pattern (time, n_neurons)
        clamp_duration: How long to clamp input
    """
    import matplotlib.pyplot as plt
    
    network.reset_state(batch_size=1, device=target_pattern.device)
    
    recalled_spikes = []
    
    for t in range(target_pattern.size(0)):
        if t < clamp_duration:
            external = target_pattern[t] * 10.0
        else:
            external = torch.zeros(network.n_neurons)
        
        spikes = network.forward_single_step(external.unsqueeze(0))
        recalled_spikes.append(spikes[0])
    
    recalled = torch.stack(recalled_spikes)
    
    # Plot raster
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    
    # Target pattern
    ax1 = axes[0]
    for neuron in range(min(50, network.n_neurons)):
        times = torch.where(target_pattern[:, neuron] > 0.5)[0]
        ax1.scatter(times.cpu(), [neuron] * len(times), s=1, c='blue')
    ax1.axvline(clamp_duration, color='red', linestyle='--', label='Clamp end')
    ax1.set_ylabel('Neuron')
    ax1.set_title('Target Pattern')
    ax1.legend()
    
    # Recalled pattern
    ax2 = axes[1]
    for neuron in range(min(50, network.n_neurons)):
        times = torch.where(recalled[:, neuron] > 0.5)[0]
        ax2.scatter(times.cpu(), [neuron] * len(times), s=1, c='green')
    ax2.axvline(clamp_duration, color='red', linestyle='--', label='Clamp end')
    ax2.set_ylabel('Neuron')
    ax2.set_xlabel('Time')
    ax2.set_title('Recalled Pattern')
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('pattern_recall.png', dpi=150)
    plt.show()
```

## Key Results

From paper evaluation:

| Metric | Value |
|--------|-------|
| Neurons | 512 |
| Delays per synapse | 41 |
| Patterns stored | 16 |
| Pattern length | 1000 timesteps |
| Mean F1 score | 1.0 (perfect recall) |
| Training | Surrogate-gradient BPTT |

**Recall Behavior:**
- Recall **emerges first near the clamped initialization window**
- Propagates **forward in time** from initialization point
- Demonstrates **temporal generalization** from limited seed

## Advantages

1. **Efficient Storage**: D delays = D-fold increase in temporal resolution without D-fold neurons
2. **Pattern Completion**: Partial cue can trigger full pattern recall
3. **Temporal Precision**: Precise spike timing preservation
4. **Energy Efficient**: Sparse spike coding for neuromorphic deployment
5. **End-to-End Trainable**: Surrogate gradient enables direct optimization

## Applications

- **Neuromorphic Working Memory**: Edge AI with temporal sequence storage
- **Sequence Prediction**: Time series forecasting
- **Pattern Recognition**: Temporal pattern classification
- **Brain Modeling**: Understanding cortical working memory mechanisms

## Extensions

### Adaptive Delays
```python
class AdaptiveDelaySNN(HeterogeneousDelaySNN):
    """
    Extension with trainable delay values (not just weights)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Trainable delay values (continuous)
        self.delay_values = nn.Parameter(
            torch.linspace(1, self.n_delays, self.n_delays)
        )
```

### Multiple Memory Slots
```python
class MultiSlotWorkingMemory(nn.Module):
    """
    Multiple independent working memory slots
    """
    def __init__(self, n_slots=4, **kwargs):
        super().__init__()
        self.slots = nn.ModuleList([
            HeterogeneousDelaySNN(**kwargs)
            for _ in range(n_slots)
        ])
        self.attention = nn.MultiheadAttention(kwargs['n_neurons'], 4)
```

## References

- Paper: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays" (arXiv:2604.14096)
- Author: Laurent U Perrinet, 2026
- Category: q-bio.NC (Neurons and Cognition)

## Related Skills

- `dual-timescale-memory-spiking-neuron-astrocyte`: Alternative working memory approach
- `adaptive-spiking-neuron-asn`: General spiking neuron designs
- `snn-learning-survey`: Comprehensive SNN learning rules

_Last updated: 2026-04-27_
