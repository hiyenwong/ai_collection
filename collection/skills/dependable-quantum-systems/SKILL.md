---
name: dependable-quantum-systems
description: >
  Dependability engineering for hybrid quantum-classical computing systems.
  Covers reliability, resiliency, security, and reproducibility patterns
  for quantum hardware integration with classical HPC infrastructure.
  Includes fault-tolerance verification, error mitigation strategies,
  and systems-level security for quantum computing platforms.
  Use when: (1) Building reliable quantum-classical hybrid systems,
  (2) Designing fault-tolerant quantum architectures, (3) Implementing
  security for quantum computing platforms, (4) Ensuring reproducibility
  of quantum experiments, (5) Evaluating dependability of quantum systems.
  Keywords: dependable quantum, quantum reliability, quantum resiliency,
  quantum security, quantum reproducibility, quantum fault tolerance,
  QHPC dependability.
---

# Dependable Quantum Systems Engineering

## Dependability Dimensions for Quantum Systems

### 1. Reliability

| Aspect | Classical HPC | Quantum HPC | Bridge Strategy |
|--------|--------------|-------------|-----------------|
| Component failures | Graceful degradation | Decoherence, gate errors | Error correction + mitigation |
| Mean time between failures | Hours to days | Microseconds to seconds | Logical qubits extend MTBF |
| Failure detection | Checksums, parity | Syndrome measurement | Real-time syndrome decoding |

### 2. Resiliency

Recovery patterns:
- **Checkpoint/restore**: Not applicable for quantum state → use algorithmic resiliency
- **Redundancy**: Physical qubit redundancy → logical qubits via QEC
- **Fallback**: Degraded operation with error mitigation when full QEC unavailable
- **Adaptive control**: Real-time parameter adjustment based on hardware calibration

### 3. Security

Quantum-specific security concerns:
- **Circuit protection**: Prevent intellectual property theft of quantum algorithms
- **Result integrity**: Verify quantum computation results (classical verification of quantum)
- **Access control**: Multi-tenant quantum hardware isolation
- **Supply chain**: Verify quantum hardware and control software integrity

### 4. Reproducibility

Challenges unique to quantum:
- **Hardware drift**: Calibration changes between runs → track calibration metadata
- **Non-determinism**: Inherent quantum randomness → statistical analysis over many shots
- **Backend variability**: Different hardware gives different results → benchmark suite
- **Noise variation**: Time-dependent noise → noise-aware compilation

## Fault-Tolerance Verification

Automated verification workflow:
```
1. Formalize fault model (error rates, correlated errors)
2. Symbolic execution of quantum circuit with fault injection
3. Verify fault-tolerance properties hold under all fault scenarios
4. Generate counterexamples for failing cases
5. Iterate on circuit design until verification passes
```

Tools and approaches:
- Quantum symbolic execution for automatic verification
- Detector error models for circuit-level analysis
- Syndrome extraction circuit robustness testing

## Error Mitigation vs. Error Correction Trade-off

| Factor | Error Mitigation | Error Correction |
|--------|-----------------|------------------|
| Overhead | Low (10-100x) | High (1000-10000x) |
| Scalability | Limited by noise | Theoretically unlimited |
| Implementation | Software-only | Requires hardware support |
| Accuracy | Approximate | Exact (below threshold) |
| Best for | NISQ, early FTQC | Full FTQC |

## KG References (kg.db entity IDs)

- [410] Dependable classical-quantum computing systems engineering
- [411] Verifying Fault-Tolerance of Quantum Error Correction Codes
- [416] A fault-tolerant neutral-atom architecture
- [417] Error Mitigation and Circuit Division for Early FTQC

## Related Existing Skills

- `quantum-fault-tolerance-verification` - Fault tolerance verification methods
- `quantum-error-correction-methods` - QEC approaches
- `quantum-systems-engineering` - General quantum systems patterns
- `quantum-reliability-assessment` - Reliability evaluation framework
- `modern-systems-engineering-patterns` - Classical systems engineering patterns
