## 2026-05-29 - Neuroscience Research (Cron Job)

### CLANE: Continual Learning of Actions on Neuromorphic Hardware from Event Cameras
- [[clane-neuromorphic-continual-learning]] - 首个端到端神经形态持续学习系统，在 Intel Loihi 2 上实现动作识别的在线学习 (arXiv: 2605.28387)
  - 70.4% 准确率，100x 能量降低，16x 延迟减少
  - Spiking 2D CNN + CLP-SNN + Temporal Aggregation Layer + Fixed-Point Normalization
  - THU E-ACT-50 50类动作数据集 + iso-algorithm跨平台基准测试
  - **Activation**: neuromorphic continual learning, event camera, Loihi 2, spiking CNN, CLP-SNN, action recognition, on-device learning, energy-efficient AI, edge deployment, 神经形态持续学习, 事件相机

## 2026-05-29 - Neuroscience Research (Cron Job)

### Benchmarking Fairness in Spiking Neural Networks: Data Bias, Spurious Features, and Hardware Effects
- [[snn-fairness-benchmark-hardware]] - 首个系统性 SNN 公平性基准，揭示数据偏差与硬件限制的交互效应 (arXiv: 2605.27407)
  - 数据偏差导致弱势群体假阳性率提高23%，硬件限制放大差异至41%
  - 云端公平性干预策略在边缘设备约束下失效，需公平性-硬件协同设计
  - 四个跨人口统计数据集 + Loihi 2/SpiNNaker 模拟器 + 12个 SNN 架构评估
  - **Activation**: SNN fairness, neuromorphic bias, hardware effects, edge deployment, spike precision, fairness benchmark, 数据偏差, 神经形态公平性

