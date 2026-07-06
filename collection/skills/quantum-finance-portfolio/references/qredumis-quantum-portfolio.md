# qReduMIS: Quantum-Informed Portfolio Selection

**Source**: arXiv 2607.01037 (Yalovetzky et al., Quantinuum, 2026)

## Core Algorithm

qReduMIS reformulates portfolio diversification as **Maximum Independent Set (MIS)** on asset correlation graphs, then uses a recursive hybrid quantum-classical loop:

1. **QAOA as Oracle, Not Solver**: Run QAOA (p=2) on correlation graph to measure node inclusion probabilities
2. **Frozen Node Detection**: Nodes appearing in >90% (or <10%) of high-quality solutions are "frozen" — confidently in/out of optimal portfolio
3. **Classical Reductions**: Remove frozen nodes and their neighbors; apply dominance/clique reductions
4. **Recursion**: Repeat on remaining subgraph until solved classically

## Performance on Real Hardware

| Index | Assets | QAOA Success | qReduMIS Success | Approx Ratio |
|-------|--------|-------------|-----------------|-------------|
| DJIA | 30 | ~0.80 | ~0.95 | ≥0.96 |
| S&P 100 | 100 | ~0.15 | ~0.40 | ≥0.96 |
| Nikkei 225 | 225 | ~0.05 | ~0.95 | ≥0.96 |

**Key result**: Time-to-solution scaling exponent is **3.2× smaller** than standalone QAOA.

## QUBO Formulation

```
Maximize: Σ w_i * x_i
Subject to: x_i + x_j ≤ 1  ∀ edges (i,j)
            x_i ∈ {0, 1}
```

Where edge (i,j) exists if correlation(i,j) > threshold, and w_i = asset quality metric.

## When to Use

- Portfolio universes of 50+ assets where classical MIS is hard
- Hybrid quantum-classical workflows (not pure quantum)
- Benchmarking quantum advantage on real financial data
- When you need approximation guarantees (≥0.96) not just heuristics

## Key Insight for Future Work

The "frozen node oracle" pattern generalizes beyond finance: use quantum sampling to identify structurally easy variables, recurse on the hard remainder. This is the pragmatic path to quantum advantage for combinatorial optimization.
