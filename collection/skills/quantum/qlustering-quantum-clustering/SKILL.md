---
name: qlustering-quantum-clustering
description: "Unsupervised clustering via steady-state quantum transport in open quantum networks (GKSL master equation). Encodes data as input states and infers cluster assignments from terminal current observables - no full state tomography required. Use when: quantum clustering, GKSL transport, analog quantum ML, open quantum network clustering, Qlustering algorithm, steady-state quantum transport clustering, tomography-free quantum learning, quantum unsupervised learning, algorithm-hardware co-design clustering. Triggered by: Qlustering, quantum transport clustering, GKSL master equation clustering, analog quantum computation clustering, steady-state quantum current clustering, quantum network unsupervised learning."
---

# Qlustering: Quantum Transport-Based Clustering

Unsupervised clustering framework using steady-state quantum transport in
open quantum networks. Data are encoded as input states; cluster assignments
are inferred from steady-state output currents measured at terminals.

## Paper

arXiv: 2605.10844v1 — *Qlustering for Data Clustering via Network-Based
Quantum Transport* by Shmuel Lorber, Yonatan Dubi (May 2026).

## Core Approach

1. **Data Encoding**: Map input data points into quantum input states of the network.
2. **Transport Dynamics**: Evolve the network under the GKSL master equation to steady state.
3. **Readout**: Extract cluster assignments from terminal output currents (no tomography needed).
4. **Training-free**: Classical data preparation; clustering carried out purely by transport dynamics.

## When to Use

- Unsupervised clustering tasks where classical methods struggle
- Quantum machine learning implementations on analog quantum hardware
- Scenarios requiring noise-robust clustering (stable across broad dephasing strengths)
- Algorithm-hardware co-design for near-term quantum devices

## Key Properties

- **No tomography**: Uses accessible transport observables (terminal currents)
- **Noise-robust**: Stable performance across wide range of dephasing strengths
- **Hybrid workflow**: Classical data prep + quantum transport clustering
- **Benchmarked**: Tested on synthetic datasets, QM9, Iris
