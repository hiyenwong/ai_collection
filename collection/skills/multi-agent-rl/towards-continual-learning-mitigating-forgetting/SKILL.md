---
name: towards-continual-learning-mitigating-forgetting
description: "Towards Continual Learning: Mitigating Forgetting With Subspace Tuning"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22293"
utility: 0.99
date: "2026-10-17"
---

# Towards Continual Learning: Mitigating Forgetting With Subspace Tuning

**arXiv:** [2610.22293](https://arxiv.org/abs/2610.22293)
**Authors:** Arnav Chavan, Kusha Sareen, Rishabh Tiwari, Abhranil Chandra, Johan Obando-Ceron...
**Published:** 2026-10-15
**Categories:** cs.LG, cs.AI
**Utility Score:** 0.99

## Abstract

Large language models (LLMs) acquire new skills through fine-tuning, but it can destroy capabilities they already have: catastrophic forgetting remains a central obstacle to continual learning in LLMs. Recent works connect forgetting to how far, and along which directions, fine-tuning moves the weights. On-policy methods such as reinforcement learning and on-policy distillation avoid updating the principal singular directions of weight matrices and thus forget less. In contrast, SFT concentrates updates along these directions and is susceptible to catastrophic forgetting. In this work, we introduce Subspace Tuning (SST), which restricts each weight update to the bottom singular subspace, eliminating changes along the principal directions. SST is optimizer-agnostic and composes well with fine-tuning recipes including SFT and self-distillation. SST combines tight subspace protection, dense gradient estimation, and a simple refresh mechanism, enabling stronger learning than prior orthogonal fine-tuning methods. With these mechanisms, protecting as much as 99\% of the weight subspace substantially improves retention while preserving strong target-task performance. This behavior strengthens with model and data size and nearly eliminates forgetting in the large-model regime. SST also keeps the model close to its base distribution, inducing $2$--$4\times$ less KL drift than the baseline recipes. Overall, SST advances the learning--forgetting Pareto frontier, making it a practical default for fine-tuning pre-trained language models.

## Key Contributions

- Novel research in cs.LG, cs.AI
- High utility score (0.99) indicating significant research value

## Activation

towards, continual, learning, mitigating, forgetting, subspace, tuning

## Notes

Added by arXiv cron job on 2026-10-17.
