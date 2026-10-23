---
name: wiener-hopf-trading-filters-signal-value
description: "Use when alpha faces trading costs. Wiener-Hopf filters."
category: finance
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [finance, trading, market-microstructure, portfolio-optimization, stochastic-control, prediction-theory]
    related_skills: [eom-gittins-index-futures-delivery, spide-liquidity-profile-clmm, markets-hard-to-predict-framework, wrap-adversarial-deep-hedging, hgf-robust-volatility-updates]
trigger: optimal trading policy, transient price impact, propagator model, trading frictions, Wiener-Hopf factorization, causal filter design, Garleanu-Pedersen, partial adjustment, aim portfolio, two-EMA policy, exponential resilience, power-law impact decay, fractional derivative trading, Ornstein-Uhlenbeck predictor, Matern predictor, alpha decay rate, signal value after costs, actionability of forecasts, spectral placement, coherence, square-root impact, exposure bleeding, stationary quadratic control, LQR limitations, no price manipulation, friction operator, Legendre-Fenchel
---

# Wiener–Hopf Trading Filters and the Value of Predictive Signals

**Source**: "Optimal Trading Filters and the Value of Predictive Signals" — Matteo Smerlak (Capital Fund Management, Paris), arXiv:2610.24558 (q-fin.MF, 17 Oct 2026).

## When to Use

Use when translating return forecasts into positions under **trading costs and transient (lingering) price impact**; when deciding **which predictive signal is worth more after frictions**, not just which forecasts better; when deriving explicit implementable policies (EMA, two-EMA, fractional) instead of solving finite-horizon execution problems; when a claimed alpha's net value must be decomposed into *where its variance sits in frequency* vs *how predictable it is*; when finite-dimensional LQR/MPC state-space control is insufficient because impact memory is non-exponential.

## Core Contribution

Solves the **stationary quadratic trading problem with transient price impact** exactly, using prediction theory instead of dynamic programming:
1. **Wiener–Hopf factorization** of the friction operator F = F−F+ makes the optimal adapted policy explicit: a *conditional forecast of a friction-adjusted signal* composed with a *causal linear filter*.
2. Net attainable value = **½·mean-square of the friction-weighted conditional forecast** — a market-dependent criterion that separates *spectral placement* (signal variance at cheap vs expensive frequencies) from *coherence* (predictability of the exploitable drift).
3. Explicit policy zoo: recovers **Gârleanu–Pedersen** partial adjustment (EMA) under instantaneous costs, the **two-EMA** policy under exponential impact, and **fractional-derivative trading filters** under power-law impact (memory beyond any finite-dimensional LQR realization).
4. **Intermediate optimal signal speed**: under power-law impact with exposure bleeding, too-slow and too-fast OU signals both lose — the optimum mean-reversion rate is θs* = β·√((1−νm)/νm).

## The Model

```
dPt = αt·dt + dMt                    (predictor α; martingale noise M)
∂tπt = ut − β·πt                     (position π; exposure bleeds at rate β≥0; β=0 for stocks, β>0 for e.g. decaying options vega)
It = ∫ g(τ)·u(t−τ)dτ,  Ct = It·ut   (Bouchaud propagator impact, kernel g)

J(π;α) = E[αtπt] − (λ/2)E[πt²] − (1/2)∫g(τ)E[ut u(t−τ)]dτ

Friction operator F = f∗π with symbol
   f̂(ω) = λ + (β² + ω²)·ĝ(ω)
   λ = inventory risk, β²·ĝ = replenishment of bleeding exposure, ω²·ĝ = adjustment cost
Assumptions: ĝ(ω) ≥ 0 (no-price-manipulation, Gatheral), inf_ω f̂(ω) > 0.
```
Adaptedness: πt must be Ft-measurable (Pπ = π, P = conditional expectation). Anticipative benchmark: π_ant = F⁻¹α.

## Wiener–Hopf Solution

