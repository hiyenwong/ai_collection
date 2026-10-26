---
name: revit-depth-programmed-experts
description: Recurrent ViT where one block applied at multiple depths matches a full-depth encoder - depth-programmed FFN expert bank with a continuous normalized-depth coordinate and weight-space merging.
category: ai_collection
trigger: recurrent transformer, weight sharing, depth-conditional FFN, mixture of experts, elastic depth, parameter-efficient vision encoder, resampleable trajectory, weight-space MoE
---

# reViT: Recurrent Vision Transformers with Depth-Programmed Experts

Methodology from arXiv:2610.12448 (Bulat, Ouali, Tzimiropoulos, 2026-10-08, cs.CV/cs.LG): a single
Transformer block applied recurrently normally forfeits depth-specific transformations. reViT
restores them so a **one-block recurrent encoder matches a full-depth encoder at comparable
inference FLOPs — no intermediate feature distillation required**.

## Core Mechanism

- Recycle one block D times; at recurrence depth d, the FFN is computed as a
  **convex combination of a small shared expert bank**:
  FFN_d(x) = Σ_k g_k(d) · E_k(x), with Σ_k g_k(d) = 1, g_k ≥ 0.
- **Depth programming**: the mixture weights g_k are produced from a continuous
  **normalized-depth coordinate** d/D ∈ [0,1] (tiny hypernetwork or fixed schedule over d).
  Depth becomes a *resampleable coordinate* in FFN parameter space — a trajectory through the
  expert bank rather than a fixed sequence of independent FFNs.
- Result: the model can also run at **other depths** by resampling the same coordinate interval
  (elastic-depth deployment from one checkpoint).

## Which MoE Family for Depth-Conditional Computation (controlled finding)

Tested families at a matched one-FFN-per-depth budget:
1. **Weight-space merging** (experts merged into effective FFN weights per depth) — **strongest**
2. Token-dispatch (route tokens to experts) — weaker
3. Output-mixture (combine expert outputs) — weaker

Lesson: when conditioning on a *continuous control variable* (depth, time, scale), merging in
**weight space** beats routing in activation space — cheaper (no dispatch logic at inference)
and more stable to train.

## Deployment Modes

- **Fixed-depth deployment**: materialize the recurrent block as a conventional dense graph —
  unroll recurrences, precompute merged FFN weights per depth → removes online routing/merging,
  keeps one-FFN-per-depth compute, at the cost of storage expansion (still ~70% fewer *stored*
  parameters than a full encoder).
- **Elastic-depth deployment**: keep the coordinate; at inference choose D' < D, resample the
  mixture trajectory for D' depths. One checkpoint, multiple tested depths.

## Empirical Anchors

- Supervised ImageNet-1k: reViT-B/16 attains **DeiT III accuracy with ~70% fewer stored params**.
- Distillation from a DINOv2 teacher using **only output features**: 8-expert model retains
  nearly all teacher linear-probe accuracy; transfers to classification, segmentation,
  depth prediction.

## Reusable Patterns

1. Parameter sharing + a **low-dimensional conditioning coordinate** over a small expert bank
   ≈ a dense model with far fewer stored parameters. Apply wherever a model is unrolled over
   a scalar variable (depth, time, scale, resolution).
2. Prefer **convex combinations in weight space** over token routing for continuous conditioning.
3. "Elastic X from one checkpoint" recipe: train with a normalized coordinate; at inference
   resample the coordinate interval for a different budget — no retraining, no architecture edit.
4. Output-feature-only distillation suffices to transfer rich pretrained representations into
   such compact recurrent encoders (no intermediate-layer hint teachers needed).
