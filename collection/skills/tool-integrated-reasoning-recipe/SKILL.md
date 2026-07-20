---
name: tool-integrated-reasoning-recipe
description: Full-pipeline recipe for injecting tool-use into thinking models without sacrificing text-only reasoning. Two-stage SFT+RL approach. Based on arXiv 2605.06326.
category: llm-reasoning
---

# Tool-Integrated Reasoning (TIR) Recipe

## Overview
A comprehensive recipe for injecting natural tool-use behavior into strong thinking models without sacrificing text-only reasoning. Achieved 96.7% and 99.2% on AIME 2025 for Qwen3 4B/30B.

## Core Pipeline

### Stage 1: TIR SFT
1. **Learnable teacher trajectories**: Prioritize problems naturally suited for tool-augmented solutions
2. **Control tool-use proportion**: Balance tool-use vs text-only to mitigate catastrophic forgetting
3. **Optimize for pass@k and response length**: Not training loss — preserves RL headroom

### Stage 2: RL with Verifiable Rewards (RLVR)
1. **Suitable SFT initialization**: Start from well-tuned SFT
2. **Explicit mode collapse safeguards**: Prevent over-reliance on tools
3. **Simple RLVR setup**: Effective when built on good SFT foundation

## Key Findings
- Tool-enabled evaluation can degrade reasoning even with minimal tool calls
- TIR SFT effectiveness hinges on teacher trajectory learnability
- Tool-use proportion must be controlled to avoid forgetting
- Pass@k and response length optimization > training loss optimization

## Implementation Steps
1. Curate problems suited for tool augmentation
2. Generate teacher trajectories with natural tool-use
3. Mix tool-use and text-only trajectories (tune ratio)
4. SFT optimizing for pass@k and response length
5. RLVR with mode collapse safeguards
6. Evaluate on both tool-required and text-only benchmarks

## Applicable Use Cases
- Adding tool use to reasoning models
- Preventing catastrophic forgetting
- Multi-stage training pipelines
- Achieving state-of-the-art math reasoning

## Triggers / Keywords
tool-integrated reasoning, TIR, SFT+RL pipeline, thinking models, AIME, mode collapse, teacher trajectories
