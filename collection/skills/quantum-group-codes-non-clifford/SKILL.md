---
name: quantum-group-codes-non-clifford
description: >
  Quantum group codes methodology for non-Clifford logic with enhanced decoding, addressability and
  parallelizability. Framework based on classical quasi group codes defining quantum CSS codes supporting
  transversal multi-control-Z gates. Uses AG code lifting from class field theory for improved decoding
  complexity. Use when: designing quantum error correcting codes, implementing non-Clifford gates at logical
  level, magic state distillation optimization, quantum LDPC code construction, or algebraic geometry codes
  for quantum computing. Trigger words: quantum group codes, non-Clifford gates, transversal gates, AG codes,
  magic state distillation, CSS codes, quasi group codes, parallelizable gates, addressable gates.
---

# Quantum Group Codes for Non-Clifford Logic

arXiv: 2606.27211 | Gasnier, Guémard (2026)

## Core Framework

Define quantum CSS codes from classical **quasi group codes** supporting transversal multi-control-Z gates
that are both **addressable** and **parallelizable**, enabling efficient implementation of non-Clifford gate
circuits at the logical level.

## Key Construction

### Lifting Procedure
1. Start with good quantum AG code over F_q with transversal C^m Z gate
2. Apply lifting from class field theory to underlying classical AG code
3. Obtain quantum group code over F_{q²} supporting:
   - Transversal C^m Z gate
   - Addressable and parallelizable C^{m-1} Z gates

### Complexity Improvement
- **Previous quantum AG codes**: cubic-time decoder
- **This work**: quasi-quadratic time decoder with linear decoding radius
- **Result**: ~linear factor decrease in magic-state distillation time complexity

## Usage Guidelines

### For Code Design
1. Choose base AG code parameters for desired rate and distance
2. Apply class field theory lifting procedure
3. Verify transversal gate support and parallelizability
4. Implement quasi-quadratic decoder

### For Magic State Distillation
- Leverage improved decoding complexity for faster distillation protocols
- Use addressable/parallelizable gates to reduce circuit depth
- Consider alphabet size trade-offs (F_q vs F_{q²})

## Applications
- Fault-tolerant quantum computing with non-Clifford gates
- Magic state distillation optimization
- Quantum LDPC code construction
- Algebraic geometry quantum codes

## Activation Keywords
quantum group codes, non-Clifford gates, transversal gates, AG codes, magic state distillation, CSS codes, quasi group codes, parallelizable gates
