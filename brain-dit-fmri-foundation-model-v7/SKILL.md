---
name: brain-dit-fmri-foundation-model-v7
description: "Brain-DiT: Universal multi-state fMRI foundation model using metadata-conditioned Diffusion Transformer (DiT) pretraining. Trained on 349,898 sessions across 24 datasets spanning resting, task, naturalistic, disease, and sleep states. Diffusion-based generative pretraining outperforms reconstruction and alignment proxy tasks. Disentangles intrinsic neural dynamics from population-level variability."
version: 1.0.0
metadata:
  hermes:
    tags: [fmri, foundation-model, diffusion-transformer, DiT, brain-states, pretraining, metadata-conditioning, multi-scale-representations, neuroscience, neuroimaging, downstream-tasks, ADNI, classification, representation-learning]
  source_paper:
    title: "Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining"
    arxiv_id: "2604.12683"
    authors: "Junfeng Xia, Wenhao Ye, Xuanye Pan, Xinke Shen, Mo Wang, Quanying Liu"
    submitted: "2026-04-14"
    categories: "cs.CV, q-bio.NC"
---

# Brain-DiT: Universal Multi-state fMRI Foundation Model (v7)

## Source

**Paper:** "Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining"
**arXiv:** 2604.12683
**Authors:** Junfeng Xia, Wenhao Ye, Xuanye Pan, Xinke Shen, Mo Wang, Quanying Liu
**Submitted:** 2026-04-14
**Categories:** cs.CV, q-bio.NC

## Abstract

Current fMRI foundation models primarily rely on a limited range of brain states and mismatched pretraining tasks, restricting their ability to learn generalized representations across diverse brain states. Brain-DiT is a universal multi-state fMRI foundation model pretrained on 349,898 sessions from 24 datasets spanning resting, task, naturalistic, disease, and sleep states. Unlike prior fMRI foundation models that rely on masked reconstruction in the raw-signal-space or a latent space, Brain-DiT adopts metadata-conditioned diffusion pretraining with a Diffusion Transformer (DiT), enabling the model to learn multi-scale representations that capture both fine-grained functional structure and global semantics. Extensive evaluations and ablations on 7 downstream tasks provide consistent evidence that diffusion-based generative pretraining is a stronger proxy than reconstruction or alignment, with metadata-conditioned pretraining further improving downstream performance by disentangling intrinsic neural dynamics from population-level variability. Downstream tasks exhibit distinct preferences for representational scale: ADNI classification benefits more from global semantic representations, whereas age/sex prediction comparatively relies more on fine-grained local structure.

## Key Concepts

### Multi-State fMRI Foundation Modeling

Traditional fMRI analysis focuses on single brain states (typically resting-state). Brain-DiT addresses the fundamental limitation that representations learned from limited brain states fail to generalize. Key innovations:

- **Universal coverage:** 5 distinct brain state categories (resting, task, naturalistic, disease, sleep)
- **Scale:** 349,898 fMRI sessions — the largest multi-state fMRI pretraining corpus to date
- **Diversity:** 24 datasets with varying acquisition parameters and populations
- **Cross-state generalization:** Single model handles all brain states without task-specific fine-tuning

### Diffusion-Based Generative Pretraining

Brain-DiT's core innovation is replacing masked reconstruction (MAE-style) with **diffusion-based generative pretraining**:

- **Why diffusion > reconstruction:** Generative modeling forces the model to learn the full data distribution, not just masked positions
- **Why diffusion > alignment:** Alignment methods (e.g., CLIP-style) require paired data; diffusion works with unpaired fMRI
- **Diffusion process:** Forward process corrupts fMRI signals; reverse process learns to denoise, capturing multi-scale structure
- **DiT backbone:** Transformer architecture naturally handles variable-length fMRI time series

### Metadata-Conditioned Learning

Metadata conditioning is the key mechanism for disentangling intrinsic dynamics from population variability:

- **Metadata types:** Age, sex, dataset source, brain state category, acquisition parameters
- **Conditioning mechanism:** Metadata is embedded and used to condition the diffusion process
- **Disentanglement effect:** The model learns what varies due to metadata (population-level) vs. what varies intrinsically (neural dynamics)
- **Downstream benefit:** Removes confounds, improving transfer learning

