---
name: differential-rtm-ageing-marker-bias
description: Differential RTM bias audit for ageing clocks. Use when validating age-gap biomarkers.
category: ai_collection
---

# Differential RTM — Health-Dependent Prediction Bias in Ageing Markers

**Source**: Prediction bias in biological ageing markers (arXiv:2609.30322, q-bio.QM, 2026-09-30). Large multi-cohort study: AlzEye (65,360 CFPs), ChestX-ray14 (21,733), Merlin abdominal CT (4,984), OASIS-3 brain MRI (1,454), UK Biobank PhenoAge (41,512). DINOv3-Large + linear regression head trained on healthy-only participants.

## Core Finding

All organ-derived ageing clocks (retinal/chest/abdominal/brain age) suffer **differential regression to the mean (differential RTM)**: estimated ages are pulled toward the training-cohort mean age **more strongly in unhealthy than in healthy individuals**. This health-dependent prediction bias:

1. **Persists after calibration** (linear & quadratic calibrators fitted on healthy participants remove only the healthy-group trend; unhealthy-group slope stays significant, p<0.001)
2. **Persists after balanced training** (inverse-frequency age reweighting made the slope difference *larger*: −0.154 vs −0.130 for Retinal Age)
3. **Makes the age-gap ↔ health association inconsistent across age subgroups** — positive in younger subgroups, weakening with age, even *reversing* (Retinal Age OR 1.114 below 50 → 0.955 at 80+; Chest Age 1.051 below 30 → 0.975 at 70+)
4. **Invalidates individual-level use**: in 25–59% of healthy/unhealthy matched pairs the HEALTHY patient had the larger age gap

Root cause: models trained on healthy participants find diseased tissue OOD → harder, noisier predictions → stronger pull toward training mean. Whole-cohort ORs (all ~1.01–1.24, p<0.05) hide this completely.

## Methodology: The Audit Protocol

### Step 1 — Detect differential RTM (slope test)
Fit one OLS on combined data:
```
AgeGap = β0 + β1·Age + β2·Group + β3·Age×Group + ε
```
Age mean-centred; Group 0=healthy, 1=unhealthy. Healthy slope = β1; unhealthy slope = β1+β3. Wald test on β3 = differential RTM test. Expect β3 < 0 (steeper negative slope in unhealthy).

Verified slopes (unhealthy vs healthy): Retinal −0.314/−0.184, Chest −0.257/−0.202, Abdominal −0.115/−0.073, Brain −0.527/−0.372.

### Step 2 — Subgroup association profile
10-year age bands (5-year for narrow-range cohorts). Per subgroup: logistic regression disease ~ AgeGap + Age → OR per +1y gap. Two tests:
- **p_trend**: Wald test on Age×AgeGap interaction (does log-OR drift with age?)
- **p_heterogeneity**: joint Wald test that all subgroup ORs are equal

Report the OR *curve* across age, never a single whole-cohort OR.

### Step 3 — OR decomposition (why the association changes)
log OR ≈ Δ/σ² where:
- **Δ** = healthy−unhealthy mean age-gap difference (coefficient of Group in AgeGap ~ Age + Group within subgroup)
- **σ²** = variance of *residuals* of per-group regressions of AgeGap on Age, pooled

Rule: Δ shrinks with age in most markers; if σ² stays flat/increases → OR falls (Retinal/Chest/Abdominal). If σ² shrinks proportionally with Δ → OR holds (Brain Age stayed ~1.19 in every subgroup despite the *strongest* differential RTM). **Differential RTM alone doesn't dictate the association outcome — must check variance too.**

### Step 4 — Individual-level pairwise ordering
Within each subgroup, pair every healthy×unhealthy sample; report % of pairs where the healthy one has the LARGER gap. >25% everywhere → marker unusable alone for individual assessment.

### Step 5 — Bias-remediation falsification tests
1. Calibrator fitted on healthy (linear + quadratic) → re-run slope test → bias persists
2. Retrain with inverse-frequency age-balanced sampling → re-run → bias persists (or worsens)
3. Interaction-term remedy: add Age×AgeGap to downstream prediction → recovers most subgroup loss

### Step 6 — Cluster-robust inference
CR1 covariance with patient as cluster (patients contribute multiple images). Patient-level bootstrap (1,000 resamples) for MAE/RMSE/Δ/σ². If no patient IDs (Merlin), treat volumes as clusters and flag as limitation.

## Key Numbers (Retinal Age, AlzEye)

| Metric | Value |
|---|---|
| r² (est vs chron age) | 0.745 (Retinal) / 0.918 (Abdominal, best) |
| MAE | 5.31y Retinal / 3.81y Brain |
| Whole-cohort OR | 1.049 [1.032,1.067] — *misleading* |
| OR <50y → 80+y | 1.114 → 0.955 (n.s.) |
| Healthy-larger-gap pairs at 80+ | 59% |

PhenoAge is the negative control: chronological age enters its equation directly with fixed weight → no pull toward training mean → no differential RTM → OR stable 1.069–1.085 in every subgroup. **Any marker that regresses chronological age from data inherits this bias; closed-form biomarker equations don't.**

## Reusable Patterns

1. **Differential RTM test** generalizes to ANY regression-based biological marker trained on a narrow population then applied broadly (ageing clocks, bone age, liver fat scores, cell-type proportions): fit the Group×Covariate interaction on the marker's residual-vs-covariate slope.
2. **Never report a single cohort-level OR** for any age-indexed biomarker; always give the subgroup OR curve + p_trend + p_heterogeneity.
3. **OR = Δ/σ² decomposition** is a cheap diagnostic: compute both within each subgroup to predict whether subgroup associations will be stable.
4. **Healthy-only training creates health-dependent bias**: OOD inputs (disease) get shrunk harder toward the mean. Mitigations that fail: post-hoc calibration, balanced training. Partial mitigation: Age×marker interaction term in downstream models.
5. **Pairwise ordering test** is the honest individual-level metric — a marker can have a "significant" OR yet fail >25% of pairwise comparisons.

## Activation
biological ageing markers, ageing clocks, brain age gap, retinal age, PhenoAge, regression to the mean, differential RTM, prediction bias, age subgroup association, odds ratio decomposition, cluster-robust, biomarker validation, health status prediction
