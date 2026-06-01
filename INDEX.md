
## 2026-06-02 - Computer Science + Quantum Computing (Cron Job - Hourly)

### AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle
- [[memory-centric-agentic-research]] - 记忆中心化的全科研生命周期自动化系统,四模块架构(SciMem/SciFlow/SciDAG/SciEvolve)实现持久化、可进化的研究代理 (arXiv: 2605.31468)
  - SciMem双层记忆:长期知识记忆(LTKM)跨项目复用,活跃研究记忆(ARM)项目级管理
  - SciFlow五阶段生命周期:文献理解→假设生成→实验→论文撰写→回复评审
  - SciEvolve反馈循环:用户/实验/评审反馈转化为版本化更新
  - **Activation**: memory-centric agent, agentic research, autonomous scientist, research lifecycle automation, SciMem, SciFlow, SciDAG, SciEvolve

### LinTree: Improving LLM Reasoning with Explicitly Structured Search Histories
- [[structured-search-llm-reasoning]] - 显式父指针结构使LLM推理链搜索历史真正可用,在Blocks World/Sokoban/Navigation全面超越隐式推理 (arXiv: 2605.31492)
  - 原始搜索历史不足以超越启发式搜索,必须显式表示树结构
  - 简单父指针标注使回溯时精确识别复用的搜索状态
  - 同时优于隐式推理模型和LLM启发式搜索
  - **Activation**: structured reasoning, search tree LLM, linearized tree reasoning, parent pointer reasoning, LinTree, explicit search structure



## 2026-06-02 - Neuroscience Research (Cron Job - Evening Update)

### The Metastable Mind: Neural Underpinnings of Naturalistic Cognition
- [[metastable-mind-event-segmentation]] - 统一事件分割认知理论与 metastable 神经活动的计算框架，证明两者研究同一 metastable 状态 (arXiv: 2605.31473)
  - 时空嵌套层级：高层慢状态约束底层快状态，形成多尺度计算
  - 神经状态反映预测模型，塑造感知、决策、记忆编码与提取
  - 状态边界为网络重构期，信息整合峰值出现在边界
  - **Activation**: metastable mind, event segmentation, metastable neural activity, MNA, neural states hierarchy, naturalistic cognition, event boundaries, metastable dynamics

## 2026-06-02 - Neuroscience Research (Cron Job)

### Dual-Spectral Flow Matching for fMRI Time Series Generation
- [[dual-spectral-flow-matching-fmri-generation]] - Wavelet+DCT双频表示结合光谱流匹配生成生理合理的BOLD信号,ICLR 2026 accepted (arXiv: 2605.30387)
  - Wavelet分解捕获多尺度瞬态动力学,DCT投影实现能量紧缩
  - 光谱流匹配在余弦频域生成类条件样本
  - 下游脑疾病分类准确率82.6%,超越真实数据增强效果
  - **Activation**: fMRI generation, BOLD signals, spectral flow matching, wavelet DCT, brain disorder identification, DSFM

## 2026-06-02 - Computer Science + Quantum Computing (Cron Job - Hourly + 3 New Skills)

### Attention-based optimizer for symmetry finding
- [[attention-quantum-symmetry]] - Set-Transformer架构搜索Pauli对称性,用自注意力编码Pauli串间的高阶关联 (arXiv: 2605.30429)
  - Set-Transformer自注意力编码Pauli串间成对及高阶关联,生成候选对称性
  - 基于对易关系的优化目标: [S,H]≈0 验证对称性,物理哈密顿量近乎确定性成功
  - **Activation**: attention symmetry finding, quantum symmetry optimizer, Set-Transformer Hamiltonian, Pauli symmetry detection

### Generative Quantum Data Embeddings for Supervised Learning
- [[generative-quantum-embedding]] - 基于能量的生成学习框架合成门序列优化量子数据嵌入,Wasserstein距离预判优化收益 (arXiv: 2605.30866)
  - 保真度代理目标引导搜索最优嵌入结构,提升分类可分性
  - Wasserstein距离提供先验诊断:经典数据几何决定嵌入优化是否有显著收益
  - **Activation**: quantum data embedding, generative quantum circuit, Wasserstein quantum, quantum encoding optimization

