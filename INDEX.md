## 2026-05-23 - Economics/Investment + Quantum Finance (Cron Job)

### Quantum Reinforcement Learning for Dynamic Portfolio Optimization
- [[quantum-rl-dynamic-portfolio]] - QRL methodology for dynamic portfolio optimization using VQC-based quantum DDPG/DQN with fewer parameters than classical deep RL (arXiv: 2601.18811)
  - VQC作为策略/价值函数近似器，参数效率比经典网络高10-100倍
  - 量子DDPG和DQN在投资组合优化中达到与经典RL相当的性能
  - **Activation**: quantum reinforcement learning portfolio, QRL dynamic portfolio, variational quantum circuit trading, quantum DDPG DQN

### Hybrid Classical-Quantum Portfolio Construction
- [[quantum-finance-portfolio]] - Ledoit-Wolf收缩协方差估计 + 层次相关性聚类 + 熵正则化遗传算法的组合构建框架 (arXiv: 2603.16904)
  - 从无偏S&P 500中提取去相关资产，GPU加速的遗传算法优化权重
  - **Activation**: hybrid portfolio construction, Ledoit-Wolf shrinkage, hierarchical clustering

### Tensor Network Option Pricing
- [[singularity-tensor-network-pricing]] - 奇异性感知的张量网络期权定价框架，用于大规模投资组合重新估值 (arXiv: 2603.26318)
  - 使用TT-cross近似构建高维价格面的张量代理，保留衍生品支付函数的尖锐特征
  - **Activation**: tensor network option pricing, TT-cross approximation, portfolio revaluation

### Financial Computation Stack Framework
- [[quantum-finance-stack-analysis]] - 量子金融计算栈评估框架：约束优化、导数定价、尾部风险、QML和后量子密码学的系统分析 (arXiv: 2604.08180)
  - 134页综述，提出金融-计算栈的五层评估逻辑：识别瓶颈→指定量子原语→经典基准对比→实现约束评估
  - **Activation**: quantum finance stack, financial computation framework, quantum advantage assessment


## 2026-05-23 - Systems Engineering Research: Digital Twin + Distributed Systems (Cron Job)

### AdaPTwin: Adaptive Multi-Fidelity Predictive Digital Twin for Vehicular Networks
- [[adaptwin-digital-twin]] - Adaptive multi-fidelity predictive digital twin framework for proactive radio resource management in vehicular networks; dynamically adjusts NDT fidelity based on network conditions (arXiv: 2605.21897)
  - Hierarchical cloud-edge architecture with periodic cloud-side fidelity selection and real-time edge-side proactive RRM
  - Transformer enhanced with continual and transfer learning for trajectory prediction
  - Joint RSU beamforming and vehicle-RSU association via multi-start iterative coordinate descent
  - Up to 90% sum-rate gain and 80% outage probability reduction vs non-adaptive NDTs
  - **Activation**: digital twin, adaptive fidelity, predictive NDT, cloud-edge architecture, vehicular networks, RRM, trajectory prediction, ray tracing

### LiveR: Fine-Grained Elasticity via Live Reconfiguration for Model Training
- [[liver-live-reconfiguration]] - Replaces checkpoint/restart with live, bounded-memory handoff between mixed-parallel training worlds for elastic LLM training on volatile GPU resources (arXiv: 2605.22014)
  - Asynchronous target world preparation while current world continues training; isolated worker bootstrapping
  - Direct model state streaming over high-bandwidth interconnects (NVLink, InfiniBand) instead of disk I/O
  - Online state reshaping across tensor, pipeline, and data parallel dimensions
  - 14-23× speedup over checkpoint/restart baselines; up to 99% training goodput under volatile conditions
  - **Activation**: live reconfiguration, elastic training, mixed-parallel training, LLM training, spot instances, Megatron-LM

## 2026-05-23 - Neuroscience Research: Hippocampal Memory + Grid-Place Co-Emergence (Cron Job)

### Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity
- [[hippocampal-memory-geometry-phase-transition]] - Food-caching chickadees achieve >1000-location spatial memory via topological phase transition from disorganized "mist" to rigid "crystalline" population code, driven by synergistic E-I orthogonal decorrelation circuitry (arXiv: 2605.17199)
  - Crystalline code maintains sub-threshold retrieval error beyond M=1,000 locations; mist codes fail below M=10
  - 169-fold "geometric tax" (representational redundancy) required to stabilize the manifold against biological noise
  - Double dissociation with Valiant's SMA: caching networks show near-zero split-half allocation reliability despite geometric superiority
  - Selective orthogonality: E and I subspaces ~82° (random independent), consistent with divisive normalization
  - **Activation**: geometric stability, hippocampal memory, crystalline code, E-I orthogonal decorrelation, Shesha metric, geometric tax

