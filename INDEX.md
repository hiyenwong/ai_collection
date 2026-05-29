## 2026-05-29 - 数论、统计学、高等数学 + 量子力学 (Cron Job)

### Rademacher Complexity Bounds for Parameterized Quantum Circuits
- [[quantum-rademacher-bounds]] - 参数化量子电路的Rademacher复杂度界：Pauli串生成电路的泛化能力分析 (arXiv: 2605.29546)
  - 核心要点：全参数域 R_M = O(L^(3/2)/sqrt(M))，受限参数域 R_M = O(L/sqrt(M))
  - 核心要点：经典线性模型 R_M = O(sqrt(L/M))，量子电路在参数依赖上更差但在特征映射表达能力上可能占优
  - 核心要点：样本复杂度估计——全参数域需 O(L^3/epsilon^2) 样本，受限域需 O(L^2/epsilon^2) 样本
  - 核心要点：电路设计启示——参数数量直接影响泛化误差界，参数范围正则化可改善界
  - **Activation**: rademacher complexity, PQC, generalization bounds, pauli strings, quantum ML, sample complexity, statistical learning

### Chain Rules for Conditional Entropies in Quantum Cryptography
- Paper: arXiv: 2605.29787 - Chain rules for conditional entropies in quantum cryptography: limitations and improvements
  - 核心要点：量子密码安全证明依赖于条件熵，链式规则将非i.i.d.过程熵与每轮熵贡献关联
  - 核心要点：熵累积定理(EAT)的关键组件，用于多轮协议的安全证明
  - **Activation**: quantum cryptography, conditional entropy, chain rules, entropy accumulation, security proofs

### Adaptive Stabilizer State Fidelity Certification
- Paper: arXiv: 2605.29820 - Adaptive Stabilizer State Fidelity Certification
  - 核心要点：自适应扩展报告完整认证保真度区间，每轮求解精确端点线性规划
  - 核心要点：证明单调收紧、完全覆盖后精确恢复、最坏情况下全覆盖的必要性
  - **Activation**: stabilizer state, fidelity certification, linear programming, quantum verification, adaptive protocol

### Exact Geometric Typicality and Bipartite Entanglement from Projected CLT
- Paper: arXiv: 2605.29732 - Exact Geometric Typicality and Bipartite Entanglement from the Projected Central Limit Theorem on Hyperspheres
  - 核心要点：从超球面上精确投影中心极限定理重推导Beta分布和Lubkin纯度公式
  - 核心要点：双分量量子互信息完整渐近展开具有Bernoulli因子化形式
  - **Activation**: geometric typicality, central limit theorem, hypersphere, bipartite entanglement, page curve

### Resolving the Phase Space in Quantum Tomography
- Paper: arXiv: 2605.29784 - Resolving the phase space
  - 核心要点：量子层析有效分辨率由测量Gram矩阵关联的采样算子决定
  - 核心要点：Gram特征基重构作为层析问题的测量自适应压缩
  - **Activation**: quantum tomography, phase space, gram matrix, finite frame theory, resolution limit


## 2026-05-29 - Neuroscience Research (Cron Job)

### Brain Critical Dynamics - Hierarchical Organization
- [[brain-critical-dynamics-hierarchical]] - 脑网络临界性的层级组织研究方法论，分析神经元雪崩、幂律分布和相变动力学
  - 核心：临界态最大化信息处理能力，跨尺度幂律不变性
  - 方法：雪崩检测、分支参数分析、重整化群变换、相变检测
  - 应用：癫痫预测、神经退行性疾病、认知功能研究
  - **Activation**: neuronal avalanche, critical brain, power-law, phase transition, scale-free dynamics


## 2026-05-29 - Anthropic Research Check (Cron Job)

### Daily Anthropic Research Fetch
- Fetched 13 articles from https://www.anthropic.com/research
- **All methodology articles already have existing skills**
- Articles without reusable patterns: Coding agents survey (empirical), Project Deal/Vend (features), Anthropic Institute Agenda (research agenda), Economic Index Survey (announcement)
- Updated kg.db with 13 new entities

