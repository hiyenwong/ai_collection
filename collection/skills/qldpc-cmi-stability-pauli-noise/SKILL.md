---
name: qldpc-cmi-stability-pauli-noise
description: Use when testing mixed-state phase stability of qLDPC codes.
category: ai_collection
arxiv_id: "2610.22357"
source_paper: "Stability of Quantum LDPC States under Local Pauli Noise (Yang, Kim, Vijay, Lee — UIUC/KIAS, 2026)"
---

# qLDPC CMI Stability under Local Pauli Noise

Use when analyzing whether qLDPC code states (as mixed-state phases) remain stable under local noise, or when applying conditional-mutual-information (CMI) decay as a phase diagnostic. From arXiv 2610.22357.

## Core Thesis

The normalized code-projector state ρ0 = PC/Tr PC of a Zd qLDPC stabilizer code is **exactly Markov** (I(A:C|B)=0 for any separating full tripartition) — but local Pauli noise induces nonzero CMI. The paper proves the noise-induced CMI decays **exponentially with buffer width**, independent of system size, in TWO complementary regimes with distinct mechanisms that bracket the decoding transition:

| Regime | Mechanism | Requirement | Toric-code X-dephasing range |
|--------|-----------|-------------|------------------------------|
| Weak noise (Thm 1, error-cluster bound) | A–C correlations need an error cluster crossing the buffer — exponentially unlikely | α < 0.2 where α = e^(Dw)·max_g Σ q_i(u)q_i(u+g) | p < 0.029 |
| Strong noise (Thm 2, information-percolation bound) | Buffer retains little info; correlations persist only along chains of still-informative buffer qudits | buffer supports no logical operator + local-normalizer completeness | p > 0.146 |

Grey uncovered region includes the Nishimori critical point pc ≈ 0.109 — the Markov length is expected to diverge near the decoding transition, analogous to correlation length at pure-state criticality.

**Toric-code thresholds (Corollary D.1, verified numerically)**: weak-noise decay condition is 6·√(p(1−p)) < 1, i.e. p < p_EC = (3−2√2)/6 ≈ 0.0286 (path-count: 4·3^(m−1) dual paths of length m, each weighted (2√(p(1−p)))^m → geometric decay iff 6√(p(1−p))<1). Strong-noise: (1−2p)² < 1/2 → p > (1−1/√2)/2 ≈ 0.1464 (noisy-link contraction coefficient vs square-lattice bond-percolation critical density 1/2). The general Theorem-1 α-bound is far cruder (toric: p < 5×10⁻⁶); the generic percolation path count would need 3(1−2p)²<1, i.e. p > 0.211. ⚠️ When transcribing from PDF, the radical in 6√(p(1−p)) is easily dropped by pdftotext — 6p(1−p)<1 gives the WRONG threshold 0.211.

## Setup Definitions

- qLDPC code: each check acts on ≤ w qudits; each qudit in ≤ D checks. **Interaction graph**: qudits as vertices, edge when two qudits share a check. dist(R,R')_B = shortest path through buffer B.
- Noise: independent onsite Pauli channels N_i with probabilities q_i(u), u ∈ Z_d². Uniform depolarizing: q(0)=1−p, q(u)=p/(d²−1).
- **Stabilizer-syndrome variable** Σ̂_R = χ_E|S(R): the commutation phases of the random error E against ALL stabilizers supported in R (S(R) can be strictly larger than checks supported in R — products of checks extending outside R may cancel).
- Key identity (Eq. 9): S((N_B(ρ0))_R) − S((ρ0)_R) = H(Σ̂_R) — entropy gained under noise = Shannon entropy of the stabilizer-syndrome distribution. Averaging over errors yields an orthogonal mixture of stabilizer sectors with the same maximally-mixed logical block.
- Weak-noise contraction coefficient for depolarizing: α = e^(Dw)·[2p(1−p)(d²−1) + (d²−2)p²]; decay rate c0 = ½·log(1/α); CMI ≤ 3e·c0·D²·(|∂B_A|+|∂B_C|)²·log d · e^(−c0·dist(A,C)_B).

## Proof Pattern (reusable for stability claims)

1. **Data-processing reduction**: I(A:C|B)_{N(ρ0)} ≤ I(A:C|B)_{N_B(ρ0)} — strip noise on A and C, reducing dependence to boundary sizes |∂B_A|, |∂B_C|.
2. **Syndrome reduction**: CMI of the noisy state equals a CMI of syndrome variables: I(A:C|B) = I(Σ_bulk,A : Σ_bulk,C | Σ̂_B). Mixed-state entanglement question becomes a classical correlation question about error configurations.
3. **Cluster/percolation probability bound**: in the surviving regime, bound the probability that an informative chain crosses the buffer by exp(−c·width).
4. **Recovery corollary**: small CMI ⇒ approximate quantum Markov property ⇒ quasi-local Petz recovery. On finite-d lattices of size n: constant-layer quasi-local Petz map of range O(poly(log n)/ε) recovering the state within trace distance ε. Note: the CMI bounds apply to general qLDPC graphs, INCLUDING geometries where constant-depth recovery need not exist — CMI decay is the more general criterion.

## Applications

- **Toric code phase diagram** (Fig. 2): rigorous exponential CMI decay for p < p_EC ≈ 0.0286 (cluster) and p > p_IP ≈ 0.1464 (percolation), bracketing the Nishimori point pc ≈ 0.109. X-dephasing splits the classical record into independent X/Z sectors; only the noisy X sector contributes (noiseless Z-sector CMI vanishes by the reference Markov condition).
- **Levin–Wen topological entropy robustness**: under space-uniformity assumption, topological entropy of the noisy code state is stable — the standard entanglement diagnostic survives noise in provable regimes.
- **Mixed-state phase classification**: CMI decay + two-way local connectivity defines equivalence classes; this paper supplies the missing "fixed points are stable" leg for Pauli noise.

## Caveats & Boundary Conditions

- Full-system tripartition A⊔B⊔C=Λ at weak noise: unconditional. **Sub-system tripartitions have a counterexample** — LDPC conditions alone are insufficient; need space-uniformity.
- Strong-noise bound requires the buffer to support NO logical operator, plus local-normalizer completeness — not automatic for all codes/partitions.
- Bounds are non-constructive about the critical region; numerics (prior work) suggest divergence of Markov length near the transition.
- Syndrome-variable decomposition is Pauli-specific; generalizing to non-Pauli noise needs different syndrome structure.

## When Applying This Skill

- Certifying that a qLDPC code's encoded structure is a stable mixed-state phase (not just a fine-tuned state) under a given noise model — check α against the 0.2 threshold first.
- Choosing CMI (not correlators or entropy alone) as the diagnostic when proving mixed-state phase equivalence.
- Deriving quasi-local recovery guarantees for noisy code states on non-local qLDPC geometries.
- Estimating which noise regimes are provably safe vs provably information-destroyed for a code+partition, leaving the decoding transition as the analytic grey zone.

## Related

- `non-isometric-qec-theory` — general non-isometric QEC framework.
- `homological-percolation-monitored-qec` — complementary percolation thresholds for monitored codes.
- `recoverability-collapse-information-decoders` — CMI/recoverability in self-referential settings.
