---
name: tianyan-quantum-cloud-services
description: "Quantum cloud infrastructure and advantage verification methodology from arXiv:2512.10504 (Tianyan-287). Covers cloud-accessible quantum advantage demonstration, SDK-based quantum hardware access, random circuit sampling benchmarks, and classical vs quantum performance comparison."
category: quantum-computing
tags:
  - quantum-computing
  - cloud-services
  - quantum-advantage
  - superconducting-qubits
  - quantum-cloud
source: "arXiv:2512.10504"
---

# Tianyan Quantum Cloud Services with Quantum Advantage

## Overview

Methodology from the Tianyan paper (arXiv:2512.10504, Dec 2025) demonstrating quantum advantage via cloud-accessible superconducting quantum processors.

**Core Achievement**: Tianyan-287 platform with 105 qubits achieved quantum advantage on random circuit sampling (RCS):
- 74-qubit × 24-cycle: 1M samples in 18.4 minutes
- Classical equivalent: ~16,000 years on state-of-the-art supercomputers

## Key Specifications

### Hardware
| Parameter | Value |
|-----------|-------|
| Total Qubits | 105 |
| Single-qubit gate fidelity | 99.90% |
| Two-qubit gate fidelity | 99.56% |
| Readout fidelity | 98.7% |
| Architecture | Zuchongzhi 3.0-like superconducting |

### Benchmark Task
- Random circuit sampling (RCS)
- 74 active qubits, 24 depth cycles
- 1,000,000 samples in 18.4 minutes
- Quantum advantage factor: ~10⁸ over classical

### SDK: Cqlib
- Open-source SDK for extended quantum circuits
- Operates at level of operators and primitives
- Cloud API for remote quantum hardware access

## Methodology

### Quantum Advantage Verification Pattern
1. **Define benchmark task** (RCS with specific qubit count and depth)
2. **Measure quantum execution time** on actual hardware
3. **Estimate classical runtime** using best-known classical algorithms + supercomputer specs
4. **Calculate advantage ratio** = classical_time / quantum_time
5. **Publish reproducibility details** (SDK, parameters, calibration data)

### Cloud Architecture Pattern
```
User → Cqlib SDK → Cloud API → Quantum Processor (Tianyan-287)
                                  ↓
                          Extended quantum circuits
                          Operators & primitives
                          Calibration data
```

### Calibration-Aware Execution
- Maintain calibration data for circuit optimization
- Adaptive circuit compilation based on qubit connectivity
- Error mitigation based on real-time fidelity data

## Implementation Patterns

### Pattern 1: RCS Benchmark Protocol
```python
# Conceptual workflow
def verify_quantum_advantage(
    qubit_count: int,      # e.g., 74
    circuit_depth: int,    # e.g., 24
    num_samples: int,      # e.g., 1_000_000
    quantum_platform,
    classical_baseline
):
    # 1. Generate random circuits
    circuits = generate_random_circuits(qubit_count, circuit_depth, num_samples)
    
    # 2. Execute on quantum hardware
    quantum_results, quantum_time = quantum_platform.sample(circuits)
    
    # 3. Estimate classical runtime
    classical_time = classical_baseline.estimate(circuits)
    
    # 4. Verify advantage
    advantage_ratio = classical_time / quantum_time
    return advantage_ratio > 1.0  # Quantum advantage achieved
```

### Pattern 2: SDK Integration
```python
# Cqlib-style API pattern
from cqlib import QuantumCloud, Circuit, Operator

# Connect to quantum cloud
cloud = QuantumCloud(endpoint="tianyan.cloud")
qpu = cloud.get_processor("tianyan-287")

# Build extended circuit
circuit = Circuit(num_qubits=74)
circuit.apply_random_gates(depth=24)

# Execute
results = qpu.sample(circuit, shots=1_000_000)
calibration = qpu.get_calibration_data()
```

### Pattern 3: Fidelity-Based Error Budgeting
```python
def estimate_circuit_fidelity(gate_sequence, calibration):
    total_fidelity = 1.0
    for gate in gate_sequence:
        if gate.type == "single":
            total_fidelity *= calibration.single_qubit_fidelity
        elif gate.type == "two":
            total_fidelity *= calibration.two_qubit_fidelity
    total_fidelity *= calibration.readout_fidelity ** num_qubits
    return total_fidelity
```

## When to Use

- Evaluating quantum cloud platforms for practical workloads
- Benchmarking quantum advantage claims
- Building hybrid quantum-classical cloud applications
- Accessing NISQ-era superconducting processors remotely
- Comparing quantum hardware specifications

## Key References

- arXiv: 2512.10504v2 - "Tianyan: Cloud services with quantum advantage"
- Cqlib: Open-source SDK for quantum cloud interaction
- Zuchongzhi processor family: Google Sycamore-era Chinese superconducting QPUs

## Activation Keywords

- quantum cloud, quantum advantage, tianyan, RCS benchmark, Cqlib, 
- cloud quantum computing, superconducting quantum processor,
- random circuit sampling, quantum hardware access, 量子云