### QASM-Eval: LLM Evaluation for OpenQASM-3 Beyond Quantum Circuits
- [[qasm-eval-llm-quantum]] - 首个OpenQASM-3硬件面向特性LLM评估数据集,覆盖经典逻辑/时序调度/脉冲控制 (arXiv: 2605.30358)
  - 4000训练任务+100测试任务,验证涵盖语法/量子态/时间线三维
  - 前沿LLM在OpenQASM-3编码任务上表现很差,针对性微调效果显著
  - **Activation**: QASM-Eval, OpenQASM-3 LLM, quantum programming benchmark, pulse-level quantum programming

### A hidden bottleneck in classical and quantum linear reservoir computing
- [[linear-reservoir-computing-bottleneck]] - 分析线性储层计算中的隐藏信息瓶颈,识别量子储层计算的真实优势 (arXiv: 2605.29071)
  - 线性储层动力学只能重分布特征,无法创造新的固定延迟表达能力
  - 单光子操作超越线性储层限制,成为量子储层计算的真实资源
  - **Activation**: linear reservoir bottleneck, reservoir computing capacity, quantum reservoir advantage

### A Quantum Algorithm for Simulating Nonunitary Dynamics Governed by Nonautonomous Linear Ordinary Differential Equations
- [[quantum-nonunitary-ode-simulation]] - 无需预先知道传播子的量子非幺正动力学模拟算法 (arXiv: 2605.29052)
  - 直接在量子硬件上执行dilation,无需经典计算机逐步计算传播子
  - 适用于非自治线性ODE系统: dv/dt = A(t)v, A(t)非斜对称
  - **Activation**: quantum nonunitary simulation, nonautonomous ode quantum, quantum algorithm dilation

## 2026-06-02 - Computer Science + Quantum (Cron Job)

### Spectral Anatomy of Quantum Gaussian Process Kernels
- [[spectral-anatomy-quantum-kernels]] - Unified spectral entropy diagnostic S(K)/log n for QGP kernels (arXiv: 2605.30952)
  - Normalized spectral entropy governs dequantization and posterior pathologies
  - Kernel-agnostic: hardware-efficient, matchgate, IQP, RBF all collapse onto same curves
  - Verified on IBM Heron hardware with median error 3.2%
  - **Activation**: quantum gaussian process, spectral entropy, quantum kernel diagnostic, Nystrom approximation, Bach degrees of freedom

### Q-ANCHOR: Federated Quantum Learning with ZNE-guided Correction
- [[q-anchor-federated-quantum-learning]] - QFL architecture addressing double-drift (client drift + hardware bias) (arXiv: 2605.30075)
  - ZNE-guided server anchoring eliminates hardware bias floor
  - Stateful client correction suppresses client drift from non-IID data
  - Proves convergence under noisy quantum gradient estimates
  - **Activation**: Q-ANCHOR, federated quantum learning, QFL, zero-noise extrapolation, quantum federated aggregation

### Support Vector Machine with a Scalable Quantum Kernel
- [[hamming-quantum-kernel-svm]] - Hamming quantum kernel avoids exponential concentration, scales to 27 qubits (arXiv: 2605.31449)
  - Uses full measurement statistics instead of single fidelity value
  - Outperforms fidelity kernel at 15+ qubits, classical Gaussian on synthetic data
  - Classical post-processing only, zero additional quantum resources
  - **Activation**: hamming quantum kernel, quantum SVM, exponential concentration, scalable quantum kernel

### Experimental demonstration of quantum advantage in communication complexity for Euclidean distance problem
- [[quantum-fingerprinting-communication]] - Quantum fingerprinting with coherent states shows advantage at input size 10^8 (arXiv: 2605.31516)
  - SMP model: Alice/Bob send quantum fingerprints to referee for distance computation
  - Amplitude modulation encoding + SNSPD detection for practical implementation
  - Surpasses best classical protocol for diverse data types including grayscale images
  - **Activation**: quantum fingerprinting, communication complexity, Euclidean distance, SMP model, coherent states


