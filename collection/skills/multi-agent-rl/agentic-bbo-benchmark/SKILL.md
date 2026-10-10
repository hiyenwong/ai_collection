---
name: agentic-bbo-benchmark
description: Use when benchmarking LLM agents on black-box optimization tasks. Combines task semantics, computation, optimization tools, and feedback-driven decisions.
tags: [benchmark, black-box-optimization, LLM-agents, decision-making, tool-use, evaluation]
---

# Agentic BBO Benchmark

## Paper Metadata

- **arXiv ID**: 2610.12183
- **Authors**: arXiv authors
- **Categories**: cs.MA, cs.AI
- **Utility Score**: 0.87
- **Date**: 2026-10
- **Link**: https://arxiv.org/abs/2610.12183

## Key Contributions

- Benchmarks LLM agents on black-box optimization (BBO) tasks
- Combines task semantics, computation, optimization tools, and feedback-driven decision making
- Tests agents' ability to optimize without gradient access — only function evaluations
- Provides a comprehensive evaluation framework for agentic optimization

## Core Methodology

The benchmark tests LLM agents on black-box optimization problems where they must find optimal solutions without access to gradients — only function evaluations (input-output pairs) are available. This mimics real-world optimization scenarios where the objective function is expensive to evaluate and has no analytic form.

The benchmark combines multiple capability dimensions: (1) task semantics — understanding what's being optimized and why, (2) computation — performing necessary calculations, (3) optimization tools — using provided tools (e.g., search algorithms, samplers) effectively, and (4) feedback-driven decisions — learning from evaluation results to guide future queries.

The evaluation measures not just final solution quality but the agent's optimization trajectory: how efficiently it explores the search space, how well it balances exploration vs exploitation, and whether it can transfer optimization strategies across different problem types. This provides a richer assessment than single-metric benchmarks.

## Relevance to multi-agent-rl

Comprehensive benchmark for agentic capabilities: tests the intersection of reasoning, tool use, and iterative decision-making in a setting that mirrors real-world optimization problems.

## Activation

benchmark, black-box-optimization, LLM-agents, decision-making, tool-use, evaluation
