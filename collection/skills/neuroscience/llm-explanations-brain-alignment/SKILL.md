---
name: llm-explanations-brain-alignment
description: "Methodology for using explainable AI attribution methods to understand and predict LLM-brain alignment during language processing. Uses gradient-based attribution to quantify word contributions to LLM predictions and predict fMRI data from narrative listening tasks. Activation: LLM-brain alignment, XAI attribution, fMRI prediction, gradient attribution, conductance analysis, language neuroscience"
metadata:
  arxiv_id: "2502.14671"
  published: "2026-08-06"
  authors: "Maryam Rahimi, Mohammad Reza Daliri, Yadollah Yaghoobzadeh"
  tags: [LLM, brain alignment, XAI, attribution, fMRI, language processing, neuroscience]
license: Complete terms in LICENSE.txt
---

# LLM Explanations Brain Alignment

## Overview

This methodology demonstrates that **explainable AI (XAI) attribution methods** can be used not only to measure Large Language Model (LLM)--brain alignment but to characterize what drives this alignment. The core insight is that gradient-based attribution methods robustly align with brain activity during language processing and can predict fMRI data from participants listening to narratives.

**Key Innovation**: Attribution-based explanations outperform internal representations in early auditory regions and reveal layer-specific computational properties that map to different brain regions.

## Core Methodology

### 1. Attribution-Based Prediction Framework
- Use gradient-based attribution methods to quantify contribution of each input word to LLM's next-word predictions
- Apply these attribution scores to predict fMRI data from narrative listening tasks
- Compare attribution-based predictions against internal representations and confound controls

### 2. Conductance Layer Analysis
- Extend attribution from words to individual layers using conductance method
- Analyze what each layer's attribution reveals about model computation
- Map layer-specific attribution patterns to brain region alignment

### 3. Confound Control
- Account for acoustic and word-rate confounds in attribution-brain alignment
- Demonstrate that attribution contributes unique variance beyond basic linguistic features
- Validate robustness across different attribution methods

## Key Findings

### Attribution vs. Internal Representations
- **Gradient-based attribution** robustly aligns with brain activity
- **Outperforms internal representations** in early auditory regions
- **Contributes unique variance** beyond acoustic and word-rate confounds

### Layer-Specific Patterns
- **Early layers**: Greater word-type sensitivity, preferential alignment with auditory regions
- **Final layer**: Dominated by positional information, exhibits broad cortical alignment
- **Computational progression**: Attribution patterns reflect hierarchical processing in the brain

### Methodological Robustness
- Multiple gradient-based attribution methods show consistent results
- Results hold across different narrative datasets and participant cohorts
- Attribution provides interpretable insights into LLM-brain correspondence

## Technical Implementation

### Gradient Attribution Calculation
```python
# Example using PyTorch Captum
import torch
from captum.attr import IntegratedGradients, Saliency

def compute_word_attribution(model, input_ids, target_token_idx):
    """Compute attribution scores for input words"""
    # Integrated Gradients (recommended)
    ig = IntegratedGradients(model)
    attributions = ig.attribute(
        inputs=input_ids,
        target=target_token_idx,
        baselines=torch.zeros_like(input_ids),
        n_steps=50
    )
    return attributions.sum(dim=-1)  # Sum over embedding dimensions

def predict_fmri_from_attribution(attribution_scores, fmri_data):
    """Use attribution scores to predict fMRI responses"""
    # Linear regression or ridge regression
    from sklearn.linear_model import Ridge
    model = Ridge(alpha=1.0)
    model.fit(attribution_scores, fmri_data)
    return model.predict(attribution_scores)
```

### Conductance Layer Analysis
```python
def conductance_layer_attribution(model, input_ids, target_idx, layer_idx):
    """Compute conductance-based attribution for specific layer"""
    # Get intermediate activations
    activations = []
    def hook_fn(module, input, output):
        activations.append(output)
    
    # Register hook on target layer
    hook = model.layers[layer_idx].register_forward_hook(hook_fn)
    
    # Forward pass
    output = model(input_ids)
    
    # Compute gradients w.r.t. layer activations
    grads = torch.autograd.grad(output[0, target_idx], activations[0])
    
    # Conductance: element-wise product of activations and gradients
    conductance = activations[0] * grads[0]
    
    # Remove hook
    hook.remove()
    
    return conductance.sum(dim=-1)  # Sum over feature dimensions
```

## Applications

### Neuroscience Research
- **Brain decoding**: Predict fMRI responses from LLM attribution
- **Computational modeling**: Understand neural basis of language processing
- **Cross-species comparison**: Bridge artificial and biological language systems

### LLM Interpretability
- **Model analysis**: Characterize what LLM computations correspond to brain activity
- **Architecture evaluation**: Compare different LLM architectures based on brain alignment
- **Training dynamics**: Track how brain alignment evolves during LLM training

### Clinical Applications
- **Language disorders**: Identify neural markers of language processing deficits
- **Brain-computer interfaces**: Develop more natural language-based BCIs
- **Neurofeedback**: Use LLM attribution as feedback signal for cognitive training

## Validation Protocol

1. **Replicate core findings**: Test attribution-brain alignment in your dataset
2. **Layer-specific validation**: Verify early vs. late layer patterns
3. **Confounding control**: Account for acoustic and linguistic confounds
4. **Method comparison**: Compare multiple attribution methods (IG, Saliency, etc.)
5. **Cross-dataset validation**: Test generalization across different narrative datasets

## Pitfalls and Considerations

### Methodological Choices
- **Attribution method selection**: Integrated Gradients generally performs best
- **Baseline selection**: Zero baseline vs. neutral token baseline affects results
- **Temporal alignment**: Proper alignment between attribution and fMRI timing is crucial

### Data Quality
- **fMRI preprocessing**: Standard preprocessing pipeline required
- **Narrative quality**: Naturalistic narratives work better than artificial text
- **Participant attention**: Ensure participants are engaged during listening

### Interpretation Challenges
- **Causality vs. correlation**: Attribution-brain alignment shows association, not causation
- **Individual variability**: High inter-subject differences require careful analysis
- **Model dependence**: Results may vary across different LLM architectures

## Comparison with Traditional Methods

| Traditional Approach | Attribution-Based Approach |
|---------------------|---------------------------|
| Internal representations | Attribution scores |
| Fixed temporal windows | Dynamic word-by-word alignment |
| Limited interpretability | Direct word contribution scores |
| Single-layer focus | Multi-layer conductance analysis |

## Tools and Libraries

- **Attribution**: Captum (PyTorch), TF-Captum (TensorFlow)
- **fMRI analysis**: Nilearn, nilearn, MNE-Python
- **Statistical analysis**: SciPy, statsmodels, scikit-learn
- **Visualization**: Matplotlib, Seaborn, Plotly

## References

- Original paper: arXiv:2502.14671 (v4, August 2026)
- Integrated Gradients: Sundararajan et al. (2017)
- LLM-brain alignment literature
- fMRI language processing studies

## Activation Keywords

- LLM-brain alignment
- XAI attribution
- fMRI prediction
- gradient attribution
- conductance analysis
- language neuroscience
- neural language processing
- explainable AI neuroscience
- attribution-based decoding
- layer-specific alignment