## 2026-06-01 - Neuroscience (Cron Job - 4 New Papers)

### Bridging Brains and Machines: A Unified Frontier
- [[bridging-brains-machines-neuro-ai]] - Position paper identifying convergence of neuroscience, AGI, and neuromorphic computing toward unified paradigm (arXiv: 2507.10722)
  - Neurobiological-to-AI architecture mapping (synaptic plasticity→fine-tuning, spike-based→sparse attention)
  - Physical substrates for brain-scale efficiency: memristive, quantum, photonic devices
  - 4 critical challenges: spiking+foundation models, lifelong plasticity, embodied language, ethical safeguards
  - **Activation**: neuroscience AGI convergence, neuromorphic computing, brain-inspired AI, synaptic plasticity AGI

### Brain Functions as Thermal Equilibrium States
- [[thermal-equilibrium-connectome]] - Algebraic quantum model where brain functions emerge as KMS thermal equilibrium states of connectome graph algebra (arXiv: 2408.14221)
  - Graph algebra of C. elegans connectome → KMS equilibrium states → functional networks
  - Integration Capacity (IC) index quantifies neuronal coordination effectiveness
  - Structure-function bridge: topology-driven functional connectome prediction
  - **Activation**: algebraic quantum neuroscience, KMS formalism, thermal equilibrium brain, integration capacity

### Emergent Schrödinger Equation for Single Neurons
- [[schrodinger-equation-single-neurons]] - Electrical noise in neuron membranes produces emergent Schrödinger equation with new neuronal constant (arXiv: 2406.16991)
  - Brownian motion in membranes → emergent quantum behavior via mathematical transformation
  - Challenges view that QM is irrelevant to macroscopic biological systems
  - Testable prediction: quantum fluctuations in subthreshold neural oscillations
  - **Activation**: emergent Schrödinger neuron, stochastic neural dynamics, quantum biology, membrane noise

### Neuromorphic Correlates of Artificial Consciousness
- [[neuromorphic-artificial-consciousness]] - NCAC framework merging neuromorphic design with brain simulations for artificial consciousness (arXiv: 2405.02370)
  - Extends NCC concept to artificial systems: neuromorphic architecture → consciousness correlates
  - Design principles: event-driven, recurrent feedback, multi-scale integration, embodied interaction
  - ML pipeline: self-supervised world models, RL for agency, attention for global workspace
  - **Activation**: artificial consciousness, neuromorphic correlates, NCAC, NCC, integrated information AI
## 2026-06-01 - Neuroscience Research (Cron Job - Latest)

### MindVoice: Reconstructing Intelligible Speech from Neural Signals
- [[mindvoice-neural-speech-reconstruction]] - First intelligible speech reconstruction from non-invasive EEG/MEG using pretrained priors with disentangled semantic-acoustic pathways (arXiv: 2605.31173)
  - Disentangled dual-pathway: semantic content decoder + acoustic attribute estimator
  - Pretrained priors bridge gap between noisy neural signals and natural speech
  - In-context voice cloning for personalized reconstruction
  - Outperforms all existing methods on intelligibility metrics (WER, MOS)
  - Non-invasive, safe, scalable speech BCI for locked-in patients
  - **Activation**: speech reconstruction, neural decoding, EEG MEG, speech BCI, pretrained priors, voice cloning, auditory neuroscience, semantic decoding, acoustic reconstruction

## 2026-06-01 - Neuroscience + Quantum Computing (Cron Job - Neuroscience Day)

### Research progress on quantum neural networks and quantum machine learning
- [[qnn-survey-design-patterns]] - Comprehensive QNN architecture selection guide with design patterns for FC-QNN, QCNN, equivariant QNN, QHN, QBM, QRC, and composite networks (arXiv: 2605.30724)
  - Architecture selection matrix by task type and resource constraints
  - 4 key design patterns: PQC encoding, quantum convolution+pooling, reservoir computing, hybrid classical-quantum
  - Barren plateau mitigation strategies: structured ansatze, layer-by-layer training, local cost functions
  - Performance comparison across QNN types: training speed, expressivity, NISQ-friendliness, scalability
  - **Activation**: QNN survey, quantum neural network design, QNN architecture selection, quantum machine learning survey, quantum CNN, quantum reservoir computing

