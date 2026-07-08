---
name: quantum-informed-portfolio-qredumis
description: "qReduMIS: recursive hybrid quantum-classical algorithm for portfolio diversification via Maximum Independent Set on asset correlation graphs. Uses QAOA measurements to identify frozen nodes, guiding provably optimal classical reductions. Validated on Quantinuum 98-qubit trapped-ion Helios system. Activation: portfolio optimization, quantum portfolio, QAOA finance, qReduMIS, trapped-ion portfolio, maximum independent set, asset correlation graph, quantum finance pipeline, MIS portfolio, frozen node reduction"
metadata:
  arxiv_id: "2607.01037"
  published: "2026-07-01"
  authors: "Romina Yalovetzky, Martin J. A. Schuetz, Zichang He, Jiayu Shen, Yue Sun, Rudy Raymond, Shauna Sahay, Kishore Perla, Ruben S. Andrist, Grant Salton, Helmut G. Katzgraber, Roger Bongiovanni, Niraj Kumar, Rob Otter"
---

# Quantum-Informed Portfolio Selection (qReduMIS)

## Overview

Portfolio diversification formulated as Maximum Independent Set (MIS) on asset correlation graphs. qReduMIS is a recursive hybrid quantum-classical algorithm that leverages QAOA measurements to identify **frozen nodes** — vertices likely to belong to optimal solutions — thereby guiding and unblocking subsequent provably optimal classical reductions on the remaining graph.

## Key Results

| Metric | S&P 100 | Nikkei 225 | All 4 Indices |
|--------|---------|------------|---------------|
| QAOA success | Fails | Fails | - |
| qReduMIS success | 0.40 | 0.95 | >= 0.96 approx ratio |
| Qubits used | - | up to 78 | - |
| Two-qubit gates | - | up to 1016 | - |
| TTS exponent reduction | 3.2x vs standalone QAOA (p=2) | | |

**Hardware**: Quantinuum 98-qubit trapped-ion Helios system, benchmarked on 73 asset correlation graphs via H2-1 noisy emulator.

## Core Algorithm

```
qReduMIS(G):
1. Run QAOA on graph G (p=2 layers)
2. Measure independent set samples
3. Identify frozen nodes (vertices consistently in/not in IS across samples)
4. Apply classical reductions using frozen node assignments
5. If reduced graph non-trivial, recurse: qReduMIS(G_reduced)
6. Return combined solution
```

### Why This Works

- Standalone QAOA fails on large portfolios (S&P 100, Nikkei 225) due to solution space complexity
- QAOA measurements still contain useful structural signal — frozen nodes
- Classical reductions are provably optimal but get blocked by ambiguous nodes
- qReduMIS unblocks reductions by using QAOA to resolve ambiguity at frozen nodes
- Combined approach achieves 3.2x better time-to-solution scaling than either alone

## Application Pipeline

1. **Build correlation graph**: Compute pairwise asset correlations from market data
2. **Threshold to edges**: Assets with correlation > threshold → edge in graph
3. **Formulate MIS**: Maximum independent set = maximum diversified portfolio
4. **Run qReduMIS**: Hybrid quantum-classical recursive solver
5. **Extract portfolio**: Independent set = selected assets for diversification

## Implementation Notes

- QAOA depth p=2 achieves best TTS scaling in experiments
- Frozen node identification uses statistical consistency across measurement samples
- Classical reductions include: degree-1 removal, twin vertex merging, folding
- Works on real market data from S&P 100, S&P 500, Nikkei 225, FTSE 100

## Pitfalls

- **QAOA alone is insufficient**: For portfolios >50 assets, standalone QAOA fails to find optimal solutions
- **Threshold selection matters**: Correlation threshold directly impacts graph density and MIS difficulty
- **Emulator vs hardware**: Results on noisy emulator may differ from real hardware; validate on actual device when possible
- **Recursion depth**: Monitor recursion depth to avoid excessive QAOA calls on small subgraphs

## Related Skills

- `quantum-portfolio-optimization` — Umbrella skill covering QAOA, QA, and qReduMIS portfolio methods
- `quantum-finance-portfolio` — broader quantum finance portfolio methods
- `quantum-portfolio-optimizer` — QAOA + QRL integration
- `penalty-free-quantum-optimization` — penalty-free QAOA approach

## References

- arXiv: 2607.01037 — "Quantum-Informed Portfolio Selection: An End-to-End Pipeline Validated on Trapped-Ion Hardware with Real Market Data"
