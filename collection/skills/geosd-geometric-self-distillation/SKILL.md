---
name: geosd-geometric-self-distillation
description: Geometric Self-Distillation (GeoSD) methodology for preserving OOD generalization during privileged-context self-distillation. Uses Hellinger loss and Fisher-Rao proximal term to prevent drift in predictive behavior.
date: 2026-07-10
arxiv: 2607.06855v1
authors: Josip Jukić, Ivan Titov
tags: [distillation, self-distillation, ood-generalization, geometric-optimization, reasoning]
activation: geosd, geometric-distillation, hellinger-loss, fisher-rao, ood-preservation
---

# Geometric Self-Distillation (GeoSD)

## Core Innovation

GeoSD prevents out-of-distribution (OOD) degradation during privileged-context self-distillation by treating drift as movement in predictive behavior space and countering it with geometric constraints.

## Key Problem Identified

### Privileged-Context Self-Distillation Drift
- **Setup**: Teacher and student are same model, but teacher sees hints/full solutions
- **Issue**: Teacher is confident about continuations student cannot yet justify
- **Result**: Distillation pull accumulates into drift that degrades OOD reasoning
- **Mechanism**: Standard matching wins agreement by draining mass from alternatives at high-entropy states → confident agreement on wrong answers

## Key Methodology

### 1. Hellinger Loss
- **Purpose**: Scale teacher preferences by overlap student already shares
- **Mechanism**: Attenuate pull on tokens student cannot yet support
- **Formula**: Uses Hellinger distance between teacher and student distributions
- **Benefit**: Prevents over-correction on unsupported tokens

### 2. Fisher-Rao Proximal Term
- **Purpose**: Penalize drift from recent checkpoint
- **Mechanism**: Measure distance in predictive behavior space (not parameter space)
- **Distance**: Fisher-Rao distance between next-token distributions
- **Benefit**: Constrains cumulative drift over training

### 3. Natural Gradient Updates
- **Purpose**: Take steps in the geometry of next-token distributions
- **Mechanism**: Natural gradient descent using Fisher information metric
- **Benefit**: Updates respect the statistical manifold structure

## Implementation Details

```python
# Pseudocode for GeoSD
for batch in data:
    student_logits = student(batch)
    teacher_logits = teacher(batch, privileged_context)
    
    # Hellinger loss: scale by overlap
    hellinger_dist = hellinger_distance(student_logits, teacher_logits)
    overlap = compute_overlap(student_logits, teacher_logits)
    scaled_loss = hellinger_dist * overlap
    
    # Fisher-Rao proximal term
    checkpoint_logits = load_checkpoint()
    fisher_rao_dist = fisher_rao_distance(student_logits, checkpoint_logits)
    proximal_loss = lambda * fisher_rao_dist
    
    # Total loss
    total_loss = scaled_loss + proximal_loss
    
    # Natural gradient update
    fisher_info = compute_fisher_information(student_logits)
    natural_grad = inverse(fisher_info) @ gradient(total_loss)
    student.update(natural_grad)
```

## Results

- **Benchmarks**: Mathematical reasoning benchmarks
- **Model Scales**: 1.7B to 32B
- **OOD Improvement**: +5.7-8.6 points over base model
- **In-Distribution**: Preserves gains from self-distillation

## When to Use

- Privileged-context self-distillation (teacher sees hints/solutions)
- When OOD generalization degrades during distillation
- For reasoning tasks (math, code, logic)
- When standard KL distillation causes confident wrong predictions

## Diagnostic Signs

Watch for these indicators that GeoSD might help:
- OOD accuracy drops during self-distillation
- Student becomes confidently wrong on novel problems
- High-entropy states collapse to low-entropy wrong answers
- In-distribution improves but OOD degrades

## Key Insight

Standard distillation "wins agreement by draining mass from alternatives at high-entropy states, resulting in confident agreement on wrong answers." GeoSD keeps alternatives in reach by using geometric constraints.

## Activation Patterns

- `geosd` - Geometric Self-Distillation
- `geometric-distillation` - Distillation using geometric constraints
- `hellinger-loss` - Hellinger distance-based loss
- `fisher-rao` - Fisher-Rao distance for distribution comparison
- `ood-preservation` - Preserving out-of-distribution generalization
