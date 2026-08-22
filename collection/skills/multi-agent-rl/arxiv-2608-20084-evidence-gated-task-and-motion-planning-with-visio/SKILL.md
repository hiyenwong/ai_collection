---
name: arxiv-2608-20084-evidence-gated-task-and-motion-planning-with-visio
description: 'Evidence-Gated Task and Motion Planning with Vision-Language Models (arXiv: 2608.20084)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# Evidence-Gated Task and Motion Planning with Vision-Language Models

**Authors:** Tsunehiko Tanaka, Matthew Stephenson, Alistair Macvicar, Edgar Simo-Serra
**arXiv:** 2608.20084
**Utility:** 1.00
**Published:** 2026-08-20T14:17:52Z
**Link:** http://arxiv.org/abs/2608.20084

## Abstract

Robots executing long-horizon manipulation tasks from natural-language instructions must reason about both semantic task structure and geometric feasibility. However, under partial observability, the availability of goal-relevant objects may be uncertain. In such cases, approaches that combine Vision-Language Models (VLMs) with Task and Motion Planning (TAMP) may generate subgoals that rely on the VLM's prior knowledge without observational support, leading to execution failures or unintended outcomes. We propose Evidence Acquisition and Feasibility Gating (EAFG), a framework that acquires visual evidence through VLM-generated exploratory subgoals and TAMP-based execution. EAFG then applies a feasibility gate to decide whether to proceed with task planning, acquire further evidence, or halt. Our experiments show that, in cooking tasks with ambiguous object use, EAFG improves recipe completion by discovering task-relevant objects before planning. For instructions requiring an absent object, EAFG promotes appropriate halt decisions and reduces repeated attempts to manipulate that object.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Evidence-Gated Task and Motion Planning with Vision-Language Models". 
The paper presents novel ideas in multi-agent-rl that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.20084
