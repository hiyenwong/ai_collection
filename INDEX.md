## 2026-05-13 - Medicine + Neuroscience (Cron Job)
## 2026-05-13 - 医学 + 量子力学 (Cron Job)

### FQPDR: Federated Quantum Neural Network for Privacy-preserving Early Detection of Diabetic Retinopathy
- [[federated-quantum-medical-diagnosis]] - 联邦量子神经网络用于隐私保护的糖尿病视网膜病变早期检测 (arXiv: 2605.08324)
  - 核心要点: 结合联邦学习与量子神经网络，实现多机构协作医疗诊断而不共享患者数据
  - 核心要点: 在有限样本和少量可学习参数下实现鲁棒的轻量级学习模型
  - **Activation**: federated quantum medical, FQPDR, quantum federated learning, privacy-preserving medical AI, 联邦量子医疗, 隐私保护医疗诊断

### Quantum Circuit Simulation of Compartmental Drug Dynamics
- [[quantum-pkpd-simulation]] - 量子电路模拟房室药代动力学模型，用于群体药代动力学参数估计 (arXiv: 2605.09691)
  - 核心要点: 将经典PK/PD微分方程重构为开放量子系统，使用12量子比特编码4个药理学房室
  - 核心要点: 量子增强SAEM算法实现更好的统计拟合，同时保持参数估计一致性
  - **Activation**: quantum PK/PD, quantum pharmacokinetics, quantum drug dynamics, 量子药代动力学, 量子临床模拟



### Letting the Neural Code Speak: Automated Characterization of Monkey Visual Neurons through Human Language
- [[neural-code-language-interpretability]] - Natural language hypothesis generation + closed-loop verification for single-neuron selectivity across visual hierarchy (arXiv: 2605.12485)
  - Three-stage pipeline: Translate (image→text via VLM) → Semantic Hypothesis (LLM distills extreme responses) → Verification (text→image generation + digital twin validation)
  - >96% of V1/V4 neurons driven to extreme percentiles by hypothesis-generated images vs ~10% random baseline
  - V4 suppression highly describable (97.6%), V1 suppression poor (56%) — reveals language expressibility limits for sub-lexical features
  - RSA shows partial alignment: neural activity ↔ DINOv3 ↔ Qwen language embeddings
  - **Activation**: neural code interpretability, neuron characterization, digital twin neuroscience, language-based neural analysis, closed-loop hypothesis testing

### MTCSN: Multi-Timescale Conductance Spiking Networks
- [[multi-timescale-conductance-snn]] - Sparse, gradient-trainable SNN with multi-timescale conductance for enhanced temporal processing (arXiv: 2605.11835)
  - Multi-timescale conductance dynamics capture diverse firing patterns (bursting, adapting, regular)
  - Sparse recurrent connectivity with gradient-based training for efficient temporal sequence processing
  - **Activation**: multi-timescale spiking, conductance SNN, gradient-trainable SNN, sparse spiking network, temporal processing

### Attractor Models for Language and Reasoning
- [[attractor-models-language-reasoning]] - Backbone pre-training with attractor dynamics for improved reasoning in language models (arXiv: 2605.12466)
  - Text representations evolve through learned energy landscape to stable attractor states
  - Multi-step reasoning modeled as trajectories through attractor basins with energy barriers
  - **Activation**: attractor language model, attractor reasoning, dynamical systems NLP, energy-based language, backbone pre-training

### EEG Microstate Discovery via Variational Deep Embedding
- [[eeg-microstate-variational-embedding]] - Unsupervised EEG microstate discovery using VAE-based deep embedding for robust biomarker identification (arXiv: 2605.10947)
  - Variational autoencoder captures nonlinear microstate structure beyond k-means limitations
  - Probabilistic soft assignment with temporal HMM for clinical biomarker discovery
  - **Activation**: EEG microstate discovery, variational EEG embedding, microstate analysis, EEG temporal segmentation, deep embedding EEG

---

## 2026-05-13 - Neuroscience Research (Cron Job)

