---
name: topology-diagnosis-mas
description: 'Know the Shape, Find the Fault: Topology-Conditioned Diagnosis of Multi-Agent LLM Failures. Using communication topology structure to distinguish coordination failure modes.'
metadata:
  arxiv_id: "2610.10126"
  utility: 0.87
  authors: ["Xinwen Liu", "Zhuocheng Pan", "Isabella Zhu", "Jawei Zhang", "Xudong Liu"]
  published: "2026-10-07"
  categories: ["cs.MA", "cs.AI"]
  tags: ["failure-diagnosis", "communication-topology", "coordination-failure", "multi-agent", "debugging"]
---

# Know the Shape, Find the Fault: Topology-Conditioned Diagnosis of Multi-Agent LLM Failures

**arXiv:** [2610.10126](https://arxiv.org/abs/2610.10126)
**Utility:** 0.87

## Key Innovation

Using **communication topology** as structural cues for distinguishing coordination failure modes in multi-agent LLM systems.

## Problem

When multi-agent coordination breaks down, similar symptoms in execution traces can reflect different problems in how information is passed, used, or verified. Without structural context, diagnosis is ambiguous.

## Method

- Capture communication topology (how agents exchange information)
- Use topology structure to condition failure diagnosis
- Distinguish between different coordination failure modes based on structural patterns

## Practical Use

- Debug multi-agent LLM systems more effectively
- Identify root causes of coordination failures
- Design more robust multi-agent communication architectures
