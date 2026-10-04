---
name: future-video-generation-visual-cortex-alignment
description: "AR video diffusion future-generation representations align better with visual cortex than observed video; predictive-brain mapping method."
category: ai_collection
tags: [neuroscience, brain-alignment, video-diffusion, predictive-coding, fmri-encoding, autoregressive-models, representational-alignment]
arxiv_id: 2609.38819
paper_title: "Future Video Generation Better Aligns with the Human Visual Cortex than Observed Video"
paper_url: https://arxiv.org/abs/2609.38819
authors: "Chang-Bae Bang, Hyungjin Chung, Byung-Hoon Kim"
published: 2026-09-30
---

# Future Video Generation Aligns Better with Visual Cortex than Observed Video

Methodology from arXiv:2609.38819 (Yonsei University / Korea University, 2026): the internal representation an **autoregressive (AR) video diffusion model** uses to GENERATE the future aligns better with human visual cortex (fMRI) than the representation of the observed video itself — direct representational evidence that visual cortex performs **future-oriented computation**, strongest in higher-order areas.

## Core Methodology

### 1. Three-Representation Comparison Design
Map three model representations onto vertex-wise fMRI (BOLD Moments Dataset, 10 subjects, 1102 3-s naturalistic videos) and let variance partitioning arbitrate:

| Representation | Source | What it captures |
|---|---|---|
| `X_obs` = c_obs | AR model's clean observed-video token embedding | passive stimulus encoding |
| `X_fut` = H^{fut}_{s,b} | AR model's **future-token** activations at denoising step s, layer b | prediction of upcoming frames |
| `X_rec` = H^{rec}_{s,b} | non-AR base model (Wan-2.1) reconstructing the observed video | denoising/reconstruction pathway |

- AR models: helios-base-v2v (40-layer, fine-tuned from Wan-2.1 T2V-14B); replication on Self-Forcing & CausVid (30-layer, from Wan-2.1 T2V-1.3B).
- AR input sequence carries observed tokens clean + future tokens at noise level σ_s; extract FUTURE token block only.

### 2. Vertex-Wise Encoding Pipeline
1. Flatten each representation per video → sparse random projection to d=6004 dims.
2. Ridge regression per cortical vertex (HCP-MMP atlas; Visual System = 7894 vertices in 5 divisions: Primary Visual, Early Visual, Dorsal, Ventral, MT+).
3. Noise-normalized accuracy: R̃²_p = R²_p / NC_p (NC = noise ceiling per vertex; only vertices NC>10% analyzed).
4. Nested CV selects ridge penalty AND best (step, layer) cell on training folds only.
5. Variance partitioning (stacked regression): U_a = R̃²_stack − R̃²_b, U_b = R̃²_stack − R̃²_a, U_ab = R̃²_a + R̃²_b − R̃²_stack.

### 3. Key Results
- **Within-model**: future-generation unique contribution beats observed-video unique contribution in every division (p=0.002); observed video adds NO unique contribution beyond future generation (Appendix). In Visual System: U_fut=0.222, shared=0.111, U_obs=−0.006.
- **Cross-model**: future generation (best 0.334 at step 0, layer 11) beats observed reconstruction (0.301 at step 16, layer 8); gap widens up the hierarchy — MT+ 0.436 vs 0.363, Ventral 0.396 vs 0.329.
- **Step profile**: future generation peaks at the NOISIEST step (s=0) and decays monotonically — the uncommitted prior-over-futures state aligns best (consistent with probabilistic/Bayesian neural coding); reconstruction peaks mid-schedule (fine detail refinement).
- **Layer profile**: both follow an inverted U peaking at early-to-middle layers.
- **Behavioral validation**: Spatiotemporal Skip Guidance (STG) amplifies one layer b∈{0,5,11,16,22,28,32,38} during generation; human preference (720 A/B trials, Bradley–Terry) correlates with layer-wise encoding accuracy at r=0.75 (p=0.029). Humans prefer videos from amplifying well-aligned layers.

## Implementation Recipe

```python
# 1. Extract future-token activations from an AR video diffusion model
#    input = [patch(z_obs) clean; patch(z_fut at σ_s)]  → split layer output:
H_fut = model.forward(z_obs, z_fut_noisy)[:, n_obs_tokens:]  # future block
# 2. Grid over denoising steps × layers; select best cell on TRAIN folds only
# 3. Sparse random projection → 6004 dims; per-vertex ridge with nested-CV penalty
# 4. Variance partition future vs observed/reconstruction:
U_fut = R2_stack - R2_other;  U_other = R2_stack - R2_fut
```

## When to Use
- Brain-aligning generative video models; choosing which denoising step/layer to read out
- Testing whether a model's PREDICTIVE (not receptive) representations match cortex
- Layer-amplification (STG) guidance validated by neural alignment → human preference
- Designing encoding studies on BOLD Moments / naturalistic video fMRI

## Related Skills
- [[cross-attention-video-encoding]] — video fMRI encoding via joint spatiotemporal attention
- [[brain-alignment-causal-dissociation-attention-heads]] — testing causal importance of aligned heads
- [[sensory-aligned-receptive-fields-expressivity]] — task-aligned RFs as computational prior

## Citation
Bang, C.-B., Chung, H., & Kim, B.-H. (2026). Future Video Generation Better Aligns with the Human Visual Cortex than Observed Video. arXiv:2609.38819.
