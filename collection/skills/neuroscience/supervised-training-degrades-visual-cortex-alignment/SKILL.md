---
name: supervised-training-degrades-visual-cortex-alignment
description: Supervised training rapidly reduces early visual cortex (V1) alignment while local learning rules (predictive coding, STDP) better preserve brain-like representations.
---

# Supervised Training Rapidly Degrades Early Visual Cortex Alignment Across Biologically Plausible Learning Rules

**arXiv**: [2605.30556](https://arxiv.org/abs/2605.30556)
**Date**: 2026-05-28
**Authors**: Nils Leutenegger
**Categories**: cs.LG, q-bio.NC

## Key Question

Why do **untrained neural networks** consistently match or exceed trained networks in representational similarity to early visual cortex? This finding challenges the assumption that learning improves brain alignment.

## Methodology

### Experimental Design

**Dataset**: 720 object images from THINGS database + fMRI data from 3 subjects across 6 visual ROIs

**Learning Rules Tested**:
1. **Backpropagation (BP)**: global error signal, biologically implausible
2. **Feedback Alignment (FA)**: fixed random feedback weights
3. **Predictive Coding (PC)**: local error signals, hierarchical inference
4. **Spike-Timing-Dependent Plasticity (STDP)**: purely local, biologically plausible

**Tracking**: Spearman correlations between model and brain representational dissimilarity matrices (RDMs) at 8 checkpoints (epochs 0-40)

### Representational Similarity Analysis (RSA)

Compare RDMs from:
- Model activations for each image
- fMRI responses in each ROI (V1, V2, V3, V4, LOC, IT)

Higher correlation = better alignment = more brain-like representation

## Key Findings

### 1. Single Epoch Destroys V1 Alignment

**After just ONE training epoch**:
- V1 alignment drops **25-90%** depending on learning rule
- Untrained networks have highest V1 alignment
- Training **reduces** rather than improves brain similarity

### 2. Learning Rule Ranking for V1 Preservation

| Learning Rule | V1 Alignment Drop (delta r) | Rank |
|---------------|----------------------------|------|
| **Backpropagation** | -0.080 | Most destructive |
| **Feedback Alignment** | ~-0.06 | Moderate |
| **Predictive Coding** | ~-0.04 | Better preservation |
| **STDP** | ~-0.04 | Best preservation |

**Interpretation**: Local learning rules (PC, STDP) preserve brain-like early representations, while global error signals (BP) aggressively reshape them.

### 3. Opposite Trend in Higher Cortex (LOC)

In object-selective cortex (LOC):
- **BP shows largest increase** in alignment during training
- Absolute change is small but opposite direction from V1
- Higher-level representations benefit from supervised training

### 4. Mechanism: Inductive Biases vs Error Signals

**Untrained networks**: capture low-level visual statistics through architectural inductive biases alone (convolution, pooling, locality)

**Training effects**:
- **Global error (BP)**: reshapes representations to optimize task performance → deviates from natural statistics
- **Local learning (PC, STDP)**: updates based on local correlations → maintains natural statistics

## Implications

### For Neuroscience

1. **Inductive biases encode brain-like structure**: architecture matters more than training for early visual processing
2. **Local vs global learning**: biological learning rules may be designed to preserve natural statistics
3. **Brain-ANN alignment paradox**: better task performance ≠ better brain alignment

### For AI/ML

1. **Untrained networks useful**: random weights sufficient for brain modeling, feature extraction
2. **Preserving alignment**: use local learning rules if goal is brain-like representations
3. **Task-brain tradeoff**: supervised training optimizes task but degrades V1 similarity

### For Neuromorphic Hardware

1. **STDP preferred**: preserves biological representations while enabling learning
2. **Avoid BP**: global error signals reshape early layers too aggressively
3. **Hybrid approach**: local learning for early layers, supervised for higher layers

## Applications

### When to Use

- **Brain modeling**: use untrained or locally-trained networks for V1/V2
- **Neuromorphic systems**: implement STDP/PC for sensory processing layers
- **Representation analysis**: track RSA during training to prevent alignment loss
- **Cognitive neuroscience**: compare learning rule effects on brain similarity
- **Self-supervised learning**: may preserve alignment better than supervised

### Activation Keywords

- brain alignment, RSA, representational similarity
- untrained networks, inductive biases, visual cortex
- learning rules comparison, BP vs STDP vs PC
- V1 degradation, local vs global learning

## Pitfalls

1. **Generalization**: tested on object images—may not apply to other domains
2. **ROI selection**: only visual ROIs studied—other cortical areas unknown
3. **Training extent**: only 40 epochs—longer training may show different patterns
4. **Architecture dependence**: CNNs used—other architectures (ViT, SNN) may differ
5. **Subject variability**: only 3 subjects—individual differences exist

## Implementation Notes

### How to Measure Alignment

```python
# Representational Similarity Analysis
from scipy.stats import spearmanr

def rsa_alignment(model_activations, brain_responses):
    # Compute RDMs
    model_rdm = compute_rdm(model_activations)  # pairwise distances
    brain_rdm = compute_rdm(brain_responses)
    
    # Spearman correlation
    correlation, p_value = spearmanr(
        model_rdm.flatten(), 
        brain_rdm.flatten()
    )
    return correlation
```

### Training with Learning Rules

**Backpropagation**: standard supervised training with gradient descent

**Feedback Alignment**: fixed random feedback weights instead of transpose

**Predictive Coding**: hierarchical inference with local error minimization (see [extended-predictive-coding-free-energy-exponential-family])

**STDP**: spike-timing-dependent updates based on pre/post coincidences

## Related Skills

- [extended-predictive-coding-free-energy-exponential-family](extended-predictive-coding-free-energy-exponential-family) — PC framework
- [untrained-cnns-match-backprop-v1](untrained-cnns-match-backprop-v1) — original finding
- [neuromodulated-synaptic-plasticity](neuromodulated-synaptic-plasticity) — STDP variants
- [brain-dnn-transformation-alignment](brain-dnn-transformation-alignment) — brain-DNN alignment methods

## References

- Original paper: arXiv:2605.30556
- THINGS database: Hebart et al. (2019)
- Untrained networks: Ilyas et al. (2019), Baradad et al. (2021)
- Feedback alignment: Lillicrap et al. (2016)
- Predictive coding: Whittington & Bogacz (2017)
- STDP: Bi & Poo (1998)