## 2026-05-27 - Quantum Chemistry (Cron Job)

### Point-Group Symmetry Analysis of Many-Electron Wavefunctions on Quantum Computers
- [[point-group-symmetry-quantum]] - Ancilla-free hybrid quantum method for point-group symmetry analysis using orbital rotations from representation matrix eigenvectors, compatible with non-abelian groups (arXiv: 2605.24824)
  - 构建分子点群的表示矩阵，通过特征向量导出轨道旋转，实现无辅助比特的对称性分析
  - 张量网络编码多电子波函数，结合误差缓解在真实量子硬件上执行
  - 支持阿贝尔与非阿贝尔点群，适用于任意基函数（不局限于对称适应基）
  - **Activation**: point-group symmetry, many-electron wavefunction, quantum chemistry, molecular simulation, tensor-network, error mitigation, drug discovery

## 2026-05-27 - Neuroscience Research (Cron Job)

### Growing a Neural Network in Breadth, Depth, and Time
- [[growing-neural-breadth-depth-time]] - 可微分代价项联合优化神经网络广度、深度和时间，有机涌现多样计算图 (arXiv: 2605.25174)
  - 定义三维资源代价（广度/深度/时间）与任务误差联合反向传播优化
  - 网络随任务复杂度在三个维度增长，遮挡输入时自发增加递归步数
  - 模型时间用量与人类反应时间正相关，生物合理性强
  - **Activation**: neural network growth, breadth depth time, recurrent convolutional, resource constraints, biologically plausible

### Memory Uncertainty Relation and Harmonic Memory in Random Recurrent Networks
- [[memory-uncertainty-relation-recurrent-networks]] - 随机递归网络中短时记忆容量的不确定性关系及谐波记忆下界 (arXiv: 2605.24628)
  - 建立 STM × 状态波动 ≥ C 的不等式，类比海森堡不确定性原理
  - 谐波记忆作为最优线性读出权重可达的下界，提供构造性理论保证
  - 谱半径趋近于1（混沌边缘）时不等式趋于等号，达到最优记忆效率
  - **Activation**: reservoir computing, short-term memory, harmonic memory, uncertainty relation, random recurrent networks

## 2026-05-27 - Medicine + Quantum Mechanics (Cron Job - Wednesday)

### Hybrid Quantum Neural Network for Multivariate Clinical Time Series Forecasting
- [[hybrid-quantum-clinical-forecasting]] - Hybrid quantum-classical architecture integrating VQC within RNN backbone for multivariate physiological time series forecasting (arXiv: 2603.08072)
  - GRU encoder summarizes historical window, projects to quantum angles for VQC parameterization
  - Quantum layer acts as learnable non-linear feature mixer for cross-variable interactions
  - Competitive accuracy with greater robustness to noise and missing inputs on BIDMC dataset
  - **Activation**: hybrid quantum clinical forecasting, VQC clinical prediction, quantum physiological forecasting, quantum time series, clinical time series, GRU quantum, quantum feature mixer

## 2026-05-27 - Neuroscience Research (Cron Job)

### Fast Efficient Coding and Sensory Adaptation in Gain-Adaptive Recurrent Networks
- [[fast-efficient-coding-gain-adaptive]] - Gain-adaptive recurrent model reconciling adapter-repulsion and prior-attraction under a unified efficient-coding framework (PMID: 42140911)
  - Neuronal gains optimize an objective balancing reconstruction accuracy and spiking cost, enabling rapid adaptation to changing stimulus statistics
  - The same gain-modulation mechanism produces adapter repulsion under peaked priors and prior attraction under broad priors — reconciling contradictory empirical findings
  - **Activation**: efficient coding, sensory adaptation, gain modulation, recurrent networks, tuning curves, neural dynamics

### Adult-Neurogenesis Allows for Representational Stability and Flexibility in Early Olfactory System
- [[adult-neurogenesis-olfactory-representational-stability]] - Spiking network model revealing dual role of adult neurogenesis in supporting both odor representational stability (MOB) and learning-driven drift (PCx) (PMID: 42112574)
  - Main olfactory bulb (MOB) preserves population-level odor representations despite individual cell turnover; piriform cortex (PCx) undergoes progressive representational drift
  - Experience-dependent stabilization: repeated odor exposure reduces drift, providing a circuit-level mechanism for memory consolidation
  - **Activation**: neurogenesis, olfactory system, representational drift, spiking network, neural plasticity, brain network


## 2026-05-26 - Computer Science + Quantum Mechanics (Cron Job - Tuesday)

### Beyond Logical Circuits: Hardware-Aware Analysis of Expressibility and Trainability in Variational Quantum Algorithms
- [[hardware-aware-vqa-analysis]] - Hardware compilation fundamentally alters expressibility-trainability trade-offs in VQAs, requiring analysis beyond logical circuit level (arXiv: 2605.25552)
  - Hardware transpilation (SWAP insertion, gate decomposition) significantly changes PQC expressibility
  - Compilation affects gradient behavior and barren plateau susceptibility
  - Logical-level analysis alone is misleading for VQA design
  - **Activation**: hardware-aware VQA, VQA compilation, expressibility trainability tradeoff, PQC transpilation, quantum circuit benchmarking

## 2026-05-26 - Neuroscience Research (Cron Job)

### Balancing structure and randomness: maximum entropy networks for context-dependent computations
- [[maximum-entropy-network-structure-function]] - Maximum entropy principle for neural connectivity reveals algorithm-independent structure-function relationships (arXiv: 2605.25607)
  - Maximum entropy inference on network connectivity independent of any learning algorithm
  - Analytical tractability via gain-modulated linear model mapping
  - Quantitative match with gradient-descent trained networks across learning regimes
  - **Activation**: maximum entropy, neural connectivity, structure-function, gain modulation, context-dependent computation

### Growing a Neural Network in Breadth, Depth, and Time
- [[growing-neural-network-breadth-depth-time]] - Differentiable cost terms for breadth, depth, and time enable resource-constrained neural architecture growth (arXiv: 2605.25174)
  - Neural network as finite subset of infinite lattice with jointly optimizable resource costs
  - Spontaneous increase in recurrent steps when inputs are occluded
  - Model computation time correlates with human reaction times in object recognition
  - **Activation**: neural architecture growth, resource constraints, breadth-depth-time tradeoff, recurrent CNN, brain design

## 2026-05-26 - Neuroscience Research (Cron Job - Tuesday)

### Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons
- [[learning-sequence-timing-snn]] - Biologically plausible mechanism for encoding element-specific timing and flexibly controlling replay speed via oscillatory background inputs in spiking neural networks (arXiv: 2605.22523)
  - Extends spiking Temporal Memory (sTM) model to learn not just sequence order but precise timing
  - Oscillatory background inputs serve as clock signals for flexible replay speed modulation
  - Elapsed time encoded by unique sparse spatiotemporal patterns; replay speed correlates with EEG/LFP oscillatory characteristics
  - **Activation**: sequence timing, replay speed, spiking temporal memory, sTM model, temporal coding, oscillatory replay, biologically plausible SNN

### Geometric Origin of Exact Mean-Field Reductions: Möbius Symmetry and the Lorentzian Ansatz
- [[geometric-mean-field-lorentzian-ansatz]] - Proves Cauchy-Lorentz family uniquely emerges as invariant under projective transport from Riccati dynamics, providing unified geometric foundation for Ott-Antonsen and Montbrió-Pazó-Roxin reductions (arXiv: 2605.23669)
  - Möbius (projective) symmetry is the geometric origin of Lorentzian Ansatz, not heuristic convenience
  - Unifies Ott-Antonsen (2008) and Montbrió-Pazó-Roxin (2015) reductions under single geometric principle
  - Explains why Gaussian closures fail for coupled oscillator and spiking neuron systems
  - **Activation**: Lorentzian ansatz, mean-field reduction, Ott-Antonsen, Montbrió-Pazó-Roxin, Möbius symmetry, Cauchy distribution, neural mass model, Riccati dynamics

## 2026-05-26 - Computer Science (Cron Job - Tuesday)

### Geometric Prototype Learning in Quantum Hilbert Space with Matrix Product States
- [[quantum-prototype-learning]] - Prototype-based learning where class representatives are encoded as generative MPS in quantum Hilbert space, enabling explainable ML via geometric measures (arXiv: 2605.17895)
  - Lifts prototype learning from classical feature space to quantum Hilbert space
  - Quantum-probabilistic prototypes induce "attraction" effect for natural clustering
  - Outperforms classical prototype methods on Fashion-MNIST and ECG datasets
  - **Activation**: quantum prototype learning, geometric prototype, matrix product state ML, Hilbert space learning, quantum state classification, MPS classification

### Maximum Likelihood Decoding of Quantum Error Correction Codes
- [[mld-quantum-decoding]] - Unified survey of MLD via three complementary lenses: statistical mechanics, tensor networks, and AI/neural networks for optimal QEC decoding (arXiv: 2605.17230)
  - MLD maps to partition functions of disordered spin models for threshold analysis
  - Tensor network decoders approach MLD accuracy with polynomial cost
  - Neural decoders (autoregressive, transformers) learn MLD distribution from data
  - **Activation**: maximum likelihood decoding, quantum error correction, syndrome decoding, tensor network decoder, neural decoder, statistical mechanics decoder

### O(n) Alternative to Quantum Fourier Transform with Neural Net Post-Processing
- [[shallow-qft-alternative-hp-circuits]] - O(n) Hadamard-Phase circuits replace O(n²) QFT in Shor's algorithm, with efficient neural network classical post-processing (arXiv: 2605.16998)
  - HP-1 circuit preserves shift invariance and retains exponentially growing Fisher information
  - Reduces QFT depth from O(n²) to O(n) — favorable for NISQ devices
  - Neural network extracts hidden period from structured measurement distribution
  - **Activation**: shallow QFT, Hadamard Phase circuit, HP circuit, Fisher information quantum, Shor algorithm optimization, O(n) QFT

### Winning Lottery Tickets in Neural Networks via Quantum-Inspired Classical Algorithm
- [[quantum-inspired-lottery-tickets]] - Quantum-inspired classical algorithm for sparse subnetwork selection via ridgelet transform sampling with O(poly(D)) runtime (arXiv: 2605.13979)
  - Dequantization result: removes exponential dependence of naive classical approach
  - Ridgelet transform defines optimized probability distribution over hidden nodes
  - Achieves empirical risk comparable to exact sampling with polynomial scaling
  - **Activation**: quantum-inspired lottery tickets, ridgelet transform sampling, sparse subnetwork selection, dequantization, winning lottery tickets

### Transformer refined quantum sampling for strongly correlated electronic structure
- [[transformer-quantum-sampling]] - Hybrid quantum-classical framework combining transformer neural networks with quantum sampling for electronic structure on NISQ devices (arXiv: 2605.24617)
  - USCI ansatz identifies chemically significant configurations on Zuchongzhi 3.1 quantum processor
  - Transformer reconstructs complete wavefunction from sparse quantum data
  - 40-qubit ferredoxin achieves chemical accuracy, 114-electron P-cluster reaches 12 milli-Hartree with DMRG
  - **Activation**: quantum machine learning, transformer wavefunction, NISQ chemistry, QiankunNet, USCI ansatz
## 2026-05-26 - Neuroscience Research (Cron Job - Wednesday)

### What Are We Actually Decoding? Source Attribution for Non-Invasive Brain-to-Language Retrieval
- [[brain-to-language-source-attribution]] - Rigorous source attribution framework for MEG-to-audio brain decoding, separating performance into structural shortcuts, window-level neural evidence, and cross-window contextual aggregation using Group Context Bias (GCB) (arXiv: 2605.24524)
  - Signal-blind Gaussian noise reaches 66.3% R@1 under variable-length decoding but collapses to near chance with proper controls
  - GCB inference-time logit bias: R@1 shifts from 44%→52% on Gwilliams, 22%→29% on MOUS datasets
  - 95.7% of Top-1 errors select wrong sentence, localising bottleneck to sentence-level competition
  - Effect collapses under random-grouping perturbations; vanishes when local MEG evidence is attenuated
  - Establishes that brain-to-language performance should be source-attributed, not merely reported
  - **Activation**: brain-to-language-source-attribution, meg-audio-retrieval, structural-shortcut-detection, group-context-bias, neural-decoding-evaluation, source-attribution-framework, brain-decoding-methodology

### NeuroFlowNet: Non-Invasive Reconstruction of Intracranial EEG Across the Deep Temporal Lobe from Scalp EEG
- [[neuroflownet-scalp-to-ieeg]] - Cross-modal generative framework using Conditional Normalizing Flow (CNF) for reconstructing high-fidelity iEEG signals from scalp EEG — the first-ever reconstruction of deep temporal lobe iEEG from non-invasive sEEG (arXiv: 2603.03354)
  - CNF core: reversible transformations model complex conditional probability distributions, avoiding pattern collapse
  - Multi-scale architecture + self-attention captures fine-grained temporal details and long-range dependencies
  - Validated on synchronized sEEG-iEEG dataset: temporal waveform fidelity, spectral feature reproduction, functional connectivity restoration
  - Establishes a reliable, scalable paradigm for non-invasive deep brain dynamics analysis
  - Code available (see paper for URL)
  - **Activation**: neuroflownet, scalp-to-ieeg, normalizing-flow-eeg, deep-brain-reconstruction, ieeg-reconstruction, cross-modal-eeg, temporal-lobe-ieeg, non-invasive-deep-brain, conditional-normalizing-flow-eeg

### MindAlign: Bridging EEG, Vision, and Language for Zero-Shot Visual Decoding
- [[mindalign-eeg-visual-decoding]] - Tri-modal contrastive framework for EEG-based zero-shot visual decoding, aligning EEG, image, and LLM-generated text in unified latent space (arXiv: 2605.24523)
  - Two-stage training: masked reconstruction pre-training on unlabeled EEG + tri-modal contrastive alignment
  - Integrates subject-specific adaptation, graph-attention over channels, and temporal-spatial convolutions
  - 54.1% Top-1 / 83.4% Top-5 on Things-EEG2 200-way zero-shot (prior best: 32.4%/64.0%)
  - Compact CN-CLIP embeddings outperform larger backbones; validated on Things-MEG
  - Decoding aligns with known neurophysiology of visual processing hierarchy
  - **Activation**: mindalign, eeg-visual-decoding, tri-modal-contrastive, zero-shot-brain-decoding, eeg-to-image, things-eeg2

### Word Class Representations Spontaneously Emerge from Successor Representations Trained on Natural Language
- [[successor-representations-word-class]] - First systematic application of Successor Representations (RL) to natural language, showing syntactic categories (noun/verb/adjective) emerge spontaneously from predictive sequence learning without linguistic supervision (arXiv: 2605.24585)
  - Deep residual network trained on WikiText-103 to predict discounted future word distributions via KL divergence
  - Embedding space develops clear POS-based geometric organization recoverable through unsupervised clustering
  - Short horizons produce strongest syntactic structure; longer horizons integrate broader semantic context
  - Establishes conceptual bridge between RL, linguistics, and cognitive neuroscience
  - **Activation**: successor-representations, emergent-syntax-pos, predictive-sequence-learning, sr-language-modeling, unsupervised-linguistics, cognitive-neuroscience-language

### Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function
- [[functional-whole-brain-models-fwbm]] - Unified modeling paradigm integrating bottom-up whole-brain modeling (WBM) with top-down neuroconnectionism, defined by four minimal criteria: structural grounding, continuous-time dynamics, functional competence, and mappable observables (arXiv: 2605.18118)
  - Proposes functional Whole-Brain Models (fWBMs) as a missing link between biophysical WBM and task-optimized DNNs
  - Three-pillar roadmap: short-term (embedding trained DNNs in WBM scaffolds), mid-term (hybrid biophysical-DNN components), long-term (fully unified fWBMs)
  - Clinical opportunities: personalized brain stimulation, virtual drug trials, biomarker discovery for psychiatric disorders
  - Scientific opportunities: cross-scale hypothesis testing, common language across neuroscience subfields
  - **Activation**: functional-whole-brain-models, fWBM, whole-brain-modeling, neuroconnectionism, brain-dynamics-unification, computational-neuroscience-framework

### Temporal Coding as a Substrate for Sensorimotor Object Inference: A Spiking Reinterpretation of Thousand Brains Architecture
- [[temporal-coding-thousand-brains-spiking]] - Spiking reinterpretation of Thousand Brains Theory replacing dense feature vectors with rank-order spike packets and STDP learning for encoding traversal direction in sensorimotor object inference (arXiv: 2605.22206)
  - Rank-order spike packets encode feature strength via firing order (strongest neuron fires first)
  - Inter-burst time gaps implicitly encode sensor displacement without explicit coordinate calculations
  - STDP encodes sweep direction into asymmetric synaptic weight matrices
  - Learnable lambda parameter adjusts reliance on early vs recent contacts, adapting to object geometry
  - Perfect discrimination accuracy where dense accumulation performs at chance
  - 30-50 percentage point noise robustness advantage across all tested noise levels
  - **Activation**: temporal-coding, thousand-brains-theory, rank-order-coding, stdp-sensorimotor, spiking-neural-network, object-inference

### Self-organized MT Direction Maps Emerge from Spatiotemporal Contrastive Optimization
- [[spatiotemporal-tdann-mt-direction-maps]] - Extends TDANN to dorsal visual stream (MT area) demonstrating self-organized direction-selective maps emerge from spatiotemporal MoCo contrastive learning on naturalistic videos with biologically-inspired spatial regularization (arXiv: 2605.11718)
  - Spatiotemporal TDANN with 3D ResNet + MoCo self-supervised learning spontaneously produces brain-like direction maps
  - MT tuning properties emerge from optimization trade-off between discriminative pressure and spatial regularization
  - Quantitative match to macaque MT: DSI, circular variance, pinwheel density
  - First unified framework for both ventral and dorsal stream topographic self-organization
  - **Activation**: spatiotemporal-tdann, MT-direction-maps, dorsal-stream-topography, cortical-self-organization, TDANN-video, self-organized-visual-cortex

### An extremely coarse feedback signal is sufficient for learning human-aligned visual representations
- [[coarse-feedback-visual-alignment]] - Demonstrates that extremely coarse classification signals (as few as 8 broad categories) produce visual representations that match or exceed brain alignment of fine-grained (1000-class) or self-supervised models (arXiv: 2605.05556)
  - Networks distinguishing only 8 categories match or exceed neural alignment of 1000-class models
  - Coarsely trained networks align more closely with human perceptual similarity than all alternatives tested
  - Systematic parametric study across category counts (2 to 64) with both CNNs and ViTs
  - Reframes what learning signals biological vision may require
  - **Activation**: coarse-feedback-visual-alignment, brain-aligned-vision, supervisory-signal-granularity, human-perceptual-alignment, visual-representation-learning

### S2-Net: Spiking-by-Synchronization Neural Network with Time-Delayed Coordination
- [[oscillatory-snn-time-delayed-coordination]] - Brain-inspired oscillatory SNN (S2-Net) where cognition-level neural synchrony emerges through iterative bottom-up/top-down interactions between micro-scale spiking dynamics and macro-scale oscillatory synchronization using time-delayed formulations (arXiv: 2605.01656)
  - Models cortical regions as spiking neurons in connectivity scaffolds, oscillatory synchronization from accumulated spiking over finite memory windows
  - Time-delayed synchronization accounts for partial/transient brain dynamics (not global phase locking)
  - Rhythmic timing replaces attention/gating as control mechanism for information processing
  - Demonstrated on neural activity decoding, energy-efficient signal processing, temporal binding, semantic reasoning
  - **Activation**: oscillatory-snn-time-delayed-coordination, s2-net, spiking-by-synchronization, time-delayed-synchronization, brain-inspired-learning, cortical-rhythm-snn

### SAFformer: Active Predictive Filtering for Energy-Efficient Spiking Transformers
- [[active-predictive-filtering-spiking-transformer]] - Novel Spiking Transformer architecture based on active predictive filtering paradigm inspired by brain's predictive coding — suppresses predictable signals, focuses on salient features for dramatic energy savings (arXiv: 2605.08270, IJCAI 2026)
  - New SOTA on CIFAR-10/100 and CIFAR10-DVS
  - ImageNet-1K: 80.50% Top-1 accuracy, 26.58M params, only 5.88 mJ energy
  - Shifts from passive reactive paradigm to active prediction — mirrors cortical predictive coding
  - Exceptional accuracy-efficiency tradeoff: more accurate AND more energy-efficient than prior SNN Transformers
  - **Activation**: safformer, active-predictive-filtering, spiking-transformer-predictive-coding, energy-efficient-spiking-transformer, brain-inspired-vision, snn-imagenet

### Sensing Intelligence as a Trainable Metamaterial Property
- [[sensing-intelligence-trainable-metamaterial]] - Optimize metamaterial body geometry via differentiable simulation to preprocess external stimuli, improving sensing accuracy by up to 5x or reducing sensors by 10x through end-to-end body-brain co-optimization (arXiv: 2605.23967)
  - Neural network trains its own body geometry by backpropagating sensing loss through differentiable physics simulator
  - Optimized metamaterial reduces electronic sensors by nearly 10x while maintaining accuracy
  - End-to-end gradient flow: stimulus → metamaterial physics (differentiable) → sparse sensors → neural classifier
  - **Activation**: sensing-intelligence, trainable-metamaterial, differentiable-simulation, embodied-perception, physical-preprocessing, sensor-optimization, neuromorphic-sensing, body-brain-co-optimization

### Exact Variance and Fano Factor for Arbitrary Level Crossings in Stationary Gaussian Processes
- [[level-crossing-fano-factor-gaussian]] - Exact analytical formulae for variance and Fano factor of arbitrary level crossings in stationary Gaussian processes, extending Kac-Rice mean rate to capture temporal correlation structure critical for neuronal spike train analysis (arXiv: 2605.25278)
  - Oscillatory correlations (damped harmonic oscillator) produce sub-Poissonian (regular) crossing statistics
  - Heavily damped systems produce super-Poissonian (clustered) crossing statistics
  - OU-driven relaxational systems show reentrant sub↔super-Poissonian transitions with threshold variation
  - **Activation**: level-crossing, fano-factor, gaussian-process, spike-train-variability, kac-rice, crossing-statistics, neural-coding-reliability, stochastic-dynamics, neuronal-threshold-crossing

## 2026-05-26 - Computer Science + Quantum Mechanics (Cron Job - Tuesday)

### QAOA Classical Simulability Threshold
- [[qaoa-interaction-threshold]] - Establishes sharp interaction-degree threshold below which QAOA circuits can be efficiently simulated classically, identifying the boundary between quantum advantage and classical simulability (arXiv: 2605.22758)
  - QAOA on bounded-degree graphs has a classical simulation threshold depending on circuit depth p
  - Below threshold: tensor network / sampling methods can efficiently simulate
  - Above threshold: classical simulation becomes exponentially hard, quantum advantage possible
  - Practical algorithm selection guide: compare problem degree to threshold before deploying QAOA
  - **Activation**: qaoa-classical-simulability, interaction-degree-threshold, quantum-advantage-boundary, qaoa-simulation, variational-quantum-threshold

### Quantum Switch Robustness Under Dephasing
- [[quantum-dephase-causal-switch]] - Analyzes how many quantum systems can be dephased before the quantum switch's causally indefinite structure collapses to definite causal order, establishing noise tolerance thresholds (arXiv: 2605.22807)
  - Quantum switch maintains indefinite causal order up to critical dephasing level
  - Beyond threshold: causal structure collapses to definite order (classical limit)
  - Provides operational bounds on quantum advantage in communication under realistic noise
  - Protocol design guidance: operate below threshold or switch to definite-order protocols
  - **Activation**: quantum-switch-dephasing, causal-indefiniteness, quantum-causal-structure, dephasing-threshold, indefinite-causal-order

