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
