---
name: scalelogic-rl-reasoning
description: Methodology for studying RL scaling laws in LLM reasoning using a synthetic logical reasoning framework (ScaleLogic) with independent control over proof depth and logical expressiveness.
category: deep-learning
tags: [LLM, RL, reasoning, scaling-laws, curriculum-learning, synthetic-data]
trigger: scalelogic, rl reasoning, reasoning depth, logical expressiveness, scaling law, curriculum training
---

# ScaleLogic: RL Reasoning Scaling Methodology

## Overview
ScaleLogic is a synthetic logical reasoning framework for systematically studying how RL training compute scales with task difficulty in LLMs. It provides independent control over reasoning depth (proof horizon) and logical expressiveness.

## Core Technique
1. **Two-Axis Difficulty Control**: Independently vary proof depth D (horizon) and logical expressiveness (implication → conjunction → disjunction → negation → quantification)
2. **Power Law Discovery**: Training compute T follows T ∝ D^γ with R² > 0.99, where γ increases monotonically with expressiveness (1.04 → 2.60)
3. **Expressiveness Transfer**: More expressive training yields larger downstream gains (+10.66 points) and more compute-efficient transfer
4. **Curriculum Training**: Progressively increasing difficulty substantially improves scaling efficiency

## Key Findings
- **What you train on matters more than how much**: logical expressiveness shapes the scaling exponent
- Power law holds across multiple RL methods (PPO, GRPO, etc.)
- Curriculum learning reduces total compute needed for same performance

## Implementation Steps
1. Define logical reasoning tasks with parametric depth D and expressiveness level E
2. Train LLM with RL (PPO/GRPO) across grid of (D, E) configurations
3. Fit power law T = a·D^γ for each expressiveness level
4. Evaluate transfer to downstream math/reasoning benchmarks
5. Apply curriculum: train on easier tasks first, progressively increase D and E

## Pitfalls
- Synthetic tasks may not perfectly capture real-world reasoning complexity
- Expressiveness axis is discrete — interpolation between levels requires careful task design
- Curriculum scheduling hyperparameters (when to increase difficulty) are task-dependent

## Activation Keywords
scalelogic, rl reasoning, reasoning depth, logical expressiveness, scaling law, curriculum training, synthetic reasoning, proof planning
