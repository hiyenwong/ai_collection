---
name: arxiv-2608-19889-write-once-run-everywhere-the-axon-dsl-for-shape-s
description: 'Write Once, Run Everywhere: The Axon DSL for Shape-Safe and Framework-Agnostic LLM Architectures (arXiv: 2608.19889)'
category: nlp-llm
version: "1.0"
date: 2026-08-22
---

# Write Once, Run Everywhere: The Axon DSL for Shape-Safe and Framework-Agnostic LLM Architectures

**Authors:** Jacob Nielsen, Danial Namazifard, Lukas Galke Poech, Peter Schneider-Kamp
**arXiv:** 2608.19889
**Utility:** 1.00
**Published:** 2026-08-20T10:56:34Z
**Link:** http://arxiv.org/abs/2608.19889

## Abstract

The entire ecosystem of open-source language models effectively relies on a single platform. What if this platform was forced to shut down tomorrow? Implementing and maintaining efficient model definitions and translating them between different training and inference regimes is a resource-heavy task that severely limits model efficiency and portability, hindering both scaling and deployment. Here, we present Axon, a strongly typed domain-specific language with Haskell-like syntax, that enables a write-once, run everywhere paradigm for LLM architectures. By basing collaboration on a language specification rather than a specific framework's vision, Axon fosters open cooperation and empowers researchers to implement highly specialized architectures without giving up optimization infrastructure or accepting deployment lock-in. Axon allows for concise, auditable specifications that can be automatically compiled to standalone implementations for leading frameworks: PyTorch, PyTorch with Triton, JAX, MLX and vLLM. In 467 inference benchmarking experiments on models ranging from 135M to 32B parameters, we demonstrate median speedups of 7% on PyTorch, 12% on PyTorch with Triton, 91% on JAX, and 107% on MLX, compared to the reference implementations from Transformers. When deployed as native vLLM architectures with PagedAttention and KV-cache, Axon models achieve a 58% median speedup over Transformers implementations.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Write Once, Run Everywhere: The Axon DSL for Shape-Safe and Framework-Agnostic LLM Architectures". 
The paper presents novel ideas in nlp-llm that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.19889
