---
name: coarse-feedback-human-aligned-visual
description: >-
  Shows that extremely coarse feedback signals (distinguishing as few as 8
  broad categories) produce neural representations matching or exceeding
  1000-class supervised models in brain alignment with primate vision.
  Trains hundreds of CNNs and ViTs across granularity levels, comparing
  against macaque electrophysiology and human fMRI. Use when analyzing
  brain-aligned vision models, role of supervision granularity in neural
  alignment, or human perceptual similarity learning.
---

# Coarse Feedback for Human-Aligned Visual Representations

Based on: Mehta & Bonner (2026). *An extremely coarse feedback signal is sufficient for learning human-aligned visual representations*. arXiv:2605.05556 [cs.CV].

## Core Finding

Networks trained to distinguish as few as **8 broad categories** learn representations that match or exceed the neural alignment of models trained on 1,000-class ImageNet classification.

### Most Surprising Result

These coarsely trained networks align more closely with **human perceptual similarity judgments** than ALL other models evaluated, including:
- Networks trained with fine-grained supervision (1,000 classes)
- Self-supervised models (SimCLR, DINO, etc.)
- Leading large-scale vision models (CLIP, DINOv2)

## Methodology

### Stimulus Granularity Manipulation

The paper parametrically varies the granularity of the learning signal:

```
Categories: 2 → 4 → 8 → 16 → 32 → 64 → 1,000
```

Categories are created via **PCA-based splits** of pre-trained embeddings, ensuring natural data-driven groupings.

### Training

- **Architectures**: CNNs (ResNet) and Transformers (ViT)
- **Tasks**: Coarse classification at each granularity level
- **Evaluation**: Representational Similarity Analysis (RSA) against:
  - Macaque electrophysiology recordings (V1-V4, IT)
  - Human fMRI (THINGS dataset, 720 stimuli, 3 subjects)

### Key Results

| Granularity | V1/V2 Alignment | IT Alignment | Perceptual Similarity |
|-------------|----------------|--------------|----------------------|
| 2 classes   | Moderate       | Low          | Good                 |
| 8 classes   | **Best**       | Moderate     | **Best overall**     |
| 64 classes  | Good           | Good         | Good                 |
| 1,000 classes | Good         | **Best**     | Worse than 8-class   |
| Self-supervised | Good       | Moderate     | Below 8-class        |

## Implications

### For Computational Neuroscience

- **Reframes what learning signals vision requires**: The brain may not need fine-grained category supervision
- **Suggests broad categorical feedback** is sufficient for developing brain-like representations
- **Questions the trend** toward increasingly fine-grained supervision in brain-aligned AI

### For AI

- Opens a path toward building AI systems that are **more aligned with human perception**
- Coarse supervision is **more efficient** (less labeling, simpler tasks)
- Suggests current large-scale vision models may be **over-specified** for human-like visual learning

### For Understanding Biological Vision

- Primate visual systems may learn from relatively **coarse behavioral outcomes**
- The 8-category sweet spot may correspond to evolutionarily relevant category distinctions
- Supports the idea that **broad ecological pressures** shaped visual representations

## Theoretical Explanation

The paper suggests:
- Fine-grained distinctions may introduce **category-specific noise** that distorts representations
- Coarse tasks force the network to learn **genuinely generic visual features**
- Self-supervised objectives optimize for instance discrimination, which may not match human perceptual organization

## When to Use

- **Brain-aligned model design**: Use coarse supervision as a stronger baseline
- **Perceptual similarity research**: Reference for how human-like similarity emerges
- **Computational neuroscience**: Evidence for the role of coarse feedback in visual development
- **Representational alignment studies**: New paradigm for studying supervision granularity

## Citation

```bibtex
@article{mehta2026coarse,
  title={An extremely coarse feedback signal is sufficient for learning human-aligned visual representations},
  author={Mehta, Yash and Bonner, Michael F},
  journal={arXiv preprint arXiv:2605.05556},
  year={2026}
}
```

## Activation
- coarse feedback visual representations
- human-aligned vision networks
- supervision granularity neural alignment
- coarse category learning vision
- brain-aligned representation learning
- minimal supervision brain alignment
- perceptual similarity emergence