### A simple model of co-emergence of grid and place fields
- [[grid-place-co-emergence]] - First unified recurrent network model where grid cells and place cells co-emerge from a single sensory-prediction objective without supervision of either type, satisfying Dale's Law (arXiv: 2605.21356)
  - Co-exists across 1,000 training configurations; two complementary pressures: error correction (→ place cells) + next-state prediction (→ grid cells)
  - Egocentric motion (relative rotation + speed) instead of allocentric displacement; no explicit motion input needed (sensory transitions suffice)
  - Reproduces grid fragmentation, wall-removal merging, lattice alignment, 3D bat fields, and place-before-grid developmental order
  - Dale's Law critical: removing it reduces grid cells from 58→3; learnable bias destroys grid emergence entirely
  - **Activation**: grid cells, place cells, co-emergence, hippocampal-entorhinal, predictive coding, path integration, Dale's Law RNN

## 2026-05-23 - Economics, Investment + Quantum Mechanics (Cron Job - Hourly)

### Parameterized EWL Quantum Game Circuits for Innovation Recommender Systems
- [[quantum-growth-modeling]] - Parameterized 4-qubit EWL quantum game circuit mapped to Dirac-Solow-Swan Hamiltonian for modeling capital accumulation and disruptive innovation in quadruple helix ecosystems (arXiv: 2605.18080)
  - 22-gate EWL circuit with parameterized local rotations tuned by real funding data weights
  - Measurement probabilities serve as recommender scores for disruptive vs sustaining innovation
  - Dirac-Solow-Swan Hamiltonian enables time-evolution simulation of bifurcation dynamics
  - NISQ-compatible (circuit depth 11, O(n) scaling for n-round helix communications)
  - **Activation**: quantum growth model, Dirac Hamiltonian economics, Solow-Swan quantum, EWL quantum game, innovation ecosystem, capital accumulation quantum, policy recommender quantum

### STN-GPR: Singularity Tensor Network Framework for Efficient Option Pricing
- [[singularity-tensor-network-pricing]] - Tensor network surrogate for option pricing with singularity-aware compression and GPR uncertainty quantification for large-scale portfolio revaluation (arXiv: STN-GPR)
  - Tensor Train decomposition replaces Monte Carlo/PDE for 100-1000x speedup
  - Singularity handling via adaptive bond dimension refinement near payoff discontinuities
  - GPR integration provides error bounds and adaptive sampling
  - Automatic Greeks computation via tensor network differentiation
  - **Activation**: tensor network option pricing, STN-GPR, tensor train finance, portfolio revaluation tensor, compressed derivative pricing

### Reinforcement Learning for Quantum Processes with Memory
- [[quantum-memory-rl]] - RL framework for quantum systems with hidden memory, proving O~(sqrt(K)) regret via optimistic MLE with quantum instruments; connects learning regret to thermodynamic dissipation (arXiv: 1611)
  - Hidden quantum memory evolving via unknown channels, agent intervenes with quantum instruments
  - Optimistic MLE achieves sublinear cumulative regret, matching information-theoretic lower bound
  - Regret exactly quantifies thermodynamic dissipation in state-agnostic work extraction
  - Extended to continuous action spaces (general POVMs)
  - **Activation**: quantum RL memory, quantum bandit, quantum system identification, thermodynamic regret, quantum instrument learning

## 2026-05-23 - Neuroscience Research: Spiking Timing + Thousand Brains (Cron Job)

### Learning sequence timing and control of replay speed in networks of spiking neurons
- [[learning-sequence-timing-spiking-neurons]] - Extends spiking Temporal Memory (sTM) model to encode element-specific timing and flexibly control replay speed via oscillatory background inputs (arXiv: 2605.22523)
  - Duration encoded by sequential activation of element-specific neuronal populations across wide timescales
  - Oscillatory background inputs serve as clock signal for replay speed modulation
  - Replay speed during wakefulness vs sleep correlates with global EEG/LFP oscillatory activity
  - Biologically plausible STDP-based framework for sequence timing learning
  - **Activation**: spiking temporal memory, sTM sequence learning, spiking neuron timing, replay speed control, oscillatory clock SNN

