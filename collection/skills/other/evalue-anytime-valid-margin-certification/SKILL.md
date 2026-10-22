---
name: evalue-anytime-valid-margin-certification
description: E-value certification of robustness margins in safe control
category: ai_collection
---

# Anytime-Valid E-Value Certification of Robustness Margins

Use when selecting robustness/safety margins from online closed-loop data (CBF safety filters, robust MPC, control Lyapunov functions), when conformal prediction is blocked by non-i.i.d. closed-loop data or missing offline calibration sets, or when a statistical certificate must be checkable at EVERY time step without error inflation.

Paper: "Anytime-Valid Certification of Robustness Margins for Safe Control via E-Values" (arXiv:2610.23746, ETH Zuerich Automatic Control Laboratory, Oct 2026).

## Problem

Robust CBF filters tighten the barrier condition with margin c_t: h(f_hat(x_t,u_t)) - c_t >= (1-gamma)h(x_t). Too small -> violations; too large -> conservative or infeasible. The margin must be chosen BEFORE the barrier loss Y_t is observed, and Y_t depends on c_t (circularity). Closed-loop data is non-i.i.d.; no offline calibration set exists.

## Core machinery

1. **Barrier loss**: Y_t := [h(f_hat(x_t,u_t)) - h(x_{t+1})]_+ (positive part of predicted-vs-observed barrier gap). Since Y_t upper-bounds the gap, Y_t <= c_t implies h(x_{t+1}) >= (1-gamma)h(x_t) — the true barrier step condition.
2. **Exceedance risk**: p_t(c) := P(Y_t > c | F_t). Goal: p_t(c_t) <= alpha_0 at every decision time.
3. **Fallback margin** c_max (Assumption 1): known-valid, always feasible; start conservative, shrink online. Candidate grid Gamma = {c^(1) < ... < c^(M)} in [0, c_max).

## E-value certification loop

- Null per candidate: H_0(c) = {P: P(Y_t > c | F_t) >= alpha for all t} ("margin is alpha-insufficient").
- Indicator Z_t(c) = 1{Y_t > c}; test supermartingale with gain lambda in [0, (1-alpha)^-1]:
  **E_t^lambda(c) = E_{t-1}^lambda(c) * [1 + lambda(alpha - Z_{t-1}(c))]**, E_0 = 1.
  Under H_0 each factor has conditional expectation <= 1, so the product is a test supermartingale.
- **Gain mixture** over Lambda = {lambda_1, ..., lambda_L}: E_t(c) = (1/L) * sum E_t^lambda(c) — linearity preserves the supermartingale property; removes sensitivity to one lambda (paper uses {0.2, 0.5, 0.8}).
- **Ville's inequality**: P(sup_t E_t(c) >= 1/delta) <= delta -> threshold 1/delta; **anytime-valid**: check at every step, no peeking penalty, no i.i.d. assumption.
- Certification time tau(c) = inf{t >= 1: E_t(c) >= 1/delta}. Certified set S_t = {c in Gamma: tau(c) <= t}.

## Two key theorems (why this beats naive approaches)

- **No union bound (Theorem 1)**: monotonicity c' >= c implies E_t(c') >= E_t(c) because exceedance events nest ({Y>c'} subset {Y>c}). Certifying c certifies all larger candidates, so all M candidates share ONE error budget delta — no M*delta inflation, no independence or stationarity assumptions.
- **Deployment guarantee (Theorem 2)**: a certificate only proves p_s(c) < alpha for some past time s. Bound the drift: p_t(c) <= p_s(c) + d_t(c; sigma, tau), where d_t = max{L_x*||x_t - x_s|| + L_u*||u_t - u_s|| + Delta_t} (Lipschitz constants from derivative bounds of f, f_hat, h; Delta_t from disturbance-distribution drift). **Deployable set** D_t = {c in S_t: d_t(c) <= alpha_0 - alpha}; deploy min(D_t), else fall back to c_max.
- **Parallel tests (Theorem 3)**: restart all-candidate tests every K steps with error allocation delta_r = delta / (kappa*(r+1)*ln^2(r+1)), kappa = sum 1/(n ln^2 n) ~= 2.11, so sum delta_r = delta: infinitely many restarts still share one budget. Deployable if ANY certificate's drift bound fits.

## Evidence growth and certification time

If p_t(c) <= p_bar(c) < alpha uniformly: log-evidence growth rate g_q(lambda) = (1-q)ln(1+lambda*alpha) + q*ln(1-lambda(1-alpha)); expected certification time E[tau(c)] <= [ln(L/delta) + ln(1+lambda*alpha)] / g_{p_bar(c)}(lambda). One positive-rate gain in the mixture suffices for almost-sure finite certification.

## Results (unicycle maze/corridor navigation, 200 MC trajectories, NVIDIA Isaac Sim)

- All certified variants: deployment-risk violation q_dep = 0% (95% UCB 1.5%), false certification q_cert <= 2.5% — inside the theoretical budget delta.
- **ACI (adaptive conformal inference) q_dep = 99.5%, quantile tracking 65.5%** — they only control time-AVERAGED exceedance frequency; e-value tests control the per-step conditional risk p_t(c_t) <= alpha_0 simultaneously at all decision times.
- Tightest variant V-C: -48% mean margin vs c_max, mission time 54.4 -> 51.3 s; smaller margins improve navigation but permit more realized CBF violations (risk is bounded, not zero).

## Implementation checklist

1. Define h, f_hat, and a provable fallback c_max (feasible input set nonempty => Y <= c_max a.s.).
2. Grid Gamma + gain set Lambda; per-candidate supermartingales; uniform mixture; threshold 1/delta.
3. Each step: observe x_t, compute Y_{t-1}, update all unfinished tests, update certified set S_t.
4. Compute drift bounds d_t (needs L_x, L_u, Delta_t from problem geometry); deploy smallest c with d_t <= alpha_0 - alpha, else c_max.
5. Parallel restarts every K with the log-square delta allocation if operating conditions drift.
6. Validate empirically: report q_dep, q_cert vs delta over MC runs — the guarantee is falsifiable, test it.

## Pitfalls

- Certificate != current safety: past evidence says nothing about NOW; deployment always needs the drift buffer d_t <= alpha_0 - alpha (choose alpha < alpha_0 to leave room).
- lambda range [0, (1-alpha)^-1] keeps update factors nonnegative; larger lambda = faster growth when no exceedance but bigger shrink on violations.
- alpha_0 > 0 still permits individual violations; the guarantee bounds the conditional risk, not realized violations.
- Assumption 2's Lipschitz/density bounds are the price of the transfer theorem — derive from problem geometry (paper Appendix D gives the stencil for unicycle navigation).

**Activation**: robustness margin, CBF safety filter, e-value, anytime-valid, test supermartingale, Ville inequality, online certification, safe control, conformal prediction alternative, exceedance risk
