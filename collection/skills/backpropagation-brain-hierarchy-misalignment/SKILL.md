---
name: backpropagation-brain-hierarchy-misalignment
description: "反向传播算法与人脑视觉处理层级的不匹配研究。使用fMRI和MEG证明梯度虽能预测脑信号，但其时空组织与生物学反向传播机制不符。激活词：反向传播、大脑层级、brain hierarchy、backpropagation、fMRI、MEG、视觉处理、DINOv3、神经网络学习机制。"
---

# Misalignment Between Backpropagation and the Hierarchy of Brain Responses to Images

## Paper Overview

**arXiv ID**: 2605.28693  
**Authors**: Joséphine Raugel, Maximilian Seitzer, Marc Szafraniec, Huy V. Vo, Jérémy Rapin, Patrick Labatut, Piotr Bojanowski, Valentin Wyart, Jean-Rémi King  
**Categories**: q-bio.NC (Neurons and Cognition), cs.AI (Artificial Intelligence)  
**Published**: May 27, 2026  
**DOI**: https://doi.org/10.48550/arXiv.2605.28693

## Research Question

Does backpropagation—the core learning mechanism of deep learning—correspond to the hierarchy of brain responses? While forward activations of vision models reliably map onto the cortical hierarchy, this study asks whether backpropagated gradients exhibit similar correspondence with neural data.

## Methodology

### Data Collection
- **fMRI**: Functional magnetic resonance imaging of human brain responses to natural images
- **MEG**: Magnetoencephalography recordings of temporal dynamics
- **Stimuli**: Natural images presented to human participants

### Models Analyzed
- **Primary**: DINOv3 (self-supervised vision model)
- **Reproduced**: 8 vision models for validation

### Analysis Framework
- Extended standard encoding analyses to map backpropagated gradients onto neural data
- Compared forward activations vs. backpropagated gradients in predicting brain signals
- Analyzed spatial and temporal organization across the visual hierarchy

## Key Findings

### 1. Gradients Can Predict Brain Signals
- Backpropagated gradients reliably predict **both fMRI and MEG signals**
- Predictions strongest in **higher-level visual cortex** and **later latencies**
- Gradient representations capture neural activity patterns

### 2. Temporal Organization Misalignment
- **Order of gradient computation** diverges from temporal hierarchy of human brain
- Brain processes information in sequence that differs from backpropagation order
- Sequential layer updates in networks ≠ temporal processing in cortex

### 3. Spatial Organization Misalignment
- **Spatial distribution of gradients** diverges from spatial hierarchy
- Cortical areas activated by gradients don't match expected biological pattern
- Layer-to-area mapping inconsistent with anatomical hierarchy

## Core Implications

### For Neuroscience
- **Deep networks and brain share representational content** but likely use **fundamentally different learning mechanisms**
- Forward activations map well, but learning dynamics diverge
- Biological learning may not implement backpropagation directly

### For AI Research
- Current optimization methods may not capture biological principles
- Self-supervised models (DINOv3) show similar patterns to supervised ones
- Need for biologically plausible learning algorithms

### For NeuroAI Alignment
- Forward pass alignment ≠ learning mechanism alignment
- Representation similarity doesn't guarantee mechanism similarity
- Different algorithms can converge on similar representations

## Technical Contributions

1. **Encoding Analysis Extension**: Novel method to map backpropagated gradients to neural data
2. **Hierarchical Analysis**: Spatial-temporal comparison across visual hierarchy
3. **Multi-modal Validation**: Both fMRI (spatial) and MEG (temporal) evidence
4. **Model Generalization**: Results reproduced across 8 vision models

## Experimental Design Strengths

- Uses natural images (ecologically valid stimuli)
- Combines fMRI and MEG (complementary spatial-temporal coverage)
- Tests multiple models (robustness across architectures)
- Clear prediction: gradients should follow brain hierarchy if backprop is biologically plausible

## Limitations & Open Questions

- Does the misalignment apply to other modalities (language, audition)?
- What biological mechanisms could achieve similar representations?
- Could feedback alignment or target propagation better match brain dynamics?
- How do different learning rules (Hebbian, predictive coding) compare?

## Relation to Existing Work

- Builds on encoding models mapping activations to brain (Kay et al., 2008; Yamins et al., 2014)
- Contrasts with "forward pass alignment" findings
- Connects to debate on biological backpropagation implementation
- Links to predictive coding theories of cortical processing

## Future Research Directions

1. **Alternative Learning Mechanisms**: Test feedback alignment, target propagation, predictive coding
2. **Developmental Studies**: Track brain-algorithm alignment across development
3. **Temporal Dynamics**: Fine-grained analysis of gradient flow timing
4. **Cross-modal Extension**: Apply to language models and auditory processing
5. **Architectural Variations**: Test biologically-inspired network architectures

## Activation Keywords

- 反向传播、大脑层级、brain hierarchy、backpropagation
- fMRI、MEG、视觉处理、visual cortex
- DINOv3、自监督学习、self-supervised
- 神经网络学习机制、biological learning
- 表征对齐、representation alignment
- 编码模型、encoding analysis

## Methodological Patterns

### Gradient-to-Brain Mapping
```python
# Extract gradients for encoding analysis
model = load_model('dinov3')
activations = forward_pass(images)
gradients = backward_pass(activations, target)

# Fit encoding models
encoding_model.fit(gradients, fMRI_data)  # Spatial
encoding_model.fit(gradients, MEG_data)  # Temporal

# Compare with forward activations
forward_score = encoding_model.score(activations, brain_data)
gradient_score = encoding_model.score(gradients, brain_data)
```

### Hierarchical Analysis
```python
# Visual hierarchy ROIs
visual_areas = ['V1', 'V2', 'V4', 'IT', 'higher_visual']

# Temporal windows for MEG
time_windows = [(0, 50), (50, 100), (100, 200), (200, 400)]  # ms

# Compare gradient-to-area mapping vs. biological expectation
gradient_order = compute_gradient_order(model)
brain_order = anatomical_hierarchy_order(visual_areas)
alignment_score = order_alignment(gradient_order, brain_order)
```

## Citation

```bibtex
@article{raugel2026misalignment,
  title={Misalignment Between Backpropagation and the Hierarchy of Brain Responses to Images},
  author={Raugel, Joséphine and Seitzer, Maximilian and Szafraniec, Marc and Vo, Huy V. and Rapin, Jérémy and Labatut, Patrick and Bojanowski, Piotr and Wyart, Valentin and King, Jean-Rémi},
  journal={arXiv preprint arXiv:2605.28693},
  year={2026}
}
```

## Related Papers

- [untrained-cnns-match-backprop-v1](untrained-cnns-match-backprop-v1) - Untrained CNNs match backprop at V1
- [brain-dit-fmri-foundation-model](brain-dit-fmri-foundation-model) - fMRI foundation models
- [vlms-human-alignment-natural-reading](vlms-human-alignment-natural-reading) - VLM vs LLM brain alignment

## Tags

#neuroscience #computational-neuroscience #backpropagation #brain-alignment #visual-processing #encoding-models #fMRI #MEG #neuroai #learning-mechanisms #self-supervised-learning
