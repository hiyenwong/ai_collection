---
name: mass-conservation-nca-reservoir-criticality
description: "Mass conservation as inductive bias for self-organized criticality in neural cellular automata reservoirs. Demonstrates 1.27× faster evolution with comparable downstream performance. Activation: self-organized criticality, neural cellular automata, reservoir computing, mass conservation, criticality"
tags: [neuroscience, reservoir computing, neural cellular automata, self-organized criticality, inductive bias]
---

## Overview

Investigates whether mass conservation—a local redistribution rule that preserves total lattice mass—serves as an inductive bias toward self-organized criticality (SOC) in evolved neural cellular automata (NCA) reservoirs.

## Core Methodology

### Neural Cellular Automata Reservoirs
- Evolve NCA toward critical avalanche dynamics
- Use as reservoirs for memory and classification tasks
- Compare mass-conserving vs standard NCA variants

### Mass Conservation Mechanism
- Local redistribution rule preserving total lattice mass
- Acts as inductive bias toward SOC
- Promotes robust criticality without sacrificing performance

## Key Findings

### Criticality Enhancement
- Mass-conserving NCA consistently exhibit stronger criticality
- More runs achieve perfect power-law fits across avalanche distributions
- 1.27× faster during evolution

### Downstream Performance
- Both variants achieve comparable performance across three benchmarks:
  - 5-bit sequential memory
  - MNIST digit classification
  - CartPole-v1 temporal control
- Conservation does not impair downstream utility
- Reservoir with perfect criticality achieves highest temporal control score

## Applications

- Reservoir computing for memory tasks
- Temporal control systems
- Classification tasks requiring critical dynamics
- Neuromorphic computing with biological plausibility

## Implementation Notes

- Mass conservation is simple to implement
- Effective mechanism for promoting robust criticality
- No trade-off between criticality quality and task performance

## Pitfalls

- Criticality alone does not guarantee optimal performance
- Need to balance criticality with task-specific requirements
- Evolution process still requires careful fitness function design

## References

- arXiv:2606.23115 (June 2026)
- Authors: Tong Zhang, Etienne Guichard, Sidney Pontes-Filho, Stefano Nichele
- 8 pages, 5 figures
