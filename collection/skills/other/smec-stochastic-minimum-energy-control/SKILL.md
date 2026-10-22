---
name: smec-stochastic-minimum-energy-control
description: Use when minimum-energy control under stochastic noise.
category: ai_collection
arxiv_id: "2610.27599"
---

# SMEC — Stochastic Minimum-Energy Control with Finite-Sample Data-Driven Guarantees

**Source**: arXiv:2610.27599 (Sharma & Katewa, IISc Bengaluru, Oct 2026, eess.SY).
Open-loop minimum-energy steering of stochastic LTI systems to a terminal-neighborhood
constraint, with closed-form solution and finite-sample bounds for the unknown-dynamics
case. All closed-forms below RE-DERIVED from KKT and verified numerically in-session
(29 checks vs direct SLSQP convex solve, agreement 1e-9).

## When to Use
- Open-loop input design steering x(T) near a target xf under process noise, minimizing
  uᵀQ_Tu with a PROBABILISTIC terminal-accuracy constraint (chance / moment / Mahalanobis).
- Data-driven version: (A,B) unknown, only experiment data (inputs + repeated runs).
- Need finite-sample guarantees on cost suboptimality and constraint violation.

## Problem

x(t+1) = Ax(t)+Bu(t)+w(t), w~N(0,Σ), x0~N(0,Σ0). x(T) = Aᵀx(0)+C_Tu_T+N_Tw_T with
C_T = [B AB … A^{T−1}B], N_T = [I A … A^{T−1}]. Error e_T ~ N(μ_e, Σ_e),
μ_e = C_Tu_T−xf, Σ_e = AᵀΣ0(Aᵀ)ᵀ+N_T(I⊗Σ)N_Tᵀ ≻ 0. **Control moves only the MEAN.**

### Constraint menu (all reduce to one QCQP)
- Chance (normalized): P{eᵀΣ_e⁻¹e ≤ ε₁²} ≥ 1−δ. Since eᵀΣ⁻¹e ~ χ²ₙ(λ), λ = μᵀΣ⁻¹μ,
  and the CDF is decreasing in λ ⟺ μᵀΣ_e⁻¹μ ≤ λ* where F_{χ²ₙ(λ*)}(ε₁²) = 1−δ.
- Second moment: E[eᵀΣ⁻¹e] = μᵀΣ⁻¹μ + n ⟹ μᵀΣ⁻¹μ ≤ ε₂².
- Mahalanobis: μᵀΣ⁻¹μ ≤ ε₃² (variance of normalized norm ≤ 2n, enables Chebyshev too).
- Absolute error: eᵀe generalized-χ² (intractable) ⟹ conservative scaled versions via
  λmin(Σ_e): P{eᵀΣ⁻¹e ≤ ε₄/λmin} ≥ 1−δ, or Chebyshev μᵀμ ≤ ε₄−√(tr Σ_e/δ)². Absolute
  versions run the SAME solver with Σ_e→I.

**Unified QCQP**: min uᵀQ_Tu s.t. (C_Tu−xf)ᵀΣ_e⁻¹(C_Tu−xf) ≤ γ, γ ≥ γ_T. Convex (Q_T,Σ_e ≻ 0).

## Closed-Form Solution (KKT derivation — VERIFIED)

Let μ ≥ 0 be the Lagrange multiplier of the active constraint and

```
S(μ)  = Σ_e + μ·C_T Q_T⁻¹ C_Tᵀ            (regularized stochastic Gramian)
u*(μ) = μ·Q_T⁻¹ C_Tᵀ S(μ)⁻¹ xf            (via push-through identity)
g(μ)  = xfᵀ S(μ)⁻¹ Σ_e S(μ)⁻¹ xf          (= constraint value along the KKT path)
```

- g is monotone DECREASING: g(0) = xfᵀΣ_e⁻¹xf (u*=0 case) → g(∞) = γ_T. Solve g(μ*)=γ by
  bisection (paper uses [0,100]). Complementary slackness: active whenever γ < xfᵀΣ_e⁻¹xf.
- **u*(μ) = 0 iff γ ≥ xfᵀΣ_e⁻¹xf**; for γ_T ≤ γ < xfᵀΣ_e⁻¹xf use the formula above.
- Optimal cost identities (both verified to 1e-8):
  `J* = μ*[xfᵀS(μ*)⁻¹xf − γ] = μ*²·xfᵀS⁻¹(C_TQ_T⁻¹C_Tᵀ)S⁻¹xf = xfᵀW_s(μ*)†xf`
  — the middle form defines the **stochastic Gramian** W_s(μ) = μ²S⁻¹C_TQ_T⁻¹C_TᵀS⁻¹,
  the stochastic analogue of W_T = C_TQ_T⁻¹C_Tᵀ (deterministic MEC Gramian).
