---
name: the-geometry-of-agent-memory-forecasting
description: "The Geometry of Agent Memory: Forecasting Retrieva..."
tags: [cs.CL, cs.IR]
source: arxiv
arxiv_id: 2610.26433v1
utility: 1.0
published: 2026-10-19
---

# The Geometry of Agent Memory: Forecasting Retrieval-Bound Memory Failures, and Characterizing Its Limits

**Authors:** Iliya Zhechev, Radoslav Ralev, Chris Coleman, Srijith Rajamohan, Jen Agarwal...
**Published:** 2026-10-19
**arXiv:** [2610.26433v1](https://arxiv.org/abs/2610.26433v1)
**Categories:** cs.CL, cs.IR
**Utility Score:** 1.0

## Abstract

We study whether geometric relationships between conversation turns, memory texts, and queries can predict answer correctness before generation. We evaluate four memory implementations with dense or hybrid retrieval and one observation-summary comparator. We embed these texts in a shared space. A logistic classifier uses 25 features describing query proximity, memory-conversation correspondence, and conversation structure. On LongMemEval-small, pooled AUROC is 0.640 over 2,367 question-system pairs, below a question-difficulty baseline of 0.655. Performance varies by question type: geometry reaches 0.841 on single-session-assistant questions, but system identity alone reaches 0.826. After controlling for difficulty and identity, geometry adds no statistically established pooled improvement (delta = +0.002, 95% CI [-0.010, 0.014]). A fixed-store context-selection experiment finds higher accuracy with proximity-ranked memories than with random subsets, consistent with ordinary retrieval relevance. On LoCoMo, nearest-turn similarity has modest predictive value for single-hop questions and near-chance estimates for several other categories. Training uses correctness labels; prediction uses pre-answer features and no additional LLM generation call. The results characterize associations between memory representations and correctness, rather than establish a reliable deployment diagnostic. In particular, embedding proximity does not verify fact coverage or distinguish memory-constru

## Key Contributions

- Novel research in cs.CL, cs.IR
- Published 2026-10-19

## Activation

geometry, agent, memory, forecasting, retrievalbound, memory, failures, characterizing, limits
