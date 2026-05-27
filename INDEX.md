
## 2026-05-28 - Neuroscience Research (Cron Job)

### Quantum Neuromorphic Spiking Dynamics: Bridging Quantum Computing and Neural Dynamics
- [[quantum-neuromorphic-spiking-dynamics]] - 量子神经形态脉冲动力学方法论，结合量子计算动力学与SNN原理实现能效计算 (arXiv:2605.XXXXX)
  - 量子膜电位类比：量子比特状态类比神经元膜电位
  - 量子脉冲时序编码：相位/振幅编码脉冲时间和强度
  - 量子 Kuramoto 振荡器实现神经同步动力学
  - **Activation**: quantum neuromorphic, spiking quantum computing, quantum SNN, quantum neural oscillator, quantum membrane potential

### Random neural networks match observed dimensionality of neural population recordings
- [[random-neural-network-dimensionality]] - 随机神经网络维数匹配神经种群记录的DMFT方法论 (arXiv:2605.26551)
  - Dynamical Mean-Field Theory扩展纳入有限测量时间和跨语境变异
  - 流形方向相似性比维数更敏感于网络结构
  - 提供推断连接结构的定量实验设计指导
  - **Activation**: neural dimensionality, DMFT, neural manifold, experimental design

### Revealing the core dimensions underlying representations in brains, behavior and AI
- [[srf-similarity-representation-factorization]] - SRF方法从相似性矩阵恢复可解释维度 (arXiv:2605.26921)
  - 非负低维嵌入提高可解释性
  - 支持稀疏采样和不完整数据
  - 假设检验效力高于直接比较相似性矩阵
  - **Activation**: SRF, representation factorization, similarity matrix, interpretability

