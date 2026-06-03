---
name: quantum-symbolic-simulation
description: >
  Symbolic simulation methodology for quantum circuits with unbounded iteration
  (while loops). Based on QSeqSim, a Qiskit-integrated symbolic backend that
  fills the gap of simulating while-loop quantum programs and their induced
  sequential quantum circuits. Use when: quantum while loops, symbolic quantum
  simulation, Qiskit sequential circuits, unbounded quantum iteration,
  quantum program verification (arXiv: 2605.14881).
---

# QSeqSim: Symbolic Simulation for Quantum While Loops

## Overview

QSeqSim provides a symbolic backend for Qiskit that enables simulation of quantum
programs with unbounded iteration (while loops). Standard quantum simulators
require fixed circuit depth; QSeqSim overcomes this by representing iterative
programs symbolically as sequential quantum circuits.

## Problem Statement

Quantum while loops cannot be directly simulated by standard backends because:
1. Circuit depth is unbounded (loop may iterate arbitrarily many times)
2. Classical measurement outcomes control quantum operations
3. Need symbolic representation of program semantics

## QSeqSim Architecture

### Core Components

1. **Sequential Quantum Circuit (SQC) Representation**
   - Symbolic encoding of unbounded iteration
   - Tracks measurement-conditioned branching
   - Preserves quantum-classical feedback structure

2. **Qiskit Integration**
   - Drop-in backend replacement
   - Supports standard Qiskit quantum operations
   - Extends with while-loop constructs

3. **Symbolic State Evolution**
   - Represents state as sum-over-paths
   - Compresses equivalent branches
   - Provides analytical expressions for output states

### While Loop Semantics

```python
# Conceptual representation
q = QuantumRegister(n)
c = ClassicalRegister(1)

while measure(c[0]) == 0:
    # Quantum operations inside loop
    qc.h(q[0])
    qc.cx(q[0], q[1])
    qc.measure(q[0], c[0])
```

The SQC represents this as an infinite sum truncated at convergence:
|ψ_final⟩ = Σ_{k=0}^{∞} P_k |ψ_0⟩

where P_k is the probability of exactly k iterations.

## Implementation Approach

### Step 1: Parse Quantum Program

Extract program structure:
- Sequential quantum gates
- Classical control flow (if/while)
- Measurement points and feedback

### Step 2: Build Symbolic Circuit

Construct the SQC representation:
- Map each loop body to a superoperator
- Compute convergence criteria
- Determine truncation depth K where ||P_{>K}|| < ε

### Step 3: Execute Simulation

Two modes:
1. **Exact symbolic**: Closed-form expressions (small circuits)
2. **Numerical approximation**: Truncated sum (larger circuits)

### Step 4: Extract Results

- Final quantum state (symbolic or numeric)
- Measurement probability distributions
- Expected loop iteration count

## Key Techniques

### Convergence Analysis

For a while loop with exit probability p per iteration:
- Expected iterations: E[k] = 1/p - 1
- Truncation at K: error ≤ (1-p)^K
- Choose K such that (1-p)^K < ε

### State Compression

Compress equivalent paths in the sum-over-paths:
- Group paths by final classical state
- Merge identical quantum operations
- Use tensor network contraction for efficiency

### Qiskit Backend Interface

```python
from qseqsim import QSeqSimBackend

# Create symbolic backend
backend = QSeqSimBackend()

# Run quantum program with while loops
result = backend.run(qc_with_loops)

# Get results
state = result.get_statevector()
counts = result.get_counts()
```

## Applications

1. **Quantum Algorithm Analysis**
   - Grover's algorithm with unknown number of solutions
   - Variational algorithms with adaptive stopping

2. **Quantum Program Verification**
   - Prove correctness of iterative quantum programs
   - Bound resource usage (gate count, depth)

3. **Quantum Error Correction**
   - Syndrome measurement with repeated rounds
   - Adaptive decoding with feedback

## Limitations

- Exponential in number of qubits (fundamental)
- Loop convergence required (non-terminating loops fail)
- Symbolic expressions grow rapidly with circuit complexity

## Activation Keywords

- quantum while loop
- symbolic quantum simulation
- Qiskit sequential circuit
- unbounded quantum iteration
- quantum program verification
- QSeqSim
- quantum loop simulation

## Related Papers

- arXiv:2605.14881 (Li, Wang, Zhang)
