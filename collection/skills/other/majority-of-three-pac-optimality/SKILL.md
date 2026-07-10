---
name: majority-of-three-pac-optimality
description: "Statistical learning theory methodology proving majority-of-three voting is optimal in the realizable PAC setting"
category: statistics
tags: ["statistical-learning", "PAC-learning", "ensemble-methods", "majority-voting", "optimal-learner", "classifier-combination"]
---

# Majority-of-Three PAC Optimality

## Description
Methodology from statistical learning theory proving that the majority vote of three independent consistent classifiers achieves optimal sample complexity in the realizable PAC (Probably Approximately Correct) setting. Provides simplified algorithmic structure and probabilistic analysis compared to previous voting learners.

## Activation Keywords
- majority of three
- PAC learning optimality
- ensemble voting
- consistent classifiers
- realizable PAC
- sample complexity
- statistical learning theory
- 三分类器投票
- PAC学习最优性

## Core Concepts

### Realizable PAC Setting
- There exists a target concept c* in hypothesis class H
- Training examples are labeled by c* (realizable)
- Goal: find hypothesis h with error ≤ ε with probability ≥ 1-δ
- Optimal sample complexity: Θ((d/ε)·log(1/δ) + d/ε) where d = VC dimension

### Majority-of-Three Algorithm
1. Split training data into 3 independent subsets
2. Find consistent classifier on each subset
3. Output majority vote of the 3 classifiers
4. Achieves optimal sample complexity with minimal voting structure

### Key Innovation
- Previous optimal learners required complex voting schemes
- Majority-of-three is the simplest possible voting scheme
- Proof simplifies both algorithmic structure and probabilistic analysis
- Tight analysis of error probability for 3-classifier voting

## Usage Patterns

### Pattern 1: Ensemble Classifier Design
1. Given hypothesis class H with VC dimension d
2. Split dataset into 3 independent parts
3. Find consistent hypotheses h₁, h₂, h₃ on each part
4. Return sign(h₁ + h₂ + h₃) as final prediction

### Pattern 2: Sample Complexity Analysis
1. Determine target error ε and confidence δ
2. Calculate required sample size: O((d/ε)·log(1/δ) + d/ε)
3. Verify majority-of-three achieves this bound
4. Compare with single classifier: O(d/ε + (1/ε)·log(1/δ))

## Mathematical Framework

### Error Bound
For majority-of-three with consistent classifiers:
- P[error > ε] ≤ δ when n ≥ C·((d/ε)·log(1/δ) + d/ε)
- Matches optimal sample complexity up to constant factors

### Probabilistic Analysis
- Key insight: independence of 3 classifiers reduces error probability
- Union bound over 3 hypotheses is tight
- Simpler than previous multi-hypothesis voting analyses

## Applications
- Ensemble learning theory
- PAC learning algorithm design
- Statistical learning complexity analysis
- Classifier combination methods

## Error Handling
### Non-Realizable Setting
- Theory applies only to realizable case (target in hypothesis class)
- Agnostic case requires different analysis

### Independence Requirement
- Three classifiers must be trained on independent data
- Correlated classifiers may not achieve optimality

## References
- arXiv:2606.13614 — Majority-of-Three is Optimal
- Valiant — Original PAC learning framework
- Hanneke — Previous optimal PAC learners
- ensemble learning and voting literature