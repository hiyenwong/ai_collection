---
name: intrinsic-locality-dimension-quantum-codes
description: "Intrinsic locality dimension methodology for quantum error-correcting codes. Measures code locality independent of background geometry. Use when: quantum code analysis, stabilizer code design, quantum error correction, topology-geometry relationships in QEC."
---

# Intrinsic Locality Dimension of Quantum Codes

## Description

The Intrinsic Locality Dimension (ILD) framework provides a geometry-independent measure of locality for stabilizer quantum error-correcting codes. Unlike traditional locality measures that depend on embedding qubits in a specific spatial geometry, ILD captures intrinsic code structure through algebraic properties of the stabilizer group.

Based on arXiv:2605.31441 (Lu, Fu & Liu, 2026).

## Core Concept

### Traditional vs. Intrinsic Locality

- **Traditional locality**: Depends on physical embedding (e.g., 2D surface codes have local stabilizers on a lattice)
- **Intrinsic locality**: Defined purely from stabilizer group structure, independent of any background geometry

### Key Results

1. ILD naturally incorporates folding/unfolding equivalences between codes
2. Provides lower bounds on spatial dimensions needed for physical implementation
3. Relates to topological order and code distance scaling

### Mathematical Framework

For a stabilizer code S acting on n qubits:

- ILD(S) = minimum d such that S admits a d-local generating set
- Invariant under local Clifford transformations
- Respects code equivalence (same ILD for equivalent codes)

## Usage Patterns

### Code Analysis

1. Compute ILD for a given stabilizer code
2. Compare ILD across code families to understand structural differences
3. Identify codes that can be embedded in low-dimensional geometries

### Code Design

1. Use ILD as optimization target when designing new QEC codes
2. Balance ILD against code distance and encoding rate
3. Understand tradeoffs between locality and fault tolerance

### Theoretical Insights

1. Study connections between ILD and topological order
2. Analyze how ILD scales with code parameters
3. Relate to holographic and tensor network code constructions

## Activation Keywords
- intrinsic locality dimension
- quantum code locality
- stabilizer code geometry
- QEC code embedding
- 量子码 内禀局部性
- quantum error correction locality
- code distance scaling
- stabilizer group structure

## References
- arXiv:2605.31441 - "Intrinsic locality dimension of quantum codes"
- Related: Quantum LDPC codes, surface codes, topological codes
