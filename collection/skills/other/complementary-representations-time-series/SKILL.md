---
name: complementary-representations-time-series
version: v1.0.0
last_updated: 2026-10-17
description: "Pair faithful + invariant views for time-series LMs."
arxiv_id: "2610.22327"
authors: "Hedi Zisling, Liran Nochumsohn, Ilan Naiman, Mihir Parmar, Omri Azencot"
tags: [time-series, language-models, multimodal, invariance, reasoning]
---

# Twice Upon a Time: Complementary Representations for Time-Series Reasoning

From arXiv:2610.22327 (2026-10-15).

## Problem

Time Series Language Models (TSLMs) expose the LM to a single representation, imposing a fixed inductive bias across all downstream tasks — whichever information the chosen representation drops is lost for every task.

## Method

**Complementary representations as a design principle.** Combine two visual views with deliberately distinct invariance profiles:

1. **Line plots** — preserve absolute measurements and the observed coordinate frame (scale/offset sensitive).
2. **Normalized delay embeddings** — factor out positive amplitude rescaling and offsets, exposing pure temporal structure.

Dedicated visual encoders integrate both views into a shared LM via visual tokens + multi-level feature fusion. **Evaluation-time interventions** verify the two views actually have different invariance profiles (the check that the design does what it claims).

## Results

- TSRBench: 44.5% (line plots alone) → 53.2% (dual view), vs 36.7% for the strongest dedicated TSLM baseline.
- TSExam 89.9%; multivariate ChatTS alignment 86.8% numerical accuracy.
- Largest gains beyond basic perception — in prediction and reasoning.

## Reusable Pattern

**Pair a faithful view with an invariant view.** Any representation-learning pipeline whose single embedding bakes in one trade-off can be upgraded by feeding two views engineered to fail differently: one preserving the raw measurement frame, one normalized to expose structure invariant to nuisance transforms. Verify complementarity by intervention (perturb what one view should be invariant to, check the other responds). Generalizes beyond time series: raw-text + syntax-normalized views, image + canonically-aligned views in vision-language models.

## Resources

- Paper: https://arxiv.org/abs/2610.22327
