---
name: survicl-synthetic-pretraining-survival
version: v1.0.0
last_updated: 2026-10-17
description: "Synthetic oracle losses beat Cox on censored survival data."
arxiv_id: "2610.22242"
authors: "Julie Alberge, Linus Bleistein, Judith Abécassis, Marine Le Moran, Gaël Varoquaux et al."
tags: [survival-analysis, foundation-models, synthetic-data, quantile-regression, tabular]
---

# SurvICL: In-context Survival Analysis via Synthetic Pretraining

From arXiv:2610.22242 (2026-10-15).

## Problem

Tabular foundation models (TFMs) beat gradient-boosted trees on classification/regression, yet on survival analysis (predicting event timing from censored data, often small clinical cohorts) **no existing TFM beats the half-century-old Cox model**. Censoring breaks standard training losses.

## Method

**SurvICL** — TFM predicting survival curves in-context:

1. Pretrain **purely on synthetic datasets** from a novel flexible **proportional-odds prior** (outperformed other prior types in ablation).
2. Because the synthetic generator knows the true event times, training can use a **plain quantile regression loss on uncensored times** — no censoring-aware surrogate loss needed.
3. Introduce the largest survival benchmark to date: 103 datasets, 63 held out from all design decisions.
4. Zero tuning at inference.

## Results

- Wins 82.9% of pairwise integrated-Brier-score comparisons vs 71.3% for runner-up **Cox** — first model to rank above Cox, including on small datasets.
- Beats 20 tree-based, deep, and foundation-model baselines.

## Reusable Pattern

**Oracle losses from synthetic generators fix censored/biased-data training.** When real training data has a fundamental observation defect (censoring, missing labels, label bias) that forces awkward surrogate losses, pretrain on a synthetic generator that can produce *uncensored ground truth*, allowing the clean standard loss (here: quantile regression). The generator's prior family becomes the key design axis — ablate it (proportional-odds won here). The foundation model then generalizes to real censored data in-context with zero task-specific tuning. Applicable to any partially-observed label domain: time-to-event, competing risks, negative-only feedback (right-censoring in recommendations), and partially-labeled domains.

## Resources

- Paper: https://arxiv.org/abs/2610.22242
