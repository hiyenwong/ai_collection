---
name: generative-ml-quantum-selected-ci
category: ai_collection
description: Generative-ML-assisted Quantum Selected Configuration Interaction (QSCI) for molecular simulations. LCNot-UCCSD ansatz with O(N⁴) MP2 initialization, RBM-based subspace expansion, and DMET-QSCI for protein-ligand systems.
version: "1.0"
created: "2026-07-01"
updated: "2026-07-01"
trigger_words: ["qsci", "lcnot-uccsd", "quantum selected ci", "dmet-qsci", "rbm subspace", "quantum molecular simulation", "protein-ligand binding", "nisq fault-tolerant"]
arxiv: "2606.30551"
---

# Generative ML Quantum Selected CI

## Background

Calculating binding energies for protein-ligand molecular systems requires accurate electronic structure treatment, which scales exponentially on classical hardware. This methodology bridges NISQ and fault-tolerant regimes using Generative-ML-Assisted Quantum Selected Configuration Interaction (QSCI).

## Core Innovations

### 1. LCNot-UCCSD Ansatz in QSCI

Replaces O(N⁶) CCSD parameter initialization (LUCJ approach) with O(N⁴) MP2-amplitude initialization:

```
LUCJ initialization:  O(N⁶) CCSD amplitudes
LCNot-UCCSD init:     O(N⁴) MP2 amplitudes
```

This provides a significant computational advantage for large molecular systems.

### 2. QSCI-RBM: RBM-based Subspace Expansion

Replaces the configuration recovery of the SQD framework with a **Restricted Boltzmann Machine (RBM)** acting as a compact generative subspace expansion model:

```
SQD framework:      Configuration recovery (classical sampling)
QSCI-RBM:           RBM as generative model for subspace expansion
```

## Workflow Architecture

```
MP2 Amplitudes (O(N⁴))
    ↓
LCNot-UCCSD Ansatz Initialization
    ↓
QSCI Quantum Circuit Execution
    ↓
RBM Generative Subspace Expansion
    ↓
DMET Fragmentation (for large systems)
    ↓
Binding Energy Calculation
```

## Key Applications

### Industry-Relevant Protein-Ligand Systems

1. **Amantadine (C₁₀H₁₇N)**: FDA-approved antiviral, 11 DMET fragments
2. **SARS-CoV-2 Main Protease + Carmofur (PDB: 7BUY, C₁₅H₂₈N₄O₅S)**: 10 DMET fragments

### Evaluation Framework

- **8 molecules** in STO-3G basis set
- **14 controlled artificial error levels**
- **100 independent runs** per configuration
- **Potential energy surface scans** of N₂ in cc-pVDZ for validation

## Resource Efficiency

This approach uses a **fraction of the classical computing resources** required by state-of-the-art work from Cleveland Clinic, RIKEN, and IBM Quantum, enabling more efficient drug discovery simulations.

## Implementation Patterns

### Pattern 1: LCNot-UCCSD Initialization

```python
# O(N⁴) MP2 initialization vs O(N⁶) CCSD
mp2_amplitudes = compute_mp2(molecule)  # O(N⁴)
uccsd_params = initialize_from_mp2(mp2_amplitudes)  # Linear scaling
# vs
# ccsd_amplitudes = compute_ccsd(molecule)  # O(N⁶) - much more expensive
```

### Pattern 2: RBM Subspace Expansion

```python
# RBM as compact generative model
rbm = train_rbm_on_configurations(measured_configs)
expanded_configs = rbm.sample(num_samples)
# Provides more efficient subspace coverage than classical SQD sampling
```

### Pattern 3: DMET-QSCI Integration

```python
# Divide-and-conquer for large protein-ligand systems
fragments = dmet_fragment(protein_ligand_complex)
for fragment in fragments:
    qsci_result = run_qsci_lcnott_uccsd(fragment)
    energies.append(qsci_result)
total_energy = combine_fragment_energies(energies)
```

## Verification Steps

1. Validate LCNot-UCCSD vs LUCJ on small molecules
2. Compare QSCI-RBM vs SQD configuration recovery quality
3. Test error resilience across 14 error levels
4. Validate PES scans against reference calculations
5. Benchmark resource usage against Cleveland Clinic/RIKEN/IBM approaches

## Related Skills

- `quantum-chemistry` - Quantum chemistry computational patterns
- `vqe-active-space-benchmarking` - Active space selection benchmarks
- `quantum-medical-diagnosis` - Quantum methods for medical applications

## References

- arXiv:2606.30551 - "Bridging the NISQ and Fault-Tolerant Regimes: Generative-ML-Assisted Quantum Selected CI for Molecular Simulations"
- LCNot-UCCSD: Linear Scaling CNOT UCCSD ansatz
- DMET: Density Matrix Embedding Theory
- QSCI: Quantum Selected Configuration Interaction
