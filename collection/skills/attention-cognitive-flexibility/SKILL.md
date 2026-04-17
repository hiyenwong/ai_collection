---
name: attention-cognitive-flexibility
description: "Gating-based and concatenation-based attention models for multi-task learning, leveraging graph-theory analysis of environmental task structure to enhance cognitive flexibility, stability, and generalization"
version: "0.1.0"
arxiv: "2604.13281v1"
paper_title: "Attention to task structure for cognitive flexibility"
tags:
  - cognitive-flexibility
  - attention-mechanisms
  - multi-task-learning
  - graph-theory
  - generalization
  - stability
  - task-switching
---

# Attention-Based Cognitive Flexibility

## Overview

This work investigates how the **structure of the environment itself** influences cognitive flexibility — the ability to retain prior knowledge (cognitive stability) while transferring it to novel tasks (cognitive generalization). It introduces gating-based and concatenation-based attention models that decompose tasks into components and sequentially allocate attention.

## Key Principles

### Multi-Task Environment Design

- Tasks are defined by a combination of **two cue dimensions**
- Environments are characterized using **graph-theory methods**
- Task connectivity in the environment graph strongly modulates both stability and generalization

### Attention Models

1. **Gating-based (Multiplicative) Attention**: Decomposes tasks via multiplicative gating over components
2. **Concatenation-based Attention**: Decomposes tasks via concatenation of component representations
3. Both models can **sequentially allocate attention** to task components

### Core Findings

- **Richer environments** improve both generalization and stability
- **Graph-theoretic connectivity** between tasks strongly modulates performance, with especially pronounced benefits for attention-based models
- Attention-based models outperform multilayer perceptrons in environments with structured task connectivity
- Environmental structure and model architecture interact to shape multi-task learning outcomes

## Implementation Guidance

1. Model the multi-task environment as a graph where nodes are tasks and edges represent shared cue dimensions
2. Implement gating-based attention: `output = gate(component_1) * gate(component_2) * ...`
3. Implement concatenation-based attention: `output = concat(attend(component_1), attend(component_2), ...)`
4. Systematically vary environmental richness and task connectivity
5. Evaluate generalization (performance on unseen tasks) and stability (retention on learned tasks)
6. Compare attention-based models against standard MLP baselines

## References

See `references/implementation.md` for code patterns and implementation details.