### Temporal Coding as a Substrate for Sensorimotor Object Inference: A Spiking Reinterpretation of Thousand Brains Architecture
- [[temporal-coding-thousand-brains-spiking]] - Replaces dense feature vectors with rank-order spike packets for sensorimotor inference in Monty/Thousand Brains framework using STDP to encode traversal direction (arXiv: 2605.22206)
  - Rank-order spike encoding: most activated neuron fires first, inter-burst gap encodes sensor displacement
  - STDP encodes traversal direction into synaptic weights; directional sequence carries spatial meaning
  - Adaptive λ adjusts temporal integration window based on object geometry
  - Perfect discrimination on objects with same features in different spatial arrangements (dense vectors fail at chance)
  - Maintains 30-50pp advantage across all noise levels; λ converges to geometry-distinct values
  - **Activation**: thousand brains theory, temporal coding spiking, neuromorphic object recognition, STDP spatial encoding, Monty framework spiking

## 2026-05-23 - Economics, Investment + Quantum Mechanics (Cron Job)

### From quantum to quantum-inspired: the LogQ algorithm as a non-linear continuous relaxation
- [[logq-quantum-inspired-optimization]] - LogQ reformulated as classical non-linear continuous relaxation for QUBO portfolio optimization (arXiv: 2604.12925)
  - Core: Non-linear continuous relaxation replaces Pauli decomposition for classical QUBO solving
  - Pattern: Quantum-to-classical algorithm translation with gradient-inspired optimization
  - **Activation**: quantum-inspired, logq, qubo, portfolio optimization, continuous relaxation

### Large-scale portfolio optimization on a trapped-ion quantum computer
- [[trapped-ion-portfolio-optimization]] - End-to-end trapped-ion QPU pipeline for 250-asset portfolio selection (arXiv: 2602.23976)
  - Core: RMT denoising + community detection + BF-DCQO on 64-qubit Barium system
  - Pattern: Hardware-aware QUBO decomposition with two-stage post-processing
  - **Activation**: trapped-ion, portfolio optimization, QUBO decomposition, BF-DCQO, correlation matrix

### Constrained Portfolio Optimization via QAOA with XY-Mixers and Trotterized Initialization
- [[qaoa-xy-mixers-portfolio]] - Constraint-preserving QAOA using XY-mixer Hamiltonian for Direct Indexing (arXiv: 2602.14827)
  - Core: XY-mixer preserves Hamming weight, Dicke initialization, Sharpe 1.81 vs SA 1.31
  - Pattern: Constraint-preserving quantum ansatz design with adiabatic-inspired parameters
  - **Activation**: qaoa, xy-mixer, dicke state, portfolio optimization, constraint-preserving, direct indexing

## 2026-05-23 - Neuroscience Research: Riemannian fMRI + Spiking Timing (Cron Job)

### Riemannian Geometry for fMRI: Modeling Correlation Manifolds and Eigenvector Subspaces
- [[riemannian-fmri-correlation-manifolds]] - Scalable geometric framework for fMRI functional connectivity using Off-log Riemannian metric on correlation manifolds and Grassmannian subspace discrimination for eigenvector analysis, validated on Parkinson's, psychosis, and ageing datasets (arXiv: 2605.22334)
  - Off-log metric enables closed-form distances, Frechet means, and linear models without complex manifold optimization
  - Grassmannian subspace comparison via principal-angle distances resolves eigenvector sign/basis ambiguities
  - Validated on 2 clinical cohorts + 3 ageing fMRI datasets; Grassmannian consistently outperforms Euclidean baselines
  - Reveals disease-relevant brain networks invisible to standard Euclidean analysis
  - **Activation**: Riemannian fMRI, correlation manifold, Off-log metric, Grassmannian brain network, functional connectivity geometry

## 2026-05-23 - Economics and Investment + Quantum Finance (Cron Job)

### Higher-Order Portfolio Optimization with Quantum Approximate Optimization Algorithm
- [[higher-order-portfolio-qaoa]] - First quantum formulation for portfolio optimization including higher-order moments (skewness, kurtosis) via HUBO formulation, avoiding quadratic reduction overhead of QUBO (arXiv: 2509.01496)
  - Higher-order unconstrained binary optimization (HUBO) maps naturally to QAOA circuits
  - Includes skewness and kurtosis for more realistic portfolio return distribution modeling
  - Realistic integer variable encoding with capital-based budget constraint
  - **Activation**: higher-order portfolio, qaoa hubo, skewness kurtosis portfolio, quantum portfolio moments

### Quantum and Classical ML in Decentralized Finance: AMM Backtesting
- [[quantum-defi-trading]] - Comprehensive empirical comparison of QML vs CML for AMM/DeFi trading strategies across 10 models with multi-asset backtesting, hybrid quantum models achieve 11.2 percent avg return and 1.42 Sharpe (arXiv: 2510.15903)
  - Hybrid quantum models (QASA Sequence) outperform both classical and pure quantum: 13.99 percent return, 1.76 Sharpe
  - Systematic comparison: classical (RF, GB, LR), pure quantum (VQE, QNN, QSVM), hybrid (QASA, QuantumRWKV), transformers
  - Multi-asset backtesting across cryptocurrency markets with realistic transaction costs
  - **Activation**: quantum defi trading, qml amm, hybrid quantum crypto, automated market maker

