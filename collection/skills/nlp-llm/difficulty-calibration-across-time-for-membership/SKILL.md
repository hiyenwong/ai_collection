---
name: difficulty-calibration-across-time-for-membership
description: "Difficulty Calibration Across Time for Membership ..."
tags: [cs.CV, cs.CR, cs.LG]
source: arxiv
arxiv_id: 2610.40616v1
utility: 0.88
published: 2026-10-29
---

# Difficulty Calibration Across Time for Membership Inference in Diffusion Models

**Authors:** Michael Joseph, Yedid Hoshen
**Published:** 2026-10-29
**arXiv:** [2610.40616v1](https://arxiv.org/abs/2610.40616v1)
**Categories:** cs.CV, cs.CR, cs.LG
**Utility Score:** 0.88

## Abstract

Modern diffusion models are trained on massive datasets that often include copyrighted or private images. Membership inference attacks (MIAs) address this by testing whether a given image was in a model's training set. The standard approach scores an image by its reconstruction loss and flags low-loss images as members. This often fails because some images are simply easier to reconstruct than others, so a simple unseen image can score a lower loss than a complex training image. Difficulty calibration separates memorization from how difficult an image is to begin with. We show how to calibrate along two axes of time: training time and diffusion time. First, across training time, we introduce Reference-Model Calibration (RMC), which compares a fine-tuned model's loss against an earlier checkpoint. This cleanly isolates newly memorized data and gives near-perfect auditing, even without text captions. Since earlier checkpoints are not always available, we next present Temporal Self-Calibration (TSC), which calibrates across diffusion time using only a single model. Our key observation is that an image's difficulty persists across noise levels, whereas memorization is localized in time. By comparing the loss at a target timestep against neighboring timesteps from the same model, TSC attenuates image difficulty using the model's own trajectory. Empirically, our methods beat the state of the art by a wide margin, and unlike most existing attacks, generalize across different model p

## Key Contributions

- Novel research in cs.CV, cs.CR
- Published 2026-10-29

## Activation

difficulty, calibration, across, time, membership, inference, diffusion, models
