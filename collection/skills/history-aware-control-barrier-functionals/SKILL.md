---
name: history-aware-control-barrier-functionals
description: Use when safety depends on state history. Fading-memory CBF.
category: ai_collection
---

# History-Aware Control Barrier Functionals (HA-CBFal)

Source: Altunkaya, Demir, Abu-Khalaf (Turkish Aerospace) & Özkol (ITU), "History-Aware Control Barrier Functionals with Nonsingular Fading-Memory Kernels", arXiv:2610.31525 (eess.SY, Oct 2026).

## Problem

Some protections must depend on HOW the state evolved, not only its current value: motor restart conditioned on thermal history, viscoelastic strain memory, flight-envelope protection at high incidence where recent adverse pitching degrades nose-down recovery capability. A history-aware policy assigns different admissible-control sets at the SAME state for different histories: U_H(x*, H_A) ⊊ U_H(x*, H_B). No history-blind map U_s(x) can reproduce this — it must use the intersection and is therefore over-restrictive for benign histories.

## Construction (5 steps)

1. Safety margin h(x) (h=0 at the limit, h<0 violation) for control-affine ẋ=f(x)+g(x)u, relative degree 1.
2. Nonsingular fading-memory kernel κ: κ(0)=κ0>0, κ̇≤0 a.e., κ(∞)=0. Weight ω=−κ̇ ≥ 0, ‖ω‖₁=κ0. "Nonsingular" = finite weight at zero age (Gaussian kernels allowed); fractional kernels are optional specializations, not requirements.
3. Memory of margin changes: qκ(t)=(κ*ḣ)(t) — past decreases and recoveries of the margin, accumulated with age weights. qκ(0)=0.
4. Weighted historical value (via integration by parts): h̄κ(t)=[κ(t)h(0)+(ω*h)(t)]/κ0, with the exact identity D_κh = κ0(h−h̄κ) (verified numerically to 1e-6).
5. Reserve policy: current margin must retain a prescribed fraction θ∈(0,1) of its weighted historical value: h(t) ≥ θ·h̄κ(t); residual gκ,θ = h − θh̄κ.

## Certificate

- Auxiliary barrier ψκ = qκ + γh with γ = κ0(1−θ)/θ; then ψκ = (κ0+γ)·gκ,θ EXACTLY (auxiliary-barrier nonnegativity ≡ reserve satisfaction).
- HA-CBFal condition Qκ = ψ̇κ + βψκ ≥ 0, affine in u: Qκ = (κ0+γ)(Lf h + Lg h·u) + ∫₀ᵗ κ̇(t−τ)ḣ(τ)dτ + βψκ.
- **Theorem 1**: h(0)≥0 + Qκ≥0 a.e. ⇒ ψκ≥0 AND h≥0 for all t — physical safety is implied by the reserve, across the ENTIRE admissible kernel family with one proof. Mechanism: integrating factor gives ψκ ≥ γe^{−βt}h(0); integration by parts rewrites h = f + λγV_ωh with f=λγ[ψκ+κ(t)h(0)] ≥ 0; the Volterra equation is solved by the POSITIVE L1 RESOLVENT (Neumann series) whose contraction factor is exactly θ = κ0/(κ0+γ) < 1 — the reserve fraction IS the contraction factor. Hence h = f + r_λγ*f with r≥0 ⇒ h≥0.
- No finite-dimensional memory realization required (Gaussian kernel provably has no exact LTI realization — its Laplace transform is entire and nonzero yet → 0 at +∞); memory is evaluated directly from retained history.
- Safety filter: u* = argmin ½‖u−u_nom‖²_W s.t. Qκ≥0 — convex program; QP when U polyhedral.

## History-parametrized certified input sets (Prop 1)

Qκ = a(x)u + b(x) + Λ(Ht) with the scalar history functional Λ(Ht)=∫[βκ(t−τ)+κ̇(t−τ)]ḣ(τ)dτ. ONE scalar determines the instantaneous certified input set at a fixed state; sets are parallel half-space cuts ordered by Λ (adverse history ⇒ larger Λ ⇒ smaller set). Worst-history intersection U_wc(x)=U∩{a(x)u+b(x)+Λ(x)≥0} with Λ(x)=inf_H Λ(H) is the GREATEST history-blind set satisfying the same certificate over the prescribed history family — use it when only x is measurable.

## Key design identities (all numerically verified)

- γ = κ0(1−θ)/θ ⟺ θ = κ0/(κ0+γ): choosing the reserve fraction fixes the barrier coefficient AND the resolvent contraction.
- ADMIRE Gaussian design: κ_G(s)=2e^{−(s/3)²}, θ_α=0.40 ⇒ γ=3; β=3.8341 s⁻¹ retained from a reference design while comparators were calibrated.
- Reserve/margin reusability: swap margin (h_α → h_α+h_α³/a²) or kernel (Gaussian → uniform κ_U(s)=2max{1−s/T_U,0}) by recomputing γ and policy terms ANALYTICALLY with β retained; common θ_c≈0.2567 for admissible initialization.

## ADMIRE high-incidence envelope protection (α_max=26°)

- 36-case calibration (twin-square peaks 2.4–3.0 g × recoveries 2–4 s × 3 histories): mean per-case tracking-RMSE ↓27.2% vs a calibrated policy-preserving state-only CBF, ↓7.0% vs a moving-average CBFal; both constraints preserved.
- 27 frozen-gain exploratory tests (incl. 1-s recovery OUTSIDE calibration): MA-CBFal violated the reserve in 17/27 DESPITE its functional staying nonnegative — functional preservation ≠ reserve satisfaction; HA-CBFal preserved both in all 27 without any gain retuning.
- History-conditioned input polytopes at a common checkpoint x*: nested volumes {0.078, 0.505, 0.861} vs 0.072 for the history-blind CBF; the adverse-history set equals their intersection, as Prop 1 predicts.

## Pitfalls

- MA-CBFal trap: enforcing Φ̇+βΦ≥0 on a moving-average functional does NOT imply the reserve requirement — verify gκ,θ≥0 directly on test maneuvers, or use the HA-CBFal construction whose nonnegativity is provably equivalent.
- Initialization: need gκ,θ(0)≥0; the paper splits activation from preparation with a nonnegative preparation contribution (memory origin qκ(t0)=0).
- The guarantee needs the margin's RELATIVE DEGREE 1 structure; higher relative degrees require extension.
- Kernel choice sets the protection horizon (decay time) and must satisfy Assumption 1 + input feasibility; nonincreasing κ is essential for the positive-resolvent argument.

Activation keywords: history-dependent safety, control barrier functional, fading memory, convolutional memory, safety margin reserve, envelope protection, Volterra resolvent, certified input sets, safety filter QP, viscoelastic/thermal history