### Multi-Scale Representations

Brain-DiT captures representations at multiple scales:

1. **Fine-grained local structure:** Region-level functional patterns, short-timescale dynamics
2. **Mid-level functional organization:** Network-level connectivity patterns, state transitions
3. **Global semantics:** Whole-brain organization, macro-scale brain state signatures

Different downstream tasks preferentially leverage different scales.

## Architecture

### Diffusion Transformer (DiT) for fMRI

The core architecture adapts the Diffusion Transformer to fMRI data:

```
Input: fMRI time series x ∈ ℝ^{T × V}
  where T = time points, V = voxels/ROIs

1. Spatial-temporal patchification:
   - Divide fMRI volume into spatiotemporal patches
   - Linear projection to embedding dimension

2. Transformer encoder blocks:
   - Multi-head self-attention over patches
   - MLP with GELU activation
   - LayerNorm + residual connections

3. Metadata conditioning:
   - Metadata m embedded via MLP
   - Injected via adaptive layer norm (adaLN)
   - Conditions attention and MLP at each block

4. Diffusion head:
   - Predicts noise at each diffusion timestep
   - Output: denoised fMRI prediction
```

### Key Architectural Details

- **Patchification strategy:** Spatiotemporal patches capturing local brain regions over short time windows
- **Transformer depth:** Multiple layers enabling hierarchical feature extraction
- **Adaptive Layer Normalization (adaLN):** Metadata conditioning mechanism that modulates layer activations
- **Diffusion timestep embedding:** Sinusoidal encoding of diffusion timestep t
- **Output prediction:** Noise prediction (ε-prediction) for the denoising objective

### Metadata Conditioning Mechanism

```
adaLN(x, m, t) = γ₁(m, t) * LayerNorm(x) + β₁(m, t)

Where:
- m = metadata embedding (age, sex, dataset, brain state, etc.)
- t = diffusion timestep embedding
- γ₁, β₁ = learned scale and shift parameters
```

This mechanism allows the model to:
1. Condition generation on known metadata
2. Remove metadata-related variance from learned representations
3. Generate brain-state-specific fMRI patterns

## Pretraining Strategy

### Data Curation

**Scale:** 349,898 fMRI sessions from 24 datasets

**Brain state categories:**
| Category | Description | Example Datasets |
|----------|-------------|-----------------|
| Resting | Eyes-open/closed resting state | HCP, UK Biobank |
| Task | Cognitive/motor tasks | HCP Task, Midnight Scan Club |
| Naturalistic | Movie watching, story listening | Study Forrest, Courtois NeuroMod |
| Disease | Clinical populations | ADNI, ABIDE, UK Biobank (clinical) |
| Sleep | Sleep stages | Sleep fMRI datasets |

### Pretraining Objective

**Forward diffusion process:**
```
q(x_t | x_0) = N(x_t; √ᾱ_t x_0, (1 - ᾱ_t)I)

Where x_0 = original fMRI signal, x_t = noised version at timestep t
```

**Reverse process (training objective):**
```
L = E_{x_0, t, ε} [||ε - ε_θ(x_t, t, m)||²]

Where:
- ε = true noise added at timestep t
- ε_θ = model's noise prediction (DiT with metadata conditioning)
- m = metadata conditioning vector
```

### Why Diffusion Pretraining Works for fMRI

1. **Distribution learning:** Diffusion models learn the full data distribution, not just local reconstruction targets
2. **Multi-scale capture:** The diffusion process naturally operates at multiple noise levels, capturing structure at each scale
3. **Noise schedule alignment:** Clean → noisy diffusion process aligns with the signal → noise hierarchy in fMRI
4. **No masking artifacts:** Avoids the artificial masking patterns of MAE-style methods that may bias representations

### Comparison with Alternative Proxy Tasks

| Proxy Task | Mechanism | Limitation |
|------------|-----------|------------|
| Masked Reconstruction (MAE) | Reconstruct masked brain signals | Only learns local structure; masking artifacts |
| Contrastive Alignment | Align paired views/modalities | Requires paired data; limited diversity |
| **Diffusion (Brain-DiT)** | **Generative denoising** | **Learns full distribution; multi-scale; no masking needed** |

## Evaluation

### 7 Downstream Tasks

