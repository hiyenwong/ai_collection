---
name: quantum-ldpc-breakeven-demonstration
description: Breakeven demonstration of quantum low-density parity-check (qLDPC) codes using trapped-ion quantum computers. Demonstrates nine different QEC codes on a single device, achieving breakeven performance with 4 logical qubits encoded into 18 physical qubits.
platforms: [all]
tags: [quantum-computing, error-correction, qldpc, trapped-ion, fault-tolerant, breakeven]
---

# Quantum LDPC Breakeven Demonstration

**Paper**: arXiv:2606.06455 - "Breakeven demonstration of quantum low-density parity-check codes"
**Date**: June 4, 2026
**Authors**: Edwin Tham, Michael L. Goldman, Shantanu Debnath, Ashay N. Patel, Jyothi Saraladevi, Jason Nguyen, Erik Nielsen, Neal Pisenti, Kenneth Wright, John Gamble, Nicolas Delfosse

## Overview

High-rate quantum low-density parity-check (qLDPC) codes are a leading candidate for fault-tolerant quantum computing. This work demonstrates breakeven performance - where logical qubit lifetimes match or exceed physical qubit lifetimes - using trapped-ion quantum computers.

## Key Innovations

1. **Multi-Code Flexibility**: Demonstrated nine different quantum error-correcting codes on a single trapped-ion device without hardware reconfiguration
2. **Three Code Families**: Spanned qLDPC codes, topological codes, and concatenated codes
3. **Breakeven Achievement**: Achieved logical error rates better than previous superconducting qubit demonstrations
4. **OMG Architecture**: Novel optical-metastable-ground architecture for addressable mid-circuit measurement and reset

## Technical Details

### Code Implementation
- **Encoding**: 4 logical qubits encoded into 18 physical qubits
- **Connectivity**: Flexible implementation without requiring long-range couplers
- **Performance**: Logical error rate significantly better than previous demonstrations

### OMG Architecture Benefits
- Addressable mid-circuit measurement and reset
- No ion transport required
- No dedicated coolant ions needed
- Reduces runtime and ion count overhead

## Applications

- Fault-tolerant quantum computing
- Quantum error correction implementation
- Trapped-ion quantum computer design
- High-rate quantum code design

## Methodology Workflow

1. **Code Selection**: Choose appropriate qLDPC code topology
2. **Hardware Mapping**: Implement on trapped-ion system using OMG architecture
3. **Measurement Protocol**: Mid-circuit measurements without transport
4. **Error Analysis**: Compare logical vs physical qubit lifetime

## Activation Keywords

quantum LDPC, qLDPC, trapped-ion, quantum error correction, fault-tolerant, breakeven, OMG architecture, mid-circuit measurement, quantum codes

## Related Skills

- quantum-error-correction-methods
- quantum-fault-tolerance-benchmark
- quantum-neuromorphic-computing
- quantum-system-engineering

## References

- arXiv:2606.06455 (primary source)
- Quantum LDPC codes theory
- Trapped-ion quantum computing architectures
- Surface code comparison
