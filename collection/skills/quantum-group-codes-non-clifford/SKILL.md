---
name: quantum-group-codes-non-clifford
description: Quantum group codes for non-Clifford logic — CSS codes with addressable and parallelizable transversal multi-control-Z gates, quasi-quadratic time decoder from AG code lifting. Reduces magic-state distillation complexity by almost linear factor.
category: quantum
trigger_words: ["quantum group codes", "non-Clifford logic", "transversal CZ", "magic state distillation", "AG code lifting", "class field theory", "parallelizable non-Clifford", "quasi-quadratic decoder"]
---

# Quantum Group Codes for Non-Clifford Logic

**Source**: arXiv:2606.27211 — Gasnier & Guémard (2026-06-25)

## Overview

A framework defining quantum CSS codes from classical quasi group codes that support **transversal multi-control-Z gates** that are both **addressable** and **parallelizable**, enabling efficient non-Clifford gate circuits at the logical level.

## Core Methodology

### 1. Quantum Group Code Construction
- Start with classical quasi group codes over alphabet F_q
- Lift to quantum CSS codes supporting transversal C^m Z gates
- Key property: gates are both addressable (target specific qubits) and parallelizable (run multiple simultaneously)

### 2. AG Code Lifting via Class Field Theory
- Input: good quantum AG code over F_q with transversal C^m Z gate
- Apply class field theory lifting to underlying classical AG code
- Output: quantum group code over F_{q^2} with:
  - Transversal C^m Z gate
  - Addressable and parallelizable C^{m-1} Z gates

### 3. Quasi-Quadratic Time Decoder
- Previous quantum AG codes: cubic-time decoder
- New construction: quasi-quadratic time decoder with linear decoding radius
- **Result**: magic-state distillation time complexity reduced by almost linear factor

## Technical Patterns

### Pattern 1: Transversal Gate Preservation
```
Classical code with property P
  → Quantum CSS code preserving P
  → Transversal gate implementation
```

### Pattern 2: Field Extension Lifting
```
Code over F_q
  → Class field theory lift
  → Code over F_{q^2} with enhanced properties
```

### Pattern 3: Decoder Complexity Reduction
```
Cubic decoder → Quasi-quadratic decoder → Linear decoding radius
```

## Applications

- **Magic state distillation**: Reduces overhead for non-Clifford gate implementation
- **Fault-tolerant quantum computing**: Parallelizable non-Clifford gates reduce circuit depth
- **Quantum error correction**: Improved decoding complexity for large-scale codes

## When to Use

- Designing quantum error correcting codes with transversal non-Clifford gates
- Optimizing magic state distillation protocols
- Building fault-tolerant quantum circuits with reduced depth
- Implementing addressable multi-qubit gates in CSS codes

## Key Insight

The lifting procedure from class field theory is the critical innovation — it simultaneously improves decoder complexity AND adds gate parallelizability, where previous approaches could only achieve one or the other.
