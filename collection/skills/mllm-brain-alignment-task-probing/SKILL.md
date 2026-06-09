---
name: mllm-brain-alignment-task-probing
description: "Task-conditioned probing methodology for evaluating brain alignment of instruction-tuned multimodal LLMs (MLLMs) using fMRI. Activation: brain-MLLM alignment, instruction-tuned MLLM, task-conditioned probing, brain encoding, fMRI-MLLM, voxel-wise encoding"
---

# MLLM Brain Alignment via Task-Conditioned Probing

> Methodology for evaluating how instruction-tuned multimodal large language models (IT-MLLMs) align with human brain activity during naturalistic movie watching, revealing task-specific neural representations across brain regions.

## Metadata
- **Source**: arXiv:2506.08277v3
- **Authors**: Subba Reddy Oota, Khushbu Pahwa, Prachi Jindal, Satya Sai Srinath Namburi, Maneesh Singh, Tanmoy Chakraborty, Bapi S. Raju, Manish Gupta
- **Published**: 2025-06-09 (v3 updated 2026-05-19)
- **Categories**: q-bio.NC, cs.AI, cs.CL, cs.CV, cs.LG

## Core Methodology

### Key Innovation
This paper introduces a **task-conditioned probing framework** that evaluates instruction-tuned multimodal LLMs (IT-MLLMs) by predicting fMRI responses recorded during naturalistic movie watching. Key findings:
- IT-MLLMs show ~9% higher brain alignment than in-context learning (ICL) models, ~15% higher than non-instruction-tuned models, and ~20% higher than unimodal baselines
- Task-specific instructions produce distinct MLLM representations that vary systematically across brain regions
- ICL models show strong coupling to instruction-text semantics (r=0.78), while IT-MLLMs show weak coupling (r=0.14), consistent with task-conditioned subspaces
- This reveals IT-MLLMs organize representations around functional task demands rather than surface semantics

### Technical Framework

**Data Pipeline:**
1. **Stimuli**: Naturalistic movie watching (video with audio) — fMRI responses from participants
2. **MLLM Models**: 6 video IT-MLLMs + 2 audio IT-MLLMs + non-instruction-tuned baselines
3. **Task Instructions**: 13 video task instructions for conditioning
4. **Encoding Model**: Voxel-wise brain encoding using ridge regression

**Probing Architecture:**
1. Extract layer-wise representations from MLLMs under different task instructions
2. Train voxel-wise encoding models to predict fMRI BOLD responses
3. Compare alignment across: IT-MLLMs vs ICL vs non-IT baselines
4. Analyze region-specific alignment patterns (visual cortex, language areas, parietal, frontal)
5. Correlate task representations with instruction semantics to dissociate task-conditioned subspaces from semantic organization

### Key Results
- **IT-MLLM superiority**: Instruction-tuned models consistently outperform across brain regions
- **Region specificity**: Different brain regions show distinct alignment with different task conditions
- **Semantic decoupling**: IT representations decouple from instruction text semantics, suggesting genuinely task-conditioned representations
- **Audio vs video**: Audio IT-MLLMs show different alignment patterns compared to video models

## Implementation Guide

### Prerequisites
- fMRI datasets with naturalistic stimuli (e.g., Natural Scenes Dataset, Algonauts)
- Access to MLLM models (Video-LLaMA, LLaVA, InstructBLIP, etc.)
- Ridge regression encoding pipeline
- Python with numpy, scikit-learn, nilearn

### Step-by-Step Analysis

1. **Select MLLM layers** for feature extraction (last hidden states or attention)
2. **Prepare task instructions**: Create instruction templates for each task condition
3. **Extract representations**: Run MLLM on video frames/audio with task instruction prefixes
4. **Align with fMRI**: Use voxel-wise ridge regression to predict BOLD responses
5. **Evaluate**: Compute Pearson correlation between predicted and actual BOLD (test split)
6. **Region analysis**: Map alignment scores to brain atlases (e.g., Harvard-Oxford, Brodmann)
7. **Semantic coupling analysis**: Compute cosine similarity between IT embeddings and instruction text embeddings

### Code Example
```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import KFold

# Assume:
# X_train: MLLM representations (n_samples x n_features) under task instruction
# y_train: fMRI BOLD responses (n_samples x n_voxels)
# X_test, y_test: held-out data

def voxelwise_encoding(X_train, y_train, X_test, y_test, alpha=1.0):
    """Train ridge regression per voxel and compute correlation."""
    n_voxels = y_train.shape[1]
    predictions = np.zeros_like(y_test)
    
    for v in range(n_voxels):
        model = Ridge(alpha=alpha)
        model.fit(X_train, y_train[:, v])
        predictions[:, v] = model.predict(X_test)
    
    # Compute per-voxel Pearson correlation
    correlations = np.array([
        np.corrcoef(y_test[:, v], predictions[:, v])[0, 1]
        for v in range(n_voxels)
    ])
    return predictions, correlations

# Compare alignment across instruction conditions
# instruction_A_corr > instruction_B_corr indicates
# specific brain regions track task A better than task B
```

## Applications
- **Brain encoding**: Understanding how LLM representations map to neural activity
- **Model evaluation**: Using brain alignment as a benchmark for MLLM quality
- **Neuroscience**: Testing whether instruction-tuning creates task-specific neural subspaces
- **AI interpretability**: Mapping functional specialization across MLLM layers to brain regions
- **Naturalistic neuroscience**: Studying brain responses to ecologically valid stimuli

## Related Skills
- lpact-brain-lm-alignment-evaluation
- behavior-vlm-neuroscience
- brain-alignment-vlm-lam-gameplay
- vlm-visual-cortex-alignment-robustness
- lrm-game-learning-brain-alignment
