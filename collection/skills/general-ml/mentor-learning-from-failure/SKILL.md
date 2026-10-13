---
name: mentor-learning-from-failure
description: 'MENTOR: On-policy pedagogical intervention to prevent zero-reward collapse in RLVR training. Use when RLVR training fails due to sudden task difficulty increases.'
arxiv_id: '2610.13594'
utility: 0.88
authors: Guanlan Yue, Hang Yu, Xiaoyong Huang, Ruipeng Li, Wei Zhang
categories: [cs.AI]
tags: [rlvr, zero-reward-collapse, pedagogical-intervention, training-stability, llm-reasoning]
---

# MENTOR: Learning from Failure with On-Policy Pedagogical Intervention

## Key Innovation

Addresses "zero-reward collapse" in RLVR — training failure where sudden task difficulty increase causes learning signal to vanish. Instead of discarding failed trajectories, leverages them as diagnostic information about cognitive gaps.

## Problem

- RLVR is key driver for Large Reasoning Models
- Vulnerable to zero-reward collapse from difficulty spikes
- Conventional approach: discard failed trajectories (wasteful)
- Failed trajectories contain valuable diagnostic information

## Method

- On-policy pedagogical intervention during training
- Extracts diagnostic signal from failed trajectories
- Identifies model's cognitive gaps from failure patterns
- Provides targeted intervention to recover training

## Results

- Prevents zero-reward collapse
- Better final performance vs discarding failures
- More stable training dynamics

## Practical Use

- Stabilizing RLVR training for reasoning models
- Building more robust agent training pipelines
- Leveraging failure data for training improvement

## URL

https://arxiv.org/abs/2610.13594
