---
name: conformal-e-process-changepoint-detection
description: Use when doing distribution-free online changepoint detection with e-processes.
category: ai_collection
---

# Conformal E-Process Changepoint Detection (RCMM)

Source: Bhattacharyya & Ramdas (Wharton/Stanford), arXiv:2609.27179 [math.ST], 23 Sep 2026.

## Problem

Sequential changepoint detection on arbitrary data space (scalars, images, text embeddings): X_1..X_T ~ P0, X_{T+1}.. ~ P1, all of P0, P1, T unknown. Two error regimes:
- **PFA regime**: control P(say "change" ever | no change) ≤ α
- **ARL regime**: control E[τ | no change] ≥ γ (average run length)

## Why prior methods fail (the dilution trap)

Vovk's conformal test martingale (CTM) S_n = f(p_1)...f(p_n) is a single martingale started at time 1. Its capital gets diluted by the long pre-change history: post-change evidence must first overcome accumulated pre-change product before crossing threshold. **Provable suboptimality**: delays Ω(T) in the PFA regime and Ω(√ARL) in the ARL regime (Examples 2.2/2.3). This is the generic failure mode of any never-restarted test martingale used for late changepoints.

## Core Construction (Restarted Conformal Mixture Martingales)

**Step 1 — Randomized conformal p-values** (i.i.d. U(0,1) under exchangeability):
```
p_t = (Σ_{i≤t} 1(X_i < X_t) + λ_t·Σ_{i≤t} 1(X_i = X_t)) / t,  λ_t ~ U(0,1)
```
Optionally apply score s: X → R first (raw data is the default, s = identity).

**Step 2 — Local mixture martingales from EVERY start k**:
```
G_{k,t}(θ) = Π_{j=k}^{t} f_θ(p_j),   M_{k,t} = ∫ G_{k,t}(θ) dΠ(θ)
```
Mixing over a betting class F = {f_θ} (e.g. power bets f_θ(p) = θp^{θ-1}) with prior Π handles unknown P1. Mixing preserves the martingale property.

**Step 3 — Weighted aggregation across starts** (restart weights w = (w_k), typically non-decreasing recency priority):
```
S_t^(w) = Σ_k w_k M_{k,t}   (Shiryaev-Roberts analogue)
Z_t^(w) = max_k w_k M_{k,t}  (CUSUM analogue)
```
Stop when S_t or Z_t crosses threshold b.

**Step 4 — Regime control via weight normalization**:
- `Σ w_k ≤ 1` → S̃_t = S_t + Σ_{k>t} w_k is an **e-process** → PFA-valid at level α with threshold b = 1/α
- `max_k w_k ≤ 1` → e-detector (Shin et al. 2024) → ARL-valid at level γ with threshold b = γ
- **Single family, two regimes**: total weight ‖w‖₁ governs PFA, sup-norm ‖w‖∞ governs ARL
- ARL-valid procedures additionally satisfy optional-horizon inequality P(τ ≤ σ) ≤ E[W_σ]/γ — no early false-alarm spiking

**Effective boundary** (delay is this divided by information rate):
```
B_{n,w}(b_n) = log(b_n / w_{T_n+1})   — only the weight AT the changepoint matters
q_{n,w}(b_n) ≥ 1 − min(1, W_{T_n}/b_n) — survival (no false alarm before change)
```

## Delay Guarantees (information measure)

Let H = law of F_{P0}(Y) for Y ~ P1 (probability-integral transform of post-change obs under pre-change law). H = U(0,1) iff no change. Separation is D_KL(H‖U).

| Regime | Weights | Delay |
|--------|---------|-------|
| PFA, oracle betting | w_k ∝ k^{-(1+η)}, Σw≤1 | O((1+η)·log T / D_KL(H‖U)) |
| PFA, **near-harmonic** | w_k ∝ 1/(k·log²(e+k)), normalized | O((log T + 2 log log T)/D_KL(H‖U)) ← optimal constant 1 |
| ARL | w_k ≡ 1 | O(log γ / D_KL(H‖U)) |

**First-order minimax optimal**: matching lower bounds log N/D and log γ/D (Theorems 3.9/3.10) over late changepoints T ∈ [⌈κN⌉, N]. No PFA/ARL-valid procedure can detect asymptotically faster. **Exponential improvement** over CTM's Ω(T).

## Betting Class Selection (no oracle knowledge needed)

- **Oracle setting** (Assumption 2): mixture reproduces log-density of H up to log penalty → constant D_KL(H‖U).
- **Directional single bet** (Assumption 4): one profitable g with E_H[g] > E_U[g] → constant I* = sup_γ{γ|J| − Cγ²} where J = E_H[log g] − E_U[log g], C bounds log g curvature. Same ORDER, only constant changes.
- **Single atom prior** (Thm 4.11): prior mass v_f on one good density → delay (B + log(1/v_f))/I_f(H). Hedging over more candidates costs log(1/v_f) per candidate.
- **Nonparametric uniform** (Thm 4.12): over L-Lipschitz H with Kolmogorov separation Δ = ‖H−F_U‖∞ ≤ ε₀/2: delay O((B + log(1/Δ))/Δ²).

