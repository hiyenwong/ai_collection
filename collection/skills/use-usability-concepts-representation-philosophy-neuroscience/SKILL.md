---
name: use-usability-concepts-representation-philosophy-neuroscience
description: "Representations play a central role in the study of both biological and artificial intelligence, as well as philosophy of mind. Across neuroscience, computer science, and philosoph... Activation: cognitive, neural, neuroscience"
---

# Use and usability: concepts of representation in philosophy, neuroscience, cognitive science, and computer science

## Overview

Representations play a central role in the study of both biological and artificial intelligence, as well as philosophy of mind. Across neuroscience, computer science, and philosophy, a recurring theme is that representations not only carry information but should be ``useful'' for or ``usable'' by an agent in some sense. Here, we review how the ``usefulness'' of representations has been conceptualized and how it figures into different conceptions of representation. We identify and explore four aspects of use and usability: representations generally carry \textit{information}; that information m

## Source Paper

- **Title:** Use and usability: concepts of representation in philosophy, neuroscience, cognitive science, and computer science
- **Authors:** Ben Baker, Richard D. Lange, Andrew Richmond et al.
- **arXiv:** [2604.13829v1](https://arxiv.org/abs/2604.13829v1)
- **Published:** 2026-04-15
- **Categories:** cs.OH
- **PDF:** [Download](https://arxiv.org/pdf/2604.13829v1)

## Core Concepts

### Key Contributions

### 1. Representations play a central role in the study of both biological and artificial intelligence, as well as philosophy of mind.
### 2. Across neuroscience, computer science, and philosophy, a recurring theme is that representations not only carry information but should be ``useful'' f
### 3. Here, we review how the ``usefulness'' of representations has been conceptualized and how it figures into different conceptions of representation.

### Methodology

Primary methods: See paper for methodology details

## Implementation

```python
# Example implementation skeleton based on Use and usability: concepts of representation in philosophy, neuroscience, cognitive science, and computer science
import torch
import torch.nn as nn

class UseUsabilityConceptsRepresentationPhilosophyNeuroscienceModel(nn.Module):
    """
    Model architecture inspired by the paper:
    Use and usability: concepts of representation in philosophy, neuroscience, cognitive science, and computer science
    """
    def __init__(self, input_dim=128, hidden_dim=256, output_dim=10):
        super().__init__()
        # Core components based on: See paper for methodology details
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
        )
        self.head = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, x):
        features = self.encoder(x)
        return self.head(features)
```

## Practical Applications



## References

- Ben Baker et al. (2026). "Use and usability: concepts of representation in philosophy, neuroscience, cognitive science, and computer science." arXiv:2604.13829v1.

## Activation Keywords

- cognitive, neural, neuroscience
