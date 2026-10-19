---
name: quantum-u-statistics-efficiency
description: Unique Cramér-Rao-efficient quantum U-statistic estimators.
version: "1.0.0"
source: arXiv:2609.08745v2
source_title: "Uniqueness, Cramér-Rao Efficiency and Concentration Bounds for Quantum U-Statistics"
authors: "Ayanava Dasgupta, Naqueeb Ahmad Warsi, Premanshu Chatterjee"
published: 2026-09-30
categories: quant-ph, math.ST
trigger_words:
  - quantum U-statistic
  - polynomial functional estimation
  - Cramér-Rao efficiency
  - permutation-invariant kernel
  - marginal kernel gradient
  - Hoeffding decomposition quantum
  - Bernstein concentration quantum
  - moderate deviation principle
  - Bures chi-square divergence estimation
  - quantum Fisher information functional
---

# Quantum U-Statistics: Uniqueness, Cramér–Rao Efficiency, and Concentration

**Source**: Dasgupta, Warsi, Chatterjee (Indian Statistical Institute Kolkata), arXiv:2609.08745v2, Sep 2026. Statistics × quantum estimation theory. Extends Guta–Butucea quantum U-statistics (JMP 2010) with uniqueness, CR-efficiency, and finite-sample tails.

## When to Use

- Estimating scalar polynomial functionals of an unknown quantum state ρ from n i.i.d. copies (purity Tr[ρ²], k-th order purity Tr[ρᵏ], Hilbert-Schmidt distance, maximal/sandwiched/Bures χ² divergence, QFI via Krylov shadow tomography)
- Deciding whether adaptive measurement / preliminary tomography is needed for CR-optimal estimation (answer: no, if permutation-invariant U-statistics allowed)
- Deriving finite-sample (non-asymptotic) tail bounds for quantum estimators
- Relaxing spectral lower-bound assumptions (λ_min(σ) ≥ δ) in divergence estimation

## Core Framework

### 1. Polynomial functional representation
Any scalar polynomial functional reduces to interleaved trace monomials:

    f(ρ) = c₀ + Σᵢ Tr[A⁽¹⁾ⱼ₁ ρ A⁽²⁾ⱼ₂ ρ ⋯ ρ A⁽ⁱ⁾ⱼᵢ]

Examples (coefficient choices): purity k=2, A=I; HS distance A₁⁽¹⁾=−2σ; Bures χ² via integral rep (below).

### 2. Kernels and the cyclic-permutation trace identity
Degree-m monomial f_B(ρ)=Tr[Bρᵐ] becomes an m-copy observable via backward cyclic permutation P_γₘ:

    Tr[P_γₘ(A₁⊗⋯⊗Aₘ)] = Tr[A₁A₂⋯Aₘ]   (generalizes SWAP identity Tr[S(X⊗Y)]=Tr[XY])

Self-adjoint kernel: O_B = ½(P_γₘ(B⊗I) + h.c.). Then symmetrize by twirling over Sₘ (quantum Rao–Blackwell): variance can only decrease (Kadison/operator convexity proof, Prop. 1).

### 3. Marginal kernel ↔ gradient equivalence (Lemma 1, key structural result)

    ∇f_B(ρ) = m·O^sym_{B,1},   O^sym_{B,1} := Tr₂..ₘ[O^sym_B(I⊗ρ^{⊗(m−1)})]

For mixed-degree polynomials embedded via identity-padding: k·O^sym_{k,1} = ∇f(ρ) + C(ρ)·I — the identity shift is invisible to traceless (physical) perturbations. **Partial trace of the kernel = functional derivative.** This is the quantum analog of classical conditional expectation.

### 4. Uniqueness theorem
The quantum U-statistic (uniform average of kernel over all k-subsets of n copies) is the **unique** unbiased permutation-invariant n-copy extension of a k-copy kernel. Proof: permutation-invariant operator space is spanned by tensor powers {A^{⊗n}}; a perm-invariant Hermitian operator with zero expectation on ALL states is the zero operator → difference of any two unbiased perm-invariant extensions vanishes.

### 5. Universal variance expansion + CR efficiency
Hoeffding decomposition (Guta–Butucea): leading variance from first-order marginal only:

    Var_{ρ^{⊗n}}(U_{n,k}) = Var_ρ(∇f(ρ))/n + O(1/n²)

The leading term equals the multiparameter SLD quantum Cramér–Rao bound (orthogonal nuisance-parameter setup, Suzuki et al. framework): the primary SLD is proportional to ∇f(ρ), so V_CR = Var_ρ(∇f(ρ)). **Consequence**: U-statistics achieve CR efficiency with state-INDEPENDENT measurement construction — no adaptive protocols, no tomography, no state-dependent SLD-basis measurement needed.

### 6. Bures χ² — spectral condition relaxed
New exact integral representation via Lyapunov equation:

    χ²_B(ρ∥σ) = 2∫₀^∞ Tr[(ρe^{−τσ})²]dτ − 1

Known reference σ ⇒ integral evaluates in σ's eigenbasis to finite linear combination of quadratic terms in ρ ⇒ polynomial functional. Bădescu–O'Donnell–Wright's λ_min(σ) ≥ δ is **sufficient but not necessary**: bounded Var_ρ(∇χ²_B) is the weaker, physically natural condition; explicit (ρₙ, σₙ) families have λ_min(σₙ)→0 with uniformly bounded variance.

