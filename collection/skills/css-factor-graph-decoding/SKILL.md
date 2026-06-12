---
name: css-factor-graph-decoding
description: "CSS quantum error correction syndrome decoding via factor-graph formulation and belief propagation. Use when: implementing CSS code decoders, comparing joint BP vs four-state BP for syndrome decoding, formulating QEC decoding as factor graph inference, designing belief propagation decoders for stabilizer codes. Keywords: CSS code, syndrome decoding, factor graph, belief propagation, QEC decoder, Tanner graph, stabilizer code."
---

# CSS Factor-Graph Syndrome Decoding

> Factor-graph formulation of CSS syndrome decoding unifying joint BP and four-state BP approaches, showing their equivalence through state relabeling.

## Metadata
- **Source**: arXiv:2605.05132
- **Author**: Kenta Kasai
- **Published**: 2026-05-06

## Core Methodology

### Key Insight
CSS codes have two independent check matrices (X and Z stabilizers) imposing binary parity-check constraints on Pauli error components. The posterior probability factors as a binary factor graph with **two Tanner graphs coupled by local joint prior** at each qubit.

### Technical Framework

**Factor Graph Structure:**
1. Two Tanner graphs: one for X-checks, one for Z-checks
2. Coupled via local joint prior P(e_X, e_Z) at each qubit node
3. Retains channel correlation between X and Z error components

**Two Equivalent Formulations:**

1. **Joint BP**: Run sum-product on binary factor graph with coupled Tanner graphs
   - Each qubit has two binary variables (e_X, e_Z)
   - Messages flow along both Tanner graphs
   - Local prior couples the two variables

2. **Four-State BP**: Single factor graph with 4-state Pauli labels {I, X, Y, Z}
   - Each edge carries message over 4 states
   - Equivalent to joint BP after relabeling: (e_X, e_Z) → Pauli state

**Equivalence Proof:** After relabeling the four local Pauli states and marginalizing irrelevant binary components, both algorithms compute identical posterior weights, messages, and beliefs.

## Implementation Guide

### Joint BP Algorithm
```
For each iteration:
  1. X-graph: send messages along X-Tanner graph (binary BP)
  2. Z-graph: send messages along Z-Tanner graph (binary BP)
  3. Couple: at each qubit, update joint prior P(e_X, e_Z)
  4. Marginalize: compute posterior P(e_X, e_Z | syndrome)
  5. Decode: choose most likely Pauli error
```

### Four-State BP Algorithm
```
For each iteration:
  1. Initialize: messages m(σ) for σ ∈ {I, X, Y, Z}
  2. Check nodes: parity-check constraints on Pauli labels
  3. Variable nodes: combine incoming messages with channel prior
  4. Update: send new messages along edges
  5. Decode: argmax over 4 Pauli states
```

## Applications
- CSS code decoder design (surface codes, LDPC codes)
- Comparing decoder performance across formulations
- Understanding channel correlation exploitation in QEC
- Syndrome extraction optimization for fault-tolerant QC

## Pitfalls
- Joint BP requires careful handling of correlated noise models
- Four-state BP has higher per-message complexity (4 states vs 2)
- Both formulations assume independent error events between qubits
- Convergence not guaranteed for graphs with short cycles

## Related Skills
- css-syndrome-decoding
- quantum-error-correction-methods
- lottery-bp-decoding
- iceberg-error-detection
