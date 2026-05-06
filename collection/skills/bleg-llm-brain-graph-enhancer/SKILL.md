---
name: bleg-llm-brain-graph-enhancer
description: BLEG (LLM-Enhanced Brain Graph Analysis) methodology. Integrates LLMs with brain graph neural networks for improved neurological disease classification via knowledge-enhanced connectivity representation.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [brain-graph, llm, gnn, neurological-disease, connectivity, multi-site]
    source_paper: "BLEG: LLM Enhanced Brain Graph Analysis for Neurological Disease Classification (arXiv:2604.12415v1)"
    created: "2026-04-18"
---

# BLEG: LLM-Enhanced Brain Graph Analysis

## Overview
BLEG integrates Large Language Models (LLMs) as knowledge enhancers for brain graph neural networks, improving disease classification by embedding clinical and neurobiological knowledge into connectivity representations. This approach bridges the gap between data-driven graph learning and domain knowledge, enabling more interpretable and generalizable brain network analysis.

## Core Concepts

### Problem Statement
Brain graph neural networks for neurological disease classification (e.g., Alzheimer's, autism, schizophrenia) typically rely solely on connectivity data without incorporating the rich clinical knowledge that neurologists use. This limits both accuracy and interpretability.

### Key Innovations
1. **LLM Knowledge Enhancement**: Use LLMs to generate textual descriptions of brain regions and their known clinical significance
2. **Knowledge-Graph Integration**: Embed LLM-derived knowledge into node features alongside connectivity data
3. **Multi-Site Generalization**: Knowledge augmentation helps the model generalize across different scanning sites and protocols
4. **Interpretability**: LLM-enhanced features provide human-readable explanations for classification decisions

### Architecture
```
┌─────────────────────┐     ┌─────────────────────┐
│   Brain Connectivity │     │   LLM Knowledge      │
│   Graph (fMRI/DTI)  │     │   (Clinical Text)    │
└────────┬────────────┘     └────────┬────────────┘
         │                           │
    ┌────▼────┐                 ┌────▼────┐
    │   GNN   │                 │  LLM    │
    │ Encoder │                 │ Encoder │
    └────┬────┘                 └────┬────┘
         │                           │
         └───────────┬───────────────┘
                     │
              ┌──────▼──────┐
              │  Knowledge   │
              │  Fusion      │
              │  Module      │
              └──────┬──────┘
                     │
              ┌──────▼──────┐
              │  Disease     │
              │  Classifier  │
              └─────────────┘
```

### Implementation Pattern
```python
class BLEG:
    def __init__(self, gnn_model, llm_encoder, fusion_dim=256):
        self.gnn = gnn_model
        self.llm_encoder = llm_encoder
        self.fusion = nn.Linear(gnn_dim + llm_dim, fusion_dim)
        
    def encode_brain_graph(self, adjacency, node_features):
        return self.gnn(adjacency, node_features)
    
    def encode_knowledge(self, clinical_descriptions):
        return self.llm_encoder(clinical_descriptions)
    
    def fuse_and_classify(self, graph_repr, knowledge_repr):
        fused = self.fusion(torch.cat([graph_repr, knowledge_repr], dim=-1))
        return self.classifier(fused)
```

## Applications
- Alzheimer's disease classification from fMRI connectivity
- Autism spectrum disorder detection
- Schizophrenia diagnosis support
- Multi-site brain network analysis
- Interpretable neurological disease prediction

## Activation Keywords
- BLEG, LLM brain graph, knowledge-enhanced GNN, brain graph analysis, neurological disease classification, LLM-GNN fusion, clinical knowledge integration, 脑图LLM增强

## References
- BLEG: LLM Enhanced Brain Graph Analysis for Neurological Disease Classification
- Authors: Multiple
- Published: 2026-04-16
- arXiv: https://arxiv.org/abs/2604.12415v1
