---
name: pauli-correlation-portfolio-optimization
description: >
  Large-scale portfolio optimization using Pauli Correlation Encoding (PCE) for
  gate-based quantum computing. Enables variational quantum algorithms to handle
  250+ asset variables by encoding multiple variables per qubit through market
  graph partitioning and Pauli operator correlations. Use when: (1) quantum portfolio
  optimization with more assets than available qubits, (2) scaling VQA/QAOA beyond
  qubit-count limits, (3) real-world financial asset allocation on NISQ hardware,
  (4) sub-portfolio construction from correlated asset clusters.
---

# Pauli Correlation Encoding for Portfolio Optimization

## Core Idea

Conventional quantum optimization assumes 1 qubit = 1 variable, limiting problems
to current qubit counts (~100-1000). Pauli Correlation Encoding (PCE) overcomes
this by:

1. **Market graph construction** — build correlation graph from asset returns
2. **Graph partitioning** — split into sub-portfolios of highly correlated assets
3. **Multi-variable-per-qubit encoding** — assign multiple asset variables to each
   qubit using Pauli operator correlations
4. **Variational optimization** — run VQA on each sub-portfolio independently

This enables 250+ variable problems on devices with far fewer qubits.

## Algorithm Steps

### Step 1: Build Market Graph

```python
import numpy as np

# returns: T x N matrix of asset returns
correlation = np.corrcoef(returns.T)  # N x N correlation matrix
adjacency = np.abs(correlation) - threshold  # threshold ~0.3-0.5
adjacency[adjacency < 0] = 0
```

### Step 2: Partition Graph

Use spectral clustering, METIS, or greedy algorithms:

```python
from sklearn.cluster import SpectralClustering

n_subportfolios = min(n_qubits_available, max_clusters)
sc = SpectralClustering(n_clusters=n_subportfolios, affinity='precomputed')
labels = sc.fit_predict(adjacency)

# Each label group = sub-portfolio of correlated assets
sub_portfolios = {i: np.where(labels == i)[0] for i in range(n_subportfolios)}
```

### Step 3: Pauli Correlation Encoding

For a sub-portfolio with `m` assets and `k` available qubits (m > k):

- Encode `m` binary asset selection variables using `k` qubits
- Use Pauli operator products Z_i Z_j to represent correlations
- Objective: maximize Sharpe ratio subject to budget constraint

```python
from qiskit.quantum_info import SparsePauliOp

# Example: 4 assets on 2 qubits using PCE
# Variables x0,x1,x2,x3 mapped via:
# x0 -> Z_0, x1 -> Z_1, x2 -> Z_0*Z_1, x3 -> (Z_0 + Z_1)/2
# This allows encoding floor(m/k) variables per qubit

def build_pce_hamiltonian(correlation_matrix, expected_returns, risk_aversion=0.5):
    """Build Hamiltonian for sub-portfolio using PCE."""
    n_assets = len(expected_returns)
    terms = []
    coeffs = []

    # Return term: -sum(mu_i * x_i)
    for i in range(n_assets):
        terms.append(f"Z{i % n_qubits}")
        coeffs.append(-expected_returns[i] * 0.5)

    # Risk term: risk_aversion * sum(sigma_ij * x_i * x_j)
    for i in range(n_assets):
        for j in range(i+1, n_assets):
            # Use Pauli products for correlations
            zi = f"Z{i % n_qubits}"
            zj = f"Z{j % n_qubits}"
            terms.append(f"{zi}*{zj}")
            coeffs.append(risk_aversion * correlation_matrix[i, j] * 0.25)

    return SparsePauliOp.from_list(list(zip(terms, coeffs)))
```

### Step 4: Variational Quantum Algorithm

```python
from qiskit.circuit.library import TwoLocal
from qiskit.algorithms.optimizers import SPSA
from qiskit.primitives import Estimator

# For each sub-portfolio:
def optimize_subportfolio(hamiltonian, n_qubits, n_layers=3):
    ansatz = TwoLocal(n_qubits, ['ry', 'rz'], 'cz', reps=n_layers)
    estimator = Estimator()
    optimizer = SPSA(maxiter=200)

    def cost_function(params):
        job = estimator.run(ansatz, hamiltonian, [params])
        return job.result().values[0]

    result = optimizer.minimize(cost_function, x0=np.random.randn(ansatz.num_parameters))
    return result
```

### Step 5: Aggregate Results

Combine sub-portfolio solutions into global allocation:

```python
def aggregate_allocation(sub_results, sub_portfolios, budget):
    """Combine sub-portfolio allocations respecting global budget."""
    global_allocation = np.zeros(total_assets)
    for label, assets in sub_portfolios.items():
        sub_alloc = decode_quantum_result(sub_results[label], assets)
        global_allocation[assets] = sub_alloc

    # Normalize to budget constraint
    global_allocation = global_allocation / global_allocation.sum() * budget
    return global_allocation
```

## Key Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| correlation_threshold | 0.3-0.5 | Edge cutoff for market graph |
| risk_aversion | 0.5 | Trade-off between return and risk |
| n_layers | 3 | Ansatz circuit depth |
| maxiter | 200 | SPSA optimizer iterations |
| n_shots | 1024 | Measurement shots per evaluation |

## Scalability Analysis

- **Qubit requirement**: O(sqrt(N)) instead of O(N) for N assets
- **Classical pre-processing**: O(N^2) for correlation + O(N log N) for partitioning
- **Quantum circuit**: depth O(sqrt(N) * layers)
- **Empirical**: 250+ assets demonstrated on simulated hardware

## When to Use PCE vs Alternatives

| Method | Max Assets | Hardware | Accuracy |
|--------|-----------|----------|----------|
| Direct encoding | ~n_qubits | Gate-based | Exact |
| **PCE (this)** | **O(n_qubits^2)** | **Gate-based** | **Approximate** |
| Quantum annealing | ~5000 | D-Wave | Approximate |
| Classical | Unlimited | CPU/GPU | Exact |

Use PCE when: gate-based quantum advantage needed + assets > available qubits.

## Activation Keywords

- pauli correlation encoding, PCE portfolio, quantum portfolio optimization,
  multi-variable qubit encoding, market graph partitioning, scalable VQA portfolio,
  quantum finance 250 assets, gate-based portfolio optimization

## References

- Soloviev & Krompiec, "Large-scale portfolio optimization using Pauli Correlation
  Encoding", arXiv:2511.21305 (2025)
