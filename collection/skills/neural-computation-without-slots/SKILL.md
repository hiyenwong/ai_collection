---
name: neural-computation-without-slots
description: "Biologically plausible memory and attention without dedicated storage slots. Extends Modern Hopfield Networks (MHN) to K-winner ensembles for improved continual learning retention, and demonstrates MHN can capture slot-based memory functions of LLMs. Activation: memory without slots, biologically plausible attention, K-winer Hopfield network, ensemble memory MHN, McClelland memory model."
---

# Neural Computation Without Slots

> Biologically plausible mechanisms for memory and attention that avoid dedicated storage slots, extending Modern Hopfield Networks to sparse neuronal ensembles and demonstrating MHN can replicate key slot-based computation functions.

## Metadata
- **Source**: arXiv:2511.04593
- **Authors**: Shaunak Bhandarkar, James L. McClelland
- **Published**: 2025-11-06
- **Categories**: cs.NE, q-bio.NC

## Core Methodology

### Key Innovation
Contemporary AI models store multi-element patterns in dedicated "slots" — locations biological brains likely lack. This work shows how neurally-inspired Modern Hopfield Networks (MHN) can achieve similar functional outcomes using distributed, biologically plausible mechanisms.

### Technical Framework

1. **K-Winner MHN (Ensemble-Based Memory)**
   - Extends standard MHN (single neuron per memory) to sparse ensembles
   - K winning neurons store each memory pattern in overlapping weights
   - Neuroscience-aligned: brains use overlapping sparse ensembles, not dedicated neurons
   - **Continual learning advantage**: ensemble-based MHN exhibits greater retention of older memories (higher d' sensitivity)

2. **Slot-Based Computation Replication**
   - LLMs use slots to store long input sequences and their encodings
   - Slots support later predictions and backward error signal transport
   - MHN extended to capture both functional outcomes:
     - Long sequence storage via distributed pattern encoding
     - Error signal transport through learned encoding gradients

3. **Graded Sensitivity Measure (d')**
   - Signal detection theory metric for memory retention
   - Measures sensitivity to stored patterns amid interference
   - Ensemble MHN shows superior d' in continual learning regimes

### Architecture Comparison
```
Slot-based (LLM):    [Slot1] [Slot2] [Slot3] ... [SlotN]
                     dedicated storage per element

Ensemble MHN:        [Neuron ensemble weights]
                     overlapping, distributed storage
                     K-winner selection per pattern
```

## Applications
- Biologically plausible memory architectures for AI
- Continual learning with reduced catastrophic forgetting
- Understanding biological memory mechanisms
- Neuromorphic memory design
- Bridging cognitive science and AI memory models

## Implementation Guide

### Prerequisites
- Understanding of Modern Hopfield Networks (Krotov & Hopfield, 2021)
- Signal detection theory (d' measure)
- Continual learning frameworks

### Step-by-Step
1. Implement standard MHN with single-neuron memory storage
2. Extend to K-winner selection: choose top-K neurons per pattern
3. Store patterns in overlapping ensemble weights
4. Evaluate memory retention using d' sensitivity measure
5. Test in continual learning regime (sequential pattern storage)
6. Extend to sequence modeling: store input encodings in MHN weights
7. Implement backward error propagation through stored encodings

### Pitfalls
- K-winner selection requires careful tuning of K value
- Overlapping ensembles can cause interference at high capacity
- d' measure assumes Gaussian noise distributions
- Sequence encoding capacity limited by ensemble size
- Biologically plausible constraints may limit performance vs. slot-based models

## Related Skills
- kernel-hopfield-associative-memory
- kernel-hopfield-attractor-geometry
- neuro-memory-architecture
- hippocampal-replay-credit-assignment
- context-selective-multimodal-memory