## 2026-05-29 - Quantum Neural Measurement Dynamics (Cron Job)

### Quantum Neural Network Measurement Dynamics and Critical Phenomena
- [[quantum-neural-measurement-dynamics]] - 量子神经网络测量动力学与临界现象：Born-rule统计、Leggett-Garg测试、动态量子相变 (arXiv: 2605.16029, 2605.12126, 2605.25214)
  - 核心要点：Born-rule统计动力学——Loschmidt echo测量神经态保真度演化，rate function非解析变化指示动态相变
  - 核心要点：Leggett-Garg不等式测试——区分扩散模型与非扩散持久随机模型，K>1违反指示非马尔可夫记忆效应
  - 核心要点：量子类比云函数 ψ(x,t) = Σ_k c_k(t)·φ_k(x)，连接谐波模式建模神经场动力学
  - **Activation**: quantum neural network, measurement dynamics, born rule, leggett-garg, dqpt, neural measurement, quantum-classical boundary, non-diffusive dynamics, memory kernel

## 2026-05-29 - Systems Engineering Research (Cron Job)

### Subsystem Structure as an Inferential Resource for Coupled Engineered Systems
- [[probabilistic-compositional-inference]] - 图架构用于耦合工程系统的概率组合推断，子系统结构作为推断资源 (arXiv: 2605.27544)
  - 核心要点：有向图表示子系统交互，概率接口消息传递不确定性，避免全局协方差矩阵
  - 核心要点：计算复杂度从 O(n³) 降低到 O(N·Smax)，支持异构模型共存，层次化组合跨尺度
  - **Activation**: coupled systems, distributed inference, uncertainty propagation, digital twins, message passing, compositional inference

### Intelligence as Managed Autonomy: Failure, Escalation, and Governance for Agentic AI Systems
- [[smart-managed-autonomy]] - SMARt模型：自主AI系统的管理自主性理论，形式化失败处理与治理可达性 (arXiv: 2605.27628)
  - 核心要点：四层框架（Stable/Meta-cognitive/Assisted/Regulated），Petri网验证界限性质
  - 核心要点：检测认知漂移→暂停推理→尝试恢复→移交控制，触发集确保安全性与完备性
  - **Activation**: managed autonomy, agentic AI safety, failure escalation, governance transitions, Petri net, epistemic drift

     1|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics (Cron Job)

### Geometric Analysis of Variational Quantum Eigensolver
- [[geometric-vqe-analysis]] - VQE优化景观的黎曼几何表征，使用量子Fisher信息矩阵分析收敛性 (arXiv: 2605.27795)
  - 核心要点：将VQE参数空间映射为黎曼流形，QFIM作为度量张量刻画优化景观
  - 核心要点：几何障碍平原检测——QFIM行列式近零对应平坦区域，自然梯度自动预处理
  - **Activation**: VQE geometry, quantum Fisher information, Riemannian VQE, natural gradient, barren plateaus, variational quantum algorithm

### Global Bounds Beyond Local Quantum Metrology
- [[global-quantum-metrology-bounds]] - 超越局部Cramér-Rao理论的全局量子计量界，使用Barankin型界进行全局参数估计 (arXiv: 2605.28374)
  - 核心要点：局部QCRB仅在参数值附近有效，全局Barankin界覆盖整个参数空间
  - 核心要点：揭示局部精度与全局覆盖之间的基本权衡，指导多阶段估计策略设计
  - **Activation**: quantum metrology, Cramér-Rao bound, Barankin bound, global estimation, quantum sensing, precision limits

### SBM Inference via Maximum Likelihood and Optimal Transport
- [[sbm-optimal-transport-inference]] - 最大似然与最优传输的桥梁，使用半松弛Gromov-Wasserstein投影进行SBM参数估计 (arXiv: 2605.28488)
  - 核心要点：MLVI可解释为srGW投影，变分目标与OT正则化匹配
  - 核心要点：Sinkhorn迭代加速社区检测，OT代价作为模型选择准则
  - **Activation**: stochastic block model, optimal transport, Gromov-Wasserstein, community detection, Sinkhorn algorithm, network inference

