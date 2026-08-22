---
name: arxiv-2608-20114-decowam-decoupled-whole-body-world-action-model-fo
description: 'DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation (arXiv: 2608.20114)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation

**Authors:** Siyuan Ma, Boshi Zhang, Yutian Zhang, Qinglian Wu, Jiaqi Zhai, Dong Wei, Qiaojun Yu
**arXiv:** 2608.20114
**Utility:** 1.00
**Published:** 2026-08-20T14:44:11Z
**Link:** http://arxiv.org/abs/2608.20114

## Abstract

Mobile manipulation requires a robot to predict how locomotion and arm motion jointly alter future observations and control. Existing world-action models, developed largely for fixed-base platforms, do not explicitly distinguish camera ego-motion from base and arm actions. Here we introduce DECOWAM, a whole-body world-action model that separates these factors through dedicated conditional interfaces. DECOWAM freezes an adapted FastWAM backbone and trains residual adapters, an action-equivalent future bottleneck distilled from privileged observations, adversarially separated base and arm latents, and base-velocity conditioning for video prediction. We further introduce ARMDOG, a real-robot dataset that synchronizes video, whole-body state and action, and language. On a fixed replay protocol, DECOWAM improved both future-video and action prediction over FastWAM, reducing action MSE by 21.7% with 25.95M trainable adaptation parameters. Across 79 closed-loop trials per method, it achieved the highest observed whole-body coordination and base-displacement robustness among the compared systems, while task completion remained comparable to the strongest baseline. These results show that embodiment-aware factorization can support parameter-efficient joint visual prediction and whole-body control under moving viewpoints.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation". 
The paper presents novel ideas in multi-agent-rl that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.20114
