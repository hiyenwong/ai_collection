---
name: fpga-quantum-decoder
description: "Design FPGA-based neural network decoders for real-time quantum error correction (QEC) in surface code architectures. Covers hardware-software co-design, deterministic low-latency decoding under 1 microsecond, NN decoder implementation on FPGA, closed-loop feedback control, and mid-circuit Pauli-frame correction for non-Clifford logical circuits. Use when building real-time QEC systems, implementing FPGA-based decoders, designing low-latency quantum control hardware, or optimizing surface code decoding throughput for fault-tolerant quantum computing."
---

# FPGA-Based Quantum Error Correction Decoder

## Overview

Surface code QEC requires classical decoding within each QEC cycle (~1-5 μs)
to prevent error accumulation. FPGA-based neural network (NN) decoders achieve
deterministic sub-microsecond latency with hardware parallelism.

## Key Architecture

### Hardware Pipeline
```
Syndrome Measurements → FPGA NN Decoder → Feedback Correction → Qubit Control
     (analog)          (digital logic)     (real-time)         (microwave)
```

### Latency Budget (from experimental results, arXiv:2605.04892)
- NN inference: 124 ns (FPGA-based)
- Full closed-loop: 550 ns
- QEC cycle: 1.25 μs
- Headroom: ~700 ns for measurement + control

### NN Decoder Design
- Input: syndrome measurement history (bit strings)
- Architecture: feedforward or lightweight CNN
- Output: predicted error pattern (Pauli frame update)
- Quantization: INT8 for FPGA efficiency

## Design Workflow

### Step 1: NN Training
1. Generate training data via QEC simulations
2. Train NN decoder offline (Python/PyTorch)
3. Quantize to INT8 weights
4. Validate logical error rate vs minimum-weight perfect matching (MWPM)

### Step 2: FPGA Implementation
1. Convert NN weights to FPGA-friendly format
2. Implement inference pipeline in HDL or HLS
3. Optimize for throughput (parallel syndrome processing)
4. Target deterministic latency < 200 ns

### Step 3: Integration
1. Connect FPGA to quantum control electronics
2. Implement syndrome capture interface
3. Add feedback correction path
4. Verify closed-loop timing budget

### Step 4: Mid-Circuit Feedback
For non-Clifford circuits (e.g., T-gate injection):
- Pauli-frame tracking alone is insufficient
- Real-time hardware feedback required
- Decoder must output active corrections, not just frame updates

## Critical Design Parameters

| Parameter | Target | Notes |
|-----------|--------|-------|
| Decoding latency | < 200 ns | Must fit within QEC cycle |
| Throughput | > 1 MHz | Keep pace with syndrome rate |
| Accuracy | ≥ MWPM | Match or exceed classical decoder |
| Power | < 10 W | Cryogenic-friendly for dilution fridge |
| Area | < 50k LUTs | Fit on mid-range FPGA |

## Activation Keywords
- FPGA quantum decoder
- real-time QEC
- surface code decoder
- neural network quantum error correction
- low-latency quantum control
- hardware QEC
- FPGA NN decoder
- quantum feedback control
- Pauli-frame correction
- 实时量子纠错
- FPGA量子解码器

## Related Concepts
- Surface codes (distance-3, distance-5, etc.)
- MWPM (Minimum Weight Perfect Matching)
- Union-Find decoder
- Quantum control electronics
- Cryogenic FPGA operation
- Fault-tolerant quantum computation (FTQC)
- Non-Clifford gate implementation

## References
- arXiv:2605.04892 — Real-time Surface-Code Error Correction Using an FPGA-based Neural-Network Decoder
