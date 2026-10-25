---
title: "METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning"
authors: "Ali Najar, Hosein Hasani, Amir Kooshan Fattah, Yasamin Rajabi, Mahdieh Soleymani Baghshah"
published: "2026-10-22"
arxiv_id: "2610.31656v1"
url: "https://arxiv.org/abs/2610.31656v1"
categories: ["cs.LG", "cs.AI"]
utility_score: 0.85
tags: [arxiv, paper, multi-agent-rl]
---

# METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning

**Authors:** Ali Najar, Hosein Hasani, Amir Kooshan Fattah, Yasamin Rajabi, Mahdieh Soleymani Baghshah
**Published:** 2026-10-22
**arXiv:** [2610.31656v1](https://arxiv.org/abs/2610.31656v1)
**Categories:** cs.LG, cs.AI
**Utility Score:** 0.85

## Abstract

Meta-reinforcement learning aims to train agents that adapt quickly to unseen tasks from limited interaction, but this requires representing task evidence over long interaction histories. Classical recurrent agents compress experience into hidden states, while transformer-based agents retrieve from past trajectories at quadratic memory and computation cost. In this work, we propose Memory-Enhanced Test-Time Adaptation (METTA) for meta-reinforcement learning. It decomposes the fast adaptation phase into two temporal scales: a causal neural memory performs fine-grained within-episode adaptation with linear sequence complexity, while compact episode-level summaries support long-range cross-episode task inference without attending over the full interaction history. Moreover, equipping agents with neural memory provides sufficient expressive capacity and test-time training capability, enabling effective adaptation to unseen held-out tasks and task families at meta-test time. On unseen held-out Meta-World ML10/45 test environments, METTA achieves a success rate over $50\%$ while maintaining a low training budget and short wall-clock time. On long-context sparse-reward PointMaze tasks, it outperforms transformer-based baselines by exhibiting more structured exploration behavior. These results show that METTA provides an efficient path toward more adaptive and scalable long-context meta-RL.

## Key Contributions

- Research paper from arXiv, auto-processed by Hermes cron job
- Utility score >= 0.85 indicates high relevance for AI/ML research
- Category: multi-agent-rl

## Related Skills

Check the `multi-agent-rl` directory for related papers and tools.