### Counterfausal Analysis of Brain Network Dynamics
- [[counterfactual-brain-dynamics]] - Hodge-theoretic counterfausal causal analysis framework modeling brain network perturbations as energy-flow problems (arXiv: 2603.29843)
  - Decomposes directed brain communication into dissipative (gradient) and persistent (harmonic) components via Hodge theory
  - Enables simulated intervention analysis: predicting how causal architecture reconfigures under lesions or neuromodulation
  - Demonstrated on temporal lobe epilepsy (400 HCP subjects) comparing pathological recurrence vs therapeutic disconnection
  - **Activation**: counterfausal brain, Hodge theory brain, causal brain network, brain network intervention, harmonic flow brain, Dirichlet energy network

### Spiking Free Energy Control (SFEC)
- [[spiking-free-energy-control]] - Bio-plausible spiking neural control framework where neurons fire only when reducing free energy (arXiv: 2603.09729)
  - Bridges Free Energy Principle/Active Inference with spiking neural circuit implementation
  - Spike constraint gating: neurons only fire when ∂F/∂t < 0, achieving high sparsity and robustness
  - Resilient to both external (sensory noise, collisions) and internal (synaptic noise, neuron silencing) perturbations
  - Deployable on neuromorphic hardware (Loihi, SpiNNaker) for energy-efficient robotics control
  - **Activation**: spiking control, free energy principle SNN, active inference spiking, neuromorphic control, spike-based free energy, SFEC

---

## 2026-05-13 - Medicine + Quantum Computing (Cron Job)

### Medical fMRI & Quantum Computing

- [[quantum-fmri-foundation-models]] - Quantum-enhanced fMRI foundation models combining Brain-DiT with quantum ML for neuroimaging analysis (arXiv: 2604.12683)
  - Integrates pre-trained fMRI foundation models with quantum feature mapping
  - Quantum kernel methods for brain disorder classification and cross-subject generalization
  - **Activation**: quantum fMRI, quantum brain imaging, quantum foundation model brain, quantum neuroimaging

- [[quantum-eeg-biomarker-discovery]] - Quantum ML for robust EEG biomarker discovery across subjects and platforms (arXiv: 2604.22116)
  - Quantum kernel-based EEG feature extraction for neurological conditions
  - Cross-subject and cross-platform biomarker validation
  - **Activation**: quantum EEG biomarker, quantum brain signal, quantum EEG classification, quantum neurological biomarker

- [[quantum-flow-matching-medical]] - Quantum-enhanced flow matching for medical image generation and longitudinal analysis (arXiv: 2605.08648)
  - Quantum variational circuits in flow matching for disease progression modeling
  - Quantum MoE routing for multimodal medical image synthesis
  - **Activation**: quantum flow matching medical, quantum medical image generation, quantum disease progression, quantum longitudinal imaging

---

## 2026-05-13 - Neuroscience Research (Cron Job - Batch 4: Standalone Sync)

### Standalone Skills Synced to ai_collection (60 skills)
Batch sync of all remaining standalone neuroscience/quantum/medical skills from `~/.hermes/skills/` to ai_collection project and INDEX.