### Entanglement in Quantum Channel Discrimination: Sometimes Less Is More
- [[quantum-entanglement-channel-discrimination]] - Unified framework for geometric quantum information: MEWC/MEBC channel discrimination + traversable/non-traversable quantum phase transitions (arXiv: 2605.31519, 2605.31472)
  - Maximal entanglement can reduce channel discriminability; separable inputs optimal for MEWC pairs
  - Counterdiabatic driving classifies QPTs by geometric distance in ground-state manifold
  - Reusable patterns: MEWC/MEBC classification, counterdiabatic protocol construction, geometric distance estimation
  - **Activation**: entanglement channel discrimination, MEWC MEBC, non-traversable quantum phase transitions, counterdiabatic driving, geometric quantum information

## 2026-06-01 - Neuroscience (Cron Job)

### The Metastable Mind: Neural Underpinnings of Naturalistic Cognition
- [[metastable-mind-event-segmentation]] - Unified neuroscience framework synthesizing metastable neural states, extended predictive coding, visual cortex alignment degradation, and fNIRS simulation (arXiv: 2605.31473, 2605.30882, 2605.30556, 2605.30552)
  - Metastable neural states as fundamental computational units with spatio-temporal nesting
  - Extended predictive coding beyond Gaussian via exponential-family distributions
  - Supervised training destroys V1 brain alignment; predictive coding/STDP preserve it
  - High-fidelity 3D fNIRS simulation for controlled neuroimaging studies
  - **Activation**: neuroscience framework, metastable states, predictive coding, visual cortex alignment, brain alignment, event segmentation, fNIRS


> Auto-generated index of all skills in the collection.
> Sorted by date (newest first).

## 2026-06-01 - Neuroscience Research (Cron Job - Evening)

### Extended Predictive Coding: Exponential Family Framework
- [[extended-predictive-coding-exponential-family]] - Variational free-energy minimization using exponential-family distributions; breakthrough in biological plausibility for predictive coding (arXiv:2605.30882)
  - Solves Gaussian PC limitations: non-negative firing rates, heterogeneous units, nonlinear responses, local plasticity
  - Multi-layer hierarchy: Poisson (sensory) → Bernoulli (V1) → Gaussian (association) → Gamma (motor)
  - Local learning rules: Hebbian-like weight updates, adaptive precision weighting
  - Natural parameter space: inherently nonlinear while maintaining tractability
  - **Activation**: extended predictive coding, exponential family, free energy principle, variational inference, local plasticity, biological plausibility

### Evolutionary Algorithm for Reservoir Learning and Yielding (EARLY)
- [[early-reservoir-evolutionary-learning]] - Graph-based genome evolution for multi-reservoir ESN architectures; combines reservoir computing with evolutionary algorithms inspired by brain modular organization; automatically discovers task-appropriate complexity (arXiv: 2605.30372)
  - Graph-based encoding: reservoir topology + hyperparameters as genome
  - Structural adaptation: simple tasks → lightweight, complex tasks → rich modularity
  - Outperforms random search on CogScale temporal learning tasks
  - Cross-situational learning adaptation validated
  - **Activation**: reservoir computing, echo state network, ESN, evolutionary algorithm, reservoir topology, multi-reservoir, modular reservoir, temporal learning, CogScale, EARLY

## 2026-06-01 - Neuroscience + Neuromorphic Hardware (Cron Job)

### A Stochastic Quantum Neural Network Model for AI
- [[stochastic-quantum-neural-network]] - Neuro-quantum model where qubits evolve via stochastic differential equations inspired by biological neuronal processes; bridges quantum computing with computational neuroscience (arXiv: 2511.11609)
  - Qubits represent neural activation states as quantum superpositions
  - Entangled qubit pairs model synaptic connections with non-local correlations
  - Stochastic SDE evolution captures inherent noise in neural processing
  - Addresses Von Neumann architecture limitations for brain-like computation
  - **Activation**: stochastic quantum neural network, QNN, neuro-quantum modeling, quantum brain simulation, quantum neural dynamics, stochastic differential equations

