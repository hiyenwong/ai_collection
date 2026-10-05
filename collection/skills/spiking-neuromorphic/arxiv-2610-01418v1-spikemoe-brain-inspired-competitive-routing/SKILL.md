---
name: arxiv-2610-01418v1-spikemoe-brain-inspired-competitive-routing
description: "SpikeMoE: Brain-inspired k-WTA spike router for SNN Mixture-of-Experts with hippocampal competition-inhibition dynamics and missing-modality handling"
tags: [arxiv, spiking-neuromorphic, mixture-of-experts, brain-inspired, competitive-routing, multimodal]
arxiv_id: "2610.01418v1"
utility: 0.88
date_added: "2026-10-05"
---

# SpikeMoE: Brain-Inspired Competitive Routing for Flexible Spiking Mixture-of-Experts

**arXiv:** 2610.01418v1 | **Utility:** 0.88 | **Date:** 2026-10-05

## Abstract

SpikeMoE integrates spiking neural network dynamics with Mixture-of-Experts expert selection via a biologically-inspired spike-based k-WTA Router. The router incorporates lateral inhibition and refractory periods (inspired by hippocampal CA1 competition-inhibition) to select Top-K experts according to discrete spike counts. A two-stage missing-modality module handles incomplete multimodal inputs.

## Key Contributions

- **k-WTA spike router**: First spike-based expert selection mechanism inspired by hippocampal CA1 competitive-inhibitory dynamics
- **Lateral inhibition + refractory period**: Selects Top-K experts based on discrete spike counts, not continuous activations
- **Missing-modality handling**: Two-stage module combining empirical prototypes from observed-modality pool with modality-specific learnable embeddings
- **SOTA SNN performance**: Matches or exceeds ANN counterparts on vision, language, and multimodal benchmarks
- **Energy efficiency**: Maintains favorable trade-off between performance and energy consumption

## Methods

1. **Spike-based k-WTA Router**: Neurons compete via lateral inhibition; refractory period prevents re-selection
2. **Expert selection**: Top-K experts selected by discrete spike counts (not softmax over continuous values)
3. **Missing modality modeling**: Stage 1 — empirical prototypes from observed modalities; Stage 2 — learnable embeddings for missing modalities
4. **Framework integration**: Neuronal-scale spiking dynamics + model-scale expert selection

## Relevance

Bridges neuroscience (hippocampal competition) and ML (MoE routing) in a principled way. The spike-based selection is fundamentally different from ANN softmax routing — it's event-driven and energy-efficient. The missing-modality handling is practically important for real-world multimodal deployment where sensors may fail. Demonstrates that brain-inspired mechanisms can match ANN performance while being more efficient.
