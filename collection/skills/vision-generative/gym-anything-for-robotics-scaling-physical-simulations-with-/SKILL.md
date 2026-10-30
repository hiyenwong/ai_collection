---
name: gym-anything-for-robotics-scaling-physical-simulations-with-
description: "Gym-Anything for Robotics: Scaling physical simulations..."
tags: [cs.RO, cs.AI, cs.LG]
source: arxiv
arxiv_id: 2610.40565v1
utility: 0.89
---

# Gym-Anything for Robotics: Scaling physical simulations with digital agents

**arXiv ID:** [2610.40565v1](https://arxiv.org/abs/2610.40565v1)
**Published:** 2026-10-29
**Authors:** Pranjal Aggarwal, Sean Welleck
**Utility Score:** 0.89

## Abstract

Realistic, fast robotics simulations could enable large-scale training of embodied AI models that transfer to the real world. However, despite decades of progress, available simulations cover only a narrow range of real-world tasks and physical phenomena. The core bottleneck is that creating better simulations requires significant expert effort and therefore does not scale. To address this, we introduce Gym-Anything for Robotics, a framework in which coding agents create realistic robotics simulations. Our core insight is that simulation creation is a coding agent task, so improvements in coding agents translate directly into richer and more faithful simulations. We select simulations based on U.S. GDP data to cover economically valuable physical work, define what makes a good simulation and a good task, and develop an adversarial creation-audit loop that checks each simulation and task against these definitions. Using this pipeline, we build RoboWorld, a set of 25 simulations with 25 test and 175 training RL environments of varying difficulty. Even the best frontier models fail on every RoboWorld test task, achieving an average reward of only 0.06. Building on RoboWorld, we introduce several new ways for frontier models to improve, including in-context learning across repeated attempts, a privileged teacher that reads the simulator state and teaches a student in context, self-assisted learning from the model's own privileged experience, and code policies that generate demons

## Key Contributions

- Research in vision-generative domain with practical applications
- Published in top arXiv categories: cs.RO, cs.AI, cs.LG

## Activation

cs.RO, cs.AI, cs.LG, arxiv paper, utility 0.89
