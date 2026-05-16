---
name: quantum-cellular-automata-symmetries
description: >
  Analysis of non-invertible (fusion category) symmetries on tensor-product Hilbert spaces combined with
  quantum cellular automata (QCA). Covers classification of realizable symmetries, weakly integral constraint,
  and QCA-refined representation categories. Use when: (1) studying non-invertible symmetries in quantum systems,
  (2) analyzing quantum cellular automata, (3) classifying fusion category symmetries on qubit lattices,
  (4) investigating symmetry-enriched tensor network states, or (5) exploring categorical symmetry in quantum
  information. Activation: quantum cellular automata, non-invertible symmetry, fusion category symmetry,
  tensor product Hilbert space, QCA symmetry, weakly integral category, 量子元胞自动机, 非可逆对称性.
---

# Quantum Cellular Automata Symmetries

## Description

Framework for analyzing (1+1)-dimensional fusion category symmetries on tensor-product Hilbert spaces
with quantum cellular automata (QCA) mixing. Based on arXiv:2605.15194.

## Core Principles

### Realizability Constraint
Any fusion category symmetry realizable on a tensor-product Hilbert space must be **weakly integral**:
- FPdim(C) must be of the form √n for integer n
- This constrains which categorical symmetries can appear in lattice models

### QCA-Refined Symmetries
Quantum cellular automata can refine realizable symmetries:
- QCA act as symmetry-preserving automorphisms
- The refined representation category Rep(QCA) classifies allowed symmetry actions
- This provides a systematic classification beyond group symmetries

### Key Mathematical Structures

1. **Fusion categories**: Generalize group representations to non-invertible objects
2. **QCA**: Locality-preserving unitary maps on lattice Hilbert spaces
3. **Representation categories**: Classification of symmetry actions via categorical data
4. **Weak integrality**: Necessary condition for lattice realizability

## Application Domains

### Quantum Error Correction
- Non-invertible symmetries as logical operators in topological codes
- QCA as fault-tolerant logical gates
- Symmetry-protected degeneracy for encoding

### Tensor Network States
- Matrix Product States (MPS) with categorical symmetries
- Classification of symmetry-protected topological phases
- Non-invertible symmetry actions on virtual bonds

### Quantum Information
- Symmetry-based resource theories
- QCA as information-processing primitives
- Classification of localizable entanglement

## Instructions for Agents

### Step 1: Identify Symmetry Structure
Determine if the system has:
- Group symmetry (invertible)
- Fusion category symmetry (potentially non-invertible)
- Mixed symmetry (group + categorical)

### Step 2: Check Weak Integrality
Verify FPdim(C) = √n condition:
- If not weakly integral, symmetry cannot be realized on tensor-product space
- Use this as a quick filter for candidate symmetries

### Step 3: Analyze QCA Action
If QCA are present:
- Determine the QCA index (GNVW index in 1D)
- Check compatibility with symmetry fusion rules
- Classify the refined symmetry category

### Step 4: Construct Representation
Build the categorical representation:
- Simple objects → symmetry defects
- Fusion rules → defect composition
- QCA action → automorphism of fusion category

## Limitations

- Primarily developed for (1+1)D systems; higher dimensions require different tools
- Assumes strict locality; long-range interactions may break classification
- Weak integrality is necessary but not sufficient for realizability

## Related Skills

- quantum-resource-distillation: Quantum resource theory and distillation
- quantum-topological-analysis: Quantum topological data analysis
- quantum-error-correction-methods: QEC patterns
- self-correcting-quantum-memory-3d: Self-correcting quantum memory
- quantum-algebraic-structures: Quantum algebraic structures

## Notes

- Based on Wen, Inamura, Schafer-Nameki (2026): "Non-Invertible Symmetries on Tensor-Product Hilbert Spaces and Quantum Cellular Automata"
- Key result: realizable fusion category symmetries are exactly those that are weakly integral
- QCA provide the mechanism for symmetry refinement beyond static classification
