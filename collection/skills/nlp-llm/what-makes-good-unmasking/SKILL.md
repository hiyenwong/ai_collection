---
title: "What Makes a Good Unmasking Policy? A Controlled Study of Learned Unmasking in Diffusion Language Models"
authors: "Jinya Sakurai, Xun Xu, Jaehong Yoon"
published: "2026-10-22"
arxiv_id: "2610.31576v1"
url: "https://arxiv.org/abs/2610.31576v1"
categories: ["cs.AI"]
utility_score: 0.87
tags: [arxiv, paper, nlp-llm]
---

# What Makes a Good Unmasking Policy? A Controlled Study of Learned Unmasking in Diffusion Language Models

**Authors:** Jinya Sakurai, Xun Xu, Jaehong Yoon
**Published:** 2026-10-22
**arXiv:** [2610.31576v1](https://arxiv.org/abs/2610.31576v1)
**Categories:** cs.AI
**Utility Score:** 0.87

## Abstract

Masked diffusion language models generate tokens in parallel, but their efficiency depends on which predictions are committed. Learned unmasking policies improve the speed--accuracy trade-off, yet differ in supervision, inputs, and capacity, obscuring which choices matter. We view supervised policies as distilling a decoding procedure through a teacher and examine independently what the teacher labels as committable, on which states the policy imitates it, what the policy observes, and how much the number of function evaluations (NFE) must decrease to offset policy overhead. We find that labeling predictions matching the final output is overly permissive at low NFE, and hidden states are weak alone but can complement confidence. About a 10% NFE reduction suffices to offset policy overhead for policies up to 7.5M parameters across tested settings. We therefore train a policy on trajectory-contraction targets, which accept only commitments staying on a reference trajectory, using confidence and hidden states. On LLaDA-8B-Instruct, the resulting 856K-parameter policy achieves the best accuracy--NFE frontier and highest throughput on GSM8K, is competitive at moderate targets on MATH-500 and HumanEval, and largely transfers to Dream-7B-Instruct.

## Key Contributions

- Research paper from arXiv, auto-processed by Hermes cron job
- Utility score >= 0.85 indicates high relevance for AI/ML research
- Category: nlp-llm

## Related Skills

Check the `nlp-llm` directory for related papers and tools.
