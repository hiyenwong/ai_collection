---
name: triage-role-typed-credit-assignment
version: 1.0.0
description: Role-typed credit assignment framework for agentic reinforcement learning that addresses outcome-only credit blind spots
tags:
  - reinforcement-learning
  - agentic-ai
  - credit-assignment
  - llm-agents
  - process-reward
categories:
  - reinforcement-learning
  - agent-research
source: arXiv 2606.32017
date_collected: 2026-07-02
---

# TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning

## Overview

TRIAGE is a role-typed credit assignment framework for agentic reinforcement learning that addresses two critical blind spots in standard GRPO (Group Relative Policy Optimization): punishing useful exploration in failed rollouts and reinforcing redundant actions in successful rollouts.

## Problem Statement

Standard GRPO uses final verifier outcomes as uniform advantages over all action tokens. This outcome-only signal is structurally incomplete:
- **Failed rollouts**: Useful exploration gets punished alongside bad actions
- **Successful rollouts**: Redundant or regressive actions get reinforced alongside decisive progress

## Core Methodology

### 1. Semantic Role Classification
A structured judge classifies each action segment into four roles:
- **Decisive progress**: Actions that directly advance toward the goal
- **Useful exploration**: Actions that gather information but don't directly progress
- **No-progress infrastructure**: Necessary but non-progressive actions (e.g., navigation)
- **Regression**: Actions that undo progress or move away from the goal

### 2. Role-Conditioned Process Rewards
Fixed role-conditioned rules map semantic labels to bounded segment-level process rewards:
- Preserves verifier outcomes as the source of optimization direction
- Adds semantic role axis to outcome credit
- Corrects the two main blind spots of outcome-only credit

### 3. Theoretical Foundation
Role-conditioned credit is proven to be the **optimal segment-level correction** expressible from role labels alone:
- It's a projection of per-segment advantage residual onto the role variable
- Fixed role constants reduce advantage estimation error when the judge is reliable
- Connects to lower-variance policy gradients

## Key Results

### Performance Improvements
- **ALFWorld**: Improves success rates over GRPO for two policy models
- **Search-QA**: Outperforms both scalar judge-derived process reward and outcome-supervised value baselines
- **WebShop**: Reduces environment-facing turns by 14.8% relative to GRPO

### Efficiency Gains
- **ALFWorld**: 10.4% reduction in environment-facing turns on completed rollouts
- **WebShop**: 14.8% reduction in environment-facing turns on completed rollouts

### Ablation Insights
- **Regression detection** inside successful trajectories is the dominant contributor to gains
- **Exploration credit** provides consistent secondary gains
- Gains come from role typing, not merely adding dense rewards

## Implementation Patterns

### Integration with GRPO
```python
# Pseudocode for TRIAGE integration
for rollout in grpo_rollouts:
    segments = segment_trajectory(rollout.actions)
    for segment in segments:
        role = judge_classify(segment)  # decisive/exploration/no-progress/regression
        process_reward = role_conditioned_reward(role)
        segment.advantage = outcome_advantage + process_reward
```

### Judge Design
- Structured judge outputs semantic role labels (not scalar scores)
- Fixed mapping from roles to bounded reward values
- Judge reliability directly impacts correction quality

## Advantages Over Alternatives

| Method | Limitation | TRIAGE Solution |
|--------|-----------|-----------------|
| Outcome-only (GRPO) | Punishes exploration in failures | Role typing preserves exploration credit |
| Scalar process rewards | No semantic distinction between action types | Four-way role classification |
| Value function baselines | Shared backbone causes cross-domain coupling | Decoupled role-conditioned correction |

## When to Use

**Apply TRIAGE when:**
- Training agentic RL systems with multi-step action sequences
- Standard GRPO shows poor sample efficiency
- You need to distinguish exploration from regression in trajectories
- Actions have varying semantic importance (not just final outcome)

**Skip TRIAGE when:**
- Actions are homogeneous in importance
- Simple outcome reward is sufficient
- Computational overhead of judge is prohibitive

## Activation Keywords

agentic RL, credit assignment, process reward, GRPO, role typing, trajectory analysis, exploration credit, regression detection, multi-step agents, LLM agents

## Related Patterns

- [[score-broadcast-decorrelation-credit-assignment]] - Alternative credit assignment via broadcast
- [[ucob-skill-memory-self-distillation]] - Skill memory with bidirectional self-distillation
- [[opcd-on-policy-distillation]] - On-policy distillation for capability integration

## References

- **Paper**: TRIAGE: Role-Typed Credit Assignment for Agentic Reinforcement Learning
- **arXiv**: [2606.32017](https://arxiv.org/abs/2606.32017)
- **Date**: 2026-06-30
- **Categories**: cs.LG, cs.AI