- Spectral form (degree-2n rational equation in μ): with M = Σ_e^{-1/2}C_TQ_T⁻¹C_TᵀΣ_e^{-1/2}
  = VΛVᵀ and x̃ = VᵀΣ_e^{-1/2}xf:  g(μ) = Σᵢ x̃ᵢ²/(1+μλᵢ)².
- Along the path C_Tu*−xf = −Σ_eS(μ)⁻¹xf (exact), so g IS the terminal Mahalanobis error.

### Feasibility threshold γ_T (Lemma 1)
γ_T = xfᵀ[Σ_e⁻¹ − Σ_e⁻¹C_T(C_TᵀΣ_e⁻¹C_T)†C_TᵀΣ_e⁻¹]xf = residual Mahalanobis distance of xf
beyond Range(C_T); γ_T = 0 ⟺ xf ∈ Range(C_T). Verify: equals min_u (C_Tu−xf)ᵀΣ_e⁻¹(C_Tu−xf).

### Deterministic-MEC limits (verified)
- γ → γ_T: μ*→∞, u* → Q_T⁻¹C_Tᵀ(C_TQ_T⁻¹C_Tᵀ)⁻¹xf (classic Gramian solution) — SMEC
  GENERALIZES DMEC; also Σ_e→0 with xf reachable gives the same limit (infeasible otherwise).
- State+input cost ΣE[xᵀR₀x]+uᵀQ₀u folds to the same QCQP with Q̄_T = Q_T + C_TᵀR_TC_T
  (trace term is u-independent).

## Fundamental Limit as T→∞ (Theorem 4 of paper)

Split A by stability: P⁻¹AP = diag(Aₙ,Aₛ), |λ(An)|≥1, |λ(As)|<1. Define (stable block only)
- W_cs = Σ_k≥0 AₛᵏBₛQ₀⁻¹Bₛᵀ(Aₛᵏ)ᵀ (control Gramian), W_ws = Σ_k≥0 AₛᵏΣₛₛ(Aₛᵏ)ᵀ (noise Gramian)
- γ∞ = (x_s^f)ᵀW_ws⁻¹x_s^f. For 0<γ<γ∞, ν∞ solves
  (x_s^f)ᵀ(W_ws+νW_cs)⁻¹W_ws(W_ws+νW_cs)⁻¹x_s^f = γ, and
  lim J* = (x_s^f)ᵀ(W_ws+ν∞W_cs)⁻¹W_cs(W_ws+ν∞W_cs)⁻¹x_s^f; if γ>γ∞, lim J* = 0.
- Unstable directions become FREE as T grows (their reachability explodes); only the
  stable block costs energy. J* decreases with T iff AΣ0Aᵀ+Σ ⪰ Σ0 (Prop. 3). No horizon
  extension beats this lower bound.

## Data-Driven Framework ((A,B) unknown; Σ0, Σ known)

N_e experiments × N_r independent repetitions: X^(j) = AᵀX0 + C U + N W^(j), with
U ∈ R^{mT×Ne}, Assumption Rank(U)=mT (persistent excitation, Ne ≥ mT).

**ML estimation (structure-enforced)**: Ĉ = X̄U† (X̄ = mean over repetitions),
Σ̂_e = (N_eN_r)⁻¹Σ_j (X^(j)−ĈU)(X^(j)−ĈU)ᵀ. Plug into the QCQP (Theorem 2 machinery).
- Ĉ ~ MN(C, Σ_e/N_r, (UUᵀ)⁻¹) ⇒ Rank(Ĉ)=min(n,mT) a.s. ⇒ plug-in problem feasible a.s.
  (γ̂ = 0 a.s.).
- Σ̂_e residuals = Σ_e^{1/2}G K with K an orthogonal projection of rank N_eN_r−mT ⇒
  GKGᵀ ~ Wishart(n, N_eN_r−mT) ⇒ E[Σ̂_e] = ((N_eN_r−mT)/(N_eN_r))Σ_e (BIASED low;
  unbiased version scales by N_eN_r/(N_eN_r−mT)).
