---
title: "DIAL: Steerable Language Models with Distilled Instruction-Adherence Levels"
authors: "Thanh Q. Tran, John Russell Himawan, Arun Verma, Kiwan Wong, Wei Xiao..."
published: "2026-10-22"
arxiv_id: "2610.31438v1"
url: "https://arxiv.org/abs/2610.31438v1"
categories: ["cs.AI", "cs.LG"]
utility_score: 0.91
tags: [arxiv, paper, nlp-llm]
---

# DIAL: Steerable Language Models with Distilled Instruction-Adherence Levels

**Authors:** Thanh Q. Tran, John Russell Himawan, Arun Verma, Kiwan Wong, Wei Xiao...
**Published:** 2026-10-22
**arXiv:** [2610.31438v1](https://arxiv.org/abs/2610.31438v1)
**Categories:** cs.AI, cs.LG
**Utility Score:** 0.91

## Abstract

When a user says "Keep it short", how short should the LLM's response be? More generally, users and applications require different levels of instruction adherence, but prompting does not reliably provide fine-grained control over them. We therefore study "steerable language models" that provide fine-grained numerical control over the degree to which models follow general instructions specified in text. However, existing approaches do not jointly offer fine-grained control, efficiency, and scalability across diverse instructions. To address this gap, we introduce DIAL (Distilled Instruction-Adherence Levels) to achieve all three properties. For fine-grained control, we perform classifier-free guidance (CFG) with a frozen LLM to provide training signals for on-policy distillation of instruction adherence at different levels. For efficiency, we design a lightweight steering adapter that uses a classifier over the LLM's hidden states to compute a closed-form steering edit. The classifier adaptively sets the steering magnitude at each token based on the target adherence level, while accounting for the geometry of the LLM's hidden states to preserve response coherence. For scalability, the classifier is text-conditioned, allowing a shared adapter to support new instructions without per-instruction fitting, and training requires only instruction and request text. Evaluation across multiple LLM families shows that DIAL achieves a competitive balance between concept expression and response fluency, with concept scores increasing monotonically across adherence levels. We introduce SteerIF, an instruction-only dataset of 98, 625 concept, persona, verifiable, and descriptive instructions. When trained on SteerIF, DIAL provides fine-grained control over personas and, when combined with prompting, improves verifiable instruction following.

## Key Contributions

- Research paper from arXiv, auto-processed by Hermes cron job
- Utility score >= 0.85 indicates high relevance for AI/ML research
- Category: nlp-llm

## Related Skills

Check the `nlp-llm` directory for related papers and tools.
