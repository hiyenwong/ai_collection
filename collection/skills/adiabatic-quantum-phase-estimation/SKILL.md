---
name: adiabatic-quantum-phase-estimation
description: "Adiabatic Quantum Phase Estimation methodology — adiabatic approach to QPE achieving Heisenberg-limited scaling with simpler circuit requirements"
---

# Adiabatic Quantum Phase Estimation

## Overview

arXiv: 2605.22770 introduces an **adiabatic approach to Quantum Phase Estimation (QPE)** that achieves the same Heisenberg-limited scaling as traditional QPE but with **simpler circuit requirements**. QPE is a fundamental algorithmic primitive for estimating eigenvalues of a Hamiltonian, and this adiabatic variant offers practical advantages for near-term quantum hardware.

**arXiv**: 2605.22770  
**Category**: quant-ph; cs.DS  
**Key Problem**: Traditional QPE requires deep circuits with controlled-unitary operations and inverse QFT, making it impractical for NISQ devices.

## Core Methodology

### 1. Adiabatic QPE Framework
- Maps the phase estimation problem to an **adiabatic evolution** process
- The system starts in a known ground state and slowly evolves to encode the eigenvalue
- The eigenvalue is extracted from the final state through measurement

### 2. Heisenberg-Limited Scaling
- Achieves **O(1/ε)** scaling in total evolution time for precision ε
- Matches the optimal Heisenberg limit of standard QPE
- No exponential overhead compared to classical alternatives

### 3. Simplified Circuit Requirements
- **No inverse QFT** required — eliminates a major source of circuit depth
- **No ancilla qubits** for phase register — reduces qubit overhead
- **No controlled-U^(2^k)** operations — avoids exponentially long gate sequences
- Only requires: Hamiltonian simulation + adiabatic evolution + measurement

### 4. Algorithm Steps
1. Prepare initial state |ψ⟩ with overlap with target eigenstate
2. Construct adiabatic Hamiltonian H(s) interpolating between initial and problem Hamiltonians
3. Evolve system adiabatically with schedule s(t) from t=0 to t=T
4. Measure final state to extract eigenvalue estimate
5. Repeat with different schedules for improved precision

## Key Insights

- **Trade-off**: Adiabatic QPE trades circuit depth for evolution time — better suited for hardware with long coherence but limited gate fidelity
- **Gap dependence**: Success depends on the minimum spectral gap of the adiabatic path
- **Schedule optimization**: Optimal annealing schedules can significantly reduce total runtime
- **Error robustness**: Less sensitive to gate errors than circuit-based QPE, but sensitive to decoherence

## Application Scenarios

Use this skill when:
- Implementing phase estimation on NISQ hardware with limited circuit depth
- Estimating molecular ground state energies (quantum chemistry)
- Solving linear systems via HHL algorithm (requires QPE subroutine)
- Comparing QPE variants for hardware-specific optimization
- Designing algorithms for quantum sensors and metrology

## Activation Keywords
adiabatic qpe, quantum phase estimation, adiabatic quantum computing, eigenvalue estimation, heisenberg limit, hamiltonian simulation, quantum algorithm, ground state energy

## Implementation Notes

### Adiabatic Schedule Design
- Linear schedule: H(s) = (1-s)H₀ + sH₁ (simplest, but not optimal)
- Optimal schedule: s'(t) ∝ 1/gap²(s(t)) — faster where gap is large
- Local adiabatic evolution: adapt schedule based on instantaneous gap

### Gap Estimation
- Minimum gap determines total runtime T ∝ 1/gap²
- For quantum chemistry: gap typically scales polynomially with system size
- Use variational methods to estimate gap before running adiabatic evolution

### Comparison with Standard QPE
| Aspect | Standard QPE | Adiabatic QPE |
|--------|-------------|---------------|
| Circuit depth | O(1/ε) controlled operations | O(1/ε) evolution time |
| Ancilla qubits | O(log(1/ε)) | 0 |
| Inverse QFT | Required | Not needed |
| Gate errors | Accumulate with depth | Less sensitive |
| Decoherence | Sensitive to T₁, T₂ | More sensitive to T₁ |
| Hardware fit | Fault-tolerant | NISQ-friendly |

## Related Work
- Standard Quantum Phase Estimation (Kitaev, 1995)
- Iterative Phase Estimation (reduces qubit count)
- Variational Quantum Eigensolver (VQE) — alternative for ground states
- Quantum Imaginary Time Evolution (QITE)
