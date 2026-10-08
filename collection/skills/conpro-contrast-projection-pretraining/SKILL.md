---
name: conpro-contrast-projection-pretraining
version: v1.0.0
last_updated: 2026-09-26
description: "ConPro methodology — self-supervised pretraining whose target is a physics-derived temporal projection (normalized drop below temporal median), converting unlabeled modality dynamics into free supervision for label-efficient segmentation. Use when: (1) unlabeled sequences record a physical process that labels encode statically, (2) designing self-supervised targets that beat reconstruction pretexts, (3) stacking pretraining + semi-supervised training for label efficiency. Keywords: self-supervised pretraining, label-efficient segmentation, temporal median, DSA, angiography."
arxiv_id: "2609.30043"
authors: "Xinge Guo, Yuanhao Wang, Liqi Shu, Yang Liu, Min Xu"
tags: [self-supervised, pretraining, label-efficiency, medical-imaging, temporal-dynamics]
---

# ConPro: Contrast Projection Pretraining

From arXiv:2609.30043 (2026-09-24).

## Problem

Dense vessel annotation in DSA sequences is laborious — but **every unlabeled sequence already records how contrast passes through vessels**. Generic self-supervised pretexts (reconstruction of static appearance) waste this signal; semi-supervised methods bootstrap from the current model instead of from the physics.

## Method

**Pretraining target = contrast projection**: for every pixel, the normalized drop below its **temporal median** over the sequence. This is a physics-derived map of contrast-agent dynamics — where and when blood flow deposits dye.

Critical design lesson from controlled comparisons:
- The gain comes from **learning to predict the projection** (input → projection target), NOT from using the projection as an input channel or pseudo-label (both help little or hurt)
- A temporal-median target with same input/loss/budget stays at scratch level → the *contrast dynamics* content matters, not the temporal filtering

## Results

- Improves over scratch at 10%/20%/50% label fractions on DIAS and DSCA
- **Composable**: initializing UniMatch (strongest semi-supervised baseline) from ConPro weights gains +0.5–2.0 Dice and +0.9–2.3 clDice at every label fraction (75.4 Dice DIAS, 81.3 DSCA)
- Architecture-agnostic: provides pretrained weights without changing the segmentation head

## Reusable Pattern

**Mine the physical process as a pretraining target.** When unlabeled data records a physically meaningful temporal signal (flow, diffusion, perfusion, growth), derive a closed-form projection of that process (here: pixelwise below-median drop) and pretrain the encoder to predict it. Two rules: (1) the target must encode process dynamics, not static statistics — controlled comparisons are mandatory to prove it; (2) pretraining must be architecturally transparent so weights compose with downstream semi-supervised methods rather than compete with them.

## Resources

- Paper: https://arxiv.org/abs/2609.30043
