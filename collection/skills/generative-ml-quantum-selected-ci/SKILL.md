---
name: generative-ml-quantum-selected-ci
description: "Hybrid quantum-classical workflow for molecular simulations using LCNot-UCCSD ansatz and RBM generative subspace expansion, enabling NISQ-to-fault-tolerant bridging for protein-ligand systems."
category: quantum
---

# Generative-ML-Assisted Quantum Selected CI

## Description
Hybrid quantum-classical workflow combining LCNot-UCCSD ansatz with RBM generative subspace expansion for molecular simulations. First DMET-QSCI application to industry-relevant protein-ligand systems (Amantadine, SARS-CoV-2 main protease), using fraction of classical resources vs state-of-the-art.

## Activation Keywords
- quantum selected CI
- QSCI molecular simulation
- LCNot-UCCSD ansatz
- DMET quantum chemistry
- RBM subspace expansion
- protein-ligand quantum simulation
- NISQ molecular simulation
- quantum drug discovery
- quantum chemistry workflow
- QARP quantum simulation

## Core Concepts

### Problem: Molecular Electronic Structure
Protein-ligand binding energy calculation requires accurate electronic structure treatment — exponential scaling on classical hardware, too noisy for current quantum hardware.

### Solution: Hybrid QSCI Workflow
1. **LCNot-UCCSD Ansatz**: Linear Scaling CNOT UCCSD replaces O(N⁶) CCSD init with O(N⁴) MP2-amplitude init
2. **QSCI-RBM**: RBM replaces configuration recovery as compact generative subspace expansion
3. **DMET Integration**: Domain decomposition for large molecular systems
4. **Platform**: Fujitsu FX700 ideal state-vector simulator with QARP

### Key Results
- Evaluated on 8 molecules in STO-3G across 14 error levels (100 runs each)
- N₂ potential energy surface scans in cc-pVDZ
- Amantadine (C₁₀H₁₇N): 11 DMET fragments
- SARS-CoV-2 main protease + Carmofur (PDB: 7BUY): 10 fragments
- Fraction of classical resources vs Cleveland Clinic/RIKEN/IBM workflow

## Usage Patterns

### Pattern 1: QSCI with LCNot-UCCSD
For quantum chemistry on NISQ hardware:
1. Use QARP framework on state-vector simulator
2. Initialize with MP2 amplitudes (O(N⁴)) instead of CCSD (O(N⁶))
3. Apply LCNot-UCCSD ansatz for reduced gate count
4. Evaluate under controlled artificial noise levels

### Pattern 2: DMET-QSCI-RBM for Large Systems
For protein-ligand systems:
1. Fragment system using DMET
2. Apply QSCI to each fragment
3. Use RBM for generative subspace expansion
4. Aggregate results across fragments

## Error Handling

### Hardware Noise
- Tested across 14 controlled error levels
- RBM provides robustness to noise through generative modeling
- Validate with potential energy surface scans

### Resource Constraints
- LCNot-UCCSD reduces classical preprocessing cost
- RBM reduces quantum measurement requirements
- DMET enables parallel fragment processing

## Resources
- arXiv:2606.30551 - "Bridging the NISQ and Fault-Tolerant Regimes: Generative-ML-Assisted Quantum Selected CI for Molecular Simulations"
- Related: `quantum-chemistry`, `vqe-active-space-benchmarking`, `quantum-medical-diagnosis`
