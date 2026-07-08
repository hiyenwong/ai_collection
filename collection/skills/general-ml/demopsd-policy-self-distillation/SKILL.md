---
name: demopsd-policy-self-distillation
description: Disagreement-Modulated Policy Self-Distillation framework for LLM reasoning. Resolves privileged information leakage and exploration preservation in on-policy distillation via reverse-KL barycenter target, achieving leakage attenuation and exploration preservation simultaneously.
trigger: policy self-distillation, DemoPSD, privileged information leakage, reverse KL, knowledge distillation, LLM reasoning training
category: ai_collection/collection/skills
---

# DemoPSD: Disagreement-Modulated Policy Self-Distillation

## Overview
DemoPSD is a novel on-policy self-distillation framework that resolves two fundamental problems in LLM reasoning distillation:
1. **Privileged information leakage**: Student encodes answer-dependent shortcuts unavailable at test time
2. **Exploration suppression**: Teacher's dense token-level supervision overfits to in-domain patterns

## Core Innovation
Instead of fitting the full teacher distribution, DemoPSD steers the student toward a **reverse-KL barycenter target** — a weighted geometric combination of teacher and student distributions.

## Key Mechanisms
1. **Disagreement Measurement**: Measure difference between teacher and student distributions at each token position
2. **Adaptive Blending**: Use discrepancy to adaptively control teacher-student blending per token
3. **Selective Adoption**: Student selectively adopts teacher guidance rather than full imitation

## Theoretical Guarantees
1. **Leakage Attenuation**: Effective mitigation of privileged information leakage
2. **Exploration Preservation**: Preserved exploration capacity under dense token-level distillation

## Results
- Outperforms GRPO and SDPO on SciKnowEval across four scientific fields
- Maintains higher training entropy
- Robustly generalizes to out-of-distribution GPQA benchmarks

## Implementation
```python
# Pseudo-implementation
teacher_dist = model(prompt, privileged=True)
student_dist = model(prompt, privileged=False)
disagreement = kl_divergence(teacher_dist, student_dist)
barycenter = geometric_mean(teacher_dist, student_dist, weight=disagreement)
loss = reverse_kl(student_dist, barycenter)
```

## Activation Keywords
policy self-distillation, DemoPSD, privileged information leakage, reverse KL, knowledge distillation, exploration preservation

## Source
arXiv: 2607.02497 (2026-07-02)
