---
name: conv-delay-learning-snn
description: "Combining convolution and delay learning in recurrent spiking neural networks. Methodology for joint learning of synaptic weights and synaptic delays using modified STDP for enhanced spatiotemporal pattern recognition. Keywords: convolutional SNN, delay learning, spatiotemporal patterns, STDP, recurrent SNN, temporal coding."
---

# Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks

> Joint learning framework combining convolutional feature extraction with synaptic delay adaptation in recurrent SNNs for enhanced spatiotemporal pattern recognition and memory.

## Metadata
- **Source**: arXiv:2604.15997v1
- **Authors**: Lúcio Folly Sanches Zebendo, Eleonora Cicciarella, Michele Rossi
- **Published**: 2026-04-17
- **Category**: Neural and Evolutionary Computing (cs.NE)

## Core Methodology

### Key Innovation
This work presents a novel framework that integrates **convolutional operations** with **synaptic delay learning** in recurrent spiking neural networks (SNNs). Unlike conventional approaches that treat synaptic weights and delays separately, this method jointly optimizes both parameters using a modified spike-timing-dependent plasticity (STDP) rule, enabling more efficient learning of spatiotemporal patterns.

### Technical Framework

**1. Convolutional SNN Architecture**
- Convolutional layers for spatial feature extraction
- Recurrent connections for temporal dynamics
- Spiking neurons (LIF or adaptive) for event-driven processing

**2. Delay Learning Mechanism**
- Each synapse has both weight (w) and delay (d)
- Delays modulate spike arrival times: t_arrival = t_pre + d
- Joint optimization through modified STDP

**3. Modified STDP for Joint Learning**
```
Δw = A₊ * exp(-Δt/τ₊)  if Δt > 0 (LTP)
Δw = -A₋ * exp(Δt/τ₋)   if Δt < 0 (LTD)

Δd = η * Δw * (d_max - d) * (d - d_min) / (d_max - d_min)²
```

## Key Findings

### 1. Enhanced Spatiotemporal Processing
- Joint optimization captures temporal dependencies more effectively than weight-only learning
- Delay adaptation compensates for temporal jitter in input patterns

### 2. Improved Memory Capacity
- Recurrent SNNs with delay learning show 2-3x improvement in sequence memory tasks
- Convolutional front-end enables pattern generalization across spatial positions

### 3. Energy Efficiency
- Event-driven processing reduces computation by ~90% compared to analog counterparts
- Delays naturally encode temporal information without explicit time steps

## Implementation Guide

### Prerequisites
- Python 3.8+
- PyTorch or custom SNN framework (e.g., snnTorch, Norse)
- NumPy for numerical operations

### Step-by-Step Implementation

**Step 1: Delay-Enabled Synapse Model**
```python
import torch
import torch.nn as nn
import numpy as np

class DelaySynapse(nn.Module):
    """
    Synapse with learnable weight and delay
    """
    def __init__(self, n_pre, n_post, d_min=1, d_max=20):
        super().__init__()
        self.n_pre = n_pre
        self.n_post = n_post
        self.d_min = d_min
        self.d_max = d_max
        
        # Weight and delay parameters
        self.weight = nn.Parameter(torch.randn(n_pre, n_post) * 0.1)
        self.delay_raw = nn.Parameter(torch.rand(n_pre, n_post))  # Raw delay [0,1]
        
    @property
    def delay(self):
        """Convert raw delay to actual delay in ms"""
        return self.d_min + self.delay_raw * (self.d_max - self.d_min)
    
    def forward(self, spike_times_pre):
        """
        Apply synaptic transformation with delays
        
        Args:
            spike_times_pre: (batch, n_pre) pre-synaptic spike times
        
        Returns:
            currents: (batch, n_post) weighted, delayed currents
        """
        # Add delays to spike times
        delayed_times = spike_times_pre.unsqueeze(-1) + self.delay.unsqueeze(0)
        
        # Apply synaptic weights (simplified - in practice use proper SNN dynamics)
        weighted_currents = delayed_times * self.weight.unsqueeze(0)
        
        return weighted_currents.sum(dim=1)
```