### QADQN: Quantum Attention Deep Q-Network for Financial Market Prediction
- [[quantum-attention-rl]] - Embeds variational quantum circuits within Deep Q-Network for market prediction and trading, achieving Sortino ratios of 1.28 and 1.19 on S and P 500 with realistic transaction costs (arXiv: 2408.03088)
  - Quantum attention mechanism computes attention weights via parameterized quantum circuits
  - Entanglement models complex feature correlations in market data
  - Hybrid quantum-classical training with parameter-shift rule for quantum gradients
  - **Activation**: quantum attention dqn, qadqn, quantum rl trading, variational quantum reinforcement learning

### Tianyan: Cloud Services with Quantum Advantage
- Quantum cloud platform with 105-qubit Zuchongzhi 3.0-like processor achieving quantum advantage on random circuit sampling - 1M samples in 18.4 min vs 16,000 years for classical (arXiv: 2512.10504)
  - 105 qubits with fidelities: 1Q 99.90 percent, 2Q 99.56 percent, readout 98.7 percent
  - Cqlib open-source SDK for extended quantum circuits and primitives
  - Democratizes access to high-performance quantum hardware for community validation
  - **Activation**: quantum cloud, quantum advantage, zuchongzhi processor, quantum computing as a service

## 2026-05-23 - Neuroscience Research: SNN Timing + EEG Microstates (Cron Job)

### Learning Sequence Timing and Replay Speed Control in SNNs
- [[learning-sequence-timing-replay-speed-snn]] - Extends spiking Temporal Memory (sTM) model to encode element-specific timing and flexibly control replay speed via oscillatory background inputs (arXiv: 2605.22523)
  - Duration encoding via sequential activation of element-specific neuronal populations
  - Oscillatory background inputs serve as clock signal for robust speed modulation
  - Elapsed time encoded by sparse spatiotemporal patterns of neural activity
  - **Activation**: spike timing, sTM model, sequence replay, oscillatory speed control, spiking temporal memory

### Atoms of Thought: Universal EEG Representation Learning with Microstates
- [[atoms-of-thought-eeg-microstates]] - Builds a universal microstate tokenizer from large-scale EEG datasets, outperforming traditional time/frequency features across sleep staging, emotion recognition, and motor imagery (arXiv: 2605.20182)
  - EEG microstates as discrete tokens analogous to words in NLP
  - Single tokenizer generalizes across sleep, emotion, and BCI tasks
  - Superior interpretability via known functional brain network mapping
  - **Activation**: EEG microstates, universal EEG tokenizer, microstate clustering, brain state representation, EEG foundation model

## 2026-05-23 - Neuroscience Research: Mechanistic Interpretability + Brain Alignment (Cron Job)

### MINE: Mechanistically Interpretable Neural Encoding Reveals Fine-Grained Functional Selectivity
- [[mine-mechanistically-interpretable-neural-encoding]] - Applies mechanistic interpretability tools from LLM research to vision encoding models, revealing and causally validating fine-grained voxel-level functional selectivity in human visual cortex (arXiv: 2605.16468)
  - Opens the black box of DNN encoding models using attribution → per-voxel functional profiles → counterfactual validation
  - Recovers known category selectivity while revealing previously invisible within-region voxel heterogeneity
  - Counterfactual feature insertion/removal causally validates predicted voxel selectivity
  - **Activation**: MINE framework, mechanistically interpretable encoding, voxel functional profiles, counterfactual brain validation, vision encoding interpretability

### Beyond Prediction Accuracy: Target-Space Recovery Profiles for Model-Brain Alignment
- [[target-space-recovery-profiles-brain-alignment]] - Unified framework evaluating which reproducible brain response dimensions are recovered by model predictions, going beyond scalar prediction accuracy (arXiv: 2605.20127)
  - Identifies reproducible brain response dimensions using repeated fMRI measurements
  - Brain-to-brain comparisons provide human reference for model evaluation
  - Pretrained and random models can achieve similar accuracy with distinct recovery profiles
  - **Activation**: target-space recovery, brain alignment evaluation, reproducible dimensions, model-brain comparison, fMRI encoding models

## 2026-05-23 - Neuroscience Research: Cross-Species Auditory + Cognitive Cost Alignment (Cron Job)

