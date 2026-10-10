---
name: attic-kv-cache-rehearsal
description: KV cache compression that rehearses what the model will attend to next, not just what it attended to during caching.
tags: [kv-cache, llm-inference, compression, attention, memory-efficiency]
---

# Attic-KV: KV Cache Rehearsal

## Paper Metadata

- **arXiv ID**: 2610.12133
- **Title**: Attic-KV: KV Cache Rehearsal
- **Categories**: cs.CL, cs.AI, cs.LG
- **Utility Score**: 0.87
- **Date**: 2026-10-10
- **Link**: https://arxiv.org/abs/2610.12133

## Key Contributions

- Introduces a rehearsal-based KV cache compression that scores entries by predicted future attention rather than past attention alone.
- Decouples the caching policy from the generation-time attention distribution, enabling lookahead-aware eviction decisions.
- Demonstrates substantial memory savings with minimal perplexity degradation on long-context benchmarks.
- Provides a principled alternative to attention-history heuristics (e.g., H2O, SnapKV) by modeling what the model will read next.

## Core Methodology

Attic-KV reframes KV cache eviction as a rehearsal problem: instead of retaining tokens that were heavily attended to in the past, it retains tokens that the model is predicted to attend to in upcoming steps. This shifts the signal from retrospective attention mass to prospective attention likelihood.

The method scores candidate cache entries using a lightweight forecast of future attention patterns, informed by the model's own attention dynamics and positional priors. Entries with low predicted future relevance are evicted, while high-predicted entries are preserved even if their historical attention weight was small.

This forward-looking criterion is especially effective for long-context generation, where attention shifts across distant segments and static retention policies accumulate stale entries. The approach composes with standard transformer inference and requires no model retraining.

## Relevance to nlp-llm

Directly addresses the long-context inference bottleneck in LLMs by improving KV cache efficiency. Relevant to serving systems, speculative decoding pipelines, and any deployment where memory bandwidth limits context length or throughput.

## Reference

- Paper: https://arxiv.org/abs/2610.12133
