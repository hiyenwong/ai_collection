## 2026-05-27 - Neuroscience Research (Cron Job)

### SpikeReg: Energy-Efficient 3D Deformable Medical Image Registration with Spiking Neural Networks
- [[spikereg-snn-medical-registration]] - First SNN-based 3D deformable brain MRI registration matching ANN accuracy at 12.8% spike rate and 55.5× energy reduction (arXiv: 2605.25144)
  - ANN-to-SNN conversion via layer-wise weight transfer + activation-percentile threshold calibration
  - Surrogate gradient fine-tuning with local cross-correlation + diffusion regularization + spike-rate sparsity
  - Negative findings: displacement distillation hurts, Dice-loss ANN teachers fail to transfer
  - **Activation**: SNN medical imaging, neuromorphic registration, energy-efficient 3D perception, ANN-to-SNN conversion

### Neuromorphic LiDAR-based Bird's Eye View Object Detection using Energy-efficient Spiking Neural Networks
- [[neuromorphic-lidar-bev-snn]] - End-to-end SNN encoder-decoder for 3D LiDAR BEV object detection with 3.33× synaptic energy reduction over CNN, 92.05/87.04/86.51 AP on KITTI (arXiv: 2605.25293)
  - Learned spike encoding outperforms hand-crafted Poisson/latency/z-axis encoding strategies
  - Two variants: membrane potential (max accuracy) and fully binary (neuromorphic hardware deployment)
  - Block-wise energy analysis via SynOps/MAC proxy model
  - **Activation**: neuromorphic autonomous driving, SNN object detection, LiDAR perception, spike encoding

## 2026-05-27 - Medicine + Quantum (Cron Job - Wednesday 13:00)

### HQNN Expressibility-Trainability Trade-off
- [[hqnn-expressibility-trainability]] - Multi-objective NAS framework for HQNNs revealing classical components decouple trainability from PQC expressibility under full end-to-end training (arXiv: 2605.25768)
  - Full end-to-end hybrid training can completely eliminate the expressibility-trainability trade-off
  - Multi-objective NAS jointly optimizes expressibility, trainability, and task performance over combined classical-quantum design space
  - Pure PQCs show only weak trade-off; hybrid architectures increasingly disrupt it
  - **Activation**: HQNN expressibility trainability, hybrid quantum neural network optimization, quantum circuit barren plateau, neural architecture search quantum, PQC expressibility, quantum classical hybrid training

## 2026-05-27 - Neuroscience Research (Cron Job)

### Random Neural Networks Match Neural Population Dimensionality
- [[random-neural-network-dimensionality]] - DMFT framework shows random connectivity explains low-dimensionality of large-scale neural recordings when finite measurement time and behavioral context variability are included (arXiv: 2605.26551)
  - Non-monotonic dependence: dimensionality varies non-monotonically with external input strength
  - Manifold orientation similarity across behavioral contexts is more sensitive to connectivity structure than dimensionality alone
  - **Activation**: random neural network, neural population dimensionality, dynamical mean field theory, neural manifold, brain recording, connectivity inference, collective dynamics

### Multi-Objective NSGA-III Optimisation of SNN Oscillatory Dynamics
- [[multi-objective-snn-oscillation]] - NSGA-III co-optimises Izhikevich RSNN connectivity for both firing rates AND oscillation frequencies in spontaneous activity, brain organoids, and decision-making dynamics (arXiv: 2605.25224)
  - Oscillation frequencies are more parameter-sensitive than firing rates — harder to pin precisely
  - Successfully validated on brain organoid recordings and simulated decision-making RSNNs
  - **Activation**: spiking neural network oscillation, NSGA-III, RSNN optimisation, Izhikevich neuron, brain organoid, neural oscillation fitting, multi-objective SNN

## 2026-05-27 - Medicine + Quantum ML (Cron Job)

### Quantum ML Medical Diagnosis Consolidated Skill
- [[quantum-ml-medical-diagnosis]] - Comprehensive quantum ML methodologies for medical diagnosis and healthcare
  - Core pattern 1: Hybrid quantum-classical feature fusion with temperature-scaled balancing (TSHF)
  - Core pattern 2: Tensor-network compression enabling small-qubit quantum processing
  - Core pattern 3: Privacy-aware federated quantum learning with MPC-secured aggregation
  - Core pattern 4: Quantum transfer learning with fair benchmarking under NISQ constraints
  - Core pattern 5: Quanvolutional neural networks for disease detection
  - **Activation**: quantum medical diagnosis, quantum healthcare, federated quantum, quantum transfer learning, quantum neural network, medical imaging quantum, quanvolutional, HQNN

