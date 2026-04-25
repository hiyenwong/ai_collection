---
name: hierarchical-connectome-ssm
description: "Parallelized Hierarchical Connectome (PHC) - A spatiotemporal recurrent framework that upgrades temporal-only State-Space Models (SSMs) into spatiotemporal recurrent networks with spiking neural dynamics. Enables O(logT) parallel training while enforcing biological constraints including Dale's Law, short-term plasticity, and reward-modulated STDP. Activation: hierarchical connectome, spiking SSM, PHC, spatiotemporal recurrent, 脉冲状态空间模型, parallelized connectome, SSN-SSM integration."
---

# Parallelized Hierarchical Connectome for Spiking State-Space Models

## Overview

This skill provides the Parallelized Hierarchical Connectome (PHC) framework that bridges State-Space Models (SSMs) with biologically-plausible spiking neural networks. PHC enables:

- **Spatiotemporal Recurrence**: Extends temporal-only SSMs with lateral/feedback connections within each timestep
- **Biological Constraints**: Enforces Dale's Law, adaptive leaky integrate-and-fire dynamics, short-term plasticity, and reward-modulated STDP
- **Parallel Efficiency**: Maintains O(logT) parallel scan complexity despite spatial recurrence
- **Parameter Efficiency**: Reduces complexity from Θ(D²L) to Θ(D²) compared to stacked SSM architectures

## When to Use This Skill

Use this skill when:
- Building spiking neural networks with efficient parallel training
- Integrating neuro-physical priors into sequence models
- Modeling multivariate time-series with spatial dependencies
- Developing parameter-efficient recurrent architectures with biological plausibility

## Core Architecture

### PHC Framework Components

```
Input Sequence → [Neuron Layer] ↔ [Synapse Layer] → Output
                    ↕
            [Connectome Topology]
                    ↕
         [Multi-Transmission Loop]
```

1. **Neuron Layer**: Shared layer where diagonal SSM core maps to spiking neurons
2. **Synapse Layer**: Inter-neuronal communication layer with hierarchical organization
3. **Connectome Topology**: Partitions neurons into hierarchical regions
4. **Multi-Transmission Loop**: Enables intra-slice spatial recurrence preserving O(logT) parallelism

### Biological Constraints Enforced

| Constraint | Implementation |
|------------|----------------|
| Dale's Law | Separate excitatory/inhibitory neuron populations |
| Adaptive LIF | Dynamic threshold based on firing history |
| Short-term Plasticity | Tsodyks-Markram synaptic dynamics |
| Reward-modulated STDP | Eligibility traces with neuromodulation |

## Workflow

### Step 1: Define Connectome Topology

```python
import torch
import torch.nn as nn

class ConnectomeTopology:
    def __init__(self, n_regions, neurons_per_region):
        self.n_regions = n_regions
        self.neurons_per_region = neurons_per_region
        # Define hierarchical connectivity matrix
        self.connectivity = self._build_hierarchical_connections()
    
    def _build_hierarchical_connections(self):
        # Implement hierarchical region-to-region connectivity
        # Higher regions connect to lower regions in a tree-like structure
        pass
```

### Step 2: Implement Multi-Transmission Loop

```python
class MultiTransmissionLoop(nn.Module):
    def __init__(self, hidden_dim, n_regions):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.n_regions = n_regions
        # Intra-slice recurrence within each temporal window
        self.spatial_recurrent = nn.Linear(hidden_dim, hidden_dim)
    
    def forward(self, x, time_slice):
        # x: [batch, hidden_dim]
        # Apply spatial recurrence while maintaining parallel scan compatibility
        return self.spatial_recurrent(x)
```

### Step 3: Build PHCSSM Model

```python
class PHCSSM(nn.Module):
    def __init__(self, input_dim, hidden_dim, n_regions, connectome):
        super().__init__()
        self.connectome = connectome
        # Diagonal SSM core (parallelizable)
        self.ssm_core = DiagonalSSM(hidden_dim)
        # Spiking neuron layer
        self.neuron_layer = AdaptiveLIFLayer(hidden_dim)
        # Synaptic layer with Dale's Law
        self.synapse_layer = DaleSynapseLayer(hidden_dim, connectome)
        
    def forward(self, input_seq):
        # Parallel scan for temporal dimension
        # Spatial recurrence through connectome
        # Spiking dynamics with biological constraints
        pass
```

### Step 4: Training with Biological Constraints

```python
# Training loop with reward-modulated STDP
optimizer = torch.optim.Adam(phcssm.parameters())

for batch in dataloader:
    output, spikes = phcssm(batch['input'])
    
    # Standard loss
    loss = criterion(output, batch['target'])
    
    # Add biological regularization
    bio_loss = enforce_dales_law(phcssm)
    
    total_loss = loss + 0.1 * bio_loss
    total_loss.backward()
    optimizer.step()
```

## Implementation Guidelines

### Key Design Decisions

1. **Diagonal SSM Core**: Use structured state matrices (e.g., HiPPO, DPLR) for long-range dependencies
2. **Region Partitioning**: Group neurons by functional similarity or anatomical location
3. **Plasticity Rules**: Implement eligibility traces for reward-modulated learning
4. **Spike Encoding**: Use rate coding or temporal coding depending on task requirements

### Performance Considerations

- Use parallel scan operations (associative scan) for O(logT) training
- Implement sparse connectivity patterns based on connectome topology
- Cache intermediate states for efficient backpropagation through time

## Applications

### Physiological Time-Series (UEA Benchmarks)

- ECG/EEG classification
- Motion recognition from IMU sensors
- Neural decoding from multi-channel recordings

### Computational Neuroscience

- Large-scale brain network simulation
- Connectome-constrained neural modeling
- Neuromorphic algorithm development

## Resources

- **Paper**: "Parallelized Hierarchical Connectome: A Spatiotemporal Recurrent Framework for Spiking State-Space Models" (arXiv:2604.01295v1)
- **PDF**: https://arxiv.org/pdf/2604.01295v1

## References

1. Gu, A., et al. (2022). Efficiently modeling long sequences with structured state spaces.
2. Zenke, F., & Vogels, T. P. (2021). The remarkable robustness of surrogate gradient learning.
3. Bellec, G., et al. (2020). A solution to the learning dilemma for recurrent networks.

## Activation Keywords

- hierarchical connectome
- spiking SSM  
- PHC framework
- spatiotemporal recurrent
- parallelized connectome
- 脉冲状态空间模型
- SNN-SSM integration
- biological SSM
