---
name: isogeny-graph-quantum-sampling
category: quantum
description: Quantum sampling of supersingular elliptic curves via isogeny graph spectral theory. Proves Quantum Unique Ergodicity for isogeny graphs, enabling secure instantiation of isogeny-based cryptographic protocols without trusted setup.
version: "1.0"
tags: [quantum-computing, number-theory, isogeny-graphs, cryptography, spectral-theory]
source: "arxiv:2602.02263"
arxiv_id: "2602.02263"
date: "2026-05-22"
---

# Isogeny Graph Quantum Sampling

## Overview

This methodology enables provably secure sampling of random supersingular elliptic curves with unknown endomorphism rings — a critical primitive for isogeny-based cryptographic protocols (CGL hash function, SIDH variants) without requiring trusted setup.

## Core Technique

### Quantum Unique Ergodicity on Isogeny Graphs

The key insight is proving the **Quantum Unique Ergodicity (QUE) conjecture** for supersingular ℓ-isogeny graphs:

- **Eigenvector delocalization**: All eigenvectors of the isogeny graph adjacency matrix are completely delocalized
- **ε-separation property**: Eigenvalues satisfy stronger separation than previously conjected (removes heuristic assumption in quantum money protocols)

### Algorithm Variants

#### Variant 1: Booher-based Sampling
- **Complexity**: Õ(log⁴p) quantum gates (heuristic)
- **Under GRH**: Õ(log¹³p) quantum gates
- **Security**: Based on average-case hardness of endomorphism ring problem
- **Use case**: General secure curve sampling

#### Variant 2: Oriented Curve Sampling
- Samples uniform 𝒪-oriented curves for any imaginary quadratic order 𝒪
- **Security**: Based on hardness of Vectorization problem
- **Use case**: Structured curve generation with specific orientations

## Mathematical Framework

### Isogeny Graph Structure
- Vertices: Supersingular elliptic curves over 𝔽_{p²}
- Edges: ℓ-isogenies between curves
- Graph properties: (ℓ+1)-regular, Ramanujan

### Spectral Delocalization
1. Compute adjacency matrix A of supersingular ℓ-isogeny graph
2. Analyze eigenvector distribution via QUE
3. Prove complete delocalization → uniform sampling guarantee

### Security Model
- **Endomorphism Ring Problem**: Given supersingular curve E, find End(E)
- **Vectorization Problem**: Given oriented curves (E, ι), (E', ι'), find isogeny φ: E → E' preserving orientation
- Both problems believed hard for quantum computers (post-quantum secure)

## Implementation Patterns

### Pattern 1: Secure Curve Generation
```
Input: Prime p, isogeny degree ℓ
Output: Supersingular curve E/𝔽_{p²} with unknown End(E)

1. Initialize quantum superposition over all supersingular curves
2. Apply quantum walk on isogeny graph
3. Measure to sample uniformly from the supersingular set
4. Verify curve is supersingular (check trace of Frobenius ≡ 0 mod p)
```

### Pattern 2: Interactive Verification Protocol
```
1. Sample curve using quantum algorithm
2. Run quantum computation verification protocol
3. Prove correctness of sampling without revealing endomorphism ring
4. Output verified secure curve for cryptographic instantiation
```

## Applications

1. **CGL Hash Function**: Secure instantiation without trusted setup
2. **SIDH/SIKE variants**: Safe parameter generation
3. **Quantum Money**: Removes heuristic eigenvalue separation assumption
4. **Isogeny-based KEM**: Provably secure public key generation

## Key Theorems

- **Theorem 1**: QUE holds for supersingular ℓ-isogeny graphs
- **Theorem 2**: ε-separation of eigenvalues (stronger than Kane-Sharif-Silverberg conjecture)
- **Corollary**: Quantum polynomial-time secure sampling with high probability

## Pitfalls

- **GRH dependency**: Õ(log¹³p) bound requires Generalized Riemann Hypothesis
- **Heuristic variant**: Õ(log⁴p) is heuristic, not rigorously proven
- **Verification overhead**: Interactive quantum verification adds protocol complexity
- **Prime selection**: Must use cryptographically appropriate prime p

## References

- arXiv:2602.02263 - "On the Spectral theory of Isogeny Graphs and Quantum Sampling"
- CGL hash function (Charles-Goren-Lauter)
- Kane-Sharif-Silverberg quantum money protocol
