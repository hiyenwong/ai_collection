---
name: mosaic-multi-session-agentic-rl
version: v1.0.0
last_updated: 2026-10-17
description: "Critic-free credit assignment for multi-session agent RL."
arxiv_id: "2610.22174"
authors: "Yilong Xu, Minrui Xu, Xinyu Zhou, Xiang Long, Haochen Tan et al."
tags: [agentic-rl, credit-assignment, multi-session, advantage-shaping, hierarchical-optimization]
---

# Mosaic: Multi-Session Agentic Reinforcement Learning

From arXiv:2610.22174 (2026-10-15).

## Problem

Agentic RL assumes single-session trajectories (one continuously accumulated context). But context compaction and subagent forking produce trajectories spanning multiple sessions — creating a train/inference mismatch, since production agents routinely restart or split context.

## Method

**Multi-Session Agentic RL setting + Mosaic (critic-free hierarchical optimization):**

1. Formalize trajectories with an arbitrary number of sessions.
2. Naive baseline: broadcast trajectory-level advantage to all sessions — ignores which sessions actually contributed, gives no signal for session allocation.
3. **Trajectory level**: incorporate session-usage signals into advantage estimation.
4. **Session level**: shape each session's advantage by its **estimated marginal contribution** (what would the outcome be without this session?).

## Results

- BrowseComp with Qwen3.5-4B: outperforms broadcasting in both context-compaction and subagent-forking scenarios, using fewer sessions on average.
- Improvements in session utility and allocation.

## Reusable Pattern

**Per-segment marginal-contribution shaping.** Any pipeline whose single execution decomposes into reusable/restartable segments (sessions, subagent calls, tool-use episodes, retry attempts) can broadcast the final outcome to all segments — or shape each segment's advantage by its estimated marginal contribution. The shaping needs no critic: estimate counterfactual contribution from trajectory-level statistics. This handles both credit assignment (which sessions earned reward) and allocation (how many sessions to spend). Directly relevant to training real agent harnesses where context windows compact, subagents fork, and restarts happen — the setting most production agents actually live in.

## Resources

- Paper: https://arxiv.org/abs/2610.22174