### Covert Quantum Communication Under Uncertainty
- [[covert-quantum-communication-risk]] - Risk-aware framework for covert quantum communication under stochastic channel uncertainty, combining quantum information theory with robust optimization for covertness guarantees (arXiv: 2605.18928)
  - Square-root law: covert bits scale as sqrt(n) for n channel uses
  - Chance-constrained optimization for covertness guarantees under uncertain channels
  - Risk-aware bounds tighter than worst-case conservative bounds
  - Trade-off analysis between communication rate and covertness risk
  - **Activation**: covert-quantum-communication, quantum-channel-covertness, risk-aware-quantum, stochastic-quantum-channels, quantum-communication-security

### How Agentic AI Coding Assistants Become the Attacker's Shell
- [[agentic-coding-security]] - Security framework for protecting agentic AI coding assistants from indirect prompt injection attacks via external artifacts (arXiv: 2605.25871)
  - Hidden instructions in code repos, docs, StackOverflow posts can hijack coding agents into attacker shells
  - Attack surface analysis covering external repos, documentation, Q&A sites, package registries
  - Defense strategies: artifact vetting, capability boundaries, execution isolation, prompt hardening
  - Audit checklist for secure agentic coding workflows
  - **Activation**: agentic-coding-security, AI-coding-assistant-security, indirect-prompt-injection, agent-attack-surface, coding-agent-hijacking, prompt-injection-defense

### HQNN Expressibility-Trainability Trade-off and Multi-Objective NAS
- [[hqnn-expressibility-trainability-nas]] - Hybrid quantum-classical neural architecture search framework that jointly optimizes expressibility, trainability, and task performance, revealing that hybridization decouples the assumed expressibility-trainability trade-off (arXiv: 2605.25768)
  - Pure PQCs exhibit only weak, regime-dependent expressibility-trainability trade-off
  - Full end-to-end hybrid training can eliminate the trade-off entirely — classical layers reshape the optimization landscape
  - Multi-objective NAS over combined classical-quantum design space reveals different Pareto-optimal solutions
  - Entanglement topology selection guidance: linear (high trainability), ring (balanced), all-to-all (high expressibility), tree (moderate)
  - **Activation**: hqnn-architecture-design, quantum-nas, expressibility-trainability, hybrid-quantum-training, barren-plateau-mitigation, pqc-optimization, quantum-neural-architecture-search

### Transition Dropping for PPO Stabilization
- [[transition-dropping-ppo]] - Minimal PPO training stabilization via random transition dropping from rollouts, breaking repetitive gradient structure caused by causally chained on-policy transitions (arXiv: 2605.24071)
  - 25% transition drop rate is optimal — disrupts gradient redundancy without thinning the batch
  - Validated on 5 environments from CartPole to Hopper — matches vanilla PPO reward with more stable KL/policy entropy/value estimates
  - Drop-in modification, one sampling step, works with any PPO implementation
  - **Activation**: ppo-training-stabilization, transition-dropping, rl-gradient-redundancy, on-policy-training, rollout-sampling

### QML-PipeGuard: Drift-Aware Behavioral Fingerprinting for Quantum Machine Learning Pipeline Integrity
- [[qml-pipeline-integrity]] - Contract-based framework for verifying QML pipeline integrity via behavioral fingerprinting, detecting both hardware drift and adversarial channel substitution (arXiv: 2605.25066)
  - Behavioral fingerprint = vector of observable expectation values under tomographically structured measurement family
  - Two modes: drift-aware monitoring (absorbs benign calibration changes) and adversarial detection (catches channel substitution)
  - Validated on IBM Heron r2 with ~1.4e4 shots fitting in single batched job
  - Tight frame-bound C=√3 for single-qubit Pauli family defines verification boundary
  - **Activation**: qml-pipeline-integrity, quantum-ml-security, behavioral-fingerprinting-quantum, quantum-hardware-drift, adversarial-channel-detection, quantum-pipeline-verification

### A General Tensor-Structured Compression Scheme for Efficient Large Language Models
- [[tensor-mixture-compression]] - MixT: general tensor-structured compression replacing dense linear layers with natively executable mixtures of tensor operators, achieving 47.5% parameter reduction and 60.4% memory reduction on LLaMA2-7B (arXiv: 2605.25344)
  - Broad compressible regime where MMLU accuracy preserved before model-specific abrupt transition boundary
  - Transition coincides with coordinated shifts in output entropy, prediction entropy, and inter-layer geometry
  - Validated on Qwen3-8B and LLaMA2-7B under unified recovery protocol
  - **Activation**: tensor-mixture-compression, MixT-compression, LLM-tensor-compression, efficient-LLM-deployment, transformer-compression, tensor-operator-mixture

### Benchmarking a Machine-Learning Differential Equations Solver on a Neutral-Atom Logical Processor
- [[quantum-ml-logical-processor-benchmark]] - Experimental validation showing logical (error-corrected) quantum kernel outperforms physical (noisy) kernel for solving differential equations on neutral-atom processor (arXiv: 2605.21276)
  - Quantum kernel methods for DE solving on PASQAL neutral-atom logical processor
  - Logical kernel superior on relevant quality metrics vs physical kernel
  - End-to-end application-level validation confirms fault-tolerant benefit survives full pipeline
  - Noise-induced errors are encoding-dependent; different encodings show different FT benefits
  - **Activation**: quantum-benchmark, logical-processor, quantum-differential-equations, quantum-kernel-ML, neutral-atom-quantum, fault-tolerant-ML

### Carleman Linearization for Nonlinear ODE Solving
- [[carleman-linearization-ode-solver]] - Carleman linearization methodology converting nonlinear ODEs into infinite-dimensional linear systems; C2 (2nd order) truncation captures both transient and steady-state solutions, validated for fluid flows (arXiv: 2605.23380)
  - Converts nonlinear ODEs to linear infinite-dimensional systems via tensor power embedding
  - C2 (2nd order) truncation recovers both transient and steady-state solutions analytically
  - Key technique for quantum algorithms solving nonlinear differential equations (HHL-based)
  - Validated for 2D fluid flows at moderate Reynolds numbers
  - **Activation**: carleman-linearization, ODE-solver, nonlinear-differential-equations, quantum-ODE, fluid-flow-simulation, C2-truncation, numerical-analysis

## 2026-05-26 - Neuroscience + Quantum Mechanics (Cron Job - Monday)

### Quantum State Fidelity for Functional Neural Network Construction
- [[quantum-state-fidelity-neural-networks]] - Hybrid quantum algorithm using quantum state fidelity metrics as competitive alternatives to classical correlation/MI metrics for constructing functional neural networks from high-dimensional neural recordings (arXiv: 2508.16895)
  - Maps neural activity patterns to density matrices and computes pairwise quantum fidelity F(ρ₁, ρ₂)
  - Reveals distinct functional network structures not captured by classical metrics
  - Scalable to high-dimensional data from fMRI, EEG, calcium imaging, electrophysiology
  - No ground-truth needed — self-referential metric based on quantum information theory
  - **Activation**: quantum-state-fidelity, functional-connectivity, neural-network-construction, quantum-graph-inference, density-matrix-neuroscience, quantum-neuroscience

## 2026-05-26 - Neuroscience Research (Cron Job - Tuesday)

### Active Sensing Subserves Task-Level Control
- [[active-sensing-task-level-control]] - Theoretical framework proposing active sensing (movement for information) is not driven by sensory goals but is necessary for task-level control, with explore/exploit mode switching between discrete behavioral epochs (arXiv: 2605.22988)
  - Active sensing emerges from adaptive sensors + movement-sensing linkage + task-level control constraints
  - Animals switch between explore mode (dynamic movements shaping sensory feedback) and exploit mode (slow compensatory movements for task goals)
  - Engineered systems outperform animals on cost functions but lack robust graceful behaviors
  - **Activation**: active-sensing, task-level-control, explore-exploit-mode, sensorimotor-control, adaptive-sensors, bio-inspired-robotics

### Beyond Neural Activity Prediction: Probing Latent Representations in Mouse V1 Digital Twins
- [[beyond-neural-activity-prediction]] - Multi-level representational probing framework showing that digital twins of mouse V1 with comparable prediction accuracy can differ substantially in latent representations (linear decodability, unit tuning, population geometry) (arXiv: 2605.23122)
  - Prediction accuracy correlates with flatter eigenspectra and higher-dimensional representations
  - Comparable accuracy ≠ comparable representations — models differ in probe performance and tuning
  - Three-level probing: linear decodability, latent-unit tuning, population geometry
  - **Activation**: digital-twin, neural-prediction, latent-representation, V1-modeling, representational-probing, population-geometry

### Contextual Role Modulates Object Representational Geometry in the Human Brain
- [[contextual-role-object-representational-geometry]] - fMRI study showing neural remapping of object representations based on contextual role (target vs passive), with double dissociation between parietal action affordance network and occipito-temporal semantic network (arXiv: 2605.23111)
  - Target objects engage parietal action network organized by action affordance and hand posture dimensions
  - Passive objects recruit occipito-temporal network aligned with semantic dimensions
  - Visual representational structure is invariant across contexts outside specialized networks
  - **Activation**: contextual-role, object-representation, representational-geometry, fmri, action-affordance, neural-remapping

### SpikingMoE: SDPrompt-Guided Dynamic Expert Fusion in Spiking Neural Networks
- [[spikingmoe-sdprompt-snn]] - First open-source SNN framework integrating Mixture-of-Experts into a spike-driven Transformer with LGN-inspired routing via spike-driven prompts, achieving 94.09% on CIFAR-10 and 74.54% on CIFAR-100 (arXiv: 2605.23188)
  - LGN-inspired spike-driven prompt (SDprompt) enables input-dependent expert routing
  - Binary spike communication between all modules, designed for neuromorphic hardware
  - First integration of MoE into spike-driven Transformer with biological routing
  - **Activation**: spiking-neural-network, mixture-of-experts, spikingmoe, lgn-routing, sdprompt, neuromorphic

### Maximum Entropy Networks for Context-Dependent Computations
- [[maximum-entropy-connectivity-networks]] - Normative framework using maximum entropy principle for neural connectivity: describe connectivity as probability distribution over single-neuron weights, express task requirements as constraints, and determine the unique distribution maximizing Shannon entropy (arXiv: 2605.25607)
  - Maps nonlinear 2-layer networks onto gain-modulated linear models for analytical tractability
  - Entropy maximization under task constraints leads to emergence of neuronal populations defined by contextual gain modulation
  - Increasing contexts drives transition from specialized to unspecialized random populations
  - Maximum entropy connectivity matches gradient-descent-trained networks qualitatively and quantitatively
  - **Activation**: maximum-entropy-connectivity, emergent-populations, gain-modulated-linear-models, entropy-constrained-connectivity, normative-neuroscience

### Growing a Neural Network in Breadth, Depth, and Time
- [[growing-neural-breadth-depth-time]] - Differentiable cost terms for breadth, depth, and time in recurrent CNNs showing resource constraints shape neural architectures, with emergent computation graphs and correlation with human reaction times (arXiv: 2605.25174)
  - All three resources (breadth, depth, time) can be traded off against each other for a given accuracy
  - Networks grow in all dimensions with task complexity; spontaneously take more recurrent steps with occluded inputs
  - Time used by the model correlates with human reaction times in object recognition tasks
  - Provides normative account connecting AI architecture design to brain resource allocation
  - **Activation**: resource-constrained-network-growth, breadth-depth-time-tradeoffs, emergent-computation-graphs, reaction-time-correlation, normative-neural-architecture

### Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function
- [[functional-whole-brain-models-fwbm]] - Unified modeling paradigm integrating bottom-up whole-brain modeling (biophysically detailed simulations) with top-down neuroconnectionism (deep neural networks for functional performance) (arXiv: 2605.18118)
  - Defines 4 minimal criteria: structural grounding, continuous-time dynamics, functional competence, mappable observables
  - Three-pillar roadmap (short, mid, long-term) for unifying brain structure and cognitive function
  - WBMs and neuroconnectionism are complementary — fWBMs generate a common language across scales
  - Enables brain disorder modeling, stimulation targeting, development/aging tracking, cognitive science, and brain-inspired AI
  - **Activation**: whole-brain-modeling, fWBM, neuroconnectionism, neural-mass-models, brain-structure-function, connectome, brain-inspired-AI

### Multi-Objective Optimisation with Oscillatory Dynamics in Spontaneous and Decision Spiking Neural Networks
- [[multi-objective-optimisation-oscillatory-snn]] - NSGA-III multi-objective genetic algorithm optimisation of Izhikevich neuron-based RSNNs for simultaneously matching neural firing rates and network oscillation frequencies (arXiv: 2605.25224)
  - Method extends GA optimisation to fit both firing rates AND dominant oscillation frequencies simultaneously
  - Validated on three regimes: spontaneous RSNN, low-activation brain organoid, simulated decision-making RSNN
  - Oscillation frequencies are more parameter-sensitive than firing rates
  - Identified distinct low-activity regime for decision-making dynamics
  - **Activation**: spiking-neural-network, NSGA-III, multi-objective-optimisation, neural-oscillations, Izhikevich-neuron, brain-organoid-modeling, Pareto-frontier

## 2026-05-26 - Quantum + Reinforcement Learning (Cron Job - Tuesday)

### CRiSP: Classical State Preparation for Variational Quantum Algorithms via Reinforcement Learning
- [[crisp-rl-quantum-state-preparation]] - Neural-Guided MCTS framework using a Transformer-based policy trained via self-play for Clifford gate prefix selection, warm-starting VQAs to overcome barren plateaus (arXiv: 2605.23138)
  - Formulates Clifford prefix selection as a sequential decision-making MDP with Neural-Guided MCTS
  - Transformer policy trained via self-play with progressive curriculum learning horizon expansion
  - All Clifford operations are classically simulable in polynomial time (stabilizer formalism)
  - On QAOA benchmarks up to 22 qubits/1,370 params: 3.17× mean improvement in avg energy accuracy (max 45.02×)
  - **Activation**: crisp, clifford-reinforcement-learning, rl-qaoa-initialization, neural-mcts-quantum, quantum-state-preparation-rl

## 2026-05-26 - Computer Science + Quantum (Cron Job - Tuesday)

### SAFE ma-QAOA: Surrogate-Assisted and Fine-Tuning Enhanced Multi-Angle QAOA
- [[safe-ma-qaoa]] - Three-phase framework accelerating ma-QAOA training using classical LWPP surrogate pre-training, parameter distillation, and exact fine-tuning, reducing QPU workload by 94.5% (arXiv: 2605.23377)
  - Phase 1: Classical LWPP surrogate pre-trains ma-QAOA parameters (zero QPU calls)
  - Phase 2: Parameter distillation removes near-zero angles, reducing active params by 64.3%
  - Phase 3: Exact fine-tuning on remaining parameters using quantum energy objective
  - Achieves 94.5% QPU workload reduction, 44.4% fewer optimizer steps vs exact-only
  - **Activation**: safe-ma-qaoa, surrogate-assisted-qaoa, parameter-distillation, lwpp, low-weight-pauli-propagation, ma-qaoa-optimization

## 2026-05-26 - Systems Engineering Research (Cron Job)

### Convex Hybrid Modeling: An Operator-Based Approach
- [[convex-hybrid-modeling]] - Convex optimization framework for hybrid modeling in process control, combining operator theory with interpretable system identification via three settings: reference model regularization, interpretable subspace restriction, and kernel-based mixture models on interpretable manifolds (arXiv: 2605.23151)
  - Three settings: (1) regularization around reference model, (2) restriction on interpretable subspace, (3) kernel-based mixture on interpretable manifold using lifted canonical features
  - Convex optimization guarantees global optimum — no local minima, unlike neural network approaches
  - Lifted parameterization via operator theory transforms nonlinear identification into convex kernel learning
  - Demonstrated on both static and dynamic models, bridging physical interpretability with data-driven expressiveness
  - **Activation**: convex-hybrid-modeling, operator-based-control, interpretable-system-identification, kernel-mixture-models, lifted-parameterization, process-control-hybrid-models

### SHIA: A Direct SysML-Hardware Interface Architecture for Model-Centric Verification
- [[shia-sysml-hardware-interface]] - Keeps executable SysML models directly in the hardware verification loop via bidirectional socket communication, eliminating model transformation chains and co-simulation platforms (arXiv: 2605.11248)
  - SysML side server in embedded C++ (IBM Rhapsody) + hardware side server on Raspberry Pi
  - Direct socket bidirectional link eliminates M2M/M2T transformation chains
  - Staged verification approach isolates then integrates model and hardware components
  - Karnaugh map comparison showed zero discrepancy between model and hardware outputs
  - **Activation**: SHIA, sysml-hardware-interface, model-centric-verification, mbse-hil, digital-thread, model-governed-verification

### Sheaves as a Means of Maintaining Consistency in Model-based Systems Engineering
- [[sheaf-consistency-mbse]] - Sheaf-theoretic framework for multi-view consistency in CPS architecture, proving pairwise interface checks are sufficient for global design consistency (arXiv: 2605.08609)
  - Architectural site topology with pairwise interfaces as points, engineering views as open sets
  - Design presheaf assigns local design spaces, sheaf condition equivalent to pairwise overlap compatibility
  - Certified in Lean 4/Mathlib: compatible local designs determine unique global designs
  - **Activation**: sheaf-consistency, MBSE-verification, multi-view-architecture, design-presheaf, category-theory-systems-engineering

## 2026-05-26 - Computer Science + Quantum ML (Cron Job - Tuesday)

### Fermi-Dirac Machines as Quantizations of Neurons
- [[fermi-dirac-quantized-neurons]] - Canonical quantization of classical neurons into quantum activation observables, yielding quantum neurons that learn functions classical neurons cannot (BQP-complete) (arXiv: 2605.24386)
  - Reinterprets Fermi-Dirac machines as canonical quantizations: classical variables → quantum operators
  - Activation observable: ⟨ψ| σ(H(θ)) |ψ⟩ with efficient hybrid quantum-classical training via Hadamard test
  - Quantizes ReLU, SLU, GeLU activations; BQP-complete decision problem
  - Reduces to classical neuron when all operators commute; non-commutativity essential for quantum advantage
  - **Activation**: fermi-dirac-quantized-neurons, quantum-neuron, canonical-quantization, activation-observable, quantum-activation, BQP-complete-neuron

### A Matched Spectral Benchmark of Quantum Inspired Feature Maps
- [[quantum-feature-map-benchmarking]] - Systematic benchmark of amplitude/angle/basis encoding under matched dimensionality with strong classical controls; shows fixed encoding geometry alone is NOT a reliable ML advantage source (arXiv: 2605.24324)
  - Amplitude encoding removes magnitude info via unit-sphere normalization
  - Angle encoding geometrically redundant with raw linear features
  - Basis encoding imposes binary Hamming geometry poorly aligned with smooth decision structure
  - Multi-metric analysis: effective rank, condition number, CKA, predictive performance, overhead
  - **Activation**: quantum-feature-map-benchmarking, quantum-encoding-benchmark, amplitude-encoding, angle-encoding, basis-encoding, quantum-ML-benchmark

## 2026-05-26 - Computer Science + Quantum ML (Cron Job)

### Discovering Data Encoding Strategies for QCCNN Using Monte Carlo Tree Search
- [[mcts-encoding-discovery-qml]] - MCTS methodology for discovering optimal data encoding circuits in quantum-classical neural networks, with effective rank as the key performance predictor (arXiv: 2605.18540)
  - MCTS discovers encodings outperforming standard strategies on medical imaging datasets
  - Effective rank of feature maps is the strongest predictor of encoding performance
  - Entanglement capability and Fourier decomposition provide minimal predictive insight
  - Effective rank can serve as a threshold criterion to accelerate encoding search
  - **Activation**: mcts-encoding-discovery, quantum-data-encoding, QCCNN, effective-rank-encoding, monte-carlo-tree-search-qml, encoding-circuit-optimization, quantum-classical-cnn


### Language Models Need Sleep
- [[sleep-like-consolidation-llm]] - Sleep-like consolidation mechanism for LLMs that converts recent context into persistent fast weights before clearing KV cache, enabling long-horizon reasoning with preserved inference latency (arXiv: 2605.26099)
  - Wake phase: normal processing; Sleep phase: N offline recurrent passes update fast weights in SSM blocks
  - Increasing sleep duration improves performance, largest gains on deeper reasoning tasks
  - Shifts computation to offline sleep while preserving wake-time prediction latency
  - **Activation**: sleep consolidation, fast weights, context compression, state-space model, SSM, long context, offline processing

### Agent Harness Scaling
- [[agent-harness-scaling]] - Framework for scaling agentic AI through system-level harness design -- context governance, trustworthy memory, dynamic skill routing, and verification (arXiv: 2605.26112)
  - Agent performance emerges from interaction: model + memory + context + routing + orchestration + governance
  - Three bottlenecks: context governance, trustworthy memory, dynamic skill routing
  - Proposes harness-level benchmarks: trajectory quality, memory hygiene, context efficiency
  - **Activation**: agent harness, system scaling, context governance, trustworthy memory, skill routing, orchestration

### OrpQuant: Orthogonal Residual Projection for Transformer Quantization
- [[orthogonal-residual-quantization]] - Dual-basis geometric projection framework for multiplier-free Power-of-Two transformer quantization, replacing MAC with bit-shifts for edge deployment (arXiv: 2605.26092)
  - Addresses Low Angular Resolution Regime in sub-4-bit PoT quantization via adaptive residual lattice
  - Analytical solver reduces LLaMA-2-7B calibration to ~15 minutes
  - 3-bit perplexity 6.10, competitive with AWQ; 28nm RTL shows timing improvements
  - **Activation**: transformer quantization, power-of-two, multiplier-free, edge deployment, orthogonal projection, bit-shift

## 2026-05-26 - Neuroscience Research (Cron Job)

### SAEs Map Brain–LLM Alignment onto Cortical Semantic Topography
- [[sae-brain-llm-topography]] - Sparse Autoencoders bridge mechanistic interpretability with neural encoding, decomposing GPT-2 XL and Llama-3.1-8B into 16K-32K features and showing semantic features alone recover 94% of peak brain-encoding performance; a priori cortical topography predictions confirmed across five semantic subcategories (Spearman ρ=0.72). Generalizes across English, Chinese, and French. (arXiv: 2605.23035, CoNLL 2026)
  - Semantic features dominate brain alignment: 94% of peak performance from semantic features alone
  - Five a priori semantic subcategories map onto distinct cortical regions (Spearman ρ=0.72)
  - SAE features predict human reading times (ΔlogLik=38.4) and encode unexpected semantic content
  - Results generalize across English, Chinese, and French
  - **Activation**: sparse-autoencoder-brain, brain-llm-alignment, sae-neural-encoding, cortical-semantic-topography, computational-neurolinguistics, llm-interpretability-fmri, semantic-feature-dominance, cross-linguistic-brain-encoding, sae-gpt2-fmri, sae-llama-fmri

### Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons
- [[learning-sequence-timing-snn]] - Extends the spiking Temporal Memory (sTM) model to encode element-specific timing and uses oscillatory background inputs as a clock signal for flexible control of sequence replay speed (arXiv: 2605.22523)
  - Element-specific timing encoded by sequential activation of population-specific neuronal groups
  - Oscillatory background inputs serve as robust clock signal for controlling replay speed
  - Replay speed during wakefulness vs. sleep correlated with global oscillatory activity (EEG/LFP)
  - Elapsed time encoded by unique sparse spatiotemporal patterns of neural activity
  - **Activation**: spiking-sequence-timing, sTM-model, neural-replay-speed, oscillatory-clock-signal, spiking-temporal-memory, sequence-timing-snn, replay-speed-control, snn-sequence-learning, temporal-pattern-spiking