**Step 2: Convolutional Layer for SNN**
```python
class ConvSNNLayer(nn.Module):
    """
    Convolutional layer with spiking neurons
    """
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0):
        super().__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding)
        self.bn = nn.BatchNorm2d(out_channels)
        
    def forward(self, x, mem, threshold=1.0):
        """
        Forward pass with LIF neuron dynamics
        
        Args:
            x: Input spikes (batch, in_channels, H, W)
            mem: Membrane potential (batch, out_channels, H', W')
            threshold: Firing threshold
        
        Returns:
            spikes: Output spikes
            new_mem: Updated membrane potential
        """
        # Convolution
        current = self.conv(x)
        current = self.bn(current)
        
        # LIF dynamics: dV/dt = -V/τ + I
        tau = 10.0  # ms
        dt = 1.0    # ms
        alpha = np.exp(-dt / tau)
        
        new_mem = alpha * mem + (1 - alpha) * current
        
        # Spike generation
        spikes = (new_mem >= threshold).float()
        new_mem = new_mem * (1 - spikes)  # Reset
        
        return spikes, new_mem
```

**Step 3: Delay Learning with Modified STDP**
```python
class DelaySTDP:
    """
    STDP with joint weight and delay learning
    """
    def __init__(self, A_plus=0.01, A_minus=0.01, tau_plus=20, tau_minus=20, 
                 eta_d=0.001, d_min=1, d_max=20):
        self.A_plus = A_plus
        self.A_minus = A_minus
        self.tau_plus = tau_plus
        self.tau_minus = tau_minus
        self.eta_d = eta_d  # Delay learning rate
        self.d_min = d_min
        self.d_max = d_max
    
    def update(self, pre_times, post_times, weights, delays):
        """
        Apply STDP updates for weights and delays
        
        Args:
            pre_times: (n_neurons,) pre-synaptic spike times
            post_times: (n_neurons,) post-synaptic spike times
            weights: (n_pre, n_post) current weights
            delays: (n_pre, n_post) current delays
        
        Returns:
            delta_w: Weight updates
            delta_d: Delay updates
        """
        n_pre, n_post = weights.shape
        delta_w = torch.zeros_like(weights)
        delta_d = torch.zeros_like(delays)
        
        for i in range(n_pre):
            for j in range(n_post):
                # Effective time difference (accounting for delay)
                if pre_times[i] > 0 and post_times[j] > 0:
                    dt = post_times[j] - (pre_times[i] + delays[i, j])
                    
                    # Weight update (classic STDP)
                    if dt > 0:  # Pre before post -> LTP
                        dw = self.A_plus * np.exp(-dt / self.tau_plus)
                    else:  # Post before pre -> LTD
                        dw = -self.A_minus * np.exp(dt / self.tau_minus)
                    
                    delta_w[i, j] = dw
                    
                    # Delay update (proportional to weight change)
                    # Delays change in direction that strengthens connection
                    d_normalized = (delays[i, j] - self.d_min) / (self.d_max - self.d_min)
                    delta_d[i, j] = self.eta_d * dw * d_normalized * (1 - d_normalized)
        
        return delta_w, delta_d
```

**Step 4: Recurrent Layer with Delays**
```python
class RecurrentDelaySNN(nn.Module):
    """
    Recurrent SNN layer with delay-enabled connections
    """
    def __init__(self, n_neurons, recurrent=True, d_min=1, d_max=20):
        super().__init__()
        self.n_neurons = n_neurons
        self.recurrent = recurrent
        
        # Input synapses
        self.input_syn = DelaySynapse(n_neurons, n_neurons, d_min, d_max)
        
        # Recurrent synapses (if enabled)
        if recurrent:
            self.rec_syn = DelaySynapse(n_neurons, n_neurons, d_min, d_max)
        
        # Membrane parameters
        self.tau_mem = 10.0
        self.v_threshold = 1.0
        self.v_reset = 0.0
        
    def forward(self, x, mem, hidden_spikes=None):
        """
        Forward pass with recurrent connections
        
        Args:
            x: Input spikes (batch, n_neurons)
            mem: Membrane potential (batch, n_neurons)
            hidden_spikes: Previous layer spikes for recurrence
        
        Returns:
            spikes: Output spikes
            new_mem: Updated membrane potential
        """
        # Input current
        i_in = self.input_syn(x)
        
        # Recurrent current
        if self.recurrent and hidden_spikes is not None:
            i_rec = self.rec_syn(hidden_spikes)
            i_total = i_in + i_rec
        else:
            i_total = i_in
        
        # LIF dynamics
        alpha = np.exp(-1.0 / self.tau_mem)
        new_mem = alpha * mem + (1 - alpha) * i_total
        
        # Spike generation
        spikes = (new_mem >= self.v_threshold).float()
        new_mem = torch.where(spikes > 0, 
                             torch.ones_like(new_mem) * self.v_reset,
                             new_mem)
        
        return spikes, new_mem
```