## 2026-05-27 - Medicine + Quantum (Cron Job)

### Design Space Exploration of Hybrid Quantum Neural Networks for Chronic Kidney Disease
- [[hqnn-design-space-exploration]] - Systematic benchmarking of 625 HQNN configurations for CKD diagnosis, IQP+Ring entanglement achieves best accuracy-efficiency trade-off (arXiv: 2604.13608)
  - Core finding: high performance does NOT require large parameter counts or complex circuits
  - IQP encoding + Ring entanglement is optimal combo — captures pairwise correlations efficiently with minimal depth
  - **Activation**: HQNN design space, quantum neural network architecture, hybrid quantum medical diagnosis, quantum encoding schemes, CKD classification, quantum circuit benchmarking

### Analyzing Blood Cells with QML: Equilibrium Propagation and VQCs for Acute Myeloid Leukemia Detection
- [[qml-equilibrium-propagation-medical]] - Energy-based backprop-free quantum training for blood cell classification, competitive under NISQ constraints (arXiv: 1808)
  - Equilibrium Propagation computes gradients via energy differences, avoiding backpropagation
  - VQC with EP achieves competitive AML detection accuracy on limited-qubit hardware
  - **Activation**: equilibrium propagation, blood cells, leukemia detection, VQC, backprop-free, energy-based, NISQ

### Lightweight Quantum-Enhanced ResNet for Coronary Angiography Classification
- [[quantum-enhanced-coronary-classification]] - Hybrid CNN-VQC architecture for CAG image classification with minimal qubits (arXiv: 1809)
  - Classical ResNet handles feature extraction, quantum circuit as lightweight classifier head
  - Addresses operator-dependency in coronary angiography interpretation
  - **Activation**: coronary angiography, CAG classification, quantum ResNet, hybrid CNN-VQC, cardiac imaging, lightweight QML

## 2026-05-27 - Neuroscience Research (Cron Job)

### CogniSNN: Enabling Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability in Spiking Neural Networks
- [[cognisnn-random-graph-snn]] - Cognition-aware SNN with Random Graph Architecture achieving 80.64% on N-Caltech101 with biologically-inspired structural properties (PMID: 42140147)
  - Random Graph Architecture (RGA) replaces rigid chain topology with stochastic connectivity mirroring cortical columns
  - Key Pathway-based Learning without Forgetting (KP-LwF) enables continual learning via selective pathway reuse
  - Dynamic Growth Learning (DGL) allows neurons/synapses to evolve along temporal dimension, mirroring adult neurogenesis
  - **Activation**: CogniSNN, spiking neural network, random graph, continual learning, neuron expandability, neuromorphic, dynamic growth

### Fast Efficient Coding and Sensory Adaptation in Gain-Adaptive Recurrent Networks
- [[fast-efficient-coding-criticality]] - Theoretical framework reconciling adapter-repulsion and prior-attraction under unified gain-modulation efficient-coding model in recurrent sensory circuits (PMID: 42140911)
  - Gain modulation propagated through recurrent weights emerges rapidly (~100ms) without synaptic plasticity
  - Peaked priors → adapter repulsion; broad priors → prior attraction — both from same gain mechanism
  - Behavioral experiment confirms fast prior-attraction prediction; reconciles decades of contradictory adaptation literature
  - **Activation**: efficient coding, sensory adaptation, gain modulation, adapter repulsion, prior attraction, recurrent network, V1

## 2026-05-27 - Neuroscience Research (Cron Job)

### The 3-Body Problem: How Astrocytes May Govern Plasticity
- [[astrocyte-3body-plasticity]] - Astrocyte-centric 3-body tripartite synapse framework for synaptic credit assignment (PMID: 42183627)
  - Astrocytes integrate Ca2+ signals over seconds-to-minutes, bridging millisecond STDP and longer-timescale memory consolidation
  - Proposes astrocytes solve local credit assignment via gliotransmitter (D-serine, ATP) gating of NMDA-dependent plasticity
  - **Activation**: astrocyte, tripartite synapse, credit assignment, plasticity, glia, hebbian learning, STDP