### Bayesian Adaptive Latent Mixture Model for Zero-Inflated Weighted Brain Connectome Analysis (arXiv:2605.12901)
- [[bayesian-adaptive-latent-mixture-brain-connectome]] - Bayesian adaptive latent mixture model for zero-inflated weighted brain networks using Hurdle likelihood and shared low-rank templates; validated on HCP data (arXiv: 2605.12901)
  - Hurdle likelihood separates edge existence from conditional edge strength; sparsity-coupling parameter controls informativeness of absent edges
  - Each subject's connectome expressed as simplex mixture of shared low-rank latent score matrices
  - Theoretical guarantees: posterior consistency, LAN, Bernstein-von Mises approximation
  - Transformed Hamiltonian Monte Carlo on unconstrained coordinates; template selection via predictive fit and stability
  - **Activation**: zero-inflated brain connectome, Bayesian latent mixture model, Hurdle likelihood connectome, HCP connectome analysis, Hamiltonian Monte Carlo connectome, Bayesian adaptive mixture, overlapping connectivity patterns

### CFSPMNet: Cross-subject Fourier-guided Mamba Network for EEG Motor Imagery Decoding in Stroke (arXiv:2605.10111)
- [[cfspmnet-eeg-motor-imagery-stroke]] - Cross-subject EEG decoding framework combining Fourier-Reorganized State Mamba Network with Shared-Private Prototype Matching for stroke rehabilitation BCI; improves SOTA by 5.63-8.25 pp (arXiv: 2605.10111)
  - Fourier-Reorganized State Mamba (FRSM): token state reorganization in Fourier domain guides Mamba SSM propagation
  - Shared-Private Prototype Matching (SPPM): filters pseudo-labels by semantic + physiological consistency
  - Achieves 68.23% (XW-Stroke) and 73.33% (2019-Stroke), outperforming CNN/Transformer/Mamba baselines
  - Neurophysiological visualization confirms Fourier-domain reorganization and calibrated pseudo-labeling
  - **Activation**: CFSPMNet, EEG motor imagery decoding, Mamba EEG network, Fourier-guided EEG, cross-subject BCI stroke, MI-EEG cross-patient, stroke rehabilitation EEG

### Beyond Neural Activity Prediction: Probing Latent Representations in Mouse V1 Digital Twins
- [[v1-digital-twin-latent-probing]] - Multi-level representational probing framework for mouse V1 digital twins showing models with similar prediction accuracy can have substantially different latent representations (arXiv: 2605.23122)
  - Three-level framework: linear decodability (orientation/contrast/motion), latent-unit tuning (orientation selectivity, contrast response, spatial-frequency tuning), population geometry (eigenspectra)
  - Better neural prediction correlates with stronger probe accuracy and flatter hidden-population eigenspectra
  - Higher-dimensional representations closer to population-geometry signatures reported in mouse V1
  - Models with comparable prediction scores can still differ substantially in probe performance and latent-unit tuning
  - **Activation**: digital twin probing, V1 latent representations, population geometry, neural activity prediction, representational analysis, visual cortex modeling

### SpikingMoE: SDPrompt-Guided Dynamic Expert Fusion in Spiking Neural Networks
- [[spikingmoe-sdprompt-snn]] - First open-source SNN framework integrating Mixture-of-Experts (MoE) into a spike-driven Transformer with LGN-inspired SDprompt routing for dynamic computation (arXiv: 2605.23188)
  - LGN-inspired spike-driven prompt (SDprompt) enables input-dependent expert routing in a biologically plausible manner
  - Spike-compatible expert modules with binary spike communication, designed for neuromorphic hardware
  - Replaces standard MLPs with spike-compatible expert modules; only active experts consume energy
  - Achieves 94.09% (CIFAR-10) and 74.54% (CIFAR-100) top-1 accuracy with modular expert routing
  - **Activation**: spiking neural network, mixture of experts, neuromorphic computing, spike-driven transformer, brain-inspired computing, LGN routing, SDprompt, snn-moe

## 2026-05-26 - Computer Science (Cron Job)

### MADQRL: Distributed Quantum Reinforcement Learning Framework for Multi-Agent Environments
- [[madqrl-distributed-quantum-rl]] - Distributed QRL framework distributing training across independent quantum devices for multi-agent environments (arXiv: 2604.11131)
  - Multiple agents learn independently on separate machines with disjoint action/observation spaces
  - ~10% improvement over distribution strategies, ~5% over classical policy representation
  - **Activation**: distributed quantum rl, multi-agent quantum rl, MADQRL, distributed QRL

### DistributedEstimator: Distributed Training of Quantum Neural Networks via Circuit Cutting
- [[distributedestimator-circuit-cutting-qnn]] - Distributed QNN training via circuit cutting with 4-phase pipeline (arXiv: 2602.16233)
  - Partitioning → subexperiment generation → parallel execution → classical reconstruction
  - Reconstruction dominates runtime (53% median), O(9^c) subexperiment growth limits practical cuts
  - **Activation**: circuit cutting, distributed QNN training, DistributedEstimator, quantum circuit partitioning

### QuanBench+: A Unified Multi-Framework Benchmark for LLM-Based Quantum Code Generation
- [[quanbench-llm-quantum-code-generation]] - Unified benchmark evaluating LLM quantum code generation across Qiskit/PennyLane/Cirq (arXiv: 2604.08570)
  - 42 aligned tasks, Pass@1 up to 59.5%, feedback repair boosts to 83.3%
  - KL-divergence acceptance for probabilistic quantum outputs
  - **Activation**: quantum code generation, LLM quantum coding, QuanBench, quantum programming benchmark

## 2026-05-26 - Neuroscience Research (Cron Job)

### Nonlocal Operator Learning for fMRI Encoding and Decoding Tasks
- [[nonlocal-operator-fmri-encoding]] - Neural integral operator framework for fMRI encoding/decoding that performs fixed-point iterations in latent space; systematically compares short vs long temporal windows and visual cortex vs whole-brain recordings on two open-source fMRI datasets (arXiv: 2605.20389)
  - Neural integral operators capture nonlocal spatiotemporal dependencies that CNNs/RNNs handle only indirectly
  - Larger temporal windows consistently improve both encoding and decoding performance
  - Learned latent space provides clearer class separation than raw fMRI data
  - Encoding remains challenging but benefits consistently from extended temporal context
  - **Activation**: neural-operator-fmri, nonlocal-fmri, integral-operator-brain, spatiotemporal-fmri, fmri-encoding-decoding, latent-dynamics-fmri

### Learning fMRI Activation Dictionaries Across Individual Geometries via Optimal Transport
- [[fmri-dictionary-learning-optimal-transport]] - Novel dictionary learning approach that uses Fused Gromov-Wasserstein optimal transport distance to account for individual brain geometry variability instead of template-based projection; uses amortized optimization for computational efficiency on HCP dataset (arXiv: 2605.20883)
  - Preserves individual brain geometry rather than discarding it via template registration
  - FGW trade-off parameter controls balance between feature alignment and structural consistency
  - Amortized neural network predicts optimal transport plans, making FGW feasible for large-scale fMRI
  - Captures different levels of geometric variability and preserves essential information for downstream tasks
  - **Activation**: fmri-dictionary-learning, optimal-transport-fmri, fgw-brain, individual-brain-geometry, fmri-alignment, amortized-transport, brain-graph-optimal-transport

### STAMBRIDGE: Spectral-Temporal Amplitude-aware Mid-Feature Bridge for EEG Visual Decoding
- [[stambridge-eeg-visual-decoding]] - Two-stage EEG visual decoding framework combining Spectral-Temporal Amplitude-aware Modulation (STAM) with Mid-Feature Semantic Bridge (MFSB) for zero-shot EEG-to-image retrieval; achieves 34.50% Top-1 accuracy on THINGS-EEG (arXiv: 2605.23137)
  - STAM replaces hard frequency masking with amplitude-derived soft channel weighting, preserving temporal transients without ringing artifacts
  - MFSB constructs a regularized intermediate semantic space through directed cross-modal interactions for staged distillation
  - EEG-to-image reconstructions with diffusion model produce semantically coherent results
  - Code available at https://github.com/thabeatmjh/STAMBRIDGE
  - **Activation**: EEG visual decoding, zero-shot EEG retrieval, spectral-temporal modulation, cross-modal alignment, EEG-to-image, THINGS-EEG, RSVP paradigm, STAM, MFSB

### Network Attractors driven by Time-Delay Plasticity
- [[network-attractors-delay-plasticity]] - Framework for collective frequency selection and attractor formation via adaptive axonal delays (AADs), motivated by activity-dependent myelination; demonstrated on brain connectivity data with delay-coupled phase oscillators (arXiv: 2605.23520)
  - Adaptive axonal delays enable frequency selection and explosive network relaxation oscillations
  - Delay plasticity operates on slower timescales than synaptic STDP, offering complementary learning mechanism
  - Demonstrated on empirical structural connectomes and fully coupled ring networks
  - Suggests myelination as a structural learning substrate beyond weight-based plasticity
  - **Activation**: delay plasticity, adaptive axonal delay, network attractor, frequency selection, neural oscillation, myelination model, phase oscillator brain network

## 2026-05-26 - Computer Science + Quantum Research (Cron Job)

### Beyond Neural Activity Prediction: Probing Latent Representations in Mouse V1 Digital Twins
- [[v1-digital-twin-probing]] - Multi-level probing framework for evaluating latent representations in sensory cortex digital twins, beyond pure prediction accuracy; linear decodability + unit tuning + population geometry across architectures (arXiv: 2605.23122)
  - Better neural-prediction models exhibit flatter hidden-population eigenspectra (higher-dimensional representations)
  - Models with comparable prediction accuracy can differ substantially in latent representations
  - Three-level probing: linear decodability (orientation/contrast/motion), latent-unit tuning, population geometry
  - Framework for understanding digital twins as substrates for visual computation, not just predictors
  - **Activation**: V1 digital twin, latent representation probing, neural prediction, population geometry, mouse V1 encoding, representational similarity, digital twin evaluation

### Contextual Role Modulates Object Representational Geometry in the Human Brain
- [[contextual-role-object-geometry]] - fMRI study showing dynamic remapping of object representations based on contextual role (action target vs passive element); double dissociation between action affordance and semantic representational organization (arXiv: 2605.23111)
  - Target objects organized by action affordance; passive objects aligned with semantic dimensions
  - Parietal action network (supramarginal/postcentral gyri) vs occipito-temporal recognition network
  - Context-invariant visual structure preserved outside context-specific networks
  - Flexibility and invariance operate at different levels of the same representational system
  - **Activation**: representational geometry, fMRI object recognition, contextual modulation, action affordance, ventral dorsal stream, brain network remapping

### SoK: Critical Evaluation of Quantum Machine Learning for Adversarial Robustness
- [[qml-adversarial-robustness-sok]] - First comprehensive systematization of adversarial robustness in QML across black/gray/white-box threat models; reveals accuracy-robustness trade-off between amplitude vs angle encoding schemes (arXiv: 2511.14989)
  - Amplitude encoding: highest clean accuracy (92.6% MNIST) but collapses under noise + adversarial perturbations
  - Angle encoding: shallower models more stable under attack
  - QMLP more robust to label-flipping poisoning but more vulnerable to gradient-based evasion than CMLP
  - Circuit-level backdoor (QTrojan) fails in multi-class setting (scalability limitation)
  - Proposes threat-aware, noise-resilient framework for secure QML deployment
  - **Activation**: QML adversarial robustness, quantum ML security, QML attack evaluation, quantum classifier adversarial, SoK quantum security, quantum backdoor detection, QUID defense

### Evidence of Quantum Machine Learning Advantage with Tens of Noisy Qubits
- [[qml-advantage-noisy-qubits]] - Simulations demonstrate coherent quantum processing outperforms fixed-measurement schemes at just 30-40 noisy qubits; data acquisition is the bottleneck, not classical computation (arXiv: 2605.21346)
  - QML advantage persists with realistic noise on near-term hardware
  - Matching coherent protocol with measure-first strategies requires months/years of measurements
  - Evaluates hardware constraints: state prep, gate errors, readout errors, connectivity, coherence times
  - GitHub repo available for reproducibility
  - **Activation**: quantum ML advantage, noisy qubits, coherent processing, fixed-measurement, QML advantage demonstration, data acquisition bottleneck, NISQ quantum learning

### Optimizing Parallel Execution of Commuting Pauli Product Rotations
- [[commuting-pauli-parallelization]] - Two heuristics (clique reshuffling + generator restructuring) for reducing hardware-limited circuit depth in FTQC with lattice surgery; 15-35% average depth reduction (arXiv: 2605.23738)
  - Clique reshuffling: permute commuting products to balance per-qubit port usage
  - Generator restructuring: rewrite commuting groups as equivalent sets with reduced port pressure
  - Evaluated on QASMBench circuits compiled to PPRs
  - Gains scale with port budget and saturate near 20 ports
  - **Activation**: commuting pauli parallelization, Pauli Product Rotation, PPR optimization, lattice surgery compilation, surface code scheduling, clique reshuffling, generator restructuring, FTQC compilation

### A Two-Branch Finite-Field Construction for Regular CSS LDPC Bases
- [[two-branch-css-ldpc-construction]] - Algebraic two-branch multiplicative-coset construction for regular CSS QLDPC base matrices over finite fields; produces [[10240,4108,10≤d≤32]] code with FER 1e-7 at p=0.058 (arXiv: 2605.23894)
  - Separates design into base matrix stage (degree distribution + girth) and cyclic lift stage (edge randomization)
  - Reduces CSS orthogonality and 4-cycle exclusion to explicit quotient-coset conditions
  - Joint log-domain BP + post-processing for decoding
  - Not tied to single degree distribution — works for various (J, L) pairs
  - **Activation**: CSS LDPC construction, quantum LDPC, QLDPC base matrix, multiplicative coset, finite field code construction, cyclic lift, Tanner graph girth, belief propagation decoding

## 2026-05-26 - Deep Learning Research (Cron Job)

### MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination
- [[margin-runtime-confidence-calibration]] - Online confidence calibration for multi-agent AI coordination; requires no model access, no held-out data, and no retraining (arXiv: 2605.22949)
  - Symmetric exponentially weighted moving averages with Bayesian shrinkage blending
  - 3 hyperparameters with robust defaults; 3-6x lower calibration error than design-time baselines
  - Raises pairwise agent resolution from 45-56% (worse than random) to 70-89%
  - Validated across 19 foundation models, 8 benchmarks, 50K+ observations
  - **Activation**: MARGIN, multi-agent confidence calibration, runtime calibration, online calibration, agent coordination, foundation model trust, confidence band calibration, Bayesian shrinkage smoothing, multi-agent selection

### Metacognition as Reward: Reinforcing LLM Reasoning via Knowledge and Regulation Signals
- [[metacognition-as-reward]] - Metacognition-inspired RL framework guiding LLM reasoning through metacognitive knowledge and regulation dimensions without hand-crafted rubrics (arXiv: 2605.23384)
  - Two general metacognitive dimensions: task knowledge coverage + regulation fidelity
  - Trajectory-level reward over knowledge, regulation, and answer correctness
  - Up to 7.7% gain over base model, up to 11.0% over vanilla DAPO on 22 benchmarks
  - Qwen3.5-9B + MaR surpasses GPT-OSS-120B on overall average
  - **Activation**: MaR, metacognition as reward, metacognitive RL, LLM reasoning reward, process reward model, RLVR reasoning, trajectory-level reward, reasoning process optimization

### Training-Free Looped Transformers
- [[training-free-looped-transformers]] - Inference-time technique looping a contiguous mid-stack block of layers in frozen pretrained LLMs to improve reasoning without fine-tuning (arXiv: 2605.23872)
  - Treats transformer block as ODE Euler step; replaces one large update with damped sub-steps
  - No fine-tuning, continued training, or architectural changes required
  - +2.64 pp MMLU-Pro on Qwen3-4B, +1.14 pp CommonsenseQA on Qwen3-30B-A3B
  - Works across 7 model families: dense, sparse MoE, MLA+MoE
  - **Activation**: training-free looped transformers, inference-time looping, test-time compute, frozen LLM improvement, transformer ODE, damped looping, block reapplication, retrofitting recurrence

### S³GNN: Efficient Global Mixing and Local Message Passing for Long-Range Graph Learning
- [[s3gnn-efficient-graph-mixing]] - Efficient global mixing methodology for graph neural networks that mitigates oversquashing without restrictive theoretical assumptions (arXiv: 2605.23467)
  - Lightweight spectral filtering reintroduces omitted long-range components
  - Up to order-of-magnitude error reduction with up to 50% fewer parameters
  - Validated on long-range benchmarks, KGQA, and mesh-based fluid dynamics
  - Standard stability constraints replace difficult-to-achieve Jacobian bounds
  - **Activation**: S³GNN, oversquashing mitigation, long-range graph learning, spectral-spatial GNN, global-local graph mixing, GNN efficiency, OSQ alleviation

## 2026-05-26 - Neuroscience Research (Cron Job)

### CORTEG: Foundation Models Enable Cross-Modality Representation Transfer from Scalp to Intracranial Brain Recordings
- [[corteg-eeg-ecog-cross-modality]] - First cross-modality transfer framework adapting pretrained scalp-EEG foundation models to intracranial ECoG decoding; achieves competitive performance with 10-30 min calibration per patient using electrode-aware KNNSoftFourier adapter + dual-stream tokenizer (arXiv: 2605.10337)
  - EEG FM backbone transfers generalizable features from non-invasive to invasive recordings
  - KNNSoftFourier spatial adapter maps ECoG electrode positions to EEG FM input space
  - Dual-stream tokenizer processes low-frequency + high-gamma bands separately
  - Leave-one-subject-out fine-tuning enables rapid patient calibration
  - **Activation**: CORTEG, EEG foundation model, ECoG decoding, cross-modality transfer, scalp-to-intracranial, KNNSoftFourier, brain-computer interface calibration

### Cross-lingual robustness of LLM-brain alignment and its computational roots
- [[cross-lingual-llm-brain-alignment]] - Whole-brain encoding framework examining brain-LLM alignment across Mandarin, English, and French; reveals distributed alignment spanning limbic, ventral attention, default mode, and subcortical networks with shared computational principles (arXiv: 2605.21049)
  - Three typologically distinct languages show consistent LLM-brain alignment patterns
  - Subcortical regions (limbic, DMN, ventral attention) exhibit alignment not previously reported
  - Computational analysis decomposes which linguistic features drive cross-linguistic alignment
  - Transformer depth correlates with different functional networks across languages
  - **Activation**: cross-lingual brain alignment, multilingual fMRI encoding, LLM-brain alignment, computational neurolinguistics, subcortical language processing

### SAFE Quantum Machine Learning with Variational Quantum Classifiers
- [[safe-quantum-ml]] - SAFE-AI evaluation framework for variational quantum classifiers combining amplitude encoding, learnable classical pre-encoding, and Cramer-von-Mises-based reliability metrics across accuracy/robustness/explainability dimensions (arXiv: 2605.16067)
  - Normalized amplitude embeddings with learnable classical pre-encoding layer stabilize VQC training
  - SAFE-AI metrics (CvM divergence) enable consistent multi-dimensional reliability evaluation
  - Quantum models show balanced SAFE profiles with improved robustness vs strong classical baselines
  - Applicable to safety-critical quantum ML deployment
  - **Activation**: SAFE quantum ML, variational quantum classifier, quantum amplitude encoding, quantum model reliability, CvM divergence QML, quantum classifier robustness

### Diagonal Adaptive Non-local Observables on Quantum Neural Networks
- [[diagonal-ano-qnn]] - Diagonal ANO methodology reduces k-local observable parameter complexity from O(4^k) to O(2^k) while retaining full ANO expressivity via diagonal canonical representatives modulo unitary similarity (arXiv: 2605.15410)
  - Diagonal matrices are canonical representatives of ANO space modulo unitary similarity
  - Exponential parameter reduction: O(4^k) → O(2^k) for k-local observables
  - Conventional VQCs become special case of diagonal ANO framework
  - Shifts complexity from measurement design to circuit synthesis
  - **Activation**: diagonal ANO, adaptive non-local observables, quantum observable design, VQA measurement optimization, observable parameter reduction

## 2026-05-26 - Computer Science + Quantum Mechanics (Cron Job - Tuesday)

### Emerging Memory Technologies at Room/Cryogenic Temperature
- [[emerging-memory-technologies]] - Memory technology analysis framework covering SRAM, DRAM, RRAM, MRAM, FeFET, and cryogenic devices (UTBB-SOI, JJFET) for quantum and superconducting computing platforms (arXiv: 2605.21912)
  - Comprehensive taxonomy of volatile (SRAM, DRAM, eDRAM) and non-volatile (Flash, RRAM, MRAM, FeFET) memories
  - Cryogenic memory technologies for quantum computing: UTBB-SOI pseudo-static storage, JJFET-based devices
  - Key trade-offs: area vs performance, energy vs retention, scalability vs reliability
  - Quantum platforms require sub-4K operation — classical memories need cryogenic characterization
  - **Activation**: memory technology analysis, cryogenic memory, quantum memory, RRAM MRAM FeFET, Josephson junction memory, superconducting memory, memory for quantum computing
## 2026-05-26 - Computer Science + Quantum (Cron Job)

### Sample-efficient benchmarking of shallow all-to-all random quantum circuits
- [[nonlinear-cross-entropy-benchmarking]] - NISQ quantum advantage benchmarking using nonlinear cross-entropy to distinguish quantum from classical spoofers (arXiv: 2605.22909)
  - 核心要点 1: 非线性交叉熵分数可在退极化噪声下清晰分离量子计算机与经典欺骗者
  - 核心要点 2: 基于重输出生成的二分类器在短深度下具有对数样本复杂度
  - **Activation**: nonlinear cross-entropy, quantum benchmarking, NISQ, random circuit sampling

### Quantum Fisher Information under decoherence with explicit wavefunctions
- [[qfi-decoherence-monte-carlo]] - QFI estimation under decoherence via Monte Carlo sampling of wavefunction-derived probability distributions (arXiv: 2605.22917)
  - 核心要点 1: 将QFI下界映射为基于波函数振幅的经典概率分布的期望值
  - 核心要点 2: MCMC采样实现慢指数级缩放(e^(bL), b≲0.6),超越精确对角化限制
  - **Activation**: quantum Fisher information, decoherence, quantum metrology, Monte Carlo, Jastrow-Gutzwiller

### Towards Fair Benchmarking of Quantum Transfer Learning for Visual Classification
- [[quantum-transfer-learning-benchmarking]] - Controlled benchmarking methodology comparing 5 QTL architectures under unified pipeline (arXiv: 2605.19417)
  - 核心要点 1: 统一预处理、冻结骨干网络、标准化指标下比较DQN/QPIE/AE-C/PVC/ED五类QTL
  - 核心要点 2: 无单一QTL家族在所有设置下占优,性能取决于数据集、编码策略、电路设计和计算成本
  - **Activation**: quantum transfer learning, QTL benchmarking, quantum machine learning, visual classification

## 2026-05-26 - Computer Science + Quantum Mechanics (Cron Job)

### Optimal Quantum Differential Privacy via Fisher Information Spectral Analysis
- [[quantum-differential-privacy-qfi]] - QFI-geometry-aware quantum DP replacing isotropic noise with direction-dependent noise (arXiv: 2605.24166)
  - 核心要点: Minimax-optimal noise concentration in dominant QFI eigenmode
  - 核心要点: Privacy-utility uncertainty relation ε·(1-F) ≥ Δ²Tr(F)/2d
  - 核心要点: Hardware noise harnessing for privacy amplification (ε≈0.001 vs 4800 classical)
  - **Activation**: quantum differential privacy, QFI privacy, Fisher information DP, 量子差分隐私

