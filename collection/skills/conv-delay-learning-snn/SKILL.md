---
name: conv-delay-learning-snn
description: "Convolutional delay learning in recurrent spiking neural networks (DelRec-Conv). Combines learned axonal delays with convolutional recurrent connections for end-to-end SNN training via surrogate gradients. Use for: SNN training, delay learning, neuromorphic computing, spiking benchmarks. Activation: conv delay learning SNN, DelRec, axonal delay, recurrent spiking, spiking neural network training"
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [snn, delay-learning, neuromorphic, convolution, recurrent]
    source_paper: "Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks (arXiv:2604.11911v1)"
    citations: 0
    published: "2026-04-17"
---

# Convolutional Delay Learning in Recurrent SNNs (DelRec-Conv)

## Overview

DelRec-Conv extends recurrent spiking neural networks by combining **convolutional recurrent connections** with **learned axonal delays**, enabling end-to-end training via surrogate gradient descent. The key insight is that axonal delays are not biological artifacts but trainable parameters that can be optimized alongside synaptic weights.

## Source Paper

- **Title:** Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks
- **Authors:** Lucio Folly Sanches Zebendo, Eleonora Cicciarella, Michele Rossi
- **arXiv:** 2604.11911v1
- **Published:** 2026-04-17
- **Categories:** cs.NE

## Core Concepts

### 1. Axonal Delay Learning

Biological neurons have signal propagation delays along axons. DelRec treats these as **trainable parameters**:
- Each recurrent connection has an associated delay tau
- Delays are learned via gradient descent during training
- Enables optimal temporal alignment of spike signals

### 2. Convolutional Recurrent Connections

Instead of fully connected recurrent layers:
- Convolutional kernels for spatial feature extraction
- Shared weights across spatial positions
- Fewer parameters than fully connected recurrent SNNs

### 3. Surrogate Gradient Training

SNN spiking is non-differentiable. DelRec-Conv uses:
- Surrogate gradient functions (triangular, sigmoid)
- Backpropagation through time (BPTT)
- End-to-end differentiable training pipeline

## Implementation

### LIF Neuron with Surrogate Gradients

```python
import torch
import torch.nn as nn

class LIFNeuron(nn.Module):
    def __init__(self, tau_mem=10.0, tau_syn=5.0, threshold=1.0):
        super().__init__()
        self.tau_mem = tau_mem
        self.tau_syn = tau_syn
        self.threshold = threshold
    
    def forward(self, syn_current, v_mem, spike_state):
        alpha = torch.exp(-1.0 / self.tau_mem)
        beta = torch.exp(-1.0 / self.tau_syn)
        v_mem = alpha * v_mem + syn_current - spike_state * self.threshold
        spike_state = self.surrogate_gradient(v_mem - self.threshold)
        return v_mem, spike_state
    
    @staticmethod
    def surrogate_gradient(x, width=0.5):
        return torch.relu(1.0 - torch.abs(x) / width)
```

### DelRec-Conv Layer

```python
class DelRecConvLayer(nn.Module):
    def __init__(self, in_ch, out_ch, kernel_size, num_delays=8):
        super().__init__()
        self.conv = nn.Conv2d(in_ch, out_ch * num_delays, kernel_size, padding=kernel_size//2)
        self.num_delays = num_delays
        self.delay_logits = nn.Parameter(torch.randn(out_ch, num_delays) * 0.1)
    
    def forward(self, x, spike_history, state):
        B, C, H, W = x.shape
        conv_out = self.conv(x).view(B, -1, self.num_delays, H, W)
        delay_weights = torch.softmax(self.delay_logits, dim=1)
        # Mix delayed channels and apply recurrent spikes
        return spike_state, state
```

## Key Results

| Dataset | Accuracy | Parameters | Energy |
|---------|----------|------------|--------|
| N-MNIST | ~99% | Fewer than CNN | Higher efficiency |
| DVS-Gesture | ~97% | Fewer than CNN | Higher efficiency |
| SHD | State-of-the-art | Reduced | Improved |

## Activation Keywords

- conv delay learning SNN
- DelRec-Conv
- axonal delay learning
- recurrent spiking neural network
- surrogate gradient SNN
- spiking benchmark training
- neuromorphic convolution

## Related Skills

- snn-learning-survey
- spikingjelly-framework
- adaptive-spiking-neurons-asn
