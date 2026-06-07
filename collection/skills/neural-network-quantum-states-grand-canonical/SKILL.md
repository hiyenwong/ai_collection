---
name: neural-network-quantum-states-grand-canonical
description: "Neural network quantum state (NQS) architecture for grand canonical ensemble bosonic systems. Enables variational Monte Carlo with variable particle number in Fock space. Activation: neural quantum states, grand canonical ensemble, bosonic wavefunctions, Fock space, variational Monte Carlo, NQS, quantum many-body ground state."
---

# Neural Network Quantum States in Grand Canonical Ensemble

> Variational Monte Carlo with neural quantum states capable of representing symmetric bosonic wavefunctions in Fock space, enabling study of systems with variable particle number.

## Metadata
- **Source**: arXiv:2605.07779
- **Authors**: Anton Hul, Matija Medvidović, Juan Carrasquilla
- **Published**: 2026-05-08
- **Category**: Quantum Physics / Machine Learning

## Core Methodology

### Key Innovation
Extends neural quantum states (NQS) from fixed-particle-number systems to the **grand canonical ensemble**, enabling:
- Variable particle number systems under chemical potential control
- Symmetric bosonic wavefunctions in Fock space
- Direct computation of one-body reduced density matrices
- Access to observables like condensate fractions and radial density profiles

### Technical Framework

1. **Fock Space Architecture**: Neural network operates in Fock space rather than fixed-particle Hilbert space
2. **Symmetric Bosonic States**: Enforces bosonic exchange symmetry in the wavefunction representation
3. **Monte Carlo Sampling**: Combines variational state with Monte Carlo sampling for efficient evaluation
4. **Geometric Optimization**: Uses geometric optimization for variational energy minimization
5. **Chemical Potential Control**: System converges to physical boson number under set chemical potential

### Results
- Competitive variational energies across 1D and 2D systems
- Converges to correct physical boson number
- Accurate one-body reduced density matrices
- Access to condensate fractions and radial density profiles

## Implementation Guide

### Prerequisites
- Neural network framework (PyTorch/JAX)
- Monte Carlo sampling infrastructure
- Variational Monte Carlo implementation

### Step-by-Step
1. **Fock Space Representation**: Encode many-body states as occupation number vectors in Fock space
2. **Symmetric Architecture**: Design neural network that respects bosonic exchange symmetry
3. **Chemical Potential**: Include μN term in Hamiltonian for grand canonical ensemble
4. **MC Sampling**: Sample configurations weighted by |ψ(n)|² where n is occupation number
5. **Optimization**: Minimize E = ⟨ψ|H - μN|ψ⟩/⟨ψ|ψ⟩ using stochastic reconfiguration
6. **Observables**: Compute 1-RDM and extract condensate fraction

### Code Pattern
```python
# Grand canonical NQS energy (conceptual)
def grand_canonical_energy(nqs, hamiltonian, mu, mc_samples):
    """Compute E = ⟨H - μN⟩ in grand canonical ensemble."""
    # Sample occupation number configurations
    configs = sample_fock_space(nqs, mc_samples)
    # Local energy: (H - μN)ψ / ψ
    local_energies = compute_local_energy(nqs, configs, hamiltonian, mu)
    return torch.mean(local_energies), torch.var(local_energies) / len(configs)
```

## Applications
- Bosonic quantum many-body systems
- Bose-Einstein condensates
- Quantum phase transitions with variable particle number
- Superfluid systems
- Quantum optics with variable photon number

## Related Skills
- universal-neural-propagator-quantum-dynamics
- quantum-neural-network-data-loading
- quantum-ml-patterns

## Pitfalls
- Fock space dimensionality grows rapidly with system size
- MC sampling efficiency depends on wavefunction quality
- Chemical potential tuning requires careful convergence checks
