---
name: quantum-signal-processing-orthogonal-poly
description: >
  Quantum Signal Processing (QSP) via orthogonal polynomial theory methodology. 
  Provides analytical angle-finding for QSP protocols using Hermite, Jacobi, and Rogers-Szego polynomial expansions.
  Enables block-encoding of smooth functions with O(log(1/epsilon)) gate complexity.
  Use when: implementing quantum signal processing, quantum algorithm design with orthogonal polynomials,
  quantum function approximation, Hamiltonian simulation, quantum eigenvalue transformation,
  or designing efficient quantum circuits for function encoding.
  Trigger words: quantum signal processing, QSP, orthogonal polynomials, Hermite polynomials,
  Jacobi polynomials, Rogers-Szego, angle-finding, block-encoding, quantum function approximation.
---

# Quantum Signal Processing via Orthogonal Polynomial Theory

## Overview

Quantum Signal Processing (QSP) is a powerful framework in quantum algorithms that enables systematic
construction of quantum circuits to apply polynomial transformations to quantum states. This methodology
characterizes achievable polynomial bases through their orthogonality/biorthogonality properties and derives
explicit QSP angles for standard polynomial families.

Based on: Bernard & Wiebe, "Analytical Angle-Finding and Series Expansions for Quantum Signal Processing via Orthogonal Polynomials" (arXiv: 2605.05321, 2026-05-08)

## Core Methodology

### Step 1: Identify Target Function and Polynomial Family

Map the target function f(x) to an appropriate orthogonal polynomial expansion:

| Polynomial Family | Domain | Best For |
|---|---|---|
| Hermite | (-∞, ∞) | Gaussian-weighted functions, unbounded domains |
| Jacobi | [-1, 1] | Bounded functions, finite intervals |
| Rogers-Szego | Unit circle | Periodic functions, phase estimation |

### Step 2: Series Expansion

Express f(x) as a series in the chosen orthogonal basis:

```
f(x) ≈ Σ c_n * P_n(x)
```

where P_n are orthogonal polynomials and c_n are expansion coefficients computed via the inner product
with respect to the orthogonality measure.

### Step 3: QSP Angle Computation

For each polynomial family, use the derived analytical expressions for QSP angles:

- **Hermite**: Angles derived from recurrence relations of Hermite polynomials
- **Jacobi**: Angles computed from three-term recurrence with parameters (α, β)
- **Rogers-Szego**: Angles from q-series expansions

### Step 4: Circuit Construction

Construct the QSP circuit using the computed angles. The circuit applies the sequence:

```
U_QSP = Π_k [R_z(φ_k) · U · R_z(ψ_k)]
```

where U is the signal operator and φ_k, ψ_k are the computed QSP angles.

### Step 5: Complexity Analysis

For ε-approximation of smooth functions via Hermite series:
- **Gate complexity**: O(log(1/ε))
- **Query complexity**: Determined by polynomial degree
- **Space complexity**: O(1) auxiliary qubits beyond signal register

## Key Results

1. **Orthogonality Characterization**: QSP-achievable polynomials are characterized by their
   orthogonality/biorthogonality with respect to a linear functional admitting an integral representation.

2. **Analytical Angles**: Explicit QSP angle expressions derived for Hermite, Jacobi, and Rogers-Szego families.

3. **Efficient Encoding**: Smooth functions can be block-encoded using O(log(1/ε)) gates via Hermite series expansion.

## Practical Applications

- **Hamiltonian Simulation**: Encode e^{-iHt} using QSP with appropriate polynomial approximation
- **Quantum Machine Learning**: Feature maps via orthogonal polynomial kernels
- **Eigenvalue Filtering**: Spectral transformation using polynomial filters
- **Amplitude Estimation**: QSP-based estimation protocols

## Related Skills

- **quantum-data-reuploading-approximation** — depth-error scaling analysis for fixed vs tunable data re-uploading circuits. Complementary to QSP: while QSP provides optimal polynomial encodings, the data-reuploading skill analyzes the resource cost of removing tunability from encoding circuits, establishing polylogarithmic depth recovery via Gevrey+Jackson+QSP (arXiv: 2606.25598).
- **quantum-ml-data-loading** — quantum data loading optimization and survey of encoding strategies.

## Pitfalls

- Polynomial degree must be chosen to balance approximation accuracy vs circuit depth
- Numerical stability of angle computation degrades for very high-degree polynomials
- QSP requires the target polynomial to satisfy |P(x)| ≤ 1 for x ∈ [-1, 1]
