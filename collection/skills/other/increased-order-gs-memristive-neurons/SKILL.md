---
name: increased-order-gs-memristive-neurons
description: Use when syncing memristive HR neurons across unequal dims.
category: neuroscience
---

# Increased-Order Generalized Synchronization (IOGS) in Memristive Neurons

**Paper**: "Increased-Order Generalized Synchronization in Memristive Neurons: Analytical and Data-Driven Approaches" — Dennis Mustafić, Marius E. Yamakou (FAU Erlangen-Nürnberg), arXiv:2610.25164 (18 Oct 2026, nlin.AO + math.DS). Code: github.com/dennismstfc/iogs-analytical-vs-ml. DFG grant YA 764/1-1.

## When to Use
- Synchronizing drive/response systems with UNEQUAL phase-space dimensions (here 4D drive → 5D response; response carries an extra slow-adaptation variable w_r ~ intracellular calcium dynamics)
- Memristive Hindmarsh–Rose neurons with parameter mismatch and a switchable memristor (electromagnetic-induction coupling, G(u)=|u+1|−|u−1| piecewise-linear: −2 / 2u / 2)
- Adaptive synchronization control with Lyapunov guarantees when a switching nonlinearity must be RETAINED explicitly (not canceled by control)
- Learning synchronization maps from data WITHOUT governing equations (memoryless NG-RC + self-supervised dynamical consistency)

## System Setup
- Drive X_d=(x,y,z,u)∈R⁴: HR + memristive autapse k(h+fu²)x + memristor state u with dynamics −ξu+mG(u)+x
- Response X_r∈R⁵: adds slow adaptation ẇ_r=η̄[γ(y_r−y₀)−ρw_r], feeding back via −σ̄w_r; control v∈R⁵ additive on every component
- Parameter mismatch: 5 uncertain response coefficients (k̄,σ̄,s̄,ξ̄,η̄) with adaptive estimates; nominal targets k=0.87, σ=0.0278, s=5.2, ξ=1.0, η=0.0009; shared params a=1, b=3, c=1, p=5, f=0.2, h=0.3, m=0.5, r=0.006, x₀=−1.56, I=3.1; response-only y₀=−1.619, γ=3, ρ=0.9573
- Drive bursts, response spikes sustained (I=5.1 uncontrolled); chaos windows confirmed by Benettin Lyapunov exponents on bifurcation diagrams

## Analytical Approach — map selection for PROVABILITY
1. Prescribe nonlinear map φ: R⁴→R⁵ = [x+α₁sin x; y+α₂x²+α₃u²; z+α₄xy; **u**; β₀+β₁x+β₂y+β₃z+β₄xu+β₅cos u], at least one nonlinear coefficient nonzero
2. **KEY DESIGN CHOICE φ₄ = u**: preserves the natural memristive error e₄=u_r−u so the switching difference m[G(u_r)−G(u)] stays EXPLICIT in the closed-loop error dynamics — control cannot hide the memristive nonlinearity
3. Controllers (Eq 14): v_i = φ̇_i − [intrinsic response terms] − λ_i e_i for i∈{1,2,3,5}; v₄ = x − x_r cancels ONLY the direct membrane-potential mismatch, NOT the switching difference
4. Adaptive laws (Eq 15): k̄̇=−Φ₁e₁, σ̄̇=Φ₂e₂, s̄̇=−Φ₃e₃, ξ̄̇=Φ₄e₄, η̄̇=−Φ₅e₅ with regressors Φ₁=(h+fu_r²)x_r, Φ₂=w_r, Φ₃=r(x_r−x₀), Φ₄=u_r, Φ₅=γ(y_r−y₀)−ρw_r — exactly cancel ALL parameter-error cross terms in V̇
5. Lyapunov V = ½(‖e‖² + k̂²+σ̂²+ŝ²+ξ̂²+η̂²) ⇒ V̇ = −λ₁e₁²−λ₂e₂²−λ₃e₃²−λ₅e₅² + Ψ(e₄), where Ψ(e₄;u,u_r,m) = [−e₄ + m(G(u_r)−G(u))]e₄

