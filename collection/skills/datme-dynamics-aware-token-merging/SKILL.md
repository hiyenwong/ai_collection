---
name: datme-dynamics-aware-token-merging
version: v1.0.0
last_updated: 2026-10-17
description: "Training-free diffusion token merging from Tweedie dynamics."
arxiv_id: "2610.22370"
authors: "SeungJu Cha, Ye-Chan Kim, HyunGee Kim, Sungho Koh, Dong-Jin Kim"
tags: [token-merging, diffusion-models, efficiency, tweedie-estimate, training-free]
---

# DaTMe: Which Tokens to Merge? Diffusion Dynamics Decide

From arXiv:2610.22370 (2026-10-15). Code: https://github.com/SeungJuCha/DaTMe

## Problem

Token merging accelerates diffusion models, but existing criteria keep prompt-aligned foreground and merge the rest — which destroys background objects and fine details not mentioned in the prompt, degrading structural coherence.

## Method

**Dynamics-aware Token Merging (DaTMe), training-free:**

1. Build an importance map from the **Tweedie denoised estimate** (the model's own prediction of the clean image).
2. Two signals: **temporal** — inter-step change of the predicted clean image (is the token still being resolved?); **structural** — local high-frequency content (boundaries, fine details).
3. Under a given compression ratio: important tokens become **anchors** (preserved); tokens both temporally stabilized and structurally homogeneous are **safe merge candidates**.
4. Merging roles assigned adaptively per generation step.

## Results

- PixArt-α and FLUX: maintains visual fidelity across the entire image (vs text-relevance baselines that only protect prompt-mentioned regions).

## Reusable Pattern

**Use the model's self-prediction as a free importance signal.** The Tweedie estimate (or any iterate's predicted-clean output) is already computed each step and encodes (a) what is settled vs still changing and (b) where high-frequency structure lives. Deriving per-token keep/merge decisions from temporal stability × structural content of this estimate gives a training-free, prompt-agnostic criterion that protects unmentioned-but-important regions. Generalizes to any iterative refinement model that exposes intermediate clean estimates (diffusion LMs, inpainting, neural ODE solvers with per-step outputs).

## Resources

- Paper: https://arxiv.org/abs/2610.22370
- Code: https://github.com/SeungJuCha/DaTMe
