---
name: blind-quantum-computation
description: >
  Blind quantum computation methodology for secure cloud quantum computing.
  Enables clients to delegate quantum computations to remote servers without
  revealing input, output, or algorithm details. Use when: (1) designing secure
  quantum cloud protocols, (2) analyzing quantum privacy guarantees, (3) implementing
  measurement-based blind quantum computing, (4) evaluating modular quantum processor
  architectures for privacy-preserving computation. Based on arXiv:2605.14656.
  Activation: blind quantum computation, secure quantum cloud, quantum privacy,
  delegated quantum computing, blind QC, 量子盲计算, 安全量子云.
---

# Blind Quantum Computation (BQC)

## Overview

Blind quantum computation allows a client with limited quantum capabilities to
delegate a quantum computation to a remote quantum server while keeping the input,
output, and algorithm hidden. The server performs the computation but learns nothing
about what it is computing.

## Key Principles

### 1. Information-Theoretic Security

BQC provides security guaranteed by quantum mechanics itself, not computational
assumptions. The server cannot distinguish between different computations being
performed.

### 2. Measurement-Based Quantum Computing (MBQC)

The primary framework for BQC uses measurement-based quantum computing:

- Server prepares a large entangled cluster state
- Client specifies computation through measurement angles
- Measurement angles are encrypted (rotated by secret random angles)
- Server measures and reports results; client unrotates

### 3. Protocol Flow

```
Client (limited quantum)          Server (full quantum)
     |                                  |
     |--- 1. Prepare initial states --->|
     |                                  |--- Creates cluster state
     |--- 2. Encrypted angles --------->|
     |                                  |--- Measures qubits
     |<-- 3. Measurement results -------|
     |--- 4. Adapt next angles -------->|
     |                                  | (repeats)
```

### 4. Modular Processor Architecture

Recent advances (arXiv:2605.14656) demonstrate BQC on modular superconducting
processors:

- Multiple quantum modules connected via entanglement links
- Each module handles a portion of the computation
- Entanglement between modules enables distributed blind computation
- Reduces per-module qubit requirements

## Implementation Patterns

### Pattern 1: Universal Blind Quantum Computing (UBQC)

```
For each computation step:
  1. Client chooses measurement angle θ_i
  2. Client generates random key r_i
  3. Client sends δ_i = θ_i + φ_i + r_i * π to server
  4. Server measures at angle δ_i, returns result b_i
  5. Client computes corrected result: b_i ⊕ r_i
```

### Pattern 2: Classical-Client BQC

For clients with NO quantum capabilities:

- Use computational assumptions (LWE hardness)
- Server prepares states via trapdoor claw-free functions
- Less efficient but requires only classical client

## Security Considerations

1. **Verifiability**: Add trap qubits to detect malicious servers
2. **Composability**: BQC protocols compose with other quantum protocols
3. **Efficiency**: Communication overhead is linear in circuit size
4. **Fault Tolerance**: BQC can be combined with error correction

## Applications

- **Secure quantum cloud computing**: Run algorithms on IBM/Qiskit/AWS without
  revealing proprietary algorithms
- **Quantum money**: Blind verification of quantum states
- **Quantum zero-knowledge**: Prove statements about quantum data
- **Multi-party quantum computation**: Multiple clients compute jointly

## Related Concepts

- **Measurement-based quantum computing**: Cluster states, graph states
- **Quantum homomorphic encryption**: Computation on encrypted quantum data
- **Quantum secure direct communication**: Direct transmission without keys
- **Device-independent protocols**: Security without trusting devices

## References

- Broadbent, Kashefi, Fitzsimons (2009): Universal Blind Quantum Computation
- arXiv:2605.14656: Blind Quantum Computation on a Modular Superconducting Processor
