---
name: arxiv-2610-01882v1-omaf-one-step-online-multi-agent-flow-policies
description: "OMAF: One-step flow model for online MARL combining expressive generative policies with efficient single-step action generation (3.4x returns, 10.5x sample efficiency)"
tags: [arxiv, multi-agent-rl, flow-models, online-rl, generative-policy, sample-efficiency]
arxiv_id: "2610.01882v1"
utility: 0.88
date_added: "2026-10-05"
---

# OMAF: Flowing Faster to Coordinate — One-Step Online Multi-Agent Flow Policies

**arXiv:** 2610.01882v1 | **Utility:** 0.88 | **Date:** 2026-10-05

## Abstract

Generative policies (diffusion/flow-based) can capture complex multi-modal coordination behaviors but costly iterative sampling hinders scalability in online MARL. OMAF combines expressive generative policies with efficient one-step action generation via a Transformer-based flow policy, achieving up to 3.4× higher returns and 10.5× sample efficiency improvement.

## Key Contributions

- **One-step flow policy**: Eliminates iterative sampling while preserving multi-modal expressiveness
- **Approximate path score surrogate**: Principled route to synchronized flow policy optimization
- **Joint optimization**: Couples softmax Q-value estimation with joint flow policy objective
- **Massive efficiency gains**: 3.4× higher returns and 10.5× sample efficiency across 10 standard tasks (MPE + MAMuJoCo)
- **Tsinghua University work**: Rigorous theoretical foundations

## Methods

1. **Transformer-based flow policy**: Captures complex coordination via self-attention over agent tokens
2. **Path score surrogate**: Approximates the true flow score for tractable optimization
3. **Softmax Q-estimation**: Enables stable value learning for coordinated policies
4. **Joint flow objective**: Synchronizes policy optimization across agents

## Relevance

Solves the key bottleneck of generative policies in online MARL — the sampling cost. One-step generation makes flow-based MARL practical for real-time multi-robot coordination and other latency-sensitive applications. The 10.5× sample efficiency is a major practical advantage when environment interaction is expensive.