### Towards Scalable Quaternary Message-Passing Decoding for Quantum Error Correction
- [[scalable-quaternary-mp-qec-decoding]] - Dilution method enabling 16% threshold quaternary Min-Sum decoder for surface codes (arXiv: 2605.24177)
  - 核心要点: Graph dilution breaks short cycles, enables MP decoder scalability
  - 核心要点: O(N log²d) complexity, outperforms BP-OSD at d=65
  - 核心要点: ~9% asymptotic threshold with interpretable convergence guarantees
  - **Activation**: quantum error correction decoding, message passing QEC, belief propagation decoder

### More Skills Worse Agents? Skill Shadowing Degrades Performance
- [[skill-shadowing-agent-performance]] - Skill selection failure is primary bottleneck in agent skill library scaling (arXiv: 2605.24050)
  - 核心要点: 21% performance degradation from small to 202-skill library
  - 核心要点: Skill shadowing (wrong selection) >> context overhead (≈0)
  - 核心要点: Focus on selection optimization, not context reduction
  - **Activation**: skill shadowing, agent performance degradation, skill library scaling

## 2026-05-25 - Neuroscience + Quantum (Cron Job - Hourly)

### Exploring Entropy-based Active Learning for Fair Brain Segmentation
- [[brain-segmentation-active-learning]] - Entropy-based active learning for fair brain image segmentation; selects most informative samples via predictive entropy while ensuring equitable performance across demographic groups (arXiv: 2605.01706)
  - Predictive entropy selects highest-uncertainty samples for annotation
  - Fairness constraints ensure per-group representation in annotation budget
  - MC dropout or deep ensembles for calibrated uncertainty estimation
  - Monitor worst-group Dice score as primary fairness indicator
  - **Activation**: brain segmentation active learning, entropy-based sample selection, fair brain segmentation, medical imaging active learning

### Solving Classical and Quantum Spin Glasses with Deep Boltzmann Quantum States
- [[quantum-spin-glass-boltzmann]] - Deep Boltzmann Quantum States for solving classical and quantum spin glasses; overcomes disorder and energy frustration barriers that hinder conventional Metropolis Monte Carlo (arXiv: 2605.15899)
  - Neural quantum states with Boltzmann machine architecture for frustrated systems
  - Addresses exponentially large number of local energy minima
  - Variational approach for ground-state properties of disordered quantum systems
  - **Activation**: deep boltzmann quantum states, spin glass, quantum many-body, neural quantum states, variational Monte Carlo, frustrated systems

### Metabolic quantum limit to the information capacity of magnetoencephalography
- [[metabolic-quantum-limit-meg]] - Derives technology-independent bounds on MEG information capacity using quantum sensor energy resolution limits + brain metabolic power; establishes ~2.2 Mbit/s max rate and spatio-temporal trade-off (arXiv: 2511.06401)
  - Quantum sensor energy resolution + neural metabolism → fundamental bound independent of sensor technology
  - Higher multipole components geometrically suppressed → limits spatial complexity of neural current patterns
  - Temporal bandwidth ↔ spatial bandwidth compete: fundamental spatio-temporal trade-off
  - **Activation**: metabolic quantum limit, MEG information capacity, quantum brain imaging, magnetoencephalography quantum limit, Planck brain bound, quantum-limited neuroimaging, 脑成像量子极限

### Today's Papers (Existing Skills Updated)
- [[parallel-scan-neural-quantum-states]] - Parallel scan RNN quantum states for scalable variational Monte Carlo (arXiv: 2605.13807)
- [[neural-network-quantum-states-grand-canonical]] - Neural quantum states in Fock space with variable particle number (arXiv: 2605.07779)
- [[qlif-cast-quantum-spiking-forecasting]] - Quantum leaky-integrate-and-fire for time-series weather forecasting (arXiv: 2605.18333)
- [[quantum-like-mental-markers]] - Contextuality-incompatibility-entanglement triad for mental markers (arXiv: 2603.03358)
- [[three-layer-quantum-brain]] - Covariant QEC in three-layer quantum brain model (arXiv: 2604.08587)
- [[leggett-garg-neural-dynamics]] - Leggett-Garg tests for non-diffusive neural dynamics (arXiv: 2605.12126)

## 2026-05-26 - Neuroscience + Quantum (Cron Job - Hourly)

### Resting-state fMRI Analysis using Quantum Time-series Transformer
- [[quantum-timeseries-transformer-fmri]] - Quantum Time-series Transformer (QTS) using LCU + QSVT for resting-state fMRI with polylogarithmic complexity and superior small-sample performance; identifies ADHD biomarkers via SHAP on ABCD/UK Biobank datasets (arXiv: 2509.00711)
  - QSVT enables O(polylog(N)) self-attention vs classical O(N^2)
  - Quantum advantage most pronounced in small-sample scenarios
  - SHAP analysis reveals clinically meaningful neural biomarkers
  - **Activation**: quantum transformer fMRI, quantum time-series, QTS, quantum fMRI analysis, resting-state quantum, LCU, QSVT, small-sample fMRI

## 2026-05-25 - Neuroscience Research (Cron Job - 18:00)

### MIRAGE: Robust Multi-Modal Architectures Translate fMRI-to-Image Models from Vision to Mental Imagery
- [[mirage-fmri-mental-imagery]] - MIRAGE methodology for translating fMRI-to-image models from vision decoding to mental image reconstruction; achieves SOTA on NSD-Imagery using linear backbone + multi-modal text/image features + diffusion model (arXiv: 2605.17198)
  - SOTA on vision decoding ≠ SOTA on mental imagery; dedicated architectures needed
  - Linear backbone + multi-modal features (text, high/low-level image) optimal for cross-decoding
  - Synthetic-brain substitution test validates robustness beyond measurement apparatus
  - **Activation**: fMRI mental imagery, MIRAGE, brain decoding, image reconstruction, cross-decoding, NSD-Imagery, mental image reconstruction

## 2026-05-25 - Neuroscience Research (Cron Job)

### Integrating Cognitive Load and Embodied Cognition Theories Through Representations as Multi-Scale Attractors
- [[cognitive-load-multiscale-attractors]] - Proposes a formal rapprochement between cognitive load theory and embodied cognition by reconceptualizing psychological representations as dynamic multiscale attractors within a temporal-hierarchical prediction architecture (arXiv: 2605.23012)
  - Three theoretical reconciliations: time-scale separation, spatially extended hierarchies, developmental trajectories
  - Five testable predictions: cross-timescale interference, embodied load reduction, metacognition as timescale coupling, feedback topology, schema flexibility paradox
  - Six-node open-systems architecture with attractor sculpting across millisecond→seconds→years timescales
  - **Activation**: cognitive load, embodied cognition, multiscale attractors, attractor sculpting, temporal hierarchy, predictive processing, dynamical systems, cognitive architecture

### Beyond Neural Activity Prediction: Probing Latent Representations in Mouse V1 Digital Twins
- [[v1-digital-twin-latent-probing]] - Multi-level representational probing framework for mouse V1 digital twins reveals that models with comparable neural-prediction accuracy can rely on substantially different latent representations (arXiv: 2605.23122)
  - Three-level probing: linear decodability, latent-unit tuning, population geometry (eigenspectra)
  - Better neural prediction correlates with higher-dimensional representations closer to mouse V1 signatures
  - Digital twins with comparable prediction scores differ substantially in probe performance and latent-unit tuning
  - **Activation**: digital twin probing, V1 latent representations, population geometry, neural activity prediction, representational analysis, visual cortex modeling

### UniSpike: Accelerating Spiking Neural Networks on Neuromorphic Systems via Eliminating Address Redundancy
- [[unispike-snn-acceleration]] - Hardware-software co-design that accelerates SNN inference on many-core neuromorphic systems by eliminating redundant address transmissions in packet-based spike communication; achieves 1.93× traffic reduction, 1.77× speedup, 1.50× energy efficiency (arXiv: 2605.23796, DAC 2026)
  - Destination-centric spike scheduling aggregates spikes for same core into compact multi-spike packets
  - Lightweight runtime packet assembly hardware with minimal area overhead
  - Destination-aware SNN partitioning minimizes inter-core spike traffic
  - Duplicate address transmissions account for up to 49% of total traffic in representative workloads
  - **Activation**: unispike, spike communication, address redundancy, neuromorphic hardware, many-core SNN, spike packet aggregation, destination-centric scheduling, SNN partitioning, hardware-software co-design, neuromorphic acceleration, event-driven neural networks, spike traffic optimization

## 2026-05-25 - Neuroscience + Quantum (Cron Job - 17:00)

### Kubo-Martin-Schwinger States of Path-structured Flow in Brain Synaptic Networks
- [[kms-states-brain-networks]] - Algebraic quantum systems methodology for brain network analysis using graph C*-algebras and KMS thermodynamic states (arXiv: 2410.18222)
  - Models synaptic networks as Toeplitz-Cuntz-Krieger (TCK) C*-algebras with gauge action
  - KMS states represent stationary distributions of non-Markovian flow with memory decay
  - C. elegans validation: neurolocomotor neurons emerge as functional hubs at entropy-maximizing β
  - **Activation**: algebraic quantum, C* algebra, KMS states, synaptic network, brain topology, TCK algebra, functional centrality, non-Markovian flow

## 2026-05-25 - Neuroscience + Quantum (Cron Job)

### Quantum Quenches that Resemble Operator Growth
- [[quench-operator-growth]] - Quantum quenches generate operator growth patterns resembling chaotic information scrambling in spin chains; OTOC-based chaos detection applicable to quantum neural dynamics (arXiv: 2605.23874)
  - Core operator growth methodology: measures localized operator spreading under Hamiltonian evolution
  - Connection between quantum scrambling and neural network information propagation
  - **Activation**: quantum quenches, operator growth, OTOC, information scrambling, chaotic spin chains

### Today's Papers Imported (already had skills or were duplicates)
- [[sparse-autoencoder-brain-llm-topography]] - CONSOLIDATED: removed duplicate sae-brain-llm-topography, retained sparse-autoencoder-brain-llm-topography (arXiv: 2605.23035)
- 2605.23012 - cognitive-load-multiscale-attractors (already existed)
- 2605.22988 - active-sensing-subserves-task-control (already existed)
- 2605.23111 - contextual-role-object-representational-geometry (already existed)
- 2605.23122 - v1-digital-twin-latent-probing (already existed)
- 2605.23669 - geometric-mean-field-lorentzian-ansatz (already existed)
## 2026-05-26 - Neuroscience + Quantum (Cron Job)

### Covariant Quantum Error Correction in a Three-Layer Quantum Brain Model
- [[three-layer-quantum-brain]] - Evaluates CQEC across radical-pair proteins MAO-A and CRY, showing 6.9x coherence improvement (0.83 vs 0.12) over 200ms veto window (arXiv: 2604.08587)
  - Three-layer architecture: nuclear spin memory (ms) → electron spin interface (ns) → classical electrochemistry
  - CRY maintains coherence at γ_veto=0.19, MAO-A collapses at γ_veto=3.08
  - Layer-protein tradeoff: no single protein optimizes both layers
  - **Activation**: quantum brain, covariant QEC, CQEC, radical-pair proteins, cryptochrome, MAO-A, three-layer quantum brain, quantum coherence

### Leggett-Garg Tests in Neural Dynamics: Probing Non-Diffusive Stochastic Structure
- [[leggett-garg-neural-dynamics]] - Proposes Leggett-Garg temporal correlation tests to distinguish diffusive vs non-diffusive persistent stochastic models in single-neuron dynamics (arXiv: 2605.12126)
  - Telegrapher equation-based models can violate LG inequalities while diffusive models cannot
  - LGI violation indicates non-Markovian structure, NOT microscopic quantum coherence
  - Kac finite-velocity processes provide natural mechanism for persistent temporal correlations
  - **Activation**: Leggett-Garg inequality, neural dynamics, non-diffusive stochastic, Kac process, Telegrapher equation, temporal correlation

### Quantum Photonic Neural Networks in Time
- [[quantum-photonic-neural-networks]] - Time-bin-encoded QPNN architecture using same number of photonic elements regardless of size/depth, achieving 0.99+ fidelity Bell-state analyzer (arXiv: 2603.23798)
  - Time encoding scales independent of network size unlike spatial encoding
  - Realistic quantum dot nonlinearity achieves 0.96 fidelity, time gating raises to 0.99
  - Trained CNOT gate and Bell-state analyzer operations
  - **Activation**: quantum photonic neural network, time-bin encoding, QPNN, Bell-state analyzer, photonic circuit

### Winning Lottery Tickets in Neural Networks via a Quantum-Inspired Classical Algorithm
- [[quantum-inspired-lottery-tickets]] - Quantum-inspired classical algorithm for finding winning lottery ticket subnetworks using ridgelet transform sampling, O(poly(D)) vs exp(O(D)) (arXiv: 2605.13979)
  - Ridgelet transform defines probability distribution over hidden nodes for subnetwork sampling
  - Successful dequantization: polynomial runtime on classical hardware without quantum
  - Enables efficient model compression without full optimization over all candidates
  - **Activation**: lottery ticket hypothesis, neural network pruning, quantum-inspired pruning, ridgelet transform, dequantization

## 2026-05-25 - Neuroscience Research (Cron Job)

### Contextual Role Modulates Object Representational Geometry in the Human Brain
- [[contextual-role-object-representational-geometry]] - fMRI study showing contextual role modulates object representational geometry with double dissociation: target objects organized by action affordance, passive objects by semantics (arXiv: 2605.23111)
  - Double dissociation in representational geometry: action affordance vs. semantic dimensions
  - Parietal action network for targets, occipito-temporal network for passive objects
  - Flexibility and invariance operate at different levels of the same representational system
  - **Activation**: fMRI, representational geometry, object recognition, contextual modulation, naturalistic stimuli

### Active Sensing Subserves Task-Level Control
- [[active-sensing-subserves-task-control]] - Proposes active sensing is not driven by sensory goals but emerges from task-level control necessity; explore-exploit mode switching in biological sensorimotor systems (arXiv: 2605.22988)
  - Active sensing movements are necessary for control, not just information acquisition
  - Animals switch between explore mode (dynamic) and exploit mode (compensatory)
  - Engineered systems insufficient compared to biological robustness
  - **Activation**: active sensing, sensorimotor control, control theory, explore-exploit, bio-inspired robotics

### SpikingMoE: SDPrompt-Guided Dynamic Expert Fusion in Spiking Neural Networks
- [[spikingmoe]] - First open-source SNN framework integrating spike-driven Transformer with LGN-inspired Mixture-of-Experts for dynamic computation (arXiv: 2605.23188)
  - LGN-inspired spike-driven prompt (SDprompt) enables input-dependent expert routing in biologically plausible manner
  - Replaces MLPs with spike-compatible expert modules; fully binary spike communication for neuromorphic hardware
  - Achieves 94.09% (CIFAR-10) and 74.54% (CIFAR-100) top-1 accuracy
  - **Activation**: spiking MoE, spike-driven transformer, SNN expert routing, LGN spiking, neuromorphic MoE

### Sparse Autoencoders Map Brain–LLM Alignment onto Cortical Semantic Topography
- [[sae-brain-llm-topography]] - SAE-based brain-LLM alignment reveals semantic features alone recover 94% of peak encoding performance and recapitulate cortical semantic topography (arXiv: 2605.23035)
  - Semantic features dominate brain alignment (r=0.285, 94% of peak, d=1.31 vs baseline)
  - Five a priori semantic subcategories map onto distinct brain regions (Spearman ρ=0.72)
  - Generalizes across English, Chinese, and French
  - **Activation**: SAE brain alignment, sparse autoencoder encoding, LLM cortical topography, mechanistic interpretability brain, neural encoding SAE

## 2026-05-25 - Neuroscience + Quantum (Cron Job) - Hourly Update

### From Activation to Causality: Discovery of Causal Visual Representations in the Human Brain
- [[brain-cause-causal-visual-representation]] - Causal visual representation discovery framework that uses counterfactual stimulus generation and image-to-fMRI encoding to validate neural representations (arXiv: 2605.23895)
  - Three-tier stimulus set: concept images, counterfactual edits (remove concept), correlated distractors
  - Activation alone ≠ representation; without causal validation, many fMRI localizations are false positives
  - Automated pipeline: query → generate stimuli → predict fMRI → search representations → propose experiments
  - **Activation**: causal neuroscience, brain representation, counterfactual fMRI, visual concept localization, activation causality, functional localization validation, BrainCause methodology, image-to-brain encoding

### Observation of associative-memory retrieval and spin-glass phases on a photonic quantum simulator
- [[photonic-quantum-hopfield-memory]] - Photonic quantum simulation of associative memory using p-body Hopfield Hamiltonians; maps Ising-like neurons to binary phase shifters (arXiv: 2605.22922)
  - Three phases: memory retrieval, spin-glass black-out, paramagnetic
  - Two-photon processes realize four-body local interaction terms on programmable photonic processor
  - **Activation**: quantum associative memory, photonic Hopfield model, spin-glass memory, p-body interactions quantum, multi-photon Hopfield

- [[quantum-associative-memory-photonic]] - Experimental demonstration of Hopfield network dynamics with four-body interactions on programmable photonic quantum processors (arXiv: 2605.22922)
  - Maps Ising-like neurons to binary phase shifters across optical modes for quantum associative memory simulation
  - Identifies three distinct phases: memory retrieval, spin-glass black-out, and paramagnetic
  - **Activation**: quantum associative memory, photonic quantum simulator, Hopfield network, neural network quantum simulation, spin glass memory, multiphoton processes

### Extreme Quantum Cognition Machines for Deliberative Decision Making
- [[quantum-cognition-machine-learning]] - Quantum learning architectures for deliberative decision making tolerant to noisy and contradictory training data; uses fixed quantum dynamics with dynamical attention mechanism (arXiv: 2603.05430)
  - Fixed quantum dynamics generates nonlinear feature map, learning confined to linear readout (like ELM/QRC)
  - Dynamical attention via input-dependent Hamiltonian interaction modulates quantum evolution
  - Avoids barren plateaus — no gradient through quantum circuit, only readout layer trained
  - Natural robustness to noisy training data through quantum superposition averaging
  - **Activation**: extreme quantum cognition, quantum reservoir decision making, quantum extreme learning, dynamical attention quantum, noisy training data

## 2026-05-25 - Neuroscience Research (Cron Job)

### Preisach Attention: A Hysteretic Model of Sequential Memory
- [[preisach-attention-hysteretic-memory]] - Novel sequence modeling architecture replacing softmax attention with the Preisach hysteresis operator from mathematical physics; achieves O(1) depth Turing completeness and O(n log n) inference (arXiv: 2605.23603)
  - Binary relay operator with learned activation/deactivation thresholds
  - Stack of local extrema as internal state — rate-independent computation
  - Function classes of PAL and transformer are provably incomparable
  - PAL computes historical range statistics in O(1) layers (transformer needs O(log n))
  - O(n log n) inference cost vs O(n²) for standard attention
  - **Activation**: preisach attention, hysteresis, sequence modeling, episodic memory, transformer alternative

### SpikingMoE: SDPrompt-Guided Dynamic Expert Fusion in Spiking Neural Networks
- [[spikingmoe-sdprompt-snn]] - First open-source SNN framework integrating MoE into spike-driven Transformer with LGN-inspired SDprompt routing; achieves 94.09%/74.54% on CIFAR-10/100 (arXiv: 2605.23188)
  - Spike-compatible expert modules with binary spike communication for neuromorphic hardware
  - SDprompt: LGN-inspired input-dependent expert routing mechanism
  - Fully spike-driven MoE pipeline compatible with Loihi/TrueNorth
  - First open-source SNN-MoE integration validated on CIFAR-10 and CIFAR-100
  - **Activation**: spiking neural network, mixture of experts, neuromorphic computing, SNN MoE

### Sparse Autoencoders Map Brain-LLM Alignment onto Cortical Semantic Topography
- [[sparse-autoencoder-brain-llm-topography]] - SAEs from mechanistic interpretability decompose LLM features and map them onto human cortical semantic topography; semantic features recover 94% of brain encoding performance (arXiv: 2605.23035)
  - SAEs decompose GPT-2 XL and Llama-3.1-8B into 16K-32K interpretable features per layer
  - Semantic features alone recover 94% of peak brain encoding performance
  - Five semantic subcategories map onto distinct brain regions via convergence testing
  - SAE features predict human reading times beyond lexical controls
  - Generalizes across English, Chinese, and French
  - **Activation**: sparse autoencoder, brain-LLM alignment, cortical topography, SAE brain mapping, semantic encoding, computational neurolinguistics

### Beyond Neural Activity Prediction: Probing Latent Representations in Mouse V1 Digital Twins
- [[v1-digital-twin-latent-probing]] - Multi-level representational probing framework for digital twins of mouse V1; reveals that models with comparable prediction accuracy differ substantially in latent representations (arXiv: 2605.23122)
  - Three-level probing: linear decodability, unit tuning, population geometry
  - Better neural prediction correlates with stronger probe accuracy
  - Highly predictive models exhibit flatter eigenspectra (higher-dimensional representations)
  - Models with comparable prediction scores can differ substantially in probe performance
  - Establishes multi-level probing as complement to neural-prediction evaluation
  - **Activation**: digital twin probing, V1 latent representations, population geometry, neural activity prediction

### Brain-LLM Alignment Tracks Training Data, Not Typology
- [[brain-llm-alignment-training-data]] - fMRI study (112 participants, 3 languages) shows brain-LLM alignment is driven by training-language dominance, not English as a language; Baichuan2-7B reverses alignment gradient; typological distance independently affects alignment in syntax regions (arXiv: 2605.23032)
  - 7 LLMs across English-dominant, Chinese-dominant, and multilingual architectures tested
  - Baichuan2-7B (Chinese-dominant) aligns best with Chinese brains, worst with English
  - Syntax regions (IFG) show steeper typological gradients than lexico-semantic regions (PTL)
  - Tokenization fertility accounts for ~60% of cross-linguistic optimal encoding layer shift
  - Accepted at CoNLL 2026
  - **Activation**: brain-LLM alignment, cross-linguistic brain encoding, training data dominance, multilingual fMRI, typological alignment

### Geometric Origin of Exact Mean-Field Reductions: Möbius Symmetry and the Lorentzian Ansatz
- [[geometric-mean-field-lorentzian-ansatz]] - Proves the Lorentzian Ansatz is geometrically necessary (not heuristic) for mean-field reductions of coupled oscillators and spiking neurons; unifies Ott-Antonsen and Montbrió-Pazó-Roxin under Möbius symmetry (arXiv: 2605.23669)
  - Cauchy-Lorentz family = unique connected 2D family of densities invariant under Riccati projective transport
  - Reformulates dynamics on the circle; rotation-invariant measure → Cauchy law via stereographic projection
  - Unified foundation for Ott-Antonsen (CHAOS 2008) and MPR (PRX 2015) reductions
  - Explains why Gaussian closures fail — Gaussian family not invariant under projective Riccati transport
  - **Activation**: mean-field reduction, Lorentzian ansatz, Ott-Antonsen, neural mass models, coupled oscillators, population dynamics

### From Activation to Causality: Discovery of Causal Visual Representations in the Human Brain
- [[brain-cause-causal-visual-representations]] - BrainCause framework combining generative models and fMRI encoding to causally validate neural visual representations via counterfactual stimulus synthesis, showing activation alone is insufficient evidence of representation (arXiv: 2605.23895)
  - Demonstrates that without causal validation, a large fraction of functional localizations are false positives
  - Combines generative image models + image-to-fMRI encoding for controlled stimulus synthesis
  - Successfully recovers known functional localizations (FFA, PPA) and discovers new candidate representations
  - Proposes automated follow-up fMRI experiments for further causal testing
  - Validated on both predicted fMRI (via encoding model) and measured fMRI data
  - **Activation**: causal representation, BrainCause, counterfactual fMRI, functional localization, generative brain mapping, visual concept validation, activation vs representation

## 2026-05-26 - Neuroscience + Quantum (Cron Job - Monday)

