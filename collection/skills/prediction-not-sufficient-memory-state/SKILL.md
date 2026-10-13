---
name: prediction-not-sufficient-memory-state
description: "Use when analyzing memory-state vs predictor separability in recurrent networks. Prediction equality does not imply update-closed state."
category: ai_collection
---

# Prediction Is Not a Sufficient Memory State

**Paper**: "Prediction Is Not a Sufficient Memory State" (arXiv: 2610.13881, Robert Jenkinson Alvarez, cs.LG, 9 Oct 2026)

## Core Thesis

A recurrent state that reproduces every **current** prediction may still have forgotten how to learn from the **next** observation. Representing the current predictor and representing a state from which that predictor can be updated are fundamentally different tasks. This distinction persists even when every present query is answered exactly — not merely on a finite evaluation set.

Canonical collision example: **regression on zero labels**. Current prediction is zero for ANY design matrix. Yet two zero-label histories respond differently to the same next nonzero label. In normalized attention, zero values similarly conceal all past keys until a new nonzero value makes their normalization mass observable. Current-output compression removes information that the update still needs.

## Key Results (6 theorems)

### Theorem 1 — Exact ridge-state dimension
- Read-only state: `dp`. State supporting all present readouts + one arbitrary new observation: `m = dp + s_d`, `s_d = d(d+1)/2`.
- Attained by recursive least squares (RLS) storing `(C_h, M_h)`. Lower bound applies to **arbitrary continuous nonlinear states**, not only matrix implementations.
- Collision instance (d=2, λ=1/4): `C_± = [[1, ±1/2], [±1/2, 1]]` agree in counts/diagonal/predictions, but appending (e₁, 1) gives rows (4/7, ∓2/7) — merged state has worst-case squared error ≥ 4/49.
- The raw delta recurrence `S+ = S + β(y − Sk)k^T` merges these histories for ANY key-dependent scalar β. Not a claim about all DeltaNet variants — extra value channels/hidden states must be counted.

### Theorem 2 — Native identification (unweighted observations)
- Two histories have identical optima after EVERY single additional observation ⟺ their accumulated gradient **functions** `Σ_{z∈h} g_z` agree (g_z(w) = xρ′(x^⊤w − y), a function-space object, not a gradient vector at one parameter).
- `r = dim G_ρ` finite → exact minimum continuous state dimension = r, attained by additive gradient coefficients. r = ∞ → no fixed finite dimension suffices.
- Proof device: one native observation suffices to identify a history — append `x = −∇F_h(w)/c, y = x^⊤w − t₀` to steer any proposed optimum to w.
- Closure: h ∼₁ h′ (equal after every single observation) is CLOSED under future updates (induction), unlike h ∼₀ (equal present predictions).

### Theorem 3 — Polynomial closure and equal-prediction memory
- Exact continuous recurrent state of history-length-independent size exists **iff ρ is polynomial**.
- Degree-D loss: minimum dimension `r_D(d) = C(d+D, D) − 1`. Predictor alone: d. Fixed-optimum family {h: w_h = w₀}: exactly `r_D(d) − d` coordinates remain NECESSARY.
- Squared loss (D=2): invisible part = s_d (the design matrix). Fourth power: C(d+4,4) − d − 1.
- Nonpolynomial losses: required dimension **unbounded even on the fixed-optimum family**.
- Why polynomial: finite-dim gradient function space G_ρ → restriction span{t ↦ ρ′(at+b)} finite-dim → differentiation D similar to all positive multiples of itself → spectrum {0} → nilpotent (Cayley–Hamilton) → ρ polynomial.

### Theorem 4/5 — Bounded logistic obstruction
- Scalar logistic, bounded features (1 < a_i < 2), 2N paired observations: every prefix has optimum zero, identical predictions, yet exact one-example continuation requires **≥ N coordinates**. No fixed continuous state computes exact cumulative logistic regression.
- Response curve `w_a′(0) = 1/(2(λ + Σ2a_i²))` and analyticity identify all past feature scales via exponential tail decay.
- Theorem 5: fixing ANY finite derivative jet (orders 0..2K+1) still leaves an (N−K)-dimensional distinguishable family. A Hessian (first-order adaptation) and any fixed higher jet both miss native nonlinear continuations.

### Theorem 6 — Finite-bit law (B-bit compression)
- Any measurable encoder into ≤ 2^B states (randomized allowed), decoder unrestricted, next key/query uniform random unit vectors:
  `R_B = Θ(2^(−2B/s_d))` on a well-conditioned zero-prediction family, `s_d = d(d+1)/2`.
- Halving average error costs Θ(s_d log(1/ε)) bits — a **quadratic-dimensional exponent**. Compression happens BEFORE the probe arrives; computation after probes arrive cannot restore evidence already merged.

### Theorem 8 — Kernel attention closure
- One-token continuation identification ⟺ equality of (B_h, Z_h) — unnormalized numerator/denominator statistics (what linear attention already stores; the result proves their NECESSITY against nonlinear compression).
- Positively weighted: exact dimension `r_κ(p+1)`, r_κ = dim span{κ(·,k)}. Unweighted exponential attention: length-N prefix with distinct keys requires exactly `N(d+p)` coordinates; zero-valued subfamily: `Nd`.

## Summary Table

| Computation | Exact state | Hidden evidence (fixed prediction) |
|---|---|---|
| Ridge, p outputs | dp + s_d | s_d (design matrix) |
| Degree-D residual loss | C(d+D,D) − 1 | C(d+D,D) − 1 − d |
| Logistic, 2N paired samples | unbounded in N | ≥ N |
| Softmax, N distinct keys | N(d+p) | Nd |

## Practical Implications (Propositions 9–10)

1. **Gradient-profile certificate**: if sup‖G(w) − ∇F(w)‖ ≤ δ over domain Ω and residual at returned point ≤ η, then ‖ŵ − w⁺‖ ≤ (δ+η)/λ. A certificate on accumulated evidence (the gradient function profile) survives common updates — a certificate on present loss does not.
2. **Attention evidence**: error in the ratio f̃ = B/Z alone gives NO continuation guarantee (B=0 hides arbitrary Z). Bounded errors (δ_Z, η) in the unnormalized pair DO: ‖f̃⁺ − f⁺‖ ≤ θ(η + δV)/(1 − θδ), θ = Z/(Z+A).
3. **Polynomial approximation escape hatch**: bounded features/labels + polynomial approx p to ρ′ with error ε → finite moment summary with error ≤ ε·Σ‖x_i‖ (connects to coresets/Huggins et al.). Growth with total feature mass is not discarded.

## Evaluation Protocol

To separate prediction from retained learning: construct histories with identical current readouts, vary hidden evidence, append the same observation, compare outputs. For ridge, full RLS statistics give the exact reference; diagonal or sketched states quantify the loss.

## Activation Triggers

prediction-memory separation, recurrent state dimension, test-time learning, DeltaNet, linear attention state, ridge regression memory, update-closed state, gradient profile, polynomial closure, finite-bit compression law, equal-prediction family, fast weights
