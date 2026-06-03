---
name: m3d-bfs-multimodal-brain-network
description: "M3D-BFS: Multi-stage Dynamic Fusion Strategy for sample-adaptive multi-modal brain network analysis. Integrates structural and functional connectivity with dynamic fusion weights. Activation: M3D-BFS, multimodal brain network, SC-FC fusion, dynamic fusion."
---

# M3D-BFS: Multi-stage Dynamic Fusion for Brain Network Analysis

## Description
M3D-BFS introduces sample-adaptive fusion for multi-modal brain network analysis, dynamically adjusting fusion weights based on individual sample characteristics.

Key innovations:
- Sample-Adaptive Fusion: Dynamic weight adjustment per sample
- Multi-stage Strategy: Progressive feature integration
- Brain Network Specific: Designed for SC-FC integration
- Disorder Diagnosis: Optimized for clinical applications

## Paper Reference
- Title: M3D-BFS: a Multi-stage Dynamic Fusion Strategy for Sample-Adaptive Multi-Modal Brain Network Analysis
- Authors: Rui Dong et al.
- arXiv: 2604.01667v1

## Core Methodology

### Multi-modal Fusion Framework
```
Structural Connectivity ----|
                            |---> Feature Extractors ---> Dynamic Fusion ---> Classification
Functional Connectivity ----|      (GNN/CNN)           (Attention-based)
```

## Activation Keywords
- M3D-BFS
- multimodal brain network
- SC-FC fusion
- dynamic fusion
- brain connectivity
- sample-adaptive

## Applications
1. Brain Disorder Diagnosis (ASD, Alzheimer's, Parkinson's)
2. Brain Development Studies
3. Brain-Computer Interfaces

## Technical Specifications
- Input: DTI SC (90x90 to 116x116) and fMRI FC matrices
- Accuracy: 85-95% on benchmark datasets
- AUC: 0.90-0.98 for disorder classification

## Related Skills
- brain-connectivity-analysis
- brain-graph-neural
- multimodal-brain-connectivity-gnn

_Last updated: 2026-04-16_
