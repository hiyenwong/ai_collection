---
name: physics-informed-qaoa-electromagnetics
description: "Physics-Informed QAOA methodology for electromagnetic optimization, embedding mutual coupling into QUBO formulations for Reconfigurable Intelligent Surfaces (RIS). Covers Ising interaction model selection, NISQ hardware feasibility tradeoffs, and sparse Hamiltonian design."
---

# Physics-Informed QAOA for Electromagnetics

## Description

Physics-Informed QAOA methodology for optimizing Reconfigurable Intelligent Surfaces (RIS) by embedding progressively realistic physics models (mutual coupling, distance-penalized interactions) into QUBO formulations. Analyzes the tradeoff between spatial pointing accuracy and quantum hardware feasibility on NISQ devices.

## Activation Keywords
- physics-informed QAOA
- QAOA electromagnetics
- reconfigurable intelligent surface
- RIS optimization quantum
- mutual coupling QUBO
- 物理感知QAOA
- 可重构智能表面量子优化

## Core Concepts

### Ising Interaction Models for QAOA-RIS

Four levels of physical fidelity mapped to Ising Hamiltonians:

| Model | J_ij Structure | Hardware Feasibility | Beamforming Accuracy |
|-------|---------------|---------------------|---------------------|
| Phase-only | Diagonal, sparse | High | Low |
| Near-neighbor | Local coupling | Medium | Medium |
| Distance-penalized | r^-α decay | Medium | High |
| Full dense | All-to-all | Low | Highest |

### Critical Tradeoff

Complete global coupling (dense J_ij) maximizes beamforming precision but introduces:
- Prohibitive qubit routing overhead on NISQ devices
- Convergence complications from dense Hamiltonians
- Circuit depth exceeding coherence times

Sparse, distance-penalized models remain the practical compromise.

## Usage Patterns

### Pattern 1: Physics-Informed QUBO Construction

1. Select physical fidelity level based on hardware constraints
2. Map element interactions to Ising coupling matrix J_ij
3. Encode element phase states as binary variables
4. Construct cost Hamiltonian H_C = Σ J_ij σ_i^z σ_j^z + Σ h_i σ_i^z
5. Choose mixer Hamiltonian H_M respecting physical constraints

### Pattern 2: NISQ Hardware Assessment

1. Count qubits needed: N_elements × bits_per_element
2. Analyze coupling graph density vs device topology
3. Estimate SWAP overhead for embedding
4. Compare circuit depth to coherence time
5. If infeasible: fall back to sparse model or classical solver

### Pattern 3: Progressive Physics Embedding

1. Start with idealized phase-only model
2. Add nearest-neighbor mutual coupling
3. Add distance-decay coupling
4. Validate each level against electromagnetic simulation
5. Identify the fidelity level where quantum advantage disappears

## Tools Used
- qiskit/pennylane: QAOA circuit construction and simulation
- numpy: Ising matrix construction, eigenvalue analysis
- scipy.sparse: Sparse coupling matrix operations
- classical solvers (CPLEX/Gurobi): baseline comparison

## Error Handling

### Dense Hamiltonian Convergence Failure
- Symptom: QAOA optimizer oscillates, doesn't converge
- Fix: Reduce coupling density, increase p (circuit depth), or use warm-start

### Hardware Embedding Failure
- Symptom: Cannot embed problem graph on device topology
- Fix: Use distance-penalized sparse model, or switch to classical solver

### Beamforming Accuracy Degradation
- Symptom: Sparse model produces poor beam patterns
- Fix: Increase p parameter, use counterdiabatic driving (CD-QAOA)

## Examples

### Example 1: 5×5 RIS Grid Optimization

Given a 5×5 RIS grid (25 elements, each 1-bit phase):
- Phase-only model: 25 qubits, diagonal J → trivial
- Near-neighbor model: ~80 coupling terms → feasible on 127-qubit Eagle
- Full dense model: ~300 coupling terms → requires extensive SWAP routing

Result: Distance-penalized model (top 50 strongest couplings) achieves 85% of full-model accuracy with 10x fewer routing operations.

## Resources

- arXiv:2605.06048 - Quantum Optimization for Electromagnetics: Physics-Informed QAOA for Reconfigurable Intelligent Surfaces
- QAOA foundational papers (Farhi et al.)
- RIS optimization literature

## Related Skills

- quantum-optimization-qaoa
- quantum-neural-architecture-search
- qbalance-quantum-workflow-optimization
- physics-guided-neural-networks
