---
name: standard-model-triorthogonal-qec
description: "One generation of Standard Model fermions (plus right-handed neutrino) is a triorthogonal quantum error-correcting code: anomaly cancellation = vanishing cubic form, yielding [[15,1,3]]_p codes (Bravyi-Kitaev 15-qubit for p=2, new qudit codes for odd p; unique shortest qutrit triorthogonal code). Use when exploring connections between particle physics anomalies, triorthogonal codes, magic state distillation, or qudit QEC code design. Activation: triorthogonal, anomaly cancellation, Standard Model QEC, Bravyi-Kitaev 15-qubit, qutrit code, magic state distillation, charge lattice, transversal non-Clifford gate."
---

# Standard Model Generation as a Triorthogonal QEC Code

Methodology from arXiv:2610.21879 (Prakash & Ramya; Oct 2026). The fermion content of one Standard Model generation, augmented by a right-handed neutrino ν^c, forms a triorthogonal quantum error-correcting code — the same code class underlying magic state distillation. Gauge anomaly cancellation and triorthogonality are the same cubic equation.

## The Dictionary (physics ↔ coding)

| Standard Model | QEC code |
|---|---|
| 16 fermion fields incl. ν^c (SO(10) spinor, 5-bit even-parity strings) | charge lattice Λ ⊂ Z^n, n=16 |
| Fermion ψ_ℓ with charge vector q_ℓ under U(1)^r torus | column ℓ of generator matrix |
| Symmetry subgroup Z_p (charges mod p) | triorthogonal space W = Λ mod p |
| Right-handed neutrino ν^c (removed) | logical qudit |
| 15 remaining quarks/leptons | physical qudits |
| Symmetries under which ν^c is neutral (gauge charges: color, weak isospin, hypercharge; exactly these for p≥5) | X-stabilizers |
| The one remaining SO(10) charge under which ν^c has charge 1 | logical X operator |
| Mixed cubic anomalies of that charge with gauge charges vanish | triorthogonality condition |
| Cubic anomaly that ν^c itself would have canceled | logical gate phase |
| Charge-conserving 4-fermion operators, e.g. Dirac-mass product (νν^c)(ee^c) | minimum-weight logical errors |
| Pairing quarks/leptons with Dirac partners | code doubling construction |

## Mathematical Core

