---
name: dexterity-supervised-play
description: "Dexterity from Supervised Play"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22340"
utility: 0.99
date: "2026-10-17"
---

# Dexterity from Supervised Play

**arXiv:** [2610.22340](https://arxiv.org/abs/2610.22340)
**Authors:** Botao He, Yiming Dou, Yiannis Aloimonos, Jitendra Malik, Akash Sharma...
**Published:** 2026-10-15
**Categories:** cs.RO, cs.AI
**Utility Score:** 0.99

## Abstract

How can robots autonomously collect the contact-rich experience needed to learn dexterous manipulation? We present DSP: Dexterity from supervised play, a framework in which a robot learns a play policy from minutes of human play through behavior cloning, then deploys it autonomously to collect hours of interaction data to train a world model. During inference, the same play policy then guides model-predictive control (MPC) by proposing candidate action sequences for evaluation under the learned world model. To accelerate inference, we also introduce a method for distilling a closed-loop, goal-conditioned policy through self-play within the learned world model. We evaluate this framework on underactuated pushing and any-to-any in-hand pose reorientation with a multifingered hand, in simulation and real world. In real world experiment, our method outperforms hindsight behavior cloning by 69.6% in success rate and achieves comparable success to reinforcement learning with 490 times less interaction data. These results demonstrate that supervised play can autonomously collect interaction data, guide model-based planning, and enable policy learning without any task-specific demonstrations or sim-to-real transfer.

## Key Contributions

- Novel research in cs.RO, cs.AI
- High utility score (0.99) indicating significant research value

## Activation

dexterity, supervised, play

## Notes

Added by arXiv cron job on 2026-10-17.
