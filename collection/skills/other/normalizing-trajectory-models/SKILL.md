---
name: normalizing-trajectory-models
description: >
  Normalizing Trajectory Models (NTM) methodology for few-step generative modeling with exact likelihood.
  Combines shallow invertible blocks within each denoising step with a deep parallel trajectory predictor,
  enabling end-to-end training and self-distillation for 4-step high-quality generation.
  Use when: normalizing trajectory, flow matching, few-step diffusion, trajectory modeling, exact likelihood,
  generative model distillation, self-distillation diffusion, invertible flow generation.
---

# Normalizing Trajectory Models (NTM)

## Core Concept

NTM reframes diffusion sampling: each reverse step is a conditional normalizing flow with **exact likelihood** training, unlike adversarial/consistency methods that lose likelihood. Architecture: shallow invertible blocks per-step + deep parallel predictor across trajectory.

## Key Architectural Components

### 1. Invertible Blocks Per-Step
- Each denoising step uses shallow invertible transformations
- Maintains bijective mapping between noisy and clean states
- Enables exact log-likelihood computation at every step

### 2. Parallel Trajectory Predictor
- Deep network predicts across the entire trajectory in parallel
- Captures long-range dependencies between time steps
- Trainable from scratch or initialized from pretrained flow-matching models

### 3. Self-Distillation Pipeline
- Train lightweight denoiser on the model's own score function
- Produces high-quality samples in 4 steps
- The exact trajectory likelihood enables this without distillation targets

## Training Workflow

```
1. Initialize: from scratch OR pretrained flow-matching model
2. Forward pass: compute trajectory with invertible blocks + parallel predictor
3. Loss: exact trajectory likelihood (log p(x_0|x_t))
4. Self-distill: train lightweight 4-step denoiser on model's score
5. Sample: run 4-step reverse process
```

## When to Use NTM

- Need few-step (2-4 steps) generation with quality matching 50+ step diffusion
- Require exact likelihood (e.g., for model comparison, anomaly detection)
- Want self-distillation without sacrificing likelihood framework
- Building on top of pretrained flow-matching or diffusion models

## Key Advantages vs Alternatives

| Method | Steps | Likelihood | Quality |
|--------|-------|------------|---------|
| Standard Diffusion | 50-1000 | Exact | High |
| Consistency Models | 1-4 | Lost | High |
| Adversarial Few-Step | 1-4 | Lost | High |
| **NTM** | **4** | **Exact** | **High** |

## References

- arXiv: 2605.08078 - "Normalizing Trajectory Models" by Jiatao Gu et al.
