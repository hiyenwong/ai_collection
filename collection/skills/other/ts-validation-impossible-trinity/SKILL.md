---
name: ts-validation-impossible-trinity
category: finance
description: Use when validating time-series models. Prices the causality law.
version: "1.0.0"
source: https://arxiv.org/abs/2609.29530
source_title: The Impossible Trinity of Time-Series Validation
authors: Jiayu Li
published: 2026-09-02
categories: cs.LG, q-fin
trigger_words:
  - time-series validation
  - backtest overfitting
  - purged k-fold
  - embargo
  - walk-forward
  - temporal causality
  - leakage
  - cross-validation
  - financial machine learning
---

# The Impossible Trinity of Time-Series Validation

**arXiv:2609.29530** (Jiayu Li, Sep 2026). Full title: "The Impossible Trinity of Time-Series Validation: A Conservation Law among Training Sufficiency, Test Coverage, and Temporal Causality".

## Overview

The paper proves that for ANY validation scheme on a time series of length T, three demands cannot hold simultaneously — this is a mathematical conservation law, not a design failure:

- **(P1) Training sufficiency** — each training run should use most of the sample (alpha -> 1)
- **(P2) Test coverage** — test sets together cover most of the sample (beta -> 1)
- **(P3) Temporal causality** — training data precedes test data (delta -> infinity, Lambda -> 0)

## The Four Laws (Theorem 1)

Let alpha = worst-fold training fraction, beta = test coverage fraction, Lambda = anti-causal mass (fraction of sample used as FUTURE training data of a test point), delta = distance from a test point to nearest training point in its future.

1. **Ledger**: `alpha + beta <= 1 + Lambda` — every unit of alpha+beta above the causal frontier alpha+beta=1 must be paid with anti-causal training mass. Equality iff test union is a suffix and some fold trains on the entire prefix.
2. **Proximity**: if Lambda > 0 then `delta <= (1-alpha)T` — the future mass cannot be parked far away; distance is paid out of sufficiency.
3. **Trinity**: `alpha + min{beta, delta/T} <= 1` — one inequality puts all three coordinates on a common scale.
4. **Exchange rate**: under beta-mixing, leakage bias at a test point <= `2M * beta_mix(delta)` — **harm depends on the DISTANCE of the violation, not its volume**.

**Key insight**: Volume (Lambda) is harmless; proximity (delta) is harmful. The same Lambda placed at margin h costs only 2M*beta_mix(h); placed adjacent to tests it costs beta_mix(1) — typically orders of magnitude larger. Shuffled vs contiguous 5-fold have identical (alpha, beta, Lambda) = (0.8, 1, 0.8) yet on pure noise report IC +0.32 vs +0.004 — two orders of magnitude spurious skill from proximity alone.

## Scheme Coordinates (Table 2)

| Scheme | alpha (worst) | alpha-bar (mean) | beta | Lambda | delta |
|---|---|---|---|---|---|
| Last-block hold-out | 1-beta0-H/T | 1-beta0-H/T | beta0 | 0 | infinity |
| Expanding walk-forward | w-H/T | 1-(m+1)(1-w)/2m-H/T | 1-w | 0 | infinity |
| Rolling walk-forward | w-H/T | w-H/T | 1-w | 0 | infinity |
| k-fold (contiguous/shuffled) | (k-1)/k | (k-1)/k | 1 | (k-1)/k | 1 (shuffled: everywhere) |
| Purged k-fold + embargo h | (k-1)/k - O(k(2H+h)/T) | approx (k-1)/k | 1 | approx (k-1)/k | >= H+h |

**Corollary 2 (conservation law)**: strictly causal implies alpha+beta <= 1. **Corollary 3**: expanding walk-forward IS the Pareto frontier of causal validation. **Theorem 4**: fully covering causal scheme (beta=1) has average training fraction alpha-bar <= (m-1)/2m < 1/2 — no more than half the data, even on average. k-fold is the extremal buyer: it attains the ledger with equality (combinatorially optimal) but buys all its violations at margin delta=1.

## The Price of Each Vertex

- **Causality violated** -> leakage bias <= 2M * Lambda_eff where Lambda_eff = fold-averaged beta_mix(delta_i(t)); under drift the violation is unpriceable (model has seen the test regime)
- **Sufficiency sacrificed** -> learning-curve bias: E[L-hat] - L(T) <= L(alpha*T) - L(T), systematic pessimism that distorts model comparison — complex models' L(n) decays slower, so small-alpha evaluations favor simple models
- **Coverage sacrificed** -> variance sigma_inf^2/(beta*T) PLUS irreparable worst-case regime error (1-beta)*Delta/2 — a regime never tested may hide anything; no statistics conjures information from unobserved intervals
- **Corollary 8**: no beta drives both bias and variance to zero; the floor strictly exceeds the variance the infeasible alpha=beta=1 point would enjoy

