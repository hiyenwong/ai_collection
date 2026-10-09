---
name: swe-journey-eval
description: 'SWE-Journey: Towards More Realistic Evaluation of Coding Assistants through Long-Horizon, Multi-Turn Interaction. Benchmark for coding agents with real-world task horizons.'
metadata:
  arxiv_id: "2610.11559"
  utility: 0.88
  authors: ["Hexuan Deng", "Yue Wang", "Wenyu Jiang", "Cheng Yang", "Haolin Yang"]
  published: "2026-10-08"
  categories: ["cs.CL", "cs.AI", "cs.MA", "cs.SE"]
  tags: ["coding-agents", "benchmark", "evaluation", "multi-turn", "long-horizon", "swe"]
---

# SWE-Journey: Realistic Evaluation of Coding Assistants

**arXiv:** [2610.11559](https://arxiv.org/abs/2610.11559)
**Utility:** 0.88

## Key Problem

Coding assistants (Claude Code, Codex) are a major LLM agent application, but existing benchmarks are far from real-world use in:
- **Task horizon**: Real development involves long chains of work
- **Interaction length**: Real use requires multi-turn clarification and adaptation

## Innovation

Benchmark designed for **long-horizon, multi-turn interaction**:
- Tasks spanning complete development workflows
- Multi-turn interaction for requirement clarification
- Continuously evolving repository states

## Practical Use

- Evaluate coding agents under realistic conditions
- Compare agent performance on extended development tasks
- Identify gaps between benchmark and real-world performance
