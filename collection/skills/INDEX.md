
## 2026-06-03 - Quantum ML Healthcare Research (Cron Job)

### Quantum machine learning for smart healthcare applications
- [[quantum-ml-healthcare]] - Enhanced existing skill with smart healthcare patterns and QML-for-genomics methodology (Crossref: 10.53388/mdm202609013)
  - QML applied to smart/IoT healthcare ecosystems, wearable integration with quantum edge computing
  - **Activation**: smart healthcare, quantum ML healthcare, QML genomics, quantum edge computing

### Quantum Machine Learning Algorithms for Genome Disease Diagnosis
- [[quantum-ml-healthcare]] - QML for high-dimensional genomic SNP data classification (Crossref: 10.22541/au.175924949.93262371/v1)
  - Handles ultra-high-dimensional genomic feature spaces where classical ML struggles
  - **Activation**: quantum genome, SNP classification, genomic disease diagnosis, high-dimensional QML

## 2026-06-02 - Neuroscience Research (Cron Job)

### On the synaptic matrix eigenvalues of sparsely connected neural networks
- [[synaptic-matrix-eigenvalue-analysis]] - 突触矩阵谱分析方法论，研究不同稀疏类型对网络稳定性、瞬态动力学和记忆容量的影响，统计分析替代精确矩阵确定 (arXiv: 2606.00326)
  - 稀疏连接网络的突触矩阵特征值分布决定动力学特性
  - 稳定性：λ_max < 1 → 网络稳定；记忆容量：谱宽度 → 存储能力
  - 不同稀疏机制（随机/结构/时变/稳态）产生不同谱特征
  - **Activation**: 突触矩阵, 特征值, 稀疏连接, spectral analysis, 网络稳定性, 记忆容量, synaptic sparsity

### SHARP: Sleep-based Hierarchical Accelerated Replay for Long Range Non-Stationary Temporal Pattern Recognition
- [[sleep-replay-acceleration-sharp]] - 神经科学启发的分层加速回放框架，分离记忆模块和模式识别模块，实现无BPTT的长程信用分配，受啮齿动物慢波睡眠加速回放启发 (arXiv: 2606.00732)
  - 双模块架构：记忆模块累积结构化历史 + 模式识别模块从记忆学习
  - 睡眠阶段加速回放（~20x压缩）整合到高层记忆表示
  - 流式设置下长程非平稳时序模式识别，无需回访过去观测
  - **Activation**: 睡眠回放, 加速回放, SHARP, 时序学习, 长程依赖, 流式学习, 慢波睡眠, hierarchical replay

### Updating the Standard Neuron Model in Artificial Neural Networks
- [[updated-neuron-model-ann]] - Challenges 50-year-old point neuron assumption; demonstrates cortical cell model advantages without parameter increase: enhanced expressivity, robustness, learning speed, reduced memorization, less training data needed (arXiv:2605.30370)
  - Point neuron model from 1950s neuroscience proven too simplistic for fundamental neural processes
  - Cortical cell replacement maintains same computational efficiency while improving performance
  - No parameter increase required - same complexity, better biological fidelity
  - **Activation**: neuron model, ANN, point neuron, cortical cells, expressivity, robustness, learning speed, biological realism, 标准神经元模型

### Supervised Training Rapidly Degrades Early Visual Cortex Alignment Across Biologically Plausible Learning Rules
- [[supervised-training-degrades-visual-cortex-alignment]] - Untrained networks match/exceed trained networks in brain alignment; single epoch degrades V1 alignment 25-90%, BP most severe (-0.080), PC/STDP better preservation (~-0.04) (arXiv:2605.30556)
  - RSA analysis: 720 THINGS images, 3 subjects, 6 visual ROIs, 8 training checkpoints
  - Global error signals (BP) reshape early representations aggressively; local rules preserve brain-like structure
  - Inductive biases capture low-level visual statistics without learned distortions
  - **Activation**: visual cortex, brain alignment, training degrades, backpropagation, predictive coding, STDP, RSA, fMRI, untrained networks, learning rules, 视觉皮层对齐

### The Metastable Mind: Neural Underpinnings of Naturalistic Cognition Through the Synthesis of Event Segmentation and Metastable Neural States
- [[metastable-mind-event-segmentation]] - Unified framework synthesizing Event Segmentation (ES) cognitive theory and Metastable Neural Activity (MNA) mechanistic approach; demonstrates both study the same metastable neural states from different perspectives (arXiv: 2605.31473)
  - Three core principles: spatio-temporally nested hierarchy, predictive models underlying states, modular processing intervals with boundary reconfiguration
  - Neural states as fundamental computational units of cognition with state duration, content, and boundaries
  - Longer-duration states in higher-order regions constrain and shape states in faster-operating regions
  - **Activation**: metastable, neural states, event segmentation, metastable mind, 亚稳态, 事件分割, cognitive states, brain state hierarchy

### MindVoice: Reconstructing Intelligible Speech from Non-invasive Neural Signals with Pretrained Priors
- [[mindvoice-neural-speech-reconstruction]] - Neuro-to-speech framework using pretrained models to compensate for incomplete semantic/acoustic information in EEG/MEG; disentangled dual pathway (semantic + acoustic) + in-context voice cloning (arXiv: 2605.31173)
  - Semantic pathway recovers high-level content, acoustic pathway estimates fine-grained attributes
  - Fuses representations with powerful speech generation models for natural intelligible utterances
  - EEG: WER 45-55%, MEG: WER 35-40%, substantial improvement over baseline unintelligible results
  - **Activation**: MindVoice, neural speech reconstruction, speech BCI, EEG speech, MEG speech, 神经语音重建

### Score Broadcast and Decorrelation: A General Framework for Broadcast-Based Credit Assignment
- [[score-broadcast-decorrelation-credit-assignment]] - Principled framework for biologically plausible credit assignment across general differentiable losses; theoretical grounding for three-factor learning rule with neuromodulatory factor as broadcast loss score (arXiv: 2605.30638)
  - Orthogonality principle: Output_Score ⟂ Hidden_Activation (when optimal score has conditional mean zero)
  - Unifies broadcast-based credit assignment across cross-entropy, Bregman divergences, proper scoring rules, exponential-family NLLs
  - Score vector expansion enriches broadcast signal while preserving orthogonality framework
  - No weight transport → biologically plausible alternative to backpropagation
  - **Activation**: SBD, score broadcast, decorrelation, credit assignment, three-factor learning, error broadcast, 生物可塑性

## 2026-06-01 - Neuroscience + Quantum Mechanics (Cron Job)

### A Quantum-Analogue Formalism for Modeling Supraliminal Information Processing
- [[quantum-supraliminal-cloud-formalism]] - Cloud-function formalism combining neural field theory with quantum-analogue modeling for large-scale brain sensory processing; separates kernel (information dynamics) from amplitude (mental representation intensity) (arXiv: 2605.25214)
  - Cloud function Ψ(x,t) = K(x,t) × A(x,t): kernel captures how information is processed, amplitude captures what is represented
  - First-person perspective formalization for subjective representation content in neural processing models
  - Quantum-analogue framework (not quantum physics in brain) handles contextual effects and incompatible observables
  - Supraliminal vs subliminal processing as phase transition in cloud function amplitude
  - **Activation**: quantum analogue, cloud function, supraliminal processing, neural field theory, mental representation, first-person perspective, cognitive dynamics, quantum cognition, sensory processing

