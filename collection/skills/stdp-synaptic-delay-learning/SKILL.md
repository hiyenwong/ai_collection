---
name: stdp-synaptic-delay-learning
description: "Extended STDP learning rule for simultaneously learning synaptic connection strengths and delays, validated on unsupervised SNN classification tasks with superior performance over delay-free STDP."
---

# Extending Spike-Timing Dependent Plasticity to Learning Synaptic Delays

> Novel learning rule extending classical STDP to simultaneously optimize both synaptic weights and temporal delays, enabling richer temporal representation in spiking neural networks.

## Metadata
- **Source**: arXiv:2506.14984 [cs.NE]
- **Authors**: Marissa Dominijanni, Alexander Ororbia, Kenneth W. Regan
- **Published**: 2025-06-17
- **Categories**: cs.NE (Neural and Evolutionary Computing), cs.LG (Machine Learning)
- **Code**: Available at https URL

## Core Methodology

### Key Innovation
Biological neuronal networks rely on precise synaptic timing, but traditional SNNs fix synaptic delays. This work extends STDP to co-learn:
- **Synaptic Weights ($w_{ij}$)**: Connection strengths
- **Synaptic Delays ($d_{ij}$)**: Temporal offsets
- **Joint Optimization**: Simultaneous weight and delay updates

### Technical Framework

#### 1. Delayed Synaptic Transmission
Standard SNN: $I_j(t) = \sum_i w_{ij} s_i(t)$

With delays: $I_j(t) = \sum_i w_{ij} s_i(t - d_{ij})$

Where $d_{ij}$ is the synaptic delay from neuron $i$ to $j$.

#### 2. Extended STDP Rule
The learning rule updates both weights and delays based on spike timing:

**Weight Update:**
$$\Delta w_{ij} = \eta_w \cdot f_w(\Delta t_{ij})$$

**Delay Update:**
$$\Delta d_{ij} = \eta_d \cdot f_d(\Delta t_{ij}) \cdot \text{sign}(w_{ij})$$

Where:
- $\Delta t_{ij} = t_j^{post} - t_i^{pre} - d_{ij}$: Effective time difference
- $f_w, f_d$: STDP window functions
- $\eta_w, \eta_d$: Learning rates

#### 3. Delay-Dependent Window Function
$$f_d(\Delta t) = -\frac{\partial f_w}{\partial \Delta t}$$

The delay update pushes the delay to better align pre- and post-synaptic spikes.

#### 4. Biological Plausibility
- Delays reflect axonal conduction times
- Activity-dependent myelination
- Synaptic distance optimization

## Implementation Guide

### Prerequisites
- Python 3.8+
- PyTorch or TensorFlow
- NumPy, SciPy
- Optional: Brian2 for biophysical simulation

### Step-by-Step Implementation

