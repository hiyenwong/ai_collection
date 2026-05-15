---
name: quantum-resource-distillation
description: >
  Universal quantum resource distillation methodology via composite generalised
  quantum Stein's lemma. Provides fundamental limits on resource conversion rates
  for quantum entanglement distillation and general quantum resource theories.
  Use when: quantum resource distillation, quantum Stein's lemma, entanglement
  distillation, resource conversion, quantum thermodynamics, composite hypothesis
  testing, quantum hypothesis testing (arXiv: 2605.15174).
---

# Universal Quantum Resource Distillation via Composite Quantum Stein's Lemma

## Overview

The composite generalised quantum Stein's lemma provides a universal framework for
quantum resource distillation. The key insight is that the optimal rate at which
desired target states can be obtained from a given supply is fundamentally bounded
by a generalised relative entropy measure.

## Core Principles

### Quantum Resource Theories

A resource theory consists of:
- **Free states** F: States that cost nothing to prepare
- **Free operations** O: Operations that don't generate resources
- **Resource states**: States outside F that contain useful properties

### Stein's Lemma in Resource Distillation

The composite quantum Stein's lemma states:

The optimal distillation rate R of a resource is bounded by:
R ≤ inf_σ∈F D(ρ||σ)

where D(·||·) is the quantum relative entropy and the infimum is taken over all
free states σ in the set F.

### Distillation Protocol

1. **Start**: n copies of resource state ρ^⊗n
2. **Apply free operations**: O_n ∈ O (free operations)
3. **Goal**: Output m copies of target state τ^⊗m
4. **Rate**: R = lim_{n→∞} m/n

The optimal rate is given by the composite Stein's bound:
R* = inf_σ∈F D(ρ||σ)

## Key Results

### Single-Resource Distillation

For a single resource state ρ and target τ:
- Rate = D_min(ρ||F) where D_min is the min-relative entropy
- Achieved via typical subspace measurement

### Composite Settings

When the free set F is composite (union of convex sets):
- Rate = min_{k} inf_{σ∈F_k} D(ρ||σ)
- Accounts for multiple free state families

### Irreversibility

- Distillation rate ≠ Formation rate in general
- Gap quantified by regularised relative entropy
- Reversibility holds only for specific resource theories

## Application Workflow

### Step 1: Identify Resource Theory

Determine the free states F and free operations O:
- Entanglement theory: F = separable states, O = LOCC
- Coherence theory: F = incoherent states, O = MIO/DIO
- Athermality: F = thermal states, O = thermal operations

### Step 2: Characterise Free States

For the specific resource theory:
- Parametrize the set F
- Determine its convex structure
- Identify extremal points if computationally tractable

### Step 3: Compute Distillation Bound

R* = inf_{σ∈F} D(ρ||σ)

Use numerical methods:
- Convex optimization for convex F
- Semidefinite programming for SDP-representable F
- Monte Carlo sampling for large systems

### Step 4: Construct Protocol

Design asymptotically achieving protocol:
- Typical subspace projection
- Measurement in resource eigenbasis
- Post-selection and amplification

## Computational Methods

### Relative Entropy Calculation

For states ρ and σ:
D(ρ||σ) = Tr[ρ(log ρ - log σ)]

Numerical approaches:
- Diagonalize both states in common basis
- Use matrix logarithm via scipy.linalg.logm
- Handle zero eigenvalues with epsilon regularization

### Composite Optimization

For F = ∪_k F_k:
```python
import numpy as np
from scipy.optimize import minimize

def composite_stein_bound(rho, free_families):
    """Compute inf over composite free set."""
    bounds = []
    for F_k in free_families:
        # Compute inf D(rho||sigma) over sigma in F_k
        bound = minimize_relative_entropy(rho, F_k)
        bounds.append(bound)
    return min(bounds)
```

## Activation Keywords

- quantum resource distillation
- quantum Stein's lemma
- entanglement distillation rate
- resource conversion
- composite hypothesis testing quantum
- quantum hypothesis testing
- free state distillation

## Related Papers

- arXiv:2605.15174 (Lami, Berta, Chiribella)
