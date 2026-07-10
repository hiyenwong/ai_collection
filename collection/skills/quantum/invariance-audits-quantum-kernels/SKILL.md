---
name: invariance-audits-quantum-kernels
description: "Real-to-Hermitian taxonomy for auditing representation invariances in quantum machine learning. Covers Grassmann/flag projector kernels, quantum fidelity kernels, QVR anchor operators, and quotient-witness experiments for validating geometric lifts. Activation: quantum kernel audit, representation invariance, Grassmann kernel, flag projector, QVR, quantum variational rewinding, projector kernel, density geometry"
metadata:
  arxiv_id: "2607.07927"
  published: "2026-07-08"
  authors: "Azadeh Alavi, Fatemeh Kouchmeshki, Hossein Akhoundi"
  tags: [quantum, machine-learning, kernel-methods, geometry, invariance]
---

# Invariance Audits for Quantum Kernels

## Description

Real-to-Hermitian taxonomy for auditing which data representations (vectors, projectors, covariances, flags, quantum states, density operators) are appropriate for a given QML task. Determines which distinctions to keep and which to quotient out before fitting a classifier.

## Activation Keywords

- quantum kernel audit
- representation invariance
- Grassmann kernel
- flag projector
- quantum variational rewinding
- QVR
- projector kernel
- density geometry
- Hilbert-Schmidt inner product kernel

## Core Concepts

### The Invariance Decision

Before fitting any QML model, data is often lifted from raw vectors to normalized directions, projectors, subspaces, flags, or density operators. This **invariance decision** determines what information is preserved vs. discarded. The taxonomy provides formal criteria for auditing whether the chosen lift matches the task geometry.

### Real-Side Geometry

| Representation | Mathematical Object | Kernel | When to Use |
|---|---|---|---|
| Vector direction | Unit sphere | Cosine kernel | Direction-only matters |
| Subspace (Grassmann) | Orthogonal projector P | Tr(P₁P₂) | Span matters, order doesn't |
| Flag manifold | Ordered sequence of subspaces | Weighted block flag kernel | Order of subspaces matters |
| Covariance | PSD matrix | Affine-invariant kernel | Second-order structure |

**Key theorem**: Weighted flag kernel is positive semidefinite and block-gauge invariant. Same-span block-swap witness detects when Grassmann geometry fails while ordered flags succeed.

### Quantum-Side Geometry

| Quantum Object | Classical Analog | Kernel |
|---|---|---|
| Pure state \|ψ⟩⟨ψ\| | Rank-1 projector | Fidelity kernel = HS inner product of projectors |
| Mixed state ρ | Density operator | Tr(ρ₁ρ₂) overlap |
| QVR return probability | Anchor overlap score | ⟨ψ\|A\|ψ⟩ with learned anchor A |
| Rank-constrained return | Complex Grassmann anchor | Multi-dimensional subspace overlap |

**Key result**: Noiseless fidelity kernel ≡ Hilbert-Schmidt inner product between rank-1 Hermitian projectors. QVR return probability ≡ overlap score between input projector and learned anchor operator.

## Usage Patterns

### Pattern 1: Kernel Selection Audit

When designing a QML pipeline:
1. Identify what geometric structure the labels depend on
2. Check if discarding that structure (via projection/normalization) loses label-bearing information
3. Select the minimal representation that preserves all label-relevant information
4. Verify with quotient-witness experiment: if a coarser representation works equally well, the finer one is wasteful

### Pattern 2: Failure Diagnosis

When a quantum kernel underperforms:
1. Check if the kernel's invariance discards label-bearing information
2. Run controlled vector → subspace → statevector → anomaly experiments
3. Use same-span block-swap witness to distinguish Grassmann-vs-flag failure modes
4. If mixed/multimodal classes exist, switch from pure-state to density-operator representation

### Pattern 3: Finite-Shot Robustness Check

For limited-data regimes:
1. Test whether the kernel remains PSD under finite-shot estimation noise
2. Verify anchor operators remain Hermitian with limited measurement shots
3. Use rank-constrained returns if class boundaries span subspaces rather than points

## Pitfalls

- **No quantum advantage claimed**: This paper makes no hardware-speedup claim — the contribution is purely about representation correctness
- **Grassmann vs Flag**: When subspaces have inherent ordering, Grassmann kernels fail. Use flag kernels instead
- **Density vs Pure state**: Multimodal classes require density operators, not pure states
- **Quotient-witness**: A representation that works "well enough" may still discard critical information — always verify with ablation

## Related Skills

- `qml-feature-encoding` (data encoding for QML)
- `qml-framework-agnostic-design` (framework-agnostic QML)
- `quantum-ml-patterns` (QML design patterns)
- `quantum-kernel-advantage` (quantum kernel methods)
