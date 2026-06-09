---
name: qldpc-breakeven-demo
description: Breakeven demonstration methodology for quantum low-density parity-check (qLDPC) codes on trapped-ion quantum computers. Design, implement, and benchmark qLDPC error correction with OMG architecture for mid-circuit measurement and reset.
category: quantum-computing
version: 1.0.0
source: arXiv:2606.06455v1
authors: Edwin Tham, Michael L. Goldman, Shantanu Debnath et al.
date: 2026-06-04
tags:
  - quantum-error-correction
  - qldpc
  - trapped-ion
  - fault-tolerance
  - mid-circuit-measurement
  - omg-architecture
---

# qLDPC Breakeven Demonstration

Breakeven demonstration methodology for quantum low-density parity-check (qLDPC) codes on trapped-ion quantum computers (arXiv:2606.06455v1, June 2026).

## Trigger Conditions

Use when:
- Designing quantum error correction experiments on trapped-ion or other flexible-connectivity platforms
- Comparing qLDPC codes vs topological codes vs concatenated codes
- Implementing mid-circuit measurement and reset for fault-tolerant QEC
- Evaluating qLDPC breakeven performance against physical qubit error rates
- Designing OMG (optical-metastable-ground) architecture for addressable measurement
- Benchmarking logical qubit lifetimes against physical qubit lifetimes

## Background

High-rate qLDPC codes are a leading candidate for fault-tolerant quantum computing. They feature higher encoding rates than planar alternatives (surface code) but require flexible qubit connectivity. Trapped-ion systems uniquely enable testing multiple QECC families on the same device without hardware reconfiguration.

## Core Methodology

### 1. Multi-Code Family Comparison on Single Device

Test three QECC families on the same quantum hardware without reconfiguration:
- **qLDPC codes**: High encoding rate, flexible connectivity requirements
- **Topological codes**: Surface code variants, local connectivity
- **Concatenated codes**: Hierarchical encoding structure

### 2. qLDPC Implementation Steps

1. **Code Selection**: Choose qLDPC code parameters (e.g., [[18,4,d]] encoding 4 logical into 18 physical qubits)
2. **Connectivity Mapping**: Map code graph to available qubit connectivity (trapped-ion all-to-all advantage)
3. **OMG Architecture Setup**:
   - Use optical-metastable-ground states for addressable mid-circuit measurement
   - Enable measurement and reset without ion transport
   - Avoid dedicated coolant ions (saves runtime and ion count)
4. **Syndrome Extraction**: Implement stabilizer measurements via mid-circuit operations
5. **Decoding**: Apply minimum-weight perfect matching or BP-OSD decoder
6. **Logical Error Rate Measurement**: Track logical error rate vs physical error rate

### 3. Breakeven Evaluation

Breakeven is achieved when logical error rate ≤ physical qubit error rate:
- Measure logical error rate through repeated QEC cycles
- Compare against physical qubit T1/T2 coherence times
- Identify error suppression factor (e.g., 9× improvement over previous demonstrations)

### 4. Hardware-Aware Code Design

For each hardware platform, optimize:
- **Trapped-ion**: Exploit all-to-all connectivity for non-local stabilizers
- **Superconducting**: Focus on surface codes and locally-connected qLDPC variants
- **Photonic**: Use measurement-based approaches with cluster states

## Implementation Patterns

### OMG Mid-Circuit Measurement Pattern
```
# Pseudocode for OMG-based mid-circuit measurement
1. Initialize data qubits + ancilla qubits
2. Apply syndrome extraction gates (CNOT/entangling)
3. Pump ancilla to metastable state (optical transition)
4. Read out metastable state (fluorescence detection)
5. Reset ancilla via optical pumping to ground state
6. Continue QEC cycle without ion transport
```

### qLDPC Code Comparison Benchmark
```
# Benchmark multiple QECC families
codes = {
    'qldpc': {'n': 18, 'k': 4, 'type': 'qLDPC'},
    'surface': {'n': 17, 'k': 1, 'type': 'surface_code'},
    'concatenated': {'n': 25, 'k': 1, 'type': 'concatenated'},
}
for code in codes:
    measure_logical_error_rate(code)
    compare_to_physical_error_rate()
```

## Key Findings

1. qLDPC [[18,4]] achieves 9× better logical error rate than previous superconducting demonstration of similar code
2. Breakeven performance achieved — logical qubit lifetime comparable to or exceeding physical qubit lifetime
3. OMG architecture eliminates need for ion transport and dedicated coolant ions
4. Trapped-ion flexibility enables testing 9 QECC families on single device
5. Higher encoding rate of qLDPC vs surface code enables more efficient logical qubit storage

## Pitfalls

- **Connectivity Mismatch**: qLDPC codes require non-local connectivity; superconducting platforms may need SWAP overhead
- **Mid-Circuit Measurement Fidelity**: OMG readout fidelity directly impacts syndrome extraction quality
- **Decoding Latency**: Real-time decoding must complete within coherence time
- **Code Distance Trade-off**: Higher-rate qLDPC codes typically have lower distance than surface codes of similar size

## Verification Steps

1. Run QEC circuit with known input states and measure logical fidelity
2. Vary physical error rate (via gate errors or injected noise) and track logical error scaling
3. Compare logical error rate against break-even threshold (physical error rate)
4. Benchmark syndrome extraction cycle time against qubit coherence times

## Activation

**Keywords**: qldpc, breakeven, quantum error correction, trapped ion, mid-circuit measurement, OMG architecture, logical qubit, fault tolerance, parity check, syndrome extraction, surface code comparison

**arXiv**: 2606.06455
