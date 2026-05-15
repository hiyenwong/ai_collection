---
name: selective-alignment-kd-snn
description: >
  Selective Alignment Knowledge Distillation (SeAl-KD) for spiking neural networks.
  Addresses the flaw of uniform timestep alignment in existing SNN distillation methods
  by selectively aligning only at erroneous timesteps, equalizing competing logits,
  and reweighting temporal alignment based on confidence and inter-timestep similarity.
  Use when distilling knowledge to SNNs, improving SNN performance via KD, or designing
  temporal-aware distillation for spiking networks.
  Activation: selective alignment distillation, SeAl-KD, SNN knowledge distillation,
  temporal distillation SNN, timestep distillation, spiking neural network distillation
---

# Selective Alignment KD for SNNs (SeAl-KD)

## Core Problem

Existing SNN knowledge distillation enforces **uniform alignment** across all timesteps,
assuming each timestep's prediction should match the teacher. But SNN predictions evolve
over time — intermediate timesteps need not all be individually correct even when the
final aggregated output is correct. Forcing every timestep toward the same target
wastes capacity and suppresses useful temporal dynamics.

## SeAl-KD Solution

Selective alignment that provides corrective guidance only where needed:

### 1. Erroneous Timestep Detection

Identify timesteps where the student prediction is wrong:
```
E = {t | argmax(logits_t) ≠ true_label}
```

### 2. Logit Equalization at Erroneous Timesteps

At erroneous timesteps, equalize competing logits to provide corrective gradient signal:
- Suppress the incorrect logit
- Boost the correct class logit
- Avoid over-penalizing near-correct predictions

### 3. Confidence-Reweighted Temporal Alignment

Reweight temporal alignment loss by:
- **Prediction confidence**: Higher confidence timesteps get less alignment pressure
- **Inter-timestep similarity**: Timesteps similar to already-correct ones get reduced weight

### 4. Combined Loss

```
L = L_task + λ1 · L_sequential + λ2 · L_temporal_similarity
```

Where L_sequential only targets erroneous timesteps with equalization.

## Advantages Over Uniform KD

- Preserves useful temporal dynamics in correct timesteps
- Avoids destructive uniform alignment that can degrade SNN performance
- Consistent improvements over existing distillation methods on static and neuromorphic datasets

## When to Use

- Knowledge distillation to SNNs (any architecture)
- Improving SNN accuracy via teacher-student training
- Temporal-aware distillation for multi-timestep spiking networks
- ANN-to-SNN or SNN-to-SNN distillation
