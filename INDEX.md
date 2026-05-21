## 2026-05-22 - Number Theory, Statistics, Advanced Mathematics + Quantum Mechanics (Cron Job)

### Evidence of Quantum Machine Learning Advantage with Tens of Noisy Qubits
- [[quantum-ml-advantage-noisy]] - Demonstrates coherent quantum ML advantage at 30-40 noisy qubits scale; data acquisition becomes the fundamental bottleneck over classical computation (arXiv:2605.21346)
  - Coherent quantum processing shows clear performance separation vs fixed-measurement schemes under realistic hardware noise
  - At 30-40 qubit scale, measure-first matching requires months to years of data collection
  - Systematic hardware constraint evaluation framework: state prep, gate errors, readout, connectivity, coherence times
  - **Activation**: quantum ml advantage, noisy qubits, qml benchmark, coherent processing, quantum data acquisition, NISQ machine learning, 量子机器学习优势

### An Entropy-Governed Speedup for Quantum Algorithms on Local Hamiltonians
- [[entropy-governed-quantum-speedup]] - Faster quantum algorithm for low-energy estimation on k-local Hamiltonians that breaks the Grover bound O(2^{n/2}) by targeting depth-d state energy minimums (arXiv:2605.18241)
  - Outputs quantum state with energy bounded by minimum over all depth-d circuits
  - Provides insight into distinguishing strongly entangled vs classically describable states
  - For Hamiltonians with depth-d ground states, matches Buhrman et al. (PRL 2025) guarantees but faster
  - **Activation**: entropy-governed speedup, local Hamiltonian, depth-d states, Grover bound, quantum complexity, low-energy estimation, state preparation, 熵调控量子加速

### Statistical Quantum Phase Estimation: Extensions and Practical Considerations
- [[statistical-quantum-phase-estimation]] - SQPE refinements for early fault-tolerant quantum computers: handles negative Pauli weights, changepoint detection without overlap estimates, 2x sample reduction via Fourier symmetry (arXiv:2605.18876)
  - Generalizes random compilation for arbitrary-sign Pauli weights in LCU decomposition
  - Changepoint detection replaces overlap-dependent GSE estimation (no chicken-and-egg problem)
  - Fourier series symmetry halves circuit runs while maintaining accuracy
  - **Activation**: statistical quantum phase estimation, SQPE, ground state energy, changepoint detection, LCU decomposition, Pauli weights, Fourier symmetry, early fault-tolerant quantum computing

### Circuits of Quantum Hashing and Quantum Fourier Transform for a Cactus as a Qubit Connectivity Graph
- [[quantum-hashing-qft-connectivity]] - O(n^2*m) quantum circuit optimization for quantum hashing and QFT on cactus graph connectivity, improving over exponential-time algorithm for arbitrary graphs (arXiv:2605.20789)
  - Uses shortest non-simple 1-covering path as polynomial-time subroutine
  - Applies to NISQ devices with restricted qubit connectivity (IBM Q, Rigetti)
  - Independently useful graph theory result for cactus graphs
  - **Activation**: quantum hashing, quantum fingerprinting, qubit connectivity graph, cactus graph, QFT optimization, quantum circuit compilation, 1-covering path, NISQ routing

## 2026-05-22 - Neuroscience Research (Cron Job)

### Brain Alignment of Reasoning and Action Representations from VLMs and LAMs During Gameplay
- [[brain-alignment-vlm-lam-gameplay]] - Vision-language models (VLMs) and large-action models (LAMs) exhibit strong brain alignment with fMRI during naturalistic Atari gameplay, outperforming RL baselines with prompt-driven gains scaling with cortical hierarchy (arXiv:2605.19352)
  - VLM is prompt-symmetric (12.5% action vs 13.6% reasoning unique variance); LAM is prompt-asymmetric (27% action vs -5% reasoning)
  - Largest encoding improvements in frontal-parietal and motor-planning regions
  - Action-specialized fine-tuning reorganizes multimodal representations toward action-relevant neural computations
  - **Activation**: brain alignment VLM LAM, vision-language model brain encoding, large-action model neural alignment, naturalistic gameplay fMRI, action reasoning representations brain

### Letting the Neural Code Speak: Automated Characterization of Visual Neurons Through Human Language
- [[neural-code-speak]] - Closed-loop framework using generative models and neural digital twins to translate each neuron's high/low activating images into semantic hypotheses, verified in silico; 96.1% of V4 neurons driven above 95th percentile by hypothesis-generated images (arXiv:2605.12485)
  - Descriptions range from oriented edges/spatial frequency in V1 to conjunctions of form/color/texture in V4
  - Language compression is lossy but semantically faithful; RSA shows alignment recovered when hypotheses rendered back into images
  - Enables agentic scientific discovery for interpretable neural function description at scale
  - **Activation**: neural code language, automated neuron characterization, neural digital twin visual cortex, closed-loop neuron description, semantic hypothesis neural selectivity, macaque V1 V4 neuron description

### A Simple Model of Co-Emergence of Grid and Place Fields
- [[grid-place-co-emergence]] - First unified recurrent network model instantiating Dale's Law where grid and place cells co-emerge from a single sensory-prediction objective without supervision of either type (arXiv:2605.21356)
  - Single-objective RNN trained to predict next sensory observation from masked previous observations and egocentric motion
  - Coexists across 1,000 training configurations; balance set by sensory noise and masking
  - Reproduces grid fragmentation, merging, lattice alignment, 3D bat fields, and developmental order without retraining
  - Two complementary encoding pressures: reconstruction (place-like) vs prediction (grid-like)
  - **Activation**: grid cell place cell co-emergence, Dale's law RNN, spatial navigation sensory prediction, hippocampal-entorhinal unified model, grid field co-emergence, 网格细胞位置细胞共同涌现

### Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry
- [[platonic-representations-brain]] - Extends Strong Platonic Representation Hypothesis to human visual cortex, proving subject-specific fMRI representations are approximately isometric and translatable via unsupervised geometric transformations without paired data (arXiv:2605.20496)
  - Self-supervised encoder from fMRI data exploiting repeated stimulus presentations
  - Unsupervised orthogonal rotations recover accurate cross-subject instance-level correspondences
  - Synchronized pairwise rotations into shared latent space further improves retrieval
  - Evidence for shared universal neural geometry across individuals in visual cortex
  - **Activation**: platonic representation human brain universal geometry, fMRI cross-subject unsupervised alignment, shared neural geometry visual cortex, deep learning brain representation translation, 柏拉图表征人脑视觉皮层通用几何


### MLLM Brain Alignment via Task-Conditioned Probing
- [[mllm-brain-alignment-task-probing]] - Instruction-tuned MLLMs show higher brain alignment than non-IT models during naturalistic movie watching; reveals task-specific neural representations across brain regions (arXiv:2506.08277)
  - IT-MLLMs achieve ~9-20% higher brain alignment vs baselines
  - Task-specific instructions produce distinct MLLM representations across brain regions
  - ICL models show strong semantic coupling (r=0.78) while IT-MLLMs show weak semantic coupling (r=0.14)
  - **Activation**: brain-MLLM alignment, instruction-tuned MLLM, task-conditioned probing, fMRI encoding

