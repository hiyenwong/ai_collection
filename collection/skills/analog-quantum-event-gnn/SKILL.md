---
name: analog-quantum-event-gnn
description: "Analog Quantum Asynchronous Event-Based Graph Neural Network (QA-AEGNN) — implementing event-based GNNs on neutral-atom quantum processors via Rydberg Hamiltonian programming. Maps streaming event data to trapped atom arrays where geometric proximity reflects spatio-temporal neighborhoods, with native Hamiltonian dynamics executing message-passing natively. Activation: quantum GNN, neutral atom, Rydberg Hamiltonian, event camera, asynchronous event, analog quantum computing, graph neural network, message passing, quantum neural network, trapped atom, quantum machine learning, event-based vision"
metadata:
  arxiv_id: "2606.11000"
  published: "2026-06-09"
  authors: "Kristian Sotirov, Shaheen Acheche, Antonio A. Gentile, Osvaldo Simeone"
---

## Context

Asynchronous event-based graph neural networks (AEGNNs) efficiently process sparse, high-temporal-resolution data from event cameras. QA-AEGNNs implement AEGNNs natively on neutral-atom quantum processors, leveraging Rydberg interactions for massive parallelism and continuous Hamiltonian dynamics for message-passing.

## Core Methodology

### 1. Event-to-Atom Mapping

- Map each incoming event (pixel, timestamp, polarity) to a trapped neutral atom
- Position atoms such that geometric proximity reflects spatio-temporal neighborhood: `distance(i,j) ∝ ||(x_i,t_i) - (x_j,t_j)||`
- Atom qubit states encode node features (event polarity, intensity, temporal decay)
- Streaming data: new events → new atoms added to the array dynamically

### 2. Rydberg Hamiltonian Message Passing

- Native Rydberg Hamiltonian: `H = Σ_i (Ω_i σ_x^i - Δ_i n_i) + Σ_{i<j} V_{ij} n_i n_j`
  - Ω_i: laser Rabi frequency (controls node feature rotation)
  - Δ_i: laser detuning (controls node bias)
  - V_{ij} = C_6 / r_{ij}^6: van der Waals interaction (realizes graph edge weights)
- Message passing emerges naturally from Hamiltonian evolution: `|ψ(t)⟩ = exp(-iHt)|ψ(0)⟩`
- Inter-atom Rydberg interactions implement weighted message aggregation
- Continuous-time dynamics replace discrete GNN layers

### 3. Hybrid Quantum-Classical Training

- Classical optimizer updates Hamiltonian parameters (Ω, Δ)
- Quantum processor executes analog evolution for each event batch
- Gradient estimation via parameter-shift rule or finite differences
- Loss: task-specific (classification, detection, segmentation on event data)

### 4. Spatio-Temporal Neighborhood via Geometry

- Key insight: Rydberg interaction strength V_{ij} ∝ 1/r_{ij}^6 provides natural distance-weighted attention
- Closer atoms (spatio-temporally nearby events) interact more strongly
- No explicit adjacency matrix needed — graph structure is encoded in atom positions
- Dynamic graph: new events create new atoms and modify interaction topology

## Implementation Steps

1. Receive event stream from event camera (x, y, t, polarity)
2. Map events to atom positions: r_i = f(x_i, y_i, t_i) with spatial scaling
3. Initialize atom qubit states from event features
4. Program Rydberg Hamiltonian parameters (Ω, Δ) from current model weights
5. Execute analog quantum evolution for time τ (message-passing step)
6. Measure atomic states → extract node embeddings
7. Compute task-specific loss on embeddings
8. Classical optimizer updates Ω, Δ via gradient descent
9. Repeat for next event batch

## Pitfalls

- **Rydberg blockade radius**: Maximum interaction range limits effective graph diameter — events beyond blockade radius cannot directly interact; multi-hop requires sequential evolution steps
- **Atom loading time**: Loading/rearranging atoms for each event batch introduces latency — buffer events to amortize loading overhead
- **Decoherence time**: Analog evolution time τ must be ≪ T1, T2 of neutral atoms — limits depth of message-passing
- **Positioning precision**: Atom positioning errors (typically ~100nm) perturb interaction strengths V_{ij} — robustness to positional noise is critical
- **Scalability**: Current neutral-atom platforms support ~100-1000 atoms — limits maximum event batch size; requires temporal downsampling for high-rate event streams

## Verification

- QA-AEGNN should match or exceed classical AEGNN accuracy on standard event camera benchmarks (N-CARS, N-Caltech101)
- Interaction strength V_{ij} should decay as 1/r^6 with atom distance — verify experimentally
- Training convergence: hybrid optimization should achieve monotonic loss decrease over epochs
- Ablation: removing Rydberg interactions (V_{ij} = 0) should reduce to independent node processing (baseline performance)