#### Key Skills Added:
- [[behavior-vlm-neuroscience]] - Finetuning-free behavioral understanding for neuroscience using VLMs
- [[cold-atom-reservoir-computing]] - Hybrid quantum-classical medical imaging with neutral-atom reservoir computing
- [[frequency-matching-snn-mmwave]] - Frequency matching in SNNs for mmWave sensing using LIF dynamics
- [[qml-spiking-encoding]] - SPATE: Spiking-phase adaptive temporal encoding for QML
- [[universal-neural-propagator]] - Universal Neural Propagator methodology for learning neural dynamics
- [[multi-scale-info-geometry-neural]] - Multi-scale information geometry for neural population codes
- [[self-correcting-quantum-memory-3d]] - Passive self-correcting quantum memory in 3D Pauli stabilizer Hamiltonian
- [[quantum-robust-control]] - Robust quantum control engineering patterns
- [[quantum-cognition]] - Quantum cognition methodology for modeling cognitive processes
- [[quantum-statistical-metrology]] - Quantum metrology for multi-parameter estimation using purification-assisted schemes
- [[spiking-phase-quantum-encoding]] - Spiking-phase adaptive temporal encoding for quantum machine learning
- [[quantum-sparsity-edge-chaos]] - Quantum sparsity design principle for robust VQAs using edge-of-chaos theory
- [[quantum-learning-theory]] - Quantum learning theory methodology — sample complexity and generalization bounds
- [[quantum-learning-theory-cv]] - Quantum learning theory for continuous-variable systems
- [[quantum-gaussian-state-learning]] - Sample-optimal learning of bosonic Gaussian quantum states
- [[verifiable-quantum-advantage]] - Verifiable quantum advantage algorithm design and analysis
- [[topological-quantum-computing]] - Topological quantum computing with anyon braiding and fault tolerance
- [[quantum-margulis-codes]] - Quantum Margulis Codes for fault-tolerant quantum computing
- [[quantum-fault-tolerance-benchmark]] - QEC code evaluation under hardware-motivated noise
- [[quantum-fault-tolerance-verification]] - Quantum fault-tolerance verification via syndrome analysis
- [[quantum-error-correction-methods]] - Reusable QEC research patterns
- [[css-factor-graph-decoding]] - CSS QEC syndrome decoding via factor graphs and belief propagation
- [[css-syndrome-decoding]] - Factor-graph formulation of CSS quantum error correction
- [[loss-biased-qec]] - Loss-biased fault-tolerant QEC methodology
- [[iceberg-error-detection]] - Fault-tolerant error detection using Iceberg [[2m, 2m-2, 2]] code
- [[state-adaptive-error-correction]] - State-adaptive error correction and fault tolerance
- [[syndrome-resampling-qec]] - Syndrome resampling for enhancing QEC performance
- [[quantum-boltzmann-machine-bilevel]] - Quantum Boltzmann Machine via bilevel optimization
- [[quantum-protocol-designer]] - Design and analyze quantum information processing protocols
- [[quantum-software-architecture]] - Component-based QSA framework
- [[quantum-program-linting]] - LLM-powered static analysis for quantum programs
- [[quantum-program-analysis]] - LLM-powered QA for quantum programs
- [[quantum-program-semantic-verification]] - Semantics-based verification for quantum programs
- [[quantum-circuit-synthesis-gst]] - Generative quantum circuit synthesis from Gate Set Tomography
- [[quantum-distributed-snapshot]] - Quantum distributed algorithms based on classical distributed snapshots
- [[quantum-os-resource-management]] - Quantum OS resource management patterns
- [[fpga-quantum-error-decoder]] - Scalable FPGA-based QEC decoding architectures
- [[rl-qec-control]] - Reinforcement learning for QEC control
- [[quanforge-qnn-testing]] - Mutation testing framework for QNNs
- [[qml-mutation-testing]] - Systematic mutation testing for QML
- [[quantum-neural-topology]] - QNNs and topological data analysis research
- [[quantum-mechanical-data-assimilation]] - Quantum Mechanical Data Assimilation methodology
- [[quantum-knowledge-graph]] - Quantum-enhanced knowledge graphs using QNLP
- [[quantum-circuit-construction-ml]] - ML for constructing quantum circuits
- [[quantum-cognition]] - Quantum cognition for cognitive process modeling
- [[quantum-tunneling-optimization]] - Quantum-inspired evolutionary optimization for non-convex problems
- [[quantum-optimization-qaoa]] - QAOA guide for combinatorial optimization
- [[quantum-optimization-transportation]] - Quantum optimization for transportation networks
- [[quantum-finance]] - Quantum computing in finance: portfolio optimization, option pricing
- [[quantum-finance-analysis]] - Quantum computing in finance and economics
- [[quantum-finance-portfolio]] - Quantum portfolio optimization: QUBO, quantum annealing, QRNG Monte Carlo
- [[quantum-game-theory-economics]] - Quantum game theory in economics and decision making
- [[quantum-positive-maps]] - Positive trace-preserving maps in quantum information
- [[quantum-proper-scoring-rules]] - Proper scoring rules for quantum state estimation
- [[quantum-statistical-estimation]] - Quantum statistical estimation theory
- [[vacuum-entanglement-extraction]] - Vacuum entanglement extraction from quantum field theory
- [[quantum-magic-state-analysis]] - Magic quantification for non-stabilizerness in quantum algorithms
- [[sample-optimal-gaussian-state-learning]] - Sample complexity bounds for bosonic Gaussian state learning
- [[multiparameter-hamiltonian-estimation]] - Optimal multiparameter Hamiltonian estimation
- [[equivariant-rl-clifford]] - Equivariant RL for Clifford quantum circuit synthesis
- [[equivariant-rl-quantum-circuit-synthesis]] - Equivariant RL for quantum circuit synthesis
- [[quantum-sparsity-edge-chaos]] - Quantum sparsity at edge of chaos for robust VQAs
- [[quantum-sensor-reliability]] - RL-optimized dynamical decoupling for quantum sensor networks
- [[spintune-quantum-sensor-reliability]] - SpinTune: RL-based DD pulse optimization
- [[photonic-qnn-algorithmic-advantage]] - Algorithmic advantage of photonic QNNs
- [[pulse-level-quantum-computing]] - Pulse-level quantum computing design and optimization
- [[pulse-level-quantum-fourier-models]] - Pulse-level QFMs for quantum machine learning
- [[pulse-level-qfm]] - Pulse-level Quantum Fourier Models
- [[qfi-stabilizer-framework]] - Quantum Fisher Information framework for stabilizer codes
- [[learnable-observable-qnn]] - Learnable Observable QNN methodology
- [[quantum-cayley-llm-adapters]] - Quantum-enhanced LLM via Cayley-parameterized adapters
- [[gated-qkan-fwp]] - Quantum-inspired sequence learning with Gated QKAN-FWP
- [[quantum-bayesian-state-estimation]] - Quantum Bayesian state estimation and transport dynamics
- [[quantum-circuit-drug-dynamics]] - Quantum circuit simulation of compartmental drug dynamics
- [[quantum-pkpd-simulation]] - Quantum PK/PD simulation for pharmacokinetics
- [[quantum-medical-feature-fusion]] - Adaptive hybrid quantum-classical medical image fusion
- [[quantum-medical-research]] - Quantum computing in medical research
- [[quantum-healthcare-research]] - Quantum healthcare research methodology
- [[quantum-healthcare-patterns]] - Reusable quantum healthcare research patterns
- [[quantum-kernel-medical-embeddings]] - Quantum kernel methods for medical AI embeddings
- [[medical-ai-diagnosis]] - AI medical diagnosis system patterns
- [[medical-domain-adaptation]] - Medical image domain adaptation and transfer learning
- [[tt-opd-medical-agent-training]] - Turn-level truncated OPD for medical agent training
- [[multi-agent-clinical-reasoning]] - Multi-agent clinical reasoning and radiology
- [[pan-fm-pan-organ-foundation]] - Pan-Organ Foundation Model for multimodal biomedical AI
- [[concept-reasoning-continual-learning]] - Concept-Reasoning Expansion for continual learning
- [[moe-optimal-transport-routing]] - MoE routing using optimal transport
- [[distributed-quantum-error-correction]] - Distributed QEC design and analysis
- [[distributed-iqft-communication]] - Communication-efficient distributed IQFT
- [[modular-quantum-shor-compilation]] - Distributed Shor's algorithm compilation on modular atoms
- [[qbalance-quantum-workflow-optimization]] - Multi-objective quantum workflow optimization for NISQ
- [[quantum-data-centers-entanglement]] - Quantum data center network design and entanglement distribution
- [[quantum-network-task-control]] - Centralized task-based quantum network control
- [[quantum-cv-learning-theory]] - Quantum learning theory for CV systems
- [[nuclear-lattice-vqe]] - VQE for nuclear lattice models
- [[fluxonium-scalable-architecture]] - Scalable fluxonium quantum processor architecture
- [[quantum-control-engineering]] - Engineering patterns for reliable quantum control
- [[dependable-quantum-systems]] - Dependability engineering for hybrid quantum-classical computing
- [[noise-enhanced-quantum-kernels]] - Noise-enhanced quantum kernels for analog quantum ML
- [[organic-quantum-reservoir-computing]] - Magnetic-field-free quantum reservoir computing
- [[compositional-quantum-heuristics]] - Compositional quantum heuristics for barren plateau mitigation
- [[mathematical-quantization]] - Kohn-Nirenberg and Lie group quantization
- [[quantum-geometric-statistical-analysis]] - Quantum probability + Fisher geometry + tensor networks
- [[quantum-geometry-topology-research]] - Quantum-geometry-topology interdisciplinary research
- [[cross-layer-crypto-analysis]] - Cross-layer cryptographic security analysis
- [[post-quantum-cryptographic-protocol-analysis]] - Post-quantum cryptographic protocol analysis
- [[ramanujan-hypergraph-quantum-routing]] - Ramanujan hypergraph block permutation routing
- [[magic-number-theoretic-complexity]] - Magic state complexity analysis
- [[hybrid-quantum-classical-architecture]] - Hybrid quantum-classical architecture design
- [[hybrid-quantum-classical-framework]] - Dataflow-based hybrid quantum-classical computing
- [[hybrid-quantum-classical-system-design]] - Hybrid quantum-classical system design patterns
- [[hybrid-quantum-classical-systems]] - Hybrid quantum-classical systems engineering
- [[mqt-quantum-classical-compiler]] - MQT Compiler Collection for future-proof quantum-classical compilation
- [[hardware-motivated-noise-modeling]] - Hardware-motivated noise modeling for fault tolerance
- [[affine-subcode-ensemble-decoding]] - Affine subcode ensemble decoding for degenerate QEC
- [[adaptive-acquisition-bbo]] - Adaptive acquisition function for black-box optimization
- [[core-cross-site-ood-brain-network]] - CORE framework for cross-site OOD brain network robustness
- [[eeg-preprocessing-reliability]] - EEG preprocessing reliability assessment methodology
- [[uncertainty-guided-hypergraph-refinement]] - Uncertainty-Guided Hypergraph Refinement
- [[flux-longitudinal-flow-matching]] - Geometry-aware longitudinal flow matching for biological data
- [[agentic-fusion-materials]] - Agentic AI framework for materials discovery
- [[digital-twin-multi-agent-consensus]] - Digital twin-based consensus for multi-agent CPS
- [[heterogeneous-contract-control]] - Heterogeneous assume-guarantee contracts for CPS
- [[graph-pooling-node-features]] - Graph pooling with node feature interaction analysis
- [[multi-scale-info-geometry-neural]] - Multi-scale information geometry for neural population codes
- [[agent-integration-testing]] - Agent integration testing patterns
- [[agentic-fast-slow-planning]] - Bridging large-model reasoning with real-time control
- [[ai-power-profiling]] - GPU power consumption profiling for generative AI
- [[ai-workload-power-profiling]] - AI workload power profiling for data centers
- [[bayesian-agent-orchestration]] - Bayes-consistent multi-agent orchestration
- [[bian-que-agentic-operations]] - Agentic framework for online system operations
- [[constraint-guided-execution]] - Constraint-guided execution for natural language interpretation
- [[coral-open-ended-discovery]] - Autonomous multi-agent open-ended discovery
- [[data-driven-distributed-control]] - Data-driven distributed controller synthesis
- [[distributionally-robust-control]] - Distributionally robust control system design
- [[dsm-llm-modularization]] - LLM-based Design Structure Matrix modularization
- [[gaussian-grpo]] - Gaussian Group Relative Policy Optimization
- [[hierarchical-moe-detection]] - Hierarchical MoE for object detection
- [[llm-sysml-alignment]] - LLM-assisted semantic alignment for SysML v2
- [[local-rl-alignment-engineering]] - Local base model RL alignment (RLHF/DPO/GRPO)
- [[ml-hybrid-distributed-caching]] - ML-hybrid distributed caching
- [[mpc-drl-autonomous-driving]] - MPC-RL integration for autonomous driving
- [[ontology-driven-cps-dataspace]] - Ontology-driven CPS dataspace
- [[plant-model-mismatch-mpc]] - MPC under plant-model mismatch
- [[psi-shared-state-architecture-v2]] - PSI shared-state architecture v2
- [[recode-agent-workflow]] - ReCode agent workflow
- [[shared-state-architecture]] - PSI persistent shared interface
- [[speculative-decoding-optimization]] - Speculative decoding with KV cache optimization
- [[stability-goal-obfuscation]] - Stability-goal obfuscation for autonomous systems
- [[quantum-tug-of-war-decision]] - Quantum Tug-of-War decision making model
- [[quantum-transport-clustering]] - Qlustering: unsupervised clustering via steady-state quantum transport
- [[qlustering-quantum-clustering]] - Unsupervised clustering via quantum transport in GKSL networks
- [[universally-robust-quantum-control]] - Universal noise-agnostic quantum control framework
- [[antic-mics-wcet-analysis]] - Mixed-Criticality WCET analysis
- [[datacenter-ai-workload-power-planning]] - Data center AI workload power planning
- [[discounted-mpc-plant-model-mismatch]] - Discounted MPC under plant-model mismatch
- [[distributed-system-resiliency]] - Distributed system resiliency patterns
- [[dockerize-node-pnpm-monorepo]] - Dockerize Node.js pnpm monorepos
- [[claude-code-token-optimization]] - Token optimization for CLI coding agents
- [[quantum-pet-biomarkers]] - Quantum entanglement degree as PET biomarkers for hypoxia
- [[neuromorphic-spintracker-asl]] - Neuromorphic visual attention for sign language on SpiNNaker

