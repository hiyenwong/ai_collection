---
name: entanglement-generalization-pac-bayesian
description: PAC-Bayesian generalization theory for quantum reinforcement learning. Analyzes entanglement as structural complexity axis via Fisher effective dimension. Use when evaluating generalization of quantum policies, designing PQCs for RL, or studying entanglement-generalization trade-offs.
version: 1.0.0
author: Hermes Agent
license: MIT
source: arXiv:2607.06230
tags: [quantum-reinforcement-learning, PAC-Bayesian, generalization, entanglement, Fisher-information, quantum-policies]
activation: quantum policy generalization, entanglement generalization tradeoff, Fisher effective dimension, PAC-Bayesian quantum, PQC generalization bound, quantum reinforcement learning, parameterized quantum circuits
---

# Entanglement-Generalization Trade-off via PAC-Bayesian Analysis

**Source**: arXiv:2607.06230 - "Entanglement as a Structural Complexity Axis: A PAC-Bayesian View of Generalization in Quantum Policies and Value Functions"

## Core Theory

Generalization in quantum reinforcement learning is governed not by raw parameter count but by the **effective dimension of the Fisher geometry** induced by the circuit. This quantity is inflated by entanglement, making entangling connectivity an independent axis of structural complexity.

### Key Findings

1. **Fisher effective dimension > parameter count**: Circuits with larger Fisher effective dimension exhibit larger train-test gaps; parameter count is a weak predictor
2. **Entanglement hurts generalization**: Non-entangled circuits consistently generalize better than entangled circuits of equal parameter count
3. **Ranking certificate**: The bound correctly orders circuits with identical parameter count, which parameter-counting bounds cannot do
4. **Effect persists under real noise**: Validated on IBM Heron quantum processor under real noise

### Mechanism

```
Entangling connectivity → Increased Fisher effective dimension → Larger train-test gap → Worse generalization
```

## Methodology

### Step 1: Compute Fisher Effective Dimension

For a parameterized quantum circuit (PQC) with parameters θ:

1. Compute the Fisher information matrix F(θ) from the circuit's output distribution
2. The effective dimension is the effective rank of F(θ), not the raw parameter count
3. Use eigenvalue spectrum: d_eff = (Tr F)² / Tr(F²)

### Step 2: PAC-Bayesian Generalization Bound

The generalization gap is bounded by a function of:
- Fisher effective dimension d_eff
- Number of training samples n
- A prior distribution over circuit parameters

### Step 3: Controlled Experiments

Design experiments that:
- Fix the number of trainable rotations
- Vary only entanglement structure (connectivity patterns)
- Measure train-test gap across: supervised classification, contextual bandits, value-function generalization

## Practical Implications

### For Quantum RL Design

1. **Minimize unnecessary entanglement** in policy/value circuits
2. **Use Fisher effective dimension** as complexity measure, not parameter count
3. **Prefer shallow, low-connectivity** circuits when generalization matters
4. **Trade-off entanglement-expressivity vs generalization**

### Circuit Design Guidelines

- Start with minimally entangled ansätze
- Add entangling gates only when expressivity requires it
- Monitor Fisher effective dimension during circuit search
- Use the PAC-Bayesian bound as a ranking certificate

## Validation Domains

The methodology was validated across:
1. Supervised classification with PQCs
2. Quantum contextual bandits
3. Value-function generalization
4. End-to-end multi-step policy learning (partially resolved due to high return variance)
5. Real hardware (IBM Heron) under noise

## Partial-Correlation Analysis

Controls confirmed that Fisher effective dimension screens off entangling pattern and controls for:
- Training accuracy
- Readout architecture
- Optimizer rules
