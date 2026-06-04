---
name: congestion-aware-axonal-delay-snn
description: "Congestion-Aware Dynamic Axonal Delay for Spiking Neural Networks. Replaces static per-synapse delays with input-dependent dynamic delays that adapt to network activity patterns, reducing delay parameters while improving temporal task performance. Activation: congestion-aware delay, dynamic axonal delay SNN, input-dependent delay, SNN temporal processing, adaptive delay learning."
---

# Congestion-Aware Dynamic Axonal Delay for Spiking Neural Networks

> Methodology that replaces static per-synapse delays in SNNs with input-dependent dynamic delays that adapt to network activity patterns, reducing parameter count while improving performance on temporal tasks.

## Metadata
- **Source**: arXiv:2605.01291v1
- **Authors**: Dewei Bai, Hongxiang Peng, Yunyun Zeng
- **Published**: 2026-05-02
- **Categories**: cs.LG

## Core Problem

Spiking Neural Networks are energy-efficient for temporal and event-driven information processing. Incorporating delays in SNNs improves spike alignment in event-driven tasks. However, existing delay learning approaches assign **static delays to individual synapses**, resulting in:
1. **Large number of delay parameters** — one per synapse, scaling poorly with network size
2. **Limited adaptability** — static delays cannot adjust to input-dependent activity dynamics

## Key Innovation

Replace static per-synapse delays with **congestion-aware dynamic delays** that:
1. **Adapt to input-dependent activity dynamics** — delays change based on current network state
2. **Share delay parameters** across synapses, dramatically reducing parameter count
3. **Model biological axonal delay** more realistically — biological axons exhibit activity-dependent conduction velocity changes

### Concept
```
Traditional: delay(synapse_ij) = d_ij  (static, per-synapse)
Proposed:    delay(synapse_ij, t) = f(activity_pattern, congestion_level)  (dynamic, shared)
```

### Congestion Mechanism
- When a neuron receives many simultaneous spikes → **congestion** → delays increase
- When activity is sparse → **low congestion** → delays decrease
- This creates **self-organizing temporal routing** that adapts to input statistics

## Core Methodology

### 1. Dynamic Delay Computation
- Delay is computed as a function of current network activity
- Uses a congestion metric based on recent spike rates in the network
- Formula: `d(t) = base_delay + α * congestion(t)` where congestion measures local activity density

### 2. Congestion Metric
- Tracks recent spike arrival rate at each neuron
- High arrival rate → high congestion → longer delays
- Low arrival rate → low congestion → shorter delays
- Implemented via exponential moving average of spike counts

### 3. Shared Delay Parameters
- Instead of N² parameters for N neurons, uses K shared delay profiles
- Each synapse is assigned to one of K delay groups
- Groups are learned during training
- Dramatic parameter reduction: O(K) vs O(N²)

### 4. Learning Rule
- Delays are learned alongside synaptic weights
- Gradient-based optimization through surrogate gradients
- Congestion-aware delay adjustment emerges naturally from loss minimization

## Implementation Guide

### Prerequisites
- SpikingJelly or similar SNN framework
- PyTorch

### Congestion-Aware Delay Module
```python
import torch
import torch.nn as nn

class CongestionAwareDelay(nn.Module):
    """Dynamic axonal delay that adapts to network congestion."""
    
    def __init__(self, n_groups=8, base_delay=1.0, alpha=0.5, tau_congestion=10.0):
        super().__init__()
        self.n_groups = n_groups
        self.base_delay = base_delay
        self.alpha = alpha  # congestion sensitivity
        self.tau_congestion = tau_congestion  # congestion decay time constant
        
        # Learnable delay profiles per group
        self.delay_profiles = nn.Parameter(
            torch.linspace(1.0, 10.0, n_groups)  # Initial range of delays
        )
        
        # Congestion state (per neuron)
        self.congestion = None
    
    def update_congestion(self, spikes):
        """Update congestion metric based on recent spike activity."""
        if self.congestion is None:
            self.congestion = torch.zeros_like(spikes.sum(dim=0, keepdim=True))
        
        # Exponential moving average of spike count
        spike_count = spikes.sum(dim=0, keepdim=True)
        self.congestion = (
            (1 - 1/self.tau_congestion) * self.congestion + 
            (1/self.tau_congestion) * spike_count
        )
    
    def get_delay(self, group_id):
        """Get dynamic delay for a given group, modulated by congestion."""
        base = self.delay_profiles[group_id]
        congestion_mod = self.alpha * self.congestion
        return base + congestion_mod
    
    def forward(self, spikes, group_assignments):
        """Apply dynamic delays to spike trains."""
        self.update_congestion(spikes)
        
        delayed_spikes = torch.zeros_like(spikes)
        for g in range(self.n_groups):
            mask = (group_assignments == g)
            delay = self.get_delay(g).int()
            if delay > 0 and delay < spikes.shape[0]:
                delayed_spikes[delay:, mask] = spikes[:-delay, mask]
        
        return delayed_spikes
```

### Integration with SNN
```python
class SNNWithDynamicDelay(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, n_delay_groups=8):
        super().__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.delay = CongestionAwareDelay(n_groups=n_delay_groups)
        
        # Assign each synapse to a delay group
        self.group_assignments = nn.Parameter(
            torch.randint(0, n_delay_groups, (hidden_size,)),
            requires_grad=False
        )
    
    def forward(self, spike_trains):
        # spike_trains: (time, batch, input_size)
        hidden = self.fc1(spike_trains)
        
        # Apply congestion-aware delays
        delayed_hidden = self.delay(hidden, self.group_assignments)
        
        output = self.fc2(delayed_hidden)
        return output
```

## Applications
- **Event-based vision**: Processing DVS camera data with adaptive temporal resolution
- **Speech recognition**: Handling variable-rate temporal patterns
- **Robotics**: Real-time sensorimotor control with adaptive response timing
- **Temporal pattern recognition**: Sequences with variable inter-event intervals
- **Neuromorphic hardware**: Efficient delay implementation with shared parameters

## Advantages Over Static Delay SNNs
| Aspect | Static Delay | Congestion-Aware Dynamic Delay |
|--------|-------------|-------------------------------|
| Parameters | O(N²) per synapse | O(K) shared profiles |
| Adaptability | Fixed after training | Adapts to input dynamics |
| Biological realism | Low | High (activity-dependent conduction) |
| Memory efficiency | Poor | Excellent |
| Temporal flexibility | Limited | High |

## Pitfalls
- **Congestion metric tuning**: The tau_congestion parameter critically affects delay dynamics
- **Group assignment**: Learning optimal group assignments for synapses requires careful initialization
- **Delay range**: Base delay range must be chosen to match task timescales
- **Gradient flow**: Surrogate gradients needed for delay learning; choice affects convergence
- **Network size**: Very small networks may not benefit from congestion-aware mechanisms

## Related Skills
- conv-delay-learning-snn
- delay-adaptive-snn-classifier
- spiking-neural-network-analysis
- snn-learning-survey
- congestion-aware-delay-snn