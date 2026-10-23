---
name: spectral-window-transfer-pretraining
description: Spectral-window transfer analysis for cross-domain foundation models - pretraining transfer quality is governed by the overlap between the pretrained model's spectral window and the target domain's spectra (infrared-pretrained model falls below untrained control on optical/UV tasks). Use for deciding pretrained-vs-in-domain pretraining for spectroscopy, sensor, or any wavelength/frequency-structured scientific data.
category: ai_collection
trigger_words: spectral foundation model, transfer learning, domain gap, auroral spectra, masked autoencoder, 1D vision transformer, linear probe, fine-tuning, spectrograph, SpectraFM, SpecFormer, scientific foundation model, pretraining window
---

# Spectral-Window Transfer: From Foundation Models to Scientific Spectra

**Source**: arXiv:2609.31206v1 (2026-09-25) — Le Lain, Cessateur, Lefèvre, cs.LG/physics.space-ph.

## Problem

Scientific instruments (here: auroral spectrographs like ASIS) produce hundreds of thousands of spectra but only hundreds of expert labels. Should you fine-tune an existing pretrained spectral/time-series foundation model, or pretrain in-domain on the unlabeled data?

## Core Finding: Transfer Is Governed by the Spectral Window

Existing pretrained models transfer **according to the overlap between their pretraining spectral window and the target's spectral range**:

- **SpectraFM** (trained in **infrared**) on optical auroral task → **falls below the untrained control** (negative transfer!)
- **SpecFormer** (trained in **optical**) → approaches in-domain pretraining but does not reach it

So for wavelength-structured data, "use the biggest pretrained model" is wrong advice — a mismatched pretraining window is worse than nothing.

## The Winning Recipe (in-domain masked pretraining)

1. Pretrain a **1D Vision Transformer with masked autoencoder** (MAE) on all 223,000 **unlabelled** spectra.
2. Probe frozen representations: they recover the **emission-line intensity ratios physicists actually use** for diagnosing precipitating particles (R² 0.91 vs. 0.77 untrained control) — without any labels.
3. Linear probe: matches classification using 13 hand-designed expert features.
4. Fine-tune: beats the previous supervised auroral classifier on its own benchmark (macro-AP 88.5 vs. 77.8); **+0.159 over training the same architecture from scratch using only 10% of the labels**; attribution confirms the model uses physically meaningful N2+ bands.

## Decision Rule (reusable)

For frequency/wavelength-structured scientific data:

```
If pretrained model's training window ∩ target window ≈ ∅  → negative transfer risk; prefer random init or in-domain pretraining
If partial overlap (adjacent bands)                        → usable but expect a gap vs. in-domain pretraining
If unlabeled target data ≥ ~100× labeled data               → in-domain MAE pretraining is cheap and dominates
```

## Reusable Methodology: Physics-Grounded Pretraining Validation

- **Probe against known physical quantities** (here: emission-line ratios) — if the frozen representation recovers the variables domain scientists use for diagnosis, pretraining learned real structure, not shortcuts.
- **Untrained control is the mandatory baseline** — it quantifies architectural inductive bias vs. learned features; skip it and you cannot detect negative transfer.
- **Attribution check**: confirm the fine-tuned model attends to physically meaningful features (N2+ bands), guarding against spurious correlations.

**Activation**: scientific spectra pretraining, MAE 1D ViT, transfer window analysis, negative transfer detection, label-efficient scientific ML, spectroscopy foundation models.
