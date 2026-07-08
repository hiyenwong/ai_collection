---
name: qredumis-quantum-portfolio-pipeline
description: "qReduMIS recursive hybrid quantum-classical pipeline for portfolio diversification using QAOA frozen-node identification on asset correlation graphs. Validated on Quantinuum 98-qubit trapped-ion Helios system with real market data up to 225 assets."
version: 1.0.0
author: Hermes Agent (Cron Job)
date: 2026-07-04
source: arXiv:2607.01037
license: MIT
metadata:
  hermes:
    tags: [quantum-finance, portfolio-optimization, qaoa, hybrid-quantum-classical, qredumis]
    trigger_words: [qredumis, quantum portfolio, frozen nodes, asset correlation graph, QAOA, MIS, maximum independent set, portfolio diversification, trapped-ion, Quantinuum]
    category: ai_collection
---

# qReduMIS: Quantum-Informed Portfolio Selection Pipeline

## Core Methodology

**qReduMIS** (recursive hybrid quantum-classical algorithm for Maximum Independent Set) solves portfolio diversification by formulating it as a **Maximum Independent Set (MIS)** problem on asset correlation graphs.

### Key Insight

Rather than using quantum optimization to directly produce a final solution, qReduMIS uses **QAOA measurements to identify frozen nodes** — vertices likely to belong to optimal solutions — which then guide and unblock subsequent provably optimal classical reductions on the remaining graph.

## Pipeline Steps

1. **Asset Correlation Graph Construction**: Build correlation graph from market data (assets = vertices, high correlation = edges)
2. **QAOA Execution**: Run QAOA on quantum hardware to sample independent sets
3. **Frozen Node Identification**: Analyze measurement outcomes to find vertices that consistently appear in high-quality solutions
4. **Classical Graph Reduction**: Fix frozen nodes and reduce the remaining graph
5. **Recursive Refinement**: Repeat steps 2-4 on progressively smaller subgraphs
6. **Classical Solver**: Apply provably optimal classical solver on the final reduced graph

## Results (Validated on Real Hardware)

- **Hardware**: Quantinuum 98-qubit trapped-ion Helios system
- **QAOA circuits**: Up to 78 qubits, 1016 two-qubit gates
- **Market indices**: S&P 100, Nikkei 225, Russell 1000, and a fourth index (up to 225 assets)
- **Success probabilities**: 0.40 (S&P 100), 0.95 (Nikkei 225)
- **Approximation ratios**: ≥ 0.96 across all four indices
- **Scaling**: Optimal time-to-solution scaling exponent 3.2× smaller than standalone QAOA at p=2 layers
- **Benchmark**: 73 asset correlation graphs on Quantinuum H2-1 noisy emulator

## Why It Works

- Standalone QAOA fails on largest indices (S&P 100, Nikkei 225)
- qReduMIS succeeds by **decoupling the quantum advantage** (finding frozen nodes) from the full optimization
- Frozen node identification is **easier than finding the optimal solution** — lower computational complexity
- Classical reductions are **provably optimal** once frozen nodes are identified

## Reusable Pattern

**Quantum-Assisted Preprocessing Pattern**: Use quantum algorithms not for final solutions, but for identifying structural properties (frozen nodes, key variables) that simplify classical solving. This pattern generalizes beyond portfolio optimization to any combinatorial problem where partial structure can be identified and exploited.

## When to Use

- Portfolio diversification and asset selection problems
- Maximum Independent Set problems on large graphs
- Any combinatorial optimization where partial solutions can guide classical reductions
- NISQ-era quantum advantage scenarios where full quantum solution is infeasible

## Pitfalls

- QAOA depth (p) matters: higher p increases circuit depth but may not improve frozen node quality proportionally
- Noisy hardware limits circuit depth — trapped-ion systems preferred for deep circuits
- Graph construction quality directly affects MIS formulation quality
- Correlation threshold selection impacts graph density and MIS difficulty
