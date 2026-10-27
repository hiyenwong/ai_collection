---
name: physics-of-deep-learning-and-brains
description: Quasi-criticality links learning in deep nets and brains.
trigger: crackling noise, neuronal avalanches, deep avalanches, quasi-criticality, edge of chaos, Widom line, susceptibility, universality class, Barkhausen noise, directed percolation, finite-size scaling, avalanche exponents, branching ratio, initialization, trainability, brain criticality, deep learning physics, mean-field theory, tanh network, scaling relations, shape collapse
category: ai_collection
---

# Toward a Physics of Deep Learning and Brains — Crackling-Noise Quasi-Criticality

Source: arXiv:2509.22649v2 (Ghavasieh, Vila-Miñana, Khurd, Beggs, Ortiz, Fortunato — Indiana U Bloomington; cond-mat.dis-nn, v1 26 Sep 2025, v2 19 Oct 2026. Code: github.com/ArshamCS/DNN_criticality). An event-resolved non-equilibrium framework showing deep networks and living brains share avalanche physics: both learn best in a quasi-critical regime, and maximal susceptibility — not proximity to the edge of chaos — predicts trainability.

## Why it matters

- Resolves the long-standing puzzle that networks ON the edge of chaos often train poorly: the edge of chaos (diverging cross-input correlation depth) and the susceptibility peak are DIFFERENT curves that meet only at exact criticality (σ_w², σ_b²) = (1, 0). Trainability tracks the Widom-like line of maximal σ_w-susceptibility.
- First crackling-noise analysis of deep avalanches: size/duration power laws, exponent scaling relation, and universal shape collapse hold in Gaussian nets — with exponents in the Barkhausen universality class; ResNets land in the mean-field directed percolation class.
- Both brains and DNNs are strongly driven, so neither can sit at a true critical point — quasi-criticality ("as critical as possible") is the correct regime, and the crackling toolkit gives operational diagnostics (exponent-relation mismatch, collapse quality) for steering architectures.

## Core framework

1. **Mean-field propagation.** Gaussian tanh net, width N, depth L: z^ℓ = W^ℓ y^ℓ + b^ℓ, y^{ℓ+1} = tanh(z^ℓ), W ~ N(0, σ_w²/N), b ~ N(0, σ_b²). Signal strength evolves by q_{ℓ+1} = σ_w²·E[tanh²(√q_ℓ ξ)] + σ_b², ξ ~ N(0,1) (Schoenholz-style recursion).
2. **Critical point and exponents.** (σ_w², σ_b²) = (1, 0) is a genuine absorbing-state transition: for σ_w² ≤ 1, q → 0 (verified: exponential decay at 0.9/0.99; algebraic marginal decay at exactly 1 — still 2.5e-6 after 200k iterations). Order parameter q_ss ~ (σ_w²−1)^β with β = 1 and σ_w-susceptibility χ = d√q_ss/dσ_w² ~ (σ_w²−1)^{−1/2} (σ = 2) — MF directed percolation exponents (verified numerically: asymptotic slopes 1.02 and −0.47 over σ_w²−1 ∈ [0.02, 0.12]).
3. **Bias = external field.** σ_b² > 0 destroys the absorbing state and rounds the transition: q*(σ_w²=1) ∝ √σ_b² (verified: q*/√σ_b² ≈ 0.71–0.78 across 1e-4..1e-2), and the critical point is replaced by a finite susceptibility ridge.
4. **Widom-like line vs edge of chaos.** Edge of chaos = locus of diverging cross-input correlation depth ζ_c (δ^ℓ ~ e^{−ζ_c}); points on it are poorly trainable except at very small σ_b². The Widom-like line = locus of maximal χ_σw²; it departs from the edge of chaos for σ_b² > 0 and vanishes as σ_b² grows. Trainability onset overlaps the Widom ridge: Pearson 98% (MNIST) / 99% (CIFAR-10) between susceptibility-peak loci and onset of trainability; 83% / 58% between log susceptibility height and width of the trainable region.
5. **Deep avalanches.** Threshold = input signal strength √q_0. Duration D = number of layers with q_ℓ above threshold; size S ∝ Σ_{ℓ≤D} (√q_ℓ − √q_0); rescale S → N·S to align input-per-neuron. Hallmarks checked: P(S) ~ S^{−τs}, P(D) ~ D^{−τd} (3+/2+ decades), ⟨S⟩_D ~ D^γ, crackling relation **γ = (τ_d − 1)/(τ_s − 1)**, and shape collapse of rescaled profiles (D on layer axis, D^{γ−1} amplitude).
6. **Input magnitude is a second drive parameter.** √q_0 shifts the susceptibility peak to larger σ_w² (best power laws at 1.005 / 1.025 / 1.05 for √q_0 = 0.1 / 1 / 1.7) while barely touching exponents — standardized data (√q₀ ≈ 1) is one more reason exact criticality is unreachable.

