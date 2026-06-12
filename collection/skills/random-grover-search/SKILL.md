---
name: random-grover-search
description: "Randomized Grover search algorithm that directly uses constraint oracles instead of constructing a global oracle for the intersection. At each iteration, randomly selects one constraint oracle for amplitude amplification, achieving quadratic speedup for multi-constraint search problems. arXiv:2606.11759"
category: "quantum-algorithms"
metadata:
  arxiv_id: "2606.11759"
  authors: "Dekuan Dong, Jiaxin Ma, Yingzhou Li"
  published: "2026-06-10"
---

## Context

Grover's algorithm achieves quadratic speedup for unstructured search given a global oracle for the target set. However, when the target set is specified as the intersection of multiple constraint sets, constructing a global oracle for the intersection can be costly. Individual constraint oracles are often much simpler to implement.

## Core Methodology

1. **Randomized oracle selection**: At each iteration, randomly select one constraint oracle from the available set
2. **Amplitude amplification**: Apply Grover diffusion operator after each random oracle application
3. **Convergence analysis**: Prove that the randomized scheme maintains quadratic speedup relative to classical search
4. **Multi-constraint intersection**: Target set = intersection of k constraint sets, each with its own simple oracle

## Implementation Steps

1. Define k constraint oracles O_1, O_2, ..., O_k, each marking elements satisfying one constraint
2. Initialize uniform superposition over search space
3. At each Grover iteration:
   a. Randomly select oracle O_j uniformly from {O_1, ..., O_k}
   b. Apply O_j (phase flip for elements satisfying constraint j)
   c. Apply Grover diffusion operator
4. After O(√(N/M)) iterations (where M = |target set|), measure to find solution
5. Verify solution satisfies ALL constraints (classical post-processing)

## Pitfalls

- **Oracle selection bias**: Uniform random selection may not be optimal if constraints have different selectivities
- **Convergence rate**: Randomized scheme may require more iterations than optimal global oracle
- **Solution verification**: Must classically verify all constraints after measurement

## Verification

- Verify quadratic scaling: runtime ∝ √N for search space of size N
- Test on problems with known solutions (e.g., SAT instances with known satisfying assignments)
- Compare iteration count against standard Grover with constructed global oracle

## Activation

Grover search, randomized oracle, constraint satisfaction, amplitude amplification, quadratic speedup, multi-constraint search
