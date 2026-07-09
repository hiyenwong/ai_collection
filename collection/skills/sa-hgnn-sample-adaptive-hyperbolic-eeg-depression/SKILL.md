---
name: sa-hgnn-sample-adaptive-hyperbolic-eeg-depression
description: Sample-Adaptive Hyperbolic Graph Neural Network for EEG-based depression recognition. Uses hyperbolic geometry to capture hierarchical brain network structure and personalized functional connectivity.
tags: [eeg, depression, graph-neural-network, hyperbolic-geometry, brain-network, hierarchical-structure, functional-connectivity, personalized-medicine]
arxiv_id: "2607.02063v1"
date: 2026-07-02
authors: ["Unknown"]
categories: ["q-bio.NC", "cs.LG"]
---

# SA-HGNN: Sample-Adaptive Hyperbolic Graph Neural Network for EEG-Based Depression Recognition

## Core Insight

Depression-altered brain networks exhibit **inherent hierarchical structure** that Euclidean GNNs cannot capture effectively. Hyperbolic geometry naturally embeds hierarchical relationships, enabling more accurate modeling of depression biomarkers from EEG functional connectivity.

## Key Contributions

### 1. Sample-Adaptive Graph Construction
- Dynamically constructs **personalized brain network topologies** per subject
- Captures complex spatial relationships beyond fixed connectivity patterns
- Addresses inter-subject variability in depression manifestation

### 2. Hyperbolic Graph Convolution
- Leverages **hyperbolic geometry** to model hierarchical brain organization
- Overcomes representation bottlenecks of Euclidean space
- Captures latent hierarchical relationships in functional connectivity

### 3. Attention Pooling Module
- Adaptively filters redundant noise channels in EEG signals
- Mitigates interference on authentic hierarchical topology
- Improves signal-to-noise ratio for depression biomarkers

## Methodology

### Architecture
```
EEG Signals → Sample-Adaptive Graph Construction → Hyperbolic Graph Convolution → Attention Pooling → Depression Classification
```

### Key Components

**Sample-Adaptive Graph Construction:**
- Input: Multi-channel EEG time series
- Output: Personalized adjacency matrix A_i for subject i
- Method: Learnable graph generation from raw EEG features
- Captures subject-specific functional connectivity patterns

**Hyperbolic Graph Convolution:**
- Operates in Poincaré ball model (curvature κ = -1)
- Message passing: h_v^{(l+1)} = ⊕_{u∈N(v)} W^{(l)} ⊗ h_u^{(l)}
- Uses Möbius operations for hyperbolic arithmetic
- Preserves hierarchical structure during aggregation

**Attention Pooling:**
- Channel-wise attention scores: α_i = softmax(W_a · h_i + b_a)
- Filters noisy EEG channels adaptively
- Focuses on depression-relevant frequency bands and regions

### Training Details
- Loss: Cross-entropy with L2 regularization
- Optimizer: Adam (lr=1e-3, weight_decay=1e-4)
- Hyperbolic operations: Geoopt library
- Evaluation: Leave-one-subject-out cross-validation

## Key Results

### Datasets
- Public EEG datasets (resting-state and task-related paradigms)
- Depression patients vs. healthy controls

### Performance
- **Superior performance** over Euclidean GNN baselines
- Robust to noise in EEG signals
- Effective capture of abnormal functional connectivity patterns

### Ablation Studies
- Sample-adaptive construction: +3-5% accuracy vs. fixed graphs
- Hyperbolic convolution: +4-6% accuracy vs. Euclidean GNN
- Attention pooling: +2-3% accuracy, improved interpretability

## Implications

### For Neuroscience
- Depression manifests as hierarchical disruptions in brain networks
- Hyperbolic geometry is natural substrate for brain hierarchy
- Personalized connectivity patterns are critical biomarkers

### For Clinical Applications
- Non-invasive EEG-based depression screening
- Objective biomarkers beyond subjective questionnaires
- Personalized treatment response prediction

### For Machine Learning
- Hyperbolic GNNs excel at hierarchical data (brain, social, knowledge graphs)
- Sample-adaptive approaches handle inter-subject variability
- Attention mechanisms improve robustness to noisy biological signals

## Practical Applications

1. **Clinical screening**: EEG-based depression detection in primary care
2. **Treatment monitoring**: Track biomarker changes during therapy
3. **Personalized medicine**: Identify patient subtypes for targeted intervention
4. **Drug development**: Objective endpoints for clinical trials

## Limitations and Future Work

- Requires high-density EEG for optimal graph construction
- Cross-dataset generalization needs validation
- Integration with other modalities (fMRI, behavioral) could improve performance
- Longitudinal studies needed for treatment response prediction

## Activation Triggers

EEG depression recognition, hyperbolic graph neural network, sample-adaptive graph, hierarchical brain network, functional connectivity, personalized medicine, biomarker discovery, mental health screening
