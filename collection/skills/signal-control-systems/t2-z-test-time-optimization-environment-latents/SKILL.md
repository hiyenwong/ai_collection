---
name: t2-z-test-time-optimization-environment-latents
description: "T2-z: Test-Time Optimization of Environment Latents for Robotic World Models"
tags: [arxiv, paper, signal-control-systems]
arxiv_id: "2610.22364"
utility: 0.93
date: "2026-10-17"
---

# T2-z: Test-Time Optimization of Environment Latents for Robotic World Models

**arXiv:** [2610.22364](https://arxiv.org/abs/2610.22364)
**Authors:** Chenyuan Zhou, Yining Hong, Huang Huang, Yunfan Jiang, Wenlong Huang...
**Published:** 2026-10-15
**Categories:** cs.RO, cs.AI, cs.CV
**Utility Score:** 0.93

## Abstract

Predicting how the world responds to an action requires more than what can be seen: robots must account for environmental factors that are neither directly observable nor explicitly specified, from physical properties such as friction and mass to human-defined environmental rules. We introduce T2-Z for test-time optimization of environment latents, which augments a robotic world model with a learnable environment latent to condition world predictions. This compact latent captures underlying environmental variation without supervision of what environmental factors exist or what values they take. During training, T2-Z alternates between two stages: a world-model optimization stage that fixes the latents and learns general action-conditioned dynamics across environments; and an environment-latent optimization stage that freezes the world model and optimizes the conditioning latents, allowing latent structure to emerge purely through world prediction. At test time, the world model remains frozen and a newly initialized environment latent is optimized from one or more test-time interactions, adapting the model to previously unseen environmental configurations. Across 7 simulated settings and 4 real-world robotic tasks, T2-Z reduces object prediction error metric from 15.20 to 7.00 and raises action success from 33.73% to 72.96%. Its emergent latents capture structured representations of individual and compounded factors across diverse visual scenes. Ablations further show that T2-Z can efficiently infer environment latents from as little as a single test-time interaction trajectory.

## Key Contributions

- Novel research in cs.RO, cs.AI
- High utility score (0.93) indicating significant research value

## Activation

testtime, optimization, environment, latents, robotic, world, models

## Notes

Added by arXiv cron job on 2026-10-17.
