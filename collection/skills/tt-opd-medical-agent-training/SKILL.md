---
name: tt-opd-medical-agent-training
description: "Turn-level Truncated On-Policy Distillation (TT-OPD) methodology for training multi-turn medical AI agents via reinforcement learning. Addresses multi-turn collapse, response length explosion, and tool-use erosion in clinical dialogue. Use when training medical AI agents, RL-based dialogue systems, or multi-turn agentic systems where sparse terminal rewards cause training instability."
---

# TT-OPD: Turn-level Truncated On-Policy Distillation

## Problem
Multi-turn agentic structures in RL training collapse into verbose single-turn monologues, with response length explosion and tool-use frequency erosion. Root cause: misalignment between sparse terminal rewards and sequential clinical trajectories.

## Core Mechanism

### Self-Distillation Architecture
1. Maintain a teacher model updated via gradient-free EMA (Exponential Moving Average)
2. Apply dense, outcome-aware KL regularization at every conversation turn
3. Leverage outcome-privileged information unavailable at inference time

### Key Steps
1. Initialize student and teacher models from same base
2. For each turn in multi-turn dialogue:
   - Compute turn-level reward signal (not just terminal)
   - Apply KL divergence between student output and teacher output
   - Weight KL by outcome quality (privileged signal)
   - Update student; update teacher via EMA of student weights
3. Monitor tool-use frequency as stability metric

## When to Use
- Training multi-turn dialogue agents with RL
- Clinical/medical AI agent training environments
- Any agentic system where GRPO/vanilla RL causes length explosion
- Systems requiring sustained tool-use across conversation turns

## Pitfalls
- Vanilla GRPO achieves strong final accuracy but suffers training instability
- Monitor response length oscillations as early warning of collapse
- Outcome-privileged information must be available during training only
- EMA update rate critically affects convergence speed

## Verification
- Tool-use frequency should remain stable across training
- Response length should not monotonically increase
- Performance on held-out benchmarks should improve steadily
