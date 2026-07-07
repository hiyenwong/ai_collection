---
name: vqe-active-space-benchmarking
description: "Systematic benchmarking methodology for evaluating active space selection strategies in VQE pipelines for quantum drug discovery. Use when benchmarking VQE ansatz choices, designing quantum chemistry validation workflows, or evaluating active space-driven molecular simulation on NISQ hardware. Covers UCCSD, HEA ansatz evaluation, chemically-motivated active space criteria, and QPU execution benchmarking for drug-like molecules (lovastatin, oseltamivir, morphine). Activation: vqe active space, quantum drug discovery benchmark, active space selection vqe, 活性空间基准, VQE基准测试, quantum chemistry benchmark."
metadata:
  arxiv_id: "2512.18203"
  published: "2025-12-20"
  authors: "Zhi Yin, Xiaoran Li, Zhupeng Han, et al."
  tags: [quantum, vqe, drug-discovery, active-space, benchmarking, uccsd]
---

# VQE Active Space Selection Benchmarking

## Description

First systematic benchmark for active space selection in VQE-driven quantum drug discovery. Evaluates how different active space choices impact the VQE pipeline across chemistry metrics (accuracy vs classical benchmarks) and architecture-centric metrics (circuit depth, parameter count, QPU execution fidelity).

## Activation Keywords
- vqe active space benchmark
- quantum drug discovery active space
- active space selection VQE
- VQE pipeline benchmarking
- 活性空间基准测试
- quantum chemistry validation
- UCCSD benchmark
- HEA ansatz evaluation
- drug molecule VQE

## Core Methodology

### Benchmark Design Principles
1. **Chemically-motivated active spaces**: Use domain knowledge to select active orbitals, not random subsets
2. **Representative molecules**: Test on drug-like molecules (lovastatin, oseltamivir, morphine) covering diverse chemical spaces
3. **Dual evaluation**: Chemistry metrics (energy accuracy) + architecture metrics (circuit complexity)
4. **Multi-ansatz comparison**: UCCSD vs HEA under identical active space conditions
5. **Simulation + QPU**: Validate both simulated and hardware execution results

### Active Space Selection Criteria
- **Chemical intuition**: HOMO-LUMO gap, orbital occupancy, correlation strength
- **Quantum information theory**: Orbital entanglement (single-orbital entropy, mutual information)
- **Molecule suitability**: Classify which molecules benefit most from quantum computing based on active space properties

### VQE Pipeline Components
| Component | Options | Evaluation |
|-----------|---------|------------|
| Ansatz | UCCSD, HEA | Energy accuracy, circuit depth, trainability |
| Active Space | Chemical vs. automated | Convergence speed, final energy error |
| Optimizer | SPSA, L-BFGS, COBYLA | Iterations to convergence, noise resilience |
| Hardware | Simulator, QPU | Noise impact, shot requirements |

### Evaluation Metrics
1. **Chemistry**: Energy error vs FCI/CCSD(T), ground state fidelity
2. **Architecture**: Circuit depth, gate count, parameter count
3. **Practicality**: Wall-clock time, shot budget, convergence reliability
4. **Scalability**: How metrics scale with active space size

## Implementation Steps

### Step 1: Define Benchmark Molecules
Select representative drug-like molecules covering:
- Small molecules (morphine, ~40 atoms)
- Medium molecules (oseltamivir, ~19 non-H atoms)
- Complex molecules (lovastatin, ~44 non-H atoms)

### Step 2: Generate Active Spaces
For each molecule:
- Compute Hartree-Fock reference
- Select active spaces using chemical intuition (e.g., pi-system, lone pairs)
- Compute quantum information metrics (entanglement entropy)
- Create 3-5 active space variants per molecule

### Step 3: Run VQE Pipeline
For each (molecule, active space, ansatz) triplet:
- Initialize with MP2 amplitudes (warm start)
- Run VQE optimization (simulator and/or QPU)
- Record: final energy, convergence trajectory, circuit metrics

### Step 4: Analyze Results
- Plot energy error vs active space size
- Compare ansatz performance under identical conditions
- Identify scaling laws for practical quantum advantage

## Error Handling

### Barren Plateaus
If VQE optimization fails to converge:
- Try smaller active space (reduces parameter space)
- Switch from HEA to UCCSD (more structured ansatz)
- Use MP2-amplitude initialization (warm start)

### QPU Noise Degradation
If QPU results significantly worse than simulation:
- Apply error mitigation (zero-noise extrapolation, readout correction)
- Reduce circuit depth via active space compression
- Use shallower ansatz (HEA with fewer layers)

## Resources
- Original paper: arXiv:2512.18203
- Related: `quantum-pave-chemistry` (QM/QM/QM multiscale)
- Related: `generative-ml-quantum-selected-ci` (QSCI with active space)
- Related: `dft-embedded-quantum-chemistry` (DFT+QSCI)
- Related: `tepid-adapt-vqe-molecular-excited-states` (ADAPT-VQE excited states)

## Pitfalls

### Active Space Too Large
- Rule of thumb: (14 electrons, 14 orbitals) is practical limit for current NISQ
- Beyond this, consider active space decomposition or downfolding

### UCCSD Circuit Depth
- UCCSD scales as O(N^4) in circuit depth — becomes infeasible quickly
- Use HEA for larger active spaces, but verify expressivity

### Benchmark Fairness
- When comparing ansatzes, use identical active spaces, optimizer settings, and initialization
- Different active spaces make comparisons meaningless