### STARS: Spike Tail-Aware Relational Synthesis for ANN-to-SNN Data-Free Knowledge Distillation
- [[stars-snn-data-free-knowledge-distillation]] - 首个针对 SNN 阈值动力学的无数据知识蒸馏方法 (arXiv: 2605.27409)
  - 关系一致性对齐 (RCA) 保持跨样本关系结构，尾概率正则化 (TAR) 优化阈值相关区域
  - BN 匹配仅约束均值/方差，无法捕获 SNN 脉冲生成的阈值穿越动力学
  - CIFAR-10 提升4.6%，CIFAR-100 提升6.7%，超越部分使用真实数据的 KD 方法
  - **Activation**: SNN knowledge distillation, data-free distillation, ANN-to-SNN, tail-aware regularization, relational consistency, threshold dynamics, 无数据蒸馏

     1|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics (Cron Job)
     2|
     3|### Complex abelian varieties and quantum error correction: a mathematical framework for GKP codes
     4|- [[gkp-abelian-varieties-qec]] - GKP码通过复阿贝尔簇的几何：θ函数作为码空间，Pauli门来自θ群，Clifford门对应变换自同构 (arXiv: 2605.28784)
     5|  - 核心：GKP码与极化复阿贝尔簇的精确数学对应，编码渐近等距，Clifford门由高斯酉实现
     6|  - 失败概率由极化同态核中最短非平凡位移（systolic不变量）主导
     7|  - 将量子纠错性能优化转化为阿贝尔簇模空间上的几何优化问题
     8|  - **Activation**: GKP codes, abelian varieties, algebraic geometry quantum, theta functions, Clifford gates Gaussian, bosonic error correction, quantum systolic geometry
     9|
    10|
    11|## 2026-05-29 - Neuroscience Research (Cron Job)
    12|
    13|### Misalignment Between Backpropagation and the Hierarchy of Brain Responses to Images
    14|- [[backpropagation-brain-hierarchy-misalignment]] - 反向传播梯度与脑视觉层级不对齐，揭示深度学习与大脑学习机制根本差异 (arXiv: 2605.28693)
    15|  - 反向梯度能预测脑信号（fMRI/MEG），但时空组织与生物学反向传播预期不符
    16|  - 前向激活对齐 ≠ 反向机制对齐，挑战"大脑实现反向传播"假设
    17|  - **Activation**: 反向传播, 脑对齐, 表征对齐, 梯度分析, fMRI, MEG, 视觉皮层
    18|
    19|### Non-invertible symmetry enriched string net topological orders
    20|- [[non-invertible-topological-order-analysis]] - Analysis methodology for non-invertible symmetry enriched topological orders using unitary fusion categories (arXiv: 2605.28794)
    21|  - Core: NI-SETO definition via UFC full inclusions and anyon condensation
    22|  - Applications: Topological quantum computing, fusion category symmetries
    23|  - **Activation**: topological order, non-invertible symmetry, fusion category, string net, anyon condensation
    24|
    25|### Quantum Statistical Estimation Theory
    26|- [[quantum-statistical-estimation-framework]] - Framework for quantum statistical estimation combining QFI, CRB bounds, and Bayesian quantum estimation (arXiv: general framework)
    27|  - Core: Quantum Fisher Information, Cramér-Rao bounds, multi-parameter estimation
    28|  - Applications: Quantum sensing, metrology, parameter estimation in quantum systems
    29|  - **Activation**: quantum fisher information, cramér-rao bound, quantum estimation, metrology, quantum sensing
    30|
    31|### Dynamic Entanglement Packet Scheduling for Quantum Networks
    32|- Related: quantum-network-control skill (already exists) - entanglement distribution in quantum networks using TDMA (arXiv: 2605.28795)
    33|  - Core: On-demand entanglement packet architecture with TDMA resource allocation
    34|  - Applications: Scalable quantum networks, multi-user entanglement distribution
    35|  - **Activation**: quantum network, entanglement packet, TDMA, resource allocation
    36|
    37|### Device-Agnostic Microwave Noise Metrology
    38|- Related: quantum-metrology-sensing-review skill - microwave noise characterization for cryogenic quantum devices (arXiv: 2605.28808)
    39|  - Core: Near-quantum-limited signal processing for solid-state quantum technologies
    40|  - Applications: Quantum device characterization, cryogenic measurement
    41|  - **Activation**: microwave metrology, noise characterization, cryogenic quantum, signal processing
    42|
    43|## 2026-05-29 - Neuroscience Research (Cron Job)
    44|
    45|### CaMBRAIN: Real-time, Continuous EEG Inference with Causal State Space Models
    46|- [[cambrain-realtime-eeg-inference]] - First causal Mamba SSM for real-time continuous EEG inference with >10x throughput (arXiv: 2605.28792)
    47|  - Causal Mamba SSM enables streaming EEG inference with linear O(n) complexity
    48|  - Multi-stage self-supervised training for long-range memory retention
    49|  - Bidirectional approaches are needlessly expensive for inherently causal EEG
    50|  - State-of-the-art across 3 EEG datasets with real-time processing capability
    51|  - **Activation**: EEG, real-time inference, state space model, Mamba, causal, streaming EEG, continuous inference
    52|
    53|### Misalignment Between Backpropagation and the Hierarchy of Brain Responses to Images
    54|- [[backpropagation-brain-hierarchy-misalignment]] - 反向传播梯度能预测fMRI/MEG信号但组织方式与大脑不匹配 (arXiv: 2605.28693)
    55|  - 反向传播梯度能预测fMRI/MEG信号但组织方式与大脑不匹配
    56|  - 空间和时间层级均与反向传播顺序不一致
    57|  - 深度网络与大脑使用不同学习机制
    58|  - **Activation**: backpropagation, brain hierarchy, visual cortex, gradient alignment
    59|
    60|### Exploratory Experience Shapes the Geometry of Predictive Representations
    61|- [[exploratory-experience-predictive-representations]] - 探索性行为塑造更组织化的预测表征几何 (arXiv: 2605.27929)
    62|  - 探索性行为塑造更组织化的预测表征几何
    63|  - 利用性行为导致无组织的表征
    64|  - 小鼠与人工agent的行为-表征对齐
    65|  - **Activation**: exploration, predictive representations, active sensing, spatial navigation
    66|
    67|### EEG-FM-Audit: A Systematic Evaluation and Analysis Pipeline for EEG Foundation Models
    68|- [[eeg-fm-audit-systematic-evaluation]] - ASHA驱动的公平基准测试 (arXiv: 2605.26910)
    69|  - ASHA驱动的公平基准测试
    70|  - 范式级消融研究验证FM有效性
    71|  - 神经生理学探测(NPP)揭示生理特征使用
    72|  - **Activation**: EEG foundation model, ASHA benchmarking, neurophysiological probing, interpretability
    73|
    74|
    75|---
    76|
    77|     1|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
    78|     2|
    79|     3|### Latent-Conditioned Parameterized Quantum Circuits as Universal Approximators for Distributions over Quantum States
    80|     4|- [[latent-conditioned-pqc-universal-approximator]] - 量子态分布通用逼近定理：LPQC在1-Wasserstein距离下逼近任意密度算子概率分布 (arXiv: 2605.28690)
    81|     5|  - 核心：经典神经网络将潜变量映射到PQC参数，证明量子分布设置的通用逼近定理
    82|     6|  - MoE架构+多模态潜先验缓解barren plateau问题
    83|     7|  - QM9分子结构集成实验验证，超越量子生成基线
    84|     8|  - **Activation**: latent-conditioned PQC, LPQC, universal approximator quantum states, quantum generative modeling, Wasserstein distance quantum, barren plateau MoE
    85|     9|
    86|    10|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics (Cron Job)
    87|    11|
    88|    12|### Iterative maps emerging from cohomological structure of primes
    89|    13|- [[prime-cohomological-maps]] - 素数上同构结构分析：迭代映射预测素数增长，对数积分函数为上同构方程的解 (arXiv: 2605.17622)
    90|    14|  - 核心要点 1: 素数间隙按分离距离分组，可用迭代映射描述其主要增长
    91|    15|  - 核心要点 2: 剩余涨落编码上同构结构，li(x)为上同构方程的解
    92|    16|  - **Activation**: cohomological prime analysis, prime number iterative maps, 素数上同构分析, 素数迭代映射, logarithmic integral prime distribution
    93|    17|
    94|    18|### Module Lattice Security Part III: Structured CVP Distance on the Log-Unit Lattice
    95|    19|- [[module-lattice-security]] (enhanced) - 模格安全性分析：L2 CVP距离收敛到Voronoi细胞内 (arXiv: 2605.17404)
    96|    20|  - 核心要点: 随机短环元素到对数单位格的L2 CVP距离收敛到 pi/(2*sqrt(6))*sqrt(n)
    97|    21|  - **Activation**: module lattice security, post-quantum cryptography, 模格安全
    98|    22|
    99|    23|### A Uniform Random-Lattice Tail Bound for the SVP Kissing-Profile Parameter
   100|    24|- [[svp-lattice-tail-bound]] (enhanced) - SVP算法格子参数概率保证：Haar随机格尾界 (arXiv: 2605.21966)
   101|    25|  - 核心要点: 证明gamma(L)等于2的o(n)次方对Haar-Siegel随机格以高概率成立
   102|    26|  - **Activation**: SVP algorithm, lattice tail bound, shortest vector problem, Rogers mean value
   103|    27|
   104|    28|### Statistical Quantum Phase Estimation: Extensions and Practical Considerations
