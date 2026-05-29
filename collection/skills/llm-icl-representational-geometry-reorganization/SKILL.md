---
name: llm-icl-representational-geometry-reorganization
description: Large language models reorganize representational geometry during in-context learning — geometric account of ICL linking neuroscience untangling perspective to LLM behavior. Use when studying ICL mechanisms, neural representation geometry, or LLM-neuroscience alignment.
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.28854"
  published: "2026-05-16"
  authors: "Hua-Dong Xiong, Li Ji-An, Robert C. Wilson, Kwonjoon Lee, Xue-Xin Wei"
  tags: [in-context-learning, representational-geometry, LLM, neuroscience, untangling, prototype-algorithm, RSA]
---

# Large Language Models Reorganize Representational Geometry During In-Context Learning

**arXiv:2605.28854** | Submitted: 2026-05-16 | Categories: cs.CL, cs.LG, q-bio.NC

## Core Innovation

### Neuroscience Viewpoint Integration
This work bridges **LLM research** with **neuroscience** by applying the concept of **representation untangling** (how neural populations separate task-relevant information) to understand in-context learning (ICL) in LLMs.

**Key Hypothesis**: ICL effectiveness depends on successful **online untangling** of task-relevant representations in the model's internal representation space.

### Geometric Account of ICL
- **Representation Structure**: ICL performance correlates systematically with the representational structure of underlying classification tasks
- **Geometric Reorganization**: Successful ICL is accompanied by geometric changes that **increase online separability** of task-relevant representations
- **Prototype-like Algorithm**: LLMs use evidence integration while reshaping representations to support classification

## Key Findings

1. **Geometric Constraint**: Representational geometry is a **mechanistic constraint** on ICL effectiveness
2. **Online Untangling**: ICL requires reshaping representations to increase separability
3. **Prototype Behavior**: LLMs implement prototype-like classification during ICL
4. **Gap Quantification**: There's a measurable gap between pretrained representations and what ICL can exploit

## Methodology

### RSA-Based Analysis
```python
# Representational Similarity Analysis
import numpy as np
from scipy.spatial.distance import pdist, squareform

def compute_rdm(representations):
    """Compute Representational Dissimilarity Matrix"""
    return squareform(pdist(representations, metric='correlation'))

def geometry_shift(rdm_before, rdm_after):
    """Measure geometric reorganization"""
    evals_before = np.linalg.eigvalsh(rdm_before)
    evals_after = np.linalg.eigvalsh(rdm_after)
    return evals_after - evals_before
```

## Applications

- **LLM Research**: Design ICL tasks with favorable representational geometry
- **Neuroscience Alignment**: Bridge neural population untangling with LLM behavior
- **Model Design**: Pretraining objectives that create untangling-friendly representations

## Key Metrics

| Metric | Interpretation |
|--------|----------------|
| RDM Correlation | Similarity of representational structure |
| Eigenvalue Spectrum | Dimensionality, variance distribution |
| Separability (SVM) | Task-relevant information extraction |
| Geometry Shift | Online untangling magnitude |

## References

- arXiv:2605.28854
- DOI: https://doi.org/10.48550/arXiv.2605.28854