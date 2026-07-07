---
name: cortico-cerebellar-modularity-rnn
description: >
  Cortico-cerebellar modular RNN architecture methodology. Augments RNNs with
  cerebellar-inspired feedforward modules for efficient temporal learning.
  The cortical RNN acts as a fixed reservoir while the cerebellar module drives
  learning efficiency. Applicable to temporal sequence learning, neural network
  architecture design, and brain-inspired AI systems.
  Activation: cortico-cerebellar, cerebellar RNN, CB-RNN, cortical-cerebellar,
  modular RNN, temporal learning architecture, brain-inspired RNN, fixed reservoir,
  heterogeneous modularity, cerebellar module, architectural inductive bias
---

# Cortico-Cerebellar Modular RNN Architecture

Based on: Voce, Giannakakis & Clopath (2026) arXiv:2605.10356

## Core Finding

Augmenting an RNN with a cerebellar-inspired feedforward module (CB-RNN) enables
faster learning and higher performance than fully recurrent baselines. After minimal
training of the recurrent core, freezing it and delegating subsequent learning to the
cerebellar module preserves efficiency.

## Architecture

```
Input → [Cortical RNN (frozen reservoir)] → [Cerebellar Feedforward Module] → Output
```

- **Cortical RNN**: Recurrent core that processes temporal context, trained briefly
  then frozen as a fixed reservoir
- **Cerebellar Module**: Feedforward module that receives cortical representations
  and performs the primary adaptive learning

## Key Principles

1. **Heterogeneous Modularity**: Different module types serve distinct computational roles
2. **Fixed Reservoir**: Cortical RNN need not be fully trained; frozen weights still provide
   rich temporal representations
3. **Delegated Learning**: Cerebellar module absorbs subsequent learning, enabling rapid
   adaptation without destabilizing core representations
4. **Structural Inductive Bias**: Architecture itself encodes priors that accelerate learning

## Implementation Pattern

```python
import torch
import torch.nn as nn

class CerebellarModule(nn.Module):
    """Feedforward module mimicking cerebellar learning."""
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        return self.fc2(self.relu(self.fc1(x)))

class CorticalRNN(nn.Module):
    """Recurrent cortical core (frozen after warmup)."""
    def __init__(self, input_dim, hidden_dim):
        super().__init__()
        self.rnn = nn.RNN(input_dim, hidden_dim, batch_first=True)
    
    def forward(self, x, h0=None):
        return self.rnn(x, h0)

class CBRNN(nn.Module):
    """Cortico-cerebellar RNN architecture."""
    def __init__(self, input_dim, cortical_dim, cerebellar_dim, output_dim):
        super().__init__()
        self.cortex = CorticalRNN(input_dim, cortical_dim)
        self.cerebellum = CerebellarModule(cortical_dim, cerebellar_dim, output_dim)
    
    def forward(self, x, warmup=False):
        # Cortical processing
        cortex_out, h_n = self.cortex(x)
        # Cerebellar readout
        output = self.cerebellum(cortex_out)
        return output, h_n
    
    def freeze_cortex(self):
        """Freeze cortical weights after warmup phase."""
        for param in self.cortex.parameters():
            param.requires_grad = False

# Usage:
# 1. Warmup: train both cortex and cerebellum for N epochs
# 2. Freeze: model.freeze_cortex()
# 3. Continue: train only cerebellar module
```

## Training Protocol

1. **Warmup Phase**: Train full CB-RNN on target task (few epochs)
2. **Freeze Cortex**: Set `requires_grad=False` on cortical RNN parameters
3. **Cerebellar Learning**: Continue training with only cerebellar module gradients

## Advantages Over Baselines

- **Faster convergence**: Cerebellar module adapts more rapidly than full RNN retraining
- **Higher performance**: Surpasses parameter-matched fully recurrent networks
- **Stability**: Freezing core prevents catastrophic forgetting during adaptation
- **Energy efficiency**: Fewer trainable parameters during deployment phase

## Applications

- Temporal sequence prediction
- Continuous learning scenarios
- Brain-inspired neural architectures
- Robotics control with temporal dependencies
- Speech and language processing

## Related Skills

- `spiking-bandpass-wavelet-encoding` - Spiking temporal encoding
- `working-memory-heterogeneous-delays` - Working memory in SNNs
- `brain-inspired-snn-pattern-analysis` - Brain-inspired computing patterns

## ArXiv Reference

- **Paper**: arXiv:2605.10356v1
- **Title**: Cortico-cerebellar modularity as an architectural inductive bias for efficient temporal learning
- **Authors**: Alexandra Voce, Emmanouil Giannakakis, Claudia Clopath
- **Date**: 2026-05-11
- **Categories**: q-bio.NC
