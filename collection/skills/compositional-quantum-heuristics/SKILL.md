---
name: compositional-quantum-heuristics
description: "Compositional Quantum Heuristics methodology for mitigating barren plateaus in quantum machine learning. Use when designing scalable quantum learning models, constructing group-invariant loss functions, building permutation-equivariant quantum graph neural networks for graph optimization, or implementing recursive hybrid quantum-classical heuristics. Covers barren plateau mitigation, symmetry-induced inductive bias, compositional circuit assembly, and QIRO-inspired recursive optimization. Trigger: compositional quantum, barren plateau mitigation, quantum graph neural network, max-clique quantum, QIRO, permutation-equivariant quantum, group-invariant loss"
---

# Compositional Quantum Heuristics

## Core Idea

Assemble larger quantum models from smaller trainable subcomponents to mitigate barren plateaus. Instead of training one large parameterized quantum circuit (which vanishes gradients), build group-invariant loss functions that introduce symmetry-induced inductive bias, improving gradient behavior and generalization.

## Key Patterns

### 1. Compositional Circuit Assembly

```
Large circuit → [Sub-component A] + [Sub-component B] + ...
```

- Train each subcomponent independently (trainable)
- Compose into larger model for inference
- Each component stays in the trainable regime (not too expressive to cause barren plateaus, not too simple to be classically simulatable)

### 2. Group-Invariant Loss Functions

Construct loss functions invariant under a group G acting on inputs:

```
L(θ) = E_{x,y}[ℓ(f_θ(x), y)]  where  f_θ(g·x) = g·f_θ(x)  ∀g∈G
```

- For graph problems: use permutation-equivariant quantum GNNs
- Symmetry reduces effective parameter space, improving gradient flow
- Inductive bias → better generalization to larger problem instances

### 3. Permutation-Equivariant Quantum GNN for Graph Problems

For identifying maximal cliques or graph optimization:

1. Encode graph structure into quantum state via adjacency-based embedding
2. Apply permutation-equivariant quantum layers (commute with vertex relabeling)
3. Measure to predict node/edge labels (e.g., clique membership)
4. Training: use group-invariant loss that respects graph symmetries

### 4. Recursive Hybrid Quantum-Classical Heuristic (QIRO-inspired)

```
while not converged:
    1. Run quantum model → get probability distribution over solutions
    2. Select highest-confidence assignments
    3. Fix those variables in the classical problem
    4. Reduce problem size, recurse on subproblem
```

- Quantum model guides classical search (not solving end-to-end)
- Each recursion reduces problem size
- Demonstrated improved inference accuracy and scalability vs. pure classical

## Trainability vs. Classical Simulatability Trade-off

| Circuit Expressiveness | Trainability | Classical Simulatability |
|----------------------|-------------|------------------------|
| Low | ✅ Good | ✅ Easy to simulate (no quantum advantage) |
| Medium | ✅ Good | ⚠️ Hard to simulate (sweet spot) |
| High | ❌ Barren plateaus | ⚠️ Hard to simulate |

Compositional approach keeps subcomponents in the "medium" regime.

## When to Use

- Quantum ML models suffering from barren plateaus
- Graph combinatorial optimization (max-clique, max-cut, graph coloring)
- Need to scale quantum models beyond small qubit counts
- Hybrid quantum-classical algorithm design
- QML model generalization to larger problem instances

## Verification

1. Check gradient magnitudes stay above threshold (e.g., > 1e-4) during training
2. Test generalization: train on small graphs, evaluate on larger ones
3. Compare recursive heuristic accuracy vs. baseline classical methods
4. Verify permutation equivariance: permute input graph → permuted output

## References

- arXiv:2605.07611 - Compositional Quantum Heuristics for Max-Clique Detection (Duneau, Krawchuk, Pearson, 2026)
