---
name: magma-bench-embodied
description: 'MAGMA-Bench: Evaluating long-horizon embodied agents under dynamic tasks and execution failures. Use when benchmarking multi-robot coordination with online perturbations.'
arxiv_id: '2610.13534'
utility: 0.86
authors: Loan Bernat, Matthieu Grard, Ariane Herbulot, Florent Lamiraux
categories: [cs.AI, cs.RO]
tags: [embodied-agents, multi-robot, benchmark, long-horizon, dynamic-tasks]
---

# MAGMA-Bench: Long-Horizon Embodied Agent Evaluation

## Key Innovation

Architecture-agnostic benchmark for persistent task reasoning in dynamic multi-robot environments. Evaluates agents across increasing task horizons and controlled online perturbations: execution failures, task interruptions, mission updates.

## Problem

Existing benchmarks investigate either dynamic task execution OR embodied multi-agent coordination, but not their intersection.

## Evaluation Dimensions

- **Task horizon**: Increasing complexity over time
- **Execution failures**: Hardware/software malfunctions
- **Task interruptions**: Mid-execution goal changes
- **Mission updates**: Dynamic requirement modifications
- **Multi-robot coordination**: Heterogeneous robot teams

## Architecture

- Architecture-agnostic: works with any agent framework
- Controlled perturbation injection
- Persistent task reasoning evaluation
- Multi-robot coordination assessment

## Results

- Reveals agent brittleness under combined perturbations
- Identifies specific failure modes in long-horizon tasks
- Benchmarks state-of-the-art embodied agents

## Practical Use

- Evaluating robustness of embodied agent systems
- Benchmarking multi-robot coordination algorithms
- Testing agent resilience to execution failures

## URL

https://arxiv.org/abs/2610.13534
