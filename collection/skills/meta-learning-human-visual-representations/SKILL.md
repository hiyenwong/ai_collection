---
name: meta-learning-human-visual-representations
description: "Meta-learning methodology for achieving human-like visual representations. Proposes that meta-learning (learning to learn) pressure shapes neural representations to support open-ended tasks. Compared to pretrained models, meta-learned representations better predict human similarity judgments, semantic rule learning, and high-level visual cortex activity. Activation: meta-learning, visual representations, brain alignment, human similarity, semantic learning, few-shot learning, visual cortex"
metadata:
  arxiv_id: "2606.28399"
  published: "2026-06-24"
  authors: "Can Demircan, Marcel Binz, Alireza Modirshanechi, Eric Schulz"
  tags: ["meta-learning", "visual-representations", "brain-alignment", "human-similarity", "few-shot-learning"]
---

# Meta-learning as a Principle for Human-like Visual Representations

## Core Thesis

Pretrained neural networks model human visual representations well but still show gaps. This paper proposes that the gap exists because these networks optimize a single fixed objective, whereas human representations must support open-ended tasks.

**Key Hypothesis**: Meta-learning (learning to learn) shapes representations to be flexible for rapid task acquisition from few observations.

## Methodology

1. **Training Approach**: Train a sequence model across thousands of semantically rich tasks mapping images to high-level concepts
2. **No Human Supervision**: Model trained without any supervision from human data
3. **Comparison**: Compare meta-learned representations vs pretrained base encoders

## Key Findings

### Behavioral Level
- Meta-learned representations better predict **human similarity judgments**
- Better at **semantic rule learning**
- Gains depend on **disentangled, high-level task distributions**

### Neural Level
- Better alignment with **high-level visual cortex**
- Brain alignment driven primarily by the **learning-to-learn pressure**

## Core Insights

1. **Flexibility through Meta-Learning**: Human visual representation flexibility reflects the functional demand to learn new semantic relationships on the fly

2. **Dissociable Mechanisms**: Behavioral gains and brain alignment have different drivers:
   - Behavioral: task distribution structure (disentangled, high-level)
   - Neural: meta-learning pressure itself

3. **Beyond Pretraining**: Fixed-objective pretraining is insufficient; representations must be shaped by the pressure to learn new tasks rapidly

## Methodological Implications

### For Brain-Model Alignment
- Meta-learning provides a more biologically plausible training paradigm
- Captures the open-ended nature of human visual processing
- Better predicts neural responses in high-level visual areas

### For AI Systems
- Few-shot learning capabilities emerge from meta-learning pressure
- Representations become more generalizable and flexible
- Semantic relationships can be acquired rapidly

## Experimental Design

- **Tasks**: Thousands of image-to-concept mappings
- **Evaluation**: Human similarity judgments, semantic rule learning, fMRI visual cortex alignment
- **Comparison**: Meta-learned vs pretrained base encoders

## Limitations & Future Directions

- Sequence model architecture choices not fully explored
- Could be extended to other modalities (auditory, multimodal)
- Integration with continual learning frameworks promising

## Related Concepts

- Few-shot learning
- Brain-model alignment
- Visual cortex representations
- Meta-learning / learning to learn
- Semantic representations
- Open-ended learning

## References

- arXiv:2606.28399 [cs.CV]
- Steinmetz et al. 2019 (neural data)
- Bolding & Franks 2018 (olfactory data, mentioned in related work)
