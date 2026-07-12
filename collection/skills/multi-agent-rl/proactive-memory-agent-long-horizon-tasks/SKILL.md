---
name: proactive-memory-agent-long-horizon-tasks
description: "Proactive memory agent that runs alongside an unmodified action agent to prevent behavioral state decay in long-horizon tasks. Updates structured memory bank from trajectory and selectively injects reminders. Plug-and-play with frontier agents. +8.3pp on Terminal-Bench 2.0, +6.8pp on τ²-Bench. Activation: proactive memory, long-horizon agents, trajectory management, context surfacing, memory retrieval, behavioral state decay."
metadata:
  arxiv_id: "2607.08716"
  published: "2026-07-09"
  authors: "Yifan Wu, Lizhu Zhang, Yuhang Zhou, Mingyi Wang, Bo Peng"
  tags: [proactive-memory, long-horizon-agents, trajectory-management, context-surfacing, memory-retrieval]
---

# Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents

## Overview

In long-horizon tasks, decision-relevant state is often scattered across an expanding trajectory. As trajectories grow, task requirements, environment facts, prior attempts, diagnoses, and open subgoals can be buried in the context window or pushed beyond it, failing to influence decisions when needed. This paper introduces "behavioral state decay" and addresses it with a proactive memory agent.

## Key Innovations

### Behavioral State Decay
- Formalizes the failure mode where relevant state exists in the trajectory but doesn't influence decisions at the right moment
- Distinct from context window overflow — state is present but not surfaced
- Affects both weaker and stronger action agents

### Proactive Memory Agent
- Separate memory agent runs alongside unmodified action agent
- Updates structured memory bank from recent trajectory
- Decides whether to inject a memory-grounded reminder or remain silent
- Plug-and-play with frontier action agents and existing agent harnesses

### Selective Intervention
- Outperforms passive bank exposure, always-on injection, advisor-only guidance, and general retrieval
- Memory is an active intervention mechanism rather than passive retrieval
- Open-weight memory policies trained via SFT and GRPO on Qwen3.5-27B

## Methodology

1. **Memory Bank**: Structured storage of task requirements, environment facts, prior attempts, diagnoses, and open subgoals
2. **Memory Agent**: Observes trajectory, updates bank, decides on injection
3. **Injection Decision**: Selective — only inject when decision-relevant state needs surfacing
4. **Training**: SFT and GRPO on SETA dataset for open-weight memory policies

## Implications

- Memory as active intervention (not passive retrieval) is a paradigm shift for agent design
- Plug-and-play design enables adoption without modifying existing agents
- Open-weight memory policies democratize the capability
- Selective intervention principle applies beyond agents to human-AI interaction

## Pitfalls

- Memory bank structure must be carefully designed for the task domain
- Injection timing is critical — too early or too late reduces effectiveness
- Training memory policies requires curated datasets
- Overhead of running a separate memory agent

## Activation Keywords

proactive memory, long-horizon agents, behavioral state decay, trajectory management, memory retrieval, selective intervention, Terminal-Bench, agent memory, plug-and-play memory agent

## Paper Reference

arXiv:2607.08716 - "Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents" (Jul 2026)
