---
name: random-dimension-reduction-quantum-learning
description: Random dimension reduction methodology for learning symmetric properties of quantum states. Black-box procedure that replaces dimension with maximum rank in sample complexity. Use when learning symmetric quantum properties, estimating state distances/fidelities, or reducing quantum tomography overhead.
---

# Random Dimension Reduction for Quantum State Learning

## Core Methodology

Procedure simultaneously reduces dimensions of many potentially distinct quantum states while preserving properties invariant under tensor power action of an isometry.

### Key Results

- Black-box method to replace dimension with maximum rank in sample complexity
- Applicable to symmetric properties depending on multiple input states
- Efficient quantum circuit implementation using Schur transform

### Applications

1. **Distance estimation**: Improved upper bounds after dimension reduction + full tomography
2. **Fidelity estimation**: More efficient symmetric property learning
3. **Relative entropy**: Reduced sample complexity for state comparisons

### Implementation

- Apply Schur transform circuit for dimension reduction
- Perform full state tomography on reduced states
- Preserve tensor-power-invariant properties