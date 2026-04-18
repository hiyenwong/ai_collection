---
name: computational-lesions-multilingual-language-models-separate
description: "Computational lesion analysis using multilingual LLMs to probe brain alignment. Method for dissecting shared vs language-specific neural representations in LLMs via targeted ablation. Activation: computational lesions, multilingual LLM brain alignment, language-specific neural representations, lesion analysis LLM, shared representations, LLM neuroscience, brain alignment, ablation LLM"
---

# Computational Lesions in Multilingual LLMs

## Overview

This methodology uses **computational lesion analysis** to probe how multilingual Large Language Models (LLMs) represent language in their internal activations, and how these representations align with human brain activity measured via fMRI.

By selectively ablating (zeroing out) specific layers, attention heads, or neurons in multilingual LLMs, researchers can determine whether the model's internal representations are:
- **Shared across languages** (language-agnostic representations)
- **Language-specific** (unique representations per language)

This approach bridges the gap between artificial language processing and human neurobiology, revealing fundamental principles about how multilingual processing works.

## Source Paper

- **Title**: Computational Lesions in Multilingual Language Models Separate Shared and Language-Specific Brain Alignment
- **Authors**: Multiple (arXiv preprint)
- **arXiv**: 2604.08117v1 (April 2026)
- **Published**: 2026-04
- **Categories**: cs.CL, cs.AI, q-bio.NC

## Core Concepts

### 1. Computational Lesion Analysis

Adapted from neuropsychology, where brain lesions reveal function-location mapping:
- **Biological lesion**: Damage to brain region → observe behavioral deficit
- **Computational lesion**: Zero out model component → observe performance change

**Key insight**: By systematically ablating different parts of an LLM, you can map which components are responsible for which functions, just as brain lesion studies map cognitive functions to brain regions.

### 2. Shared vs Language-Specific Representations

Multilingual LLMs may process different languages in fundamentally different ways:

| Representation Type | Description | Evidence |
|---------------------|-------------|----------|
| **Shared** | Common internal code across languages | Same neurons activate for equivalent concepts in EN/FR/ZH |
| **Language-Specific** | Unique processing per language | Different neural pathways for different languages |

