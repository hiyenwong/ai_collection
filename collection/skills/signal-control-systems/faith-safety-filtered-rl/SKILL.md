---
name: faith-safety-filtered-rl
description: "Feasibility-Aware Safety-Filtered RL separating safety from task performance via analytic safety functions, addressing myopia of classical filters to long-horizon return."
tags: [safe-rl, safety-filter, feasibility, control-systems, long-horizon, signal-control-systems]
---

# FAITH: Feasibility-Aware Safety-Filtered RL

Derived from arXiv:2610.12432 — FAITH: Feasibility-Aware Safety-Filtered RL

## Paper Metadata

- **arXiv ID**: 2610.12432
- **Category**: signal-control-systems
- **Utility Score**: 0.87
- **Date**: October 2026
- **Link**: https://arxiv.org/abs/2610.12432

## Key Contributions

- Safety-filtered RL framework that cleanly separates safety enforcement from task performance optimization
- Requires only an analytic safety function, avoiding learned safety critics that may be unreliable
- Identifies and addresses the myopia problem: classical safety filters are short-sighted with respect to long-horizon return
- Feasibility-aware mechanism that preserves task performance while maintaining strict safety guarantees

## Core Methodology

FAITH introduces a safety-filtered reinforcement learning architecture where safety and task performance are decoupled. The safety filter operates as a separate module that modifies the policy's actions to ensure constraint satisfaction, while the underlying RL agent focuses purely on task optimization. This separation allows each component to be designed and verified independently.

The framework requires only an analytic safety function — a mathematical specification of safe states — rather than learned safety critics that may introduce approximation errors. This design choice provides stronger safety guarantees but requires domain knowledge to specify the safety function correctly.

A key insight is that classical safety filters are myopic: they ensure immediate safety but may sacrifice long-horizon return by blocking actions that are temporarily unsafe but lead to high-reward trajectories. FAITH addresses this through feasibility-aware filtering that considers the long-term consequences of safety interventions, allowing the agent to navigate around safety constraints rather than being permanently blocked by them.

## Relevance to Category

FAITH directly addresses core challenges in safety-critical control systems: how to enforce hard safety constraints while preserving task performance, and how to avoid the myopia that plagues reactive safety mechanisms. The framework is applicable to robotics, autonomous vehicles, industrial control, and any domain where safety violations are catastrophic but task performance still matters.

## Activation

faith-safety-filtered-rl, 2610.12432, safe rl, safety filter, feasibility, analytic safety function

## References

- arXiv: https://arxiv.org/abs/2610.12432
