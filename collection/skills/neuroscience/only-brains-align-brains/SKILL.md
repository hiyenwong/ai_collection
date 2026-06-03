---
name: only-brains-align-brains
description: "Alignment Pattern Analysis (APA) methodology for model-brain alignment benchmarking. Introduces cross-region alignment patterns as a second-order structural consistency test. Only brains reproduce other brains' alignment patterns; even top-ranked models fail. Activation: model-brain alignment, fMRI, benchmarking, representational geometry, vision models, BOLD."
---

# Only Brains Align with Brains: Alignment Pattern Analysis

> Introduces alignment patterns — characteristic functional relationship profiles of each brain region to all others — as a rigorous second-order test for model-brain alignment. Reveals that even top-ranked vision models fail to capture these cross-region patterns, while they are highly stable across human subjects.

## Metadata
- **Source**: arXiv:2604.21780
- **Authors**: Larissa Höfling, Matthias Tangemann, Lotta Piefke, Susanne Keller, Katrin Franke et al.
- **Published**: 2026-04-23
- **Category**: q-bio.NC

## Core Methodology

### Key Innovation
Standard model-brain alignment benchmarks lack discriminative power — diverse models appear equivalent. This work introduces **Alignment Pattern Analysis (APA)**: a second-order structural consistency test where a model aligned to a given ROI must reproduce that ROI's characteristic cross-region alignment profile. The key finding: only brains align with brains.

### Technical Framework

1. **Standard Alignment Benchmarking**:
   - Extract activations from vision models for video stimuli
   - Measure alignment with fMRI BOLD responses across visual ROIs
   - Use representational similarity measures (RSA, linear regression predictivity)
   - Problem: diverse models cluster together, lacking discriminative power

2. **Alignment Pattern Analysis (APA)**:
   - For each brain ROI, compute its alignment profile with all other ROIs
   - This forms a characteristic "alignment pattern" — a fingerprint
   - Test whether models reproduce this pattern
   - Second-order test: not just whether model aligns to one region, but whether the pattern of alignments across regions matches

3. **Dataset**: BOLD Moments video fMRI dataset with multiple visual ROIs

### Key Findings
- Standard benchmarks show diverse models appearing equivalent in brain alignment
- Alignment patterns are highly stable across different human subjects
- Even top-ranked models (by standard metrics) fail to reproduce cross-region alignment patterns
- Only brains reproduce other brains' alignment patterns
- Reveals fundamental limitation of current normative models of visual processing
- Argues for clearer distinction between criteria for brain-alignment

## Implementation Guide

### Prerequisites
- fMRI dataset with multiple ROIs and stimulus conditions
- Vision model activations for same stimuli
- Python: numpy, scipy, scikit-learn, rsatoolbox (optional)

### Step-by-Step Analysis
1. **Standard alignment**: Compute model-to-brain alignment for each ROI using RSA or linear regression
2. **Brain alignment patterns**: For each subject's ROI, compute its representational similarity with every other ROI
3. **Model alignment patterns**: For each model's layer aligned to an ROI, compute its representational similarity with every other brain ROI
4. **Pattern comparison**: Compare model alignment patterns to brain alignment patterns using correlation
5. **Cross-subject stability**: Verify alignment patterns are consistent across subjects
6. **Statistical testing**: Test whether model patterns significantly deviate from brain patterns

### Code Example
```python
import numpy as np
from scipy.stats import spearmanr
from sklearn.linear_model import RidgeRegression

def compute_alignment_pattern(roi_representations, all_other_rois):
    """Compute alignment profile of one ROI with all others."""
    pattern = []
    target_rdm = compute_rdm(roi_representations)
    for other_roi in all_other_rois:
        other_rdm = compute_rdm(other_roi)
        corr, _ = spearmanr(target_rdm.flatten(), other_rdm.flatten())
        pattern.append(corr)
    return np.array(pattern)

def compute_rdm(activations):
    """Compute Representational Dissimilarity Matrix."""
    from scipy.spatial.distance import pdist, squareform
    return squareform(pdist(activations, metric='correlation'))

def apa_test(model_pattern, brain_pattern, n_bootstrap=1000):
    """Test if model alignment pattern matches brain pattern."""
    observed_corr, _ = spearmanr(model_pattern, brain_pattern)
    # Bootstrap null distribution
    null_corrs = []
    for _ in range(n_bootstrap):
        perm = np.random.permutation(len(brain_pattern))
        null_corrs.append(spearmanr(model_pattern, brain_pattern[perm])[0])
    p_value = np.mean(np.array(null_corrs) >= observed_corr)
    return observed_corr, p_value
```

## Applications
- **Model evaluation**: More rigorous model-brain alignment assessment than standard benchmarks
- **Model selection**: Identify models that truly capture brain-like computation
- **Neuroscience theory**: Understand what aspects of brain computation current models miss
- **Computer vision**: Guide development of more brain-like vision architectures
- **Benchmark design**: Improve neuro-AI benchmarking methodology

## Pitfalls
- APA is a necessary but not sufficient condition for brain alignment
- Requires fMRI data from multiple brain regions (not just one ROI)
- Alignment patterns may vary with stimulus set characteristics
- High cross-subject stability is a prerequisite — verify before applying APA
- Does not specify what specific computational properties models lack

## Related Skills
- neuroscience-of-transformers
- representation-use-usability-framework
- untrained-cnns-match-backpropagation-at-v1