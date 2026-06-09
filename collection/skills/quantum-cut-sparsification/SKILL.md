---
name: quantum-cut-sparsification
description: "Hamiltonian sparsification methodology for Quantum Cut (QC) Hamiltonians. Achieves O(n) term sparsification in n-qubit systems while preserving energy of every state. Uses invariant subspace decomposition and expander graph techniques."
tags: ["quantum", "sparsification", "hamiltonian", "graph-algorithms", "expander-decomposition", "spectral-approximation"]
related_skills: ["quantum-algorithm-framework-designer", "quantum-hamiltonian-learning-long-times"]
---

# Quantum Cut Sparsification

## Context

Hamiltonian sparsification is a key technique for reducing the complexity of quantum simulations. The Quantum Cut (QC) Hamiltonians are widely studied but suffer from exponential term counts that make simulation intractable.

## Core Methodology

### 1. Main Result
In an n-qubit system, any n-qubit QC Hamiltonian can be sparsified to **O(n)** many terms while preserving the energy of every state up to a multiplicative factor.

### 2. Importance Sampling Scheme
The result provides an importance sampling scheme for graph edges such that:
- The **Kikuchi graph** at level ℓ of the sampled graph is a spectral approximation to the Kikuchi graph of the original graph G
- The **same sampling scheme** works simultaneously for all levels ℓ

### 3. Why Leverage Score Sampling Fails
Standard leverage score sampling (analyzed via matrix concentration inequalities) yields polynomially worse bounds because the underlying matrices have dimension 2^n — exponential in qubit count.

### 4. Invariant Subspace Decomposition
The approach decomposes the action of these matrices into invariant subspaces, avoiding the exponential dimension problem.

### 5. Expander Graph Extension
Using an operator-valued inequality of Alon and Kozma (building on the octopus inequality of Caputo, Liggett, and Richthammer):
- Extends sparsification technique to all expander graphs
- Invokes expander decomposition to extend sparsifier to all graphs

## Implementation Steps

1. Identify the QC Hamiltonian structure in your problem
2. Apply importance sampling to Hamiltonian terms
3. Decompose action into invariant subspaces
4. Apply operator-valued inequalities for spectral approximation bounds
5. For non-expander graphs: use expander decomposition as preprocessing
6. Verify energy preservation on test states

## Pitfalls

- **Leverage score trap**: Standard matrix concentration fails due to 2^n dimension — must use invariant subspace approach
- **Octopus inequality requirement**: The Alon-Kozma inequality requires specific graph properties
- **Expander decomposition overhead**: Converting general graphs to expanders adds preprocessing cost
- **Energy preservation factor**: The sparsified Hamiltonian only approximately preserves energies — the factor depends on sampling quality

## Verification

1. Test on small n-qubit QC Hamiltonians (n ≤ 10)
2. Compare ground state energies: original vs sparsified
3. Verify spectral approximation quality on Kikuchi graphs
4. Measure term count reduction: should achieve O(n) scaling

## Activation

quantum cut sparsification, Hamiltonian sparsification, Kikuchi graph, expander decomposition, spectral approximation, quantum simulation, invariant subspaces, arxiv:2606.09728
