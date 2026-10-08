---
name: candle-null-space-source-imaging
description: "CANDLE methodology: learning-based EEG source imaging that resolves the ESI ill-posed problem by learning a prior ONLY over the null space of the subject-specific lead-field matrix, with range-space component analytically recovered. Use when solving ill-posed bioelectric inverse problems (EEG/MEG source localization), building sim-to-real pipelines with subject-specific geometry, or designing neural mass model simulators for training data."
---

# CANDLE: Null-Space Learning for Brain Source Imaging

Source: arXiv:2610.07824v1 (Suzuki, Wada, Sugiura — 2026-10-08)

## Core Idea

EEG source imaging (ESI) is ill-posed: cortical source space (N_s regions) is much higher-dimensional than sensor space (N_e electrodes, N_s >> N_e). Instead of learning the full EEG→source mapping, CANDLE decomposes source space via the **range-null space decomposition** induced by the subject-specific lead-field matrix L (from T1-MRI + BEM):

- x = P_range·x + P_null·x, where P_range = L⁺L, P_null = I − L⁺L
- **Range-space component is analytically recoverable** (observable through L): x_range = L⁺·L·x — no learning needed
- **Only the null-space component x_null (completely unobservable from measurements) is learned** from data

This restricts learning to degrees of freedom not determined by measurements, preserving geometric consistency by construction.

## Pipeline

1. T1-MRI → FreeSurfer → subject-specific cortical geometry (Hagmann/Lausanne parcellation, ~N_s regions)
2. 3-layer BEM (inner-skull/outer-skull/scalp) → lead-field L ∈ R^(N_e × N_s)
3. Denoise model D(·): denoises EEG Y before inversion (avoid noise amplification through L⁺)
4. Null-space model: estimates x_null given denoised signal
5. Final estimate: x̂ = L⁺·D(Y) + x̂_null (range + null)
6. Training loss: L_loss = ‖x̂ − x‖² + ‖D(Y) − Y_clean‖² + ‖x̂_null − x_null‖² (supervise each role separately)

## Whole-Brain Simulator (Training Data Generation)

- 1,113 subject-specific cortical geometries (HCP-scale diversity)
- Neural mass model (Jansen–Rit) per cortical region, coupled via structural connectivity → biophysically grounded source dynamics
- Source configurations from **26,273 statistical brain maps** (NeuroVault), clustered with 1,315 cognitive terms → representative source patterns modulate excitatory gain of corresponding regions
- 12,762 (EEG, source) triplets; 64-channel BioSemi montage, 500 Hz, 0.5–45 Hz bandpass

## Architecture

- Backbone: Kimi Delta Attention (Delta Rule family) + gated attention unit (GAU) module + inverted temporal normalization for non-stationarity robustness
- ~M params, ~G FLOPs, 20 epochs, batch 64, AdamW; trained in ~1.8h on RTX 4090
- Sim-to-real zero-shot: no fine-tuning on empirical data

## Results

- Simulated: HD95 37.3 mm, Dice 0.48 — beats LCMV, sLORETA, wMNE, eLORETA, ConvDip, DeepSIF, GBF
- Empirical task 1: intracranial single-pulse electrical stimulation (SPES) localization from simultaneous scalp EEG — best spatial dispersion & peak distance (stratified by SPES depth)
- Empirical task 2: epileptogenic zone estimation from presurgical interictal EEG
- Both empirical tasks: trained only on simulation, applied zero-shot; significance via two-sided Wilcoxon signed-rank with Holm correction

## Reusable Patterns

- **Null-space learning for ill-posed inverse problems**: applicable beyond ESI — any linear inverse problem with a known forward operator (image inpainting, super-resolution already cited; EEG/MEG, EIT, ultrasound tomography candidates)
- **Geometry-conditioned training**: derive hard constraints from subject anatomy; let the network learn only what measurements cannot determine
- **Sim-to-real with population diversity**: train across 1,100+ geometries so the prior covers anatomical variability → zero-shot transfer
- **NeuroVault statistical maps as source priors**: cluster 26k maps by cognitive-term correlation to sample realistic activation patterns
- **Role-separated supervision**: separate loss terms for denoiser vs null-space estimator prevent role collapse

## Limitations

- Fixed 64-channel montage; single parcellation (Hagmann/Lausanne); single neural mass model (Jansen–Rit) — different dynamics models per physiological regime may improve priors.
