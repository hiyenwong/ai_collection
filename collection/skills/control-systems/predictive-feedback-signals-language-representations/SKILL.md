---
name: predictive-feedback-signals-language-representations
description: "Multi-signal model of adult language learning using transformer brain alignment. Prediction shapes group-level neural architecture, feedback explains individual differences. fMRI-based with 102 subjects over 7 days. Activation: language learning, predictive coding, feedback signals, brain-model alignment, individual differences, transformer language models, artificial language learning, fMRI language representation."
---

# Predictive and Feedback Signals in Language Representations

> Multi-signal model showing prediction shapes common neural language architecture across learners, while feedback-related mechanisms explain individual differences in language learning. Validated with fMRI (n=102) and transformer models.

## Metadata
- **Source**: arXiv:2605.09409
- **Authors**: Shuguang Yang, Shaoyun Yu, Xin Jiang, Suiping Wang, Gangyi Feng
- **Published**: 2026-05-10
- **Category**: Neurons and Cognition (q-bio.NC)

## Core Methodology

### Key Innovation
This paper resolves a long-standing question in language neuroscience: what signals drive adult language learning and why do individuals differ so dramatically? The answer is a **dual-signal model**:
- **Prediction signals** → shape the **common** neural learning architecture across all learners
- **Feedback signals** → better explain **individual differences** in generalization outcomes

### Technical Framework

#### Experimental Design
- **102 adults** learned an artificial language over **7 days**
- **Corrective feedback** paradigm with behavioral tracking
- **fMRI data** collected throughout learning period
- **Individual generalization** measured on Day 7

#### Computational Modeling
Three matched transformer architectures trained with different objectives:
1. **Prediction-focused model**: Learns through next-element prediction
2. **Feedback-focused model**: Learns through error correction signals
3. **Combined model**: Joint prediction + feedback objectives

#### Brain-Model Alignment Analysis
- **RSA (Representational Similarity Analysis)**: Compare model internal representations to brain activity patterns
- **Variance partitioning**: Quantify unique neural variance explained by each model type
- **Temporal dynamics**: Track how brain-model alignment shifts during learning

### Key Findings

1. **Group-Level Dominance of Prediction**: Despite the human task being feedback-based, prediction model representations accounted for the **largest share of unique neural variance** at the group level

2. **Individual Prediction from Feedback**: Neural patterns from the **feedback model** were most useful for predicting **individual generalization outcomes** on Day 7

3. **Abstraction Trajectory**: Both prediction and feedback objectives showed a **shift from sensory to higher-order language and associative networks** during model training, mirroring human abstraction processing

## Implementation Guide

### Prerequisites
- fMRI dataset with longitudinal language learning design
- Transformer model implementations (PyTorch/HuggingFace)
- Brain-model alignment tools (RSA, encoding models)

### Step-by-Step

1. **Design artificial language learning paradigm** with corrective feedback
2. **Train matched transformers** with three objectives:
   ```python
   # Prediction objective
   loss_pred = cross_entropy(model.predict(sequence[:-1]), sequence[1:])
   
   # Feedback objective  
   loss_fb = cross_entropy(model.correct(sequence, feedback), target)
   
   # Combined objective
   loss = alpha * loss_pred + (1 - alpha) * loss_fb
   ```
3. **Extract layer-wise representations** from each model at each training stage
4. **Compute brain-model alignment** using RSA between model RDMs and fMRI RDMs
5. **Variance partitioning** to quantify unique contributions:
   ```python
   # Unique variance: prediction
   unique_pred = var(prediction) - var(prediction ∩ feedback)
   # Unique variance: feedback  
   unique_fb = var(feedback) - var(prediction ∩ feedback)
   ```
6. **Individual prediction**: Train regression from feedback-model neural patterns → Day 7 behavioral scores

### Code Example
```python
import numpy as np
from sklearn.linear_model import Ridge

# Brain-model alignment via encoding models
def brain_model_alignment(model_features, brain_data, train_idx, test_idx):
    """Fit encoding model and predict held-out brain activity."""
    model = Ridge(alpha=1.0)
    model.fit(model_features[train_idx], brain_data[train_idx])
    predictions = model.predict(model_features[test_idx])
    corr = np.corrcoef(predictions, brain_data[test_idx])[0, 1]
    return corr

# Variance partitioning
def unique_variance(pred_features, fb_features, brain_data):
    """Compute unique variance explained by each model type."""
    from sklearn.linear_model import Ridge
    
    # Full model
    full_features = np.hstack([pred_features, fb_features])
    full_model = Ridge(alpha=1.0)
    full_model.fit(full_features, brain_data)
    full_r2 = full_model.score(full_features, brain_data)
    
    # Prediction-only
    pred_model = Ridge(alpha=1.0)
    pred_model.fit(pred_features, brain_data)
    pred_r2 = pred_model.score(pred_features, brain_data)
    
    # Feedback-only
    fb_model = Ridge(alpha=1.0)
    fb_model.fit(fb_features, brain_data)
    fb_r2 = fb_model.score(fb_features, brain_data)
    
    unique_pred = full_r2 - fb_r2
    unique_fb = full_r2 - pred_r2
    return unique_pred, unique_fb
```

## Applications
- **Language learning neuroscience**: Understanding individual differences in L2 acquisition
- **Brain-model alignment**: Using multiple training objectives to probe different neural mechanisms
- **Educational AI**: Personalized language tutoring based on prediction vs. feedback profiles
- **Neuroimaging methodology**: Multi-objective model comparison for fMRI studies

## Pitfalls
- **Sample size critical**: Paper used n=102 — smaller samples may not detect individual difference signals
- **Artificial language limitations**: Results may not fully generalize to natural language learning
- **7-day timescale**: Longer learning periods may shift the prediction/feedback balance
- **Transformer matching**: Models must be architecturally matched to isolate training objective effects
- **Variance partitioning assumptions**: Requires orthogonalized features for clean interpretation

## Related Skills
- computational-lesions-multilingual-language-models-separate
- lrm-game-learning-brain-alignment
- online-generalised-predictive-coding
- lateral-predictive-coding-modular
- neuroscience-transformers-cortical-analogy
- decoding-encoding-alignment-critique
