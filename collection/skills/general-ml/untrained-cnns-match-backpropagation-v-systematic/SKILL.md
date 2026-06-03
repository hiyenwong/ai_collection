---
name: untrained-cnns-match-backpropagation-v-systematic
description: "backpropagation convolutional cortex cortical fmri methodology from arXiv:2604.16875. A central question in computational neuroscience is whether the learning rule used to train a neural network determines how well its internal represen... Activation: backpropagation, convolutional, cortex, cortical, fmri, learning rule, neural, plasticity, representational, rsa"
---

# Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI

## Overview

A central question in computational neuroscience is whether the learning rule used to train a neural network determines how well its internal representations align with those of the human visual cortex. We present a systematic comparison of four learning rules -- backpropagation (BP), feedback alignment (FA), predictive coding (PC), and spike-timing-dependent plasticity (STDP) -- applied to identical convolutional architectures and evaluated against human fMRI data from the THINGS-fMRI dataset (720 stimuli, 3 subjects) using Representational Similarity Analysis (RSA). Crucially, we include an untrained random-weights baseline that reveals the dominant role of architecture. We find that early visual alignment (V1/V2) is primarily architecture-driven: an untrained CNN achieves rho = 0.071, statistically indistinguishable from BP (rho = 0.072, p = 0.43). Learning rules only differentiate at higher visual areas: BP dominates at LOC/IT, and PC with local Hebbian updates achieves IT alignment statistically indistinguishable from BP (p = 0.18). FA consistently impairs representations below the random baseline at V1. Partial RSA confirms all effects survive pixel-similarity control. These results demonstrate that the relationship between learning rules and cortical alignment is region-specific: architecture determines early alignment, while supervised objectives drive late alignment.

## Source Paper

- **Title:** Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI
- **Authors:** Nils Leutenegger
- **arXiv:** [2604.16875](https://arxiv.org/abs/2604.16875)
- **Published:** 2026-04-18
- **Category:** cs.LG
- **PDF:** [Download](https://arxiv.org/pdf/2604.16875)

## Core Concepts

### Key Contributions

1. A central question in computational neuroscience is whether the learning rule used to train a neural network determines how well its internal representations align with those of the human visual cortex.

2. We present a systematic comparison of four learning rules -- backpropagation (BP), feedback alignment (FA), predictive coding (PC), and spike-timing-dependent plasticity (STDP) -- applied to identical convolutional architectures and evaluated against human fMRI data from the THINGS-fMRI dataset (720 stimuli, 3 subjects) using Representational Similarity Analysis (RSA).

3. We find that early visual alignment (V1/V2) is primarily architecture-driven: an untrained CNN achieves rho = 0.

4. Learning rules only differentiate at higher visual areas: BP dominates at LOC/IT, and PC with local Hebbian updates achieves IT alignment statistically indistinguishable from BP (p = 0.

5. FA consistently impairs representations below the random baseline at V1.


### Technical Framework

The paper introduces methods relevant to: backpropagation, convolutional, cortex, cortical, fmri, learning rule, neural, plasticity, representational, rsa

**Domain:** Computational Neuroscience, Neural Networks, Machine Learning
**Technique:** Supervised Learning
**Application:** Brain Signal Analysis

## Methodology

### Approach

Based on the paper's contributions, the core methodology involves:

1. **Problem Formulation:** A central question in computational neuroscience is whether the learning rule used to train a neural network determines how well its internal representations align with those of the human visual cortex.
2. **Key Innovation:** A central question in computational neuroscience is whether the learning rule used to train a neural network determines how well its internal representations align with those of the human visual cortex.
3. **Evaluation:** Experimental validation with quantitative results.

### Implementation Considerations

```python
# Key concepts from the paper
# Reference: arXiv:2604.16875

# Note: This is a conceptual framework based on the paper abstract.
# For full implementation details, refer to the original paper.

import numpy as np

class Untrainedcnnsmatchbackpropagat:
    """
    Framework based on: Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI
    arXiv: 2604.16875
    """
    
    def __init__(self, **kwargs):
        # Initialize model parameters
        self.params = kwargs
    
    def forward(self, x):
        """Forward pass / main computation."""
        raise NotImplementedError("See original paper for implementation details")
    
    def evaluate(self, x, y):
        """Evaluation on test data."""
        raise NotImplementedError("See original paper for evaluation protocol")
```

## Practical Applications

### Application 1: Research Replication
- Use this framework to replicate the paper's findings
- Compare with baseline methods on standard benchmarks
- Extend the methodology to new datasets or domains

### Application 2: Method Extension
- Build upon the paper's contributions for new research
- Combine with complementary techniques
- Apply to related but different problem domains

## Experimental Results

The paper reports experimental results demonstrating:

- Crucially, we include an untrained random-weights baseline that reveals the dominant role of architecture.

- We find that early visual alignment (V1/V2) is primarily architecture-driven: an untrained CNN achieves rho = 0.

- Learning rules only differentiate at higher visual areas: BP dominates at LOC/IT, and PC with local Hebbian updates achieves IT alignment statistically indistinguishable from BP (p = 0.

- FA consistently impairs representations below the random baseline at V1.


## Limitations

- As a preprint, findings have not been peer-reviewed
- Results may be specific to the datasets used
- Generalization to other domains requires further validation
- Implementation details may require supplementary material

## Related Work

This paper relates to:
- Spiking Neural Networks and neuromorphic computing
- Brain signal processing and neural decoding
- Computational neuroscience modeling
- Neural network learning rules and optimization

## References

- Nils Leutenegger et al. (2026). "Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI." arXiv:2604.16875.

## Activation Keywords

- backpropagation, convolutional, cortex, cortical, fmri, learning rule, neural, plasticity, representational, rsa
- arXiv:2604.16875

---
*Generated: 2026-04-23 | Source: arXiv automated research workflow*
