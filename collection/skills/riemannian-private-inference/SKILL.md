---
name: riemannian-private-inference

description: Use for private inference on manifold-valued optimization.
category: ai_collection
---

# Locally Private Inference for Riemannian Stochastic Optimization

**Source**: arXiv:2609.22642 (Chang, Jiang, Hu — NTU / Shanghai UFE, Sep 2026)

Methodology for statistical inference on manifold-valued parameters (sphere, SPD cone, hyperbolic space, quotient manifolds) when each observation belongs to a different participant and only locally private (LDP) messages reach the analyst.

## When to Use

- Estimating intrinsic Fréchet means, directional locations, streaming PCA, log-Euclidean SPD means, or affine-invariant covariance from **federated/private** data
- Users cannot share raw data (health surveys, DTI tensors, anthropometrics) — only randomized messages
- Need confidence regions / Wald tests on manifold parameters under (ε,δ)-LDP

## Core Problem: Target Shift

The naive approach — release a private surrogate `Z` per observation and plug it into the original loss — **shifts the population minimiser** for any nonlinear loss: a centred perturbation of the data is NOT a centred perturbation of the score. This is a statistical bias issue, not a geometry issue (arises for Euclidean M-estimators too).

Works only when the channel is exactly correctable (mean-preserving mechanisms for squared error; randomised response inversion for categorical data; log-Euclidean mean with privatized matrix logs).

**Fix**: randomize the **tangent score** evaluated at each public query. Conditional centring `E[ĝ(x)|Y] = g(x)` preserves the population first-order equation.

## Algorithm (per pair of participants)

1. **Public frame**: fix orthonormal basis `B_x` at reference point, parallel-transport along geodesics → smooth frame in normal convex neighbourhood.
2. **Tangent Gaussian mechanism**: participant computes `g(x) = ∇ℓ(x,Y)`, clips to `‖g‖≤G`, releases `B_x R_{ε,δ}(B_x⁻¹g)` with analytic Gaussian calibration (sensitivity Δ=2G). Unbiased conditional on data.
3. **Symmetric-pair queries**: at pair k, freeze iterate `x_{k-1}`; two fresh participants evaluate gradients at **opposite offsets** `q± = R(±h B v_k)` in public direction `v_k`. Server transports to base, forms:
   - `U_k = (z+ + z-)/2` → drives **point update** (first-order effects of offsets cancel; bias O(h²))
   - `D_k = (z+ − z-)/2`, `X_k = h v_k` → **regresses on X_k to estimate Hessian H** (base gradient cancels)
   - Residual variation of D_k → **score covariance Σ**
4. **RSGD + Polyak–Ruppert averaging**: update `x_k = Π(R(−γ_k B Ũ))` with metric projection safeguard; report intrinsic average `x̄_K = Exp_{x̄}(Log(x_k)/k)`. Root-n efficiency without step-size tuning.
5. **Inference**: sandwich covariance `Ξ/n = H⁻¹Σ_tot H⁻¹/n`; tangent Gaussian noise adds known floor σ²I to Σ_tot (Corollary: `Σ_tot = Σ_0 + σ²I`).

## Key Theoretical Facts

- **CLT**: `√n R⁻¹(x̄_K) → N(0, H⁻¹Σ_tot H⁻¹)` — privacy noise inflates covariance but **does not shift the target**
- **Both nuisance matrices (H, Σ) are identified from the same transcript** — no holdout, no second release. Pair differences are a first-order regression for H; predictability + martingale LLNs replace independence
- **Pairing halves variance**: converting K pairs → n=2K users restores user-scale normalisation
- Completed design directions give `Q_n = (s_n/d)I` — curvature identification doesn't depend on optimization path randomness

## Implementation Notes

- Retraction R may replace Exp (agreement through 2nd order); either works for Wald regions
- Clip updates (not differences): `Ũ = C_{δ₀/γ}(U)` — capped update keeps iterates in region; original D_k remain for regression
- Step sizes: γ_k ~ k^(-α), h_k → 0 slowly; offsets must stay in public query set K_q
- Manifolds validated: S²/S³, SPD(2/3) (log-Euclidean + affine-invariant), H² (Fréchet, pseudo-Huber), quotient spaces
- Coverage near-nominal under moderate privacy (ε ≈ 1–4); privacy cost appears as inflated variance, not bias

## Reusable Pattern: Gradient-Message Duality

One randomized gradient message per participant serves **three** estimation roles simultaneously:
1. **Optimization**: pair average ≈ gradient at base point
2. **Curvature**: pair difference ≈ Hessian applied to offset direction (finite-difference in tangent space)
3. **Uncertainty**: residual spread of differences ≈ score covariance

This 'one message, three uses' pattern generalizes: any streaming system with paired/controlled perturbations can identify 2nd-order structure without revisiting data — applicable to federated learning diagnostics, zeroth-order private optimization, and online experimental design.

## Cross-Domain Connections

- **Quantum differential privacy**: entanglement reshapes the information geometry of privacy channels (cf. kg entity: 'How Entanglement Reshapes the Geometry of Quantum Differential Privacy') — the tangent-space randomisation here is the classical analogue of noise engineered to respect parameter-space geometry
- **Quantum Fisher information**: sandwich form H⁻¹ΣH⁻¹ mirrors QFI-based Cramér–Rao bounds; manifold-aware noise calibration parallels covariant noise models
- c-interior PML (arXiv:2609.28297): tighter contraction analysis when input densities bounded away from zero — complementary privacy accounting for this pipeline

## Verification Checklist

- [ ] Conditional centring: verify `E[released gradient | data] = true gradient` (no surrogate bias)
- [ ] Frame smoothness: B_x varies smoothly; queries stay in normal convex neighbourhood
- [ ] Offset paths `R_x(±tB v_k)`, t ∈ [0,h] ⊂ K_q (public)
- [ ] Sandwich covariance uses known σ² floor from the privacy mechanism
- [ ] Wald region: Log vs R⁻¹ differ by o(n^{-1/2}) — either acceptable
