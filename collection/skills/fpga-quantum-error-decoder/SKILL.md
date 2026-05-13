---
name: fpga-quantum-error-decoder
description: >
  Real-time surface-code quantum error correction using FPGA-based neural network
  decoders. Covers hardware-integrated control architecture for closed-loop QEC
  with deterministic low-latency feedback. Includes NN decoder implementation on
  FPGA, latency optimization, mid-circuit feedback correction, and Pauli-frame
  updating. Use when: implementing real-time QEC systems, designing FPGA-based
  quantum decoders, building hardware-integrated quantum control, or developing
  low-latency feedback systems for fault-tolerant quantum computing.
  Trigger keywords: FPGA decoder, real-time QEC, surface code, neural network decoder,
  closed-loop quantum feedback, low-latency quantum control.
---

# FPGA-Based Quantum Error Decoder

From arXiv:2605.04892 "Real-time Surface-Code Error Correction Using an FPGA-based
Neural-Network Decoder" (Yang et al., 2026).

## Core Architecture

### Hardware-Integrated Control System

The system combines a superconducting quantum processor with an FPGA-based
neural network decoder in a closed-loop configuration.

**Key performance metrics**:
- Deterministic closed-loop latency: **550 ns**
- NN decoding time: **124 ns**
- QEC cycle: **1.25 μs**
- Code: Distance-3 surface code

## Technique 1: FPGA-Based Neural Network Decoder

### Real-Time Syndrome Processing

Errors are inferred from repeated stabilizer (syndrome) measurements in the
surface code. The decoder must operate within each QEC cycle to prevent
error accumulation.

**Implementation pattern**:
1. Syndrome measurements from quantum processor → FPGA
2. Neural network on FPGA decodes syndromes to error patterns
3. Feedback corrections applied within the QEC cycle

**NN decoder design principles**:
- Must be implementable on FPGA hardware (fixed-point arithmetic)
- Latency budget: < 200 ns for d=3 surface code
- Accuracy must match offline decoding performance

## Technique 2: Closed-Loop Feedback Correction

### Latency Budget Management

Total latency breakdown:
- Syndrome readout: ~100 ns
- NN decoding: 124 ns
- Control signal generation: ~200 ns
- Gate application: ~126 ns
- **Total: 550 ns < 1.25 μs QEC cycle**

**Critical constraint**: Decoding must complete before the next QEC cycle
begins, otherwise errors accumulate faster than they are corrected.

## Technique 3: Mid-Circuit Feedback Correction

### Beyond Pauli-Frame Updating

For non-Clifford logical circuits, Pauli-frame updating alone becomes
insufficient. Active feedback correction during the circuit is required.

**When Pauli-frame is insufficient**:
- Non-Clifford gates (T gates, Toffoli)
- Adaptive circuits with measurement-dependent operations
- Logical operations requiring real-time syndrome feedback

**Implementation**:
1. Detect that accumulated Pauli frame cannot be tracked classically
2. Apply active physical correction based on NN decoder output
3. Continue circuit execution with corrected state

## Technique 4: Robustness Under Varying Error Conditions

The system maintains performance comparable to offline decoding across
different error rates and error types, demonstrating robustness.

**Key finding**: Real-time NN decoding achieves logical performance
matching offline decoding — no accuracy trade-off for low latency.

## Hardware Requirements

- FPGA with sufficient DSP slices for NN inference
- Low-latency interconnect between quantum processor and FPGA
- Classical control electronics for gate application

## Scalability Pathway

- Current: Distance-3 surface code (9 data qubits)
- Target: Distance-5 and above for practical fault tolerance
- Scaling challenge: NN decoder complexity grows with code distance
- Solution: Hierarchical or parallel decoder architectures

## Pitfalls

- NN decoder must be trained on representative error distributions
- FPGA resource constraints limit NN model complexity
- Interconnect latency dominates at larger distances
- Mid-circuit feedback requires precise timing synchronization

## Activation

Keywords: FPGA quantum decoder, real-time error correction, surface code decoder,
neural network QEC, low-latency quantum feedback, closed-loop quantum control,
mid-circuit correction
