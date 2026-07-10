# Physics-Informed VQC for Phase Detection — Session Notes (arXiv: 2606.14489)

## Paper
- **Title**: Physics-Informed Variational Quantum Classifier for Phase Detection in Strongly Correlated Matter
- **arXiv**: 2606.14489v1
- **Date**: 2026-06-12
- **Domain**: Quantum ML + Condensed Matter Physics

## Core Methodology

### Symmetry-Preserving Ansatz
- Extract symmetry group of Hamiltonian (Z2, U(1), SU(2))
- Construct parameterized gates that commute with symmetry operators
- Remove gates violating conservation laws
- Include physics-motivated entanglement patterns matching system correlation structure

### Physics-Regularized Loss
- L = L_classification + λ × L_physics
- Physics terms: symmetry violation penalty ||[U(θ), S]||², order parameter alignment ⟨O⟩_predicted vs ⟨O⟩_known, energy constraints ⟨H⟩ within expected phase range

### Applications
- 1D transverse field Ising model: ferromagnetic vs paramagnetic phase detection
- Topological phase classification: trivial vs topological without explicit winding number calculation
- Near critical points: physics-informed VQC outperforms generic VQC

## Why This Matters
- Generic VQCs suffer from barren plateaus and lack physical consistency guarantees
- Physics priors reduce required circuit depth, improve trainability, ensure predictions respect known physical laws
- Bridges quantum ML with condensed matter theory — reusable across phase detection, materials characterization, quantum simulation validation

## Related Skills
- `fourier-vqc-nonlinear-embedding-barren-plateau` (barren plateau mitigation)
- `quantum-ml-patterns` (general QML patterns)
- `quantum-neural-dynamics` (NQS for quantum systems)