---
name: quantum-transport-clustering
description: "Qlustering methodology for unsupervised data clustering via steady-state quantum transport in open quantum networks governed by GKSL master equations. Algorithm-hardware co-design for quantum machine learning: encode data as input states, infer cluster assignments from steady-state output currents without full state tomography. Use when: quantum clustering, unsupervised quantum learning, GKSL transport, quantum network clustering, quantum machine learning clustering, steady-state quantum dynamics, quantum transport observables, hybrid classical-quantum workflows, open quantum system learning, tomography-free quantum readout. Activation: quantum clustering, qlustering, GKSL clustering, quantum transport learning, open quantum network clustering, steady-state quantum ML."
---

# Quantum Transport Clustering (Qlustering)

## Core Idea

Unsupervised clustering via **steady-state quantum transport** in open quantum networks. Data are encoded as input states to a quantum network; cluster assignments are inferred from steady-state output currents measured at terminal nodes — avoiding full state tomography.

## The GKSL Framework

The quantum network dynamics are governed by the Gorini-Kossakowski-Sudarshan-Lindblad (GKSL) master equation:

$$\dot{\rho} = -i[H, \rho] + \sum_k \mathcal{L}_k(\rho)$$

where $H$ is the system Hamiltonian encoding the data, and $\mathcal{L}_k$ are Lindblad dissipators modeling interaction with baths (source/drain terminals).

## Three-Stage Workflow

### Stage 1: Classical Data Preparation

1. **Feature Encoding**: Map data points to quantum states
   - Normalize features to [0, 1] range
   - Use amplitude or angle encoding depending on dimensionality
   - For n-dimensional data: use n-level quantum system or qubit encoding

2. **Input State Construction**: Build density matrix $\rho_{in}$
   - Each data point becomes an initial state
   - Consider using mixed states to represent uncertainty

3. **Hamiltonian Design**: Construct $H$ to reflect data structure
   - Data similarity $\to$ coupling strengths between nodes
   - Use kernel methods (RBF, polynomial) to define coupling matrix

### Stage 2: Quantum Transport Evolution

1. **Lindblad Setup**: Configure source/drain terminals
   - Source terminals: inject states into network
   - Drain terminals: absorb states, produce measurable currents
   - Set dephasing rates $\gamma$ — key hyperparameter

2. **Steady-State Computation**: Solve $\dot{\rho} = 0$
   - For simulation: use scipy.sparse linear solver
   - Vectorize the GKSL equation into Lindblad superoperator $\mathcal{L}$
   - Solve $\mathcal{L}|\rho_{ss}\rangle = 0$ for steady-state density matrix

3. **Current Readout**: Measure terminal currents
   - $I_\alpha = \text{Tr}[L_\alpha \rho_{ss}]$ for each terminal $\alpha$
   - Currents are directly measurable — no tomography needed

### Stage 3: Classical Cluster Assignment

1. **Current Vector Analysis**: Stack terminal currents into feature vectors
   - Each data point maps to a current vector $\vec{I}$
   - Dimension = number of drain terminals

2. **Clustering**: Apply classical clustering to current vectors
   - k-means, DBSCAN, or hierarchical clustering
   - Currents naturally separate due to quantum transport interference

## Key Parameters

| Parameter | Role | Tuning Guidance |
|-----------|------|-----------------|
| Dephasing strength $\gamma$ | Controls quantum coherence | Robust over broad range; start with $\gamma \in [0.1, 1.0]$ |
| Network size | Number of quantum nodes | Match to data dimensionality |
| Terminal placement | Which nodes are source/drain | Experiment; symmetry matters |
| Coupling matrix | Encodes data similarity | RBF kernel works well |

## Python Implementation Pattern

```python
import numpy as np
from scipy.sparse import kron, identity, csc_matrix
from scipy.sparse.linalg import spsolve

def build_lindblad(H, L_ops, dephasing_rates):
    """Build GKSL Lindblad superoperator.
    H: system Hamiltonian (n x n)
    L_ops: list of Lindblad operators
    dephasing_rates: corresponding rates
    Returns: Liouvillian superoperator (n^2 x n^2)
    """
    n = H.shape[0]
    I = np.eye(n)
    
    # Hamiltonian part: -i[H, rho]
    L_H = -1j * (np.kron(H, I) - np.kron(I, H.T))
    
    # Dissipator part: sum gamma_k (L_k rho L_k^dagger - 0.5 {L_k^dagger L_k, rho})
    L_D = 0
    for gamma, L in zip(dephasing_rates, L_ops):
        L_dag = L.conj().T
        L_D += gamma * (np.kron(L, L.conj()) 
                        - 0.5 * np.kron(L_dag @ L, I)
                        - 0.5 * np.kron(I, (L_dag @ L).T))
    
    return L_H + L_D

def solve_steady_state(L_super):
    """Solve L|rho> = 0 with Tr(rho) = 1 constraint."""
    n = int(np.sqrt(L_super.shape[0]))
    # Replace last row with trace constraint
    L_super[-1, :] = 0
    L_super[:, -1] = 0
    L_super[-1, -1] = 1
    b = np.zeros(L_super.shape[0])
    b[-1] = 1.0
    rho_vec = spsolve(csc_matrix(L_super), b)
    return rho_vec.reshape(n, n)

def qlustering_pipeline(data, n_terminals, gamma=0.5):
    """Full Qlustering pipeline.
    data: (N, d) array of data points
    n_terminals: number of drain terminals
    gamma: dephasing strength
    Returns: current vectors for each data point
    """
    # 1. Encode data into Hamiltonian
    n_nodes = data.shape[1]
    H = build_hamiltonian(data, n_nodes)  # similarity-based coupling
    
    # 2. Build Lindblad operators for terminals
    L_ops = build_terminal_operators(n_nodes, n_terminals)
    
    # 3. Solve for steady-state currents
    currents = []
    for point in data:
        H_point = build_point_hamiltonian(point, n_nodes)
        L_super = build_lindblad(H_point, L_ops, [gamma] * len(L_ops))
        rho_ss = solve_steady_state(L_super)
        I = measure_currents(rho_ss, L_ops, gamma)
        currents.append(I)
    
    return np.array(currents)
```

## Advantages Over Classical Methods

1. **Tomography-free**: Direct current readout avoids expensive state tomography
2. **Robust to dephasing**: Works over broad range of noise strengths
3. **Hardware-natural**: Currents are native observables in quantum devices
4. **Hybrid workflow**: Classical prep + quantum transport + classical clustering
5. **No training required**: Unsupervised by construction

## Benchmark Datasets

- **Synthetic**: Blobs, circles, moons with varying noise
- **QM9**: Molecular property clustering
- **Iris**: Standard benchmark for validation
- **Localization**: Anderson localization-inspired clustering

## Related Patterns

- **GKSL master equation**: Standard for open quantum systems
- **Hybrid classical-quantum**: Classical data prep → quantum processing → classical analysis
- **Algorithm-hardware co-design**: Design algorithm for specific hardware observables
- **Transport-based learning**: Use physical transport phenomena as computational resource

## When to Use

- Unsupervised clustering where quantum advantage may apply
- Scenarios where full quantum state tomography is infeasible
- Hardware implementations with accessible current measurements
- Data with structure that maps naturally to quantum network topology
