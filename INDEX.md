
## 2026-05-20 - Medicine + Quantum (Cron Job)

### Discovering Data Encoding Strategies for QCCNN Using MCTS
- [[effective-rank-encoding-predictor]] - Uses effective rank of quantum feature maps to predict encoding performance, accelerating QML encoding search (arXiv: 2605.18540)
  - 核心要点 1: Entanglement capability and Fourier decomposition provide minimal insight into encoding performance
  - 核心要点 2: Effective rank of feature maps exhibits meaningful correlation and serves as threshold criterion
  - **Activation**: effective rank encoding, feature map rank QML, encoding performance prediction

### Multi-Class Neurological Disorder Prediction with Tensor Network
- [[tensor-network-neurological-predictor]] - Tensor Network Feature Engineering for multi-class neurological disorder prediction from sparse MRI data (arXiv: 2605.17771)
  - 核心要点 1: Tensor decompositions extract rich features from sparse MRI representations
  - 核心要点 2: Supports multi-class disorder classification with interpretable factor matrices
  - **Activation**: tensor network MRI, neurological disorder prediction, tensor feature engineering

### Adaptive Hybrid Quantum-Classical Feature Fusion for Breast Cancer
- [[adaptive-hybrid-feature-fusion-medical]] - Learns optimal complementarity between quantum and classical features through adaptive weighting for medical image classification (arXiv: 2604.22903)
  - 核心要点 1: Adaptive fusion module learns per-sample optimal quantum/classical feature weighting
  - 核心要点 2: Fusion weights reveal when quantum features complement classical features
  - **Activation**: adaptive hybrid feature fusion, quantum classical complementarity, medical image quantum fusion

## 2026-05-19 - Neuroscience Research (Cron Job - Evening)

### Session Summary
- **Papers Scanned**: 17 total (q-bio.NC: 4 new, cs.NE: 4 new + 4 cross + 9 replaced)
- **Neuroscience-Relevant Papers Analyzed**: 6
- **Coverage Rate**: 100% (6/6 papers already covered by existing skills)
- **New Skills Created**: 0 (collection at extreme maturity)
- **Standalone Skills Synced**: 1 (neuromorphic-spiNNaker-asl)

### Papers Analyzed
| # | Paper Title | arXiv ID | Status | Existing Skill |
|---|-------------|----------|--------|----------------|
| 1 | MIRAGE: Robust multi-modal architectures translate fMRI-to-image models from vision to mental imagery | 2605.17198 | ✅ Covered | `mirage-fmri-mental-imagery-decoding` |
| 2 | Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity | 2605.17199 | ✅ Covered | `geometric-phase-transition-hippocampal-memory` |
| 3 | Von Economo neurons enable reliable social skill acquisition in recurrent spiking neural networks | 2605.17399 | ✅ Covered | `ven-circuit-snn-social-learning` |
| 4 | Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function | 2605.18118 | ✅ Covered | `functional-whole-brain-models` |
| 5 | Spiker-LL: An Energy-Efficient FPGA Accelerator Enabling Adaptive Local Learning in SNNs | 2605.18003 | ✅ Covered | `spiker-ll-snn-accelerator` |
| 6 | Self-supervised local learning rules learn the hidden hierarchical structure of high-dimensional data | 2605.18557 | ✅ Covered | `self-supervised-local-learning-hierarchy` |

### Collection Statistics
- **Total Skills**: 1325
- **Coverage Maturity**: Extreme (>99%)
- **Standalone Sync**: neuromorphic-spiNNaker-asl synced to ai_collection

## 2026-05-20 - Neuroscience Research (Cron Job)

### Von Economo neurons enable reliable social skill acquisition in recurrent spiking neural networks
- [[vencircuit-ven-gradient-scaffold]] - Von Economo neurons as residual gradient scaffolds in SNNs, explaining their role in reliable learning and clinical patterns in bvFTD/ASC (arXiv: 2605.17399)
  - VENs (2% of neurons) provide direct gradient pathway immune to Jacobian instabilities in recurrent circuits
  - 98% convergence with VENs vs 70% without (OR=21.0, p=8.7e-5); failed ablated networks show complete learning absence
  - **Activation**: vencircuit, ven neurons, von economo, gradient scaffold, residual pathway, social cognition SNN

### Self-supervised local learning rules learn hidden hierarchical structure of high-dimensional data
- [[self-supervised-local-learning-rhm]] - Layerwise self-supervised local rules match backprop data efficiency while being biologically plausible (arXiv: 2605.18557)
  - Direct feedback approximations fail (miss input-specific masking); layerwise contrastive/non-contrastive rules succeed
  - No symmetric error network needed — solves weight transport problem with cortical-compatible plasticity
  - **Activation**: self-supervised local learning, random hierarchy model, biologically plausible backprop, layerwise contrastive

## 2026-05-20 - Medicine + Quantum Computing (Cron Job)

### CovAngelo: A hybrid quantum-classical computing platform for accurate and scalable drug discovery
- [[quantum-drug-discovery-pipeline]] - Hybrid quantum-classical platform combining VQE/QAOA for molecular conformation search with classical scoring for drug discovery (arXiv: 2604.10487)
  - Quantum algorithms explore conformational space more efficiently than classical methods
  - CovAngelo architecture: quantum sampling + classical scoring for scalable pipelines
  - **Activation**: quantum drug discovery, 量子药物发现, VQE molecular, QAOA drug screening, CovAngelo

### Latent Style-based Quantum Wasserstein GAN for Drug Design
- [[quantum-drug-discovery-pipeline]] - Quantum-classical generative model for molecular design with latent style conditioning and Wasserstein distance (arXiv: 2603.22399)
  - Quantum circuits provide high-dimensional feature space for molecular generation
  - Style conditioning controls molecular properties (solubility, toxicity, binding)
  - **Activation**: quantum WGAN, drug design, molecular generation, quantum generative

### Discovering Data Encoding Strategies for Quantum-Classical Neural Networks Using Monte Carlo Tree Search
- [[quantum-medical-imaging-pipeline]] - MCTS discovers optimal encoding circuits for QCCNN on medical imaging datasets; effective rank predicts performance (arXiv: 2605.18540)
  - Effective rank of feature maps correlates with encoding performance
  - Entanglement capability and Fourier decomposition provide minimal insight
  - **Activation**: quantum medical imaging, 量子医学影像, encoding discovery, MCTS encoding

### Adaptive Hybrid Quantum-Classical Feature Fusion for Breast Cancer Classification
- [[quantum-medical-imaging-pipeline]] - Temperature-Scaled Hybrid Fusion (TSHF) achieves 87.82% accuracy on BreastMNIST with quantum-classical architecture (arXiv: 2604.22903)
  - Three fusion strategies: SHF (offline), DHF (end-to-end), TSHF (dynamic balancing)
  - Temperature scaling resolves quantum-classical gradient mismatch
  - **Activation**: hybrid quantum classical, feature fusion, breast cancer QML, TSHF

### FQPDR: Federated Quantum Neural Network for Privacy-preserving Early Detection of Diabetic Retinopathy
- [[quantum-healthcare-privacy-framework]] - Federated QNN for early DR detection using limited samples and few learnable parameters (arXiv: 2605.08324)
  - Privacy-preserving: model parameters shared, patient data stays local
  - Lightweight quantum models effective for medical image tasks
  - **Activation**: federated quantum healthcare, 联邦量子医疗, privacy QNN, FQPDR

### Quantum-Enhanced Processing with Tensor-Network Frontends for Privacy-Aware Federated Medical Diagnosis
- [[quantum-healthcare-privacy-framework]] - MPS/TTN/MERA compression + QEP refinement for federated medical imaging with MPC-secured aggregation (arXiv: 2604.01616)
  - Tensor compression reduces both quantum processing dimension and MPC communication overhead
  - TTN+QEP combination shows most balanced overall profile
  - **Activation**: tensor network federated, quantum healthcare privacy, MPC quantum, QEP

## 2026-05-20 - Deep Learning Research (Cron Job)

### Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics
- [[probe-trajectory-reasoning-monitoring]] - Probe trajectories track concept probability evolution across CoT tokens; max-pooling achieves 95% AUROC, avg/last-token collapse to random (arXiv: 2605.18549)
  - Evaluating probes at every generated token yields better outcome prediction than static single-point probes
  - Template-based training data achieves near-parity with costly dynamically generated responses
  - Signal-processing features (volatility, trend, steady-state) capture temporal reasoning dynamics
  - **Activation**: probe trajectory, reasoning monitoring, LRM safety, CoT faithfulness, max-pooling probe

### Implicit Hierarchical GRPO: Decoupling Tool Invocation from Execution for Tool-Integrated Mathematical Reasoning
- [[implicit-hierarchical-grpo]] - Decouples tool invocation from execution via delayed execution; surrogate loss bridges explicit/implicit hierarchical policies; +2.53% on Qwen3-8B (arXiv: 2605.18500)
  - Immediate tool execution disrupts reasoning coherence; delayed execution preserves reasoning flow
  - Surrogate loss enables single policy to learn behavior equivalent to explicit hierarchical policy
  - Consistent gains across 6 out-of-domain math benchmarks without multi-stage training
  - **Activation**: hierarchical GRPO, tool-integrated reasoning, IH-GRPO, delayed tool execution

### SD-Search: On-Policy Hindsight Self-Distillation for Search-Augmented Reasoning
- [[sd-search-on-policy-hindsight-distillation]] - Derives step-level supervision from policy itself via on-policy hindsight self-distillation; no external teacher or annotations needed (arXiv: 2605.18299)
  - Single model plays student (inference context) and teacher (hindsight block) roles with different conditioning
  - Jensen-Shannon divergence at query positions layers dense step-level signal on GRPO trajectory reward
  - Eliminates need for external teacher models or sub-question annotation pipelines
  - **Activation**: sd-search, on-policy distillation, hindsight self-distillation, search-augmented reasoning, step-level credit

