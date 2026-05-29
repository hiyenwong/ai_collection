---
name: sbm-optimal-transport-inference
description: "Bridging Maximum Likelihood and Optimal Transport for efficient inference in Stochastic Block Models. Uses semi-relaxed Gromov-Wasserstein projection with entropy regularization for SBM parameter estimation. Activation: stochastic block model, optimal transport inference, Gromov-Wasserstein SBM, network inference optimal transport, community detection OT."
---

# SBM Inference via Maximum Likelihood and Optimal Transport

## Source

arXiv:2605.28488 — "Bridging Maximum Likelihood and Optimal Transport for Efficient Inference and Model Selection in Stochastic Block Models"

## Problem

Stochastic Block Models (SBMs) are fundamental for community detection in networks, but:
- Maximum Likelihood Variational Inference (MLVI) is computationally expensive for large networks
- Standard variational methods may get stuck in poor local optima
- Model selection (choosing number of communities) is difficult
- No unified framework connecting likelihood-based and geometry-based inference

## Core Methodology

### OT-MLVI Connection

1. **Key insight**: MLVI for SBM can be interpreted as a semi-relaxed Gromov-Wasserstein (srGW) projection:
   - The variational objective = srGW distance between observed and model adjacency matrices
   - Entropy regularization from the variational approximation matches OT regularization
   - This connects statistical inference with geometric transport theory

2. **Algorithmic framework**:
   ```
   Given: Observed adjacency matrix A, target community structure B
   
   Step 1: Formulate srGW problem
     min_{T ∈ Π(a, b)} ⟨C_A, T⟩ - ε·H(T) + ⟨C_B, T⟩
   
   Step 2: Solve via Sinkhorn iterations (efficient for large networks)
   
   Step 3: Extract community assignments from optimal transport plan T
   
   Step 4: Model selection via OT-based criteria
     - Compare OT costs across different community numbers
     - Lower OT cost = better model fit
   ```

3. **Advantages over standard MLVI**:
   - **Faster convergence**: Sinkhorn iterations vs. EM-style updates
   - **Better global optima**: OT geometry provides smoother optimization landscape
   - **Natural model selection**: OT cost serves as information criterion
   - **Scalability**: O(n²) vs O(n³) for large networks

## Implementation Steps

1. **Preprocess**: Compute adjacency matrix and node degree distributions
2. **Set up srGW**: Define source/target cost matrices, marginals
3. **Sinkhorn optimization**: Iteratively solve with entropy regularization
4. **Extract communities**: From optimal transport plan
5. **Model selection**: Sweep over number of communities, choose minimum OT cost

## Applications

- Community detection in social networks
- Protein interaction network analysis
- Brain network community structure
- Recommender system clustering
- Knowledge graph entity grouping

## Pitfalls

- **Entropy regularization parameter**: Too large → blurry assignments; too small → numerical instability
- **Initialization sensitivity**: Still may find local optima for complex networks
- **Degree-corrected SBM**: Standard srGW assumes homogeneous degrees; requires modification
- **Dynamic networks**: Extending to time-varying SBMs needs dynamic OT formulation

## Keywords

stochastic block model, optimal transport, Gromov-Wasserstein, community detection, variational inference, network analysis, Sinkhorn algorithm, model selection