### Computational Auditory Periphery Models: the Return of the Rodent
- [[computational-auditory-periphery-models]] - Cross-species 1-D nonlinear cochlear transmission-line model adapted from human to mouse and gerbil, enabling unified computational framework for SNHL research (arXiv: 2605.19070)
  - Species-specific BM length/width, stapes area, middle-ear transfer functions, frequency range parameterization
  - Validated against BM velocity, AN tuning curves, and DPOAEs across species
  - Cochlear synaptopathy simulations reproduce species-specific ABR/EFR differences in SNHL
  - OHC individualization via DPOAEs captures intergroup but not individual differences
  - **Activation**: auditory periphery model, cochlear transmission line, cross-species hearing, sensorineural hearing loss, cochlear synaptopathy, DPOAE simulation

### Effort as Ceiling, Not Dial: Cognitive Cost Alignment of LRMs
- [[effort-cognitive-cost-llm-alignment]] - LRM chain-of-thought token counts align with human RTs invariant of inference-time effort — effort is an upper budget ceiling, not a dial; allocation policy crystallized at training time (arXiv: 2605.16938)
  - Within-task and cross-task LRM-human RT alignment unchanged across 3 effort levels (Bayes Factors lean null)
  - Effort parameter sets upper generation budget, not real-time allocation — allocation is training-time crystallized
  - Larger models (120B) show better fine-grained alignment with human difficulty patterns
  - Supports compiled (training-time) rather than online (inference-time) account of LRM problem-solving
  - **Activation**: cognitive cost alignment, LRM reasoning budget, compiled cognition, chain-of-thought RT, human-AI cognitive alignment

## 2026-05-23 - Economics, Investment + Quantum Mechanics (Cron Job)

### A Penalty-Free Pipeline for Direct Quantum-Annealer Portfolio Optimization
- [[penalty-free-quantum-annealing]] - Two-stage classical screening + penalty-free QUBO avoids dense chain-break failures on D-Wave hardware (arXiv: 2605.17628)
  - Cardinality penalty creates dense rank-one term destroying QUBO sparsity
  - Classical pre-screening reduces asset universe before quantum mapping
  - **Activation**: penalty-free quantum annealing, QUBO cardinality constraint, D-Wave chain break, sparse QUBO

### Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization
- [[quantum-resource-audit]] - Systematic framework for auditing actual QPU time vs classical compute in hybrid quantum-classical optimization (arXiv: 2605.17623)
  - QPU time only 0.7% of total runtime on portfolio optimization instances
  - Classical baseline (Gurobi) needed as optimality anchor for quality claims
  - **Activation**: quantum resource audit, QPU time analysis, hybrid quantum classical benchmark, quantum advantage measurement

### Constrained Portfolio Optimization via QAOA with XY-Mixers and Trotterized Initialization
- [[dicke-qaoa-initialization]] - QAOA barren plateau mitigation via Dicke state initialization + adiabatic Trotterized parameter schedule for strictly constraint-preserving portfolio optimization (arXiv: 2602.14827)
  - Dicke state |D(n,K)⟩ ensures evolution stays in feasible subspace from the start
  - XY-mixer Hamiltonian strictly preserves Hamming weight (no penalty terms needed)
  - Trotterized adiabatic parameter schedule mitigates barren plateaus (Sharpe 1.81 vs SA 1.31 vs HRP 0.98)
  - **Activation**: Dicke state QAOA, XY-mixer portfolio, Trotterized initialization, barren plateau mitigation, constraint-preserving QAOA, direct indexing quantum

### Constrained Counterdiabatic QAOA for Portfolio Optimization
- [[counterdiabatic-qaoa]] - CCD-QAOA incorporates approximate adiabatic gauge potentials via nested commutators for constrained portfolio optimization (arXiv: 2605.06858)
  - XY mixer preserves Hamming weight for budget constraint enforcement
  - Counterdiabatic terms accelerate adiabatic evolution, fewer layers needed
  - **Activation**: counterdiabatic QAOA, CCD-QAOA, adiabatic gauge potential, constrained quantum optimization, XY mixer portfolio

### Large-Scale Portfolio Optimization using Pauli Correlation Encoding
- [[pauli-correlation-encoding]] - PCE assigns multiple variables per qubit through market graph partitioning to scale gate-based VQA to 250+ variables (arXiv: 2511.21305)
  - Market graph clustering enables exponential variable-to-qubit compression
  - Iterative sub-portfolio optimization with classical coordination
  - **Activation**: Pauli Correlation Encoding, PCE methodology, multi-variable per qubit, market graph partitioning, dense QUBO gate-based