## 2026-05-19 - Neuroscience Research (Cron Job)

### Von Economo neurons enable reliable social skill acquisition in recurrent spiking neural networks: a computational account with clinical predictions
- [[ven-circuit-snn-social-learning]] - VENs as acquisition scaffolds in recurrent SNNs enabling 98% vs 70% convergence; clinical predictions for bvFTD and ASC (arXiv: 2605.17399)
  - VENs provide direct gradient pathway immune to Jacobian instabilities in recurrent circuits
  - Phase-ablation shows mid-training VEN removal most disruptive; inference ablation causes stochastic collapse
  - **Activation**: von economo neurons, VEN, social learning SNN, acquisition scaffold, bvFTD, autism, gradient pathway

### Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity
- [[geometric-phase-transition-hippocampal-memory]] - Crystalline population geometry enables >100x memory capacity in food-caching species vs non-caching (arXiv: 2605.17199)
  - Shesha stability metric quantifies geometric rigidity; caching hippocampus shows 2x temporal coherence
  - 169-fold representational redundancy as "geometric tax" against biological noise
  - **Activation**: geometric phase transition, hippocampal memory, population geometry, crystalline coding, Shesha stability, spatial memory

## 2026-05-20 - Neuroscience Research (Cron Job)

## 2026-05-20 - Medicine + Quantum (Cron Job)

### Multi-Class Neurological Disorder Prediction with Tensor Network Feature Engineering
- [[tensor-network-medical-imaging]] - PARAFAC/CP tensor decompositions extract discriminative features from 55,160 MRI images across 8 diagnostic categories; quantum-inspired classical framework matches recent baselines (arXiv: 2605.17771)
  - Ensemble classifier enriched with PARAFAC CP tensor decompositions achieves robust validation across tensor rank configurations
  - 5-fold nested stratified cross-validation demonstrates robustness to tensor network expressivity
  - **Activation**: PARAFAC medical imaging, tensor decomposition MRI, quantum-inspired classification, neurological disorder prediction, CP decomposition medical, tensor feature engineering

### Practical Quantum Federated Learning for Privacy-Sensitive Healthcare: Communication Efficiency and Noise Resilience
- [[quantum-federated-healthcare-communication]] - Hybrid QFL architecture reduces quantum transmissions from 3·T·N·M·P to {3t + 2(T−t)}·N·M·P with dynamic centralized/decentralized switching (arXiv: 2603.03853)
  - Light-cone feature selection eliminates redundant qubit features in PQC
  - Decentralized aggregation is more noise-resilient under depolarizing noise than centralized
  - **Activation**: quantum federated learning, QFL healthcare, communication efficiency, light-cone feature selection, decentralized quantum aggregation

### Quantum-Enhanced Processing with Tensor-Network Frontends for Privacy-Aware Federated Medical Diagnosis
- [[tensor-network-frontend-quantum-medical]] - Tensor-network (MPS/TTN/MERA) client-side compression with quantum-enhanced processor refinement; TTN+QEP most balanced for medical classification (arXiv: 2603.04674)
  - Client-side tensor networks compress local inputs → MPC-secured aggregation → QEP quantum-state refinement
  - TTN architecture best captures hierarchical spatial features in medical images
  - **Activation**: tensor network frontend, TTN medical, quantum enhanced processor, federated medical diagnosis, MPS compression

### Hybrid Quantum Neural Networks for Enhanced Breast Cancer Thermographic Classification: A Novel Quantum-Classical Integration Approach
- [[hqnn-breast-cancer-thermographic]] - HQNN integrates 4-qubit variational circuit with multi-head attention and classical CNN for thermal breast cancer classification (arXiv: 2604.16953)
  - Multi-head attention selects discriminative features before quantum encoding
  - Strongly entangling layers with RY rotations and CNOT chains for maximum expressivity
  - **Activation**: HQNN breast cancer, quantum thermographic, hybrid quantum CNN, parameterized quantum circuit medical, thermal image quantum

### Quantum Kernel Advantage over Classical Collapse in Medical Foundation Model Embeddings
- [[quantum-kernel-medical-embeddings]] - Two-tier fair comparison framework; QSVM wins F1 in all 18 configs vs classical collapse on MIMIC-CXR (arXiv: related)
  - Classical linear kernel collapses to majority-class prediction on 90-100% of seeds; QSVM maintains non-trivial recall
  - Quantum kernel effective rank reaches 69.80 at q=11 vs linear kernel collapse
  - **Activation**: quantum kernel medical, QSVM medical imaging, quantum advantage evaluation, classical collapse

## 2026-05-20 - Neuroscience Research (Cron Job)

### Standalone Skill Sync Batch
- [[spiker-ll-fpga-snn-accelerator]] - FPGA accelerator for adaptive local learning in SNNs without BPTT, enabling on-device edge training (arXiv: 2605.18351)
  - Core: Three-factor local learning rule with pre-synaptic, post-synaptic, and modulatory factors
  - Core: Event-driven processing with fixed-point arithmetic for minimal FPGA resource usage
  - **Activation**: FPGA SNN local learning, adaptive local learning, on-device spiking training, three-factor learning
- [[qlif-cast-quantum-spiking-forecasting]] - Quantum Leaky-Integrate-and-Fire for time-series weather forecasting with hybrid quantum-classical recurrent architecture (arXiv: 2605.18333)
  - Core: Qubit superposition neuron excitation states with Rx rotation gates and T1 decay
  - Core: 15.4% lower MSE than classical LIF, 94% faster convergence than QLSTM
  - **Activation**: quantum spiking neural network, quantum LIF, time-series forecasting, weather prediction
- [[spike-forecast-behavioral-decoding]] - Implicit behavioral decoding from next-step spike forecasts using Mamba forecaster for closed-loop BCI (arXiv: related)
  - Core: Single spike forecaster enables both prediction and implicit behavioral readout
  - **Activation**: spike forecasting, behavioral decoding, Mamba forecaster, closed-loop BCI
- [[quantum-feature-amplification-network]] - Quantum Feature Amplification Network for hybrid quantum-classical ML feature enhancement
  - Core: Quantum circuit-based feature amplification in hybrid architectures
  - **Activation**: quantum feature amplification, quantum-classical hybrid, ML feature enhancement
- [[quantum-feature-amplification]] - Quantum feature amplification methodology for quantum machine learning
  - **Activation**: quantum feature amplification, QML
- [[spike-forecast-behavioral]] - Implicit behavioral decoding from next-step spike forecasts (arXiv: related)
  - **Activation**: spike forecast, behavioral decoding

### Papers Analyzed (already covered)
- MIRAGE: fMRI-to-image mental imagery → `mirage-fmri-mental-imagery-decoding` (arXiv: 2605.17198)
- Geometric Phase Transition hippocampal memory → `geometric-phase-transition-hippocampal-memory` (arXiv: 2605.17199)
- VENCircuit VENs social skill SNN → `ven-circuit-snn-social-learning` (arXiv: 2605.17399)
- Functional Whole-Brain Models → `functional-whole-brain-models` (arXiv: 2605.18118)
- Selective Alignment KD SNN → `sealkd-snn-knowledge-distillation` (arXiv: 2605.14252)

## 2026-05-19 - Computer Science + Quantum (Cron Job)

### QuantFPFlow: Quantum Amplitude Estimation for Fokker-Planck Policy Optimisation in Continuous RL
- [[quantum-amplitude-estimation-rl]] - Quantum amplitude estimation for RL achieving O(1/ε) quadratic speedup over classical O(1/ε²) (arXiv: 2605.16429)
  - Grover-amplified amplitude estimator for partition function estimation
  - Exploration bonus R_aug = R_env + α·log(1/ρ*(s)) for multimodal landscapes
  - Quantum-inspired classical simulation exhibits same algorithmic structure
  - **Activation**: quantum amplitude estimation, QuantFPFlow, Fokker-Planck RL, Grover amplification

### Byzantine-Resilient Federated Learning via QUBO-Based Client Selection on Quantum Annealers
- [[qubo-federated-learning-security]] - QUBO-based client selection outperforms MultiKrum on advanced Byzantine attacks (arXiv: 2605.16438)
  - Joint QUBO optimization over all client subsets vs greedy MultiKrum scoring
  - 95.11% vs 81.33% accuracy on Advanced LIE attack (MNIST)
  - Quantum annealer solves pairwise distance encoding for honest client detection
  - **Activation**: QUBO federated learning, Byzantine-resilient FL, quantum annealer security

### QuChaTeR: A Hybrid Quantum-Chaotic Temporal Framework for Earthquake Prediction
- [[quantum-chaotic-temporal-forecasting]] - Hybrid quantum-chaotic architecture combining wavelet, chaotic maps, and VQC for time series (arXiv: 2605.16454)
  - Wavelet decomposition + chaotic maps + variational quantum circuits
  - Outperforms LSTM/GRU/RNN/Reservoir on real-world seismic datasets
  - Faster convergence with richer quantum state representations
  - **Activation**: quantum chaotic forecasting, QuChaTeR, VQC time series, PennyLane

### LoopQ: Quantization for Recursive Transformers
- [[loop-aware-transformer-quantization]] - Loop-aware PTQ framework for recursive/looped Transformer models (arXiv: 2605.16343)
  - Addresses distribution shift across loop roles and recursive error accumulation
  - Combines activation scaling, cross-loop state alignment, trajectory-aware optimization
  - First systematic study of quantization in looped language models
  - **Activation**: LoopQ quantization, recursive transformer PTQ, looped model compression

