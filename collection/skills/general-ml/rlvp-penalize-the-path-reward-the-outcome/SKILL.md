---
name: rlvp-penalize-the-path-reward-the-outcome
description: 'Agents acting on our behalf in the real world (e.g. placing phone calls) must learn online from costly, often irreversible interactions rather than cheap simulator steps. Two things follow. First, dep. Based on arXiv:2607.07435.'
---

# RLVP: Penalize the Path, Reward the Outcome

**arXiv**: 2607.07435 | **Authors**: Bojie Li, Noah Shi | **Utility**: 0.85

## Overview

Agents acting on our behalf in the real world (e.g. placing phone calls) must learn online from costly, often irreversible interactions rather than cheap simulator steps. Two things follow. First, deployability depends on the path, not only the outcome. An agent must respect outcome-neutral constraints such as not repeatedly calling an unresponsive user, respecting business hours, or completing required authentication constraints that outcome-based rewards cannot express, since violating them frequently improves apparent success. Second, because each interaction is expensive, the agent must learn efficiently from very few examples. Reinforcement learning from verifiable rewards (RLVR) is blind to both challenges: it optimizes solely on the outcome and wastes expensive rollouts on all-fail groups where group-relative advantage collapses to zero. Attempts to densify supervision by rewarding progress target the hard-to-verify direction. In contrast, real agentic environments can cheaply detect bad moves. Since group-relative advantage is equivalent to within-group variance, a dense signal helps only when it supplies variance the outcome lacks. A verifiable penalty on the path meets this condition reliably, while a progress potential helps only where partial progress is reachable. The resulting recipe "penalize the path, reward the outcome" achieves high task success with near-zero violations, where outcome-only training violates constraints on nearly every episode. We provide four design rules for effective penalties, including avoidance of the inaction trap that arises when a penalty is used in isolation.

## Key Contributions

1. Agents acting on our behalf in the real world (e.g.
2. placing phone calls) must learn online from costly, often irreversible interactions rather than cheap simulator steps.
3. First, deployability depends on the path, not only the outcome.

## Implementation Notes

- **Keywords**: machine-learning
- **Categories**: cs.LG, cs.AI
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: machine-learning.
