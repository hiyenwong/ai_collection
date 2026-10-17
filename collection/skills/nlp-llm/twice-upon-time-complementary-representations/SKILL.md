---
name: twice-upon-time-complementary-representations
description: "Twice Upon a Time: Complementary Representations for Time-Series Reasoning"
tags: [arxiv, paper, nlp-llm]
arxiv_id: "2610.22327"
utility: 0.89
date: "2026-10-17"
---

# Twice Upon a Time: Complementary Representations for Time-Series Reasoning

**arXiv:** [2610.22327](https://arxiv.org/abs/2610.22327)
**Authors:** Hedi Zisling, Liran Nochumsohn, Ilan Naiman, Mihir Parmar, Omri Azencot
**Published:** 2026-10-15
**Categories:** cs.LG, cs.AI, cs.CL
**Utility Score:** 0.89

## Abstract

Time Series Language Models (TSLMs) enable language-based understanding and reasoning over temporal data, yet a fundamental question remains: what information should their time-series representations preserve, and what variation should they factor out? Existing TSLMs typically expose the language model to a single representation, imposing a fixed inductive bias across downstream tasks. We instead introduce complementary representations as a design principle for time-series reasoning. Our model combines two visual views: line plots preserve absolute measurements and the observed coordinate frame, while normalized delay embeddings factor out positive amplitude rescaling and offsets while exposing temporal structure. Dedicated visual encoders integrate both views into a shared language model through visual tokens and multi-level feature fusion. Evaluation-time interventions verify that the two views exhibit distinct invariance profiles, while single-view ablations show that their combination is particularly beneficial beyond basic perception, with the large gains in prediction and reasoning. Built on Qwen3-VL-8B, our dual-view model improves overall TSRBench accuracy from 44.5% with line plots alone to 53.2%, substantially exceeding the strongest evaluated dedicated TSLM baseline at 36.7%. It further achieves 89.9% accuracy on TSExam and 86.8% numerical accuracy on multivariate ChatTS alignment. Together, these results demonstrate that complementary representations provide an effective design principle for general-purpose TSLMs, enabling models to exploit temporal structure without sacrificing access to the original measurement frame.

## Key Contributions

- Novel research in cs.LG, cs.AI
- High utility score (0.89) indicating significant research value

## Activation

twice, upon, time, complementary, representations, timeseries, reasoning

## Notes

Added by arXiv cron job on 2026-10-17.
