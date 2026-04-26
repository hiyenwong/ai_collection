---
name: neuro-evolutionary-gauge-covariant
version: 1.0.0
description: "Neuro-evolutionary stochastic architectures in gauge-covariant neural fields. Promotes architecture-level parameters to slow stochastic variables in function space, with Markovian evolutionary scheme compatible with gauge symmetry for architecture search within field-theoretic description. arXiv:2604.20373."
date: 2026-04-23
arxiv_id: "2604.20373"
authors: "Rodrigo Carmo Terin"
categories: "cs.NE, hep-th, nlin.AO"
activation:
  - gauge covariant neural field
  - neuro-evolutionary architecture
  - Lyapunov exponent
  - spectral kernel
  - field theory neural network
  - architecture search
  - stochastic neural field
---

# Neuro-Evolutionary Stochastic Architectures in Gauge-Covariant Neural Fields

## Overview
Extends gauge-covariant stochastic neural-field framework by promoting architecture-level parameters to slow stochastic variables evolving in function space. Introduces a Markovian evolutionary scheme compatible with gauge symmetry, enabling neural architecture search (NAS) directly within the field-theoretic description.

## Key Methodology

### Gauge-Covariant Neural Fields
- Neural network described as continuous field with gauge symmetry
- Architecture parameters become stochastic variables with their own dynamics
- Effective theory uses classical commuting fields

### Diagnostics of Marginality
- **Maximal Lyapunov exponent**: quantifies chaos vs. stability in architecture dynamics
- **Amplification factor**: measures signal propagation through layers
- **Dressed spectral kernels**: capture finite-width corrections to infinite-width limit

### Markovian Evolutionary Scheme
1. Initialize architecture parameters as stochastic variables
2. Evolve via Markov chain in function space
3. Gauge symmetry constrains allowed mutations
4. Fitness evaluated through field-theoretic observables
5. Selection preserves gauge-invariant properties

### Implementation Guidance
- Start from infinite-width (Gaussian process) limit
- Introduce finite-width corrections via dressed kernels
- Use Lyapunov exponent to diagnose training stability
- Evolutionary search navigates architecture space within symmetry constraints

## Key Insights
- Architecture search can be formulated as stochastic dynamics in field space
- Gauge symmetry provides theoretical constraints that regularize search
- Finite-width effects (normally neglected) carry crucial architectural information
- Marginality conditions signal phase transitions in architecture quality

## Pitfalls
- Requires familiarity with quantum field theory formalism
- Computational cost of spectral kernel evaluation
- Gauge-fixing ambiguities may affect practical implementation
- Bridging continuous theory to discrete architectures is non-trivial

## References
- arXiv: [2604.20373](https://arxiv.org/abs/2604.20373)
- Key terms: neural architecture search, gauge theory, neural tangent kernel, Lyapunov exponent, field theory, stochastic optimization
