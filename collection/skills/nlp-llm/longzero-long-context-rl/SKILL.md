---
name: longzero-long-context-rl
description: "LongZero: Enhancing long-context reasoning in LLMs from zero data. RL-based method that synthesizes long, diverse, challenging, verifiable training data without external corpora."
paper_id: 2610.30132
utility_score: 0.82
categories: [cs.CL, cs.LG]
date: 2026-10-21
tags: [long-context, reinforcement-learning, data-synthesis, llm-reasoning, zero-data]
---

# LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data

## Key Contribution
Proposes LongZero, an RL-based method to enhance long-context reasoning in LLMs without requiring external training data. Addresses the data bottleneck: RL needs long, diverse, challenging, verifiable data, but human annotation is expensive, natural data is scarce, and synthesis methods depend on external corpora or stronger teacher models.

## Core Method
- **Problem**: RL for long-context reasoning requires training data that is (1) long, (2) diverse, (3) challenging, (4) verifiable — but all existing data sources have limitations
- **Solution**: Zero-data synthesis pipeline that generates training instances from scratch
- **Approach**: 
  - Generate long contexts procedurally (no external corpus needed)
  - Create verifiable questions/tasks over these contexts
  - Use RL (GRPO/PPO) to train the model on these synthetic instances
  - Curriculum: start simple, increase length and complexity
- **Key insight**: Synthetic data can be more diverse and challenging than natural data when designed with RL training dynamics in mind

## Why It Matters
- Eliminates dependency on external corpora or stronger teacher models for long-context training
- Scalable: can generate unlimited training data
- Verifiable by construction (synthetic tasks have known answers)
- Outperforms methods that rely on natural data or distillation from stronger models
- Practical for teams without access to large annotated long-context datasets

## Application Scenarios
- Training LLMs for long-document QA, summarization, code understanding
- Enhancing reasoning capabilities in open-source LLMs
- Scenarios where external data is proprietary or unavailable
- Building long-context capabilities from scratch in new model families

## Implementation Notes
- Synthesis pipeline: procedural context generation → question generation → verification
- RL algorithm: GRPO recommended (more stable than PPO for long sequences)
- Curriculum design: length and complexity should increase together
- Verification: synthetic tasks must have deterministic correctness checks
- Cost: synthesis is cheap (no human annotation), RL training is the main cost
