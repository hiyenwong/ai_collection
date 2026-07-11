---
name: unifying-dynamics-graph-neural-computation
description: "Framework unifying dynamical systems and graph theory to mechanistically understand computation in neural networks. Uses resolvent-based multi-hop pathway analysis to recover input-output routing structure from connectivity, introduces R-RNNs with resolvent-based regularization for temporally structured sparsity. Activation: multi-hop, resolvent RNN, graph computation, neural network interpretability, structure-function mapping, temporal routing, R-RNN, network communication."
---

# Unifying Dynamical Systems and Graph Theory to Mechanistically Understand Computation in Neural Networks

**arXiv:** 2605.03598 [cs.NE, cs.AI] (May 2026)  
**Authors:** Jatin Sharma, Dan F.M. Goodman, Danyal Akarca (Imperial College London)  
**Source:** https://arxiv.org/abs/2605.03598

## Core Problem

How to infer what a neural network computes from its structure? In neural systems, structural and functional connectivity diverge — direct connections capture only single-step interactions, but computation in recurrent networks is mediated by multi-hop pathways unfolding over time.

## Key Insight: Multi-Hop Pathways Over Single Connections

Computation in recurrent networks is better understood through **multi-hop pathways** than through individual weight connections. The raw weight matrix W alone cannot recover the learned input-output structure, even when the network has sufficient capacity. Multi-hop graph measures reveal the spatial-temporal routing that mediates information flow.

## Technical Framework

### Neural Networks as Graphs

An RNN's weight matrices form an adjacency matrix W ∈ R^(n×n) where n = i + h + o (input + hidden + output units). The key property: W^k tells you how many walks of length k exist between any two nodes. Different network structures can share the same multi-hop pattern (W^k) despite different single-hop structures (W).

### The Resolvent as Multi-Hop Summary

The graph resolvent aggregates walks of all lengths with exponential decay:

```
R = (I - αW*)^(-1) = Σ(k=0→∞) (αW*)^k
```

Where W* = W/λ_max (normalized) and α ∈ (0,1) controls long-walk influence. The resolvent corresponds to a **leaky cascade** dynamical process — information propagates through the network with diminishing influence at each hop.

### Truncated Resolvent for Temporal Tasks

For RNNs with sequence length L, only finite hops can influence output:

```
R_io = Σ(k=2→L+1) (αW*)^k  [input-to-output block]
```

This truncated resolvent captures the input-output influence map R_io, representing the signed weighted sum over all walks between each input and output node.

### Hop-Wise Decomposition Reveals Temporal Routing

Decomposing by hop length (computing W^k_io for individual k) reveals **how the network temporally routes information**:
- Hop length k corresponds to inputs arriving at time t = L - (k - 2)
- Even-numbered hops process signal inputs; odd hops process noise inputs
- This provides an input-agnostic method to characterize routing capacity

## R-RNNs: Resolvent-Based Regularization

### The Problem with L1 Regularization

L1 regularization acts on individual weights (single-hop), but computation is implemented through multi-hop pathways. Sparse weights ≠ sparse functional pathways — a small number of strong connections can still induce dense multi-hop routing.

### R-RNN Solution

Regularize the resolvent directly instead of individual weights:

```
L_sparsity = Σ|R_io|  (vs. L1: Σ|W|)
```

Where R is computed from W (not normalized W*) to prevent trivial reduction by increasing λ_max.

### Advantages of R-RNNs

1. **Improved performance**: Lower test MSE than L1-RNNs on modular tasks
2. **Temporal sparsity**: Suppresses redundant pathways across all temporal routes
3. **Task-aligned sparsity**: Selectively suppresses hops matching task structure (e.g., suppresses signal-carrying hops when signal is sparse)
4. **Robustness under strong regularization**: Maintains performance at high β where L1-RNNs degrade rapidly
5. **Sparsity-function alignment**: Achieves communication sparsity with minimal performance loss

## Mechanistic Interpretability Applications

### Reconciling Sherringtonian and Hopfieldian Views

- **Sherringtonian** (localized computation): Local connectivity generates distributed routing patterns through accumulation of walks
- **Hopfieldian** (distributed computation): What appears as distributed processing reflects exploitation of many parallel pathways
- The resolvent makes this link explicit, connecting local weights to global functional consequences