### Forecasting Medium-Horizon Alzheimer Disease Progression: Residual Gap-Aware Transformers
- [[residual-gap-aware-transformer-medical]] - Residual gap-aware transformer for 24-month CDR-SB change prediction from irregular biomarker histories (arXiv: 2605.16319)
  - Anchor-based prediction using only data available at MCI visit
  - Predicts residual changes vs absolute scores to avoid baseline confounding
  - Handles irregular biomarker observation patterns in longitudinal data
  - **Activation**: residual gap prediction, Alzheimer prognosis, CDR-SB forecasting, ADNI


## 2026-05-19 - Neuroscience Research (Cron Job)
## 2026-05-19 - Computer Science + Quantum (Cron Job)

### AgentWall: A Runtime Safety Layer for Local AI Agents
- [[agent-safety-layer]] - Runtime safety interception layer for local AI agents with declarative policy enforcement (arXiv: 2605.16265)
  - Intercept agent actions before execution with policy evaluation
  - 92.9% enforcement accuracy with sub-millisecond overhead
  - **Activation**: agent safety, runtime guardrails, action interception, policy enforcement, AI agent security

### ANNEAL: Adapting LLM Agents via Governed Symbolic Patch Learning
- [[governed-symbolic-patch]] - Neuro-symbolic methodology for persistent fault elimination via knowledge graph repair (arXiv: 2605.16309)
  - Failure-Driven Knowledge Acquisition (FDKA) localizes and patches recurring faults
  - Reduces recurring failure rates to 0% vs 72-100% for baselines
  - **Activation**: self-evolving agents, knowledge graph repair, persistent faults, symbolic patching, FDKA

### ACE + TDDev: Adversarial Test-Driven Development
- [[adversarial-test-driven-dev]] - Self-evolving code generation combining adversarial testing with TDD (arXiv: 2605.16299, 2605.17242)
  - Solver-adversary architecture discovers failures without ground-truth code
  - TDD improves web app generation quality by 34-48 percentage points
  - **Activation**: adversarial testing, self-evolving code, test-driven development, code generation, web app generation


### Von Economo neurons enable reliable social skill acquisition in recurrent spiking neural networks
- [[vencircuit-ven-gradient-scaffold]] - VENs as residual gradient pathway scaffolds in recurrent SNNs, providing immune gradient flow for reliable learning (arXiv: 2605.17399)
  - VEN-intact networks converge 98% vs VEN-ablated 70% — complete absence of learning in failures, not just slower
  - VENs provide direct gradient pathway structurally immune to Jacobian product instabilities in BPTT
  - Clinical predictions: bvFTD → learning failure, ASC → stochastic variable social skill acquisition
  - **Activation**: Von Economo, VEN, gradient scaffold, VENCircuit, social learning SNN, bvFTD, residual SNN

### Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity
- [[geometric-phase-transition-hippocampal-memory]] - Discrete phase transition from "mist" to "crystalline" population geometry enables >100x memory capacity (arXiv: 2605.17199)
  - Caching chickadees show crystalline geometry (Shesha: 0.245 vs 0.166) with 2x temporal coherence
  - Crystalline codes sustain M>1000 locations while mist codes fail below M=10, validated across 10k configs
  - E-I synergy: excitatory neurons form spatial scaffold, inhibitory provides orthogonal decorrelation
  - **Activation**: hippocampal memory, population geometry, crystalline coding, Shesha metric, memory scaling

## 2026-05-19 - Neuroscience Research (Cron Job 10PM)

### MIRAGE: Robust Multi-Modal fMRI-to-Mental-Image Decoding
- [[mirage-fmri-mental-imagery-decoding]] - Linear backbone + multi-modal features + diffusion model achieves SOTA mental image reconstruction from fMRI, showing seen-image performance ≠ mental-image generalization (arXiv: 2605.17198)
  - 核心要点 1: SOTA visual decoder performance does NOT guarantee mental imagery generalization — architecture must be explicitly designed for cross-decoding
  - 核心要点 2: Low-dimensional image features + text guidance + high+low-level features required for optimal mental image reconstruction
  - 核心要点 3: Simple linear backbone outperforms complex nonlinear encoders for cross-decoding from perception to imagination
  - **Activation**: MIRAGE, fMRI mental imagery, brain-to-image decoding, NSD-Imagery, vision decoder generalization

### Self-Supervised Local Learning for Hierarchical Structure Discovery
- [[self-supervised-local-learning-hierarchy]] - Layerwise self-supervised contrastive/non-contrastive learning matches backprop data efficiency on Random Hierarchy Model, while direct-feedback methods fail (arXiv: 2605.18557)
  - 核心要点 1: Direct feedback methods fail on hierarchical tasks due to missing input-specific nonlinearities (masking) essential for complex learning
  - 核心要点 2: Layerwise self-supervised learning (contrastive AND non-contrastive) succeeds — data-efficient as backprop, compatible with cortical plasticity
  - 核心要点 3: Brain likely uses self-supervised objectives rather than approximate backprop for learning abstract hierarchical representations
  - **Activation**: self-supervised local learning, biological plasticity, Random Hierarchy Model, Gerstner, contrastive learning, hierarchical structure learning

## 2026-05-19 - Computer Science + Quantum Mechanics (Cron Job 8PM)

### Hybrid Quantum-Classical Neural Architecture Search
- [[hqnn-neural-architecture-search]] - NAS methodology for designing HQNNs with hardware-aware FLOPs-constrained search (arXiv: 2605.18345)
  - 核心要点 1: HQNN architecture design via NAS — encoding strategies, PQC structures, measurement design, classical-quantum coupling
  - 核心要点 2: FLOPs-aware search optimizes accuracy vs computational cost for NISQ deployment
  - **Activation**: HQNN architecture search, quantum NAS, hybrid quantum NAS, FLOPs-aware quantum search, neural architecture search quantum

## 2026-05-19 - Computer Science + Quantum Mechanics (Cron Job 7PM)

### RL-CQE: Reinforcement Learning Contracted Quantum Eigensolver for Excited States
- [[rl-quantum-eigensolver]] - Deep Q-network agent adaptively selects two-body operators for compact excited state ansätze (arXiv: 2605.18569)
  - 核心要点 1: RL agent selects operators at each CQE iteration, extending ground-state method to excited states and real-time dynamics
  - 核心要点 2: Orthogonality constraints enforced via penalty terms; McLachlan variational principle for time evolution
  - **Activation**: RL quantum eigensolver, contracted quantum eigensolver, excited state quantum, quantum dynamics RL

### Entropy-Governed Quantum Algorithm Speedup for Local Hamiltonians
- [[entropy-quantum-algorithm-speedup]] - Breaks Grover bound O(2^{n/2}) achieving O(2^{n/2-d}) for k-local Hamiltonian energy estimation (arXiv: 2605.18241)
  - 核心要点: Uses depth-d local quantum states with entropy constraint to achieve faster-than-Grover energy estimation and state preparation
  - **Activation**: entropy quantum algorithm, Grover speedup improvement, local Hamiltonian algorithm, quantum energy estimation

