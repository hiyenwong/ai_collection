---
name: vlm-lam-brain-alignment
description: "VLM/LAM brain alignment during naturalistic gameplay. Brain alignment of reasoning and action representations from vision-language and action models. Triggers: VLM brain alignment, LAM brain alignment, naturalistic gameplay, neural representation alignment."
---

# VLM/LAM Brain Alignment During Naturalistic Gameplay

**Reference Paper:** [2605.19352](https://arxiv.org/abs/2605.19352) — *Brain alignment of reasoning and action representations from vision-language and action models during naturalistic gameplay*
**Authors:** Subba Reddy Oota, Anant Khandelwal, Khushbu Pahwa, Satya Sai Srinath Namburi, Tanmoy Chakraborty, Bapi S. Raju, Manish Gupta
**Published:** 19 May 2026 · 21 pages, 11 figures
**Subjects:** Neurons and Cognition (q-bio.NC); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

---

## Overview

This paper studies **brain alignment** of foundation models — specifically **Vision-Language Models (VLMs)** and **Large-Action Models (LAMs)** — using fMRI recordings from human participants playing naturalistic Atari-style video games. It addresses a gap in brain-encoding research: prior work focuses on passive tasks (language comprehension, static visual processing) or reinforcement-learning (RL) agents, but not on modern foundation models during interactive gameplay.

**Key finding:** Action-specialized fine-tuning reorganizes multimodal representations toward action-relevant neural computations, even when whole-brain prediction accuracy is statistically equivalent between VLM and LAM.

---

## Methodology

### Experimental Paradigm

| Component | Description |
|---|---|
| **Stimuli** | Naturalistic Atari-style video games |
| **Recording** | fMRI (whole-brain) from human participants during gameplay |
| **Models compared** | VLMs (vision-language), LAMs (large-action), RL baselines |
| **Prompt conditions** | Action-focused prompts vs. reasoning-focused prompts |

### Brain-Encoding Framework

The study uses a **voxel-wise encoding model** approach:

1. **Feature extraction:** Pass gameplay frames (and game state) through VLMs and LAMs with different prompts to extract internal representations (activations from intermediate layers)
2. **Temporal alignment:** Synchronize model features with fMRI time series (accounting for hemodynamic response function)
3. **Ridge regression:** Train per-voxel linear encoders mapping model features → fMRI BOLD signal
4. **Cross-validation:** Split data into train/test folds; evaluate prediction accuracy (e.g., Pearson correlation) on held-out data
5. **Dimensionality matching:** Control experiments with matched feature dimensionality to ensure fair comparison

### Key Analyses

#### 1. Voxel-wise Encoding Performance

Compare encoding performance (predictive accuracy per voxel) across model families:
- **VLM** vs. **LAM** vs. **RL baselines**
- Tested under both **matched** and **unmatched** feature dimensionality
- Statistical significance assessed across participants

#### 2. Cortical Hierarchy Analysis

Examine how encoding gains distribute across the cortical processing hierarchy:
- **Early visual cortex** (V1–V4): lower-level visual processing
- **Frontal-parietal regions**: higher-level reasoning and planning
- **Motor-planning regions**: action preparation and execution

**Finding:** Prompt-driven gains scale with cortical hierarchy — largest improvements in frontal-parietal and motor-planning regions; early visual cortex gains roughly half as much.

#### 3. Variance Partitioning

Decompose representational overlap between action and reasoning conditions:

| Model | Unique Action (%) | Unique Reasoning (%) | Pattern |
|---|---|---|---|
| **VLM** | 12.5% | 13.6% | Prompt-symmetric |
| **LAM** | 27.0% | -5.0% | Prompt-asymmetric |

- **VLM is prompt-symmetric:** action and reasoning prompts each capture unique variance (~equal)
- **LAM is prompt-asymmetric:** action prompt captures substantial unique variance (27%), reasoning prompt captures negative unique variance (−5%), indicating overlapping/redundant representations
- **Asymmetry strongest in frontal-motor cortex**

---

## Key Findings Summary

1. **Foundation models outperform RL baselines:** Both VLMs and LAMs exhibit significantly better voxel-wise encoding performance than RL baselines, even under matched feature dimensionality.

2. **Gains scale with cortical hierarchy:** Prompt-driven improvements are largest in high-level regions (frontal-parietal, motor-planning) and smaller (~half) in early visual cortex.

3. **Representational reorganization via action fine-tuning:** LAMs show prompt-asymmetric variance partitioning (heavy action bias), while VLMs remain symmetric. This demonstrates that action-specialized fine-tuning reorganizes representations toward action-relevant neural computations.

4. **Equivalent whole-brain accuracy, different organization:** Despite statistically equivalent whole-brain prediction accuracy between VLM and LAM, their internal representational organization differs qualitatively.

---

## Relevance to Brain-Encoding Research

This paper is a methodological reference for studies that:
- Use **foundation models** (not just task-specific or RL models) as encoding features
- Study **interactive/naturalistic** paradigms rather than passive stimulus presentation
- Examine how **prompt engineering** shapes model representations and their brain alignment
- Apply **variance partitioning** to understand representational overlap between model conditions
- Compare models across the **cortical processing hierarchy**

---

## Related Concepts

- **Brain-encoding models:** Predict brain activity from computational model features
- **RSA (Representational Similarity Analysis):** Compare representational geometry across brains and models
- **Hemodynamic response function (HRF):** Convolution kernel for fMRI temporal alignment
- **Voxel-wise encoding:** Per-voxel regression from model features to BOLD signal
- **Variance partitioning:** Decomposition of unique vs. shared variance across model conditions
- **Vision-Language Models (VLMs):** Multimodal models trained on image-text pairs (e.g., CLIP-family, LLaVA-family)
- **Large-Action Models (LAMs):** Models fine-tuned or specialized for action prediction/selection in interactive environments
- **Cortical hierarchy:** Processing gradient from early sensory → association → motor regions

---

## Citation

```bibtex
@article{oota2026brain,
  title={Brain alignment of reasoning and action representations from vision-language and action models during naturalistic gameplay},
  author={Oota, Subba Reddy and Khandelwal, Anant and Pahwa, Khushbu and Namburi, Satya Sai Srinath and Chakraborty, Tanmoy and Raju, Bapi S. and Gupta, Manish},
  journal={arXiv preprint arXiv:2605.19352},
  year={2026}
}
```