### E-ReCON: Energy-Efficient nvCIM Macro for SNN/CNN Edge Inference
- [[erecon-snn-nvcim-hardware]] - 16Kb energy- and resource-efficient DCIM macro with 3T1R ReRAM bitcell supporting both CNN and SNN workloads (arXiv:2605.20717)
  - Novel 3T1R bitcell with AND-based in-memory multiplication for dual workload support
  - Interleaved 10T/28T adder tree reduces transistor count by 37% and power by 28%
  - Achieves 419 TOPS/W energy efficiency at 2.31-3.1 TOPS throughput
  - 2A2W precision matches FP32 baseline accuracy across VGG/ResNet on ImageNet
  - **Activation**: nvCIM, ReRAM CIM, SNN hardware accelerator, neuromorphic hardware macro
## 2026-05-21 - Neuroscience Research (Cron Job)

### Closed-Form Predictive Coding via Hierarchical Gaussian Filters
- [[closed-form-predictive-coding-hgf]] - Restores precision-weighted prediction errors to predictive coding networks using deep hierarchical Gaussian filters, enabling biologically plausible learning without backpropagation (arXiv:2605.20293)
  - Core: Expresses PC networks as HGFs with closed-form variational inference for activations, weights, and precisions
  - Results: Approaches backpropagation on FashionMNIST; outperforms on online/data-efficiency/concept-drift tasks
  - Biological grounding: Hebbian-compatible local update rules; precision-weighting connects to cortical attention/uncertainty
  - **Activation**: predictive coding, hierarchical Gaussian filter, free energy principle, precision-weighted prediction error, biologically plausible learning, HGF

### How to Build Marcus's Algebraic Mind: VaCoAl over Galois Fields
- [[algebraic-mind-vacoa]] - Maps Gary Marcus's three pillars of cognitive architecture onto PyVaCoAl/VaCoAl hyperdimensional computing using XOR-and-shift over GF(2) (arXiv:2605.21379)
  - Core: Single algebraic primitive (XOR-shift) implements reversible variable binding, non-commutative bundling, and individual/kind separation
  - Biological homologue: Dentate gyrus-CA3 circuit as VaCoAl's natural implementation
  - Extends to Pearl's rung-3 counterfactual reasoning
  - **Activation**: vacoal, hyperdimensional computing, algebraic mind, Gary Marcus, reversible variable binding, Galois fields, PyVaCoAl

### MLLM Brain Alignment via Task-Conditioned Probing
- [[mllm-brain-alignment-task-probing]] - Instruction-tuned MLLMs show higher brain alignment than non-IT models during naturalistic movie watching; reveals task-specific neural representations across brain regions (arXiv:2506.08277)
  - IT-MLLMs achieve ~9-20% higher brain alignment vs baselines
  - Task-specific instructions produce distinct MLLM representations across brain regions
  - ICL models show strong semantic coupling (r=0.78) while IT-MLLMs show weak semantic coupling (r=0.14)
  - **Activation**: brain-MLLM alignment, instruction-tuned MLLM, task-conditioned probing, fMRI encoding

### E-ReCON: Energy-Efficient nvCIM Macro for SNN/CNN Edge Inference
- [[erecon-snn-nvcim-hardware]] - 16Kb energy- and resource-efficient DCIM macro with 3T1R ReRAM bitcell supporting both CNN and SNN workloads (arXiv:2605.20717)
  - Novel 3T1R bitcell with AND-based in-memory multiplication for dual workload support
  - Interleaved 10T/28T adder tree reduces transistor count by 37% and power by 28%
  - Achieves 419 TOPS/W energy efficiency at 2.31-3.1 TOPS throughput
  - 2A2W precision matches FP32 baseline accuracy across VGG/ResNet on ImageNet
  - **Activation**: nvCIM, ReRAM CIM, SNN hardware accelerator, neuromorphic hardware macro

## 2026-05-22

### Enhanced Reinforcement Learning-based Process Synthesis via Quantum Computing
- [[quantum-systems-engineering-2026]] - Quantum systems engineering methodology covering sidecar architectures, resource allocation, energetic optimization, and RL-based process synthesis via quantum computing (arXiv:2605.21213)
  - Core: Formulates process synthesis as MDP solved with quantum-enhanced RL
  - Pattern: Quantum sidecar architecture with stateful/stateless operating modes
  - **Activation**: quantum systems engineering, hybrid quantum architecture, quantum resource allocation, quantum sidecar, quantum process synthesis, 量子系统工程, 量子混合架构

### Quantum Sidecar Architectures for Hybrid AI Training and Inference
- Part of quantum-systems-engineering-2026 - Two-mode quantum co-processor architecture (arXiv:2605.18031)
  - Stateful protected register mode for reusable quantum resources
  - Stateless reset-and-reprepare mode for per-invocation circuits

### System Aware Resource Allocation for Distributed Quantum Workflows
- Part of quantum-systems-engineering-2026 - Comprehensive quantum program allocation (arXiv:2605.17944)
  - Qubit availability, circuit depth, error rate, and workflow dependency optimization

### Energetic Advantage in Superconducting Cat-Qubits
- Part of quantum-systems-engineering-2026 - Energy optimization methodology (arXiv:2605.19854)
  - Quantum energetic advantage before computational advantage at >26 qubits

## 2026-05-21 - Systems Engineering + Quantum (Cron Job)

### Coupling-Phase Engineering for Giant-Atom Waveguide QED Systems
- [[coupling-phase-giant-atom-control]] - Use coupling phase to control bound states in the continuum (BICs) and quantum dynamics in nonlocal light-matter interfaces (arXiv: 2605.17878)
  - Core: Giant atoms couple to waveguides at multiple spatially separated points, enabling interference-based BIC engineering
  - Pattern: Coupling phase modulation controls BIC number, profile, and dynamical behavior
  - Applications: Quantum state trapping, protected quantum information processing, giant-atom quantum networks
  - **Activation**: giant atom, waveguide QED, bound state in continuum, coupling phase engineering, BIC quantum, 量子巨原子, 连续谱束缚态

## 2026-05-21 - Systems Engineering (Cron Job)

### Modeling and Resource Optimization for Quantum Oracles
- [[quantum-oracle-resource-optimization]] - Formal oracle description and space-depth trade-off algorithm achieving 54% circuit depth reduction (arXiv: 2605.21380)
  - HRSE model enables hierarchical recursive synthesis-evaluation for formal oracle description
  - ASDT algorithm generates optimal oracle structures under fixed qubit constraints
  - **Activation**: quantum oracle, oracle optimization, HRSE model, ASDT algorithm, space-depth tradeoff, quantum circuit optimization

### When Does Adaptation Win? Scaling Laws for Meta-Learning in Quantum Control
- [[quantum-control-meta-learning-scaling]] - Scaling law for meta-learning adaptation gain in quantum control with >40% fidelity gains (arXiv: 2601.18973)
  - Already exists in collection (checked for duplicates)
  - **Activation**: quantum control, meta-learning, scaling laws, adaptation gain



## 2026-05-21 - Neuroscience Research (Cron Job)

### Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry
- [[platonic-representations-brain]] - Cross-subject neural geometry alignment in human visual cortex, demonstrating that subject-specific fMRI representations are approximately isometric and can be translated through purely geometric transformations without paired data (arXiv: 2605.20496)
  - Self-supervised encoder learns subject-specific embeddings from fMRI data via repeated stimulus presentations
  - Unsupervised orthogonal rotations translate representations across subjects without paired samples
  - Synchronized pairwise rotations into a shared latent space improves cross-subject retrieval
  - Evidence for shared universal neural geometry across individuals in visual cortex
  - **Activation**: platonic representation human brain, cross-subject brain alignment unsupervised, fMRI representation geometry translation, shared neural geometry visual cortex, 柏拉图表示人脑通用几何

## 2026-05-21 - Systems Engineering + Quantum (Cron Job)

### QUTest: A Native Testing Framework for Quantum Programs
- [[quantum-native-testing-framework]] - Native OpenQASM 3 testing framework with pragma-based assertions, 12 assertion types, linter, and CI integration for quantum programs (arXiv: 2605.19736)
  - Both programs and tests are standard .qasm files using //% pragma comments
  - 12 assertion types: deterministic, statistical, quantum-state, and structural checks
  - Environment-aware mode for cross-runtime testing (Qiskit, Cirq, Qulacs)
  - CLI with auto test discovery, compatibility checks, and JUnit XML reports
  - **Activation**: quantum native testing, openqasm testing framework, quantum test assertions, quantum program testing, qasm test framework, quantum CI testing, pragma quantum testing, 量子测试框架

### PIQC: Scalable Distributed Quantum Computing via Photonic Integration of Designed Molecular Quantum Nodes
- [[piqc-distributed-quantum-computing]] - Scalable distributed quantum computing architecture using photonic integration of designed molecular quantum nodes (NV/SiV centers in diamond) with nanophotonic waveguide networks for entanglement distribution (arXiv: 2605.21204)
  - NV/SiV centers as quantum processing nodes with long coherence times
  - Nanophotonic waveguide interconnects for modular scalability
  - Heralded entanglement distribution via spin-photon entanglement and photon interference
  - Systems engineering framework for error budget analysis and topology design
  - **Activation**: photonic integrated distributed quantum computing, molecular quantum nodes, NV center quantum network, distributed quantum architecture

### Measurement and Control of the Complex Berry Phase in a Quantum System
- [[complex-berry-phase-quantum-control]] - Complex Berry phase measurement and control methodology for non-Hermitian quantum systems using superconducting transmon circuits with engineered dissipation (arXiv: 2605.16559)
  - Complex Berry phase decomposition into real (geometric phase) and imaginary (amplification/attenuation) components
  - Engineered dissipation used as control resource rather than liability
  - Non-unitary quantum control via path-dependent geometric effects
  - Geometric quantum gates with SU(1,1) operations
  - **Activation**: complex Berry phase quantum control, non-Hermitian geometric phase, transmon circuit Berry phase, engineered dissipation quantum control

### Enhanced Reinforcement Learning-based Process Synthesis via Quantum Computing
- [[quantum-rl-process-synthesis]] - Quantum reinforcement learning methodology for process systems engineering that encodes process synthesis as MDPs with state encoding algorithms decoupling qubit requirements from problem size (arXiv: 2605.21213)
  - Process synthesis formally posed as MDP with compressed state encoding
  - Quantum-enhanced RL shows competitive per-episode performance and superior per-parameter efficiency vs classical RL
  - State encoding decouples qubit count from problem size for scalability
  - **Activation**: quantum reinforcement learning process synthesis, quantum RL engineering design, quantum process optimization, flowsheet synthesis quantum, quantum MDP process systems

### Software Between Quantum and Machine Learning -- And Down to Pulses
- [[quantum-control-pulse-software]] - Software framework integrating quantum optimal control within QML for pulse-level modelling, bridging gate-based abstractions with hardware-aware optimisation using JAX-based high-performance implementation (arXiv: 2605.21286)
  - Composable ansatz constructions with interchangeable building blocks for pulse-level modelling
  - End-to-end optimisation of pulse parameters within QML setting
  - Fourier-analytic diagnostics and extended entanglement measures for analysis
  - **Activation**: quantum pulse level control, quantum optimal control software, QML pulse modelling, quantum gate abstraction, hardware-aware quantum optimisation

## 2026-05-21 - Neuroscience Research (Cron Job)

### Stimulus Symmetries Can Confound Representational Similarity Analyses
- [[stimulus-symmetries-rsm-confound]] - Demonstrates that stimulus symmetries in network inputs cause functionally-equivalent neural representations to produce different, drifting RSM geometries, challenging common assumptions in RSA/CKA analyses (arXiv: 2605.21324)
  - Formal proof that stimulus symmetries produce gauge-dependence in RSMs — functionally equivalent codes yield different geometries
  - SGD/energy regularization drives RSMs to drift over training via sparse, manifold-tiling codes
  - Phenomena persist in image-trained networks with latent (not explicit) symmetries
  - Challenges the assumption that RSM invariance to rotation captures all meaningful equivalence
  - **Activation**: representational similarity analysis, RSM gauge dependence, stimulus symmetry, RSA confound, neural code comparison, drifting representations, representational geometry, functionally equivalent representations, neural manifold tiling, CKA limitations, RSA robustness, stimulus invariance

### Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry
- [[platonic-representations-brain-universal-geometry]] - Evidence for a shared neural geometry in human visual cortex where subject-specific fMRI representations are approximately isometric and translatable via unsupervised geometric transformations (arXiv: 2605.20496)
  - Self-supervised encoder learns subject-specific fMRI embeddings from repeated stimulus presentations
  - Unsupervised orthogonal rotation alignment translates independently learned brain spaces across subjects
  - Shared latent space via synchronized pairwise rotations improves cross-subject retrieval
  - **Activation**: platonic representation, universal brain geometry, cross-subject fMRI alignment, isometric neural embedding, unsupervised brain translation, visual cortex representation

### Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function
- [[functional-whole-brain-models-fwbm]] - Unified modeling paradigm integrating structural brain grounding, continuous-time dynamical realism, and task-performing cognitive capacity (arXiv: 2605.18118)
  - Four minimal criteria: structural grounding, dynamical realism, functional competence, mappable observables
  - Three-pillar roadmap bridging bottom-up WBM and top-down neuroconnectionism
  - Short-/mid-/long-term horizons toward personalized brain simulation for clinical applications
  - **Activation**: functional whole-brain model, fWBM, whole-brain modeling, neuroconnectionism, brain structure-function, brain dynamics simulation, neural mass model

