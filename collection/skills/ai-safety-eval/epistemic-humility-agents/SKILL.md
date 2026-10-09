---
name: epistemic-humility-agents
description: 'Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents under Knowledge Conflict. Framework for measuring agent willingness to acknowledge uncertainty.'
metadata:
  arxiv_id: "2610.12360"
  utility: 0.87
  authors: ["Kaiser Sun", "Bernal Jimenez Gutierrez", "Hongjun Liu", "Jingyu Zhang", "Jie Gao"]
  published: "2026-10-08"
  categories: ["cs.AI", "cs.CL"]
  tags: ["epistemic-humility", "knowledge-conflict", "evaluation", "uncertainty", "agent-evaluation"]
---

# Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents

**arXiv:** [2610.12360](https://arxiv.org/abs/2610.12360)
**Utility:** 0.87

## Key Question

When retrieved evidence contradicts an agent's prior beliefs, does it:
1. Revise its answer?
2. Acknowledge uncertainty?
3. Persist with an incorrect conclusion?

## Core Contribution

Framework for evaluating **epistemic humility (EH)**: the agent's willingness to recognize, act on, and communicate the limits of its knowledge.

## Problem

Existing evaluations focus primarily on task success, offering limited insight into how agents handle knowledge conflicts.

## Findings

Agents can be accurate but lack humility — they persist with incorrect conclusions when evidence contradicts their priors rather than acknowledging uncertainty.

## Practical Use

- Evaluate agent behavior under knowledge conflict
- Design agents that appropriately express uncertainty
- Build more trustworthy agent systems that know their limits