### Collection Statistics
- **Total ai_collection skills**: 1186 (Hermes) / 2306 (Project)
- **Coverage Rate**: 100% of 42 May 2026 neuroscience papers
- **Standalone Skills Synced**: 198 skills synced to ai_collection project
- **Collection Status**: Extreme maturity — all major neuroscience, quantum, and medical domains covered

## 2026-05-13 - Neuroscience Research (Cron Job)

### Spatiotemporal TDANN for MT Direction Maps
- [[mt-direction-maps-spatiotemporal]] - 3D ResNet with MoCo self-supervised learning + spatial loss produces brain-like direction-selective maps and pinwheel structures matching macaque MT physiology (arXiv: 2605.11718)
  - Extends TDANN to dorsal stream: 3D ResNet trained on naturalistic videos via contrastive learning
  - MT tuning emerges from strict trade-off between discriminative pressure and spatial regularization
  - Quantitative match to in vivo macaque MT: direction selectivity index, circular variance, pinwheel density
  - Unifies ventral and dorsal stream topographic origins under single computational mechanism
  - **Activation**: MT direction maps, spatiotemporal TDANN, dorsal stream self-organization, motion direction selectivity, cortical topography, MoCo visual neuroscience

### Attractor Models for Language and Reasoning
- [[attractor-models-language-reasoning]] - Fixed-point attractor architecture with implicit differentiation for scalable iterative refinement; 770M outperforms 1.3B Transformer on 2× tokens, 27M achieves 91.4% Sudoku-Extreme (arXiv: 2605.12466)
  - Two-stage: backbone proposes embeddings, attractor refines via fixed-point solving
  - Constant memory for effective depth; iterations chosen adaptively by convergence
  - Equilibrium internalization: fixed-point training enables solver removal at inference
  - Outperforms Claude and GPT-o3 on challenging reasoning tasks with tiny model
  - **Activation**: attractor models, fixed-point reasoning, implicit differentiation, looped Transformer, iterative refinement, equilibrium internalization

