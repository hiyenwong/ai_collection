---
name: stateful-streaming-transformer-inference
category: skills
description: "Stateful streaming transformer inference methodology with persistent KV cache, Flash Queries prefetching, and multi-tenant continuous-batching for efficient streaming workloads."
---

# Stateful Streaming Transformer Inference

## Trigger Words
stateful inference, streaming LLM, KV cache persistent, flash queries, continuous batching, O(1) query latency

## Core Idea

Conventional transformer inference engines are request-driven, paying O(n) prefill cost on every query. In streaming workloads where data arrives continuously, this cost is prohibitive. Stateful streaming inference moves prefill off the critical path by maintaining persistent KV cache across queries.

## Key Patterns

### 1. Stateful Session Model
- Persistent KV cache advanced incrementally as new data arrives
- Query latency becomes O(|q|), independent of accumulated context size
- Prefill moved off the critical path entirely
- Contrast: stateless engines discard intermediate state between requests

### 2. Flash Queries (Speculative Prefetching)
- Reclaim idle GPU cycles between data arrivals to pre-evaluate registered questions
- Return cached answers before the user asks
- Structurally impossible in stateless engines (no persistent state)
- Pattern: use compute gaps for speculative computation

### 3. Multi-Tenant Continuous-Batching Scheduler
- Cell-budget admission control for fair resource allocation
- Prefix-aware grouped prefill for efficient batch processing
- Dozens of stateful sessions coexist on single GPU
- Preserves full quadratic self-attention within each session

## Performance
- Up to 5.9x speedup over conventional inference engines (vLLM, SGLang, TensorRT-LLM, llama.cpp)
- Query latency remains constant as accumulated context grows

## Implementation Considerations
- Session lifecycle management (creation, eviction, resource limits)
- Memory budgeting for persistent KV cache per session
- Admission control policies for multi-tenant scenarios
- Trade-off: memory consumption vs. query latency savings

## Source
arXiv: 2605.13784v1 - "Attention Once Is All You Need: Efficient Streaming Inference with Stateful Transformers"
