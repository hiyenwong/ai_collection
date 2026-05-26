---
name: cognisnn-random-graph-snn
version: "1.0"
description: "Cognition-aware Spiking Neural Network (CogniSNN) methodology. Random Graph Architecture (RGA) enabling neuron-expandability, pathway-reusability, and dynamic-configurability in SNNs for neuromorphic and continual learning tasks."
tags:
  - spiking-neural-networks
  - neuromorphic
  - continual-learning
  - random-graph
  - computational-neuroscience
  - brain-inspired-ai
trigger_conditions:
  - "spiking neural network with biological structure"
  - "SNN continual learning"
  - "neuromorphic random graph architecture"
  - "neuron expandability pathway reusability"
  - "CogniSNN"
  - "dynamic spiking network"
  - "N-Caltech SNN benchmark"
source: "PubMed PMID:42140147 / Neural Networks 2026"
authors: ["Yongsheng Huang", "Peibo Duan", "Yujie Wu", "Kai Sun"]
doi: "10.1016/j.neunet.2026.109071"
---

# CogniSNN: Cognition-Aware Spiking Neural Network with Random Graph Architecture

## Overview

CogniSNN is a novel SNN paradigm grounded in **Random Graph Architecture (RGA)** that explicitly models three key biologically-inspired structural characteristics missing from mainstream SNNs:

1. **Neuron-Expandability** — neurons and synapses can grow dynamically over time
2. **Pathway-Reusability** — structural pathways are reused across tasks for efficient continual learning
3. **Dynamic-Configurability** — network topology adapts along the temporal dimension

## Core Problem

Mainstream SNNs adopt rigid, chain-like architectures borrowed from ANNs. This ignores the fundamental reality of biological neural circuits: neurons are stochastically interconnected, forming complex pathways. This rigidity causes:
- Poor continual learning (catastrophic forgetting)
- Fixed timestep constraints limiting temporal dynamics
- Lack of structural adaptability

## Methodology

### 1. Random Graph Architecture (RGA)
- Replace fixed chain topology with stochastic connectivity
- Neurons form random directed connections within layers
- Mimics biological stochastic synaptic connectivity
- Enables exponentially larger functional pathway space

### 2. Purely Spiking Residual Mechanism
```python
# Spiking residual connection (no ANN-style shortcuts)
class SpikingResidual(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.snn_block = SpikingBlock(channels)
        self.skip = SpikingSkipConnection(channels)  # spike-based
    
    def forward(self, x):
        return self.snn_block(x) + self.skip(x)  # both paths spike
```

### 3. Adaptive Pooling Strategy
- Handles dimensional mismatch in deep RGA networks
- Adaptive spatial pooling preserves temporal spike patterns
- No ANN-style normalization needed

### 4. Key Pathway-based Learning without Forgetting (KP-LwF)
```python
def select_key_pathways(model, task_id, top_k=0.3):
    """Identify and protect the most activated pathways for each task"""
    pathway_importance = compute_pathway_gradients(model, task_id)
    key_paths = topk_pathways(pathway_importance, k=top_k)
    return key_paths

def kp_lwf_loss(new_task_loss, old_pathways, lambda_kd=0.5):
    """Distillation loss preserving key pathways"""
    pathway_distill = pathway_preservation_loss(old_pathways)
    return new_task_loss + lambda_kd * pathway_distill
```

### 5. Dynamic Growth Learning (DGL)
- Neurons and synapses evolve dynamically along the temporal dimension
- Growth triggered by error signals and synaptic activity
- Pruning of inactive connections prevents parameter explosion

## Key Results

| Metric | CogniSNN | Previous SOTA (SSNN) | Improvement |
|--------|----------|----------------------|-------------|
| N-Caltech101 Accuracy | **80.64%** | 77.97% | +2.67% |
| Timesteps needed | 5 | 5 | equal |
| Continual learning | Superior | - | significant |
| Noise robustness | Enhanced | - | significant |

## Activation Keywords
- spiking neural network, SNN, neuromorphic, random graph
- continual learning, catastrophic forgetting, pathway reuse
- CogniSNN, neuron expandability, dynamic growth
- N-Caltech, N-MNIST, DVS, event-based vision

## Implementation Guidance

### When to Use
- Building SNNs for neuromorphic hardware (Intel Loihi, BrainScaleS)
- Continual/lifelong learning with spiking networks
- Event-based vision (DVS cameras, neuromorphic sensors)
- Bio-inspired architecture research bridging ANN and SNN

### Quick Start Pattern
```python
from spikingjelly.activation_based import neuron, layer, functional

class CogniSNNBlock(nn.Module):
    def __init__(self, in_ch, out_ch, p_random=0.3):
        super().__init__()
        # Random graph connectivity
        self.random_conv = RandomGraphConv(in_ch, out_ch, p=p_random)
        self.lif = neuron.LIFNode(tau=2.0)
        self.residual = SpikingResidual(out_ch)
    
    def forward(self, x):
        out = self.lif(self.random_conv(x))
        return self.residual(out)
```

### Pitfalls
- RGA increases memory footprint — use structured sparsity to control
- DGL needs careful growth threshold tuning (too aggressive = parameter explosion)
- KP-LwF requires task boundaries to be known — adapt for online learning

## Connection to Neuroscience

CogniSNN is directly inspired by:
- **Cortical connectivity statistics**: ~20% random connectivity in cortical columns
- **Hebbian-based pathway strengthening**: KP-LwF mirrors LTP/LTD consolidation
- **Adult neurogenesis**: DGL mirrors neurogenesis in hippocampus

## References
- Huang et al. (2026). *Neural Networks* DOI:10.1016/j.neunet.2026.109071
- SpikingJelly framework: https://github.com/fangwei123456/spikingjelly
- Related: SSNN (ICLR 2024), TET (ICLR 2022)
