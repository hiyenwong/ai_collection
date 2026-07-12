---
name: latent-memory-palace-reasoning-control-variational-inference
description: "Latent Memory Palace (LMP): reasoning for control policies as autoregressive variational inference. Organizes information in latent memory palace with iterative adaptive retrieval. LMP-π achieves strong performance with interpretable adaptive test-time compute. Variable-length action tokenizer. Activation: latent memory, reasoning for control, autoregressive variational inference, adaptive reasoning, continuous control."
metadata:
  arxiv_id: "2607.08724"
  published: "2026-07-09"
  authors: "Chuning Zhu, Eva Xu, Jose Barreiros, Krishnan Srinivasan, Paarth Shah"
  tags: [latent-memory, reasoning-for-control, autoregressive-variational-inference, adaptive-reasoning, continuous-control]
---

# Latent Memory Palace: Reasoning for Control as Autoregressive Variational Inference

## Overview

Human decision-making is highly flexible — some actions are taken immediately; others require longer deliberation. Language models exhibit similar adaptive reasoning capacity, but transferring this to continuous control policies has been challenging. Latent Memory Palace (LMP) shows that reasoning for control can emerge by organizing information in an autoregressive latent space reminiscent of a memory palace, formulated as variational inference.

## Key Innovations

### Latent Memory Palace
- Information organized in autoregressive latent space
- Retrieval is iterative and adaptive (like a memory palace)
- Enables reasoning in continuous control, not just language space
- Provides granularity needed for spatial understanding and precise motions

### Variational Inference Formulation
- Reasoning formulated as variational inference with autoregressive latent distribution
- Latent-space RL technique to tractably optimize variational lower bound
- Enables principled optimization of reasoning behavior

### Adaptive Test-Time Compute
- LMP-π exhibits interpretable, adaptive allocation of test-time compute
- Some actions taken immediately; others require more deliberation
- Flexible like human decision-making

### Variable-Length Action Tokenizer
- LMP-tok: same framework yields variable-length action tokenizer
- Significantly improves performance of downstream autoregressive policies
- Connects reasoning and action representation

## Methodology

1. **Latent Distribution**: Define autoregressive latent distribution for reasoning
2. **Variational Bound**: Derive and optimize variational lower bound via RL
3. **Policy Training**: Train LMP-π in simulation and real-world domains
4. **Tokenizer Derivation**: Derive LMP-tok from same framework
5. **Evaluation**: Test in simulation and real-world control tasks

## Implications

- Reasoning for control can emerge from latent space organization
- Variational inference provides a principled framework for adaptive reasoning
- Variable-length tokenization connects reasoning depth to action complexity
- Bridges the gap between LLM reasoning and continuous control

## Pitfalls

- Variational inference optimization via RL can be unstable
- Latent space organization may not be interpretable in high dimensions
- Real-world control evaluation may be limited in scope
- Variable-length tokenizer adds complexity to action decoding

## Activation Keywords

latent memory palace, reasoning for control, autoregressive variational inference, adaptive test-time compute, continuous control, variable-length tokenizer, LMP-π, LMP-tok, latent reasoning

## Paper Reference

arXiv:2607.08724 - "Latent Memory Palace: Reasoning for Control as Autoregressive Variational Inference" (Jul 2026)
