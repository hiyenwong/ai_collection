---
name: quartic-certificate-pure-state-tomography
description: Certify pure-state Pauli tomography via quartic e4 spectral certificates.
category: ai_collection
trigger: UDP, UDA, pure-state tomography, Pauli measurement design, omitted observables, four-set-free, uniqueness certificate, measurement kernel, compressed tomography, quantum state certification
---

# Quartic Certificates for Pure-State Tomography with Pauli Measurements

**Source**: Hengjian Li, Baisong Sun, Bei Zeng (UT Dallas), arXiv:2610.12320 [quant-ph + math-ph cross], Oct 2026.

## When to Use

- Designing reduced Pauli-basis tomography when the state is known pure (saves observables).
- Certifying that a chosen retained-observable set uniquely determines EVERY pure state (universal uniqueness), not just generic states.
- Distinguishing UDP (unique among pure states) vs UDA (unique among ALL density operators — excludes mixed-state explanations).
- Explaining/avoiding failing sets in 3-qubit measurement schemes; verifying variational tomography schemes analytically.

## Core Framework

### 1. Setup: measurement kernel
- Retained family A = {I, A_1..A_m}; data = Tr(A_j ρ). Two states indistinguishable ⟺ difference lies in Hermitian kernel K_A = {∆=∆†: Tr(∆)=0, Tr(A_j∆)=0}.
- With omitted Pauli support T (unmeasured nonidentity Paulis), K_A = real span V_T of omitted Paulis.
- **Spectral criteria** (∆ ∈ K_A nonzero): UDP fails ⟺ rank ∆ = 2; UDA fails ⟺ n₊(∆)=1 or n₋(∆)=1 (pure-vs-mixed difference has exactly one positive eigenvalue: ρ_φ − σ ⪯ rank-1). Universal uniqueness = kernel criterion holds for ALL nonzero ∆.

### 2. The quartic certificate (the central tool)
- For traceless Hermitian A with eigenvalues λ_1..λ_d (d = 2^n), define **e₄(A)** = fourth elementary symmetric polynomial Σ_{i<j<k<l} λ_iλ_jλ_kλ_l.
- Homogeneous quartic in Pauli coefficients of A. **e₄(A) > 0 ⇒ A has ≥2 positive AND ≥2 negative eigenvalues ⇒ A cannot be a pure-vs-anything difference ⇒ certifies universal UDA.**
- Exact quartic identity: e₄(A) decomposes into (a) nonneg commuting squared-pair terms with positive coefficient d(d−6)/4 (valid d ≥ 8, i.e. n ≥ 3), and (b) monomials from **commuting zero-sum four-sets**.

### 3. Four-set-freeness — the finite combinatorial test
- **Commuting zero-sum four-set**: four DISTINCT pairwise-commuting Pauli labels u,v,w with u+v+w+x=0 (multiply to ±I).
- **Theorem 1**: n ≥ 3 and T contains NO commuting zero-sum four-set ⇒ e₄(A) ≥ [d(d−2)/8] Σ a_u⁴ > 0 for every nonzero A ∈ V_T ⇒ **universal UDA, no optimization over states or coefficients — just binary addition + symplectic commutation checks.**
- Theorem 2 (3 qubits): four-set-freeness is also NECESSARY — exact characterization of UDP and UDA. Each four-set F = {u,v,w,u+v+w} yields rank-2 kernel operator λ(|ψ+⟩⟨ψ+| − |ψ−⟩⟨ψ−|) hiding a population difference between two orthogonal common-eigenbasis states.
- **945 minimal failing sets** = 63·30·12/24 — all in one Clifford orbit of {IIZ, IZI, ZII, ZZZ} (which hides |000⟩ vs |111⟩ population). Structure: 135 maximal commuting label spaces L × 7 sign-pattern four-sets each.
- n ≥ 4: four-set-freeness sufficient but NOT necessary — eigenvalue multiplicities can preserve UDA even with a four-set omitted.

### 4. Commuting omitted supports — UDP = UDA (any n)
- **Theorem 3**: if T pairwise-commuting, Clifford-diagonalize T to Z-strings. Then every pure–mixed ambiguity forces a pure–pure ambiguity (rank-2 population difference |x0⟩⟨x0| − |y⟩⟨y|) ⇒ **UDP ⟺ UDA**.
- Exact criterion: universal uniqueness ⟺ **span_F2 S_Z = F_2^n** (retained diagonal labels distinguish every pair of computational basis states).
- Separation between UDP and UDA at n ≥ 4, if it exists, requires a NONcommuting omitted set containing a commuting zero-sum four-set.

## Methodological Lessons (reusable patterns)

1. **Turn uniqueness into kernel spectral conditions**: "is the measurement injective on pure states?" reduces to rank/inertia of nonzero kernel elements — check rank(∆)≥3 AND n±(∆)≥2 for all nonzero kernel directions.
2. **Symmetric-polynomial certificates**: e₄ (or higher e_k) converts a universally-quantified spectral property into a polynomial-positivity check on the measurement design — certification without solving optimization problems.
3. **Combinatorialize the certificate**: the quartic identity's only negative terms come from small forbidden configurations (commuting zero-sum four-sets) — "local obstruction → global failure" structure; a finite pattern test replaces an infinite family of states.
4. **Clifford orbits classify failures**: all 3-qubit minimal failing sets are one Clifford orbit — when analyzing measurement ambiguity, quotient by the symmetry group first; count = orbit-counting arithmetic (63·30·12/24).
5. **Distinguish UDP from UDA only when noncommuting**: commuting omitted supports make pure–mixed ambiguity collapse to pure–pure ambiguity — a general principle: diagonal (population-only) kernels can't mix spectra.
6. **Counting minimal obstructions explains numerics**: prior variational searches found 945 failing sets numerically; the analytic characterization retro-explains them. When a numerics-only result exists, look for the finite family of minimal algebraic obstructions.

## Connections

- Heinosaari–Mazzarella–Wolf (general measurement kernel criteria); Ma et al. optimal 11/31 observable counts; compressed sensing low-rank recovery; GKR (Goemans–Kraenzlin–Ruskai?) classical uniqueness; stabilizer measurement design; Pauli grouping / classical shadows (different axis: sample efficiency vs determinism).

## Verification Notes

- Theorems 1–3, the 945 count, and the commuting-case criterion quoted from arXiv:2610.12320v1 PDF (Secs. II–V verified against extracted text; Eqs (60)–(77) structure confirmed).