Brain-DiT was evaluated across 7 diverse downstream tasks:

1. **ADNI Classification** — Alzheimer's disease detection from fMRI
2. **Age Prediction** — Chronological age regression from brain activity
3. **Sex Prediction** — Binary sex classification from fMRI
4. **Brain State Decoding** — Classifying cognitive state during task fMRI
5. **Functional Connectivity Prediction** — Predicting connectivity matrices
6. **Disease Phenotyping** — Multi-disease classification across clinical datasets
7. **Sleep Stage Classification** — Staging sleep from fMRI dynamics

### Performance Highlights

- **Consistent improvement** over MAE-based and contrastive fMRI foundation models
- **Metadata conditioning** provides measurable gains across all tasks
- **Diffusion pretraining** outperforms reconstruction and alignment baselines

### Scale Preferences Discovery

A key finding is that **different downstream tasks prefer different representational scales:**

| Task | Preferred Scale | Interpretation |
|------|----------------|---------------|
| ADNI Classification | **Global semantics** | Alzheimer's affects whole-brain organization |
| Age Prediction | **Fine-grained local** | Aging manifests in region-specific patterns |
| Sex Prediction | **Fine-grained local** | Sex differences are region-level |
| Brain State Decoding | **Multi-scale** | Cognitive states involve multiple scales |
| Disease Phenotyping | **Global semantics** | Clinical conditions affect large-scale networks |

**Implication:** Foundation model representations should capture multiple scales, and downstream heads should select appropriate scales.

### Ablation Studies

Key ablations confirming design choices:

1. **Diffusion vs. MAE vs. Contrastive:** Diffusion consistently wins
2. **Metadata conditioning:** Removing metadata degrades all tasks
3. **Multi-state pretraining:** Single-state models underperform multi-state
4. **Scale of pretraining data:** More sessions → better representations
5. **DiT vs. U-Net backbone:** DiT better captures long-range temporal dependencies

## Key Findings

### Primary Findings

1. **Diffusion-based generative pretraining is the strongest proxy task** for fMRI foundation models, outperforming both masked reconstruction and contrastive alignment approaches.

2. **Metadata-conditioned pretraining disentangles intrinsic neural dynamics from population-level variability**, improving downstream performance by removing confounding factors.

3. **Multi-state pretraining is essential** — models trained on diverse brain states learn more generalizable representations than single-state models.

4. **Downstream tasks exhibit distinct scale preferences:**
   - Disease classification (ADNI) benefits from **global semantic representations**
   - Demographic prediction (age/sex) relies on **fine-grained local structure**
   - This has implications for feature extraction strategies in fMRI analysis

5. **Scale matters:** 349,898 sessions across 24 datasets provides substantially better representations than smaller-scale pretraining.

### Practical Implications

- **For fMRI analysis:** Brain-DiT representations can serve as universal feature extractors
- **For clinical applications:** Global semantic representations are most informative for disease detection
- **For cognitive neuroscience:** Multi-scale representations capture both local and network-level phenomena
- **For data collection:** Diverse brain state coverage is more important than sheer volume of a single state

## Activation Keywords

`fmri`, `foundation model`, `diffusion transformer`, `DiT`, `brain states`, `pretraining`, `metadata conditioning`, `multi-scale representations`, `ADNI`, `age prediction`, `sex prediction`, `resting state`, `task fMRI`, `naturalistic`, `sleep`, `disease classification`, `representation learning`, `generative pretraining`, `brain-DiT`

## References

1. Xia, J., Ye, W., Pan, X., Shen, X., Wang, M., & Liu, Q. (2026). Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining. arXiv:2604.12683
2. Peebles, W., & Xie, S. (2023). Scalable Diffusion Models with Transformers (DiT). ICCV 2023.
3. He, K., et al. (2022). Masked Autoencoders Are Scalable Vision Learners. CVPR 2022.
4. Dosovitskiy, A., et al. (2021). An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale. ICLR 2021.
5. Thomas, A. W., et al. (2023). BRAID: fMRI foundation model. Nature Methods (related prior work).
6. Ho, J., Jain, A., & Abbeel, P. (2020). Denoising Diffusion Probabilistic Models. NeurIPS 2020.
7. Van Essen, D. C., et al. (2013). The Human Connectome Project. NeuroImage.