### Low-Latency Visuotactile Neuron Using Self-Oscillating Memristor
- [[nbox-memristor-visuotactile-snn]] - NbOx Mott-transition self-oscillating neuron for 260 ns TTFS multimodal spike encoding (PMID: 42183948)
  - NbOx devices use intrinsic parasitic capacitance as integration element - no external capacitors needed
  - Simultaneously encodes visual and pressure stimuli via TTFS + rate coding for embodied intelligence
  - **Activation**: NbOx memristor, Mott transition, visuotactile, TTFS, low latency, self-oscillating neuron, neuromorphic hardware

## 2026-05-27 - Neuroscience Research (Cron Job)

### Balancing structure and randomness: maximum entropy networks for context-dependent computations
- [[maximum-entropy-neural-connectivity]] - Maximum entropy framework revealing minimal low-rank connectivity structure required for working memory and context-dependent computation (arXiv: 2605.25607)
  - Maximum entropy principle applied to neural connectivity: maximize randomness subject to functional constraints
  - Reveals that context-dependent tasks require specific low-rank structure; other 95% of connectivity can remain random
  - Aligns with empirical low-dimensional structure in prefrontal/cortical recordings
  - **Activation**: maximum entropy, neural connectivity, context-dependent computation, low-rank structure, working memory

### Growing a Neural Network in Breadth, Depth, and Time
- [[growing-neural-network-breadth-depth-time]] - Bio-inspired differentiable framework for autonomous neural network growth in width, depth, and recurrent timesteps matching task complexity (arXiv: 2605.25174)
  - Differentiable cost terms for breadth, depth, and time jointly optimized with task performance
  - Networks grow breadth-first then depth, mirroring cortical developmental trajectories
  - ~30-50% parameter reduction vs. fixed architectures at equivalent accuracy
  - **Activation**: neural network growth, bio-inspired architecture, breadth depth time, resource constraints, differentiable NAS


## 2026-05-27 - Medicine + Quantum (Cron Job - Wednesday)

### A Quantum-Analogue Formalism for Modeling Supraliminal Information Processing
- [[quantum-analogue-supraliminal-processing]] - Cloud-function formalism using Schrödinger-type equations with nonlinear non-Hermitian Hamiltonians to model supraliminal sensory processing and change-of-mind decisions (arXiv: 2605.25214)
  - Non-Hermitian Hamiltonian captures open system dynamics (gain/loss) in neural networks
  - Connectome harmonics as basis for psycho-neural bridge between first-person and third-person perspectives
  - Lotka-Volterra competition terms model neural population interactions
  - Applied to change-of-mind phenomenon: fast preconscious vs slow conscious processing interplay
  - **Activation**: quantum analogue formalism, cloud function, supraliminal processing, Schrödinger neural field, non-Hermitian Hamiltonian, change of mind, connectome harmonics, Lotka-Volterra neural, phase-shift invariance

### On the Complementarity of Quantum and Classical Features: Adaptive Hybrid Quantum-Classical Feature Fusion for Breast Cancer Classification
- [[adaptive-hybrid-feature-fusion-medical]] - 自适应混合量子-经典特征融合方法，通过温度缩放混合融合(TSHF)解决量子-经典优化不对称问题，乳腺癌分类达87.82%准确率 (arXiv: 2604.22903)
  - 核心要点1：提出三种渐进融合策略：SHF(离线)、DHF(端到端)、TSHF(温度缩放自适应)，TSHF最优
  - 核心要点2：可学习标量τ动态平衡量子与经典分支梯度，解决经典梯度主导问题，ResNet+可训练量子电路达最佳性能
  - **新增**: scripts/tshf_fusion.py — 完整PyTorch实现，支持SHF/DHF/TSHF三种策略的即插即用融合模块
  - **Activation**: hybrid quantum-classical feature fusion, 混合量子经典特征融合, temperature-scaled hybrid fusion, TSHF, quantum medical imaging, 量子医学图像, adaptive feature fusion

