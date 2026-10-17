---
name: training-free-on-policy-distillation
version: v1.0.0
last_updated: 2026-10-17
description: "Merge fine-tuned specialists into one model, training-free."
arxiv_id: "2610.22236"
authors: "Bangji Yang, Jiajun Fan, Zhaoyu Zhu, Hongbo Ma, Ge Liu"
tags: [distillation, model-merging, on-policy, least-squares, efficiency]
---

# Training-Free On-Policy Distillation

From arXiv:2610.22236 (2026-10-15).

## Problem

On-policy distillation consolidates specialist models into one student but pays rollouts + teacher passes + gradient steps for every teacher. When specialists share a base model, much of this cost is unnecessary.

## Method

**Forward-pass-only consolidation.** When specialists share a base model, distillation has an exact layer-wise solution:

1. Each linear layer of the fused model must reproduce every specialist's output **on the inputs that specialist receives, while reading its own answers** (self-consistency condition).
2. This is a least-squares problem per layer, solvable from **only the second moments of the inputs** — no gradients, no backprop.
3. One forward pass over a few hundred rollouts per specialist provides the second moments.
4. Rollout curation beats solver sophistication: answers truncated in repetition loops are a small fraction of a math specialist's rollouts but carry a large share of tokens; removing them lifts the fused model from task-arithmetic level to specialist level at matched precision.

## Results

- Olmo 3 7B: a few GPU-hours of forward compute per specialist yields a generalist keeping most of each specialist's gain across 7 math/code benchmarks.
- Fused model on average more accurate than either specialist alone.
- Repetition-loop filtering on AIME25 was the decisive factor, not the solver.

## Reusable Pattern

**Second-moment closed-form fusion for shared-base specialists.** Whenever multiple fine-tunes branch from the same base model, the fusion can be computed per-layer as least squares from input second moments gathered by a single forward pass over rollout data. Two transferable sub-patterns: (1) "reading its own answers" — the fused layer must reproduce specialist outputs when fed the fused model's own preceding activations, making the solution self-consistent rather than a naive weight average; (2) data curation of degenerate rollouts (repetition loops) matters more than optimization details. Applies to merging RL-tuned agents, task-vector consolidation, and routing-free specialist deployment.

## Resources

- Paper: https://arxiv.org/abs/2610.22236
