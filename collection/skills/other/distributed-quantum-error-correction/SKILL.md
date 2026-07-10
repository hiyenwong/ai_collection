---
name: distributed-quantum-error-correction
description: >
  Design and analyze distributed quantum error correction (QEC) systems using
  bivariate bicycle (BB) codes in modular quantum computing architectures.
  Covers qLDPC code partitioning across multiple processors, star network
  topology for inter-processor connectivity, BP+OSD decoding, and fault
  tolerance threshold analysis under circuit-level noise. Use when: designing
  modular quantum computers, implementing distributed QEC, partitioning qLDPC
  codes across processors, analyzing inter-processor entanglement overhead,
  or studying BB codes for trapped-ion/neutral-atom platforms.
---

# Distributed Quantum Error Correction

## Overview

Bivariate bicycle (BB) codes — a class of quantum LDPC codes — offer higher
encoding rates than surface codes but require long-range stabilizer connections
impractical on monolithic nearest-neighbor devices. The solution: partition
qubits across modular processors linked by shared Bell pairs.

## Key Concepts

### BB Codes (qLDPC)
- [[144,12,12]] BB code: 144 physical qubits, 12 logical qubits, distance 12
- Encoding rate k/n ≈ 0.083 vs surface code k/n ≈ 1/(2d²)
- Long-range stabilizers require non-local connectivity

### Modular Architecture
- Partition qubits across N processors (4, 6, or 12 typical)
- Each processor: all-to-all internal connectivity (trapped-ion, neutral-atom)
- Inter-processor links: shared Bell pairs via star network
- Nonlocal gate noise scaling factor β relative to local gates

### Star Network Topology
```
    Processor 1 ──┐
    Processor 2 ──┼── Central Hub (shared Bell pair generation)
    Processor 3 ──┤
    ...          ──┘
```

### Decoding Pipeline
1. Syndrome extraction via stabilizer measurements
2. BP+OSD (Belief Propagation + Ordered Statistics Decoding)
3. Monte Carlo simulation for logical error rate estimation
4. Pseudo-threshold analysis across noise parameters

## Design Workflow

### Step 1: Code Selection
Choose qLDPC code parameters [[n,k,d]] based on target logical error rate and
hardware constraints. BB codes offer superior rate-distance tradeoffs.

### Step 2: Partitioning Strategy
Partition n physical qubits across P processors:
- Minimize inter-processor stabilizer crossings
- Balance qubit count per processor (n/P each)
- Ensure each processor's internal connectivity supports local stabilizers

### Step 3: Inter-Processor Connectivity
- Use star network for Bell pair distribution
- Model inter-processor noise as β × local_noise_rate
- β typically 5-100× higher depending on link technology

### Step 4: Threshold Analysis
Vary physical error rate p and noise scaling β to map:
- Pseudo-threshold curves for each processor count
- Logical error rate vs physical error rate
- Scaling behavior as P increases

## Critical Design Considerations

1. **Inter-processor overhead**: Each stabilizer crossing requires a Bell pair
2. **β sensitivity**: Performance degrades sharply when β > 10 for surface-level
   noise; BB codes tolerate higher β due to sparse stabilizer structure
3. **Processor count tradeoff**: More processors → smaller chips but more
   inter-processor crossings
4. **Decoding complexity**: BP+OSD scales O(n·polylog(n)) vs O(n²) for MWPM

## Activation Keywords
- distributed quantum error correction
- modular quantum computing
- qLDPC codes
- bivariate bicycle codes
- BB code
- quantum error correction architecture
- multi-processor quantum computer
- star network quantum
- BP+OSD decoding
- quantum fault tolerance
- 分布式量子纠错
- 模块化量子计算

## Related Concepts
- Surface codes (planar, nearest-neighbor only)
- Trapped-ion quantum computing (all-to-all connectivity)
- Neutral-atom quantum computing (reconfigurable connectivity)
- Quantum LDPC codes (qLDPC)
- Circuit-level noise models
- Fault-tolerant quantum computation (FTQC)

## References
- arXiv:2605.04663 — Distributed Quantum Error Correction with Bivariate Bicycle Codes in a Modular Architecture
