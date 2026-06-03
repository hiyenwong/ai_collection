---
name: ohp-rl-human-preference-guidance
description: "OHP-RL methodology — using online human preference interventions to guide reinforcement learning policy for robot manipulation. Addresses unsafe exploration in real-world RL by encoding human interventions as relative preference signals. Activation: OHP-RL, online human preference, human-in-the-loop RL, robot manipulation RL, human-guided RL, human intervention RL."
---

# OHP-RL: Online Human Preference as Guidance in RL

**Paper:** "OHP-RL: Online Human Preference as Guidance in Reinforcement Learning for Robot Manipulation"
**arXiv:** [2605.15971](https://arxiv.org/abs/2605.15971)
**Authors:** Yunyang Mo, Jian Li, Qiwei Wu, Yihang Kang, Renjing Xu (HKUST-GZ)
**Date:** 2026-05-15

## Core Problem

RL for real-world robots suffers from inefficient and unsafe exploration. Existing human-in-the-loop methods treat interventions as auxiliary training signals without capturing richer preference information about *when* and *how* autonomy should be guided.

## Key Insight

Human interventions encode **relative preferences over behavior** under safety/task constraints, not exact action prescriptions to imitate.

## Method Architecture

### State-Dependent Preference Gate

```
human_intervention → Preference Gate → Policy Gradient Adjustment
     ↓                                      ↓
  state-action history                modulated update
```

The gate `g(s)` adaptively regulates:
- **When** human interventions should shape learning
- **To what extent** they influence policy updates

### Algorithm Steps

1. **Collect** state-action trajectories with intermittent human interventions
2. **Encode** intervention signals as relative preference pairs (not imitation targets)
3. **Compute** state-dependent preference gate value `g(s) ∈ [0, 1]`
4. **Apply** gated preference signal to policy gradient: `∇J = g(s) · ∇J_preference + (1 - g(s)) · ∇J_RL`
5. **Update** policy with modulated gradient

### Design Principles

- Human feedback can be **intermittent and imperfect** — policy still learns autonomously
- Gate preserves **autonomous exploration** while benefiting from guidance
- Stable policy optimization via soft gating (not hard overrides)

## Evaluation

- Tested on 3 contact-rich manipulation tasks (Franka robot)
- Results: Strong success rates, faster convergence, substantially lower human intervention effort vs. baselines
- Learned policies exhibit stable, human-aligned behavior throughout training

## Applications

- Robot manipulation with human supervision
- Safety-critical RL where exploration is constrained
- Any RL task where expert demonstrations are sparse or intermittent

## Related Work

- [[rlhf-from-human-feedback]] - RL from human feedback (scalar rewards)
- [[safe-reinforcement-learning]] - Safety-constrained RL
- [[sdar-self-distilled-agentic-rl]] - Self-distilled agentic RL (complementary dense supervision)