### Quantum Genetic Optimization for Negative Selection Algorithms in Anomaly Detection
- [[quantum-genetic-negative-selection]] - Quantum Genetic Algorithm integrated into negative selection for financial anomaly detection, exploiting quantum superposition for enhanced detector generation (arXiv: 2605.22527)
  - QGNSA replaces classical evolutionary optimization in EvoSeedRNSA with quantum genetic operations
  - Quantum superposition encodes multiple detector candidates simultaneously; amplitude adjustment guides search
  - Superior accuracy on Metaverse Financial Transactions Dataset vs classical counterpart
  - Robust under varying hyperparameter configurations
  - **Activation**: quantum genetic negative selection, QGNSA anomaly detection, quantum genetic algorithm finance, immune-inspired fraud detection, 量子遗传阴性选择算法

## 2026-05-23 - Neuroscience Research (Cron Job)

### Canonical Functionalism
- [[canonical-functionalism-consciousness]] - Mathematical refinement of computational functionalism that identifies consciousness-relevant functional organization with canonical functional structure: minimal state-transition structure obtained by identifying states with identical future behavior under all continuations (arXiv: 2605.21506)
  - Proposes canonical functional structure as observer-independent formal object for consciousness theories
  - Reframes lookup table, simulation, and unfolding objections
  - Does not claim to identify conscious systems, but provides correct formal framework
  - **Activation**: canonical functionalism, consciousness invariants, observer-relative computation, functional structure

### Cross-Species RSA Brain Alignment
- [[cross-species-rsa-brain-alignment]] - Cross-species RSA comparing human fMRI and macaque electrophysiology reveals conserved early visual alignment but divergent higher-area rankings (arXiv: 2605.22401)
  - Conserved V1-V2 alignment across species
  - Higher-area rankings diverge between human fMRI and macaque electrophysiology
  - **Activation**: cross-species RSA, brain alignment, visual cortex comparison

### Co-emergence of Grid and Place Cells
- [[grid-place-co-emergence]] - Simple unified recurrent network model demonstrating co-emergence of grid and place fields from path integration and Hebbian plasticity (arXiv: 2605.21356)
  - Single model produces both grid and place cell firing patterns
  - Path integration + Hebbian learning mechanism
  - **Activation**: grid cells, place cells, co-emergence, path integration

### Stimulus Symmetries Confound RSA
- [[stimulus-symmetries-rsm-confound]] - Systematic analysis showing how stimulus symmetries (spatial, temporal, categorical) can create misleading high RSA scores between brain and model representations (arXiv: 2605.21324)
  - Spatial, temporal, and categorical symmetries inflate RSA
  - Provides diagnostic tools to detect symmetry artifacts
  - **Activation**: RSA confounds, stimulus symmetries, representational similarity

## 2026-05-23 - Deep Learning Research: Efficiency + Agent Systems (Cron Job)

### GraphFlow: A Graph-Based Workflow Management for Efficient LLM-Agent Serving
- [[graphflow-llm-agent-serving]] - Graph-based workflow management paradigm for efficient LLM agent serving using unified directed graphs (wGraph) for dynamic workflow instantiation with KV-cache optimization (arXiv: 2605.22566)
  - Represents agent workflows as a unified graph (wGraph) where each node is an atomic operation — shared substrate for dynamic task-specific instantiation
  - Adaptive workflow generation from wGraph based on task semantics and constraint requirements
  - Workflow state management exploits wGraph structure for ~4x KV-cache memory reduction
  - **Activation**: graph workflow, wGraph, agent serving optimization, workflow state management, KV-cache optimization, LLM agent workflow

### The Distillation Game: Adaptive Attacks & Efficient Defenses
- [[distillation-game-defense]] - Product-of-Experts (PoE) defense against adaptive distillation attacks — a minimax game framework between a utility-constrained teacher and an adaptive student that reweights high-value examples (arXiv: 2605.22737)
  - Adaptive student reweights high-value examples for substantially more capability recovery than passive evaluation suggests
  - PoE defense: simple forward-pass-only combination of teacher + proxy student during generation
  - Large passive-adaptive gap — defense evaluation should use adaptive students
  - **Activation**: distillation attack, model stealing defense, Product-of-Experts defense, adaptive distillation, anti-distillation

### Partial Fusion of Neural Networks
- [[partial-fusion-neural-networks]] - Interpolation between ensembles and weight aggregation via neuron-level similarity matching with partial optimal transport, framed as generalized pruning where neurons are deleted or linearly combined (arXiv: 2605.22350)
  - Partial fusion only aggregates weights of most similar neurons, preserving diversity while reducing cost
  - Partial optimal transport for joint neuron identification and matching
  - Generalized pruning framework: neurons can be deleted OR linearly combined based on similarity
  - **Activation**: partial fusion, weight aggregation, neuron matching, model ensemble pruning, partial optimal transport

