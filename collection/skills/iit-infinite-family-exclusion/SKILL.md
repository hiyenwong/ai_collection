---
name: iit-infinite-family-exclusion
description: XOR-cycle IIT substrates with quadratic Phi growth, Lean 4 verified. Use when analyzing consciousness metrics.
category: neuroscience
---

# IIT Infinite Family with Arbitrarily Large Integrated Information

**Paper**: "Existence of an infinite family of substrates satisfying all the postulates of integrated information theory, exclusion included, with arbitrarily large integrated information" (arXiv:2610.02219, A. Mayeux, Sep 2026)

## Core Result

For every N ≥ 8 with 3∤N, the cycle **A_N** of N binary units — each unit taking the XOR of itself and its two clockwise neighbours — satisfies BOTH IIT 4.0 demands simultaneously:

1. **Exclusion (Theorem 3.4)**: In EVERY state and against every background, A_N is a complex: φ_s(A_N, s) ≥ 4 > φ_s(S', s) for every nonempty proper subsystem S'.
2. **Lower bound (Theorem 3.5)**: At the all-ones state, Φ_max ≥ 2^⌊N²/8⌋ · (1/2)^N/(2N) − 1, so **log₂Φ = Ω(N²)** (already 2.6×10⁷ at N=20, 1.8×10⁴⁶ at N=40).

This is the **first lower bound on Φ for a growing family** and the first substrate proven (not computed at small sizes) to satisfy every IIT 4.0 postulate. The ceiling is O(N²·2^(2^N)) — the family sits strictly inside at 2^Θ(N²).

## The Substrate (Definition 3.1)

- Units indexed by ℤ_N, state space {0,1}^ℤ_N
- Deterministic transition: (F_N s)_z = s_z ⊕ s_{z+1} ⊕ s_{z+2}
- **F₂-linear circulant**: C = I + P + P² (P = cyclic shift); invertible ⟺ gcd(1+x+x², x^N−1) = 1 ⟺ 3∤N (roots of 1+x+x² are primitive cube roots of unity)
- Bijectivity (3∤N) is what makes the cause side collapse onto the effect side
- The all-ones state 1 is a fixed point: 1⊕1⊕1 = 1

**Key structural insight**: the substrate is uniform, sparse, flat — the OPPOSITE of densely connected architectures one might expect large Φ to require. Each unit reads only 3 units regardless of N.

## The Damage Reduction (Proposition 4.1) — Key Technique

System integrated information φ_s reduces EXACTLY to a combinatorial damage count:
- Unit j is "damaged" by partition θ when a live input of j lies in the cut set of j's own block
- **φ_s(θ) = dmg(θ)** at the all-ones state on the full cycle
- Effect side: severed XOR input flattens effect repertoire to 1/2 → product gives 2^(−dmg) → log returns the count
- Cause side: requires bijectivity (3∤N) — the fibre over 1 is a single point

On proper subsystems: φ_s(S, 1) = 2^(−corank(C_S)) · dmgval(S), where the corank factor is the fibre size — **singular subsystems are penalized by a factor ≥ 2**.

**False guess warning**: subtractive corrections to the damage count are FALSE (state-entry only through the corank factor).

## Exclusion Proof Structure (Section 5)

Two halves:
1. **Whole cycle φ_s ≥ 4**: classify partitions by damage budget — D=1 forces 𝒩(θ)=N−1; D=2 gives 2(N−1) or ≤N²/4; D=3 gives 4𝒩(θ) ≤ (N−1)²+8(N−1). A single explicit witness ϑ* (three arcs of sizes a,k,k with k=⌊(N+1)/3⌋, damage ≤4) undercuts all three floors simultaneously. So every minimizer damages ≥4 → φ_s ≥ 4 via the supremum-over-argmin convention.
2. **Proper subsystems < 4**: shielded-witness partition. Delete unit d ∉ S with d−1 ∈ S; the arc P behind d−1 has its head NOT damaged (deleted units are not live inputs — deletion REMOVES rather than cuts). Choosing |P|=⌊|S|/2⌋ gives 𝒩 ≥ (|S|²−1)/4 with damage 1, yielding φ_s(S,s) ≤ 4|S|/(|S|+1) < 4. No case analysis on S's shape needed.

## Distinctions and the Quadratic Rate (Sections 6–7)

- **Every arc of length ≥3 is an irreducible distinction** (Prop 6.1); its maximally irreducible cause purview contains the arc itself
- Distinctions are EXACTLY the arcs (Prop 6.2, verified by exhaustive evaluation N=8,10,11,13; counts 41,71,89,131 = N(N−3)+1) — quadratically many, each sharing units with neighbours
- **Family bound (Lemma 7.1)**: F distinctions all containing a common stated unit p, each with φ_d/|supp| ≥ c > 0, give Φ_max ≥ (2^|F| − 1 − |F|)·c — the 2^|F| comes from RELATIONS: every subset of F is a relation since members overlap congruently at p
- |F| = (⌊N/2⌋−1)(N−⌊N/2⌋−1) ≥ N²/8 arcs through unit 0 → quadratic exponent

**Why quadratic is forced**: a family of 2^cN distinctions sharing a unit would give Φ = 2^(2^Θ(N)); only-arcs classification rules this out.

## Method: Human Direction + LLM Assistants + Proof Assistant (Section 8)

The working arrangement that produced the result:
1. **Human strategic direction**: choosing to formalize IIT in Lean at all (non-obvious — field is computational/empirical); fixing which questions to ask
2. **LLM assistants**: carried out the formalization file-by-file against stated blueprints (statements fixed in advance, proofs left to them); also supplied proof-strategy suggestions
3. **Lean 4 kernel**: certified every inference; no unproved steps (single exception: Prop 6.2, flagged explicitly)

**Key epistemological insight**: formal verification does NOT catch wrong conjectures — the authors' original doubly-exponential conjecture was FALSE and refutation came from realizing irreducible parts are all contiguous arcs (only quadratically many). "The principal hazard is not incorrect reasoning, but correct reasoning about an object that cannot support the intended conclusion, and often only a proof carried to the end distinguishes the two."

## Reusable Patterns

1. **Proof-assistant-as-discovery-instrument**: symbolic manipulation with size as variable settles every size at once vs. pointwise numerical evaluation
2. **Damage-count reduction**: replace nested optimizations (partition argmin over φ_s(θ)/𝒩(θ)) by an exact combinatorial count for deterministic XOR-like dynamics
3. **Shielded-witness partitions**: deletion (not cutting) removes live inputs; heads of arcs adjacent to deleted units escape damage — construct low-damage/high-𝒩 competitor partitions this way
4. **Counting via common-unit relation families**: exponential Φ growth from subsets of overlapping distinctions; certify family size, apply counting identity
5. **Circulant invertibility arithmetic**: F₂-circulant C = f(P) with f(x) = 1+x+x² = (x³−1)/(x−1); bijectivity ⟺ 3∤N via root-of-unity argument over 𝔽₂[x]/(x^N−1)

## Verification Status

Every theorem (except Prop 6.2, explicitly flagged) machine-checked in **Lean 4** against the IIT 4.0 formalization ([5]); the development is public and independently re-checkable. Cross-validated against PyPhi at small sizes.

## Key Lessons

- Large integrated information does NOT require dense connectivity — sparse uniform local rules suffice
- IIT 4.0's exclusion postulate is satisfiable by provably growing families (counters any claim it forces only small complexes)
- AI-assisted formal proof works: human direction + LLM proofs + kernel certification is a viable research arrangement for theories whose quantities are "too intricate to paraphrase safely"

## Related Skills

- [[iit-critical-review]] — critical evaluation of IIT as a theory
- [[iit-fep-maxcaliber-bridge]] — Maximum-Caliber Deviation framework bridging IIT and FEP
- [[canonical-functionalism-consciousness]] — mathematical refinement of consciousness theories
