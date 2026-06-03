---
name: fault-tolerant-ancilla-preparation-bch
description: "Efficient fault-tolerant ancilla preparation for quantum BCH codes via cyclic symmetry. Two-stage approach using non-fault-tolerant preparation + entanglement distillation with cyclic symmetry exploitation. arXiv: 2605.19471."
---

# Fault-Tolerant Ancilla Preparation for Quantum BCH Codes

**arXiv**: 2605.19471 (May 2026)
**Authors**: Kohei Yamamoto, Keisuke Fujii
**Category**: quant-ph

## Overview

Framework for efficient fault-tolerant ancilla preparation for quantum BCH codes, leveraging cyclic symmetry to reduce overhead in fault-tolerant quantum computing (FTQC).

## Problem
- FTQCs require large numbers of physical qubits
- High-rate quantum error correcting codes (QECCs) efficiently embed logical qubits into physical qubits
- Quantum BCH codes offer high rates and large code distances
- No fault-tolerant ancilla preparation method specialized for quantum BCH codes existed

## Two-Stage Approach

### Stage 1: Non-Fault-Tolerant Preparation
- Prepare ancilla states using standard (non-FT) circuits
- Lower overhead but susceptible to errors

### Stage 2: Entanglement Distillation
- Purify the prepared states to fault-tolerant quality
- **Key innovation**: Leverage cyclic symmetry of quantum BCH codes
- Determines which non-FT circuits can successfully produce FT states
- Lower spatial overhead than conventional distillation circuits

## Key Results
- Demonstrated on quantum BCH codes up to 127 qubits
- Lower spatial overhead than conventional distillation
- Lower logical error rates under circuit-level noise model
- Particularly suitable for highly connected platforms (neutral atom systems)

## Design Principles

### Cyclic Symmetry Exploitation
1. Identify cyclic symmetry group of the quantum BCH code
2. Use symmetry to constrain valid distillation circuits
3. Reduce search space for effective distillation protocols
4. Achieve lower overhead through symmetry-guided circuit design

### Performance Benchmarking
- Evaluate under circuit-level noise model (realistic settings)
- Compare spatial overhead vs conventional methods
- Measure logical error rates across code distances

## Activation
quantum BCH code, fault-tolerant ancilla, entanglement distillation, cyclic symmetry, quantum error correction, FTQC, high-rate code

## Pitfalls
- Method requires codes with cyclic symmetry structure
- Two-stage approach adds circuit depth vs single-stage methods
- Best suited for highly connected quantum hardware (neutral atoms)
- Distillation circuit design must respect code's cyclic structure

## Reusable Patterns

### Pattern 1: Symmetry-Guided Circuit Design
Use algebraic symmetries of error-correcting codes to constrain and optimize quantum circuit construction. This reduces the search space for valid circuits and enables lower-overhead implementations.

### Pattern 2: Two-Stage Fault Tolerance
Separate state preparation (cheap, error-prone) from error purification (expensive, error-free). This decoupling allows optimization of each stage independently.

### Pattern 3: Code-Specific Distillation
Design distillation protocols tailored to specific code families rather than using generic approaches. Code structure (cyclic symmetry, stabilizer properties) guides protocol selection.
