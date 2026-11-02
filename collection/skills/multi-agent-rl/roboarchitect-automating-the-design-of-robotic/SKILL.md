---
name: roboarchitect-automating-the-design-of-robotic
description: "RoboArchitect: Automating the Design of Robotic Ag..."
tags: [cs.RO, cs.AI, cs.CV]
source: arxiv
arxiv_id: 2610.42141v1
utility: 0.9
published: 2026-10-30
---

# RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory

**Authors:** Shengguang Wu, Suning Huang, Cherie Ho, Ria Doshi, Hao Zhu...
**Published:** 2026-10-30
**arXiv:** [2610.42141v1](https://arxiv.org/abs/2610.42141v1)
**Categories:** cs.RO, cs.AI, cs.CV
**Utility Score:** 0.9

## Abstract

Recent work shows that a frozen robot policy performs far better inside an agent harness, where control code decides when to query the policy, consult vision tools, or command the arm directly. Yet today these harnesses are built by hand and redesigned for each new robot or benchmark. We show that harness design can be automated, offering a strong alternative to finetuning on a novel setup. In RoboArchitect, a coding model observes a robot's rollouts, diagnoses failures, and iteratively revises the harness around the frozen policy. The harness evolves on a set of episodes for its optimization and is evaluated on held-out scenes and tasks. Without updating any model weights, RoboArchitect raises average success from 9.7% to 43.3% on unseen scenes (4.5x) and from 12.7% to 40.2% on unseen tasks (3.2x), across multiple benchmarks and policies. The gains are largest where the benchmark is far from the policy's training data: wrapping a general-purpose policy, the evolved harness yields a specialist that often outperforms even the finetuned version. Intuitive control strategies are automatically designed, such as lifting a jammed arm clear or reaching in horizontally when an obstacle blocks the way from above. The harness also evolves its own persistent memory, carrying learned experience, such as effective grasp depths, into later decisions. These results suggest that substantial headroom in robotic manipulation lies in the agent harness, and its design can be effectively automate

## Key Contributions

- Novel research in cs.RO, cs.AI
- Published 2026-10-30

## Activation

roboarchitect, automating, design, robotic, agents, persistent, memory
