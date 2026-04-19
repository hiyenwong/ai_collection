---
name: spiking-compositional-neural-operator
description: "Spiking Compositional Neural Operator (SCNO) - 模块化脉冲神经算子架构，用于PDE求解。通过组合基础微分算子块解决耦合PDE，实现零遗忘模块化扩展。适用于科学计算、PDE代理模型、神经形态计算、核工程仿真。Activation: spiking neural operator, compositional, PDE solving, modular neural network, DeepONet, zero-forgetting, neuromorphic computing"
version: 1.0.0
metadata:
  hermes:
    tags: [spiking, neural-operator, PDE, modular, zero-forgetting, compositional]
    source_paper: "SCNO: Spiking Compositional Neural Operator -- Towards a Neuromorphic Foundation Model for Nuclear PDE Solving (arXiv:2604.11625)"
    authors: "Samrendra Roy, Souvik Chakraborty, Rizwan-uddin, Syed Bahauddin Alam"
    published: "2026-04-13"
---

# Spiking Compositional Neural Operator (SCNO)

## Overview

SCNO is a **modular spiking neural operator architecture** that solves partial differential equations (PDEs) by composing small specialized blocks, each trained on a single elementary differential operator. This approach addresses three key limitations of existing neural operators: monolithic training, GPU dependency, and catastrophic forgetting when adding new physics.

**Source Paper**: arXiv:2604.11625 (2026-04-13)

## Core Concepts

### 1. Modular Operator Library
SCNO maintains a library of small spiking neural operator blocks:
- **Convection block**: Handles transport/advection terms
- **Diffusion block**: Handles diffusive processes
- **Reaction block**: Handles reactive/source terms

Each block is trained independently on its corresponding elementary operator.

### 2. Input-Conditioned Aggregator
A lightweight aggregator composes the pre-trained blocks to solve coupled PDEs not seen during individual block training:
```
f_total = Σ_i w_i(x) · block_i(input)
```
where weights `w_i(x)` are conditioned on the input PDE characteristics.

### 3. Correction Network for Cross-Coupling
A small correction network learns cross-coupling residuals between blocks:
- All base blocks remain **frozen** during correction training
- Preserves zero-forgetting property by construction
- Only 95K trainable parameters vs 462K for monolithic baseline

### 4. Zero-Forgetting Modular Expansion
New physics can be added by training a new block without retraining existing ones:
- Existing blocks are frozen
- Only correction network needs updating
- No catastrophic forgetting

## Implementation

### SCNO Architecture

