# 2026-05-23 Economics/Quantum Finance Session Notes

## Session Summary
- Saturday economics/investment + quantum mechanics rotation
- Browser search on arxiv.org: 6 papers discovered, 5 imported to KG
- 2 skills created: constrained-counterdiabatic-qaoa-portfolio, quantum-reservoir-computing-finance
- KG: 1473 entities, 1501 vectors, 310416 relationships

## Key Paper Details

### CCD-QAOA (arXiv:2605.06858) - Falla & Safro
- Constrained Counterdiabatic QAOA for portfolio optimization
- XY mixer preserves Hamming weight → natural budget constraint enforcement
- Counterdiabatic terms from nested commutators [H_prob, [H_prob, ...[H_prob, H_XY]...]]
- Benchmarks: beats standard XY-mixer, Grover-mixer, penalty-based QAOA at fixed depth

### QRC for Volatility (arXiv:2505.13933) - Li et al.
- Published: Physical Review Research 8, 023028 (2026)
- Fully connected transverse-field Ising Hamiltonian as reservoir
- Input qubits + memory qubits separation
- Wrapper-based forward selection + Shapley values for interpretability
- Evaluated against ARIMA, GARCH, standard ML with Model Confidence Set procedures

### Other Papers
- arXiv:2602.09047: Carbon credit portfolio QAOA+ZNE on IBM Torino/Fez (88 variables)
- arXiv:2604.19426: Landscape Span Compression for QAOA noise characterization on IBM Heron r2
- arXiv:2602.21562: Ternary portfolio QAOA (non-binary)
- arXiv:2602.14827: Direct indexing QAOA with Dicke state init + XY-mixer
- arXiv:2510.05475: Quantum logic for human-centric AI in finance
- arXiv:2508.21548: Quantum Leap in Finance review + PQC

## KG Graph Analysis Results
- PageRank #3 overall: Quantum Feature Amplification Network (0.0376)
- 6 communities detected; Community 2 (19 nodes) = quantum reservoir + time series cluster
- QRC volatility paper similarity top matches: uncertainty quantification (0.478), quantum logic finance (0.419), quantum RL portfolio (0.409)
