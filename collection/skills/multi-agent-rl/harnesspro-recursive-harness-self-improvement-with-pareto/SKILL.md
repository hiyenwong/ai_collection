---
name: harnesspro-recursive-harness-self-improvement-with-pareto
description: "HarnessPro: Recursive Harness Self-Improvement wit..."
tags: [cs.LG, cs.CL]
source: arxiv
arxiv_id: 2610.26770v1
utility: 1.0
published: 2026-10-19
---

# HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for Performance-Cost Trade-offs

**Authors:** Zhuoshi Pan, ZhiYuan Feng, Yukuo Cen, Honglin Lin, Junru Lu...
**Published:** 2026-10-19
**arXiv:** [2610.26770v1](https://arxiv.org/abs/2610.26770v1)
**Categories:** cs.LG, cs.CL
**Utility Score:** 1.0

## Abstract

Harness development plays a crucial role in building capable AI agents. Recent approaches improve harnesses through recursive self-improvement (RSI), but their performance gains often come with higher execution costs. We introduce HarnessPro, a label-free method for evolving harnesses to improve task performance while reducing execution cost. In this setting, candidate harnesses are evaluated using LLM-generated tests without access to ground-truth solutions or official tests. Specialized agents diagnose execution trajectories, plan updates with different performance-cost priorities, and implement them as candidate harnesses. Rather than returning a single harness, HarnessPro uses normalized weighted squared-distance selection to provide cost-focused (lite), balanced (medium), and performance-focused (heavy) harnesses for different deployment budgets. Selected harnesses enter the next iteration, where execution feedback guides further updates. Our experiments cover Terminal-Bench 2, SWE-Bench Pro, and ProgramBench, using GPT-5.5 with Codex and GLM-5.2 with Claude Code. Across these benchmarks using GPT-5.5 with Codex, the heavy mode of HarnessPro achieves an average pass-rate gain of 2.0 percentage points and an average per-task cost reduction of 26.1% relative to RHO. This advantage also holds when using GLM-5.2 with Claude Code. Code is available at https://github.com/pzs19/HarnessPro

## Key Contributions

- Novel research in cs.LG, cs.CL
- Published 2026-10-19

## Activation

harnesspro, recursive, harness, selfimprovement, pareto, optimization, performancecost, tradeoffs
