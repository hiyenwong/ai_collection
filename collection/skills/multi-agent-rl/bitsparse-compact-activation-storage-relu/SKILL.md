---
name: bitsparse-compact-activation-storage-relu
description: "BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22256"
utility: 0.88
date: "2026-10-17"
---

# BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks

**arXiv:** [2610.22256](https://arxiv.org/abs/2610.22256)
**Authors:** Max Zhu, Bohang Sun, Pietro Lio, Jialin Yu
**Published:** 2026-10-15
**Categories:** cs.LG
**Utility Score:** 0.88

## Abstract

Reducing memory use in large language model (LLM) training is an ongoing challenge. Activation checkpointing saves memory by recomputation, while lossy compression changes the stored activations. The reemergence of sparse $\relu$ and $\relu^2$ activations creates a third opportunity: losslessly compressing the activation cache itself. We present BitSparse, a GPU-resident lossless compression format for sparse activations. Compression and reconstruction run in custom Triton kernels fused into an autograd function, shrinking the activation cache while recovering it exactly for the backward pass. Bfloat16 (BF16) and FP8 activations are supported. Optional sign-bit packing further increases compression up to close to the theoretical limit. We analyze its compression ratio and compare it to the theoretical optimum. BitSparse lowers per-token VRAM by 31\% and 30\% Modded-NanoGPT and Nemotron-H respectively, with overheads of no more than 1\% at practical sequence lengths. Additionally, a new preallocated buffer system avoids host synchronization during training when variable size tensors are allocated.

## Key Contributions

- Novel research in cs.LG
- High utility score (0.88) indicating significant research value

## Activation

bitsparse, compact, activation, storage, relu, feedforward, networks

## Notes

Added by arXiv cron job on 2026-10-17.
