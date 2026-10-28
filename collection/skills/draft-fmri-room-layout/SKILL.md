---
name: draft-fmri-room-layout
description: "Use when fMRI decodes scene layout with trajectory priors."
category: ai_collection
version: 1.0
author: neuro-cron-2026-10-26
license: MIT
metadata:
  hermes:
    tags: [fmri-decoding, room-layout, layout-code, free-space-prior, camera-trajectory, early-visual-cortex, flow-matching, coarse-to-detail, metric-evaluation]
    related_skills: [fmri-gesture-reconstruction, mind-omni-brain-vision-language-unified, geometric-brain-dynamics-mapping-gbf, visual-imagery-decoding-fmri]
  arxiv_id: "2610.31108"
  paper_title: "DRAFT: Decoding and Reconstructing 3D Room Layouts from fMRI and Camera Trajectories"
  paper_authors: "Chi-Wei Lee, An-Kai Chen, Cheng-Han Chiang, Yi-Chun Chang, Po-Chih Kuo"
  published: "2026-10-22"
---

# DRAFT: fMRI Room-Layout Decoding with Camera-Trajectory Priors

Decode a **22-number interpretable layout code** from early visual cortex (EVC) + camera motion, fuse it with a free-space prior derived from the camera path, and swap the fused layout into the **low frequencies of ANY depth decoder without retraining**. First method to recover the **metric geometry of held-out rooms from fMRI of moving-viewpoint walkthroughs** (no visual frames), evaluated against ray-cast ground truth. arXiv 2610.31108 (NTHU / NYCU).

## When to Use

Use when: decoding scene/layout geometry (walls, floor, depth structure) from brain signals rather than dense pixels; you have **known or estimable agent/camera trajectories** alongside neural recordings and want to exploit them as a prior; fMRI is slow/blurry relative to the signal (BOLD vs fast viewpoint changes) so dense per-frame decoding is hopeless; you need a **plug-in coarse-geometry prior** that improves existing decoders post hoc; evaluating reconstruction claims where pixel metrics reward plausible detail over correct geometry.

## Problem

Dense fMRI decoders (MindEye, Brain-Diffuser, DREAM) produce plausible images but their low-frequency geometry is wrong, and they are scored with pixel metrics that even a WRONG SCENE passes. BOLD blurs seconds together while the viewpoint moves every second; recordings are few. None of them decode metric layout of unseen scenes from a moving viewpoint.

## Core Method

### 1. Decode a small interpretable code, not the dense signal

Per 1-s view, target a 22-dim layout code in log radial depth:

    y(D) = [w_1..w_12, f_1..f_4, o_1..o_4, med log D, IQR log D]

- w_k: wall distance near horizon in azimuth bin k (12 bins)
- f_b: floor extent in vertical band b (4)
- o_q: share of far pixels in quadrant q (4)
- plus median and interquartile range of log depth

Ridge regressions beat deep decoders on the geometry question because the target matches what the metric scores.

### 2. Readout with per-entry error bars

Six ridge regressions (different voxel counts, penalties, response windows), averaged. Inputs: EVC (V1, V2, V3v, hV4) most-reliable voxels compressed to 16 PCs, + 12 camera-motion regressors (constant, speed and turning speed at lags 0-4 s, linear trend). Each code entry j gets posterior mean µ_j and spread s_j = out-of-fold residual SD. Pooling across styles: average readouts of recordings sharing poses, weighted by counts — never uses depth labels.

### 3. Trajectory as free-space prior (the "dark room" argument)

Every visited position is free space — walking through a dark room shows where the walls are NOT. Trajectory head: ridge on 111 path features, core = per-direction free-space distance (largest camera-to-visited-position distance in each of 12 directions) -> 3x3 log-depth layout. Use as a LEARNED PRIOR, not a hard bound on wall distance.

### 4. Fusion by stacking

    l_hat_t = W_F [µ_t ; l_T_t] + b_F

Fusion head (ridge, fitted on out-of-fold inputs) combines brain-code readout and trajectory layout into the DRAFT layout l_hat ∈ R^9 (3x3 cells).

### 5. Training-free low-frequency swap (the plug-in)

    log D_t = G_σ * U(l_hat_t) + (log Ď_t − G_σ * log Ď_t),   σ = 4 px

U = bilinear upsample, G_σ = Gaussian low-pass. Set the broad structure from the layout, keep any decoder's detail. Zero fitted parameters -> applies to ANY depth source post hoc (7/7 decoders improved, no retraining).

### 6. Reliability-weighted generative detail