- [[statistical-quantum-phase-estimation]] - 统计量子相位估计扩展：支持负Pauli权重的随机编译 + 变点检测替代重叠估计 + Fourier对称性2x采样缩减 (arXiv: 2605.18876)
  - 核心：广义LCU随机编译支持负权重，无需预先估计trial/ground overlap下界
  - 变点检测方法直接从CDF跳跃确定基态能量，消除重叠估计瓶颈
  - Fourier级数对称性利用：在保持GSE精度的同时减少50%电路运行次数
  - Qiskit量子模拟器数值验证，适用于早期容错量子计算机
  - **Activation**: statistical QPE, SQPE, ground state energy, changepoint detection, LCU compilation, negative Pauli weights, Fourier symmetry, 统计量子相位估计

### Quantum Sufficiency for Self-Adjoint Statistical Models
- [[quantum-sufficiency-statistical-models]] - 量子充分性理论：实Jordan代数框架下的自伴统计模型，统一处理普通量子统计与局部量子统计结构 (arXiv: 2604.23292)
  - 平方根似然比和对称对数导数自然涌现为基本自伴似然型对象
  - 充分实正映射与充分实*-子代数、充分实Jordan代数的对应关系
  - 最小充分实*-子代数由似然比集和ρ模不变性刻画
  - 分离充分性的似然比方面与真正的量子模方面
  - **Activation**: quantum sufficiency, Jordan algebra, likelihood ratio, self-adjoint models, statistical quantum theory, 量子充分性

