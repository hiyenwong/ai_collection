---
name: brain-digital-twins-execution-semantics-v4
description: "Brain digital twins execution semantics survey bridging computational neuroscience to neuromorphic systems - arXiv:2604.13574 (April 2026). Covers physically constrained executability taxonomy, execution regimes, hybrid-time correctness, and neuro-neuromorphic physical systems. Supersedes v3 with systems/runtime perspective."
---

# Brain Digital Twins: Execution Semantics and Neuro-Neuromorphic Systems

**arXiv:** [2604.13574](https://arxiv.org/abs/2604.13574)
**Date:** April 15, 2026
**Author:** Alexandre Muzy
**Categories:** cs.SE, cs.CE, q-bio.NC, cs.NE

## Core Thesis

Brain digital twins aim to provide faithful, individualized computational representations of brains as dynamical systems. Current approaches are **fragmented** across data pipelines, model classes, temporal scales, and computing platforms, preventing preservation of execution semantics across end-to-end workflows.

The paper introduces **physically constrained executability** as a unifying perspective — comparing approaches at the level of execution rather than model form.

## Key Concepts

### Physically Constrained Executability

A framework comparing brain digital twin approaches based on:
1. **Execution state persistence** — whether state survives across executions
2. **Permitted events** — simulation, measurement, actuation
3. **Temporal/causal coupling** — how strongly execution is coupled to neurobiological dynamics
4. **Physical constraints** — shared physical constraints between biological and computational dynamics

### Execution Regimes Taxonomy

The paper proposes a taxonomy ranging from:

| Regime | Description | Coupling |
|--------|-------------|----------|
| **Isolated offline models** | Traditional simulation, no live data | None |
| **Coordinated co-simulation** | Multiple models running with coordination | Weak |
| **Continuously executing digital twins** | Sustained by online data assimilation | Strong |
| **Neuro-neuromorphic physical systems** | Biological and computational dynamics co-executed under shared physical constraints | Physical |

### Why Accuracy Alone Is Insufficient

Accuracy metrics ignore:
- **Semantic interoperability** — how systems communicate meaningfully
- **Hybrid-time correctness** — handling continuous and discrete time together
- **Evaluation protocols** — standardized testing across regimes
- **Scalable reproducible workflows** — reproducibility at scale
- **Safe closed-loop validation** — safety in live brain-computer interfaces

## Research Agenda

1. **Semantic Interoperability** — standardizing how brain models communicate
2. **Hybrid-Time Correctness** — formal methods for mixed continuous/discrete execution
3. **Evaluation Protocols** — standardized benchmarks across execution regimes
4. **Scalable Reproducible Workflows** — tools for reproducible brain modeling
5. **Safe Closed-Loop Validation** — safety frameworks for live brain interfaces

## Applications

- Clinical intervention prediction
- Mechanistic understanding of brain dynamics
- Personalized medicine
- Brain-computer interfaces
- Neuromorphic computing systems

## Related Work

- Brain-DiT foundation models (arXiv:2604.18469)
- Alzheimer's disease progression models (arXiv:2604.18470)
- Higher-order brain interactions (arXiv:2604.17713)
- EEG foundation model adaptation (arXiv:2604.16926)

## Implementation Notes

- Focus on execution semantics, not model architecture
- Consider physical constraints in system design
- Evaluate across multiple coupling regimes
- Prioritize semantic interoperability for integration

## Citations

```bibtex
@article{muzy2026brain,
  title={From Brain Models to Executable Digital Twins: Execution Semantics and Neuro-Neuromorphic Systems},
  author={Muzy, Alexandre},
  journal={arXiv preprint arXiv:2604.13574},
  year={2026}
}
```
