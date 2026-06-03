---
name: llm-eeg-graph-refinement
description: LLM as Clinical Graph Structure Refiner for EEG seizure diagnosis. Two-stage framework using LLMs to refine graph edges for cleaner, more interpretable graph representations in automated seizure detection. Accepted by IJCAI-ECAI 2026.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [eeg, seizure-detection, graph-neural-network, llm, clinical-ai, graph-refinement]
    source_paper: "LLM as Clinical Graph Structure Refiner: Enhancing Representation Learning in EEG Seizure Diagnosis (arXiv:2604.28178)"
    citations: 0
    venue: "IJCAI-ECAI 2026"
---

# LLM-EEG Graph Refinement

## Overview

Methodology from arXiv:2604.28178 (accepted by IJCAI-ECAI 2026). Uses Large Language Models as clinical graph structure refiners to enhance EEG representation learning for automated seizure detection. Addresses the problem of redundant/irrelevant edges in graph construction from noisy EEG data.

## Core Problem

EEG signals are inherently noisy, making robust graph construction challenging. Existing methods (correlation-based or learning-based) often generate:
- Redundant edges between unrelated channels
- Irrelevant connections that impair downstream task performance
- Uninterpretable graph structures for clinical use

## Two-Stage Framework

### Stage 1: LLM-Based Edge Refinement (Verification)

1. Construct initial graph using correlation or learning-based methods
2. Extract features for each node pair:
   - Statistical features (correlation, coherence, mutual information)
   - Textual descriptions of channel properties (anatomical location, frequency band)
3. Prompt LLM to decide whether each edge should exist
4. Remove edges deemed redundant by LLM
5. Verify improvement in seizure detection accuracy

### Stage 2: Robust Graph Learning Pipeline

```
Raw EEG → Transformer Edge Predictor → MLP Scoring → Threshold → Initial Graph → LLM Refiner → Refined Graph → GNN → Seizure Classification
```

**Components:**
- **Transformer-based edge predictor**: Assigns probability scores to potential edges
- **Multilayer Perceptron (MLP)**: Processes node pair features
- **Threshold mechanism**: Determines edge existence based on probability scores
- **LLM edge set refiner**: Makes informed decisions using textual + statistical features

## Key Insights

1. **LLMs understand clinical context**: LLMs can leverage medical knowledge to identify which EEG channel connections are physiologically meaningful vs. spurious
2. **Graph quality matters more than quantity**: Fewer, cleaner edges yield better GNN performance than dense, noisy graphs
3. **Interpretability improves**: LLM-refined graphs produce more clinically meaningful connectivity patterns
4. **Two-stage validation**: First verify LLM can improve graphs, then build robust pipeline

## Implementation Pattern

```python
import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModelForCausalLLM

class EEGEdgeRefiner:
    """LLM-based EEG graph edge refinement."""
    
    def __init__(self, llm_name="meta-llama/Llama-3-8b"):
        self.tokenizer = AutoTokenizer.from_pretrained(llm_name)
        self.llm = AutoModelForCausalLLM.from_pretrained(llm_name)
    
    def extract_node_features(self, eeg_data, channel_info):
        """Extract statistical and textual features for each channel pair."""
        # Statistical features
        corr_matrix = torch.corrcoef(eeg_data)  # Channel correlations
        coherence = compute_coherence(eeg_data)  # Frequency-domain coherence
        
        features = []
        for i in range(eeg_data.shape[0]):
            for j in range(i+1, eeg_data.shape[0]):
                feat = {
                    'correlation': corr_matrix[i, j].item(),
                    'coherence': coherence[i, j].item(),
                    'channel_i': channel_info[i],  # e.g., "Fp1 (Frontal)"
                    'channel_j': channel_info[j],  # e.g., "Fp2 (Frontal)"
                }
                features.append(feat)
        return features
    
    def llm_refine_edges(self, features, threshold=0.5):
        """Use LLM to refine graph edges."""
        refined_edges = []
        
        for feat in features:
            prompt = self._build_prompt(feat)
            decision = self._query_llm(prompt)
            
            if decision['keep_edge']:
                refined_edges.append({
                    'source': feat['channel_i'],
                    'target': feat['channel_j'],
                    'weight': feat['correlation'],
                    'confidence': decision['confidence']
                })
        
        return refined_edges
    
    def _build_prompt(self, feat):
        """Build prompt for LLM edge refinement decision."""
        return f"""As a clinical neurophysiologist, evaluate whether the following EEG channel pair should have a functional connection in a seizure detection graph:

Channel 1: {feat['channel_i']}
Channel 2: {feat['channel_j']}
Correlation: {feat['correlation']:.4f}
Coherence: {feat['coherence']:.4f}

Consider: (1) anatomical proximity, (2) physiological plausibility, (3) relevance to seizure activity.

Respond with JSON: {{"keep": true/false, "confidence": 0.0-1.0, "reasoning": "..."}}"""
    
    def _query_llm(self, prompt):
        """Query LLM and parse response."""
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.llm.generate(**inputs, max_new_tokens=100)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Parse JSON response...
        return {'keep_edge': True, 'confidence': 0.8}
```

## Applications

- **Automated seizure detection**: Cleaner graphs improve GNN classification accuracy
- **Clinical decision support**: Interpretable connectivity patterns aid neurologists
- **Epilepsy focus localization**: Refined graphs highlight pathological connections
- **EEG biomarker discovery**: Remove noise-induced spurious connections

## Limitations

- LLM inference adds computational overhead
- Requires careful prompt engineering for clinical accuracy
- Performance depends on LLM's medical knowledge
- May not generalize across different EEG montages without adaptation

## References

- Li, L., Chen, Z., & Dong, Y. (2026). "LLM as Clinical Graph Structure Refiner: Enhancing Representation Learning in EEG Seizure Diagnosis." arXiv:2604.28178. Accepted by IJCAI-ECAI 2026.
- TUSZ (Temple University Seizure) dataset for evaluation

## Related Skills

- [[eeg-hopfield-emotion-energy]] - EEG-based Hopfield energy analysis
- [[brain-graph-neural]] - Graph Neural Network methods for brain connectivity
- [[explainable-gnn-eeg-neurological]] - Explainable GNN for EEG evaluation
- [[irene-eeg-seizure-detection]] - Information Bottleneck-guided EEG seizure detection

## Activation Keywords

- llm eeg graph refinement
- clinical graph structure refiner
- EEG seizure detection LLM
- graph edge refinement
- 脑电图图结构优化
- LLM 脑电图
- seizure diagnosis graph
