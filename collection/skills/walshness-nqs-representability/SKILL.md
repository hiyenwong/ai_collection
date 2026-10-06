---
name: walshness-nqs-representability
category: ai_collection
description: Use when gauging if an NQS can compactly represent a quantum state, or choosing optimal basis via Walshness.
version: "1.0.0"
source: arXiv
source_title: "Walshness: an intrinsic neural-network representability metric for quantum states"
authors: Nisarga Paul, Kehuang Chen, Jessica K. Jiang, Haimeng Zhao, Di Luo
published: 2026-09-30
categories: cond-mat.dis-nn, quant-ph
trigger_words:
  - neural quantum states
  - NQS representability
  - Walshness
  - optimal basis choice
  - Marshall sign rule
  - sign structure
  - quantum state complexity
  - NQS learnability
---

# Walshness — Intrinsic NQS Representability Metric

## Overview

Walshness (arXiv:2610.00505) is a basis-optimized complexity metric for n-qubit states |ψ⟩ that **provably characterizes when a neural quantum state (NQS) can compactly represent |ψ⟩**, two-sided: low Walshness ⟺ efficient NQS representation. It converts the murky question "is this state learnable by a neural network?" into a computable number, and basis selection into a **classical spin-model energy minimization** — recovering and generalizing the Marshall sign rule.

## Core Definitions

### 1. Fixed-basis α-Walshness (Z basis)
Take the Walsh transform ψ̂(r) of the computational-basis wavefunction. Normalize |ψ̂(r)|² into a classical distribution p_ψ(r) over Walsh modes r ∈ {0,1}ⁿ. Then:

**Wᶻ_α[|ψ⟩] = (1/α) · log E_{r∼p_ψ}[ e^{α|r|₁} ]**,  α > 0

- |r|₁ = Hamming weight of the Walsh mode index = **interaction order** of the corresponding Walsh character.
- 0 ≤ Wᶻ_α ≤ n. Low Walshness ⇔ Walsh spectral mass concentrated on **low-degree Walsh modes** (few-body-like structure).
- Numerics: evaluate via **LogSumExp** (SciPy) for stability, relative tolerance 10⁻¹⁰.

### 2. Intrinsic Walshness (basis-independent)
**W_α[|ψ⟩] = min_{U=⊗ᵢUᵢ, Uᵢ∈SU(2)} Wᶻ_α[U|ψ⟩]**

Minimize over all local Pauli-basis rotations (one SU(2) per site). This is the intrinsic complexity analogue of entanglement entropy — but it captures **learnability structure beyond entanglement** (stabilizer states have low Walshness; GHZ does not).

### 3. Key properties
- Invariant under: rescaling, qubit permutation, single-site unitaries.
- **Additive over tensor products**: W_α[ψ⊗φ] = W_α[ψ] + W_α[φ].
- **Vanishes iff |ψ⟩ is a product state**.
- GHZ: intrinsic W_α = n/2 (n even); Haar-random & random stabilizer states: W_α ≈ n·g_α where g_α = (1/α)log((1+e^α)/2) — near maximal.
- **Entanglement bound**: S_L:R ≤ (n/2)·h₂(2W_α/n) for W_α ≤ n/2 (h₂ = binary entropy). Extensive Walshness is *necessary* for extensive entanglement, but low Walshness states (stabilizers) can still be highly entangled — Walshness measures *neural-compressibility structure*, not entanglement per se.

## Proposition 1 — Basis Search as Classical Spin Model

Parameterize each single-qubit rotation by a 3D unit vector n̂ⱼ: Uⱼ†XⱼUⱼ = n̂ⱼ·σⱼ. Define per-site operator A_α(n̂) = cosh(α/2)·I − sinh(α/2)·n̂·σ. Then:

**W_α[|ψ⟩] = (n/2) + (1/α)·log min_{n̂ⱼ} E[⊗ⱼ A_α(n̂ⱼ)]**

The minimizing basis is found by minimizing the energy of a **classical spin Hamiltonian** with one spin-1 vector n̂ⱼ per site, whose couplings are multi-spin correlations ⟨σⱼ₁···σⱼₖ⟩ of |ψ⟩. The minimizing basis can exhibit **spontaneous ordering** (e.g. period-two staggering in TFIM at g<1 that breaks translation symmetry).

**Practically**: optimize n̂ⱼ with gradient descent / Adam on the energy landscape (use ≥32 random inits for TFIM; multiple restarts matter — the functional is highly non-convex).