### Robust Moment-Based Estimation via Spectral Gradient Reweighting
- [[robust-moment-estimation-spectral]] - 基于谱梯度重加权的鲁棒矩估计，在似然不可用/误设时提供抗异常值推断 (arXiv: 2605.27718)
  - 核心要点：对矩雅可比矩阵进行谱分解，按逆谱密度重加权梯度贡献
  - 核心要点：自动抑制高方差方向（异常值集中），无需手动调参即实现有界影响函数
  - **Activation**: moment estimation, GMM, robust statistics, spectral reweighting, M-estimation, outlier robustness

## 2026-05-29 - Neuroscience Research (Cron Job)

### Bullet Trains: Parallelizing Training of Temporally Precise Spiking Neural Networks
- [[bullet-trains-parallel-snn-training]] - 并行训练时间精确SNN，使用关联扫描实现44倍加速，机器精度脉冲时间求解器 (arXiv: 2603.13283)
  - 核心要点：电荷-放电-重置动力学可关联化，并行扫描消解顺序处理瓶颈
  - 核心要点：Newton-Raphson求解器避免时间离散化近似，支持端到端事件驱动训练
  - **Activation**: spiking neural network, snn training, parallel scan, spike timing, event-based, neuromorphic, 并行训练, 脉冲时间

### Misalignment Between Backpropagation and the Hierarchy of Brain Responses to Images
- [[backpropagation-brain-hierarchy-misalignment]] - 反向传播梯度虽能预测脑信号但其时空组织与生物学机制不符 (arXiv: 2605.28693)
  - 核心要点：梯度预测 fMRI/MEG 但计算顺序与脑时间层次不匹配
  - 核心要点：空间组织偏离解剖层级，深度网络与大脑学习机制根本不同
  - **Activation**: 反向传播, 大脑层级, fMRI, MEG, DINOv3, 表征对齐

