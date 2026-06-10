---
name: unipet-universal-pet-denoising
description: Universal PET image denoising methodology that handles varied dose reduction factors (DRFs) without performance degradation. Based on arXiv:2606.11131.
tags: [medical-imaging, pet, nlow-dose, ndenoising, ndose-reduction, nuniversal-network, ndeep-learning, nmedical-ai]
arxiv: "2606.11131"
created: "2026-06-10"
---

# UniPET: Universal PET Denoising

Methodology for building universal PET image denoising networks that handle varied dose reduction factors (DRFs) without the performance degradation seen in fixed-DRF approaches.

## Context

Most existing deep learning-based PET image denoising methods assume a fixed and known dose reduction factor (DRF) for low-dose PET images. However, these methods encounter significant performance degradation when the DRF varies beyond the assumed one in practical applications.

## Core Problem

- **Fixed DRF assumption**: Models trained on specific DRF (e.g., 1/4 dose) fail when applied to different DRFs (e.g., 1/8 or 1/16 dose)
- **Clinical reality**: Dose reduction varies based on patient weight, scanner protocol, and clinical indication
- **Need**: A single model that generalizes across all DRF levels

## Methodology

### 1. DRF-Conditional Architecture

- **Input conditioning**: Encode DRF as an additional input channel or parameter to the network
- **Adaptive feature extraction**: Network learns DRF-specific feature transformations
- **Unified representation**: Shared backbone with DRF-conditioned modulation

### 2. Training Strategy

- **Multi-DRF training**: Train on simulated low-dose PET images across a range of DRFs (1/2, 1/4, 1/8, 1/16)
- **Dose-aware loss**: Weight loss function based on DRF level (lower dose = higher weight)
- **Cross-DRF regularization**: Penalize performance variance across DRF levels

### 3. Key Design Patterns

- **Dose embedding**: Learnable embedding vector for each DRF level
- **Adaptive normalization**: DRF-conditioned batch/instance normalization
- **Multi-scale processing**: Handle noise characteristics that vary with dose level

### 4. Evaluation Protocol

- **Metrics**: PSNR, SSIM, RMSE on denoised vs full-dose reference
- **Clinical validation**: SUV (Standardized Uptake Value) accuracy for lesion detection
- **Generalization test**: Evaluate on unseen DRF levels

## When to Use

- Building PET denoising models for clinical deployment
- Low-dose PET imaging workflows
- Medical imaging AI requiring dose-agnostic performance
- Quantitative PET analysis where SUV accuracy is critical

## Trigger Words

PET denoising, low-dose PET, dose reduction, universal denoising, medical image quality, nuclear medicine, SUV quantification
