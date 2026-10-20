---
name: design-pseudorandom-separation
description: Separate unitary designs from pseudorandom unitaries via planted structure.
category: ai_collection
---

# Separating Unitary Designs from Pseudorandom Unitaries

**Source**: On the pseudorandomness of simple quantum processes (Dujmovic, Haferkamp, Poremba, arXiv:2610.02100, Oct 2026)

## When to Use

- Proving that statistical moment matching (unitary t-designs) does NOT imply computational pseudorandomness
- Constructing ensembles that fool all statistical tests yet retain efficiently learnable structure
- Auditing claims that "maximal scrambling ⇒ Haar-like behavior" in many-body physics or black-hole models

## Counterexample Pattern 1: Doped Clifford Local Walk (refutes Quantum HMMR)

Ensemble: random nearest-neighbor **Clifford** gates, except with probability 1/m (m = Θ_t(n²)) apply a random non-Clifford single-qubit Z-rotation. After T = O_t(n² log² n) steps the ensemble is an approximate adaptive unitary t-design with error exp(−Ω(log² n)) — yet distinguishable with O_t(log² n) queries.

Why it works:
1. Clifford walk converges rapidly to the **Clifford twirl**, but the Clifford twirl fixes more operators than the Haar twirl.
2. For fixed t, the fixed-point space of the t-fold Clifford twirl has **dimension bounded independently of n** [GNW21]. Clifford mixing suppresses the entire spectrum except constantly many eigenvalues.
3. Only those constant-many eigenvalues need the rare non-Clifford rotations; in that constant-dimension subspace, apply known spectral bounds on doped Clifford circuits.
4. Adaptive-query security: express acceptance probability via spectral decomposition of the moment operator; exponentially small eigenvalues absorb the dimension factor; the remaining constant-size sum of decaying exponentials is bounded by the **boundedness of the outcome probabilities themselves** (polynomial-method spirit) — not by coefficient-wise estimates.

Detectable structure: stabilizer structure survives (computational-basis action yields stabilizer states, recognizable efficiently).

## Counterexample Pattern 2: FB Ensemble (separates poly-order designs from PRUs)

Construction: U = F·B where
- **F** = diagonal phase circuit from a 2t-wise independent phase function f (trace function over F_{2^n}/F_2 with 2nt seed bits), mapping the fixed subspace S = span(|+⟩^⊗n) to a planted binary phase state |ψ_f⟩;
- **B** = block-diagonal circuit leaving S invariant, Haar-random on S^⊥ (implemented via controlled constant-depth generators + Kazhdan-constant spectral gap walk on O(n) circuits, depth poly(n, t, log 1/ε)).

Design property: insert a uniform computational-basis permutation P (fixes |+⟩^⊗n, so distribution unchanged): FB = F P B viewed as an instance of the **PFC ensemble** [MPSY24]; use the positive-operator/collision analysis of [CSBH25] to get adaptive t-design error O(t²/2^n) with **no square-root loss**.

The distinguisher (efficient, O(n^t) forward queries):
1. Query U on |+⟩^⊗n repeatedly — every output is the SAME phase state |ψ_f⟩ (m copies).
2. **Derivative measurement** [ABDY23]: each copy yields a uniform distinct pair {x,y} and the relative phase f(x)+f(y) — one linear equation in the 2nt seed bits.
3. O(n^t) equations ⇒ finite-field character-sum (Weil) bound ⇒ seed determined up to constant; Gaussian elimination recovers f; test on fresh copies ⇒ constant distinguishing advantage.

## Core Reusable Lessons

- **Moment matching ≠ pseudorandomness, at any polynomial order** — the separation holds for all 1 ≤ t ≤ 2^{n/4−4}.
- **Plant structure in an invariant 1-D subspace**: mixing on the orthocomplement supplies all Haar moments; the planted phase state is invisible to moments but learnable from enough copies.
- **PFC-style permutation insertion** launders a structured block into a known design construction — check whether your ensemble factorizes through a permutation-invariant decomposition.
- **Physics caution**: an ensemble can have expected min-entropy within 8 bits of maximal on every balanced crossed cut (maximal scrambling [LLZZ18] at t = Θ(n)) and still be efficiently distinguishable with O(n²) queries. Entanglement saturation is NOT a proxy for Haar randomness; pseudorandomness is.
- **Threshold conjecture (Conjecture 6.1)**: local ensembles forming approximate t-designs at t = Θ(n) (maximal scrambling scale) with negligible error may be the genuine threshold where PRUs emerge — neither counterexample applies there. Both known counterexamples fail in this regime (near-Clifford: fixed constant order only; FB: artificial non-local phase circuit).

## Verification Checklist (when auditing a "pseudorandom" claim)

1. Is the claimed security against statistical tests only (design order t), or all poly-query algorithms?
2. Does the ensemble preserve an invariant low-dimensional subspace? Query it.
3. Do repeated queries on a fixed input produce copies of ONE learnable state (phase/Bell/derivative sampling attacks)?
4. Does the ensemble factor through a known design construction (PFC) with a hidden structured factor?
5. Is the "scrambling" evidence entanglement-based? If so, it does not rule out efficient distinguishers.
