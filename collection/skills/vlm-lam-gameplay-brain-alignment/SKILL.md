---
name: vlm-lam-gameplay-brain-alignment
description: Use when aligning VLM or large-action-model representations with fMRI during interactive gameplay.
category: ai_collection
trigger_words: VLM brain alignment, LAM, large-action model, Atari gameplay fMRI, voxel-wise encoding, variance partitioning, action prompt, reasoning prompt, naturalistic gameplay, world models, frontal-parietal encoding, prompt-driven alignment gain
metadata:
  arxiv_id: "2605.19352"
  published: "2026-05-19 (v2: 2026-10-07)"
  authors: "Subba Reddy Oota, Anant Khandelwal, Khushbu Pahwa, Satya Sai Srinath Namburi, Tanmoy Chakraborty, Bapi S. Raju, Manish Gupta"
  tags: [brain-alignment, fMRI-encoding, vision-language-models, large-action-models, variance-partitioning, naturalistic-gameplay, world-models]
---

# VLM/LAM Brain Alignment During Naturalistic Gameplay (arXiv 2605.19352)

Oota et al. (MSR/AWS/IIT-Delhi/IIIT-H), "Brain alignment of reasoning and action representations from vision-language and action models during naturalistic gameplay" — first systematic brain-encoding evaluation of **vision-language models (VLMs)** and **large-action models (LAMs)** on interactive gameplay fMRI (32 subjects playing Atari-style games, Tomov et al. 2023 dataset), extending brain alignment from passive perception/language to interactive decision-making.

## Experimental Design

**Data**: 32 participants × 6 Atari-style games × 6 runs (566s each, TR=2s, 283 timepoints/run), fMRIPrep v25.2.0, surface-projected, Glasser-atlas ROIs grouped as early-visual (CAL/CUN/LING), higher-visual (SOG/IOG/MOG), higher-order frontal-parietal+motor (AG, IFGtriang, IFGoperc, MFG, SMA).

**Models** (2+2 with matched-backbone contrast):
- VLMs: Qwen2.5-VL-7B-Instruct, InternVL3-8B (28 layers, dim 3584)
- LAMs: UI-TARS-7B-DPO, OS-Atlas-Pro-7B — both fine-tuned from the SAME Qwen2-VL backbone (SFT+DPO on ~50B GUI/game-interaction tokens), isolating action-affordance supervision while holding architecture fixed.
- Thinking-mode probe: Qwen3.5 (explicit CoT traces) — reasoning-trace vs final-answer readouts.
- RL baselines: EMPA (theory-based: 8 per-frame regressors incl. surprise, spriteKL, R_GG) and DDQN (25M-step agent action distributions).

**Feature extraction (the transferable recipe)**:
1. Per fMRI TR (2s ≈ 40 game frames @ 20 FPS), sample k=4 frames evenly from the LAST ~1.5s of the TR (≈0.5s spacing) — window ends at TR boundary, never crosses runs.
2. Pass 4 frames as a multi-image sequence + text prompt through `model.generate()` (greedy), extract last-token hidden state at EVERY layer → E_t ∈ R^(L+1)×d per TR.
3. Prompt battery: **action prompt** (commit to next action + justify) vs **reasoning prompt** (analyze objects/spatial/threats step-by-step, then act) vs no-prompt; plus 7 controls (scrambled-neutral, scrambled, lowlevel, scene, goal, action-bare, action-full).
4. Voxel-wise encoding: bootstrap ridge regression, z-scored features/responses, 4 hemodynamic lags (2/4/6/8s concatenated), per-layer fit with best-layer reporting, strict leave-one-run-out CV per subject.

**Variance partitioning** (the key analysis): decompose explained brain variance into shared (action∩reasoning) + unique-action u_A + unique-reasoning u_R, per model, per ROI.

## Four Key Findings

1. **VLMs/LAMs >> RL baselines** in voxel-wise encoding (EMPA r=.013, DDQN r=.005 vs substantially higher), **even at matched feature dimensionality** (8/64/1024-dim PCA; 8→64 significant, 64→1024 saturated) — multimodal foundation-model representations carry more brain-relevant game-state information than task-optimized RL policies.

2. **Prompt gains are regionally graded**: prompting (vs no-prompt) improves alignment in 10-11/11 ROIs, with gains in higher-order cortex 2–2.5× early-visual gains (VLM: +0.012 group Δ, q=.019; LAM: +0.020, q=.039). Largest single-ROI gains: LAM SMA +0.057, IOG +0.059, MFG +0.042. Layer-wise: visual ROIs peak early (L4/L7), motor/prefrontal at intermediate-deep layers (L18–L21) — consistent with a ventral→dorsal/abstract hierarchy. Interpretation: prompts engage goal/planning/decision representations (multiple-demand network), not just language.

