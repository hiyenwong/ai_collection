---
name: convolution-delay-recurrent-snn
description: "Combining convolution operations with learnable axonal delays in recurrent SNNs for efficient temporal processing. Uses structured delays as temporal filters, enabling rich temporal dynamics with fewer neurons. Activation: convolution delay learning, temporal SNN, axonal delay SNN, recurrent spiking convolution."
version: 1.0.0
metadata:
  hermes:
    source_paper: "Combining Convolution and Delay Learning in Recurrent SNNs (arXiv:2604.15997)"
    tags: [neuroscience, spiking, convolution, delay-learning, temporal-processing]
---

# Convolution and Delay Learning in Recurrent SNNs

## Source Paper
- **Title**: Combining Convolution and Delay Learning in Recurrent SNNs
- **arXiv**: 2604.15997
- **PDF**: https://arxiv.org/pdf/2604.15997

## Overview

Spiking neural networks are gaining momentum as an alternative to conventional ANNs in resource-constrained edge computing. This paper introduces a novel architecture that **combines convolution operations with learnable axonal delays** in recurrent SNNs, creating temporal filters that capture complex spatiotemporal patterns with fewer neurons and lower energy consumption.

## Core Concepts

### Convolutional Delay Learning
- Traditional SNNs use fixed delays or no delays
- Learnable delays act as temporal convolution kernels
- Each delay channel captures a different temporal frequency band
- Delays + weights form a 2D spatiotemporal filter

### Recurrent Temporal Processing
- Recurrent connections create feedback loops
- Delayed feedback creates oscillatory dynamics
- Self-organized temporal receptive fields emerge through training
- Multiple timescales coexist in the same network

### Efficiency Benefits
- Fewer neurons needed for equivalent temporal computation
- Event-driven: computation only on spike events
- Reduced memory bandwidth vs. traditional RNNs
- Naturally parallelizable on neuromorphic hardware

## Implementation Pattern

```python
import numpy as np
from scipy.signal import convolve

class ConvDelaySNN:
    """Convolutional SNN with learnable delays."""
    
    def __init__(self, n_channels, n_delays=16, kernel_size=3):
        self.n_channels = n_channels
        self.n_delays = n_delays
        self.kernel_size = kernel_size
        
        # Spatial convolution weights
        self.W_spatial = np.random.randn(n_channels, n_channels, 
                                          kernel_size, kernel_size) * 0.1
        
        # Temporal delay weights (learnable)
        self.W_temporal = np.random.randn(n_channels, n_delays) * 0.05
        
        # Delay values (initialized uniformly, then learned)
        self.delays = np.linspace(1, 20, n_delays).astype(int)
        
        # State
        self.membrane = np.zeros(n_channels)
        self.spike_buffer = np.zeros((n_channels, 21))  # max delay + 1
        
    def forward(self, input_spikes):
        """Forward pass with spatial convolution and temporal delays."""
        # Spatial convolution
        spatial_out = np.zeros(self.n_channels)
        for c_out in range(self.n_channels):
            for c_in in range(self.n_channels):
                # Simplified 1D convolution
                spatial_out[c_out] += np.sum(
                    input_spikes[c_in] * self.W_spatial[c_out, c_in]
                )
        
        # Temporal delay convolution
        temporal_out = np.zeros(self.n_channels)
        for d_idx, d in enumerate(self.delays):
            delayed_spikes = self.spike_buffer[:, min(d, 20)]
            temporal_out += self.W_temporal[:, d_idx] * delayed_spikes
        
        # Update membrane potential
        self.membrane = 0.9 * self.membrane + spatial_out + temporal_out
        
        # Spike generation
        output_spikes = (self.membrane > 1.0).astype(float)
        self.membrane *= (1 - output_spikes)
        
        # Update spike buffer
        self.spike_buffer = np.roll(self.spike_buffer, 1, axis=1)
        self.spike_buffer[:, 0] = output_spikes
        
        return output_spikes
    
    def train_delay(self, error_signal, lr=0.001):
        """Update delay weights based on error."""
        # Gradient through delay channels
        for d_idx in range(self.n_delays):
            d = self.delays[d_idx]
            delayed = self.spike_buffer[:, min(d, 20)]
            grad = error_signal * delayed
            self.W_temporal[:, d_idx] += lr * grad
```

## Training Methodology
- **Surrogate gradients**: Differentiable approximation of spike function
- **Delay gradient approximation**: Smooth relaxation of discrete delays
- **BPTT with delay-aware backprop**: Truncated BPTT through delay paths

## Applications
- **Temporal event detection**: Anomaly detection in time series
- **Audio processing**: Speech recognition on neuromorphic chips
- **Sensor fusion**: Multi-modal temporal alignment
- **Edge AI**: Low-power temporal pattern recognition

## Related Skills
- [[snn-working-memory-heterogeneous-delays]]
- [[spiking-neural-network-training]]
- [[physics-aware-spiking-har]]
