---
name: magic-multi-step-marl
description: MAGIC (Multi-step Advantage-Gated Interventional Causal MARL) — counterfactual action interventions with advantage-gated intrinsic rewards for multi-agent coordination.
---

# MAGIC: Multi-Step Causal MARL

## Overview

Multi-agent RL framework that estimates multi-step causal influence between agents via counterfactual action interventions and converts them into advantage-gated intrinsic rewards.

## Core Methodology

### Problem
- MARL needs learning signals that promote coordination
- Single-step influence insufficient for multi-step effects
- Need to estimate how one agent's action affects teammates over future steps

### Solution: MAGIC Framework
1. **Counterfactual Action Interventions**: Simulate alternative actions and observe teammate futures
2. **Multi-Step Causal Effect**: Measure teammate trajectory divergence under factual vs. counterfactual
3. **Advantage-Gated Intrinsic Rewards**: Gate causal influence by advantage (task-aligned)
4. **CTDE Compatible**: Centralized training, decentralized execution

### Key Algorithm
For each agent:
- Simulate counterfactual action a' instead of factual action a
- Observe teammate trajectories under both branches (multi-step horizon)
- Measure causal influence: Δ(teammate futures)
- Gate by advantage: intrinsic reward = causal_influence × advantage_gate

## Implementation Steps

1. Build multi-agent environment simulator (can simulate counterfactuals)
2. For each agent, sample counterfactual actions
3. Simulate teammate trajectories for factual + counterfactual branches
4. Compute multi-step causal influence metric
5. Apply advantage gate: only promote beneficial coordination
6. Add intrinsic reward to environmental reward

## Applications

- StarCraft micromanagement (SMAC, SMACv2)
- Multi-agent particle environments (MPE)
- Team coordination tasks
- Dec-POMDP with partial observability

## Pitfalls

- **Don't**: Apply intrinsic rewards without advantage gate (distracts from task)
- **Check**: Counterfactual simulation doesn't break CTDE paradigm
- **Monitor**: +26.9% on MPE, +10.1% on SMAC expected

## Related Skills

- [[gcpo-cooperative-policy-optimization]] — cooperative policy optimization
- [[arms-automatic-reward-shaping-marl]] — automatic MARL reward shaping

## Activation Keywords

MAGIC, multi-agent causal influence, counterfactual MARL, advantage-gated intrinsic reward, multi-step coordination, CTDE, causal MARL, StarCraft RL

## Source

arXiv:2605.01805 — MAGIC: Multi-Step Advantage-Gated Causal Influence for Multi-Agent Reinforcement Learning