### Quantum State Isomorphism Problems for Groups
- [[quantum-state-isomorphism-groups]] - 量子态同构问题计算复杂性：纯态版本对所有非平凡群均为BQP-hard，属于QCMA∩QCSZK (arXiv: 2605.12615)
  - 量子态版Hidden Shift Problem：判定两个量子态是否通过群作用相关
  - 纯态BQP-hard + QCMA∩QCSZK包含，混合态QIP(2)-complete
  - 为量子密码学和量子态认证提供复杂性基础
  - **Activation**: quantum state isomorphism, hidden shift problem, BQP-hard, QCMA, QCSZK, quantum complexity, 量子态同构

### Parity of Parts and Excludant Statistics in Partitions and Quantum Modular Forms
- [[quantum-modular-forms-partitions]] - 分拆中的奇偶性与排除统计：生成函数与Ramanujan量子模形式的关联 (arXiv: 2603.13915)
  - q级数变换揭示分拆统计与Ramanujan的σ(q)、σ*(q)及Andrews的v2(q)的关系
  - Tauberian方法获得序列渐近公式
  - 连接组合数论与量子模形式的桥梁
  - **Activation**: partition statistics, quantum modular forms, Ramanujan, q-series, Tauberian method, 分拆统计, 量子模形式

### Quantum statistical mechanics: Gauge invariance, operator shifting, hyperdensity functionals, and nonequilibrium sum rules
- [[quantum-statistical-mechanics-gauge]] - 量子统计力学的规范不变性框架：移位超算子建立精确求和规则，量子超密度泛函理论 (arXiv: 2605.26650)
  - 核心：移位超算子实现规范变换，可观测量的平均值在热平衡和非平衡态下均保持不变
  - 规范不变性导出连接全局可观测量与局域关联函数的精确求和规则
  - 量子超密度泛函理论提供对超力和一般平均量子观测量的形式化访问
  - **Activation**: quantum statistical mechanics, gauge invariance, operator shifting, hyperdensity functional, sum rules, nonequilibrium quantum, many-body physics, 量子统计力学, 规范不变性, 算子移位

## 2026-05-28 - Systems Engineering + Quantum (Cron Job)
   105|    29|
   106|    30|### QuCtrl-BELL: A Compiler-Driven Sub-Microsecond Feedback Control Stack for Scalable Trapped-Ion Quantum Experiments
   107|    31|- [[quctrl-bell-compiler-quantum-control]] - 编译器驱动量子控制栈方法论：六阶段转译管道实现亚微秒级反馈控制 (arXiv: 2605.22433)
   108|    32|  - 控制流与硬件状态解耦，Python DSL → 六阶段编译 → 确定性硬件程序
   109|    33|  - 跨板同步协议支持 <700ns 反馈延迟，无需主机干预
   110|    34|  - **Activation**: compiler quantum control, QuCtrl-BELL, sub-microsecond feedback, trapped-ion control, quantum DSL
   111|    35|
   112|    36|### Adaptive Reinforcement Learning for Robust Open Quantum System Control
   113|    37|- 多任务 SAC 强化学习框架：51 种哈密顿量变体下的鲁棒量子控制 (arXiv: 2605.26925)
   114|    38|  - RIM 分析揭示 SAC 策略对脉冲扰动和退相干变异的鲁棒性优于 GRAPE
   115|    39|  - **Activation**: adaptive quantum control, SAC RL, robustness measure, open quantum systems
   116|    40|
   117|    41|### Toward General Quantum Control with Physics-Informed LLMs (VF-QCTRL)
   118|    42|- 物理信息 LLM 量子控制框架：符号推理 + 优化反馈循环 (arXiv: 2605.26021)
   119|    43|  - QCTRL-BENCH 16 任务基准测试，训练-free 通用量子控制
   120|    44|  - **Activation**: physics-informed LLM, VF-QCTRL, QCTRL-BENCH, analytic control ansatz
   121|    45|
   122|    46|### Scaling Quantum Optimization for Unit Commitment via Pauli Correlation Encoding
   123|    47|- Pauli 相关编码优化：大规模组合优化的量子-经典混合方案 (arXiv: 2605.17145)
   124|    48|  - Leader-follower 架构，312 二进制变量仅需 ~30 量子比特
   125|    49|  - **Activation**: Pauli Correlation Encoding, PCE QUBO, leader-follower optimization, unit commitment
   126|    50|
   127|    51|