```python
import torch
import torch.nn as nn

class SpikingOperatorBlock(nn.Module):
    """Single spiking neural operator block for one elementary operator."""
    
    def __init__(self, in_dim=2, hidden_dim=64, out_dim=1, num_spiking_layers=3):
        super().__init__()
        self.encoder = nn.Linear(in_dim, hidden_dim)
        self.spiking_layers = nn.ModuleList([
            SpikingLIF(hidden_dim) for _ in range(num_spiking_layers)
        ])
        self.decoder = nn.Linear(hidden_dim, out_dim)
        
    def forward(self, x, timesteps=10):
        h = self.encoder(x)
        for layer in self.spiking_layers:
            h = layer(h, timesteps)
        return self.decoder(h)


class InputConditionedAggregator(nn.Module):
    """Lightweight aggregator that composes blocks based on input."""
    
    def __init__(self, num_blocks, in_dim, hidden_dim=32):
        super().__init__()
        self.weight_net = nn.Sequential(
            nn.Linear(in_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_blocks),
            nn.Softmax(dim=-1)  # Normalized block weights
        )
        
    def forward(self, x):
        return self.weight_net(x)  # [batch, num_blocks]


class CorrectionNetwork(nn.Module):
    """Small network for learning cross-coupling residuals."""
    
    def __init__(self, in_dim=2, hidden_dim=32, out_dim=1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, out_dim)
        )
        
    def forward(self, x):
        return self.net(x)


class SCNO(nn.Module):
    """Spiking Compositional Neural Operator."""
    
    def __init__(self, operator_types=['convection', 'diffusion', 'reaction'],
                 in_dim=2, out_dim=1):
        super().__init__()
        
        # Modular operator library
        self.blocks = nn.ModuleDict({
            op: SpikingOperatorBlock(in_dim, hidden_dim=64, out_dim=out_dim)
            for op in operator_types
        })
        
        # Aggregator
        num_blocks = len(operator_types)
        self.aggregator = InputConditionedAggregator(num_blocks, in_dim)
        
        # Correction network
        self.correction = CorrectionNetwork(in_dim, hidden_dim=32, out_dim=out_dim)
        
    def forward(self, x, use_correction=True, timesteps=10):
        # Get block outputs
        block_outputs = []
        for block in self.blocks.values():
            block_outputs.append(block(x, timesteps))
        
        block_outputs = torch.stack(block_outputs, dim=-1)  # [batch, out, num_blocks]
        
        # Aggregate
        weights = self.aggregator(x)  # [batch, num_blocks]
        aggregated = torch.sum(block_outputs * weights.unsqueeze(-2), dim=-1)
        
        # Add correction
        if use_correction:
            aggregated = aggregated + self.correction(x)
        
        return aggregated
    
    def freeze_blocks(self):
        """Freeze all operator blocks for zero-forgetting training."""
        for block in self.blocks.values():
            for param in block.parameters():
                param.requires_grad = False
        for param in self.aggregator.parameters():
            param.requires_grad = False
```

### Training Pipeline

```python
def train_scno_modular():
    """Two-phase training for SCNO."""
    
    # Phase 1: Train individual blocks
    for op_name, block in model.blocks.items():
        train_single_block(block, operator_data[op_name])
    
    # Phase 2: Freeze blocks, train aggregator + correction
    model.freeze_blocks()
    train_aggregator_and_correction(
        model.aggregator, 
        model.correction, 
        coupled_pde_data
    )
```

## Applications

### 1. Nuclear Engineering
- 1-group neutron diffusion equation solving
- Multi-physics coupled simulations
- Real-time reactor analysis

### 2. Scientific Computing
- PDE surrogate modeling
- Multi-physics problems (convection-diffusion-reaction)
- Real-time simulation for control systems

### 3. Neuromorphic Hardware
- Deploy on spiking neuromorphic chips
- Energy-efficient PDE solving at edge
- Real-time physics simulation on low-power devices

## Performance

| Metric | SCNO | Monolithic Spiking DeepONet | ANN DeepONet |
|--------|------|----------------------------|--------------|
| Parameters | 95K | 462K | Varies |
| Coupled PDE accuracy | Best (4/5 cases) | Up to 62% worse | Up to 65% worse |
| Forgetting | Zero | N/A | N/A |
| Modularity | Yes | No | No |

## Key Advantages

1. **Parameter efficiency**: 5x fewer trainable parameters than monolithic
2. **Zero-forgetting**: Add new physics without retraining
3. **Compositional generalization**: Solve unseen coupled PDEs
4. **Neuromorphic compatibility**: Spiking components for energy-efficient deployment

## Limitations

- Requires pre-training individual operator blocks
- Correction network capacity limits coupling complexity
- Currently validated on 1D/2D problems

## References

- Roy, S. et al. (2026). "SCNO: Spiking Compositional Neural Operator -- Towards a Neuromorphic Foundation Model for Nuclear PDE Solving." arXiv:2604.11625.

## Activation Keywords

- spiking compositional neural operator
- SCNO
- modular PDE solving
- neural operator
- zero-forgetting
- DeepONet spiking
- neuromorphic PDE
- operator learning
- 脉冲神经算子
- 模块化PDE求解

## Related Skills

- [[spiking-neural-network-analysis]]
- [[learning-neuron-dynamics-deep-snn]]
- [[data-driven-moving-horizon-estimation]]
