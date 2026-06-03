---
name: crisp-rl-quantum-state-preparation
description: CRiSP (Clifford Reinforcement Learning agent for State Preparation) — RL-based classical state preparation for VQA warm-start using Neural-Guided MCTS with Transformer policy.
---

# CRiSP: Classical State Preparation for VQAs via Reinforcement Learning

CRiSP (Clifford Reinforcement Learning agent for State Preparation) framework from arXiv:2605.23138 (May 2026). Formulates discrete Clifford gate prefix selection as a sequential decision-making problem for warm-starting Variational Quantum Algorithms (VQAs).

## Core Technique

CRiSP uses Neural-Guided Monte Carlo Tree Search (MCTS), driven by a Transformer-based policy trained via self-play, to insert learned Clifford gates before fixed parameterized rotations. This constructs high-quality initial states entirely through polynomial-time classical stabilizer simulation without altering the underlying circuit architecture.

### Key Components

1. **Reinforcement Learning Formulation**: Formulates Clifford prefix selection as an MDP where the agent sequentially selects Clifford gates to prepend
2. **Neural-Guided MCTS**: Combines MCTS planning with a learned Transformer policy for efficient search over combinatorial spaces
3. **Self-Play Training**: The agent improves via self-play, iteratively generating training data from its own search trajectories
4. **Curriculum Learning**: Progressively expands the search horizon to scale to deep circuits
5. **Stabilizer Simulation**: All Clifford operations are classically simulable in polynomial time

## Performance

- Evaluated on QAOA benchmarks up to 22 qubits and 1,370 parameters
- Outperforms state-of-the-art Clifford initialization methods:
  - Mean 3.17× improvement in average energy accuracy (max 45.02×)
  - Mean 2.44× improvement in best-achieved energy accuracy (max 16.01×)
- VQE tasks demonstrate robustness and generalizability

## Activation

crisp, clifford-reinforcement-learning, rl-qaoa-initialization, neural-mcts-quantum, quantum-state-preparation-rl

## When to Use

- Initializing VQA circuits (QAOA, VQE) to avoid barren plateaus
- Warm-starting quantum optimization with classically optimized Clifford prefixes
- Any scenario where a good initial state can accelerate variational quantum optimization
- Benchmarking RL-based vs heuristic-based initialization methods

## Implementation Pattern

```
1. Define Clifford gate pool (H, S, CNOT, etc.)
2. Train Transformer policy via self-play with Neural-Guided MCTS
3. During search: MCTS explores Clifford gate sequences, guided by policy
4. Select best prefix by evaluating energy expectation via stabilizer simulation
5. Prepend prefix before parameterized VQA circuit
6. Run VQA/QAOA optimization starting from Clifford-warm-started state
```
