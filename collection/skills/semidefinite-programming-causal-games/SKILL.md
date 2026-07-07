---
name: semidefinite-programming-causal-games
description: "GPU-accelerated semidefinite programming for causal game analysis — using SDP hierarchies to compute bounds in causal inference games, with GPU acceleration for scalability. From arXiv:2606.20519."
metadata:
  arxiv_id: "2606.20519"
  published: "2026-06-18"
  authors: "Boghiu, Simonov"
---

# GPU-Accelerated SDP for Causal Games

## Core Concept

Semidefinite programming (SDP) hierarchies provide computable bounds for causal inference problems formulated as games. GPU acceleration enables scaling these computations to larger causal structures that were previously intractable.

## Methodology

### 1. Formulate the Causal Game
- Express the causal inference problem as a game between Nature and an observer
- Identify the causal constraints and compatibility conditions
- Map to a polynomial optimization problem

### 2. SDP Hierarchy Construction
- Use the NPA (Navascués-Pironio-Acín) or similar hierarchy
- Each level provides tighter bounds on the causal compatibility
- Higher levels → more accurate but computationally expensive

### 3. GPU Acceleration
- Reformulate SDP constraints for parallel GPU computation
- Use cuBLAS/cuSOLVER for matrix operations
- Batch multiple SDP instances for parallel solving

## Key Advantages

- **Scalability**: GPU parallelization handles larger causal structures
- **Tight Bounds**: SDP hierarchies provide provably correct bounds
- **Causal Compatibility**: Certifies whether observed distributions are compatible with causal hypotheses

## Usage Patterns

### Pattern 1: Causal Compatibility Testing
When testing if data is compatible with a causal model:
1. Formulate the causal structure as constraints
2. Choose SDP hierarchy level based on accuracy needs
3. Solve the SDP (preferably on GPU for large instances)
4. Interpret feasibility: feasible → compatible, infeasible → ruled out

### Pattern 2: Causal Bound Computation
When computing bounds on causal effects:
1. Express the causal quantity as an objective function
2. Add causal constraints from the graph structure
3. Solve SDP at increasing hierarchy levels until convergence
4. Report bounds at the highest computable level

## Pitfalls

### Hierarchy Level Selection
- Low levels: fast but loose bounds
- High levels: tight but may exceed GPU memory
- Start at level 2, increase until memory/time constraints

### Numerical Stability
- SDP solvers can have numerical issues at high levels
- Use appropriate tolerance settings
- Verify results across different solvers when possible

## Activation
- SDP causal games, semidefinite programming causal inference, GPU causal analysis
- 因果推断, 半定规划, 因果博弈
- causal compatibility, NPA hierarchy, quantum causal models
