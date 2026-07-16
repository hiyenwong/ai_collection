---
name: memops-benchmarking-lifecycle-memory-operations-in
description: "MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations - Long-term memory has become a foundational capability for LLM-based agents that accompany users across extended, multi-session interactions. Existing ..."
version: 1.0.0
author: Xixuan Hao, Zeyu Zhang, Zehao Lin et al.
arxiv_id: 2607.12893
created: 2026-07-14
category: nlp-llm
tags: [cs.AI, cs.CL]
activation_keywords: [memops, benchmarking, lifecycle, memory, operations, long, horizon, conversations, term, become]
---

# MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations

## Overview

Long-term memory has become a foundational capability for LLM-based agents that accompany users across extended, multi-session interactions. Existing benchmarks, however, evaluate such memory almost exclusively through downstream question answering, scoring only the correctness of a final answer. This black-box formulation conflates the heterogeneous causes of memory failure, such as missing the introduction of a relevant fact, binding an operation to the wrong target, or relying on stale values after a correction. As a result, it can credit correct answers despite their reliance on inconsistent or unsafe memory states. In this paper, we argue that, in dynamic long-horizon interactions, memory is not a static collection of facts but a lifecycle of explicit operations, including remembering, forgetting, updating, reflecting, and their compositions. We introduce MemOps, a benchmark that reformulates conversational memory as a sequence of lifecycle operations and represents each memory event with a structured trace specifying its trigger, target, scope, state transition, and supporting evidence. A controllable generation pipeline embeds these operations into long, task-oriented conversations and produces gold operation traces together with six categories of operation-level probes, evaluated under both adjacent-evidence and long-context settings. Across long-context, retrieval-based, parametric and managed-memory systems, MemOps disentangles failure modes that final-answer accuracy alone conceals, revealing that current systems remain far from uniformly reliable. For instance, session-level retrieval outperforms turn-level retrieval, and long-context models remain notably weak at reconstructing ordered memory-state trajectories. These results move long-term memory evaluation from final-answer scoring toward interpretable, operation-level diagnosis.

## Key Insights

- TODO: Extract key insights from the paper

## Implementation Approach

- TODO: Describe how to implement the techniques from this paper

## Applications

- TODO: List potential applications

## Activation Keywords

memops, benchmarking, lifecycle, memory, operations, long, horizon, conversations, term, become

---
