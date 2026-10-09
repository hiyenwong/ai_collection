---
name: conventionplay-adhoc
description: 'ConventionPlay: Capability-Limited Training for Robust Ad-Hoc Collaboration. Training agents to adapt to partner conventions under asymmetric capability constraints.'
metadata:
  arxiv_id: "2610.11842"
  utility: 0.86
  authors: ["Abhishek Sriraman", "Eleni Vasilaki", "Robert Loftin"]
  published: "2026-10-08"
  categories: ["cs.MA"]
  tags: ["ad-hoc-collaboration", "conventions", "reinforcement-learning", "capability-limits", "multi-agent"]
---

# ConventionPlay: Capability-Limited Training for Robust Ad-Hoc Collaboration

**arXiv:** [2610.11842](https://arxiv.org/abs/2610.11842)
**Utility:** 0.86

## Key Problem

Ad-hoc collaboration requires agents to identify and adhere to shared conventions within cooperative tasks. Existing RL methods train agents to adapt to partner conventions but fail to consider that:
- Some partners follow only a single fixed convention
- Others might have capability limitations

## Innovation

Training framework accounting for **capability-limited partners** in ad-hoc collaboration:
- Agents learn to identify partner conventions
- Adapt to partners with different capability levels
- Maintain robustness across diverse partner populations

## Practical Use

- Build agents that collaborate effectively with diverse partners
- Handle asymmetric capability in multi-agent teams
- Improve robustness of ad-hoc team formation
