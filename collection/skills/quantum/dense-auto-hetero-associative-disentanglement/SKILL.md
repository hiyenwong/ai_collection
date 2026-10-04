---
name: dense-auto-hetero-associative-disentanglement
description: "Dense Hopfield module networks that disentangle pattern mixtures."
category: ai_collection
---

# Dense Auto-Hetero Associative Memories for Pattern Disentanglement

**Source**: Agliari, Alessandrelli, Barra, Fachechi (Sapienza Roma / Salento), arXiv:2609.32605 (26 Sep 2026), cond-mat.dis-nn.

**Trigger**: disentangling pattern mixtures, dense/modern Hopfield modules, attractor-based decoding, high-order Hebbian couplings, blind source separation via attractors, mixture-state splitting, BAM/TAM generalization.

## Core Idea

Networks of interacting Hebbian networks go **beyond associative memory** into *pattern disentanglement*: fed a spurious mixture of stored patterns, modules spontaneously specialize on and retrieve the different constituents. This paper upgrades the pairwise architecture to **dense** (high-order) Hebbian couplings so disentanglement survives **linearly extensive load K = Θ(N)** where the pairwise version fails.

## Architecture

- L modules of N binary neurons each (state σ^a ∈ {−1,+1}^N; full state σ ∈ {−1,+1}^{L×N}).
- Stored patterns ξ^µ (µ=1..K), Rademacher entries.
- **Auto-associative** (within-module): order-P Hebbian couplings J^(P), attractive, term ∝ Σ (m_a^µ)^P; P even, P>2.
- **Hetero-associative** (across modules): order-D couplings J^(D), **repulsive** (penalty sign), term ∝ −λ Σ (m_a^µ m_b^µ)^{D/2}; D/2 even (module-wise spin-flip symmetry preserved).
- n-body Hebbian rule: J^(n)_{i1..in} = N^{-(n−1)} Σ_µ ξ^µ_{i1}···ξ^µ_{in}.
- Effective field on module a: ĥ^a = h_{a→a} (auto) + Σ_{b≠a} h_{b→a} (anti-imitative) + θ h^a (external cue = the mixture signal).
- Dynamics: σ^a(t+1) = sign[tanh(β ĥ^a(σ(t))) + u^a(t)], u ~ U([−1,1]) — stochastic parallel updates; β = inverse temperature.

## Key Design Rule (the central insight)

**Set 2 < P ≤ D.** Storage capacity is determined by the LOWEST interaction order, so densifying only auto couplings while leaving hetero pairwise keeps the bottleneck. With P>2 the pattern-induced slow noise vanishes (low-load regime relative to capacity Θ(N^{P−1})); requiring P ≤ D makes module-induced noise suppressed even more strongly. Result: clean K = αN storage with order parameters = Mattis magnetizations only (no spin-glass machinery).

Cost: couplings need O(N^P) + O(N^D) entries — Hebbian construction is deterministic, but *learning* them would be hard. (Simulation shortcut: dynamics computable via overlaps m_a^µ in O(KN) per update without materializing tensors.)

## Statistical Mechanics (Guerra interpolation, RS ansatz)

- Order parameters: module-wise Mattis magnetizations m̄_a^µ. Disentangled state = **diagonal** magnetization matrix (each module on a distinct pattern); mixture state = all-entries matrix.
- Quenched free energy A(β) via Guerra's interpolation; self-consistency equations (input–output relations):
  `m̄_a^ν = E_ξ ξ^ν tanh β[Σ_µ (m̄_a^µ)^{P−1} − (λD/2)Σ_{b≠a}(m̄_a^µ)^{D/2−1}(m̄_b^µ)^{D/2} ξ^µ + βθh^a]`
