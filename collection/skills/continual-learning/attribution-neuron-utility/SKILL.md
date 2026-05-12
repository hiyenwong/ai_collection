---
name: attribution-neuron-utility
description: "Gradient-based eXplained Deviation (GXD) neuron utility metric for plasticity restoration in deep networks. Combines attribution-guided neuron importance scoring with critical bottleneck period (CBP) detection and targeted reset. Use when: catastrophic forgetting, plasticity loss, neuron-level analysis, continual learning reset methods, attribution-guided training."
---

# Attribution-Based Neuron Utility for Plasticity Restoration

## Core Method

**GXD (Gradient-based eXplained Deviation)**: Attribution-based neuron utility metric that identifies which neurons contribute to prediction vs. which are dead.

## CBP Detection

Critical Bottleneck Periods (CBPs) are phases where gradient norms systematically decrease, indicating plasticity loss.

## Reset Strategy

1. Compute GXD scores per neuron
2. Identify low-utility (dead) neurons during CBPs
3. Selective reset of dead neurons while preserving functional ones
4. Outperforms L2 regularization, dropout, and L3 methods

## Paper

- Elisii et al., arXiv:2605.06834, 2026