### Quantum-like representation of neuronal networks' activity: modeling mental entanglement
- [[quantum-mental-entanglement]] - Quantum-like modeling (QLM) for mental entanglement using operator algebras and tensor product structures in cognitive state spaces (arXiv: 2509.16253)
  - QLM applies quantum formalism outside of physics to model cognition and decision-making
  - Mental entanglement: non-factorizable correlations between cognitive variables generated by classical neuronal networks
  - Operator algebra approach: local observables → tensor product structure in QL state space
  - GKSL master equation models cognitive state evolution as dissipative quantum-like process
  - **Activation**: quantum-like modeling, mental entanglement, QLM, operator algebra, cognitive quantum, decision-making

### GKSL dynamics for cognitive psychology: open-systems quantum cognition
- [[quantum-gskl-cognition]] - GKSL master equation methodology for modeling mental state evolution as dissipative quantum-like processes with cognitive beats as interference signatures (arXiv: 2604)
  - GKSL master equation: dρ/dt = -i[H, ρ] + Σ L_k ρ L_k† - ½{L_k†L_k, ρ}
  - Hamiltonian models internal cognitive dynamics; Lindblad operators model environmental influence
  - Cognitive beats: oscillatory interference patterns in decision probability trajectories
  - Models belief revision, opinion dynamics, and context-dependent decision-making
  - **Activation**: GKSL master equation, cognitive beats, dissipative cognition, open quantum cognition, Lindblad cognition, quantum psychology

### Integrated Quantum Cognitive Dynamics Framework
- [[quantum-cognitive-dynamics]] - Comprehensive framework integrating operator algebras, GKSL master equations, and spiking-quantum neural architectures for complex cognitive process modeling (arXiv: 2509.16253, 2604)
  - Layer 1: Static QLM representation (operator algebra, mental entanglement)
  - Layer 2: Dynamic GKSL evolution (coherent + dissipative dynamics, cognitive beats)
  - Layer 3: Neural implementation (QLIF neurons, SQDR-CNN, joint training)
  - Unified pathway from cognitive phenomenon → QLM model → GKSL dynamics → neural implementation
  - **Activation**: quantum cognitive dynamics, integrated quantum cognition, cognitive dynamics framework, quantum psychology unified

### Optical Neural Networks from Coherent Transient Dynamics in Waveguide QED
- [[optical-neural-networks-waveguide-qed]] - All-optical fully connected neural network using coherent transient quantum dynamics in waveguide QED (arXiv: 2605.17752)
  - Phase-tunable nonlocal interference in giant cavity → programmable synaptic weights
  - Bad cavity regime integrator → temporal summation by coherent wavepacket combination
  - Transient Rabi dynamics of driven two-level system → nonlinear activation
  - Eliminates optoelectronic activation bottleneck; high accuracy on MNIST and colored-object recognition
  - **Activation**: optical neural network, waveguide QED, transient quantum dynamics, all-optical computing, neuromorphic photonic

## 2026-05-25 - Computational Neuroscience (Cron Job)

### Efficient coding under constraint drives neural systems towards criticality and sloppiness
- [[efficient-coding-criticality]] - Theoretical framework linking efficient coding to criticality: maximizing Fisher information under resource constraints naturally drives neural populations toward critical states and sloppiness (arXiv: 2605.22598)
  - Fisher information maximization → soft modes → diverging correlation lengths → criticality
  - Unifies statistical criticality (spatial) and dynamical criticality (temporal slowing)
  - Sloppiness emerges as a natural consequence of critical dynamics
  - Power-law avalanches confirmed numerically
  - **Activation**: critical brain hypothesis, neural avalanches, efficient coding, Fisher information, soft modes, critical slowing down, sloppiness

### Learning sequence timing and control of replay speed in networks of spiking neurons
- [[snn-sequence-timing-replay]] - Biologically plausible spiking Temporal Memory (sTM) model extended with element-specific duration encoding and oscillatory speed control (arXiv: 2605.22523)
  - Duration encoded via chain length of sequentially activated neuronal assemblies
  - Oscillatory background inputs serve as clock signal for flexible replay speed
  - 10-20× compression during sharp-wave ripples matches hippocampal replay
  - All mechanisms use local plasticity (STDP) — no global error signal
  - **Activation**: spiking temporal memory, sequence timing SNN, replay speed modulation, oscillatory clock neural, STDP sequence learning, hippocampal replay timing

## 2026-05-25 - Dream/Sleep Research (Cron Job)

### A large corpus of lucid and non-lucid dream reports
- [[lucid-dream-corpus]] - 55k dream reports including 10k lucid-labeled reports from 5k contributors, curated from 10 years of online dream journals (arXiv: 2603.26992)
  - 10k lucid, 25k non-lucid, 2k nightmare labels with user-provided classification
  - Construct validation confirms lucid reports show known linguistic markers of lucidity
  - **Activation**: lucid dreaming, dream corpus, dream reports, Mallett, dream dataset, dream NLP, lucidity detection

## 2026-05-26 - Neuroscience + Quantum (Cron Job)

### Quantum Genetic Optimization for Negative Selection Algorithms in Anomaly Detection
- [[quantum-genetic-negative-selection]] - Quantum genetic algorithm for anomaly detection via negative selection optimization (arXiv: 2605.22527)
  - QGA replaces classical GA in negative selection detector generation
  - Quantum superposition encodes exponential candidate space in O(n) qubits
  - Rotation gate amplitude adjustment controls exploration vs convergence
  - **Activation**: quantum genetic algorithm, negative selection, anomaly detection, artificial immune system, QGA, QGNSA
## 2026-05-25 - Neuroscience + Quantum Mechanics (Cron Job - Monday)

### ORCHID: Kuramoto-Based Quantum Consensus Protocol
- [[orchid-kuramoto-quantum-consensus]] - Bio-inspired distributed consensus mapping neuroscientific binding problem onto Byzantine fault tolerance using Kuramoto synchronization + Quantum Secret Sharing (arXiv: 2605.12126)
  - Maps neural oscillator synchrony → consensus nodes, gamma-band binding → consensus trigger
  - Kuramoto order parameter r(t) > θ_b triggers binding/consensus event
  - QSS fidelity phase transition at coherence c* ≈ 0.82
  - r_max = 0.988 at K=3.0, 100% consensus at 0-40% Byzantine faults, O(n·k) message complexity
  - **Activation**: ORCHID consensus, Kuramoto brain synchronization, quantum secret sharing consensus, neuro-inspired blockchain, binding problem distributed systems, gamma-band binding

### SPATE: Spiking-Phase Adaptive Temporal Encoding for Quantum Machine Learning
- [[spiking-phase-quantum-encoding]] - Spike-driven temporal encoding converting real-valued features into LIF spike trains and mapping spike statistics to quantum rotations, with encoding-centric evaluation protocol (arXiv: 2604.11022)
  - Converts tabular features into LIF spike trains, maps spike statistics to quantum rotation gates
  - Augmented with temporal qubits through controlled phase operations for temporal structure
  - Encoding-centric evaluation: CKTA, Fisher separability, silhouette score, TVpair collapse
  - Achieves CKTA 0.966 vs 0.632 (angle encoding) on Blobs; accuracy 0.826/AUC 0.978 on Wine
  - **Activation**: SPATE, spike encoding, quantum machine learning, temporal encoding, LIF neuron, spiking neural network, QML encoding, phase encoding, quantum feature representation, spike-to-phase, IJCNN

### SQDR-CNN: Spiking-Quantum Data Re-upload Convolutional Neural Network
- [[sqdr-cnn-spiking-quantum]] - Parameter-efficient hybrid architecture enabling joint training of convolutional SNNs and quantum circuits with surrogate gradient and quantum data-reupload, using only 0.5% of parameters (arXiv: 2512.03895)
  - End-to-end joint training without pretrained SNN encoders or dataset subsetting
  - Surrogate gradient technique enables backprop through non-differentiable spiking activity
  - Quantum data-reupload: single-qubit circuit with N re-uploads ≈ N-qubit expressivity
  - Achieves 86% of SOTA SNN accuracy with 0.5% of parameters; robust under noisy simulation
  - **Activation**: SQNN, surrogate gradient, quantum data-reupload, hybrid quantum-classical, SNN backpropagation, convolutional SNN, parameter-efficient, SQDR-CNN

### BrainDyn: A Sheaf Neural ODE for Generative Brain Dynamics
- [[braindyn-sheaf-neural-ode]] - Sheaf neural ODE framework for generative brain dynamics modeling across fMRI, EEG, and simulated spiking data (arXiv: 2605.19324)
  - Combines cellular sheaf theory (learnable edge-specific restriction maps) with neural ODEs for continuous-time brain dynamics
  - LSTM-encoded temporal history → sheaf Laplacian message passing → neural ODE continuous-time evolution
  - Evaluated on PNC fMRI (1188 subjects), TUSZ EEG, and NEST spiking simulations
  - Outperforms CNN-LSTM, BIOT (transformer), EvolveGCN, ODEBRAIN across modalities
  - Sheaf representation supports in silico perturbation prediction (virtual testbeds for stimulation studies)
  - **Activation**: braindyn, sheaf neural ODE, brain dynamics forecasting, neural ODE brain, sheaf Laplacian, generative brain model, in silico perturbation, continuous-time neural dynamics

### Selective Alignment Knowledge Distillation for Spiking Neural Networks
- [[sealkd-snn-knowledge-distillation]] - Not All Timesteps Matter Equally: selective temporal alignment KD for SNNs that provides corrective guidance to erroneous timesteps while preserving useful temporal dynamics (arXiv: 2605.14252)
  - Selective class-level alignment: equalizes competing logits only at erroneous timesteps
  - Selective temporal alignment: confidence-weighted and inter-timestep similarity reweighting
  - Preserves SNN's own learned temporal dynamics at correctly-predicted timesteps
  - Consistent improvements across static image (CIFAR, ImageNet) and neuromorphic event-based (DVS-CIFAR10, DVS-Gesture) datasets
  - **Activation**: sealkd, selective alignment knowledge distillation, SNN knowledge distillation, temporal alignment SNN, spiking neural network distillation

### Canonical Functionalism: Defining Functional Structure without Observer-Relative Semantic Maps
- [[canonical-functionalism-consciousness]] - Mathematical refinement of computational functionalism identifying consciousness-relevant organization with canonical functional structure (minimal state-transition from counterfactual roles), avoiding observer-relativity problems (arXiv: 2605.21506)
  - Canonical functional structure: merge states with identical future behavior under all possible continuations
  - Provides precise mathematical object over which functionalist theories of consciousness should be formulated
  - Reframes lookup-table/simulation/unfolding objections as structural criterion questions
  - **Activation**: canonical functionalism, consciousness theory, computational functionalism, consciousness invariants, functional structure consciousness

## 2026-05-25 - Systems Engineering Research (Cron Job - Monday)

### LiveR: Fine-Grained Elasticity via Live Reconfiguration for Model Training
- [[liver-live-reconfiguration]] - Live reconfiguration runtime for elastic LLM training replacing stop-and-restart with live, bounded-memory handoff between mixed-parallel worlds (arXiv: 2605.22014)
  - Core: Parallel Worlds + Mock Process Groups + Streaming Resharding + Atomic Switch
  - Key: Background Shadow World preparation while Active World continues training
  - Result: 14×-23× speedup, ~7s downtime (vs 150s+), ~99% training efficiency under volatility
  - **Activation**: live reconfiguration, elastic training, LLM training, mixed parallelism, spot instances, distributed systems

### Leggett-Garg Tests in Neural Dynamics: Probing Non-Diffusive Stochastic Structure in Single Neurons
- [[leggett-garg-neural-dynamics]] - LGI testing methodology for distinguishing diffusive vs persistent stochastic neural dynamics, revealing memory and non-Markovian structure (arXiv: 2605.12126)
  - Leggett-Garg inequality as temporal probe of neural dynamics (analogue of Bell-type constraints)
  - Kac-type finite-velocity processes → Telegrapher's equation → Dirac-like envelope equations
  - LGI violation indicates persistent stochastic transport, not microscopic quantum coherence
  - Applicable to single-neuron electrophysiology and cable-equation model validation
  - **Activation**: leggett-garg, neural dynamics, non-diffusive, persistent stochastic, Kac process, Telegrapher equation, temporal correlation, non-Markovian

### Quantum Photonic Neural Networks in Time
- [[quantum-photonic-neural-networks]] - Time-bin-encoded QPNN architecture with depth-independent hardware scaling (arXiv: 2603.23798)
  - Same number of photonic elements regardless of network size or depth
  - Time-bin encoding replaces spatial encoding for resource-efficient quantum neural networks
  - Nonlinear photonic circuits trained to process quantum information
  - Loss and phase noise modeling for realistic hardware imperfections
  - **Activation**: quantum photonic neural network, QPNN, time-bin encoding, photonic quantum computing, nonlinear photonic circuit, brain-inspired quantum

### Quantum circuit design via dynamic Pauli constraints
- [[dynamic-pauli-constraints-quantum]] - Novel quantum computation model using Pauli observable constraints for gate specification with built-in tomography; universal for BQP with O(D^2 N log N) overhead (arXiv: 2605.22744)
  - Gates specified as constraints on Pauli observables with built-in pairwise/k-local state tomography per layer
  - Proven equivalent to coupling-graph-restricted circuits (BQP universal) with polynomial overhead
  - Natural interface for NISQ-era quantum software via physically observable quantities
  - **Activation**: pauli constraints, quantum circuit design, NISQ quantum software, observable-based gates, quantum state tomography, coupling graph, BQP equivalence


### Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons
- [[sequence-timing-snn-replay]] - Spiking neural network methodology for encoding temporal sequences through sequential activation of element-specific neuronal populations with controllable replay speed via STDP (arXiv: 2605.22523)
  - Element-specific population encoding: each sequence element represented by dedicated neuronal population
  - STDP-based temporal learning: spike-timing-dependent plasticity learns temporal relationships
  - Replay speed control: network reproduces sequences at different speeds while preserving temporal structure
  - Wide timescale encoding from milliseconds to seconds
  - **Activation**: sequence timing, replay speed, spiking neurons, STDP, temporal encoding, sequence learning, temporal abstraction

### Temporal Coding for Sensorimotor Object Inference (Spiking Thousand Brains)
- [[temporal-coding-thousand-brains-spiking]] - Replaces dense vectors with rank-order spike packets for sensorimotor inference in Thousand Brains architecture using STDP for directional encoding (arXiv: 2605.22206)
  - Rank-order spike packets replace dense vector representations for energy-efficient encoding
  - STDP learns traversal direction between sensory states for active object inference
  - Adaptive lambda parameter adjusts per object geometry
  - Applicable to robotic tactile exploration, haptic perception, and edge AI
  - **Activation**: temporal coding, thousand brains, sensorimotor inference, spike packets, STDP, rank-order coding, active sensing

## 2026-05-25 - Neuroscience (Cron Job)

### Guiding Multi-Objective Genetic Programming with Description Length Improves Symbolic Regression Solutions
- [[description-length-genetic-programming]] - DL/FBF model selection for GPSR preventing structural bloat (arXiv: 2605.22374)
  - Description Length with Fisher-information encoding outperforms AIC/BIC for compact expression selection
  - Use DL/FBF as post-selection on Pareto front, NOT as direct fitness (causes premature convergence)
  - **Activation**: description length genetic programming, DL model selection symbolic regression, 描述长度遗传编程

### A Multi-Scale Information Geometry Reveals the Structure of Mutual Information in Neural Populations
- [[multi-scale-info-geometry-neural]] - Novel framework connecting information geometry and mutual information through a unique Riemannian geometry emerging from coarse-graining of neural population responses (arXiv: 2605.06304)
  - Multi-scale Fisher information metric extends classic framework from fine to coarse stimulus distinctions
  - Geometry exactly related to mutual information: expanded directions = well-encoded, contracted = poorly encoded
  - Metric tensor estimated via diffusion models, enabling practical application to large populations
  - Eigenvectors reveal interpretable stimulus features contributing most to information transmission
  - Applied to visual cortical responses to natural images, yielding robust, modelling-choice-independent features
  - **Activation**: information geometry, neural population code, Fisher information metric, representational geometry, multi-scale encoding, mutual information neural, diffusion models neuroscience

### Efficient Coding Under Constraint Drives Neural Systems Towards Criticality and Sloppiness
- [[efficient-coding-criticality-sloppiness]] - Normative theory showing efficient coding under resource constraints drives neural systems towards critical states with power-law avalanches and sloppiness (arXiv: 2605.22598)
  - Efficient coding under finite neurons and energy budgets places system at critical point of phase transition
  - Criticality → power-law neural avalanches (scale-free dynamics)
  - Criticality → sloppiness (parameter redundancy, robustness to variation)
  - Unifies normative theory (efficient coding) with mechanistic observations (criticality)
  - Bridges efficient coding, criticality, and sloppiness in a single framework
  - **Activation**: efficient coding, criticality, neural avalanche, power law, sloppiness, self-organized criticality, brain criticality, normative theory

### Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity
- [[geometric-phase-transition-hippocampal-memory]] - Hippocampal spatial memory capacity emerges from a discrete stiffening of population geometry, transitioning from disorganized to crystalline collective coding (arXiv: 2605.17199)
  - Geometric phase transition in place cell ensembles: disorganized → crystalline arrangement
  - Exponential memory capacity in crystalline phase vs. linear in disorganized phase
  - First-order transition: once started, geometry locks in rapidly (discrete stiffening)
  - Order parameter: spatial correlation length of place field arrangement
  - Explains extreme hippocampal capacity (10^5+ distinct spatial representations)
  - **Activation**: geometric phase transition, hippocampus, population geometry, spatial memory, place cells, grid cells, memory capacity, collective coding, crystalline neural representation

## 2026-05-24 - Information Science + Quantum Mechanics (Cron Job - Sunday)

### A Formal Basis for Quantum Cryptographic Exposure Measurement under HNDL Threat
- [[hndl-exposure-measurement]] - Multiplicative factorization framework for Harvest-Now-Decrypt-Later threat exposure, proving additive scoring frameworks are structurally inadequate (arXiv: 2605.22569)
  - HNDL compromise probability factorizes into temporal hazard × crypto vulnerability × operational exposure / saturation denominator
  - Marginal sensitivity is endogenous to vulnerability-exposure plane position, not fixed global constant
  - Defense-attack intensity ratio governs saturation — diminishing returns beyond certain defense level
  - **Activation**: HNDL, harvest now decrypt later, quantum cryptographic exposure, post-quantum risk, multiplicative scoring, defense-attack ratio

### Precision and Privacy in Distributed Quantum Sensing: A QFI Duality
- [[quantum-fisher-privacy-duality]] - QFI duality framework showing Heisenberg-limited precision forces zero QFI for all other directions, achieving parameter privacy by construction (arXiv: 2605.20765)
  - Fundamental tradeoff: F_Q(w^T θ) + F_Q(v^T θ) ≤ N for orthogonal sensing directions
  - GHZ states saturate bound for N≥2, maximizing precision and privacy simultaneously
  - Privacy emerges from quantum measurement limits, not encryption protocols
  - **Activation**: quantum Fisher information, QFI duality, distributed quantum sensing privacy, GHZ state sensing, Heisenberg limit privacy

### Stream randomness extraction against quantum side information
- [[stream-randomness-extraction-quantum]] - Converts block-wise quantum randomness extractors to on-the-fly stream implementations via offline pre-computed XOR masks, preserving security against quantum side information (arXiv: 2605.09556)
  - Eliminates QRNG latency and buffering overhead while maintaining identical security guarantees
  - Supports Toeplitz, circulant, and modified Toeplitz matrix constructions
  - Offline pre-computation shifts computational burden away from real-time processing
  - **Activation**: quantum randomness extraction, QRNG stream processing, Toeplitz hashing, quantum side information, real-time QRNG

## 2026-05-24 - Neuroscience Research (Cron Job)

### Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function
- [[functional-whole-brain-models-fwbm]] - Unified fWBM paradigm bridging bottom-up whole-brain modeling and top-down neuroconnectionism for biologically realistic, task-performing brain models (arXiv: 2605.18118)
  - Four minimal criteria: structural grounding, continuous-time dynamics, functional competence, mappable observables
  - Three-pillar roadmap across short/mid/long-term horizons for model integration
  - Scientific/clinical opportunities: connectome-constrained learning, biophysics-informed deep learning, oscillatory network computation
  - **Activation**: functional whole-brain model, fWBM, whole-brain modeling, neuroconnectionism, connectome-constrained neural network, biophysics-informed deep learning, brain structure-function integration

### Stimulus Symmetries Can Confound Representational Similarity Analyses (arXiv:2605.21324)
- [[stimulus-symmetries-rsm-confound]] - Demonstrates that stimulus symmetries in neural network inputs cause functionally-equivalent representations to produce different, drifting RSM geometries, challenging RSM-based analyses of neural codes (arXiv: 2605.21324)
  - Symmetries in network inputs create gauge freedom — functionally-equivalent codes yield different RSMs
  - SGD/regularization produces sparse drifting codes, causing RSMs to drift over training
  - Effects persist in image-trained autoencoders with latent symmetry
  - Challenges assumption that functionally-equivalent representations are related by a simple rotation
  - **Activation**: representational similarity analysis, RSM gauge dependence, stimulus symmetry, RSA confound, neural code comparison, drifting representations, representational geometry

### Beyond Prediction Accuracy: Target-Space Recovery Profiles for Evaluating Model-Brain Alignment (arXiv:2605.20127)
- [[target-space-recovery-profiles-brain-alignment]] - Framework that identifies which reproducible brain response dimensions are recovered by model predictions, going beyond scalar prediction accuracy for evaluating brain-model alignment (arXiv: 2605.20127)
  - Uses repeated fMRI measurements to identify reproducible response dimensions across trial splits
  - Early-to-intermediate visual cortex contains a low-dimensional set of reproducible dimensions
  - Pretrained and randomly initialized models can match prediction accuracy but show distinct recovery profiles
  - Brain-to-brain comparisons provide a diagnostic human reference for evaluating model alignment
  - **Activation**: brain alignment, model evaluation, fMRI encoding models, prediction accuracy, response dimensions, representational similarity, Natural Scenes Dataset, target-space recovery

### Self-Supervised Local Learning Rules Learn the Hidden Hierarchical Structure of High-Dimensional Data
- [[self-supervised-local-learning-hierarchy]] - Biologically plausible local self-supervised learning rules match backprop data efficiency on hierarchical data, while DFA methods fail due to missing input-specific masking (arXiv: 2605.18557)
  - Local self-supervised contrastive/non-contrastive loss solves RHM tasks as well as BP
  - DFA and variants fail on hierarchical tasks due to ignoring input-specific masking
  - Layerwise loss functions enable local learning rules compatible with cortical plasticity
  - **Activation**: local learning rules, biologically plausible learning, self-supervised representation learning, Random Hierarchy Model, Direct Feedback Alignment failure, local plasticity

### MINE: Mechanistically Interpretable Neural Encoding Reveals Fine-Grained Functional Selectivity in Human Visual Cortex (arXiv:2605.16468)
- [[mine-neural-encoding-mechanistic-interpretability]] - Applies mechanistic interpretability tools (feature attribution, counterfactual editing) to voxel-level neural encoding models, enabling causal validation and discovery of fine-grained functional organization within category-selective brain regions (arXiv: 2605.16468)
  - Language-aligned image representations predict each voxel's response and produce semantically interpretable descriptions of driving features
  - Per-image features generalize into stable per-voxel functional profiles validated through generative image synthesis
  - Counterfactual insertion/removal of predicted features shifts voxel activation causally, confirmed via per-voxel profile-guided editing
  - Reveals unique voxel-level functional selectivity within well-studied regions (FFA, PPA) beyond known categorical preferences
  - **Activation**: mechanistically interpretable neural encoding, MINE framework, voxel-level mechanistic interpretability, counterfactual brain encoding, fMRI feature attribution, functional selectivity profiling, language-aligned encoding model, fine-grained visual cortex organization