### EEG Microstate Discovery via Variational Deep Embedding
- [[eeg-microstate-variational-embedding]] - Variational deep embedding replaces k-means microstate clustering with uncertainty-aware latent space learning for interpretable EEG analysis (arXiv: 2605.10947)
  - Deep VAE learns continuous temporal representation of EEG segments
  - Systematic architecture search identifies optimal configuration
  - Multi-quadrant evaluation: interpretability, stability, accuracy, scalability
  - Principled uncertainty quantification via variational posterior
  - **Activation**: EEG microstate discovery, variational EEG embedding, microstate clustering, interpretable EEG analysis, deep EEG pipeline

## 2026-05-13 - 医学 + 量子力学 (Cron Job - 周三医学主题)

### Hybrid Quantum Neural Networks for Enhanced Breast Cancer Thermographic Classification
- [[hybrid-quantum-medical-imaging]] - Integrates quantum variational circuits with classical CNN backbones for thermographic breast cancer classification, leveraging quantum advantage in complex thermal pattern discrimination (arXiv: 2604.16953)
  - Hybrid architecture: Classical CNN encoder → Quantum variational layer → Classical classifier
  - Amplitude encoding of CNN features into quantum states for enhanced discrimination
  - Quanvolutional filters as alternatives to convolutional layers for medical image patches
  - Joint classical-quantum optimization using parameter-shift rule for gradient computation
  - **Activation**: hybrid quantum neural network, quantum medical imaging, thermographic cancer detection, quanvolutional network, quantum healthcare AI, breast cancer quantum classification

