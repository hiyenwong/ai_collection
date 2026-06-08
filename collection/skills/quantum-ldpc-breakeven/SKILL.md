---
name: quantum-ldpc-breakeven
description: "Breakeven demonstration methodology for quantum low-density parity-check (qLDPC) codes on trapped-ion platforms. Combines coding theory (mathematics) with experimental quantum error correction to achieve logical qubit lifetimes matching physical qubit performance."
category: quantum-computing
---

## Context

Quantum low-density parity-check (qLDPC) codes are a leading candidate for fault-tolerant quantum computing, offering higher encoding rates than planar surface codes. This methodology addresses the challenge of implementing qLDPC codes on physical hardware, which typically requires long-range couplers.

Source: arXiv:2606.06455 (Tham et al., June 2026)

## Core Methodology

### 1. Trapped-Ion Platform Selection

**Key advantage**: Trapped-ion systems allow arbitrary qubit connectivity without hardware reconfiguration, making them ideal for testing qLDPC codes that require non-local stabilizer measurements.

### 2. Optical-Metastable-Ground (OMG) Architecture

Implement addressable mid-circuit measurement and reset using OMG states:
- **Optical**: Use for state preparation and readout
- **Metastable**: Use as ancilla for syndrome extraction
- **Ground**: Use as computational qubits

**Benefit**: Eliminates need for ion transport or dedicated coolant ions, reducing runtime and ion count overhead.

### 3. Multi-Code Family Testing

Demonstrate codes across three families on the same device:
1. **qLDPC codes**: High-rate, non-local stabilizers
2. **Topological codes**: Surface codes, planar layouts
3. **Concatenated codes**: Hierarchical protection

### 4. Breakeven Verification Protocol

Measure logical error rate vs physical error rate:
- Encode k logical qubits into n physical qubits
- Perform repeated error correction cycles
- Compare logical qubit lifetime to physical qubit T1/T2
- **Breakeven criterion**: Logical error rate ≤ physical error rate per cycle

## Implementation Steps

1. Prepare trapped-ion register with N qubits
2. Implement OMG architecture for mid-circuit measurement
3. Encode logical qubits using qLDPC parity-check matrix
4. Run syndrome extraction cycles
5. Apply corrections based on syndrome decoding
6. Measure logical state fidelity over time
7. Compare with unencoded physical qubit performance

## Key Results (2606.06455)

- **Code**: 4 logical qubits encoded in 18 physical qubits (qLDPC)
- **Performance**: Logical error rate better than previous superconducting demonstrations
- **Breakeven**: Some instances achieve qubit lifetimes ≥ physical qubit T1
- **Platform**: Trapped-ion with OMG architecture

## Pitfalls

- **Hardware complexity**: qLDPC codes typically need long-range couplers (avoided with trapped ions)
- **Decoding overhead**: Syndrome decoding for qLDPC codes is more complex than surface codes
- **Calibration**: OMG states require precise laser control and timing
- **Comparison baseline**: Must compare against same physical qubit platform, not different technology

## Verification

1. Run logical qubit memory experiment for ≥ 100 error correction cycles
2. Measure logical error rate per cycle
3. Compare with physical qubit error rate (T1, gate errors)
4. Confirm logical lifetime ≥ physical T1 for breakeven claim

## Activation

quantum ldpc, qldpc breakeven, trapped ion error correction, OMG architecture, quantum error correction codes, qec breakeven, high-rate quantum codes, 量子LDPC, 量子纠错突破
