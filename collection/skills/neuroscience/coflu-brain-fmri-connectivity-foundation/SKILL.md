---
description: Use when pretraining models on fMRI connectivity views.
name: coflu-brain-fmri-connectivity-foundation
category: ai_collection
trigger_words: fMRI foundation model, functional connectivity pretraining, cofluctuation, retained-dropped FC views, brain network representation, self-supervised fMRI
---

# CoFlu-Brain: Cofluctuation-Based fMRI Connectivity Foundation Model

**Source**: arXiv:2610.15450 (Sui, Xia, Ye, Wang, Liu — 11 Oct 2026)

## Core Insight

An observed FC matrix is a finite-sample statistical estimate determined by its supporting BOLD frames — not a fixed brain graph. CoFlu-Brain makes this explicit: it decomposes Pearson FC into framewise cofluctuation matrices E_t = z_t z_t^T, then builds multiple related FC views from different frame subsets, turning FC estimation variance into a self-supervised signal.

## View Construction (the reusable pattern)

For each fMRI segment (200 frames, Schaefer-400 atlas):
1. For frame subset A: standardize each regional signal within A → framewise cofluctuation E_t^A = z_t^A (z_t^A)^T
2. FC view: R_ij^A = (1/(|A|-1)) Σ_{t∈A} E_t,ij^A, Fisher-transform off-diagonal, zero diagonal
3. Per partition v: sample retained set S_v (proportion r_v) without replacement; dropped set D_v = complement (disjoint within pair)
4. V independently sampled partitions per scan → V retained/dropped view pairs

## Architecture & Objective

- **Encoder**: row-wise MLP φ maps each ROI connectivity profile c_i to a token; ViT contextualizes N ROI tokens; mean-pool to scan-level representation f_θ(C)
- Shared encoder+projector g on BOTH retained and dropped views; predictor h maps retained projection to predict dropped projection
- Three complementary losses:
  1. **Consistency**: align representations across retained views (different frame compositions of same scan)
  2. **Prediction** (JEPA-style latent): retained → dropped prediction captures information predictive of held-out frames
  3. **SIGReg**: distributional regularization against representation collapse
- After pretraining: discard projector + predictor, frozen encoder for linear probing

## Pretraining & Results

- 13,444 subjects, 8 datasets (CHCP, HCP, ABCD, ABCC, HBN, PNC, MDD, AOMIC); no downstream labels
- Evaluation: 2 in-cohort (HCP/ABCD sex) + 7 out-of-cohort tasks (PPMI 3-class, ADNI AD/MCI, ABIDE ASD, ADHD200 diagnosis+age, SALD age)
- **Led 8 of 9 tasks** vs BrainGFM/BrainMASS/BrainLM/LCM; cohort-averaged rank 1.14 (permutation p<0.001)
- Highlights: HCP sex 77.5% acc; SALD age nMAE 0.657 / r=0.64; ADHD200 age r=0.60 (next best 0.44)

## Ablation Findings (what matters)

- **Objective components** (rank): Full 1.50 > No consistency 1.79 > No SIGReg 3.14 > No prediction 3.57 — prediction and SIGReg are critical; consistency helps some tasks
- **Random vs ordered partitioning**: random wins across all 7 cohorts (sign test p=0.016) — sample frames throughout the sequence, don't take contiguous blocks
- **Branch count**: 4 retained/dropped pairs optimal; 8 branches double GPU cost (10.54→26.72 h) with no gain
- **Retained ratio**: 0.4–0.7 sampled per partition
- **Consistency schedule**: Decay-25 (emphasize consistency early, prediction later) best for classification; constant best for age
- **Data coverage**: 100% manifest beats 12.5% on all tasks

## Interpretability

Network-restricted probing (Yeo-17): replace non-network FC with probe-training means, keep within-network FC. Default-network components dominate both age and ADHD prediction (consistent with maturation literature); salience/ventral-attention joins for diagnosis. Rankings consistent across seeds (ρ=0.906 age, ρ=0.857 diagnosis).

## Why It Works (mechanism)

Consistency across retained estimates → stability under frame resampling. Retained→dropped prediction → representations predictive of complementary, unseen evidence. SIGReg → diversity. All three map directly onto the finite-sample structure of FC estimation. This generalizes "augmentation = view construction" to statistical estimators: any finite-sample estimate (FC, covariance, spectra) can be turned into a view-family by subsampling its supporting observations.

## Limitations

- Aggregating framewise products loses timing/order/amplitude information (views are set-based summaries)
- Schaefer-400 fixed parcellation; single 200-frame window granularity
- In-cohort tasks may benefit from pretraining exposure

## Relations

- Family: BrainGFM, BrainMASS, BrainLM, LCM (FC/graph fMRI foundation models) — CoFlu-Brain beats all with linear probing
- Method ancestry: BYOL/DINO (consistency), JEPA/I-JEPA (latent prediction), VICReg/SIGReg (collapse prevention)
- Neuro foundation: Zamani Esfahlani 2020 (cofluctuation drives FC), Faskowitz 2020 (edge-centric)
