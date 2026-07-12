---
name: harness-vla-steering-frozen-vlas-memory-guided-agents
description: "Memory-augmented agentic framework that exposes a frozen VLA as a retryable contact-rich primitive composed with analytic primitives. Learns operating range from execution traces and failure models. +38.6pp on LIBERO-Pro, +25.4pp on RoboCasa365. Activation: vision-language-action, memory-guided agents, manipulation primitives, frozen VLA, robot manipulation."
metadata:
  arxiv_id: "2607.08448"
  published: "2026-07-09"
  authors: "Yixian Zhang, Huanming Zhang, Feng Gao, Xiao Li, Zhihao Liu"
  tags: [vision-language-action, memory-guided-agents, manipulation-primitives, frozen-vla, robot-manipulation]
---

# Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents

## Overview

Harness VLA is a memory-augmented agentic framework that exposes a frozen Vision-Language-Action (VLA) model as a retryable contact-rich primitive, composed with a small fixed library of analytic primitives for grounding, staging, transport, navigation, and release. Rather than expanding the skill library, the harness learns the operating range of fixed primitives from execution traces and failure models.

## Key Innovations

### Frozen VLA as Retryable Primitive
- Exposes frozen VLA as a contact-rich primitive that can be retried on failure
- Avoids finetuning the VLA, preserving its original capabilities
- Composes with analytic primitives for non-contact phases

### Memory-Guided Operating Range Learning
- Learns from task-specific execution traces
- Uses global success rules and failure models
- Determines when to use VLA vs. analytic primitives
- Lifts semantic re-grounding, non-contact execution, and VLA re-staging to planner

### Compositional Architecture
- Frozen VLA for local contact-rich phases
- Analytic primitives for grounding, staging, transport, navigation, release
- Planner orchestrates primitive selection and execution

## Methodology

1. **Primitive Library**: Fixed set of VLA + analytic primitives
2. **Execution Traces**: Collect task-specific execution data
3. **Operating Range Learning**: Learn when each primitive succeeds/fails
4. **Planner Integration**: Planner uses learned models for primitive selection
5. **Evaluation**: Test on perturbed tabletop, household kitchen, bimanual manipulation

## Implications

- Frozen VLAs can be extended beyond their original trajectory distribution without finetuning
- Compositional approach leverages strengths of both learned and analytic methods
- Memory-guided operating range learning is a general principle for primitive orchestration
- Significant improvements demonstrate practical viability

## Pitfalls

- Requires task-specific execution traces for operating range learning
- Fixed primitive library may not cover all task types
- Planner quality affects overall system performance
- Retry mechanism may increase execution time

## Activation Keywords

vision-language-action, Harness VLA, memory-guided agents, manipulation primitives, frozen VLA, robot manipulation, operating range learning, compositional architecture, LIBERO-Pro, RoboCasa365

## Paper Reference

arXiv:2607.08448 - "Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents" (Jul 2026)
