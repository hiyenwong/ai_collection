---
name: multi-agent-ai-control-distributed-attacks-hamper-per-instance-monitors
description: 'AI control is a family of techniques to prevent an AI with malicious goals from subverting its operators intent. AI Control usually studies a single agent in one trajectory, but real deployments run. Based on arXiv:2607.07368.'
---

# Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors

**arXiv**: 2607.07368 | **Authors**: Oliver Makins, Orazio Angelini, Zohreh Shams, Mary Phuong | **Utility**: 0.92

## Overview

AI control is a family of techniques to prevent an AI with malicious goals from subverting its operator's intent. AI Control usually studies a single agent in one trajectory, but real deployments run many agents over shared infrastructure, and the most severe risks (model-weight exfiltration, training-run poisoning) plausibly need several agents acting in concert. We initiate the empirical study of multi-agent AI control, formalising distributed attacks in which several agents jointly aim for a malicious goal. We develop FakeLab: a synthetic AI-lab codebase (9 services, 86 benign tasks, 4 attack objectives). We evaluate single agent monitoring against distributed attacks, varying the number of agents, their coordination, model capabilities and precise monitoring configuration. Our central finding is the fragmentation effect: as more agents coordinate to attack, per-agent monitoring becomes less likely to catch any of the attackers. Secondly, this is not driven by the ratio of benign to malicious code -- we argue this is likely dependent on model capability. Third, an explicit planner amplifies the fragmentation effect, raises the rate of completing the attack up to sevenfold, and mildly sharpens executors' poor monitor-theory-of-mind. Finally: a weak "trusted" monitor misses most attacks, while a stronger one cuts undetected success by more than an order of magnitude but remains imperfect. We are happy to share FakeLab, our control setting, with safety researchers on request.

## Key Contributions

1. AI control is a family of techniques to prevent an AI with malicious goals from subverting its operator's intent.
2. AI Control usually studies a single agent in one trajectory, but real deployments run many agents over shared infrastructure, and the most severe risks (model-weight exfiltration, training-run poisoning) plausibly need several agents acting in concert.
3. We initiate the empirical study of multi-agent AI control, formalising distributed attacks in which several agents jointly aim for a malicious goal.
4. We develop FakeLab: a synthetic AI-lab codebase (9 services, 86 benign tasks, 4 attack objectives).

## Implementation Notes

- **Keywords**: multi-agent, control-systems
- **Categories**: cs.LG, cs.AI, cs.MA
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: multi-agent, control-systems.
