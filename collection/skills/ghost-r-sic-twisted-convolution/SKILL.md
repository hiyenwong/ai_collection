---
name: ghost-r-sic-twisted-convolution
metadata:
  arxiv_id: "2609.39192"
  published: "2026-09-30"
  authors: "Marcus Appleby, Steven T. Flammia, Gene S. Kopp"
  categories: "math.NT, quant-ph, math-ph"
  tags: [number-theory, quantum-dilogarithm, SIC-POVM, twisted-convolution, ghost-SIC, equichordal, pentagon-relation, Stark-conjecture, Weyl-Heisenberg]
description: "Use for ghost r-SIC construction via twisted convolution identity."
---

# Ghost r-SICs from Finite Quantum Dilogarithms: The Twisted Convolution Identity

Source: Appleby-Flammia-Kopp, "The twisted convolution identity and ghost r-SICs from finite quantum dilogarithms", arXiv:2609.39192 (2026-09-30). math.NT + quant-ph; builds on Radchenko-Wheeler arXiv:2609.21892.

## Overview

AFK extend the Radchenko-Wheeler (RW) proof of the finite pentagon relation from rank-1 principal-form case to **all rank-r admissible tuples** (including nonprincipal forms). Result: for positive integers d, r with r < (d−1)/2 and (d²−1)/(r(d−r)) ∈ ℤ, there exist **ghost r-SICs** — d² rank-r subspaces in ℂ^d satisfying a non-Hermitian equichordal condition. Under the Stark conjecture these become genuine (Hermitian) r-SICs via Galois conjugation. The results are **unconditional**; Stark conjectures enter only in the ghost→Hermitian upgrade.

## Core Objects

### 1. Admissible Tuple t = (d, r, Q)
- d, r positive integers, r < (d−1)/2, (d²−1)/(r(d−r)) ∈ ℤ
- Q integral binary quadratic form with (d+1)(d−3)/disc(Q) a square integer

### 2. Twisted Convolution Identity (TCI) — Theorem 1.2
Quadratic relation on the Shintani–Faddeev cocycle ש:
```
Σ_{q∈I} ζ_d^{r⟨p,(λI+L)q⟩} · ש_{dγ}^{(q−p)/(d−1)}(τ) · ש_{γ⁻¹}(τ) = 0
```
where L ∈ SL₂(ℤ) has odd order 2m+1 mod d, γ = L^{2m+1}, τ = attracting fixed point, ⟨x,y⟩ = x₂y₁ − x₁y₂ symplectic form. λ chosen so gcd(2λ+tr(L), d)=1.

### 3. Ghost r-SICs — Theorem 1.3
d×d complex matrices Π̃_p indexed by p ∈ ℤ²/dℤ² satisfying:
1. **Weyl–Heisenberg covariant**: Π̃_p = D_p Π̃_0 D_p⁻¹, where D_p = e^{(d+1)πi/d · p₁p₂} X^{p₁}Z^{p₂}
2. **Rank-r projections**: Π̃_p² = r·Π̃_p (idempotent after scaling — TCI enforces this)
3. **Equichordal**: tr(Π̃_p Π̃_q) = r(dr−1)/(d²−1) for p ≠ q
4. **Parity-Hermitian**: Π̃_p† = U_P Π̃_p U_P†

### 4. Finite Pentagon Relation (RW input, extended)
- RW proved finite pentagon relation for real quadratic special values of the modular quantum dilogarithm
- AFK derive a **subgroup version**: pentagon relation for sums of quotients of quantum dilogarithm values on dual pairs H, H^∨ of subgroups of the RW metric group G — via **character theory of finite abelian groups**
- Historical framing: finite pentagon = "higher reciprocity law", a finite analogue of Dimofte's continuous pentagon identity; proof style parallels Kronecker's residue-calculus evaluation of quadratic Gauss sums

