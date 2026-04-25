---
name: computational-lesions-multilingual-language-models-separate
description: Computational lesion analysis using multilingual LLMs to separate shared and language-specific brain alignment. Targets parameter subsets important for cross-language vs. language-specific processing, revealing shared backbone with embedded specializations in the human brain. April 2026 update.
version: 1.1.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    source_paper: "Computational Lesions in Multilingual Language Models Separate Shared and Language-specific Brain Alignment (arXiv:2604.10627)"
    authors: "Yang Cui, Jingyuan Sun, Yizheng Sun, Yifan Wang, Yunhao Zhang, Jixing Li, Shaonan Wang, Hongpeng Zhou, John Hale, Chengqing Zong, Goran Nenadic"
    published: "2026-04-12"
    citations: 0
    tags: [neural-encoding, LLM, multilingual, brain-alignment, computational-lesion, fMRI, language-processing, cross-language]
    arxiv_id: "2604.10627"
---

# Computational Lesions for Multilingual Brain-Model Alignment

## Overview

This paper introduces **computational lesion analysis** as a causal framework for studying how multilingual language models align with human brain responses across languages. By creating targeted "lesions" (zeroing specific parameter subsets) in LLMs, researchers can distinguish between:

1. **Shared core parameters** — important for processing across all languages
2. **Language-specific parameters** — specialized for individual languages

**Key finding**: Lesioning a compact shared core reduces whole-brain encoding correlation by **60.32%** relative to intact models, while language-specific lesions preserve cross-language separation but selectively weaken brain predictivity for the matched native language. This supports a **shared backbone with embedded specializations** architecture for human language processing.

## Methodology

### Computational Lesion Framework

The approach treats LLMs as controllable proxy systems for human language processing:

```
┌─────────────────────────────────────────────────────┐
│              Computational Lesion Pipeline           │
├─────────────────────────────────────────────────────┤
│                                                      │
│  1. Train multilingual encoding model on fMRI data  │
│     (English, Chinese, French; 112 participants)     │
│                                                      │
│  2. Identify important parameters via saliency       │
│     - Shared importance: across all languages        │
│     - Language-specific: high for one language       │
│                                                      │
│  3. Create targeted lesions                          │
│     - Shared core lesion: zero shared parameters     │
│     - Language-specific lesion: zero L-specific      │
│                                                      │
│  4. Compare intact vs. lesioned brain predictivity   │
│     - Whole-brain encoding correlation               │
│     - Cross-language embedding separation            │
│     - Regional vulnerability analysis                │
│                                                      │
└─────────────────────────────────────────────────────┘
```

### Parameter Importance Scoring

