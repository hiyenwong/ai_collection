---
name: sparseforge-hessian-mask
description: Efficient semi-structured LLM sparsification via annealing of Hessian-mask guided pruning. Achieves high sparsity with minimal accuracy loss using second-order importance estimation.
category: deep-learning
tags: [LLM, sparsification, pruning, Hessian, compression, efficiency]
trigger: sparseforge, hessian mask, semi-structured pruning, LLM sparsification, 2:4 sparsity, model compression
---

# SparseForge: Hessian-Mask Guided Semi-Structured Pruning

## Overview
SparseForge achieves efficient semi-structured (e.g., 2:4) sparsity in LLMs by using Hessian-based second-order importance estimation with an annealing schedule to guide pruning decisions.

## Core Technique
1. **Hessian-Driven Importance**: Compute diagonal Hessian (or Fisher information) to estimate parameter sensitivity
2. **Mask Annealing**: Instead of one-shot pruning, gradually anneal a binary mask over training steps
3. **Semi-Structured Constraints**: Enforce N:M sparsity patterns (e.g., 2 out of every 4 weights = 0) for hardware efficiency
4. **Recovery Fine-Tuning**: Brief fine-tuning with the annealed mask to recover accuracy

## Key Benefits
- **Higher accuracy** at same sparsity vs. magnitude-based pruning
- **Hardware-friendly** 2:4 sparsity patterns compatible with Tensor Cores
- **Annealing** prevents catastrophic accuracy drops from aggressive one-shot pruning

## Implementation Steps
1. Compute per-parameter Hessian diagonal via Fisher approximation (gradient outer product)
2. Initialize soft mask with sigmoid parametrization
3. Anneal mask temperature over training: soft → hard binary decisions
4. Apply N:M structural constraints during mask hardening
5. Fine-tune with masked weights, optionally with distillation loss from dense model

## Pitfalls
- Hessian computation is expensive — use diagonal/Fisher approximation for LLM-scale models
- Annealing schedule is critical: too fast → accuracy collapse; too slow → wasted compute
- N:M constraints require specialized kernel support or careful indexing for inference speedup

## Activation Keywords
sparseforge, hessian mask, semi-structured pruning, LLM sparsification, 2:4 sparsity, model compression, Fisher information, mask annealing
