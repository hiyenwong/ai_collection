---
name: hqnn-expressibility-trainability-nas
description: "Hybrid Quantum Neural Network (HQNN) architecture design methodology based on expressibility-trainability analysis and multi-objective neural architecture search. Use when designing hybrid quantum-classical models, optimizing parameterized quantum circuits (PQCs), selecting entanglement topologies, performing neural architecture search for quantum models, or analyzing the expressibility-trainability trade-off in quantum machine learning. Covers PQC depth selection, qubit count optimization, classical-quantum hybrid training strategies, and Pareto-optimal architecture discovery. Activation: quantum neural network design, HQNN architecture, expressibility trainability, quantum NAS, barren plateau mitigation, hybrid quantum training, PQC optimization."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.25768"
  published: "2026-05-25"
  authors: "Muhammad Kashif, Muhammad Shafique"
  tags: [quantum, machine-learning, neural-architecture-search, hybrid-models]
---

# HQNN Expressibility-Trainability NAS Methodology

Based on arXiv:2605.25768 — "Rethinking Expressibility-Trainability Trade-off in Hybrid Quantum Neural Networks" (ICML 2026).

## Key Findings

The commonly assumed trade-off between PQC expressibility and trainability (highly expressive = more barren plateaus) is **weak and regime-dependent** in pure PQCs, and **can be eliminated** in hybrid architectures under full end-to-end training. Classical components reshape the optimization landscape, decoupling trainability from PQC expressibility.

## Design Principles

### 1. Hybridization Matters

- Pure PQC analysis alone is insufficient for predicting HQNN performance
- Classical network layers reshape the loss landscape
- Full end-to-end training can eliminate the expressibility-trainability trade-off
- Don't avoid expressive circuits out of barren plateau fear — test with hybrid training

### 2. Multi-Objective NAS Framework

Jointly optimize three objectives over combined classical-quantum design space:
- **Expressibility**: Circuit's ability to represent diverse unitaries
- **Trainability**: Gradient variance, barren plateau susceptibility
- **Task Performance**: Accuracy/loss on the target task

Reveals different Pareto-optimal solutions under:
- Quantum-only training (PQC parameters only)
- Full hybrid training (classical + quantum parameters)

### 3. Architecture Search Space

```
Quantum parameters:
  - Circuit depth (number of layers)
  - Qubit count
  - Entanglement topology (linear, ring, all-to-all, tree)
  - Gate types and parameterization

Classical parameters:
  - Network depth and width
  - Activation functions
  - Connection patterns to PQC
```

## Practical Workflow

### Step 1: Baseline Characterization

```python
def characterize_pqc(circuit, n_shots=1024):
    """Measure expressibility and trainability of a PQC."""
    # Expressibility: KL divergence from Haar measure
    expressibility = compute_kl_from_haar(circuit, n_samples=1000)
    
    # Trainability: gradient variance across parameter space
    gradients = compute_gradient_variance(circuit, n_points=100)
    trainability = 1.0 / (1.0 + np.var(gradients))  # Higher = better
    
    return expressibility, trainability
```

### Step 2: Hybrid Integration Analysis

```python
def test_training_regimes(hqnn, X, y):
    """Compare quantum-only vs full hybrid training."""
    # Regime A: Freeze classical, train PQC only
    pqc_only_metrics = train_and_evaluate(hqnn, X, y, freeze_classical=True)
    
    # Regime B: Full end-to-end training
    full_metrics = train_and_evaluate(hqnn, X, y, freeze_classical=False)
    
    # Compare: full training should show decoupled expressibility-trainability
    return pqc_only_metrics, full_metrics
```

### Step 3: Multi-Objective NAS

```python
def nas_hqnn(search_space, objectives=['expressibility', 'trainability', 'accuracy']):
    """Pareto-optimal architecture search."""
    # Use NSGA-II or similar MOEA
    population = initialize_population(search_space)
    
    for gen in range(n_generations):
        # Evaluate all three objectives
        fitness = [evaluate(arch, objectives) for arch in population]
        
        # Non-dominated sorting + crowding distance
        population = nsga2_select(population, fitness)
    
    # Return Pareto front
    return get_pareto_front(population)
```

## Entanglement Topology Selection

- **Linear**: Low expressibility, high trainability — good for shallow circuits
- **Ring**: Balanced expressibility-trainability — good default
- **All-to-all**: Highest expressibility, variable trainability — test with full hybrid training
- **Tree**: Moderate expressibility, good trainability — good for constrained qubit count

## When to Apply

- Designing quantum-classical hybrid models
- Experiencing barren plateaus in QML training
- Selecting PQC architecture for a specific task
- Performing neural architecture search with quantum components
- Analyzing why a QNN isn't training despite high expressibility

## Pitfalls

- **Don't** use pure PQC expressibility metrics to predict HQNN performance
- **Don't** assume high expressibility always causes barren plateaus in hybrid settings
- **Do** test with full end-to-end training before concluding a circuit is untrainable
- **Do** use multi-objective optimization — no single architecture dominates all three objectives
