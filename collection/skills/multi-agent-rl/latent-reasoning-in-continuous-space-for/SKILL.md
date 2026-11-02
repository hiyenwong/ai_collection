---
name: latent-reasoning-in-continuous-space-for
description: "Latent Reasoning in Continuous Space for Unified M..."
tags: [cs.CV, cs.CL, cs.LG]
source: arxiv
arxiv_id: 2610.42149v1
utility: 1.0
published: 2026-10-30
---

# Latent Reasoning in Continuous Space for Unified Multimodal Models

**Authors:** Byungwoo Jeon, Yoonwoo Jeong, Hyunseok Lee, Minsu Cho, Jinwoo Shin
**Published:** 2026-10-30
**arXiv:** [2610.42149v1](https://arxiv.org/abs/2610.42149v1)
**Categories:** cs.CV, cs.CL, cs.LG
**Utility Score:** 1.0

## Abstract

Unified Multimodal Models (UMMs) achieve remarkable success on diverse multimodal understanding and generation tasks, yet they still struggle to effectively leverage language-based chain-of-thought reasoning for image generation. As a result, existing reasoning-augmented UMMs often fail to inherit the test-time scaling and fine-grained controllability observed in large language models. We attribute this failure to a fundamental modality mismatch: reasoning is performed in a discrete token space, whereas image generation operates in a continuous space. To bridge this gap, we introduce a Latent Reasoning framework in Continuous space (LARC), which alleviates the token-level bottleneck by reasoning over continuous hidden states. Specifically, the training framework consists of two stages: (i) curriculum supervised fine-tuning (SFT), and (ii) information-gain reinforcement learning (RL). First, the curriculum SFT stage gradually converts token-level reasoning into latent reasoning. Subsequently, the information-gain RL stage self-evolves latent reasoning without ground truth supervision. Experiments across diverse text-to-image generation benchmarks show that LARC consistently improves generation quality, prompt following, and compositional fidelity. Notably, LARC achieves state-of-the-art performance on GenEval with a 7%p gain over BAGEL and demonstrates clear test-time scaling behavior, outperforming token-based generation under both parallel and sequential test-time scaling st

## Key Contributions

- Novel research in cs.CV, cs.CL
- Published 2026-10-30

## Activation

latent, reasoning, continuous, space, unified, multimodal, models