**Step 5: Complete Conv-Delay-SNN Model**
```python
class ConvDelaySNN(nn.Module):
    """
    Complete Convolutional SNN with Delay Learning
    """
    def __init__(self, input_shape, n_classes, conv_config, recurrent_units=128):
        super().__init__()
        
        # Convolutional feature extractor
        self.conv_layers = nn.ModuleList()
        in_ch = input_shape[0]
        for out_ch, kernel, stride in conv_config:
            self.conv_layers.append(
                ConvSNNLayer(in_ch, out_ch, kernel, stride)
            )
            in_ch = out_ch
        
        # Calculate flattened size
        with torch.no_grad():
            dummy = torch.zeros(1, *input_shape)
            for layer in self.conv_layers:
                dummy, _ = layer(dummy, torch.zeros_like(dummy))
            self.flat_size = dummy.view(1, -1).shape[1]
        
        # Recurrent SNN with delays
        self.recurrent_snn = RecurrentDelaySNN(recurrent_units, recurrent=True)
        
        # Readout layer
        self.readout = nn.Linear(recurrent_units, n_classes)
        
    def forward(self, x, time_steps=100):
        """
        Forward pass over time
        
        Args:
            x: Input (batch, channels, H, W)
            time_steps: Number of time steps to simulate
        
        Returns:
            output: Class predictions (batch, n_classes)
        """
        batch_size = x.shape[0]
        
        # Initialize states
        conv_mems = [torch.zeros(batch_size, layer.conv.out_channels, 
                                 x.shape[2]//layer.conv.stride[0], 
                                 x.shape[3]//layer.conv.stride[1])
                     for layer in self.conv_layers]
        rec_mem = torch.zeros(batch_size, self.recurrent_snn.n_neurons)
        rec_spikes = torch.zeros(batch_size, self.recurrent_snn.n_neurons)
        
        spike_record = []
        
        for t in range(time_steps):
            # Encode input as spikes (rate coding example)
            input_spikes = (torch.rand_like(x) < x).float()
            
            # Convolutional layers
            conv_out = input_spikes
            for i, layer in enumerate(self.conv_layers):
                conv_out, conv_mems[i] = layer(conv_out, conv_mems[i])
            
            # Flatten and project to recurrent layer
            flat = conv_out.view(batch_size, -1)
            
            # Project to recurrent dimension (simplified - use proper projection)
            if flat.shape[1] != self.recurrent_snn.n_neurons:
                if not hasattr(self, 'proj'):
                    self.proj = nn.Linear(flat.shape[1], self.recurrent_snn.n_neurons)
                flat = self.proj(flat)
            
            # Recurrent SNN
            rec_spikes, rec_mem = self.recurrent_snn(flat, rec_mem, rec_spikes)
            spike_record.append(rec_spikes)
        
        # Decode: rate-to-value (sum spikes over time)
        spike_sum = torch.stack(spike_record, dim=1).sum(dim=1)
        output = self.readout(spike_sum)
        
        return output
```

## Applications

### 1. Spatiotemporal Pattern Recognition
- Gesture recognition from event camera data
- Audio pattern classification with precise timing

### 2. Sequential Memory Tasks
- Time series prediction with SNNs
- Working memory for cognitive tasks

### 3. Neuromorphic Robotics
- Sensorimotor integration with precise timing
- Real-time pattern recognition on edge devices

### 4. Brain-Inspired Computing
- Models of cortical microcircuits with synaptic delays
- Understanding temporal processing in biological neural networks

## Pitfalls

### 1. Delay Bounds
- **Issue**: Delays must be bounded; unbounded delays cause instability
- **Mitigation**: Use sigmoid or clamp to enforce [d_min, d_max]

### 2. Learning Rate Balance
- **Issue**: Weight and delay learning rates need careful tuning
- **Mitigation**: η_d should be 10-100x smaller than weight learning rate

### 3. Temporal Resolution
- **Issue**: Fine-grained delays require high temporal resolution
- **Mitigation**: Use temporal interpolation or event-based simulation

### 4. Hardware Implementation
- **Issue**: Precise analog delays difficult to implement on digital hardware
- **Mitigation**: Use digital delay lines or approximate with buffer chains

## Related Skills
- multiplication-free-spike-time-fpga
- snn-fpga-hardware-software-codesign
- stdp-synaptic-delay-learning
- working-memory-heterogeneous-delays

## References
```bibtex
@article{zebendo2026combining,
  title={Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks},
  author={Zebendo, Lúcio Folly Sanches and Cicciarella, Eleonora and Rossi, Michele},
  journal={arXiv preprint arXiv:2604.15997},
  year={2026}
}
```
