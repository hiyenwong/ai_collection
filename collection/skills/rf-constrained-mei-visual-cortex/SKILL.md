---
name: rf-constrained-mei-visual-cortex
description: Use when synthesizing most-exciting-inputs for early visual cortex voxels.
category: ai_collection
---

# Receptive-Field-Constrained MEI Optimization for Early/Intermediate Human Visual Cortex

**Source**: arXiv:2609.36391 (Zhao†, Guo†, Luo, Henderson — CMU & HKU, 28 Sep 2026)

## Core Problem

Most-exciting-input (MEI) synthesis — data-driven probing of neural feature selectivity — worked for human *higher* visual cortex (large pRFs) but fails for V1–hV4: **small receptive fields** mean an unconstrained optimizer puts features anywhere in the image, ignoring where the voxel actually looks. Fix: build the pRF into the encoding model itself, then optimize through it.

## Two Frameworks

Both start from a subject-specific **pRF-constrained voxelwise encoding model** (afwRF-style: pRF-weighted feature pooling over a pretrained backbone, trained on Natural Scenes Dataset fMRI).

### RF-DiVE (Receptive Field Diffusion for Visual Exploration)
- Stable Diffusion v2.1, DPM-Solver, 100 denoising steps, empty prompt, CFG disabled
- At each step, gradients from the generation encoder guide denoising to maximize ONE target voxel's predicted response (brain-guidance scale 300, self-attention guidance 0.75)
- Output: naturalistic, colorful, coherent images

### RF-GO (Receptive Field Gradient Optimization)
- Fourier-phase gradient ascent (à la feature visualization), 100 steps, NAdam lr=1.0
- Output: texture-like, higher spatial-frequency images

**Shared protocol**: per voxel, generate **1,000 images with different random seeds**, then rank. Luma controls during optimization AND before ranking/eval: full-image mean luma 116/255, RMS contrast 57.48/255 (match natural training stats); pRF-local luma/contrast controls in appendix. Top-10 MEIs by an independent **ranking model** selected for analysis.

**Three-model design (critical for validity)**: generation encoder (trained on subject P1 train split) ≠ ranking model ≠ independent **test encoder** for in-silico validation. Without this separation, MEIs that exploit encoder quirks look falsely good.

## Findings

1. **Spatial + feature specificity**: MEIs show consistent structure *inside* the pRF circle, random outside — the pRF constraint works as intended. Features include contour, color, texture, form (e.g., high-contrast yellow-black rectilinear contours for some V1 voxels)
2. **MEIs beat natural images**: across V1–hV4, both methods, both backbones (ADV, DINO), MEIs elicit higher model-predicted responses than the top natural images from NSD or LAION-fMRI (paired-voxel tests, BH-corrected)
3. **Method trade-off**: RF-GO wins difference score under its own generation encoder but **generalizes worse to the independent test encoder** (worse for DINO backbone); RF-DiVE MEIs are more coherent/colorful — generator choice shapes MEI appearance, statistics, and cross-model generalizability
4. **Behavioral validation**: n=32 forced-choice — hV4 RF-DiVE MEIs judged to have more 3D form than V1 MEIs (matches known V1→V4 form-sensitivity increase); the same preference was NOT reliable for natural LAION images — synthesized MEIs expose selectivity that natural image mining misses

## Reusable Patterns

1. **pRF-constrained optimization**: any stimulus-optimization for retinotopic cortex must route gradients through the pRF-weighted model — unconstrained MEIs are spatially meaningless at voxel level
2. **Diffusion-guided neural stimulation (RF-DiVE)**: brain-guidance gradient injected at every denoising step — a general recipe for naturalistic, model-guided stimulus synthesis; scale ~300 shows neural signal can dominate SD's prior
3. **Generation/ranking/test model separation**: never evaluate synthesized stimuli with the model that generated them; use a held-out encoder for in-silico validation and an independent ranker for selection
4. **Many-seeds + top-k selection**: 1,000 seeds per voxel → rank → top-10; MEI optimization is stochastic, single-seed results are unreliable
5. **Matched-luma projection during optimization**: control brightness/contrast continuously during the search (not post-hoc) so the optimizer can't win via luminance shortcuts
6. **Cross-method triangulation**: features consistent across RF-DiVE + RF-GO are likely real tuning; method-unique features may be generator artifacts — use multiple generators as robustness filter
7. **Behavioral closed-loop check**: human forced-choice on synthesized stimuli as external validity test

## Limitations

- All validation in-silico except one preliminary behavioral study; closed-loop fMRI presentation still needed
- Quantitative feature analysis limited to low-level stats (Gabor, color, edge, curvature); mid-level feature space not characterized
- Early-visual MEIs here don't yet rival single-unit MEI interpretability

**Activation**: most-exciting-input, MEI, receptive field, pRF, voxelwise encoding model, fMRI, stimulus optimization, diffusion-guided generation, gradient ascent visualization, natural scenes dataset, visual cortex selectivity, V1 hV4, feature visualization, model-guided experiment design