## Concentration Bounds (Section V)

### MGF bound with exact variance isolation
Moment expansion over overlapping k-subsets mapped to **intersection graphs**, higher-order connected moments bounded by **spanning-tree counting (Cayley's formula r^{r−2})**:

    Tr[ρ^{⊗n} e^{tŪ}] ≤ exp(t²Var/2 + Σ_{r≥3} |t|^r 2^r r^{r−2} k^{2r−2} ‖O‖^r_∞ / (r! n^{r−1}))

converges for 2ek²|t|‖O^sym_k‖_∞/n < 1. Reparameterize t = sn to factor out n; define auxiliary penalty Ψ(s).

### Closed-form Bernstein-type bound (Cor. 9)

    Pr[|Z_{U} − f(ρ)| ≥ ε] ≤ 2 exp(−nε² / (2nVar_{ρ^{⊗n}}(U) + 4√(8e³k⁴‖O‖³∞·ε) + 8ek²‖O‖∞·ε))

Derivation pattern: cubic Stirling-based geometric-series bound on Ψ(s); **numerically stable test parameter** s* = ε/(√(nVₙ) + 2√(Aε) + 2Bε) obtained by rationalizing the quadratic root to avoid catastrophic cancellation at small ε (a reusable numerical-analysis insight). Small-ε regime → CLT Gaussian (variance-dominated); large-ε → spectral sub-exponential tail.

### Moderate Deviation Principle (Thm 3)
For εₙ → 0 with nεₙ² → ∞:

    Pr[|Z_U − f(ρ)| ≥ εₙ] ≤ 2 exp(−nεₙ²/(2Var_ρ(∇f(ρ))) · (1 − O(εₙ) − O(1/n)))

If additionally nεₙ³ → 0 (εₙ = n^{−α}, 1/3 < α < 1/2): **purely Gaussian tail governed solely by QFI** Var_ρ(∇f). Third-moment skewness corrections appear only when εₙ decays slower than n^{−1/3} — that is the CLT↔LD bridge point.

## Reusable Method Patterns

1. **Marginalization-equals-differentiation**: for permutation-invariant multi-copy observables, the partial trace marginal computes the functional gradient — use to derive CR bounds without explicit SLD computation.
2. **Uniqueness via spanning**: to prove an averaged estimator is canonical, show the invariant operator space is spanned by {A^{⊗n}} so any unbiased invariant competitor differs by a zero-expectation operator ≡ 0.
3. **Twirling = quantum Rao–Blackwell**: symmetrize any kernel over the symmetry group leaving the product state invariant; expectation preserved, variance never increased (Kadison inequality).
4. **Cayley spanning-tree moment counting**: to bound r-th connected moments of subset-overlap statistics, count spanning trees r^{r−2} instead of building minimal subgraphs — converts intractable combinatorial sums to geometric series.
5. **Test-parameter rationalization**: sup_{s}(sε − Vs²/2 − As³) at rationalized s* avoids catastrophic cancellation; general trick for Bernstein-style closed forms.
6. **Lyapunov integral representations**: χ²-type divergences with SLD inverse superoperators admit e^{−τσ} heat-kernel integral forms that reduce (known σ) to polynomial functionals.

## Pitfalls

- Kernel must be permutation-symmetrized BEFORE marginal analysis; asymmetric kernels have perm-dependent marginals.
- The identity shift C(ρ)I in the gradient correspondence is harmless only for traceless perturbations — careful when parameterizing non-density-matrix perturbations.
- Uniqueness holds within unbiased + permutation-invariant class; biased or non-invariant estimators (e.g. shadow tomography predictors) are outside the theorem.
- CR efficiency is asymptotic (1/n leading); the O(1/n²) term comes from higher-order Hoeffding marginals and matters at small n.
- Degenerate geometry Var_ρ(∇f(ρ)) = 0 (e.g. maximally mixed state for purity) breaks MDP non-degeneracy; higher-order scaling must be re-derived at such points.

## Key Formulas

| Object | Formula |
|---|---|
| Monomial kernel | O_B = ½(P_γₘ(B⊗I^{⊗m−1}) + h.c.), Tr[O_B ρ^{⊗m}] = Tr[Bρᵐ] |
| Gradient–marginal | ∇f_B(ρ) = m·O^sym_{B,1} |
| Variance expansion | Var(U_{n,k}) = Var(∇f)/n + O(n⁻²) |
| Bernstein bound | ≤ 2exp(−nε²/(2nV + 4√(8e³k⁴‖O‖³ε) + 8ek²‖O‖ε)) |
| MDP Gaussian rate | nεₙ²/(2Var_ρ(∇f)) for n^{−1/3} ≫ εₙ ≫ n^{−1/2} |
| Bures χ² integral | 2∫₀^∞ Tr[(ρe^{−τσ})²]dτ − 1 |

## Related
- Guta & Butucea, "Quantum U-statistics", J. Math. Phys. 51 (2010) — Hoeffding decomposition origin
- Bădescu, O'Donnell, Wright (STOC 2019) — quantum state certification, spectral condition
- Suzuki, Hayashi et al. — multiparameter nuisance-parameter QCRB framework
- De Palma & Pastorello — quantum concentration via local norms (alternative route)