### Parameter-efficient Quantum Multi-task Learning
- [[parameter-efficient-quantum-mtl]] - 参数高效量子多任务学习框架，用量子预测头替代传统线性头，参数随任务数线性而非二次增长 (arXiv: 2604.13560)
  - 核心要点1：共享VQC编码 + 轻量级任务特定ansatz块，量子头参数复杂度O(T) vs 经典O(d×T)
  - 核心要点2：在医学图像、NLP、多模态基准上达到与经典MTL相当或更优的性能，且参数显著更少
  - **Activation**: quantum multi-task learning, 量子多任务学习, parameter-efficient quantum, QMTL, quantum prediction head

## 2026-05-27 - Neuroscience Research (Cron Job)

### Efficient coding under constraint drives neural systems towards criticality and sloppiness
- [[efficient-coding-criticality-sloppiness]] - 资源约束下的高效编码驱动神经系统趋向临界性与sloppiness (arXiv: 2605.22598)
  - 核心要点 1：最大化Fisher信息在资源约束下自然涌现软模式（soft modes）和发散相关长度——临界性的标志
  - 核心要点 2：统一了统计临界性（发散相关长度）与动力学临界性（临界减速+分岔）两种视角
  - **Activation**: efficient coding, neural criticality, Fisher information, sloppiness, critical brain, power-law neural

### Multi-Objective Optimisation with Oscillatory Dynamics in Spontaneous and Decision Spiking Neural Networks
- [[multi-objective-snn-oscillation]] - 用NSGA-III多目标遗传算法同时优化SNN的发放率和振荡频率，验证于脑类器官数据 (arXiv: 2605.25224)
  - 核心要点 1：NSGA-III可在Pareto前沿上同时匹配神经元发放率和网络振荡频率（gamma/beta/theta band）
  - 核心要点 2：振荡频率对参数更敏感，发放率更鲁棒；成功识别脑类器官的低活跃度制度
  - **Activation**: SNN oscillation, NSGA-III neural, Izhikevich RSNN, brain organoid, multi-objective SNN

## 2026-05-27 - Medicine + Quantum (Cron Job)

### Toward General Quantum Control with Physics-Informed Large Language Models
- [[vf-qctrl-llm-quantum-control]] - 物理信息大语言模型框架用于通用量子控制（VF-QCTRL），结合符号推理与优化提出解析控制ansätze并通过反馈迭代优化参数 (arXiv: 2605.26021)
  - 核心要点1：LLM符号推理提出解析脉冲序列，数值优化精炼参数，无需任务特定训练即可跨多种量子系统工作
  - 核心要点2：QCTRL-Bench基准测试16个任务，涵盖单/多量子比特、闭/开系统动力学、无噪声/有噪声环境，性能匹敌传统最优控制求解器
  - **Activation**: physics-informed LLM, quantum control, vf-qctrl, qctrl-bench, symbolic reasoning, analytic control ansatz, training-free quantum control, benchmark-driven evaluation

## 2026-05-27 - Neuroscience Research (Cron Job)

### Balancing structure and randomness: maximum entropy networks for context-dependent computations
- [[maximum-entropy-network-structure-function]] - 基于最大熵原理的神经网络连接性规范模型，揭示任务约束如何决定神经群体结构 (arXiv: 2605.25607)
  - 核心要点1：最大熵原理 + 任务约束 → 神经元群体结构自发涌现，无需假设特定学习算法
  - 核心要点2：权重尺度β和上下文数K驱动从专业化到随机化的相变，定量匹配梯度下降训练网络
  - **Activation**: maximum entropy, neural connectivity, structure-function, context-dependent computation, gain modulation

### MindAlign: Bridging EEG, Vision, and Language for Zero-Shot Visual Decoding
- [[mindalign-eeg-visual-decoding]] - 三模态对比框架（EEG+视觉+语言）用于零样本视觉解码，200路准确率54.1% vs 此前最优32.4% (arXiv: 2605.24523)
  - 核心要点1：两阶段设计：掩码重建预训练EEG编码器 + 三模态对比对齐（文本作语义正则化器）
  - 核心要点2：紧凑嵌入几何（CN-CLIP）优于大型模型，时序注意力对齐N170/P300神经电生理标志
  - **Activation**: EEG visual decoding, zero-shot, contrastive learning, tri-modal, brain-computer interface

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
  - M

... [OUTPUT TRUNCATED - 162972 chars omitted out of 212972 total] ...

 QFI for all other independent directions (arXiv: 2605.20765)
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