- **Phase diagram** in (β, λ): ergodic (m̄≈0) / spurious (stuck in mixture, m̄≈0.5 for L=3) / disentangling (m̄≈1). Disentangling region = {spurious states unstable} ∩ {disentangled states stable}.
- Unlike pairwise case, region boundary is load-independent; disentangling→ergodic transition is **discontinuous** for P>2.
- Worked params (L=3): P=4, D=8, β=10, λ=3.5, θ≈0.1–0.2 — disentangles 3-mixtures at α up to ~0.3–0.5, N=1000 f_dis→1. Pairwise (P=D=2) fails at any α>0.
- Moderate temperature HELPS escape from mixtures (too-cold dynamics gets stuck at m≈0.5; too-hot destroys retrieval) — a constructive role of noise.

## Application 1: Pattern Reconstruction from Hebbian Tensors

Given only d unlabeled mixtures x^γ = sign(Σ_µ z_µγ ξ^µ) and the tensors:
1. **Candidate generation**: run dynamics from each x^γ in every module → pool of candidates.
2. **Redundancy removal**: dedupe candidates by mutual overlap.
3. **Acceptance test**: filter via pairwise tensor J^(2) compatibility (higher-order tensors carry the retrieval info; J^(2) suffices for acceptance).
Minimal observations: d_min ~ (K/L) log(K/ε). Dense model succeeds at extensive α; pairwise baseline degrades rapidly with α (works only as α→0).

## Application 2: Attractor-Based Communication Protocol (crypto PoC)

- Vocabulary size ≤ C(K,3): each token ↔ triplet (µ,ν,ℓ) of secret Rademacher patterns.
- **Encode**: σ = sign(ξ^µ+ξ^ν+ξ^ℓ+T_enc·ũ) (encoding temperature T_enc trades obfuscation vs decodability; correlation with each constituent = 1/2 for T_enc≤1, ~1/T_enc beyond 3).
- **Mask**: η^w = sign(J^(2) τ^w) where τ^w is fresh PRNG Rademacher from shared seed → ciphertext σ̃ = η^w ⊙ σ (bitwise XOR keystream; mask depends on two independent secrets: seed + tensor).
- **Decode**: regenerate η^w, unmask, run dense TAM dynamics with σ as init + external field → modules converge to the three constituents (in arbitrary order) → permutation-invariant code ĉ = Θ(σ^1⊙σ^2⊙σ^3), match vs shared codebook by Hamming distance.
- **Robustness**: attractor decoding degrades GRACEFULLY — error-free up to T_enc≈4 on clean channel; still error-free up to T_enc≈2.5 with 60% block erasure; few % error at 80% erasure. Insensitive to burst structure (sites statistically equivalent). Masking defeats frequency analysis + trained classifiers (rank-frequency flat, chance-level accuracy).
- L=3 is principled: three-mixtures are the most stable spurious states; also RGB channels, major triads. L=2 = cocktail-party/blind source separation; L=5 ~ multisensory integration.

## When to Use

- Disentangling superposed signals with attractor dynamics (BSS alternative)
- Error-correcting decoding for extremely noisy/erasure channels (graceful degradation vs conventional codes' cliff)
- neuromorphic/physical implementations where attractor basins = free error correction
- Formal security analysis is NOT done — this is a channel-robustness result, not cryptographic security.

## Key Formulas

- Cost: H = −Σ J^(P) σ…σ + (λ/2)Σ_{b>a} J^(D) σ^a…σ^b… − (θ/√N)Σ h^a·σ^a
- Dense capacity: K = Θ(N^{P−1}); operate at K = αN ≪ capacity for RS-solvable regime.
- Mean-field effective field: ĥ^a_i = J^(P) convolution within module − (λD/2) J^(D) cross-module + θ h^a_i.

## Related

- Extends: pairwise disentanglement [Agliari et al., Physica A 2025], multi-channel BAM [Fachechi et al.]
- Dense Hopfield lineage: Krotov-Hopfield (DAM), Demircigil et al., Lucibello-Mézard exponential capacity
- Acknowledged Dmitry Krotov for discussions. Open: RSB saturated regime, learned (non-Hebbian) coupling representations, formal crypto analysis.