### 5. Convention Dictionary (Section 2)
- RW: F_γ^± (row vectors, finite quantum dilogarithm Φ_γ,m,n)
- AFK: ש_γ^r(τ) (column vectors, Shintani–Faddeev Jacobi cocycle σ_γ)
- Bridge: F_γ^±(u^⊤) = e^{πi/12 Ψ(γ)} · ש_{γ^N}^{(I−γ⁻¹)Su}(...) with N = tr(γ)−2, S = [[0,1],[−1,0]], Ψ = Rademacher class invariant
- µ_γ = e^{πi/12 Ψ(γ)} links the eta multiplier to the Rademacher symbol

## Methodology Patterns

### Pattern 1: Convention-Dictionary Bridging
When two papers prove overlapping results in different notations, write an **explicit dictionary** (Prop 2.1 style) rather than re-proving. The dictionary makes each paper's results importable to the other's framework and is often the main technical contribution.

### Pattern 2: Rank-1 → Rank-r Lift via Character Theory
RW's pentagon is rank-1 principal-form. AFK lift to all admissible r by:
1. Passing to subgroups H ≤ G and dual pairs H, H^∨
2. Applying **finite abelian character theory** to push the pentagon identity through subgroup sums
3. Tracking the odd-order symmetry matrix L (order 2m+1 mod d) via Fibonacci-like recurrences: L^m = r_{j,m}L − r_{j,m−1}I (Lemma 4.3), L^{2m+1} − I = d_{j,m}L^m(L−I) (Lemma 4.2), det(L−I) = −(d^j−3) (Lemma 4.4)
This "subgroup + characters" lift is reusable whenever an identity holds on a group but is needed on coset representatives.

### Pattern 3: Unconditional Core + Conditional Upgrade
Prove what you can unconditionally (ghost equichordal configurations), and state precisely which additional conjecture (Stark → Galois automorphism) upgrades the result to the target object (Hermitian SIC). Keeps the theorem honest and modular:
- **Unconditional**: TCI ⟹ ghost r-SIC existence (all admissible (d,r,Q))
- **Conditional (Stark)**: ghost r-SIC ⟶ Galois conjugate ⟶ Hermitian r-SIC

### Pattern 4: Equichordal Geometry from Cocycle Quadratic Relations
The quadratic (twisted convolution) identity on cocycle special values is exactly what makes the constructed operator idempotent (Π̃² = rΠ̃). General reusable fact: to build projector-valued configurations from transcendental special values, encode idempotency as a **vanishing quadratic form** on those values, then prove the vanishing via a pentagon/reciprocity-type identity.

## Applications & Open Problems

- Zauner's conjecture (SIC-POVM existence in every dimension) still needs the Galois automorphism √∆ → −√∆ intertwining complex conjugation — NOT provided by these methods (Ocneanu rigidity is ineffective)
- Unitary near-group categories: same missing Galois step
- Full rank-1 real quadratic Stark conjecture: still open beyond algebraicity
- Three simultaneous Sept 2026 preprints (Huang; Radchenko-Wheeler; Gannon-Schopieray-Yadav) on finite pentagon relations — active area

## Verification Recipe (for numerical checks)

```python
# Given ghost projections {Pi_p} constructed from cocycle values:
# 1. Covariance: D_p Pi_0 D_p^-1 == Pi_p
# 2. Idempotency: Pi_p @ Pi_p == r * Pi_p  (requires TCI)
# 3. Equichordal: trace(Pi_p @ Pi_q) == r*(d*r-1)/(d*d-1) for p != q
# 4. Parity: U_P Pi_p U_P^-1 == Pi_p.conj().T
# Any failure of (2) ⟺ TCI numerically violated for that tuple
```

## Related Skills
- `stark-units-quantum-dilogarithm-algebraicity` (RW base paper arXiv:2609.21892)
- `sic-overlap-stark-units-number-theory` / `stark-units-sic-overlaps` (Stark units in SIC overlaps)
- `modular-nahm-sums-construction` (related cocycle special-value constructions)
