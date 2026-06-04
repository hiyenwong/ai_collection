---
name: computational-lesions-multilingual-language-models-separate
description: >
  Causal framework for studying multilingual brain-model alignment using targeted "computational lesions" 
  in multilingual LLMs. Zero out parameters to separate shared vs language-specific brain processing. 
  Use when: multilingual LLM analysis, brain-model alignment, fMRI encoding studies, computational lesions, 
  cross-lingual neuroscience, language processing in brain.
  Trigger: computational lesion, multilingual brain alignment, language-specific processing, 
  fMRI encoding models, shared backbone, language LLM, 多语言模型, 计算损伤.
version: 1.0.0
author: Research Synthesis (arXiv:2604.10627)
license: MIT
metadata:
  hermes:
    tags: [multilingual, LLM, brain-alignment, computational-lesion, fMRI, language-processing]
    source_paper: "Computational Lesions in Multilingual Language Models Separate Shared and Language-specific Brain Alignment (arXiv:2604.10627)"
---

# Computational Lesions for Multilingual Brain-Model Alignment

## Overview

Uses targeted "computational lesions" (zeroing small parameter sets) in multilingual LLMs to causally 
study whether brain language processing is shared across languages or language-specific.

## Key Findings

- **Shared core lesion**: Reduces whole-brain encoding correlation by 60.32% across all languages
- **Language-specific lesions**: Preserve cross-language separation but selectively weaken predictivity for matched language
- **Conclusion**: Supports "shared backbone with embedded specializations" model

## Methodology

### Experimental Design
```
6 Multilingual LLMs → Targeted Lesions → fMRI Encoding Comparison
                              │
                    ┌─────────┼─────────┐
                    ↓         ↓         ↓
              Shared Core  Language   Control
              Lesion       Specific   (intact)
                           Lesion
```

### Lesion Types
1. **Shared Core Lesion**: Zero parameters important across ALL languages
2. **Language-Specific Lesion**: Zero parameters important for ONE language only
3. **Control**: Intact model (baseline)

### fMRI Encoding
- 112 participants, 3 languages (English, Chinese, French)
- 100 minutes of naturalistic story listening per language
- Compare intact vs lesioned model brain predictivity

## Implementation Pattern

```python
def compute_lesion(model, importance_scores, threshold):
    """Create targeted computational lesion."""
    lesioned = model.clone()
    for param_name, importance in importance_scores.items():
        if importance > threshold:  # High importance = critical parameter
            param = get_parameter(lesioned, param_name)
            param.zero_()  # "Lesion" by zeroing
    return lesioned

def evaluate_brain_alignment(model, fmri_data, language):
    """Evaluate how well model predicts brain responses."""
    embeddings = model.encode(stimuli, language=language)
    encoding_scores = fit_encoding_model(embeddings, fmri_data)
    return encoding_scores

# Shared vs language-specific analysis
shared_lesion = compute_lesion(model, shared_importance, threshold)
lang_lesion = compute_lesion(model, lang_specific_importance, threshold)

shared_reduction = 1 - eval(shared_lesion) / eval(intact_model)  # ~60%
```

## Applications
- Causal analysis of multilingual processing
- Brain-model alignment studies
- Language-specific vs shared neural representations
- LLM interpretability for neuroscience

## Activation Keywords
- computational lesion, multilingual brain alignment, fMRI encoding
- language-specific processing, shared backbone, LLM neuroscience
- 计算损伤, 多语言脑对齐, 语言特异性处理

## References
- Yang Cui, Jingyuan Sun, et al. "Computational Lesions in Multilingual Language Models Separate Shared 
  and Language-specific Brain Alignment." arXiv:2604.10627
