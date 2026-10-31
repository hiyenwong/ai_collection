---
name: on-the-fundamental-limits-of-prefill-based
description: "On the Fundamental Limits of Prefill-Based Decodin..."
tags: [cs.AI, cs.CL, cs.IT]
source: arxiv
arxiv_id: 2610.40541v1
utility: 0.97
published: 2026-10-29
---

# On the Fundamental Limits of Prefill-Based Decoding Length Prediction

**Authors:** Haowen Shi, Xuzhe Yan, Fahao Chen, Peng Li
**Published:** 2026-10-29
**arXiv:** [2610.40541v1](https://arxiv.org/abs/2610.40541v1)
**Categories:** cs.AI, cs.CL, cs.IT
**Utility Score:** 0.97

## Abstract

Predicting how many tokens a large language model (LLM) will decode, using only prefill-phase hidden states, is a key primitive for inference scheduling. We show that current benchmarks conflate predictor quality with task hardness: when the target model, dataset, or sampling configuration changes, reported accuracy collapses even though the predictor is unchanged. We trace this instability to an overlooked error source---the inherent stochasticity of autoregressive decoding---and derive bounds that every prefill-side method must obey. Our analysis treats decoding as a stopped stochastic process. The per-step stopping probability of a response is not constant but ramps up over hundreds of steps, so the decode length inherits a central limit theorem from the many local decisions that determine where a response ends; this yields per-prompt normality with an explicit error term, together with an affine variance law $σ=αμ+b$ whose slope is the coefficient of variation of the number of response segments. Empirically, the normal law reproduces the per-prompt MAE and the central mass of the decode-length distribution to within a few percent, and the residual departures from normality (mild right skew, slight excess kurtosis) are the ones predicted by the sampling-noise correction. Under fixed model, data, and sampling conditions, a broad design space of predictors (MLP, EGTP, FiLM, soft-label, and Mixture-of-Experts variants) converges to similar performance close to the bound, conf

## Key Contributions

- Novel research in cs.AI, cs.CL
- Published 2026-10-29

## Activation

fundamental, limits, prefillbased, decoding, length, prediction
