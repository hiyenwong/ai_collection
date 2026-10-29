---
name: scaling-laws-for-tool-use-agents
description: "Research paper: Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis"
tags: [arxiv, paper, cs.LG]
arxiv_id: "2610.37648"
utility: 0.89
---

# Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis

**arXiv:** [2610.37648](https://arxiv.org/abs/2610.37648)
**Authors:** Andrew Szot, Samira Abnar, Omar Attia, Abbas Kazerouni, Michael Kirchhof...
**Published:** 2026-10-27
**Categories:** cs.LG
**Utility Score:** 0.89

## Abstract

We explore how to build performant large language model (LLM) tool-use agents that complete complex, multi-step tasks. Specifically, we study how data composition in synthetically generated tool-use environments affects the training of such agents. To do so, we propose the SynthAPI pipeline, which explicitly controls the diversity of generated environments along the axes of tools, tasks, and the databases on which the tools operate. By systematically varying SynthAPI's generation controls in 458,752 tasks across 849 trained models of four different sizes, we derive a scaling law that predicts downstream tool-use agent generalization based on the scale and composition of the synthesized environments. These predictable relationships reveal several lessons for scaling tool-use agent data. As data budgets grow, scaling tool and database diversity becomes more effective than increasing the number of tasks, and increasing data complexity yields larger gains. Scaling according to these findings yields agents that outperform models trained on data from prior work in large-scale tool-use agent and synthetic environment generation across four evaluation benchmarks.

## Key Contributions

- Paper identified as high-utility (≥0.85) from arXiv scan
- Relevant to: cs.LG

## Potential Applications

- Research reference for multi agent rl domain
- Building block for future work in this area
