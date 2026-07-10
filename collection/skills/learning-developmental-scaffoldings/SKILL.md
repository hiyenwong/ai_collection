---
name: learning-developmental-scaffoldings
description: "Developmental scaffoldings methodology for guiding self-organisation through learned pre-patterns. Joint NCA+SIREN model that offloads information to initial conditions, enabling robustness, encoding capacity, and symmetry breaking improvements. Activation: developmental scaffoldings, self-organisation, neural cellular automata, NCA, pre-patterns, morphogenetic, developmental biology, SIREN, information offloading."
---

# Learning Developmental Scaffoldings to Guide Self-Organisation

**Paper:** Learning Developmental Scaffoldings to Guide Self-Organisation
**arXiv:** 2605.14998v1 (2026-05-14)
**Authors:** Milton L. Montero, Elias Najarro, Jakob Schauser, Sebastian Risi
**Categories:** cs.AI, eess.SY, q-bio.QM

## Problem Statement

Natural systems generate complex organization through self-organisation (local interactions → global structure without blueprint). However, biological development is NOT purely self-organizing — significant information is **offloaded to initial conditions**:

- Maternal morphogen gradients in early embryogenesis
- Tissue-level morphogenetic pre-patterns guiding organ formation
- Positional and symmetry-breaking information encoded in starting states

This is analogous to a **memory-compute trade-off** in computational systems: pre-patterns store information that the self-organizing process would otherwise need to compute.

**Key question:** How do pre-patterns and self-organizing dynamics interact, and what information is distributed between them?

## Approach: Joint NCA + SIREN Model

### Architecture

```
[SIREN Pre-Pattern Generator] → [Initial Condition] → [NCA Self-Organization] → [Final Pattern]
      (learned coordinate-           (bias/seed)           (local rules)          (target)
       based pattern gen)
```

**Novel contribution:** Both components are **trained simultaneously**, allowing their interplay to be varied and measured under controlled conditions.

### Components

1. **SIREN (Coordinate-based Pattern Generator)**
   - Generates spatial pre-patterns from coordinate inputs
   - Implicitly encodes target pattern structure
   - Provides initial conditions (seeds/biases) for the NCA

2. **Neural Cellular Automaton (NCA)**
   - Self-organizing system with local interaction rules
   - Evolves from pre-pattern initial state
   - Learns rules that complement (not replace) the pre-pattern

3. **Joint Training**
   - Both components trained end-to-end
   - Loss on final pattern drives learning of both pre-pattern and NCA rules
   - Enables measuring information distribution between components

## Key Findings

### 1. Information-Theoretic Analysis

Joint learning reveals how information is distributed between:
- **Pre-pattern component**: Encodes positional/symmetry-breaking information
- **Self-organizing component**: Encodes local interaction rules

The trade-off between these is measurable and tunable.

### 2. Robustness Improvements

Jointly learned systems are **more robust** than purely self-organizing alternatives:
- Better tolerance to noise in initial conditions
- More reliable convergence to target patterns
- Reduced sensitivity to perturbations during development

### 3. Encoding Capacity

Pre-patterns increase the **diversity of patterns** the system can generate:
- Pure self-organization: limited by local rule expressivity
- With pre-patterns: global structure can be pre-specified

### 4. Symmetry Breaking

Effective pre-patterns provide **symmetry-breaking signals** that:
- Resolve ambiguities in self-organizing dynamics
- Guide development toward specific outcomes
- Enable complex patterns that pure self-organization cannot achieve

### 5. Non-Trivial Pre-Pattern Structure

**Critical insight:** Effective pre-patterns do NOT simply approximate their targets. Instead, they:
- **Bias the developmental dynamics** in ways that facilitate convergence
- Create a **non-trivial relationship** between initial condition structure and dynamics
- Provide the *right kind* of perturbation, not a crude approximation

## Technical Framework

### Information-Theoretic Metrics

- **Pre-pattern information**: I(pre-pattern; target) — how much target info is encoded in initial conditions
- **Self-organization contribution**: I(NCA state progression; target | pre-pattern) — what dynamics add beyond the seed
- **Total mutual information**: Decomposed into pre-pattern vs. dynamics contributions

### Training Objective

```
L = ||NCA(SIREN(x), t=T) - target||²
```

Both SIREN and NCA parameters are updated simultaneously to minimize this loss.

## Applications to Neuroscience

### 1. Brain Development Modeling

- **Cortical column formation**: Pre-patterns could represent molecular gradients that guide cortical area specification
- **Retinotopic mapping**: Initial positional biases guide self-organizing connectivity
- **Critical periods**: Information offloading may explain developmental windows

### 2. Neural Circuit Development

- **Axon guidance**: Morphogenetic gradients provide pre-patterns for self-organizing synapse formation
- **Cell-type specification**: Initial positional information guides differentiation programs
- **Network topology**: Pre-patterns may encode structural constraints on self-organizing connectivity

### 3. Neurodevelopmental Disorders

- Misaligned pre-patterns could model developmental disruptions
- Understanding information distribution between genetic programs and self-organization

### 4. Neural Network Architecture Design

- **Inductive biases as pre-patterns**: Structured initialization as a form of information offloading
- **Developmental AI**: Models that grow rather than are trained end-to-end
- **Robust initialization**: Understanding why certain initializations lead to better convergence

## Comparison with Pure Self-Organization

| Aspect | Pure NCA | Joint NCA + Pre-Pattern |
|--------|----------|------------------------|
| Robustness | Moderate | High |
| Encoding capacity | Limited by local rules | Extended by global seed |
| Symmetry breaking | Random/stochastic | Guided |
| Convergence reliability | Variable | Consistent |
| Information source | Dynamics only | Dynamics + initial conditions |

## Related Concepts

- **Morphogenetic pre-patterns**: Biological gradients that guide development
- **Memory-compute trade-off**: Storing information vs. computing it
- **Neural Cellular Automata**: Self-organizing systems with neural local rules
- **SIREN**: Sinusoidal Representation Networks for coordinate-based pattern generation
- **Information offloading**: Distributing computation across initial conditions and dynamics
- **Developmental biology**: Embryogenesis, morphogenesis, cell differentiation

## Implementation Considerations

1. **NCA Design**: Local rules with sufficient expressivity for target patterns
2. **SIREN Architecture**: Frequency tuning affects pattern resolution
3. **Joint Optimization**: Gradient flow through both components requires careful balancing
4. **Information Analysis**: Requires multiple runs to estimate mutual information
5. **Pattern Complexity**: Start simple (gradients, stripes) before complex targets

## Related Skills

- brain-inspired-nca
- neural-cellular-automata-attractors
- brain-inspired-cellular-automata
- neurotrain-local-learning-snn-benchmarking

## Activation Keywords

- developmental scaffoldings
- self-organisation
- neural cellular automata
- NCA
- pre-patterns
- morphogenetic
- developmental biology
- SIREN
- information offloading
- memory-compute trade-off
- joint learning NCA
- brain development modeling
- morphogenesis
- developmental AI

## References

- arXiv: https://arxiv.org/abs/2605.14998
- PDF: https://arxiv.org/pdf/2605.14998
