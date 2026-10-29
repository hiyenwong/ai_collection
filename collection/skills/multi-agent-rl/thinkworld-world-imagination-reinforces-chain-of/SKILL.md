---
name: thinkworld-world-imagination-reinforces-chain-of
description: "Research paper: ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning"
tags: [arxiv, paper, cs.RO, cs.AI, cs.CV]
arxiv_id: "2610.37666"
utility: 0.85
---

# ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning

**arXiv:** [2610.37666](https://arxiv.org/abs/2610.37666)
**Authors:** Chaehyun Kim, Chi-Pin Huang, Jisoo Kim, Min-Hung Chen, Yu-Chiang Frank Wang...
**Published:** 2026-10-27
**Categories:** cs.RO, cs.AI, cs.CV
**Utility Score:** 0.85

## Abstract

Vision-Language-Action (VLA) models have made substantial progress in robotic manipulation, but their generalization remains constrained by the diversity and coverage of action-labeled robot demonstrations. Human videos provide much broader behavioral and environmental experience, while learning from them faces a fundamental trade-off between scalable data and explicit action grounding. We introduce ThinkWorld, a VLA learning framework that grounds action reasoning in world dynamics and strengthens it through reinforcement learning with world imagination. ThinkWorld represents each action thought as a Chain-of-Dynamics (CoD), a sequence of discrete motion tokens that captures the intermediate dynamics connecting the current world to a future state and serves as a common action representation across embodiments. We first initialize CoD with action-labeled demonstrations, then predict the future induced by each CoD and reinforce those whose predictions better match the observed outcome. This enables videos without action annotations to provide direct supervision from observed state transitions, allowing human and robot experience to refine the same reasoning space. Experiments in simulation and on real robots demonstrate effective human-to-robot transfer and strong generalization to unseen tasks and environments.

## Key Contributions

- Paper identified as high-utility (≥0.85) from arXiv scan
- Relevant to: cs.RO, cs.AI, cs.CV

## Potential Applications

- Research reference for multi agent rl domain
- Building block for future work in this area
