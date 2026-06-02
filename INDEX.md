## 2026-06-02 - Neuroscience Research (Cron Job)

### Mapping Whisper Representations to Human ECoG Responses
- [[whisper-ecog-alignment]] - Speech foundation model Whisper intermediate layers align strongest with human cortical activity using interpretable time-resolved neural encoding (arXiv: 2606.02305)
  - Intermediate Whisper layers provide strongest brain-model correspondence (hierarchical alignment)
  - Time-resolved encoder with soft attention outperforms linear mappings for ECoG
  - Phoneme interpretability shows anatomically coherent organization among encoding-informative electrodes
  - **Activation**: whisper-ecog-alignment, speech encoding, brain alignment, temporal encoder, speech foundation model, phoneme organization, cortical speech, soft attention

### How Optimality Structures Sparse Dictionaries
- [[sae-optimality-structures-dictionaries]] - Mathematical theory explains why Sparse Autoencoders extract interpretable features — layer-wise splitting/absorption, residual structure, dense opposing features emerge from optimal solutions (arXiv: 2606.02385)
  - Demonstrates hierarchical feature organization follows from sparsity constraint optimality
  - Absorbed features become densified opposing representations
  - **Activation**: SAE optimality, sparse dictionary learning, interpretable features, layer-wise splitting, feature absorption

### The Neuromorphic Supremacy
- [[neuromorphic-supremacy-hybrid-astrocytic-spiking]] - Hybrid neural architectures combining astrocytic modulation and spiking dynamics achieve few-shot learning and noise robustness that surpass standard deep learning (arXiv: 2606.01841)
  - Introduces "neuromorphic supremacy" regime where bio-inspired circuits outperform ANNs in data-scarce noisy environments
  - Astrocytic gain control + sparse spiking encoding prevent performance collapse under >50% occlusion/impulse noise
  - **Activation**: neuromorphic supremacy, astrocyte, spiking neural network, few-shot learning, noise robustness, embodied AI, hybrid architecture

## 2026-06-02 - Computer Science + Quantum Computing (Cron Job - Hourly)

### Evolutionary Discovery of Bivariate Bicycle Codes with LLM-Guided Search
- [[llm-guided-quantum-code-discovery]] - LLM-guided evolutionary workflow discovers 465 distinct quantum LDPC codes including new indecomposable [[288,16,12]] code (arXiv: 2606.02418)
  - LLM mutates Python programs generating BB and perturbed BB code ansätze across ~1650 evolutionary iterations
  - Staged validation pipeline: GF(2) rank, distance estimation, MILP, BLISS Tanner-graph dedup, local-Clifford equivalence
  - **Activation**: quantum code discovery, LLM-guided search, bivariate bicycle codes, quantum LDPC, evolutionary code search

### Branch-Aware Quantum Constant Propagation for Dynamic Quantum Circuits
- [[branch-aware-quantum-constant-propagation]] - Compile-time optimization for dynamic quantum circuits with mid-circuit measurements and classical feedforward, accepted at IEEE QSW 2026 (arXiv: 2606.02018)
  - Extends QCP by tracking classical measurement outcomes with post-measurement quantum states across execution branches
  - Path-sensitive reasoning inside conditional blocks with bounded state representation for scalability
  - **Activation**: quantum compiler optimization, dynamic quantum circuits, mid-circuit measurement, classical feedforward, branch-aware analysis

## 2026-06-02 - Computer Science + Quantum Computing (Cron Job)

### Tianyan: Cloud Services with Quantum Advantage
- [[tianyan-quantum-cloud-services]] - Cloud-accessible superconducting quantum processor (105 qubits) demonstrating quantum advantage: 74-qubit RCS in 18.4min vs 16,000 years classical (arXiv: 2512.10504)
  - Tianyan-287: 105 qubits, 99.90% single-qubit, 99.56% two-qubit, 98.7% readout fidelity
  - Cqlib open-source SDK for extended quantum circuits, operators, and primitives
  - **Activation**: quantum cloud, quantum advantage, tianyan, RCS benchmark, Cqlib, superconducting quantum processor, random circuit sampling

