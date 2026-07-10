---
name: magic-informed-quantum-architecture-search
description: "Magic-Informed Quantum Architecture Search (QAS) methodology using Monte Carlo Tree Search with Graph Neural Networks for quantum circuit design. Use when designing quantum circuits with controlled nonstabilizerness (magic) levels, when optimizing quantum architecture search, when applying AlphaGo-style MCTS to quantum problems, when estimating magic properties of quantum circuits using GNNs, or when searching for optimal quantum circuit structures balancing magic resource requirements."
metadata:
  arxiv_id: "2605.03932"
  published: "2026-05-05"
  authors: "Vincenzo Lipardi, Domenica Dibenedetto, Georgios Stamoulis, Mark H.M. Winands"
  tags: [quantum-architecture-search, monte-carlo-tree-search, graph-neural-networks, quantum-magic, nonstabilizerness, circuit-design]
---

# Magic-Informed Quantum Architecture Search

## Description

Methodology for quantum architecture search that uses nonstabilizerness (magic) as a guiding resource. Combines Monte Carlo Tree Search (MCTS) with Graph Neural Networks (GNN) to estimate magic properties of candidate circuits and steer the search toward desired magic regimes.

## Activation Keywords

- magic-informed architecture search
- quantum architecture search MCTS
- nonstabilizerness-guided circuit design
- magic-based quantum optimization
- MCTS quantum circuit search
- GNN magic estimation
- quantum circuit architecture search
- AlphaGo-style quantum design
- 魔力量子架构搜索
- 非稳定化力量子电路设计

## Core Concepts

### Magic (Nonstabilizerness)

Magic quantifies quantum advantage beyond classical simulation. Stabilizer states can be efficiently simulated classically; magic states enable universal quantum computation.

- High-magic circuits: Greater quantum advantage potential
- Low-magic circuits: More classically simulable, easier to verify
- Magic is a consumable resource in quantum computation

### Architecture Search Framework

MCTS explores the space of quantum circuit architectures. GNN provides heuristic guidance by estimating magic properties of partial circuits.

## Methodology

### Step 1: Problem Formulation

Define target objective:
- Ground-state energy estimation
- Quantum state approximation
- Circuit synthesis for target unitary
- Specify target magic level (high/low/intermediate)

### Step 2: MCTS Configuration

- **Selection**: UCB with magic-based bias from GNN
- **Expansion**: Add quantum gates from allowed gate set
- **Simulation**: Estimate magic using GNN proxy model
- **Backpropagation**: Update node statistics with magic-weighted rewards

### Step 3: GNN Magic Estimation

- Represent circuits as graphs (gates as nodes, qubits as edges)
- GNN predicts magic metric for partial circuits
- Enables O(1) magic estimation vs exponential exact computation
- Trains on diverse circuit families for generalization

### Step 4: Magic Bias Integration

- High-magic bias: Steer search toward quantum-advantageous circuits
- Low-magic bias: Favor efficiently simulable circuits
- Adaptive bias: Adjust during search based on progress

## Usage Patterns

### Pattern 1: High-Magic Circuit Discovery

Find circuits maximizing quantum advantage:
1. Set high-magic bias in GNN
2. Run MCTS with magic-weighted selection
3. Extract circuits with highest magic per gate count
4. Verify magic using exact methods on final candidates

### Pattern 2: Low-Magic Approximation

Find classically-simulable approximations:
1. Set low-magic bias
2. Search for circuits approximating target with minimal magic
3. Useful for hybrid quantum-classical workflows
4. Enables classical verification of quantum results

### Pattern 3: Magic-Aware State Preparation

Prepare quantum states with controlled magic:
1. Define target state fidelity threshold
2. Optimize for magic level constraint
3. Trade-off between state fidelity and magic cost

## Key Findings

- Magic-informed search consistently outperforms uninformed baselines
- GNN generalizes to out-of-distribution circuit sizes
- Problem-agnostic magic bias improves solution quality across domains
- Effective for both structured and unstructured problems

## Implementation Guidelines

### MCTS Parameters
- Tree depth: Scale with circuit depth target
- Iterations: 1000-10000 per search
- GNN inference: Batch for parallel evaluation
- Magic estimation: Use efficient proxies (stabilizer extent, mana)

### GNN Architecture
- Graph input: Circuit connectivity and gate types
- Output: Scalar magic estimate
- Training: Supervised on exact magic calculations
- Generalization: Test on varying qubit counts and depths

## Error Handling

### GNN Out-of-Distribution
- Detect when GNN operates on unseen circuit patterns
- Fall back to exact magic computation for small circuits
- Use confidence intervals from GNN predictions

### Search Stagnation
- Monitor improvement rate in MCTS
- Adjust exploration-exploitation balance
- Restart with different random seeds

## Related Concepts

- Stabilizer formalism and Clifford gates
- Quantum resource theories
- Neural architecture search (NAS)
- AlphaGo/AlphaZero-style MCTS
- Quantum circuit compilation
- Variational quantum algorithms
