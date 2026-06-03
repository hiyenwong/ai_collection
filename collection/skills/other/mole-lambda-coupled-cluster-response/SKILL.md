---
name: mole-lambda-coupled-cluster-response
description: "MōLe-Λ methodology for learning coupled-cluster response states. Extends Molecular Orbital Learning (MōLe) to predict full CCSD response state by jointly learning T and Λ amplitudes from localized Hartree-Fock orbitals. Provides CC-quality energies, forces, dipoles, polarizabilities, electron density at ML speed. ICML 2026 AI4Physics. Activation: coupled-cluster, CCSD response, molecular orbital learning, quantum chemistry surrogate, Λ-amplitudes, equivariant quantum chemistry, wavefunction learning"
metadata:
  arxiv_id: "2605.29622"
  published: "2026-05-28"
  authors: "Andreas Burger, Luca Thiede, Abdulrahman Aldossary, Jorge A. Campos-Gonzalez-Angulo, Alex Zook, Jérôme Florian Gonthier, Alán Aspuru-Guzik"
  tags: [quantum-chemistry, coupled-cluster, equivariant-ml, molecular-orbitals, surrogate-model, response-theory]
---

## MōLe-Λ: Learning the Coupled-Cluster Response State

## Core Insight

Coupled-cluster (CC) theory is the gold standard of quantum chemistry, but its O(N⁶) computational cost limits routine access to accurate energies, forces, and response properties. **MōLe-Λ** extends the Molecular Orbital Learning (MōLe) framework to learn the **full CCSD response state** — not just the wavefunction (T amplitudes) but also the response (Λ amplitudes) — enabling prediction of **all** CC-quality observables at ML inference speed.

## Key Architecture Components

### 1. Joint T + Λ Amplitude Learning

The coupled-cluster equations have two sides:
- **Right-hand (T) amplitudes**: Determine the correlated wavefunction |Ψ⟩ = e^T |Φ₀⟩
- **Left-hand (Λ) amplitudes**: Required for computing response properties (forces, dipoles, polarizabilities)

MōLe-Λ learns **both** from localized Hartree-Fock molecular orbitals:

```
(T, Λ) = MōLe-Λ(orbital_features)
```

### 2. Symmetry-Consistent Readout Heads

```python
class MoLeLambdaArchitecture:
    """
    Extends MōLe with Λ and T readout heads that mirror
    the symmetry constraints of the CCSD equations.
    """
    def __init__(self):
        self.encoder = EquivariantOrbitalEncoder()  # Original MōLe encoder
        self.T_head = OddSignEquivariantDecoder()    # T amplitudes (antisymmetric)
        self.Lambda_head = OddSignEquivariantDecoder()  # Λ amplitudes (antisymmetric)

    def forward(self, localized_orbitals):
        features = self.encoder(localized_orbitals)
        T = self.T_head(features)
        Lambda = self.Lambda_head(features)
        return T, Lambda
```

### 3. Preserved Invariance Properties

MōLe-Λ preserves the key physical invariances:
- **Equivariant orbital encoder**: Respects rotational/translational symmetry
- **Odd sign-equivariant decoding**: Correct behavior under orbital sign flips
- **Locality**: Exploits spatial decay of electron correlation
- **Size-extensivity**: Energy scales correctly with system size

## Observable Prediction

MōLe-Λ recovers **all** CCSD-quality observables:

| Observable | Requires | MōLe-Λ Support |
|---|---|---|
| Energy | T only | ✓ |
| Forces (gradients) | T + Λ | ✓ |
| Dipole moments | T + Λ | ✓ |
| Quadrupole moments | T + Λ | ✓ |
| Polarizabilities | T + Λ | ✓ |
| Electron density | T + Λ | ✓ |
| Pair density (2-electron) | T + Λ | ✓ |

## Speed Advantage

```
Full CCSD:     O(N⁶) — expensive, scales poorly
MōLe-Λ:        O(N) inference — after training, near-constant cost
Speedup:       ~100-1000x for large molecules
```

## Workflow

```
1. Prepare localized Hartree-Fock molecular orbitals
2. Encode orbitals with equivariant encoder
3. Decode T and Λ amplitudes via symmetry-consistent readout heads
4. Compute observables from (T, Λ) pair using standard CC formulas
5. Validate against reference CCSD calculation
```

## Practical Usage

```python
# Pseudocode for MōLe-Λ inference
import torch

def compute_cc_properties(molecule, model):
    """Compute CC-quality properties using MōLe-Λ."""
    # Step 1: Get localized HF orbitals
    hf_orbitals = get_localized_orbitals(molecule)

    # Step 2: Encode + decode
    T, Lambda = model(hf_orbitals)

    # Step 3: Compute observables
    energy = cc_energy(T)
    forces = cc_forces(T, Lambda)
    dipole = cc_dipole(T, Lambda)
    polarizability = cc_polarizability(T, Lambda)
    density = cc_electron_density(T, Lambda)
    pair_density = cc_pair_density(T, Lambda)

    return {
        'energy': energy,
        'forces': forces,
        'dipole': dipole,
        'polarizability': polarizability,
        'density': density,
        'pair_density': pair_density,
    }
```

## When to Apply

- **Surrogate modeling**: Replace expensive CCSD calculations with ML inference
- **High-throughput screening**: Scan thousands of molecules at CC quality
- **Response property prediction**: When forces, dipoles, or polarizabilities are needed
- **Molecular dynamics**: CC-quality forces at ML speed enables ab initio MD

## Key Findings

1. **Joint learning works**: T and Λ can be learned simultaneously from localized orbitals
2. **Symmetry matters**: Enforcing CCSD symmetry constraints in readout heads is critical
3. **Property expansion**: Extending from energies-only to full response properties
4. **Speed without sacrifice**: Near-CCSD accuracy at ML inference speed

## Pitfalls

- **Training data**: Requires pre-computed CCSD reference data (T, Λ pairs) for training
- **Transferability**: Model trained on specific chemical space may not generalize
- **Orbital localization**: Results depend on quality of localized orbital construction
- **Extrapolation**: ML surrogate may fail on molecules outside training distribution

## References

- **Paper**: "MōLe-Λ: Learning the Coupled-Cluster Response State for Energies, Gradients, and Properties" (arXiv:2605.29622)
- **Conference**: ICML 2026 AI4Physics
- **Categories**: cs.LG, physics.chem-ph
- **Date**: May 28, 2026
