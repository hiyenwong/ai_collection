## 2026-05-14 - Systems Engineering + Quantum Mechanics (Cron Job)

### Syndrome Adaptive Gain Control for Min-Sum Decoding of Quantum LDPC Codes
- [[syndrome-adaptive-gain-qldpc]] - Dynamically adjusts MS scaling factor based on syndrome patterns, eliminating per-code optimization (arXiv: 2605.10433)
  - Adaptive gain based on fraction of unsatisfied stabilizers during iterative decoding
  - Matches/exceeds offline-optimized SMS FER, approaches BP performance with O(E) complexity
  - Degree-robust: avoids fixed scaling penalty across varying CN degrees
  - **Activation**: quantum LDPC decoding, min-sum scaling, syndrome adaptive gain, SAGMS, QEC decoder optimization, iterative decoding, 量子LDPC解码

### Affiliated Operators for Classical and Quantum Control
- [[von-neumann-quantum-control]] - Extends Lie algebra rank condition to infinite-dimensional bilinear quantum systems via von Neumann algebra affiliation (arXiv: 2605.13774)
  - Drift and control operators affiliated with von Neumann algebra M ⇒ standard LARC applies
  - Spectral projections replace boundedness requirement for unbounded operators
  - Enables controllability analysis for CV systems, quantum field control, bosonic codes
  - **Activation**: von Neumann algebra quantum control, infinite-dimensional controllability, bilinear quantum systems, affiliated operators, 无限维量子控制

### Lower Overhead Fault-Tolerant Building Blocks for Noisy Quantum Computers
- [[quantum-fault-tolerance-building-blocks]] - Reduces spacetime cost of fault tolerance via flag FT, 100% yield state prep, distance-4 planar code (arXiv: 2605.12385v1)
  - Combinatorial proof exponentially reduces flag qubits for stabilizer measurement of any size
  - Distance-4 planar code encodes 6 logical qubits using 1/10 the physical qubits of d=5 surface code
  - Classical-code-protected measurement cuts computation time by 2-6x
  - **Activation**: flag fault tolerance, stabilizer measurement optimization, Steane code, Golay code, surface code optimization, qubit overhead reduction

### Pre-Asymptotic Trainability in Photonic Variational Circuits under Postselection
- [[photonic-variational-trainability]] - Analyzes barren plateau dynamics in photonic variational circuits: allow-bunching and collision-free regimes remain trainable, dual-rail causes exponential concentration (arXiv: 2605.11879v1)
  - Photonic circuits constrained to Lie algebra O(m²), not full exponential Hilbert space
  - Postselection geometry, not dimension, determines gradient concentration
  - Dual-rail postselection induces barren plateaus beyond moderate system sizes
  - **Activation**: photonic barren plateau, variational photonic circuits, postselection gradient concentration, dual-rail postselection, linear optical quantum computing

### Scalable Measurement-Based Quantum Simulation Patterns for Benchmarking
- [[quantum-measurement-patterns]] - QPatLib workflow for generating Pauli-string unitary measurement patterns with commuting subset conventions for MBQC benchmarking (arXiv: 2605.12502v1)
  - Standardized testbed for pattern-optimization protocols in measurement-based quantum simulation
  - Multiple commuting conventions (sequential, grouped, parallel) for trade-off analysis
  - **Activation**: measurement-based quantum computing, QPatLib, Pauli-string patterns, MBQC, quantum simulation patterns

## 2026-05-13 - Medicine + Quantum Mechanics (Cron Job)

### Quantum Circuit Simulation of Compartmental Drug Dynamics
- [[quantum-pkpd-simulation]] - Quantum circuit simulation of PK/PD compartmental drug dynamics using PennyLane variational algorithms (arXiv: 2605.09691v1)
  - 4-compartment model (central, peripheral, effect-site, response) encoded in 12 qubits
  - Quantum-enhanced SAEM achieves improved log-likelihood vs classical ODE fitting
  - **Activation**: quantum PK/PD, pharmacokinetic simulation, drug dynamics quantum, quantum circuit SAEM, pennylane pharmacokinetics

