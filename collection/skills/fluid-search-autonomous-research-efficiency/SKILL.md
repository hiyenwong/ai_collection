---
name: fluid-search-autonomous-research-efficiency
version: 1.0.0
description: Fluid search methodology for adaptive search efficiency in autonomous research systems. Uses portfolio bandit to dynamically allocate evaluation budget across search processes, optimizing area under Pareto frontier curve.
trigger_words:
  - fluid search
  - autonomous research efficiency
  - search efficiency AUC
  - portfolio bandit search
---

# Fluid Search: Adaptive Search Efficiency for Autonomous Research

## Overview
AI-driven autonomous research (AR) systems are evaluated primarily by final outcome quality, but search efficiency—the ability to reach high-quality results with minimal evaluation budget—is equally important. Fluid search addresses this by dynamically allocating a fixed evaluation budget across multiple search processes using a portfolio bandit approach.

## Core Principles

### 1. Search Efficiency as Performance Dimension
- Evaluate AR systems using Area Under Curve (AUC) of Pareto frontier
- Measure both final outcome quality AND convergence speed
- Recognize that best final result ≠ most efficient search process

### 2. Portfolio Bandit Allocation
- Maintain forest of diverse search processes (hill climbing, beam search, tree search, evolutionary)
- Use multi-armed bandit to allocate budget based on recent performance
- Dynamically shift resources to more promising search structures

### 3. Adaptive Budget Management
- Fixed total evaluation budget constraint
- Real-time performance monitoring and allocation adjustment  
- Per-task oracle matching performance without prior knowledge

## Implementation Steps

### Step 1: Search Process Forest Setup
- Initialize multiple search algorithm families:
  - Hill climbing variants
  - Beam search with different widths
  - Tree search with various expansion policies
  - Evolutionary search with diverse mutation operators
- Ensure each process can report intermediate quality metrics

### Step 2: Portfolio Bandit Configuration
- Implement Upper Confidence Bound (UCB) or Thompson Sampling
- Track reward as recent quality improvement per evaluation
- Include exploration bonus for under-explored search processes

### Step 3: Dynamic Allocation Loop
```
while budget_remaining > 0:
    selected_process = bandit.select()
    result = selected_process.evaluate_next()
    reward = compute_improvement(result)
    bandit.update(selected_process, reward)
    budget_remaining -= 1
```

### Step 4: Performance Evaluation
- Record Pareto frontier at each evaluation step
- Compute AUC metric for search efficiency comparison
- Compare against per-task oracle baseline

## Benefits
- Highest overall search efficiency across diverse tasks
- Closely matches per-task oracle performance
- Adapts to unknown optimal search structure
- Handles real-world costly evaluation scenarios

## Use Cases
- Autonomous research with expensive verification
- Scientific discovery with physical experiments
- Systems optimization with limited evaluation budget
- Multi-algorithm ensemble optimization

## References
- arXiv:2607.24647 [cs.AI]
- Authors: Haiqian Yang, Yuan Cao