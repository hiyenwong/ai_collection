---
name: dendritic-icl-snn
description: Dendritic computation patterns enabling in-context learning in spiking neural networks.
trigger_keywords: ["dendritic in-context learning", "spiking neural network ICL", "dendritic computation SNN", "biological attention SNN", "spiking transformer"]
---

# Dendritic In-Context Learning SNN

## Description

Methodology from arXiv:2607.02289 that enables in-context learning in spiking neural networks through dendritic computation. Combines biological dendritic processing with transformer-like attention mechanisms, achieving ICL capabilities without requiring the standard transformer architecture.

## Core Methodology

1. **Dendritic Computation**: Model dendritic branches as parallel processing units that can perform local nonlinear operations
2. **Biological Attention**: Use dendritic filtering and gating to implement attention-like mechanisms biologically
3. **Event-Driven Context**: Leverage spike timing and dendritic integration windows for context encoding
4. **Weight-Sharing ICL**: Achieve in-context learning through dynamic dendritic gating rather than attention weight updates

## Key Patterns

- **Dendritic Gating**: Individual dendritic branches act as gates controlling information flow based on context
- **Temporal Integration Windows**: Dendritic compartments integrate spikes over different timescales for context retention
- **Event-Driven Attention**: Spike-based attention where importance is encoded in spike timing patterns
- **Biological Realism**: Maintains biological plausibility while achieving ML capabilities

## Applications

- Energy-efficient in-context learning on neuromorphic hardware
- Biological modeling of context-dependent neural computation
- Low-power edge AI with transformer-like capabilities
- Understanding biological basis of few-shot learning

## Activation

Use when: implementing ICL in spiking neural networks, designing biologically plausible attention mechanisms, neuromorphic computing with context learning, energy-efficient transformer alternatives.

**Keywords**: dendritic computation, in-context learning, spiking neural networks, biological attention, event-driven processing, neuromorphic computing, few-shot learning
