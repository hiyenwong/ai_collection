---
name: quantum-ldpc-breakeven
description: qLDPC code breakeven demonstration methodology for fault-tolerant quantum computing using trapped-ion hardware
category: quantum
---

# Quantum LDPC Breakeven Demonstration

## Methodology
High-rate quantum low-density parity-check (qLDPC) codes are leading candidates for fault-tolerant quantum computing, featuring higher encoding rates than planar alternatives such as the surface code.

## Key Insights
1. **Trapped-ion flexibility**: A single trapped-ion device can demonstrate multiple QEC code families (qLDPC, topological, concatenated) without hardware reconfiguration
2. **OMG architecture**: Optical-metastable-ground architecture enables addressable mid-circuit measurement and reset without ion transport or dedicated coolant ions
3. **Breakeven performance**: qLDPC code encoding 4 logical qubits into 18 physical qubits achieved logical error rate up to 9x better than superconducting solid-state demonstrations
4. **Qubit lifetime**: Some instances achieved lifetimes comparable to or exceeding trapped-ion qubits

## Implementation Patterns
- Use trapped-ion platforms for flexible QEC code testing
- Leverage OMG architecture for mid-circuit operations
- Compare across code families on identical hardware
- Target breakeven: logical error rate <= physical error rate

## Activation
qLDPC, quantum error correction, fault tolerance, trapped-ion, breakeven, logical qubits
