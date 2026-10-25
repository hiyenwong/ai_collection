---
name: sparsedecoding-decoding-aware-pruning
description: Decoding-aware pruning for LLM inference - calibrate Hessian pruning on self-generated tokens, not natural text, plus N:M sparse SpMV kernels for wall-clock decoding speedup.
category: ai_collection
trigger: LLM pruning, structured pruning, N:M sparsity, Hessian calibration, decoding latency, SpMV kernel, memory-bound inference, layer-wise compression, OBS pruning
---

# SparseDecoding: Decoding-Aware Pruning for LLM Inference

Methodology from arXiv:2610.12327 (Wang et al., 2026-10-08, cs.LG/cs.CL): layer-wise training-free
LLM pruning fails silently when calibration data distribution mismatches the decoding-time
distribution. Fix both the **algorithmic axis** (calibration distribution) and the **system axis**
(kernel support) to get real decoding speedups.

## The Distribution-Shift Diagnosis (reusable insight)

- Standard Hessian pruning (OBS/Wanda-style) computes layer Hessians from **pre-collected natural
  sequences** (e.g., C4/WikiText). But during autoregressive decoding the model consumes
  **self-generated tokens** — a persistent distribution shift.
- The Hessian computed on natural text misestimates which weights matter during generation.
  Consequence: the activation distribution during generation **deviates from the one used to
  set pruning masks**, so error compounds over long-form generation far more than on
  short perplexity benchmarks.
- Rule: **any pruning calibration that targets decoding must sample from the model's own
  autoregressive rollout, excluding the prefill phase.**

## Algorithmic Axis: Generation-Aligned Calibration

1. Run the dense model in greedy/sampled autoregressive generation on a small set of prompts.
2. Collect layer-wise activations **from generated tokens only** (skip prefill activations).
3. Build per-layer Hessian proxies H = 2·XᵀX from these activations (X = collected inputs).
4. Apply standard layer-wise pruning (OBS-style weight removal + reconstruction) under an
   N:M sparsity constraint using this generation-aware Hessian.
- This alone recovers most of the accuracy gap on long-form generation benchmarks
  (perplexity under self-generated context, instruction following, summarization).

## System Axis: N:M SpMV Kernel (the actual speedup lever)

- Most "sparse LLM speedup" work optimizes sparse mat-mat (SpMM) — useful in prefill,
  but **decoding is memory-bound sparse mat-vec (SpMV)**, which 2:4-style kernels often ignore.
- SparseDecoding builds an optimized N:M SpMV CUDA kernel with:
  - **Bitmask indexing** for nonzero locations (compact metadata vs full index tensors)
  - **Fixed-step traversal** (regular memory access pattern; the N nonzeros per M group
    are laid out so the kernel reads a fixed number of cache lines per group)
- Deployment recipe: prune with N:M structured sparsity, materialize the bitmask layout,
  call the kernel during decoding; prefill can keep SpMM or fall back to dense.

## Empirical Anchors

- Models: Llama-3.1-8B, Llama-3.3-70B, Qwen3-14B/32B.
- Up to **1.48× end-to-end wall-clock decoding speedup on A100**, consistently beating
  fixed-text-calibrated pruning baselines on long-form generation benchmarks.
- Natural-text calibration is not just suboptimal — its failure grows with generation length,
  so evaluate pruning methods on **self-generated long outputs**, not only short-sequence PPL.

## Reusable Checklist (when pruning for inference)

1. Ask: is the target workload prefill-heavy (SpMM) or decode-heavy (SpMV)? Pick kernel first.
2. Calibrate on the distribution the runtime actually sees:
   - decoding target → self-generated tokens (exclude prefill)
   - prefill target → natural long contexts
3. Use N:M structured sparsity with a real SpMV kernel + bitmask layout; unstructured
   sparsity without kernel support gives zero wall-clock gain.
4. Evaluate with long-form generation metrics (not just short-context PPL) to expose
   rollout drift of the pruned model.
