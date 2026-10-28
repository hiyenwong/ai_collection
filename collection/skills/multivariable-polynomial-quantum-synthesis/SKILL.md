---
name: multivariable-polynomial-quantum-synthesis
description: "Multivariable polynomial transformations of noncommuting matrices via joint block access and Schur-Agler realization. Complete constructive synthesis: compact coefficient recurrence → residual coordinates → semidefinite defect certificate → Douglas factor → quantum circuit. Use when synthesizing quantum algorithms for polynomials of several noncommuting matrices (multivariable QSP), reducing LCU normalization blowup for ordered matrix products, or transforming coherent Kraus/channel implementations. Activation: multivariable QSP, noncommuting polynomial synthesis, Schur-Agler certificate, joint block encoding polynomial, 多变量量子信号处理, 非对易多项式合成."
---

# Multivariable Polynomial Quantum Synthesis

Complete constructive theory for compiling polynomials of **several noncommuting matrices** into quantum circuits — the multivariable generalization of QSP/SVT. Source: Shen, Wu, Yuan, Zhang, Zhang, "Quantum Algorithms for Multivariable Polynomial Transformations: From Efficient Synthesis to Quantum Channel Transformations" (arXiv:2610.08714, Oct 2026).

## When to Use

- Target polynomial p(A) = Σ_w c_w A_{j1}···A_{jd} mixes **matrix multiplication order** (e.g. commutators A_1A_2 − A_2A_1,nested transforms), and matrices are blocks of **one shared unitary**.
- Term-by-term LCU would be normalized by Σ|c_w|·(encoding scales) — potentially **exponentially worse** than the true polynomial norm ‖p‖. This method achieves β ≤ (1+τ)‖p‖.
- Coefficients given by a **compact finite-state recurrence** c_w = λ T_{j1}···T_{jd} r_0 (rational series / weighted automaton) that would expand to exponentially many words.
- Need **channel-level** transformations: polynomial maps on a coherent Kraus implementation, or controllers from causal Choi data.

Not needed for single-matrix polynomial transforms — use standard QSP/QSVT there.

## Input Model: Joint Block Access

All matrices A_1,…,A_k (‖A_j‖ ≤ 1, acting on n-dim signal) are placed as blocks of ONE unitary U_A, queried forward-only. Three layouts (Δ: a×b block matrix, f_{μν,j} its structure constants):

| Layout | Block | Constraint | Use |
|---|---|---|---|
| Diagonal | Δ_diag = diag(A_1,…,A_k) | max_j ‖A_j‖ ≤ 1 | independent contractions via coherent selection |
| Row | Δ_row = [A_1 … A_k] | Σ_j A_j A_j† ⪯ I | one query removes one degree (D queries exact) |
| Column | Δ_col = (A_1;…;A_k) | Σ_j A_j† A_j ⪯ I | coherent Kraus implementations |

Label 0 carries the **identity branch** — lets terms of different degrees share one query count. A selector U_sel applies block-encoding U_j at label j and identity at label 0; known rotation converts selector ↔ weighted row.

## Synthesis Pipeline (5 stages)

```
recurrence (s states, degree D)
   → [1] residual basis f_1..f_r (r ≤ s+1)      Lemma 3.1: poly bit time
   → [2] SDP feasibility: find S,T ⪰ 0          Prop 3.5: ellipsoid, poly bits
         β²E†E − P†P = S + Φ(T)
   → [3] Douglas factor V = Y·T₀⁻¹·X†           Lemma 3.4: strict contraction
   → [4] degree-combination circuit              Sec 4: weights v_t or row factor
   → [5] unitary completion of each contraction  Sec 4.2: finite gates, error ε
```

### Stage 1 — Residual coordinates (the key compression)

Left residual ∂_j f deletes the first letter: ∂_j f(x) = Σ_w f_{jw} x_w. All residuals of the recurrence share its state coordinates; the span of {1, residuals of p} is closed under every ∂_j and has **r ≤ s+1** dimensions even when p has exponentially many words (e.g. (x_1+x_2)^D: 2^D words, r = D).

Common basis: g = (1, x_j f_ℓ)_{j,ℓ}, h = 1+kr. Numerical arrays:
- a_0, A_j^res (residual maps), p_j (target residuals) — Eq (3.1)-(3.2)
- E (1×h), J (r×h), P (1×h), L_j (r×h zero-one) — Eq (3.4); identities Eg=1, Jg=f, Pg=p, L_j g = x_j f.

### Stage 2 — Semidefinite defect certificate

The norm bound ‖p‖_{SA,Δ} ≤ β ⟺ **affine equation in two PSD matrices** (Theorem 3.2):

β² E†E − P†P = S + Φ(T),  S ⪰ 0 (h×h), T ⪰ 0 (br×br)

Φ(T) = Σ_α E_α† T E_α − Σ_μ M_μ† T M_μ, with E_α (br×h, J in block row α) and M_μ built from f_{μν,j} L_j. **Completeness**: restricting auxiliary polynomials to the residual span loses nothing — hereditary-positivity separation shows any feasible norm bound has a certificate in this space. Strict margin ν (‖p/γ‖ ≤ ν < 1) makes discovery polynomial-bit via rounded ellipsoid; feasibility is **exactly verified** against rational inequalities, so a returned certificate is valid even if the promise was false (failed cap ⇒ certified lower bound B > b_0 → relative norm estimation to factor (1+η), Theorem 3.6).

### Stage 3 — Contraction extraction (Douglas factor)