### Memristor-Based Spiking Neural Network Accelerator for Bio-inspired Interception Task
- [[memristor-snn-interception-task]] - Analog memristor-based SNN accelerator with in-memory synaptic computation and analog IF neurons; achieves 12.7x lower energy and 1.26x lower delay vs digital baseline in predator-prey tracking task (arXiv: 2605.31299)
  - Eliminates multi-transistor CMOS synapse circuits
  - Asynchronous event-driven operation at 45nm node
  - MSE 0.004 matches ideal software inference
  - Energy-efficient real-time edge intelligence
  - **Activation**: memristor SNN, neuromorphic hardware, in-memory computing, analog neurons, edge intelligence, bio-inspired interception

## 2026-06-01 - Neuroscience Research (Cron Job - Latest)

### MindVoice: Reconstructing Intelligible Speech from Non-Invasive Neural Signals
- [[mindvoice-neural-speech-reconstruction]] - Neuro-to-speech framework using pretrained priors to compensate for EEG/MEG limitations, disentangling semantic-acoustic pathways, achieving first intelligible speech reconstruction from non-invasive signals (arXiv: 2605.31173)
  - Two-pathway design: semantic content + fine-grained acoustic attributes
  - Pretrained models fill information gaps in noisy neural recordings
  - In-context voice cloning for natural speech output
  - Breakthrough: intelligible vs. prior unintelligible reconstruction
  - Applications: speech BCI, locked-in patient communication, silent speech
  - **Activation**: neural speech reconstruction, EEG MEG decoding, speech BCI, voice cloning, pretrained prior, non-invasive BCI

### Learning sequence timing and control of replay speed in networks of spiking neurons
- [[stm-sequence-timing-replay]] - Extended sTM model learns precise element timing (not just order) via sequential population activation, with oscillatory background inputs providing flexible replay speed control for wake vs. sleep states (arXiv: 2605.22523)
  - Oscillatory inputs act as clock signals for speed modulation
  - Spatiotemporal patterns encode elapsed time uniquely and sparsely
  - EEG/LFP oscillations correlate with replay speed differences
  - Biological plausibility: no external timekeeper required
  - **Activation**: sequence timing, replay speed, sTM, spiking temporal memory, oscillatory control, temporal encoding

## 2026-06-01 - Neuroscience + Quantum Computing (Cron Job)

### Task-specific programming of chaos in neural circuits
- [[chaos-programming-neural-circuits]] - 混沌神经网络的任务特定编程方法，通过分岔控制实现神经形态计算 (arXiv: 2605.19465)
  - **Activation**: neuromorphic chaos, bifurcation control, edge of chaos, chaotic computing, reservoir computing

### Optical Neural Networks from Coherent Transient Dynamics in Waveguide QED
- [[optical-neural-networks-waveguide-qed]] - 基于波导QED相干瞬态动力学的光学神经网络，实现超快光子计算 (arXiv: 2605.17752)
  - **Activation**: optical neural network, waveguide QED, photonic computing, coherent transient

### Metabolic quantum limit to MEG information capacity
- [[metabolic-quantum-limit-meg]] - MEG信息容量的代谢量子极限，结合量子传感器能耗与大脑代谢功率 (arXiv: 2511.06401)
  - **Activation**: MEG limits, quantum sensors, metabolic power, SQUID, atomic magnetometer

### Efficient Clifford+T synthesis for small-angle rotations
- [[efficient-clifford-t-synthesis]] - 小角度旋转的高效Clifford+T综合方法，降低容错量子编译的T门开销 (arXiv: 2605.31544)
  - **Activation**: clifford T synthesis, quantum compilation, trotterization, T gate optimization