### NeuroRing: Scaling Spiking Neural Networks via Multi-FPGA Bidirectional Ring Topologies and Stream-Dataflow Architectures
- [[neuroring-multi-fpga-snn]] - 多FPGA双向环形拓扑SNN加速器，实现实时因子0.83的快速执行 (arXiv:2604.28059)
  - 双向环形拓扑：确定性延迟、容错性、线性扩展
  - 流数据流架构：事件驱动、异步、高吞吐量
  - NEST集成：无缝工作流过渡，生物学保真度验证
  - 强扩展性：RTF从2.1（1 FPGA）→0.83（4 FPGA）
  - **Activation**: NeuroRing, multi-FPGA SNN, neuromorphic hardware, ring topology, FPGA accelerator

     1|## 2026-05-28 - Systems Engineering (Cron Job)
     2|
     3|### Statistical and Algorithmic Foundations of Probing Quantum Systems with Compressive Measurements: A Review
     4|- [[structured-quantum-tomography]] - 结构化量子态层析成像方法论，结合压缩感知、低秩表示、张量网络和神经量子态实现可扩展量子态重建 (arXiv: 2605.27191)
     5|  - 三大主题：紧凑态表示、测量设计（IC-POVM/随机测量）、计算算法
     6|  - 随机测量（Pauli/Clifford）提供近最优采样复杂度
     7|  - 凸优化保证恢复、非凸优化提升可扩展性
     8|  - **Activation**: quantum state tomography, compressive quantum measurement, IC-POVM, randomized measurement
     9|
    10|
    11|## 2026-05-27 - Neuroscience Research (Cron Job)
    12|
    13|### MindAlign: Bridging EEG, Vision, and Language for Zero-Shot Visual Decoding
    14|- [[mindalign-eeg-visual-decoding]] - 三模态对比学习框架，实现EEG零样本视觉解码，54.1% Top-1准确率大幅超越基线 (arXiv: 2605.24523)
    15|  - 两阶段训练：Masked autoencoder预训练 + 三模态对比对齐
    16|  - CN-CLIP紧凑嵌入优于大型CLIP模型
    17|  - 文本描述作为语义正则化器，权重α=0.3最优
    18|  - **Activation**: EEG visual decoding, zero-shot image retrieval, tri-modal alignment
    19|
    20|### Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons
    21|- [[stm-sequence-timing-replay]] - 脉冲神经网络中的序列时序学习，振荡背景输入控制重放速度 (arXiv: 2605.22523)
    22|  - 持续编码：元素特定神经元群的顺序激活表示时长
    23|  - 振荡时钟：背景振荡作为时钟信号控制重放速度
    24|  - EEG/LFP相关性：清醒/睡眠重放速度与脑电振荡特征相关
    25|  - **Activation**: spiking sequence timing, replay speed control, oscillatory clock
    26|
    27|
    28|## 2026-05-27 - Neuroscience Research (Cron Job)
    29|
    30|### Random neural networks match observed dimensionality of neural population recordings and motivate stronger experimental tests
    31|- [[random-network-neural-dimensionality]] - First quantitative validation that minimally structured random neural networks can account for observed low dimensionality using DMFT with finite measurement time corrections (arXiv: 2605.26551)
    32|  - Core methodology: Dynamical Mean-Field Theory extended with measurement time and behavioral context variability
    33|  - Key finding: manifold orientation similarity more sensitive to network structure than dimensionality alone
    34|  - **Activation**: neural dimensionality, random neural network, population recording, DMFT, neural manifold, connectivity inference
    35|
    36|### Revealing the core dimensions underlying representations in brains, behavior and AI
    37|- [[srf-similarity-representation-factorization]] - Similarity-Based Representation Factorization (SRF) for recovering interpretable non-negative embeddings from similarity matrices across neural/behavioral/AI data (arXiv: 2605.26921)
    38|  - Core methodology: Non-negative factorization of similarity matrices with robustness to sparse/incomplete data
    39|  - Key advantage: higher statistical power for hypothesis testing than traditional RSA
    40|  - **Activation**: representation factorization, SRF, similarity matrix, interpretable embedding, brain-AI alignment
    41|
    42|## 2026-05-27 - Medicine + Quantum (Cron Job)
    43|
    44|### What Molecular Structure Cannot Tell Us: A Taxonomy of Explainability Gaps in GNN-Based Drug Toxicity Prediction
    45|- [[gnn-drug-toxicity-explainability]] - Gap Taxonomy (GAP-1 to GAP-4) for systematic analysis of explainability limitations in GNN drug toxicity prediction using GNNExplainer on MPNN models (arXiv: 2605.26183)
    46|  - Core methodology: Train MPNN on Tox21, apply GNNExplainer for atom-level attribution, categorize missing predictions into 4 gap types
    47|  - Key finding: molecular structure explains ~45% of known adverse effects; MNAR gap reveals systematic data absence in ChEMBL
    48|  - **Activation**: GNN drug toxicity, GNNExplainer, MPNN, Gap Taxonomy, MNAR drug data, Tox21, pharmacovigilance, drug safety signals
    49|
    50|### Autonomous oscillations in quantum electromechanics: tensor network treatment
    51|- [[tensor-network-quantum-electromechanics]] - Tensor network framework for quantum electromechanical self-oscillations using binary vibrational mode representation with mesoscopic reservoir embeddings (arXiv: 2605.27326)
    52|  - Core methodology: Map bosonic Hilbert space to binary representation, embed fermionic leads, compute steady states without real-time propagation
    53|  - Key finding: self-oscillation window preceded by peak in occupation fluctuations, observed for both slow and fast mechanical modes
    54|  - **Activation**: tensor network quantum, quantum electromechanics, self-oscillation, mesoscopic leads, binary mode mapping, quantum thermodynamics
    55|
    56|     1|## 2026-05-28 - Neuroscience Research (Cron Job)
    57|     2|
    58|     3|### Arbor-TVB: Multi-Scale Co-Simulation Framework for Neural-Level Seizure Generation and Whole-Brain Propagation
    59|     4|- [[arbor-tvb-multiscale-simulation]] - MPI-based integration of microscopic Arbor neurons with macroscopic TVB brain models, enabling bidirectional spike ↔ mean activity translation (arXiv: 2505.16861)
    60|     5|  - First framework linking detailed spiking neurons (Arbor) with whole-brain network models (TVB) via MPI intercommunicator
    61|     6|  - Real-time translation: discrete spikes → continuous mean activity, continuous input → synaptic currents
    62|     7|  - Seizure case study: 38-region mouse brain model, seizure onset propagation from Arbor-embedded hippocampus to whole-brain
    63|     8|  - Modular design: replace any TVB node with biologically realistic Arbor populations
    64|     9|  - **Activation**: multiscale simulation, arbor tvb, seizure propagation, brain network model, mpi neuroscience, neural mass model
    65|    10|
    66|    11|## 2026-05-28 - Medicine + Quantum (Cron Job)
    67|    12|
    68|    13|### Parallel Multi-Circuit Quantum Feature Fusion in Hybrid Quantum-Classical Convolutional Neural Networks for Breast Tumor Classification
    69|    14|- [[qcnn-parallel-feature-fusion-medical]] - Hybrid QCNN with parallel amplitude+angle encoding VQCs for medical image classification, statistically validated via Wilcoxon test and Cohen's d (arXiv: 2512.02066)
    70|    15|  - Core methodology: Two distinct quantum circuits (amplitude-encoding VQC + angle-encoding VQC with circular entanglement) run in parallel on 4 qubits; quantum embeddings fused with classical conv features
    71|    16|  - Statistical validation: Parameter-matched comparison, 5 independent runs, Wilcoxon signed-rank test (p=0.03125), Cohen's d=2.14 (large effect)
    72|    17|  - **Activation**: qcnn parallel feature fusion, quantum feature fusion medical, statistical validation quantum ml, wilcoxon quantum advantage, cohen d quantum classification, breastmnist quantum
    73|    18|
    74|    19|### Discovering Data Encoding Strategies for Quantum-Classical Neural Networks Using Monte Carlo Tree Search
    75|    20|- [[mcts-encoding-discovery-qml]] - MCTS discovers optimal data encoding circuits for QCCNN, effective rank as encoding performance predictor (arXiv: 2605.18540)
    76|    21|  - Core methodology: MCTS searches encoding circuit space for quantum-classical CNN with non-variational quantum block + classical classifier
    77|    22|  - Key insight: Effective rank of feature maps correlates with encoding performance (not entanglement capability or Fourier decomposition)
    78|    23|  - **Activation**: mcts encoding discovery, effective rank encoding, quantum data encoding, QCCNN encoding, monte carlo tree search quantum
    79|    24|
    80|    25|## 2026-05-27 - Medicine + Quantum (Cron Job)
    81|    26|
    82|    27|### A novel perspective on denoising using quantum localization with application to medical imaging
    83|    28|- [[a-novel-perspective-on-denoising-using-quantum-loc]] - Quantum-enhanced medical image classification framework (arXiv: 2405.12226)
    84|    29|  - Core methodology: Background noise in many fields such as medical imaging poses significant challenges for accurate diagnosis, prompting the development of denoising algorithms. Traditional methodologies, however, ofte
    85|    30|  - **Activation**: diagnosis, measurement, image, medical, noise, quantum
    86|    31|
    87|    32|## 2026-05-27 - Medicine + Quantum Metrology (Cron Job)
    88|    33|
    89|    34|### Journey in quantum metrology and sensing from foundations to applications: a review
    90|    35|- [[quantum-metrology-sensing-review]] - 93页量子计量与传感综述，涵盖参数估计、量子Fisher信息、量子成像与照明、原子钟 (arXiv: 2605.21702)
    91|    36|  - 经典/贝叶斯参数估计框架与量子Cramér-Rao界
    92|    37|  - 量子Fisher信息矩阵用于多参数估计与资源检测
    93|    38|  - 量子照明在噪声环境中的目标检测优势
    94|    39|  - 量子传感在生物医学中的应用(NV中心磁力计、量子增强MRI)
    95|    40|  - **Activation**: quantum metrology, quantum sensing, quantum Fisher information, quantum thermometry, quantum imaging, quantum illumination
    96|    41|
    97|    42|## 2026-05-27 - Medicine + Quantum ML (Cron Job)
    98|    43|
    99|    44|### High-fidelity molecular quantum logic gates resilient to interaction fluctuation
   100|    45|- [[quantum-ml-medical-diagnosis]] - Quantum ML methodologies for medical diagnosis and healthcare
   101|

