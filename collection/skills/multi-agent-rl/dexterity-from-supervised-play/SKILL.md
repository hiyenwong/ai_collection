---
name: dexterity-from-supervised-play
description: "Dexterity from Supervised Play..."
tags: [cs.RO, cs.AI]
source: arxiv
arxiv_id: 2610.22340v1
utility: 0.94
published: 2026-10-15
---

# Dexterity from Supervised Play

**Authors:** Botao He, Yiming Dou, Yiannis Aloimonos, Jitendra Malik, Akash Sharma...
**Published:** 2026-10-15
**arXiv:** [2610.22340v1](https://arxiv.org/abs/2610.22340v1)
**Categories:** cs.RO, cs.AI
**Utility Score:** 0.94

## Abstract

How can robots autonomously collect the contact-rich experience needed to learn dexterous manipulation? We present DSP: Dexterity from supervised play, a framework in which a robot learns a play policy from minutes of human play through behavior cloning, then deploys it autonomously to collect hours of interaction data to train a world model. During inference, the same play policy then guides model-predictive control (MPC) by proposing candidate action sequences for evaluation under the learned world model. To accelerate inference, we also introduce a method for distilling a closed-loop, goal-conditioned policy through self-play within the learned world model. We evaluate this framework on underactuated pushing and any-to-any in-hand pose reorientation with a multifingered hand, in simulation and real world. In real world experiment, our method outperforms hindsight behavior cloning by 69.6% in success rate and achieves comparable success to reinforcement learning with 490 times less interaction data. These results demonstrate that supervised play can autonomously collect interaction data, guide model-based planning, and enable policy learning without any task-specific demonstrations or sim-to-real transfer.

## Key Contributions

- Novel research in cs.RO, cs.AI
- Published 2026-10-15

## Activation

dexterity, supervised, play
