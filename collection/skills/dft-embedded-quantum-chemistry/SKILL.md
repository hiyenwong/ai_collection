---
name: dft-embedded-quantum-chemistry
description: "DFT-embedded quantum-selected configuration interaction methodology for accurate large-scale electronic structure calculations on quantum computers. Bridges quantum active space treatment with classical wave-function methods using Manby projection technique. Achieved ~1 kcal/mol accuracy on 144-qubit hardware."
category: quantum-chemistry
---

## Context

This skill extracts reusable methodology from arXiv:2606.06015 (Do, Yoshida, Shiota, Mizukami — "Quantum computing for accurate large-scale electronic-structure calculations: DFT-embedded, post-processed quantum-selected configuration interaction"). Demonstrates practical quantum advantage pathway for quantum chemistry.

## Core Methodology

### 1. Multilevel Embedding Framework

- Three-tier hierarchy: DFT (environment) → classical wave-function (surrounding region) → quantum algorithm (active space)
- **Tier 1**: Low-cost DFT description of the full system environment
- **Tier 2**: High-level wave-function method (coupled cluster or multireference perturbation theory) for surrounding region correlation
- **Tier 3**: Quantum algorithm for strongly correlated active space

### 2. Quantum-Selected Configuration Interaction (QSCI)

- Sampling-based quantum algorithm bridges quantum and classical treatments
- Quantum computer generates important configurations via measurement
- Classical post-processing selects and diagonalizes in the important subspace
- More resource-efficient than full VQE for large active spaces

### 3. Manby's Projection Technique

- Embeds quantum-classical hybrid calculation in DFT environment
- Projects active space orbitals onto the DFT density
- Ensures consistent treatment of electron density across all tiers
- Avoids double-counting of correlation energy

### 4. Active Space Selection

- Identify strongly correlated orbitals via chemical intuition or automated methods
- Quantum computer handles the exponential scaling within active space
- Classical methods handle dynamic correlation outside active space

### 5. Resource Optimization

- Uses only subset of qubits available on hardware
- Demonstrated on 144-qubit superconducting quantum computer (University of Osaka)
- Bond dissociation energies, adsorption energies, reaction barriers all computed

## Implementation Steps

1. **Define system**: Identify molecule/material and chemical property of interest
2. **DFT preprocessing**: Run DFT calculation on full system to get orbitals and density
3. **Active space selection**: Choose strongly correlated orbitals for quantum treatment
4. **Manby projection**: Project active space onto DFT environment
5. **QSCI on quantum hardware**: Run quantum-selected CI to get active space wavefunction
6. **Classical post-processing**: Apply coupled cluster or MRPT to surrounding region
7. **Energy assembly**: Combine all tiers with proper double-counting correction
8. **Validation**: Compare against classical benchmarks (~1 kcal/mol target)

## Pitfalls

- **Active space size**: QSCI scales exponentially with active space size. Keep active space within qubit limits.
- **DFT functional choice**: Different DFT functionals give different environments — benchmark against known results.
- **Manby projection errors**: Projection can introduce artifacts if active space and environment orbitals overlap significantly.
- **Hardware noise**: On NISQ hardware, QSCI measurements are noisy. Use error mitigation techniques.
- **Double counting**: Careful energy accounting needed to avoid counting correlation energy twice across tiers.

## Verification

- Reproduce Menshutkin S_N2 reaction barrier in carbon nanotube with ~1 kcal/mol accuracy
- Verify bond dissociation energies for organic, metal-organic, and metallic systems
- Check that QSCI configurations span the important subspace adequately
- Compare with classical CCSD(T) or FCI results where available

## Activation

DFT embedding, quantum chemistry, quantum-selected configuration interaction, QSCI, Manby projection, active space, electronic structure, bond dissociation, Menshutkin reaction, 2606.06015