### Q-SpiRL: Quantum Spiking Reinforcement Learning for Adaptive Robot Navigation
- [[q-spirl-quantum-spiking-rl]] - Quantum spiking RL framework comparing 5 agent families (Q-learning, MLP, SNN, QMLP, QSNN) with quantum variational circuit integration for enhanced state representation (arXiv: Q-SpiRL)
  - Architecture: State → Quantum Feature Map → Variational Circuit → Measurement → SNN/MLP Policy → Action
  - QSNN outperforms classical SNN on complex obstacle-aware navigation tasks
  - Encoding strategies: amplitude/angle/basis; entanglement: linear/circular/all-to-all
  - Pitfalls: barren plateaus (shallow ansatz), spike saturation (threshold scaling), quantum-classical mismatch (normalization layer)
  - **Activation**: quantum spiking RL, Q-SpiRL, QSNN, QMLP, quantum-enhanced SNN, quantum robot navigation, neuromorphic quantum, quantum policy

### QLIF-CAST: Quantum Leaky-Integrate-and-Fire for Time-Series Forecasting
- [[qlif-cast-quantum-spiking-forecasting]] - 量子泄漏积分发放神经网络时间序列预测，应用于天气预报 (arXiv: qlif-cast)
  - **Activation**: quantum LIF, spiking forecasting, quantum time series, weather prediction


## 2026-06-01 - Neuroscience Research (Cron Job)

### Supervised Training Rapidly Degrades Early Visual Cortex Alignment Across Biologically Plausible Learning Rules
- [[supervised-training-degrades-visual-cortex-alignment]] - RSA tracking shows untrained CNNs match trained networks at V1; backpropagation destroys alignment while local rules (PC, STDP) preserve brain-like structure (arXiv: 2605.30556)
  - Single training epoch reduces V1 alignment 25-90%
  - BP: delta r=-0.080 (most severe), STDP/PC: delta r~-0.04
  - Untrained networks capture V1 statistics via inductive biases
  - Local learning rules preserve early visual representations
  - Hierarchical divergence: V1 degrades, LOC improves
  - **Activation**: brain alignment, visual cortex, RSA, untrained networks, learning rules, backpropagation, predictive coding, STDP

### The Metastable Mind: Neural Underpinnings of Naturalistic Cognition Through the Synthesis of Event Segmentation and Metastable Neural States
- [[metastable-mind-neural-states]] - Comprehensive review synthesizing event segmentation (ES) and metastable neural activity (MNA) - same phenomenon from cognitive and mechanistic perspectives (arXiv: 2605.31473)
  - ES states = MNA states (same neural phenomenon)
  - Three core principles: nested hierarchy, predictive models, modular processing
  - Spatio-temporal hierarchy: fast sensory → slow cognitive states
  - Boundaries: prediction error triggers state transitions
  - Modular processing with boundary reconfiguration
  - **Activation**: metastable states, event segmentation, neural dynamics, naturalistic cognition, brain states, predictive models

## 2026-06-01 - Neuroscience + Quantum Mechanics (Cron Job - Hourly Round 4)

### A Stochastic Quantum Neural Network Model for Ai
- [[stochastic-quantum-neural-network]] - Mathematical formalization of QNNS where qubits evolve via stochastic differential equations inspired by biological neuronal processes, bridging quantum computing and computational neuroscience (arXiv: 2511.11609)
  - Qubits represent neural activation states in superposition
  - Entanglement models synaptic connectivity
  - Stochastic SDEs capture biological neural noise
  - **Activation**: quantum neural network, stochastic differential equations, neuro-quantum, QNN, computational neuroscience, brain modeling

### BehaviorVLM: Unified Finetuning-Free Behavioral Understanding
- [[behaviorvlm-neuroscience-vlm]] - Vision-language framework for pose estimation and behavioral understanding requiring no task-specific finetuning, leveraging quantum-dot-grounded behavioral data (arXiv: 2603.12176)
  - Multi-stage pipeline: temporal, spatial, cross-view reasoning
  - Deep embedded clustering for over-segmented behavior discovery
  - VLM-based video captioning + LLM reasoning for behavior labeling
  - **Activation**: behavioral understanding, pose estimation, VLM, quantum-dot data, animal behavior

---## 2026-06-01 - Neuroscience Research (Cron Job Round 3)

