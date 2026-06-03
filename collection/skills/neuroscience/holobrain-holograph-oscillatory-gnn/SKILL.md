---
name: holobrain-holograph-oscillatory-gnn
description: >
  HoloBrain and HoloGraph framework: modeling brain rhythms through coupled oscillatory
  synchronization and applying this principle to graph neural networks. Addresses GNN
  over-smoothing and enables reasoning on graphs through oscillatory dynamics.
---

# HoloBrain & HoloGraph: Oscillatory Synchronization for Brain Modeling and GNNs

**Paper:** arXiv:2602.00057
**Authors:** Tingting Dan, Jiaqi Ding, Guorong Wu
**Categories:** q-bio.NC, cs.LG
**Year:** 2026

## Overview

Two-part framework connecting neuroscience and machine learning through oscillatory synchronization:
1. HoloBrain: Models brain rhythms through interference of spontaneously synchronized neural oscillations
2. HoloGraph: Applies synchronization principle to GNNs, enabling oscillatory computation beyond heat diffusion

## Key Concepts

### Neural Oscillatory Synchronization
- Brain rhythms emerge from synchronization of coupled neural oscillators
- Phase relationships between oscillators encode abstract concepts
- Synchronization patterns dynamically reconfigure for different cognitive functions

### HoloGraph: Oscillatory GNNs
- Each node is an oscillator; edges define coupling strength
- Information propagation through phase synchronization rather than feature diffusion
- Addresses over-smoothing: oscillatory dynamics maintain distinct phase patterns even after many iterations

## Methodology

### HoloGraph Implementation
1. Replace conventional GNN message passing with oscillatory synchronization
2. Node states as complex numbers (amplitude + phase)
3. Information encoded in phase relationships
4. Synchronization dynamics enable iterative refinement
5. Readout maps final phase patterns to predictions

### Advantages over Traditional GNNs
- No over-smoothing
- Natural multi-scale representation
- Biological plausibility
- Enhanced reasoning capability

## Applications
- Brain rhythm modeling
- Graph classification
- Molecular property prediction
- Knowledge graph reasoning

## Key Insights
1. Shared mechanism: same oscillatory synchronization for brain rhythms and graph computation
2. Over-smoothing solution through oscillatory dynamics
3. Phase as richer representation
4. Biology inspires computation

## References
- Dan, T., Ding, J., & Wu, G. (2026). HoloBrain & HoloGraph. arXiv:2602.00057.
