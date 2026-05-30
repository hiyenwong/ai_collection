---
name: basis-adaptive-sparse-simulation
description: "Basis-Adaptive Sparse-State Simulation (BASS) methodology for classical simulation of quantum circuits. Updates each qubit's local representation basis during execution to maintain amplitude clustering under entanglement. Use when simulating quantum circuits classically with limited memory, analyzing circuit complexity, or studying how basis rotations affect state overlap and fidelity."
metadata:
  arxiv_id: "2605.27285"
  published: "2026-05-26"
  authors: "Ch Nihar Kartikeya, Anjana K, Bijita Sarma, Sangkha Borah"
  tags: [quantum, simulation, sparse-state, basis-adaptive, circuit-analysis]
---

# Basis-Adaptive Sparse-State Simulation (BASS)

## Description

Classical simulation of quantum circuits via adaptive basis rotation. Instead of fixing the computational basis throughout simulation, BASS rotates each qubit into the eigenbasis of its single-qubit reduced density matrix before truncation, keeping retained amplitudes clustered even under high entanglement.

## Core Methodology

### Problem
Fixed-basis sparse simulators keep the largest k computational-basis amplitudes. When entanglement or basis rotations spread weight across Hilbert space, fidelity drops rapidly.

### BASS Algorithm
1. **Before each truncation step**, compute each qubit's single-qubit reduced density matrix
2. **Rotate each qubit** into the eigenbasis of its reduced density matrix (natural-orbital idea from quantum chemistry)
3. **Truncate**: keep top-k amplitudes in the new basis (uniquely optimal for one-step truncation)
4. **Inverse rotation** if needed for measurement in computational basis

### Key Theoretical Results
- Top-k amplitude selection is **uniquely optimal** for one-step truncation in any fixed basis
- The one-body reduced-density-matrix eigenbasis is a **stationary product basis** for the inverse participation ratio (IPR)
- Residual bounded by local entanglement coherence

### Performance Indicator
The ratio `k/PR_Z` (sparse budget over computational participation ratio) indicates when adaptive bases provide advantage:
- High ratio → fixed basis sufficient
- Low ratio → adaptive basis provides significant improvement

### Benchmarks
- **Structured brickwork circuits**: substantially higher fidelity than fixed-basis at moderate wall-clock increase
- **Disordered Ising circuits**: ~1 order of magnitude improvement in state overlap at fixed budget

## Usage Patterns

### Pattern 1: Memory-Limited Quantum Circuit Simulation
When simulating large circuits with limited memory:
1. Implement fixed-basis sparse simulator as baseline
2. Compute PR_Z for circuit to estimate k/PR_Z ratio
3. If ratio is low, switch to BASS with adaptive basis rotation
4. Monitor fidelity vs computational budget tradeoff

### Pattern 2: Circuit Complexity Analysis
Use BASS behavior to understand circuit complexity:
1. Run BASS at fixed k budget across circuit instances
2. Track state overlap as function of circuit depth
3. Circuits where BASS degrades slowly have structure exploitable by adaptive bases
4. Circuits where BASS degrades rapidly approach Haar-random behavior

### Pattern 3: Benchmarking Quantum Advantage
Compare BASS performance to quantum hardware results:
1. Simulate circuit classically with BASS at maximum feasible k
2. Compare classical fidelity to quantum device results
3. Gap between classical and quantum fidelity indicates quantum advantage potential

## Error Handling

### High Entanglement Regime
When entanglement is near-maximal (e.g., deep random circuits), BASS degrades toward fixed-basis performance. In this regime, consider tensor network methods instead.

### Memory Bottleneck
Computing reduced density matrices for all qubits adds overhead. Only rotate qubits where local entanglement coherence exceeds threshold.

## Implementation Notes
- Complexity: O(k * n * d) per gate where n=qubits, d=circuit depth (moderate increase over O(k) fixed-basis)
- Best for structured circuits with moderate entanglement growth
- Wall-clock increase is moderate; memory savings can be substantial
- Qiskit/Cirq compatible — basis rotation is standard single-qubit gate

## References
- arXiv: https://arxiv.org/abs/2605.27285v1
- PDF: https://arxiv.org/pdf/2605.27285v1
- 40 pages, 8 figures, Journal article
