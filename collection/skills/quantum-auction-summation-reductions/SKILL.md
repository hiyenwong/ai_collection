---
name: quantum-auction-summation-reductions
category: ai_collection
description: Reductions between quantum auctions and secure summation.
trigger: quantum auction, quantum summation, secure multi-party computation SMC, sealed-bid auction protocol, exponential race, threshold disjunction, auctioneer-free auction, amplitude estimation summation, composite key search
---

# Quantum Auction ↔ Secure Summation Mutual Reductions

Based on Sandhu, Mishra & Pathak (arXiv:2606.27693v2, Oct 2026). For single-item first-price sealed-bid auctions with scalar bids, quantum auction protocols and secure multi-party summation (SMC) are **mutually reducible** — they share one operational structure (summation oracles over threshold indicators). Use this skill when designing, analyzing, or breaking quantum auction/summation/e-commerce SMC protocols.

## Direction 1 — Auction as Black Box → Secure Sum

Each party P_i holds private integer x_i ∈ {0,…,X}; goal is S = Σx_i.

**Exponential race key construction** (the core trick):
1. P_i draws fresh private U_i ~ Uniform(0,1)
2. Key: K_i = U_i^(1/x_i) for x_i ≥ 1; K_i = 0 for x_i = 0
3. Bid: b_i = ⌊B·K_i⌋ into bid space {0,…,B-1}
4. Auction announces clearing price p = max b_i (first-price, winner identity NOT published)

**Threshold law (Lemma 1)**: Pr[p < m] = (m/B)^S exactly. The clearing-price distribution depends on inputs ONLY through S. (−ln K_i is exponential with rate x_i; max key = min of exponentials = exponential with rate S.)

**Estimator**: for threshold m, c = −ln(m/B), q̂ = fraction of M rounds with p < m:
`Ŝ = round(−ln(q̂) / c)`, clipped to [0, S_hi], Ŝ = S_hi if q̂ = 0.

**Two-stage protocol Π_race** (public params S_hi = NX, B, failure δ):
- Scale stage: J = ⌈log2 S_hi⌉+1, M1 = ⌈14·ln(4(J+1)/δ)⌉ rounds; thresholds m_j = ⌊B·e^(−2^j)⌋; pick smallest j with q̂_j ≥ 0.335 → S̃ = min(2^(j*+1), S_hi)
- Resolution stage: M2 = ⌈52·S̃²·ln(4/δ)⌉ rounds at m = ⌊B·e^(−1/S̃)⌋ → output Ŝ

**Complexity**: O(S² log(1/δ)) auction rounds — OPTIMAL for independently sampled bids (Theorem 3). Coherent access (amplitude estimation on the auction unitary) drops to O(S log(1/δ)). Requires B ≥ 32e·S_hi. Private randomness is necessary.

**Hard pitfalls**:
- Publishing winner identity reveals EVERY input (Proposition 2) — only clearing price is safe
- Second-price auctions do NOT work: their threshold law depends on individual inputs, not just S
- Sum itself necessarily leaks nonzero info about each input (unavoidable residual)

## Direction 2 — Summation → Auction (Composite Key Search)

**Composite keys**: κ_i = B_max·b_i + π(i), where π is a public random injection breaking ties. Keys take values in {0,…,B_max·N−1}.

**Threshold disjunctions**: define f_t(i) = 1[κ_i ≥ t]. Winner/price determination = search over thresholds using only summation-oracle evaluations of these indicators. L = ⌈log2(B_max+1)⌉ + ⌈log2 N⌉ levels: first ⌈log2(B_max+1)⌉ locate the price, next ⌈log2 N⌉ break ties via π.

**Two query primitives** (both verified on 156-qubit ibm_kingston Heron):

1. **Disjunction query (leakage-minimal)**: register of d = |G| dimension (G = Z_4 demo). QFT prepares uniform superposition; every bidder with κ_i ≥ t adds independent uniform z_i ∈ Z_d via phase gates; inverse QFT returns Σz_i mod d. Query positive iff any round nonzero (6 rounds, 128 shots, miss prob 4^−6). Reveals ONLY that some key reaches t, not how many. **Requires Fourier-basis coherence across all bidders** — dephased control fails uniformly (verified).

2. **Sampling query**: uniform superposition over bidder indices + ancilla flipped for κ_i ≥ t; Pr[anc=1] = S_t/N. Positive if frequency > 1/(2N); O(N) shots. **LEAKS the count S_t** — a count-revealing search transcript determines the entire key histogram = whole bid vector up to bidder labels. No coherence needed; photonic linear-optical sampler suffices.

