---
name: growing-neural-network-breadth-depth-time
title: "Growing Neural Networks in Breadth, Depth, and Time"
description: >
  Differentiable cost framework for jointly optimizing neural network architecture
  (breadth/width, depth/layers, temporal recurrence) alongside task performance.
  Bio-inspired growth principle enabling networks to autonomously develop architectures
  matching task complexity — mimicking biological neural development.
tags:
  - neural-architecture
  - bio-inspired
  - neural-development
  - recurrent-networks
  - architecture-search
  - resource-constraints
  - breadth-depth-time
  - differentiable-architecture
activation_keywords:
  - neural network growth
  - bio-inspired architecture
  - differentiable cost
  - breadth depth time
  - recurrent convolutional
  - resource constraints
  - neural development
  - architecture optimization
source:
  arxiv: "2605.25174"
  authors: ["Eivinas Butkus", "Kedar Garzón Gupta", "Nikolaus Kriegeskorte"]
  published: "2026-05-24"
  category: "q-bio.NC, cs.NE"
---

# Growing Neural Networks in Breadth, Depth, and Time

## Overview

Biological neural systems develop from minimal circuits, growing in complexity to match environmental demands. This skill presents a **differentiable bio-inspired growth framework** that enables artificial neural networks to autonomously grow in three dimensions:

- **Breadth**: Width/number of channels per layer
- **Depth**: Number of layers
- **Time**: Number of recurrent processing steps

The key insight: define differentiable resource cost terms and jointly optimize them with task loss, producing networks that are as simple as possible while as complex as necessary.

## Core Framework

### The Three-Dimensional Growth Space

Consider a recurrent convolutional network (RCN) on an infinite lattice $\mathcal{L} = \mathbb{Z}^2$:

$$h_{t+1}^{(l)} = f\left(W^{(l)} * h_t^{(l)} + U^{(l)} h_{t}^{(l)} + b^{(l)}\right)$$

The **active** portion of this lattice is characterized by:
- $B$ = breadth (channels per layer)  
- $D$ = depth (number of layers used)
- $T$ = time (recurrent steps per inference)

### Differentiable Resource Costs

Define smooth, differentiable costs for each dimension:

$$\mathcal{L}_{\text{breadth}} = \lambda_B \sum_{l=1}^{D} \|\alpha_l\|_1$$

$$\mathcal{L}_{\text{depth}} = \lambda_D \|\beta\|_1$$

$$\mathcal{L}_{\text{time}} = \lambda_T \|\gamma\|_1$$

where $\alpha_l$, $\beta$, $\gamma$ are soft gates (0-1 valued) for channel, layer, and timestep usage.

**Total loss**:
$$\mathcal{L} = \mathcal{L}_{\text{task}} + \mathcal{L}_{\text{breadth}} + \mathcal{L}_{\text{depth}} + \mathcal{L}_{\text{time}}$$

### Soft Gating Mechanism

```python
class SoftGate(nn.Module):
    """Learnable soft gate for controlling resource usage."""
    
    def __init__(self, size, temperature=0.1):
        super().__init__()
        self.logits = nn.Parameter(torch.zeros(size))
        self.temperature = temperature
    
    def forward(self):
        # Straight-through estimator for binary gates
        probs = torch.sigmoid(self.logits / self.temperature)
        # Hard gate during forward, soft gradient during backward
        hard = (probs > 0.5).float()
        return hard - probs.detach() + probs
    
    def l1_cost(self):
        return torch.sigmoid(self.logits / self.temperature).sum()
```

## Implementation

### Growing RCN Architecture

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class GrowingRCN(nn.Module):
    """
    Recurrent Convolutional Network that grows in breadth, depth, and time.
    
    Architecture lives on a finite subset of an infinite lattice.
    """
    
    def __init__(self, max_breadth=64, max_depth=8, max_time=16,
                 in_channels=1, out_size=10):
        super().__init__()
        self.max_breadth = max_breadth
        self.max_depth = max_depth
        self.max_time = max_time
        
        # Architecture gates
        self.breadth_gates = nn.ModuleList([
            SoftGate(max_breadth) for _ in range(max_depth)
        ])
        self.depth_gates = SoftGate(max_depth)
        self.time_gates = SoftGate(max_time)
        
        # Full-capacity layers (some will be gated off)
        self.conv_layers = nn.ModuleList([
            nn.Conv2d(max_breadth, max_breadth, 3, padding=1)
            for _ in range(max_depth)
        ])
        self.recurrent_layers = nn.ModuleList([
            nn.Conv2d(max_breadth, max_breadth, 3, padding=1)
            for _ in range(max_depth)
        ])
        
        self.input_proj = nn.Conv2d(in_channels, max_breadth, 1)
        self.output_head = nn.Linear(max_breadth, out_size)
    
    def forward(self, x):
        batch_size = x.shape[0]
        
        # Project input
        h = self.input_proj(x)
        
        # Get active timesteps
        time_gates = self.time_gates()
        active_steps = int(time_gates.sum().item()) + 1  # At least 1 step
        
        # Recurrent processing
        states = [h.clone() for _ in range(self.max_depth)]
        
        for t in range(active_steps):
            if time_gates[t] < 0.5 and t > 0:
                break
                
            new_states = []
            depth_gates = self.depth_gates()
            
            for l, (conv, rec) in enumerate(zip(self.conv_layers, self.recurrent_layers)):
                if depth_gates[l] < 0.5 and l > 0:
                    new_states.append(states[l])
                    continue
                
                # Apply breadth gating
                b_gate = self.breadth_gates[l]()
                
                # Feedforward + recurrent
                ff = conv(states[l-1] if l > 0 else h)
                rec_h = rec(states[l])
                new_state = F.relu(ff + rec_h) * b_gate.view(1, -1, 1, 1)
                new_states.append(new_state)
            
            states = new_states
        
        # Pool and classify
        out = states[-1].mean(dim=[2, 3])  # Global average pool
        return self.output_head(out)
    
    def resource_cost(self, lambda_B=1e-3, lambda_D=1e-2, lambda_T=1e-3):
        """Compute total resource cost."""
        breadth_cost = sum(g.l1_cost() for g in self.breadth_gates)
        depth_cost = self.depth_gates.l1_cost()
        time_cost = self.time_gates.l1_cost()
        
        return (lambda_B * breadth_cost + 
                lambda_D * depth_cost + 
                lambda_T * time_cost)
    
    def effective_architecture(self):
        """Report the currently active architecture."""
        with torch.no_grad():
            active_breadths = [int(g().sum().item()) for g in self.breadth_gates]
            active_depth = int(self.depth_gates().sum().item()) + 1
            active_time = int(self.time_gates().sum().item()) + 1
        return {
            'breadths': active_breadths[:active_depth],
            'depth': active_depth,
            'time_steps': active_time,
            'total_params': active_depth * active_breadths[0]**2 * 9  # Approx
        }


