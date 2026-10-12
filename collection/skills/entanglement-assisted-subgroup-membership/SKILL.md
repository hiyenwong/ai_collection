---
name: entanglement-assisted-subgroup-membership
description: Use for one-way entanglement-assisted protocol separations.
category: ai_collection
trigger: entanglement-assisted communication, subgroup membership, remote state preparation, coset state Hadamard test, shifted equality problem, one-way quantum communication lower bound, communication complexity separation, moment method lower bound, matrix Bernstein, representation theory dimension bound, Heisenberg group irrep, min-max success probability, flat state RSP, quantum vs classical communication
arxiv_id: "2610.02099"
published: "2026-10-01"
---

# Entanglement-Assisted Subgroup Membership & One-Way Communication Separation

**Paper**: "An exponential separation between entanglement-assisted and unassisted one-way quantum communication" — Ryan Anselm (UT Austin), Srijita Kundu (Foxconn Research), Olivier Lalonde, Ashwin Nayak (Waterloo/IQC), arXiv:2610.02099, 1 Oct 2026.

## Core Result (Theorem 1.1)

First asymptotic separation between entanglement-assisted CLASSICAL communication and unassisted QUANTUM communication for a **total** Boolean function, in the one-way model:

- **With entanglement**: f_n computable with **O(log n) bits** of one-way classical communication + Θ(n) shared EPR pairs
- **Without entanglement**: one-way QUANTUM and randomized complexity are both **Θ(n^{1/3})** qubits/bits
- Exponential gap resolves the Buhrman–de Wolf / Brassard open question (2001/2003) in the one-way setting
- Rules out any shared-entanglement analogue of Newman's theorem (shared randomness removal), even for total functions
- Shi–Zhu simulation: entanglement-assisted C bits → unassisted classical 2^{O(C)} bits is **asymptotically optimal** — exponential blowup is necessary
- Trade-off: any one-way protocol with E EPR pairs and C bits/qubits satisfies **E + C = Ω(n^{1/3})** (protocol uses Θ(n) EPR; lower bound only forces Ω(n^{1/3}) — gap open)

## Reusable Component 1: Bounded-Order Subgroup Membership Protocol (Theorem 4.1)

**Problem** Memb_{G,k}: Alice gets subgroup H ≤ G with |H| ≤ k; Bob gets g ∈ G; decide g ∈ H. For ALL finite groups G:

**Protocol** (entanglement-assisted, one-way, 2⌈log₂|G|⌉ EPR pairs, O(log k) classical bits):
1. Let m = [G:H], T_1..T_m left cosets. Define flat mixed state ρ = (1/m) Σ_i |T_i⟩⟨T_i|, where |T_i⟩ = |H|^{-1/2} Σ_{t∈T_i} |t⟩ — rank-m mixture of orthogonal coset states
2. Alice **remotely prepares** two copies of ρ on Bob's side (RSP of flat states, Kundu–Lalonde): costs log(rank) = log(|G|/|H|)^{-1}... specifically log(|G|/(|G|/|H|)) = **log|H|** bits per copy + O(log(1/ε))
3. Bob runs **Hadamard test** with U_g: |x⟩ → |xg⟩ on each copy; outputs 1 iff both give 0

**Why it works**: tr(ρU_g) = 1 if g ∈ H (Hg = H fixes each coset), 0 otherwise (right coset disjoint). Hadamard test accepts w.p. ½ + ½Re tr(σU_g). Two copies + ε=0.01 RSP error → error ≤ 1/3.

**Key insight**: sending the MIXED coset-state ensemble ρ instead of pure |H⟩ cuts communication from O(log|G|) to **O(log|H|)** — because RSP cost scales with log rank, not log dimension. When |H| ≤ k = polylog|G|, cost is O(log log|G|).

**Limit**: for abelian G, O(log k) is achievable even WITHOUT entanglement (Theorem 4.2 — random characters from the annihilator H^⊥). Separation requires nonabelian structure.

## Reusable Component 2: Shifted Equality Problem (Hidden-Matching Generalization)