## 2026-05-28 - Systems Engineering + Quantum (Cron Job)

### Magic-Informed Quantum Architecture Search
- [[magic-informed-quantum-architecture-search]] - MCTS+GNN量子架构搜索，利用魔量(nonstabilizerness)引导量子电路设计，实现可控量子资源优化 (arXiv: 2605.03932)
  - 核心要点 1: 使用GNN估计量子电路的magic属性，作为MCTS搜索的启发式引导
  - 核心要点 2: 支持高/低magic偏置，可搜索量子优势最大化和经典可模拟近似两种模式
  - 核心要点 3: GNN泛化到分布外电路尺寸，跨问题类型一致提升搜索质量
  - **Activation**: magic-informed architecture search, quantum architecture search MCTS, nonstabilizerness-guided circuit design, 魔力量子架构搜索, 非稳定化力量子电路设计

### Adaptive Reinforcement Learning for Robust Open Quantum System Control
- [[rl-quantum-control]] - 多任务SAC强化学习框架用于开放量子系统控制，跨Hamiltonian分布学习最优脉冲序列 (arXiv:2605.26925)
  - 多任务策略共享：单个策略处理多种量子控制任务，同时适应系统参数
  - 最大熵RL(SAC)确保探索稳定性，自动温度调优
  - 在未知参数下实现高保真度控制，无需显式系统辨识
  - **Activation**: rl quantum control, multi-task quantum control, SAC quantum control, reinforcement learning quantum, 强化学习量子控制

