---
name: conv-delay-learning-recurrent-snn
description: "Convolutional delay learning in recurrent spiking neural networks. Extends DelRec with convolutive recurrent connections for 99% parameter reduction and 52x faster inference in audio classification. Activation: convolutional delay learning, DelRec SNN, delay learning spiking, conv recurrent SNN, efficient SNN architecture"
---

# Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks

## Overview

This skill implements convolutional delay learning in recurrent SNNs, extending the DelRec framework. By advocating the use of convolutional recurrent connections alongside delay learning mechanisms, it achieves:
- **~99% parameter reduction** in recurrent connections
- **52x faster inference time**
- Retains the accuracy of full delay learning

## Source Paper

- **Title**: Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks
- **Authors**: See arXiv:2604.15997
- **arXiv**: https://arxiv.org/abs/2604.15997
- **Published**: 2026-04-17
- **Categories**: cs.NE

## Core Concepts

### 1. DelRec (Delay Learning in Recurrent SNNs)

DelRec learns axonal delays at runtime alongside other network parameters:
- Each connection has an associated delay that is trainable
- Delays are updated via gradient-based learning
- Captures temporal dependencies more efficiently than dense recurrent connections

### 2. Convolutional Recurrent Connections

Key innovation: replace dense recurrent weight matrices with convolutional operations:
- **Shared weights** across time steps and feature dimensions
- **Temporal convolutions** replace dense recurrent connections
- **Sparse connectivity** pattern inherent in convolutions
- **Local receptive fields** instead of global connectivity

### 3. Parameter Efficiency

| Metric | DelRec (Dense) | Conv-DelRec |
|--------|---------------|-------------|
| Recurrent Parameters | 100% | ~1% |
| Inference Speed | 1x | 52x |
| Accuracy | Baseline | Same |
| Memory Footprint | Full | ~1% |

## Implementation

```python
import numpy as np
import torch
import torch.nn as nn

class ConvDelayRecurrentSNN(nn.Module):
    """
    Convolutional Delay Learning in Recurrent SNN.
    
    Combines convolutive recurrent connections with
    trainable axonal delays (DelRec extension).
    """
    
    def __init__(self, input_dim, hidden_dim, output_dim,
                 n_delay_channels=4, conv_kernel_size=3):
        super().__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.n_delay_channels = n_delay_channels
        self.conv_kernel_size = conv_kernel_size
        
        # Feedforward weights
        self.input_proj = nn.Linear(input_dim, hidden_dim)
        
        # Convolutional recurrent connection
        # Replaces dense recurrent matrix: hidden_dim x hidden_dim
        # With convolution: much fewer parameters
        self.conv_recurrent = nn.Conv1d(
            in_channels=hidden_dim,
            out_channels=hidden_dim,
            kernel_size=conv_kernel_size,
            padding=conv_kernel_size // 2,
            bias=False
        )
        
        # Delay channels for temporal processing
        # Each channel represents a different delay
        self.delay_channels = nn.Parameter(
            torch.randn(n_delay_channels, hidden_dim) * 0.1
        )
        
        # Readout
        self.output_proj = nn.Linear(hidden_dim, output_dim)
        
        # LIF neuron parameters
        self.tau_m = 20.0  # Membrane time constant (ms)
        self.threshold = 1.0
        self.reset_potential = 0.0
        
    def lif_step(self, v, spike):
        """LIF neuron step with reset."""
        # Decay membrane potential
        alpha = np.exp(-1.0 / self.tau_m)
        v = v * alpha
        
        # Spike generation
        spike = (v >= self.threshold).float()
        v = v * (1 - spike) + self.reset_potential * spike
        
        return v, spike
    
    def forward(self, x, n_timesteps):
        """
        Forward pass with convolutional delay learning.
        
        Args:
            x: Input tensor [batch, time, features]
            n_timesteps: Number of time steps to simulate
        """
        batch_size = x.shape[0]
        
        # Initialize membrane potentials
        v = torch.zeros(batch_size, self.hidden_dim, device=x.device)
        spikes = []
        
        # Process input sequence
        for t in range(n_timesteps):
            # Get input at current time step
            if t < x.shape[1]:
                inp = x[:, t, :]
            else:
                inp = torch.zeros(batch_size, self.input_dim, device=x.device)
            
            # Feedforward projection
            feedforward = self.input_proj(inp)
            
            # Convolutional recurrent processing
            # Apply convolution on the hidden state
            if len(spikes) > 0:
                recent = torch.stack(spikes[-self.conv_kernel_size:], dim=1)
                # recent: [batch, kernel_size, hidden_dim]
                recent = recent.permute(0, 2, 1)  # [batch, hidden, kernel]
                recurrent = self.conv_recurrent(recent)
                recurrent = recurrent.sum(dim=1)  # Sum over output channels
            else:
                recurrent = torch.zeros_like(v)
            
            # Delay channel processing
            delay_contribution = torch.zeros(batch_size, self.hidden_dim, device=x.device)
            for i in range(self.n_delay_channels):
                # Each delay channel contributes at different time lags
                if len(spikes) > i + 1:
                    delay_contribution += self.delay_channels[i] * spikes[-(i+1)]
            
            # Update membrane potential
            v = v + feedforward + recurrent + delay_contribution
            
            # LIF neuron update
            v, spike = self.lif_step(v, torch.zeros_like(v))
            spike = (v >= self.threshold).float()
            v = v * (1 - spike)
            
            spikes.append(spike)
        
        # Output from accumulated spikes
        output = torch.stack(spikes).mean(dim=0)
        return self.output_proj(output)


# === Audio Classification Example ===
class ConvDelayAudioClassifier(nn.Module):
    """Audio classification using Conv-Delay Learning SNN."""
    
    def __init__(self, n_mel_bins=64, n_classes=10, hidden_dim=128):
        super().__init__()
        self.snn = ConvDelayRecurrentSNN(
            input_dim=n_mel_bins,
            hidden_dim=hidden_dim,
            output_dim=n_classes,
            n_delay_channels=4,
            conv_kernel_size=5
        )
    
    def forward(self, mel_spectrogram):
        """
        Args:
            mel_spectrogram: [batch, time, mel_bins]
        """
        n_timesteps = mel_spectrogram.shape[1]
        return self.snn(mel_spectrogram, n_timesteps)
```

## Practical Applications

### 1. Audio Classification
Deploy on resource-constrained edge devices for:
- Keyword spotting
- Environmental sound classification
- Music genre classification

### 2. Temporal Pattern Recognition
Any task requiring efficient temporal processing:
- Time series classification
- Sequential data processing
- Event-based vision processing

### 3. Edge AI Systems
Perfect for deployment on:
- Microcontrollers (MCUs)
- Edge TPUs
- Neuromorphic hardware

## Key Insights

1. **Convolution > Dense**: Convolutional recurrent connections dramatically reduce parameters while maintaining accuracy
2. **Delay + Conv is Synergistic**: The combination of delay learning and convolutions captures temporal structure more efficiently than either alone
3. **52x Speedup**: The architectural change enables real-time inference on edge hardware
4. **Drop-in Replacement**: Can be used as a drop-in replacement for standard RNN/LSTM in SNN architectures

## Related Skills
- [[conv-delay-learning-snn]]
- [[snn-learning-survey]]
- [[spiking-neural-network-analysis]]

## Activation Keywords
- convolutional delay learning
- DelRec SNN
- delay learning spiking
- conv recurrent SNN
- efficient SNN architecture
- audio SNN classification
- parameter-efficient SNN
