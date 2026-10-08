---
name: guarded-coherent-two-party-qdp
description: Use for quantum two-party DP and guarded coherent protocols.
category: ai_collection
trigger: two-party differential privacy, quantum communication advantage, Hamming distance privacy, guarded coherent round trip, equal-Gram rigidity, Klauck honest model, hockey-stick divergence QDP, multiparty quantum privacy, quantum differential privacy protocol
arxiv_id: "2610.02113"
published: "2026-10-01"
---

# Guarded Coherent Two-Party Quantum Differential Privacy

**Paper**: "Quantum Advantage for Two-Party Differential Privacy" — Daniel Alabi, Emil T. Khabiboulline (UIUC / NIST-UMD), arXiv:2610.02113, 1 Oct 2026.

## Core Result

First information-theoretic quantum protocol that crosses the classical two-party DP accuracy barrier for Hamming distance. In Klauck's honest, nonpreemptive, message-preserving (KHNP) model:

- **Classical info-theoretic** (McGregor et al.): Ω(√n) error under pure DP; Ω(√n/log n) under strong approximate DP
- **Quantum protocol (this paper)**: O(1) expected error — `E|d̂ − d| < 2/sinh ε + γ` — with pure ε-QDP and O(n) communication, NO computational assumptions, trusted setup, prior entanglement, or bounded storage
- Quantum communication recovers exactly the accuracy classically available only under computational security

## Methodology Components

### 1. Ideal common-output functionality (the DP core)

For inputs x, y ∈ {0,1}ⁿ, d = HD(x,y), fix odd modulus m = 4n+1 with circular metric d_m(a,b) = min{[a−b]_m, [b−a]_m}. The cyclic-geometric noise distribution:

```
q_α(g) = exp[−α·d_m(g,0)] / Σ_h exp[−α·d_m(h,0)]
```

Alice samples A ~ q_ε, Bob samples B ~ q_ε independently; the functionality releases Z = d + A + B (mod m). Both parties decode with the interval decoder Dec(z) = min argmin_{r∈{0..n}} d_m(z, r).

- Privacy: adjacent inputs (1 bit flip → d changes by ≤1) give likelihood ratio ∈ [e^{−ε}, e^ε] → pure ε-DP for BOTH views
- Accuracy: E|d̂−d| ≤ 2/sinh ε (factor 2 from both noise shares; circular distance is 1-Lipschitz; interval decoding never adds error)
- Why circular: the wrap-around on Z_m keeps the geometric noise full-support, avoiding infinite max-divergence from support mismatch

### 2. Guarded coherent round trip (the quantum realization)

Alice prepares a superposition with a small input-INDEPENDENT guard branch:

```
|ψ_{x,A}⟩ = √(1−κ)|0⟩_C|x,A⟩_M + √κ|1⟩_C|⊥⟩_M,   κ = γ/(n+γ)
```

Bob coherently computes the noisy release into a residue register and returns the ENTIRE state:

```
|ϕ⟩ = √(1−κ)|0⟩|x,A⟩|HD(x,y)+A+B mod m⟩ + √κ|1⟩|⊥⟩|z⊥⟩
```

Alice measures branch+residue registers, broadcasts the classical residue Z; both output Dec(Z). Error budget: (1−κ)·(2/sinh ε) + κ·n < 2/sinh ε + γ. Discrete variant uses K = 2^k branches (Hadamard-prepared, κ = 1/K) when exact rotations are unavailable.

### 3. Equal-Gram rigidity (the privacy mechanism)

**Claim 1 (no-information principle)**: If pure-state families {|u_i⟩}, {|v_i⟩} satisfy ⟨u_i|u_j⟩ = ⟨v_i|v_j⟩ ≠ 0 (i≠j) and a CPTP map sends each |u_i⟩⟨u_i| → pure |v_i⟩⟨v_i|, then the complementary (retained) output state is INDEPENDENT of i.

Proof sketch (Stinespring): W|u_i⟩ = e^{iθ_i}|v_i⟩|e_i⟩ forces ⟨e_i|e_j⟩ = e^{i(θ_i−θ_j)}·⟨u_i|u_j⟩/⟨v_i|v_j⟩ = phase — all complementary states identical.

