---
name: dendritic-icl-snn
description: DendriCL methodology for dendritic in-context learning in single-layer spiking neural networks. Demonstrates that a single dendritic compartment with online-LMS dynamics is sufficient for general-purpose ICL without attention, depth, or inference-time plasticity.
tags: [spiking-neural-network, in-context-learning, dendritic-computation, neuromorphic, biological-plausibility]
arxiv_id: "2607.02283"
authors: ["Juwei Shen", "Yujie Wu", "Changwen Chen"]
published: "2026-07-02"
---

# Dendritic In-Context Learning in Single-Layer SNN (DendriCL)

## Core Insight

**In-context learning requires neither attention, depth, nor inference-time plasticity: a single compartment with online-LMS dynamics is sufficient.**

This paper challenges the fundamental assumption that ICL in SNNs requires synaptic plasticity during inference. Instead, it demonstrates that the subthreshold dynamics of a single dendritic compartment already implement a complete online learning algorithm.

## Key Contributions

### 1. Paradigm Shift: Dendrite as Computational Substrate
- **Previous assumption**: Dendrites are passive conduits for error/teacher signals
- **New insight**: Dendritic compartment IS the computational substrate
- Subthreshold dynamics of single dendritic compartment = complete online learning algorithm

### 2. DendriCL Architecture
- **Single-layer** compartmental spiking architecture
- Apical recurrence structurally identical to **leaky online Widrow-Hoff LMS**
- Dynamics-only update collapses architectural depth to single layer
- No attention mechanism required
- No inference-time synaptic plasticity needed

### 3. Performance Breakthrough
- **First SNN to pass Garg-2022 ICL benchmark** at non-trivial task dimensions
- **Seed-stable** at super-dimensional ICL tasks
- Dense Transformers exhibit grokking-style instability at same dimension; DendriCL remains stable
- Linear probe recovers reference online-LMS trajectory from apical membrane with **R² = 0.93**
- Algorithm is structurally embedded in dynamics, not implicitly discovered during training

## Technical Details

### Architecture Components
```
Single SNN Layer
├── Somatic compartment (standard LIF dynamics)
└── Apical dendritic compartment
    ├── Recurrent connections
    └── Subthreshold dynamics ≡ online Widrow-Hoff LMS
```

### Mathematical Equivalence
The apical dendritic recurrence implements:
- Online LMS (Least Mean Squares) update rule
- Leaky integration of prediction errors
- Real-time adaptation without explicit gradient computation

### Biological Plausibility
- Single compartment with realistic biophysics
- No backpropagation through time
- No separate learning phase vs inference phase
- Consistent with known dendritic computation in pyramidal neurons

## Implications

### For Neuroscience
- Provides computational theory for dendritic function
- Explains how single neurons might perform complex learning
- Supports "dendritic democracy" hypothesis
- Bridges gap between biophysics and machine learning

### For AI/ML
- Dramatically reduces architectural complexity for ICL
- Eliminates need for deep stacks or attention
- Enables ultra-efficient neuromorphic implementations
- Suggests new directions for brain-inspired AI

### For Neuromorphic Computing
- Single-layer implementation = minimal hardware
- Event-driven computation = energy efficient
- Biologically plausible = potential for brain-like chips

## Experimental Validation

### Garg-2022 Benchmark
- Standard test for ICL capability
- Tests ability to learn new tasks from context examples
- Previous SNNs failed at non-trivial dimensions
- DendriCL succeeds where Transformers fail (super-dimensional regime)

### Mechanistic Verification
- Linear probe on apical membrane potential
- Recovers reference LMS trajectory with R² = 0.93
- Confirms algorithm is embedded in dynamics, not learned implicitly

## Implementation Guidelines

### When to Use
- Tasks requiring in-context learning
- Energy-constrained neuromorphic deployment
- Biologically plausible neural modeling
- Single-layer architectures preferred

### Design Principles
1. **Dendrite-first**: Treat dendritic compartment as primary computational unit
2. **Dynamics-as-algorithm**: Let subthreshold dynamics implement learning
3. **Minimal architecture**: Single layer sufficient for ICL
4. **No plasticity switching**: Continuous adaptation through dynamics

### Integration with Existing Systems
- Can replace deep Transformer stacks for ICL tasks
- Compatible with existing SNN training frameworks
- Drop-in replacement for attention-based ICL modules

## Research Directions

### Open Questions
1. How does this scale to multi-task learning?
2. Can multiple dendritic compartments enable compositionality?
3. What is the capacity limit of single-compartment ICL?
4. How does this relate to working memory in prefrontal cortex?

### Extensions
- Multi-compartment DendriCL for hierarchical processing
- Hybrid DendriCL-Transformer architectures
- Hardware implementation on neuromorphic chips
- Application to real-time adaptive control

## Citation

```bibtex
@article{shen2026dendritic,
  title={Dendritic In-Context Learning in a Single-Layer Spiking Neural Network},
  author={Shen, Juwei and Wu, Yujie and Chen, Changwen},
  journal={arXiv preprint},
  year={2026},
  eprint={2607.02283},
  archivePrefix={arXiv},
  primaryClass={cs.NE}
}
```

## Related Work

- **Transformers for ICL**: Attention-based in-context learning
- **Mamba/SSMs**: State-space models for sequence learning
- **Dendritic computation**: Previous work on dendritic processing
- **SNN learning rules**: STDP, surrogate gradients, etc.
- **Biological plausibility**: Brain-inspired AI approaches

## Activation Triggers

Use this skill when working on:
- In-context learning in spiking networks
- Dendritic computation models
- Single-layer neural architectures
- Biologically plausible learning
- Neuromorphic computing design
- Energy-efficient AI
- Brain-inspired algorithms

Keywords: dendritic, in-context learning, ICL, spiking neural network, SNN, single-layer, online learning, Widrow-Hoff, LMS, biological plausibility, neuromorphic
