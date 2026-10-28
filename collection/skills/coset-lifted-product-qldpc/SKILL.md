---
name: coset-lifted-product-qldpc
description: Build quantum LDPC codes from non-normal subgroup coset actions.
category: ai_collection
trigger_words: quantum LDPC, lifted product, coset action, two-block group algebra, bivariate bicycle, CSS code construction, non-normal subgroup, quantum code search
---

# Coset Lifted Product Codes: Quantum LDPC from Non-Normal Subgroup Actions

**Source:** arXiv:2610.12782 (Rajpurohit, Lalitha, Garani — IISc/IIIT, Oct 2026)

## When to Use
- Designing short-to-medium length (n ≤ 400) quantum LDPC codes beating published Q = kd²/n records
- Searching beyond bivariate bicycle (BB) / two-block group algebra (2BGA) code families
- Need explicit certified-distance codes at check weights 6, 7, 9

## The Construction

Combine **lifted products** (protograph structure) with **coset actions** (Aydin-Tamo-Barg non-normal subgroup trick):

Given: finite group G, subgroup H ≤ G (**need not be normal**), normalizer N = N_G(H), protograph A over F₂[G], protograph B over F₂[N].

- Left action: L(g)(xH) = gxH (coset space Ω = G/H, m = |G|/|H| points)
- Right action: R(n)(xH) = xnH (well-defined because n⁻¹Hn = H)
- Key lemma: **L(g)R(n) = R(n)L(g)** — the two actions commute → CSS orthogonality for free

**CLP code (Definition III.1):**
```
H_X = ( L(A) ⊗ I_{nB0}   |  I_{nA0} ⊗ R(B) )
H_Z = ( I_{nA1} ⊗ R(B)^T |  L(A)^T ⊗ I_{nB1} )
```
n = m(n_A1·n_B0 + n_A0·n_B1) qubits. Over F₂ the commutativity makes each H_X H_Z^T block compute to L(α)R(β) + R(β)L(α) = 0.

## Subgroup Selection Logic (Prop III.4 — critical for search)

Every CLP code reduces to one with a **core-free** subgroup (quotient by Core_G(H)). The productive search space is exactly:
- H core-free, and **H < N < G** (strict inclusions)
- H normal → just a lifted product over G/H (nothing new)
- N = H (self-normalizing) → right action trivial, B contributes only parity of entry weights (degenerate)

## Dimension Formula (odd |G|, Theorem III.7)

k = Σ_ρ [ κ(A_ρ)·κ(B_ρ^T) + κ(A_ρ^T)·κ(B_ρ) ]  over irreducible representations ρ with μ_ρ = dim(ρ^H) > 0

- A_ρ = A with entries mapped through ρ; B_ρ = B through τ_ρ (Schur blocks of R(β))
- Multiplicity μ_ρ = dim ρ^H = dim of H-fixed subspace (Frobenius reciprocity)
- CLP dimension = sum of hypergraph product code dimensions per representation
- Rank invariant under the basis change S that block-diagonalizes L(g) (Maschke applies since |G| odd)

## Certification & Search Pipeline

1. Enumerate pairs (G, H) — 14,843 pairs searched, H non-normal, 120 ≤ n ≤ 400 (GAP SmallGroup library)
2. Layouts: 1×1 protograph A over 2×2 protograph B (or transposed)
3. Distance certification: split the weight-≤ d_ub logical-operator search into **sectors by coset-translation class**; each sector = binary integer program solved in **Gurobi** with cutoff d_ub − ½; all sectors terminating at cutoff ⟹ d ≥ d_ub; any sector solving without cutoff pins d exactly
4. Independent NumPy recheck of orthogonality, dimension, weights from raw matrices

## Record Codes Found

| w | Code | Q = kd²/n | (G, H) |
|---|---|---|---|
| 6 | **[[360, 20, 20]]** | 22.2 | (SmallGroup(270,26), C₃) |
| 7 | **[[360, 24, 20]]** | 26.67 | m=90, C₃ subgroup |
| 9 | **[[252, 16, 18]]**, **[[288, 16, 20]]** | 20.6 / 22.2 | odd-order groups |
| 6 | [[168, 10, 14]], [[240, 8, 20]] | 11.7 / 13.3 | high-distance |
| 10 | [[360, 20, ≤27]] (candidate) | Q ≤ 40.5 | SmallGroup(270,25) |

All exceed best published Q at their check weights; all matrices printed in the paper (reproducible).

## Reusable Patterns

1. **Commuting-action pair → CSS for free**: any two commuting representations (here left-coset vs normalizer-right) give H_X H_Z^T = 0 automatically over F₂ (the two equal terms cancel). Look for commuting action pairs before hand-checking orthogonality.
2. **Non-normal H expands code space at no cost**: regular-representation constructions (2BGA/BB) are the H={e} special case; coset actions G/H with core-free H < N < G give genuinely new matrix geometries.
3. **Representation-theoretic dimension counting**: block-diagonalize via Maschke + Schur; dimension becomes a sum of small hypergraph-product formulas per irrep — fast k computation without building the full CSS check matrices.
4. **Sector-wise ILP distance certification**: decompose minimum-weight-codeword search by symmetry class (translation/coset orbits), run per-sector ILP with cutoff, combine for certified bounds — scalable to n=400 where brute force fails.
5. **Q = kd²/n at fixed check weight w** is the record metric for small qLDPC; certification (not estimates) is what makes a code publishable.

## Relation to Prior Families
- H = {e}: ordinary lifted product LP(A,B) over regular rep
- 1×1 protographs: Aydin-Tamo-Barg coset two-block codes
- H normal: lifted product over quotient group G/H
- Bivariate bicycle (BB, IBM/Bravyi et al.): G = Z_ℓ × Z_ℓ', regular action — a small corner of CLP space
