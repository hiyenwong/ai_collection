---
name: bosonic-cyclic-codes-qec
description: "Bosonic cyclic codes methodology for quantum error correction — generalizing rotation-symmetric codes to trade error protection for fault-tolerant logical phase gates via passive Gaussian rotations. Covers cyclic cat codes, Vandermonde codes, and stabilizer-to-gate conversion paradigm. Activation: bosonic codes, cyclic codes, rotation-symmetric, cat code, binomial code, non-Clifford gates, Gaussian rotations, QEC."
category: quantum
tags: ["qec", "bosonic-codes", "error-correction", "non-clifford"]
arxiv_id: "2606.11010"
date_added: "2026-06-11"
---

## Context

Rotation-symmetric bosonic codes (cat codes, binomial codes) provide hardware-efficient quantum error correction against loss and dephasing. However, they are limited to a single native logical Pauli gate — all other logical gates require non-linear operations, blocking practical quantum algorithm execution. Bosonic cyclic codes solve this by enabling a measured tradeoff: sacrifice single-photon-loss detectability to gain multiple fault-tolerant logical phase gates, all achievable via **passive Gaussian rotations**.

## Core Methodology

### 1. Bosonic Cyclic Code Construction

Generalize rotation-symmetric codes by reducing the rotational symmetry order:

- **Original rotation-symmetric code**: Symmetry order N → detects up to N/2 photon losses, 1 logical Pauli gate
- **Bosonic cyclic code**: Reduce symmetry → gain N logical phase gates via passive Gaussian rotations
- **Tradeoff**: Each additional phase gate costs one photon-loss detection capability

### 2. Code Families

- **Cyclic Cat Codes**: Generalization of cat codes with cyclic symmetry
- **Vandermonde Codes**: Generalization of binomial codes using Vandermonde structure
- Both families transfer desirable properties from their rotation-symmetric ancestors

### 3. SU(2) Symmetry and Rotation Gates

- Larger SU(2) symmetry structure yields additional stabilizers and logical Pauli gates
- New non-Clifford gates for the smallest 'kitten' binomial code
- New error detection protocol derived from symmetry structure

### 4. Stabilizer-to-Gate Conversion Paradigm

**General recipe**: Higher-order stabilizers can be converted to logical gates:

1. Identify stabilizer generators of the rotation-symmetric code
2. Select stabilizers to sacrifice (reduce error detection)
3. Convert selected stabilizers to logical phase gates
4. Verify remaining stabilizers still provide adequate error protection
5. Implement gates via passive Gaussian rotations (no non-linear operations needed)

## Implementation Steps

### Design a Bosonic Cyclic Code

```python
# Step 1: Choose rotation symmetry order N
# Higher N → more error protection, fewer phase gates

# Step 2: Select tradeoff point
# Sacrifice k photon-loss detections → gain k logical phase gates
# N - k stabilizers remain for error detection
# k phase gates available via Gaussian rotations

# Step 3: Construct code states
# |0_L⟩ = Σ c_n |n⟩ with cyclic symmetry constraints
# |1_L⟩ = R(π/k)|0_L⟩ where R is rotation operator

# Step 4: Verify properties
# - Logical Pauli gates: check commutation with remaining stabilizers
# - Phase gates: verify implementable via Gaussian rotations
# - Error detection: confirm remaining stabilizers detect expected loss events
```

## Pitfalls

- **Tradeoff awareness**: Each logical phase gate costs one photon-loss detection capability — carefully balance based on target application
- **Gate fidelity**: Passive Gaussian rotations may have lower fidelity than native gates — account for gate errors in QEC budget
- **Code distance reduction**: Reducing symmetry lowers effective code distance — verify fault-tolerance threshold is still met
- **Non-linear operations still needed for some gates**: Phase gates are Gaussian, but other gates (e.g., logical X, CNOT) may still require non-linear operations
- **Multimode extension**: Converting higher-order stabilizers to gates applies to multimode codes but requires careful analysis of cross-mode interactions

## Verification

- [ ] Code states satisfy cyclic symmetry constraints
- [ ] Logical phase gates implementable via passive Gaussian rotations only
- [ ] Remaining stabilizers detect expected photon loss events
- [ ] Non-Clifford gate availability confirmed for target code family
- [ ] SU(2) symmetry structure analyzed for additional stabilizers

## Activation

bosonic codes, cyclic codes, rotation-symmetric, cat code, binomial code, non-Clifford gates, Gaussian rotations, QEC, fault-tolerant gates, Vandermonde codes, stabilizer conversion

## References

- arXiv: 2606.11010 — "Bosonic Cyclic Codes: Trading Stabilizers for Gaussian Non-Clifford Phase Gates"
- Authors: Owen C. Wetherbee, Yijia Xu, Victor V. Albert, Baptiste Royer, Valla Fatemi
