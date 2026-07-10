---
name: brain-alignment-vlm-lam-gameplay
version: v1.0.0
last_updated: 2026-05-22
description: "Brain alignment of vision-language models (VLMs) and large-action models (LAMs) with fMRI during naturalistic gameplay. Use when: studying brain-AI alignment during interactive tasks, comparing VLMs vs LAMs neural encoding, analyzing action vs reasoning representations in frontal-parietal cortex, or designing fMRI encoding studies with foundation models."
---

# Brain Alignment of VLMs and LAMs During Naturalistic Gameplay

This skill covers methodology from the paper "Brain alignment of reasoning and action representations from vision-language and action models during naturalistic gameplay" (arXiv:2605.19352), which studies how VLMs and LAMs align with human brain activity during Atari-style video game playing.

## Core Findings

1. **VLM/LAM outperform RL baselines**: Both vision-language models and large-action models exhibit significantly better voxel-wise encoding performance than traditional RL agents, with the advantage holding under matched feature dimensionality.

2. **Prompt-driven gains scale with cortical hierarchy**: Largest improvements in frontal-parietal and motor-planning regions; early visual cortex gains roughly half as much.

3. **Representational organization asymmetry**:
   - VLM: prompt-symmetric (12.5% unique action vs 13.6% unique reasoning)
   - LAM: prompt-asymmetric (27% unique action vs -5% unique reasoning)
   - Asymmetry strongest in frontal-motor cortex

## Methodology

### Data
- fMRI recordings from participants playing Atari-style video games
- Naturalistic interactive paradigm (unlike passive visual or language tasks)

### Models
- **VLMs**: Vision-Language Models (e.g., CLIP, BLIP) with reasoning-focused prompts
- **LAMs**: Large-Action Models with action-focused prompts
- **Baseline**: Reinforcement learning agents

### Analysis
1. **Voxel-wise encoding**: Measure how well model internal representations predict fMRI voxel activity
2. **Variance partitioning**: Separate unique contributions of action vs reasoning representations
3. **Cortical hierarchy mapping**: Identify which brain regions benefit most from prompt-driven gains

## Key Insights

- Action-specialized fine-tuning reorganizes multimodal representations toward action-relevant neural computations
- Whole-brain prediction accuracy can be statistically equivalent between VLM and LAM despite fundamentally different representational organization
- Interactive tasks reveal brain alignment patterns not observable in passive paradigms

## Resources

- Paper: https://arxiv.org/abs/2605.19352
- Authors: Subba Reddy Oota, Anant Khandelwal, Khushbu Pahwa, Satya Sai Srinath Namburi, Tanmoy Chakraborty, Bapi S. Raju, Manish Gupta
- Submitted: 19 May 2026

## Activation Keywords

- brain alignment VLM LAM
- vision-language model brain encoding
- large-action model neural alignment
- naturalistic gameplay fMRI
- action reasoning representations brain
- 脑对齐 VLM LAM 游戏 fMRI
- frontal-parietal motor cortex encoding
- prompt-driven brain representation
