---
name: equivariant-rl-clifford
description: >
  Equivariant reinforcement learning for Clifford quantum circuit synthesis.
  Use when synthesizing Clifford quantum circuits with RL, designing
  equivariant neural networks for quantum tasks, building size-agnostic
  policies across qubit counts, or optimizing quantum circuit compilation
  with all-to-all connectivity. Covers graph-based state representations,
  permutation-equivariant architectures, and RL reward design for gate synthesis.
  Activation: equivariant RL, quantum circuit synthesis, Clifford circuits,
  RL quantum, permutation equivariant, qubit routing, quantum compilation,
  量子线路综合, 等变强化学习, Clifford synthesis.
---

# Equivariant RL for Clifford Quantum Circuit Synthesis

Methodology from arXiv:2605.10910 (Yeung, Kissinger, Cornish, 2026-05-11).

## Core Innovation

Synthesize Clifford quantum circuits via RL using a **permutation-equivariant** neural network architecture that is **size-agnostic** — a single learned policy generalizes across different qubit counts.

## Key Results

- Agent finds circuits within one two-qubit gate of optimality in milliseconds per instance
- Optimal circuits found in 99.2% of instances
- Single policy works across varying qubit counts (transfer learning by design)

## Architecture

### State Representation

- Represent quantum circuit state as a graph over qubits
- Nodes: qubits with local Clifford tableau information
- Edges: two-qubit gate history / entanglement structure
- State update: apply gate action to graph (local modification)

### Permutation-Equivariant Network

- **Critical property**: relabeling qubits should produce equivalent output
- Network architecture respects S_n (symmetric group) equivariance
- Use graph neural network (GNN) or similar permutation-invariant layers
- Output: distribution over valid gate actions (invariant to qubit ordering)

### Action Space

- Actions: apply specific quantum gates (CNOT, H, S, etc.)
- For all-to-all connectivity: any qubit pair can receive two-qubit gates
- Action masking: exclude redundant or identity operations

### Reward Design

- **Primary**: negative gate count (minimize circuit depth)
- **Termination**: bonus when target Clifford is reached
- **Penalty**: small per-step cost to encourage shorter circuits
- Verification: check equivalence via stabilizer formalism (Clifford simulation is efficient)

## Workflow

### Step 1: Define Target Clifford

```python
# Target specified as stabilizer tableau or unitary
# Clifford group on n qubits has efficient classical representation
# via stabilizer tableau (Gottesman-Knill theorem)
target_tableau = get_clifford_target(n_qubits)
```

### Step 2: Initialize RL Environment

```python
env = CliffordCircuitEnv(
    n_qubits=n,
    action_space='all_to_all',
    gates=['CNOT', 'H', 'S'],
    max_steps=50
)
```

### Step 3: Build Equivariant Policy Network

```python
# Key: network must be equivariant to qubit permutations
policy = EquivariantCliffordNet(
    node_dim=tableau_dim,
    edge_dim=connectivity_dim,
    hidden_dim=128,
    num_layers=4
)
# Output: P(action | state) invariant under qubit relabeling
```

### Step 4: Train with PPO or Similar

```python
# Standard RL training loop
for episode in range(num_episodes):
    state = env.reset()
    while not done:
        action = policy.select_action(state)
        next_state, reward, done = env.step(action)
        # Verify: check if current circuit = target Clifford
        if env.verify_equivalence(target_tableau):
            reward += terminal_bonus
        store_transition(state, action, reward)
```

### Step 5: Evaluate

```python
# Metrics:
# 1. Optimality gap: gates_found - gates_optimal
# 2. Success rate: % of instances solved optimally
# 3. Generalization: test on unseen qubit counts
# 4. Inference time: ms per instance
```

## Why Equivariance Matters

1. **Data efficiency**: symmetry constraints reduce effective search space exponentially
2. **Generalization**: policy learned on 3 qubits works on 8 qubits
3. **Physical correctness**: quantum gates commute with qubit relabeling — architecture respects this
4. **No retraining**: deploy single model across device sizes

## Pitfalls

- **Tableau representation**: must use efficient Clifford simulation (not full state vector). Stabilizer tableaux update in O(n²) per gate.
- **Action space size**: for n qubits with all-to-all connectivity, O(n²) two-qubit actions. Use action masking to reduce.
- **Reward sparsity**: reaching exact Clifford match is sparse. Add intermediate rewards (e.g., Hamming distance between current and target tableau).
- **Equivalence checking**: Clifford equivalence is O(n³) via tableau comparison — fast enough for RL but don't use full state vector simulation.
- **Over-counting**: multiple gate sequences produce same Clifford. Factor out global phases and redundant gate orderings.

## Extensions

- **Noisy devices**: add gate error rates to reward function
- **Hardware constraints**: modify action space for limited connectivity (linear, grid)
- **Non-Clifford gates**: extend to include T-gate synthesis (requires non-stabilizer simulation)
- **Multi-objective**: jointly optimize depth, gate count, and fidelity

## References

- arXiv:2605.10910 — Equivariant Reinforcement Learning for Clifford Quantum Circuit Synthesis
- Gottesman-Knill theorem: efficient classical simulation of Clifford circuits
- Stabilizer formalism for quantum error correction