### EFaaS: Quantum-Classical Serverless Entangled Scheduler
- [[efaas-quantum-serverless]] - Serverless middleware for hybrid variational algorithms reducing TTNS by 11.4%-94.3% and convergence time by 83.2%-98.3% (arXiv: 2605.27540)
  - Calibration-aware placement routes circuits to QPUs with warm calibration caches
  - Dual-resource fair queuing and EF-QuantumFuture speculative execution primitive
  - **Activation**: quantum serverless, EFaaS, VQA scheduling, TTNS optimization, hybrid quantum workflow, calibration-aware routing

### SQARL: Size-Agnostic RL for Distributed Quantum Circuit Allocation
- [[sqarl-distributed-quantum]] - Transformer-based RL for qubit allocation across distributed quantum cores, 33% cost reduction vs HQA without retraining (arXiv: 2605.27027)
  - Handles arbitrary qubit/core counts with single trained policy
  - Minimizes inter-core communication (SWAP overhead) in multi-core quantum architectures
  - **Activation**: distributed quantum, qubit allocation, circuit compilation, SQARL, multi-core quantum, SWAP optimization

### Support Vector Machine with a Scalable Quantum Kernel
- [[hamming-quantum-kernel-svm]] - Hamming quantum kernel avoids exponential concentration in quantum SVMs, scales to 27 qubits (arXiv: 2605.31449)
  - Uses full measurement statistics instead of single fidelity value
  - Zero additional quantum cost — purely classical post-processing improvement
  - **Activation**: hamming quantum kernel, quantum SVM, exponential concentration, scalable quantum kernel

### Quantum State Preparation via Neural Network Encoding
- [[nn-quantum-state-encoding]] - Classical NN maps data to quantum circuit parameters, 0.992 fidelity, 5000x speedup (arXiv: 2605.31006)
  - Train-once-infer-many pattern replaces per-instance variational optimization
  - Fixed ansatz with NN-predicted rotation angles
  - **Activation**: neural network quantum state preparation, QML data loading, quantum circuit encoding

### Generative Quantum Data Embeddings for Supervised Learning
- [[generative-quantum-embedding]] - Energy-based generative framework optimizes quantum data embeddings with Wasserstein bounds (arXiv: 2605.30866)
  - Synthesizes gate sequences via fidelity-based surrogate objective
  - Wasserstein distance provides a priori diagnostic for embedding optimization feasibility
  - **Activation**: quantum data embedding, quantum encoding optimization, generative quantum circuit

### Attention-based Optimizer for Symmetry Finding
- [[attention-quantum-symmetry]] - Set-Transformer searches Pauli symmetries of Hamiltonians with commutation-based objectives (arXiv: 2605.30429)
  - Self-attention encodes pairwise and higher-order correlations among Pauli strings
  - Near-deterministic success on physical Hamiltonians (Ising, Toric code)
  - **Activation**: attention symmetry finding, quantum symmetry optimizer, Set-Transformer Hamiltonian

### Software Framework for Pulse-Level Quantum Computing
- [[quantum-control-pulse-software]] - Bridges gate-based abstractions with hardware-aware pulse-level optimization via JAX-based QML framework (arXiv: 2605.21286)
  - Composable ansatz constructions combining gate-based and pulse-level representations
  - Fourier-analytic diagnostics for circuit expressivity and entanglement measures
  - **Activation**: quantum pulse level control, quantum optimal control software, QML pulse modelling, hardware-aware quantum optimisation

### Progressive Swapping to the Middle Protocol
- [[psm-quantum-memory-distribution]] - Entanglement distribution optimized for imperfect quantum memories, presented at EuCNC 2026 (arXiv: 2605.31493)
  - Swaps progressively from both ends toward center, minimizing idle memory time
  - ~2x fidelity advantage over naive sequential swapping for linear chains
  - **Activation**: progressive swapping quantum, PSM protocol, imperfect quantum memory, entanglement distribution

### Quantum Sequence Samplers for Stochastic Processes
- [[quantum-sequence-samplers]] - Quantum circuits generate coherent superpositions of stochastic processes for O(1/ε) Monte Carlo (arXiv: 2603.24069)
  - Quantum amplitude estimation gives quadratic speedup over classical sampling
  - Applications in financial risk analysis, DNA sequencing, physics simulation
  - **Activation**: quantum sequence sampler, stochastic process quantum encoding, quantum Monte Carlo