3. **Equal accuracy, different organization (the headline dissociation)**: whole-brain accuracy does NOT differ significantly between VLM and LAM at matched prompts — but variance partitioning reveals:
   - **VLM prompt-symmetric**: u_A=12.4% vs u_R=9.5% unique variance (p=.75), shared 78.1%
   - **LAM action-dominant**: u_A=25.6% vs u_R=−8.2% (p=.032), shared 82.4%; reasoning becomes REDUNDANT given action representations
   - Regionally: AG (LAM u_A=24% vs u_R=−8%); SMA strongest (u_A=34%, u_R=−14% — one-third of explainable variance is action-unique)
   - Replicates on the second pair (InternVL3 vs OS-Atlas-Pro): OS-Atlas u_A=.0102 vs u_R=.002; InternVL3 ~symmetric.
   - Voxel-wise maps: VLM r_Reasoning>r_Action across dorsal stream/lateral occipital; LAM widespread action-dominant voxels in early visual + ventral stream.
   - **Methodological lesson: raw encoding accuracy masks representational reorganization — variance decomposition is required to see it.** Action fine-tuning reshapes what the model encodes (action-associated cortical alignment) without changing how well it predicts.

4. **CoT reasoning traces align WORSE**: Qwen3.5 last-token reasoning-trace readout r=.012 vs final-answer readout r=.031 (p=.032); mean-pooling over the reasoning span recovers r=.036. Explicit chain-of-thought does not automatically improve brain alignment — readout granularity matters.

## Reusable Protocol

**When to use**: any study aligning foundation-model internals with brain activity during interactive/naturalistic tasks; auditing what action-tuning does to representations; designing prompt batteries for encoding studies.

**Core pipeline**:
- TR-aligned frame windows (k=4, trailing 1.5s) → multi-image + prompt → per-layer last-token embeddings → ridge encoding with hemodynamic lags → LORO CV → layer profiles.
- Report: (a) unthresholded full-voxel means, (b) ROI-group contrasts (higher-order vs early-visual) on prompt GAINS Δr = r_prompted − r_no-prompt (not absolute r), (c) variance partitioning on prompt sets.
- Dimensionality-matched baselines (PCA to 8/64/1024) to separate "more features" from "better features".
- Nine-condition prompt battery distinguishes: syntax (scrambled variants), low-level vs scene vs goal content, and motor commitment (action-bare vs action-full).

**FDR + paired t-tests across participants** for all ROI comparisons; report layer-wise profiles to show conclusions don't hinge on best-layer selection (which is slightly optimistic by construction).

## Applications

1. **Agent-brain alignment audits**: variance partitioning as the standard diagnostic for whether fine-tuning (RLHF, action-tuning, tool-use training) reorganizes representations toward specific cortical systems — invisible to benchmark accuracy.
2. **World-model probing**: the action-vs-reasoning prompt contrast operationalizes "understanding the environment" vs "committing to action" — a reusable dissociation assay for whether models acquire structured world models.
3. **Prompt design for encoding studies**: goal/action content drives frontal-parietal alignment; scene-only content does not — prompts are not neutral, they select which cortical systems a model's features predict.
4. **CoT evaluation**: reasoning-trace readouts need mean-pooling or span-level treatment; last-token trace embeddings under-represent brain-relevant content.

## Limitations (from paper)

- Best-layer selection uses held-out scores (slightly optimistic; mitigated by full layer profiles).
- Absolute alignment values are modest (r ~0.03–0.06 voxel means) — typical for naturalistic encoding but limits fine-grained claims.
- Prompt effects may include language-network confounds; the 9-condition battery controls for this but cannot fully separate multiple-demand from language activity.
- Two VLMs and two LAMs — generalization beyond Qwen-family backbones partially tested (InternVL3/OS-Atlas).

## References

- Paper: arXiv 2605.19352v2 (7 Oct 2026). Dataset: Tomov et al. 2023 naturalistic Atari fMRI (public BIDS).
- Encoding methodology: Toneva & Wehbe 2019 (lags); Jain & Huth 2018 (PCC); LeBel et al. 2021 / de Heer et al. 2017 (variance partitioning); Glasser et al. 2016 (parcellation).
- Related in collection: [[lrm-game-learning-brain-alignment]] (behavioral+brain alignment of large reasoning models), [[braid-fmri-cross-dataset-clip-decoding]], [[generative-priors-naturalness-alignment]] (generative-loss-side of human alignment), [[vlm-brain-alignment-task-probing]] (task-conditioned probing).
