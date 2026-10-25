---
name: reverse-kl-tensorization-mcdiarmid
description: "One-sided McDiarmid concentration for heavy-tailed (infinite-variance) functions of independent variables via a new reverse KL tensorization: bounded above + conditional p-moment (p∈(1,2]) suffices for exponential upper-tail decay. Use when applying McDiarmid/bounded-differences to unbounded or heavy-tailed losses, median-of-means risk bounds, or needing KL tensorization inequalities in reverse (conditional-moment) form."
---

# Reverse KL Tensorization → One-Sided McDiarmid for Heavy Tails

**Source**: A One-Sided McDiarmid-Type Inequality for Heavy Tails via Reverse KL Tensorization (arXiv: 2610.21103, math.ST, 2026-10-15)

## Problem

McDiarmid's bounded-differences inequality requires the function to have
**almost surely bounded** deviations in every coordinate. Heavy-tailed losses
(infinite variance, p < 2 moments) violate this, and the standard
Bernstein/sub-Weibull alternatives require variance or sub-exponential tails.
Yet robust statistics (median-of-means, trimmed estimators) still need
exponential deviation control.

## Key Insight

Replace almost-sure boundedness by:

- **Bounded above only** (one-sided), and
- a **conditional moment assumption of order p ∈ (1, 2]**.

Then large deviations *above the mean* are still exponentially unlikely —
even when the function has **infinite variance** (p < 2).

## The New Tool: Reverse KL Tensorization

The proof engine is a new tensorization inequality for Kullback–Leibler
divergence, termed **reverse KL tensorization**:

```
KL( joint ‖ product-of-conditionals-reversed )  ≤  Σ_i  E[ φ_p(conditional deviation) ]
```

It tensorizes the KL divergence across coordinates in the *opposite direction*
to the standard chain rule, charging each coordinate by a conditional moment
functional φ_p instead of a bounded-difference constant c_i. For p → 2 the
charge recovers quadratic (variance-type) behavior; for p < 2 it charges the
p-th moment — the price of heavy tails is a slower exponent, not a broken one.

## What You Get

- One-sided McDiarmid: P[F − EF > t] ≤ exp(−t^p / C(p, moments))
- Concentration of the **sample mean** under p < 2 moments (one-sided)
- Concentration of **median-of-means** estimators
- **One-sided uniform risk bounds for unbounded losses** — usable directly as
  the concentration step in empirical-risk minimization analyses with
  heavy-tailed data.

## Reusable Pattern: "One-Sided Sufficiency"

When a two-sided almost-sure condition (bounded differences) is unavailable:

1. Ask which tail actually matters for the application (upper tail for risk
   bounds, lower tail for coverage guarantees).
2. Impose structure only on that side (bounded above + conditional p-moment).
3. Let the opposite tail carry the heavy-tailed mass.

This asymmetric-conditioning pattern recurs across modern concentration
theory (one-sided Bernstein, lower-tail Talagrand for product measures, heavy
tails via truncation+union).

## Reusable Pattern: "Charge-by-Moment Tensorization"

Standard information-theoretic concentration charges each coordinate by its
worst-case influence (L∞). The reverse-KL tensorization charges by
**conditional moments** — an interpolation between bounded differences
(p=∞ effectively) and Chebyshev (p=1). Use this interpolation consciously:

- Need exponential tails but only have p-th moments → moment-charged
  tensorization with exponent p/(p−1)-type rates.
- Have bounded *conditional* structure (martingale-type filtrations) →
  tensorization in reverse direction exploits exactly that.

## Limitations

- One-sided only: lower tail remains heavy — applications needing two-sided
  control must symmetrize with a separate argument.
- Constants C(p, ·) depend on the conditional moment profile; explicitness
  matters for finite-sample use (paper gives the exact forms).
- For p close to 1 the exponent degrades toward polynomial — the result is
  genuinely exponential only for the upper tail with p > 1.

## Related Skills

- `kl-minimality-distribution-reconstruction` — (today, sibling) KL's special structural role
- `robust-nonparametric-median-of-means` — MoM under α-mixing
- `conformal-e-process-changepoint-detection` — distribution-free online tools