**Key Finding**: Some LLMs show **separable alignment patterns** where:
- Middle layers → shared representations (align with brain's language-agnostic processing)
- Outer layers → language-specific representations (align with language-specific brain regions)

### 3. Brain Alignment Measurement

The methodology uses fMRI data to validate LLM internal representations:
- Extract LLM layer activations for stimuli
- Predict brain activity from activations using encoding models
- Compare alignment scores across languages and layers

**Workflow:**
```
1. Present same stimuli in multiple languages to human subjects (fMRI)
2. Feed same stimuli through multilingual LLM
3. Extract activations from each layer
4. Train encoding model: LLM activations → brain activity
5. Compare alignment scores across languages
6. Perform computational lesions to test necessity
```

## Implementation

### Step 1: Extract Layer Activations

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def extract_layer_activations(model, tokenizer, texts, layers=None):
    """
    Extract hidden states from specific layers of a multilingual LLM.
    
    Args:
        model: Pretrained multilingual LLM (e.g., mT5, XLM-R)
        texts: List of texts in different languages
        layers: List of layer indices to extract (None = all)
    
    Returns:
        Dictionary of layer index -> activations tensor
    """
    inputs = tokenizer(texts, return_tensors="pt", padding=True)
    
    with torch.no_grad():
        outputs = model(**inputs, output_hidden_states=True)
    
    # hidden_states is a tuple: (embeddings, layer_0, layer_1, ..., final)
    all_hidden = outputs.hidden_states
    
    if layers is None:
        layers = range(len(all_hidden))
    
    return {i: all_hidden[i] for i in layers}
```

### Step 2: Compute Brain Alignment

```python
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
import numpy as np

def compute_brain_alignment(llm_activations, brain_data, alpha=1.0):
    """
    Measure how well LLM activations predict brain activity.
    
    Args:
        llm_activations: [n_samples, n_features] from LLM layer
        brain_data: [n_samples, n_voxels] fMRI data
    
    Returns:
        alignment_score: Mean cross-validated R² score
    """
    model = Ridge(alpha=alpha)
    scores = cross_val_score(model, llm_activations, brain_data, cv=5)
    return scores.mean()
```

### Step 3: Computational Lesion

```python
def perform_computational_lesion(model, tokenizer, texts, 
                                  lesion_layer, lesion_type="zero"):
    """
    Ablate a specific layer and measure impact.
    
    Args:
        lesion_layer: Index of layer to ablate
        lesion_type: "zero" (set to 0), "noise" (add noise), "shuffle"
    
    Returns:
        degraded_activations: Activations after lesion
    """
    inputs = tokenizer(texts, return_tensors="pt", padding=True)
    
    with torch.no_grad():
        outputs = model(**inputs, output_hidden_states=True)
    
    hidden = list(outputs.hidden_states)
    
    if lesion_type == "zero":
        hidden[lesion_layer] = torch.zeros_like(hidden[lesion_layer])
    elif lesion_type == "noise":
        hidden[lesion_layer] = hidden[lesion_layer] + torch.randn_like(hidden[lesion_layer])
    
    return hidden
```

### Step 4: Analyze Shared vs Language-Specific Patterns

```python
def analyze_representation_sharing(alignment_scores, languages):
    """
    Determine if representations are shared or language-specific.
    
    Args:
        alignment_scores: Dict of {language: {layer: score}}
        languages: List of language codes
    
    Returns:
        shared_layers: Layers with consistent alignment across languages
        specific_layers: Layers with language-varying alignment
    """
    all_layers = list(alignment_scores[languages[0]].keys())
    
    shared_layers = []
    specific_layers = []
    
    for layer in all_layers:
        scores = [alignment_scores[lang][layer] for lang in languages]
        variance = np.var(scores)
        
        if variance < 0.01:  # Low variance = shared
            shared_layers.append(layer)
        else:  # High variance = language-specific
            specific_layers.append(layer)
    
    return shared_layers, specific_layers
```

## Practical Applications

### 1. Probing LLM Multilingual Architecture
- Understand how models like mT5, XLM-R organize language representations
- Inform model architecture improvements for better cross-lingual transfer
- Identify which layers handle language-agnostic vs language-specific processing

### 2. Neuroscience Validation
- Test hypotheses about human multilingual processing
- Compare artificial vs biological language representation strategies
- Validate computational models of bilingual/multilingual cognition

### 3. Model Interpretability
- Map LLM internal structure to cognitive functions
- Identify which components are responsible for translation vs comprehension
- Understand cross-lingual transfer mechanisms

### 4. Clinical Applications
- Inform language disorder research (aphasia, bilingual aphasia)
- Develop better computational models of language processing deficits
- Bridge gap between computational and clinical linguistics

## Related Work

- **Brain-LM alignment**: Using fMRI to validate LLM representations
- **Mechanistic interpretability**: Understanding LLM internal mechanisms
- **Cross-lingual transfer**: How models transfer knowledge between languages
- **Computational neuropsychology**: Using models to understand brain function

## Limitations

1. **Model specificity**: Results may vary across LLM architectures
2. **Brain data quality**: fMRI has limited temporal resolution
3. **Task dependency**: Alignment patterns may be task-specific
4. **Language coverage**: Results from 2-3 languages may not generalize
5. **Causal vs correlational**: Lesion analysis shows necessity, not sufficiency

## References

- Original paper: arXiv:2604.08117v1 (2026)
- Related: Brain-LM alignment literature
- Foundational: Mechanistic interpretability research

## Activation Keywords

- computational lesions
- multilingual LLM brain alignment
- language-specific neural representations
- lesion analysis LLM
- shared representations
- LLM neuroscience
- brain alignment
- ablation LLM
- multilingual processing
- cross-lingual transfer
- mechanistic interpretability
