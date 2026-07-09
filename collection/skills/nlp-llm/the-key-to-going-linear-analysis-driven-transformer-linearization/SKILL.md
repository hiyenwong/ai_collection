---
name: the-key-to-going-linear-analysis-driven-transformer-linearization
description: 'The quadratic cost of causal self-attention severely bottlenecks long-context transformer inference. While numerous post hoc linearization pipelines exist, it is difficult to identify which components. Based on arXiv:2607.07706.'
---

# The Key to Going Linear: Analysis-Driven Transformer Linearization

**arXiv**: 2607.07706 | **Authors**: Anna Kuzina, Paul N. Whatmough, Babak Ehteshami Bejnordi | **Utility**: 0.85

## Overview

The quadratic cost of causal self-attention severely bottlenecks long-context transformer inference. While numerous post hoc linearization pipelines exist, it is difficult to identify which components preserve model quality. This work isolates the effect of state update design in a strict frozen-backbone regime. We show that softmax relies on key-dependent, rank-1 orthogonal projections, elucidating why delta-style networks outperform purely gated accumulation. We identify a potential source of approximation errors and introduce structural interventions, specifically sink tokens, short convolutions, and fixed-budget cache routing, which reduces the remaining gap. We scale this linearization approach across LLaMA and Qwen models up to 32B parameters, outperforming prior post hoc baselines on MMLU and matching the long-context retrieval of complex adaptive-caching frameworks.

## Key Contributions

1. The quadratic cost of causal self-attention severely bottlenecks long-context transformer inference.
2. While numerous post hoc linearization pipelines exist, it is difficult to identify which components preserve model quality.
3. This work isolates the effect of state update design in a strict frozen-backbone regime.
4. We show that softmax relies on key-dependent, rank-1 orthogonal projections, elucidating why delta-style networks outperform purely gated accumulation.

## Implementation Notes

- **Keywords**: transformer
- **Categories**: cs.LG
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: transformer.
