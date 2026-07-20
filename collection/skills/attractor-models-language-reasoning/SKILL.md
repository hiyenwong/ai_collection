---
name: attractor-models-language-reasoning
description: >
  Attractor Models for language and reasoning — backbone proposes output embeddings, attractor module
  refines them by solving for fixed point via implicit differentiation. Constant memory for effective depth,
  adaptive iteration count, equilibrium internalization phenomenon. Outperforms standard and looped Transformers
  across language modeling and challenging reasoning tasks (Sudoku-Extreme 91.4%, Maze-Hard 93.1% with 27M params).
  Use when designing recurrent/iterative refinement architectures, fixed-point models, energy-based reasoning,
  or efficient looped Transformers. arXiv: 2605.12466 (cs.LG, cs.AI, cs.CL, cs.NE). Fein-Ashley, Rashidinejad.
---

# Attractor Models for Language and Reasoning

> Fixed-point attractor models turn recurrence into scalable iterative refinement with implicit
> differentiation, achieving equilibrium internalization — solver removable at inference with minimal loss.

## Metadata
- **Source**: arXiv:2605.12466
- **Authors**: Jacob Fein-Ashley, Paria Rashidinejad
- **Published**: 2026-05-12
- **Subjects**: cs.LG, cs.AI, cs.CL, cs.NE

## Core Problem

Looped Transformers improve language modeling and reasoning through iterative refinement, but face:
1. **Training instability** — recurrent architectures are hard to optimize
2. **Fixed recurrence depth** — constrained to small, pre-defined iteration counts
3. **High deployment cost** — scaling recurrence is computationally expensive

## Key Innovation

**Attractor Models**: Two-stage architecture that decouples proposal from refinement:

1. **Backbone module**: Proposes initial output embeddings
2. **Attractor module**: Refines embeddings by solving for the fixed point
   - Gradients via **implicit differentiation** (not backprop-through-time)
   - Training memory is **constant** in effective depth
   - Iteration count chosen **adaptively by convergence**

### Novel Phenomenon: Equilibrium Internalization

Fixed-point training places the model's initial output embedding **near equilibrium**, allowing
the solver to be **removed at inference time** with little degradation. The model learns to
internalize the fixed-point computation.

## Results

### Language Modeling
- 770M Attractor Model outperforms 1.3B Transformer trained on **2× more tokens**
- Pareto improvement over standard and stable looped Transformers across sizes
- Up to 46.6% perplexity improvement, 19.7% downstream accuracy gain
- Reduced training cost

### Reasoning (27M params, ~1000 examples)
- **Sudoku-Extreme**: 91.4% accuracy
- **Maze-Hard**: 93.1% accuracy
- Outperforms Claude and GPT-o3 (which fail completely)
- Specialized recursive reasoners collapse at larger sizes; Attractor Models scale favorably

## Implementation Guide

### Architecture Design
```
Input → Backbone → Initial Embeddings → Attractor → Fixed Point → Output
                  (feed-forward)        (iterative, implicit diff)
```

### Training
- Implicit differentiation for gradients through fixed point
- No need for BPTT or truncated backprop
- Memory efficient — constant regardless of effective depth

### Inference
- Adaptive convergence: iterate until solution stabilizes
- After training: solver may be removed (equilibrium internalization)
- Backbone alone produces near-fixed-point outputs

## Applications
- Efficient language model pretraining with iterative refinement
- Reasoning tasks requiring recursive/iterative computation
- Memory-constrained deployment of recurrent architectures
- Energy-based inference systems
- Neuro-inspired reasoning models with attractor dynamics

## Pitfalls
- Fixed-point convergence not guaranteed for all inputs
- Implicit differentiation requires stable Jacobian at fixed point
- Equilibrium internalization is an emergent property, not enforced

## Related Skills
- attractor-fcm-gradient-descent
- attractor-metadynamics-neural
- attention-residuals
- memory-efficient-looped-transformer
- neuro-attractor-landscape-working-memory