### The Metastable Mind: Neural Underpinnings of Naturalistic Cognition
- [[metastable-mind-neural-states]] - Unified framework synthesizing Event Segmentation (ES) and Metastable Neural Activity (MNA), revealing neural states as fundamental computational units of naturalistic cognition with predictive model foundations (arXiv: 2605.31473)
  - Spatio-temporal nested hierarchy: slower higher-order states constrain faster lower states
  - Neural states reflect underlying predictive models shaping perception, decision, memory
  - Modular processing periods interspersed by connectivity reconfiguration boundaries
  - **Activation**: metastable, event segmentation, neural states, predictive model, brain hierarchy, MNA, ES

---

## 2026-06-01 - Neuroscience Research Update (Cron Job Round 2)

### Extended Predictive Coding Framework (Revised Skill)
- [[extended-predictive-coding-free-energy-exponential-family]] - Exponential-family distributions extend predictive coding beyond Gaussian assumptions, enabling biological realism: nonlinearity, heterogeneous neurons, positive firing rates via local plasticity (arXiv: 2605.30882)
  - Key: variance depends on mean in EFD → automatic nonlinearity
  - FEP-PC correspondence maintained up to second cumulant
  - **Activation**: predictive coding, exponential family, local plasticity, biological plausibility

### Supervised Training vs Visual Cortex Alignment
- [[supervised-training-degrades-visual-cortex-alignment]] - RSA tracking shows 25-90% V1 alignment drop after one epoch; backpropagation most destructive (-0.080), predictive coding and STDP preserve better (-0.04) (arXiv: 2605.30556)
  - Untrained networks: inductive biases encode brain-like structure
  - Local learning (PC, STDP) maintains natural statistics better than global BP
  - **Activation**: brain alignment, RSA, learning rules comparison, untrained networks

---

## 2026-06-01 - Neuroscience (Cron Job)

### The Metastable Mind: Neural Underpinnings of Naturalistic Cognition Through the Synthesis of Event Segmentation and Metastable Neural States
- [[metastable-neural-states-event-segmentation]] - Synthesizes event segmentation theory with metastable neural activity, revealing spatio-temporally nested hierarchies of neural states as computational units of cognition (arXiv: 2605.31473)
  - Metastable neural states are fundamental computational units, not artifacts
  - Spatio-temporally nested hierarchy: slower higher-order states constrain/shape faster lower-level states
  - **Activation**: metastable neural states, event segmentation, neural state hierarchy, predictive processing

### Extended predictive coding framework as variational free-energy minimisation under exponential-family assumption
- [[exponential-family-predictive-coding]] - Extends predictive coding beyond Gaussian assumptions to exponential family distributions, capturing biological neural network properties like nonlinearity and heterogeneity (arXiv: 2605.30882)
  - EFD extension maintains FEP-PC correspondence up to second cumulant
  - Reveals biologically plausible local plasticity rules without global error signals
  - **Activation**: exponential family, predictive coding, free energy principle, local plasticity, variational inference

### Supervised Training Rapidly Degrades Early Visual Cortex Alignment Across Biologically Plausible Learning Rules
- [[brain-alignment-learning-rules-comparison]] - Comparative study showing single training epoch reduces V1 alignment by 25-90%; BP most destructive, PC and STDP preserve brain-like structure (arXiv: 2605.30556)
  - Untrained networks capture low-level visual statistics through inductive biases alone
  - Local learning rules (PC, STDP) preserve brain-like structure better than global BP
  - **Activation**: brain alignment, learning rules comparison, representational similarity analysis, biologically plausible learning

### The Spiking Tolman-Eichenbaum Machine: Emergent Spatial and Temporal Coding through Spiking Network Dynamics
- [[spiking-tolman-eichenbaum-machine]] - Biologically realistic SNN implementation of TEM framework for spatial navigation and memory, combining grid-place cell dynamics with STDP learning (crossref: 2025.10.16.682754)
  - Grid cells emerge from continuous attractor dynamics on 2D toroidal manifold
  - Place cells learn through STDP from grid cell patterns + sensory inputs
  - Natural temporal coding via spike latency, phase precession, and sequence replay
  - **Activation**: spiking tolman-eichenbaum, sTEM model, spiking spatial navigation, grid place cell spiking, hippocampal entorhinal spiking