- **Bias-variance insight**: enforcing the structure X = CU cuts the effective sample
  dimension from N_e to mT: Cov(direct-sample estimator) = (N_e/N_r)Σ_e vs
  (mT/N_r)Σ_e for ML — structural estimation wins by factor mT/N_e < 1. Direct sample
  estimators can also return α̂* ∈ Null(U) (û*=0) in regimes where Theorem 2 forbids it.

**Conformal calibration (for absolute-error constraint P{‖e‖²≤ε²} ≥ 1−δ)**:
Split (U,X̄) into est/cal; Ĉ from est set; scores Sᵢ = ‖x⁽ⁱ⁾−Ĉu⁽ⁱ⁾‖² on cal set; empirical
(1−δ)-quantile q₁₋δ. Exchangeability ⟹ P{‖x−Ĉu‖ ≤ q₁₋δ} ≥ 1−δ; triangle inequality
⟹ sufficient constraint ‖Ĉu−xf‖ ≤ ε−q₁₋δ (needs ε ≥ q₁₋δ). Solve the QCQP with
hard constraint (Ĉu−xf)ᵀ(Ĉu−xf) ≤ (ε−q₁₋δ)². Accuracy set by N_est (estimation) and
N_cal (quantile). Trade-off: split sizes.

## Finite-Sample Guarantees

- Ĉ error: ‖Ĉ−C‖ ≤ ρ·ε_C w.p. 1−β, ε_C = √n+√(mT)+√(2log(1/β)) (Davidson–Szarek),
  **ρ = NSR = N_r^{-1/2}‖(AᵀΣ0(Aᵀ)ᵀ+NΣ_wNᵀ)^{1/2}‖₂·λmin(UUᵀ)^{-1/2}** — noise-to-signal.
- Σ̂_e error: ≤ ρ₁ + c·ε_Σ w.p. 1−β with the Wishart dimension factor
  √((N_eN_r−mT+log(1/β))/(N_eN_r)).
- Constraint violation: w.p. ≥ 1−β the TRUE normalized error of û* exceeds γ by at most
  η_β = max{B_β−γ, 0}, B_β = √((1+ρ_β)q̂) + ε_C(β)‖û*‖‖Σ̂_e⁻¹‖ + ε_Σ(β), ρ_β = ε_Σ(β)/λmin(Σ̂_e⁻¹).
- Cost suboptimality: P{|J*−Ĵ*| ≤ ε_J} ≥ 1−β with ε_J = ‖xf‖₂²·ε_tot + γ·ε_ν;
  ε_ν bounds |ν*−ν̂*| via mean-value theorem on f (needs inf|f′| ≥ m_f on the interval),
  ε_tot bounds ‖S(ν*)⁻¹−Ŝ(ν̂*)⁻¹‖ (matrix perturbation + multiplier error). Degrades with:
  estimation error, poor conditioning of S, flat f, small ν*.

## Reference Example (paper §VI)
n=4 stable A, m=3, σ0=0.2, σ=0.3, Q0=diag(2,3,4,5), xf=[4,5,6,7]ᵀ, εᵢ=2.4, δ=0.4 →
γ = λ* = 1.62 (scipy ncx2 quantile); Ne = mT+10 Gaussian inputs, Nr = 100; bisection on
ν∈[0,100]. Known-model chance constraint met with EQUALITY (complementary slackness);
plug-in ML slightly violates; conformal satisfies the original constraint.

## Pitfalls / Transcription Notes
- **pdftotext corrupts this paper's eqs (17)-(21)**: the ½ in f(ν_T) and the placement of
  ν_T inside S_T are displaced superscripts (known corruption class). The verified forms
  above use the Lagrange multiplier μ with S(μ)=Σ_e+μC_TQ_T⁻¹C_Tᵀ; the paper's ν_T is the
  same multiplier up to this factor ambiguity — bisection on g(μ)=γ reproduces the direct
  convex optimum to 1e-9 either way.
- Q₀ is m×m (input weight), NOT n×n — Q_T = I_T⊗Q₀.
- Q0 weighting inside W_cs uses Q₀⁻¹ (per-unit input cost), while the objective uses Q₀.
- Σ̂_e is biased low by (N_eN_r−mT)/(N_eN_r) — scale it back before threshold/quantile use.
- γ̂=0 a.s. in the plug-in problem (Ĉ a.s. full rank) — don't read plug-in feasibility
  as true feasibility; that's what the violation bound η_β is for.
- The limit theorem needs P splitting A into stable/unstable; W_cs/W_ws are STABLE-block
  quantities only.
