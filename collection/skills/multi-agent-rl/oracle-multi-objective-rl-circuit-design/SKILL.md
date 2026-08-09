---
name: oracle-multi-objective-rl-circuit-design
title: ORACLE Multi-Objective Reinforcement Learning Circuit Design
description: Multi-objective reinforcement learning framework for analog circuit design optimization using LLM-guided exploration and preference-aware conditioning.
trigger: When designing analog circuits with multiple competing objectives that require Pareto-optimal trade-offs without retraining models for each specification change.
---

# ORACLE: A Multi-Objective Reinforcement Learning-Based Analog Circuit Design Optimizer with Large Language Models-Guided Exploration

## Overview
ORACLE is an open-source reinforcement learning (RL)-based framework for multi-objective (MO) analog circuit design optimization that addresses key limitations in existing approaches:

1. **True Multi-Objective Optimization**: Instead of reducing multiple design specifications to a single scalar reward, ORACLE uses vector-valued learning with preference-aware conditioning
2. **Single Model, Multiple Trade-offs**: A single trained model can generate designs across diverse trade-off settings without retraining by using a preference vector to specify relative weights of objectives
3. **LLM-Guided Action Selection**: Incorporates large language model (LLM)-guided action selection to filter actions likely to lead to suboptimal designs or increased runtime

## Core Methodology

### Preference Vector Conditioning
- Replace scalar reward optimization with vector-valued learning
- Use preference vector to specify relative weights of multiple objectives
- Enable single trained model to handle diverse trade-off settings

### Preference-Guidance Strategies
1. **Normalized-Weight Guidance**: Normalize preference weights to improve convergence
2. **Cosine-Aligned Guidance**: Align action selection with preference direction using cosine similarity

### LLM-Guided Action Selection
- Filter actions that are likely to lead to suboptimal designs
- Reduce runtime by avoiding inefficient exploration paths
- Leverage LLM's understanding of circuit design principles

## Performance Results
- **Runtime Reduction**: 20.4x - 104.4x faster than state-of-the-art approaches
- **Specification Compliance**: Meets 99.9% of target specifications across 2,000 test cases
- **Figure of Merit**: Achieves 5.1x - 318.6x better figure of merit in resulting output specifications

## Implementation Steps

### 1. Problem Formulation
- Define multiple circuit design objectives (e.g., power consumption, gain, bandwidth, area)
- Establish constraint boundaries for each objective
- Determine feasible design space

### 2. Preference Vector Setup
- Create preference vector p = [p₁, p₂, ..., pₙ] where Σpᵢ = 1
- Each pᵢ represents relative importance of objective i
- Normalize weights if necessary

### 3. RL Environment Configuration
- State space: Circuit parameters and performance metrics
- Action space: Component value adjustments and topology modifications
- Reward function: Vector-valued reward R = [r₁, r₂, ..., rₙ]

### 4. LLM Integration
- Train or fine-tune LLM on circuit design knowledge base
- Implement action filtering mechanism using LLM predictions
- Set confidence thresholds for action acceptance/rejection

### 5. Training and Deployment
- Train single model with diverse preference vectors
- Validate across multiple circuit topologies
- Deploy for real-time design optimization

## Use Cases
- Analog amplifier design with gain-bandwidth-power trade-offs
- Filter design with frequency response and component count optimization
- Power management circuits with efficiency-size-cost considerations
- RF circuit design with noise-figure-linearity-power balancing

## Pitfalls and Considerations
- **Preference Vector Sensitivity**: Small changes in preference vectors can lead to significantly different designs
- **LLM Knowledge Gaps**: Ensure LLM is trained on relevant circuit design domains
- **Computational Overhead**: LLM inference adds computational cost that must be balanced against runtime savings
- **Convergence Issues**: May require careful tuning of preference-guidance strategies

## Verification Steps
1. Validate that single model produces different designs for different preference vectors
2. Measure runtime improvement compared to baseline approaches
3. Verify specification compliance across test cases
4. Evaluate figure of merit improvements
5. Test robustness to preference vector variations

## References
- arXiv:2608.04999 [eess.SY]
- DOI: https://doi.org/10.48550/arXiv.2608.04999

## Activation Keywords
analog circuit design, multi-objective optimization, reinforcement learning, LLM-guided design, preference conditioning, Pareto optimization, circuit automation