### The Metastable Mind: Neural Underpinnings of Naturalistic Cognition
- [[metastable-mind-event-segmentation]] - 综合Event Segmentation与Metastable Neural Activity两大孤立分支，证明二者研究同一神经状态现象，提出三大核心原理：时空嵌套层级、预测模型基础、模块化处理边界重构 (arXiv: 2605.31473)
  - ES理论提供认知/行为效用解释，MNA提供机制层面实现
  - 神经状态作为认知基本计算单元，状态边界触发连接重构
  - 高阶区域长时程状态约束并塑造低阶快速区域状态
  - **Activation**: metastable, event segmentation, neural states, cognitive segmentation, metastable neural activity, 亚稳态神经状态, 事件分割

### Extended Predictive Coding under Exponential-Family Assumption
- [[extended-predictive-coding-exponential-family]] - 扩展预测编码框架至指数族分布，捕获生物神经网络特性：非线性、异质性、正发放率，维持FEP-PC对应至后验二阶累积量，支持生物合理局部可塑性规则 (arXiv: 2605.30882)
  - 传统Gaussian假设导致负发放率、线性转移函数等不生物合理性质
  - 指数族(Bernoulli/Poisson/Exponential/Gamma)自然约束正域，匹配生理观测
  - 层级微电路实现：L4计算预测误差，L2/3生成预测(EDF参数)，L5/6反馈
  - **Activation**: predictive coding, exponential family, free-energy principle, variational inference, local plasticity, 预测编码, 自由能原理

## 2026-06-02 - Computer Science + Quantum Computing (Cron Job)

### Quantum Algorithm for Distributed Reduction of Entanglements (QADR)
- [[qadr-distributed-entanglement-reduction]] - QADR框架将全局VQC分解为因果光锥内的局部子电路，将经典模拟内存从O(2^n)降至O(2^d)，自然缓解 barren plateaus，在32+量子比特处全球VQC崩溃时仍可运行 (arXiv: 2606.01291)
  - 因果光锥分解：分析电路结构识别每个目标量子比特的影响范围
  - 局部代价函数避免指数级梯度衰减
  - 在MNIST和NASA IMS风轮机诊断任务中匹配或超越经典架构
  - **Activation**: qadr, distributed entanglement reduction, causal light cone, VQC decomposition, barren plateau mitigation, quantum machine learning, variational quantum circuit, simulation efficiency

### Quantum Tunneling-Aware Machine Learning (QTAML)
- [[qtaml-quantum-tunneling-ml]] - 基于WKB近似的量子隧穿感知ML，推导部署时权重误差分布，TAC算法以少3.4-33.6倍ECC开销达到95%清洁准确率 (arXiv: 2606.00741)
  - WKB推导三层结构：仿射均值漂移、逐比特方差层级、逐层依赖性
  - 闭式饱和比ρ*可提前预测补偿效果
  - 层自适应比特预算分配在小预算下优于幅度分配24个百分点
  - 无需重训练、无需标签、无推理时开销
  - **Activation**: quantum tunneling, WKB approximation, noise modeling, deployment robustness, hardware-aware ML, error correction, tunneling-aware compensation, TAC, QTAML

## 2026-06-02 - Neuroscience Research (Cron Job)

### Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons
- [[snn-sequence-timing-replay-v2]] - 扩展sTM模型以学习序列元素精确时序，通过振荡背景输入灵活控制重放速度，支持宽范围时间尺度编码和清醒/睡眠状态速度调节 (arXiv: 2605.22523)
  - 元素特定神经元群体的顺序激活编码持续时间
  - 振荡背景输入作为时钟信号，频率调制重放速度
  - 稀疏时空模式编码经过时间，EEG/LFP振荡特性与重放速度相关性
  - **Activation**: sequence timing, replay speed, spiking temporal memory, oscillatory control, element-specific timing, EEG/LFP oscillation, sTM model, memory consolidation

