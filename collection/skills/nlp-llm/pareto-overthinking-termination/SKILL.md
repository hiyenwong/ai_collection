---
name: pareto-overthinking-termination
description: 'Pareto frontiers for optimal reasoning termination to combat overthinking in reasoning models. Use when determining when to stop LLM reasoning to avoid diminishing returns.'
arxiv_id: '2610.13570'
utility: 0.85
authors: Weixin Guan, Liang Li, Shiyu Xie, Jiapeng Liu, Bing Li
categories: [cs.AI]
tags: [overthinking, reasoning-termination, test-time-scaling, pareto-frontier, llm-reasoning]
---

# Pareto Frontiers of Optimal Reasoning Termination

## Key Innovation

Reasoning models benefit from test-time scaling but continued reasoning can become harmful ("overthinking"). Introduces Step-wise Truncation Probing (STP) to characterize overthinking at model-task level and construct Pareto frontiers of optimal termination strategies.

## Problem

- Accuracy vs token usage tradeoff lacks theoretical grounding
- No reference for overthinking severity
- No characterization of strategies' theoretical mitigation potential

## Method

- Step-wise Truncation Probing (STP): generate answers from multiple retained prefixes
- Characterize overthinking at model-task level
- Construct Pareto frontiers of accuracy vs computation
- Identify optimal termination points

## Results

- Quantifies overthinking severity per model-task pair
- Provides theoretical bounds on termination strategies
- Identifies optimal stopping points for reasoning

## Practical Use

- Optimizing inference cost for reasoning models
- Building early-stopping mechanisms for chain-of-thought
- Understanding when more thinking hurts performance

## URL

https://arxiv.org/abs/2610.13570
