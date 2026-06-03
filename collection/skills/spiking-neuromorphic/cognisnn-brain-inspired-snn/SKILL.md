---
name: cognisnn-brain-inspired-snn
title: CogniSNN - Brain-Inspired Spiking Neural Network Framework
description: |
  CogniSNN (Cognition-aware Spiking Neural Network) is a comprehensive framework that bridges 
  artificial intelligence and computational neuroscience through Random Graph Architecture (RGA).
  It implements three core brain-inspired mechanisms: Neuron-Expandability, Pathway-Reusability, 
  and Dynamic-Configurability for advanced SNN design and training.

  Based on: "CogniSNN: Enabling Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability 
  with Random Graph Architectures in Spiking Neural Networks" (arXiv:2512.11743)

triggers:
  - cognisnn
  - random graph architecture
  - neuron expandability
  - pathway reusability
  - dynamic configurability
  - spiking neural network RGA
  - OR gate residual
  - key pathway learning
  - dynamic growth learning
  - brain-inspired SNN

tools:
  - python
  - pytorch
  - terminal

---

# CogniSNN: Brain-Inspired Spiking Neural Network Framework

## Overview

CogniSNN introduces a paradigm shift from rigid chain-like architectures to brain-inspired random graph structures. The framework models three fundamental brain mechanisms:

1. **Neuron-Expandability**: Massive scale and depth enabling complex information processing
2. **Pathway-Reusability**: Functional orthogonality with selective pathway activation for continual learning
3. **Dynamic-Configurability**: Continuous synaptic growth/apoptosis for adaptive reconfiguration

## Core Components

### 1. Random Graph Architecture (RGA)

The network is formalized as a Directed Acyclic Graph (DAG) G = {V, E} where:
- V: Node set (each node is a ResNode)
- E: Edge set (synaptic connections with learnable weights)
- A: Adjacency matrix encoding connectivity

**Supported Graph Generators:**
- **WS (Watts-Strogatz)**: Small-world networks with high clustering and short path lengths
- **ER (Erdős-Rényi)**: Random networks with uniform connection probability

### 2. ResNode Architecture

Each ResNode consists of Conv-BN-SN triplets:

```
ConvBNSN(x) = SN(BN(Conv(x)))
```

**Innovation: OR Gate Residual Mechanism**

Unlike traditional additive residual connections that generate floating-point values:

```python
# Traditional (problematic for SNNs)
output = identity + residual  # Float accumulation

# CogniSNN OR Gate (pure spiking)
output = OR(identity, residual)  # Binary spike output
```

**Key Properties:**

1. **Identity Mapping**: With BN weights/biases initialized to zero, the residual mapping O₂[t] ≡ 0, making output = identity

2. **Gradient Flow**: OR Gate yields four gradient scenarios:
   - When O₁[t]=1, O₂[t]=0: gradient = 1
   - When O₁[t]=1, O₂[t]=1: gradient = 0
   - When O₁[t]=0, O₂[t]=0: gradient = 1 + ∂O₂[t]/∂O₁[t]
   - When O₁[t]=0, O₂[t]=1: gradient = ∂O₂[t]/∂O₁[t]

3. **No Value Accumulation**: Binary output (0 or 1) prevents unbounded growth

### 3. Adaptive Pooling Strategy

Resolves spatial dimension mismatches from random connectivity:

```python
def adaptive_pooling(features, target_dim):
    kernel_size = floor(input_dim / target_dim)
    return AvgPool(features, kernel_size)
```

### 4. Key Pathway-Based Learning without Forgetting (KP-LwF)

**Betweenness Centrality (BC) Calculation:**

```
BC(v) = Σ φₛₜ(v) / φₛₜ  (for node v)
BC(e) = Σ φₛₜ(e) / φₛₜ  (for edge e)
BC(p) = Σ BC(vᵢ) + Σ BC(eⱼ)  (for pathway p)
```

**Key Pathway Selection:**

```python
def select_key_pathways(graph, K=1, scenario='similar'):
    sorted_paths = sort_pathways_by_BC(graph)
    
    if scenario == 'similar':
        return sorted_paths[:K]  # High-BC for shared features
    else:
        return sorted_paths[-K:]  # Low-BC to minimize interference
```

**Algorithm Flow:**
1. Clone original model
2. Align classifier layers
3. Freeze all parameters except key pathways and new classifier
4. Train with combined loss: L = λ·L_old + L_new + R(θ)

### 5. Dynamic Growth Learning (DGL)

Simulates biological neural pathway expansion:

```python
def dynamic_growth_step(t, T, total_paths):
    if 1 <= t < T:
        q(t) = floor(t * |P| / T)
    else:
        q(t) = |P|
    return q(t)

# Active subgraph at timestep t
Z(t) = {p_k | 1 ≤ k ≤ q(t)}
```