## Case-Wise Switching Analysis (technical core)
- Ψ partitions the (u,u_r) plane into 9 cases C1–C9:
  - C1 (u≥1,u_r≥1), C9 (u≤−1,u_r≤−1): ALWAYS strictly dissipative, Ψ=−e₄² (µ≤1)
  - C5 (both in (−1,1)): Ψ=(2m−1)e₄² → dissipative iff m<1/2; at m=0.5: Ψ=0
  - C2,C3,C4,C6,C7,C8 (mixed regions): dissipativity conditional on trajectory position and m
- Dissipative set D_µ = union of case regions where Ψ ≤ −µe₄²; complement N_µ = non-dissipative

## Main Theorems (know the exact scope)
- **Thm 4.1 (asymptotic IOGS)**: IF (u(t),u_r(t)) ∈ D_µ ∀t (uniform strict dissipativity) + bounded drive + global existence THEN V̇ ≤ −α‖e‖² with α=min{λ₁,λ₂,λ₃,µ,λ₅}; Barbalat ⇒ ‖e‖→0; parameter-estimation errors bounded. SUFFICIENT, not necessary.
- **Thm 4.3 (practical, switching-independent)**: |G|≤2 ⇒ |G(u_r)−G(u)|≤4; Young's inequality: m[G(u_r)−G(u)]e₄ ≤ (ε/2)e₄² + 8m²/ε ⇒ V̇ ≤ −α‖e‖² + C with C=8m²/ε, α=min{λ₁,λ₂,λ₃,λ₅,1−ε/2}, ε∈(0,2). V decreasing whenever ‖e‖>δ=√(C/α)=√(8m²/(εα)). **Remark 1 (honest): a Lyapunov DECREASE condition, NOT a proof of ultimate boundedness or practical synchronization.**
- Remark 3: without persistence-of-excitation, parameter estimates converge to constants — synchronization ≠ identification

## Numerical Honesty Pattern (rigor exemplar)
- At m=0.5: monotonicity + 2-Lipschitz G ⇒ Θ(t) = Ψ/e₄² = −1 + ½·[G(u_r)−G(u)]/e₄ ∈ [−1,0] — Ψ≤0 throughout, BUT the trajectory repeatedly visits C5 with e₄≠0 ⇒ Θ=0 there ⇒ uniform strict dissipativity VIOLATED
- Errors still decay: ‖e‖ → 6.19×10⁻⁷ at t=5×10⁵ (RK45, rtol 1e-6/atol 1e-8, 14-state closed loop: 4 drive + 5 response + 5 estimates); max 1.22×10⁻⁵ over final 20%; e₃ slowest
- Paper explicitly frames this as "numerical evidence of synchronization beyond the sufficient conditions" — NOT a corroboration of Thm 4.1 under its hypotheses (V̇≤0 gives boundedness only)
- Parameter recovery observed (most <3×10⁻⁹; ŝ slowest at −1.53×10⁻⁴) but no identification theorem claimed