### NeuralSet: A High-Performing Python Package for Neuro-AI
- [[neuralset-neuro-ai-framework]] - 统一Python框架处理多样化神经记录（fMRI, M/EEG, spikes）和复杂刺激（文本、音频、视频），惰性加载+深度嵌入集成+计算追溯 (arXiv: 2605.03169)
  - 模态无关数据统一，单一PyTorch-ready接口
  - 惰性加载支持TB级数据集，内存占用降至样本级别
  - 预训练深度嵌入（BERT/wav2vec/CLIP）自动生成
  - 计算可追溯性保证重现性
  - **Activation**: neuro-ai, neural data preprocessing, fMRI EEG MEG harmonization, deep learning embeddings, lazy loading, memory-efficient, PyTorch-ready, computational provenance

## 2026-06-02 - Computer Science Research (Cron Job)

### Quantum Reservoir Computing and Risk Bounds
- [[quantum-reservoir-computing-risk-bounds]] - Rademacher complexity-based generalization error bounds for quantum reservoir computing, with explicit qubit-scaling analysis and polynomial readout function risk convergence (arXiv: 2501.08640)
  - Rademacher complexity bounds for multiple quantum reservoir classes
  - Generalization bounds scale exponentially with number of qubits n — key limitation for large-scale QRC
  - Polynomial readout functions: risk bounds converge in number of training samples
  - Explicit parameter dependence enables partial generalization error control
  - **Activation**: quantum reservoir computing, Rademacher complexity, generalization bounds, risk bounds, qubit scaling, QRC theory, polynomial readout

## 2026-06-02 - Quantum Computing Research (Cron Job)

### More Efficient Clifford+T Synthesis for Small-Angle Rotations and Application to Trotterization
- [[efficient-clifford-t-synthesis]] - 突破性方法将小角度旋转的 T gate 成本从 O(log 1/δ) 降至 Õ(θ²/δ)，Trotterization 小步长极限下门成本变为常数，颠覆了"Clifford+T 成本独立于角度θ"的普遍误解 (arXiv: 2605.31544)
  - 准概率方法进一步将总 T 成本降低数个数量级，仅需小样本复杂度开销
  - 新 θ-依赖公式用于容错量子算法资源估计，Trotterization 应用需重新审视成本
  - 降低魔态资源需求，推进早期容错量子计算实用性
  - **Activation**: Clifford+T synthesis, small-angle rotation, fault-tolerant quantum compilation, Trotterization, T gate optimization, magic state distillation, quasi-probability decomposition

## 2026-06-02 - Neuroscience Research (Cron Job)

### XOResNet: Exclusive-OR Meta-Residuals for Deep Spiking Neural Networks
- [[xoresnet-deep-snn-learning]] - Novel SNN residual architecture using OR-ADD shortcuts and XOR meta-residuals to address spike redundancy, information loss, and redundant learning; outperforms SOTA on CIFAR-10/100 (arXiv: 2605.30362)
  - OR-ADD shortcut merges identity+residual branches (OR for spikes, ADD for currents)
  - XOR meta-residuals select novel residual components, eliminating redundant learning
  - Works at 18-101 layers, +2-5% accuracy improvement over baseline deep SNNs
  - **Activation**: xoresnet, xor meta-residual, deep snn, snn residual, spike redundancy, neuromorphic architecture, or-add shortcut

### Reinterpreting Safety Thresholds as Neuron Spiking Thresholds for Automated Driving
- [[snn-safety-thresholds-automated-driving]] - 将 Surrogate Safety Measures (SSMs) 重新诠释为 LIF 神经元脉冲阈值，SNN 结合多个 SSM 输入使脉冲与人类制动时机对齐 (arXiv: 2605.30368)
  - 用 LIF 神经元替代固定阈值，捕获持续边缘条件和短暂高峰风险
  - 学习的阈值相对一致（客观 SSM 有效），衰减因子编码个体时间敏感度（主观感知）
  - **Activation**: safety thresholds, SNN driving, LIF safety, autonomous driving safety, surrogate safety measures, SSM, braking prediction, spiking thresholds

## 2026-06-02 - Systems Engineering Research (Cron Job)

### Kairos: Lightweight Testing Framework for Timing-Induced Interaction Failures in LTE/5G Core Networks
- [[kairos-cps-timing-testing]] - CPS/分布式系统时序诱导交互故障轻量级测试框架，无需解析标准文档即可发现20个新漏洞、复现34个已知问题 (arXiv: 2605.30985)
  - 控制平面交互模式分类体系与故障模式映射
  - 轻量级时序测试生成与自动化故障检测
  - **Activation**: timing-induced failures, CPS testing, 5G core networks, LTE testing, control-plane interactions, network function crash