## 2026-05-14 - 医学 + 量子力学 (Cron Job - 周三医学主题)

### FQPDR: Federated Quantum Neural Network for Privacy-preserving Early Detection of Diabetic Retinopathy
- [[fqpdr-quantum-medical-diagnosis]] - Federated Quantum Neural Network for distributed medical diagnosis across hospitals without sharing patient data; trains local QNNs and aggregates via FedAvg (arXiv: 2605.08324)
  - Multi-hospital federated QNN architecture with parameterized quantum circuits
  - Classical medical features encoded into quantum states via angle embedding
  - Privacy-preserving: patient data never leaves originating institution
  - Applicable to rare disease detection requiring pooled sparse data
  - **Activation**: federated quantum, quantum medical diagnosis, FQN, privacy-preserving medical AI, diabetic retinopathy quantum, distributed quantum healthcare

## 2026-05-14 - Quantum Computing Research (Cron Job)

### Pre-Asymptotic Trainability in Photonic Variational Circuits under Postselection
- [[photonic-variational-trainability]] - Challenges barren plateau assumption in passive photonic circuits; postselection prevents strong mixing dynamics that cause gradient vanishing (arXiv: 2605.11879)
  - Linear optical quantum computing shows trainability despite deep circuits
  - Postselection maintains gradient variance at usable levels
  - Implications for photonic VQA optimization and NISQ-era training

