---
name: neural-dimensional-analysis
description: "Use when Transformer scale or units drift. NDA UVI GCT."
category: ai_collection
---

# Neural Dimensional Analysis (NDA) — Transformer Unit Consistency

Unify all Transformer scale-control mechanisms (normalization, residual scaling, attention temperature, loss weighting, adaptive updates) under one rule: **quantities that are added must share units; inputs to exp/sigmoid/softmax must be dimensionless**. Source: arXiv 2610.17969 (Kim, Kawano, Iwasawa, Matsuo; UTokyo, Oct 2026).

## When to Use
- Diagnosing training instability / scale drift in Transformers (compare Pre-LN, LLaMA-style, QK-Norm, nGPT)
- Designing normalization, residual scaling, or attention temperature from first principles instead of heuristics
- Improving learning-rate transfer (width/depth) and post-training quantization robustness of residual streams
- Building dimensionless diagnostics comparable across blocks

## Core Framework

### 1. Neural units as transformation laws
- Rescaling group G = (R+)^K, one factor per independent internal scale degree of freedom.
- Unit of node v = representation rho_v: G -> GL(V_v), x_v -> rho_v(g) x_v. Dimensionless iff rho_v = identity.
- Scalar units are characters chi_u(g) = prod_k g_k^{u_k}; unit type u(x) specifies transformation, empirical scale s_x (RMS) measures magnitude and shares the type, so x/s_x is dimensionless.

### 2. Unit-consistency rule (equivariance identity)
An operation y = f(x_1..x_n) is unit-consistent when for every g in G:
f(rho_1(g)x_1, ..., rho_n(g)x_n) = rho_y(g) f(x_1, ..., x_n).
Rescaling inputs before the operation must equal rescaling the output afterward. Parameters follow the same rule (declared rho_phi).

### 3. Local typing rules
- **Addition/residuals**: z = x + y requires u(x) = u(y) = u(z). A residual branch must return the residual-stream unit U_res; in Pre-LN, N: U_res -> 1 strips units and the branch F: 1 -> U_res restores them.
- **Normalization = nondimensionalization**: N(x) = x/RMS(x) satisfies N(cx) = N(x) for c > 0 — removes unit and magnitude at once.
- **Attention**: logit differences must be dimensionless (softmax outputs probability ratios). Raw scores carry u(q)u(k); the temperature is a unit converter with u(tau) = u(q)u(k). Calibrated per-head temperature tau = sqrt(d_h * s_Q * s_K), of which 1/sqrt(d_h) is the s_Q = s_K = 1 special case.
- **Activations/gates**: sigmoid, tanh, GELU, SiLU require dimensionless arguments. In gated MLPs z = v . g, units multiply, so the gate must be dimensionless. SwiGLU's raw gate a*sigma(a) silently assumes dimensionless a — use normalized gate g_tilde = C(a) sigma(C(a)).
- **Loss aggregation**: in L = sum_i lambda_i L_i, consistency forces u(lambda_i) = u(L_i)^{-1}. Factor each weight into dimensionless preference alpha_i and inverse characteristic scale: lambda_i = alpha_i / S_i with u(S_i) = u(L_i). Cross-entropy is dimensionless iff logits are; squared error carries U_y^2.
- **Gradients (dual typing)**: if L is dimensionless and u(x) = U then u(grad_x L) = U^{-1}; under x -> cx, grad -> c^{-1} grad (transforms by rho^{-T}). Dimensionless sensitivity: elementwise x . grad, or on shared-unit blocks the primal-dual RMS product Pi_x = RMS(x) * RMS(grad_x L).
- **Optimizer updates**: update needs u(delta_theta) = U_theta while u(grad) = U_theta^{-1}; with dimensionless LR a typed preconditioner supplies the missing factor u(P_theta) = U_theta^2.

### 4. Residual scale dynamics
With step size alpha_l = RMS(r_l)/RMS(h_l) and alignment c_l = cos(h_l, r_l):
s_{l+1}^2 = s_l^2 (1 + alpha_l^2 + 2 alpha_l c_l).
- Persistent positive alignment (c_l >= c_0 > 0) forces sum alpha_l = O(1), i.e. O(1/L) steps per layer.
- Orthogonalization removes the linear term: sum alpha_l^2 = O(1) with uniform Theta(L^{-1/2}) steps (as in depth-muP).