**Problem** ShiftEq_{G,r}: Alice gets g₁,g₂: ℤ₂ʳ → G; Bob gets h: ℤ₂ʳ → G and s ∈ ℤ₂ʳ. Decide: ∀x, g₁(x)·g₂(x+s) = h(x)?

- Generalizes Boolean Hidden Matching: translation-by-s pairs (x, x+s) form a perfect matching between two copies of ℤ₂ʳ; XOR → group operation of G
- **Total function**: no promise on no-instances (discrepancy δ(x) = h(x)⁻¹g₁(x)g₂(x+s) may equal identity at scattered points)
- Discrepancy formulation: ShiftEq = 1 iff δ(x) ≡ e for all x

**Reduction (Theorem 5.1)**: ShiftEq_{G,r} reduces to Memb_{Ĝ,k} over Ĝ = G^S ⋊_shift S̃ (semidirect product encoding shift action), with k = 2^{r+1}, |Ĝ| = k|G|^k. Alice's pair (g₁,g₂) becomes a conjugated subgroup X(g₁,g₂) = (g̃,0)H₀(g̃,0)⁻¹ where H₀ = {(e, s̃_e)}; Bob's (h,s) becomes element Y(h,s) = (h̃, s̃_e). Membership ⇔ shifted equality. **Pattern**: encode a functional constraint problem as subgroup membership via conjugation in a semidirect product.

## Reusable Component 3: Entanglement-Sensitive Lower Bound Technique (Theorems 5.2–5.3)

The central difficulty: most lower-bound techniques (e.g. discrepancy) apply equally to entangled and unentangled protocols. This one does NOT — it exploits that an unassisted C-qubit message lives in a 2^C-dimensional space:

1. **Min-max (easy direction)**: fix hard input distribution μ; success ≤ max over Bob POVMs of E ‖E_y M_{f(x,y)}‖∞ — Alice's best message is the top eigenvector of E_y M_{f(x,y)} (operator norm in dimension 2^C). With entanglement Bob's POVM acts on an unbounded-dimensional joint space — technique breaks, which is exactly why it separates the models.