### Adaptive Clifford+T Decomposition of Multi-Controlled Toffoli Gates
- [[adaptive-clifford-toffoli-decomposition]] - Optimized decomposition of n-controlled Toffoli gates using one clean ancilla with reduced T-count/T-depth (arXiv: 2605.18169)
  - 核心要点 1: Single clean ancilla + relative-phase Toffoli gates reduce T-cost significantly
  - 核心要点 2: Dynamic circuit techniques with mid-circuit measurement and feed-forward optimization
  - **Activation**: Clifford T decomposition, Toffoli gate optimization, quantum gate synthesis, T-count reduction

     1|## 2026-05-19 - Neuroscience Research (Cron Job)
     2|
     3|### Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function
     4|- [[functional-whole-brain-models]] - Unified modeling paradigm bridging bottom-up whole-brain modeling and top-down neuroconnectionism with four minimal criteria (arXiv: 2605.18118)
     5|  - 核心要点 1: fWBMs defined by four criteria: structural grounding, dynamical realism, functional competence, mappable observables
     6|  - 核心要点 2: Three-pillar roadmap: short-term (differentiable WBM), mid-term (cross-modal validation), long-term (clinical translation)
     7|  - **Activation**: functional whole-brain model, fWBM, whole-brain modeling, neuroconnectionism
     8|
     9|### Spiker-LL: An Energy-Efficient FPGA Accelerator Enabling Adaptive Local Learning in SNNs
    10|- [[spiker-ll-fpga-snn-accelerator]] - FPGA-based SNN accelerator with on-device STSF local learning, DSP-free, sub-ms latency (arXiv: 2605.18003)
    11|  - 核心要点 1: Extends Spiker+ inference architecture with STSF local learning rule for supervised training without BPTT
    12|  - 核心要点 2: 92-93% accuracy on MNIST/F-MNIST/DIGITS, <0.1mJ per inference, scales from <5k LUTs to larger networks
    13|  - **Activation**: FPGA SNN accelerator, spiker-ll, on-device learning, STSF, edge neuromorphic
    14|
    15|## 2026-05-19 - Computer Science + Quantum Mechanics (Cron Job)
    16|
    17|### QLIF-CAST: Quantum Leaky-Integrate-and-Fire for Time-Series Weather Forecasting
    18|- [[hybrid-quantum-time-series-forecasting]] - Hybrid quantum-classical neural architecture for time-series forecasting using QLIF spiking neurons (arXiv: 2605.18333, 2605.18345)
    19|  - 核心要点 1: QLIF neuron encodes membrane potential as single-qubit superpositions via Rx rotation gates and T1 relaxation decay, achieving 15.4% lower MSE vs classical LIF
    20|  - 核心要点 2: Hybrid quantum-classical recurrent architecture combines classical preprocessing with quantum recurrent layers for multivariate time-series prediction
    21|  - **Activation**: quantum time series, QLIF, quantum spiking neural network, hybrid quantum-classical, quantum recurrent, quantum machine learning forecasting
    22|
    23|## 2026-05-19 - Computer Science + Quantum Mechanics (Cron Job 4PM)
    24|
    25|### Noise-Aware Quantum Program Testing
    26|- [[noise-aware-quantum-testing]] - Mutation testing methodology that evaluates quantum program robustness under realistic hardware noise, extending mutation analysis beyond noiseless simulators (arXiv: 2605.13279)
    27|  - 核心要点: Noise can mask up to 40% of detectable mutants — tests passing on simulators may fail on real NISQ devices
    28|  - 核心要点: Four noise models (depolarizing, amplitude damping, phase damping, readout error) integrated into mutation testing workflow
    29|  - **Activation**: noise-aware quantum testing, quantum mutation testing under noise, robust quantum testing, NISQ quantum testing, quantum software testing noise
    30|
    31|### Quantum Software Architecture Framework (QSAF)
    32|- [[quantum-software-architecture-framework]] - Component-based framework for designing hybrid quantum-classical systems with separation of concerns, reusability, and engineering rigor (arXiv: 2605.01800)
    33|  - 核心要点: Three-layer architecture (quantum algorithm, hybrid interface, classical processing) with standardized component interfaces
    34|  - 核心要点: Design patterns for VQE/QAOA loops, QML training, and quantum subroutines with anti-patterns for monolithic programs
    35|  - **Activation**: quantum software architecture, QSAF, hybrid quantum-classical architecture, quantum component design, quantum system design
    36|
    37|## 2026-05-19 - Neuroscience Research (Cron Job)
    38|
    39|### Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity
    40|- [[geometric-phase-transition-hippocampal-memory]] - 高容量空间记忆源于海马群体几何的离散硬化相变：从无序"雾"到"晶体"编码 (arXiv: 2605.17199)
    41|  - 核心要点 1: 晶体编码通过拓扑刚性实现 M=1,000+ 地点记忆，雾编码在 M=10 以下失效（>100倍容量优势）
    42|  - 核心要点 2: E/I 协同机制 — 兴奋性神经元构建空间支架，抑制性神经元正交去相关，占据非重叠表示子空间
    43|  - 核心要点 3: "几何税"概念 — 169倍表示冗余维持流形稳定性，对抗生物噪声
    44|  - 核心要点 4: 与 Valiant 稳定记忆分配器的双重分离，确认优势来自连续拓扑组织而非离散神经元分配
    45|  - **Activation**: geometric phase transition, hippocampal memory, crystalline code, population geometry, Shesha metric, geometric stability, geometric tax
    46|
    47|### Spiker-LL: An Energy-Efficient FPGA Accelerator Enabling Adaptive Local Learning in SNNs
    48|- [[spiker-ll-fpga-snn-accelerator]] - 基于 FPGA 的 SNN 加速器，通过 STSF 局部学习规则实现片上训练，无需 DSP 且能耗 <0.1mJ (arXiv: 2605.18003)
    49|  - 核心要点 1: STSF (Spiking Time Sparse Feedback) 局部学习 — 使用随机反馈对齐+脉冲触发局部可塑性，无需 BPTT 和资格迹
    50|  - 核心要点 2: 最小化微架构扩展 — 仅在突触状态访问点添加训练支持，复用现有数据路径和控制逻辑
    51|  - 核心要点 3: MNIST/F-MNIST/DIGITS 上 92-93% 准确率，亚毫秒延迟，<0.1mJ 每推理，完全无 DSP
    52|  - **Activation**: Spiker-LL, SNN FPGA accelerator, on-device learning, STSF learning rule, DSP-free neuromorphic hardware, edge intelligence
    53|
    54|## 2026-05-19 - Computer Science + Quantum Mechanics (Cron Job 3PM)
    55|
    56|### Quantum Feature Amplification Network (QFAN)
    57|- [[quantum-feature-amplification-network]] - Autoregressive quantum generative model that removes register-size bottleneck by generating images as block sequences with reused small quantum circuits (arXiv: 2605.16044)
    58|  - 核心要点: autoregressive quantum generation, block-based image synthesis, fixed qubit budget, 3-qubit circuit with 12 shared params
    59|  - 核心要点: shot-noise propagation bound, empirical decoder-capacity heuristic, hardware verified on IBM QPU
    60|  - **Activation**: quantum feature amplification, QFAN, autoregressive quantum generation, quantum generative model blocks, qubit-efficient quantum generative
    61|
    62|### Algorithmic Advantage on Gate-Based Photonic QNN
    63|- [[photonic-qnn-algorithmic-advantage]] - Gate-based photonic QNN achieves 100% accuracy on XOR with just 2 trainable parameters, solving tasks requiring 4x+ classical parameters (arXiv: 2605.10801)
    64|  - 核心要点: effective dimension as capacity measure, proven generalization-error bound, parameter-matched QNN vs ANN comparison
    65|  - 核心要点: gradient-free optimization on real 6-qubit photonic processor, robustness to photon loss and phase-shifter noise
    66|  - **Activation**: photonic quantum neural network, algorithmic advantage QNN, effective dimension quantum, gate-based photonic QNN, gradient-free quantum training
    67|
    68|### Quantum-Inspired Lottery Tickets
    69|- [[quantum-inspired-lottery-tickets]] - Quantum-inspired classical algorithm for finding winning lottery tickets in neural networks via sparse subnetwork selection (arXiv: 2605.13979)
    70|  - 核心要点: quantum-inspired classical algorithm avoids quantum hardware requirement, efficient sparse subnetwork selection
    71|  - 核心要点: bridges QML with practical classical network compression
    72|  - **Activation**: quantum-inspired lottery tickets, winning lottery tickets, sparse subnetwork selection, quantum-inspired classical algorithm, neural network pruning
    73|## 2026-05-19 - Neuroscience Research (Cron Job)
    74|
    75|### NERVE: Network-Aware Bilinear Tokenization for Brain Functional Connectivity Representation Learning
    76|- [[nerve-fc-bilinear-tokenization]] - Self-supervised FC representation learning via structured bilinear factorization that aligns tokenization with brain network organization, outperforming agnostic MAE baselines on cross-cohort prediction (arXiv: 2605.14048)
    77|  - 核心要点: 网络感知块划分将FC矩阵按脑网络对内/块间连接分区,通过结构双线性分解嵌入异构块,参数复杂度从二次降为线性
    78|  - 核心要点: 在ABCD/PNC/CCNP三个发育队列上验证,跨队列迁移能力显著优于结构无关MAE和图自监督基线
    79|  - **Activation**: NERVE tokenization, brain FC representation, functional connectivity MAE, bilinear factorization brain, network-aware brain ML, rs-fMRI deep learning
    80|
    81|### MTC-SN: Multi-Timescale Conductance Spiking Networks
    82|- [[mtc-spiking-networks]] - Gradient-trainable SNN framework using fast/slow/ultra-slow conductances to shape I-V curves, enabling exact BPTT without surrogate gradients and richer firing dynamics (arXiv: 2605.11835)
    83|  - 核心要点: 多时间尺度电导(快/慢/超慢)塑造I-V曲线,在单一模型内实现tonic/phasic/bursting等多种发放模式
    84|  - 核心要点: 离散化可微动力学公式实现精确BPTT,在Mackey-Glass时间序列回归上超越LIF和AdLIF且稀疏度更高
    85|  - **Activation**: multi-timescale conductance, MTC-SN, conductance-based SNN, gradient-trainable spiking, temporal regression SNN, neuromorphic regression
    86|
    87|## 2026-05-19 - Computer Science (Cron Job)
    88|
    89|### QLIF-CAST: Quantum Leaky-Integrate-and-Fire for Time-Series Weather Forecasting
    90|- [[qlif-cast-quantum-spiking-forecasting]] - Quantum Leaky-Integrate-and-Fire spiking neural network for time-series regression, achieving 15.4% lower MSE than classical LIF (arXiv: 2605.18333)
    91|  - 核心要点: QLIF, quantum spiking, time-series forecasting, hybrid quantum-classical
    92|
    93|### Diagonal Adaptive Non-local Observables on Quantum Neural Networks
    94|- [[diagonal-adaptive-non-local-observables]] - Dynamic observable methodology expanding VQA function space with efficient diagonal approximation (arXiv: 2605.15410)
    95|  - 核心要点: adaptive observables, VQA expressivity, quantum neural networks, diagonal ANO
    96|
    97|
    98|### SPIKER-LL: An Energy-Efficient FPGA Accelerator Enabling Adaptive Local Learning in SNNs
    99|- [[spiker-ll-snn-accelerator]] - FPGA-accelerated SNN with STSF local learning rule, DSP-free, sub-ms latency, <0.1 mJ per inference (arXiv: 2605.18003)
   100|  - Extends Spiker+ inference architecture with STSF (Spike-Timing-Specific-Feedback) local learning for on-device training
   101|  - DSP-free implementation using only LUT/FF/BRAM, achieving 93% accuracy on MNIST/F-MNIST/DIGITS
   102|  - **Activation**: spiker-ll, FPGA SNN accelerator, adaptive local learning SNN, STSF learning rule, edge FPGA SNN, on-device SNN training
   103|
   104|## 2026-05-19 - Computer Science + Quantum Mechanics (Cron Job 1PM)
   105|
   106|### Non-Gaussian Entanglement Hierarchy Based on the Schmidt Number
   107|- [[non-gaussian-entanglement-hierarchy]] - Rigorous hierarchy for classifying continuous-variable entanglement via Schmidt number, providing computable bounds and operational criteria for entanglement detection beyond Gaussian operations (arXiv: 2605.18605)
   108|  - Schmidt number SN(ρ) classifies states: separable (1), k-dimensional entanglement (k), infinite-dimensional (CV limit)
   109|  - Lower/upper bounds via entanglement witnesses and non-Gaussianity measures
   110|  - Operational bound: distillable key rate R ≤ log₂(SN(ρ))
   111|  - **Activation**: non-Gaussian entanglement, Schmidt number hierarchy, continuous-variable entanglement, quantum entanglement bounds, CV quantum systems
   112|
   113|### Bounds on Quantum Conference Key Agreement in Pair-Entangled Networks
   114|- New paper establishing fundamental limits on multipartite quantum key rates from bipartite resources (arXiv: 2605.18399)
   115|  - Proves limitations on conference key rates when parties share only pairwise entanglement
   116|  - Connects quantum network topology with achievable secure communication rates
   117|  - **Activation**: quantum conference key, pair-entangled networks, multipartite QKD, quantum network bounds
   118|
   119|### Topologically Protected Long-Range Correlations in Driven-Dissipative Bosonic Chains
   120|- Demonstrates topological protection of correlations in non-Hermitian quantum many-body steady states (arXiv: 2605.18394)
   121|  - Connects non-Hermitian topology with quantum many-body physics in open systems
   122|  - Long-range correlations robust against local perturbations via topological invariants
   123|  - **Activation**: topological protection, bosonic chains, non-Hermitian topology, driven-dissipative systems, quantum correlations
   124|
   125|## 2026-05-19 - Computer Science + Quantum Mechanics (Cron Job 12PM)
   126|
   127|### ACE: Self-Evolving LLM Coding Framework via Adversarial Unit Test Generation
   128|- [[adversarial-testing-framework]] - Self-evolving code generation using solver-adversary architecture with execution-level supervision, no ground-truth or reward models needed; SFT + KTO joint optimization (arXiv: 2605.16299)
   129|  - Solver generates code, adversary generates adversarial tests inducing runtime failures
   130|  - Execution boolean table discriminates code quality, top fraction selected for SFT
   131|  - KTO with length penalty optimizes adversary; converges in 4-5 rounds with 3-7% pass@1 gains
   132|  - **Activation**: adversarial testing, solver-adversary, self-evolving coding, ACE framework, execution-based supervision, preference optimization, KTO training, fuzzing LLM, robust code generation
   133|
   134|### Lean-QEC: End-to-End Formalization of Quantum Error Correction
   135|- [[quantum-error-formal-verification]] - First Lean 4 formalization of stabilizer-code theory delivering machine-checked distance certificates for qLDPC codes up to 144 qubits via verified SAT reduction (arXiv: 2605.16523)
   136|  - Distance condition → Boolean satisfiability via verified reduction with BitVec-flattened encoding
   137|  - Error-location encoding reduces variables: n → k·⌈log₂n⌉, scaling to industrial code sizes
   138|  - Covers CSS and Bivariate Bicycle code families (J90,8,10K, J70,6,9K BB codes)
   139|  - **Activation**: quantum error correction formalization, Lean QEC, stabilizer code verification, distance certificate, qLDPC formal proof, machine-checked quantum proof, formal quantum verification
   140|
   141|### Quokka#: Quantum Computing with #SAT
   142|- [[quantum-circuit-sat-analysis]] - Reduces quantum circuit simulation, verification, equivalence checking, and synthesis to weighted model counting (#SAT) with complex-valued weights (arXiv: 2605.16509)
   143|  - Four engines: simulation, Hoare logic verification, exact/approximate equivalence, depth-optimal synthesis
   144|  - Computational-basis and Pauli-basis encodings with complex weight support
   145|  - Depth-optimal synthesis via Max#SAT enabling arbitrary gate set translation
   146|  - **Activation**: quantum circuit SAT, weighted model counting quantum, Quokka#, quantum circuit verification, quantum equivalence checking, quantum circuit synthesis #SAT
   147|
   148|## 2026-05-19 - Neuroscience Research (Cron Job 1PM)
   149|
   150|### VENCircuit: Von Economo Neurons as Acquisition Scaffolds in Recurrent SNNs
   151|- [[ven-circuit-snn-social-learning]] - VENs function as gradient pathway bypass ensuring reliable training convergence (98% vs 70%), with clinical predictions for bvFTD and ASC (arXiv: 2605.17399)
   152|  - VEN-intact networks converge 49/50 (98%) vs ablated 35/50 (70%); failed networks show complete absence of learning
   153|  - Phase-ablation reveals critical window (epochs 5-25) when co-adaptive dependency forms
   154|  - Formal account: VENs provide direct gradient pathway immune to recurrent Jacobian instabilities
   155|  - **Activation**: Von Economo neurons, VEN, VENCircuit, social skill acquisition, recurrent SNN, gradient pathway, acquisition scaffold, bvFTD, autism spectrum condition, stochastic learning failure
   156|
   157|## 2026-05-19 - Neuroscience Research (Cron Job 12PM)
   158|
   159|### Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity
   160|- [[geometric-phase-transition-hippocampal-memory]] - Memory capacity via neural population geometry phase transition (crystalline vs mist codes), Shesha metric, and 169-fold geometric tax for manifold stability (arXiv: 2605.17199)
   161|  - Shesha metric: geometric stability (0.245 crystalline vs 0.166 mist) and temporal coherence
   162|  - E/I subspace segregation: excitatory scaffold + inhibitory decorrelation in orthogonal subspaces
   163|  - Double dissociation with Valiant's SMA: advantage from continuous topology, not discrete allocation
   164|  - **Activation**: geometric phase transition, hippocampal memory, Shesha metric, crystalline geometry, neural code stability, spatial memory capacity, geometric tax
   165|
   166|## 2026-05-19 - Computer Science + Quantum (Cron Job 11AM)
   167|
   168|### Hybrid Quantum-Classical Neural Architecture Search
   169|- [[hqnn-neural-architecture-search]] - Systematic NAS for HQNN design combining parameterized quantum circuits with classical neural networks, with FLOPs-aware optimization balancing accuracy and computational efficiency for NISQ-era deployment (arXiv: 2605.18345)
   170|  - Defines HQNN search space: encoding, circuit structure, measurement, classical coupling
   171|  - FLOPs-aware search as proxy for computational complexity
   172|  - Hardware-constrained architecture optimization for practical deployment
   173|  - **Activation**: hybrid quantum NAS, HQNN architecture search, quantum neural architecture, FLOPs-aware quantum, hardware-aware QML
   174|
   175|### Discovering Data Encoding Strategies for Quantum-Classical Neural Networks Using Monte Carlo Tree Search
   176|- [[mcts-quantum-encoding-discovery]] - Uses MCTS to automatically discover optimal data encoding circuits for quantum-classical CNNs, with effective rank analysis as performance predictor to accelerate search (arXiv: 2605.18540)
   177|  - MCTS discovers encoding circuits that outperform common strategies on medical imaging datasets
   178|  - Effective rank of feature maps correlates with encoding performance — usable as threshold criterion
   179|  - Entanglement capability and Fourier decomposition provide minimal predictive insight
   180|  - **Activation**: quantum encoding discovery, MCTS encoding search, quantum data embedding, effective rank encoding
   181|
   182|### Geometric Prototype Learning in Quantum Hilbert Space with Matrix Product States
   183|- [[quantum-hilbert-prototype-learning]] - Prototype-based learning with class representatives as generative MPS in quantum Hilbert space, enabling classification/clustering via geometric quantum state measures (arXiv: 2605.17895)
   184|  - Lifts prototype learning from classical feature space to quantum Hilbert space
   185|  - Identifies quantum "attraction" effect from coherent superposition of assigned states
   186|  - Prototype-based dimensionality reduction from 2^n to k (number of classes)
   187|  - Outperforms classical prototype approaches on Fashion-MNIST and ECG datasets
   188|  - **Activation**: quantum prototype learning, quantum Hilbert space learning, MPS classification, quantum geometric learning
   189|
   190|## 2026-05-19 - Neuroscience Research (Cron Job 11AM)
   191|
   192|### Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function
   193|- [[functional-whole-brain-models-fwbm]] - Proposes fWBMs as a unified paradigm bridging bottom-up whole-brain modeling and top-down neuroconnectionism, requiring structural grounding, dynamical realism, functional competence, and mappable observables (arXiv: 2605.18118)
   194|  - Unifies biophysically realistic brain models with task-performing neural networks
   195|  - Establishes four minimal criteria and a three-pillar roadmap for integration
   196|  - Opens pathways for virtual patient models and cross-scale neuroscience hypotheses
   197|  - **Activation**: functional whole-brain model, fWBM, whole-brain modeling, neuroconnectionism, brain structure function integration
   198|
   199|### Not All Timesteps Matter Equally: Selective Alignment Knowledge Distillation for Spiking Neural Networks
   200|- [[selective-alignment-knowledge-distillation-snn]] - SeAl-KD selectively aligns temporal knowledge in SNNs by equalizing competing logits at erroneous timesteps and reweighting temporal alignment based on confidence, improving over uniform KD (arXiv: 2605.14252)
   201|  - Recognizes SNN predictions evolve over time — not all timesteps need equal supervision
   202|  - Two-part method: logit equalization for errors + confidence-weighted temporal alignment
   203|  - Validated on static image and neuromorphic event-based datasets
   204|  - **Activation**: SNN knowledge distillation, selective alignment KD, SeAl-KD, temporal alignment SNN
   205|
   206|## 2026-05-19 - Computer Science + Quantum (Cron Job 11AM)
   207|
   208|### Beyond Commutativity: Redesigning Trotter Decomposition via Local Symmetry
   209|- [[trotter-local-symmetry]] - Local symmetry-based Trotter decomposition for quantum simulation using operators that commute with Hamiltonian subsets, enabling improved partitioning beyond commutativity methods (arXiv: 2605.16016)
   210|  - Local symmetries reveal hidden structure enabling larger Hamiltonian blocks
   211|  - Fewer Trotter steps → shallower circuits for fixed accuracy
   212|  - Applicable to condensed matter and quantum chemistry Hamiltonians
   213|  - **Activation**: local symmetry Trotter, Hamiltonian partitioning, quantum simulation decomposition
   214|
   215|### Encoding Circuit Synthesis for Fault-Tolerant Quantum Computation
   216|- [[ftqc-encoding-circuit-synthesis]] - Systematic encoding circuit synthesis for preparing arbitrary logical states in QECCs, optimizing two-qubit gate count and circuit depth for FTQC (arXiv: 2605.15266)
   217|  - Uses stabilizer structure and Gaussian elimination for circuit construction
   218|  - Focuses on dominant resource costs: two-qubit gates and depth
   219|  - Applicable to surface codes, color codes, and LDPC codes
   220|  - **Activation**: encoding circuit synthesis, fault-tolerant state preparation, logical state encoding
   221|
   222|## 2026-05-19 - Computer Science + Quantum (Cron Job 10AM)
   223|
   224|### Diagonal Adaptive Non-local Observables on Quantum Neural Networks
   225|- [[diagonal-ano-qnn]] - Reduces k-local quantum observable complexity from O(4^k) to O(2^k) using diagonal observables, preserving full ANO expressivity via unitary similarity equivalence (arXiv: 2605.15410)
   226|  - Diagonal matrices are canonical representatives of ANO space modulo unitary similarity
   227|  - Enables joint optimization of circuit parameters and observable eigenvalues
   228|  - Conventional VQCs with Pauli-Z measurements are a subset of diagonal ANO
   229|  - **Activation**: diagonal ANO, adaptive observables, quantum neural network observables, VQA measurement optimization
   230|
   231|### Measurement-Efficient VQLS for Carleman-Linearized Nonlinear Dynamics
   232|- [[carleman-vqls]] - Hybrid quantum-classical pipeline combining Carleman linearization with VQLS to solve nonlinear differential equations, tested on IBM and Xanadu platforms (arXiv: 2605.15366)
   233|  - Carleman linearization converts weakly nonlinear ODEs to high-dimensional linear systems
   234|  - Symmetry-grouped Hadamard Tests reduce measurement overhead
   235|  - Local cost formulations more resilient to barren plateaus than global costs
   236|  - **Activation**: Carleman linearization, VQLS nonlinear equations, quantum differential equation solver
   237|
   238|### Controllable Quantum Memory Capacity in Quantum Reservoir Networks
   239|- [[quantum-reservoir-memory]] - Unified QRC framework using tunable partial-SWAP gates to interpolate between feedback and recurrent architectures, providing single hyperparameter for memory control (arXiv: 2605.12713)
   240|  - partial-SWAP parameter θ controls memory capacity: θ=0 (feedback limit), θ=π/2 (recurrent limit)
   241|  - Trade-off between quantum memory capacity and processing speed
   242|  - Echo state property validation essential for reservoir stability
   243|  - **Activation**: quantum reservoir computing, quantum memory capacity, partial-SWAP QRC, temporal quantum ML
   244|
   245|
   246|## 2026-05-19 - Neuroscience Research (Cron Job)
   247|
   248|### Thermodynamic Networks: Harnessing Non-Equilibrium Steady States for Computation
   249|- [[thermodynamic-networks-computation]] - Autonomous physics-based computation using non-equilibrium steady states, with NDC as the expressivity switch (arXiv: 2605.15985)
   250|  - Identifies Negative Differential Conductance (NDC) as the critical property for universal function approximation in thermodynamic networks
   251|  - Demonstrated on quantum dot networks and enzymatic reaction networks, training via natural equilibration
   252|  - **Activation**: thermodynamic networks, non-equilibrium computation, NDC, steady-state computing, physics-based computation
   253|
   254|## 2026-05-19 - Computer Science + Quantum Computing (Cron Job)
   255|
   256|### Quantum Solvers for Nonlinear Matrix Equations in Quantum Chemistry
   257|- [[quantum-riccati-solver]] - Quantum algorithm for algebraic Riccati equations via Riesz projectors and QSVT, enabling linear-scaling RPA and coupled-cluster computations (arXiv: 2605.16189)
   258|  - Block-encodes Riccati solutions as Riesz projectors onto invariant subspaces
   259|  - Contour-integral resolvents + QSVT achieve poly(m) scaling in excitation rank
   260|  - Opens route to quantum algorithms for coupled-cluster theory
   261|  - **Activation**: quantum riccati, quantum nonlinear matrix, RPA quantum, algebraic riccati equation, quantum chemistry algorithm
   262|
   263|### Efficient Quantum Algorithm for Linear Matrix Differential Equations
   264|- [[quantum-linear-differential-equation]] - Nearly optimal O~(nu*L*t/epsilon) quantum algorithm for linear matrix ODEs with polynomial-to-exponential speedups for dissipative dynamics (arXiv: 2605.16195)
   265|  - Computes matrix entries directly, avoiding exponential state-amplitude decay
   266|  - Constant query complexity for dissipative dynamics, linear for unitary
   267|  - Proven optimal up to logarithmic factors
   268|  - **Activation**: quantum differential equation, open quantum system, dissipative dynamics, linear matrix ODE quantum, quantum time evolution
   269|
   270|## 2026-05-19 - Neuroscience Research (Cron Job)
   271|
   272|### Scalable neuromorphic computing from autonomous spiking dynamics in a clockless reconfigurable chip
   273|- [[clockless-asynchronous-neuromorphic-computing]] - FPGA-based clockless Boolean spiking networks achieve analog-level energy efficiency without custom ASICs (arXiv: 2605.16114)
   274|  - Clockless (asynchronous) digital circuits enable autonomous time-continuous spiking dynamics
   275|  - Commodity FPGAs with configurable excitatory/inhibitory synapses rival analog neuromorphic power
   276|  - Complete spike-encoding pipeline demonstrated on audio classification
   277|  - **Activation**: clockless SNN, FPGA neuromorphic, asynchronous spiking, autonomous spiking dynamics, reconfigurable neuromorphic chip
   278|
   279|### Mechanistic Interpretability of EEG Foundation Models via Sparse Autoencoders
   280|- [[eeg-foundation-sae-interpretability]] - SAE-based interpretability framework for EEG transformers reveals clinical entanglements and enables concept steering (arXiv: 2605.13930)
   281|  - TopK SAEs extract monosemantic features from SleepFM, REVE, LaBraM across architectures
   282|  - Three operational regimes: selectively steerable, encoded-but-entangled, non-encoded
   283|  - Detects "wrecking-ball" interventions and age-pathology confounding failures
   284|  - Spectral decoder maps latent steering to physiologically interpretable frequency signatures
   285|  - **Activation**: EEG interpretability, sparse autoencoder, concept steering, EEG foundation model, monosemanticity
   286|
   287|## 2026-05-19 - Systems Engineering Research (Cron Job)
   288|
   289|### From Backup Restoration to Minimum Viable Factory Recovery
   290|- [[mvf-recovery-critical-infrastructure]] - Reframes ransomware recovery as interdependency and continuity problem across IT/OT/physical/supply-chain domains (arXiv: 2605.16167)
   291|  - Core contribution: Defines Minimum Viable Factory (MVF) Recovery as the smallest safe, trusted, and operationally meaningful production capability
   292|  - Identifies 9 evidence-backed recovery failure modes: dependency blindness, backup over-trust, identity trust collapse, unsafe OT reconnection, etc.
   293|  - **Activation**: mvf recovery, minimum viable factory, ransomware recovery, critical infrastructure, IT-OT recovery
   294|
   295|### Detecting Privilege Escalation in Polyglot Microservices via Agentic Program Analysis
   296|- [[neo-agentic-program-analysis]] - Combines LLM agents with classic program analysis for cross-service vulnerability detection (arXiv: 2605.15569)
   297|  - Core contribution: Neo framework achieves 81% precision / 85% recall on 25 microservice apps across 7 languages, discovering 24 zero-day vulnerabilities
   298|  - Key technique: Dynamic analysis planning + adaptive code search primitives + semantic validation
   299|  - **Activation**: neo analysis, agentic program analysis, privilege escalation, microservice security, polyglot vulnerability
   300|
   301|
   302|## 2026-05-19 - Computer Science + Quantum Mechanics (Cron Job - Hourly v2)
   303|
   304|### HOPPER: A Hop-by-hop Entanglement Distribution Protocol for Asynchronous Quantum Networks
   305|- [[hopper-entanglement-distribution]] - 异步量子网络中逐跳纠缠分发协议，中间节点自主决策实现多路并行ebit建立，突破串行瓶颈 (arXiv: 2605.15869)
   306|  - 多路并发ebit请求在同一量子路径上同时传输，无需等待前一个完成
   307|  - 中间节点基于本地资源状态自主进行逐跳决策，无需全局同步
   308|  - 在长距离高延迟网络中显著优于同步方案，充分利用多量子比特内存
   309|  - **Activation**: quantum network protocol, entanglement distribution, hop-by-hop, async quantum, HOPPER, quantum internet
   310|
   311|### Thermodynamic Networks: Harnessing Non-Equilibrium Steady States for Computation
   312|- [[thermodynamic-networks-computation]] - 利用非平衡稳态的热力学网络计算框架，将计算任务映射到热力学系统的稳态演化中 (arXiv: 2605.15985)
   313|  - 计算通过热力学网络向非平衡稳态的自然演化涌现，耗散是特征而非缺陷
   314|  - 能量流执行逻辑操作，热耗散限制计算精度
   315|  - 速度、精度、能耗之间的基本权衡关系
   316|  - **Activation**: thermodynamic computing, non-equilibrium steady states, physical computation, thermodynamic networks
   317|
   318|## 2026-05-19 - 量子计算/计算机科学 (Cron Job)
   319|
   320|### Mutually Unbiased Bases for Variational Quantum Initialization
   321|- [[mub-qaoa-initialization]] - MUB集合初始化变分量子算法，理论证明MUB集成最大化随机哈密顿宽度，QAOA暖启动在80%案例中不劣于标准方案 (arXiv: 2605.16060)
   322|  - MUB集成在所有d+1正交基并集中最大化各向同性高斯随机哈密顿宽度
   323|  - 自适应MUB-XRot暖启动QAOA在MaxCut/MIS/背包问题上1500个测试案例80%不劣
   324|  - **Activation**: MUB initialization, mutually unbiased bases, QAOA warm-start, variational quantum
   325|
   326|### Bias Analysis and Regularization of SMO-VQE
   327|### SMO-VQE Bias Analysis and Regularization
   328|- [[smo-vqe-regularization]] - 分析SMO-VQE偏差累积，发现偏差校正在小曲率方向 destabilizes 优化，提出正则化方法提升VQE性能 (arXiv: 2605.15813)
   329|  - NFT/Rotosolve算法利用三角依赖性实现解析一维最小化，仅需2-3次能量评估
   330|  - 偏差校正 destabilizes 小曲率方向优化，原始偏差隐式充当正则化器
   331|  - 正则化方法实现误差累积同时保持无偏估计，跨系统规模/电路深度/哈密顿量一致提升
   332|  - **Activation**: SMO-VQE, Rotosolve, NFT algorithm, VQE optimization, quantum circuit bias
   333|
   334|## 2026-05-19 - Neuroscience Research (Cron Job)
   335|
   336|All 12 papers scanned across q-bio.NC and cs.NE categories (May 15-18, 2026).
   337|**75% coverage** (9/12 papers covered by existing skills). 0 new skills created.
   338|3 papers skipped: single-subject exploratory study (no generalizable methodology), symbolic regression (not neuroscience), evolutionary algorithm optimization (not neuroscience).
   339|
   340|### Key Recent Papers Analyzed
   341|- **The Complex Brain Hypothesis** (2605.16146) — Karl Friston group extends consciousness/entropy framework → [[complex-brain-hypothesis]]
   342|- **Code-Modulated Motion VEP for BCI** (2605.15801) — New BCI paradigm → [[code-modulated-motion-vep-bci]]
   343|- **Interpreting EEG Transformers with LRP** (2605.11885) — EEG foundation model explainability → [[eeg-foundation-lrp-interpretability]]
   344|- **Cortical Microcircuits Information Flux** (2605.14680) — Reverse engineering study → [[cortical-microcircuits-information-flux-optimization]]
   345|- **Rhythm Switching RNNs** (2605.14388) — Adaptive time constants → [[rhythm-switching-adaptive-time-constants-rnn]]
   346|- **Clockless Neuromorphic Computing** (2605.16114) — Autonomous spiking on reconfigurable chip → [[clockless-asynchronous-neuromorphic-computing]]
   347|- **Hippocampal-Entorhinal World Model** (2605.15733) — Structure abstraction and generalization → [[hippocampal-entorhinal-world-model]]
   348|- **Algebro-Deterministic Memory VaCoAl** (2605.15652) — Bridging silicon and hippocampus → [[vacoal-algebro-deterministic-memory]]
   349|- **Thermodynamic Networks** (2605.15985) — Non-equilibrium steady states → [[neuronal-murburn-thermodynamic-electricity]]
   350|
   351|### Skipped Papers
   352|- **From Observed Viability to Internal Predictive Approximation** (2605.15862) — Single-subject exploratory, no generalizable methodology
   353|- **Diversified Residual Symbolic Regression** (2605.15809) — Symbolic regression, not neuroscience
   354|- **Co-Evolutionary Algorithm Portfolios** (2605.15729) — Evolutionary optimization, not neuroscience
   355|
   356|**Activation**: neuroscience research, arxiv monitoring, cron job, zero new skills
   357|
   358|- 分析SMO-VQE中偏差累积，发现偏差校正在小曲率方向 destabilizes 优化，提出正则化方法 (arXiv: 2605.15813)
   359|  - NFT/Rotosolve算法利用三角依赖性实现解析一维最小化
   360|  - 偏差校正 destabilizes 优化，原始偏差估计器隐式充当正则化器
   361|  - **Activation**: VQE, SMO, Rotosolve, variational quantum eigensolver
   362|
   363|### σ-VQE: Excited-state Preparation of Quantum Many-Body Scars
   364|- σ-VQE变分量子本征求解器针对中间谱本征态，利用浅层电路有限表达能力优先选择疤痕态 (arXiv: 2602.20881)
   365|  - 低深度电路+能量选择性目标函数，显式惩罚目标能量附近的能量方差
   366|  - 在IBM Fez (Heron r2 QPU)上完成原理验证演示
   367|  - **Activation**: sigma-VQE, quantum many-body scars, excited state, shallow circuit
   368|
   369|## Quantum State Isomorphism Problems for Groups
   370|- [[quantum-state-isomorphism-groups]] - Computational complexity of quantum state equivalence under group actions (arXiv: 2605.12615)
   371|  - 核心要点 1: Pure-state version is BQP-hard for all nontrivial groups, contained in QCMA∩QCSZK
   372|  - 核心要点 2: Mixed-state version is QSZK-complete; resolves open question on abelian state hidden subgroup
   373|  - 核心要点 3: Clifford group ≥ Graph Isomorphism, Pauli group BQP-complete, bosonic optical ≥ Graph Isomorphism
   374|  - **Activation**: quantum state isomorphism, state hidden subgroup, quantum group actions, QSZK-complete, BQP-hard, 量子态同构, 2605.12615
   375|
   376|## 2026-05-19 - Computer Science + Quantum (Cron Job - Hourly)
   377|## 2026-05-19 - Neuroscience Research (Cron Job)
   378|
   379|### Bridging Silicon and the Hippocampus: Algebro-Deterministic Memory "VaCoAl" as a Substrate for Vector-HaSH and TEM
   380|- [[vacoal-hippocampal-memory]] - 用Galois域LFSR构建海马体记忆的代数确定性基底，连接Vector-HaSH、TEM与iEEG发现 (arXiv: 2605.15652)
   381|  - 确定性Galois域扩散替代随机投影，提供比特级可复现的准正交向量基底
   382|  - 提出CR2 = ∏CR1^n 多跳回放保真度衰减的首个代数可处理模型
   383|  - **Activation**: hippocampal memory, VaCoAl, Vector-HaSH, TEM, grid cells, episodic replay, sharp-wave ripples, hyperdimensional computing, Galois field, STDP
   384|
   385|### FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping
   386|- [[fits-interpretable-spiking-neuron]] - 将SNN神经元时序计算分解为频率选择性和时间塑形两个可解释模块 (arXiv: 2605.13071)
   387|  - FS模块学习神经元目标频率，TS模块通过群延迟调制控制时序对齐
   388|  - 在无循环/延迟的前馈SNN中超越LIF基线，提供神经元级可解释参数
   389|  - **Activation**: FiTS, frequency selectivity, temporal shaping, interpretable SNN, LIF neuron, group delay, auditory processing
   390|
   391|
   392|### AQKA: Active Quantum Kernel Acquisition Under a Shot Budget
   393|- [[aqka-active-quantum-kernel-acquisition]] - Closed-form gradient-based optimal shot allocation for quantum kernel estimation (arXiv: 2605.14672)
   394|  - 核心要点 1: Optimal shot allocation s_ij* ∝ |g_ij|√(K_ij(1-K_ij)) using KRR/SVM dual variables
   395|  - 核心要点 2: Regime decomposition - AQKA dominates budget-limited, Nyström-QKE wins at saturating budgets
   396|  - 核心要点 3: Live hardware results: +26-32 pts on 156-qubit Heron, advantage grows with N
   397|  - **Activation**: AQKA, active quantum kernel, shot budget allocation, adaptive shot allocation, quantum kernel ridge regression, 2605.14672
   398|
   399|## 2026-05-19 - Computer Science + Quantum (Hourly Cron Job)
   400|
   401|### Shot-Based Quantum Encoding: A Data-Loading Paradigm for Quantum Neural Networks
   402|- [[shot-based-quantum-encoding]] - NISQ data loading via shot distribution over input states (arXiv: 2604.06135)
   403|  - 核心要点 1: SBQE allocates shots according to data-dependent classical distributions instead of deep encoding circuits
   404|  - 核心要点 2: Achieves high expressivity with shallow circuits — optimizes the hardware-native resource (shots)
   405|  - 核心要点 3: Outperforms angle/amplitude/basis encoding on expressivity-depth tradeoff
   406|  - **Activation**: shot-based encoding, SBQE, quantum data loading, quantum neural network encoding, 2604.06135
   407|
   408|### Soft-Quantum Algorithms
   409|- [[soft-quantum-algorithms]] - Direct matrix element optimization bypassing gate-based VQC training (arXiv: 2604.06523)
   410|  - 核心要点 1: Trains unitary matrix elements directly, avoiding gate decomposition overhead and barren plateaus
   411|  - 核心要点 2: Efficient for few-qubit problems with large datasets — matrix size scales as 2^n
   412|  - 核心要点 3: Post-training compilation step required to deploy on quantum hardware
   413|  - **Activation**: soft-quantum, direct matrix optimization, quantum operation optimization, VQC alternatives, 2604.06523
   414|
   415|### Do Quantum Transformers Help? A Systematic VQC Architecture Comparison
   416|- [[vqc-architecture-comparison]] - Systematic comparison of FC-VQC, ResNet-VQC, QT, FQT on tabular benchmarks (arXiv: 2604.23931)
   417|  - 核心要点 1: ResNet-VQC provides best accuracy-parameter tradeoff for most tabular tasks
   418|  - 核心要点 2: Quantum transformers show promise but require more qubits than NISQ devices provide
   419|  - 核心要点 3: No single architecture dominates — benchmark-dependent selection needed
   420|  - **Activation**: VQC architecture, quantum transformer, variational quantum circuit comparison, quantum tabular learning, 2604.23931
   421|
   422|## 2026-05-19 - Computer Science + Quantum (Cron Job)
   423|
   424|### Winning Lottery Tickets in Neural Networks via a Quantum-Inspired Classical Algorithm
   425|- [[quantum-inspired-lottery-tickets]] - Classical dequantization of quantum ML lottery ticket algorithm achieving polynomial-time sparse subnetwork selection via ridgelet transform sampling (arXiv: 2605.13979)
   426|  - 核心要点 1: QML algorithm selects sparse subnetworks from large shallow NNs via ridgelet transform
   427|  - 核心要点 2: Classical dequantized algorithm runs in O(poly(D)) vs O(exp(D)) naive approach
   428|  - 核心要点 3: Achieves comparable empirical risk to exact sampling, much better than uniform sampling
   429|  - **Activation**: quantum-inspired, lottery tickets, dequantization, ridgelet sampling, sparse subnetwork, 量子启发中奖彩票, 2605.13979
   430|
   431|### Quantum Feature Pyramid Gating for Seismic Image Segmentation
   432|- [[quantum-feature-pyramid-gating]] - Hybrid quantum-classical image segmentation using multi-scale quantum feature extraction with adaptive gating mechanism (arXiv: 2605.15370)
   433|  - 核心要点 1: Multi-scale feature pyramid with quantum feature encoding at each scale
   434|  - 核心要点 2: Parameterized quantum circuits process encoded features, adaptive gates fuse quantum+classical
   435|  - **Activation**: quantum feature pyramid, QFPG, quantum segmentation, hybrid quantum-classical, 量子特征金字塔, 2605.15370
   436|
   437|### Wavelet Variance Equipartition as Threshold for Quantum Kernel TN-Simulability
   438|- [[wavelet-variance-equipartition-quantum]] - Wavelet scaling exponent α as diagnostic for representation quality and classical simulability boundary of quantum kernels (arXiv: 2605.11557)
   439|  - 核心要点 1: α=1/2 is sharp boundary — area-law (>1/2) admits classical emulation, volume-law (<1/2) is exponentially hard
   440|  - 核心要点 2: VideoMAE latents show spatial tokens ~0.423, feature channels ~-0.123 (deep volume-law)
   441|  - 核心要点 3: Shot noise wall: measurement budget M=Ω(d²) constrains quantum ML scalability
   442|  - **Activation**: wavelet variance equipartition, scaling exponent, quantum kernel simulability, tensor network bond dimension, 小波方差等配分, 2605.11557
   443|
   444|## 2026-05-19 - Neuroscience Research (Cron Job)
   445|
   446|### Decoding Alignment without Encoding Alignment: A critique of similarity analysis in neuroscience
   447|- [[decoding-encoding-alignment-critique]] - Fundamental critique of RSA/CKA/Procrustes showing decoding metrics saturate with small subpopulations and are blind to encoding manifold topology (arXiv: 2605.05907)
   448|  - 核心要点 1: RSA/CKA/Procrustes can be saturated by 5% of neurons and miss functional architecture
   449|  - 核心要点 2: Encoding manifold (neuron-centric) vs decoding manifold (stimulus-centric) duality
   450|  - 核心要点 3: Causal evidence via MNIST — identical decoding scores with different encoding topologies
   451|  - 核心要点 4: Gromov-Wasserstein distance as complementary metric for neural population comparison
   452|  - **Activation**: decoding alignment critique, RSA limitations, CKA blindness, encoding manifold, neural population topology, Gromov-Wasserstein neural, 2605.05907
   453|
   454|### Clockless Asynchronous Neuromorphic Computing on FPGA
   455|- [[clockless-asynchronous-neuromorphic-computing]] - Scalable B-SNN architecture using autonomous Boolean spiking neurons on commercial FPGAs with nanosecond spike dynamics (arXiv: 2605.16114)
   456|  - 核心要点 1: 196-neuron B-SNN with Dale's principle (20% inhibitory), receptive neurons (CM=2), local connectivity
   457|  - 核心要点 2: Synaptic weights embedded in circuit topology (not registers) via delayed-path replication
   458|  - 核心要点 3: Liquid State Machine on SHD audio classification; 2.07 ns spikes vs 10ns measurement clock
   459|  - 核心要点 4: UDP/Ethernet real-time spike streaming; 10-100x lower power than clocked designs
   460|  - **Activation**: clockless FPGA neuromorphic, Boolean spiking neuron, autonomous circuit SNN, asynchronous neuromorphic, 2605.16114
   461|
   462|### Ensemble Engineering for Quantum Measurements
   463|- [[ensemble-engineering-quantum-measurements]] - General framework mitigating destructive cancellation in NISQ quantum measurements by encoding sampling distribution in prepared quantum state (arXiv: 2605.03729)
   464|  - 核心要点 1: Destructive cancellation is structural mismatch between ensemble weights and operator sign structure, not just statistical
   465|  - 核心要点 2: Grover-type amplitude amplification + oracle-free shallow circuit for near-term hardware
   466|  - 核心要点 3: Demonstrated on IBM quantum processors up to 20 qubits
   467|  - **Activation**: quantum ensemble engineering, destructive cancellation, NISQ measurement, amplitude amplification, 2605.03729
   468|
   469|### QBalance: Multi-Objective Quantum Workflow Optimization
   470|- [[qbalance-workflow-optimization]] - Reproducible multi-objective strategy selection for quantum compilation, noise suppression, and error mitigation (arXiv: 2605.02966)
   471|  - 核心要点 1: Formulates quantum compilation as weighted multi-objective optimization over circuits, backends, and policies
   472|  - 核心要点 2: Non-dominated Pareto selection, Bayesian candidate ordering, survival-product error proxy
   473|  - **Activation**: QBalance, quantum workflow optimization, quantum compilation strategy, NISQ compilation, 2605.02966
   474|
   475|### Adaptive Bistable Qubit Control
   476|- [[adaptive-bistable-qubit-control]] - 1-bit feedback protocol for operating bistable qubits with TLS defects using FPGA real-time control at ~136 kHz (arXiv: 2605.03187)
   477|  - 核心要点 1: Estimates qubit bistable frequency from single single-shot measurement — reaches Shannon information limit
   478|  - 核心要点 2: 77% error reduction in gate fidelity suppression, validated on superconducting qubit
   479|  - 核心要点 3: Scalable to large qubit arrays via parallel FPGA feedback channels
   480|  - **Activation**: bistable qubit, TLS defect mitigation, 1-bit feedback, adaptive qubit control, FPGA quantum control, 2605.03187
   481|
   482|### Embedded Quantum Machine Learning in Embedded Systems
   483|- [[embedded-quantum-machine-learning]] - Feasibility analysis and hybrid architectures for embedding quantum ML workloads in resource-constrained embedded systems (arXiv: 2603.12540)
   484|  - 核心要点 1: Explores hybrid classical-quantum architectures for embedded deployment
   485|  - 核心要点 2: Addresses resource constraints in edge quantum computing scenarios
   486|  - **Activation**: embedded quantum ML, edge quantum computing, hybrid quantum-classical embedded, 2603.12540
   487|
   488|### Diagonal Adaptive Non-local Observables on Quantum Neural Networks
   489|- [[diagonal-adaptive-non-local-observables]] - Reduces k-local observable complexity from O(4^k) to O(2^k) while preserving full ANO expressivity via diagonal canonical representation (arXiv: 2605.15410)
   490|  - 核心要点 1: 对角可观测量是 ANO 空间在酉相似变换下的规范代表元，保持等效表达能力
   491|  - 核心要点 2: 将 k 局部可观测量复杂度从 O(4^k) 降至 O(2^k)，显著降低经典优化成本
   492|  - **Activation**: diagonal ANO, quantum observable optimization, VQA function space, adaptive quantum measurements, 2605.15410
   493|
   494|## 2026-05-19 - Neuroscience Research (Cron Job)
   495|
   496|### Hippocampal-Entorhinal Inspired World Model
   497|- [[hippocampal-entorhinal-world-model]] - Brain-inspired hierarchical world model for structure abstraction and generalization from video (arXiv: 2605.15733)
   498|  - Simultaneously infers latent transitions and constructs predictive visual world model
   499|  - HPC-MEC coupling dissociates relational structures (MEC) from integrated episodic scenes (HPC)
   500|  - **Activation**: hippocampal-entorhinal model, world model, structure abstraction, HPC-MEC coupling
   501|