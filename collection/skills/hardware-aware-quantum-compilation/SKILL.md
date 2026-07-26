---
name: hardware-aware-quantum-compilation
description: "Hardware-aware quantum compilation with data-driven lightweight error detection for early fault-tolerant NISQ systems. Use when: (1) optimizing qubit mapping and SWAP insertion for NISQ devices, (2) integrating error detection into compilation pipelines, (3) balancing detection overhead against success probability under latency constraints, (4) co-designing compilation and quantum error detection (QED) for early fault-tolerant quantum processors. Activation: quantum compilation, qubit mapping, error detection, NISQ, hardware-aware, fault-tolerant, QED, syndrome scheduling"
metadata:
  arxiv_id: "2606.07666"
  published: "2026-06-04"
  authors: "Sumit Chongder"
  tags: ["quantum-compilation", "error-detection", "NISQ", "hardware-aware", "qubit-mapping", "fault-tolerance"]
---

# Hardware-Aware Quantum Compilation with Error Detection

## Core Methodology

Joint co-design of quantum compilation and lightweight error detection (QED) for NISQ processors entering early fault-tolerance regimes. Addresses the gap between full QEC (prohibitively expensive) and no protection (low success rates).

### Key Innovations

1. **Noise-weighted cost function**: Combines qubit mapping quality, SWAP overhead, and error-detection placement into a unified objective
2. **Learned multi-objective scheduler**: Uses ML to optimize syndrome-schedule placement
3. **Integrated pipeline**: Jointly optimizes qubit mapping, SWAP insertion, and QED placement rather than treating them separately

### Results (arXiv:2606.07666)

- Up to **68% improvement** in algorithmic success probability over SABRE baseline
- Tested on 6-20 qubit circuits (depths 10-160) across VQE, phase-estimation, and Grover benchmarks
- Three noise profiles, GPU-accelerated density-matrix simulation (cuQuantum SDK)
- 8-qubit VQE with post-selection: 95% CI [60%, 76%] improvement

## Agent Workflow

### Step 1: Identify Target Hardware Profile

Characterize the target quantum processor:
- Qubit connectivity topology (linear, grid, heavy-hex)
- Noise profile (T1, T2, gate fidelities, readout errors)
- Latency constraints for error detection cycles

### Step 2: Build Noise-Weighted Cost Model

The cost function combines:
```
C_total = w_map * C_mapping + w_swap * C_swap + w_qed * C_qed
```
Where:
- `C_mapping`: Quality of initial qubit placement based on gate frequency and qubit quality
- `C_swap`: Number and placement of SWAP gates weighted by their error rates
- `C_qed`: Overhead of syndrome measurement placement vs. protection benefit

### Step 3: Optimize Compilation Pipeline

1. **Qubit mapping**: Assign logical qubits to physical qubits minimizing expected error
2. **SWAP insertion**: Minimize routing overhead using noise-aware routing algorithms
3. **Syndrome scheduling**: Place error-detection checkpoints at optimal circuit points

### Step 4: Apply Learned Scheduler

Use the multi-objective scheduler to balance:
- Detection coverage (probability of catching errors)
- Circuit overhead (additional gates from QED)
- Latency constraints (time-critical algorithms)

## Implementation Patterns

### Pattern 1: SABRE Extension with QED

Extend SABRE-like routing by adding QED placement as a third optimization dimension alongside routing and scheduling.

### Pattern 2: Noise-Aware Initial Mapping

Before routing, assign logical qubits to the highest-fidelity physical qubits based on:
- Measured gate fidelities from calibration data
- Expected circuit structure (frequently interacting logical qubits on well-connected physical qubits)

### Pattern 3: Adaptive QED Density

For early fault-tolerant systems:
- Use lightweight error detection (post-selection) instead of full correction
- Place syndrome measurements adaptively: more frequently in high-error regions, less in low-error regions
- Trade off detection coverage against circuit depth increase

## Error Handling

### Insufficient Qubit Resources
When QED overhead exceeds available qubit budget:
- Reduce QED frequency
- Use selective QED on critical circuit paths only
- Consider circuit cutting as alternative

### Hardware Calibration Drift
QED effectiveness depends on accurate noise models:
- Use recent calibration data
- Implement adaptive noise estimation during execution
- Fall back to conservative QED placement when noise data is stale

## Pitfalls

- **Don't treat compilation and QED separately**: Joint optimization is essential — separate optimization leaves significant performance on the table
- **Post-selection is not error correction**: QED with post-selection improves success rates but cannot recover from detected errors
- **Benchmark-specific optimization**: QED placement strategies that work for VQE may not transfer to phase estimation or Grover's algorithm
