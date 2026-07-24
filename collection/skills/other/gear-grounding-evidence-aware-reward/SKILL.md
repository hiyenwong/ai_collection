---
name: gear-grounding-evidence-aware-reward
version: 1.0.0
description: Grounding Evidence-Aware Reward for Long-Context Reasoning to Reduce Repetitive Copying
trigger_words:
  - gear
  - grounding evidence-aware reward
  - long-context reasoning
  - repetitive copying
arxiv_id: 2607.19345
---

# GEAR: Grounding Evidence-Aware Reward

## Overview
GEAR (Grounding Evidence-Aware Reward) is a reward shaping method that addresses repetitive copying in long-context reasoning by encouraging models to focus on task-relevant evidence while avoiding irrelevant distractors.

## Key Components

### 1. Evidence-Distractor Separation
- Separates prompts into task-relevant key evidence and irrelevant distractor context
- Identifies that insufficient grounding is the root cause of repetitive copying
- Shows that models failing to focus on key evidence are more likely to answer incorrectly

### 2. Reward Shaping
- **Grounding Reward**: Augments accuracy signal with reward for overlap with key evidence
- **Distractor Penalty**: Applies penalty for overlap with irrelevant context
- Combined reward guides models toward productive reasoning rather than copying

### 3. Automated Evidence Annotation Pipeline
- Constructs evidence-annotated training data from arbitrary documents
- Enables GEAR application on natural-language datasets without manual annotation

## Implementation Steps

1. **Data Preparation**: Use automated pipeline to annotate evidence in your training data
2. **Reward Function Design**: Implement combined reward with grounding and distractor components
3. **RL Training**: Train your long-context LLM using GEAR instead of standard accuracy-only rewards
4. **Evaluation**: Measure both task performance and copying behavior reduction

## Benefits
- Up to +4.6 average points improvement over standard RL
- Larger gains at longer contexts
- Reduces repetitive copying behavior
- Decreases thinking length (more efficient reasoning)
- Improves grounding in relevant evidence

## Use Cases
- Long-context question answering
- Document-based reasoning tasks
- Legal or medical document analysis
- Any scenario requiring complex reasoning over long inputs

## References
- Paper: [Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning](https://arxiv.org/abs/2607.19345)
- Related work: reinforcement learning, long-context LLMs, reward shaping, evidence grounding