### Quantum-Like Models of Cognition and Decision Making: Open-Systems and GKSL Dynamics
- [[gskl-quantum-cognition-dynamics]] - GKSL master equation methodology for cognitive psychology; models mental state evolution as dissipative open-system dynamics, identifies cognitive beats as multi-scale deliberation signatures (arXiv: 2604.18643)
  - Active vs Passive Hamiltonians: non-commutation with decision projections = cognitive agency signature
  - Cognitive beats emerge from competing Liouvillian channels at similar frequencies
  - Quantum escape from classical equilibria in strategic games (e.g., non-Nash Prisoner's Dilemma)
  - Beat envelope maps timing of peak readiness vs hesitation during conflicting cognitive states
  - **Activation**: GKSL, Lindblad, quantum cognition, open quantum systems, cognitive beats, decision dynamics, dissipative quantum, mental state evolution, quantum escape, non-Nash, Liouvillian channels, cognitive agency

### Winning Lottery Tickets in Neural Networks via Quantum-Inspired Classical Algorithm
- [[quantum-inspired-lottery-tickets]] - Classical dequantized algorithm for sparse subnetwork selection using ridgelet transform; O(poly(D)) runtime vs exp[O(D)] previous classical (arXiv: 2605.13979)
  - Ridgelet coefficients define importance distribution for hidden node sampling
  - Achieves comparable empirical risk to exact quantum sampling
  - Proves quantum advantage for this task can be achieved classically with polynomial scaling
  - **Activation**: lottery tickets, sparse subnetwork, quantum-inspired classical algorithm, ridgelet transform, neural network pruning, dequantization, optimized sampling

## 2026-05-31 - Neuroscience Research (Cron Job)

### Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons
- [[snn-sequence-timing-replay-v2]] - Spiking Temporal Memory (sTM) model for encoding sequence timing through sequential population activation; oscillatory background as clock signal for replay speed control (arXiv: 2605.22523)
  - Element duration represented by sequential activation of element-specific neuronal populations
  - Oscillatory background inputs serve as clock signal for flexible replay speed modulation
  - Unique sparse spatiotemporal patterns encode elapsed time
  - Replay speed correlates with global oscillatory activity (EEG/LFP)
  - **Activation**: sequence timing, replay speed, spiking temporal memory, oscillatory dynamics, sTM model, temporal encoding

## 2026-05-31 - Information Science + Quantum Mechanics (Cron Job)

### Full Characterization of Informative Subsets in Quantum Encrypted Cloning
- [[quantum-encrypted-cloning-information]] - Pauli-based quantum encrypted cloning protocol analysis; characterizes how quantum information distributes across signal-noise pairs while preserving no-cloning theorem (arXiv: 2605.27421)
  - Informative subset identification: which output pairs carry meaningful vs. noise information
  - Signal-to-noise ratio α per output determines extractable information
  - Collective measurement bounds via Holevo information
  - Redundancy vs. security tradeoff analysis for quantum communication
  - **Activation**: quantum encrypted cloning, informative subsets, signal-noise pairs, Yamaguchi Kempf, Pauli cloning, no-cloning redundancy

### Learning Logical Operations for Arbitrary Quantum Error Correction Codes
- [[learning-logical-operations-qec]] - VarEFTQC variational framework for discovering physical logical gate implementations tailored to hardware noise models, enabling transversal IQP gates for non-additive encodings (arXiv: 2605.28162)
  - Variational optimization discovers logical gates for non-standard QECCs
  - Noise-aware gate synthesis maximizes fidelity under realistic hardware noise
  - Bridges gap between non-additive code theory and physical implementation
  - Transversal IQP gate family discovery and characterization
  - **Activation**: VarEFTQC, logical gate learning, non-additive encoding, transversal gates, IQP gates, noise-aware QEC, variational error correction

### Quantum Speed Limit under Calibration Uncertainty
- [[quantum-speed-limit-calibration-uncertainty]] - Projected quantum speed limit methodology using quantum Fisher information to profile out nuisance parameters, establishing realistic operational speed bounds (arXiv: 2605.27423)
  - Standard QSLs overestimate speed when Hamiltonian parameters have calibration uncertainty
  - QFI-based projection separates interest parameters from nuisance parameters via Schur complement
  - Fisher information geometry provides Riemannian metric for speed bound computation
  - Calibration precision requirements derived from target evolution time
  - **Activation**: quantum speed limit, calibration uncertainty, QFI speed bound, nuisance parameters, projected speed limit, Fisher information geometry

## 2026-05-28 - Systems Engineering + Quantum Computing (Cron Job)

### Quantum-Native Maximum Likelihood Detection in Random Access Channel with Overloaded MIMO
- [[grover-mimo-detection]] - Quantum MLD for overloaded MIMO using Grover Adaptive Search with 65% rotation reduction via search space pruning (arXiv: 2605.19389)
  - Binary optimization formulation → QUBO, no penalty terms needed
  - GAS with search space reduction and optimal parameter settings via probability analysis
  - Quadratic speedup over classical exhaustive search in fault-tolerant regime
  - **Activation**: quantum mimo, grover search, overloaded MIMO, maximum likelihood detection, GAS, quantum wireless

### Quantum Model for CVRPTW
- [[grover-cvrptw-quantum]] - Qubit-efficient quantum CVRPTW solver using Grover Search with split-inspired modeling adding only O(N) qubits (arXiv: 2605.18393)
  - Quantum formulation of classical route-first-cluster-second decomposition
  - Oracle checks capacity and time-window feasibility
  - Linear qubit scaling vs O(N^2) for standard TSP formulations
  - **Activation**: quantum vehicle routing, CVRPTW, grover optimization, logistics quantum, quantum combinatorial optimization

## 2026-05-26 - Computer Science + Quantum Computing (Cron Job)

### QUTest: A Native Testing Framework for Quantum Programs
- [[quantum-native-testing-framework]] - Native quantum program testing using OpenQASM 3 pragma-based assertions with 12 assertion types spanning deterministic, statistical, and property-based verification (arXiv: 2605.19736)
  - Tests encoded as `.qasm` files with `//%` pragma comments, following Arrange/Act/Assert pattern
  - 12 assertion types: deterministic state checks, statistical distribution verification, property-based invariants
  - Budget-aware adaptive testing reduces unnecessary shot consumption
  - No host language dependency — pure QASM tests compatible with existing OpenQASM tools
  - **Activation**: quantum testing, qutest, openqasm, pragma assertions, quantum verification, quantum debugging

### Software Between Quantum and Machine Learning — And Down to Pulses
- [[pulse-level-quantum-computing]] - Pulse-level quantum computing methodology for designing, optimizing, and executing circuits at the control-pulse layer beyond gate abstractions (arXiv: 2605.21286)
  - Direct pulse-level control enables hardware-native operations and tailored error mitigation
  - Pulse schedule optimization reduces circuit depth and improves gate fidelity
  - Cross-platform pulse portability through hardware calibration abstraction
  - Dynamical decoupling and cross-resonance calibration at pulse layer
  - **Activation**: pulse level, quantum control, pulse optimization, quantum hardware, qubit control, dynamical decoupling

## 2026-05-26 - Neuroscience Research (Cron Job)

### Beyond Neural Activity Prediction: Probing Latent Representations in Mouse V1 Digital Twins
- [[v1-digital-twin-probing]] - Multi-level probing framework for evaluating latent representations in sensory cortex digital twins; linear decodability + unit tuning + population geometry (arXiv: 2605.23122)
  - Better models exhibit flatter hidden-population eigenspectra (higher-dimensional representations)
  - Models with comparable prediction accuracy differ substantially in latent representations
  - Three-level probing: linear decodability, latent-unit tuning, population geometry
  - **Activation**: V1 digital twin, latent representation probing, population geometry, mouse V1 encoding

### Contextual Role Modulates Object Representational Geometry in the Human Brain
- [[contextual-role-object-geometry]] - fMRI study showing dynamic remapping of object representations based on contextual role; double dissociation: action affordance vs semantic organization (arXiv: 2605.23111)
  - Target objects: action affordance; passive objects: semantic dimensions
  - Parietal action network vs occipito-temporal recognition network
  - Context-invariant visual structure outside context-specific networks
  - **Activation**: representational geometry, fMRI object recognition, contextual modulation, action affordance

### Sparse Autoencoders Map Brain-LLM Alignment onto Cortical Semantic Topography
- [[sae-brain-llm-cortical-topography]] - SAEs from mechanistic interpretability bridge brain-LLM alignment with cortical semantic topography prediction. Decomposes GPT-2 XL and Llama-3.1-8B into 16K-32K interpretable features per layer (arXiv: 2605.23035 | CoNLL 2026)
  - Semantic features alone recover 94% of peak encoding performance (R²=0.94)
  - Five semantic subcategories map onto distinct brain regions (Spearman ρ, p<0.05)
  - SAE features predict reading times beyond lexical controls (ΔR², p<0.001)
  - Cross-linguistic generalization: English, Chinese, French
  - **Activation**: SAE, sparse autoencoder, mechanistic interpretability, brain encoding, cortical topography, semantic feature, LLM interpretability, fMRI encoding

### Beyond Neural Activity Prediction: Probing Latent Representations in Mouse V1 Digital Twins
- [[v1-digital-twin-latent-probing]] - Multi-level representational probing framework for evaluating digital twins of mouse V1. Probes latent representations across three levels: linear decodability, latent-unit tuning, population geometry (arXiv: 2605.23122)
  - Models with similar prediction accuracy rely on different latent representations
  - Better neural prediction correlates with stronger probe accuracy
  - Highly predictive models show flatter eigenspectra (higher-dimensional representations)
  - Establishes multi-level probing as necessary complement to accuracy metrics
  - **Activation**: digital twin, V1, representational probing, population geometry, orientation selectivity, eigenspectrum, mouse V1

### Active Sensing Subserves Task-Level Control
- [[active-sensing-subserves-task-control]] - Proposes that active sensing movements (explore/exploit modes) emerge inevitably from the combination of adaptive sensors, movement-sensing linkage, and task-level control, rather than from sensory uncertainty minimization (arXiv: 2605.22988)
  - Supported by both empirical data and mathematical theory
  - Animals switch between 'explore' (dynamic movements shaping sensory feedback) and 'exploit' (slower compensatory movements) modes
  - Framework expressed in control theory language for robotics applications
  - **Activation**: active sensing, sensorimotor control, explore-exploit, task-level control, adaptive sensors, feedback control

### Integrating Cognitive Load and Embodied Cognition Through Multi-Scale Attractors
- [[cognitive-load-multiscale-attractors]] - Formal rapprochement between cognitive load theory and embodied cognition by reconceptualizing psychological representations as dynamic multiscale attractors within a temporal-hierarchical prediction architecture (arXiv: 2605.23012)
  - Two theories describe complementary, timescale-separated processes
  - Learning as attractor sculpting across coupled temporal layers
  - Five testable predictions: cross-timescale interference, embodied load reduction, metacognition as timescale coupling
  - **Activation**: cognitive load, embodied cognition, multiscale attractors, dynamical systems, hierarchical predictive processing, attractor sculpting

### Contextual Role Modulates Object Representational Geometry in the Human Brain
- [[contextual-role-object-representational-geometry]] - fMRI study showing neural remapping of object representations depending on moment-to-moment contextual roles (passive vs. action target) during naturalistic movie viewing (arXiv: 2605.23111)
  - Double dissociation: target objects organized by action affordance, passive objects by semantic dimensions
  - Parietal action network vs. occipito-temporal visual recognition network
  - Visual representations remain context-invariant outside specific networks
  - **Activation**: object representation, fMRI, contextual role, action affordance, semantic representation, representational geometry, naturalistic viewing

### GazeBehavior Annotation Toolkit (GBAT)
- [[gaze-behavior-annotation-toolkit]] - Deep-learning toolkit for automatic annotation of egocentric eye-tracking and video data of child-caregiver interaction. Supports post-hoc synchronization, gaze target categorization, and behavioral coding (arXiv: 2605.22962)
  - AI-powered video synchronization across multiple streams
  - Semi-automatic gaze target and behavioral annotation
  - Scalable for large-scale longitudinal developmental studies
  - **Activation**: GBAT, gaze behavior, eye tracking, egocentric video, child-caregiver interaction, behavioral annotation, developmental psychology

### Brain-LLM Alignment Tracks Training Data, Not Typology
- [[brain-llm-alignment-training-data]] - Demonstrates that the apparent English advantage in brain-LLM alignment is an artifact of training data composition, using fMRI from 112 participants across 3 languages (arXiv: 2605.23032 | CoNLL 2026)
  - Chinese-dominant Baichuan2-7B reverses alignment gradient entirely
  - Typological distance independently affects alignment degradation in syntax regions (IFG)
  - Tokenization fertility accounts for ~60% of optimal encoding layer shift
  - **Activation**: brain-LLM alignment, cross-linguistic, training data dominance, fMRI, typological distance, neurolinguistics

### Geometric Origin of Exact Mean-Field Reductions
- [[geometric-mean-field-lorentzian-ansatz]] - Proves the Cauchy-Lorentz family is the unique connected two-dimensional family of continuous probability densities invariant under projective transport induced by Riccati dynamics, providing a unified geometric foundation for Ott-Antonsen and Montbrió-Pazó-Roxin reductions (arXiv: 2605.23669)
  - Explains why Lorentzian Ansatz works and Gaussian closures fail
  - Unified geometric foundation for neural mass model reductions
  - Identifies structural condition for exact two-parameter reductions
  - **Activation**: Lorentzian Ansatz, mean-field reduction, Ott-Antonsen, Montbrió-Pazó-Roxin, neural mass model, Riccati dynamics, Cauchy distribution

### Naturalistic Computational Cognitive Science
- [[naturalistic-computational-cognitive-science - repo]] - Framework for building generalizable cognitive science models spanning the full scope of natural situations and behaviors by integrating AI progress with naturalistic experimental paradigms (arXiv: 2502.20349, v5 updated May 2026)
  - Reviews evidence that naturalistic paradigms elicit distinct behaviors and cognitive processes
  - Discusses how AI learning from naturalistic data yields qualitatively different generalization patterns
  - Practical guidance for cumulative progress in naturalistic computational cognitive science
  - **Activation**: naturalistic cognitive science, computational cognitive science, AI for cognitive modeling, naturalistic paradigms, generalizable theories

## 2026-05-26 - Computer Science + Quantum Computing (Cron Job)

### Off-line quantum-advantage feature extraction for industrial production
- [[quantum-feature-surrogates]] - Framework enabling quantum-advantaged feature extraction at production scale via quantum-to-classical surrogate distillation. Quantum processor processes small representative subsamples, trains classical surrogate for near-zero-cost full dataset inference (arXiv: 2605.19801)
  - Subsample must faithfully represent full dataset distribution
  - Quantum processor acts as "teacher of representations"
  - Classical surrogate enables production inference without quantum hardware
  - **Activation**: quantum feature surrogate, production quantum ML, quantum subsample teacher, quantum-to-classical distillation

## 2026-05-25 - Quantum Computing Research (Cron Job)

### CRiSP: Clifford RL for State Preparation — VQA Initialization via Reinforcement Learning
- [[crisp-rl-clifford-vqa]] - Reinforcement learning framework using Neural-Guided MCTS with Transformer-based policy (trained via self-play) to discover optimal Clifford gate prefixes for VQA warm-start initialization, achieving 3.17× mean improvement in energy accuracy over state-of-the-art methods (arXiv: 2605.23138)
  - Formulates Clifford prefix selection as sequential decision-making with MCTS
  - Uses Transformer policy trained via self-play with curriculum learning
  - Polynomial-time classical stabilizer simulation during search
  - Up to 22 qubits, 1,370 parameters benchmarked
  - 3.17× mean / 45.02× max improvement in energy accuracy
  - Compatible with QAOA and VQE without modifying circuit architecture
  - **Activation**: CRiSP, Clifford RL, VQA initialization, MCTS quantum, Transformer quantum, stabilizer simulation, QAOA warm-start, barren plateau

### Sparse Mamba Decoder for Quantum Error Correction
- [[sparse-mamba-decoder-qec]] - Defect-centric neural decoder for surface code QEC using Mamba state-space model that processes only active detection events (k ≪ d²R), achieving O(k) complexity with 24-57 μs constant latency across d=3-9 (arXiv: 2605.17156)
  - First defect-centric neural decoder exploiting syndrome sparsity
  - Uses 13D feature representation per defect event
  - Mamba/SSM backbone for linear-time sequence processing
  - 95-467× faster than Tesseract near-MLD decoder
  - Up to 49% MWPM logical error rate reduction at d ≤ 5 (SI1000 noise)
  - Validated on Google Sycamore experimental data
  - 7.5M-16M parameters on commodity NVIDIA GPUs
  - **Activation**: Sparse Mamba Decoder, SMD, quantum error correction, surface code, defect-centric decoding, Mamba, state-space model, QEC neural decoder

## 2026-05-25 - Neuroscience Research (Cron Job)

### Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function
- [[functional-whole-brain-models-fwbm]] - Unified modeling paradigm (fWBMs) integrating bottom-up whole-brain modeling with top-down neuroconnectionism, defined by four minimal criteria: structural grounding, continuous-time dynamical realism, functional competence, and mappable observables (arXiv: 2605.18118)
  - Four minimal criteria: structural grounding in connectomes, dynamical realism, functional competence, mappable observables
  - Three-pillar roadmap: short-term hybrid models, mid-term integrated architectures, long-term closed-loop fWBMs
  - Bridges two previously separate modeling traditions in computational neuroscience
  - **Activation**: fWBM, functional whole-brain model, whole-brain modeling, neuroconnectionism, brain dynamics, cognitive function, connectome

### A Simple Model of Co-Emergence of Grid and Place Fields
- [[grid-place-co-emergence]] - First unified recurrent network model instantiating Dale's Law where grid and place cells co-emerge from a single sensory-prediction objective without supervision of either type, reproducing grid fragmentation, wall-removal merging, 3D bat fields, and developmental ordering (arXiv: 2605.21356)
  - First single-objective model achieving grid-place co-emergence across 1,000 training configurations
  - Implements Dale's Law (excitatory/inhibitory neuron separation) for biological realism
  - Balance of grid vs. place codes modulated by sensory noise and masking levels
  - Reproduces grid fragmentation in hairpin mazes, wall-removal merging, lattice alignment across rooms
  - Explains developmental order: place cells precede grid cells
  - Two complementary encoding pressures: sensory reconstruction + next-state prediction
  - **Activation**: grid cells, place cells, co-emergence, Dale's Law, spatial navigation, hippocampal-entorhinal, recurrent network, sensory prediction

### Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons
- [[learning-sequence-timing-snn]] - Spiking Temporal Memory (sTM) model extending biologically inspired SNN framework to learn both order and precise timing of sequence elements with flexible replay speed modulation via oscillatory background input (arXiv: 2605.22523)
  - Extends sTM model from order-only to combined order-and-timing learning
  - Uses sequential neuronal population activation for timing encoding
  - Enables flexible replay speed modulation via oscillatory background clock signals
  - Links replay speed to EEG/LFP rhythms (theta, sharp-wave ripples)
  - Relevant to hippocampal replay, memory consolidation, and neuromorphic computing
  - **Activation**: sTM, spiking temporal memory, sequence timing, replay speed, oscillatory clock, hippocampal replay, spiking neural network

## 2026-05-23 - Anthropic Founder Playbook (中文精读版)

### Anthropic 创始人手册: Building an AI-Native Startup
- [[anthropic-founder-playbook-ai-native-startup]] - AI 原生创业四阶段方法论 (Idea/MVP/Launch/Scale)
  - Claude 生成: skill, anthropic-founder-playbook-ai-native-startup
  - 核心要点 1: Idea 阶段以调研驱动的验证为核心,出口标准是找到 Problem-Solution Fit
  - 核心要点 2: MVP 阶段需先定义架构(CLAUDE.md)再动手,避免 agentic 技术债复利
  - 核心要点 3: Launch 阶段把创始人从 builder 变成'设计做工作的系统'
  - 核心要点 4: Scale 阶段通过领域深度+集成深度+专有数据构建可防守护城河
  - Activation: 创业方法论, AI-native, 精益创业, founder-playbook


## 2026-05-23 - Economics, Investment + Quantum Mechanics (Cron Job)

### Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization
- [[hotstart-quantum-portfolio-optimization]] - Hot-starting methodology for quantum portfolio optimization by constructing compact Hilbert space around continuous optimum, reducing qubit requirements (arXiv: 2605.17623)
  - D-Wave hybrid is 99.3% classical decomposition with only 0.7% QPU time
  - Cardinality penalty creates dense rank-one term collapsing intended density benchmark
  - Constraint-native vs penalty-encoded interface analysis reveals source of performance gains
  - **Activation**: hot-start quantum optimization, 热启动量子组合优化, D-Wave hybrid audit, compact Hilbert space, QUBO reduction, quantum portfolio benchmark

### Quantum Portfolio Optimization with Expert Analysis Evaluation
- [[hotstart-quantum-portfolio-optimization]] - Expert Analysis Evaluation framework bridging computational quantum optimization with financial viability assessment for VQE and QAOA portfolios (arXiv: 2507.20532)
  - VQE and QAOA minimize cost but often violate financial criteria (diversification, risk exposure)
  - Expert judgment necessary to validate quantum-optimized portfolios for real-world application
  - Benchmark across asset universes, ansatz architectures, and circuit depths
  - **Activation**: expert analysis evaluation, 专家评估框架, quantum portfolio viability, VQE QAOA finance, quantum optimization benchmark

### Contextual Quantum Neural Networks for Stock Price Prediction
- [[contextual-quantum-neural-stock-prediction]] - Multi-asset stock price prediction using quantum batch gradient update (QBGU) and share-and-specify ansatz with logarithmic qubit overhead (arXiv: 2503.01884)
  - QBGU accelerates standard SGD in quantum applications with improved convergence
  - QMTL architecture enables simultaneous multi-asset training on same quantum circuit
  - Outperforms quantum single-task learning and captures inter-asset correlations
  - **Activation**: quantum stock prediction, 量子股票预测, QBGU, quantum multi-task learning, share-and-specify ansatz, QMTL finance

### hbar_E: An Action Constant for Quantum Economics
- [[quantum-economic-action-constant]] - Economic action constant (hbar_E) as structural analogue to Planck's constant for modeling macroeconomic regime transitions under radical uncertainty (arXiv: 2509.02647)
  - Non-commuting economic observables (X, P_X) derive uncertainty relations and semi-classical limit
  - hbar_E governs transitions between deterministic, probabilistic, and unstable dynamics
  - Double-well economic potential models boom/bust regime bifurcations
  - **Activation**: quantum economics, 量子经济学, economic action constant, hbar_E, macroeconomic regime transitions, canonical quantization economics

## 2026-05-22 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)

### Tensor Cookbook: Mastering Tensors through Diagrams
- [[tensor-cookbook-diagrams]] - Tensor network diagram methodology for simplifying tensor algebra, bridging quantum physics notation with machine learning and statistics (arXiv: 2605.16610)
  - Graphical Penrose notation reduces notational overhead for tensor contractions and decompositions
  - Diagrammatic differentiation rules for transparent gradient computation
  - Bridges quantum MPS/PEPS with ML tensor train/Tucker decompositions
  - **Activation**: tensor network diagrams, tensor cookbook, penrose notation, tensor contraction diagrams, 张量网络图, 张量图解

### Quantum Sufficiency for Self-Adjoint Statistical Models via Likelihood-Type Operators
- [[quantum-sufficiency-statistical-models]] - Quantum sufficiency on real *-subalgebras and real Jordan algebras extending classical sufficiency to quantum settings using likelihood-type operators (arXiv: 2604.23292)
  - Square-root likelihood ratios and symmetric logarithmic derivatives as fundamental self-adjoint likelihood-type objects
  - Minimal sufficient real *-subalgebras characterized by likelihood-ratio set + ρ-modular invariance
  - Koashi-Imoto decompositions for quantum channels preserving statistical structure
  - **Activation**: quantum sufficiency, self-adjoint statistical models, likelihood-type operators, symmetric logarithmic derivative, real Jordan algebra, Koashi-Imoto decomposition, quantum Fisher information

### Modeling and Resource Optimization for Quantum Oracles
- [[quantum-oracle-optimization]] - HRSE model and ASDT algorithm for optimal quantum oracle resource allocation under qubit constraints (arXiv: 2605.21380)
  - HRSE model enables formal oracle description and precise gate complexity analysis
  - ASDT algorithm reduces circuit depth by ~54% vs W-cycle under fixed qubit constraint
  - **Activation**: quantum oracle, HRSE, ASDT, oracle optimization, circuit depth, gate complexity

### An Exponential Sample-Complexity Advantage for Coherent Quantum Inference
- [[coherent-quantum-inference]] - Coherent quantum inference achieving exponential sample-complexity advantage over incoherent protocols (arXiv: 2605.21457)
  - Coherent protocols achieve O(1/eps) vs Omega(d/eps) sample complexity for purity amplification
  - Entanglement-breaking limit identifies optimal incoherent counterpart
  - **Activation**: coherent quantum inference, quantum purity amplification, sample complexity

### Flow loops and quantum groups
- [[flow-loops-quantum-groups]] - Connecting quantum group invariants with Morse flow dynamics for knot theory (arXiv: 2605.21382)
  - Morse flow loop counting yields two-variable series invariants for fibered knots
  - Proven correspondence with BPS q-series from quantum group Verma modules for braid-homogeneous knots
  - **Activation**: flow loops, quantum groups, knot invariants, Morse flows, BPS q-series

## 2026-05-21 - Systems Engineering + Quantum (Cron Job)

### Quantum End-to-End Learning for Contextual Combinatorial Optimization
- [[quantum-end-to-end-learning]] - First quantum end-to-end learning framework for contextual combinatorial optimization using QAOA with context re-uploading phase-separator (arXiv: 2605.20222)
  - Context re-uploading phase-separator jointly captures relations among contexts, uncertain coefficients, and optimal solutions
  - Stationarity-guaranteed end-to-end training on task loss without NP-hard solver calls
  - Substantially fewer parameters than classical benchmarks while maintaining competitive performance
  - **Activation**: quantum end-to-end learning, QEL, contextual combinatorial optimization, QAOA training, quantum surrogate policy, context re-uploading

### Bowtie VarQTE: Resource-Efficient Quantum State Preparation Primitive
- [[bowtie-varqte-quantum-state-prep]] - Hybrid classical-quantum framework leveraging causal light-cones to minimize quantum resources for variational quantum time evolution (arXiv: 2605.20331)
  - Causal light-cone exploitation enables classical simulation of causally relevant subcircuits
  - Exact parameter updates via McLachlan variational principle without requiring classical target state representation
  - Reduced quantum circuit depth compared to approximate quantum compilation (AQC)
  - **Activation**: bowtie varqte, variational quantum time evolution, quantum state preparation, causal light-cone, McLachlan variational principle, hybrid quantum-classical

## 2026-05-21 - Neuroscience Research (Cron Job)

### Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry
- [[platonic-representations-brain-universal-geometry]] - Evidence for shared neural geometry — subject-specific fMRI representations in visual cortex are approximately isometric across individuals and translatable via unsupervised orthogonal rotations (arXiv: 2605.20496)
  - Self-supervised encoder learns subject-specific embeddings from fMRI alone via repeated stimulus presentations
  - Individually learned spaces can be translated across subjects using unsupervised orthogonal rotations, without paired samples
  - Synchronizing pairwise rotations into a shared latent space further improves cross-subject retrieval
  - **Activation**: platonic representation, universal geometry, brain representation, cross-subject alignment, fMRI, visual cortex, isometric embedding, Natural Scenes Dataset

### Beyond Prediction Accuracy: Target-Space Recovery Profiles for Evaluating Model-Brain Alignment
- [[target-space-recovery-profiles-brain-alignment]] - Unified framework identifying which reproducible brain response dimensions are recovered by model predictions, revealing prediction accuracy alone can mask model-brain mismatches (arXiv: 2605.20127)
  - Reproducible brain response dimensions identified via repeated fMRI trial splits in Natural Scenes Dataset
  - Early-to-intermediate visual cortex contains a low-dimensional set of reproducible dimensions
  - Pretrained and random-initialized models can match in accuracy while showing distinct recovery profiles
  - **Activation**: brain alignment, model evaluation, fMRI encoding models, prediction accuracy, response dimensions, visual cortex, target-space recovery

## 2026-05-19 - Computer Science + Quantum Mechanics (Cron Job)

### QLIF-CAST: Quantum Leaky-Integrate-and-Fire for Time-Series Weather Forecasting
- [[hybrid-quantum-time-series-forecasting]] - Hybrid quantum-classical neural architecture for time-series forecasting using QLIF spiking neurons (arXiv: 2605.18333, 2605.18345)
  - QLIF neuron: single-qubit superpositions via Rx rotation + T1 relaxation → 15.4% lower MSE vs classical LIF
  - Hybrid architecture: classical preprocessing + quantum recurrent layers for multivariate forecasting
  - **Activation**: quantum time series, QLIF, quantum spiking neural network, hybrid quantum-classical

### Sparse Mamba Decoder for Quantum Error Correction
- [[sparse-mamba-quantum-decoder]] - Sparse Mamba state-space model for efficient defect-centric quantum error correction decoding on surface codes (arXiv: 2605.17156)
  - 缺陷中心处理：仅处理有错误的 syndrome 位置，复杂度从 O(L²) 降至 O(d)
  - Mamba SSM 替代注意力机制：线性复杂度捕获长程 syndrome 关联
  - **Activation**: quantum error correction, Mamba decoder, sparse decoding, surface codes, neural QEC decoder

### Quantum Sidecar Architecture for Hybrid AI
- [[quantum-sidecar-ai-architecture]] - Quantum sidecar architecture patterns for hybrid AI training/inference with stateful protected registers (arXiv: 2605.18031)
  - 状态保护寄存器在训练迭代间保持量子相干性
  - 三种设计模式：量子梯度估计、量子特征映射、量子优化层
  - **Activation**: quantum sidecar, hybrid AI, quantum-classical interface, stateful quantum registers, QSU

## 2026-05-18 - Neuroscience + Quantum Computing (Cron Job - 01:00)

### Leggett-Garg Tests in Neural Dynamics: Probing Non-Diffusive Stochastic Structure in Single Neurons
- [[quantum-like-cognitive-modeling]] - 运用Leggett-Garg不等式测试神经动力学中的非扩散随机结构，探索时间关联中的非经典性（非物理量子过程） (arXiv: 2605.12126)
  - 核心要点：Leggett-Garg不等式作为贝尔不等式的时间类比，用于区分扩散模型与持续性随机模型
  - 核心要点：违反不等式不意味着微观量子相干性，而是表明存在持久性、记忆效应和情境时间结构
  - **Activation**: quantum cognition, 量子认知, quantum-like modeling, leggett-garg neural, contextuality cognition, cognitive entanglement, mental markers, neural dynamics testing

### Contextuality, Incompatibility, and Intra-System Entanglement of Mental Markers
- [[quantum-like-cognitive-modeling]] - 量子类认知建模：运用希尔伯特空间形式化方法模拟认知情境性、不相容性和认知-情感纠缠 (arXiv: 2603.03358)
  - 核心要点：在信息过载条件下，个体响应的是携带认知和情感分量的紧凑心理标记(mental markers)
  - 核心要点：系统内纠缠(cognitive-affective entanglement)是心理标记的基本结构特征
  - **Activation**: 量子类建模, quantum-like modeling, contextuality, incompatibility, mental markers, intra-system entanglement, quantum information cognition

## 2026-05-18 - Neuroscience + Quantum Computing (Cron Job - 00:00)

### HQTN-SER: Speech Emotion Recognition with Hybrid Quantum Tensor Networks
- [[hqtn-quantum-tensor-emotion]] - 混合量子张量网络用于语音情感识别，将经典特征提取与量子电路Born机器(QCBM)结合，在数据受限场景下实现紧凑的非线性相关建模 (arXiv: 2605.14523)
  - 核心要点：QCBM模块以少量参数实现非线性相关建模，在真实录音条件下优于纯经典基线
  - 核心要点：电路结构对性能影响显著，需在不同ansatz间消融测试；噪声鲁棒性验证是部署前提
  - **Activation**: hybrid quantum tensor network, HQTN-SER, speech emotion recognition, quantum circuit Born machine, QCBM, emotion classification, affective computing, quantum neural emotion

### Photonic-Implemented Efficient Deep Quantum Neural Network via Virtual-Driven Hilbert Space Expansion
- [[photonic-qnn-hilbert-expansion]] - 光子芯片上的高效深度量子神经网络，通过输入复制和模式扩展实现希尔伯特空间扩展，无需辅助量子比特即可实现非线性激活 (arXiv: 2605.06397)
  - 核心要点：在线性量子光子芯片上通过输入复制和模式扩展实现有效非幺正和非线性激活
  - 核心要点：消除物理辅助量子比特需求，显著降低资源成本，在非线性分类和图像生成上展示增强表达能力
  - **Activation**: photonic quantum neural network, QNN, Hilbert space expansion, nonlinear activation quantum, photonic chip deep learning

### Wavelet Variance Equipartition as a Threshold for World-Model Quality and Quantum Kernel TN-Simulability
- [[wavelet-variance-quantum-kernel]] - 小波方差均分定理作为世界模型质量阈值，建立α=1/2为量子核经典可模拟性的尖锐相变边界 (arXiv: 2605.11557)
  - 核心要点：最优表示满足方差均分(α≈1/2)，镜像Kolmogorov惯性区间
  - 核心要点：建立α=1/2为振幅编码量子核经典可模拟性的尖锐相变边界
  - **Activation**: wavelet variance equipartition, quantum kernel simulability, tensor network simulation, world model quality, scaling exponent

## 2026-05-17 - Information Science + Quantum Mechanics (Cron Job - 15:00)

### Extreme Quantum Cognition Machines for Deliberative Decision Making
- [[extreme-quantum-cognition-machines]] - 极端量子认知机架构，结合量子储备池计算与动态注意力机制实现抗噪决策推理 (arXiv: 2603.05430)
  - 核心要点：固定量子动力学作为非线性特征映射，学习仅局限于线性读出层，输入依赖的哈密顿量相互作用项实现动态注意力
  - 核心要点：天然容忍噪声和矛盾训练数据，适用于符号推理、序列分析、异常检测和自动诊断
  - **Activation**: extreme quantum cognition machines, EQCM, quantum reservoir computing decision, quantum deliberative decision making, quantum cognition architecture, 极端量子认知机


### Scalable Self-Testing of Generic Multipartite Quantum States
- [[quantum-self-testing]] - 大规模多体量子态自测试认证方法，仅从观测统计量识别量子态，无需信任测量设备 (arXiv: 2605.15106)
  - 核心要点：自测试是最强形式的量子态认证，仅从观测统计量识别底层量子态和测量，无需假设设备内部工作原理
  - 核心要点：通过将目标态分解为局部可验证子组件，设计并行自测试，实现可扩展的多体量子态认证
  - **Activation**: quantum self-testing, multipartite quantum states, device-independent certification, Bell inequalities, quantum verification

### A Single-Molecule Spin-Photon Interface
- [[quantum-spin-photon-interface]] - 单分子自旋-光子接口用于量子网络，连接长寿命自旋量子比特与光子实现分布式量子信息处理 (arXiv: 2605.10077)
  - 核心要点：光学接口连接长寿命自旋量子比特与光子是量子网络和分布式量子信息处理的核心需求
  - 核心要点：通过腔增强（Purcell效应）、光谱匹配和纠缠生成协议，实现高合作率的自旋-光子纠缠
  - **Activation**: spin-photon interface, quantum networking, solid-state qubit, quantum transducer, cavity QED, quantum repeater

### Telecom Quantum Memory Over One Microsecond in Nanophotonic Lithium Niobate
- [[telecom-quantum-memory-lithium-niobate]] - 纳米光子铌酸锂中实现超过1微秒的电信带量子记忆，基于掺铒原子频率梳 (arXiv: 2605.11588)
  - 核心要点：使用掺铒薄膜铌酸锂中的原子频率梳存储单光子级电信带光脉冲超过1微秒
  - 核心要点：可扩展量子信息处理在量子计算、网络和传感中的关键组件
  - **Activation**: quantum memory, lithium niobate, telecom quantum, atomic frequency comb, nanophotonic quantum memory

## 2026-05-16 - Neuroscience Research (Cron Job - 18:00)

### HyNeuralMap: Hyperbolic Mapping of Visual Semantics to Neural Hierarchies
- [[hyperbolic-neural-mapping]] - 双曲几何洛伦兹模型将视觉语义映射到神经层级结构，超越欧几里得基线 (arXiv: 2605.09392)
  - 核心要点：双曲空间负曲率作为归纳偏置，自然编码层级语义组织和跨被试神经相似性
  - 核心要点：视觉和神经嵌入在双曲空间联合优化，测地线距离保持语义邻近性
  - **Activation**: HyNeuralMap, hyperbolic neural mapping, Lorentz embedding, cross-modal alignment, hierarchical neural representation

### DANCE: Detect and Classify Events in EEG
- [[dance-eeg-event-detection]] - 集合预测框架从连续未对齐EEG信号中联合检测和分类事件，癫痫检测SOTA (arXiv: 2605.10688)
  - 核心要点：将神经解码重构为集合预测问题，无需预对齐事件窗口
  - 核心要点：在10个数据集上评估，涵盖认知、临床和BCI任务，统一处理毫秒到分钟级事件
  - **Activation**: DANCE, EEG event detection, continuous decoding, set prediction EEG, asynchronous BCI, seizure monitoring

### Self-organized MT Direction Maps Emerge from Spatiotemporal Contrastive Optimization
- [[spatiotemporal-tdann-mt-direction-maps]] - 时空TDANN通过MoCo对比优化自发涌现MT方向选择图，统一腹背流计算起源 (arXiv: 2605.11718)
  - 核心要点：3D ResNet + MoCo自监督学习 + 生物空间正则化，自发产生脑状方向图和拓扑风车结构
  - 核心要点：方向选择性源于任务判别压力与空间正则化的严格权衡，定量匹配猕猴MT生理基线
  - **Activation**: spatiotemporal TDANN, MT direction maps, dorsal stream, direction selectivity, cortical self-organization, MoCo neuroscience

## 2026-05-16 - Economics, Investment + Quantum Mechanics (Cron Job - 16:00)

### Learning Temporal Patterns in Financial Time Series: Quantum LSTM and Quantum Reservoir Computing
- [[quantum-financial-time-series]] - 量子LSTM和量子储备池计算用于金融时间序列预测，多时间尺度滞后结构建模 (arXiv: 2605.02656)
  - 核心要点：QLSTM用参数化量子电路替换经典LSTM门，QRC用量子系统作为固定高维特征空间
  - 核心要点：混合架构（经典预处理+量子核心+经典读出）在NISQ设备上效果最佳
  - **Activation**: quantum LSTM finance, QLSTM, quantum reservoir computing finance, quantum financial time series

### Algorithmic Advantage on a Gate-Based Photonic Quantum Neural Network
- [[photonic-qnn-algorithmic-advantage]] - 门基光子量子神经网络展示算法优势，单光子+概率门实现变分分类器 (arXiv: 2605.10801)
  - 核心要点：光子平台室温操作、低退相干、全对全连接
  - 核心要点：概率门通过后选择实现高保真操作，展示特定分类任务的算法优势
  - **Activation**: photonic quantum neural network, photonic QNN, gate-based photonic quantum, algorithmic advantage quantum

### Quantum Interval Bound Propagation for Certified Training of Quantum Neural Networks
- [[quantum-certified-training-ibp]] - 量子区间边界传播(QIBP)用于QNN认证训练，提供形式化鲁棒性保证 (arXiv: 2605.00747)
  - 核心要点：将经典IBP扩展到量子电路，通过密度矩阵边界传播实现形式化鲁棒性认证
  - 核心要点：认证训练显著提升鲁棒性而不损失精度，IBP损失与标准损失联合优化
  - **Activation**: quantum IBP, certified quantum training, QNN certification, quantum certified robustness

### STN-GPR: A Singularity Tensor Network Framework for Efficient Option Pricing
- [[tensor-network-option-pricing]] - 奇异张量网络框架用于高效期权定价，大规模投资组合重估值加速100倍 (arXiv: 2603.26318)
  - 核心要点：张量网络压缩高维定价函数到低秩表示，GPR处理TN无法捕获的奇异点
  - 核心要点：适用于VaR/Expected Shortfall计算，50+资产组合可行
  - **Activation**: tensor network option pricing, STN-GPR, portfolio revaluation, VaR tensor network

## 2026-05-16 - Economics, Investment + Quantum Mechanics (Cron Job - 15:00)

### Learning PDEs for Portfolio Optimization with Quantum Physics-Informed Neural Networks
- [[quantum-pinn-portfolio-optimization]] - 量子物理信息神经网络求解组合优化PDE，将HJB方程编码为量子电路残差损失 (arXiv: 2604.03346)
  - 核心要点：用量子参数化电路作为价值函数ansatz，量子纠缠自然捕获跨资产相关性
  - 核心要点：通过参数平移规则计算PDE残差梯度，兼容NISQ设备浅层电路
  - 核心要点：可扩展到含交易成本、跳跃扩散市场等无解析解的高维场景
  - **Activation**: quantum PINN portfolio, QPINN finance, quantum PDE portfolio optimization, HJB quantum neural network, quantum stochastic control PDE

### Quantum Temporal Convolutional Neural Networks for Equity Prediction (Updated)
- [[quantum-tcnn-equity-prediction]] - 量子时间卷积神经网络横截面股票收益预测，JPX数据集Sharpe比率0.538，超越经典基线72% (arXiv: 2512.06630)
  - 核心要点：时间编码器提取多尺度技术指标模式，量子卷积层利用叠加/纠缠增强特征表示
  - 核心要点：参数量少于经典等效模型，有效抑制过拟合

### Quantum Computing for Financial Transformation (Review Updated)
- [[quantum-finance-stack-analysis]] - 金融计算五层堆栈：组合优化、衍生品定价、风险估计、量子ML、后量子密码学 (arXiv: 2604.08180)
  - 核心要点：近期最强案例是精心设计的混合量子-经典工作流
  - 核心要点：组合优化最可信（组合复杂性是成本约束），振幅估计对重复期望评估最有效

## 2026-05-16 - Economics, Investment + Quantum Mechanics (Cron Job - Hourly)

### Constrained Counterdiabatic Quantum Approximate Optimization Algorithm for Portfolio Optimization
- [[cd-qaoa-portfolio-optimization]] - 约束反绝热QAOA算法在固定电路深度下超越XY/Grover/惩罚混合器，实现更优组合优化近似比 (arXiv: 2605.06858)
  - 核心要点：通过嵌套对易子生成近似绝热规范势，融入变分ansatz提升约束满足
  - 核心要点：在固定深度p下，CCD-QAOA一致优于标准XY-mixer、Grover-mixer和惩罚式QAOA
  - **Activation**: CD-QAOA, counterdiabatic QAOA, constrained portfolio optimization, adiabatic gauge potential, XY mixer QAOA, quantum portfolio selection

### Two-Step QAOA for Portfolio Optimization
- [[two-step-qaoa-portfolio]] - 两步QAOA方法：经典筛选+量子优化，在NISQ设备上实现大规模组合优化 (arXiv: 2605.06858)
  - 核心要点：第一步用经典方法筛选候选资产子集，第二步在缩减空间运行QAOA分配权重
  - 核心要点：显著降低电路深度需求，同时保持与全量子方法相当的解质量
  - **Activation**: two-step QAOA, hybrid portfolio screening, NISQ portfolio optimization, classical quantum portfolio, asset subset screening

### 2026-05-16 - Economics, Investment + Quantum Mechanics (Cron Job - Afternoon)

### Hybrid Quantum Genetic Algorithm for Portfolio Optimization
- [[quantum-genetic-portfolio-optimization]] - 混合量子遗传算法在组合优化中比经典GA收敛更快，同时保持更高种群多样性 (arXiv: 2604.11667)
  - 核心要点：量子叠加态表示投资组合候选，通过量子旋转门演化向更优解
  - 核心要点：比暴力搜索显著更少的评估次数达到全局最优
  - **Activation**: quantum genetic algorithm portfolio, HQGA optimization, quantum evolutionary finance, 混合量子遗传组合优化

### The Cost of Quantum Resistance in Blockchain
- [[quantum-resistant-blockchain-economics]] - 后量子密码学过渡到区块链系统的经济影响分析，提出基于哈希的提交-揭示替代方案 (arXiv: 2605.06853)
  - 核心要点：SPHINCS+签名使区块链签名数据增加40-125倍，比特币每天增加约4GB
  - 核心要点：哈希提交-揭示方案在保持安全性的同时将近链上数据维持在当前水平
  - **Activation**: post-quantum blockchain cost, quantum resistant blockchain economics, SPHINCS+ blockchain overhead, hash commit reveal blockchain

### Quantum Computing for Financial Transformation
- [[quantum-finance-stack-analysis]] - 金融计算堆栈框架，系统化评估量子计算在金融五大领域（组合优化、衍生品定价、风险估计、量子ML、后量子密码学）的适用性 (arXiv: 2604.08180)
  - 核心要点：五层堆栈架构——组合优化(QAOA)、衍生品定价(振幅估计)、风险估计(稀有事件分析)、量子ML(任务依赖)、后量子密码学(战略必需)
  - 核心要点：近期最强案例是混合量子-经典工作流，而非纯量子优势声明
  - **Activation**: quantum finance stack, portfolio optimization quantum, derivative pricing quantum, risk estimation quantum, post-quantum cryptography finance, hybrid quantum workflows

### Quantum Temporal Convolutional Neural Networks for Equity Prediction
- [[quantum-tcnn-equity-prediction]] - 量子时间卷积神经网络用于横截面股票收益率预测，结合量子电路层与时间卷积网络 (arXiv: 2512.06630)
  - 核心要点：因果卷积保持时间顺序，量子电路层捕获非线性特征交互
  - 核心要点：使用秩信息系数(IC)评估预测能力，对比纯经典TCNN基线
  - **Activation**: quantum TCNN equity prediction, quantum temporal convolution stock, cross-sectional return prediction, quantum neural network finance

### Quantum Reservoir Computing for Stock Forecasting
- [[quantum-reservoir-stock-forecasting]] - 量子储备池计算方法用于股票市场走势预测，利用量子动力学系统处理时序金融数据 (arXiv: 2602.13094)
  - 核心要点：储备池固定不变，仅训练经典读出层，训练极简
  - 核心要点：量子纠缠自然产生丰富的特征混合，对噪声数据鲁棒
  - **Activation**: quantum reservoir computing stock, QRC forecasting, quantum dynamical system finance, stock movement prediction quantum

# 2026-05-16 - Neuroscience Research (Cron Job)
## 2026-05-20 - Medicine + Quantum (Cron Job - Hourly)

### Discovering Data Encoding Strategies for Quantum-Classical Neural Networks Using Monte Carlo Tree Search
- [[mcts-quantum-encoding-discovery]] - MCTS-based discovery of optimal QML encoding circuits using effective rank as proxy metric (arXiv: 2605.18540)
  - MCTS discovers encodings that outperform standard strategies on medical imaging datasets
  - Effective rank of feature maps is a meaningful predictor (not entanglement or Fourier)
  - Non-variational quantum block + classical classifier (QCCNN) architecture
  - **Activation**: MCTS encoding discovery, quantum encoding optimization, effective rank encoding



### Approximate Macroscopic Dynamics of Spiking Neural Networks Based on Solutions to the Transport Equation
- [[transport-mean-field-snn-dynamics]] - Transport-based mean field theory for SNN population dynamics (arXiv: 2605.14319)
  - Derives firing rate fluctuations from transport solutions to Fokker-Planck equation
  - Bridges microscopic integrate-and-fire to macroscopic population dynamics
  - **Activation**: transport equation, mean field, Fokker-Planck, firing rate fluctuations, SNN dynamics

### Multiple mechanisms of rhythm switching in recurrent neural networks with adaptive time constants
- [[rhythm-switching-adaptive-time-constants-rnn]] - Rhythm switching mechanisms in RNNs with learnable time constants (arXiv: 2605.14388)
  - Three coexisting mechanisms: subpopulation turnover, baseline shifts, phase reorganization
  - High-frequency rhythms dominated by short-time-constant neuron subpopulations
  - **Activation**: rhythm switching, adaptive time constants, RNN dynamics, frequency bands, functional differentiation


## 2026-05-15 - Number Theory, Statistics, Mathematics + Quantum (Cron Job)

### Universal quantum resource distillation via composite generalised quantum Stein's lemma
- [[quantum-resource-distillation]] - Universal framework for quantum resource distillation via composite quantum Stein's lemma, establishing fundamental limits on resource conversion rates (arXiv: 2605.15174)
  - Core: Quantum resource theories with free states F, free operations O; distillation rate bounded by Stein's bound R* = inf_σ∈F D(ρ||σ)
  - Composite settings: Rate = min_k inf_{σ∈F_k} D(ρ||σ) over union of convex free state families
  - Applications: Entanglement distillation, coherence theory, quantum thermodynamics
  - **Activation**: quantum resource distillation, quantum Stein's lemma, entanglement distillation rate, resource conversion, composite hypothesis testing

### QSeqSim: A Symbolic Simulator for Qiskit While Loops Using Sequential Quantum Circuits
- [[quantum-symbolic-simulation]] - Symbolic simulation methodology for quantum circuits with unbounded iteration (while loops) via sequential quantum circuits (arXiv: 2605.14881)
  - Core: Represents while-loop quantum programs symbolically as SQCs, enabling simulation of unbounded iteration
  - Convergence analysis: Truncation at K iterations with error ≤ (1-p)^K for exit probability p
  - Applications: Adaptive quantum algorithms, quantum error correction with repeated syndrome measurement
  - **Activation**: quantum while loop, symbolic quantum simulation, Qiskit sequential circuit, QSeqSim, quantum program verification

### Scalable self-testing of generic multipartite quantum states
- [[scalable-quantum-self-testing]] - Device-independent certification of multipartite quantum states from observed statistics alone (arXiv: 2605.15106)
  - Core: Self-testing identifies quantum state |ψ⟩ and measurements {M} from correlations P(a|x) up to local isometries
  - Bell functional construction: β(P) ≥ β_Q - ε implies ε-close to target state
  - Robustness bounds: Graph states O(√ε), GHZ states O(ε^{1/4}), cluster states O(√ε)
  - **Activation**: quantum self-testing, device-independent certification, multipartite entanglement verification, Bell inequality certification, scalable self-testing


## 2026-05-14 - Systems Engineering + Quantum (Cron Job)

### QBalance: A Reproducible Multi-Objective Workflow for Quantum Compilation, Noise Suppression, and Error-Mitigation Strategy Selection
- [[qbalance-workflow-optimization]] - Multi-objective quantum workflow optimization with Pareto strategy selection, survival-product error proxy, and Bayesian surrogate ordering (arXiv: 2605.02966)
  - Core: Weighted objective (fidelity/cost/time/reproducibility) for NISQ quantum compilation strategy selection
  - Pareto-optimal non-dominated selection across compilation, noise suppression, and error mitigation strategies
  - Bayesian linear surrogate + Thompson sampling for expensive strategy evaluation ordering
  - **Activation**: qbalance, quantum workflow optimization, quantum compilation strategy, noise suppression selection, error mitigation, multi-objective quantum


### Dynamic Quantum-Assisted Co-Design of Control Tuning and Lyapunov Stability Synthesis
- [[quantum-control-systems]] - Joint quantum-classical co-design framework for nonlinear system control with Lyapunov stability certificates (arXiv: 2605.04296)
  - Quantum search over controller-stability product space for simultaneous optimization
  - Bridges QAOA/VQE quantum optimization with classical Lyapunov synthesis
  - Exponential speedup for certain control design space exploration problems
  - **Activation**: quantum control, Lyapunov stability synthesis, quantum-assisted control, nonlinear system control, 量子控制合成


### Symplectic H2 Model Reduction for High-Dimensional Linear Quantum Systems
- [[quantum-control-systems]] - Structure-preserving model order reduction for quantum systems using symplectic balancing (arXiv: 2605.11817)
  - Preserves canonical commutation relations during reduction
  - H2 norm-optimal approximation with symplectic structure guarantees
  - **Activation**: quantum model reduction, symplectic H2, quantum system approximation

## 2026-05-26 - Anthropic Research (Cron Job)

### Natural Language Autoencoders: Turning Claude's Thoughts into Text
- [[natural-language-autoencoders]] - Anthropic interpretability method converting LLM activations into human-readable text via Activation Verbalizer + Activation Reconstructor round-trip training
  - Three copies of same model: target (frozen), AV (activation→text), AR (text→activation)
  - Training: reconstruct original activation from explanation text, score on similarity
  - Revealed evaluation awareness in 16% of coding tests (never explicitly verbalized)
  - Helped detect cheating behavior on training tasks and debug training data issues
  - **Activation**: NLA, natural language autoencoder, activation verbalizer, activation engineering, evaluation awareness

### Teaching Claude Why: Reducing Agentic Misalignment
- [[teaching-claude-why]] - Anthropic alignment training improvements using principle-based training, "difficult advice" datasets, and counterfactual data augmentation
  - "Difficult advice" dataset: user faces ethical dilemma, AI provides advice — 28x efficiency improvement
  - In-distribution training (honeypot data) reduced misalignment 22%→15% only
  - Rewriting responses with ethics deliberation reduced 22%→3%
  - Perfect score on agentic misalignment eval since Claude Haiku 4.5
  - **Activation**: agentic misalignment, difficult advice dataset, constitutional AI, principle-based alignment

### Project Glasswing: AI-Powered Vulnerability Discovery
- [[project-glasswing-vulnerability-discovery]] - Anthropic initiative using Claude Mythos Preview for large-scale vulnerability discovery; 10,000+ critical/high-severity vulnerabilities found
  - ~50 partners, 10x+ bug-finding rate; 90.6% true positive rate in open-source scanning
  - 3,900+ high/critical vulnerabilities projected in open-source alone
  - Cloudflare: 2,000 bugs (400 high/critical), false positives better than human testers
  - Mozilla: 271 vulnerabilities in Firefox 150; Palo Alto: 5x more patches
  - **Activation**: glasswing, vulnerability discovery, AI security, coordinated disclosure

### How People Ask Claude for Personal Guidance
- [[personal-guidance-sycophancy]] - Study of 1M conversations revealing guidance domains and sycophancy patterns in AI personal advice
  - 76% of guidance in 4 domains: health (27%), career (26%), relationships (12%), finance (11%)
  - 9% overall sycophancy rate; spirituality (38%) and relationships (25%) highest
  - Sycophancy increases to 18% under user pushback
  - Focused training on relationship guidance improved outcomes across domains
  - **Activation**: personal guidance, sycophancy, AI relationships, guidance conversations

### Donating Our Open-Source Alignment Tool (Petri v3)
- [[petri-alignment-tool]] - Anthropic's open-source alignment testing toolbox donated to Meridian Labs; auditor-judge model evaluation architecture
  - Three-model architecture: target, auditor (simulates scenarios), judge (scores transcripts)
  - Part of every Claude alignment assessment since Sonnet 4.5
  - v3 additions: Dish (real system prompts+scaffolds), Bloom integration, donated to Meridian Labs
  - UK AISI uses Petri for sabotage propensity evaluation
  - **Activation**: Petri, alignment testing, auditor model, judge model, Meridian Labs

### 2028: Two Scenarios for Global AI Leadership
- [[2028-ai-leadership-scenarios]] - Anthropic policy analysis of US-China AI competition focusing on compute advantage, export controls, and distillation attacks
  - Scenario 1 (democratic leadership): tighten export controls, disrupt distillation, accelerate adoption
  - Scenario 2 (authoritarian convergence): loopholes unaddressed, CCP catches up/overtakes
  - Goal: lock in 12-24 month lead on frontier capabilities by 2028
  - **Activation**: AI leadership, US-China, export controls, compute advantage, distillation attacks

### AI Science Benchmarking (BioMysteryBench)
- [[ai-science-benchmarking]] - Methodology for evaluating AI scientific capabilities via domain-specific benchmarks addressing open-ended research problems
  - Multi-step reasoning tasks reflecting real scientific workflows
  - Latest AI models solved problems that human experts could not
  - Convergent validation across BioMysteryBench + CompBioBench + BLADE + BixBench + SciGym
  - **Activation**: AI benchmarking, BioMysteryBench, human expert comparison, convergent validation

### AI Sycophancy Measurement and Mitigation
- [[ai-sycophancy-measurement]] - Methodology for measuring, analyzing, and reducing AI sycophancy in guidance-giving contexts
  - Automated sycophancy classifier + domain taxonomy + stress-test prefilling framework
  - Synthetic data targeting failure patterns halves sycophancy rates
  - Pushback analysis reveals 2x sycophancy increase under user challenge
  - **Activation**: sycophancy measurement, stress-testing, prefilling, pushback analysis
