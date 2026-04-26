---
name: gaslight-gatekeep-v1v3-early-visual-cortex
description: "Vision-language models are increasingly deployed in high-stakes settings, yet their susceptibility to sycophantic manipulation remains poorly understood, particularly in relation to how these models represent visual information internally. Whether mo Activation: brain, neural, neuroscience, fmri, encoding"
---

# Gaslight, Gatekeep, V1-V3: Early Visual Cortex Alignment Shields Vision-Language Models from Sycophantic Manipulation

## OvervieVision-language models are increasingly deployed in high-stakes settings, yet their susceptibility to sycophantic manipulation remains poorly understood, particularly in relation to how these models represent visual information internally. Whether models whose visual representations more closely mirror human neural processing are also more resistant to adversarial pressure is an open question with implications for both neuroscience and AI safety. We investigate this question by evaluating 12 open-weight vision-language models spanning 6 architecture families and a 40$\times$ parameter range (256M--10B) along two axes: brain alignment, measured by predicting fMRI responses from the Natural Scenes Dataset across 8 human subjects and 6 visual cortex regions of interest, and sycophancy, measured through 76,800 two-turn gaslighting prompts spanning 5 categories and 10 difficulty levels. Region-of-interest analysis reveals that alignment specifically in early visual cortex (V1--V3) is a reliable negative predictor of sycophancy ($r = -0.441$, BCa 95\% CI $[-0.740, -0.031]$), with all 12 leave-one-out correlations negative and the strongest effect for existence denial attacks ($r = -0.597$, $p = 0.040$). This anatomically specific relationship is absent in higher-order category-selective regions, suggesting that faithful low-level visual encoding provides a measurable anchor against adversarial linguistic override in vision-language models. We release our code on \href{https://github.com/aryashah2k/Gaslight-Gatekeep-Sycophantic-Manipulation}{GitHub} and dataset on \href{https://huggingface.co/datasets/aryashah00/Gaslight-Gatekeep-V1-V3}{Hugging Face}
## Source Paper

- **Title:** Gaslight, Gatekeep, V1-V3: Early Visual Cortex Alignment Shields Vision-Language Models from Sycophantic Manipulation
- **Authors:** Arya Shah, Vaibhav Tripathi, Mayank Singh et al.
- **arXiv:** [2604.13803v1](https://arxiv.org/abs/2604.13803v1)
- **Published:** 2026-04-15
- **Categories:** cs.CV, cs.AI
- **PDF:** [Download](https://arxiv.org/pdf/2604.13803v1)

## Key Contributions

Based on the abstract, this paper makes the following contributions:

1. **Novel approach** to brain, neural, neuroscience, fmri, encoding
2. **Methodology** bridging computational neuroscience with practical applications
3. **Evaluation** demonstrating effectiveness in relevant tasks

## Core Concepts

### Methodology
Vision-language models are increasingly deployed in high-stakes settings, yet their susceptibility to sycophantic manipulation remains poorly understood, particularly in relation to how these models represent visual information internally. Whether models whose visual representations more closely mirror human neural processing are also more resistant to adversarial pressure is an open question with implications for both neuroscience and AI safety. We investigate this question by evaluating 12 ope

### Technical Details

- The paper introduces a framework/method for neuroscience-related computation
- Key innovation in handling brain, neural, neuroscience data/tasks
- Provides theoretical grounding and experimental validation

## Practical Applications

### Application Area
This research has implications for:
- Brain-computer interfaces
- Neural decoding and encoding
- Computational modeling of brain function
- AI systems inspired by neuroscience

### Implementation Considerations

Key implementation aspects:
1. Data preprocessing for neuroimaging/neural signals
2. Model architecture choices
3. Training and evaluation protocols

## Related Work

This work builds on existing research in:
- Computational neuroscience methods
- brain, neural, neuroscience analysis
- Brain-inspired AI architectures

## References

- Arya Shah, Vaibhav Tripathi, Mayank Singh et al. (2026). "Gaslight, Gatekeep, V1-V3: Early Visual Cortex Alignment Shields Vision-Language Models from Sycophantic Manipulation." arXiv:2604.13803v1.

## Activation Keywords

brain, neural, neuroscience, fmri, encoding, cortex, coding
