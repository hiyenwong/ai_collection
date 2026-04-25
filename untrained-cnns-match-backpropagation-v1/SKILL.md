---
name: untrained-cnns-match-backpropagation-v1
description: "Systematic RSA comparison showing untrained CNNs match backpropagation-trained networks at V1 cortical representations. Demonstrates that architectural biases alone (without learning) produce brain-aligned representations in early visual cortex, questioning the necessity of task-driven training for V1 modeling. (arXiv:2604.16875, April 2026)"
tags: [untrained CNN, V1 cortex, representational similarity analysis, fMRI, visual cortex, brain-model alignment, architectural bias]
---

# Untrained CNNs Match Backpropagation at V1: RSA vs fMRI

**arXiv:** 2604.16875 (April 18, 2026)
**Categories:** cs.LG, q-bio.NC

## Summary

Systematic comparison using Representational Similarity Analysis (RSA) showing that untrained (randomly initialized) CNNs achieve representations matching backpropagation-trained CNNs when compared against fMRI recordings of human V1 visual cortex. This challenges the assumption that task-driven training is necessary for brain-aligned representations in early visual areas.

## Key Methodology

### Core Approach
1. **Architecture Selection:** Test multiple CNN architectures (ResNet, VGG, AlexNet variants) in both trained and untrained configurations
2. **Representational Similarity Analysis (RSA):** Compare CNN layer representations against fMRI BOLD responses from human V1
3. **Random Initialization Controls:** Use multiple random seeds to establish statistical distributions of untrained representations
4. **Layer-wise Comparison:** Systematic evaluation across all layers to identify where trained vs untrained diverge

### Key Findings
- **V1 Alignment:** Untrained CNNs match trained networks at V1 level — architectural biases dominate
- **Higher Visual Areas:** Trained networks diverge and better capture higher visual area representations
- **Implication:** Architectural inductive biases (convolution, pooling, hierarchical processing) are sufficient for early visual cortex alignment
- **RSA Framework:** Provides rigorous statistical framework for comparing artificial and biological representations

### Technical Framework
- **fMRI Data:** Human visual cortex recordings with controlled stimulus sets
- **RSA RDMs:** Representational Dissimilarity Matrices computed for each CNN layer and brain ROI
- **Statistical Testing:** Bootstrap-based significance testing with correction for multiple comparisons
- **Architecture Variants:** Systematic evaluation across depth, width, and connectivity patterns

## Practical Applications

### When to Use This Approach
- Evaluating brain-model alignment without expensive training procedures
- Understanding what drives cortical representation similarity
- Designing architectures with built-in brain-aligned inductive biases
- Benchmarking computational neuroscience models against neural data

### Implementation Steps
1. Select CNN architectures to evaluate
2. Generate random initialization variants (10+ seeds)
3. Compute RDMs for each layer of each model variant
4. Load fMRI RDMs for target brain regions (V1, V2, V4, IT)
5. Compute RSA correlation (Kendall tau or Spearman) between model and brain RDMs
6. Compare trained vs untrained distributions statistically
7. Identify layers and regions where differences emerge

## Limitations & Considerations

- **Scope:** Findings specific to V1 — higher visual areas require training
- **Stimulus Dependence:** Results may vary with stimulus set complexity
- **fMRI Resolution:** BOLD signal limitations affect spatial precision of comparisons
- **Architecture Coverage:** Not all architectural families tested

## Related Skills
- `brain-graph-neural` — Brain connectivity analysis
- `neural-encoding-evaluation-ground-truth` — Neural encoding evaluation
- `vlm-visual-cortex-alignment-robustness` — VLM visual cortex alignment