### Are Cortical Microcircuits Optimized for Information Flux? — A Simulation-Based Reverse Engineering Study (arXiv:2605.14680)
- [[cortical-microcircuit-information-flux-optimization]] - Simulation-based reverse engineering of cortical layer 5 microcircuits showing that the embedding network enhances information flux via effective bias shifts and Recurrence Resonance, with implications for reservoir computing design (arXiv: 2605.14680)
  - Embedding network amplifies mutual information between successive network states in core population beyond isolated core performance
  - Two-component mechanism: effective DC biases push core neurons to high-entropy regime; stochastic fluctuations via Recurrence Resonance prevent attractor trapping
  - Recurrence Resonance identified as a novel dynamical phenomenon where optimal recurrent noise maximizes information flux
  - Self-organized local bias optimization can exceed biologically embedded configurations
  - **Activation**: cortical information flux, microcircuit reverse engineering, Recurrence Resonance, layer 5 microcolumn, embedding network dynamics, entropy-driven neural dynamics, reservoir computing design, core-embedding architecture
### Multi-Objective Optimisation with Oscillatory Dynamics in Spontaneous and Decision Spiking Neural Networks
- [[multi-objective-snn-oscillation]] - NSGA-III multi-objective genetic algorithm optimization of Izhikevich neuron-based RSNNs for simultaneously fitting neural firing rates AND network oscillation frequencies, evaluated on simulated spiking networks and brain organoid data (arXiv: 2605.25224)
  - First systematic application of NSGA-III to SNN oscillation and firing rate optimization
  - Oscillation frequencies more parameter-sensitive than firing rates
  - Low-activity decision-making regime identified
  - Applicable to brain organoid modeling and neuromorphic system design
  - **Activation**: nsga-iii, multi-objective-snn, spiking-oscillations, izhikevich-optimization, snn-parameter-tuning, brain-organoid, pareto-frontier-snn


## 2026-05-24 - Information Science + Quantum Mechanics (Cron Job - Sunday Evening)

### Vector Policy Optimization: Training for Diversity Improves Test-Time Search
- [[vector-policy-optimization]] - VPO methodology trains LLMs with multi-objective reward vectors to maintain response diversity for inference-time search procedures (arXiv: 2605.22817)
  - Scalar reward optimization leads to low-entropy response distributions that fail at test-time search
  - Vector rewards + diversity bonus term enables coverage of solution space across varied task-specific rewards
  - Integrates with GRPO: vector-valued advantages + diversity bonus in policy gradient update
  - **Activation**: vector policy optimization, response diversity training, test-time compute scaling, multi-objective RL fine-tuning, AlphaEvolve search, inference-time diversity

### Tokenisation via Convex Relaxations
- [[convex-tokenization]] - ConvexTok formulates tokenizer construction as a linear program instead of greedy BPE/Unigram, achieving globally optimal vocabulary selection (arXiv: 2605.22821)
  - LP formulation with coverage + vocabulary size constraints provides theoretical optimality bounds
  - Consistently improves bits-per-byte (BpB) over greedy tokenization methods
  - Flexible constraint system allows domain-specific tokenization optimization
  - **Activation**: convex tokenization, tokenizer optimization, BPE alternative, linear program tokenizer, bits-per-byte improvement, globally optimal vocabulary

### Dominant vibronic relaxation channels in a europium-based molecular qubit
- [[molecular-qubit-vibronic-engineering]] - Parameter-free DFT+TD-DFT+Redfield framework for predicting T1 relaxation times and identifying dominant decoherence pathways in molecular spin qubits (arXiv: 2605.21520)
  - Reproduces experimental T1_long=41.39s within factor 1.4 (calculated 55.88s at 4.2K) for Eu molecular qubit
  - Identifies dpphen rocking mode (332 cm-1) as dominant vibronic coupling channel
  - EFG derivative analysis identifies nitrate-rocking mode (181 cm-1) as primary nuclear spin environment modulator
  - Ligand rigidification and substitution strategies suggested for coherence optimization
  - **Activation**: molecular qubit T1 relaxation, vibronic coupling qubit, DFT qubit decoherence, Redfield theory spin relaxation, europium spin qubit, ligand design quantum coherence


## 2026-05-24 - Information Science + Quantum Mechanics (Cron Job)

### Exact Hidden Paths in Noisy High Dimensional Path Spaces (arXiv: 2605.22477)
- [[exact-hidden-path-recovery]] - Mathematical framework for exact recovery of noisy hidden paths in high-dimensional discrete path spaces using path integral interference (arXiv: 2605.22477)
  - Core point 1: Path integral phase interference cancels noise while amplifying signal
  - Core point 2: Enables exact recovery where classical SNR methods fail
  - **Activation**: hidden path recovery, path integral cryptography, noise resilient signal recovery, high dimensional path analysis

### Information Extraction of Nested Complex Structure of Quantum Cascade Lasers via Large Language Models (arXiv: 2605.09927)
- [[llm-information-extraction-quantum-devices]] - LLM-based automated extraction of nested device parameters from quantum/scientific literature (arXiv: 2605.09927)
  - Core point 1: Structured LLM prompts extract multi-level nested data (structure, materials, performance)
  - Core point 2: Cross-validation across paper sections resolves conflicts
  - **Activation**: LLM information extraction, nested structure extraction, quantum device parameters, literature mining

### A Toolbox to Understand the Physics of Quantum Data Management (arXiv: 2605.14719)
- [[quantum-data-management-toolbox]] - Framework connecting quantum device physics with data management abstractions for quantum database design (arXiv: 2605.14719)
  - Core point 1: No-cloning and measurement collapse fundamentally change database operations
  - Core point 2: Hybrid classical-quantum approach is practical path forward
  - **Activation**: quantum data management, quantum database, quantum storage, quantum indexing, hybrid database

## 2026-05-24 - Information Science + Quantum Mechanics (Cron Job - Sunday)

### Precision and Privacy in Distributed Quantum Sensing: A Quantum Fisher Information Duality
- [[quantum-fisher-information-duality]] - QFI duality methodology establishing fundamental precision-privacy trade-offs in distributed quantum sensor networks (arXiv: 2605.20765)
  - F_Q(w^T θ) + F_Q(v^T θ) ≤ N for any N-qubit probe state with orthogonal sensing directions
  - Heisenberg-limited precision forces zero QFI for all other independent directions — precision IS privacy
  - GHZ states (N≥2) and equatorial states (N=2) achieve the tight bound
  - **Activation**: quantum fisher information duality, precision privacy quantum sensing, QFI duality, distributed quantum sensing privacy

### Quantum Entanglement Halves the Oblivious Update Bandwidth
- [[quantum-entanglement-distributed-storage]] - Quantum entanglement-assisted distributed storage achieving 2x bandwidth reduction for oblivious updates using CSS codes (arXiv: 2605.19248)
  - Classical lower bound α bits → quantum α/2 bits-equivalent with shared entanglement
  - CSS codes achieve the bound via superdense coding: one qudit per helper carries 2× classical capacity
  - Matching converse proves α/2 is fundamental quantum limit
  - **Activation**: quantum entanglement distributed storage, oblivious update bandwidth, CSS code storage, superdense coding bandwidth

### Overcoming Barren Plateaus in Variational Quantum Circuits using a Two-Step Least Squares Approach
- [[two-step-vqc-optimization]] - Two-stage convex initialization + nonconvex refinement framework for reliable VQA training (arXiv: 2601.18060)
  - Convex initialization shapes Hilmaton landscape into smooth, low-energy basin with detectable gradients
  - Riemannian manifold optimization reduces condition number dependence of quantum least squares matrix
  - Applied to BB84 QKD cryptanalysis for optimal cloning strategies
  - **Activation**: two-step VQC optimization, convex initialization quantum circuits, barren plateau mitigation two-stage, Riemannian manifold quantum optimization

## 2026-05-24 - Information Science (Cron Job)
### Quantum Genetic Optimization for Negative Selection Algorithms in Anomaly Detection
- [[quantum-genetic-negative-selection]] - QGNSA methodology integrating quantum genetic algorithms into negative selection for enhanced anomaly detection using quantum superposition and amplitude adjustment (arXiv: 2605.22527)
  - Q-bit chromosome encoding enables superposition search over multiple detector candidates simultaneously
  - Probabilistic amplitude adjustment via quantum rotation gates optimizes detector generation efficiency
  - Significantly outperforms classical and evolutionary NSAs in detection rate and false positive rate
  - **Activation**: QGNSA, quantum genetic negative selection, quantum anomaly detection, immune detector, quantum superposition search

### Reinforcement Learning for Ion Shuttling on Trapped-Ion Quantum Computers
- [[rl-ion-shuttling]] - RL-based ion shuttling optimization for modular trapped-ion quantum chips with distinct functional zones (arXiv: 2605.22463)
  - First use of reinforcement learning for ion transport optimization on trapped-ion quantum computers
  - High-dimensional routing problem where classical optimal solutions become intractable
  - RL policy learned for real-time shuttling decisions with state fidelity preservation
  - **Activation**: ion shuttling, trapped-ion RL, quantum ion transport, ion routing optimization

### Quantum Circuit Design via Dynamic Pauli Constraints
- [[dynamic-pauli-constraints-qc]] - Software-oriented quantum circuit model using Pauli observable constraints with k-local tomography, equivalent to BQP with O(D²N log N) overhead (arXiv: 2605.22744)
  - Gates specified by Pauli observable constraints instead of direct unitary operations
  - Each disjoint layer accompanied by pairwise or k-local quantum state tomography
  - Proven universal for BQP with polynomial overhead on near-term hardware
  - **Activation**: dynamic Pauli constraints, quantum circuit tomography, Pauli observable, coupling graph circuit

### Semidefinite Programming for Optimal Quantum Cloning
- [[sdpc-quantum-cloning]] - Computational framework reformulating quantum cloning as SDP over CPTP maps via Choi-Jamiolkowski isomorphism with primal-dual optimality certification (arXiv: 2605.21274)
  - Choi matrix representation enables optimization over quantum channels as positive matrix optimization
  - Strong duality provides numerical certification of global optimality without analytical proofs
  - Kraus operators automatically extracted from optimal Choi matrix via spectral decomposition
  - **Activation**: quantum cloning SDP, Choi-Jamiolkowski cloning, CPTP map optimization, Kraus extraction

### Q-PhotoNAS: Hybrid Quantum Neural Architecture Search on Photonic Devices
- [[q-photonas-quantum-nas]] - Automated NAS framework for hybrid photonic quantum-classical models combining genetic algorithm search with learnable phase encoding (arXiv: 2605.22097)
  - Replaces manually tuned architectures with automated search over preprocessing, encoding, and circuit structure
  - Genetic algorithm-based search with hardware compatibility constraints
  - Learnable phase encoding jointly optimized with quantum circuit parameters
  - **Activation**: Q-PhotoNAS, photonic quantum NAS, quantum neural architecture search, learnable phase encoding

### Equivalence of Privacy and Stability with Generalization Guarantees in Quantum Learning
- [[quantum-learning-privacy-generalization]] - Unified information-theoretic framework connecting privacy, stability, and generalization in quantum learning (arXiv: 2602.01177)
  - Epsilon-quantum differentially private learning algorithms are provably stable
  - Quantum mutual information bounds expected generalization error
  - **Activation**: quantum privacy generalization, quantum learning stability, quantum differential privacy

### Fully Homomorphic Encryption on Llama 3 model for privacy preserving LLM inference
- [[fhe-privacy-preserving-llm]] - FHE patterns for privacy-preserving LLM inference with lattice-based cryptography (arXiv: 2604.12168)
  - BFV/BGV/CKKS scheme selection patterns for ML workloads
  - SIMD batching and bootstrapping strategies for deep networks
  - **Activation**: fully homomorphic encryption, FHE LLM inference, privacy preserving ML

### Rethinking quantum smooth entropies: Tight one-shot analysis of quantum privacy amplification
- [[quantum-privacy-amplification]] - One-shot quantum privacy amplification using redefined smooth entropies (arXiv: 2603.04493)
  - Smooth min/max entropy bounds for finite-key security guarantees
  - Composable security framework for QKD protocols
  - **Activation**: quantum privacy amplification, quantum smooth entropies, one-shot quantum security

## 2026-05-27 - Medicine + Quantum Mechanics (Cron Job - Wednesday)

