---
name: area-theorems-quantum-error-correction
description: "EXIT/GEXIT area theorems generalized to QEC: coset-entropy formalism for nested codes C2⊆C1 (area = normalized quotient dimension); for any [[n,k]] stabilizer code the quantum GEXIT area = 2k (k/n per channel use); erasure folding identity A_Q(ε)+A_Q(1−ε)=2k gives converse R≤1−2ε matching quantum erasure capacity; depolarizing converse R≤[(h4(f(p))−h4(p))/2]+ with no positive-rate stabilizer threshold at p≥1/4. Use when bounding stabilizer code rates or linking code rate to optimal syndrome decoding. Activation: EXIT area theorem, GEXIT, coset entropy, stabilizer rate bound, quantum erasure capacity, depolarizing converse, correction-class entropy."
---

# Area Theorems for Quantum Error Correction

Methodology from arXiv:2610.22710 (Mandal, Gökduman & Pfister; Oct 2026). Generalizes the classical EXIT/GEXIT area theorems — conservation laws linking code rate to MAP-decoding performance on binary memoryless channels — to quantum error correction via a coset-entropy formalism for stabilizer codes. All bounds are single-letter and use only classical information quantities.

## Classical Background

EXIT area theorem (BEC/BSC): the area under the extrinsic-information-transfer curve equals the code rate in bits/channel-use. GEXIT (generalized EXIT) extends this to arbitrary binary memoryless channels. These are decoder-independent conservation laws: any optimal-decoder performance curve must enclose the same area.

## Core Construction: Coset Entropy for Nested Linear Codes

Setup: nested linear codes C2 ⊆ C1 ⊆ F_2^n. The **message specifies a coset** of C2 in C1; encoder randomization picks a codeword inside the coset. This is exactly QEC decoding structure: the syndrome pins the Pauli error to a coset of the stabilizer group S in S⊥; the residual freedom is the logical correction class.

Normalized coset EXIT function (BEC, erasure probability ε):

h_{C1/C2}(ε) := (1/n) Σ_{j=1}^n [ H(U_j | E_~j, Y_~j) − H(V_j | E_~j, Y'_~j) ]

Key identities:
- h_{C1/C2}(ε) = (1/n) d/dε A_{C1/C2}(ε)  (derivative of the coset area function)
- ∫_0^1 h_{C1/C2}(ε) dε = dim(C1/C2)/n  (area = normalized quotient dimension)

## Stabilizer Translation

For an [[n,k]] stabilizer code with stabilizer group S and Paulis commuting with it (S⊥):
- The measured syndrome restricts the Pauli error but **does not always determine its logical effect**; the remaining uncertainty is an entropy over logical correction classes.
- That entropy equals a **classical coset entropy** of the nested pair (S, S⊥).
- Depolarizing channel: handled through the joint four-valued (I,X,Y,Z) Pauli-error distribution; per-qubit noise entropy h4(p) := h2(p) + p·log2 3 ∈ [0,2] bits for p ∈ [0,3/4]; normalized GEXIT parameter a(p) := h4(p)/2.

## Key Results

| Theorem | Statement |
|---|---|
| Thm 13 — Stabilizer EXIT area (erasure) | A_Q(0)=0, A_Q(1)=2k; 0 ≤ A_Q(ε')−A_Q(ε) ≤ 2n(ε'−ε) |
| Thm 14 — CSS erasure EXIT | h_CSS(CX,CZ) = ½(h_{CZ/CX⊥} + h_{CX/CZ⊥}); ∫_0^1 h_CSS = k/n. CSS decoding separates into two binary coset-decoding problems |
| Thm 15 — Stabilizer GEXIT area (depolarizing) | G_Q(0)=0, G_Q(1)=2k — holds for **any** stabilizer code |
| Thm 17 — Erasure folding identity | A_Q(ε) + A_Q(1−ε) = 2k, hence γ_Q(ε)=γ_Q(1−ε); from the duality between S and the Paulis commuting with it |
| Thm 18 — Erasure converse | Vanishing logical error at erasure ε∈[0,1/2] ⟹ R ≤ 1−2ε (matches quantum erasure channel capacity) |
| Lemma 20 — Coherent information link | Correction-class entropy connects to coherent information via the complementary channel |
| Lemma 21 — Complementary channel | Tr_{F2}(N_p^c(ρ)) = N_{f(p)}(ρ), f(p) = (3−2p−2√(3p(1−p)))/4; f decreasing, f(1/4)=1/4 |
| Thm 22 — Depolarizing folding inequality | G_Q(a(p)) + G_Q(a(f(p))) ≥ 2k |
| Thm 23 — Depolarizing converse | R ≤ [(h4(f(p)) − h4(p))/2]+; in particular R=0 for p∈[1/4,3/4] |

**No-go consequence**: no positive-rate stabilizer code family has a depolarizing threshold at or above p=1/4.

## Workflow: Applying the Framework

1. Model the physical noise as Pauli noise (erasure; or depolarizing with joint 4-valued distribution).
2. For a candidate stabilizer code: identify S, S⊥. Syndrome decoding = coset decoding of the nested pair.
3. Compute or bound the correction-class EXIT/GEXIT curve; check the area equals k/n per channel use — deviations flag analytic/implementation errors.
4. CSS codes: split into the two binary coset problems (CZ/CX⊥, CX/CZ⊥) and apply classical EXIT machinery to each.
5. Use the folding identity A_Q(ε)+A_Q(1−ε)=2k to halve computation and as a symmetry sanity check on simulated decoder curves.
6. Converse check: a claimed family with rate R and vanishing logical error at noise level p must satisfy R ≤ 1−2ε (erasure) or R ≤ [(h4(f(p))−h4(p))/2]+ (depolarizing). Violation falsifies the claim.

## Why It Matters

- Imports EXIT/GEXIT machinery (the workhorse of turbo/LDPC code design: threshold prediction without full simulation) into QEC as a fast sanity check and design-curve tool for qLDPC/stabilizer families.
- The conservation laws are optimal-decoder-level constraints any practical decoder must respect.
- Reproduces the quantum erasure capacity (1−2ε) and a depolarizing converse from purely classical entropy arguments.

## Pitfalls

- Degeneracy: optimal decoders can succeed on the logical correction class while misidentifying the physical error — all bounds are stated for correction-class error probability.
- GEXIT curves are not the measurable EXIT charts of iterative decoders; they are MAP-decoding conservation laws (a related but distinct object).
- The p≥1/4 zero-rate converse applies to stabilizer families; it does not rule out non-stabilizer schemes (approximate/covariant codes).

## Related Skills

- mld-quantum-decoding — MAP/ML decoding framework the area theorems constrain
- bf-osd-qldpc-decoding, lottery-bp-decoding — practical qLDPC decoders bounded by these theorems
- qldpc-breakeven-evaluation — code-family evaluation context for rate/noise converses
- bosonic-gaussian-classical-capacity — adjacent channel-capacity results
