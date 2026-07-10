# Neural Quantum States (NQS) for Light-Matter Systems

## Distinction from QNNs
**NQS ≠ QNN**. NQS uses classical neural networks to parameterize quantum many-body wavefunctions (Ψ(σ,n)) for variational Monte Carlo simulation. The neural network is a classical model; no quantum hardware is involved. QNNs use quantum circuits as computational layers.

## Paper: arXiv 2606.14352v1
"Modeling light-matter coupled systems with neural quantum states"

### System Studied
- 2D lattice of Rydberg atoms coupled to a photon mode
- Short-range atom-atom interactions (Rydberg blockade)
- Long-range photon-mediated interactions
- Hybrid Hilbert space: discrete spin + continuous bosonic degrees of freedom

### Architecture
```
Ψ(σ, n) = NNS(σ, n; θ)
```
- σ: spin configuration (discrete, per-site)
- n: photon occupation number (bosonic, requires truncation)
- NNS: Neural network with parameters θ
- Trained via variational Monte Carlo with energy minimization

### Key Results
- Captures spin-spin and spin-photon correlations beyond mean-field
- Ground state phase boundaries deviate quantitatively from mean-field theory
- Efficient in large photon occupation regime (superradiant states)
- Extensible to spin-phonon systems and other hybrid Hilbert spaces

### When to Use NQS vs Other Methods
| Scenario | Method |
|----------|--------|
| Pure spin system, small | Exact diagonalization |
| Pure spin system, large | NQS (RBM, CNN, etc.) |
| Hybrid spin-boson | NQS with hybrid architecture (this work) |
| Mean-field regime sufficient | Mean-field theory (faster) |
| Quantum hardware available | Quantum simulation |

### Skill Link
- New umbrella: `neural-quantum-states-light-matter` covers the general NQS methodology
- This reference file provides the specific paper detail for `quantum-neural-dynamics` context
