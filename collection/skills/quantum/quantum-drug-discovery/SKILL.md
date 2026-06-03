---
name: quantum-drug-discovery
description: "Analysis skill for quantum computing in drug discovery and molecular simulation. Use when researching quantum algorithms for molecular dynamics, quantum ML for drug screening, quantum chemistry methods (DFT, QM/MM), or quantum optimization for drug design. Triggers: quantum drug discovery, quantum molecular simulation, quantum chemistry, quantum pharmacology, quantum screening."
---

# Quantum Drug Discovery Analysis

Analyzes quantum computing applications in pharmaceutical research and drug discovery.

## Overview

This skill provides structured analysis patterns for quantum-enhanced drug discovery, including quantum molecular simulations, quantum machine learning for drug screening, and quantum optimization for drug design.

## Core Research Areas

### 1. Quantum Molecular Simulation

**Key Methods:**
- Density Functional Theory (DFT) - electronic structure calculations
- Hartree-Fock (HF) - molecular orbital theory
- Quantum Mechanics/Molecular Mechanics (QM/MM) - hybrid simulations
- Fragment Molecular Orbital (FMO) - large molecule computations

**Quantum Advantage:**
| Task | Classical Complexity | Quantum Potential |
|------|---------------------|-------------------|
| Electronic structure | O(N^3) | O(log N) |
| Molecular dynamics | O(N^2) per step | O(N) |
| Binding affinity | Approximate | Exact calculations |

### 2. Quantum ML for Drug Screening

**Algorithms:**
- Variational Quantum Eigensolver (VQE) - molecular property prediction
- Quantum Support Vector Machines (QSVM) - compound classification
- Quantum Neural Networks (QNN) - drug-likeness prediction
- Quantum Boltzmann Machines - generative drug design

**Pipeline:**
```
Compound Library → Quantum Encoding → Quantum ML → Hit Identification → Validation
```

### 3. Quantum Optimization for Drug Design

**Applications:**
- QUBO formulation for molecular optimization
- Quantum annealing for lead optimization
- QAOA for multi-objective drug design
- Grover's algorithm for structure search

## Analysis Framework

### Paper Extraction Template

```markdown
# Paper: [Title]
- **Quantum Method**: [DFT/VQE/QM/MM/QAOA/etc.]
- **Drug Stage**: [Discovery/Preclinical/Clinical]
- **Performance**: [accuracy/speedup/novel compounds]
- **Validation**: [Simulation/In vitro/In vivo]
- **Key Insight**: [quantum advantage specific to drug discovery]
```

### Key Questions to Ask

1. **Molecular Scale**: What molecular size is feasible?
2. **Quantum Hardware**: What qubit requirements?
3. **Clinical Impact**: What drug development phase?
4. **Classical Comparison**: What's the baseline method?

## Common Patterns

**Pattern 1: Hybrid Quantum-Classical**
- QM/MM combines quantum core with classical environment
- Practical for large biomolecules
- Most current approaches are hybrid

**Pattern 2: Property Prediction Focus**
- Quantum excels at molecular property calculation
- Binding affinity, solubility, stability
- Faster than classical DFT

**Pattern 3: Early-Stage Applications**
- Most quantum drug work is discovery phase
- Clinical validation still theoretical
- Hardware limitations constrain scale

## Quick Reference

### Quantum Chemistry Methods

| Method | Use Case | Qubit Count |
|--------|----------|-------------|
| VQE | Ground state energy | ~100-1000 qubits |
| QAOA | Optimization | ~50-500 qubits |
| Quantum Phase Estimation | Exact energies | ~1000+ qubits |
| DFT-on-Quantum | Electronic structure | ~200-2000 qubits |

### Drug Development Stages

- **Discovery**: Target identification, hit screening (most quantum papers)
- **Preclinical**: ADMET prediction, lead optimization (some quantum)
- **Clinical**: Trial design, patient matching (few quantum papers)

## Scripts

### analyze_drug_paper.py

Extracts structured insights from quantum drug discovery papers.

```bash
python scripts/analyze_drug_paper.py --paper "path/to/paper.pdf" --output analysis.json
```

## References

For quantum chemistry background:
- `references/quantum_chemistry.md` - DFT, HF, QM/MM methods
- `references/drug_pipeline.md` - drug development stages
- `references/qubit_requirements.md` - hardware scalability

## Related Skills

- **quantum-medical-imaging** - Quantum diagnostics and imaging
- **arxiv-search** - Find quantum drug papers on arXiv
- **neural-dynamics-universal-translator** - Related molecular dynamics

## Notes

- Quantum drug discovery is rapidly evolving - check 2024-2026 papers
- Most research focuses on discovery phase, not clinical
- Hybrid methods (QM/MM) are most practical currently
- Hardware requirements are substantial for large molecules