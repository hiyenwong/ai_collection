---
name: fpga-quantum-error-decoder
description: >
  FPGA-based real-time quantum error correction decoding architecture. Combines
  hardware-integrated NN decoders on FPGA with superconducting quantum processors
  for low-latency closed-loop QEC. Use when: (1) Designing real-time QEC control
  systems, (2) Implementing FPGA-based syndrome decoders, (3) Building low-latency
  feedback loops for fault-tolerant quantum computing, (4) Analyzing closed-loop
  latency budgets for QEC cycles, (5) Implementing mid-circuit Pauli-frame
  corrections in non-Clifford logical circuits. Trigger: FPGA QEC decoder,
  real-time quantum error correction, low-latency syndrome decoding, hardware
  integrated QEC, surface code FPGA, closed-loop quantum feedback.
---

# FPGA-Based Real-Time Quantum Error Decoder

Hardware-integrated control architecture for real-time surface-code QEC using
FPGA-based neural network decoders, achieving deterministic closed-loop latency
of 550 ns (124 ns NN decoding) within a 1.25 μs QEC cycle.

## Core Architecture

```
Quantum Processor → Syndrome Measurement → FPGA Controller → NN Decoder → Feedback Correction
     (superconducting)    (repeated)      (Xilinx/Intel)   (124 ns)    (within 1.25 μs)
```

### Key Metrics (from arXiv:2605.04892)

| Component | Latency | Description |
|-----------|---------|-------------|
| NN Decoding | 124 ns | FPGA-based neural network inference |
| Total Closed-Loop | 550 ns | End-to-end syndrome to correction |
| QEC Cycle | 1.25 μs | Full error correction cycle period |
| Code Distance | d=3 | Surface code demonstration |

### Hardware Design Principles

1. **Deterministic Latency**: Fixed-latency FPGA pipelines avoid timing jitter
2. **On-Chip NN Inference**: Neural network weights stored in FPGA BRAM/LUTs
3. **Closed-Loop Feedback**: Decoder output directly drives quantum control pulses
4. **Mid-Circuit Correction**: Supports Pauli-frame updates during logical operations

## Implementation Workflow

### Step 1: Neural Network Quantization for FPGA

```python
# Quantize trained decoder to FPGA-friendly precision
import torch

# Original: float32 trained model
model = load_trained_decoder()  # CNN/MLP for syndrome decoding

# Quantize to INT8 for FPGA deployment
model_int8 = torch.quantization.quantize_dynamic(
    model, {torch.nn.Linear, torch.nn.Conv2d}, dtype=torch.qint8
)

# Export weights for FPGA synthesis
torch.onnx.export(model_int8, dummy_syndrome, "decoder_int8.onnx")
```

### Step 2: FPGA Pipeline Design

```
Input Layer (syndrome bits) → [FPGA registers]
    ↓
Convolution Layer → [DSP slices + BRAM for weights]
    ↓
Activation (ReLU) → [LUT-based lookup]
    ↓
Output Layer (correction bits) → [Pipeline registers]
    ↓
Control Signal → Quantum processor feedback
```

**Latency Budget Breakdown:**
- Syndrome readout: ~100 ns
- NN inference (INT8): 124 ns
- Correction computation: ~50 ns
- Control signal routing: ~100 ns
- **Total: 550 ns**

### Step 3: QEC Cycle Integration

```python
# Pseudocode for QEC cycle management
def qec_cycle(fpga_controller):
    # 1. Trigger syndrome measurement
    syndromes = measure_stabilizers()  # X and Z stabilizers
    
    # 2. Send to FPGA decoder (550 ns round-trip)
    corrections = fpga_controller.decode(syndromes)
    
    # 3. Apply feedback within QEC cycle
    if corrections.needs_feedback:
        apply_physical_correction(corrections)
    else:
        update_pauli_frame(corrections)
    
    # Must complete within 1.25 μs to prevent error accumulation
    assert elapsed_time() < 1250  # ns
```

## Critical Design Considerations

### Latency vs Accuracy Tradeoff

| Decoder Latency | Logical Error Rate | Use Case |
|-----------------|-------------------|----------|
| < 200 ns | ~0.1% degradation | Real-time feedback |
| < 1 μs | ~0.01% degradation | Near-real-time |
| > 10 μs | Baseline (offline) | Post-processing |

### Scaling to Larger Distances

For distance-5 and distance-7 surface codes:
- Syndrome data size grows as d²
- NN model size grows proportionally
- FPGA resource utilization: LUTs, DSPs, BRAM
- **Pipeline parallelism** is key: decode multiple syndrome patches concurrently

### Mid-Circuit vs Pauli-Frame Correction

- **Pauli-frame updating**: Software-only, zero latency, works for Clifford circuits
- **Mid-circuit feedback**: Required for non-Clifford gates (T-gates, magic state distillation)
- FPGA decoder enables mid-circuit correction when Pauli-frame alone is insufficient

## Error Model Adaptation

The FPGA-based NN decoder adapts to varying error conditions:

```
Training: Offline NN training with diverse noise models
Deployment: FPGA inference adapts to real-time error statistics
Adaptation: Periodic model updates based on observed syndrome patterns
```

### Robustness Features

1. **Error condition variation**: Maintains performance across different physical error rates
2. **Calibration drift**: Retraining triggers when logical error rate exceeds threshold
3. **Crosstalk compensation**: NN naturally learns spatial error correlations

## Comparison with Traditional Decoders

| Feature | MWPM | BP | FPGA-NN Decoder |
|---------|------|-----|-----------------|
| Latency | ms-scale | μs-scale | 124 ns |
| Hardware | CPU/GPU | CPU/FPGA | FPGA (dedicated) |
| Adaptability | Fixed model | Iterative | Learned patterns |
| Circuit-level noise | Requires modification | Limited | Native support |
| Real-time feedback | No | Marginal | Yes |

## Resources

- **arXiv:2605.04892**: "Real-time Surface-Code Error Correction Using an FPGA-based Neural-Network Decoder"
- **arXiv:2605.04459**: "Triage: Adaptive Parallel Window Decoding Scheduler"
- Related skill: `neural-decoder-quantum-error-correction` (algorithm-level)
- Related skill: `quantum-fault-tolerance-verification` (verification methods)
