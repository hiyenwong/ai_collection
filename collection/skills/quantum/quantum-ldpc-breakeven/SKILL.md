---
name: quantum-ldpc-breakeven
description: Breakeven demonstration methodology for quantum low-density parity-check (qLDPC) codes on trapped-ion hardware.
platforms: [linux, macos, windows]
tags: [quantum-error-correction, qLDPC, trapped-ion, fault-tolerant, OMG-architecture]
arxiv: 2606.06455
---

# Breakeven Demonstration of Quantum LDPC Codes

**Paper**: arXiv:2606.06455 - "Breakeven demonstration of quantum low-density parity-check codes"
**Authors**: Edwin Tham et al.
**Date**: 2026-06-04

## Core Achievement

**First breakeven demonstration** of quantum low-density parity-check (qLDPC) codes with:
- Logical error rate **9× better** than previous superconducting demonstration
- Qubit lifetimes **comparable to or exceeding** trapped-ion qubits
- 4 logical qubits encoded into 18 physical qubits

## Key Methodology

### OMG Architecture (Optical-Metastable-Ground)

Novel implementation enabling:
- **Addressable mid-circuit measurement and reset**
- **No ion transport required**
- **No dedicated coolant ions**
- Significantly reduced runtime and ion count overhead

### Code Families Demonstrated

1. **qLDPC codes**: High-rate quantum error-correcting codes
2. **Topological codes**: Surface code alternatives
3. **Concatenated codes**: Classical quantum error correction

### Flexibility Advantage

- **9 different codes** demonstrated on single device
- **No hardware reconfiguration** needed
- **Trapped-ion flexibility**: Adapt to different connectivity requirements

## Technical Details

### qLDPC Code Implementation

- Encoding: 4 logical qubits into 18 physical qubits
- Connectivity: Varying qubit connectivity requirements
- Performance: Up to 9× improvement vs superconducting

### Breakeven Achievement

- Logical qubit lifetime ≥ physical qubit lifetime
- Some instances slightly exceed trapped-ion qubit lifetimes
- First demonstration of practical qLDPC advantage

### OMG Architecture Benefits

1. Mid-circuit measurement capability
2. Addressable reset operations
3. No ion transport overhead
4. No coolant ion requirements
5. Reduced runtime consumption

## Comparison with Previous Work

### vs Superconducting qLDPC

- **9× better** logical error rate
- Different hardware platform (trapped-ion)
- No long-range coupler requirements

### vs Surface Codes

- Higher encoding rates
- Reduced physical qubit overhead
- Different connectivity requirements

## Research Significance

- First practical demonstration of qLDPC advantage
- Validates high-rate quantum error correction
- Demonstrates trapped-ion flexibility for QEC
- Establishes OMG architecture for efficient QEC

## Implementation Insights

### Trapped-Ion Advantages

- Flexible connectivity without hardware changes
- High-fidelity operations
- Long coherence times
- Addressable operations

### qLDPC Benefits

- Higher encoding rates vs surface codes
- Reduced qubit overhead
- Scalable error correction
- Breakeven performance achieved

## Related Skills

- [[quantum-error-correction-methods]] - QEC overview
- [[trapped-ion-quantum-computing]] - Trapped-ion hardware
- [[quantum-ldpc-decoding]] - qLDPC decoding algorithms

## References

- arXiv:2606.06455 - Original paper
- qLDPC literature - Quantum LDPC codes
- OMG architecture - Optical-metastable-ground implementation

**Activation**: qLDPC, quantum-error-correction, trapped-ion, breakeven, OMG-architecture, fault-tolerant