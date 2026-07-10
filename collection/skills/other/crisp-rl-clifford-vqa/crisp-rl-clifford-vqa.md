---
name: crisp-rl-clifford-vqa
description: CRiSP — Reinforcement learning with Neural-Guided MCTS for Clifford circuit initialization of Variational Quantum Algorithms. Uses Transformer-based policy trained via self-play to insert learned Clifford gates before fixed parameterized rotations, enabling high-quality VQA initialization through polynomial-time classical stabilizer simulation.
category: ai_collection
platforms: [linux, macos]
---

# CRiSP: Clifford RL for State Preparation — VQA Initialization via Reinforcement Learning

**arXiv: 2605.23138 (May 2026)**
**Authors: Gino Kwun, Dhanvi Bharadwaj, Gokul Subramanian Ravi**

## Overview

CRiSP (Clifford Reinforcement Learning agent for State Preparation) formulates the problem of finding optimal Clifford gate prefixes for Variational Quantum Algorithms (VQAs) as a sequential decision-making problem. It uses Neural-Guided Monte Carlo Tree Search (MCTS) driven by a Transformer-based policy trained via self-play.

### Key Innovation

Traditional VQA initialization methods struggle because the combinatorial search space of Clifford circuits is vast. CRiSP replaces heuristic search with learned search, using RL to discover Clifford prefixes that produce high-quality initial states for VQA parameter optimization.

## Core Methodology

### 1. Problem Formulation

- **State**: Partial Clifford prefix (sequence of Clifford gates inserted before parameterized rotations)
- **Action**: Select next Clifford gate to append to prefix
- **Reward**: Energy achieved after classical stabilizer simulation of the resulting state
- **Goal**: Find Clifford prefix that minimizes energy for the target Hamiltonian

### 2. Architecture

- **Neural-Guided MCTS**: Uses a Transformer-based policy network to guide the tree search
- **Self-Play Training**: The agent plays against itself, generating training data from MCTS rollouts
- **Curriculum Learning**: Progressively expands the search horizon (prefix length) during training

### 3. Clifford Gate Prefix

- Inserts learned Clifford gates before fixed parameterized rotations in the VQC
- All operations are classically simulable via stabilizer formalism (polynomial time)
- Does NOT alter the underlying circuit architecture — only the initialization

### 4. Workflow

```
1. Initialize empty prefix
2. For each step:
   a. Query Transformer policy for next gate distribution
   b. Run MCTS guided by policy + stabilizer simulation reward
   c. Select highest-scoring Clifford gate
   d. Append to prefix
3. After prefix construction: parameterized rotations are optimized from this warm-start initialization
```

## Key Results

- **Up to 22 qubits** and **1,370 parameters** benchmarks
- **3.17× mean improvement** (max 45.02×) in average energy accuracy over state-of-the-art Clifford initialization
- **2.44× mean improvement** (max 16.01×) in best-achieved energy accuracy
- Evaluated on QAOA and VQE tasks
- Demonstrates robustness and generalizability

## When to Use

- You need to improve VQA convergence (QAOA, VQE) without modifying circuit architecture
- You have a target Hamiltonian and want to find a good initial state classically
- You want to mitigate barren plateaus in VQA training
- You need to reduce quantum resource requirements by pre-training classically

## Implementation Considerations

- Requires a stabilizer simulator (e.g., Stim, Qiskit's Clifford simulator, or custom)
- Transformer policy can be implemented with standard RL frameworks (e.g., Ray RLlib, Stable-Baselines3, or custom PyTorch)
- MCTS implementation with UCB-based exploration
- Curriculum learning: start with short prefixes (e.g., 2-4 gates), gradually increase to 10-20+

## Activation

**Keywords**: CRiSP, Clifford RL, VQA initialization, variational quantum algorithm, QAOA warm-start, MCTS quantum, Transformer quantum, stabilizer simulation, barren plateau mitigation, quantum RL, classical state preparation

## References

- arXiv:2605.23138 — CRiSP original paper
- arXiv:2404.08712 — Clifford-based warm-starting for VQAs
- arXiv:2305.07590 — MCTS for quantum circuit compilation
- arXiv:2207.11862 — Stabilizer formalism and Clifford simulation
