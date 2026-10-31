---
name: impact-inverter-informed-multimodal-learning-for-photovoltaic
description: "IMPACT: Inverter-Informed Multimodal Learning for ..."
tags: [cs.LG, cs.AI]
source: arxiv
arxiv_id: 2610.40418v1
utility: 0.85
published: 2026-10-29
---

# IMPACT: Inverter-Informed Multimodal Learning for Photovoltaic Generation Forecasting

**Authors:** Anushka Katiyar, Cong Feng, Jing Wang, Tristan Liu, Simon Julien...
**Published:** 2026-10-29
**arXiv:** [2610.40418v1](https://arxiv.org/abs/2610.40418v1)
**Categories:** cs.LG, cs.AI
**Utility Score:** 0.85

## Abstract

This work develops a physics-informed multimodal deep learning framework for 10- to 110-minute-ahead probabilistic photovoltaic power forecasting. The forecasting model is built on a four-branch architecture that separately encodes plant-level temporal history and inverter-level spatial cloud dynamics through a graph attention encoder with a learned adjacency, known-future solar geometry, and the current meteorological state, fused through gated cross-attention. The geometry branch adds two forward-looking physical signals, spatial cloud heterogeneity and inverter ramp-down activity, each empirically weighted toward the horizon where it is most predictive. The decoder anchors its prediction to a smart persistence baseline, learning a horizon-conditioned correction, and the resulting quantile forecasts are calibrated online through a kernel-weighted adaptive conformal calibration step. The proposed model outperforms all 14 baselines, achieving a forecast skill score (FSS) of 0.2950, 0.099 above the next-best model. A branch-composition ablation shows that every branch contributes positively and the model retains substantial skill in challenging overcast and variable sky conditions (FSS 0.198 and 0.255).

## Key Contributions

- Novel research in cs.LG, cs.AI
- Published 2026-10-29

## Activation

impact, inverterinformed, multimodal, learning, photovoltaic, generation, forecasting