### Adaptive Hybrid Quantum-Classical Feature Fusion for Medical Imaging
- [[quantum-medical-feature-fusion]] - Temperature-scaled hybrid quantum-classical feature fusion for breast cancer classification (arXiv: 2604.22903v1)
  - Three fusion strategies: SHF (static), DHF (dynamic), TSHF (temperature-scaled)
  - TSHF achieves 87.82% accuracy, 91.77% F1, 89.08% AUC-ROC on BreastMNIST
  - **Activation**: quantum feature fusion, hybrid quantum medical imaging, temperature-scaled fusion, quantum breast cancer, quantum medical classification

## 2026-05-13 - Medicine + Quantum Mechanics (Cron Job)

### Quantum Kernel Advantage over Classical Collapse in Medical Foundation Model Embeddings
- [[quantum-kernel-medical-embeddings]] - Quantum support vector machines with frozen medical foundation model embeddings achieve advantage on chest radiograph classification (arXiv: 2604.24597)
  - QSVM with MedSigLIP/RAD-DINO embeddings outperforms classical kernel collapse
  - ZZFeatureMap preserves discriminative structure in Hilbert space
  - **Activation**: quantum kernel medical, QSVM medical imaging, quantum advantage healthcare, 量子核医疗分类

## 2026-05-13 - Computer Science + Quantum Mechanics (Cron Job)

### Qlustering for Data Clustering via Network-Based Quantum Transport
- [[qlustering-quantum-clustering]] - Unsupervised clustering via steady-state quantum transport where quantum walker occupation probabilities encode cluster membership (arXiv: 2605.10844)
  - Maps clustering to stationary distributions of open quantum systems
  - Lindblad dissipation at sink nodes reveals cluster structure
  - **Activation**: quantum clustering, quantum transport clustering, Qlustering, 量子聚类, steady-state quantum computation

### Algorithmic Advantage on a Gate-Based Photonic Quantum Neural Network
- [[photonic-qnn-algorithmic-advantage]] - Evaluates QNN expressivity via effective dimension, a capacity measure with proven generalization-error bounds (arXiv: 2605.10801)
  - Effective dimension quantifies model capacity beyond parameter count
  - Photonic QNNs show higher expressivity than classical ANNs
  - **Activation**: photonic QNN, effective dimension, quantum neural network expressivity, 光子量子神经网络

### MAGIQ: A Post-Quantum Multi-Agentic AI Governance System with Provable Security
- [[magiq-post-quantum-agent-governance]] - Post-quantum multi-agent governance system with provable security for agentic AI (arXiv: 2605.06933)
  - Addresses secure communication and accountability in multi-agent systems
  - Integrates post-quantum cryptography with agentic AI governance
  - **Activation**: post-quantum AI governance, multi-agent security, MAGIQ

### Learning to Concatenate Quantum Codes
- [[quantum-code-concatenation-learning]] - ML-guided selection of optimal quantum error correction code sequences under concatenation (arXiv: 2604.14931)
  - Automates code sequence selection by estimating effective noise channels
  - Drives logical error rates down double-exponentially across levels
  - **Activation**: quantum code concatenation, QEC learning, quantum error correction

### Breaking QAOA's Fixed Target Hamiltonian Barrier
- [[quantum-boltzmann-machine-bilevel]] - Fully connected Quantum Boltzmann Machine via bilevel optimization extending QAOA architecture (arXiv: 2605.07473)
  - Inner-loop: positive phase energy minimization
  - Outer-loop: quantum circuit as negative phase sampler for log-likelihood maximization
  - **Activation**: quantum boltzmann machine, QAOA extension, bilevel quantum optimization

## 2026-05-13 - Computer Science + Quantum Mechanics (Cron Job)

### Equivariant Reinforcement Learning for Clifford Quantum Circuit Synthesis
- [[equivariant-rl-quantum-circuit-synthesis]] - RL framework leveraging Clifford group symmetries for efficient quantum circuit synthesis (arXiv: 2605.10910)
  - Equivariant policy network respects quantum operation symmetries
  - Stabilizer tableau representation enables efficient Clifford simulation
  - Symmetry reduction collapses equivalent states to canonical representatives
  - **Activation**: equivariant RL, quantum circuit synthesis, clifford group, symmetry-aware reinforcement learning, steerable neural networks, 量子电路合成, 等变强化学习