Rectified-flow generator (3D U-Net over space × views, FiLM conditioning) learns the residual between GT inverse depth and a rendered coarse depth D_0. Code-agreement penalty weighted by inverse readout variance:

    L = E ||v_θ(z_τ,τ,c) − (z_1−z_0)||² + λ · mean_j [ w_j (A_i(Q̂_1)_j − µ_j)² ],  λ=0.1, w_j ∝ s_j^{−2}

Train conditions on OUT-OF-FOLD posteriors so the generator sees realistic readout error, not clean targets.

### 7. Range calibration (ridge shrinkage correction)

Ridge readouts shrink spread: DRAFT cell log depths have only 0.49 of true range. Post-hoc expansion around the video's own mean (no test depth labels): log D -> m + a(log D − m), a=2 chosen by inner validation -> restores 0.97 of true spread. Linear readouts need variance de-shrinking before geometric metrics mean anything.

## Key Results (10 held-out scenes, 20 participants, leave-one-scene-out, 324 routes)

- layout r (Pearson of 3x3 cell median log depths vs ray-cast GT): DRAFT 0.480 > camera path alone 0.446 > readout-to-3x3 0.440 > trajectory head (motion only) 0.390 > best of 7 adapted fMRI decoders 0.429 > fixed template 0.324 > generator alone 0.303.
- **Plug-in**: DRAFT layout lifts all 7 decoders (linear depth, CLIP retrieval, image/depth decoding, DREAM, Brain-Diffuser, MindEye) from 0.171–0.429 to 0.487–0.493; path-only gives just 0.450–0.458.
- Brain-input controls: replacing EVC features by training means or circularly shifting BOLD by 37 s lowers layout r and F-score in ALL 10 scenes (−0.037, −0.043). Brain gain peaks at BOLD lag 3–4 s. EVC beats scene-selective OPA/PPA/RSC in 9/10 scenes.
- **Surfaces are the honest test and DRAFT does NOT win them**: unmodified MindEye (F@25cm 0.494) and Brain-Diffuser (0.492) stay slightly ahead of DRAFT (0.484); their detail comes from large pretrained image models.

## Implementation Recipe

1. Choose a task-matched compact code (here 22 numbers) and a metric that scores it directly (layout r).
2. Ridge-ensemble readout from few reliable voxels (PCs) + motion nuisance regressors; keep per-entry out-of-fold spread.
3. Build the trajectory prior: visited-position free-space distances per direction; ridge to the same 3x3 target.
4. Stack (fusion ridge) brain code + trajectory layout on out-of-fold predictions.
5. Swap fused layout into low frequencies of any decoder (σ≈4 px); keep decoder detail.
6. Calibrate range post hoc around the predicted mean; validate factor on training folds.
7. Evaluate with: fMRI-free references (fixed template, per-second median), wrong-scene reference, input controls, paired scene-bootstrap + sign-flip tests; flag post hoc analyses.

## Generalizable Patterns

- **Code-before-pixels**: when the scientific claim is about coarse structure, decode the minimal code that the claim lives in; small targets beat large pretrained decoders and stay interpretable.
- **Trajectory = free-space prior**: an agent's own path certifies where the scene is empty; a learned prior overpowers hard occupancy bounds.
- **Coarse-then-detail, output-space**: low-frequency replacement is decoder-agnostic, training-free guidance (cf. ILVR/ControlNet, but post hoc on outputs).
- **Uncertainty-weighted code agreement**: propagate readout error bars into downstream losses via inverse-variance weights; train generative models on out-of-fold (realistic-error) conditions.
- **Wrong-scene reference**: if predicting a DIFFERENT scene scores nearly as well, your metric is insensitive — report that before claiming decoding.

## Honest Limitations (from the paper)
- Needs known camera paths and pooled recordings (not single-trial); developed on these scenes with several post hoc analyses; range-calibration factor fixed after earlier results.
- Brain gain over the camera path is small (+0.035 layout r) and was NOT separable from low-level image features; replicated in only 2 of 5 withheld scenes.
- Generator detail is mostly one pattern shared across scenes (corr 0.026 with true detail); scene-specific geometry comes from the layout, not the generator.
- Surface metrics separate methods little: wrong-scene depth keeps most of the F-score (correct scene adds only 0.055–0.069); F@25cm rewards depth range, which pretrained models supply.
- A loss-coordinate bug fix weakened the generator (0.369→0.303) and DRAFT barely moved — part of the fusion gain reflects a weaker baseline, transparently reported.

## Related Skills

- [[fmri-gesture-reconstruction]] — dual brain decoding alignment for gestures
- [[mind-omni-brain-vision-language-unified]] — any-to-any brain decoding framework
- [[geometric-brain-dynamics-mapping-gbf]] — geometry-aware whole-brain mapping
- [[visual-imagery-decoding-fmri]] — latent-alignment fMRI decoding
