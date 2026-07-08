---
name: dendritic-in-context-learning-snn
description: DendriCL methodology for in-context learning in single-layer spiking neural networks using dendritic compartment dynamics. Use when: implementing ICL in biologically-plausible SNNs, designing compartmental spiking architectures, studying online LMS in dendrites, or building seed-stable ICL at super-dimensional task complexity. arXiv: 2607.02289
category: neuro-quantum
created: 2026-07-06
source: arxiv
tags: [dendritic-computing, in-context-learning, spiking-neural-networks, online-LMS, compartmental-models, seed-stability, neuromorphic]
trigger_words: dendritic in-context learning, DendriCL, compartmental spiking, online Widrow-Hoff LMS, seed-stable ICL, Garg-2022 benchmark, apical recurrence, single-layer SNN
---

# Dendritic In-Context Learning in Spiking Neural Networks (DendriCL)

## Source
Paper: "Dendritic In-Context Learning in a Single-Layer Spiking Neural Network" (arXiv: 2607.02289, July 2026)

## Core Discovery
In-context learning (ICL) does NOT require:
- Attention mechanisms
- Architectural depth
- Inference-time synaptic plasticity

A **single dendritic compartment with online-LMS dynamics is sufficient**.

## Key Insight
Prior SNN designs fail the Garg-2022 ICL benchmark because they route adaptation through inference-time synaptic plasticity, treating the dendritic compartment as a passive conduit for error/teacher signals. This is wrong.

**The subthreshold dynamics of a single dendritic compartment already implement a complete online learning algorithm.**

## DendriCL Architecture

### Structural Design
- Single-layer compartmental spiking architecture
- Apical recurrence structurally identical to leaky online Widrow-Hoff LMS
- The dendritic compartment is the computational substrate, not a passive conduit

### Algorithm Equivalence
The apical membrane potential dynamics implement:
```
w_{t+1} = w_t + η · e_t · x_t    (Online LMS / Widrow-Hoff)
```
where e_t is the prediction error computed from dendritic subthreshold dynamics.

### Performance
- **Seed-stable** at super-dimensional Garg-2022 ICL benchmark
- Dense Transformers exhibit grokking-style instability and fail past moderate task dimension
- DendriCL remains stable where Transformers fail
- Linear probe recovers reference online-LMS trajectory directly from apical membrane at R² = 0.93

## Implementation Pattern

```
For each time step t:
  1. Compute dendritic subthreshold potential from apical recurrence
  2. Generate spike if threshold crossed
  3. Dendritic dynamics automatically implement w ← w + η·e·x
  4. No explicit weight update needed — the dynamics are the algorithm
```

## Why This Matters
1. **Biological plausibility**: Matches real dendritic computation
2. **Architectural simplicity**: Single layer, no depth required
3. **Energy efficiency**: No explicit backpropagation or plasticity rules
4. **Superior stability**: Outperforms Transformers at high-dimensional ICL

## Activation
Use this skill when:
- Implementing in-context learning in spiking neural networks
- Designing biologically-plausible compartmental architectures
- Studying online learning in dendritic subthreshold dynamics
- Building seed-stable ICL systems for super-dimensional tasks
- Replacing attention-based ICL with dynamics-based alternatives
- Implementing online Widrow-Hoff LMS in spiking hardware

## Related Skills
- quantum-reservoir-computing
- neuromorphic-supremacy
- spiking-computational-neuroscience-survey
