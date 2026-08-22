---
name: path-integral-cognition-model
description: Path Integral Model of Cognition methodology combining quantum physics path integrals with cognitive cost optimization using imaginary-time evolution under projector Hamiltonians and Wick rotation for unitary equivalent representation
license: CC BY 4.0
---

# Path Integral Model of Cognition

This skill implements the mathematical and physical framework from arXiv:2607.24807 "A Path Integral Model of Cognition" by Emori et al. (2026).

## Core Framework

The model treats goal-directed cognitive processes as **imaginary-time evolution (ITE)** under a **projector Hamiltonian** that rewards configurations consistent with target concepts.

### Three Key Results

1. **ITE as Riemannian Gradient Flow**: The imaginary-time evolution coincides with double-bracket flow and represents the Riemannian gradient flow of a Hilbert-Schmidt cost function, with unique minimum as the solution.

2. **Wick Rotation Equivalence**: A Wick rotation re-expresses the non-unitary descent as equivalent unitary evolution on the same Hilbert space, admitting an exact discrete path-integral representation where:
   - Oracle plays role of potential energy
   - Initial-state diffusion projector plays role of kinetic energy

3. **Consciousness Continuum**: The transition from unconscious to conscious processing corresponds to the strength of unitary interaction between cognitive system and neural-environment probe:
   - **Weak coupling limit**: Recovers GKSL decoherence model (Markovian)
   - **Strong coupling limit**: Achieves projective, reportable fixation ("Aha" insight endpoint)
   - Both regimes share same ITE and path-integral structure; only measurement-interaction strength varies

## Implementation Guidelines

### Mathematical Setup

For cognitive state |ψ⟩ evolving toward target concept |φ⟩:

```
H_projector = |φ⟩⟨φ|  # Projector Hamiltonian
∂_τ|ψ(τ)⟩ = -H_projector|ψ(τ)⟩  # Imaginary-time evolution
```

### Cost Function

The Hilbert-Schmidt cost function to minimize:
```
C(|ψ⟩) = || |ψ⟩⟨ψ| - |φ⟩⟨φ| ||_HS²
```

### Path Integral Representation

After Wick rotation (τ → it), the unitary evolution becomes:
```
|ψ(t)⟩ = e^(-iHt)|ψ(0)⟩
```

With discrete path integral:
```
⟨ψ_f|e^(-iHt)|ψ_i⟩ = ∫ D[ψ] e^(iS[ψ]/ℏ)
```
Where S[ψ] = ∫ dt [⟨ψ|T|ψ⟩ - ⟨ψ|V|ψ⟩] with T = diffusion projector, V = oracle.

### Decoherence Modeling

GKSL master equation for system-environment interaction:
```
dρ/dt = -i[H, ρ] + Σ_k (L_k ρ L_k† - ½{L_k†L_k, ρ})
```

Where coupling strength γ determines consciousness level:
- γ → 0: Unconscious processing (decoherence-dominated)
- γ → ∞: Conscious reportable state (projective measurement)

## When to Use This Skill

Use when modeling cognition with quantum-inspired methods, implementing path integral approaches to neural dynamics, studying consciousness models based on quantum formalism, or exploring Wick rotation in cognitive contexts.

## References

- Emori, H., Kondo, K., Iriki, A., & Khrennikov, A. (2026). A Path Integral Model of Cognition. arXiv:2607.24807 [q-bio.NC]
- Asano, M., et al. GKSL decoherence model applications in cognitive contexts
- RIKEN-iTHEMS-Report-26

## Activation Keywords

- path integral cognition
- imaginary time evolution cognition  
- Wick rotation consciousness
- projector Hamiltonian cognition
- GKSL cognitive model
- quantum cognition path integral
- double bracket flow cognition
- Hilbert-Schmidt cognitive cost