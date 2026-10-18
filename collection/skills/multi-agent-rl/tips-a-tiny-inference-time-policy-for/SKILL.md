---
name: tips-a-tiny-inference-time-policy-for
description: "TIPS: A Tiny Inference-time Policy for Scaling in ..."
tags: [cs.LG, cs.AI]
source: arxiv
arxiv_id: 2610.22099v1
utility: 0.92
published: 2026-10-15
---

# TIPS: A Tiny Inference-time Policy for Scaling in Diffusion Language Models

**Authors:** Ya-Shi Zhang, Jian Tang, Pierre-André Noël, Oleksiy Ostapenko
**Published:** 2026-10-15
**arXiv:** [2610.22099v1](https://arxiv.org/abs/2610.22099v1)
**Categories:** cs.LG, cs.AI
**Utility Score:** 0.92

## Abstract

Masked diffusion language models expose an inference-time choice: which positions become visible after each denoising pass. Many existing decoding methods use hand-designed rules or require visibility to grow monotonically. We present a $\textbf{T}$iny $\textbf{I}$nference-time $\textbf{P}$olicy for $\textbf{S}$caling ($\textbf{TIPS}$), an approximately $600$K-parameter controller that learns both unmasking and remasking while keeping the underlying language model frozen. TIPS uses visibility-aware confidence features and a shallow transformer to select which tokens should be visible, while a fixed schedule controls the expected visible fraction. We train the controller through supervised warmup followed by reinforcement learning from terminal correctness rewards. On GSM8K and MATH-500 with LLaDA-8B-Instruct, the full-canvas and two-block TIPS variants achieve $58.46\%$ and $57.97\%$ micro-averaged accuracy at a budget of $32$ decoder evaluations, exceeding the strongest baseline in our main comparison by $12.1$ and $11.6$ percentage points, respectively. Both variants are trained at a budget of $32$ evaluations and remain competitive at higher budgets without retraining. These results demonstrate that learning when to reveal and reconsider tokens can improve the accuracy-compute trade-off without updating the decoder backbone.

## Key Contributions

- Novel research in cs.LG, cs.AI
- Published 2026-10-15

## Activation

tips, tiny, inferencetime, policy, scaling, diffusion, language, models
