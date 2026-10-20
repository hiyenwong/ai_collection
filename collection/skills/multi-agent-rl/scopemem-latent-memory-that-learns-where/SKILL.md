---
name: scopemem-latent-memory-that-learns-where
description: "ScopeMem: Latent Memory That Learns Where to Revis..."
tags: [cs.AI]
source: arxiv
arxiv_id: 2610.26503v1
utility: 0.9
published: 2026-10-19
---

# ScopeMem: Latent Memory That Learns Where to Revise Frozen GUI Agents

**Authors:** Zhicheng Zheng, Cheng Zhang, Shengping Yu, Tianxiang Zhao
**Published:** 2026-10-19
**arXiv:** [2610.26503v1](https://arxiv.org/abs/2610.26503v1)
**Categories:** cs.AI
**Utility Score:** 0.9

## Abstract

Latent memory is gaining ground as a lightweight history supplement for GUI agents. It supplies history to a frozen vision-language model via prefix vectors trained with step-wise cross-entropy (CE). While resulting gains are naturally attributed to encoded history, our controlled experiments show they primarily stem from action revision. The prefix learns to alter the model's default actions. However, this revision is unscoped because step-wise CE pushes outputs toward reference actions at every step without explicitly preserving correct decisions. Consequently, it repairs errors but also breaks 8-13% of initially correct answers. Overall accuracy metrics hide these losses. We therefore propose ScopeMem, a latent-memory method for scoped revision. Its encoder conditions prefix generation on the model's initial answer and is trained to correct errors while preserving correct decisions. On the controlled ablation set, ScopeMem reduces the share of broken correct decisions to 5.6% while repairing more errors than any evaluated CE-trained prefix. On AndroidControl, GUI-Odyssey, and zero-shot AITW, ScopeMem outperforms all evaluated prompting and latent-memory baselines, enabling a frozen Qwen3-VL-8B to match or surpass GUI-specialized agents and Qwen3-VL-32B.

## Key Contributions

- Novel research in cs.AI
- Published 2026-10-19

## Activation

scopemem, latent, memory, that, learns, where, revise, frozen, agents
