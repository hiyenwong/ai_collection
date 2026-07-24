---
name: foveated-dynamic-token-selection
description: Foveation-guided dynamic token selection for robust and efficient vision transformers. Inspired by human visual system foveated sampling + eye movements. Use when building efficient ViTs, dynamic token pruning/selection, or robustness-to-noise/adversarial without explicit robust training.
---

# Foveated Dynamic Token Selection (FDT)

Architecture from "Foveated Dynamic Transformer" (arXiv:2607.09480). Integrates human visual
system (HVS) foveated sampling + saccadic eye movements into a vision transformer to get adaptive
computation AND emergent robustness to noise/adversarial attacks without ever training for them.

## When to use
- Building efficient ViTs where you want to drop a fraction of tokens (fixation budget) and still
  beat a dense baseline on accuracy.
- You need robustness to input noise / corruptions / adversarial perturbations but do NOT want to
  add adversarial training or augmentations (FDT is robust by construction).
- You want a biologically-plausible adaptive-computation story for a vision model.

## Core idea
Split token processing into two learned modules:
1. **Fixation module** — given the current token set, selects fixation points (which tokens/regions
   to attend closely). Implement as a lightweight scorer that filters out "irrelevant" tokens under a
   fixed *fixation budget* (e.g. keep top-50% of tokens).
2. **Foveation module** — for the retained (fixated) tokens, generates foveated embeddings that
   carry multi-scale information (center = high-res detail, periphery = coarse context), analogous
   to the retina's acuity gradient.

The fixation budget is a dial: lower budget → less MACs, higher budget → more accuracy.

## Implementation steps
1. Start from a standard ViT (patch tokens + cls). Insert a fixation scorer after each (or selected)
   transformer blocks: `scores = fixation_net(hidden_states)` where `fixation_net` is a 1–2 layer MLP
   over token dim.
2. At each fixation step, keep the top-k fraction of tokens by score (k = fixation budget). Drop/
   mask the rest (they are not passed to the next block, or zeroed with a mask).
3. The foveation module: for each kept token, aggregate a local neighborhood at multiple downsampling
   rates (multi-scale) into a single foveated embedding. Concatenate or gated-sum with the original
   token embedding.
4. Train with the standard classification loss only. No robustness loss.
5. At inference, sweep the fixation budget to trace the accuracy–efficiency frontier.

## Key results (from paper)
- At 50% fixation budget: 81.9% vs DeiT-S 80.9%, with **34.57% fewer MACs**.
- Emergent robustness: noise and adversarial attacks degrade FDT far less than DeiT-S, despite no
  explicit robust training — because dynamic selection breaks the static receptive-field assumption
  attackers rely on.

## Pitfalls
- Fixation scoring must be cheap; if the scorer costs more than the tokens it saves, you lose the
  efficiency win. Keep it 1–2 layers.
- Multi-scale foveation needs careful padding/stride at patch boundaries; use unfold/im2col with
  valid padding then average, not naive conv, to avoid leakage.
- The fixation budget interacts with depth: apply fixation progressively (more aggressive dropping in
  early layers, conservative in late layers) — uniform dropping hurts accuracy.
- Evaluate robustness on the SAME budget you deploy at; robustness gains can shrink if you push the
  budget too low.

## Verification
- Compare accuracy vs MACs curve against the dense baseline at matched depth/width.
- Report clean accuracy, corrupted (e.g. ImageNet-C style) accuracy, and PGD/FGSM adversarial
  accuracy at the chosen budget.
