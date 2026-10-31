---
name: scarl-sequence-confidence-aligned-reinforcement-learning
description: "SCARL: Sequence Confidence-Aligned Reinforcement L..."
tags: [cs.LG, cs.AI]
source: arxiv
arxiv_id: 2610.40407v1
utility: 0.87
published: 2026-10-29
---

# SCARL: Sequence Confidence-Aligned Reinforcement Learning

**Authors:** Zhenghong Ke, Jingbo Zhou, Hua Wu
**Published:** 2026-10-29
**arXiv:** [2610.40407v1](https://arxiv.org/abs/2610.40407v1)
**Categories:** cs.LG, cs.AI
**Utility Score:** 0.87

## Abstract

Reinforcement learning with verifiable rewards (RLVR) improves language-model reasoning by scoring sampled responses with a rule-based verifier and reinforcing those that pass. Where a classifier's training couples predicted probability to labels, nothing ties an RLVR policy's confidence in a response to its reward: aligned training would drive responses with the same advantage toward equal confidence, yet the advantage is blind to confidence. Under this sequence-confidence misalignment, a success the policy barely found earns the same update as one it produces with near certainty, and a confident error is corrected no harder than an exploratory one. We propose SCARL (Sequence Confidence-Aligned Reinforcement Learning), which reshapes, but never re-signs, each advantage with the alignment gap between the response's group-relative confidence and the outcome its advantage certifies, normalized into shares of each class's advantage budget. Misaligned samples absorb the force, responses with the same advantage are driven toward equal confidence, and repairing the misalignment doubles as a remedy for the entropy collapse that erodes exploration. SCARL provably reduces to its base estimator when a class's confidences agree, adds no extra passes and one hyperparameter. On Qwen3-4B-Base it lifts average Pass@32 by 2.4 points over DAPO and is best among nine compute-matched methods on both coverage and per-draw accuracy; applied unchanged across four estimators and four backbones, it 

## Key Contributions

- Novel research in cs.LG, cs.AI
- Published 2026-10-29

## Activation

scarl, sequence, confidencealigned, reinforcement, learning
