---
name: generative-priors-naturalness-alignment
description: Use when probing whether visual generative models encode human perceptual priors via native loss differences.
category: ai_collection
trigger_words: generative priors, naturalness perception, Thatcher effect, paired relational intervention, directional loss difference, native prediction error, denoising loss, image naturalness, psychophysics of generative models, diffusion loss landscape
metadata:
  arxiv_id: "2610.09928"
  published: "2026-10-07"
  authors: "Taiki Fukiage (NTT Communication Science Laboratories)"
  tags: [naturalness-perception, generative-models, psychophysics, thatcher-effect, diffusion-models, brain-alignment, iq-a]
---

# Generative Priors Align with Human Naturalness Perception (arXiv 2610.09928)

Fukiage (NTT), "Do Generative Priors Align with Human Naturalness Perception?" — tests whether the **native prediction losses** of 25 open image/video generators (SD v1.5/XL/3, FLUX.1/2, Qwen-Image, JiT, PixelGen, HiDream, CogVideoX, LTX-Video, Wan2.1/2.2, HunyuanVideo) directly encode human naturalness judgments — zero-shot, no feature readouts, no supervised heads.

## Core Method: Paired Directional Loss Difference (PDLD)

Raw single-image generative losses fail as naturalness measures (density confounds: complexity, background statistics, manifold geometry — Nalisnick/Serrà/Kamkari). The fix is **content-preserving relational interventions + paired subtraction**:

1. **Intervene, don't corrupt**: rearrange EXISTING image content in place (flip eyes/mouth via facial landmarks; mirror floor region to swap shadows/reflections; mirror central object for light direction). Color histograms and edge content stay ~intact — no object insertion/deletion.
2. **Directional score**: `u_{m,i} = L_m(x_i^mod) − L_m(x_i^orig)` where `L_m(x) = mean over t∈T_m, ε∈E_m of ℓ_m(x,t,ε)` (aggregate 100 timesteps × 20 noise draws for image models; 50 × 20 for video). Positive u = model penalizes the relational violation.
3. **Standardize per task**: `ũ_{m,i} = u_{m,i}/s_{m,task}` (divide by task-wide sample SD, N−1 dof) so models and human ratings share a scale. Human counterpart: `h_i = R(x_orig) − R(x_mod)` from 5-point naturalness ratings (143 observers Thatcher, 105 Illumination; ~35/26 ratings/item).
4. **Alignment metric**: item-level Pearson `r_m = corr_i(u_{m,i}, h_i)`.

Why paired subtraction is essential: unconditioned single-image losses `L_m(x)` correlate near zero with human unnaturalness (25-model medians −.20 to .24), while paired differences reach **r=.841 (Thatcher faces, SD v1.5) / .639 (Illumination, Wan2.1 14B)**. Condition-centering (subtract condition means) preserves positive correlation for ALL 25 models — item-level ranking within conditions is real signal, not condition-mean artifacts.

## Key Empirical Findings

- **Thatcher effect reproduced in loss landscape**: upright feature inversions penalized 2.44σ (top-5 median) vs 0.91 inverted; humans 2.73 vs 1.09. Orientation dependence emerges without face-specific training — ImageNet-only JiT scales alignment with capacity (r=.577 for JiT-H/32).
- **Geometric selectivity in illumination**: models penalize shadow rotations for directionally-landmarked objects (teapot) but tolerate them for symmetric shapes (Spot) — mirroring human perceptual heuristics (Casati copycat solution), NOT strict physical simulation.
- **Beats all baselines**: top-5 generative median r=.816 vs .660 for best-layer-optimized frozen encoders (CLIP, DINOv2/v3, SigLIP2, PE-Core, Qwen3-VL-Embed); NR-IQA ~.09/.009 (near zero — rules out generic-artifact explanations); FR-IQA .103/.254 (rules out low-level change magnitude).
- **Non-redundant signal**: bidirectional partial correlations — generative scores retain r(h,G|X)=.676 (Thatcher) after controlling for best encoders; encoders retain only .130. Complementary on Illumination (.510 vs .375); encoders win only on surface reflections.
- **Spatial maps**: paired pixel-level prediction-error maps concentrate on manipulated regions (inverted eyes/mouth) but also propagate contextually (floor→objects above altered shadows; central object→unmodified flankers) — models evaluate scene-wide relational consistency, not local patches.
- **Sensitivity ≠ alignment (dissociation)**: coarse violation sensitivity S_m covaries with alignment across models (r=.663/.821) BUT decouples along denoising schedules — alignment peaks EARLIER than sensitivity in 20/25 (Thatcher) and 25/25 (Illumination) models; median peak shift 0.141/0.444 of normalized schedule. Interpretation: human-aligned relational structure resolves at intermediate noise levels (global layout), late steps add detail-driven loss inflation without perceptual refinement. Divergence case: reflection hue shifts — humans strongly penalize, models weakly respond; larger models grow MORE sensitive to reflection violations WITHOUT improving human alignment.
- **Practical link**: model-level alignment correlates with generation benchmarks (Illumination image ρ=.827 with human-preference Elo; video ρ=.929/.821 with VBench Quality), surviving control for sensitivity (partial ρ .670–.900). Alignment, not sensitivity, is the benchmark-predictive component.