## 2026-05-13 - 医学 + 量子力学 (Cron Job - 周三医学主题)

### Quantum Entanglement Degree as Novel PET Biomarkers for Hypoxia
- [[quantum-pet-biomarkers]] - Novel quantum sensing method using positronium photon entanglement degree, lifetime, and annihilation ratios to non-invasively assess tissue oxygen concentration (arXiv: 2605.00021)
  - Two approaches: (1) dual-parameter τ_oPs + R_oPs-3γ/2γ measurement, (2) entanglement degree sensitivity to pick-off vs self-annihilation
  - Derived formula linking pO₂ to quantum entanglement metrics
  - Quantitative C_QE predictions across tissue types (adipose: 0.890, water: 0.867)
  - **Activation**: quantum PET biomarkers, positronium hypoxia sensing, quantum entanglement PET, positronium lifetime oxygen, pick-off conversion annihilation

### Quantum Circuit Simulation of Compartmental Drug Dynamics: Leveraging Variational Algorithms for Nonlinear Mixed-Effects Population Pharmacokinetics
- [[quantum-pkpd-simulation]] - Reformulates compartmental PK/PD models as open quantum systems using PennyLane quantum circuits for population pharmacokinetics parameter estimation (arXiv: 2605.09691)
  - Classical ODE-based PK/PD models encoded as quantum circuit evolution
  - Variational quantum algorithms for nonlinear mixed-effects population model fitting
  - Potential exponential speedup for multi-compartment drug dynamics simulation
  - Population-level predictions via quantum expectation values
  - **Activation**: quantum PK/PD, quantum pharmacokinetics, drug dynamics simulation, compartmental quantum model, quantum circuit drug simulation, variational quantum healthcare

### Medical Imaging Classification with Cold-Atom Reservoir Computing using Auto-Encoders and Surrogate-Driven Training
- [[cold-atom-medical-imaging]] - Hybrid quantum-classical pipeline with neutral-atom reservoir computing for medical image classification (polyp detection) using guided auto-encoder for dimensionality reduction (arXiv: 2605)
  - Guided auto-encoder compresses medical images while preserving clinically relevant features
  - Cold neutral-atom reservoir provides rich nonlinear dynamics for classification
  - Surrogate-driven training avoids repeated expensive quantum experiments
  - NISQ-compatible — works with noisy physical reservoirs
  - **Activation**: cold-atom reservoir computing, neutral-atom medical imaging, quantum reservoir medical classification, auto-encoder reservoir, surrogate-driven training, quantum-classical medical pipeline

## 2026-05-13 - Neuroscience Research (Cron Job)

### Letting the neural code speak: Automated characterization of monkey visual neurons through human language
- [[neural-code-language-characterization]] - Closed-loop framework using natural language to characterize neural selectivity at scale; LLM-generated semantic hypotheses verified in silico on digital twins of macaque V1/V4 (arXiv: 2605.12485)
  - Natural language descriptions capture neural selectivity from V1 (oriented edges, spatial frequency) to V4 (form, color, texture conjunctions)
  - LLM-generated activating/suppressing hypotheses drive 96.1% of V4 neurons above 95th percentile of natural-image responses
  - Representational similarity analysis: vision most aligned to neural activity; linguistic compression lossy yet semantically faithful
  - **Activation**: neural code characterization, language-based neural description, digital twin neuroscience, interpretable neural selectivity, agentic neural discovery, V1 V4 semantic description