```python
import torch
import torch.nn as nn
import numpy as np
from typing import Tuple, Optional

class STDPSynapticDelay(nn.Module):
    """
    STDP with synaptic delay learning
    """
    def __init__(
        self,
        in_features: int,
        out_features: int,
        max_delay: float = 20.0,  # ms
        dt: float = 1.0,  # ms
        tau_pre: float = 20.0,  # Pre-synaptic time constant
        tau_post: float = 20.0,  # Post-synaptic time constant
        lr_weight: float = 0.01,
        lr_delay: float = 0.001,
        A_plus: float = 0.1,
        A_minus: float = 0.1
    ):
        super().__init__()
        
        self.in_features = in_features
        self.out_features = out_features
        self.max_delay = max_delay
        self.dt = dt
        self.tau_pre = tau_pre
        self.tau_post = tau_post
        
        # Synaptic weights
        self.weight = nn.Parameter(torch.randn(out_features, in_features) * 0.1)
        
        # Synaptic delays (in timesteps)
        self.delay = nn.Parameter(
            torch.rand(out_features, in_features) * max_delay / dt,
            requires_grad=False  # Updated via STDP, not backprop
        )
        
        # Learning rates
        self.lr_weight = lr_weight
        self.lr_delay = lr_delay
        self.A_plus = A_plus
        self.A_minus = A_minus
        
        # Spike time tracking
        self.pre_spike_times = torch.full((in_features,), -1000.0)
        self.post_spike_times = torch.full((out_features,), -1000.0)
        
        # Delay buffers for each connection
        self.delay_buffers = None
    
    def initialize_buffers(self, batch_size: int = 1):
        """Initialize delay line buffers"""
        max_delay_steps = int(self.max_delay / self.dt)
        self.delay_buffers = torch.zeros(
            batch_size, self.in_features, max_delay_steps
        )
    
    def apply_delays(self, pre_spikes: torch.Tensor) -> torch.Tensor:
        """
        Apply synaptic delays to pre-synaptic spikes
        
        Args:
            pre_spikes: [batch, in_features] current pre-synaptic spikes
        
        Returns:
            delayed_spikes: [batch, in_features, out_features] delayed spikes
                Each output neuron sees differently delayed inputs
        """
        batch_size = pre_spikes.size(0)
        
        if self.delay_buffers is None or self.delay_buffers.size(0) != batch_size:
            self.initialize_buffers(batch_size)
        
        # Update delay buffers (shift and insert)
        self.delay_buffers = torch.roll(self.delay_buffers, shifts=1, dims=2)
        self.delay_buffers[:, :, 0] = pre_spikes
        
        # Sample delayed spikes
        delayed = torch.zeros(batch_size, self.in_features, self.out_features)
        
        for j in range(self.out_features):
            for i in range(self.in_features):
                delay_idx = int(self.delay[j, i].item())
                delay_idx = min(delay_idx, self.delay_buffers.size(2) - 1)
                delayed[:, i, j] = self.delay_buffers[:, i, delay_idx]
        
        return delayed
    
    def stdp_window(self, delta_t: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        STDP window function and its derivative
        
        Args:
            delta_t: [out_features, in_features] time differences
        
        Returns:
            f_w: Weight update magnitude
            f_d: Delay update magnitude (derivative)
        """
        # Exponential STDP window
        # LTP: pre before post
        ltp_mask = delta_t > 0
        ltd_mask = delta_t < 0
        
        f_w = torch.zeros_like(delta_t)
        f_d = torch.zeros_like(delta_t)
        
        # LTP part
        f_w = torch.where(
            ltp_mask,
            self.A_plus * torch.exp(-delta_t / self.tau_post),
            f_w
        )
        f_d = torch.where(
            ltp_mask,
            self.A_plus / self.tau_post * torch.exp(-delta_t / self.tau_post),
            f_d
        )
        
        # LTD part
        f_w = torch.where(
            ltd_mask,
            -self.A_minus * torch.exp(delta_t / self.tau_pre),
            f_w
        )
        f_d = torch.where(
            ltd_mask,
            self.A_minus / self.tau_pre * torch.exp(delta_t / self.tau_pre),
            f_d
        )
        
        return f_w, f_d
    
    def update_delays_and_weights(
        self,
        pre_spike_times: torch.Tensor,
        post_spike_times: torch.Tensor
    ):
        """
        Apply extended STDP to update weights and delays
        
        Args:
            pre_spike_times: [in_features] pre-synaptic spike times
            post_spike_times: [out_features] post-synaptic spike times
        """
        # Compute effective time differences
        # delta_t = t_post - t_pre - delay
        delta_t = post_spike_times.unsqueeze(1) - pre_spike_times.unsqueeze(0)
        delta_t = delta_t - self.delay * self.dt
        
        # Get STDP window values
        f_w, f_d = self.stdp_window(delta_t)
        
        # Update weights
        delta_w = self.lr_weight * f_w
        self.weight.data += delta_w
        
        # Update delays (clipped to valid range)
        delta_d = self.lr_delay * f_d * torch.sign(self.weight)
        self.delay.data -= delta_d  # Negative because we want to reduce |delta_t|
        self.delay.data.clamp_(0, self.max_delay / self.dt)
        
        return delta_w, delta_d
    
    def forward(self, pre_spikes: torch.Tensor) -> torch.Tensor:
        """
        Forward pass with delayed synaptic transmission
        
        Args:
            pre_spikes: [batch, time, in_features] or [batch, in_features]
        
        Returns:
            current: [batch, out_features] synaptic current
        """
        if pre_spikes.dim() == 3:
            # Temporal input - use last timestep
            pre_spikes = pre_spikes[:, -1, :]
        
        batch_size = pre_spikes.size(0)
        
        # Apply delays
        delayed_spikes = self.apply_delays(pre_spikes)
        
        # Compute synaptic current
        # Sum over input neurons with delays
        current = torch.zeros(batch_size, self.out_features)
        for j in range(self.out_features):
            for i in range(self.in_features):
                current[:, j] += self.weight[j, i] * delayed_spikes[:, i, j]
        
        return current


class DelayLearningSNN(nn.Module):
    """
    Complete SNN with synaptic delay learning
    """
    def __init__(
        self,
        input_size: int,
        hidden_size: int,
        output_size: int,
        time_steps: int = 100,
        **stdp_kwargs
    ):
        super().__init__()
        
        self.time_steps = time_steps
        
        # Input to hidden layer with delay learning
        self.syn1 = STDPSynapticDelay(
            input_size, hidden_size, **stdp_kwargs
        )
        
        # Hidden to output (standard for simplicity)
        self.fc2 = nn.Linear(hidden_size, output_size)
        
        # LIF neuron parameters
        self.tau_mem = 20.0
        self.v_thresh = 1.0
        self.v_reset = 0.0
        
        # State
        self.v_hidden = None
        self.spike_times_hidden = torch.full((hidden_size,), -1000.0)
        self.spike_times_input = torch.full((input_size,), -1000.0)
    
    def reset_state(self, batch_size: int = 1):
        """Reset neuron states"""
        self.v_hidden = torch.zeros(batch_size, self.syn1.out_features)
        self.spike_times_hidden.fill_(-1000.0)
        self.spike_times_input.fill_(-1000.0)
        self.syn1.initialize_buffers(batch_size)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass
        
        Args:
            x: [batch, time_steps, input_size] input spike trains
        
        Returns:
            output: [batch, output_size]
        """
        batch_size, time_steps, input_size = x.shape
        
        if self.v_hidden is None or self.v_hidden.size(0) != batch_size:
            self.reset_state(batch_size)
        
        hidden_spikes = []
        
        for t in range(time_steps):
            x_t = x[:, t, :]
            
            # Record input spike times
            for i in range(input_size):
                if x_t[0, i] > 0.5:  # Spike occurred
                    self.spike_times_input[i] = t
            
            # Synaptic current with delays
            i_syn = self.syn1(x_t)
            
            # LIF dynamics
            dv = (self.v_reset - self.v_hidden) / self.tau_mem + i_syn
            self.v_hidden = self.v_hidden + dv
            
            # Spike generation
            spike = (self.v_hidden >= self.v_thresh).float()
            self.v_hidden = self.v_hidden * (1 - spike) + self.v_reset * spike
            
            hidden_spikes.append(spike)
            
            # Record hidden spike times and apply STDP
            for j in range(self.syn1.out_features):
                if spike[0, j] > 0.5:
                    self.spike_times_hidden[j] = t
                    
                    # Apply STDP updates
                    if t > 0:
                        self.syn1.update_delays_and_weights(
                            self.spike_times_input,
                            self.spike_times_hidden
                        )
        
        # Output layer (rate coding)
        hidden_rate = torch.stack(hidden_spikes, dim=1).mean(dim=1)
        output = self.fc2(hidden_rate)
        
        return output
```

