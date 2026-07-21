---
name: learning-curve-dataset-size-estimation
description: Empirical framework to estimate the minimum training-set size needed to reach a target accuracy, via logarithmic learning-curve fitting and a "stability point" metric. Use when planning data collection campaigns, deciding how much labeled data is enough, or extrapolating total data needs from a small pilot study.
---

# Learning-Curve Dataset-Size Estimation (from arXiv:2607.09402)

Systematic, data-driven method to answer "how much training data do I actually need?" instead of
guessing. Validated on inertial-sensor classification (human activity recognition, smartphone
location) across 6 datasets / 102.7h of recordings, but the framework generalizes to any task where
accuracy grows predictably with data.

## When to use
- Planning a recording / labeling campaign and want to minimize effort while hitting a reliability bar.
- You have a small pilot dataset and need to predict total data requirements for production.
- Traditional heuristics (e.g. "10× classes", fixed per-class counts) are costing you time/money.

## Core findings
- **Accuracy follows a consistent logarithmic growth pattern** w.r.t. dataset size, independent of
  task complexity: `acc(N) ≈ A − B / log(N)` (or equivalently a saturating log curve). Fit this to
  observed (N, acc) points.
- Models often reach *practical stability* with substantially fewer samples than rule-of-thumb
  heuristics suggest.

## Method: Stability Point metric
1. Collect pilot data; train models at several increasing subsample sizes N₁ < N₂ < … Measure accuracy
   at each.
2. Fit a saturating curve `f(N)` to the learning curve (log-growth or power-law saturating form).
   Estimate asymptotic max `A = lim_{N→∞} f(N)` (extrapolate, do not assume 100%).
3. Define the **stability point** N* as the smallest N where the curve stabilizes within a
   predefined **mean absolute percentage deviation (MAPD)** of A:
   `N* = min{ N : |f(N) − A| / A ≤ MAPD }` (e.g. MAPD = 1–2%).
4. Report N* as the recommended minimum dataset size. Extrapolate total needs from the pilot by
   reading off the N where `f(N)` enters the MAPD band.

## Implementation steps
- Use bootstrap or cross-validation to get a stable accuracy estimate at each N (avoid single-run
  noise; learning curves are noisy at small N).
- Fit with scipy `curve_fit` on `log(N)`; bound A ≥ best-observed accuracy.
- Plot acc vs N with the fitted curve + MAPD band shaded; mark N*.
- Sensitivity: vary MAPD to show the tradeoff (tighter MAPD → larger N*).

## Pitfalls
- Log-growth holds for the *in-distribution* regime; distribution shift / new classes breaks the
  extrapolation. Re-estimate when the task or sensor changes.
- Asymptotic A from a short pilot is an upper-bound estimate — under-estimate risk if pilot is too
  small; use conservative A (e.g. 95th percentile of bootstrap fits).
- Data efficiency ≠ model choice invariance: re-fit the curve if you swap architectures.
- Does not replace label-quality checks; garbage labels flatten the curve regardless of N.

## Verification
- Hold out the largest N subset; confirm the predicted N* actually lands inside the MAPD band when
  you train at full data.
- Compare recommended N* against what the old heuristic would have mandated — quantify the savings.
