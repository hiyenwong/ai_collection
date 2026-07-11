---
name: qubo-federated-learning-security
description: "QUBO-based Byzantine-resilient federated learning methodology. Reformulates client selection in federated learning as Quadratic Unconstrained Binary Optimization solved by quantum annealers. Jointly optimizes over all client subsets to find mutually closest group, outperforming greedy MultiKrum on advanced Byzantine attacks. Use when: QUBO client selection, Byzantine-resilient federated learning, quantum annealing FL, QUBO optimization, federated learning security, MultiKrum improvement, quantum annealer, adversarial client detection."
---

# QUBO-Based Byzantine-Resilient Federated Learning

## Core Concept

Reformulate Byzantine-resilient client selection in federated learning as QUBO (Quadratic Unconstrained Binary Optimization), solved by quantum annealers. Unlike greedy per-client scoring (MultiKrum), QUBO jointly optimizes over all subsets to find the mutually closest group of m clients.

## Mathematical Formulation

Given pairwise distance matrix D between clients, encode as:
```
min x^T Q x
s.t. Σ x_i = m (select exactly m clients)
```
Where Q encodes pairwise distances: Q_ij = D_ij for i≠j, with penalty terms enforcing the cardinality constraint.

## Why QUBO > MultiKrum

- **MultiKrum**: Greedy per-client scoring — scores each client against nearest neighbors independently
- **QUBO**: Joint optimization — finds the globally optimal subset of m mutually closest clients
- **Result**: On advanced Byzantine attacks (Advanced LIE), QUBO achieves 95.11% vs 81.33% (MNIST) and 97.78% vs 75.56% (CIFAR-10)

## Implementation Pattern

```python
from dwave.system import LeapHybridSampler
import numpy as np

def qubo_client_selection(gradients, m, n_total):
    """QUBO-based Byzantine-resilient client selection"""
    # 1. Compute pairwise distance matrix
    D = pairwise_distances(gradients)  # shape: (n_total, n_total)
    
    # 2. Build QUBO matrix
    Q = np.zeros((n_total, n_total))
    for i in range(n_total):
        for j in range(n_total):
            if i != j:
                Q[i, j] = D[i, j]
    
    # 3. Add cardinality constraint penalty
    penalty = 10.0  # must be large enough
    for i in range(n_total):
        Q[i, i] -= penalty * m
    
    # 4. Solve with quantum annealer
    sampler = LeapHybridSampler()
    response = sampler.sample_qubo(Q, num_reads=100)
    
    # 5. Extract selected clients
    best_sample = response.first.sample
    selected = [i for i, v in best_sample.items() if v == 1]
    return selected
```

## Application Scenarios

**Scenario 1: Large-scale FL with privacy guarantees** — When FL scales to hundreds of clients, QUBO finds optimal honest subsets even under sophisticated attacks.

**Scenario 2: Advanced Byzantine attacks** — Attacks that preserve statistical properties of honest clients defeat MultiKrum but are caught by QUBO's joint optimization.

## Pitfalls

- **Scalability**: Current quantum annealers limited to ~5000 qubits — for large FL, use hybrid classical-quantum solvers
- **QUBO formulation quality**: Distance metric choice critically affects results — cosine similarity works well for gradients
- **Constraint penalty tuning**: Too small → violates cardinality; too large → dominates objective

## Activation

QUBO联邦学习, QUBO Byzantine FL, quantum annealing federated learning, QUBO client selection, Byzantine-resilient aggregation, quantum annealer security