# Training loop
def train_growing_network(model, train_loader, n_epochs=100):
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    
    for epoch in range(n_epochs):
        for x, y in train_loader:
            # Forward pass
            logits = model(x)
            
            # Task loss
            task_loss = F.cross_entropy(logits, y)
            
            # Resource cost (gradually increase pressure)
            resource_weight = min(epoch / 20, 1.0)  # Warm up resource penalty
            resource_loss = resource_weight * model.resource_cost()
            
            # Total loss
            total_loss = task_loss + resource_loss
            
            optimizer.zero_grad()
            total_loss.backward()
            optimizer.step()
        
        # Monitor growth
        arch = model.effective_architecture()
        print(f"Epoch {epoch}: depth={arch['depth']}, "
              f"time={arch['time_steps']}, loss={task_loss.item():.4f}")
```

## Growth Trajectories

The model exhibits **developmental stages**:

1. **Seed stage** (epochs 0-10): Minimal breadth, 1 layer, 1 timestep
2. **Growth stage** (epochs 10-50): Width expands first, then depth, then time
3. **Pruning stage** (epochs 50+): Redundant capacity pruned back
4. **Mature stage**: Stable architecture matching task complexity

```python
# Visualize growth trajectory
import matplotlib.pyplot as plt

def plot_growth(history):
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    
    axes[0].plot(history['breadth'])
    axes[0].set_title('Breadth Growth')
    axes[0].set_xlabel('Epoch')
    
    axes[1].plot(history['depth'])
    axes[1].set_title('Depth Growth')
    axes[1].set_xlabel('Epoch')
    
    axes[2].plot(history['time'])
    axes[2].set_title('Temporal Depth')
    axes[2].set_xlabel('Epoch')
    
    plt.tight_layout()
    plt.savefig('growth_trajectory.png')
```

## Key Findings

### 1. Breadth Before Depth
Networks consistently grow width before depth — mirroring biological cortical development and the empirical observation that wider shallow networks are often more efficient than narrow deep ones.

### 2. Task-Matched Complexity
Simple tasks → shallow, narrow, fast; complex tasks → deep, wide, multi-step. The framework automatically discovers the right complexity without manual architecture search.

### 3. Recurrence for Temporal Tasks
Time dimension only grows for tasks requiring temporal integration (sequence modeling, video), remaining minimal for static input tasks.

### 4. Efficiency vs. Fixed Architectures
- ~30-50% parameter reduction vs. fixed architectures at same accuracy
- Better generalization due to implicit regularization via resource pressure
- Comparable to NAS at fraction of search cost

## Biological Connections

| Network Property | Biological Analogue |
|-----------------|---------------------|
| Breadth growth | Cortical column width expansion |
| Depth growth | Hierarchical area addition |
| Time steps | Processing cascade duration |
| Soft pruning | Synaptic pruning in adolescence |
| Resource cost | Metabolic/wiring cost minimization |

## Use Cases

1. **Efficient AI**: Discover minimal architectures for embedded systems
2. **Neuroscience Models**: Model developmental trajectories of cortical circuits
3. **Continual Learning**: Grow network when new task demands increase
4. **Architecture Comparison**: Understand what makes tasks harder/easier

## Pitfalls

- Temperature parameter in soft gates requires tuning — too high → no pruning, too low → unstable training
- Resource cost weights (λ_B, λ_D, λ_T) need task-specific calibration
- Growing from minimal seed can get stuck in local minima; warm restarts help
- Breadth-depth-time interactions are complex — monitor all three simultaneously

## Citation

```bibtex
@article{butkus2026growing,
  title={Growing a Neural Network in Breadth, Depth, and Time},
  author={Butkus, Eivinas and Garz{\'o}n Gupta, Kedar and Kriegeskorte, Nikolaus},
  journal={arXiv preprint arXiv:2605.25174},
  year={2026}
}
```