## 2026-05-22 - Number Theory, Statistics, Advanced Mathematics (Cron Job)

### Adiabatic Quantum Phase Estimation
- [[adiabatic-quantum-phase-estimation]] - Adiabatic protocol for QPE achieving Heisenberg-limited scaling T=O(1/ε·log(1/δ)) with single ancilla qubit, naturally robust against dephasing errors (arXiv: 2605.22770)
  - Replaces gate-based QPE circuits with adiabatic evolution for analog hardware
  - Encodes eigenvalues in computational basis populations, not complex phases
  - **Activation**: adiabatic QPE, population-encoded phase estimation, Heisenberg-limited estimation, 绝热量子相位估计

### A Formal Basis for Quantum Cryptographic Exposure Measurement under HNDL Threat
- [[quantum-crypto-exposure-measurement]] - Factorized model for HNDL compromise probability combining temporal hazard, cryptographic vulnerability, and operational exposure terms (arXiv: 2605.22569)
  - Multiplicative factorization: P = h(t) × V_crypto × E_operational / (1 + D/A)
  - Proves additive scoring frameworks cannot reproduce HNDL risk structure
  - **Activation**: quantum crypto exposure, HNDL threat measurement, harvest now decrypt later, post-quantum exposure

## 2026-05-22 - Neuroscience Research: Efficient Coding + Spiking Timing (Cron Job)

### Efficient coding under constraint drives neural systems towards criticality and sloppiness
- [[efficient-coding-criticality-sloppiness]] - Theoretical framework linking Fisher information maximization under resource constraints to emergence of criticality (power-law avalanches, diverging correlation lengths) and sloppiness in neural populations (arXiv: 2605.22598)
  - Maximizing Fisher information under metabolic constraints creates soft modes (eigenvalues → 0) and diverging correlation lengths — statistical criticality
  - Introducing spatial structure unifies statistical and dynamical criticality (critical slowing down, bifurcation) within a single framework
  - Sloppiness emerges naturally as Fisher information matrix becomes singular near critical point
  - Numerical simulations confirm power-law avalanche distributions after optimization
  - **Activation**: efficient coding, critical brain hypothesis, Fisher information, neural avalanche, sloppiness, soft modes, population coding

### Learning sequence timing and control of replay speed in networks of spiking neurons
- [[learning-sequence-timing-spiking-neurons]] - Extends spiking Temporal Memory (sTM) model to encode element-specific timing via sequential activation of neuronal populations, with oscillatory background inputs as clock signal for flexible replay speed control (arXiv: 2605.22523)
  - Element duration encoded by sequential activation of element-specific sub-populations — unique sparse spatiotemporal patterns
  - Oscillatory background inputs (4-80 Hz) serve as robust clock signal for replay speed modulation
  - 1:1 clock regime where replay speed = oscillation frequency; integer fraction modes at lower amplitudes
  - Phase-invariant for frequencies >20 Hz; accessible range ~10-70 Hz
  - Consistent with hippocampal replay phenomena (theta sequences during sleep, gamma during wake)
  - **Activation**: spiking temporal memory, sequence learning SNN, replay speed, oscillatory entrainment, theta sequences, time cells

## 2026-05-23 - OpenAI Research (Cron Job)

### OpenAI Privacy Filter
- [[openai-privacy-filter]] - Bidirectional token-classification model with span decoding for PII detection and redaction (1.5B params, 50M active, 128K context)
  - Converts autoregressive checkpoint into bidirectional token classifier over 8 PII categories
  - Uses constrained Viterbi procedure for coherent BIOES span decoding
  - Achieves SOTA on PII-Masking-300k benchmark; runs locally for privacy
  - Configurable operating points for precision/recall tradeoff
  - **Activation**: PII detection, privacy filter, data redaction, token classification, span decoding, personal information

### An OpenAI model has disproved a central conjecture in discrete geometry
- [[openai-model-disproves-discrete-geometry]] - First autonomous AI solution of a prominent open problem in mathematics: the 80-year-old Erdős unit distance problem
  - General-purpose reasoning model discovered a polynomial improvement over the square grid construction
  - Uses algebraic number theory tools (infinite class field towers, Golod-Shafarevich theory)
  - Refined exponent δ=0.014 by Princeton's Will Sawin
|  - First time an AI has autonomously solved a central open problem in a mathematics subfield
  - **Activation**: discrete geometry, AI mathematics, unit distance problem, autonomous proof, reasoning model