**Benefits:**
- Enhanced robustness through progressive feature learning
- Flexible timestep deployment (train with T, infer with T' < T)
- Implicit apoptosis through weight convergence to near-zero

## Mathematical Formulation

### Spiking Neuron Dynamics (LIF)

```
U_i[t] = τ·U_i[t-1] + Σⱼ W_ij·S_j[t] - S_i[t-1]·U_th

S_i[t] = Θ(U_i[t] - U_th) = {1 if U_i[t] ≥ U_th
                             {0 if U_i[t] < U_th
```

Where:
- U_i[t]: Membrane potential of neuron i at time t
- τ: Decay factor
- W_ij: Synaptic weight from neuron j to i
- S_j[t]: Spike from neuron j at time t
- U_th: Firing threshold
- Θ: Heaviside step function

### Surrogate Gradient (for BPTT)

```
σ(x, α) = 1 / (1 + e^(-αx))
```

During backpropagation, ∂S/∂U is approximated by σ'(x, α).

## Implementation Guide

### Step 1: Create RGA-based SNN

```python
import torch
import torch.nn as nn

class ResNode(nn.Module):
    """CogniSNN Residual Node with OR Gate"""
    
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, 3, padding=1)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.sn1 = LIFNeuron()
        
        self.conv2 = nn.Conv2d(out_channels, out_channels, 3, padding=1)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.sn2 = LIFNeuron()
    
    def forward(self, x):
        identity = self.sn1(self.bn1(self.conv1(x)))
        residual = self.sn2(self.bn2(self.conv2(identity)))
        return torch.logical_or(identity, residual).float()
```

### Step 2: Calculate Betweenness Centrality

```python
import networkx as nx

def calculate_pathway_bc(graph, pathway):
    node_bc = sum(nx.betweenness_centrality(graph)[n] 
                  for n in pathway.nodes)
    edge_bc = sum(nx.edge_betweenness_centrality(graph)[e] 
                  for e in pathway.edges)
    return node_bc + edge_bc
```

### Step 3: Implement KP-LwF

```python
class KPLwF:
    def __init__(self, model, key_pathways, lambda_distill=1.0):
        self.old_model = model
        self.new_model = copy.deepcopy(model)
        self.key_pathways = key_pathways
        self.lambda_distill = lambda_distill
        self._freeze_parameters()
    
    def compute_loss(self, x, y_new):
        with torch.no_grad():
            y_old = self.old_model(x)
        
        y_old_pred = self.new_model(x, task='old')
        y_new_pred = self.new_model(x, task='new')
        
        L_old = F.cross_entropy(y_old_pred, y_old)
        L_new = F.cross_entropy(y_new_pred, y_new)
        
        return self.lambda_distill * L_old + L_new
```

### Step 4: Dynamic Growth Training

```python
def train_with_dynamic_growth(model, dataloader, epochs, T):
    total_paths = len(model.pathways)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
    
    for epoch in range(epochs):
        for x, y in dataloader:
            spike_accumulator = 0
            
            for t in range(1, T+1):
                q_t = (t * total_paths) // T
                active_paths = model.pathways[:q_t]
                o_t = model(x, active_paths=active_paths, timestep=t)
                spike_accumulator += o_t
            
            o_mean = spike_accumulator / T
            loss = F.cross_entropy(o_mean, y)
            
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
```

## Experimental Results

### Classification Performance

| Dataset | CogniSNN (WS) | CogniSNN (ER) | Best Baseline |
|---------|---------------|---------------|---------------|
| DVS-Gesture | **96.2%** | 95.8% | 94.9% |
| CIFAR10-DVS | **81.5%** | 80.9% | 78.3% |
| N-Caltech101 | **83.7%** | 82.4% | 81.2% |
| Tiny-ImageNet | **58.3%** | 57.1% | 55.8% |

## Advantages over Traditional SNNs

1. **Biological Plausibility**: Random connectivity mirrors biological neural networks
2. **No Floating-Point Accumulation**: OR Gate maintains pure spiking computation
3. **Continual Learning**: Pathway reusability enables lifelong learning
4. **Robustness**: Dynamic growth improves noise tolerance
5. **Deployment Flexibility**: Supports variable inference timesteps

## Key Insights

1. **Random Graphs are Features, Not Search Space**: Unlike NAS approaches that use random graphs to find optimal structures, CogniSNN treats randomness as an intrinsic biological feature

2. **OR Gate > ADD**: Logical OR operations preserve spiking nature while enabling deep architectures

3. **BC-Guided Learning**: Betweenness centrality identifies pathways critical for different types of knowledge transfer

4. **Progressive Growth Mimics Biology**: Dynamic pathway activation during training mirrors neural development

## References

```bibtex
@article{huang2025cognisnn,
  title={CogniSNN: Enabling Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability with Random Graph Architectures in Spiking Neural Networks},
  author={Huang, Yongsheng and Duan, Peibo and Wu, Yujie and Sun, Kai and Liu, Zhipeng and Zhang, Changsheng and Zhang, Bin and Xu, Mingkun},
  journal={arXiv preprint arXiv:2512.11743},
  year={2025}
}
```

## Code Repository

- GitHub: https://github.com/Yongsheng124/CogniSNN
- Framework: PyTorch + SpikingJelly

---

*This skill is based on research published on arXiv:2512.11743 (December 2025)*
