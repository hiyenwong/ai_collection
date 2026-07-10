---
name: brain-segmentation-active-learning
description: "Entropy-based active learning methodology for fair and efficient brain image segmentation. Use when: (1) performing brain MRI/CT segmentation with limited labeled data, (2) needing fair segmentation across demographic groups, (3) selecting most informative samples for annotation, (4) optimizing annotation budget for medical imaging, (5) addressing bias in brain segmentation models."
arxiv_id: "2605.01706"
published: "2026-05-03"
authors: ["Ghazal Danaee", "M\u00e9lanie Gaillochet", "Christian Desrosiers", "Herve Lombaert", "Sylvain Bouix"]
tags: ["brain-segmentation", "active-learning", "entropy", "fairness", "medical-imaging", "MRI"]
---

# Brain Segmentation via Entropy-Based Active Learning

## Methodology Overview

Active learning strategy that uses model prediction entropy to select the most informative samples for annotation, combined with fairness constraints to ensure equitable segmentation performance across demographic groups.

## Core Algorithm

1. **Entropy-based sample selection**: Compute predictive entropy over unlabeled pool
   - H(y|x) = -\sum_k p(y=k|x) log p(y=k|x)
   - Select samples with highest entropy (most uncertain)
2. **Fairness-aware selection**: Ensure selected samples represent all demographic groups
   - Track per-group annotation budget
   - Penalize over-representation of any group
3. **Iterative training**: Retrain model after each annotation batch
   - Monitor both overall accuracy and per-group fairness metrics

## Key Components

### Entropy Computation
- Use model prediction uncertainty as informativeness proxy
- Monte Carlo dropout or deep ensembles for uncertainty estimation
- Normalize entropy across classes to handle class imbalance

### Fairness Metric
- Demographic parity in segmentation quality (Dice score per group)
- Equal opportunity: similar false negative rates across groups
- Track worst-group performance as primary fairness indicator

### Selection Strategy
- Greedy: pick highest-entropy samples until budget exhausted
- Batch: diversify within high-entropy subset using clustering
- Fair: constrain selection to maintain group representation

## Usage Patterns

### Pattern 1: Limited Annotation Budget
When annotation budget is constrained (e.g., 10% of data):
1. Train initial model on seed set (5-10%)
2. Compute entropy on remaining unlabeled pool
3. Select top-K highest entropy samples
4. Annotate and retrain
5. Repeat until budget exhausted

### Pattern 2: Fairness-Constrained Segmentation
When ensuring fair performance across groups:
1. Define demographic groups (age, sex, scanner site, etc.)
2. Compute per-group entropy distributions
3. Select samples proportionally from each group's high-entropy tail
4. Monitor per-group Dice scores during active learning
5. Adjust selection weights if any group falls behind

## Pitfalls
- Entropy can be miscalibrated: use temperature scaling or MC dropout
- Small groups may be undersampled: enforce minimum per-group quota
- Class imbalance affects entropy: normalize by class prior
- Medical domain shift: validate on held-out sites/scanners

## Activation
- brain segmentation active learning
- entropy-based sample selection
- fair brain segmentation
- medical imaging active learning
- 脑分割主动学习
- 公平性脑影像分割
