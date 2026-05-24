---
name: quantum-forensic-gnn
description: "GNN-based forensic framework for inferring hardware noise in cloud quantum backends. Use when: (1) analyzing transparency and security of cloud quantum platforms like IBM Quantum, (2) inferring backend error rates from user-visible artifacts, (3) verifying whether quantum circuits were executed on claimed hardware, (4) building forensic tools for quantum computing, (5) studying quantum hardware noise characterization using graph neural networks, (6) detecting resource allocation deception in quantum cloud services. Activation: quantum forensic, cloud quantum security, GNN quantum noise, hardware noise inference, quantum backend verification, IBM quantum error rates, quantum transparency."
---

# Quantum Forensic GNN Framework

GNN-based forensic framework for inferring hardware noise of cloud quantum backends. Addresses the security gap where cloud quantum providers may redirect jobs to more error-prone regions while presenting stale calibration data.

## Core Methodology (from arXiv:2512.14541)

### Problem
Cloud quantum platforms give users access to backends with different qubit technologies, coupling layouts, and noise levels. Users cannot verify whether circuits were executed on the hardware they were charged for due to opaque internal allocation/routing policies.

### Solution Architecture

1. **Graph Construction**: Model quantum backend as a graph where nodes = qubits, edges = qubit couplings
2. **Feature Engineering**: Merge static calibration features with dynamic transpilation features
3. **GNN Regressors**: Train separate models for one-qubit and two-qubit error rates
4. **Inference**: Predict per-qubit and per-qubit-link error rates using only topology + transpiled circuit features (no calibration data from target backend)

### Key Results
- Average mismatch: ~22% for single-qubit errors, ~18% for qubit-link errors
- Strong ranking agreement (high Spearman correlation)
- Identifies weak links and high-noise qubits
- Robust under realistic temporal noise drift

## Workflow

### Step 1: Extract Transpilation Features

```python
from qiskit import transpile

def extract_transpilation_features(circuit, backend):
    """Extract features visible to the user after transpilation."""
    transpiled = transpile(circuit, backend)
    features = {
        'depth': transpiled.depth(),
        'width': transpiled.width(),
        'num_gates': transpiled.count_ops(),
        'routing_depth': get_routing_depth(transpiled),
    }
    return features
```

### Step 2: Build Topology Graph

```python
import networkx as nx

def build_backend_graph(backend):
    """Construct graph from backend coupling map."""
    coupling = backend.configuration().coupling_map
    G = nx.Graph()
    G.add_nodes_from(range(backend.configuration().n_qubits))
    G.add_edges_from(coupling)
    return G
```

### Step 3: Train GNN Error Predictors

```python
import torch
import torch.nn as nn

class QubitErrorGNN(nn.Module):
    """GNN for predicting per-qubit error rates."""
    def __init__(self, in_features, hidden=64):
        super().__init__()
        self.conv1 = nn.Linear(in_features, hidden)
        self.conv2 = nn.Linear(hidden, hidden)
        self.out = nn.Linear(hidden, 1)
        
    def forward(self, x, edge_index):
        x = torch.relu(self.conv1(x))
        x = torch.relu(self.conv2(x))
        return self.out(x)
```

### Step 4: Inference on Target Backend

At inference, the model operates WITHOUT calibration data from the target backend:
- Input: topology + transpilation features
- Output: reconstructed complete error map
- Validation: compare ranking of predicted vs actual error rates (Spearman correlation)

## Application Scenarios

1. **Audit cloud quantum providers**: Verify execution fidelity matches billing
2. **Detect error drift**: Monitor noise changes over time without direct calibration access
3. **Optimize circuit placement**: Choose qubits based on predicted error landscape
4. **Multi-backend comparison**: Rank backends by reconstructed noise profiles

## Pitfalls

- **Temporal drift**: Calibration data becomes stale quickly; forensic approach accounts for this
- **Feature availability**: Only use features visible to end users (topology, transpilation output)
- **Ground truth**: Actual calibration data needed for model training/validation, not inference
- **Ranking > absolute values**: Strong Spearman correlation is more actionable than absolute error prediction

## Related Papers

- arXiv:2512.14541 - Original paper (Das, Ghosh, Ghosh)
- arXiv:2512.06661 - Scalable quantum cryptographic conferencing (complementary security work)
- arXiv:2512.20489 - High-dimensional quantum blockchain protocol

## Activation Keywords

quantum forensic, GNN quantum noise, cloud quantum security, IBM quantum verification, hardware noise inference, quantum backend audit, quantum error rate prediction
