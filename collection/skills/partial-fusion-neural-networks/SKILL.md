---
name: partial-fusion-neural-networks
title: "Partial Fusion of Neural Networks"
description: "Partial fusion of neural networks interpolating between ensembles and weight aggregation via neuron-level similarity matching and partial optimal transport. Frames partial fusion as generalized pruning where neurons are deleted or linearly combined."
arxiv: "2605.22350"
authors: ["Fabian Morelli", "Stephan Eckstein"]
published: "2026-05-21"
tags: ["model merging", "ensembles", "weight aggregation", "partial optimal transport", "neuron matching", "pruning"]
category: "ai_collection"
---

# Partial Fusion of Neural Networks: Efficient Tradeoffs Between Ensembles and Weight Aggregation

**arXiv: 2605.22350**

## Summary

Partial fusion of networks interpolates between two extremes: **ensembles** (high computational cost, high accuracy) and **weight aggregation** (low cost, lower accuracy). The core idea extends weight aggregation by leveraging **neuron-level similarity** between networks — only the weights of the most similar neurons are aggregated, while dissimilar neurons are kept separate.

## Key Concepts

### 1. Neuron Matching via Partial Optimal Transport

- Networks are aligned by computing neuron similarity across models using **partial optimal transport**
- Unlike standard weight averaging (which averages _all_ corresponding weights), partial fusion only averages weights for matched neuron pairs above a similarity threshold
- Unmatched/dissimilar neurons are retained individually, preserving diversity

### 2. Weight Aggregation ↔ Ensemble Interpolation

- **Pure ensemble**: All model outputs are combined (keep all neurons separate)
- **Full weight aggregation**: All corresponding weights are averaged (remove all neuron diversity)
- **Partial fusion**: A tunable middle ground — some neurons are aggregated, others are kept separate

### 3. Partial Fusion as Generalized Pruning of Ensembles

- The paper frames weight aggregation and partial fusion as a form of **generalized pruning** of ensemble models
- In traditional pruning, neurons are **deleted**; in partial fusion, neurons can be either **deleted** OR **linearly combined**
- This provides a smoother, more flexible accuracy–cost tradeoff than standard pruning

## Method

1. **Train multiple networks** (the ensemble members) on the same task
2. **Compute neuron similarity** across networks (e.g., using activation correlations, weight similarity, or representation similarity)
3. **Solve a partial optimal transport problem** to find matched neuron pairs and decide which neurons to fuse vs. keep separate
4. **Fuse matched neurons** by averaging their weights (or some convex combination)
5. **Keep unmatched neurons** as separate computational paths
6. **Optionally prune** low-salience fused neurons

## Use Cases

- Deploying accurate models under strict latency/memory constraints
- Model compression with better accuracy–cost Pareto frontier than pruning or distillation alone
- Federated learning where client models exhibit heterogeneity (partial fusion can handle structural misalignment better than FedAvg)

## Pitfalls & Considerations

- The neuron matching step (optimal transport) can be computationally expensive for very large networks — consider approximate solvers or minibatch matching
- The similarity metric choice strongly affects fusion quality; experiment with activation-based vs. weight-based metrics
- Partial fusion introduces architectural irregularity (variable width) that may be unfriendly to hardware accelerators — consider structured matching constraints

## Related Work

- **Weight averaging** (e.g., model soups, stochastic weight averaging)
- **Model merging** (e.g., Git Re-Basin, TIES-Merging, DARE)
- **Ensemble pruning** (selecting a subset of ensemble members)
- **Neuron alignment** techniques (optimal transport-based permutation alignment)

## References

- Morelli, F. & Eckstein, S. (2026). *Partial Fusion of Neural Networks: Efficient Tradeoffs Between Ensembles and Weight Aggregation*. arXiv:2605.22350.
