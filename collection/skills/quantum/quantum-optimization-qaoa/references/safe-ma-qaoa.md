# SAFE ma-QAOA: Surrogate-Assisted Fine-Tuning Framework

## Source
Kim, H. & Lee, Y. "SAFE ma-QAOA: Surrogate-Assisted and Fine-Tuning Enhanced Multi-Angle QAOA with Parameter Distillation" (arXiv:2605.23377, May 2026)

## Three-Phase Architecture

### Phase 1: Surrogate Pre-training (Classical, Zero QPU)
- Use **Low-Weight Pauli Propagation (LWPP)** as classical surrogate
- Truncates high-weight Pauli terms to approximate quantum state evolution
- Pre-trains all ma-QAOA parameters classically
- Benefits: rapid exploration, zero quantum hardware cost

### Phase 2: Parameter Distillation
- Identify angles near zero after surrogate convergence
- Remove these parameters from optimization (≈64.3% reduction)
- Exploits natural sparsity in ma-QAOA parameter landscape

### Phase 3: Exact Fine-tuning (Quantum)
- Optimize remaining active parameters on exact quantum objective
- Only distilled subset requires QPU evaluations
- Achieves 94.5% QPU workload reduction vs exact-only baseline

## Key Results
- SK model, 2D spin glass, Max-Cut benchmarks
- 64.3% fewer active parameters, 94.5% less QPU work
- 44.4% fewer optimizer steps with distillation vs without

## When to Apply
- ma-QAOA with many independent parameters
- NISQ hardware with limited QPU budget
- LWPP surrogate tractable (low-depth circuits)

## Pitfalls
- LWPP truncation error grows with circuit depth
- Distillation threshold must be tuned per problem class
- Surrogate may miss higher-order quantum correlations