## Key results

- **Gaussian nets (L=3000, N up to 1000, ~4×10⁶ avalanches, re-init every 5000 perturbations):** γ_fit = 1.5303 (N=1000), shape-collapse γ* = 1.58, relation prediction 1.5883. Finite-size extrapolation τ(N) = τ + cN^{−w} gives (τs, τd) → (1.34, 1.53) — matching Barkhausen noise (models 1.34/1.55; experiments 1.33±0.05, 1.50±0.07). Relation re-check with quoted exponents: (1.53−1)/(1.34−1) = 1.559 ✓. Weight variance tuned slightly above 1 (δσ_w² = 0.001–0.03 by width) to compensate finite-size effects.
- **Learning landscape (N=L=300, MNIST 10 epochs; also CIFAR-10):** accuracy peaks on the heightened-susceptibility region; as σ_b² grows the trainable region narrows, shifts to larger σ_w², and at σ_b² = 10^{−2.2} disappears. Trainable width grows with N and hugs σ_w² → 1 (finite-size trend). Depth 200–500: criticality matters MORE for deeper nets.
- **ResNets (18/50/152):** avalanche distributions are power laws with exponents clustering across variants and thresholding n = 0..3; γ ≈ 2 — the MF directed percolation line (check: (2−1)/(1.5−1) = 2.00 ✓). Order parameter S̃_z = Σ√q_ℓ/σ_total (per-config fluctuation normalisation, Eq 9), control parameter = BatchNorm affine scale γ: sharp transition at γ ≈ 1 with susceptibility χ_γ = ΔS̃_z/Δlog₁₀γ peaking there — precisely the onset of the successful-training range (performance degrades for γ > 1 and very small γ). BatchNorm acts as a tunable criticality knob.
- **Shared physics with brains:** the same battery (power-law sizes/durations, exponent relation, shape collapse) is the standard for neuronal avalanches (Beggs–Plenz; quasi-criticality of Williams-García/Fosque/Beggs/Ortiz); deep learning inherits it because both systems pass information as cascades through processing stages and need neither attenuation nor saturation at the far end.

## Practical playbook

- **Diagnostics:** track exponent-relation mismatch γ vs (τ_d−1)/(τ_s−1), collapse quality, and susceptibility peaks as distance-from-criticality meters during development/training pipelines.
- **Knobs as control parameters:** dropout, spectral constraints, batch normalization, injected noise, residual depth — tune by their effect on the susceptibility landscape; regularizers can bias training toward the quasi-critical plateau.
- **Universality-class steering:** task performance is predicted to differ between criticalities {τs, τd, γ} (Barkhausen vs MF DP here) — a design axis for architectures, not just a descriptor.
- **Caveats:** analysis is at initialization (training introduces characteristic scales; trained nets plausibly leave criticality except in subspaces); finite sizes and subsampling complicate exponent estimation (use ML fits + finite-size extrapolation); observables beyond pre-activations unexplored.

## When to use

- Deciding initialization scales σ_w²/σ_b² for very deep nets — place on the Widom-like line, not the edge of chaos; expect finite-size shift of the trainable window with width.
- Diagnosing untrainable deep stacks via avalanche/crackling statistics instead of (or alongside) Lyapunov/branching proxies.
- Bridging neuronal-avalanche/critical-brain literature with deep learning theory: shared crackling framework, quasi-criticality, external-field analogies (σ_b² ↔ spontaneous activation p_s ↔ input drive √q_0).
- Universality-class identification and finite-size-scaling analysis of activity cascades in any layered feedforward system.