```
Factor:      F = F−F+,  F− = (F+)∗,  F+ causal (outer spectral factor, f̂ = |f̂+|²)
             requires log-integrability: ∫ |log f̂(ω)|/(1+ω²) dω < ∞
Optimal:     π* = Kα,  K = (PFP)⁻¹ = F+⁻¹ ∘ P ∘ F−⁻¹
Value:       v* = ½·E[( (P F−⁻¹ α)² )t]      (friction-weighted conditional forecast)
Gross gain:  E[αt·π*t] = 2·v*
Causality gap: v_ant − v* = ½·E[( (I−P)F−⁻¹α )²]
```
**Operational reading**: apply the anticausal inverse friction to the signal (weights FUTURE signal values), take the causal conditional expectation, then rebuild exposure with the causal inverse friction. Do NOT condition the anticipative position directly — condition the friction-transformed one (errors must be measured in the friction norm, not the position norm).

### Transfer function (Gaussian predictor)
```
π̂*(ω) = k̂(ω)·α̂(ω),
k̂(ω) = (1 / (f̂+·Sα,+)) · [ (Sα,+ / f̂−) ]+     ([·]+ = causal projection)
Sα = |Sα,+|²  (outer factor of the predictor spectrum; needs only 2nd-order stats)
Position spectrum:  Sπ*(ω) = (1/f̂(ω))·|[ (Sα,+/f̂−) ]+(ω)|²
Value:   v* = (1/4π)∫ f̂(ω)·Sπ*(ω) dω
```

## Explicit Policies

**Markov (OU) predictor** with decay rate θs (E[α(t+s)|Ft] = e^{−θs·s}αt):
```
π* = F+⁻¹α / f̂+(iθs),    v*(θs) = s²α / (2·f̂+(iθs)²)
changing θs changes only the GAIN of k̂; shape/phase set by market params
```
**Instantaneous costs** (ĝ = η > 0, b = √(λ/η)):  EMA / partial adjustment — Gârleanu–Pedersen
```
∂tπ* + b·π* = α / (η(θs + b)),   v* = s²α / (2η(θs+b)²)
```
**Exponential impact** (ĝ = η + γ/(θm²+ω²)): **two-EMA policy** — GP Prop. 2
```
π*t ∝ w1·EMA_b1[α]/b1 + w2·EMA_b2[α]/b2,  w1+w2=1,  0 < b1 < θm < b2
b1² + b2² = θm² + (λ+γ)/η,   b1²·b2² = λθm²/η
```
**Power-law impact** (ĝ = γ|ω|^(2νm−2), ½<νm<1): **fractional trading**
```
u*t = θs^(1−νm) / (γ(θs+β)) · ∂t^(1−νm) αt
π*t = θs^(1−νm)/(γ(θs+β)) · (∂t+β)⁻¹ ∂t^(1−νm) αt
```
Non-rational transfer ⇒ NO exact finite-dimensional LTI/LQR realization; a sufficiently declining positive signal can rationally induce selling (fractional derivative goes negative).
**Matérn predictor memory** (Sα ∝ (θs²+ω²)^(νs−1), νs<½): smoother signals reshape magnitude AND phase of k̂, not just gain; combined scaling |k̂| ∝ |ω|^(−νm) below θs and |ω|^(−(νm+νs)) above.

## The Value of Predictive Signals (fixed variance s²α)

Frictionless Markowitz value is the SAME for all signals of equal instantaneous strength — costs are where signals differ.
```
Benchmark:  v ≤ v_ant = (1/4π)∫ Sα(ω)/f̂(ω) dω  ≤  s²α / (2·inf_ω f̂(ω))
Coherence:  random-phase sinusoid at ω* = argmin f̂  ATTAINS the bound (v = s²α/2f̂(ω*))
            perfectly predictable oscillation at a costly frequency → value ≈ 0
```
**Decomposition of losses**: (bound − v_ant) = spectral-placement cost (variance parked at expensive frequencies); (v_ant − v*) = causality loss (unavailable future observations).

