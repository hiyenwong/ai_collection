---
name: convergent-evolution-algorithmic-space
title: Convergent Evolution in Algorithmic Space
version: 1.0.0
description: Framework for analyzing convergent evolution in neural network weight structures during training. Uses matching-based comparison with permutation-invariant features and Hungarian matching to align hidden neurons, then applies structural distance metrics to identify task-specific attractors in weight space.
trigger_words:
  - convergent evolution neural networks
  - structural weight space analysis
  - task-specific attractors
  - neural network morphogenesis
  - permutation-invariant neuron alignment
authors:
  - Patrick Krauss
  - Achim Schilling
  - Andreas Maier
  - Thomas Kinfe
  - Henri Stübner
  - Niklas Römmelt
  - Claus Metzner
arxiv_id: 2608.05985
date: 2026-08-06
domain: computational neuroscience
---

# Convergent Evolution in Algorithmic Space

## Overview
This methodology addresses whether neural networks with different random initializations develop similar internal weight structures when trained on the same task, analogous to convergent evolution in biology. The framework overcomes the technical challenge that hidden neurons can be arbitrarily permuted without changing the represented function.

## Core Methodology

### 1. Neuron Alignment Framework
- **Coarse Alignment**: Use permutation-invariant features to initially align hidden neurons between networks
- **Refined Matching**: Apply iterative Hungarian matching algorithm to optimize neuron correspondence
- **Structural Distance Metrics**: Compare aligned networks using metrics that emphasize task-relevant weight patterns

### 2. Key Findings
- Networks trained on the same task remain closer to each other than to networks trained on different tasks
- Task-specific training guides initially random networks toward distinct regions (attractors) in structural network space
- Early learning phase shows rapid accuracy improvement before strong task-specific structural separation is visible
- Individual weight entries begin coordinated drift early, suggesting subtle distributed adjustments affect function while coarse morphology remains unchanged

### 3. Applications
- **Neural Network Analysis**: Compare ensembles of MLPs trained on different datasets (MNIST, Fashion-MNIST, KMNIST)
- **Training Dynamics**: Study morphogenesis during early phases of neural network training
- **Architecture Comparison**: Analyze how different architectures converge to similar or different structural solutions
- **Transfer Learning**: Understand structural similarities between source and target task networks

## Implementation Steps

### Step 1: Prepare Network Ensembles
```python
# Train multiple networks with different random seeds on same task
networks = []
for seed in range(num_networks):
    net = train_network(dataset=task_dataset, seed=seed)
    networks.append(net)
```

### Step 2: Extract Permutation-Invariant Features
- Compute layer-wise statistics (mean, variance, higher moments)
- Calculate activation patterns across validation set
- Extract spectral properties of weight matrices

### Step 3: Coarse Neuron Alignment
- Cluster neurons based on invariant features
- Create initial correspondence mapping between networks

### Step 4: Hungarian Matching Refinement
- Define cost matrix based on feature distances
- Apply Hungarian algorithm iteratively to optimize alignment
- Validate alignment quality using reconstruction error

### Step 5: Structural Distance Calculation
- Compute pairwise distances between aligned networks
- Use metrics like Frobenius norm, cosine similarity, or custom task-relevant measures
- Visualize network relationships in structural space

## Pitfalls and Considerations

### Common Issues
- **Permutation Sensitivity**: Direct weight matrix comparison is meaningless due to neuron permutation symmetry
- **Scale Differences**: Networks may have different weight scales even with same architecture
- **Architecture Mismatch**: Method assumes same architecture; cross-architecture comparison requires additional steps

### Best Practices
- Always validate alignment quality before computing distances
- Use multiple invariant features for robust coarse alignment
- Consider both local (individual weights) and global (layer statistics) structural properties
- Account for training dynamics by analyzing networks at multiple checkpoints

## Verification

### Expected Results
- Networks trained on same task should cluster together in structural distance space
- Task-specific separation should increase with training progress
- Early training phase should show functional improvement before structural convergence

### Validation Metrics
- Classification accuracy correlation with structural distance
- Clustering quality metrics (silhouette score, Davies-Bouldin index)
- Statistical significance testing of distance distributions

## References
- Original paper: arXiv:2608.05985 [q-bio.NC]
- Related work on neural network geometry and representation learning
- Hungarian algorithm implementations for optimal assignment problems

## Use Cases
Use this methodology when:
- Analyzing neural network training dynamics and convergence patterns
- Comparing structural similarities between networks trained on different tasks
- Studying the relationship between function and structure in neural networks
- Investigating early morphogenesis during neural network training
- Understanding task-specific attractors in weight space