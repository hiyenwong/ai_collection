---
name: ppt-entanglement-distillation
description: "Use when analyzing PPT-channel entanglement distillation rates, Rains bound separations, or negativity lower bounds."
category: ai_collection
---

# PPT Entanglement Distillation (Lami, arXiv:2610.12454)

Analyze entanglement distillation under PPT channels (asymptotically vanishing error regime) — regularised achievability formula + two single-letter converses resolving the Regula et al. open problem.

## Core Method

**Relaxation ladder**: LOCC → PPT channels (Choi state PPT across AA′:BB′) → SDP-tractable. Three obstacles isolated: (1) LOCC set complexity — removed by PPT relaxation; (2) non-zero finite-block error; (3) asymptotic copy limit. This paper tackles (2)+(3) together.

**Theorem 1 — regularised formula** (achievable side):
```
E_d,PPT(ρ) = L∞(ρ) = sup_n (1/n) L(ρ^⊗n)
L(ρ) = sup_M Σ_j Tr[ρE_j] · log( Tr[ρE_j] / ‖E_j^Γ‖_∞ )
```
POVM-optimization functional L; zero effects omitted; limit exists by superadditivity. Restricting POVM to projectors recovers Rains's original measurement bound. Converse direction: two-outcome measurement = pullback of protocol's Bell test; direct direction: fixed measurement + classical typicality. E_d,PPT is lower semicomputable (enumerate rational POVMs).

**Theorem 2 — quadratic-form converse** (operator-space, Hilbert–Schmidt inner product):
```
V_α[ω,K] := (1/α)⟨√ω, log(L_√ω ∘ K⁻¹ ∘ L_√ω)[√ω]⟩
E_Q(ρ) = inf_{extensions ρ_AA':BB', α>0, K, J} V_α[ρ_AA':BB', K] − V_α[ρ_A':B', J]
```
subject to all-copy tensor-stable quadratic hypothesis: ⟨Q^n ⊗ X_n, K^⊗n[Q^n ⊗ X_n]⟩ ≤ ⟨X_n, J^⊗n[X_n]⟩ ∀n. Geometric means of positive super-operators → data processing for V_α. Rains bound = special choice of right multiplication; different quadratic forms improve it.

**Theorem 3 — analytic-family converse** (Hirschman strengthening of Hadamard three-line):
- Interpolate input through trace-one analytic family Z(z) on annulus O, reference point z* with σ = Z(z*), supp ρ ⊆ supp σ.
- Boundary density k_{O,z*} built from β_θ(s) = sin(πθ)/(2θ cosh(πs) + cos(πθ)) — masses (1−θ) inner, θ outer = harmonic measure.
- If D(ρ‖σ) + J_{Z,O,z*}(R) < 0 (J = boundary integral of min(log‖Z‖₁, log‖Z^Γ‖₁) − R against k), then R is an **exponential strong-converse rate**.
- Trace-norm duality gives two boundary bounds; Hirschman averages their smaller value; quantum hypothesis testing transfers to input.

**Theorem 4 — certified Rains separation** (3×3 Werner, antisymmetric weight 25/26):
```
0.5836 ≤ E_d,PPT(ρ_25/26) ≤ 0.6211 < R∞ = (25/26)log₂5 − log₂3 ≈ 0.6477
```
Resolves Regula et al. (NJP 2019) conjecture E_d,PPT = R∞ **in the negative**. Lower bounds: Werner twirling reduces collective POVMs to finite LP; one feasible 48-copy POVM certifies displayed rate. Upper: analytic family with rational annular parameters + directed-rounding interval arithmetic (companion certificate files, run_certificates.py, stdlib only).

**Faithful negativity lower bound** (byproduct of Theorem 1):
```
N(ρ) := (‖ρ^Γ‖₁ − 1)/2, d := min{d_A, d_B}
E_d,PPT(ρ) ≥ 1 − h₂( N(ρ) / (1/2 + 1/(d+1)) )   [h₂ = binary entropy]
```
Quantifies "every NPT state is PPT-distillable" (Eggeling et al. 2001): strictly positive rate whenever N(ρ) > 0.

**Grothendieck comparison (Prop. 15)**: little noncommutative Grothendieck inequality applied ONCE to whole n-copy space — factor 2 costs only 1/(2n) bits/copy (per-copy application would lose 2ⁿ). Within tensor-stable quadratic class, alternative forms cannot beat the regularised one-state construction on Werner inputs. Effect-dependent forms (using Q² ≤ Q) escape this no-improvement result.

**Rate-propagation rule** (Werner family): valid upper bound U_q propagates LEFT: E_d,PPT(ρ_p) ≤ (p−1/2)U_q/(q−1/2); valid lower bound L_p propagates RIGHT similarly. Pointwise min/max of applicable bounds remain valid. NOT convexity — no arbitrary interpolation.

## Key Lessons

- **Regularise the achievability side too**: the same measured-relative-entropy functional L, regularised, gives exact equality — don't seek single-letter formulas on only one side.
- **Two converse technologies complement**: quadratic forms (algebraic, tensor-stability hypotheses, condition on ancillas) vs analytic families (complex analysis, Hirschman boundary weights, hypothesis-testing transfer).
- **Certified numerics**: rational annulus parameters + interval arithmetic turn analytic bounds into machine-checkable certificates; companion files with SHA-256 manifest.
- **Bound hierarchy for E_d,LOCC**: E_d,LOCC ≤ E_d,PPT ≤ min(R∞, E_sq, E_Q, E_A) — new bounds E_Q (12) and E_A (119) join squashed entanglement.
- **AI-assisted proof note**: author states main results derived "almost entirely by ChatGPT Astra" with human validation — an order of magnitude less human time.

## Verification Hooks

- Qutrit Werner: check R∞(ρ_25/26) = (25/26)log₂5 − log₂3 ≈ 0.64766 numerically.
- Werner twirling → 2D LP: symmetric/antisymmetric sectors give tractable POVM certification.
- Sandwiched Rényi: D̃_α(ρ‖σ) = (α−1)/α · log Tr σ^{(1−α)/2α} ρ^α σ^{(1−α)/2α}.
