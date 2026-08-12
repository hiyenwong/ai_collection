---
name: mpp-gnn-subject-adaptive-community-detection
version: 1.0.0
description: "MPP-GNN: Subject-Adaptive Community Detection for fMRI-Based Alzheimer's Disease Classification"
tags:
  - fMRI
  - Alzheimer's disease
  - graph neural networks
  - community detection
  - brain networks
  - subject-adaptive
  - functional connectivity
trigger_words:
  - MPP-GNN
  - subject-adaptive community detection
  - fMRI Alzheimer's classification
  - bilevel optimization GNN
  - functional module discovery
  - brain network dedifferentiation
---

# MPP-GNN Framework

## Overview
MPP-GNN (Meta Probabilistic Pooling Graph Neural Network) addresses limitations in existing GNN approaches for fMRI analysis by performing subject-adaptive community detection and using discovered brain modules as explicit priors to guide edge refinement and representation learning for Alzheimer's disease classification.

## Core Innovation

### Problem Addressed
- **Fixed Module Assumption**: Traditional methods assume preset number of functional modules across all subjects, overlooking inter-subject variability
- **Module-Connectivity Disconnect**: Discovered modules rarely used to directly guide learned connectivity patterns
- **Individual Differences**: Failure to account for personalized brain organization in disease classification

### Solution: Bilevel Optimization Framework
1. **Upper Level**: Adaptive graph partitioning to discover subject-specific functional modules
2. **Lower Level**: Edge refinement and representation learning guided by discovered modules as explicit priors
3. **Coupled Training**: Joint optimization ensures modules and connectivity patterns are mutually consistent

## Methodology

### Step 1: Input Preparation
- **Data**: fMRI time series converted to functional connectivity matrices
- **Graph Construction**: Nodes represent brain regions, edges represent functional connectivity strength
- **Preprocessing**: Standard fMRI preprocessing (motion correction, normalization, etc.)

### Step 2: Subject-Adaptive Community Detection
- **Probabilistic Pooling**: Learn soft assignments of nodes to communities
- **Hierarchical Partitioning**: Discover modules at multiple scales
- **Subject-Specific**: Each subject gets personalized community structure
- **Meta Learning**: Share statistical strength across subjects while preserving individual differences

### Step 3: Module-Guided Edge Refinement
- **Explicit Prior**: Use discovered modules to constrain edge learning
- **Within-Module Enhancement**: Strengthen connections within detected communities
- **Between-Module Modulation**: Adjust inter-module connections based on functional relationships
- **Representation Learning**: Generate node embeddings informed by modular structure

### Step 4: Classification Head
- **Graph-Level Features**: Aggregate node representations to graph-level features
- **Disease Classification**: Binary or multi-class classification for Alzheimer's disease stages
- **Interpretability**: Analyze contribution of specific modules to classification decisions

## Validation Results

### Performance Metrics
- **Dataset 1**: Achieved highest AUC compared to established baselines
- **Dataset 2**: Consistently outperformed competing methods on second public dataset
- **Robustness**: Maintained performance across different preprocessing pipelines

### Biological Validation
- **Yeo Atlas Alignment**: Significant alignment with canonical functional-network organization
- **AD Dedifferentiation**: Revealed network-level dedifferentiation pattern in Alzheimer's disease
- **Clinical Relevance**: Discovered modules correspond to known AD-affected brain networks

## Implementation Guidelines

### Architecture Components
1. **Graph Encoder**: Initial GNN layers for basic representation learning
2. **Meta Probabilistic Pooling**: Adaptive community detection module
3. **Edge Refinement**: Module-guided connectivity adjustment
4. **Classification Head**: Final prediction layer

### Training Strategy
- **Bilevel Optimization**: Alternate between upper and lower level updates
- **Meta Learning Rate**: Control transfer of information across subjects
- **Regularization**: Prevent overfitting to individual subject noise
- **Convergence Monitoring**: Track both levels independently

### Hyperparameters
- **Number of Communities**: Allow flexible range rather than fixed number
- **Pooling Ratio**: Control granularity of community detection
- **Learning Rates**: Different rates for upper and lower level optimization
- **Regularization Strength**: Balance individual adaptation vs group consistency

## Use Cases

### When to Apply MPP-GNN
- fMRI-based brain disorder classification (Alzheimer's, Parkinson's, etc.)
- Studies requiring individualized brain network analysis
- Research on functional module organization in disease states
- Applications needing interpretable GNN predictions
- Cross-subject analysis with high inter-individual variability

### Expected Benefits
- Improved classification accuracy through personalized modeling
- Enhanced interpretability via discovered functional modules
- Better biological plausibility through module-guided learning
- Robust performance across diverse subject populations
- Insights into disease-specific network reorganization patterns

## Pitfalls and Considerations

### Computational Complexity
- Bilevel optimization increases training time significantly
- Memory requirements scale with number of subjects
- Consider approximation strategies for large cohorts

### Data Requirements
- Requires sufficient fMRI data per subject for reliable connectivity estimation
- Performance may degrade with low-quality or short-duration scans
- Needs careful preprocessing to avoid artifacts

### Interpretation Challenges
- Discovered modules may not always correspond to canonical networks
- Individual variability can make group-level conclusions difficult
- Requires validation against established brain atlases

## References
- Zhang, Y., Zhou, X., Warrell, J., Holmes, A., Zhang, X., & Gerstein, M. (2026). MPP-GNN: Subject-Adaptive Community Detection for fMRI-Based Alzheimer's Disease Classification. arXiv:2607.28681 [cs.LG]
- https://doi.org/10.48550/arXiv.2607.28681
- Submitted to IEEE Transactions on Medical Imaging

## Activation Keywords
- MPP-GNN
- subject-adaptive community detection
- fMRI Alzheimer's classification
- bilevel optimization GNN
- functional module discovery
- brain network dedifferentiation
- meta probabilistic pooling
- personalized brain networks