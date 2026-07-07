---
name: quantum-cut-sparsifiers
description: "Hamiltonian sparsification methodology showing any n-qubit Quantum Cut Hamiltonian can be sparsified to O~(n/eps^2) terms while preserving energy using invariant subspace decomposition."
---

# Quantum Cut Sparsifiers

## Description

Methodology for sparsifying Quantum Cut (QC) Hamiltonians. Any n-qubit QC Hamiltonian can be reduced to O~(n/eps^2) terms while preserving the energy of every state up to a factor of 1 ± eps. Uses invariant subspace decomposition and operator-valued inequalities rather than standard leverage score sampling.

## Activation Keywords

- quantum cut sparsifier
- hamiltonian sparsification
- quantum graph sparsification
- QC hamiltonian reduction
- quantum spectral approximation
- Kikuchi graph approximation
- 量子切割稀疏化
- 哈密顿量稀疏化

## Tools Used

- terminal: Run quantum simulations with sparse Hamiltonians
- execute_code: Implement sparsification algorithms and spectral analysis

## Usage Patterns

### Pattern 1: Hamiltonian Sparsification via Invariant Subspaces
Instead of leverage score sampling (which gives polynomially worse bounds for 2^n dimensional matrices):
1. Decompose the Hamiltonian action into invariant subspaces
2. Apply operator-valued inequality of Alon and Kozma (2020)
3. Sample edges using importance sampling within each subspace
4. Verify spectral approximation: |E_sparse(ψ) - E_full(ψ)| ≤ eps · E_full(ψ)

### Pattern 2: Expander Graph Extension
For arbitrary graphs:
1. Perform expander decomposition on the input graph
2. Apply sparsification to each expander component
3. Combine sparsified components preserving global spectral properties
4. The same sampling scheme works simultaneously for all Kikuchi graph levels ℓ

### Pattern 3: Kikuchi Graph Approximation
The sparsification can be interpreted as:
1. Importance sampling scheme for edges of arbitrary graph G
2. Sampled graph's Kikuchi graph at level ℓ approximates G's Kikuchi graph spectrally
3. Single sampling scheme works for all ℓ simultaneously

## Instructions for Agents

### Step 1: Identify QC Hamiltonian Structure
- Express Hamiltonian as sum of Pauli string terms
- Identify the underlying graph structure
- Determine target sparsification parameter eps

### Step 2: Invariant Subspace Decomposition
- Find invariant subspaces of the Hamiltonian
- Use symplectic properties of Pauli strings
- Decompose action into block-diagonal form where possible

### Step 3: Apply Sampling Scheme
- Use importance sampling within each invariant subspace
- Sample O~(n/eps^2) terms total
- Preserve energy spectrum within 1 ± eps factor

### Step 4: Verify Spectral Approximation
- Check that sampled Hamiltonian approximates original on all states
- Verify Kikuchi graph spectral properties at multiple levels
- Compare with leverage score baseline (should be polynomially better)

## Error Handling

### Leverage Score Sampling Fails
For 2^n dimensional matrices, leverage scores give polynomially worse bounds:
- Switch to invariant subspace decomposition approach
- Use operator-valued inequalities instead of matrix concentration

### Expander Decomposition Overhead
For dense graphs, expander decomposition adds overhead:
- Check if direct subspace decomposition suffices
- Balance between decomposition cost and sparsification quality

## Key Results from Paper (arXiv: 2606.09728)

- Any n-qubit QC Hamiltonian sparsifiable to O~(n/eps^2) terms
- Preserves energy of every state up to 1 ± eps
- Leverage score sampling gives polynomially worse bounds (2^n dimension)
- Invariant subspace decomposition + Alon-Kozma inequality enables efficient sparsification
- Extends to all expander graphs, then to all graphs via expander decomposition
- Same sampling scheme works for all Kikuchi graph levels simultaneously

## References

- arXiv: 2606.09728 - "Quantum Cut Sparsifiers"
- Authors: Arpon Basu, Joshua Brakensiek, Pravesh K. Kothari, Aaron Putterman
- Published: 2026-06-08
- Categories: quant-ph, cs.DS
