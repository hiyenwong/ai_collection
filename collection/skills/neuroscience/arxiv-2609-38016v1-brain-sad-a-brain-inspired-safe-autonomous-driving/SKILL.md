---
name: arxiv-2609-38016v1-brain-sad-a-brain-inspired-safe-autonomous-driving
description: "arXiv paper: Brain-SAD: A Brain-Inspired Safe Autonomous Driving Control Framework with Dynamic Fear-Oriented Constraint on Dual-Policy"
tags: [arxiv, cs.AI, research]
created: 2026-10-04
utility: 1.0
---

# Brain-SAD: A Brain-Inspired Safe Autonomous Driving Control Framework with Dynamic Fear-Oriented Constraint on Dual-Policy

**arXiv ID:** 2609.38016v1
**Authors:** Huan Rong, Chao Yin, Anouar Imel et al.
**Published:** 2026-09-29
**Category:** cs.AI
**Utility Score:** 1.0
**URL:** https://arxiv.org/abs/2609.38016v1

## Abstract

Constrained Reinforcement Learning has recently gained increasing attention in the field of Safe Autonomous Driving, where the general mechanism is to maximize the expected reward while keeping the overall action risk bounded. In this way, the safety issues arising in AD can be mitigated through constrained actions. However, existing Constrained RL methods still lack dynamics on the imposed constraints. For instance, the action cost adopted by the existing Primal-Dual/soft-constrained methods is often defined as static state-to-cost mapping, and the safe-action projection in hard-constrained methods relies on the static projection with the fixed feasible region boundary estimated from offline demonstrations. The above drawback tightly couples the imposed constraints to the training scenarios, leaving the AD policy hard to handle different interaction scenarios, due to the improper state-level action-cost and the static projection boundary. Consequently, in this paper, we propose Brain-SAD, a brain-inspired safe autonomous driving control framework with dynamic fear-oriented constraints. By perceiving the current vehicle-interaction scene, Brain-SAD generates dynamic fear signal as fear reaction to online decide long-term policy for regular interaction or short-term policy for urgent-collision defense. In such two policy, the above fear-reaction will be constructed as the dynamic fear constraints, respectively reflecting the overall fear cost directly coupled with action-impact, and the dynamic fear boundary of the feasible region derived from different risky neighbors, both of which will in turn serve for the online policy optimization. Experimental results show that Brain-SAD outperforms existing methods, achieving higher success rate in shorter task-completion and collision-recovery time, and exhibits stronger reliability across continuous intersections of fluctuating complexity.

## Key Contributions

- Novel research in cs.AI
- Published on arXiv: 2026-09-29

## Related Work

See arXiv for citations and references.
