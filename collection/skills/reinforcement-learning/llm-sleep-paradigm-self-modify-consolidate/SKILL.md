---
name: llm-sleep-paradigm-self-modify-consolidate
description: "Sleep-Dreaming paradigm for LLM continual learning via Knowledge Seeding (on-policy distillation + RL imitation learning) and RL-generated synthetic curriculum for self-improvement."
---

# Language Models Need Sleep: Self-Modification and Memory Consolidation

## Core Concept
Inspired by human learning, introduce **Sleep paradigm** enabling LLMs to:
1. Continually learn and transfer in-context knowledge to long-term parameters
2. Distill short-term fragile memories into stable knowledge
3. Recursively improve with self-generated training data

## Two-Stage Process

### Stage 1: Memory Consolidation (Knowledge Seeding)
- **Upward distillation**: Smaller-self memories → larger network
- **Generalized Distillation**: On-policy distillation + RL-based imitation learning
- Preserves knowledge while expanding capacity

### Stage 2: Dreaming (Self-Improvement)
- RL generates curriculum of **synthetic data**
- Rehearse new knowledge
- Refine existing capabilities
- No human supervision required

## Implementation
1. Knowledge Seeding process: on-policy distillation + RL imitation learning
2. Dreaming phase: RL-curriculum generation
3. Recursive self-improvement loop

## Applications
- Long-horizon tasks
- Continual learning
- Knowledge incorporation
- Few-shot generalization

## Source
- arXiv: 2606.03979
- Title: Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories
- Authors: Ali Behrouz, Farnoosh Hashemi, Vahab Mirrokni

## Activation Keywords
sleep paradigm, knowledge seeding, dreaming phase, continual learning, self-modification, memory consolidation, synthetic curriculum