## Reusable Protocol (for replication/extension)

**Stimulus generation** — two domains, ~570 pairs:
- Thatcher: 140 FFHQ faces × {upright, inverted}, landmark-guided vertical reflection of eye/mouth regions (dlib 68-landmark), 280 pairs.
- Illumination: 96 Kubric-rendered scenes × {cast-shadow, reflection, light-direction} (mirror floor or central object), 288 pairs. Vary geometry/orientation/color/material/lighting for graded difficulty.

**Model scoring** (per model m):
- Neutral/empty-prompt single pass, no CFG (prompt content doesn't change findings — Appendix O).
- Static frames→17-frame clips for video models (21 for CogVideoX1.5 patching).
- `L_m(x)` = mean native loss (denoising MSE or flow-matching velocity loss) over stored timesteps × 20 noise draws.
- Paired difference per item; standardize by task-wide SD; correlate with item-mean human unnaturalness.

**Statistical machinery**: 10,000 participant-and-scene bootstrap for CIs; cluster bootstrap over model families for cross-model correlations; condition-centering robustness; bidirectional partial correlations vs. encoder/IQA baselines; independent-noise-draw replication (sensitivity and alignment estimated from disjoint ε draws — Appendix P kills the shared-MC-error worry).

**Schedule-resolved probing**: compute alignment r and sensitivity separately per normalized schedule position (0→1); peak locations dissociate. This is the paper's cleanest diagnostic that "violation detection" and "human-like judgment" are different model properties.

## Applications

1. **Perceptual-IQA without training**: PDLD is a zero-shot naturalness probe — useful when no supervised head or rating data exists for a new distortion type; strictly more human-aligned than NR-IQA on relational violations.
2. **Model selection / scaling audit**: use alignment-vs-sensitivity dissociation to audit whether scaling/post-training moves models toward human perceptual structure or mere violation hypersensitivity (reflections: the failure mode).
3. **Neuro-AI convergence tracking**: repeat the paradigm as models evolve — the framework explicitly positions itself as a longitudinal convergence/divergence assay between generative and biological vision.
4. **Cognitive-science probe**: generative losses as an empirical surrogate for "internal distributional prior" in Bayesian-perception accounts (Yuille & Kersten) — testable alternative to explicit inverse-graphics models.

## Limitations (from paper)

- Controlled interventions sacrifice scene diversity; extension to unconstrained imagery risks reintroducing low-level confounds.
- Off-the-shelf models confound objective/architecture/scale/post-training; cannot attribute alignment to the generative objective alone.
- Benchmark correlations are observational; no causal test that optimizing human-aligned relational priors improves generation.

## References

- Paper: arXiv 2610.09928 (7 Oct 2026); code/data/stimuli: `github.com/t-fukiage/generative-priors-naturalness`
- Clark & Jaini 2023 (text-to-image models are zero-shot classifiers); Nalisnick et al. 2019 (OOD likelihood pathology); Thompson 1980 (Thatcher illusion); Nightingale et al. 2019 (illumination insensitivity); Sclocchi et al. 2025 (coarse-to-fine diffusion dynamics).
- Related in collection: [[flyhash-connectome-lsh-test]], [[connectome-only-message-passing-fly-vision]] (connectome-vs-statistics questions), [[braid-fmri-cross-dataset-clip-decoding]] (brain alignment via decoders).
