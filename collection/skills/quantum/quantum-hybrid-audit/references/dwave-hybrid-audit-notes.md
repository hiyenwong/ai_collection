# Quantum Hybrid Audit - Research Notes

## Source Paper
**Title**: Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization
**arXiv**: 2605.17623
**Categories**: quant-ph, math.OC, q-fin.PM
**Date**: 2026-05-17

## Key Findings

### Experimental Setup
- **Problem**: Cardinality-constrained mean-variance-turnover portfolio optimization
- **Size range**: N = 10 to 640 assets
- **Classical baseline**: Gurobi MIQP with optimality anchor
- **Quantum solver**: D-Wave LeapHybridCQM service
- **Wall-clock budget**: 5 seconds per run

### Results Summary
| Metric | Value |
|--------|-------|
| Instances matching Gurobi optimum | 54/54 (100%) |
| Mean QPU access time | 0.034 seconds |
| QPU time / Wall-clock ratio | ~0.7% |
| Classical overhead | ~99.3% |

### Implications
1. **Quantum contribution is minimal**: Despite using a "quantum" solver, actual QPU time is <1%
2. **Classical components do the real work**: Problem decomposition, post-processing, and communication dominate
3. **Solution quality is excellent**: Hybrid matches Gurobi on all provable instances
4. **Investment claim caution**: "Quantum portfolio optimization" may be 99% classical

## Audit Checklist for Future Hybrid Systems
- [ ] Measure QPU access time vs wall-clock time
- [ ] Compare solution quality against classical baseline
- [ ] Identify which constraints are handled by quantum vs classical
- [ ] Test scaling across problem sizes
- [ ] Check if QPU output requires classical post-processing for feasibility
- [ ] Calculate Quantum Contribution Index (QCI)

## Related Papers
- arXiv:2605.17628 - Penalty-Free Pipeline (complementary: shows penalty-encoded QUBO fails on D-Wave)
- arXiv:2605.06858 - Constrained Counterdiabatic QAOA for Portfolio
- arXiv:2604.19426 - Noise-Induced Landscape Distortion in QAOA
