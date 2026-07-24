---
name: continuous-metadata-conditioning-peft
description: Continuous (non-discretized) metadata conditioning for parameter-efficient VL/CLIP adaptation — feed numerical attributes directly into the prompt representation so the embedding space modulates smoothly, while inference stays purely visual (no metadata needed at test). Use when adapting vision-language models to longitudinal/temporal distribution shift where discretizing metadata into text loses signal.
---

# Continuous Metadata Conditioning for PEFT (from arXiv:2607.09443)

A parameter-efficient CLIP-adaptation trick for longitudinal / temporal robustness (animal
re-identification across years/seasons). The key contribution is a **continuous metadata-conditioning
mechanism** that preserves the numeric structure of attributes instead of turning them into text
categories.

## When to use
- Adapting a frozen VLM/CLIP to a domain with **continuous numeric metadata** (age, size, timestamp,
  sensor reading, dosage, temperature…).
- You need **robustness to temporal / distribution shift** but want to keep inference metadata-free.
- Discretizing numeric metadata into prompt text ("small", "medium", "large") is throwing away signal.

## Core idea
- Standard approach: "age: 3" → text token "three" → loses the ordered, continuous nature.
- Instead: embed the numeric value `v` through a small continuous projector (MLP / Fourier feature)
  and **add/concat it directly into the prompt representation vector** (the soft-prompt or the
  text-encoder output space), not as a discrete token.
- This lets the embedding space shift **smoothly** with the attribute → better interpolation between
  seen values and generalization to unseen ones.
- At inference: drop the metadata branch entirely — the adapted visual backbone is purely visual, so
  no metadata is required at test time.

## Implementation steps
1. Take a PEFT-CLIP baseline: LoRA on visual encoder + prompt-based supervision + cross-modal
   alignment loss. Freeze the big backbone.
2. Add a **continuous metadata projector** `g(v) → ℝ^d`: e.g. `g(v) = MLP([v; sin(2π f v); cos(2π f
   v)])` (Fourier features help cover the range) or a small 2-layer MLP with layer-norm.
3. Inject `g(v)` into the prompt representation: add to the soft-prompt tokens, or to the [CLS]/text
   embedding before the contrastive head. (Additive works; gated-add is more stable.)
4. Train with the same contrastive + ID-classification losses. The metadata branch is only active at
   train time.
5. At inference: run the visual encoder alone; metadata projector is unused.

## Results (paper)
- Improves closed-set, open-set, and **time-aware** evaluation on a 7-year longitudinal fish dataset
  + wildlife benchmarks.
- Purely visual inference pipeline (no metadata at test) thanks to PEFT + train-only conditioning.

## Pitfalls
- Scale/normalize `v` to a sensible range before Fourier/MLP; raw large numbers destabilize.
- Don't discretize upstream — the whole point is continuity. If you only have categorical metadata,
  this adds little over text prompts.
- Additive injection can be washed out by a strong prompt; use a learned gate or a dedicated prompt
  slot reserved for `g(v)`.
- Confirm train/test metadata distribution overlap; if test has values far outside train range,
  smooth modulation extrapolates poorly (still better than discrete, but verify).

## Verification
- Time-aware eval: split by timestamp; show continuous conditioning beats discretized-text and
  no-metadata baselines on future-time slices.
- Ablate the projector: mean-absolute-error of embedding modulation vs `v` should be smooth
  (monotonic-ish), confirming continuity.
- Confirm zero-metadata inference parity: test accuracy with metadata branch dropped equals trained
  capability.
