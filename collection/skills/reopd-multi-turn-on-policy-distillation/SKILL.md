---
name: reopd-multi-turn-on-policy-distillation
category: ai_collection
description: "ReOPD (Replayed-Prefix On-Policy Distillation) methodology for scalable multi-turn agent distillation without environment interaction during training. Addresses the 'prefix trap' in multi-turn OPD via reliability-aware prefix sampling."
tags: [on-policy-distillation, agent-training, multi-turn, prefix-replay, reliability-aware, tool-free-training]
---

# ReOPD: Multi-Turn On-Policy Distillation with Prefix Replay

## Core Problem

Full online OPD for agentic tasks is expensive: each update requires fresh student rollouts through the environment AND teacher queries at visited histories. The "prefix trap": making histories more student-on-policy improves relevance but queries the teacher on histories where its target is unreliable — creating a two-sided distribution shift between student occupancy and teacher reliability.

## Methodology

**ReOPD (Replayed-Prefix On-Policy Distillation)**:
1. Reuse pre-collected teacher trajectories as replayed prefixes
2. Student acts at selected steps; teacher provides dense per-step supervision WITHOUT executing new environment interactions
3. Treat multi-turn OPD as reliability-aware prefix distribution design
4. Implement with step-decaying sampling schedule emphasizing early, lower-shift prefixes

## Key Insights

- Multi-turn OPD has a fundamental prefix trap: on-policy histories → unreliable teacher targets
- ReOPD turns expensive agent-environment interaction into reusable offline resource
- Zero tool calls during student training
- At least 4× faster per training step than full online OPD
- Preserves or improves OPD-level accuracy across mathematical reasoning with Python and search environments

## When to Use

- Training LLM agents on multi-turn interactive tasks (tool use, search, code execution)
- When teacher trajectories are expensive to regenerate but already collected
- When you need scalable distillation across tools, tasks, and environments
- When environment interaction during student training is a bottleneck

## Pitfalls

- Prefix trap: naive on-policy prefix sampling degrades teacher reliability
- Step-decaying schedule is critical — don't uniformly sample all prefix lengths
- Works best when teacher trajectories are high-quality and diverse

## Reference

arXiv:2607.04763 - "Multi-Turn On-Policy Distillation with Prefix Replay" (Liao et al., 2026)

## Activation

ReOPD, multi-turn on-policy distillation, prefix replay, agent distillation, off-environment distillation, prefix trap, agent training distillation, tool-free agent distillation
