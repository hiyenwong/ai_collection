---
name: loop-composition-quantum
description: "Loop composition methodology for quantum algorithms. Modeling quantum algorithms as compositions of loop structures for modular algorithm design and analysis (arXiv: 2605.07518)"
---

# Loop Composition in Quantum Algorithms

## Description

Methodology for modeling quantum algorithms as compositions of loop structures. Enables modular algorithm design, compositional reasoning about quantum algorithm correctness, and systematic optimization of iterative quantum protocols.

## Activation Keywords
- loop composition quantum
- quantum algorithm composition
- modular quantum algorithms
- iterative quantum protocols
- quantum algorithm patterns
- 量子算法组合
- 循环组合量子

## Core Methodology

### Step 1: Loop Structure Identification
- Identify iterative components in quantum algorithms (amplitude amplification, phase estimation, QAOA)
- Decompose algorithm into: initialization -> loop body -> measurement
- Each loop body is a quantum channel (CPTP map)

### Step 2: Composition Rules
- **Sequential composition**: Loop A followed by Loop B = B o A
- **Nested composition**: Loop B inside Loop A = iterate(iterate(A, k), m)
- **Parallel composition**: Loop A and Loop B on different subsystems = A tensor B

### Step 3: Convergence Analysis
- Fixed point analysis: Find stationary states of loop channel
- Convergence rate: Spectral gap of the loop superoperator
- Error accumulation: Compose error bounds across iterations

### Step 4: Optimization
- Unroll small loops into direct unitaries
- Merge commuting loop bodies
- Replace nested loops with single optimized loop when possible

## Common Patterns
```
Amplitude Amplification Loop:
  [State prep] -> [Oracle] -> [Diffusion] -> repeat k times -> [Measure]

Phase Estimation Loop:
  [State prep] -> [Controlled-U^2^j] for j=0..n-1 -> [Inverse QFT] -> [Measure]

QAOA Loop:
  [Initial state] -> [Cost Hamiltonian] -> [Mixer Hamiltonian] -> repeat p times
```

## Related Skills
- quantum-optimization-qaoa
- variational-quantum-algorithms
- quantum-computing-patterns
