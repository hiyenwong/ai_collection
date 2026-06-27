## 2026-06-27 - Economics, Investment + Quantum Mechanics (Cron Job)

### Benchmarking Quantum Algorithmic Resilience for CVaR Portfolio Optimization
- [[qaoa-cvar-portfolio-benchmark]] - Hardware benchmark comparing HE-VQNN vs WS-QAOA for CVaR portfolio optimization on NISQ devices (arXiv: 2606.07727)
  - 核心要点 1: WS-QAOA suffers catastrophic decoherence from SWAP tax on heavy hex topology
  - 核心要点 2: Classical-quantum hybrid proxy matrix bypasses CVaR auxiliary qubit bottleneck
  - **Activation**: qaoa, cvar, portfolio optimization, quantum benchmark, expressibility-coherence trade-off, SWAP tax

### A Penalty-Free Pipeline for Direct Quantum-Annealer Portfolio Optimization
- [[penalty-free-quantum-annealing-pipeline]] - Removes cardinality penalty from QUBO, enforces constraint classically via feasibility projector (arXiv: 2605.17628)
  - 核心要点 1: Penalty encoding causes 83-92% chain breaks on D-Wave Pegasus/Zephyr
  - 核心要点 2: Penalty-free pipeline reduces chain breaks to ≤ 0.04%, regret ≤ 0.03%
  - **Activation**: penalty-free QUBO, quantum annealing, chain-break reduction, D-Wave, cardinality constraint

### Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization
- [[hybrid-quantum-classical-audit]] - Four-metric audit protocol reveals QPU access is only 0.68% of wall-clock budget (arXiv: 2605.17623)
  - 核心要点 1: QPU time fraction is ~0.7%, 99% is classical decomposition and reassembly
  - 核心要点 2: QPU portfolios Sharpe 1.94 vs 1/N baseline 2.22; hybrid wins are constraint-native classical
  - **Activation**: hybrid quantum-classical audit, D-Wave hybrid, operational decomposition, quantum advantage verification

### Rethinking Expressibility-Trainability Trade-off in Hybrid Quantum Neural Networks
- [[hqnn-expressibility-trainability-nas]] - Multi-objective NAS for HQNN showing end-to-end training eliminates expressibility-trainability trade-off (arXiv: 2605.25768)
  - 核心要点 1: Classical components reshape optimization landscape, decoupling trainability from PQC expressibility
  - 核心要点 2: Multi-objective NAS finds Pareto-optimal solutions across classical-quantum design space
  - **Activation**: hybrid quantum neural network, expressibility-trainability, neural architecture search, barren plateaus

### Entanglement in the Quantum Volunteer's Dilemma
- [[quantum-game-theory-economics]] - Quantum entanglement reduces free-rider problems in economic games (arXiv: 2606.08227)
  - Core point 1: Entanglement creates decision correlations without communication
  - Core point 2: Improves collective utility beyond Nash equilibrium
  - **Activation**: quantum game theory, volunteer's dilemma, entanglement, collective action

### Mitigating Bias in Low-SNR Financial Reinforcement Learning via Quantum Representations
- [[fpqc-sac-low-snr-financial-rl]] - Quantum feature representations stabilize SAC in financial markets (arXiv: 2606.10448)
  - Core point 1: PQC front-end reduces Q-value overestimation and policy collapse
  - Core point 2: Quantum interference provides better regime separation
  - **Activation**: FPQC-SAC, low-SNR RL, financial RL, PQC, market stability

### Markets Are Not Random, They Are Hard to Predict
- [[markets-hard-to-predict-framework]] - Distinguishes epistemic vs aleatoric uncertainty in markets (arXiv: 2606.08209)
  - Core point 1: Markets have reducible epistemic and irreducible aleatoric uncertainty
  - Core point 2: Portfolio construction should address each type differently
  - **Activation**: market predictability, epistemic uncertainty, aleatoric uncertainty, portfolio theory

## 2026-06-27 - Quantum Optimization + Cryptanalysis (Cron Job)

### Discovery of Connectivity-Trainability Trade-off of IQP Circuits
- [[iqp-circuit-trainability]] - IQP circuits show fundamental connectivity vs trainability trade-off for Hamiltonian optimization (arXiv: 2606.24264)
  - Core point 1: Higher connectivity improves expressibility but triggers barren plateaus
  - Core point 2: Circuit structure profoundly affects both optimization performance and gradient variance simultaneously
  - **Activation**: iqp circuits, connectivity-trainability, quantum optimization, barren plateau, NISQ ansatz, Hamiltonian optimization

### LWE Meets Coherent Ising Machine: Penalty-Free QUBO Reduction
- [[cim-lwe-qubo-cryptanalysis]] - Penalty-free algebraic reduction of LWE to QUBO for CIM-based cryptanalysis (arXiv: 2606.22843)
  - Core point 1: Algebraic elimination of secret + nearest-plane decomposition eliminates penalty terms
  - Core point 2: Hybrid quantum-classical attack on post-quantum cryptography security parameters
  - **Activation**: LWE cryptanalysis, CIM, coherent ising machine, QUBO reduction, penalty-free, post-quantum security, BDD