**Power-law impact + exposure bleeding (β>0, λ=η=0)** — friction = γβ²|ω|^(2νm−2) (replenishment) + γ|ω|^(2νm) (adjustment):
```
v*(OU, θs) = s²α·θs^(2−2νm) / (2γ(θs+β)²)   → vanishes for θs→0 AND θs→∞
Cheapest fully-predictable oscillation:  ω* = β·√((1−νm)/νm)
Optimal OU mean-reversion rate:           θs* = β·√((1−νm)/νm)
Bound:  vmax = s²α·νm^νm(1−νm)^(1−νm) / (2γβ^(2νm))
```
**Smoothness**: rate-optimized Matérn value is nondecreasing in smoothness (νs ↓); at FIXED decay rate the ordering can REVERSE (rough signals better at slow rates — less variance at costly low frequencies). Exponential impact: all Matérn exponents share the same rate-optimized supremum — smoothness only matters through market memory.

## Design Recipe

1. Calibrate frictions: impact kernel g (exponential vs power-law fit), instantaneous cost η, replenishment β, inventory penalty λ; check ĝ ≥ 0 (no self-impact round-trip profits).
2. Build f̂(ω) = λ + (β²+ω²)ĝ(ω); factor f̂ = |f̂+|² (minimum-phase); precompute h+ = inverse kernel of F+⁻¹.
3. Policy (Gaussian/Markov case): π* = F+⁻¹[ z ], z_t = ∫₀^∞ h+(s)·E[α(t+s)|Ft]·ds — i.e. forecast future α with the signal's own law, weight by inverse friction, then filter causally. OU shortcut: π* = F+⁻¹α/f̂+(iθs).
4. Value any signal: v* = ½E[z²]; report the two shortfalls (spectral placement, causality) against s²α/(2·inf f̂).
5. Signal selection: prefer variance concentrated near argmin f̂ with high coherence at that band; under power-law+bleeding pick θs ≈ β√((1−νm)/νm); do NOT compare smoothness at fixed speed — optimize the rate per family first.
6. Empirics: estimate predictive strength JOINTLY with signal dynamics and costs; realized Sharpe and horizon-forecast accuracy are different objects from stationary net value.

## Pitfalls

- **Accuracy ≠ value**: frictionless Markowitz equalizes signals of equal variance; only the friction-weighted forecast discriminates. A perfect forecaster at expensive frequencies can be worthless (sinusoid at high ω with ĝ→∞).
- **Point-estimate conditioning is wrong**: projecting π_ant directly minimizes unweighted error; the correct object is the F+⁻¹-transformed forecast (friction-norm geometry).
- **Finite-memory controllers truncate power-law policies**: fractional ∂^(1−νm) needs long signal history; a finite-dim LQR approximation silently drops the nonlocal term.
- **β flips conclusions**: β=0, λ>0 favors slow signals (f̂ minimized at ω=0); β>0 penalizes persistence and creates an interior optimal speed.
- **Fixed-rate smoothness comparisons invert** vs rate-optimized ones; state which comparison is being made.
- Linearity of impact in trade rate is assumed; decay-law (exponential vs power-law) is market- and estimation-dependent — Bouchaud's order-flow-correlation confound applies when estimating g.

## Connections

- Gârleanu–Pedersen dynamic portfolio choice: this is its stationary, zero-discount specialization + general-kernel extension.
- Obizhaeva–Wang resilient LOB: exponential impact special case.
- Bouchaud propagator market impact: the empirical basis for g; power-law decay is the empirically favored law.
- 2610.25802 (amortized neural filtering for stat-arb): the conditional expectation stage P can be amortized/learned; keeping its second moment (not just the mean) is exactly the value formula v* = ½E[z²].
- 2610.27100 (LOB-impact benchmark): the impact kernel g assumed here is what generative LOB world models must reproduce before agents' simulated policies transfer.
