---
name: learnad-neuro-symbolic-alzheimers
description: "LearnAD: Neuro-symbolic method for Alzheimer's disease prediction from MRI with fully interpretable rules. Combines statistical models and symbolic learning. Activation: neuro-symbolic, Alzheimer's disease, interpretable rules, brain networks, GNN"
---

# LearnAD: Learning Interpretable Rules for Brain Networks in Alzheimer's Disease

> A neuro-symbolic method for predicting Alzheimer's disease from brain MRI that learns fully interpretable rules, matching GNN accuracy while providing symbolic explanations.

## Metadata
- **Source**: arXiv:2601.00877
- **Authors**: [Paper authors]
- **Published**: 2026-01
- **Categories**: cs.LG, cs.AI

## Core Methodology

### Key Innovation
LearnAD bridges the accuracy-interpretability tradeoff by first using statistical/GNN models to identify relevant brain connections, then applying FastLAS symbolic learning to extract human-readable rules that match or approach black-box performance.

### Technical Framework

#### Two-Stage Pipeline
1. **Feature Selection** (Statistical/Neural)
   - Decision Trees
   - Random Forests
   - Graph Neural Networks
   - Output: Relevant brain connections

2. **Symbolic Learning** (FastLAS)
   - Learning global rules from selected features
   - Fully interpretable output
   - Logical rule representation

### Performance Comparison

| Method | Accuracy | Interpretability |
|--------|----------|------------------|
| Decision Trees | Lower | High |
| Support Vector Machine | Moderate | Low |
| Random Forests | High | Low |
| GNNs (all features) | Very High | Very Low |
| **LearnAD (best)** | **High** | **Very High** |

#### Key Finding
LearnAD performs only slightly below full-feature Random Forests and GNNs while remaining fully interpretable.

### Ablation Insights
- Neuro-symbolic approach maintains interpretability
- Comparable performance to pure statistical models
- Feature selection critical for rule quality
- Symbolic learning benefits from neural feature discovery

## Implementation Guide

### Prerequisites
- Brain MRI data (structural connectivity)
- FastLAS symbolic learning system
- Scikit-learn or PyTorch Geometric
- Graph construction from brain regions

### Workflow
1. **Preprocessing**: Extract brain networks from MRI
2. **Feature selection**: Train statistical/GNN models
3. **Identify connections**: Select top relevant edges
4. **Symbolic learning**: Apply FastLAS to learn rules
5. **Evaluation**: Compare accuracy vs interpretability
6. **Deployment**: Use interpretable rules for prediction

### Rule Interpretation
Example symbolic rules might look like:
```
IF (hippocampus-amygdala connectivity > threshold) 
   AND (temporal lobe atrophy > threshold)
THEN Alzheimer's = High Risk
```

## Applications
- Clinical decision support with explanations
- Alzheimer's research hypothesis generation
- Understanding disease mechanisms
- Regulatory-compliant medical AI
- Educational tools for medical students
- Brain network biomarker discovery

## Advantages Over Black-Box Models
- **Explainable decisions**: Human-readable rules
- **Trust**: Clinicians can verify logic
- **Debugging**: Easy to identify failure modes
- **Knowledge extraction**: Learn disease patterns
- **Regulatory**: Compliant with medical AI guidelines

## Pitfalls
- Rule complexity may grow with accuracy demands
- Feature selection stage still involves some black-box computation
- Limited to classification (may not capture complex patterns)
- FastLAS may struggle with very high-dimensional rules
- Tradeoff between rule simplicity and accuracy

## Related Skills
- gnn-visual-category-decoding-functional-networks
- alzheimer-pet-suvr-network-models
- multimodal-brain-connectivity-gnn
- brain-graph-neural
