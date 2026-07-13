---
name: tensor-cookbook-diagrams
description: "Tensor network diagram methodology for simplifying tensor algebra - graphical notation for contractions, decompositions, and gradient computation bridging quantum physics notation with machine learning. Activation: tensor network diagrams, tensor cookbook, penrose notation, tensor contraction diagrams, 张量网络图, 张量图解."
---

# Tensor Network Diagrams - The Tensor Cookbook Methodology

Self-contained guide to tensor networks and their use in tensor algebra through graphical (Penrose) notation. Bridges quantum physics tensor network methods with machine learning, signal processing, and statistics applications.

Based on arXiv:2605.16610 "Tensor Cookbook: Mastering Tensors through Diagrams" by Beheshteh T. Rakhshan & Guillaume Rabusseau.

## Core Concept

Tensor networks provide a graphical language that encodes tensor contractions as edges in a graph, reducing notational overhead and revealing structural properties obscured by index notation. This methodology makes high-dimensional tensor manipulation transparent and intuitive.

## Key Operations via Diagrammatic Notation

### 1. Basic Elements

- **Tensor**: Node with legs (edges) representing indices
- **Contraction**: Connecting legs between nodes (summing over shared indices)
- **Outer product**: Disconnected nodes placed side by side
- **Trace**: Connecting two legs of the same node (forming a loop)

### 2. Tensor Decompositions in Diagram Form

- **CP Decomposition**: Star graph with core tensor connected to factor matrices
- **Tucker Decomposition**: Core tensor with legs connected to factor matrices
- **Tensor Train (TT/MPS)**: Linear chain of 3rd-order tensors
- **Tensor Ring**: Cyclic chain (closed tensor train)
- **PEPS/2D-TN**: 2D grid of connected tensors
- **HOSVD**: Higher-order SVD expressed as sequential matrix unfoldings

### 3. Advanced Operations

- **Gradient computation**: Diagrammatic differentiation rules - replacing a node with its derivative
- **Rank bounds**: Graph-theoretic bounds on tensor ranks via network topology
- **Probability distributions**: High-dimensional probability as tensor networks
- **Classical identities**: Shorter, more transparent proofs via diagrams vs index manipulation

## Quantum-ML Bridge

| Quantum Physics | ML/Statistics Equivalent |
|---|---|
| Matrix Product State (MPS) | Tensor Train decomposition |
| PEPS | 2D tensor network for image data |
| MERA | Hierarchical feature extraction |
| Tensor contraction | Multi-linear operation |
| Bond dimension | Compression rank / model capacity |

## When to Use

- **Multi-modal data**: Representing data with multiple modes/dimensions
- **High-dimensional probability**: Factorizing joint distributions
- **Model compression**: Low-rank tensor approximations of weight tensors
- **Gradient derivation**: Simplifying backprop through tensor operations
- **Proof simplification**: Replacing index-heavy proofs with diagrammatic reasoning

## Workflow

1. **Represent** the tensor operation as a diagram (nodes = tensors, edges = indices)
2. **Simplify** by applying diagrammatic rewrite rules (contraction, trace, etc.)
3. **Decompose** using standard patterns (TT, Tucker, CP)
4. **Derive gradients** by applying diagrammatic differentiation
5. **Analyze** structural properties (rank, sparsity, symmetry) from graph topology

## Pitfalls

- **Leg ordering matters**: The order of legs on a node encodes index ordering
- **Directed vs undirected edges**: Complex conjugation requires directed edges
- **Symmetry exploitation**: Diagrams can obscure symmetry - explicitly mark symmetric legs
- **Bond dimension explosion**: Uncontrolled contractions can lead to exponential intermediate size
- **Index convention**: Consistently use Einstein summation convention for diagram-to-index translation

## Practical Applications

- **Neural network compression**: Compressing FC/Conv layers via tensor decomposition
- **Quantum-inspired ML**: Using tensor network methods for classical ML tasks
- **Signal processing**: Multi-way signal analysis and denoising
- **Computational physics**: Ground state computation, partition function evaluation
- **Statistics**: High-dimensional covariance estimation via low-rank tensor models