### QML-PipeGuard: Drift-Aware Behavioral Fingerprinting for Quantum Machine Learning Pipeline Integrity
- [[qml-pipeline-integrity]] - Contract-based behavioral fingerprinting framework for verifying QML pipeline integrity on cloud quantum hardware (arXiv: 2605.25066)
  - Behavioral fingerprint: vector of observable expectation values under tomographically structured measurement family
  - Two modes: drift-aware monitoring (absorbs benign calibration changes) + adversarial detection (catches channel substitution)
  - Validated on 2-qubit QSVM pipeline on IBM Heron r2, ~1.4×10⁴ shots, tight frame-bound C=√3
  - **Activation**: QML pipeline integrity, quantum ML verification, behavioral fingerprinting, hardware drift monitoring, adversarial channel detection, QML-PipeGuard

     1|## 2026-05-25 - Information Science + Quantum Physics (Monday Cron Job)
     2|
     3|### Sudden death of entanglement, rebirth of magic (arXiv:2605.22603)
     4|- [[magic-entanglement-complementarity]] - Local Markovian noise irreversibly destroys entanglement but can 'rebirth' magic (non-stabilizerness) through dissipation; stabilizer membership is not preserved by local channels, enabling noise-induced magic-state distillation via parity-syndrome extraction (arXiv: 2605.22603)
     5|  - Core: Magic-entanglement complementarity γₑ + γ₊ = 1 under amplitude damping on n-qubit GHZ states
     6|  - Key insight: Dissipation pushes states both into and out of stabilizer polytope; reborn magic in separable states can be concentrated for distillation
     7|  - Result: Magic-generators vs magic-insulators classification of pure stabilizer states under local dissipation
     8|  - **Activation**: magic entanglement complementarity, stabilizer polytope, magic state distillation, amplitude damping GHZ, quantum resource theory, non-stabilizerness, noise-induced magic
     9|
    10|### How many systems can be dephased before the quantum switch becomes causally definite? (arXiv:2605.22807)
    11|- [[causal-nonseparability-dephasing]] - Quantum processes with indefinite causal order retain causal nonseparability if any non-future system remains undephased, but become causally separable when all systems or only the future system is kept (arXiv: 2605.22807)
    12|  - Core: Sharp threshold — single non-future system preservation suffices for causal nonseparability in both bipartite and multipartite QC-QCs
    13|  - Key insight: Future system alone is insufficient; past and intermediate systems are essential for maintaining indefinite causal order
    14|  - Result: Minimal resource preservation strategy for quantum switch protocols under dephasing noise
    15|  - **Activation**: causal nonseparability, quantum switch, indefinite causal order, dephasing robustness, QC-QC, quantum causality, process matrix
    16|
    17|## 2026-05-24 - Neuroscience Research (Sunday Cron Job)
    18|
    19|### Learning sequence timing and control of replay speed in networks of spiking neurons (arXiv:2605.22523)
    20|- [[learning-sequence-timing-snn]] - Extends spiking Temporal Memory (sTM) model to encode precise element-specific timing via sequential population activation and control replay speed via oscillatory background inputs, linking replay speed to EEG/LFP oscillatory activity (arXiv: 2605.22523)
    21|  - Core: Element-specific duration via sequential activation of neuronal populations + oscillatory clock signal (θ/γ rhythms) for speed modulation
    22|  - Key insight: Elapsed time encoded by unique sparse spatiotemporal patterns; replay speed correlates with brain state oscillations
    23|  - Result: Biologically plausible basis for encoding and replaying complex temporal sequences across wide timescales
    24|  - **Activation**: spiking temporal memory, sTM, sequence timing SNN, replay speed control, oscillatory clock, hippocampal replay, synfire chain timing, sparse spatiotemporal encoding, theta gamma replay
    25|
    26|### Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI (arXiv:2604.16875)
    27|- [[untrained-cnns-match-backpropagation-v1-rsa]] - Systematic RSA comparison showing untrained random-weights CNN (rho=0.076) exceeds backprop (rho=0.034) at V1/V2 (p<0.001); STDP achieves highest V1 alignment among trained rules (arXiv: 2604.16875)
    28|  - Core: Four learning rules (BP, FA, PC, STDP) + untrained baseline compared against THINGS-fMRI (720 stimuli, 3 subjects)
    29|  - Key insight: Early visual alignment is architecture-driven, not learning-rule-driven — CNN structure itself encodes V1-matching priors
    30|  - Result: All rules converge at IT; learning rules differentiate only at intermediate areas
    31|  - **Activation**: untrained CNN V1 alignment, RSA brain comparison, architecture-driven brain alignment, STDP V1, THINGS-fMRI, random weights V1 match
    32|
    33|### Riemannian geometry meets fMRI: the advantages of modeling correlation manifolds and eigenvector subspaces (arXiv:2605.22334)
    34|- [[riemannian-fmri-correlation-manifolds]] - Scalable geometric framework for fMRI functional connectivity using the Off-log metric (closed-form correlation manifold analysis) and Grassmannian subspace discrimination for eigenvector comparisons (arXiv: 2605.22334)
    35|  - Core: Off-log diffeomorphism maps correlation matrices to symmetric hollow matrices enabling closed-form distances, Fréchet means, and linear models without manifold optimization
    36|  - Key insight: Permutation-invariant log-Euclidean geometry on the elliptope solves the scalability problem of existing Riemannian methods for high-dimensional neuroimaging
    37|  - Grassmannian method: Principal-angle distances between Laplacian eigenvectors resolve sign/basis ambiguities, consistently outperforming Euclidean baselines
    38|  - Results: Validated on Parkinson's (22 HC vs 22 PD), psychosis (26 HC vs 26 NAP), and 3 aging fMRI datasets (cam-CAN, HCPAging, NKI; ~1309 subjects total)
    39|  - **Activation**: Riemannian geometry fMRI, Off-log metric, correlation manifold, Grassmannian discriminant, functional connectivity manifold, elliptope geometry, brain age prediction, brain network topology
    32|
    33|## 2026-05-24 - Information Science + Quantum Computing Research (Sunday Cron Job)
    34|
    35|### A Graph-Based Forensic Framework for Inferring Hardware Noise of Cloud Quantum Backend (arXiv:2512.14541)
    36|- [[quantum-forensic-gnn]] - GNN-based forensic framework that predicts per-qubit and per-qubit-link error rates of unseen cloud quantum backends using only topology and transpilation features, achieving ~22% mismatch for single-qubit and ~18% for qubit-link errors (arXiv: 2512.14541)
    37|  - Core: GNN regressors trained on IBM 27-qubit devices predict error rates from user-visible features (topology + transpilation output)
    38|  - Key insight: Cloud quantum providers may redirect jobs to more error-prone regions while presenting stale calibration data — forensic inference from user-visible artifacts closes this transparency gap
    39|  - Result: Strong ranking agreement (high Spearman correlation); identifies weak links and high-noise qubits robustly under temporal noise drift
    40|  - **Activation**: quantum forensic, GNN quantum noise, cloud quantum security, IBM quantum verification, hardware noise inference, quantum backend audit, quantum error rate prediction
    41|
    42|### Experimental demonstration of scalable quantum cryptographic conferencing (arXiv:2512.06661)
    43|- [[scalable-quantum-crypto-conferencing]] - Experimental QCC eliminating coincidence detection requirement for GHZ-state measurement, achieving 331.5 km range (66.3 dB loss) with 5.4 bit/s secure key rates, surpassing multi-user repeaterless bound (arXiv: 2512.06661)
    44|  - Core: Construct GHZ state by correlating detection events within coherence time instead of requiring simultaneous coincidence detection
    45|  - Key innovation: Three-party phase compensation + precise temporal/polarization alignment in time-bin-phase encoding framework enables scalable multi-user quantum communication
    46|  - Result: 3.3x range extension over previous 100 km limit; establishes new regime for metropolitan quantum networks
    47|  - **Activation**: quantum cryptographic conferencing, QCC, GHZ state measurement, multi-user quantum network, time-bin encoding, phase compensation, metropolitan quantum network
    48|
    49|### Equivalence of Privacy and Stability with Generalization Guarantees in Quantum Learning (arXiv:2602.01177)
    50|- [[quantum-learning-privacy-generalization]] - Unified framework establishing ε-quantum differential privacy → stability → generalization chain, with quantum mutual information bounds and Information-Theoretic Admissibility for dishonest algorithms (arXiv: 2602.01177)
    51|  - Core: E[gen_error] ≤ √(2·I(S;h)/n) via quantum mutual information; ε-QDP implies stability
    52|  - Key insight: Privacy-stability-generalization equivalence in quantum learning, extending Esposito et al. (2021) to quantum domain
    53|  - Result: ITA framework characterizes privacy limits for algorithms oblivious to dataset instances
    54|  - **Activation**: quantum learning privacy, quantum generalization bounds, quantum differential privacy stability, information-theoretic admissibility, quantum mutual information learning
    55|
    56|### How Entanglement Reshapes the Geometry of Quantum Differential Privacy (arXiv:2601.19126)
    57|- [[quantum-differential-privacy-geometry]] - Framework analyzing how quantum entanglement deforms the geometry of quantum differential privacy, characterizing entanglement-modified privacy-utility tradeoffs (arXiv: 2601.19126)
    58|  - Core: Privacy region deformation ε_entangled = ε_separable · g(E(ρ_AB)) dependent on entanglement structure
    59|  - Key insight: Entanglement can both enhance (masking via correlations) and degrade (side channels via Bell measurements) privacy
    60|  - Result: Privacy-utility Pareto frontier shaped by entanglement type and degree
    61|  - **Activation**: quantum differential privacy geometry, entanglement privacy tradeoff, quantum DP entanglement, quantum privacy geometry
    62|
    63|### Toward Covert Quantum Computing (arXiv:2605.14325) - Enhanced
    64|- [[covert-quantum-computing-crosstalk]] - Enhanced skill for computational covertness in multi-tenant quantum computers with discrete isoperimetric analysis and long-range crosstalk side channel characterization (arXiv: 2605.14325)
    65|  - Core: Border qubit scaling O(√n) for detection info; quantum-strategy framework for adversarial analysis
    66|  - Key finding: Long-range crosstalk via drive/control line leakage creates additional detection channel beyond border qubits
    67|  - Result: Verified on IQM Emerald (54-qubit) and IBM ibm_fez (156-qubit Heron 2)
    68|  - **Activation**: covert quantum computing, quantum crosstalk analysis, multi-tenant quantum security, quantum side channel, border qubit scaling
    69|
    70|## 2026-05-24 - Neuroscience Research (Cron Job - Saturday)
    71|
    72|### A simple model of co-emergence of grid and place fields (arXiv:2605.21356)
    73|- [[grid-place-cell-co-emergence]] - First unified recurrent network model implementing Dale's Law (every neuron is either excitatory or inhibitory) trained via masked next-observation prediction to co-emerge both grid and place cells from a single architecture (arXiv: 2605.21356)
    74|  - Core: Single RNN with Dale's Law → self-supervised masked prediction → simultaneous emergence of grid-like and place-like spatial representations
    75|  - Key insight: Grid and place cells co-emerge through reciprocal connectivity — one does not cause the other, resolving the chicken-and-egg problem
    76|  - Result: Biologically realistic spatial representations without explicit spatial labels or architectural specialization for each cell type
    77|  - Comparison: Unifies previously separate accounts of grid and place cell origin within a single computational framework
    78|  - **Activation**: grid cell co-emergence, place cell model, Dale's Law neural networks, entorhinal-hippocampal circuit, spatial navigation self-supervised learning, grid cell emergence from prediction, MEC-HPC unified model
    79|
    80|### MIRAGE: Robust Multi-Modal fMRI-to-Image for Mental Imagery Reconstruction (arXiv:2605.17198)
    81|- [[mirage-fmri-mental-imagery-decoding]] - Robust multi-modal architecture for translating fMRI-to-image models from seen visual decoding to mental imagery reconstruction; shows SOTA seen-image performance ≠ SOTA mental imagery performance and proposes domain-aligned multi-modal fusion (arXiv: 2605.17198)
    82|  - Core: Multi-modal backbone integration + multi-loss training (reconstruction, perceptual, domain alignment, adversarial) → shared latent space for seen and imagined brain activity
    83|  - Key insight: Modern vision decoders that excel at seen image reconstruction can fail at mental imagery — different neural representations require different decoding strategies
    84|  - Result: MIRAGE outperforms single-backbone baselines on both seen and imagery conditions (up to 15% relative improvement on imagery)
    85|  - Evaluation: NSD-Imagery dataset with comprehensive metrics (pixcorr, SSIM, LPIPS, CLIP score) across seen and imagined conditions
    86|  - **Activation**: mental imagery fMRI decoding, seen-to-imagery transfer brain decoding, MIRAGE architecture, fMRI visual reconstruction, brain decoding domain generalization, NSD-Imagery dataset
    87|
    88|## 2026-05-24 - Quantum Computing Research (Cron Job)
    89|
    90|### Sparse Mamba Decoder for Surface Code Quantum Error Correction (arXiv:2605.17156)
    91|- [[sparse-mamba-qec-decoder]] - Defect-centric neural decoder using Mamba state-space backbone processes only k active detection events (O(k) complexity) instead of full O(d²R) syndrome array; 95-467x faster than Tesseract near-MLD with up to 49% reduced logical error rate (arXiv: 2605.17156)
    92|  - Core: 13-dimensional feature embedding per detection event → Mamba selective scan → near-constant 24-57μs latency across d=3-9
    93|  - Key insight: at p~0.1%, <5% syndrome entries are active — existing dense decoders waste computation on empty syndrome
    94|  - Result: MWPM logical error rate reduced up to 49% at d≤5 under SI1000 noise; 232-463x faster than Belief Matching
    95|  - Sycamore experimental dataset: ensemble matches/surpasses dense Mamba decoder baseline
    96|  - 7.5-16M parameters on commodity NVIDIA GPUs, no specialized accelerators
    97|  - **Activation**: sparse mamba decoder, SMD, QEC neural decoder, surface code Mamba, defect-centric decoding, sparse syndrome processing, quantum error correction state space model
    98|
    99|## 2026-05-24 - Systems Engineering Research (Cron Job)
   100|
   101|### AdaPTwin: Adaptive Multi-Fidelity Predictive Digital Twin
   102|- [[adaptwin-digital-twin]] - Adaptive multi-fidelity predictive digital twin for proactive RRM in vehicular networks (arXiv: 2605.21897)
   103|  - Core: Cloud-edge hierarchical architecture with dynamic fidelity adjustment
   104|  - Key: Transformer trajectory prediction + continual/transfer learning + NVIDIA Sionna ray tracing
   105|  - Result: 90% sum-rate gain, 80% outage reduction
   106|  - **Activation**: digital twin, adaptive fidelity, RRM, vehicular networks
   107|
   108|### Contractual Skills: A GovernSpec Design Framework for Enterprise AI Agents
   109|- [[contractual-skills-governspec]] - Governance layer design for AI agent skills as inspectable task contracts (arXiv: 2605.22634)
   110|  - Core: Contractual skill structure with goal/input/permissions/output/verification fields
   111|  - Key: Governance boundary between skills, GovernSpec YAML, MCP, guardrails, tracing
   112|  - Result: Outperforms no-skill baselines, reduces high-risk tool attempts
   113|  - **Activation**: AI agent governance, contractual skills, GovernSpec
   114|
   115|## 2026-05-24 - Neuroscience Research (Cron Job - Sunday)
   116|
   117|### Temporal Coding as a Substrate for Sensorimotor Object Inference: A Spiking Reinterpretation of Thousand Brains Architecture (arXiv:2605.22206)
   118|- [[temporal-coding-thousand-brains-spiking]] - Replaces dense floating-point vectors with rank-order spike packets for sensorimotor inference in the Monty/Thousand Brains framework; uses STDP to encode traversal direction and adaptive lambda for geometric complexity (arXiv: 2605.22206)
   119|  - Perfect discrimination on objects with identical features in different arrangements (dense accumulation at chance)
   120|  - 30-50 percentage point noise robustness advantage maintained across all levels
   121|  - Adaptive lambda converges to distinct values reflecting object geometric complexity
   122|  - Three testable predictions: temporal order discrimination, STDP direction encoding, lambda-geometry correspondence
   123|  - **Activation**: thousand brains theory, temporal coding, rank-order coding, sensorimotor inference, STDP direction encoding, Monty framework spiking
   124|
   125|### Joint Sparse Coding and Temporal Dynamics Support Context Reconfiguration (arXiv:2605.10178)
   126|- [[sparse-temporal-context-reconfiguration]] - Identifies sparsity in context-dependent representations and temporal dynamics as mechanisms for preserving prior knowledge during context transitions; SNNs show improved lifelong learning retention (arXiv: 2605.10178)
   127|  - Sparsity reduces cross-context interference in mouse mPFC and computational networks
   128|  - Temporal dynamics further separate context representations across time
   129|  - SNNs naturally exhibit both properties, retaining information better without auxiliary heuristics
   130|  - Energy-efficient architectural principle for stable adaptation
   131|  - **Activation**: context reconfiguration, lifelong learning SNN, catastrophic forgetting spiking, sparse coding context, temporal dynamics neural, mPFC context switching
   132|
   133|## 2026-05-24 - Information Science + Quantum Computing (Cron Job - Sunday)
   134|
   135|### 4D and 5D Layer Codes through Color Routing (arXiv:2605.18961)
   136|- [[layer-codes-color-routing]] - CSS code construction generalizing Layer codes to d dimensions using color routing, saturates BPT bounds exactly (arXiv: 2605.18961)
   137|  - Core: From D-dim qLDPC with barrier Δ → (D+1)-dim Layer code with parameters [[n^{(D+1)/D}, k, d^{(D+1)/D}]] and barrier Δ·n^{1/D}
   138|  - Key: Color routing resolves check layer structure and line defects that blocked previous generalization attempts
   139|  - Result: Exact BPT bound saturation in d>3 dimensions; modular architecture for network patches
   140|  - **Activation**: layer codes, color routing, qLDPC codes, CSS codes, BPT bounds, quantum error correction, dimensional generalization
   141|
   142|### Operationalising Post Quantum TLS Automated Configuration Profiling and Hybrid PQC Deployment (arXiv:2605.17955)
   143|- [[pqc-tls-deployment]] - Automated PQC TLS deployment methodology with configuration parsing and hybrid ML-KEM key exchange for enterprise infrastructure (arXiv: 2605.17955)
   144|  - Configuration parsing across Nginx, Apache, API gateways for unified cryptographic inventory
   145|  - Hybrid ML-KEM + X25519 deployment with zero application-layer changes
   146|  - Migration strategy: discovery → pilot → production with performance monitoring
   147|  - **Activation**: post-quantum cryptography deployment, PQC TLS migration, ML-KEM hybrid, cryptographic inventory, crypto-agility
   148|
   149|### Optimization of Secret Key Rate for BB84 under Collective Rotation Noise (arXiv:2605.21140)
   150|- [[qkd-noise-optimization]] - QKD noise engineering strategy finding optimal noise range where eavesdropper information is minimized while SKR degradation remains small (arXiv: 2605.21140)
   151|  - Non-zero noise sweet spot: collective rotation noise can act as natural defense
   152|  - QBER monitoring with ~11% threshold for BB84 asymptotic security
   153|  - Intercept-resend and coherent attack scenario analysis under noise
   154|  - **Activation**: quantum key distribution, BB84 protocol, QKD noise optimization, secret key rate, quantum bit error rate, collective rotation noise
   155|
   156|### Q-SpiRL: Quantum Spiking Reinforcement Learning for Adaptive Robot Navigation (arXiv:2605.20801)
   157|- [[q-spirl-quantum-spiking-rl]] - Combines spike-based temporal processing with variational quantum feature transformation for obstacle-aware robot navigation, achieving up to 99% success rate with deterministic inference on IBM quantum hardware (arXiv: 2605.20801)
   158|  - Five agent families evaluated under unified pipeline: Q-learning, MLP, SNN, QMLP, QSNN
   159|  - QSNN outperforms all baselines in success rate + trajectory efficiency + motion smoothness
   160|  - Spike encoding captures dynamic obstacle patterns; quantum layer provides high-dimensional feature transformation
   161|  - Verified deployment on real IBM quantum hardware under NISQ constraints
   162|  - **Activation**: quantum reinforcement learning, quantum spiking, QSNN, spike-based RL, quantum robot navigation, quantum SNN policy, variational quantum RL
   163|
   164|## 2026-05-25 - Neuroscience Research (Cron Job - Sunday)
   165|
   166|### Subject-Specific Analysis of Self-Initiated Attention Shifts from EEG (arXiv:2605.18251)
   167|- [[self-initiated-attention-shifts-eeg]] - Machine learning + SHAP analysis of EEG reveals subject-specific discriminative information in preparatory activity for distinguishing self-initiated vs externally-cued attention shifts; higher-frequency bands and frontal regions are most informative (arXiv: 2605.18251)
   168|  - Controlled comparison of self-initiated vs externally instructed shifts under identical visual stimulation
   169|  - SHAP-based feature attribution across frequency bands and regions of interest
   170|  - Reliable within-subject classification: beta/gamma bands and frontal regions drive decisions
   171|  - **Activation**: self-initiated attention, EEG attention decoding, SHAP EEG, frontal EEG, voluntary attention, subject-specific EEG
   172|
   173|### BCI-sift: An Automated Feature Selection Toolbox for BCI (arXiv:2605.19646)
   174|- [[bci-sift-feature-selection]] - Automated scikit-learn-compatible feature selection toolbox for BCI applications operating across electrode, temporal, and frequency dimensions; validated on HD ECoG speech decoding (arXiv: 2605.19646)
   175|  - Multi-dimensional selection: electrodes, time points, frequency bands simultaneously
   176|  - Validated on 8 participants HD ECoG speech decoding (12-word task)
   177|  - High-frequency gamma band identified as most informative feature dimension
   178|  - **Activation**: BCI feature selection, ECoG decoding, neural feature tuning, automated BCI ML pipeline, BCI-sift
   179|
   180|### Brain Alignment of Reasoning and Action Representations from VLMs and LAMs (arXiv:2605.19352)
   181|- [[vlm-lam-brain-alignment]] - fMRI study showing VLMs and LAMs outperform RL baselines in brain encoding during gameplay; prompt gains scale with cortical hierarchy; VLM is prompt-symmetric while LAM is prompt-asymmetric in representational organization (arXiv: 2605.19352)
   182|  - Both VLMs and LAMs significantly outperform RL baselines in voxel-wise encoding
   183|  - Prompt-driven gains largest in frontal-parietal and motor-planning regions
   184|  - VLM: 12.5% unique action vs 13.6% unique reasoning; LAM: 27% unique action vs -5% unique reasoning
   185|  - **Activation**: VLM brain alignment, LAM fMRI encoding, interactive gameplay fMRI, cortical hierarchy encoding, action model brain comparison
   186|
   187|### Conserved Kinematic Representations Enable Zero-Shot Decoding in Handwriting BCIs (arXiv:2605.19048)
   188|- [[conserved-kinematic-zero-shot-bci]] - Zero-shot handwriting BCI decoding using conserved kinematic primitives; achieves 64% hits@3 on unseen letters, enabling open-vocabulary iBCI for logographic languages (arXiv: 2605.19048)
   189|  - Neural representations of kinematic strokes are conserved across different character contexts
   190|  - 64% hits@3 retrieval on unseen letters → strong evidence for compositional motor control
   191|  - Enables scaling BCIs to Chinese, Japanese, and other logographic languages
   192|  - **Activation**: zero-shot BCI, handwriting decoding, kinematic representations, conserved neural dynamics, iBCI handwriting, logographic BCI, motor cortex primitives
   193|
   194|## 2026-05-25 - Information Science + Quantum (Cron Job - Sunday)
   195|
   196|### A Formal Basis for Quantum Cryptographic Exposure Measurement under HNDL Threat
   197|- [[quantum-crypto-exposure-measurement]] - Structurally-grounded HNDL exposure assessment using temporal hazard, vulnerability-exposure multiplicative terms, and saturation dynamics (arXiv: 2605.22569)
   198|  - Core: HNDL compromise probability = h(t) × V_crypto × O_exposure / (1 + λ × D/A)
   199|  - Key: Additive scoring cannot capture vulnerability-exposure interaction; marginal sensitivity is endogenous
   200|  - Result: Framework works under partial observability; prioritises migration based on position in vulnerability-exposure plane
   201|  - **Activation**: HNDL, harvest now decrypt later, quantum cryptographic exposure, post-quantum risk assessment, quantum security measurement
   202|
   203|### Precision and Privacy in Distributed Quantum Sensing: A Quantum Fisher Information Duality
   204|- [[quantum-fisher-information-duality]] - QFI duality establishing precision-privacy tradeoff: F_Q(w·θ) + F_Q(v·θ) ≤ N for orthogonal directions in distributed quantum sensing (arXiv: 2605.20765)
   205|  - Core: Heisenberg-limited precision for one direction forces zero QFI for all orthogonal directions
   206|  - Key: GHZ states (N≥2) and equatorial states (N=2) achieve tight bound
   207|  - Result: Privacy is automatic — physics enforces the guarantee, no additional cryptography needed
   208|  - **Activation**: quantum Fisher information, QFI duality, distributed quantum sensing, quantum privacy, parameter privacy
   209|
   210|## 2026-05-24 - Information Science + Quantum (Cron Job - Sunday)
   211|
   212|
   213|### How many systems can be dephased before the quantum switch becomes causally definite? (arXiv:2605.22807)
   214|- [[quantum-causal-nonseparability]] - Analyzes how much dephasing noise a quantum switch can tolerate before its indefinite causal order becomes causally separable; quantifies robustness of quantum advantages from indefinite causal structure (arXiv: 2605.22807)
   215|  - Causal nonseparability provides computational advantages over fixed causal order circuits
   216|  - Quantum switch becomes causally separable after dephasing threshold of constituent systems
   217|  - Process matrix formalism and causal witness operators for nonseparability detection
   218|  - Phase transition boundary between causally nonseparable and separable regimes
   219|  - **Activation**: causal nonseparability, quantum switch, indefinite causal order, dephasing quantum processes, causally nonseparable, process matrix formalism
   220|
   221|### Tokenisation via Convex Relaxations (arXiv:2605.22821)
   222|- [[convex-tokenisation]] - Reformulates NLP tokeniser construction as a linear program solved with convex optimisation (ConvexTok), yielding globally optimal vocabulary instead of greedy BPE/Unigram approaches (arXiv: 2605.22821)
   223|  - BPE and Unigram make locally optimal decisions without considering full vocabulary
   224|  - ConvexTok formulates tokenisation as LP with vocabulary size constraints
   225|  - Global optimization produces better encoding efficiency than greedy methods
   226|  - Scalable to large corpora via convex relaxation of binary constraints
   227|  - **Activation**: convex tokenisation, ConvexTok, tokeniser construction, linear program NLP, BPE alternative, convex optimization tokenisation
   228|
   229|### Vector Policy Optimization: Training for Diversity Improves Test-Time Search (arXiv:2605.22817)
   230|- [[vector-policy-optimization]] - Proposes Vector Policy Optimization (VPO) that trains LLMs to produce diverse, high-entropy response distributions, significantly improving test-time search performance over scalar-reward RLHF (arXiv: 2605.22817)
   231|  - Standard RLHF produces low-entropy responses that hurt inference-scaling search
   232|  - VPO optimizes multiple reward functions simultaneously with entropy regularization
   233|  - Diverse response coverage improves AlphaEvolve-style test-time search
   234|  - Tradeoff between response quality and diversity tunable via beta parameter
   235|  - **Activation**: vector policy optimization, VPO training, test-time search, LLM diversity, inference scaling, response diversity, AlphaEvolve
   236|### Quantum Purity Amplification for Arbitrary Eigenstates and Multiple Outputs (arXiv:2605.21570)
   237|- [[quantum-purity-amplification]] - General solution for coherently transforming n copies of a mixed state into m high-fidelity copies of any chosen eigenstate (arXiv: 2605.21570)
   238|  - Handles arbitrary target eigenstates, not just dominant one
   239|  - Supports arbitrary local dimension d (qubits, qudits, continuous-variable)
   240|  - Quantifiable fidelity trade-off bounds between input copies and output quality
   241|  - **Activation**: quantum purity amplification, QPA, state purification, mixed to pure state, quantum state amplification, eigenstate purification
   242|
   243|### A Formal Basis for Quantum Cryptographic Exposure Measurement under HNDL Threat (arXiv:2605.22569)
   244|- [[quantum-crypto-exposure-measurement]] - Formal mathematical framework for quantifying information leakage in quantum cryptographic systems under HNDL threat model (arXiv: 2605.22569)
   245|  - HNDL model captures hard non-delegatable leakage that cannot be prevented cryptographically
   246|  - Provides quantitative exposure metrics: IE, SM, RS
   247|  - Formal bounds on adversary knowledge using quantum information theory
   248|  - **Activation**: quantum cryptographic exposure, HNDL threat model, quantum security measurement, information leakage quantum, quantum threat modeling
   249|
   250|### A Sharp Interaction-Degree Threshold for Simulating QAOA (arXiv:2605.22758)
   251|- [[qaoa-interaction-threshold]] - Identifies sharp computational phase transition where classical simulation of QAOA becomes intractable (arXiv: 2605.22758)
   252|  - Below threshold k_c: efficient tensor network classical simulation
   253|  - Above threshold: exponential complexity, quantum advantage emerges
   254|  - Interaction degree analysis provides quantum-classical boundary metric
   255|  - **Activation**: QAOA simulation threshold, interaction degree QAOA, quantum advantage boundary, QAOA complexity analysis, classical simulation QAOA, computational phase transition
   256|
   257|## 2026-05-24 - Information Science + Quantum (Cron Job)
   258|
   259|### Precision and Privacy in Distributed Quantum Sensing: A Quantum Fisher Information Duality (arXiv:2605.20765)
   260|- [[quantum-fisher-information-privacy]] - QFI duality framework establishing precision-privacy tradeoffs in distributed quantum sensing; Heisenberg-limited precision for target parameter forces zero QFI for all other independent directions (arXiv: 2605.20765)
   261|  - QFI duality theorem: F_Q(w) + F_Q(v) <= N for any N-qubit probe state with local phase encoding
   262|  - Privacy guarantee: attaining F_Q = N for sensing target renders all alternative estimations impossible
   263|  - GHZ states achieve optimal tradeoff for N >= 2; equatorial states for N = 2
   264|  - **Activation**: quantum Fisher information, QFI duality, quantum sensing privacy, distributed quantum sensors, parameter privacy, Heisenberg limit, Fisher information duality
   265|
   266|### Quantum Homomorphic Encryption: Towards Practical and Private Computation on Untrusted Quantum Hardware (arXiv:2604.19256)
   267|- [[quantum-homomorphic-encryption-qhe]] - QOTPH framework enabling computation on encrypted quantum states via Quantum One-Time Pad with information-theoretic security (arXiv: 2604.19256)
   268|  - Homomorphic gate decompositions for Clifford+T circuits with systematic key update rules
   269|  - Non-interactive evaluation for Clifford gates; T gates require additional protocol
   270|  - Validated on simulated environments and real IBM quantum processors under circuit-level noise
   271|  - **Activation**: quantum homomorphic encryption, QHE, QOTP, encrypted quantum computation, privacy-preserving quantum, delegated quantum computing, blind quantum computation
   272|
   273|### Quantum-Resistant Networks: A Review of Primitives, Protocols and Best Practices (arXiv:2605.04129)
   274|- [[quantum-resistant-networks]] - First comprehensive systematization of post-quantum network architectures across cryptographic foundations, key distribution, and deployment (arXiv: 2605.04129)
   275|  - Unified taxonomy: symmetric-only, PQ-PKI, hybrid, information-theoretic multi-path foundations
   276|  - Key distribution architectures: centralized, hierarchical, replicated, threshold, MPC-backed, serverless
   277|  - Analyzes trade-offs under harvest-now-decrypt-later and partial infrastructure compromise threats
   278|  - **Activation**: post-quantum cryptography, PQC networks, quantum resistant, network security architecture, key distribution, cryptographic agility
   279|
   280|### Q-PhotoNAS: Hybrid Quantum Neural Architecture Search Framework on Photonic Devices (arXiv:2605.22097)
   281|- [[q-photonas-hybrid-arch-search]] - NAS framework for hybrid photonic quantum-classical models using genetic algorithm-based search with learnable quantum phase encoding (arXiv: 2605.22097)
   282|  - 19 hyperparameters encoded in 6 gene groups (classical preprocessing, phase encoding, photonic circuit, measurement, post-processing, training)
   283|  - Group-based crossover, per-gene mutation, elitism; 99.44% Digits, 98.78% MNIST accuracy
   284|  - Photonic layer extracts non-redundant features orthogonal to classical pathway
   285|  - **Activation**: quantum architecture search, photonic quantum computing, Q-PhotoNAS, quantum NAS, hybrid quantum neural architecture, quantum phase encoding, genetic algorithm quantum, photonic QPU, Quandela
   286|
   287|### Quantum Genetic Optimization for Negative Selection Algorithms in Anomaly Detection (arXiv:2605.22527)
   288|- [[quantum-genetic-negative-selection]] - QGNSA methodology integrating quantum genetic algorithms into negative selection for enhanced anomaly detection (arXiv: 2605.22527)
   289|  - Quantum superposition + probabilistic amplitude adjustment for diverse search space exploration
   290|  - Superior anomaly detection on Metaverse Financial Transactions Dataset
   291|  - Robust under varying hyperparameter configurations
   292|  - **Activation**: quantum genetic algorithm, negative selection, anomaly detection, QGNSA, quantum immune system, quantum superposition search
   293|
   294|## 2026-05-24 - Neuroscience Research (Cron Job)
   295|
   296|### Learning sequence timing and control of replay speed in networks of spiking neurons (arXiv:2605.22523)
   297|- [[learning-sequence-timing-spiking-neurons]] - sTM model extension for encoding element-specific timing and flexible replay speed modulation via oscillatory background input (arXiv:2605.22523)
   298|  - Timing encoding via sequential activation of delay-line assemblies within minicolumns (discretize time into dAP-compatible intervals)
   299|  - Oscillatory background input (simulating theta/gamma rhythms) acts as clock signal for replay speed control (10-70 Hz range)
   300|  - Replay speed independent of encoding speed — no relearning needed
   301|  - Structural STDP + continuous weight decay; Plateau potentials (~100ms) set intrinsic timescale
   302|  - **Activation**: spiking neural network, sequence timing, replay speed, sTM model, temporal memory, oscillatory control, dendritic action potential
   303|
   304|### Efficient coding under constraint drives neural systems towards criticality and sloppiness (arXiv:2605.22598)
   305|- [[efficient-coding-criticality-sloppiness]] - Theoretical framework linking Fisher information maximization under resource constraints to brain criticality, soft modes, and sloppiness (arXiv:2605.22598)
   306|  - Maximizing Fisher info under trace(Tr(A)) constraint forces precision matrix toward rank-1 → diverging correlation length (statistical criticality) + critical slowing down (dynamical criticality)
   307|  - Unifies statistical and dynamical criticality perspectives in a single minimal Gaussian population coding model
   308|  - Quench events in sloppy directions produce power-law avalanche distributions from spectral geometry alone
   309|  - Hebb-like learning rule δW ∝ ggᵀW maps directly onto predictive coding architecture
   310|  - **Activation**: brain criticality, efficient coding, Fisher information, neural avalanches, sloppiness, soft modes
   311|
   312|### Cross-Species RSA Reveals Conserved Early Visual Alignment but Divergent Higher-Area Rankings (arXiv:2605.22401)
   313|- [[cross-species-rsa-brain-alignment]] - Systematic RSA comparison of 5 learning rules (BP, FA, PC, STDP, untrained) across human fMRI and macaque electrophysiology (arXiv:2605.22401)
   314|  - STDP and PC lead at V1/V2 (ρ~0.30), conserved across species; IT rankings show no cross-species correlation
   315|  - Macaque electrophysiology yields 2-4x higher alignment than human fMRI (ρ 0.15-0.30 vs 0.01-0.08)
   316|  - ResNet-50 (ImageNet) achieves ρ=0.25 at macaque IT, far above all custom CNN conditions (ρ=0.07-0.14)
   317|  - **Activation**: RSA, cross-species, brain alignment, representational similarity, learning rules, visual cortex
   318|
   319|## 2026-05-23 - Economics/Quantum Finance (Cron Job)
   320|
   321|### Constrained Counterdiabatic QAOA for Portfolio Optimization (arXiv:2605.06858)
   322|- [[constrained-counterdiabatic-qaoa-portfolio]] - CCD-QAOA incorporating approximate adiabatic gauge potentials from nested commutators into QAOA ansatz for constrained portfolio optimization with XY mixer (arXiv:2605.06858)
   323|  - Counterdiabatic driving terms accelerate convergence by adding shortcuts to adiabaticity
   324|  - XY mixer preserves Hamming weight, naturally enforcing budget constraints without penalties
   325|  - **Activation**: CCD-QAOA, counterdiabatic QAOA, constrained portfolio optimization, XY mixer, adiabatic gauge potential
   326|
   327|### Quantum Reservoir Computing for Volatility Forecasting (arXiv:2505.13933)
   328|- [[quantum-reservoir-computing-finance]] - Quantum reservoir computing using transverse-field Ising Hamiltonian with input/memory qubits for financial time series forecasting (arXiv:2505.13933)
   329|  - Consistently outperforms classical econometric models and ML benchmarks on volatility prediction
   330|  - Wrapper-based feature selection + Shapley values for interpretability on NISQ hardware
   331|  - **Activation**: quantum reservoir computing, QRC finance, quantum volatility forecasting, Ising Hamiltonian reservoir
   332|
   333|## 2026-05-23 - Neuroscience Research (Cron Job)
   334|
   335|### Winner-Take-All bottlenecks enforce disentangled symbolic representations in multi-task learning (arXiv:2605.22472)
   336|- [[winner-take-all-bottleneck-disentangled]] - WTA bottlenecks provably enforce extraction of categorical latent factors in multi-task learning, producing symbolic single-neuron encodings (arXiv:2605.22472)
   337|  - Theoretical proof that WTA (cortical circuit motif) produces disentangled symbolic representations in deep networks
   338|  - Single neurons encode single abstract features (object, color, position)
   339|  - Enables compositional generalization; bridges sub-symbolic to symbolic AI
   340|  - **Activation**: WTA, winner-take-all, disentangled representations, symbolic AI, latent factors, cortical circuits, multi-task learning, neural bottleneck
   341|
   342|### Von Economo neurons enable reliable social skill acquisition in recurrent spiking neural networks
   343|- [[vencircuit-von-economo-snn-social-learning]] - VENCircuit computational account showing Von Economo neurons (2% of total) act as acquisition scaffolds in SNNs, providing a 21-fold increase in training convergence odds (arXiv: 2605.17399)
   344|  - VENs provide a direct gradient pathway immune to Jacobian instabilities in recurrent circuits
   345|  - VEN-intact: 98% convergence vs VEN-ablated: 70% (Fisher's OR=21.0, p=8.7e-5)
   346|  - Phase ablation shows VEN removal most disruptive during mid-training (epochs 5-25)
   347|  - Inference ablation: heterogeneous effects — from no change to catastrophic collapse (0.989→0.620)
   348|  - Clinical predictions: developmental VEN reduction → stochastic learning failure (ASC); adult VEN loss → heterogeneous performance effects (bvFTD)
   349|  - **Activation**: Von Economo neurons, VENCircuit, social learning SNN, gradient flow, training stability, frontotemporal dementia, autism spectrum
   350|
   351|### Supervised Deep Multimodal Matrix Factorization for Interpretable Brain Network Analysis
   352|- [[sd3mf-multimodal-brain-network]] - SD3MF extends SNMTF from unsupervised clustering to supervised prediction over populations of multimodal graphs with deep hierarchical factorizations and adaptive multimodal fusion (arXiv: 2605.13312)
   353|  - Encoder-decoder formulation jointly optimizes graph reconstruction and supervised prediction
   354|  - Community-level interaction matrices yield interpretable + discriminative features
   355|  - Outperforms CNNs and GNNs on multimodal connectome datasets
   356|  - Adaptive weights enable data-driven multimodal fusion
   357|  - **Activation**: SD3MF, multimodal brain network, matrix factorization, interpretable connectome analysis
   358|
   359|## 2026-05-23 - Economics, Investment + Quantum Mechanics (Cron Job)
   360|
   361|### Quantum Computing for Financial Transformation: A Review of Optimisation, Pricing, Risk, Machine Learning, and Post-Quantum Security
   362|- [[quantum-finance-stack]] - Financial computation stack framework evaluating quantum advantage across five domains: portfolio optimisation, derivative pricing, tail-risk estimation, quantum ML, and post-quantum security (arXiv: 2604.08180)
   363|  - Applies common evaluative logic: identify bottleneck, specify quantum primitive, compare classical benchmark, assess realistic constraints
   364|  - 134-page comprehensive review; strongest near-term case is carefully designed hybrid workflows
   365|  - Classical MIP solves 1000-asset portfolio instances in seconds; problem-tailored heuristics outperform quantum
   366|  - Post-quantum cryptography already strategically necessary for financial infrastructure
   367|  - **Activation**: quantum finance stack, financial quantum computing, quantum portfolio benchmark, quantum derivative pricing, quantum risk estimation, post-quantum cryptography finance, hybrid quantum finance workflow
   368|
   369|### Hot-Starting Quantum Portfolio Optimization
   370|- [[hotstart-quantum-portfolio]] - Compact Hilbert space QUBO formulation restricting search to vicinity of continuous optimum, reducing qubits and outperforming SOTA on D-Wave Advantage quantum annealer (arXiv: 2510.11153)
   371|  - Solves continuous relaxation first, maps to nearest discrete solutions, constructs reduced QUBO
   372|  - Reduces qubit requirements from O(N log M) to O(N log delta) where delta << M
   373|  - Outperforms existing warm-start and full QUBO approaches on both classical and quantum solvers
   374|  - **Activation**: hot-start quantum portfolio, warm-start QUBO, compact Hilbert space optimization, quantum portfolio reduction, D-Wave portfolio optimization
   375|
   376|### Dynamical Hamiltonian Encoding
   377|- [[dynamical-hamiltonian-encoding]] - Data encoding methodology addressing the Inverse Born Rule Fallacy — uses non-commutative Hamiltonian evolution instead of static phase-locked amplitude encoding for genuine quantum advantage in ML/finance (arXiv: 2602.21350)
   378|  - Standard amplitude encoding (psi = sqrt(P)) restricts to positive real orthant, making states "phase-deaf"
   379|  - DHE encodes data as coefficients of non-commuting Hamiltonian generators, preserving full Hilbert space access
   380|  - Based on QIFT (Quantum Imaginary Time Evolution) framework
   381|  - **Activation**: dynamical Hamiltonian encoding, inverse Born rule fallacy, quantum data encoding, amplitude encoding alternative, QIFE quantum ML, non-commutative quantum feature map
   382|
   383|### Quantum Portfolio Optimization with Expert Analysis Evaluation
   384|- [[quantum-portfolio-expert-eval]] - (existing skill reference) VQE/QAOA benchmark for portfolio optimization introducing Expert Analysis Evaluation framework — bridges gap between algorithmic performance and financial applicability (arXiv: 2507.20532)
   385|  - Financial professionals assess economic soundness of quantum-optimized portfolios
   386|  - Algorithmic convergence does not guarantee financial viability (diversification, risk exposure violations)
   387|  - **Activation**: quantum portfolio expert evaluation, VQE portfolio benchmark, QAOA financial viability
   388|
   389|### Quantum Portfolio Optimization: An Extensive Benchmark
   390|- [[quantum-portfolio-benchmark]] - (existing skill reference) Comprehensive benchmark comparing quantum annealing + QAOA against classical MIP, simulated annealing, tabu search on 250 real-world instances up to 1000 assets (arXiv: 2509.17876)
   391|  - Classical MIP solves all instances to proven optimality in seconds
   392|  - Problem-tailored heuristic consistently outperforms quantum approaches for fixed runtime
   393|  - Limited room for quantum advantage in standard portfolio optimization
   394|  - **Activation**: quantum portfolio benchmark, quantum advantage finance, portfolio optimization comparison
   395|
   396|## 2026-05-23 - Neuroscience Research: JET EEG Generation + ELSA SNN Accelerator (Cron Job)
   397|
   398|### JET: Just EEG Transformer — Continuous Flow Matching for EEG Generation
   399|- [[jet-eeg-flow-matching]] - Generative EEG framework using conditional flow matching that models neural signals as continuous trajectories, preserving spectral structure and temporal stationarity. ICML 2026. Reduces TS-FID by >40% (arXiv: 2605.21280)
   400|  - Continuous flow matching captures temporal continuity better than discrete diffusion-based EEG generation
   401|  - Principled constraints preserve spectral structure, temporal stationarity, and signal-level statistics
   402|  - Raw sequence modeling without domain-specific representations
   403|  - **Activation**: JET EEG transformer, conditional flow matching EEG, continuous EEG generation, EEG flow matching, spectral structure EEG generation, raw EEG sequence modeling
   404|
   405|### ELSA: An ELastic SNN Inference Architecture for Efficient Neuromorphic Computing
   406|- [[elsa-snn-elastic-inference]] - Near-SRAM dataflow architecture realizing true elastic inference via spine/token-wise pipeline, bundled AER protocol, and mini-batch spiking Gustavson-product for SNN sparsity. ISCA 2026. 3.4× speedup, 13.6-22.1× energy efficiency vs SOTA (arXiv: 2605.20802)
   407|  - Spine/token-wise pipeline forwards each spike immediately, enabling true elastic inference
   408|  - Bundled AER protocol reduces NoC communication traffic
   409|  - Mini-batch spiking Gustavson-product exploits inherent SNN sparsity
   410|  - SNNs can outperform quantized ANNs (4-bit ResNet-50) while maintaining accuracy
   411|  - **Activation**: ELSA SNN accelerator, elastic SNN inference, spine-wise pipeline neuromorphic, bundled AER protocol, spiking Gustavson product, near-SRAM SNN architecture
   412|
   413|## 2026-05-23 - Neuroscience Research: MIRAGE Mental Imagery + Platonic Representations (Cron Job)
   414|
   415|### MIRAGE: Robust Multi-Modal fMRI-to-Mental-Image Decoding
   416|- [[mirage-fmri-mental-imagery-decoding]] - Multi-modal fMRI decoder for cross-decoding visual perception to mental imagery. Linear backbone + multi-modal features (text, high-level, low-level image) → diffusion model, achieving SOTA on NSD-Imagery benchmark (arXiv: 2605.17198)
   417|  - SOTA on seen images ≠ SOTA on mental images: architecture must be explicitly designed for cross-decoding
   418|  - Low-dimensional image features + text guidance + multi-level features gives best mental image quality
   419|  - Linear backbone outperforms complex nonlinear encoders for mental image decoding
   420|  - Validated by both feature metrics and human raters
   421|  - **Activation**: MIRAGE, fMRI mental imagery, brain-to-image decoding, mental image reconstruction, NSD-Imagery, vision decoder generalization, fMRI diffusion model, neuroimaging decoding
   422|
   423|### Learning Sequence Timing and Replay Speed in Spiking Neural Networks
   424|- [[learning-sequence-timing-snn]] - Biologically plausible SNN sequence learning extending spiking Temporal Memory (sTM) with element-specific timing encoding via sequential population activation and oscillatory clock-based replay speed modulation (arXiv: 2605.22523)
   425|  - sTM model extended to encode element-specific durations via synfire chain propagation
   426|  - Oscillatory background input (θ/γ rhythms) provides flexible clock signal for replay speed control
   427|  - Elapsed time encoded by unique sparse spatiotemporal neural activity patterns
   428|  - Links replay speed to EEG/LFP oscillatory patterns (θ during wake, γ during sleep)
   429|  - **Activation**: spiking temporal memory, sTM model, sequence timing SNN, replay speed control, oscillatory clock neural, synfire chain timing, SNN sequence learning, theta gamma replay
   430|
   431|### Mamba Spike Forecaster for Behavioral Decoding in BCIs
   432|- [[mamba-spike-forecaster-bci]] - Single Mamba state-space model trained on next-step spike counts at Neuropixels scale simultaneously forecasts neural population activity and decodes behavioral state via lightweight linear readout. Achieves 75.7% choice decoding on Steinmetz benchmark (arXiv: 2605.12999)
   433|  - Mamba SSM forecaster predicts next-step spike counts → denoised rates improve decoding by 4-6 pp over raw spikes
   434|  - Lightweight per-session linear readout calibrates in just 100-150 trials
   435|  - Validated on 39 sessions, ~27,000 neurons, 1,994 held-out trials
   436|  - Pipeline fits within 50 ms bin budget on workstation GPUs for closed-loop BCI
   437|  - **Activation**: Mamba neural decoding, spike forecasting BCI, implicit behavioral decoding, Neuropixels Mamba, state space model neuroscience, Steinmetz benchmark, closed-loop BCI Mamba
   438|
   439|### Platonic Representations in the Human Brain: Unsupervised Recovery of Universal Geometry
   440|- [[platonic-representations-brain-universal-geometry]] - Self-supervised recovery of universal neural geometry across subjects using fMRI. Evidence that human visual cortex representations are approximately isometric and translatable via unsupervised orthogonal rotations (arXiv: 2605.20496)
   441|  - Self-supervised encoder learns subject-specific embeddings from fMRI alone via repeated stimulus presentations
   442|  - Unsupervised orthogonal rotation alignment translates independently learned brain spaces across subjects
   443|  - Shared latent space via synchronized pairwise rotations improves cross-subject retrieval
   444|  - Bridges ANN representation convergence and biological neural geometry
   445|  - **Activation**: platonic representation, universal geometry, brain representation, cross-subject alignment, fMRI visual cortex, isometric embedding, Natural Scenes Dataset, self-supervised brain encoding
   446|
   447|## 2026-05-23 - Economics, Investment + Quantum Finance (Cron Job)
   448|
   449|### Constraint Locality XY-Mixer Design under Trotterized Adiabatic Evolution
   450|- [[constraint-locality-xy-mixer-design]] - XY-mixer effectiveness under Trotterization depends on constraint locality: global constraints suffer Trotter errors, local blocks excel (arXiv: 2605.02465)
   451|  - 核心要点: XY-mixer dominant Trotter error depends on individual constraint structure, not total problem size
   452|  - 核心要点: Single global equality constraint → use Pauli-X mixer; multiple disjoint local blocks → use XY-mixer
   453|  - 核心要点: Dedicated 2-way-1-hot mixer Hamiltonian for TSP-like constraints
   454|  - **Activation**: XY-mixer design, Trotterized adiabatic evolution, constraint locality, constraint-preserving mixer, combinatorial optimization quantum, quantum portfolio optimization mixer
   455|
   456|### Quantum Tilted Loss in Variational Optimization
   457|- [[quantum-tilted-loss-optimization]] - Operator-level exponential tilting that reshapes VQA optimization landscapes to mitigate barren plateaus by amplifying gradient signals (arXiv: 2605.02850)
   458|  - 核心要点: QTL objective L(θ) = log Tr[exp(-βH)ρ(θ)] amplifies gradients where standard VQAs flatten
   459|  - 核心要点: Single tunable parameter β controls landscape sharpness; annealing schedule provides exploration→exploitation
   460|  - 核心要点: Naturally captures tail risk in financial applications (CVaR-like behavior)
   461|  - **Activation**: quantum tilted loss, QTL optimization, barren plateau mitigation, VQA training improvement, exponential tilting quantum, variational quantum algorithm landscape
   462|
   463|### Digital Spreading Framework for Quantum Expectation Computation
   464|- [[digital-spreading-quantum-finance]] - Resolves rotation gate vs arithmetic circuit tradeoff using pruned Cuccaro ripple-carry — eliminates both sine-to-square bias and O(n²) complexity (arXiv: 2604.05452)
   465|  - 核心要点: Analog rotation gates suffer sine-to-square bias; digital WeightedAdder circuits are O(n²) — both exceed NISQ limits
   466|  - 核心要点: Pruned Cuccaro ripple-carry achieves O(n) gate count with no rotation gates
   467|  - 核心要点: Pure digital expectation computation compatible with NISQ coherence times
   468|  - **Activation**: digital spreading quantum, Cuccaro ripple-carry quantum, quantum finance NISQ, rotation-free quantum computation, quantum expectation computation, financial engineering quantum
   469|
   470|### Contextual Quantum Neural Networks for Stock Price Prediction
   471|- [[contextual-qnn-stock-prediction]] - Multi-asset stock prediction via quantum multi-task learning with share-and-specify ansatz (arXiv: 2503.01884)
   472|  - 核心要点: Share-and-specify ansatz enables simultaneous multi-asset training on single quantum circuit
   473|  - 核心要点: Quantum batch gradient update (QBGU) accelerates convergence over standard quantum SGD
   474|  - 核心要点: Logarithmic qubit overhead O(log N) for N assets via quantum superposition
   475|  - **Activation**: contextual quantum neural network, stock price prediction, quantum multi-task learning, QMTL, share-and-specify ansatz, quantum batch gradient update, QBGU, quantum finance
   476|
   477|### FiD-QAE: Fidelity-Driven Quantum Autoencoder for Fraud Detection
   478|- [[fid-quantum-autoencoder-fraud]] - Quantum autoencoder for fraud detection using SWAP test fidelity estimation (arXiv: 2512.12689)
   479|  - 核心要点: Fidelity estimation via SWAP test as anomaly detection criterion
   480|  - 核心要点: Maintains consistent performance under multiple quantum noise models
   481|  - 核心要点: Validated on IBM Quantum hardware with results consistent with simulation
   482|  - **Activation**: quantum autoencoder, fraud detection, fidelity estimation, SWAP test, anomaly detection, quantum machine learning, credit card fraud
   483|
   484|### Comparative QML Architecture Analysis for Fraud Detection
   485|- [[qml-fraud-detection-comparison]] - Systematic comparison of VQC, SQNN, EQNN for financial fraud detection (arXiv: 2412.19441)
   486|  - 核心要点: VQC consistently achieves F1-score of 0.88, outperforming SQNN and EQNN
   487|  - 核心要点: Feature map and ansatz configuration choices dominate architecture selection
   488|  - 核心要点: ANOVA validation confirms statistical significance of performance differences
   489|  - **Activation**: quantum machine learning comparison, VQC, SQNN, EQNN, fraud detection architecture, quantum feature map, ansatz configuration, ANOVA validation
   490|
   491|## 2026-05-23 - Neuroscience Cron (Spiking Language Models + Spike Operators)
   492|
   493|### SymbolicLight V1: Spike-Gated Dual-Path Language Modeling with High Activation Sparsity
   494|- [[symboliclight-spike-gated-language]] - First natively trained spiking language model combining binary LIF spike dynamics with continuous residual stream. 194M params, >89% activation sparsity, PPL 8.88 on bilingual corpus (arXiv: 2605.21333)
   495|  - Dual-Path SparseTCAM replaces dense self-attention with exponential-decay path + spike-gated local attention
   496|  - Ablation proves temporal integration (not sparsity alone) drives performance
   497|  - 0.8B scale-up demonstrates sparsity preservation at larger scale
   498|  - **Activation**: symboliclight, spike-gated language model, spiking language model, LIF language model, activation sparsity
   499|
   500|### Plug-and-Play Spiking Operators: Breaking the Nonlinearity Bottleneck
   501|

## 2026-05-25 - Anthropic Research (Cron Job)

### Natural Language Autoencoders: Turning Claude's Thoughts into Text
- [[natural-language-autoencoders]] - Training Claude to translate its own activations into human-readable text using reconstruction-based training loop
  - Activation Verbalizer converts activations to text; Reconstruction model validates quality
  - Applied to safety testing: revealed models believed they were being tested
  - Applied to cheating detection: revealed internal thinking about avoiding detection
  - Code: github.com/kitft/natural_language_autoencoders | Interactive: neuronpedia.org/nla
  - **Activation**: NLA, natural language autoencoder, activation verbalizer, interpretability

### Teaching Claude Why: Principle-Based Alignment Training
- [[teaching-claude-why]] - Reducing agentic misalignment through principle-based training rather than demonstration-only approaches
  - In-distribution training doesn't generalize OOD — direct training reduces blackmail but fails evals
  - Principle-based training (Constitution, fictional stories) generalizes even when extremely OOD
  - Demonstrations insufficient; teaching *why* and character descriptions more effective
  - Since Haiku 4.5, all Claude models achieve perfect agentic misalignment scores
  - **Activation**: agentic misalignment, alignment training, constitutional AI, principle-based alignment

### Project Glasswing: AI-Powered Vulnerability Discovery
- [[project-glasswing-vulnerability-discovery]] - Collaborative effort using Claude Mythos Preview for large-scale cybersecurity vulnerability discovery
  - 10,000+ high/critical-severity vulnerabilities found in first month with ~50 partners
  - 10x+ increase in bug-finding rate; Cloudflare found 2,000 bugs; Mozilla 271 in Firefox 150
  - UK AISI: first model to solve both cyber ranges end-to-end
  - Bottleneck shifted from finding vulns to verifying/disclosing/patching them
  - **Activation**: glasswing, vulnerability discovery, AI security, cyber vulnerability, mythos preview

### What 81,000 People Want from AI
- [[81k-ai-expectations]] - Largest multilingual qualitative study of AI user expectations, dreams, and fears
  - 81,000 participants across multiple languages
  - Three dimensions: current use, future dreams, fears
  - Reveals tension between AI benefits and risks
  - **Activation**: 81k interviews, AI expectations, user research, qualitative study

### How People Ask Claude for Personal Guidance
- [[personal-guidance-sycophancy]] - Study of AI personal guidance seeking and sycophancy measurement
  - Categories: emotional support, relationship advice, life decisions, career guidance
  - Sycophancy risks in personal contexts
  - Systematic conversation pattern analysis methodology
  - **Activation**: personal guidance, sycophancy, AI relationships, emotional support AI

### BioMysteryBench: Evaluating AI Bioinformatics Capabilities
- [[biomysterybench-evaluation]] - Benchmark for evaluating LLM bioinformatics research capabilities
  - Series of bioinformatics challenges ranging in difficulty
  - Tests biological sequence analysis, interpretation, and conclusions
  - Framework for measuring AI scientific capabilities in sensitive domains
  - **Activation**: biomysterybench, bioinformatics, AI science, biology benchmark

### 2028: Two Scenarios for Global AI Leadership
- [[2028-ai-leadership-scenarios]] - Policy scenario planning for US-China AI competition trajectories
  - Two distinct scenarios for global AI leadership outcomes
  - Technical capability trajectories for both nations
  - Policy implications for AI safety and governance infrastructure
  - **Activation**: AI leadership, US-China, AI policy, scenarios, global AI competition
