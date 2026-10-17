---
name: libero-perm-benchmarking-personalized-robotic-manipulation
description: "LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22372"
utility: 0.97
date: "2026-10-17"
---

# LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation

**arXiv:** [2610.22372](https://arxiv.org/abs/2610.22372)
**Authors:** Zhixu Li, Keqian Tang, Litian Gong, Jingyu Yao, Wenqian Zhang...
**Published:** 2026-10-15
**Categories:** cs.RO, cs.AI, cs.LG
**Utility Score:** 0.97

## Abstract

Personalization is essential for general-purpose robots to transition into household environments and achieve true practicality. While general robotic manipulation has been extensively studied, personalized robotic manipulation (PeRM) lacks a controlled benchmark for separating task completion from preference satisfaction. We introduce LIBERO-PeRM, a benchmark for preference learning in embodied agents. LIBERO-PeRM studies five questions: 1) how policies follow preferences in zero-shot settings; 2) how they learn single preferences from demonstrations; 3) how efficiently they acquire preferences as demonstrations increase; 4) how learned preferences generalize across layouts and tasks; and 5) how policies compose preferences and behave under conflicts. We propose a controlled formulation and taxonomy of observable preferences in simulation, covering motion, skill, and user-profile choices. This formulation is restricted to language-expressible preferences that can be instantiated in LIBERO without changing the task goal, evaluated automatically, and reused across tasks. Building on LIBERO, our procedural pipeline generates paired demonstrations with and without preferences. We create five task suites (312 tasks) with high-quality demonstrations, rich metadata, and preference-satisfaction metrics. Experiments show that current VLA policies struggle with zero-shot personalization, while SFT makes preferences learnable. Mixed training achieves better no-preference retention than sequential adaptation and improves performance with contextual prompts compared with preference-only training, but can weaken motion-preference learning; preference generalization, decomposition, and conflict handling remain difficult. The code, datasets, and demos can be found on the project website: https://libero-perm.github.io/.

## Key Contributions

- Novel research in cs.RO, cs.AI
- High utility score (0.97) indicating significant research value

## Activation

liberoperm, benchmarking, personalized, robotic, manipulation

## Notes

Added by arXiv cron job on 2026-10-17.
