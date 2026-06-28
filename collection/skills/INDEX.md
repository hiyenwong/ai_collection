## 2026-06-28 - Information Science + Quantum Mechanics (Cron Job)

### CIM-BDD: When LWE Meets Coherent Ising Machine — Penalty-Free Algorithm-Hardware Co-Design
- [[cim-bdd-penalty-free-lwe-cryptanalysis]] - Hybrid BDD solver reduces LWE to QUBO via penalty-free mapping, CR-BNP projection drives adaptive mixed-radix encoding (arXiv: 2606.22843)
  - 核心要点 1: Algebraic elimination absorbs modular arithmetic — squared error norm used directly as QUBO energy (no penalty)
  - 核心要点 2: CR-BNP encoding reduces qubit count and coefficient range enabling single batched submission on CPQC-550
  - **Activation**: cim-bdd, penalty-free qubo, lwe cryptanalysis, coherent ising machine, bounded distance decoding

### Tensor Network Characterization and Mitigation of Readout Errors
- [[tensor-network-readout-error-mitigation]] - MPO-based framework for correlated readout error characterization with near-linear sample cost scaling up to 20 qubits (arXiv: 2606.25974)
  - 核心要点 1: MPO model captures spatial correlations missed by tensor-product approximations
  - 核心要点 2: Integrates with tensor-network QEC decoders for joint inference over data and readout errors
  - **Activation**: tensor network readout, mpo readout error, correlated readout error, matrix product operator calibration

### Toric Code Made Subsystem: Topological Subsystem Codes from Anticommuting Quantum Spin Liquids
- [[topological-subsystem-code-construction]] - Framework for topological subsystem codes with extensive local gauge qubits undisturbed by check operators (arXiv: 2606.26226)
  - 核心要点 1: Extensive anticommuting local conserved operators form subsystem degrees of freedom
  - 核心要点 2: Weight-3/4 local check measurements on kagome/square lattices suitable for near-term hardware
  - **Activation**: topological subsystem code, anticommuting quantum spin liquid, subsystem qec, gauge qubits

### Quantum Computer Architecture with Ions in Tweezer Arrays
- [[ion-tweezer-quantum-architecture]] - Scalable trapped-ion architecture combining long coherence with tweezer reconfigurability via dipole-mediated entangling gates (arXiv: 2606.27249)
  - 核心要点 1: Effective electric dipoles enable temperature-robust entangling gates with no residual qubit-motion entanglement
  - 核心要点 2: Crosstalk suppression enables parallel gate execution for transversal QEC gates
  - **Activation**: ion tweezer quantum computer, trapped ion tweezer architecture, dipole-mediated entangling gate

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
