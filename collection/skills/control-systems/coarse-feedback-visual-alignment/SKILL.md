---
name: coarse-feedback-visual-alignment
description: "Coarse feedback for human-aligned visual representations. Demonstrates that extremely coarse classification signals (e.g., 8 classes) produce representations that match or exceed brain alignment of fine-grained (1000-class) or self-supervised models. Use when: studying visual-brain alignment, computational neuroscience, brain-inspired vision models, training signal granularity, representational similarity analysis."
---

# Coarse Feedback Visual Alignment

Methodology demonstrating that human-like visual representations emerge from remarkably coarse feedback signals.

## arXiv Reference
- **Paper**: "An extremely coarse feedback signal is sufficient for learning human-aligned visual representations"
- **arXiv ID**: 2605.05556
- **Date**: May 7, 2026
- **Authors**: Yash Mehta, Michael F. Bonner

## Core Finding
Networks trained on **as few as 8 broad categories** learn representations that match or exceed the neural alignment of models trained on 1,000 classes. These coarsely trained networks align more closely with human perceptual similarity judgments than all other models, including self-supervised models and large-scale vision models.

## Methodology
1. **Coarse Label Generation**: 
   - PCA-based splits of pretrained embeddings partition training images into varied category counts (2, 4, 8, 16, ..., 64)
   - Parametric variation of signal granularity
2. **Training**: 
   - Train hundreds of neural networks (CNNs and ViTs) on these coarse classification tasks
3. **Evaluation**: 
   - Compare representations to macaque electrophysiology recordings
   - Compare to human fMRI responses
   - Test alignment with human perceptual similarity judgments

## Key Insights
- **Granularity Paradox**: Finer supervisory signals do not necessarily yield better brain alignment
- **Emergence**: Human-like visual representations emerge from minimal categorical distinctions
- **Efficiency**: Coarse training provides a more efficient path to brain-aligned AI
- **Perceptual Alignment**: Coarse models outperform fine-grained models on human similarity judgments

## Implications
- Reframes what learning signals biological vision may require
- Suggests biological vision might rely on broad categorical structures rather than fine distinctions
- Provides efficient training strategy for brain-aligned computer vision models

## Application Triggers
- Building brain-aligned vision models
- Studying the role of supervisory signal granularity in neural alignment
- Investigating representational similarity between ANN and biological vision
- Developing efficient training protocols for neuroscience-inspired AI

## Related Skills
- `untrained-cnns-match-backpropagation-at-v1`
- `neurally-guided-adversarial-robustness`
- `vlm-visual-cortex-alignment-robustness`