### Exploratory Experience Shapes the Geometry of Predictive Representations
- [[exploratory-predictive-representation-geometry]] - 探索性行为塑造预测性表征几何，使表征更具空间结构 (arXiv: 2605.27929)
  - 核心要点：探索性agents形成更有组织的空间表征，更好保留转换结构
  - 核心要点：小鼠行为与agent探索度对应，行为通过主动感知塑造学习
  - **Activation**: 探索性学习, predictive coding, active sensing, latent geometry

     2|
     3|### Complex abelian varieties and quantum error correction: a mathematical framework for GKP codes
     4|- [[gkp-abelian-varieties-qec]] - 复阿贝尔簇与量子纠错的数学框架，建立GKP码与代数几何之间的精确对应字典 (arXiv: 2605.28784)
     5|  - 编码空间映射到Theta函数空间，Pauli门对应Theta群，Clifford门对应极化阿贝尔簇自同构
     6|  - 编码渐近等距，小噪声下失败概率由极化同源核的最短非平凡位移（systolic不变量）控制
     7|  - **Activation**: GKP codes, abelian varieties, quantum error correction, theta functions, algebraic geometry, number theory, systolic bounds, 复阿贝尔簇, 量子纠错
     8|
     9|## 2026-05-29 - Neuroscience Research (Cron Job)
    10|
    11|### VLMs May Not Globally Enhance Human Alignment over LLMs During Natural Reading
    12|- [[vlms-human-alignment-natural-reading]] - 受控文本评估揭示多模态预训练无全局优势，视觉语义内容选择性激活 VLM 对齐 (arXiv: 2605.28818)
    13|  - 多模态预训练不带来全局脑对齐优势，语言内部表征是关键因素
    14|  - VLM 优势仅在视觉语义内容强的句子中涌现（fMRI + 眼动验证）
    15|  - 受控设计：紧密匹配 LLM-VLM 对 + 文本-only 评估 + whole-cortex fMRI + 同步眼动追踪
    16|  - **Activation**: VLM-LLM alignment, human brain model comparison, natural reading fMRI, eye-tracking alignment, visual semantic content, multimodal pretraining, text-only evaluation, RSA, 脑模型对齐
    17|
    18|## 2026-05-29 - Neuroscience Research (Cron Job)
    19|
    20|### CLANE: Continual Learning of Actions on Neuromorphic Hardware from Event Cameras
    21|- [[clane-neuromorphic-continual-learning]] - 首个端到端神经形态持续学习系统，在 Intel Loihi 2 上实现动作识别的在线学习 (arXiv: 2605.28387)
    22|  - 70.4% 准确率，100x 能量降低，16x 延迟减少
    23|  - Spiking 2D CNN + CLP-SNN + Temporal Aggregation Layer + Fixed-Point Normalization
    24|  - THU E-ACT-50 50类动作数据集 + iso-algorithm跨平台基准测试
    25|  - **Activation**: neuromorphic continual learning, event camera, Loihi 2, spiking CNN, CLP-SNN, action recognition, on-device learning, energy-efficient AI, edge deployment, 神经形态持续学习, 事件相机
    26|
    27|## 2026-05-29 - Neuroscience Research (Cron Job)
    28|
    29|### Benchmarking Fairness in Spiking Neural Networks: Data Bias, Spurious Features, and Hardware Effects
    30|- [[snn-fairness-benchmark-hardware]] - 首个系统性 SNN 公平性基准，揭示数据偏差与硬件限制的交互效应 (arXiv: 2605.27407)
    31|  - 数据偏差导致弱势群体假阳性率提高23%，硬件限制放大差异至41%
    32|  - 云端公平性干预策略在边缘设备约束下失效，需公平性-硬件协同设计
    33|  - 四个跨人口统计数据集 + Loihi 2/SpiNNaker 模拟器 + 12个 SNN 架构评估
    34|  - **Activation**: SNN fairness, neuromorphic bias, hardware effects, edge deployment, spike precision, fairness benchmark, 数据偏差, 神经形态公平性
    35|
    36|### STARS: Spike Tail-Aware Relational Synthesis for ANN-to-SNN Data-Free Knowledge Distillation
    37|- [[stars-snn-data-free-knowledge-distillation]] - 首个针对 SNN 阈值动力学的无数据知识蒸馏方法 (arXiv: 2605.27409)
    38|  - 关系一致性对齐 (RCA) 保持跨样本关系结构，尾概率正则化 (TAR) 优化阈值相关区域
    39|  - BN 匹配仅约束均值/方差，无法捕获 SNN 脉冲生成的阈值穿越动力学
    40|  - CIFAR-10 提升4.6%，CIFAR-100 提升6.7%，超越部分使用真实数据的 KD 方法
    41|  - **Activation**: SNN knowledge distillation, data-free distillation, ANN-to-SNN, tail-aware regularization, relational consistency, threshold dynamics, 无数据蒸馏
    42|
    43|     1|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics (Cron Job)
    44|     2|
    45|     3|### Complex abelian varieties and quantum error correction: a mathematical framework for GKP codes
    46|     4|- [[gkp-abelian-varieties-qec]] - GKP码通过复阿贝尔簇的几何：θ函数作为码空间，Pauli门来自θ群，Clifford门对应变换自同构 (arXiv: 2605.28784)
    47|     5|  - 核心：GKP码与极化复阿贝尔簇的精确数学对应，编码渐近等距，Clifford门由高斯酉实现
    48|     6|  - 失败概率由极化同态核中最短非平凡位移（systolic不变量）主导
    49|     7|  - 将量子纠错性能优化转化为阿贝尔簇模空间上的几何优化问题
    50|     8|  - **Activation**: GKP codes, abelian varieties, algebraic geometry quantum, theta functions, Clifford gates Gaussian, bosonic error correction, quantum systolic geometry
    51|     9|
    52|    10|
    53|    11|## 2026-05-29 - Neuroscience Research (Cron Job)
    54|    12|
    55|    13|### Misalignment Between Backpropagation and the Hierarchy of Brain Responses to Images
    56|    14|- [[backpropagation-brain-hierarchy-misalignment]] - 反向传播梯度与脑视觉层级不对齐，揭示深度学习与大脑学习机制根本差异 (arXiv: 2605.28693)
    57|    15|  - 反向梯度能预测脑信号（fMRI/MEG），但时空组织与生物学反向传播预期不符
    58|    16|  - 前向激活对齐 ≠ 反向机制对齐，挑战"大脑实现反向传播"假设
    59|    17|  - **Activation**: 反向传播, 脑对齐, 表征对齐, 梯度分析, fMRI, MEG, 视觉皮层
    60|    18|
    61|    19|### Non-invertible symmetry enriched string net topological orders
    62|    20|- [[non-invertible-topological-order-analysis]] - Analysis methodology for non-invertible symmetry enriched topological orders using unitary fusion categories (arXiv: 2605.28794)
    63|    21|  - Core: NI-SETO definition via UFC full inclusions and anyon condensation
    64|    22|  - Applications: Topological quantum computing, fusion category symmetries
    65|    23|  - **Activation**: topological order, non-invertible symmetry, fusion category, string net, anyon condensation
    66|    24|
    67|    25|### Quantum Statistical Estimation Theory
    68|    26|- [[quantum-statistical-estimation-framework]] - Framework for quantum statistical estimation combining QFI, CRB bounds, and Bayesian quantum estimation (arXiv: general framework)
    69|    27|  - Core: Quantum Fisher Information, Cramér-Rao bounds, multi-parameter estimation
    70|    28|  - Applications: Quantum sensing, metrology, parameter estimation in quantum systems
    71|    29|  - **Activation**: quantum fisher information, cramér-rao bound, quantum estimation, metrology, quantum sensing
    72|    30|
    73|    31|### Dynamic Entanglement Packet Scheduling for Quantum Networks
    74|    32|- Related: quantum-network-control skill (already exists) - entanglement distribution in quantum networks using TDMA (arXiv: 2605.28795)
    75|    33|  - Core: On-demand entanglement packet architecture with TDMA resource allocation
    76|    34|  - Applications: Scalable quantum networks, multi-user entanglement distribution
    77|    35|  - **Activation**: quantum network, entanglement packet, TDMA, resource allocation
    78|    36|
    79|    37|### Device-Agnostic Microwave Noise Metrology
    80|    38|- Related: quantum-metrology-sensing-review skill - microwave noise characterization for cryogenic quantum devices (arXiv: 2605.28808)
    81|    39|  - Core: Near-quantum-limited signal processing for solid-state quantum technologies
    82|    40|  - Applications: Quantum device characterization, cryogenic measurement
    83|    41|  - **Activation**: microwave metrology, noise characterization, cryogenic quantum, signal processing
    84|    42|
    85|    43|## 2026-05-29 - Neuroscience Research (Cron Job)
    86|    44|
    87|    45|### CaMBRAIN: Real-time, Continuous EEG Inference with Causal State Space Models
    88|    46|- [[cambrain-realtime-eeg-inference]] - First causal Mamba SSM for real-time continuous EEG inference with >10x throughput (arXiv: 2605.28792)
    89|    47|  - Causal Mamba SSM enables streaming EEG inference with linear O(n) complexity
    90|    48|  - Multi-stage self-supervised training for long-range memory retention
    91|    49|  - Bidirectional approaches are needlessly expensive for inherently causal EEG
    92|    50|  - State-of-the-art across 3 EEG datasets with real-time processing capability
    93|    51|  - **Activation**: EEG, real-time inference, state space model, Mamba, causal, streaming EEG, continuous inference
    94|    52|
    95|    53|### Misalignment Between Backpropagation and the Hierarchy of Brain Responses to Images
    96|    54|- [[backpropagation-brain-hierarchy-misalignment]] - 反向传播梯度能预测fMRI/MEG信号但组织方式与大脑不匹配 (arXiv: 2605.28693)
    97|    55|  - 反向传播梯度能预测fMRI/MEG信号但组织方式与大脑不匹配
    98|    56|  - 空间和时间层级均与反向传播顺序不一致
    99|    57|  - 深度网络与大脑使用不同学习机制
   100|    58|  - **Activation**: backpropagation, brain hierarchy, visual cortex, gradient alignment
   101|