## Main Theorems (informal)

### Theorem 1 — MLP representability, two-sided
- **(⟸)** Fixed-basis Walshness ω = Wᶻ_α[ψ] admits an MLP representation of ψ(s) with **width n^O(ω), depth O(log ω)** to any constant infidelity.
- **(⟹)** If W⁰_α or W_α ≥ n − O(1) (near-maximal Walshness), then ANY MLP achieving constant infidelity needs depth Ω(log n) (polynomial nonlinearity) or Ω(log n / log log n) (analytic nonlinearity like tanh — effective c_σ scales with depth d).

### Theorem 2 — RBM representability (multiplicative Walshness)
RBMs parameterize ψ multiplicatively (exponential form), so the right quantity is **multiplicative Walshness** of log ψ(s):
- Bounded multiplicative Walshness ⟹ RBM with **poly(n) hidden units + bounded hidden-visible connectivity** to constant infidelity.
- Conversely, bounded-connectivity RBM ⟹ bounded multiplicative Walshness.
- Use multiplicative variant whenever the NQS ansatz factorizes (RBM, DBM, deep Boltzmann); use additive W_α for MLP-style direct wavefunction ansätze.

## Case Studies (from paper)

| State | Result |
|---|---|
| Ferromagnetic product states | W_α = 0 (product states, tight) |
| Stabilizer states | Bounded W_α despite high entanglement — efficiently NQS-learnable |
| GHZ | Intrinsic W = n/2; even with basis optimization GHZ is NOT compactly representable |
| TFIM ground state (g=0.2, ferromagnetic) | **Several orders of magnitude lower infidelity** when training MLP-NQS in Walshness-minimizing basis vs Z basis at comparable compute; minimizer shows period-2 staggering |
| Mixed-field toric code | Large infidelity reduction via Walshness-minimizing local basis |
| 1D/2D antiferromagnets (XY/XYZ AFM) | Walshness minimization **recovers and generalizes the Marshall sign rule** — the optimal basis is exactly Marshall-like |

## Practitioner Workflow

1. **Compute fixed-basis Walshness** of your state in the current basis (Walsh transform → p_ψ → LogSumExp formula).
2. **Optimize the basis**: minimize E[⊗ⱼA_α(n̂ⱼ)] over n̂ⱼ ∈ S² via gradient descent, many restarts (non-convex).
3. **Re-parameterize** the NQS input: ψ(s) expressed in the new local Pauli basis defined by n̂ⱼ.
4. **Train** (infidelity or variational loss) — expect orders-of-magnitude infidelity reduction for sign-structured states.
5. **Diagnose**: if intrinsic W_α ≈ n even after optimization, no basis will rescue compact NQS representation — switch architecture (depth Ω(log n) needed) or representation (e.g. density-matrix/symmetric ansatz).

## Activation

- Choosing a local basis / sign rule before NQS training (replaces ad-hoc Marshall/Jastrow guesses with a principled objective)
- Predicting NQS trainability/compactness before spending GPU hours
- Diagnosing why an NQS fails to converge on a given state
- Benchmarking state complexity beyond entanglement entropy
- Any NQS architecture selection question (MLP vs RBM → additive vs multiplicative Walshness)

## Pitfalls

- **α choice**: α > 0 tunes which Walsh-mode orders dominate; results are qualitatively stable across α but pick one α (e.g. α=1, the "W₁" used in figures) and keep it fixed when comparing bases.
- Walshness of the **same state differs per basis** — always report intrinsic W_α (post-minimization) for fair comparison, not Wᶻ_α of an arbitrary basis.
- The minimization landscape is non-convex: single-init optimization can miss the Marshall-like basis; use ≥32 restarts.
- Entanglement is an *upper* bound on what Walshness explains — high-Walshness states can have modest entanglement (and vice versa: stabilizers). Don't conflate the two metrics.
- GHZ-type cat states sit at intrinsic W = n/2 even in the best basis — no basis trick makes them compact.

## References

- Paul, Chen, Jiang, Zhao, Luo. "Walshness: an intrinsic neural-network representability metric for quantum states." arXiv:2610.00505 (2026)
- Marshall (1955) sign rule — recovered as special case of Walshness-minimizing basis
- Levin & Nave (2007) TEBD / sign-structure literature — Walshness gives the first intrinsic, computable sign-structure complexity
