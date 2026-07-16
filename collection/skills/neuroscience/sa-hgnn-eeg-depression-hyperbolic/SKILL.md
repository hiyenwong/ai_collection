---
name: sa-hgnn-eeg-depression-hyperbolic
description: >
  Sample-Adaptive Hyperbolic Graph Neural Network (SA-HGNN) for EEG-based depression
  recognition. Combines sample-adaptive graph construction with hyperbolic graph convolution
  and attention pooling to capture hierarchical brain network structure in EEG signals.
version: 1.0.0
author: Hermes Agent (from arXiv:2607.02063v1)
license: MIT
metadata:
  hermes:
    tags: [eeg, depression, hyperbolic-gnn, graph-neural-network, brain-network,
      sample-adaptive, attention-pooling, functional-connectivity]
    trigger_words: [sa-hgnn, sample-adaptive hyperbolic, eeg depression recognition,
      hyperbolic graph convolution, attention pooling, brain network topology,
      functional connectivity hierarchy, euclidean bottleneck, noise channel filtering]
  paper:
    arxiv_id: "2607.02063v1"
    title: "SA-HGNN: Sample-Adaptive Hyperbolic Graph Neural Network for EEG-Based Depression Recognition"
    authors: ["Yang Li", "Pan Hu", "Yan Zhang", "Wenfan Yang", "Lianbo Guo", "Tao Wu"]
    published: "2026-07-02"
    categories: ["cs.LG", "cs.AI"]
---

# SA-HGNN: Sample-Adaptive Hyperbolic Graph Neural Network for EEG-Based Depression Recognition

## Paper

- **Title**: SA-HGNN: Sample-Adaptive Hyperbolic Graph Neural Network for EEG-Based Depression Recognition
- **Authors**: Yang Li, Pan Hu, Yan Zhang, Wenfan Yang, Lianbo Guo, Tao Wu
- **Affiliation**: School of Software Engineering, Huazhong University of Science and Technology
- **arXiv**: 2607.02063v1 [cs.LG, cs.AI] (2026-07-02)
- **License**: CC BY 4.0

## Core Problem

EEG-based depression recognition using GNNs faces two key challenges:

1. **Hierarchical structure bottleneck**: Functional connectivity in depression-affected brain networks has inherent hierarchical organization that Euclidean GNNs cannot capture accurately
2. **Static topology limitation**: Traditional methods use fixed brain network graphs, failing to capture sample-specific (individual) spatial relationships and complex connectivity patterns

## SA-HGNN Architecture

Three core modules:

### 1. Sample-Adaptive Graph Construction

Dynamically constructs **personalized brain network topologies** per sample:

- **Physical Prior Branch**: Incorporates neurophysiological priors (spatial proximity, frequency band coherence)
- **Sample-Specific Correlation Branch**: Learns subject-specific functional connectivity from EEG data
- **Fusion & Normalization**: Combines both branches with adaptive weighting

**Key insight**: Each EEG sample has unique functional connectivity — fixed graphs lose individual diagnostic signals.

### 2. Hyperbolic Graph Convolution

Overcomes **Euclidean representation bottleneck**:

- Maps nodes between Euclidean and hyperbolic space (Poincaré ball model)
- Hyperbolic geometry naturally represents **hierarchical/tree-like structures** (exponential growth of space)
- Depression-affected brain networks exhibit hierarchical organization → hyperbolic space is a better fit than Euclidean

```
Euclidean space → Hyperbolic space → Graph Conv → Map back
     (input)        (Poincaré ball)   (message passing)  (output)
```

**Why hyperbolic?** Tree-like hierarchical structures have exponential branching — hyperbolic space has exponential volume growth, enabling distortion-free embedding. Euclidean space requires distortion for the same structures.

### 3. Attention Pooling

Adaptively filters **redundant noise channels**:

- **Node Scoring**: Multi-head attention scores each EEG channel by diagnostic relevance
- **Coarsened Graph**: Selects high-scoding channels, constructs coarsened graph
- **AP Uniformity Loss**: Regularizes attention distribution to prevent channel collapse

**Key benefit**: EEG has inherent noise and redundant channels — attention pooling focuses on diagnostically meaningful signals.

## Pipeline

```
Raw EEG → Temporal Feature Extraction → Sample-Adaptive Graph Construction
                                                ↓
                                        Hyperbolic Graph Convolution
                                                ↓
                                        Attention Pooling
                                                ↓
                                        Classifier (Depression Recognition)
```

## Experimental Results

- Evaluated on public EEG datasets for depression recognition
- Outperforms baseline GNN methods (standard GCN, GAT, Euclidean GNNs)
- Ablation studies confirm contribution of each module:
  - Sample-adaptive graph: +X% accuracy over fixed graph
  - Hyperbolic convolution: +Y% over Euclidean convolution
  - Attention pooling: +Z% over uniform pooling

## Key Takeaways

1. **Hyperbolic geometry for brain networks**: Depression affects brain network hierarchy → hyperbolic GNNs are better suited than Euclidean
2. **Sample-adaptive > fixed topology**: Individual connectivity patterns matter for diagnosis
3. **Noise-aware processing**: Attention pooling effectively handles EEG's inherent noisiness
4. **End-to-end trainable**: All modules (graph construction, hyperbolic conv, attention) are differentiable

## Application Patterns

### EEG-Based Clinical Screening
- Use SA-HGNN for automated depression screening from resting-state EEG
- Sample-adaptive graph handles inter-subject variability
- Hyperbolic convolution captures depression-specific hierarchical changes

### Generalized Brain Network Analysis
- Replace SA-HGNN's task-specific classifier for other neurological conditions
- Hyperbolic graph construction applicable to any hierarchical brain network analysis
- Attention pooling generalizes to any noisy multi-channel neurophysiological data

### Multi-Modal Fusion
- Combine SA-HGNN EEG features with fMRI, behavioral, or clinical data
- Sample-adaptive graph construction can incorporate multi-modal edges

## Implementation Considerations

- **Hyperbolic operations**: Requires specialized math (Poincaré ball exponential/log maps, Möbius addition)
- **Numerical stability**: Hyperbolic operations near ball boundary can be unstable — clamp distances
- **Computational cost**: Hyperbolic ops are more expensive than Euclidean — consider mixed precision
- **Graph construction**: Balance between physical prior (stable but rigid) and data-driven (flexible but noisy)
- **Attention regularization**: AP Uniformity Loss prevents attention collapse to single channel

## Trigger Words

sa-hgnn, sample-adaptive hyperbolic, eeg depression recognition, hyperbolic graph convolution,
attention pooling, brain network topology, functional connectivity hierarchy, euclidean bottleneck,
noise channel filtering, poincare ball, hyperbolic geometry, graph neural network,
depression classification, resting-state eeg, multi-channel eeg
