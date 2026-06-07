---
title: "SpikingMoE: SDPrompt-Guided Dynamic Expert Fusion in Spiking Neural Networks"
source: "arXiv:2605.23188"
authors: "Yukai Yang, Chenxi Qin, Jungang Li, Xin Zhang, Wenwei Shao, Liqun Chen"
category: "ai_collection"
tags:
  - spiking-neural-network
  - mixture-of-experts
  - transformer
  - neuromorphic
  - vision
  - lgn-routing
---

# SpikingMoE: SDPrompt-Guided Dynamic Expert Fusion in Spiking Neural Networks

**arXiv:2605.23188** | Submitted: 22 May 2026 | cs.NE

## Summary

SpikingMoE integrates a **spike-driven Transformer** with a **Mixture-of-Experts (MoE)** framework for dynamic computation in visual recognition. Inspired by the **lateral geniculate nucleus (LGN)** in the visual pathway, it introduces a **spike-driven prompt (SDprompt)** that enables input-dependent expert routing in a biologically plausible manner. This is the **first open-source SNN framework** integrating MoE into a spike-driven Transformer with LGN-inspired routing.

## Key Innovations

1. **LGN-inspired routing**: Takes biological inspiration from the lateral geniculate nucleus to route inputs to appropriate expert modules.
2. **Spike-driven prompt (SDprompt)**: Enables input-dependent expert routing while maintaining binary spike communication.
3. **Spike-compatible expert modules**: Replaces standard MLPs with spiking neuron-based expert modules.
4. **Binary spike communication**: Enforces all communication between modules through binary spikes, making it neuromorphic-hardware friendly.

## Performance

- **CIFAR-10**: 94.09% top-1 accuracy
- **CIFAR-100**: 74.54% top-1 accuracy
- Demonstrates that modular expert routing can be incorporated while retaining reasonable performance.

## Architecture

- Base: Spike-driven Transformer backbone
- MoE layers replace standard MLP feedforward blocks
- SDprompt generates routing decisions based on input spike patterns
- LGN-inspired gating mechanism for expert selection
- All inter-module communication via binary spikes

## Implications

- Bridges **neuromorphic computing** with **mixture-of-experts** architectures
- Provides a **biologically plausible routing mechanism** for sparse computation
- Opens the door for energy-efficient, large-scale SNN models with conditional computation
- Demonstrates feasibility of **brain-inspired modular architectures** in SNNs

## Activation Keywords

spiking-neural-network, mixture-of-experts, spikingmoe, transformer, neuromorphic, lgn-routing, sdprompt, visual-recognition, brain-inspired, sparse-computation
