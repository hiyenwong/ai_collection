---
name: growing-neural-breadth-depth-time
description: >
  Differentiable cost terms for breadth, depth, and time in recurrent convolutional
  neural networks. Jointly optimizes spatial/temporal resource costs with task errors
  to produce adaptive computational graphs that grow organically through training.
triggers:
  - neural network growth
  - breadth depth time optimization
  - recurrent convolutional network
  - computational graph emergence
  - spatial temporal resource constraints
  - biologically plausible growth
  - network architecture optimization
  - reaction time neural correlates
category: ai_collection
tags:
  - neural-networks
  - recurrent-networks
  - computational-neuroscience
  - architecture-search
  - resource-constraints
  - q-bio-NC
---

# Growing a Neural Network in Breadth, Depth, and Time

## Overview

**Paper**: "Growing a Neural Network in Breadth, Depth, and Time"  
**Authors**: Eivinas Butkus, Kedar Garzón Gupta, Nikolaus Kriegeskorte  
**arXiv**: [2605.25174](https://arxiv.org/abs/2605.25174)  
**Published**: 2026-05-24  
**Categories**: q-bio.NC, cs.LG, cs.NE

## Core Methodology

This framework introduces **differentiable cost terms** for three orthogonal resource dimensions in neural networks:

1. **Breadth** — number of neurons/channels per layer
2. **Depth** — number of processing layers
3. **Time** — number of recurrent processing steps

These cost terms are jointly optimized with task errors during backpropagation, yielding diverse computational graphs that emerge organically through training.

## Key Contributions

### Differentiable Resource Cost Framework
- Define cost functions $$C_\text{breadth}$$, $$C_\text{depth}$$, $$C_\text{time}$$ as differentiable penalties
- Optimize: $$\mathcal{L} = \mathcal{L}_\text{task} + \lambda_B C_B + \lambda_D C_D + \lambda_T C_T$$
- Pressure weights $$\lambda$$ control trade-off priorities between dimensions

### Recurrent Convolutional Network Architecture
- Network modeled as a **finite subset of an infinite lattice**
- Each cell may connect to neighbors in spatial and temporal dimensions
- Allows organic emergence of hierarchical vs. iterative processing

### Key Empirical Findings
1. **Resource trade-offs**: All three resources (breadth, depth, time) can substitute for each other to achieve accuracy targets
2. **Complexity scaling**: Networks grow in all three dimensions as task complexity increases
3. **Adaptive temporal processing**: Networks spontaneously use more recurrent steps when inputs are occluded or ambiguous
4. **Reaction time correlates**: Model temporal usage correlates with human reaction time — biologically plausible!

## Implementation Guide

### Step 1: Define Resource Cost Terms

```python
import torch
import torch.nn as nn

class ResourceCostModule(nn.Module):
    """Differentiable resource cost for breadth, depth, and time."""
    
    def __init__(self, lambda_breadth=0.01, lambda_depth=0.01, lambda_time=0.01):
        super().__init__()
        self.lambda_b = lambda_breadth
        self.lambda_d = lambda_depth
        self.lambda_t = lambda_time
    
    def breadth_cost(self, activations_per_layer):
        """Cost proportional to average number of active channels."""
        return sum(a.abs().mean() for a in activations_per_layer) / len(activations_per_layer)
    
    def depth_cost(self, depth_gates):
        """Cost proportional to depth utilization."""
        return torch.stack(depth_gates).mean()
    
    def time_cost(self, time_steps_used):
        """Cost proportional to recurrent steps taken."""
        return time_steps_used.float().mean()
    
    def total_cost(self, activations, depth_gates, time_steps):
        return (self.lambda_b * self.breadth_cost(activations) +
                self.lambda_d * self.depth_cost(depth_gates) +
                self.lambda_t * self.time_cost(time_steps))
```

### Step 2: Recurrent Convolutional Network with Adaptive Steps

```python
class AdaptiveRecurrentConvNet(nn.Module):
    """Network that grows in breadth, depth, and time based on task demands."""
    
    def __init__(self, max_depth=8, max_time_steps=16, channels=64):
        super().__init__()
        self.max_depth = max_depth
        self.max_time_steps = max_time_steps
        
        # Depth gates — learnable binary-ish gates per layer
        self.depth_gates = nn.Parameter(torch.ones(max_depth))
        
        # Recurrent convolutional cells
        self.cells = nn.ModuleList([
            nn.Conv2d(channels, channels, 3, padding=1) 
            for _ in range(max_depth)
        ])
        
        # Confidence/halting network for adaptive time
        self.halt_net = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Flatten(),
            nn.Linear(channels, 1),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        activations = []
        time_used = []
        
        h = x
        for t in range(self.max_time_steps):
            for d, (gate, cell) in enumerate(zip(
                    torch.sigmoid(self.depth_gates), self.cells)):
                h = gate * cell(h) + (1 - gate) * h  # gated skip
                activations.append(h)
            
            # Adaptive halting
            halt_prob = self.halt_net(h)
            time_used.append(halt_prob)
            if halt_prob.mean() > 0.9 and not self.training:
                break
        
        return h, activations, self.depth_gates, torch.stack(time_used)
```

### Step 3: Joint Training with Resource Costs

```python
def train_step(model, optimizer, data, labels, cost_module):
    optimizer.zero_grad()
    
    output, activations, depth_gates, time_steps = model(data)
    
    # Task loss
    task_loss = nn.CrossEntropyLoss()(output, labels)
    
    # Resource costs
    resource_cost = cost_module.total_cost(activations, [depth_gates], time_steps)
    
    # Joint loss
    total_loss = task_loss + resource_cost
    total_loss.backward()
    optimizer.step()
    
    return task_loss.item(), resource_cost.item()
```

## Design Principles

### Biologically Motivated Constraints
| Resource | Biological Analog | Constraint Type |
|----------|------------------|-----------------|
| Breadth | Synapse count / dendritic arbor | L1/L2 norm on activations |
| Depth | Cortical layer count | Gating probability |
| Time | Reaction time / inference time | Halting probability |

### Setting Pressure Weights
- **High λ_breadth**: Produces sparse, efficient networks (energy-constrained)
- **High λ_depth**: Favors flat, wide architectures
- **High λ_time**: Produces fast feed-forward processing
- **Balanced λ**: Diverse architectures with task-adaptive depth/time

## Applications

1. **Neuro-inspired architecture search**: Let the resource costs drive NAS organically
2. **Reaction time modeling**: Time cost correlates with human RT — useful for cognitive modeling
3. **Adaptive inference**: Networks naturally use more computation for hard inputs
4. **Multi-task learning**: Different tasks induce different resource profiles

## Pitfalls

- **Mode collapse**: If one λ is too high, the network collapses to trivial solutions
- **Gradient flow**: Gated depth can cause vanishing gradients — use highway-style connections
- **Training stability**: Anneal λ values from small to target values
- **Evaluation**: Measure both accuracy AND resource usage (FLOPs, active neurons)

## Related Work

- Adaptive Computation Time (ACT) — Graves 2016
- Neural Architecture Search (NAS) — Zoph & Le 2017
- Universal Transformers — Dehghani et al. 2019
- Liquid Neural Networks — Hasani et al. 2021

## Citation

```bibtex
@article{butkus2026growing,
  title={Growing a Neural Network in Breadth, Depth, and Time},
  author={Butkus, Eivinas and Gupta, Kedar Garzón and Kriegeskorte, Nikolaus},
  journal={arXiv preprint arXiv:2605.25174},
  year={2026}
}
```
