---
name: learning-from-unverified-peers-via-shared
description: "Learning from Unverified Peers via Shared Residual..."
tags: [cs.AI]
source: arxiv
arxiv_id: 2610.22080v1
utility: 0.9
published: 2026-10-15
---

# Learning from Unverified Peers via Shared Residual Distillation

**Authors:** Feiyang Chen, Runze Ma, Zichen Wang, Jiong Lou, Zihan Wang...
**Published:** 2026-10-15
**arXiv:** [2610.22080v1](https://arxiv.org/abs/2610.22080v1)
**Categories:** cs.AI
**Utility Score:** 0.9

## Abstract

A language model can generate several solutions to the same problem, some leading to correct answers and others to incorrect ones. Many post-training methods turn these trajectories into learning signals using supervision from reference answers, verifiable feedback, or external teachers. Without such supervision, learning from the model's own generations becomes less straightforward, as their correctness cannot be reliably assessed. An incorrect solution may nevertheless contain useful intermediate reasoning, so its value as supervision need not be determined solely by its final answer. Can a model improve by learning from its unverified peer solutions without first determining which are correct? We propose Shared Residual Distillation (SRD), an on-policy self-distillation method that learns from the model's own unverified peer trajectories. SRD compares how peers change the prediction distribution relative to a control, retaining adjustments that agree in direction and are conservative in magnitude. This yields supervision without treating any complete solution as correct, and the trained model requires no peers at inference time. Starting from the corresponding base models, SRD raises mean AIME24--26 avg@12 from 11.02 to 16.20 on Qwen3-1.7B, from 19.07 to 45.46 on Qwen3-4B, and from 21.39 to 54.44 on Qwen3-8B. Controlled ablations support the value of the shared-residual construction, and we observe no degradation relative to the base models on two general-capability benchm

## Key Contributions

- Novel research in cs.AI
- Published 2026-10-15

## Activation

learning, unverified, peers, shared, residual, distillation
