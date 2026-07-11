---
name: quantum-transport-clustering
description: "Qlustering: Unsupervised clustering via steady-state quantum transport in GKSL-governed quantum networks. Data encoded as input states, cluster assignments inferred from terminal output currents. Use when: quantum machine learning, unsupervised quantum clustering, GKSL master equation applications, open quantum network learning, quantum data clustering, or algorithm-hardware co-design for quantum ML."
---

# Qlustering — Quantum Transport for Unsupervised Clustering

Analog quantum computation framework for unsupervised clustering using steady-state quantum transport in open quantum networks (arXiv: 2605.10844).

## Core Idea

Cluster data by encoding it as quantum states in an open quantum network and reading out cluster assignments from **steady-state terminal currents** — no full state tomography required.

## GKSL Master Equation

The quantum network evolves under the GKSL (Gorini-Kossakowski-Sudarshan-Lindblad) master equation:

```
dρ/dt = -i[H, ρ] + Σ_k γ_k (L_k ρ L_k† - ½{L_k†L_k, ρ})
```

Where:
- `ρ`: density matrix of the quantum system
- `H`: Hamiltonian encoding the data structure
- `L_k`: Lindblad operators for dephasing/dissipation
- `γ_k`: coupling strengths

## Workflow

### Step 1: Data Encoding

Map classical data points to quantum input states:
- Each data point → a specific input state configuration
- Feature distances → Hamiltonian coupling strengths

### Step 2: Quantum Transport Dynamics

- Initialize the network with data-encoded input states
- Let the system evolve under GKSL dynamics
- System reaches steady state naturally (no active control needed)

### Step 3: Current Readout

- Measure terminal currents (particle flow rates at output nodes)
- Cluster assignments are inferred from current magnitudes/patterns
- High current to terminal T_i → data point belongs to cluster i

### Step 4: Classical Post-Processing

- Map current patterns to discrete cluster labels
- Validate against known labels (if available)

## Key Advantages

1. **Tomography-free**: No full state reconstruction needed — only measure terminal currents
2. **Hardware-native**: Current readout is a natural observable in quantum transport setups
3. **Robust to dephasing**: Stable performance across wide range of dephasing strengths
4. **Hybrid workflow**: Classical data prep + quantum dynamics + classical readout

## Benchmarks

- Synthetic datasets: competitive with classical methods
- QM9 (molecular dataset): effective clustering
- Iris dataset: competitive performance
- Stable across dephasing strength variations

## Design Principles

1. **Algorithm-hardware co-design**: Match encoding to available hardware observables
2. **Transport over state**: Use particle flow (currents) as the computational output, not quantum states
3. **Open system advantage**: Decoherence/dephasing is a feature, not a bug — helps convergence to steady state
4. **Minimal measurement**: Only terminal currents, not full density matrix

## When to Use

- Unsupervised clustering on quantum hardware
- When state tomography is too expensive
- Hybrid classical-quantum ML pipelines
- Quantum networks with accessible transport measurements