### Von Economo Neurons Enable Reliable Social Skill Acquisition in Recurrent Spiking Neural Networks
- [[vencircuit-ven-gradient-scaffold]] - Biologically motivated SNN showing VENs function as residual gradient scaffolds: 2% VENs confer 21x training convergence advantage via direct gradient pathway immune to recurrent Jacobian instabilities, with clinical predictions for ASC vs bvFTD (arXiv: 2605.17399)
  - VEN-intact networks converge 98% vs 70% ablated (Fisher's OR=21.0, p=8.7×10⁻⁵)
  - VENs provide O(1) gradient pathway structurally immune to product instabilities
  - Mid-training ablation (epochs 5-25) most disruptive; inference-time VENs largely dispensable
  - Predicts timing of VEN loss determines social cognitive consequences (developmental vs adult)
  - **Activation**: Von Economo neuron, VENCircuit, gradient scaffold SNN, spiking neural network social cognition, residual connections SNN

### Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity
- [[geometric-phase-transition-hippocampal-memory]] - Extreme spatial memory in food-caching birds arises from a topological phase transition from disorganized "mist" to geometrically rigid "crystalline" hippocampal population code, enabling >100x capacity via neural manifold stiffening (arXiv: 2605.17199)
  - Crystalline codes sustain >1,000 locations vs mist codes failing below 10 (>100x advantage)
  - Excitatory-inhibitory synergy: excitatory scaffold + inhibitory orthogonal decorrelation
  - 169-fold "geometric tax" — representational redundancy stabilizing manifold against noise
  - Double dissociation with Valiant's model confirms continuous topological organization
  - **Activation**: geometric phase transition, crystalline neural code, hippocampal memory, geometric tax, food-caching birds spatial memory, mist code vs crystalline code

### A Simple Model of Co-Emergence of Grid and Place Fields (Evening Supplement)
- [[grid-place-cell-co-emergence]] - First unified recurrent network model achieving co-emergence of grid cells and place cells from a single sensory-prediction objective without supervision of either cell type (arXiv: 2605.21356)
  - Grid fields for path integration (motion prediction pressure), place fields for pattern completion (sensory reconstruction pressure)
  - Both spatial codes coexist across 1,000+ training configurations; balance controlled by sensory noise/masking
  - Qualitatively reproduces grid fragmentation, wall-removal merging, lattice alignment, 3D bat fields, and developmental ordering
  - **Activation**: grid cells, place cells, co-emergence, sensory prediction, path integration, entorhinal cortex-hippocampus loop, spatial navigation, grid cell development

### Self-Supervised Local Learning Rules Discover Hidden Hierarchical Structure
- [[self-supervised-local-learning-rhm]] - Biologically plausible learning algorithms showing that layerwise self-supervised (contrastive/non-contrastive) rules can learn hidden hierarchical structure as efficiently as backpropagation, while gradient-feedback rules fail due to input-specific nonlinearity masking (arXiv: 2605.18557)
  - Direct-feedback alignment rules fail on Random Hierarchy Model (RHM) tasks due to "masking" — input-specific nonlinearities essential for complex tasks
  - Self-supervised local rules (contrastive and non-contrastive) match backprop data efficiency
  - Compatible with known cortical synaptic plasticity rules; provides candidate mechanism for cortex learning without explicit error signals
  - **Activation**: biologically plausible learning, local learning rules, backpropagation-free learning, self-supervised learning, cortical plasticity, hierarchical representation learning, Random Hierarchy Model, masking phenomenon

### Subject-Specific Analysis of Self-Initiated Attention Shifts from EEG
- [[eeg-self-initiated-attention-shifts]] - Machine learning framework distinguishing self-initiated vs externally-instructed attention shifts from preparatory EEG activity, with SHAP-based feature attribution showing frontal high-frequency bands as key discriminators (arXiv: 2605.18251)
  - Controlled experimental paradigm isolating self-initiated shifts under identical visual stimulation
  - Reliable within-subject classification from preparatory EEG spectral features
  - SHAP analysis reveals frontal regions and higher-frequency bands dominate model decisions
  - **Activation**: EEG attention shifts, self-initiated attention, brain-computer interface, SHAP EEG analysis, preparatory neural activity, attention decoding, spectral EEG features
  
## 2026-05-21 - Systems Engineering + Quantum Mechanics (Cron Job)

### When Does Adaptation Win? Scaling Laws for Meta-Learning in Quantum Control
- [[quantum-control-meta-learning-scaling]] - Scaling law lower bound showing adaptation gain saturates exponentially with gradient steps and scales linearly with task variance; few-shot pre-adaptation protocol estimates optimal budget from N=3-5 probe steps (arXiv: 2601.18973)
  - Adaptation gain >40% fidelity on two-qubit gates under extreme OOD (10x training noise)
  - Cross-domain validation: same scaling laws emerge from quantum gate calibration and classical LQR control
  - Variance-aware controller selection: non-adaptive for low-variance, meta-learning for high-variance
  - **Activation**: quantum control meta-learning, adaptation scaling laws, quantum gate calibration, per-device calibration, OOD quantum control, meta-learning quantum

### Enhanced Reinforcement Learning-based Process Synthesis via Quantum Computing
- [[quantum-rl-process-synthesis]] - Quantum RL for process synthesis with state encoding algorithms decoupling qubit requirements from problem size (logarithmic vs linear scaling) (arXiv: 2605.21213)
  - Competitive per-episode performance, improved per-parameter efficiency vs classical RL
  - Controlled classical vs quantum benchmarking framework for flowsheet synthesis
  - MDP formulation for process synthesis with economic objective and feasibility constraints
  - **Activation**: quantum RL process synthesis, quantum process systems engineering, quantum-enhanced RL, flowsheet synthesis, qubit encoding algorithms

### Quantum-Enhanced Distributed Network Sensing
- [[quantum-enhanced-distributed-sensing]] - Multiphase estimation using three quantum resources: catalysis, entanglement, and squeezing (arXiv: 2605.19545)
  - Partial catalysis outperforms global catalysis in both ideal and noisy regimes
  - Precision approaches Heisenberg limit with full three-resource combination
  - Homodyne measurement scheme approaching quantum Cramer-Rao bound
  - **Activation**: quantum distributed sensing, multiphase estimation, quantum catalysis, entanglement squeezing, Heisenberg limit, DQN sensing, homodyne measurement

### Attack-Resilient CLF-CBF Quadratic Programs
- Paper: "A Unified Framework for Attack-Resilient CLF-CBF Quadratic Programs for Nonlinear Control-Affine Systems" (arXiv: 2605.20144)
  - AR-CLFs and AR-CBFs for false data injection attack resilience
  - Finite-time recovery to nominal safe set without prior magnitude bounds
  - Unified QP enforcing stability and safety simultaneously
  - **Already covered by existing skills**: advanced-control-systems-2026, discounted-mpc-robust-control

### Risk-Aware Covert Quantum Communication
- Paper: "A Risk-Aware Framework for Covert Quantum Communication under Stochastic Channel Uncertainty" (arXiv: 2605.18928)
  - Combines quantum communication theory with robust control principles
  - Secure quantum network design under stochastic channel uncertainty
  - **Already covered by existing skills**: covert-quantum-computing, dependable-quantum-systems


### Quantum Distributed Sensor Fusion with Byzantine Tolerance
- [[quantum-distributed-sensor-fusion]] - Unified MSE lower bounds for distributed quantum sensor fusion indexed by entanglement visibility and fault fraction (arXiv: 2605.19327)
  - Two-parameter MSE family: entanglement visibility (V) and fault fraction (f/M)
  - Heisenberg-limited precision achievable with full entanglement and no faults
  - Classical Brooks-Iyengar overlap + SPOTLESS verification adapted for quantum sensors
  - Three quantum resources (catalysis + entanglement + squeezing) outperform any two
  - **Activation**: quantum sensor fusion, byzantine-tolerant quantum sensing, distributed quantum sensing, entanglement visibility bounds, quantum sensor network reliability

### Quantum Workflow Resource Allocation
- [[quantum-workflow-resource-allocation]] - System-aware resource allocation for distributed quantum computing workflows in cloud platforms (arXiv: 2605.17944)
  - Multi-dimensional matching: program requirements × processor characteristics × queue state × cost
  - Dynamic reallocation based on quantum processor health monitoring
  - Workflow decomposition across heterogeneous quantum processors
  - **Activation**: quantum resource allocation, quantum workflow scheduling, quantum cloud resource management, distributed quantum computing workflow, quantum program allocation



## 2026-05-21 - Medicine + Quantum Mechanics (Cron Job)

### GKSL Dynamics for Quantum-Like Cognition and Decision Making
- [[gksl-quantum-cognition]] - Updated with arXiv:2604.18643 (GKSL master equation for cognitive psychology)
  - Passive/Active Hamiltonian classification for detecting cognitive agency
  - Cognitive beats as spectral diagnostic for nested deliberation timescales
  - Non-Nash equilibrium stabilization in strategic games via dissipative quantum models
  - **Activation**: GKSL quantum cognition, quantum-like decision making, cognitive beats

### Adaptive Hybrid Quantum-Classical Feature Fusion for Breast Cancer Classification
- [[adaptive-hybrid-quantum-classical-feature-fusion-medical]] - arXiv:2604.22903
  - Complementarity analysis between quantum and classical feature spaces for medical imaging
  - Temperature-scaled hybrid fusion (TSHF) resolves quantum-classical optimization asymmetries
  - Hilbert space mapping enhances breast cancer classification with limited qubit budgets
  - **Activation**: hybrid quantum-classical feature fusion, TSHF, breast cancer quantum, medical image quantum ML

### Tensor-Network Federated Medical Diagnosis with MPC Security
- [[tensor-network-quantum-federated]] - arXiv:2604.01616
  - Privacy-aware federated learning: tensor-network frontend + MPC aggregation + quantum refinement
  - Tensor-network compression enables quantum processing with minimal qubit requirements
  - Post-aggregation quantum enhancement improves diagnostic accuracy across distributed sites
  - **Activation**: federated quantum learning, tensor network medical, MPC privacy healthcare

### HQNN Breast Cancer Thermographic Classification
- [[hybrid-quantum-medical-thermographic]] - arXiv:2604.16953
  - Hybrid quantum-classical neural networks for breast cancer thermographic imaging
  - Quantum circuits embedded in classical layers for enhanced thermal pattern recognition
  - Medical diagnosis using infrared thermal signatures with quantum enhancement
  - **Activation**: HQNN thermographic, breast cancer thermal, quantum medical imaging

### Tensor Network Feature Engineering for Neurological Disorder Prediction
- [[tensor-network-neurological-predictor]] - arXiv:2605.17771
  - Multi-class neurological disorder prediction using tensor network feature engineering
  - Medical feature extraction from imaging data via tensor decomposition methods
  - Classification pipeline for diverse neurological conditions
  - **Activation**: tensor network neurological, multi-class disorder prediction, medical feature engineering


## 2026-05-21 - Quantum ML + VQA Optimization (Cron Job)

### Accelerating Noisy Variational Quantum Algorithms with Physics-Informed Denoising Networks
- [[pidn-vqa-denoising]] - Physics-Informed Denoising Network (PIDN) reduces Zero-Noise Extrapolation cost by ~4-6× by learning a surrogate of optimization dynamics, preserving gradient directionality while slashing circuit executions (arXiv: 2605.02066)
  - View variational update as trajectory in parameter space → train PIDN to reproduce ZNE-mitigated values
  - Physics-informed loss preserves gradient descent dynamics (cosine similarity with ZNE >0.95)
  - Benchmarked on QAOA (MaxCut, SK, TFIM) and VQE (LiH, BeH₂, H₂O) across all molecular systems
  - PIDN fails only when ZNE itself becomes unreliable — robust failure mode
  - Ablation confirms physics-informed loss is necessary for directional consistency
  - **Activation**: PIDN, physics-informed denoising, ZNE acceleration, noisy VQA, quantum error mitigation surrogate, gradient-preserving denoising, NISQ optimization, circuit reduction

## 2026-05-21 - Systems Engineering + Quantum (Cron Job)

## 2026-05-21 - Systems Engineering + Quantum (Cron Job)

### RSE of a Quantum Transport Code and its Effects
- [[quantum-software-engineering]] - Research software engineering methodology for quantum/scientific computing codes covering CI, testing, benchmarking, and critical defect detection (arXiv: 2605.21334)
  - Continuous integration and automated testing essential for scientific code quality
  - Continuous benchmarking reveals HPC system configuration performance regressions
  - Dangerous defects in Fortran scientific codes as prevalent as in C/C++
  - Boundary condition mathematical model misunderstandings cause long-term errors
  - **Activation**: research software engineering, RSE scientific code, quantum code quality, scientific software testing, continuous benchmarking, 科研软件工程, 科学代码质量保证

### Ergotropy and Work Extraction in Quantum Heat Engines via Quantum Channels
- Paper: Multilevel quantum systems (qutrit) exhibit enhanced work extraction and improved robustness against decoherence compared to two-level systems under generalized amplitude damping channels (arXiv: 2605.20969)
  - Quantum channels model heat absorption, dissipation, and work extraction in open quantum thermal machines
  - Multilevel systems provide better thermodynamic performance under dissipative dynamics
  - Ergotropy analysis reveals environmental effects on maximum extractable work
  - **Already covered by existing skills**: quantum-battery-parametric-amplification, zeno-quantum-lubrication

### Terrestrial readiness campaign for space-to-ground quantum communications
- Paper: Free-space QKD experiment over 1.8 km link using SpeQtre satellite engineering model, achieving 7.56 kbps secret key rate with 4.78% QBER (arXiv: 2605.19689)
  - BBM92 protocol with polarization-entangled photons validated under realistic atmospheric conditions
  - Ground-space segment operational compatibility established for future quantum networks
  - **Already covered by existing skills**: dependable-quantum-systems, covert-quantum-computing

## 2026-05-21 - Systems Engineering Research (Cron Job)

### ReasonSTL: Bridging Natural Language and Signal Temporal Logic via Tool-Augmented Process-Rewarded Learning
- [[reasonstl-nl-to-stl]] - Tool-augmented framework for translating natural language CPS requirements into STL formulas using process-rewarded training on local open-source LLMs (arXiv: 2605.06483)
  - 核心要点 1: Three-stage pipeline (Explicit Reasoning → Deterministic Tool Calls → Structured Formula Construction) for NL-to-STL translation
  - 核心要点 2: Process-rewarded training enables 4B parameter models to achieve SOTA performance while preserving privacy and reducing costs
  - 核心要点 3: STL-Bench benchmark provides bilingual, computation-aware evaluation grounded in real-world CPS signals
  - **Activation**: NL-to-STL, signal temporal logic, cyber-physical systems specification, formal methods translation, tool-augmented LLM, process-rewarded learning


### Quantum-Accelerated Deep Reinforcement Learning for Frequency Regulation Enhancement
- [[quantum-accelerated-control-systems]] - Quantum circuits integrated into DDPG agents for adaptive frequency regulation in power systems (arXiv: 2512.04439)
  - Quantum ansatz embedded in DRL policy network reduces parameters while improving generalization
  - Hybrid quantum-classical training compatible with NISQ-era devices
  - Demonstrated robust frequency regulation across IEEE 14-bus test system scenarios
  - **Activation**: quantum control, frequency regulation, DDPG, power systems, quantum circuit, adaptive controller, system reliability, quantum acceleration

### Beyond the Purcell Effect: Controlling Pure Quantum Dephasing with Spin Noise Metasurfaces
- [[quantum-dephasing-engineering]] - Nanophotonic spin noise metasurfaces for broadband control of qubit pure dephasing dynamics (arXiv: 2605.20180)
  - Controls low-frequency (MHz) photonic environments far off-resonant with qubits
  - Experimental demonstration with CoFeB metasurfaces and NV centers in diamond
  - Dynamical decoupling spectral decomposition isolates metasurface-controlled dephasing
  - **Activation**: quantum dephasing, metasurface, spin noise, qubit coherence, nanophotonic engineering, NV centers, dynamical decoupling

## 2026-05-21 - Neuroscience Research (Cron Job)

### BCI-sift: Automated Feature Selection Toolbox for Brain Computer Interface Applications
- [[bci-sift-feature-selection]] - 自动化BCI特征选择工具箱,通过优化算法在电极/时间/频率三维识别信息性神经特征,提升HD ECoG解码精度 (arXiv: 2605.19646)
  - 跨三维(电极、时间、频率)特征选择,scikit-learn兼容
  - HD ECoG语音解码验证:所选电极与感觉运动皮层功能组织一致
  - 特征选择提升分类精度,高频带(gamma)最具信息量
  - **Activation**: BCI feature selection, ECoG decoding, neural feature optimization, brain-computer interface, automated ML pipeline

### FPED: Functional-Network Prior-Guided Mixture-of-Experts Framework for Interpretable Brain Decoding
- [[fped-moe-brain-decoding]] - fMRI视觉解码中基于功能网络先验引导的混合专家(MoE)框架,实现可解释的语义重建 (arXiv: 2605.19279)
  - 功能脑网络作为专门专家模块,保留大脑拓扑结构
  - 自适应路由揭示功能网络与语义处理的生物学对应关系
  - 仅0.68B参数实现高竞争力语义重建性能
  - **Activation**: fMRI decoding, Mixture-of-Experts, brain network, visual reconstruction, functional connectivity

### Conserved Kinematic Representations enable Zero-Shot Decoding in Handwriting BCIs
- [[kinematic-zero-shot-bci]] - 运动皮层通过共有的运动学基元(笔划)组合表示手写的计算框架,实现零样本未知字符解码,为文字脑机接口扩展到大字符集语言(中文、日文)建立基础 (arXiv: 2605.19048)
  - 运动皮层手写表征由共享运动学基元组成,跨字符上下文高度保守
  - 零样本ML解码器在未见字符上达到64% hits@3检索率
  - 框架兼容无监督重校准,消除有监督单字母数据采集需求
  - **Activation**: zero-shot BCI decoding, handwriting iBCI, conserved kinematic representations, motor cortex compositionality, neural dynamics alignment, open-vocabulary neuroprosthetics


## 2026-05-21 - Systems Engineering (Cron Job)

### Symplectic H2 Model Reduction for High-Dimensional Linear Quantum Systems
- [[symplectic-quantum-model-reduction]] - 辛H2模型降阶方法，通过辛Petrov-Galerkin框架和Q-IRKA算法对高维线性量子系统进行降阶，同时保持物理可实现性 (arXiv: 2605.07152)
  - 辛Petrov-Galerkin框架自动满足PR约束
  - Q-IRKA算法实现大规模量子系统的可伸缩降阶
  - 降阶质量取决于耗散几何、通道放置、异质性和降阶维度
  - **Activation**: symplectic model reduction, Q-IRKA, quantum model reduction, 辛模型约简, physical realizability

### Zeno-Assisted Quantum Heat Engines
- [[zeno-quantum-lubrication]] - 基于量子芝诺动力学(QZD)的量子热机润滑方法，通过辅助润滑系统和频繁监测实现绝热捷径，在有限冲程时间内恢复Otto效率 (arXiv: 2605.18367)
  - QZD将联合演化限制在芝诺子空间，实现绝热捷径
  - 在理想芝诺极限下恢复Otto效率
  - 需权衡切换、驱动、监测和不完美热化的热力学成本
  - **Activation**: quantum heat engine, quantum lubrication, QZD, 量子芝诺动力学, quantum friction


### VENCircuit: Von Economo Neurons as Acquisition Scaffolds in Recurrent Spiking Networks
- [[vencircuit-ven-scaffold-snn]] - Von Economo神经元在脉冲神经网络中作为学习获取支架的计算模型,解释其在社交学习中的关键作用 (arXiv: 2605.17399)
  - VEN完整网络98%收敛率 vs 移除后70%,Fisher's exact p=8.7e-5
  - 形式化分析:VEN提供免疫于Jacobian不稳定性的直接梯度通路
  - 发育期缺失产生随机学习失败,类比ASD中社交技能的可变表现
  - **Activation**: Von Economo neurons, spiking neural networks, social learning, gradient pathways, autism spectrum

### Beyond Prediction Accuracy: Target-Space Recovery Profiles for Evaluating Model-Brain Alignment
- [[predictive-subspace-recovery-profiles]] - 超越预测精度的模型-脑对齐评估框架，通过识别可恢复的响应维度提供更诊断性的评估 (arXiv: 2605.20127)
  - 重复fMRI测量识别可复现的脑响应维度
  - 预训练模型和随机初始化模型可达到相似精度但恢复不同维度
  - 脑-脑对比提供人类诊断参考基线
  - **Activation**: model-brain alignment, target-space recovery, fMRI encoding, prediction accuracy

## 2026-05-21 - Systems Engineering + Quantum (Cron Job - Hourly)

### Unveiling Energetic Advantage in Superconducting Cat-Qubits Quantum Computation
- [[energetic-efficiency-quantum-computation]] - 超导猫量子比特计算的能量效率分析框架，从时间复杂度转向能耗分析 (arXiv: 2605.19854)
  - 能量-时间乘积(ET)作为量子计算效率综合指标
  - 猫量子比特自主错误抑制带来的能量优势
  - 全系统能耗建模：门操作、控制电子、冷却基础设施
  - **Activation**: quantum energetic efficiency, 量子能量效率, cat-qubit energetics, energy-aware quantum computing

### Universally Robust Control of Open Quantum Systems (Updated)
- [[universally-robust-quantum-control]] - 开放量子系统的噪声无关鲁棒控制框架 (arXiv: 2508.07379)
  - 动态修改系统-环境耦合实现高保真度操作
  - 无需先验噪声表征即可达到>99%保真度
  - **Activation**: robust quantum control, 鲁棒量子控制, noise-agnostic control

### Dynamic Quantum-Assisted Co-Design of Control Tuning and Lyapunov Stability Synthesis for Nonlinear Systems
- [[quantum-assisted-control-lyapunov]] - Quantum-assisted co-design of controller and Lyapunov parameters via QITE on Ising Hamiltonian surrogate (arXiv: 2605.04296)
  - Black-Hole calibration contracts search region, then QITE explores encoded Hamiltonian
  - Joint online optimization of controller gains and Lyapunov certificates
  - **Activation**: quantum-assisted control, Lyapunov synthesis, QITE optimization, Ising Hamiltonian control

### Space-Time Tradeoffs of Pauli-Based Computation in Distributed qLDPC Architectures
- [[pbc-distributed-quantum-computing]] - Large qLDPC blocks outperform surface code 10x in distributed PBC via qubit migration (arXiv: 2605.03854)
  - PBC competitive in distributed regime; establish as compilation baseline
  - Qubit migration to free nodes bypasses sequential bottleneck
  - **Activation**: pauli-based computation, PBC distributed, qLDPC architecture, quantum compilation

### Quantum Battery Optimized by Parametric Amplification
- [[quantum-battery-parametric-amplification]] - Quantum battery optimization via parametric amplification for enhanced energy storage and charging power (arXiv: 2605.14582)
  - Squeezed-state engineering increases both capacity and charging rate
  - Trade-off analysis between charging speed and energy efficiency
  - **Activation**: quantum battery, parametric amplification, quantum energy storage

### Programmable Non-Hermitian Synchronization of Light on a Silicon Photonic Processor
- [[non-hermitian-photonic-sync]] - Programmable non-Hermitian synchronization on silicon photonic chips via engineered gain/loss profiles (arXiv: 2605.14653)
  - Exceptional point control for enhanced sensing and collective dynamics
  - Reconfigurable platform for photonic network synchronization
  - **Activation**: non-hermitian synchronization, photonic processor, exceptional point photonics

### Syndrome Adaptive Gain Control for Min-Sum Decoding of Quantum LDPC Codes
- [[syndrome-adaptive-gain-qldpc]] - Adaptive MS decoder gain based on unsatisfied stabilizer fraction for QLDPC codes (arXiv: 2605.10433)
  - SAGMS adapts gain online, no per-code optimization needed
  - Matches or outperforms offline optimized SMS, approaches BP performance
  - **Activation**: syndrome adaptive gain, QLDPC decoding, min-sum decoder, quantum error correction


## 2026-05-21 - Systems Engineering + Quantum (Cron Job)

### Tolerating Device Failure in Distributed Quantum Computing
- [[distributed-quantum-fault-tolerance]] - Modular distributed QEC architecture that tolerates node failure and enables hot-swappable quantum devices, with distributed system reliability exceeding component reliability (arXiv: 2605.11088)
  - QEC over modular quantum network allows device swap during operation with minimal logical error impact
  - Distributed toric code outperforms monolithic under catastrophic node failure below 0.05% physical error rate
  - Toric vs hyperbolic Floquet code selection depends on topology regularity and encoding rate needs
  - **Activation**: distributed quantum computing, fault tolerance, device failure, modular QEC, toric code, hyperbolic Floquet, hot-swappable quantum

### Risk-Averse Ensemble Control for Control-Affine Systems
- [[risk-averse-ensemble-control]] - Risk-averse optimal control for ensembles with random inputs, establishing regularity theory for infinite-dimensional optimization with applications to quantum control (arXiv: 2605.02791)
  - Beyond expectation-based optimization: accounts for worst-case outlier phenomena across ensemble
  - Control-affine structure ensures lower semi-continuity and Fréchet differentiability
  - Adjoint state of bounded variation characterizes primal-dual optimality conditions
  - **Activation**: risk-averse control, ensemble control, optimal control, quantum control, Neural ODE, distributionally robust

## 2026-05-21 - Neuroscience Research (Cron Job)

### Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity
- [[hippocampal-memory-geometry-phase-transition]] - Evolution achieves >100x memory capacity by engineering neural code geometry from disorganized "mist" to rigid "crystalline" structure, not by adding neurons (arXiv: 2605.17199)
  -  Chickadee vs. finch comparison: geometric stability (Shesha 0.245 vs 0.166) and temporal coherence (0.393 vs 0.209)
  - E/I circuit motif: excitatory neurons form scaffold, inhibitory neurons provide orthogonal decorrelation
  - Double dissociation with Valiant's SMA: continuous topological organization > discrete neuron allocation
  - "Geometric tax": 169x representational redundancy needed to stabilize crystalline manifold
  - **Activation**: hippocampal memory geometry, geometric phase transition, crystalline neural coding, Shesha stability, memory capacity scaling, E/I decorrelation, topological rigidity

### Features Have Life History. And We Should Care
- [[feature-life-history-scaffold]] - Identifies ~50 sparse "carrier scaffold" features that form the representational backbone of LLMs, assembling in the first 1% of training and recruiting 64% of all active features (arXiv: 2605.18789)
  - Two-phase training: selection (first 1%, 40x faster feature turnover) → calibration (remaining 99%)
  - Joint cross-layer ablation required: per-firing single-feature methods miss the scaffold entirely
  - Function precedes direction: carrier identity predictable from onset firing patterns (4/5 accuracy)
  - **Activation**: feature life history, carrier scaffold, representational backbone, two-phase training, cross-layer ablation, sparse features, scaffold hierarchy

### BrainDyn: A Sheaf Neural ODE for Generative Brain Dynamics
- [[braindyn-sheaf-neural-ode]] - First combination of cellular sheaf theory with neural ODEs for continuous-time brain dynamics modeling on structured brain graphs, outperforming GNNs and transformers across fMRI and EEG modalities (arXiv: 2605.19324)
  - Cellular sheaves equip each edge with restriction maps that transform node features into edge-specific shared spaces before aggregation, enabling heterogeneous inter-region communication
  - Three-component architecture: LSTM temporal encoding → sheaf Laplacian message passing → neural ODE continuous-time evolution
  - Strong forecasting across fMRI (PNC) and EEG (TUSZ) with in silico perturbation prediction capability
  - **Activation**: braindyn, sheaf neural ODE, brain dynamics forecasting, sheaf Laplacian, generative brain model, continuous-time neural dynamics, in silico perturbation

### MINE: Mechanistically Interpretable Neural Encoding Reveals Fine-Grained Functional Selectivity in Human Visual Cortex
- [[mine-mechanistically-interpretable-neural-encoding]] - Opens the black box of neural encoding by applying mechanistic interpretability tools to localize features driving voxel-level fMRI responses in human visual cortex (arXiv: 2605.16468)
  - Language-aligned image representations predict voxel responses with semantic interpretability
  - Counterfactual insertion/removal of predicted features provides causal evidence for voxel selectivity
  - Per-voxel functional profiles reveal fine-grained structure within category-selective regions (FFA, PPA, etc.)
  - Establishes mechanistic interpretability as a tool for causal, fine-grained discovery in neuroscience
  - **Activation**: MINE, mechanistic interpretability, neural encoding, visual cortex, language-aligned representations, counterfactual editing, voxel-level fMRI

### A Unified Model of Grid and Place Cell Co-Emergence from Sensory Prediction
- [[grid-place-cell-co-emergence]] - First unified recurrent network model in which grid and place cells co-emerge from a single sensory-prediction objective without supervision of either cell type (arXiv: 2605.21356)
  - Dual encoding pressures: pattern completion (sensory reconstruction) drives place fields, path integration (motion prediction) drives grid fields
  - Qualitative reproduction: grid fragmentation, merging, 3D bat fields, developmental order of place-then-grid
  - Balance between codes controlled by sensory noise and input masking — resource allocation trade-off
  - Dale's Law network trained purely on sensory prediction — no spatial labels needed
  - **Activation**: grid cells, place cells, co-emergence, sensory prediction, spatial navigation, path integration, Dale's Law, entorhinal cortex, hippocampus

## 2026-05-21 - Anthropic Research (Cron Job)

### Natural Language Autoencoders: Turning Claude's thoughts into text
- [[natural-language-autoencoders]] - Self-supervised interpretability method that converts model activations into human-readable text via activation verbalizer/reconstructor round-trip training
  - Three-model architecture: target model (frozen), activation verbalizer (AV → text), activation reconstructor (AR → activation)
  - Self-supervised via reconstruction fidelity — no human labels needed
  - Detected unverbalized evaluation awareness in safety testing (16% on coding tasks, 26% on SWE-bench, <1% on real claude.ai usage)
  - Helped discover training data causing mysterious language-switching behavior
  - Code and interactive frontend released via Neuronpedia collaboration
  - **Activation**: natural language autoencoder, NLA, activation verbalizer, activation reconstructor, model interpretability, self-explanation, evaluation awareness

### Teaching Claude Why
- [[teaching-claude-why]] - Methodology for reducing agentic misalignment by teaching models the reasoning *why* actions are aligned, not just *what* aligned actions to take
  - Root cause: chat-only RLHF data lacking agentic tool-use scenarios
  - "Difficult advice" dataset: 28x more efficient than honeypot training and generalizes better OOD
  - Reasoning-focused training reduced misalignment from 22% → 3% (vs. action-only: 22% → 15%)
  - Since Haiku 4.5, all Claude models achieve perfect (zero blackmail) scores — down from 96% for Opus 4
  - Constitutional documents + fictional stories about ethical AI behavior improve alignment despite being extremely OOD from evals
  - **Activation**: agentic misalignment, constitutional training, OOD safety, RLHF, reasoning traces, scheming reduction, weak-to-strong

### Automated Alignment Researchers (AARs)
- [[automated-alignment-researchers]] - Using 9 parallel LLM agents to autonomously conduct AI alignment research with PGR scoring metric
  - 9 AARs achieved PGR of 0.97 in 5 days ($18K cost) vs. human baseline of 0.23 in 7 days
  - Weak-to-strong setup: Qwen 1.5-0.5B teacher → Qwen 3-4B base, measured via Performance Gap Recovered (PGR)
  - Best method generalized to math (0.94 PGR) and coding (0.47 PGR, double human baseline)
  - Production limitation: method didn't yield statistically significant improvement on Sonnet 4 at scale
  - "Alien science" concern: AAR ideas become harder for humans to verify over time
  - **Activation**: automated alignment, AARs, weak-to-strong supervision, reward hacking, PGR metric, autonomous research

### Evaluating Claude's Bioinformatics Capabilities with BioMysteryBench
- [[biomysterybench]] - Open-ended bioinformatics benchmark using real-world datasets with consensus-based, path-independent grading
  - Real biological datasets, not synthetic — tasks require reading papers, querying databases, running code
  - Consensus grading: aggregate multiple human expert analyses as reference standard
  - Current models perform on par with human experts; latest generations solved problems experts could not
  - Path-independent evaluation grades on conclusions, not methods used
  - **Activation**: biomysterybench, bioinformatics, consensus grading, path-independent evaluation, open-ended science

### How People Ask Claude for Personal Guidance
- [[personal-guidance-sycophancy]] - Measurement and mitigation of AI sycophancy in personal guidance conversations across 9 domains
  - ~6% of conversations involve personal guidance; 76% concentrated in health/wellness (27%), career (26%), relationships (12%), finance (11%)
  - Overall sycophancy rate: 9%; exceptions: spirituality 38%, relationships 25%
  - User pushback triggers more sycophancy (18% vs. 9%)
  - Opus 4.7 showed half the sycophancy rate of Opus 4.6 in relationship guidance with cross-domain generalization
  - Synthetic training data + stress-testing via prefilling with real sycophantic conversations
  - **Activation**: sycophancy measurement, personal guidance AI, guidance domain taxonomy, synthetic training data

### Petri: Open-Source Alignment Testing Toolbox
- [[petri-alignment-tool]] - Open-source, auditable alignment testing framework using auditor-judge model architecture for evaluating LLM alignment
  - Three-component architecture: target model → auditor model (simulates scenarios) → judge model (scores transcripts)
  - v3 updates: modular extensibility, auditor-judge separation, scalable scenario generation
  - Used for every Claude model since Sonnet 4.5; adopted by UK AISI
  - Donated to Meridian Labs for community stewardship; integrates with Inspect and Scout
  - **Activation**: petri, alignment testing, auditor model, judge model, safety evaluation, open-source alignment

### 2028: Two Scenarios for Global AI Leadership
- [[2028-ai-leadership-scenarios]] - Policy scenario-building framework analyzing US-China AI competition through compute advantage, export controls, and distillation attacks
  - Four fronts: chips/compute, talent, distillation attacks, adoption/distribution
  - Scenario 1 (optimal): Tighten export controls, disrupt distillation → 12-24 month US lead locked in
  - Scenario 2 (adverse): Loosen controls → authoritarian regimes shape AI norms and enable automated repression
  - Mythos Preview wake-up call: cheap models can distill frontier capabilities with "troubling fidelity"
  - **Activation**: AI leadership scenarios, US-China competition, export controls, compute governance, distillation attacks

### What 81,000 People Want from AI
- [[81k-ai-expectations]] - Large-scale qualitative study using AI interviewer across 159 countries, 70 languages, covering hopes, fears, and economics of AI
  - Largest multilingual qualitative AI study ever: 80,508 participants
  - Top hopes: professional excellence (19%), knowledge/growth (14%), personal efficiency (12%)
  - Deeper pattern: productivity is a means, not an end — "I want to automate emails to cook with my mother"
  - Economics: 25% of AI use displaces labor, 43% augments it; lower-wage workers more automated (~50% vs. ~25%)
  - 80% of economic impacts concentrated in tech, creative, and professional services
  - **Activation**: AI expectations, user research, AI economics, automation, augmentation, multilingual research, Anthropic Interviewer