### Joint sparse coding and temporal dynamics support context reconfiguration
- [[context-reconfiguration-sparse-temporal]] - Identifies sparse coding + temporal dynamics in mouse mPFC as core mechanism for preserving prior knowledge during context transitions; SNNs naturally exhibit both properties for lifelong learning (arXiv: 2605.10178)
  - Sparse context-dependent representations reduce cross-context interference
  - Temporal dynamics enhance context separability across time
  - Networks with both properties (e.g., SNNs) show improved retention without auxiliary heuristics
  - **Activation**: context reconfiguration, sparse coding temporal dynamics, catastrophic forgetting, lifelong learning SNN, mPFC context switching, neural representation stability

## 2026-05-13 - Neuroscience Research (Cron Job)

### Encoding and Decoding Temporal Signals with Spiking Bandpass Wavelets
- [[spiking-bandpass-wavelet-encoding]] - Recasts spike encoders as time-causal wavelet frames with quantitative bandwidths and reconstruction error bounds; achieves NRMSE comparable to continuous wavelet transforms on ECG and audio (arXiv: 2605.09770)
  - Spike-based encoding reformulated as wavelet frame decomposition
  - Quantitative bandwidth analysis and reconstruction error bounds for spiking representations
  - Direct mapping to neuromorphic hardware (Loihi, SpiNNaker)
  - **Activation**: spiking bandpass wavelet, spike-based signal encoding, neuromorphic signal processing, temporal signal encoding, wavelet spike encoding, time-causal wavelet frames

### Cortico-cerebellar modularity as architectural inductive bias for efficient temporal learning
- [[cortico-cerebellar-modularity-rnn]] - Augments RNN with cerebellar-inspired feedforward module (CB-RNN), enabling faster convergence on temporal tasks via bidirectional cortico-cerebellar coupling (arXiv: 2605.10356)
  - Cortical module (RNN) for rich temporal dynamics + cerebellar module (feedforward) for fast predictive correction
  - Bidirectional coupling between slow recurrent and fast feedforward pathways
  - Improved learning efficiency and temporal precision across tasks
  - **Activation**: cortico-cerebellar RNN, cerebellar neural architecture, temporal sequence learning, brain-inspired RNN, modular neural architecture

## 2026-05-13 - Neuroscience Research (Cron Job - Batch 3)

### Multi-Timescale Conductance Spiking Networks: A Sparse, Gradient-Trainable Framework with Rich Firing Dynamics for Enhanced Temporal Processing
- [[multi-timescale-conductance-snn]] - SNN framework using fast/slow/ultra-slow conductances to shape I-V curve, enabling direct BPTT (no surrogate gradients) with rich firing regimes and high sparsity (arXiv: 2605.11835)
  - Multi-timescale conductance parametrization replaces phenomenological LIF dynamics
  - Direct backpropagation through time without surrogate gradient approximation
  - Single model exhibits tonic, phasic, and bursting firing regimes
  - Outperforms LIF and AdLIF on Mackey-Glass regression with substantially sparser activity
  - **Activation**: multi-timescale spiking, conductance SNN, gradient-trainable SNN, I-V curve shaping, temporal processing SNN, direct BPTT SNN

### Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching
- [[autoregressive-flow-matching-neural-dynamics]] - Generative forecasting framework using autoregressive flow matching for probabilistic neural dynamics prediction from multimodal sensory input and past neural history (arXiv: 2604.11178)
  - Flow matching learns conditional distribution of future neural states given past dynamics
  - Autoregressive factorization captures temporal dependencies between predictions
  - Past neural history is the dominant predictor — more than sensory input alone
  - Significantly outperforms GLM and non-autoregressive baselines on fMRI data
  - **Activation**: neural dynamics prediction, autoregressive flow matching, fMRI forecasting, probabilistic neural prediction, closed-loop neurotechnology, transport-based generative modeling

     1|## 2026-05-13 - Quantum Metrology Research (Cron Job)
     2|
     3|### Optimal FALQON for Quantum Approximate Optimization via Layer-wise Parameter Tuning
     4|- [[optimal-falqon-qaoa]] - Treats per-layer time step (δ_k) and scaling factor (M_k) as classical optimization variables, reducing circuit depth vs standard FALQON, outperforms QAOA on all 94 3-regular graphs (12 vertices) (arXiv: 2605.08332)
     5|  - Single circuit evaluation per layer maintained, NISQ-compatible
     6|