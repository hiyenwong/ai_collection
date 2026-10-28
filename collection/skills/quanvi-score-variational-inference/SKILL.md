---
name: quanvi-score-variational-inference
description: "QuanVI methodology: scalable score-based variational inference via quantum maximally mixed states + MPO tensor network parameterization. Use when doing score-based VI (Fisher divergence) on high-dimensional Bayesian posteriors, degenerate low-energy subspace problems, eigenvalue-based score-VI that hits exponential parameter blowup or eigenvector non-uniqueness, or quantum-inspired density-operator optimization."
---

# QuanVI: Score-based Variational Inference via Quantum Maximally Mixed States

Source: arXiv:2609.39164 — Cong, Tao, Li, Sun, Zhao (Sep 2026).

## Problem with prior score-VI

Score-based VI minimizes **Fisher divergence** `E_q[‖∇log q − ∇log p‖²]` instead of KL. The prior eigenvalue-based formulation rewrites the objective as a quadratic form and constructs the variational distribution q from **low-energy eigenstates** of a generalized eigenvalue problem. Two obstacles at high dimension:

1. **Exponential parameter count** — eigenvector ansätze scale with ambient dimension.
2. **Eigenvector non-uniqueness** — in degenerate or nearly-degenerate low-energy subspaces, individual eigenvectors are ill-defined (arbitrary rotations within the subspace), destabilizing optimization.

## Core methodology

### 1. Density-operator (mixed-state) reformulation

Replace the individual eigenvector with the **maximally mixed state over the degenerate low-energy subspace**:

```
ρ = (1/d) Σ_{i=1..d} |ψ_i⟩⟨ψ_i|     (d = subspace dimension)
```

- Rotation-invariant within the subspace → removes non-uniqueness: any orthonormal basis gives the same ρ.
- The Fisher-divergence objective becomes a **linear (trace) functional of ρ**, so optimization is over density operators, not vectors.

### 2. Quantum tensor network (QTN) parameterization

Compress ρ as a **Matrix Product Operator (MPO)**:

```
ρ(θ) = MPO with bond dimension χ  →  parameters O(n·χ²·d_phys²) instead of O(d^n)
```

- Local structure: each site carries a physical index pair (row, col) — ρ is a doubled operator.
- Optimization: DMRG-style sweeps over the MPO tensors (alternating local least-squares), inheriting tensor-network scalability.
- Positivity trace class handled by construction on the mixed-state form.

### 3. Pipeline

1. Build the score-VI quadratic form: A = Fisher-information-like operator, B = normalization overlap operator.
2. Solve the **generalized eigenproblem** A v = λ B v restricted to low-energy subspace — but only extract the **subspace projector**, not eigenvectors.
3. Form ρ = normalized projector onto the r-dimensional low-energy space (maximally mixed).
4. Compress ρ into an MPO ansatz with bond dimension χ.
5. Sweep-optimize MPO tensors against the Fisher divergence; monitor trace normalization.
6. Samples from q recovered via density-operator factorization (per-site marginals + autoregressive or tensor-skeleton decomposition).

## Key results (paper)

- Exact agreement with eigenvalue-based score-VI in low dimensions (sanity check).
- Scales to high-dimensional synthetic targets and **Bayesian posterior approximation** benchmarks, including **non-Gaussian** posteriors where KL-VI and eigenvalue score-VI both struggle.
- Ablations: MPO bond dimension χ controls the accuracy-cost frontier; density-operator form converges where eigenvector-based form oscillates in degenerate subspaces.

## When to use vs alternatives

| Method | Divergence | Handles degeneracy | High-dim scaling |
|---|---|---|---|
| KL-VI (standard) | reverse KL | n/a (mode-seeking) | good, but wrong objective for multimodal |
| Eigenvalue score-VI | Fisher | ✗ (eigenvector ill-defined) | ✗ exponential params |
| **QuanVI** | Fisher | ✓ (maximally mixed state) | ✓ (MPO compression) |

Use QuanVI when: the target is multimodal/degenerate; you need score matching objectives (e.g., when ∇log p is easier to evaluate than p); dimension makes vector ansätze impossible.

## Implementation checklist

- [ ] Define ∇log p (score) oracle for the target — only scores needed, never normalized p
- [ ] Assemble the quadratic-form operators (A, B) from score evaluations
- [ ] Low-energy subspace: compute eigenvalues only up to a gap; project — do NOT use individual eigenvectors
- [ ] ρ = projector / rank; verify Tr ρ = 1, ρ ≽ 0
- [ ] MPO ansatz: start χ=4, double until validation Fisher divergence plateaus
- [ ] Sweep optimizer: two-site updates (DMRG2-like) more stable than single-site
- [ ] Diagnostics: subspace rotation test (objective must be invariant to basis re-choice), trace drift per sweep
- [ ] Sampling: per-site marginal + conditional chain, or MPO-to-tensor cross-approximation

## Pitfalls

1. **Do not chase eigenvectors in degenerate subspaces** — the whole point of the mixed-state form; basis-dependence noise is a symptom you skipped this.
2. **Bond dimension vs posterior rank** — multimodal posteriors need χ ≥ (modes × local correlation length); under-parameterized MPO silently collapses to nearest Gaussian-like factor.
3. **Score oracle quality** — near-zero-density regions make ∇log p estimates explode; clip or reweight like score-matching practice.
4. **Trace normalization drift** during sweeps — renormalize per sweep or the effective q tilts.

## Related skills

- `qml-feature-encoding-survey` — when quantum feature maps feed the density operator
- Tensor-network skills (`tensor-network-*`) for MPO machinery