## Hardness = Memory of the Process (Section 4.5)

- **i.i.d. limit (H=0)**: beta_mix(d)=0 — trinity vanishes, shuffled k-fold is fully legitimate
- **Finite memory** (exponential mixing tau): causality can be BOUGHT BACK — embargo h >= several tau caps harm at 2MC*e^{-h/tau} at sample cost O(m(2H+h)/T). This is the mechanism of purged k-fold: it exchanges the volume constraint for a severity constraint, not "breaking" the trinity (Lambda stays (k-1)/k). Window closes when tau or H ~ T/k.
- **Infinite memory / non-stationarity**: NOT redeemable. An embargo redeems only the stationary-dependence part; the non-stationarity part is payable only by walk-forward — whose report answers "could you have made the money at the time", a rehearsal of deployment including the tuning process.

## Operating Card (Section 6)

1. **Measure memory first, choose scheme second**: label horizon H (known) + dependence scale tau (autocorrelation half-life of features/losses). All gaps/purges/embargoes denominated in H + c*tau, c = 2-3.
2. **Stationarity credible, goal = tuning/comparison** -> purged k-fold + embargo (or CPCV). Check k(2H+h)/T << 1, else reduce k.
3. **Non-stationarity feared, quoting expected live performance** -> expanding walk-forward; report per-fold-vs-training-size curve (extrapolates toward L(T)), rehearse tuning inside the rolling procedure.
4. **Tuning must be nested**: inner selection may use item 2; outer strictly causal segment never touched by selection confirms. Winner of N configurations deflated at sigma*sqrt(2 ln N) scale (deflated Sharpe / PBO).
5. **Report coordinates (alpha, alpha-bar, beta, Lambda, delta)** — one line states where the backtest stands; a referee needs only delta/(H+tau) to decide whether to trust Lambda > 0.
6. **Red line**: shuffled k-fold is unusable on any serially dependent data. For a "too-good backtest", the first suspect is always a small-delta leak, never alpha.

## Computing Scheme Coordinates (template)

```python
def scheme_coords(scheme):
    """scheme = list of (train_indices, test_indices), 0-based, ordered by time."""
    T = max(max(max(r), max(e)) for r, e in scheme) + 1
    alpha = min(len(r) / T for r, e in scheme)                 # worst-fold training fraction
    w = sum(len(e) for _, e in scheme)
    alpha_bar = sum(len(r) * len(e) for r, e in scheme) / (T * w)  # coverage-weighted mean
    beta = len(set().union(*[set(e) for _, e in scheme])) / T  # coverage
    Lam = 0.0; delta = float('inf')
    for r, e in scheme:
        rset = set(r)
        for t in e:
            f = [s for s in rset if s > t]
            if f:
                Lam = max(Lam, len(f) / T)
                delta = min(delta, min(s - t for s in f))
    return dict(alpha=alpha, alpha_bar=alpha_bar, beta=beta, Lambda=Lam, delta=delta)
```

Label horizon H > 0: usable training requires s + H <= min E — purge H samples on each side of test blocks (both directions: past labels overlap test label windows, future labels not yet resolved).

## Activation

Use when: designing or auditing a backtest/validation protocol for time-series ML; seeing suspiciously good backtest metrics; choosing between walk-forward / k-fold / purged CV; tuning hyperparameters on financial or other serially dependent data; arguing with a referee/risk manager about validation legitimacy.

## Pitfalls

- Do NOT fixate on Lambda (volume of future data) — compute Lambda_eff = avg beta_mix(delta) instead; two schemes with identical Lambda can differ by 100x in spurious skill
- Learning-curve bias is pessimistic but NOT neutral: it systematically favors simpler models in comparisons at small alpha
- Hold-out vs walk-forward at equal beta are the same point in (alpha, beta); what differs is alpha-bar (up to (1-w)/2) — the folklore table conflates coordinates with customary parameter choices
- Tuning multiplies every edge: variance -> selection bias (sqrt(2 ln N)), leakage -> preferentially selects configs that exploit the leak, sufficiency -> ranking distortion
- k-fold validity for AR with uncorrelated errors (Bergmeir et al.) is not an exception but a small algorithm-specific exchange rate beta_Psi (Theorem 5) — the total-variation bound requires nothing of the algorithm
- Overlapping labels give i.i.d. returns memory: corr(Y_t, Y_{t+d}) = (H-d)+/H for H-period forward-return labels — the dependence envelope that the embargo must exceed
