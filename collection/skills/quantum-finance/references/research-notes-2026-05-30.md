# 2026-05-30 Economics + Quantum Research Notes

## Session Overview
- Weekly theme: Economics/Investment (Saturday)
- arXiv API rate-limited; fell back to kg.db existing papers
- 14 quantum finance papers surveyed from kg.db

## Key Papers Surveyed

### D-Wave Pipeline Audit Papers
- **2605.17628** Penalty-Free Pipeline: cardinality penalty → dense all-ones matrix → chain-break 83-92%
- **2605.17623** D-Wave Audit: QPU = 0.034s / 5s (0.7%), LeapHybridCQM matches Gurobi on 54/54 instances

### Novel Methodologies
- **2602.06367** Entangled Neural Traders: quantum entanglement eliminates pathological Nash equilibrium in speculative markets
- **2602.13094** QRC Stock Forecasting: ≤6 qubits, >86% accuracy, platform-agnostic (superconducting + trapped ion)
- **2602.14827** Cardinality-Constrained Portfolio: hybrid quantum-classical for Direct Indexing + ESG mandates
- **2603.09966** Projective Geometry QM+Finance: numeraire invariance maps to curved state space, measurable cubic term

### Established Benchmarks
- **2509.17876** Extensive Benchmark: 250 instances, up to 1000 assets — classical MIP solves in seconds, problem-tailored heuristic beats quantum
- **2510.11153** Hot-Starting: restrict search near continuous optimum, compact Hilbert space, outperforms on D-Wave Advantage
- **2507.20532** Expert Analysis Evaluation: VQE/QAOA portfolios often violate financial criteria despite good cost minimization
- **2601.18811** QRL Dynamic Portfolio: quantum DDPG/DQN with fewer params than classical baselines

## Knowledge Graph State
- kg.db: 36 entities, pagerank computed
- Louvain Community 6 (16 entities): Financial quantum portfolio clustering
- PageRank top: quant-ph (0.003), Quantum Hierarchical RL (0.002)

## Skills Created This Session
1. `quantum-annealer-pipeline-audit` - QA failure diagnosis + hybrid service audit
2. `quantum-market-entanglement` - Entangled trader valuation methodology
3. `quantum-reservoir-finance` - QRC for financial time-series forecasting
