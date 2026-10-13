---
name: curriculum-grpo-difficulty
description: 'Benefits and limits of curriculum difficulty progression in GRPO training. Use when designing training curricula for GRPO-based LLM reasoning training.'
arxiv_id: '2610.13669'
utility: 0.85
authors: Ronghan Li, Fei Chen, Mingyu Lu
categories: [cs.AI]
tags: [curriculum-learning, grpo, difficulty-progression, llm-training, reasoning]
---

# Curriculum Difficulty Progression in GRPO: Benefits and Limits

## Key Innovation

Investigates whether persistently selecting medium-difficulty samples (which yield informative GRPO signals) leads to strongest final performance, or whether progressing to harder samples helps. Addresses that sample difficulty changes as policy evolves.

## Problem

- Medium-difficulty samples are attractive for online GRPO selection
- They yield informative group-relative learning signals
- But: does persistent medium selection lead to best final model?
- Sample difficulty changes as policy evolves → fixed estimates become misaligned

## Method

- Analyzes curriculum difficulty progression in GRPO
- Tests easy→medium→hard progression vs static difficulty
- Tracks how sample difficulty shifts during training
- Measures final performance across curriculum strategies

## Key Findings

- Persistent medium-difficulty selection is NOT always optimal
- Progression to harder samples can improve final performance
- Dynamic difficulty tracking needed as policy evolves
- Trade-off between training efficiency and final capability

## Practical Use

- Designing training curricula for reasoning models
- GRPO hyperparameter and data selection strategies
- Understanding when to increase training difficulty

## URL

https://arxiv.org/abs/2610.13669