**Why it matters**: classical honest-but-curious players copy every message without disturbance (transcript factorization p(t|x,y) = a_t(x)·b_t(y) — the root of the McGregor lower bound). Non-orthogonal quantum messages CANNOT be copied while returning the prescribed state — the action that is automatic classically is physically impossible quantumly.

### 4. Exact hockey-stick calibration for approximate DP

For (ε,δ)-QDP, don't waste the δ-budget: compute the exact hockey-stick divergence of the finite cyclic-geometric distribution. The likelihood ratio between adjacent shifts takes only values {1, e^α, e^{−α}}, so:

```
Δ_{n,ε}(α) = (1 − e^{ε−α}) · (1 − e^{−2nα}) / (1 + e^{−α} − 2e^{−(2n+1)α})
```

Δ is continuous and strictly increasing from 0 at α=ε to 1 as α→∞, so every δ determines a unique α* > ε with Δ(α*) = δ. Running the same protocol with q_{α*} noise gives error ≤ 2/sinh(α*) + γ — strictly smaller than 2/sinh ε. The equal-Gram argument is α-independent, so the improvement lifts for free.

## Boundary of the Advantage (critical for honest claims)

| View model | Privacy | Result |
|---|---|---|
| PC (prescribed-channel) | pure ε | Prop 6: EXACT classical reversible realization exists — no separation possible |
| KHNP (Klauck-honest) | pure ε | Thm 7: quantum, error < 2/sinh ε + γ, O(n) comm |
| KHNP | (ε,δ) | Thm 8: error ≤ 2/sinh(α*) + γ, strictly better |
| Classical KHNP | pure+approx | Cor 9: Ω(√n) / Ω(√n/log n) — separation is same-model |
| RR (retention-robust, malicious) | pure ε | Thm 10: quantum protocol BREAKS (measure-and-abort distinguishes adjacent inputs); classical randomized response n/(2 sinh(ε/2)) + 1/(2 sinh²(ε/2)) matches McGregor accuracy |

The advantage is specific to the exact message-preserving honesty condition. Under fully malicious security the question remains open.

## Reusable Patterns

1. **Guard-branch pattern**: embed a small input-independent fallback branch (probability κ) in a coherent encoding to make approximate rigidity EXACT — the approximation cost moves entirely into a rare event affecting only accuracy (κ·n), never privacy
2. **Equal-Gram no-information lemma**: for privacy proofs of quantum protocols — prescribe returned states with a Gram matrix equal to the sent states, and non-orthogonality (constant overlap κ > 0) forces retained information to be input-independent
3. **Dual-noise-share construction**: both parties independently sample noise from the same DP distribution and the release is the mod-sum — this enforces common-output DP against both views simultaneously
4. **Circular-geometric noise on Z_m**: full-support, finite-cycle variant of geometric noise with exact hockey-stick divergence in closed form — use whenever a DP mechanism needs finite-support noise with tight (ε,δ) calibration
5. **Model-aware claims**: always state which adversarial view model (PC/KHNP/RR) a quantum privacy advantage holds in — the separation can vanish or invert across models

## Application Domains

- Privacy-preserving similarity/matching (Hamming distance = edit-distance-1 bounded metric): private record linkage, biometric matching, genomic distance
- Distributed DP without trusted curator where quantum channels exist (QKD-adjacent infrastructure)
- Fundamental studies: non-copyability of quantum information as a privacy resource; connection to communication-complexity lower bounds

## Key Formulas

- Pure QDP error: `E|d̂−d| < 2/sinh ε + γ`, communication `2n + O(log n)`
- Guard probability: `κ = γ/(n+γ)` (continuous) or `1/K, K = 2^k ≥ max{2, n/γ}` (discrete/Hadamard)
- Approximate calibration: unique `α* > ε` s.t. `Δ_{n,ε}(α*) = δ`; error `≤ 2/sinh(α*) + γ`
- Classical RR baseline (RR model): `n/(2 sinh(ε/2)) + 1/(2 sinh²(ε/2))`

## References
- arXiv:2610.02113 — Alabi & Khabiboulline, "Quantum Advantage for Two-Party Differential Privacy"
- McGregor, Mironov, Pitassi, Reingold, Talwar, Vadhan — classical two-party DP lower bounds
- Klauck — honest, nonpreemptive, message-preserving quantum communication model
- Related skills: qdp-quantum-differential-privacy (DP-SGD for QML), entanglement-quantum-differential-privacy, predictability-privacy-framework