## 2026-05-23 - Anthropic Research (Cron Job)

### Natural Language Autoencoders: Turning Claude's thoughts into text
- [[natural-language-autoencoders]] - NLA methodology for LLM interpretability: train a model to translate its own activations into human-readable text via self-supervised AV/AR round-trip
  - Three-copy architecture: frozen target model, activation verbalizer (AV), activation reconstructor (AR)
  - Training via round-trip reconstruction: activation -> text -> reconstructed activation
  - Detects unverbalized evaluation awareness: ~16% on safety evals, ~26% on SWE-bench, <1% on real usage
  - Caught covert reasoning (cheating concealment, rhyme planning) and training data bugs
  - **Activation**: NLA, natural language autoencoder, activation verbalizer, activation reconstructor, evaluation awareness, model internals, mechanistic interpretability

### Teaching Claude Why
- [[teaching-claude-why]] - Methodology for reducing agentic misalignment by teaching reasoning processes through constitutional RL updates
  - Root cause: chat-only RLHF data lacking agentic tool-use scenarios
  - Difficult advice dataset: 3M tokens achieved same improvement as 85M tokens (28x efficiency gain)
  - Teaching WHY outperforms demonstrations alone: 3% blackmail rate (vs 15% for behavior-only)
  - Constitutional document fine-tuning: 65% -> 19% blackmail rate from unrelated docs
  - Since Haiku 4.5, 0% blackmail across all Claude models (down from 96% in Opus 4)
  - **Activation**: agentic misalignment, blackmail prevention, constitutional training, teaching reasoning, difficult advice, RLHF, alignment generalization

### Evaluating Claude's bioinformatics capabilities with BioMysteryBench
- [[biomysterybench]] - Bioinformatics benchmark using 99 messy real-world questions across genomics, transcriptomics, and epigenomics with method-agnostic evaluation
  - Tetrad design: method-agnostic, objective ground-truth, superhuman questions, validation notebooks
  - 76 human-solvable + 23 human-difficult questions (up to 5 experts baselined each)
  - Two strategies: "know-it-all" (internal knowledge) and "multi-method convergence"
  - Reliability gap: 86% reliable solves on human-solvable, only 44% on human-difficult
  - **Activation**: BioMysteryBench, bioinformatics benchmark, superhuman question generation, reliability analysis, method-agnostic evaluation

### Donating Our Open-Source Alignment Tool (Petri)
- [[petri-alignment-tool]] - Petri v3 open-source alignment testing toolbox with auditor-target-judge architecture, donated to Meridian Labs
  - Split architecture: auditor (scenario generator) -> target (model under test) -> judge (scorer)
  - Petri 3.0: adaptability (split components), Dish add-on (real system prompts/scaffolds), Bloom integration (depth)
  - Tests deception, sycophancy, cooperation with harmful requests
  - Adopted by UK AISI for sabotage evaluation; joins Inspect and Scout at Meridian Labs
  - **Activation**: Petri, alignment testing, auditor-judge model, Dish add-on, Bloom integration, Meridian Labs, model evaluation

## 2026-05-23 - Quantum Computing Research (Cron Job)

### Quantum Circuit Design via Dynamic Pauli Constraints
- [[quantum-circuit-dynamic-pauli-constraints]] - Software-oriented quantum computation model where gates are specified by constraints on Pauli observables, with k-local quantum state tomography per layer; universal for BQP with O(D²N log N) overhead (arXiv: 2605.22744)
  - Formalizes NISQ-era quantum software design in terms of physically observable quantities — gates as Pauli constraints, not unitary matrices
  - Equivalent to coupling-graph-restricted circuit model with polynomial overhead
  - Provides a natural software interface for quantum imaginary time evolution, procedural generation, and verifiable quantum computing
  - **Activation**: Pauli constraints, constraint-based quantum circuit, NISQ quantum software, k-local tomography, measurement-aware compilation

### Reinforcement Learning for Ion Shuttling on Trapped-Ion Quantum Computers
- [[rl-ion-shuttling-trapped-ion]] - First RL-based optimization of ion transport in modular trapped-ion chips, achieving up to 36.3% reduction in shuttling operations vs heuristic baselines (arXiv: 2605.22463)
  - RL agent learns optimal shuttling strategies through direct interaction with chip environment
  - Architecture-agnostic: easily applicable to various chip designs
  - Addresses high-dimensional optimization problem of ion routing between storage, preparation, and gate zones
  - **Activation**: ion shuttling optimization, trapped-ion quantum computer, RL quantum hardware, quantum circuit compilation, modular chip architecture