### 5. UVI diagnostics (dimensionless, cheap)
- UVI_res(l) = log((alpha_l + eps)/(alpha* + eps)), target alpha* = 1/sqrt(2L).
- UVI_attn(l,h) = log((v_l,h + eps)/(1 + eps)), v = batch-averaged row-centered logit variance after all model-specific scaling.
- Large values locate the interface where a scale mismatch arises; computable on small batches at intervals. Five indices total plus drift diagnostics (activation/gradient/optimizer variants in App E.4).

### 6. Gauge-Canonical Transformer (GCT)
Factor every unitful quantity: unitful = unit scale x canonical coordinate. State h_l = s_l * hbar_l, RMS(hbar_l) = 1.
- Canonicalizer: C(x) = x / sqrt(RMS(x)^2 + eps_x).
- Orthogonalized residual update per sub-block: a_bar = Phi(hbar); a_hat = C(P_perp a_bar); hbar_plus = C(hbar + alpha_l * a_hat). Learnable dimensionless alpha_l initialized at 1/sqrt(2L). P_perp subtracts the component along the current state: P_perp a = a - <a,hbar>/||hbar||^2 * hbar.
- Attention: canonicalize q, k per head (qbar = C(q), kbar = C(k)), per-head dimensionless gain g_h init 1.
- Output head: dimensionless logits from C(hbar_L) with learnable logit gain; unitful outputs y_hat = s_y * ybar_hat restore explicit scale.
- Invariance: with zero canonicalization floors, C(ch) = C(h) makes the dimensionless output invariant to any positive rescaling at every block boundary.

## Validation Results (51M-1B LM on FineWeb-Edu, matched recipes)
- Stable training across a 16x learning-rate range; at 124M, GCT 3.045 vs QK-Norm 3.091 (each at its tuned LR); GCT mean loss within 0.005 nats of LayerScale/nGPT/Pre-LN.
- Depth transfer with hyperparameters unchanged from L=8: GCT 3.903 at L=48 vs nGPT 4.243. Adding GCT's P_perp to nGPT reduces nGPT's L=48 loss by 0.275 nats — the projection is a portable component.
- LR transfer 51M -> 124M: GCT improves 0.125 nats vs 0.052-0.072 for baselines.
- PTQ at 1B, residual stream quantized at every block boundary: per-tensor int8 raises GCT loss only +0.009 nats vs up to +5.51 for baselines; per-token int4 +0.739 vs +4.661 (nGPT) and >= +5.230 (others). Rule: cross-token scale variation consumes log2(kappa_scale) bits — GCT fixes every token RMS at 1 so kappa_scale = 1.
- Weight-space audit (Prop 6, zero radial sensitivity predictions): 54/54 architecture-by-role predictions matched at 124M, 34/34 at 1B.
- Vision + PINN experiments confirm benefits beyond language modeling.

## Implementation Checklist
1. Declare a unit for every tensor: residual stream U_res, per-head q/k, logits dimensionless, per-loss units.
2. Audit existing architecture with UVI: flag residual step sizes far from 1/sqrt(2L) and logit variance far from 1.
3. Apply typing rules: normalized gates, calibrated temperature sqrt(d_h s_Q s_K), loss weights factored as alpha_i/S_i.
4. For new builds, use GCT canonicalization + orthogonal projection; keep scales explicit only where outputs need units.

## Pitfalls
- RMS is a valid scale only on shared-unit blocks; mixed-unit tensors need separate scales.
- Orthogonality holds before retraction (the post-normalization displacement need not be orthogonal).
- Exact invariance requires zero floors; finite eps_x floors break it slightly (App F.1 quantifies deviations).
- Targets depending on absolute magnitude or scale ratios require retaining the scale state — pure canonical coordinates discard it.

## Related Work Anchors
- muP (Yang & Hu) prescribes update scales; unit scaling (Blake) targets low precision; nGPT constrains to unit hypersphere; units-equivariant learning (Villar) handles physical data units. NDA unifies all of these over the whole computation graph including objectives, gradients, and optimizers.

**Activation**: transformer scale, normalization design, attention temperature, residual scaling, unit consistency, quantization robustness, learning-rate transfer, training stability diagnostics, nGPT, muP, gauge