### A Data-Driven Methodology for Scalable Distributed MPC in Heterogeneous Building Aggregation
- [[data-driven-distributed-mpc-buildings]] - MPC-aware特征选择+分布式凸优化框架，解决大规模异构建筑需求响应协调的计算可扩展性和多步预测误差累积问题 (arXiv: 2605.30763)
  - MPC-aware特征选择方法论（考虑多步预测误差累积）
  - 异构建筑聚类的分布式凸优化控制框架
  - **Activation**: distributed MPC, building aggregation, demand response, feature selection, convex optimization, data-driven control

## 2026-06-02 - Computer Science + Quantum Mechanics (Cron Job)

### Mitigating Noise-Induced Barren Plateaus Using a Non-Unitary Ansatz
- [[non-unitary-ansatz-barren-plateau]] - Non-unitary variational ansatz restores finite gradients under depolarizing noise, enabling VQA scalability on NISQ hardware (arXiv: 2605.30572)
  - Core: Dissipative nonunitary elements counteract hardware noise effects in VQAs
  - Core: Floquet-type parameter sharing reduces deep circuit to analyzable quantum channel
  - **Activation**: barren plateau, NIBP, non-unitary ansatz, VQA, Floquet variational, NISQ

### A Denser Planar Surface Code
- [[denser-planar-surface-code]] - 4.5x encoding rate improvement over rotated surface codes using hex grid twist defects and padding-free lattice surgery (arXiv: 2605.30455)
  - Core: Dense twist defect packing on 2D hex grid with optimal 4-layer stabilizer cycles
  - Core: Pareto frontier analysis: 36x space, 6.6x spacetime improvement, 89k qubits for FeMoco
  - **Activation**: surface code, QEC, hex grid, twist defect, lattice surgery, fault tolerance

### Hybrid Quantum-Classical FBPINN for Full Waveform Inversion
- [[hybrid-quantum-fbpinn]] - Hybrid quantum-classical FBPINN achieves 8x faster convergence with 33% fewer parameters for wave-based inverse problems (arXiv: 2606.01110)
  - PQC as differentiable JAX statevector simulator enables end-to-end autodiff through classical PINN → quantum circuit → physics loss
  - Outperforms all 15 classical hyperparameter variants on geophysical anomaly benchmark
  - Applicable to medical ultrasound tomography, non-destructive evaluation, and wave-based inverse problems
  - **Activation**: hybrid quantum-classical neural networks, physics-informed neural networks, full waveform inversion, quantum machine learning for PDEs, differentiable quantum circuits, JAX quantum simulation, wave-based inverse problems, domain-decomposed PINNs, FBPINN quantum



### The Metastable Mind: Neural States as Computational Units (Enhanced Skill)
- [[metastable-mind-neural-states]] - Metastable neural states作为认知基本计算单元，整合事件分割理论与神经亚稳态框架，揭示三大核心原理：时空嵌套层级、预测模型基础、模块化处理边界重构 (arXiv: 2605.31473v1, May 29 2026)
  - 认知心理学分支(ES)与计算神经科学分支(MNA)研究同一现象
  - 高阶区域长时程状态约束并塑造低阶快速区域状态
  - 状态边界标志着连接重构和计算模式切换
  - **Activation**: metastable neural states, event segmentation, brain state transitions, neural state hierarchy, cognitive boundaries, metastable mind, predictive neural states, MNA, ES

### Memristor-Based SNN Accelerator (Enhanced Skill)
- [[memristor-snn-interception-task]] - Analog memristor crossbar阵列+模拟IF神经元实现异步事件驱动SNN，predator-prey拦截任务MSE 0.004，45nm工艺能耗比5nm数字方案降低12.7倍、延迟降低1.26倍 (arXiv: 2605.31299v1, May 29 2026, DCAS 2026)
  - In-memory synaptic computation消除多晶体管CMOS突触电路
  - Analog integrate-and-fire neurons实现阈值检测和脉冲生成
  - HSPICE仿真验证边缘智能实时追踪潜力