### dSABRE & ATHENA: Distributed Quantum Computing Routing and Scheduling
- [[distributed-quantum-routing]] - 多核分布式量子计算机路由和调度方法论，最小化EPR对消耗 (arXiv:2605.21960, 2605.21795)
  - dSABRE启发式路由：SABRE风格路由适配分布式架构，最小化纠缠资源使用
  - ATHENA编译器优化：协调量子比特移动和门执行，考虑隐形传态延迟和成功率
  - SQARL无尺度RL分配：训练跨电路大小的通用分配策略
  - **Activation**: distributed quantum routing, dSABRE, ATHENA compiler, EPR optimization, quantum circuit allocation, 分布式量子路由

### QuCtrl-BELL: Compiler-Driven Quantum Feedback Control
- [[quantum-compiler-feedback]] - 编译器驱动的微秒级反馈控制栈，将电路优化与硬件级实时反馈结合 (arXiv:2605.22433)
  - 离线编译所有测量结果对应的控制序列，硬件级执行
  - 反馈延迟O(1)，不随电路复杂度增长，关键用于量子纠错
  - BELL序列（Basic Embedded Logic for Low-latency）架构
  - **Activation**: quantum feedback control, compiler quantum control, QuCtrl-BELL, sub-microsecond feedback, low-latency quantum, 量子编译器反馈

### Performance Limits of Fault-Tolerant Quantum Error Correction
- [[quantum-error-correction-limits]] - 现实条件下的量子纠错性能极限分析，考虑测量误差、解码延迟和控制噪声 (arXiv:2605.24501)
  - 现实阈值始终低于理想阈值（测量误差降低10-30%）
  - 解码延迟引入等待错误：p_idle = 1 - exp(-t_decode / T_1)
  - 系统化评估所有误差源对资源开销的影响
  - **Activation**: QEC performance limits, fault tolerance analysis, syndrome measurement error, decoder latency, realistic QEC, 量子纠错性能极限

### Homomorphic Quantum Error Correction
- [[homomorphic-qec]] - 同态量子纠错方法论，保护服务器端处理的量子数据免受未授权访问和环境噪声 (arXiv:2605.25692)
  - 代数兼容性分析：同态操作与量子纠错码的兼容性
  - 同时实现隐私保护和噪声抵抗
  - **Activation**: homomorphic quantum error correction, quantum data protection, 同态量子纠错

### Scalable Quaternary Message-Passing Decoding for QEC
- [[scalable-quaternary-qec-decoding]] - 可扩展的四元消息传递解码方法，解决表面码等QEC解码的可扩展性和可解释性问题 (arXiv:2605.24177)
  - 四元置信传播(Belief Propagation)解码器
  - 解决大规模量子纠错解码的可扩展性挑战
  - **Activation**: quaternary QEC decoding, message-passing decoding, belief propagation quantum, scalable QEC decoder

### Quantum Sensing and QEC: Two Sides of the Same Coin
- [[quantum-sensing-qec-duality]] - 揭示量子传感与量子纠错的内在联系：最优传感态设计可借鉴QEC码结构 (arXiv:2605.24120)
  - 参数估计最优态与纠错码的等价性
  - 统一量子计量与纠错的理论框架
  - **Activation**: quantum sensing QEC, quantum metrology error correction, quantum parameter estimation

### SQARL: Size-Agnostic RL for Distributed Quantum Circuit Allocation
- [[sqarl-quantum-allocation]] - 无尺度强化学习方法用于分布式量子电路分配，适应不同规模的量子处理器 (arXiv:2605.27027)
  - 训练策略适应任意电路尺寸和硬件拓扑
  - 奖励函数：最小化EPR消耗和执行时间
  - 在线部署新电路分配
  - **Activation**: SQARL, size-agnostic RL quantum, circuit allocation RL, distributed quantum allocation

