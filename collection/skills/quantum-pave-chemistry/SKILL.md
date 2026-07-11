---
name: quantum-pave-chemistry
version: v1.0.0
last_updated: 2026-05-30
description: "QuantumPave — hybrid quantum-classical workflow for computing additive binding energies using quantum-centric supercomputing. Demonstrates practical quantum chemistry application on real quantum processors by sampling dominant electronic configurations on a QPU and performing classical diagonalization on HPC resources."
---

# QuantumPave: Quantum Chemistry on Quantum Processors

## Description

QuantumPave is a hybrid quantum-classical workflow for computing additive binding energies in materials using quantum-centric supercomputing. The approach samples dominant electronic configurations on a quantum processor and leverages classical HPC resources for diagonalization, providing a practical route to correlated electronic-structure calculations on NISQ devices.

**arXiv**: 2605.27640
**Title**: Additive binding energies in asphalt on a quantum processor via quantum-selected configuration interaction (QSCI)
**Categories**: quant-ph, cond-mat

## Core Methodology

### Quantum-Selected Configuration Interaction (QSCI)

QSCI is a hybrid algorithm that separates the exponential complexity of electronic structure into two parts:

1. **Quantum Sampling** — The quantum processor samples the dominant electronic configurations from a correlated wavefunction
2. **Classical Diagonalization** — Classical HPC resources diagonalize the Hamiltonian in the sampled subspace

This separation enables practical quantum chemistry calculations on noisy intermediate-scale quantum (NISQ) devices by offloading the most computationally intensive part (diagonalization) to classical systems.

## Workflow

### Step 1: Problem Formulation
- Define the molecular/material system and basis set
- Map the electronic structure problem to a qubit Hamiltonian using standard transformations (Jordan-Wigner, Bravyi-Kitaev)
- Determine the active space for configuration interaction

### Step 2: Quantum State Preparation
- Prepare an initial state on the quantum processor
- Apply variational or Trotterized evolution to explore configuration space
- Use error mitigation techniques to improve state fidelity on NISQ hardware

### Step 3: Configuration Sampling
- Measure the quantum state to sample dominant electronic configurations
- Each measurement collapses to a specific configuration (Slater determinant)
- Accumulate statistics over many shots to identify high-weight configurations

### Step 4: Classical Diagonalization
- Construct the Hamiltonian matrix in the subspace of sampled configurations
- Perform exact diagonalization on classical HPC resources
- Extract ground state energy and excited state properties

### Step 5: Binding Energy Computation
- Compute additive binding energies from the correlated ground state
- Compare with classical benchmarks to assess quantum advantage
- Iterate with refined active spaces or improved state preparation

## Key Advantages

### NISQ-Compatible
- Shallow circuit depth compared to full quantum phase estimation
- Error mitigation sufficient for useful results on current hardware
- No need for fault-tolerant quantum computing

### Hybrid Efficiency
- Quantum part scales polynomially with system size
- Classical part leverages existing HPC infrastructure
- Communication overhead minimized between quantum and classical stages

### Practical Applications
- **Materials science**: Binding energy calculations for complex materials
- **Catalysis**: Reaction energetics for industrial catalysts
- **Energy materials**: Battery materials, fuel cells, photovoltaics
- **Asphalt chemistry**: Additive binding energies for pavement materials (demonstrated application)

## Error Mitigation

- **Readout error correction**: Calibrate measurement errors using known states
- **Zero-noise extrapolation**: Run circuits at different noise levels and extrapolate
- **Symmetry verification**: Enforce particle number and spin conservation
- **Configuration filtering**: Remove low-weight configurations from the sampled subspace

## Integration with Quantum-Centric Supercomputing

QuantumPave exemplifies the quantum-centric supercomputing paradigm:
- **Quantum processor**: Samples configurations (exponential space exploration)
- **Classical HPC**: Diagonalization and post-processing (polynomial scaling)
- **Tight coupling**: Iterative refinement between quantum and classical stages

## Activation Keywords
- quantum chemistry
- binding energy calculation
- quantum configuration interaction
- QSCI algorithm
- quantum-centric supercomputing
- materials science quantum
- electronic structure quantum
- quantum processor chemistry
- 量子化学
- 结合能计算

## Resources
- Paper: https://arxiv.org/abs/2605.27640
- Related: quantum-neural-architecture, quantum-error-correction-methods, quantum-chemistry