### Structure-Function Relationships

Structural modularity only translates to functional modularity if the walk structure respects module boundaries. Computing R_io for networks with varying structural modularity reveals why the structure-function relationship breaks down in some regimes.

### Input-Agnostic Routing Capacity

Unlike the Jacobian (which measures input-dependent sensitivity and requires extensive controlled experiments), hop-based measures describe a network's "routing capacity" just from its connectivity — enabling comparison of how networks would respond to novel stimuli without new input-output measurements.

## Implementation Guide

### Computing the Resolvent

```python
import numpy as np

def compute_resolvent(W, alpha=0.8, L=None):
    """
    Compute truncated resolvent for RNN weight matrix.
    
    Args:
        W: Weight matrix (n x n), n = i + h + o
        alpha: Damping parameter (0 < alpha < 1)
        L: Sequence length (truncation point)
    
    Returns:
        R: Truncated resolvent (input-to-output block)
    """
    lambda_max = np.max(np.abs(np.linalg.eigvals(W)))
    W_norm = W / lambda_max
    
    if L is not None:
        # Truncated: only hops 2 to L+1
        R = np.zeros_like(W)
        Wk = W_norm @ W_norm  # Start at k=2
        for k in range(2, L + 2):
            R += (alpha ** k) * Wk
            Wk = Wk @ W_norm
    else:
        # Full resolvent: (I - alpha*W_norm)^(-1)
        n = W.shape[0]
        R = np.linalg.inv(np.eye(n) - alpha * W_norm)
    
    # Extract input-to-output block
    i, h, o = input_size, hidden_size, output_size
    R_io = R[:i, i+h:i+h+o]
    
    return R_io
```

### R-RNN Regularization

```python
def resolvent_regularization(W, alpha=0.8, L=None):
    """Compute L_sparsity = sum|R_io| for R-RNN training."""
    R_io = compute_resolvent(W, alpha, L)
    return np.sum(np.abs(R_io))

# In training loop:
# loss = task_loss + beta * resolvent_regularization(W)
```

### Hop-Wise Decomposition

```python
def hop_wise_decomposition(W, k, input_size, hidden_size, output_size):
    """Compute W^k input-to-output block."""
    Wk = np.linalg.matrix_power(W, k)
    i, h, o = input_size, hidden_size, output_size
    return Wk[:i, i+h:i+h+o]

# Analyze temporal routing
for k in range(2, L + 2):
    Wk_io = hop_wise_decomposition(W, k, i, h, o)
    # Wk_io reveals routing for inputs at time t = L - (k - 2)
```

## Experimental Validation

### Tasks Tested
- Module averaging (within-module aggregation)
- Subtraction (hierarchical inhibitory pathways)
- Addition (hierarchical excitatory pathways)
- Multiplication (non-linear, defined via task Jacobian)
- Oscillating on-off signal (temporal routing)

### Key Results
- R_io correlation with optimal solution: 0.92-0.99 (vs. W_hh: 0.03-0.24)
- R-RNNs achieve lower test MSE than L1-RNNs across all β values
- R-RNNs maintain performance under strong regularization where L1-RNNs fail

## Applications to Biological Networks

1. **Brain network analysis**: Use resolvent to predict functional connectivity from structural connectivity
2. **Clinical populations**: Compare R_io between healthy and clinical groups as graph metric
3. **Information theory**: Test whether high R_io pathways carry more mutual information
4. **Physical computing systems**: Extend to any system where dynamics unfold on a graph

## Limitations

1. Resolvent assumes a specific dynamical prior (leaky cascade); other systems may need communicability or alternative measures
2. Current validation on intentionally modular tasks; generality to naturalistic, high-dimensional tasks is open
3. Extending beyond shallow RNNs (Transformers, MoEs) requires careful node/edge definitions
4. Connection to information theoretic quantities remains to be established

## Activation Keywords

multi-hop pathways, resolvent RNN, R-RNN, graph theory neural networks, structure-function mapping, temporal routing, network communication, mechanistic interpretability, sparsity regularization, input-output routing, communicability, leaky cascade, Sherringtonian, Hopfieldian, routing capacity, neural network as graph

## Related Skills

- unifying-dynamics-graph-neural-computation
- brain-network-controllability
- hermes-brain-connectivity
- snn-learning-survey
