---
name: spikingmoe-sdprompt-snn
description: "SpikingMoE — first open-source SNN framework integrating Mixture-of-Experts (MoE) into a spike-driven Transformer with LGN-inspired SDprompt routing. Uses spike-compatible expert modules with binary spike communication for neuromorphic hardware. Activation: spiking neural network, mixture of experts, neuromorphic computing, spike-driven transformer, brain-inspired computing"
---

# SpikingMoE: SDPrompt-Guided Dynamic Expert Fusion in Spiking Neural Networks

**arXiv**: [2605.23188](https://arxiv.org/abs/2605.23188) (cs.NE)
**Authors**: Yukai Yang, Chenxi Qin, Jungang Li, Xin Zhang, Wenwei Shao, Liqun Chen
**Submitted**: 22 May 2026

## Overview

SpikingMoE integrates a spike-driven Transformer with a Mixture-of-Experts (MoE) framework for dynamic computation in Spiking Neural Networks (SNNs). Inspired by the lateral geniculate nucleus (LGN) in the visual pathway, it introduces a **spike-driven prompt (SDprompt)** mechanism enabling input-dependent expert routing in a biologically plausible manner. This is the **first open-source SNN framework** that integrates MoE into a spike-driven Transformer with LGN-inspired routing.

## Key Innovations

### 1. Spike-Driven Mixture-of-Experts
- Replaces standard MLPs with **spike-compatible expert modules**
- Enforces **binary spike communication** throughout the MoE pipeline
- Designed for neuromorphic hardware (Loihi, TrueNorth)
- Only active experts consume energy — fully exploits SNN sparsity

### 2. LGN-Inspired SDprompt Routing
- Inspired by the Lateral Geniculate Nucleus (LGN) which selectively routes sensory inputs to specific neural pathways
- **Spike-Driven Prompt (SDprompt)** uses spike-form signals for context-aware expert selection
- Biologically plausible: the LGN acts as a "routing center" that gates visual information
- Enables **input-dependent** (not fixed) expert routing

### 3. Spike-Compatible Expert Design
- Each expert is a spike-driven module with binary spike I/O
- Expert outputs are aggregated via sparse addition (no multiplication)
- Compatible with event-driven neuromorphic processors

### 4. Integration with Spike-Driven Transformer
- Builds on Spike-Driven Self-Attention (SDSA) — replaces matrix multiplication with Hadamard product and sparse additions
- MoE replaces the MLP component of each transformer block
- End-to-end fully spike-driven computation

## Performance

| Dataset | SpikingMoE Top-1 Accuracy | Reference |
|---------|--------------------------|-----------|
| CIFAR-10 | 94.09% | First open-source SNN MoE |
| CIFAR-100 | 74.54% | First open-source SNN MoE |

## Architecture

```
Input (spike-form)
  ↓
Spike-Driven Self-Attention (SDSA)
  ↓
SDprompt Router (LGN-inspired):
  - Generates spike-form routing probabilities
  - Selects top-k experts per token
  ↓
Spike-Compatible Expert Modules (×N):
  - Each expert: spike-driven computation
  - Binary spike I/O throughout
  ↓
Expert Aggregation (sparse addition)
  ↓
Output (spike-form)
```

## Code & Implementation

- **Open-source**: available at the project page (see arXiv abstract for link)
- Built on the Spike-driven Transformer architecture
- Experiments on CIFAR-10 and CIFAR-100

## When to Use

This skill is relevant when:
- Working on **Spiking Neural Networks (SNNs)** for vision tasks
- Implementing **Mixture-of-Experts** in biologically plausible neural networks
- Designing **neuromorphic hardware** compatible algorithms
- Exploring **brain-inspired routing mechanisms** (LGN)
- Scaling SNN-Transformers to more complex visual tasks
- Combining SNN efficiency with MoE dynamic computation

## Related Work

- **Spikformer**: Introduced self-attention to SNNs with Spiking Self-Attention (SSA)
- **Spike-driven Transformer**: Proposed SDSA with fully spike-driven computation
- **DeepSeekV3, LLaMA4**: MoE architectures in large language models
- **LGN (Lateral Geniculate Nucleus)**: Biological routing center in the visual pathway

## Limitations

- Moderate accuracy on CIFAR datasets (improvement room vs. state-of-the-art ANNs)
- Only validated on small-scale datasets (CIFAR-10/100)
- Expert load balancing not explicitly addressed
- No ablation study isolating SDprompt contribution

## Activation

**Keywords**: spiking neural network, mixture of experts, neuromorphic computing, spike-driven transformer, brain-inspired computing, LGN routing, visual recognition, event-driven computation, spike routing, SDprompt, sparse activation
