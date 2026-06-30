---
name: quantum-enhanced-mcts
version: v1.0.0
last_updated: 2026-06-30
description: "AtomTreeSearch: Hybrid classical-quantum algorithm integrating quantum subroutines (maximal weighted independent set on neutral-atom computers) within Monte Carlo Tree Search for combinatorial optimization. Quantum subroutine produces more diverse and higher-quality branches than classical alternatives. Validated on TSP up to 60 cities (random Euclidean) and 100 cities (TSPLIB). Keywords: quantum MCTS, combinatorial optimization, neutral-atom quantum, TSP quantum, hybrid classical-quantum, AtomTreeSearch, Monte Carlo Tree Search quantum."
---

# Quantum-Enhanced Monte Carlo Tree Search (AtomTreeSearch)

## Description

AtomTreeSearch is a hybrid classical-quantum algorithm that embeds a quantum subroutine natively implementable on neutral-atom quantum computers within a Monte Carlo Tree Search (MCTS) framework. At each expansion step, a maximal weighted independent set (MWIS) of candidate actions is selected by the quantum processor, producing more diverse and higher-quality branches than classical alternatives.

## Activation Keywords

- quantum MCTS
- combinatorial optimization quantum
- neutral-atom quantum computer
- TSP quantum solver
- hybrid classical-quantum search
- AtomTreeSearch
- quantum subroutine in MCTS
- maximal weighted independent set quantum
- 量子蒙特卡洛树搜索

## Algorithm Architecture

```
┌─────────────────────────────────────────┐
│           Classical MCTS Loop           │
│                                         │
│  Selection → Expansion → Simulation     │
│                    │                    │
│              ┌─────▼─────┐              │
│              │  Quantum   │              │
│              │ Subroutine │              │
│              │  (MWIS)    │              │
│              └─────┬─────┘              │
│                    │                    │
│              Backpropagation            │
└─────────────────────────────────────────┘
```

## Workflow

### Step 1: Problem Formulation as MCTS

```python
class TSPState:
    def __init__(self, n_cities, distance_matrix):
        self.n_cities = n_cities
        self.dist_matrix = distance_matrix
        self.visited = set()
        self.path = []
    
    def get_candidate_actions(self):
        """Return set of unvisited cities as candidate actions"""
        return set(range(self.n_cities)) - self.visited
```

### Step 2: Quantum Subroutine — MWIS Selection

The key innovation: at each MCTS expansion step, instead of using a classical heuristic to select the next action, use a quantum processor to find a maximal weighted independent set:

```python
def quantum_mwis_selection(state, candidates):
    """
    Use neutral-atom quantum computer to select MWIS of candidate actions.
    
    The quantum subroutine:
    1. Encodes candidates as graph vertices with weights
    2. Finds MWIS using quantum annealing / neutral-atom Rydberg blockade
    3. Returns diverse, high-quality set of actions for exploration
    """
    # Map to MWIS problem
    graph = build_conflict_graph(candidates, state)
    
    # Quantum MWIS solver (neutral-atom platform)
    mwis = run_quantum_mwis(graph)
    
    return mwis
```

### Step 3: MCTS with Quantum Expansion

```python
def atom_tree_search(root_state, n_iterations=1000):
    tree = MCTSTree(root_state)
    
    for _ in range(n_iterations):
        # Selection: UCB1 tree policy
        node = tree.select()
        
        if not node.is_terminal():
            # Expansion: Use quantum MWIS for action selection
            candidates = node.state.get_candidate_actions()
            actions = quantum_mwis_selection(node.state, candidates)
            
            # Create child nodes from quantum-selected actions
            for action in actions:
                child_state = node.state.apply_action(action)
                tree.add_child(node, child_state, action)
        
        # Simulation: Rollout to estimate value
        value = rollout_simulation(node)
        
        # Backpropagation
        tree.backpropagate(node, value)
    
    return tree.get_best_action()
```

### Step 4: Classical Fallback

For NISQ-era deployment, provide classical MWIS approximation:

```python
def classical_mwis_fallback(candidates, state):
    """
    Classical greedy MWIS approximation as fallback
    when quantum hardware is unavailable.
    """
    graph = build_conflict_graph(candidates, state)
    return greedy_mwis(graph)
```

## Key Findings

### Benchmark Results (TSP)

| Instance Type | Max Cities | Performance vs OR-Tools | Performance vs Simulated Annealing |
|--------------|------------|------------------------|-----------------------------------|
| Random Euclidean | 60 | **Matches or exceeds** | **Exceeds** |
| TSPLIB | 100 | **Matches or exceeds** | **Exceeds** |

### Quantum Advantage Sources

1. **Diversity**: Quantum subroutine produces more diverse branches
2. **Quality**: Higher-quality candidate action sets
3. **Collective selection**: MWIS selects actions collectively, not greedily

## Applicable Problems

- Traveling Salesman Problem (validated)
- Vehicle Routing Problem
- Graph coloring
- Scheduling problems
- Any combinatorial optimization with MCTS-solvable structure

## Hardware Requirements

- **Quantum**: Neutral-atom platform (Rydberg blockade for MWIS)
- **Classical fallback**: Standard CPU for greedy MWIS approximation
- **Hybrid mode**: Classical MCTS + quantum subroutine at expansion

## Advantages Over Pure Quantum Approaches

1. **NISQ-compatible**: Quantum subroutine is shallow and focused
2. **Graceful degradation**: Falls back to classical MWIS
3. **Proven MCTS framework**: Builds on well-understood classical algorithm
4. **Near-term quantum utility**: Carefully scoped quantum subroutine

## Resources

- Paper: arXiv:2606.30415
- MCTS reference: Browne et al., "A Survey of Monte Carlo Tree Search Methods"
- Neutral-atom MWIS: https://pasqal.com/
