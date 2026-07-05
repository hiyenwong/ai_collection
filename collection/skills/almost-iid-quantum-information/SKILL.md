---
name: almost-iid-quantum-information
description: >
  Alternative definitions and analysis of "almost i.i.d." quantum states for practical
  quantum information theory. The i.i.d. assumption is ubiquitous in quantum information theory
  but too stringent for practical settings. Introduces definitions based on normalized quantum
  Wasserstein distance and local-structure analysis. Use when: analyzing quantum information
  sources beyond i.i.d. assumption, designing quantum protocols for correlated sources,
  studying quantum Wasserstein distance applications, or evaluating practical quantum
  communication/computation under realistic noise models.
  Activation: almost i.i.d. quantum, quantum Wasserstein distance, quantum source correlation,
  non-i.i.d. quantum, quantum information practical, quantum correlated sources.
---

# Almost i.i.d. Quantum Information Theory

Methodology from arXiv:2605.15114 — "New approaches to almost i.i.d. information theory" (Girardi, De Palma, Lami, 2026).

## Problem Statement

The i.i.d. assumption in quantum information theory enables clean asymptotic analysis but
is unrealistic in practice. Physical sources exhibit correlations, memory effects, and
structured dependencies.

## Alternative Definitions

### Definition 1: Normalized Quantum Wasserstein Distance

Define "almost i.i.d." via proximity to i.i.d. states under normalized quantum Wasserstein
distance:

- **Wasserstein metric**: Quantifies transport cost between quantum states
- **Normalization**: Ensures meaningful comparison across system sizes
- **Threshold**: States within ε distance of an i.i.d. state are "almost i.i.d."

### Definition 2: Local Structure Analysis

Based on examining local subsystem properties:

- Analyze reduced density matrices of small subsystems
- Require local statistics to approximate i.i.d. behavior
- Global correlations may exist but remain locally invisible

## Applications

1. **Quantum channel capacity**: Extend Shannon-like results to correlated sources
2. **Quantum key distribution**: Security proofs under realistic noise models
3. **Quantum data compression**: Coding theorems for non-i.i.d. ensembles
4. **Quantum thermodynamics**: Work extraction from correlated quantum states

## Key Insight from Mazzola/Sutter/Renner (arXiv:2603.15792)

The original "almost i.i.d." class was proposed based on physical plausibility arguments.
The new definitions provide:

- **Mathematical tractability**: Enable rigorous proofs
- **Physical grounding**: Connect to measurable quantities
- **Computational accessibility**: Enable practical verification

## When to Apply

- Designing quantum protocols for realistic (non-i.i.d.) noise environments
- Analyzing quantum communication over correlated channels
- Extending asymptotic quantum information results to finite-size regimes
- Evaluating quantum advantage under practical source models
