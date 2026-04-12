---
name: sign-complex-systems
description: "Sparse Identification Graph Neural Network (SIGN) for inferring governing equations of complex networked systems. Use when working with: (1) complex systems dynamics prediction, (2) equation discovery from data, (3) graph neural networks for networked systems, (4) interpretable AI for dynamical systems, (5) large-scale network modeling (climate, biological, technological networks), (6) symbolic regression on graphs. Keywords: SIGN, sparse identification, equation discovery, complex systems, graph neural networks, network dynamics, interpretable prediction."
---

# SIGN: Sparse Identification Graph Neural Network

A framework for inferring governing equations of ultra-large complex networked systems from data, combining the interpretability of symbolic discovery with the scalability of neural networks.

## Core Innovation

SIGN overcomes the fundamental trade-off in complex systems modeling:
- **Equation discovery methods**: Interpretable but fail to scale
- **Neural networks**: Scale but operate as black boxes, lose reliability over long times

**Solution**: Define symbolic discovery as edge-level information, decoupling sparse identification scalability from network size.

## Key Capabilities

- **Scalability**: Handles networks with >100,000 nodes
- **Robustness**: Resistant to noise, sparse sampling, missing data
- **Interpretability**: Recovers governing equations with high precision
- **Long-term prediction**: Sustains accurate predictions over extended periods

## Architecture

```
Network Data → Graph Neural Network → Edge-level Symbolic Discovery → Governing Equations
```

### Components

1. **Graph Neural Network Backbone**
   - Processes network structure and dynamics
   - Node embeddings capture local dynamics
   - Edge embeddings capture interaction patterns

2. **Sparse Identification Module**
   - Edge-level symbolic regression
   - Library of candidate functions (polynomials, trigonometric, etc.)
   - LASSO/STRidge for sparse coefficient selection

3. **Equation Assembly**
   - Combines edge-level discoveries
   - Generates compact network equations
   - Validates against observed dynamics

## Methodology

### Step 1: Data Preparation

```python
# Network time series data
# X: node states over time [T, N, D]
# A: adjacency matrix [N, N]

import numpy as np

def prepare_network_data(time_series, adjacency):
    """Prepare network dynamics data for SIGN."""
    # Extract node features
    node_features = extract_features(time_series)
    # Compute edge features
    edge_features = compute_edge_features(time_series, adjacency)
    return node_features, edge_features
```

### Step 2: GNN Encoding

```python
# Graph neural network for encoding
def sign_gnn_encode(node_features, edge_features, adjacency):
    """Encode network dynamics using GNN."""
    # Message passing
    messages = compute_messages(node_features, edge_features)
    # Node updates
    updated_nodes = update_nodes(node_features, messages)
    # Edge representations
    edge_repr = compute_edge_repr(updated_nodes, edge_features)
    return edge_repr
```

### Step 3: Sparse Identification

```python
# Symbolic discovery at edge level
def sparse_identify(edge_repr, library):
    """Discover governing equations via sparse regression."""
    # Build candidate library
    Theta = build_library(edge_repr, library)
    # Sparse regression (STRidge)
    coefficients = stridge(Theta, derivatives)
    # Extract active terms
    equation = extract_equation(coefficients, library)
    return equation
```

## Applications

### Climate Networks
- Sea surface temperature prediction
- Climate pattern identification
- Long-term forecasting (2+ years)

### Biological Networks
- Neural dynamics modeling
- Gene regulatory networks
- Epidemic spreading

### Technological Networks
- Power grid dynamics
- Communication networks
- Traffic flow

## Implementation Guide

### Dependencies

```bash
pip install torch numpy scipy sympy networkx
```

### Basic Usage

```python
from sign import SIGN

# Initialize SIGN model
model = SIGN(
    num_nodes=100000,
    node_dim=3,
    library='polynomial_trigonometric',
    sparsity_threshold=0.01
)

# Fit to network data
model.fit(time_series_data, adjacency_matrix)

# Get discovered equations
equations = model.get_equations()

# Predict future dynamics
predictions = model.predict(horizon=100)
```

## References

- **Paper**: [Predicting Dynamics of Ultra-Large Complex Systems by Inferring Governing Equations](https://arxiv.org/abs/2604.00599)
- **Detailed methodology**: See [references/methodology.md](references/methodology.md)
- **Benchmark results**: See [references/benchmarks.md](references/benchmarks.md)
- **Sea surface temperature case study**: See [references/sst_case_study.md](references/sst_case_study.md)

## Scripts

- `scripts/sign_model.py` - Core SIGN implementation
- `scripts/sparse_regression.py` - STRidge and sparse identification
- `scripts/equation_library.py` - Function library construction

## Comparison with Alternatives

| Method | Scalability | Interpretability | Long-term Accuracy |
|--------|-------------|------------------|-------------------|
| SINDy | Low | High | Medium |
| Neural Networks | High | Low | Low |
| SIGN | **High** | **High** | **High** |

## Key Insights

1. **Edge-level discovery**: Key innovation enabling scalability
2. **Sparse library**: Compact equations from large candidate sets
3. **Noise robustness**: Statistical methods handle measurement errors
4. **Missing data tolerance**: GNN structure inference fills gaps

## Description

This skill provides specialized capabilities for its domain.

## Activation Keywords

- keyword1
- keyword2
- keyword3

## Tools Used

- read: Read files
- write: Write files
- exec: Execute commands

## Instructions for Agents

When this skill is activated:

1. Identify the user's specific need
2. Apply the specialized knowledge
3. Provide clear guidance

## Examples

```
User: How do I use this skill?
Agent: I'll help you with this skill...
```