**Re-encoding attack**: each query consumes bidders' quantum encodings, so bidders must re-encode after observing intermediate outcomes — a bidder can adapt its effective bid on the fly UNDETECTED. **Fix**: fixed query set (batch all 2L−1 thresholds), restoring sealed bidding at cost O(B_max·N) summations. Binding adaptively requires computational/relativistic assumptions (info-theoretic quantum bit commitment impossible).

**Randomized inputs are essential**: bidders add fresh random z_i so positive queries leak nothing beyond the disjunction bit.

## Instantiation + Published-Protocol Vulnerability

Black-box instantiation: auctioneer-free quantum auction of Shi & Li. **Their disjunction subroutine as published leaks occupancy counts** — a one-line label-rule modification is REQUIRED, and this is a measured hardware counterexample to their Theorem 5: with published labels, public value never = 00 for m=1 but = 00 in 31.7% of rounds for m=2 → a party seeing 00 learns ≥2 others hold 1. After modification the law is uniform (TVD 0.13 ≈ sampling noise).

When reusing ANY existing quantum auction as the black box, check its disclosure variant: F_price (no winner disclosed) works; winner-notified-privately adds O(log S_hi) register cost; publicly-announced winner breaks the reduction entirely.

## Complexity Summary

| Method | Invocations | Notes |
|---|---|---|
| Auction→Sum, sampled | Θ(S² log(1/δ)) | optimal for independent bids |
| Auction→Sum, coherent | O(S log(1/δ)) | amplitude estimation |
| Sum→Auction, adaptive exact | L summations | O(N·L) bidder ops |
| Sum→Auction, sealed (fixed set) | 2L−1 | O(B_max N²) bidder ops |
| Sum→Auction, amplitude est. | O(L^(3/2)·N/δ) | quadratic speedup |
| Sum→Auction, sampling | O(L·N·log(L/δ)) | leaks counts |
| Quantum maximum finding | O(√N) | compares bids pairwise — forbidden here |

**Not cost-preserving**: composing the two reductions multiplies overheads. The result is STRUCTURAL — it transfers protocols, security proofs, and hardware demonstrations between the two task classes, not efficiency.

## Hardware Demo Reference Points (ibm_kingston, no error mitigation)
- N=4 bidders, bids {0..3}, β=ν=2, L=4; 5 bid vectors (3 with ties), 615 circuits, 145,920 shots
- Disjunction circuits: depth 29–34, six 2-qubit gates; deviation from ideal sum 4.7% avg / 10.2% max; ideal sum still most-frequent in all 450 rounds; positive-query outcomes uniform on Z_4 (χ²=1.1, 3 dof)
- Sampling: ≤0.49% freq for negative, ≥24.1% for positive (decision level 12.5%); counts exact in all 75 queries
- Sum-from-auctions: 470 auctions, 2874 Bell-pair rounds (2N qubits, depth 17, seven 2q gates, 16 shots/round majority vote); per-shot parity error 12.4% (2 parties) / 16.7% (3) yet majority correct in all 3354 rounds; ML 95% CIs [0.00,0.06], [0.75,1.08], [1.84,2.58], [3.98,5.66] for true S = 0,1,2,4 — all contain truth
- Photonic realization: sampling query needs only low-loss routing + detector efficiency; disjunction query needs phase stability across ALL bidders (the real obstacle)

## Scope Limits (do not extrapolate)
- Single item, scalar bids, linear order, first-price payment ONLY
- Combinatorial auctions (set-function valuations, NP-hard winner determination, exposure problem) — NOT reducible; use Hogg-Harsha-Chen adiabatic protocol for bundles
- Malicious adversaries, device independence, hardware side channels — out of scope (semi-honest collusion model only)
- Coherent reduction (Prop 5) has NO privacy proof yet (specious adversaries open)
- Whether correlated randomness can beat S² round complexity — open

## Reuse Checklist
1. Identify which direction your task needs (aggregate statistics ↔ price+winner)
2. Verify disclosure variant of the auction building block BEFORE composition
3. Add randomized inputs (fresh z_i or U_i) at every oracle interaction
4. Choose query primitive by leakage budget: disjunction (coherent HW) vs sampling (leaks counts)
5. For sealed bidding integrity, use fixed query sets — never adaptive without commitments
6. Budget error: amplitude-estimation oracles add union-bound over queries, keep quadratic advantage
