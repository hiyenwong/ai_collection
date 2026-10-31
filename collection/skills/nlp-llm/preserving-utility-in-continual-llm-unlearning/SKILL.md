---
name: preserving-utility-in-continual-llm-unlearning
description: "Preserving Utility in Continual LLM Unlearning via..."
tags: [cs.LG, cs.CL]
source: arxiv
arxiv_id: 2610.40483v1
utility: 0.87
published: 2026-10-29
---

# Preserving Utility in Continual LLM Unlearning via Orthogonal Projections

**Authors:** Juan Belieni, Ana Carolina Erthal, Eliezer de Souza da Silva, Diego Mesquita
**Published:** 2026-10-29
**arXiv:** [2610.40483v1](https://arxiv.org/abs/2610.40483v1)
**Categories:** cs.LG, cs.CL
**Utility Score:** 0.87

## Abstract

Unlearning concerns the task of removing the influence of a sensitive portion of the training data, such as protected, copyrighted or private text, from a model without retraining it from scratch. While unlearning requests happen continuously during a model's lifetime, the vast majority of LLM unlearning methods are ill-suited for iterated removal, yielding steep decay in forgetting and utility upon sequential unlearning. This decay stems from interference between successive updates, as each new deletion can undo earlier ones or push the model further along directions already degraded by them. To address this, we introduce Continual Orthogonal Projection (COP), a gradient-projection scheme that restricts each update to the orthogonal complement of activation subspaces cached from prior forget sets. This approach provably guarantees first-order non-interference with earlier deletions. COP stores only a low-rank basis per layer, requiring neither past gradients nor previous forget sets, and plugs into unlearning methods that update the model through gradient steps on a differentiable loss without modifying its objective. Experiments on standard LLM unlearning benchmarks (TOFU and RWKU) show that COP preserves utility across sequential requests without weakening forgetting, preventing the collapse of standard objectives and forgetting more effectively than continual-specific baselines.

## Key Contributions

- Novel research in cs.LG, cs.CL
- Published 2026-10-29

## Activation

preserving, utility, continual, unlearning, orthogonal, projections
