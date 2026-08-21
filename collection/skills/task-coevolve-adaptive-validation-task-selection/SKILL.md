---
name: task-coevolve-adaptive-validation-task-selection
description: "Adaptive validation for LLM harness optimization."
metadata:
  arxiv_id: "2608.20169"
  published: "2026-08-22"
  authors: "Agent4Science-UTokyo"
  tags: [llm, harness, optimization, validation, adaptive, task-selection]
license: Complete terms in LICENSE.txt
---

# Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection

## Overview
Task-CoEvolve is a novel approach to efficient LLM agent harness optimization through adaptive validation task selection. It co-evolves the validation tasks with the harness by addressing two key challenges: selecting informative tasks and estimating full-set performance from partial evaluations.

## Core Principles

### Informative Task Selection
Task-CoEvolve builds on the observation that tasks on which candidate harnesses disagree are more informative for distinguishing among them than tasks that are consistently solved or failed. It uses variance-weighted sampling based on past outcomes to focus evaluation on tasks near the agent's capability frontier.

### Adaptive Sampling Distribution
The sampling distribution adapts as the harness evolves, ensuring that the most discriminative tasks are evaluated at each iteration rather than wasting resources on tasks that have become less informative.

### Performance Estimation
Task-CoEvolve estimates full-set scores from the sampled tasks by accounting for their sampling probabilities, enabling consistent comparisons across iterations despite evaluating different subsets.

## Implementation Workflow

### 1. Initialize Task Pool
- Start with a comprehensive validation task set
- Track historical performance for each task across harness iterations

### 2. Variance-Weighted Sampling
- Calculate variance of performance across candidate harnesses for each task
- Sample tasks with probability proportional to their variance
- Focus on tasks near the capability frontier (neither consistently solved nor failed)

### 3. Evaluate Sampled Tasks
- Run the current harness candidates on the sampled task subset
- Record detailed performance metrics per task

### 4. Estimate Full-Set Performance
- Weight each sampled task's score by the inverse of its sampling probability
- Compute unbiased estimate of full validation set performance
- Enable fair comparison between harness candidates

### 5. Update Harness and Repeat
- Select best-performing harness based on estimated full-set scores
- Update historical performance data
- Adapt sampling distribution for next iteration

## Benefits
- Reduces evaluation costs by 80% compared to full-set evaluation
- Maintains final performance equivalent to full-set search
- Dynamically adapts to the evolving capabilities of the harness
- Provides consistent performance estimation across iterations

## Use Cases
- LLM agent harness optimization
- Automated prompt engineering
- Tool-augmented agent development
- Multi-agent system coordination optimization

## Activation Keywords
- task-coevolve
- adaptive validation
- harness optimization
- variance-weighted sampling
- capability frontier
- partial evaluation

## References
- Original paper: https://arxiv.org/abs/2608.20169
- Code repository: https://github.com/Agent4Science-UTokyo/Task-CoEvolve