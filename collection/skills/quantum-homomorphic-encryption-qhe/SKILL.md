---
name: quantum-homomorphic-encryption-qhe
description: "Quantum Homomorphic Encryption (QHE) methodology — enables computation on encrypted quantum states using Quantum One-Time Pad (QOTP) framework. Covers homomorphic gate decompositions, key update rules, and Clifford+T circuit evaluation. Activation: quantum homomorphic encryption, QHE, QOTP, encrypted quantum computation, privacy-preserving quantum."
---

# Quantum Homomorphic Encryption (QHE)

Quantum homomorphic encryption methodology based on arXiv:2604.19256 (Hernández-Bueno et al., April 2026).

## Core Concept

**Quantum Homomorphic Encryption (QHE)** enables computation on encrypted quantum data without decryption, analogous to classical fully homomorphic encryption but for quantum states.

## QOTPH Framework (Quantum One-Time Pad Homomorphic)

Built from the Quantum One-Time Pad (QOTP) scheme, maintaining **information-theoretic security** while supporting homomorphic operations.

### QOTP Basics

For an n-qubit state ρ:
- Encryption: Apply random Pauli operators (X^a * Z^b) where a,b ∈ {0,1}^n
- Key: (a, b) — 2n classical bits
- Decryption: Apply inverse Pauli operators

### Homomorphic Gate Evaluation

The key insight: quantum gates transform predictably under Pauli encryption.

**Clifford gates**: Transform Pauli keys via conjugation
- H: X → Z, Z → X (swap key bits)
- S: X → Y = iXZ (update key: b → b ⊕ a)
- CNOT: Propagates key between control and target qubits

**T gate (non-Clifford)**: Requires special handling
- Introduces phase that depends on key
- Need key update protocol or interactive correction

### Key Update Rules

For each gate g applied to encrypted state:
1. Compute g's effect on Pauli operators: g P g† = P'
2. Update encryption key to reflect P' instead of P
3. Non-interactive for Clifford gates
4. T gates may require additional protocol

### Supported Operations

- **Clifford+T circuits**: Universal quantum computation
- **Controlled operations**: Multi-qubit gates with encrypted controls
- **Parameterized operations**: Variational quantum algorithm primitives
- **Delegated computation**: Outsourced quantum processing on untrusted hardware

## Implementation Procedure

1. **Setup**: Generate QOTP key (a, b) for each qubit
2. **Encrypt**: Apply X^a * Z^b to input state
3. **Evaluate**: Apply gates, updating keys after each operation
4. **Decrypt**: Apply inverse Pauli operations with final keys

## Experimental Validation

- Tested on simulated environments (noise models)
- Validated on real quantum processors (IBM Q)
- Correctness verified under circuit-level noise
- Key secrecy preserved under real-device constraints

## Applications

- **Cloud quantum computing**: Run algorithms on untrusted quantum hardware
- **Blind quantum computation**: Hide both input and algorithm from provider
- **Variational algorithms**: VQE, QAOA on encrypted data
- **Quantum machine learning**: Privacy-preserving QML inference
- **Multi-party quantum computation**: Secure collaborative quantum processing

## Security Properties

- **Information-theoretic**: Security doesn't depend on computational assumptions
- **Perfect secrecy**: Encrypted state is maximally mixed to adversary
- **Non-interactive evaluation**: No communication needed during computation (Clifford circuits)

## Limitations

- **T-gate overhead**: Non-Clifford gates require additional resources
- **Key management**: 2n bits per qubit, grows with circuit depth
- **Noise sensitivity**: Errors accumulate during homomorphic evaluation
- **NISQ constraints**: Limited by current hardware coherence times

## Related Concepts

- **Classical FHE**: Fully homomorphic encryption for classical data
- **Blind quantum computing**: Protocol for private quantum computation
- **Quantum secure multi-party computation**: Multi-party quantum protocols
- **Delegated quantum computation**: Outsourcing quantum computation securely

## Reference

- arXiv:2604.19256 — "Quantum Homomorphic Encryption: Towards Practical and Private Computation on Untrusted Quantum Hardware"
- Authors: Jon Hernández-Bueno, Oscar Lage, Marivi Higuero, Jasone Astorga