### Delay Analysis and Visualization

```python
def analyze_learned_delays(model: DelayLearningSNN):
    """
    Analyze learned synaptic delay distribution
    
    Args:
        model: Trained model
    
    Returns:
        stats: Dictionary of delay statistics
    """
    delays = model.syn1.delay.detach().cpu().numpy() * model.syn1.dt
    weights = model.syn1.weight.detach().cpu().numpy()
    
    # Only consider significant weights
    significant_mask = np.abs(weights) > 0.01
    significant_delays = delays[significant_mask]
    
    stats = {
        'mean_delay_ms': np.mean(significant_delays),
        'std_delay_ms': np.std(significant_delays),
        'min_delay_ms': np.min(significant_delays),
        'max_delay_ms': np.max(significant_delays),
        'delay_distribution': significant_delays,
        'delay_weight_correlation': np.corrcoef(
            delays.flatten(), np.abs(weights).flatten()
        )[0, 1]
    }
    
    return stats


def visualize_delay_weights(model: DelayLearningSNN):
    """
    Visualize learned delays and weights
    """
    import matplotlib.pyplot as plt
    
    delays = model.syn1.delay.detach().cpu().numpy() * model.syn1.dt
    weights = model.syn1.weight.detach().cpu().numpy()
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    # Delay histogram
    axes[0].hist(delays.flatten(), bins=50)
    axes[0].set_xlabel('Delay (ms)')
    axes[0].set_ylabel('Count')
    axes[0].set_title('Learned Delay Distribution')
    
    # Weight histogram
    axes[1].hist(weights.flatten(), bins=50)
    axes[1].set_xlabel('Weight')
    axes[1].set_ylabel('Count')
    axes[1].set_title('Learned Weight Distribution')
    
    # Delay vs Weight scatter
    axes[2].scatter(delays.flatten(), weights.flatten(), alpha=0.3)
    axes[2].set_xlabel('Delay (ms)')
    axes[2].set_ylabel('Weight')
    axes[2].set_title('Delay vs Weight')
    
    plt.tight_layout()
    plt.savefig('delay_weight_analysis.png')
    plt.close()
```

