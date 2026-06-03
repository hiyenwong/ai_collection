---
name: brain-mri-foundation-models
description: Self-supervised learning for brain MRI foundation models with insights from FOMO25 challenge on clinical deployment, domain generalization, and task-specific pretraining objectives. Research from arXiv:2604.11679 (April 2026).
category: neuroscience
tags: [neuroscience, brain-MRI, foundation-model, self-supervised-learning, clinical-deployment, domain-shift, FOMO25, MICCAI]
paper: arXiv:2604.11679
date: 2026-04-13
---

# Towards Brain MRI Foundation Models for the Clinic: Findings from the FOMO25 Challenge

**Source Paper:** [Towards Brain MRI Foundation Models for the Clinic: Findings from the FOMO25 Challenge](https://arxiv.org/abs/2604.11679)

**Authors:** Asbjørn Munk, Stefano Cerri, Vardan Nersesjan, et al.

**Published:** April 13, 2026

**Categories:** cs.CV

## Overview

Clinical deployment of automated brain MRI analysis faces a fundamental challenge: clinical data is heterogeneous and noisy, and high-quality labels are prohibitively costly to obtain. The **FOMO25 challenge** at MICCAI 2025 evaluated foundation models trained on the large **FOMO60K** pretraining dataset on real clinical data under domain shift.

## Key Contributions

### 1. FOMO60K Pretraining Dataset

- Large pretraining dataset for brain MRI foundation models
- Enables self-supervised learning on clinical-scale data
- Addresses limitation of small pretraining datasets

### 2. Clinical-Grade Evaluation

- Models evaluated on **data sourced directly from clinical workflows**
- Few-shot and out-of-domain settings
- Tasks: infarct classification, meningioma segmentation, brain age regression

### 3. Standardized Evaluation Pipeline

- **Nineteen foundation models** from sixteen teams
- Containerized pipeline for fair comparison
- Method track (FOMO60K only) vs. Open track (any data)

## Key Findings

### Finding 1: Self-Supervised Pretraining Improves Generalization

**Results:**
- Strongest models trained **out-of-domain** surpass supervised baselines trained **in-domain**
- Self-supervised pretraining improves generalization on clinical data under domain shift
- Foundation models more robust to data heterogeneity

**Implication:**
- Pretraining on large unlabeled data enables clinical deployment
- Domain shift can be mitigated through proper pretraining

### Finding 2: No Single Pretraining Objective Benefits All Tasks

**Task-Specific Optimal Objectives:**

| Task | Best Objective | Reasoning |
|------|---------------|-----------|
| **Segmentation** | MAE (Masked Autoencoder) | Reconstruction favors spatial precision |
| **Classification** | Hybrid reconstruction-contrastive | Combines local and global representations |
| **Regression** | Varies by target | Task-dependent optimal objective |

**Implication:**
- Pretraining objective should match downstream task
- One-size-fits-all approach is suboptimal
- Consider task characteristics when designing pretraining

### Finding 3: Small Pretrained Models Can Be Highly Effective

**Surprising Results:**
- Strong performance achieved by **small pretrained models**
- Scaling model size and training duration did not yield reliable benefits
- Efficiency matters as much as scale

**Implication:**
- Don't automatically scale up; optimize architecture
- Clinical deployment benefits from efficient models
- Resource-constrained settings can use smaller models

## Challenge Structure

### Method Track
- Models trained exclusively on **FOMO60K**
- Tests effectiveness of specific pretraining dataset
- Controls for external data effects

### Open Track
- Models trained on **any data**
- Tests absolute performance ceiling
- Includes existing public models

### Evaluation Tasks

1. **Infarct Classification**
   - Binary classification of stroke lesions
   - Tests sensitivity to small pathological changes

2. **Meningioma Segmentation**
   - Tumor boundary delineation
   - Tests spatial precision

3. **Brain Age Regression**
   - Predicting chronological age from MRI
   - Tests global pattern recognition

## Technical Insights

### Pretraining Objectives

**MAE (Masked Autoencoder):**
- Reconstructs masked image patches
- Favors local spatial coherence
- Best for segmentation tasks

**Contrastive Learning:**
- Learns invariant representations
- Captures global semantics
- Good for classification

**Hybrid Approaches:**
- Combines reconstruction and contrastive losses
- Balances local and global features
- Flexible across tasks

### Clinical Data Challenges

**Heterogeneity:**
- Different scanners and protocols
- Variable image quality
- Acquisition differences

**Noise:**
- Motion artifacts
- Partial coverage
- Protocol variations

**Label Scarcity:**
- Expert annotation expensive
- Time-consuming
- Error-prone

## Implications

### For Clinical Practice

**Deployment Feasibility:**
- Self-supervised learning enables clinical deployment
- Models can generalize across clinical sites
- Reduces need for site-specific training

**Cost Reduction:**
- Less reliance on expensive expert labels
- Reusable pretrained models
- Efficient small models viable

### For Research

**Dataset Development:**
- Importance of large pretraining datasets
- Need for clinical-grade benchmarks
- Standardized evaluation critical

**Method Development:**
- Task-aware pretraining objectives
- Efficiency as important as performance
- Domain adaptation techniques

### For Industry

**Product Development:**
- Clinical validation requirements
- Regulatory considerations for AI
- Deployment across heterogeneous sites

## Methodology

1. **Dataset Creation:** FOMO60K from clinical workflows
2. **Challenge Organization:** MICCAI 2025 satellite event
3. **Model Submission:** 19 models from 16 teams
4. **Containerized Evaluation:** Standardized pipeline
5. **Analysis:** Cross-task and cross-model comparison

## Limitations

- Limited to three clinical tasks
- Evaluation on specific clinical sites
- May not generalize to all pathologies
- Short follow-up period

## Future Directions

- Extend to more diverse clinical tasks
- Longitudinal evaluation
- Multi-site deployment studies
- Integration with clinical workflows

## Citation

```bibtex
@article{munk2026brain,
  title={Towards Brain MRI Foundation Models for the Clinic: Findings from the FOMO25 Challenge},
  author={Munk, Asbj{\o}rn and Cerri, Stefano and Nersesjan, Vardan and others},
  journal={arXiv preprint arXiv:2604.11679},
  year={2026}
}
```

## Related Concepts

- Self-supervised learning
- Foundation models
- Medical imaging
- Brain MRI analysis
- Domain generalization
- Transfer learning
- Clinical deployment
- MICCAI challenges

## Activation Keywords

- brain MRI foundation model
- FOMO25
- self-supervised learning medical imaging
- clinical deployment
- domain shift
- MAE pretraining
- medical AI
- neuroimaging foundation model

## Use Cases

1. **Clinical Deployment:** Deploying AI for brain MRI analysis
2. **Pretraining Strategy:** Choosing objectives for medical imaging
3. **Research Benchmarking:** Standardized evaluation of medical AI
4. **Domain Adaptation:** Handling heterogeneous clinical data
5. **Resource Planning:** Deciding on model size for clinical AI