Given S,T ≻ 0: K = T^{1/2} (m = br rows),
- X = [K M_1; …; K M_a; E] ((am+1)×h), Y = [K E_1; …; K E_b; P] ((bm+1)×h)
- T₀ = X†X (rational, invertible); **V = Y T₀⁻¹ X†** = [[A,B],[C,D]], ‖V‖² ≤ 1 − μ/t₀ < 1.

V realizes q: q_∅ = D, q_{j1···jd} = C F_{j1} A F_{j2} ··· A F_{jd} B, with F_j^{(m)} = [f_{μν,j} I_m]. Entries computable to p bits in poly time (guarded square roots/inverses).

### Stage 4 — Circuit assembly

**General joint input (Q = O(D/√τ) queries):** choose weights v_0..v_Q, Σv_t² = 1. Splitting/collection ratios α_t = v_t/u_t, ζ_t = u_{t+1}/u_t, ξ_t = v_t/z_t, γ_t = z_{t−1}/z_t (u,z = tail/prefix norms, Eq 4.1). Update per stage (Eq 4.2): injection α_t·s into transfer update, pending ζ_t·s, collection ξ_t(C h + α_t D s) + γ_t y. Amplitude entering at t and collected at r contributes degree r−t−1 with weight v_t v_r.

**Row input (exactly D queries, optimal):** certificate completes target to a polynomial column; each step strips one degree, reversed by one row query. Matches the degree lower bound for exact synthesis.

**Degree compensation:** before realization, reweight each homogeneous degree by known scalars so the strict-norm promise holds; the certificate uses the same residual coordinates.

### Stage 5 — Unitary completion

Each contraction V_t is completed to a unitary on ancilla (preserving the joint contraction inequality Eq 2.18); oracle calls interleaved with known gates W_t. Total circuit: (⟨0|⊗I) 𝒰_A (|0⟩⊗I) = p(A)/β with error ε, gate count polynomial in description length, register width, τ^{-1/2}, log(1/ε).

## Guarantees

| Input | Queries | Normalization | Classical cost |
|---|---|---|---|
| General joint | O(D/√τ) | β ≤ (1+τ)B | poly(desc, τ^{-1/2}, log 1/ε) |
| Row-block | exactly D | β ≤ (1+τ)B | poly(desc, log 1/τ, log 1/ε) |

B = ‖p‖_{SA,Δ} (free Schur-Agler norm over all admissible tuples/sizes). Both classical synthesis and gate entries are polynomial-bit computable.

## Channel Transformations (Section 5)

- **Joint polynomial outputs:** F_b(K) on distinct output labels → after label test, CP map M_β(ρ) = β^{-2} Σ_b F_b(K) ρ F_b(K)†. One certificate bounds the whole output column → trace-nonincreasing. Query count governed by max degree.
- **Coherent Kraus access** (column layout): polynomial operations with **coherent interference among Kraus histories** — beyond channel-only access.
- **Causal Choi data → quantum combs:** separate gate compiler (Appendix D) synthesizes fixed-order controllers from explicit causal Choi matrices.

## Worked Example (verified in scripts/)

q(x) = (1 + x_1 x_2)/4 on the diagonal domain (the paper's running example):
- Residual basis f = (1, x_2), g = (1, x_1, x_1x_2, x_2, x_2²), h=5, r=2, b=2, m=br=4
- Certificate (Eq 3.7): T = diag(1,8,16,1)/64, S = ([43,0,−4,0,0],[0,1,0,0,0],[−4,0,4,0,0],[0,0,0,7,0],[0,0,0,0,1])/64
- Extracted blocks (Eq 3.20): A = (e_2/√2 + e_8/4)e_7^T, B = e_1/8 + e_7/2, C = e_2^T/√2, D = 1/4
- Only nonzero path: C F_1 A F_2 B = 1/4 → generates exactly (1+x_1x_2)/4 with all other words zero.

`scripts/verify_worked_example.py` reconstructs all of this numerically (numpy only): certificate identity, Douglas extraction, coefficient generation, contractivity, and the norm bound ‖q(A)‖ ≤ 1 on random noncommuting contractive tuples.

## Relation to Concurrent Work

Low (concurrent): multivariate QSP via Schur-Agler realizations + analytic transfer functions. This work: complete synthesis from **compact rational descriptions**, near-optimal uniform normalization, polynomial bit complexity, channel transformations. For single-variable completion/phase recovery see Haah factorization, Berntson-Sünderhauf canonical complementary polynomials, Alexis et al. nonlinear Fourier analysis.

## Tools

- execute_code / terminal: run verification scripts (numpy sufficient)
- write_file: certificate/circuit parameter files

## Error Handling

- **Certificate search fails at threshold b_0** → norm lower bound B > b_0 (use for bisection, Theorem 3.6)
- **Singular separator in completeness proof** → kernel argument (ker R_H ⊆ ker Z_{j,H}) keeps pseudoinverse construction well-defined
- **Strict margin missing** → degree compensation reweighting (Sec 4.1) before applying Prop 3.5
- **Joint oracle not supplied, only controlled U_j** → build selector with one controlled call per input (distinct resource model)

## Related Skills

- `analytic-quantum-control-qsp` (univariate QSP)
- `fourier-lcu-quantum-optimization`, `pauli-sparse-counterdiabatic-qaoa` (LCU-based alternatives)
- `quantum-channel-transformations` family: `girsanov-quantum-control`, `non-unitary-qml-fisher-efficiency`
