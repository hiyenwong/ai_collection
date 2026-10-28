---
name: private-capacity-superactivation
description: Two zero-private-capacity channels jointly send private bits (arXiv 2609.10520).
category: ai_collection
---

# Private-Capacity Superactivation via Joint Use of Zero-Capacity Channels

**Source**: Zhu & Wang, "Private communication via zero-private-capacity quantum channels", arXiv:2609.10520 (Sep 2026). Resolves a longstanding open problem (QIP 2009): two channels with **zero** private capacity can jointly achieve positive private communication. Lean 4-formalized (Mathlib + Lean-QIT).

## Core Result

- **Channel N**: 4-level channel (A=B=C⁴, Kraus: diagonal D=diag(1,−4,4,−1) + three transition pairs A₁,A₂,A₃ with weights (4,12,31)/56, identity branch weight 1/7). Zero private capacity via **transpose-antidegradability**: ∃ CPTP map 𝒟 with 𝒟∘N^c = T_B∘N (conjugate-simulation certificate). Data processing ⇒ χ(Bob) ≤ χ(Eve) at every blocklength ⇒ P(N)=0.
- **Helper**: qubit erasure channel E_{2,p}, p ≥ 1/2 (antidegradable ⇒ zero private capacity).
- **Theorem 1**: P(E_{2,p} ⊗ N) ≥ 6·ln2·(1−p)² / (49·(27+169p)) > 0 for all 1/2 ≤ p < 1. At p=1/2: ≈ 1.903×10⁻⁴ private bits per product use.
- Impossible for classical memoryless wiretap channels (classical wiretap capacity is additive) — a purely quantum phenomenon.

## Reusable Encoding Pattern: Weak Signal in Mixed Background

Three orthogonal directions: background span{u₀,u₁} + signal w (all detect the 7 non-identity errors: P_S(I⊗L)P_S = 0).

1. **Letters**: ρ₀ = ½(|u₀⟩⟨u₀|+|u₁⟩⟨u₁|) (background, prob 3/4) and ρ_t = (1−t)ρ₀ + tρ₁ (diluted signal, prob 1/4), ρ₁=|w⟩⟨w|. Helper marginal identical for both letters (helper alone carries no info).
2. **Bob's advantage — linear**: fixed binary measurement {|w⟩⟨w|, I−|w⟩⟨w|} on the product output. Click ⇒ U=1 with certainty. I(U:Y) ≥ ½·a_p·t with a_p=(1−p)/7 — **linear in signal strength t**.
3. **Eve's leakage — quadratic**: support containment ϵ₁ ⪯ (205/9)ϵ₀ (background fills Eve's relevant support; invertibility on support gives finite c in ω₁⪯cω₀) + **Classical Coin Bound** (Lemma 2): if ω₁ ⪯ cω₀ (c≥3), the ¾/¼ ensemble with ω_t=(1−t)ω₀+tω₁ has χ ≤ 3(c−1)t²/(32 ln 2) — **quadratic in t**, no commutativity required. Proof: decompose ω_s = r_s ω₁ + (1−r_s)τ with τ=(cω₀−ω₁)/(c−1) ⪰ 0, then data-processing bounds χ by the coin's classical mutual information; entropy curvature −f''(s) ≤ (c−1)/ln2 on s∈[0,½].
4. **Rate extraction**: gap I(U:Y) − χ(U:E) ≥ a_p t/2 − 3κ_p t²/(32 ln 2); maximize by t = 8a_p ln2/(3κ_p) → positive rate. The fixed measurement per use + classical wiretap coding across uses completes the protocol.

**Generalization recipe** (§5): whenever (i) a receiver event has zero background probability but positive signal probability, and (ii) Eve's signal support ⊆ background support (making c = max{3, ‖ω₀^{-1/2}ω₁ω₀^{-1/2}‖_∞} finite on support), the same linear-vs-quadratic argument certifies privacy for mixed letters.

## PPT/LOCC Impossibility (Proposition 3)

If N admits transpose simulator 𝒟N^c = T_B₁N and A is antidegradable, then any decoder whose effects stay positive under partial transpose across the two output groups (includes all separable/LOCC decoders) satisfies ε + δ ≥ 1 − 1/M at every blocklength. The winning measurement |w⟩⟨w| has partial-transpose eigenvalue −½ — **entanglement across the product outputs is essential**; privacy comes from the joint measurement per use (classical coding suffices across uses).

## Structural Insights

- **Capacity ≠ value**: a channel's private capacity alone does not determine its worth for secure communication — regularization over joint uses can unlock hidden value.
- Separates **degradability from the regularized less-noisy order**: N's complement dominates in Holevo info at all blocklengths yet N is not antidegradable (else it couldn't activate).
- Counterpoint (Ref. [23]): a qutrit zero-private channel whose complement dominates *with arbitrary quantum reference* tensorizes and cannot be activated — information domination alone, without the reference, does not give stability.
- **AI-assisted discovery**: initial activation example found through LLM interaction (QudeLeap AI Quantum Scientist), then human-verified and Lean 4-formalized — a working human+AI methodology for open-problem search in quantum information.

## Applications / Triggers

- Use when: analyzing private capacity, wiretap codes, channel superactivation/nonadditivity, transpose-antidegradable channels, antidegradable helpers, PPT decoder bounds, zero-capacity channel combinations, Lean formalization of quantum Shannon results, LLM-assisted theorem discovery.
- Keywords: private capacity superactivation, zero private capacity, transpose antidegradable, erasure channel helper, classical coin bound, signal dilution, weak signal encoding, PPT decoding bound, private bits, quantum wiretap.

## Related Skills

- `sharp-pairwise-reduction-pgm-hypothesis-testing` — PGM hypothesis testing bounds
- `measurement-free-quantum-error-correction` — other zero-capacity channel tricks
- `almost-iid-quantum-information` — robustness of asymptotic info-theoretic exponents (companion skill, arXiv:2609.17309)