```python
import torch
import torch.nn as nn
from typing import Dict, List, Tuple

class ComputationalLesionAnalyzer:
    """Analyze LLM parameters for cross-language vs. language-specific importance."""
    
    def __init__(self, model: nn.Module, languages: List[str]):
        self.model = model
        self.languages = languages
        self.param_importance = {}  # lang -> {param_name: importance_score}
        
    def compute_gradient_importance(self, dataloader, language: str) -> Dict[str, torch.Tensor]:
        """
        Compute parameter importance via gradient-based saliency.
        
        Args:
            dataloader: fMRI encoding data for a specific language
            language: language identifier (e.g., 'en', 'zh', 'fr')
            
        Returns:
            Dictionary mapping parameter names to importance scores
        """
        importance = {}
        
        # Compute encoding performance (brain predictivity)
        self.model.eval()
        total_loss = 0
        
        for batch in dataloader:
            stimulus_embeddings, fmri_responses = batch
            predictions = self.model(stimulus_embeddings)
            loss = self._encoding_loss(predictions, fmri_responses)
            total_loss += loss.item()
            
            # Backward to get gradients
            loss.backward()
            
            for name, param in self.model.named_parameters():
                if param.grad is not None:
                    if name not in importance:
                        importance[name] = 0
                    importance[name] += (param.grad ** 2).sum().item()
            
            self.model.zero_grad()
        
        # Normalize importance scores
        for name in importance:
            importance[name] /= total_loss + 1e-8
            
        self.param_importance[language] = importance
        return importance
    
    def identify_shared_vs_language_specific(
        self, 
        top_k_fraction: float = 0.05
    ) -> Tuple[Dict[str, torch.Tensor], Dict[str, Dict[str, torch.Tensor]]]:
        """
        Identify shared core parameters and language-specific parameters.
        
        Args:
            top_k_fraction: fraction of top parameters to consider
            
        Returns:
            shared_params: parameters important across all languages
            language_specific_params: {lang: important_params}
        """
        all_importance = {}  # param_name -> {lang: score}
        
        for lang, importance in self.param_importance.items():
            for param_name, score in importance.items():
                if param_name not in all_importance:
                    all_importance[param_name] = {}
                all_importance[param_name][lang] = score
        
        # Rank parameters for each language
        lang_top_params = {}
        for lang in self.languages:
            sorted_params = sorted(
                self.param_importance[lang].items(),
                key=lambda x: x[1], reverse=True
            )
            top_k = int(len(sorted_params) * top_k_fraction)
            lang_top_params[lang] = set(p[0] for p in sorted_params[:top_k])
        
        # Shared: in top-K for ALL languages
        shared_params = set.intersection(*lang_top_params.values())
        
        # Language-specific: in top-K for one language but not others
        language_specific = {}
        for lang in self.languages:
            other_langs = set(self.languages) - {lang}
            specific = lang_top_params[lang]
            for other in other_langs:
                specific -= lang_top_params[other]
            language_specific[lang] = specific
        
        return shared_params, language_specific
    
    def apply_lesion(
        self, 
        param_names: set,
        lesion_type: str = "zero"
    ) -> Dict[str, torch.Tensor]:
        """
        Apply targeted lesion to identified parameters.
        
        Args:
            param_names: set of parameter names to lesion
            lesion_type: 'zero' (set to 0) or 'randomize' (random noise)
            
        Returns:
            Dictionary of saved original values for recovery
        """
        saved_values = {}
        
        for name, param in self.model.named_parameters():
            if name in param_names:
                saved_values[name] = param.data.clone()
                if lesion_type == "zero":
                    param.data.zero_()
                elif lesion_type == "randomize":
                    param.data = torch.randn_like(param.data) * param.data.std()
        
        return saved_values
    
    def recover_lesion(self, saved_values: Dict[str, torch.Tensor]):
        """Recover original parameter values after lesion experiment."""
        for name, value in saved_values.items():
            for param_name, param in self.model.named_parameters():
                if param_name == name:
                    param.data.copy_(value)
                    break
    
    def evaluate_lesion_impact(
        self,
        dataloader,
        language: str
    ) -> Dict[str, float]:
        """
        Evaluate the impact of a lesion on brain predictivity.
        
        Returns:
            Dictionary with encoding metrics
        """
        self.model.eval()
        all_predictions = []
        all_responses = []
        
        with torch.no_grad():
            for batch in dataloader:
                stimulus_embeddings, fmri_responses = batch
                predictions = self.model(stimulus_embeddings)
                all_predictions.append(predictions)
                all_responses.append(fmri_responses)
        
        predictions = torch.cat(all_predictions)
        responses = torch.cat(all_responses)
        
        # Compute brain predictivity (Pearson correlation per voxel)
        correlations = torch.cat([
            self._pearson_corr(predictions[:, i], responses[:, i]).unsqueeze(0)
            for i in range(predictions.shape[1])
        ])
        
        return {
            'mean_correlation': correlations.mean().item(),
            'median_correlation': correlations.median().item(),
            'voxelwise_correlations': correlations.numpy(),
            'language': language
        }
```

### Experimental Protocol

1. **Encoding Model**: Train ridge regression or neural network to predict fMRI from LLM representations
2. **Naturalistic Stimuli**: ~100 minutes of story listening per language
3. **Participants**: 112 participants across 3 languages (English, Chinese, French)
4. **Lesion Types**:
   - **Shared core lesion**: Zero parameters important across all languages
   - **Language-specific lesion**: Zero parameters important for one specific language
5. **Metrics**:
   - Whole-brain encoding correlation change (%)
   - Cross-language embedding separation
   - Regional vulnerability (which brain areas are most affected)

## Key Findings

| Finding | Result |
|---------|--------|
| Shared core lesion effect | 60.32% reduction in whole-brain encoding correlation |
| Language-specific lesion | Preserves cross-language separation in embedding space |
| Selective weakening | Matched native language predictivity drops most |
| Architecture implication | Shared backbone with embedded language specializations |

## Applications

- **Multilingual brain-computer interfaces**: Understanding shared vs. language-specific neural representations
- **Cross-lingual NLP model design**: Informing architecture choices for multilingual models
- **Cognitive neuroscience of language**: Causal evidence for shared/specialized processing
- **Neuro-linguistic modeling**: Bridging LLM representations with brain responses

## Activation Keywords

- computational lesion, multilingual brain alignment, language-specific processing
- shared backbone, embedded specializations, cross-language encoding
- LLM-brain predictivity, neural encoding fMRI, language network
- 触发词：计算损伤、多语言脑对齐、语言特异性、共享骨干、脑模型对齐

## Limitations

- fMRI has limited temporal resolution for fast language processing dynamics
- Lesioning is binary (zero vs. intact); does not capture graded importance
- Naturalistic stimuli may not isolate specific linguistic processes
- Encoding models approximate but do not fully capture neural computation

## References

- Original paper: arXiv:2604.10627 (2026-04-12)
- Authors: Cui et al., University of Manchester, CAS, CityU Hong Kong, JHU

## Related Skills

- [[neural-encoding-evaluation-ground-truth]] - Neural encoding model evaluation framework
- [[neural-encoding-evaluation-meeg]] - M/EEG encoding model evaluation
- [[convergent-representations-linguistic-constructions]] - Linguistic constructions in brain
- [[in-context-brain-decoding]] - Meta-learning approach for brain decoding