2. **Hard distribution**: pick central element ζ ∈ Z(G) of order 3. Set h(x) = ζ^φ g₁(x)g₂(x+s) with φ = 0 w.p. ½, φ ∈ {1,2} w.p. ¼ each (order-3 analogue of Hidden Matching's random bit). Success bound reduces to E‖T(g₁,g₂)‖∞ where T = E_s[½M₁^{h₀,s} − ¼M₁^{ζh₀,s} − ¼M₁^{ζ²h₀,s}].

3. **Moment method + decoupling**: bound E tr(T^p) via E tr(T̃^p) where T̃ applies INDEPENDENT uniform phase rotations ζ^{φ_s} per s (makes summands independent → matrix Bernstein/Tropp moment inequality applies: E tr(ΣAᵢ)^p ≤ d(4pn)^{p/2} for independent zero-mean ‖Aᵢ‖≤1). Approximation error controlled by products of scalar functions w_s with ‖w_s‖∞ ≤ 1.

4. **Fourier domain spectral bound**: the approximation error is ‖(I−P)K‖∞ where K (pair-swap on G²) and P (phase-average) are transition operators of random walks on Cayley graphs of G². Fourier transform block-diagonalizes: irreps with ρ(ζ) = I cancel; remaining blocks are (1/d_ρ)·(permutation), so **‖(I−P̂)K̂‖∞ = 1/D**, where **D(G,ζ) = min{d_ρ : ρ(ζ) ≠ I}** — the smallest irrep dimension on which ζ acts nontrivially.

5. **Conclusion (Theorem 5.2)**: Q^{1,pub}_{1/3}(ShiftEq_{G,r}) = **Ω(min{2^r, (log D)/2})** — need central ζ of order 3 invisible to all irreps of dimension < D.

**Reusable pattern**: *lower-bound strength = representation-theoretic parameter D of the group*. Build hard communication problems from groups with large low-dimensional-rep gaps around a central element.

## Reusable Component 4: Group Instantiation (Theorem 6.1)

**Generalized Heisenberg group** H_m(𝔽₃): elements (u,v,w), u,v ∈ 𝔽₃^m, w ∈ 𝔽₃; product (u₁,v₁,w₁)(u₂,v₂,w₂) = (u₁+u₂, v₁+v₂, w₁+w₂+u₁·v₂) — upper-triangular (m+2)×(m+2) matrices. Central ζ = (0,0,1) has order 3.

**D(H_m, ζ) = 3^m** (Lemma 6.2): Schur → ρ(ζ) = ω^s I; X_u := ρ(u,0,0), Y_v := ρ(0,v,0) satisfy X_u Y_v = ω^{s·u·v} Y_v X_u (Weyl-pair structure); simultaneous eigenbasis of {X_u} shifted by Y_v to orthogonal eigenbases forces dim ≥ 3^m (Stone–von Neumann rigidity).

**Choice m = 2^r**: D = 3^{2^r} → log D = 2^r log 3 → lower bound Ω(min{2^r, 2^r log3/2}) = **Ω(2^r)** = Ω(n^{1/3}) since input length n = Θ(2^{3r}). Pattern: *tune the Heisenberg parameter m exponentially in r to keep (log D)/2 ahead of 2^r*.

## Methodology Transfer Checklist

When proving communication/resource separations where a shared resource (entanglement, advice, correlation) beats a stronger message model:
1. Find a problem with an efficient resource-assisted protocol whose cost scales with a **local parameter** (log|H|, not log|G|) via resource-assisted state preparation
2. For the lower bound, use a technique that **breaks when the receiver's Hilbert space is unbounded** (top-eigenvector/min-max argument)
3. Hard distribution: inject a **low-order central element** as random phase — order 3 (not 2) prevents parity-style cancellation and matches the Weyl commutation
4. Moment method with **decoupling by independent random phases**, then **Fourier/representation analysis** to extract a spectral gap parameter D
5. Instantiate with a group family where D is **exponentially large in a tunable parameter** (Heisenberg/Weyl groups: D = 3^m)
6. Check the simulation theorem converse (Shi–Zhu): if the separation is optimal, it certifies tightness of the classical simulation cost

## Pitfalls

- **Newman's theorem does NOT lift to entanglement**: shared-entanglement removal is not O(log n) — this separation is the counterexample; do not assume random-rental tricks transfer
- **Abelian groups give no separation**: characters diagonalize everything; the protocol then needs no entanglement (Theorem 4.2). Nonabelian structure with large irreps is essential
- **Teleportation makes quantum ⊇ entanglement-assisted up to factor 2** — comparisons must be entanglement-assisted CLASSICAL vs unassisted QUANTUM, not the other way
- **Moment method needs decoupling first**: dependent summands over shared g₁,g₂ make tr(T^p) intractable; rotate each term by independent uniform ζ^{φ_s} before applying Tropp
- **POVM convention**: eliminate the 0-outcome via M₁ = I − M₀ so the optimization is over operators 0 ≤ M₁ ≤ I only
- The two-copy Hadamard test matters: single copy gives error ½+½·0.505 ≈ too weak; squaring acceptance (0.505² ≈ 0.255) plus RSP failure (0.02) lands under 1/3
- Paper's AI disclosure: LLMs (GPT-6 Astra) proposed the ShiftEq instantiation; authors verified and simplified — treat LLM-suggested problem constructions as hypotheses requiring independent proof

## Related Skills

- `guarded-coherent-two-party-qdp` — same week's quantum communication advantage (DP protocols), complementary lower-bound style
- `quantum-auction-summation-protocols` — related one-way quantum communication security results in kg.db
- `boltzmann-attention`, `free-energy-moe-routing` — unrelated

## Sources

- arXiv:2610.02099 (quant-ph, 1 Oct 2026); builds on Aaronson–Le Gall–Russell–Tani subgroup membership (ALRT11), Watrous (Wat00), Boolean Hidden Matching (BJK04, GKKRW08), Kundu–Lalonde RSP tradeoffs (arXiv:2602.09428), Shi–Zhu simulation (SZ08)
