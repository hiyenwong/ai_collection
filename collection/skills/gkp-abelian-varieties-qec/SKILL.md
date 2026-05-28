---
name: gkp-abelian-varieties-qec
description: "GKP (Gottesman-Kitaev-Preskill) quantum error correction codes through the lens of complex abelian varieties and algebraic geometry. Provides a mathematical dictionary between GKP code structures and classical objects in abelian variety theory: theta functions as code space, theta group as Pauli operators, automorphisms as Clifford gates, isogeny as stabilizer concatenation. Use when: designing or analyzing GKP codes, optimizing bosonic quantum error correction, applying algebraic geometry to quantum codes, studying lattice-based quantum error correction, analyzing Gaussian unitary implementations of logical gates, or working with bosonic continuous-variable quantum computing."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.28784"
  published: "2026-05-27"
  authors: "Maxence Mayrand, Baptiste Royer"
  tags: [quantum, algebraic-geometry, number-theory, error-correction, gkp, bosonic]
---

# GKP Codes via Complex Abelian Varieties

## Overview

GKP (Gottesman-Kitaev-Preskill) codes are bosonic quantum error-correcting codes built from symplectically integral lattices. This framework establishes a precise mathematical dictionary between GKP code theory and classical algebraic geometry of polarized complex abelian varieties.

## Core Dictionary

| GKP Concept | Abelian Variety Object |
|---|---|
| Lattice Λ | Symplectically integral lattice |
| Code space | Theta functions H⁰(X, L) |
| Logical Pauli gates | Theta group elements |
| Passive Clifford gates | Automorphisms of polarized variety (X, L) |
| Stabilizer concatenation | Isogeny of abelian varieties |
| Noise threshold | Systolic invariant (shortest displacement in polarization kernel) |

## Key Mathematical Results

### Asymptotic Isometric Encoding

The encoding map from the logical qudit space to the physical oscillator becomes asymptotically isometric as the lattice scale increases. This justifies the common physics heuristic that GKP codes "approximately" encode finite-dimensional states.

### Clifford Gates from Gaussian Unitaries

Every logical Clifford gate on a GKP code is realized by a Gaussian unitary operation. This provides the mathematical foundation for fault-tolerant gate implementation in continuous-variable quantum computing.

### Failure Probability and Systolic Geometry

For noise of small variance σ², the logical failure probability is governed to first order by the shortest nontrivial displacement in the kernel of the polarization isogeny. This is a systolic invariant of the underlying polarization, connecting code performance to geometric optimization on the moduli space of polarized abelian varieties.

## Usage Patterns

### Pattern 1: Analyzing GKP Code Structure

To analyze the structure of a GKP code defined by lattice Λ:

1. Identify the symplectic form on Λ
2. Construct the polarized abelian variety (X, L) from Λ
3. Map logical operators to theta group elements
4. Identify Clifford gates as automorphisms of (X, L)

### Pattern 2: Optimizing Code Performance

To optimize a GKP code for noise resilience:

1. Express the noise model in terms of displacement operators
2. Identify the polarization isogeny kernel
3. Compute the systolic invariant (shortest nontrivial displacement)
4. Optimize over the moduli space of polarized abelian varieties to maximize the systole

### Pattern 3: Concatenation via Isogeny

To concatenate a GKP code with a discrete stabilizer code:

1. Identify the stabilizer code as defining an isogeny
2. Compose the isogeny with the polarization
3. The resulting polarized variety encodes the concatenated code
4. Logical operators transform under the isogeny pullback

## Error Handling

### Large Variance Noise

The systolic approximation for failure probability applies only for small-variance noise. For larger noise, use the full theta function analysis or numerical simulation.

### Non-Symplectic Lattices

The framework requires symplectically integral lattices. For non-symplectic lattices, first find a symplectic embedding or use alternative code constructions.

## Related Skills

- [[bosonic-gkp-parity-encoding]] - Loss-tolerant GKP communication using parity encoding
- [[bosonic-grid-states-qec]] - Bosonic QEC using GKP grid states
- [[quantum-error-correction-methods]] - General QEC patterns
