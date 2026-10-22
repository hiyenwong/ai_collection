---
name: neural-dual-critics-general-utility-rl
description: "Use when RL objective is a nonlinear occupancy functional."
category: reinforcement-learning
---

# Sample-Efficient RL with General Utilities via Neural Dual Critics

Source: arXiv:2610.24880 (Ankur Naskar, Vaneet Aggarwal — IISc & Purdue, Oct 2026). Natural actor-critic for concave general-utility RL (RLGU) that learns the utility-induced pseudo-reward DIRECTLY as a neural dual critic instead of estimating the occupancy measure first; achieves Õ(ε⁻²) global convergence above an explicit approximation floor, covering infinite state-action spaces.

Use when: the RL objective is a nonlinear functional of the state-action occupancy measure — visitation-entropy exploration, KL occupancy matching for imitation, f-divergence or quadratic density-matching objectives — and the space is too large for explicit occupancy estimation, or you need sample-complexity guarantees for convex-RL-style objectives beyond linear returns.

## Problem class (RLGU)

J(θ) = F(λθ), where λθ is the normalized discounted occupancy: λπ(B) = (1−γ) Σₜ≥0 γᵗ Pπ((sₜ,aₜ) ∈ B), and F is a concave utility functional. Standard RL = F linear in λ. Core identity (variational policy gradient, Zhang et al. 2020):

∇θJ(θ) = (1−γ) ∇ϑ V^πϑ(rθ)|ϑ=θ

where the pseudo-reward rθ = ∇λF(λθ) is HELD FIXED while differentiating the policy. Consequence: learning an exact dual minimizer rθ is SUFFICIENT for the actor — the occupancy only ever needs to appear inside an expectation.

## Method: learn the dual reward, not the occupancy

1. **Exact dual representation (Assumption 2)**: F(λθ) = min_r { Eλθ[r] − Ψ(r) }, with rθ an argmin. No density estimation anywhere.
2. **Separable utilities (Assumption 3)**: F = C − ∫f(p)dν − ∫c·p dν with density p = dλθ/dν. Fenchel duality gives Ψ(r) = −C − ∫f*(−r−c)dν and the exact pseudo-reward **rθ = −f′(pθ) − c**. Concrete instantiations (Table 2):
   - Entropy (exploration): F = −∫p log p dν → Ψ(r) = −∫e^(−r−1)dν, rθ = −1 − log p (bounded for 0 < a ≤ p ≤ b < ∞)
   - Smoothed entropy f_τ(u) = u log(u+τ): rθ = −log(p+τ) − p/(p+τ) (bounded for 0 ≤ p ≤ b)
   - KL imitation: F = −KL(λ‖Q), reference measure Q → rθ = −1 − log(dλ/dQ)
   - Quadratic matching: F = −½∫(p−q)²dν → Ψ(r) = E_Q[r] − ½∫r²dν, rθ = q − p
3. **Neural critic**: parameterize r(s,a,ζ) as an L-layer net with scaled output m^(−1/2)b⊤x^(L); minimize E(θₖ,ζ) = Eλθₖ[r] − Ψ(r) by projected stochastic updates using FROZEN tangent features g₀ = ∇ζ r(s,a,ζ₀) (NTK-style) while evaluating the nonlinear reward inside the dual derivative; finite-width linearization error η_m = O(m^(−1/2)) is an explicit approximation floor.
4. **MLMC bias control (function-valued — the key trick)**: a single critic run has O(H^(−1/2)) RMSE above its floor — too biased for direct actor use. Draw Nₖ ~ Geom(1/2); if Nₖ ≤ J run the critic 2^Nₖ updates and take outputs at horizons 2^(Nₖ−1) and 2^Nₖ; the dyadic combination matches the LONGEST run's bias at LOGARITHMIC expected cost. Novelty: MLMC controls a learned dual reward function, not scalarization coefficients.
5. **NPG actor**: θₖ₊₁ = θₖ + αwₖ, with w*(θ) from the Fisher-preconditioned least-squares (regress the advantage of r̂ onto the score uθ). The analysis separates conditional actor bias from estimator second moments in a KL-potential bound, and accounts explicitly for dual-optimization, critic-approximation, and neural-linearization errors.

## Guarantees

- Õ(T^(−1/2)) global convergence to F* above policy-transfer, dual-stability, and local critic-regularity floors, using Õ(T) expected transitions + reference samples.
- Fixed critic representation: **Õ(ε⁻²) sampling complexity** above the approximation floor — vs Õ(ε⁻⁴) for linear (Barakat 2023) or parametric (Barakat 2026) occupancy estimators, both of which are also restricted to finite spaces. First RLGU guarantee for infinite state-action spaces (Table 1).
- vs CURL (concave function of finitely many expected returns): in infinite spaces general RLGU is strictly more expressive — finitely many occupancy integrals cannot represent every occupancy utility (Prop 2).

## Pitfalls

- Requires concave F in occupancy + an exact dual (Assumption 2); non-separable utilities need their own Ψ construction.
- Reward boundedness needs density-range conditions (entropy needs p ∈ [a,b]; smoothed entropy relaxes the lower bound).
- Do NOT estimate the occupancy and then differentiate — that stacks two approximation problems; the whole point is to place approximation burden on the reward function the actor actually consumes.
- MLMC dyadic correction adds variance; tune J (max horizon exponent) to critic mixing speed.

## Relation

- Builds on variational policy gradients (Zhang et al. 2020), policy-cost game (Zahavy et al. 2021), occupancy-estimation RLGU (Barakat et al. 2023/2026), CURL (Agarwal & Aggarwal 2023), MLMC (Blanchet & Glynn 2015).
- Related skills: [[dmrl-density-matrix-policy-reinforcement-learning]] (generalized policy objects), [[svdrl-stein-variational-distributional-rl]] (distributional RL), [[reward-function-design-framework]], [[graft-gradient-routing-reward-hacking]].

## Activation keywords

general utility RL, concave RL, RLGU, occupancy matching, visitation entropy objective, imitation via occupancy, variational policy gradient, Fenchel dual, neural dual critic, pseudo-reward, MLMC bias control, convex reinforcement learning
