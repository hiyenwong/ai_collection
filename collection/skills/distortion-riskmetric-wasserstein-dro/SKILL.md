---
name: distortion-riskmetric-wasserstein-dro
description: Solve Wasserstein-DRO for distortion riskmetrics (nonconvex VaR/RVaR/CPT) via 3-tier exactness→regularization→bound hierarchy.
category: econ-finance
trigger: distortion riskmetric, Wasserstein ambiguity, distributionally robust risk, nonconvex risk measure, robust portfolio
---

# Robust Distortion Riskmetrics under Wasserstein Ambiguity

Methodology from "Robust distortion riskmetrics under Wasserstein ambiguity" (Liu, Wang & Wang, arXiv:2610.09622, Oct 2026). Solves the previously open problem of distributionally robust optimization (DRO) for the **full class of distortion riskmetrics** — signed Choquet integrals with NO convexity, monotonicity, or continuity assumptions — over a p-Wasserstein ball as the sole ambiguity constraint.

## When to Use

- Robust risk evaluation when the reference distribution is an estimate and NO moment information justifies restricting alternatives
- Nonconvex risk objectives: VaR, RVaR, inverse-S prospect-theory distortions (Tversky-Kahneman), inter-quantile/Gini/mean-median deviation measures
- Distributionally robust portfolio selection with a single transportation budget (not moment constraints)
- Any setting where existing convex DRO methods give overly conservative answers and you need to know whether that conservatism is real

## Core Framework

**Problem**: `inf_ω sup_{F ∈ W_p-ball(P0, ε)} ρ_h(ωᵀ X)` where ρ_h is a distortion riskmetric with distortion function h, and the Wasserstein ball uses ℓ_r transportation cost.

**Key distinction from moment-constraint DRO**: A single transportation budget must be allocated among changes in mean, dispersion, AND shape simultaneously — this joint allocation is why the problem is nontrivial even though the formulation is one line.

## Three-Tier Solution Hierarchy (decision sequence)

### Tier 1 — Check convexification exactness FIRST (Theorem 1)
Replace h by its concave envelope h*. This preserves the worst-case value **iff the reference quantile G0⁻¹ is flat on I_h** (the region where h < h*), for p > 1:
- `S_h(ε) = S_h*(ε) ⟺ G0⁻¹ flat on I_h` (p > 1)
- Flatness is sufficient but not necessary for p = 1; if not flat, strict inequality for small ε
- **Practical meaning**: existing convex methods are exact only under quantile flatness. Otherwise the concave-envelope answer is a strict upper bound → apparent extra conservatism is an artifact of the method, not the problem.

### Tier 2 — Exact value via regularization sequence (Theorem 2)
When Tier-1 conditions fail:
1. Regularize the distortion: h_η = h + η·(smooth/regular term)
2. Solve each regularized problem (solvable via Prop 2's penalized formulation)
3. `S_h(ε) = lim_{η↓0} S_{h_η}(ε)`
4. Worst-case distributions P*_ηₙ converge weakly to an optimizer F* (which need not be attained by the original problem when h ≠ h*; left-VaR is the canonical non-attainment example)
5. For p > 1 with h = h*: F* is unique

### Tier 3 — Explicit approximation with computable error bounds (Theorem 3)
No optimization or root finding needed. Construct P_ε explicitly from the envelope optimizer:
- `ρ_h(P_ε) = ρ_h(G0) + ε·[ρ_{h*}(G0) − ρ_h(G0)]/ε + ε·‖ψ_{h*}‖_{p'} ...`
- Error bounds: `0 ≤ S_h(ε) − ρ_h(P_ε) ≤ ρ_{h*}(G0) + ε‖ψ_{h*}‖_{p'} − ρ_h(P_ε)`
- For p > 1 the bound is O(ε^−min{p−1,1}) as ε→∞; error → 0 as ε↓0; O(ε) for absolutely continuous h with ψ_h ∈ L^{p'}(0,1)
- **Use when**: exact evaluation via the η-limit is too costly and you need a certified accuracy/cost tradeoff inside a larger decision problem

## Price of Robustness (Proposition 1)

The concave-envelope worst-case value is **linear in ε** with slope given by a dual norm of the quantile density:
`S_{h*}(ε) = ρ_{h*}(G0) + ε·‖ψ_{h*}‖_{p'}`
- ψ_{h*} = (h*)' is the quantile-density (distortion derivative); ‖·‖_{p'} is the dual exponent norm
- p = 1 requires the max-set of |ψ_{h*}| to have positive Lebesgue measure for attainment
- Worst-case optimizer: quantile shift `r*(u) ∝ sgn(ψ_{h*}(u))·|ψ_{h*}(u)|^{p'−1}` scaled to exhaust the radius

## Portfolio Application (Section 6)

- Feasible set: long-only simplex or any SOCP-representable constraint set
- **Projection identity (elliptical benchmark)**: for P0 = E(μ, Σ, φ), every portfolio faces the SAME 1-D worst-case problem at a different effective radius:
  `V_h(ω) = h(1)·ωᵀμ + s_ω·S_h(ε·‖ω‖_{r'} / s_ω)`, with s_ω = √(ωᵀΣω)
- This converts the d-dimensional robust portfolio problem into a 1-D worst-case evaluation + SOCP outer loop ("exact outer optimization by regularization")
- Numerics use tolerance 0.05 SD; gaps/bounds/radii measured in reference-loss SD units; code: github.com/Murphy116/Robust-distortion-riskmetrics-under-Wasserstein-ambiguity

## Reusable Patterns

1. **Envelope-exactness check before convexifying** — for any robust problem with a nonconvex objective over a ball geometry, test whether the convex counterpart is exact (flatness of the reference object on the envelope-gap region) before trusting convex solutions
2. **Regularization-limit for non-attained suprema** — when the adversarial inner problem has no optimizer, solve a sequence of smoothed versions and take the limit; extract convergence of both values AND optimizers (subsequence weak convergence)
3. **Certificate-style approximation** — construct a feasible explicit candidate + a computable upper bound on the gap; the certificate lets you skip solving the hard problem when the bound meets tolerance
4. **Dual-norm pricing of ambiguity** — linear-in-ε worst-case slopes via a dual norm of a sensitivity function generalize far beyond risk (any locally-linear sensitivity ψ of the objective to quantile perturbations)
5. **Quantile-shift adversary construction** — worst-case distributions are quantile shifts proportional to sign·power of the sensitivity function, exhausting the transport budget
6. **1-D projection reduction** — elliptical/factor benchmarks let multivariate robust objectives collapse to a family of 1-D problems at portfolio-dependent effective radii, keeping the outer problem SOCP

## Pitfalls

- Concave-envelope replacement is NOT always conservative-safe: it changes the worst-case value whenever the flatness condition fails (Theorem 1(ii)); report which regime you are in
- For p = 1, the worst case may not be attained (sup vs max) — use the regularization route or left-continuous modifications
- Moment constraints + Wasserstein together can LOWER the worst-case value by excluding alternatives; combine only when moment info is trustworthy
- Radius ε is a modeling choice (transport budget), not data-calibrated; report results in SD units of the reference loss

## Related

- arXiv:2610.11917 (mean-expectile Wasserstein portfolio — envelope theorem for worst-case expectiles; complementary tractability route)
- Pesenti et al. 2025 (concentration-closed ambiguity sets — the flatness idea generalized)
- Mohajerin Esfahani & Kuhn 2018 (convex Wasserstein DRO — the Tier-1 regime)
- Liu et al. 2022 (worst-case convex distortion risk measures over Wasserstein balls)
