---
name: omnimouse-scaling-properties-multimodal-multitask-brain
description: "brain cortex decoding driving multi-modal methodology from arXiv:2604.18827. Scaling data and artificial neural networks has transformed AI, driving breakthroughs in language and vision. Whether similar principles apply to mode... Activation: brain, cortex, decoding, driving, multi-modal, neural, neurons, scaling"
---

# OmniMouse: Scaling properties of multi-modal, multi-task Brain Models on 150B Neural Tokens

## Overview

Scaling data and artificial neural networks has transformed AI, driving breakthroughs in language and vision. Whether similar principles apply to modeling brain activity remains unclear. Here we leveraged a dataset of 3.1 million neurons from the visual cortex of 73 mice across 323 sessions, totaling more than 150 billion neural tokens recorded during natural movies, images and parametric stimuli, and behavior. We train multi-modal, multi-task models that support three regimes flexibly at test time: neural prediction, behavioral decoding, neural forecasting, or any combination of the three. OmniMouse achieves state-of-the-art performance, outperforming specialized baselines across nearly all evaluation regimes. We find that performance scales reliably with more data, but gains from increasing model size saturate. This inverts the standard AI scaling story: in language and computer vision, massive datasets make parameter scaling the primary driver of progress, whereas in brain modeling -- even in the mouse visual cortex, a relatively simple system -- models remain data-limited despite vast recordings. The observation of systematic scaling raises the possibility of phase transitions in neural modeling, where larger and richer datasets might unlock qualitatively new capabilities, paralleling the emergent properties seen in large language models. Code available at https://github.com/enigma-brain/omnimouse.

## Source Paper

- **Title:** OmniMouse: Scaling properties of multi-modal, multi-task Brain Models on 150B Neural Tokens
- **Authors:** Konstantin F. Willeke, Polina Turishcheva, Alex Gilbert, Goirik Chakrabarty, Hasan A. Bedel et al.
- **arXiv:** [2604.18827](https://arxiv.org/abs/2604.18827)
- **Published:** 2026-04-20
- **Category:** q-bio.NC
- **PDF:** [Download](https://arxiv.org/pdf/2604.18827)

## Core Concepts

### Key Contributions

1. OmniMouse achieves state-of-the-art performance, outperforming specialized baselines across nearly all evaluation regimes.

2. The observation of systematic scaling raises the possibility of phase transitions in neural modeling, where larger and richer datasets might unlock qualitatively new capabilities, paralleling the emergent properties seen in large language models.


### Technical Framework

The paper introduces methods relevant to: brain, cortex, decoding, driving, multi-modal, neural, neurons, scaling

**Domain:** Computational Neuroscience, Neural Networks, Machine Learning
**Technique:** Neural Network
**Application:** Brain Signal Analysis

## Methodology

### Approach

Based on the paper's contributions, the core methodology involves:

1. **Problem Formulation:** Scaling data and artificial neural networks has transformed AI, driving breakthroughs in language and vision.
2. **Key Innovation:** OmniMouse achieves state-of-the-art performance, outperforming specialized baselines across nearly all evaluation regimes.
3. **Evaluation:** Experimental validation with quantitative results.

### Implementation Considerations

```python
# Key concepts from the paper
# Reference: arXiv:2604.18827

# Note: This is a conceptual framework based on the paper abstract.
# For full implementation details, refer to the original paper.

import numpy as np

class Omnimousescalingpropertiesmult:
    """
    Framework based on: OmniMouse: Scaling properties of multi-modal, multi-task Brain Models on 150B Neural Tokens
    arXiv: 2604.18827
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

- OmniMouse achieves state-of-the-art performance, outperforming specialized baselines across nearly all evaluation regimes.

- We find that performance scales reliably with more data, but gains from increasing model size saturate.


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

- Konstantin F. Willeke et al. (2026). "OmniMouse: Scaling properties of multi-modal, multi-task Brain Models on 150B Neural Tokens." arXiv:2604.18827.

## Activation Keywords

- brain, cortex, decoding, driving, multi-modal, neural, neurons, scaling
- arXiv:2604.18827

---
*Generated: 2026-04-23 | Source: arXiv automated research workflow*