## Data-Driven Approach — map selection for LOW CONTROL EFFORT
1. **Memoryless NG-RC predictors** (one per system): features O(t)=[1; X̃(t); distinct monomials of X̃, total degree 2..q]; ridge readout W_out=(YOᵀ)(OOᵀ+νI)⁻¹ on standardized finite-difference rates, Δt=0.02; q≤3 (35 drive / 56 response features, includes constant); (q,ν) via Bayesian optimization (GP surrogate + expected improvement, 30 trials); memoryless valid for deterministic full-state systems AND permits evaluating F̂_r at mapped drive / controlled response states where no history exists. Test RMSE 3.7e-3 / 3.3e-3
2. **Affine map in standardized coordinates**: φ_θ(X_d) = X̄_r + D_r(AX̃_d + b), A∈R⁵ˣ⁴ + b∈R⁵ = 25 trainable params; family includes reference correspondence φ₀ (identity on 4 shared components + w_r at response training mean); standardization makes A entries dimensionless/comparable
3. **Self-supervised dynamical consistency loss**: L_dyn = (1/N)Σ‖aₙ−bₙ‖²/Δt² with aₙ = φ_θ(X_d,n + Δt·F̂_d(X_d,n)) (advance-then-map), bₙ = φ_θ(X_d,n) + Δt·F̂_r(φ_θ(X_d,n)) (map-then-advance) — seeks an approximately invariant graph under learned dynamics; NO paired drive-response data needed (cf. conjugate mappings, Bramburger–Brunton–Kutz)
4. **Anti-collapse (VICReg-adapted)**: constant map φ≡c with F̂_r(c)=0 yields L_dyn=0! Add L_var = Σ max(0, 1−√S_ii) (hinge keeping target std ≥ unit scale) + L_cov = Σ_{i≠j}(S_ij−R_ij)² matching off-diagonals to the OBSERVED response covariance R — unlike VICReg which drives them to zero. S(θ)=A₁:₄C_dA₁:₄ᵀ. Fifth component exempt (slow w_r). λ_var=λ_cov=1
5. Optimization: init A=0, b=0 (NO coordinate-correspondence prior); L-BFGS-B with exact gradient, N=14400 states (1800 × 8 recordings); objective 75.6 → 8.3×10⁻³ (763 iters); learned A₁:₄ near-diagonal (diag∈[0.98,1.01], off-diag<0.1, singular values∈[0.95,1.05]); RK4-oracle diagnostic L_dyn=3.3×10⁻³ confirms consistency with true dynamics
6. **Sampled-data control** (Eq 49–50): v(t) = [φ_θ(X̂_d(t+Δt)) − X̂_r^free(t+Δt) + ζ·e_θ(t)]/Δt with ζ=e^(−κΔt) — three terms: target-rate prediction + response-drift compensation + proportional error feedback (effective gain (1−ζ)/Δt → κ as Δt→0); zero-order hold between samples; RK4 with 4 substeps between samples; κ=1, control on at t=100

## Data-Driven Results (8 initial-condition pairs, final 50 time units)
- Learned map: median tracking error 1.4×10⁻³, control effort 2.1×10⁻²
- Reference map φ₀: 4.8×10⁻³ and 1.7×10⁻¹ → **learned map ≈8× lower median control effort AND better tracking accuracy**
- Oracle predictors (RK4 of governing equations): 2.3×10⁻⁴ → predictor error dominates the residual
- Caveats (stated): full-state sampling + full additive actuation assumed; no stability proof; memristive channel treated like any other (learned predictors absorb the switching — no explicit G(u_r)−G(u) structure); results numerical, not a direct analytical-vs-ML performance comparison

## Transferable Lessons
- Map selection is a two-objective design: analytic tractability (φ₄=u preserves error structure for Lyapunov proofs) vs dynamical compatibility (learned map minimizes forcing) — choose based on whether you need guarantees or efficiency
- "Advance-then-map ≈ map-then-advance" is a general self-supervised criterion for learning synchronization targets/conjugacies from UNCOUPLED trajectories
- Always pair dynamical-consistency objectives with anti-collapse penalties — degenerate (constant-map) solutions hide in self-supervised losses
- Bound retained switching with case-wise partitions first (exact), Young's inequality second (switching-independent, explicit radius δ=√(8m²/(εα)))
- Report Lyapunov-condition violations honestly: Ψ≤0 (V̇≤0) ≠ asymptotic convergence; distinguish "convergence beyond sufficient conditions" from "theorem corroborated"

## Related Skills
- [[memristive-ei-multiscale-excitability]] — memristive EI models
- [[chaotic-griffiths-phase-neuron-map-networks]] / [[bipartite-oscillator-synchronization-modes]] — synchronization analysis
- [[esn-empirical-boundaries-fewshot-patterns]] — reservoir computing boundaries
- [[lyapunov-spectrum-random-neural-networks]] — Lyapunov analysis of neural dynamics