## Score Data-Processing Inequality

For score s: X → R with continuous P0-CDF: D_KL(H_s‖U) ≤ D_KL(P1‖P0), **equality iff likelihood ratio L = dP1/dP0 is σ(T_s)-measurable**. The likelihood-ratio score s*(x) = L(x) is the unique lossless score. A poorly chosen score (e.g. projecting text embeddings to a weak axis) silently degrades the information rate and lengthens delay by D_KL(P1‖P0)/D_KL(H_s‖U).

## Null-Bet Regularization (forces a.s. finite stopping)

M̄_{k,t}^ρ = ρ + (1−ρ)M_{k,t}. The deterministic floor ρ·W_t guarantees S_t^ρ ≥ ρW_t → ∞ whenever Σw_k diverges (needed for ARL minimax achievability). Cost: additive log(1/(1−ρ)) in the boundary. Use small ρ (e.g. 0.01–0.05).

## Algorithm (streaming, O(t) per step; keep G_{k,t} table)

```
init: S = Z = 0, G[k][θ] table empty
for t = 1, 2, ...:
    observe X_t; draw λ_t ~ U(0,1)
    p_t = randomized conformal p-value vs X_1..X_t (with score s if used)
    G[t][θ] = f_θ(p_t)                         # new restart
    for k < t: G[k][θ] *= f_θ(p_t)             # update all open bets
    M[k] = ∫ G[k][θ] dΠ(θ)                    # integrate prior
    S_t = Σ_k w_k M[k]; Z_t = max_k w_k M[k]
    if S_t ≥ b or Z_t ≥ b: ALARM at t
```
PFA: b = 1/α, Σw ≤ 1. ARL: b = γ, max w ≤ 1 (+ null-bet ρ).

## Practical Defaults (from the paper's simulations)

- Betting density: f(p) = θ p^{θ-1} with θ ∈ {0.15, 0.3, 0.5, 0.75, 1}, uniform prior — or single f(p) = 0.15·p^{-0.85}
- PFA weights: w_k ∝ k^{-1.1} normalized (or near-harmonic for optimal constant)
- ARL weights: w_k ≡ 1
- Empirical PFA stays below nominal across levels (α = 0.05, horizon 20000, 1000 reps)
- Median delay ~ log T scale; **~350× faster than Vovk's CTM** at the right end of tested T range; gap widens as T grows

## Reusable Patterns

1. **Restart-everywhere beats single-run martingales** for late-change detection: any capital-based test (likelihood ratios, e-processes) dilutes over pre-change history; aggregate per-start statistics with recency-prioritized weights.
2. **Weight-norm regime switch**: ‖w‖₁ ≤ 1 (e-process/FDR-style anytime validity) vs ‖w‖∞ ≤ 1 (e-detector/ARL) — one construction, two guarantees, choose by weight normalization alone.
3. **Conformal p-values as the distribution-free interface**: convert ANY data type into i.i.d. U(0,1) under the null of no change; then all the betting machinery is data-agnostic.
4. **Mixture over betting classes with prior mass v_f**: robustness to unknown alternative costs only log(1/v_f) additive delay per candidate — cheap hedging.
5. **Probability-integral-transform KL as the change metric**: D_KL(H‖U) with H = law of F_{P0}(post-change obs) is the natural separation measure for rank-based detection; likelihood-ratio scoring preserves it exactly.
6. **Deterministic floor (null bet) for a.s. finite stopping**: add ρ to per-start statistics when total weight diverges — turns "crosses eventually w.h.p." into "crosses a.s." at constant boundary cost.
7. **Effective boundary B = log(b/w_{T+1})**: tuning restart weights controls detection delay directly — only the weight at the true changepoint enters the first-order delay.

## Related Skills / Corpus

- `weibull-change-point-detection` (copula-based offline changepoint) — this skill is its online, distribution-free counterpart
- `sharp-pairwise-reduction-pgm-hypothesis-testing` (arXiv:2609.28440) — same-session quantum state discrimination; shared theme: sharp constants in hypothesis testing
- `sequential-quantum-hypothesis-testing` — sequential testing in the quantum setting
- e-detector framework: Shin et al. (2024); conformal CUSUM/SR: Vovk et al. (2021, 2025)

## Verification Notes

- PFA validity: S̃ is a nonnegative martingale w.r.t. p-value filtration → Ville's inequality → P(∃t: S̃_t ≥ 1/α) ≤ α; distribution-free because conformal p-values are i.i.d. U(0,1) under exchangeability.
- ARL validity: e-detector aggregation → E_{P0,∞}[τ] ≥ γ (Theorem 2.7) plus linear early-alarm control P(τ ≤ m) ≤ m/γ.
- Minimaxity: lower bounds via change-of-measure arguments over late-changepoint windows; upper bounds attained with likelihood-ratio score + near-harmonic (PFA) or unit (ARL) weights.
- Sharpness of log T / D: constant 1/D achieved by near-harmonic weights (log log T slack unavoidable).
