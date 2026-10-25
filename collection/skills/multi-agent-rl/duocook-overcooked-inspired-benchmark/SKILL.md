---
title: "DuoCook: An Overcooked-Inspired Benchmark for Visual Planning and Coordination"
authors: "Ziyi Jiao, Heng Zhang, Drishti Regmi, Xiaokang Ye, Lianhui Qin..."
published: "2026-10-22"
arxiv_id: "2610.31511v1"
url: "https://arxiv.org/abs/2610.31511v1"
categories: ["cs.AI"]
utility_score: 0.94
tags: [arxiv, paper, multi-agent-rl]
---

# DuoCook: An Overcooked-Inspired Benchmark for Visual Planning and Coordination

**Authors:** Ziyi Jiao, Heng Zhang, Drishti Regmi, Xiaokang Ye, Lianhui Qin...
**Published:** 2026-10-22
**arXiv:** [2610.31511v1](https://arxiv.org/abs/2610.31511v1)
**Categories:** cs.AI
**Utility Score:** 0.94

## Abstract

Coordinating two players in a cooking task requires a vision-language agent to track changing scene states, sequence recipe steps, and allocate shared resources under a time budget. We introduce an Overcooked-inspired benchmark for evaluating these capabilities in Unreal Engine environments constructed using coding agents. A single vision-language model controls both players from top-down visual observations, selecting high-level actions while the engine executes navigation. The benchmark contains 20 maps in five categories. These categories support evaluation of centralized coordination under equipment contention, changing terrain, and handoff dependencies. A prop legend and pot ingredient-count indicators provide explicit visual cues, while grid-based destinations support spatial grounding. The evaluation compares four VLMs on all 20 maps, measuring task score, order completion, delivery precision, action acceptance rate, and model API expenditure. A memory ablation on the same 20 maps examines the effect of a shared, self-authored notebook while retaining six-response action history in both conditions. The strongest evaluated model, \texttt{gpt-6-astra}, achieves 26.2\% mean order completion. Notebook memory has mixed score effects across models, with positive mean differences for Claude and Qwen and negative differences for GPT and Gemini.

## Key Contributions

- Research paper from arXiv, auto-processed by Hermes cron job
- Utility score >= 0.85 indicates high relevance for AI/ML research
- Category: multi-agent-rl

## Related Skills

Check the `multi-agent-rl` directory for related papers and tools.