**Cubic anomaly form**: For n Weyl fermions with chiralities c_ℓ = ±1 and integer charges x, y, z ∈ Z^n (rows of the charge lattice):
τ_c(x,y,z) = Σ_ℓ c_ℓ x_ℓ y_ℓ z_ℓ.
Anomaly-free spectrum ⟺ τ_c vanishes on Λ — call Λ **triorthogonal**. Modulo prime p, the same vanishing defines a **triorthogonal space** W ⊆ F_p^n. Note: no self-orthogonality required (transversal gate doesn't need it; the code is not self-orthogonal for any odd p).

**Code construction**: Delete coordinate 0 (remove ν^c): CSS code on remaining n−1 = 15 coordinates. X-stabilizers = vectors of W vanishing at coordinate 0; logical X = g ∈ W with g_0 = 1. Result: **[[15,1,3]]_p for every prime p**:
- p=2: the Bravyi–Kitaev 15-qubit code (the original magic-state distillation code).
- odd p: new p-level qudit codes.
- p=3 (qutrits): **unique** shortest distance-3 triorthogonal code (exhaustive search; previous shortest had 19 qutrits).

**Transversal non-Clifford gate**: ⊗_{ℓ≠0} U^{c_ℓ} where U = π/8-type gate:
- p=2: T = diag(1, e^{iπ/4})
- p≥5: U = Σ_j ω^{j³}|j><j|, ω = e^{2πi/p}
- p=3: diag(1, ζ, ζ^{-1}), ζ = e^{2πi/9}

Logical states |a̅> ∝ Σ_x |ag + x⟩. Each qudit phase ω^{c_ℓ w_ℓ³} multiplies to ω^{Σc_ℓ w_ℓ³} = ω^{-c_0 a³} (since τ_c(w,w,w) = 0 by anomaly freedom) — **the logical gate phase is exactly the anomaly that the removed fermion ν^c would have canceled**. Gate fixed up to Pauli correction (p=3) or Clifford correction (p=2).

**Distance**: d_Z = smallest Hamming weight of undetectable nontrivial Z-error. Weight-3 (nuance: 4-fermion operators like Dirac masses (νν^c)(ee^c) saturate the bound). For odd p, relation ν^c = e^c + u^c_1 − d^c_1 among SO(10) weights supplies the distance argument.

## Workflow: Build a Code from a Physics Spectrum

1. **Write the charge lattice**: n Weyl fermions, chirality signs c_ℓ, integer charge vectors q_ℓ ∈ Z^r under U(1)^r (for SM generation: r=5, the SO(10) Cartan; q vectors = hypercharge/color/isospin assignments).
2. **Verify anomaly cancellation**: check τ_c(x,y,z) = 0 for all x,y,z ∈ Λ (equivalently on generator rows; for SM generation this is A(10) + A(5̄) = 0 within SU(5) ⊂ SO(10)).
3. **Check chirality**: useful triorthogonal codes need anomaly-free **and chiral** spectra — if all q_ℓ = ±1·(single column span), d=1. Nontrivial distance requires the charge lattice to genuinely mix.
4. **Reduce mod p**: W = Λ mod p (requires q_0 ≢ 0 mod p for the removed fermion). Obtain triorthogonal space.
5. **Delete coordinate 0**: CSS code, X-stabilizers from W∩{w_0=0}, logical X from g_0=1.
6. **Read off the logical gate**: transversal U^{c_ℓ} acting as logical U^{-c_0} (anomaly of the removed fermion).
7. **Compute d_Z**: enumerate low-weight charge-conserving operators (Dirac-mass-like pairings give the minimum logical errors).

## Why This Matters

- **Uniqueness result**: the qutrit [[15,1,3]]_3 is the shortest possible distance-3 triorthogonal qutrit code — a new distillation primitive candidate for qudit fault-tolerant stacks.
- **Cross-domain transfer**: any anomaly-free chiral fermion spectrum (particle physics model building) is automatically a candidate qudit triorthogonal code library; conversely, QEC code design constraints (distance, transversality) become consistency conditions on spectra.
- **Conceptual bridge**: magic (non-stabilizerness) distillation — the resource-theory heart of FTQC — is governed by the same cubic structure as gauge anomaly cancellation in the SM. The 5-bit even-parity labeling of one fermion generation is not a coincidence but a code structure.

## Limitations & Caveats

- The [[15,1,3]]_p code family from the SM generation is primarily a structural/uniqueness result; full distillation protocol performance (noise thresholds, yield) for the qutrit code is future work ("we comment on its potential").
- Not self-orthogonal for odd p — relevant when your stack requires self-orthogonality for additional gates.
- The physics→code map requires integer charges; fractional hypercharge conventions must be rescaled to integers first.
- Anomaly freedom of the full SO(10) spectrum is what makes the construction work — partial spectra (e.g. without ν^c) only give the code after deletion, and their standalone anomaly structure differs.

## Related Skills

- `bunny-codes-qec` — alternative QEC construction via cellular automata.
- `deterministic-cat-state-generation` — 100+ photon cat states (bosonic FTQC track).
- `borrowed-identity-magic-distillation` — other magic-state distillation protocols.
- `qudit-many-hypercube-qec-codes` — high-rate qudit qLDPC codes (complementary qudit track).
- `logical-catalyst-dyadic-phase` — reusable logical catalysts for surface codes.

## References

- arXiv:2610.21879 — "One generation of the Standard Model as a quantum error-correcting code" (Prakash, Ramya 2026)
- Bravyi & Kitaev 2012 (15-qubit code); triorthogonal codes: Campbell-Howard-O'Gorman / Haah 2017-class
- Anomaly-as-cubic-form lattice viewpoint: currently standard in math-physics literature [refs 6-8 in paper]
- SO(10) grand unification, 16-component spinor, five-oscillator construction
