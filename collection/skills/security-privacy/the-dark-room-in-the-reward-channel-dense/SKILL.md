---
name: the-dark-room-in-the-reward-channel-dense
description: 'The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and What Actually Works'
metadata:
  {
    "arxiv_id": "2607.21273",
    "utility": 1.0,
    "date_added": "2026-07-26"
  }
---

# The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and What Actually Works

arXiv: 2607.21273  
Published: 2026-07-23  
Utility: 1.0

## Summary
Dense per-step supervision is an appealing remedy for sparse-reward, long-horizon LLM agents: reward the agent for predicting its next observation, and memory should follow. We show that under group-normalized RL (GRPO), this recipe does not merely fail -- it destroys the policy. Across Qwen3-1.7B/4B/8B on ALFWorld, a potential-based prediction reward drives every run into a degenerate absorbing state (prediction accuracy -> 1.0, task success -> 0,episode length pinned at the horizon): the "dark room" pathology, built automatically by the optimizer. A single-factor ablation localizes the cause -- removing only GRPO's std normalization turns the same reward from catastrophic (0%) into baseline parity -- and a two-line proposition explains why: in all-fail groups the z-scored advantage is invariant to the shaping coefficient, so bounded rewards become unbounded pressure and annealing cannot help. Our central insight generalizes this: what z-scoring amplifies is a dense signal's within-group variance while all-fail groups dominate, so signals whose variance decays by mastery are structurally amplifier-safe.This variance-profile criterion retrodicts our collapses, carries preregistered predictions for arms that had not yet run, and is consistent with published reward-channel successes (a compatibility check, not an independent test). Finally, a controlled signal-delivery matrix (identical signal, varying only the consumption mechanism) shows the reward channel is at best neutral ...

## Key Information
- **Title**: The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and What Actually Works
- **Authors**: [Extract from entry]
- **Primary Category**: cs.LG

## Potential Skill Application
This paper presents research relevant to AI agent systems. Consider extracting methodologies, algorithms, or frameworks for skill development.

## Reference
- arXiv: https://arxiv.org/abs/2607.21273