### Equilibrium Propagation with Predictive Learning in Leaky Integrate-and-Fire Spiking Neural Networks
- [[equilibrium-propagation-lif-snn]] - EP extended to LIF spiking neurons: backprop-free training using free/nudged phase energy comparison with predictive learning for temporal dependencies (crossref: 2026.05.19.726261)
  - Two-phase learning: free equilibrium vs nudged (target-perturbed) equilibrium
  - Local plasticity rules from pre/post spike correlations — no BPTT needed
  - Predictive variant learns temporal dependencies without storing full trajectories
  - **Activation**: equilibrium propagation SNN, EP leaky integrate-and-fire, biologically plausible SNN training, EP without BPTT

### Daily Quantum Mechanics Papers (2026-06-01)
- 61 new quant-ph papers submitted today covering Clifford+T synthesis, quantum cryptography, entanglement in channel discrimination, quantum advantage in communication complexity, quantum networks, and quantum phase transitions
- 48 new cs.NE papers including SNN accelerators, photonic reservoir computing, evolutionary algorithms, and zero-shot quantum neural architecture search
- 38 new q-bio.NC papers including metastable neural states, extended predictive coding, and fNIRS simulation
## 2026-06-01 - Neuroscience (Cron Job)

### High-Fidelity 3D Simulator for Synthetic fNIRS Data Generation
- [[fnirs-3d-monte-carlo-simulator]] - 3D fNIRS simulator using mesh-based Monte Carlo for synthetic neuroimaging data generation (arXiv: 2605.30552)
    - Mesh-based Monte Carlo simulates photon transport in 3D head tissue
    - Combines hemodynamic response + systemic physiology + artifact models
    - Enables unlimited labeled datasets for ML pipeline validation
    - **Activation**: fNIRS simulator, synthetic fnirs data, Monte Carlo light transport, hemodynamic response simulation

## 2026-06-01 - Neuroscience (Cron Job)

### Extended predictive coding framework as variational free-energy minimisation under exponential-family assumption
- [[predictive-coding-exponential-family-plasticity]] - Predictive coding with exponential-family distributions and biologically plausible local plasticity rules (arXiv: 2605.30882)
    - EFD assumption captures neural heterogeneity and non-negative firing rates
    - FEP-PC correspondence maintained up to second cumulant
    - Derives local plasticity rules without global backpropagation
    - **Activation**: exponential family predictive coding, local plasticity rules, free energy principle beyond gaussian

## 2026-06-01 - Neuroscience (Cron Job)

### Extended Predictive Coding Beyond Gaussian Assumption
- [[predictive-coding-exponential-family]] - 通用指数族预测编码框架，扩展高斯假设到任意分布 (arXiv: 2605.30882)
  - 核心要点 1: 将预测编码从单一高斯假设推广到任意指数族分布
  - 核心要点 2: 推导泊松(脉冲计数)、伽马(反应时)、狄利克雷(比例编码)的预测误差公式
  - **Activation**: predictive-coding, exponential-family, non-gaussian, bayesian-inference

## 2026-06-01 - Neuroscience + AI (Cron Job)

### EvoGM: Learning to Merge LLMs via Evolutionary Generative Optimization
- [[evo-generative-llm-merging]] - 进化式LLM模型合并优化方法 (arXiv: 2605.29295)
  - 核心要点 1: 将LLM模型合并建模为进化优化问题，替代固定启发式线性插值
  - 核心要点 2: 分层粒度合并策略：浅层任务特异性权重、深层共享表示、输出层最优微调
  - **Activation**: evolutionary-optimization, llm-merging, model-composition, generative-ai

## 2026-06-01 - Neuroscience + Security (Cron Job)

### Privacy-Enhanced Zero-Order Federated Learning via xMK-CKKS over Wireless Channels
- [[zeroth-order-federated-learning-he]] - 结合零阶优化与同态加密的隐私保护联邦学习 (arXiv: 2605.30123)
  - 核心要点 1: 零阶优化避免梯度泄漏，仅传输函数评估值而非梯度
  - 核心要点 2: xMK-CKKS多密钥同态加密方案支持无线信道上的安全聚合
  - **Activation**: federated-learning, zeroth-order, homomorphic-encryption, ckks, privacy

