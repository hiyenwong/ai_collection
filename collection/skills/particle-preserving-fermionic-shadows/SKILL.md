---
name: particle-preserving-fermionic-shadows
description: "Classical shadow estimation for fermionic states with mode-independent sample complexity. Improves worst-case bound for Slater determinant overlap estimation from O(√n log n) to O(η log η), using harmonic analysis on AIII symmetric space."
---

# Particle-Preserving Fermionic Shadows

## Description
Methodology for learning expectation values of particle-preserving operators with respect to unknown η-particle n-mode fermionic states via classical shadows. Achieves mode-independent sample complexity O(η log η) for Slater determinant overlap estimation, reducing from the previous worst-case O(√n log n) bound. Uses harmonic analysis on the AIII symmetric space U(n)/(U(η) × U(n-η)) and Jacobi ensemble techniques.

## Activation Keywords
- fermionic classical shadows
- mode-independent sample complexity
- Slater determinant overlap
- AIII symmetric space quantum
- Jacobi ensembles quantum
- particle-preserving operators
- fermionic state tomography
- 费米子经典阴影
- 模式无关采样复杂度
- Slater行列态重叠

## Core Concepts

### Classical Shadow Estimation for Fermions
- **Problem**: Learn expectation values of particle-preserving operators from unknown fermionic states
- **Key insight**: Particle-preserving structure enables mode-independent sample complexity
- **Randomization**: Approximate unitary designs in first-quantized encoding achieve polylogarithmic circuit depth

### Sample Complexity Improvement
- **Previous worst case**: O(√n log n) samples
- **New bound**: O(η log η) samples (independent of total mode count n)
- **For quadratic observables**: O(η ||h₀||₂²) where h₀ is traceless component
- **Classical post-processing**: O(n η²) for generic dense orbital, O(n² η) for quadratic observables

### AIII Symmetric Space Analysis
- **Reduction**: Extremal shadow variance → harmonic analysis on U(n)/(U(η) × U(n-η))
- **Techniques**: Jacobi ensembles and orthogonal polynomials for integral evaluation
- **Significance**: The mathematical technique may be of independent interest beyond shadows

## Usage Patterns

### Pattern 1: Fermionic State Learning
1. Identify particle number η and mode count n
2. Select appropriate randomization scheme (first-quantized vs second-quantized)
3. Apply classical shadow protocol with O(η log η) samples
4. Post-process classically in O(n η²) time

### Pattern 2: Slater Determinant Overlap Estimation
1. Target state: unknown η-particle n-mode fermionic state
2. Reference state: arbitrary Slater determinant
3. Sample complexity: O(η log η) for fixed additive precision
4. Advantage: exponential improvement when η ≪ n

## Mathematical Framework

### Symmetric Space Decomposition
```
Shadow variance extremal problem
    ↓ reduction
Harmonic analysis on AIII symmetric space U(n)/(U(η) × U(n-η))
    ↓ evaluation
Jacobi ensemble integrals + orthogonal polynomials
    ↓ result
O(η log η) sample complexity bound
```

### Circuit Depth Comparison
- **First-quantized**: Polylogarithmic depth (approximate unitary designs)
- **Second-quantized matchgate**: Linear depth (nearest-neighbor)

## Error Handling
### Sample Complexity Bounds
- If η ≈ n: The O(η log η) bound approaches O(n log n), still better than O(√n log n) for large n
- If observables not particle-preserving: Different shadow protocol required
- If classical post-processing too slow: Consider sparse orbital structure optimization

## References
- arXiv:2606.27254 - Particle-preserving fermionic shadows (West, Cerezo, Larocca 2026)
- Classical shadow tomography literature
- Harmonic analysis on symmetric spaces
