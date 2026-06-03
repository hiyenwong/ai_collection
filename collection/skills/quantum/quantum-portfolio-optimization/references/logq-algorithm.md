# LogQ Algorithm - Quantum-Inspired Classical Optimization

## Overview

LogQ reformulates quantum QUBO solving as classical non-linear continuous
relaxation of variables, eliminating need for quantum hardware.

## Key Advantages

- No Pauli decomposition required
- No quantum measurement overhead
- Gradient-inspired parameter optimization
- Fewer resources than quantum circuits
- Applicable to industrial QUBO problems

## Reformulation Steps

1. Express QUBO as quadratic form: x^T Q x
2. Apply LogQ encoding to reduce dimensionality
3. Reformulate as continuous relaxation problem
4. Use gradient-inspired optimization
5. Round solution to binary if needed

## Applications

- Portfolio optimization
- Fleet optimization
- Charging station placement
- General combinatorial optimization