## Applications

### 1. Temporal Pattern Recognition
- **Spike Timing Codes**: Precise temporal patterns
- **Auditory Processing**: Sound localization via delays
- **Sequence Learning**: Order-sensitive tasks

### 2. Auditory Localization
- **ITD/ILD Encoding**: Interaural time/level differences
- **Sound Source Separation**: Delay-based segregation
- **Spatial Hearing**: 3D audio processing

### 3. Sequence Learning
- **Time Series Prediction**: Temporal dependencies
- **Speech Recognition**: Phoneme timing
- **Rhythm Processing**: Musical patterns

### 4. Neural Coding
- **Temporal Coding**: Beyond rate coding
- **Synchrony Detection**: Coincidence detection
- **Phase Coding**: Oscillatory synchronization

## Pitfalls

1. **Delay Bounds**: Delays must be within practical limits
   - *Mitigation*: Hard constraints, regularization, decay terms

2. **Stability**: Learning can be unstable with large delays
   - *Mitigation*: Conservative learning rates, normalization

3. **Hardware Implementation**: True analog delays difficult
   - *Mitigation*: Digital delay lines, approximations

4. **Interpretability**: Many equivalent delay/weight combinations
   - *Mitigation*: Regularization toward biological values

5. **Computational Cost**: Delay lines require memory
   - *Mitigation*: Sparse connectivity, shared delays

## Related Skills
- stdp-learning: Classical STDP
- snn-working-memory-delays: Delay-based working memory
- stdp-spiking-transformer-attention: STDP in Transformers
- spiking-reservoir-robustness: Reservoir computing with delays

## References
```bibtex
@article{dominijanni2025delay,
  title={Extending Spike-Timing Dependent Plasticity to Learning Synaptic Delays},
  author={Dominijanni, Marissa and Ororbia, Alexander and Regan, Kenneth W},
  journal={arXiv preprint arXiv:2506.14984},
  year={2025}
}
```

## Further Reading
- Axonal Delays: Swadlow, "Efferent neurons and suspected interneurons in S-1"
- Delay Learning: Natschläger & Ruf, "Spatial and Temporal Pattern Analysis"
- STDP: Bi & Poo, "Synaptic modification by correlated activity"
- Temporal Coding: Hopfield, "Pattern recognition computation using action potential timing"
