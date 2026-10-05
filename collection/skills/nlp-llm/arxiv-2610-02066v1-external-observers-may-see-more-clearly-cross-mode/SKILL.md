---
name: arxiv-2610-02066v1-external-observers-may-see-more-clearly-cross-mode
description: "arXiv paper: External Observers May See More Clearly: Cross-Model Span-Level Hallucination Detection in Large Language Models via Hidden State Probing"
tags: [arxiv, cs.AI, research]
created: 2026-10-04
utility: 0.95
---

# External Observers May See More Clearly: Cross-Model Span-Level Hallucination Detection in Large Language Models via Hidden State Probing

**arXiv ID:** 2610.02066v1
**Authors:** Kingshuk Gupta, Davide Buscaldi
**Published:** 2026-10-01
**Category:** cs.AI
**Utility Score:** 0.95
**URL:** https://arxiv.org/abs/2610.02066v1

## Abstract

As Large Language Models (LLMs) increasingly serve as foundational reasoning engines, their tendency to hallucinate remains a critical vulnerability. While recent internal state probes offer a promising alternative to slow external retrieval systems, they largely reduce hallucination detection to a token-wise binary classification task, failing to capture the structured, sequential boundaries of semantic drift. Here, we introduce an internal hidden state framework for fine-grained, span-level hallucination detection. By inspecting layer-wise activation patterns, we attempt to detect the exact hallucination onset and continuation tokens in an LLM generation. Our experiments show that this approach successfully isolates hallucination onsets, achieving substantial improvements in Precision-Recall AUC over random baselines despite extreme class imbalance. Ultimately, we propose a novel cross-model detection framework in which one model observes the internal representations elicited by another model's generation. We find that an external observer can match or exceed a generator's self-detection of its own hallucination onsets, including when the observer is the smaller model, suggesting that self-detection is not the ceiling for onset localisation.

## Key Contributions

- Novel research in cs.AI
- Published on arXiv: 2026-10-01

## Related Work

See arXiv for citations and references.
