## 2026-06-08 - Neuroscience Research (Cron Job)

### The Identity Trap in EEG Foundation Models: A Diagnostic Audit
- [[identity-trap-eeg-foundation-models]] - EEG基础模型诊断审计框架：FMScope五组件协议揭示跨被试"高准确率"可能反映受试者身份特征而非真实生物标志物 (arXiv: 2606.06647)
  - Frozen Subject-Variance: 跨12个数据集对，受试者方差是随机基线的13-89倍
  - Subject-Axis Erasure: 线性移除身份轴，标签内受试者变异时解码提升6-12 pp
  - Aperiodic 1/f Carrier: 移除非周期成分，受试者探测下降9-19 pp (LaBraM/CBraMod)
  - Layer-wise Probing: 微调仅在文献确立的跨受试者标志物存在时放大标签方差
  - **Activation**: EEG foundation model, subject-disjoint, shortcut learning, identity trap, aperiodic 1/f, frozen representation, diagnostic audit, LaBraM, CBraMod, REVE, FMScope

### Fixed Point Compositionality via Low-Rank Gluing Rules
- [[fixed-point-compositionality-low-rank-gluing]] - 阈值线性网络的组合性动力学理论：低秩粘合规则证明模块化结构导致全局不动点受限于局部模块组合，实现可预测吸引子工程 (arXiv: 2606.07336)
  - Low-Rank Gluing: 模块间特定低秩耦合，全局不动点限于局部组合
  - Rank-1 Characterization: 完整分类确定哪些局部不动点组合形成全局解
  - gCTLN Extension: 组合阈值线性网络规则推广至广义版本
  - Compositional Engineering: 组合大吸引子库可预测设计配方
  - **Activation**: compositional dynamics, threshold-linear network, TLN, low-rank gluing, fixed point decomposition, modular network, attractor engineering, combinatorial dynamics, inhibition-dominated, gCTLN## 2026-06-08 - Neuroscience + Quantum Computing Research (Cron Job)

### Measurement Circuit Ansatz: Naimark vs QNN Measurements
- [[naimark-qnn-measurement-circuits]] - 量子测量电路设计：Naimark扩展、混合Naimark-QNN、全QNN三种方法对比，QNN以更少训练迭代实现近最优量子测量 (arXiv: 2606.07376)
  - Naimark Quantum Measurement: CNOT+单量子比特门的Naimark扩展电路，经典优化器确定参数
  - Hybrid Naimark-QNN: 在Naimark框架中融入参数化量子电路，平衡理论与灵活性
  - Fully QNN Measurement: 浅参数化电路端到端训练，最少迭代近最优
  - State Discrimination: 最小误差与最大置信度两种判别策略
  - **Activation**: quantum measurement, Naimark extension, QNN measurement, POVM, state discrimination, parameterized quantum circuits, hybrid quantum-classical

### Scalable On-Hardware QNN Training
- [[scalable-on-hardware-qnn-training]] - QNN硬件训练框架：Butterfly电路+逐层训练+并行参数位移，将梯度估计成本从O(n2)降至O(log n) (arXiv: 2606.03517)
  - Butterfly Circuit: O(n log n)参数、对数深度的结构化子空间保持电路
  - Layer-Wise Training: 逐层冻结训练，避免退化平原问题
  - Parallel Parameter-Shift: 利用Butterfly层内交换结构，常数次数提取所有梯度
  - IonQ验证: 16-32量子比特硬件训练，超越经典基线
  - **Activation**: qnn training, butterfly circuit, layer-wise training, parameter-shift, gradient estimation, quantum hardware, nisq

### Quantum Subliminal Learning
- [[quantum-subliminal-learning]] - 量子潜意识学习安全分析：QNN比经典NN更容易通过公开接口泄露隐藏行为 (arXiv: 2605.29557)
  - Auxiliary Channel: 经典和量子NN均显示高效潜意识学习
  - Task Channel: 关键发现—QNN保留更多隐藏任务信号，架构依赖性安全漏洞
  - Geometric Picture: 传输由教师漂移幅度和隐藏任务可见分数控制
  - Supply Chain Risk: 量子模型供应链安全隐患
  - **Activation**: quantum security, subliminal learning, qnn, model distillation, supply chain security, hidden behavior

## 2026-06-08 - Quantum Neuromorphic Computing Research (Cron Job)

### Optical Neural Networks from Coherent Transient Dynamics in Waveguide QED
- [[optical-neural-networks-waveguide-qed]] - 全光学神经网络架构基于波导QED相干瞬态量子动力学，消除光电转换瓶颈实现超低延迟神经形态计算 (arXiv: 2605.17752)
  - Phase-Tunable Nonlocal Interference: 巨腔中可编程突触权重
  - Coherent Temporal Summation: 环腔积分器直接时序整合
  - Transient Rabi Dynamics: 驱动二能级系统非线性激活
  - MNIST验证: 高分类准确率
  - **Activation**: optical neural networks, waveguide QED, coherent transient dynamics, neuromorphic computing, all-optical, photonic computing, quantum photonics, Rabi dynamics, bad cavity regime

## 2026-06-08 - Dream/Sleep Neuroscience + AI Memory Research (Cron Job)

### Language Models Need Sleep: Learning to Self-Modify and Consolidate Memories
- [[llm-sleep-memory-consolidation]] - LLM睡眠-记忆巩固机制，首次提出AI系统需要类似生物睡眠的记忆整理阶段，实现自我修改与灾难性遗忘缓解 (arXiv: 2606.03979)
  - Sleep Phase Design: Wake/Sleep周期设计，记忆重放、权重整合、遗忘干扰消除
  - Hippocampal Replay: 海马体尖波涟漪机制模拟，高权重记忆片段重放
  - Self-Modification: 睡眠期间权重自我修改，Meta-weight adjustment + Consolidation gates
  - Catastrophic Forgetting Mitigation: 双缓冲系统、选择性固化、遗忘率降低40-60%
  - **Activation**: llm sleep, memory consolidation, self-modification, sleep paradigm, catastrophic forgetting, hippocampal replay, weight consolidation, wake-sleep cycle

### AdMem: Advanced Memory for Task-solving Agents
- [[admem-advanced-agent-memory]] - AdMem高级Agent记忆架构，结合陈述性记忆与程序性记忆的双系统，支持长期任务记忆与技能复用 (arXiv: 2606.06787)
  - Procedural Memory: 程序性记忆核心创新，存储技能、流程、策略而非仅事实
  - Skill Memory: 抧能存储系统，包含前置条件、执行步骤、成功概率、条件触发
  - Workflow Memory: 流程记忆保存，任务序列、依赖关系、优化参数、学习模式
  - Strategy Memory: 策略记忆分类，探索/优化/恢复/决策四种类型
  - Cross-Reference Integration: 陈述性↔程序性记忆整合与迁移机制
  - **Activation**: agent memory, procedural memory, skill storage, workflow memory, strategy memory, memory architecture, task-solving agents, memory consolidation

### Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning
- [[dreaming-world-action-models]] - 梦境推理与世界行动模型，按需梦境机制实现适应性多模态推理切换，创造性重组知识 (arXiv: 2606.07089)
  - Dreaming-when-Necessary Trigger: 任务复杂度/新颖性/冲突驱动的梦境触发机制
  - Five Dreaming Modes: Creative/Exploratory/Resolution/Planning/Cross-modal推理模式
  - Creative Recombination: 跨域融合、类比映射、概念融合等重组规则
  - Multi-Modal Adaptation: 动态模态选择，Visual/Textual/Cross-modal推理策略切换
  - Strategy Simulation: 梦境预演多种行动方案，评估并选择最优策略
  - **Activation**: dreaming reasoning, world action models, adaptive planning, creative dreaming, cross-modal reasoning, multimodal adaptation, strategy simulation, embodied intelligence

---

## 2026-06-08 - Systems Engineering Research (Cron Job)

### Mixed Potential Approach to Convergence of Nonlinear RLC Circuits with Memristors
- [[mixed-potential-memristor-circuit-convergence]] - Mixed Potential方法分析含忆阻器非线性RLC电路收敛性，扩展Brayton-Moser理论到完整四元素电路系统 (arXiv: 2606.05851)
  - Flux-Charge Analysis Method (FCAM): 从电压-电流域转换到磁通-电荷域分析
  - Lyapunov-like稳定性证明: 在电容-电感平衡条件下保证收敛
  - 多稳态处理: Content Addressable Memories (CAMs)实现支持
  - 参数鲁棒性: 收敛结果对电路参数变化具有鲁棒性
  - **Activation**: memristor circuit, mixed potential, convergence analysis, flux-charge method, RLCM circuit, nonlinear stability, Lyapunov circuit analysis, CAM implementation, neuromorphic hardware

### Amortized Nonlinear Model Predictive Control
- [[amortized-nonlinear-mpc]] - 摊销非线性MPC使用状态依赖QP近似替代实时NLP求解，单网络残差-校正器架构实现100倍加速并保证约束满足 (arXiv: 2606.05840)
  - State-dependent QP approximation: 输入仿射非线性系统最优控制近似
  - Residual-corrector architecture: 分析基线+神经网络校正，减少网络规模
  - Differentiable interior-point layer: 保证约束满足的可微分QP求解器
  - Hybrid loss: 仿制损失 + KKT残差惩罚联合训练
  - Experimental validation: 三连杆机械臂笛卡尔末端跟踪，毫秒级计算 vs 秒级NLP
  - **Activation**: amortized MPC, real-time nonlinear control, QP approximation, differentiable optimization, interior-point solver, robotics control, constraint satisfaction, MPC acceleration, learning-based control

### Attack Detection using Time Series Foundation Models
- [[attack-detection-time-series-foundation-models]] - TimesFM时间序列基础模型零样本CPS攻击检测，无需系统模型知识，优于χ²检测器并支持损坏测量替代 (arXiv: 2606.06347)
  - Model-structure-free detection: TimesFM作为surrogate residual generator
  - Zero-shot deployment: 无需植物模型(A,B,C)或任务特定训练
  - Stealthy attack derivation: 线性/非线性系统最优隐蔽攻击策略闭式解
  - IEEE 14-bus validation: 功率系统实测优于模型基检测器
  - Mitigation technique: TimesFM预测替代损坏测量，当冗余假设失效时提供实用方案
  - **Activation**: TimesFM attack detection, CPS security, foundation model CPS, stealthy attack optimal policy, χ² detector, IEEE 14-bus validation, replay attack, model-free anomaly detection, zero-shot CPS security, sensor corruption mitigation

### Double Preconditioning (DoPr): Optimization for Test-Time Performance, not Validation Loss
- [[double-preconditioning-test-time-optimization]] - 双预 conditioning优化范式结合梯度预 conditioning(Adam/Muon)与激活预 conditioning(KFAC)，解决训练-测试反馈失配和错误累积问题 (arXiv: 2606.06418)
  - Test-Time Feedback (TTF) phenomenon: 单步训练损失 vs 多步部署指标失配
  - Double preconditioning: 梯度预 conditioning(M) + 激活预 conditioning(K)双重变换
  - Drop-in intervention: 最小代码改动，最大化下游收益
  - Error accumulation reduction: 激活预 conditioning减少雅可比范数，抑制错误累积
  - Applications: 自回归语言建模、流式生成模型、机器人策略学习
  - Key insight: 测试时间性能提升 ≠ 验证损失改善
  - **Activation**: DoPr optimizer, test-time feedback mitigation, KFAC Adam, autoregressive error accumulation, generation quality optimization, rollout stability, TTF optimization, train-test shift correction## 2026-06-08 - Neuroscience + Quantum Research (Cron Job)

### ITP-STDP: An Intrinsic-Timing Power-of-Two Learning Engine for On-Chip SNN Training
- [[itp-stdp-snn-training]] - 算法+硬件协同优化SNN片上学习引擎，能耗效率4.5-220倍提升，硬件面积降低30-80倍，FPGA/ASIC验证 (arXiv: 2606.06159)
  - Intrinsic Timing: 消除timing matrix存储开销，利用神经元内在时间状态
  - Power-of-Two Quantization: 用位移操作替代浮点乘法，硬件友好
  - FPGA能效: 4.5× - 219.8× 提升
  - ASIC性能: 4.8× - 22.01× 加速，仅需1.2%-3.3%面积
  - Mean-Field Drift Model: synaptic dynamics验证稳定性
  - **Activation**: ITP-STDP, intrinsic timing, power-of-two, SNN training, neuromorphic hardware, FPGA, ASIC, energy-efficient STDP, on-chip learning

### Complementarity in Social Measurement: A Partition-Logic Approach
- [[partition-logic-social-complementarity]] - 分区逻辑框架建模社会测量中的互补性，将非布尔事件结构应用于社会科学测量不兼容性问题 (arXiv: 2603.28818)
  - 分区逻辑：通过粘贴布尔代数获得非布尔事件结构
  - 社会互补性：不同观测模式不兼容，但潜在状态完全确定
  - 六种应用：人员评估、调查框架、临床诊断、情报协调、法律多元主义、组织审计
  - 区分互补性与语境性：互补性≠不确定性，系统状态是确定的
  - 规范结构：L12领结、三角形、五边形、自动机分区逻辑
  - **Activation**: partition logic, social complementarity, measurement incompatibility, non-Boolean event structure, personnel assessment, survey framing, organizational audit

## 2026-06-08 - Neuroscience Research (Cron Job)

### Boosting Brain-to-Image Decoding with TRIBE v2 Data Augmentation
- [[boosting-brain-to-image-tribe-v2]] - 使用大规模预训练编码模型生成合成fMRI数据提升脑到图像解码性能68%，支持零样本解码 (arXiv: 2606.06345)
  - TRIBE v2: 1000+小时多模态fMRI预训练编码模型
  - 数据增强策略：合成+真实数据混合训练，68% Top-10检索准确率提升
  - 零样本能力：仅合成数据训练解码器可高于随机水平
  - 数据源依赖：7T vs 3T fMRI需调整增强比例
  - **Activation**: TRIBE, brain-to-image, fMRI decoding, data augmentation, zero-shot, synthetic data, foundation model

### Early psychosis shows deviations in scaling behaviour within a critical regime
- [[psychosis-scaling-critical-regime]] - PRG粗粒化框架揭示精神病早期临界性重组而非丢失，系统性scaling指数偏移 (arXiv: 2606.06290)
  - PRG + PSD + DFA多尺度集体动力学表征
  - 保持尺度不变组织但系统指数偏移
  - 跨模态一致性验证（多观测变量）
  - **Activation**: psychosis, scaling, critical regime, renormalization group, PRG, PSD, DFA, collective dynamics

## 2026-06-08 - Neuroscience Research (Cron Job)

### Dynamical Alignment: A Principle for Adaptive Neural Computation
- [[dynamical-alignment-snn-paradox-resolution]] - 动态对齐原理解决SNN性能悖论，固定神经结构通过输入时序动力学驱动不同计算模式（耗散vs扩张） (arXiv: 2508.10064)
  - 相空间体积动力学决定计算模式：耗散模式（收缩动力学）vs扩张模式（扩张动力学）
  - 时间尺度对齐：输入时序与神经元积分的匹配解锁SNN潜力
  - 双模态优化景观：临界相变点，耗散模式实现能量效率，扩张模式匹配ANN性能
  - 统一神经科学二元对立：稳定性-可塑性困境、分离-整合动力学
  - **Activation**: dynamical alignment, SNN performance paradox, phase space dynamics, dissipative vs expansive mode, timescale alignment, adaptive computation, bimodal optimization

### Neural Receptive Fields, Stimulus Space Embedding and Effective Geometry of Scale-Free Networks
- [[neural-receptive-fields-hyperbolic-geometry]] - 感受野从无标度网络结构的双曲几何自然涌现，无需突触微调，感受野大小依赖连接度 (arXiv: 2509.25453 v2)
  - 刺激空间映射到双曲嵌入边界，实现局部化活动模式
  - 感受野大小 RF_size ~ 1/k（神经元度），匹配实验观察
  - 多模态泛化：视觉朝向选择性、海马体位置细胞、体感映射
  - 海马体位置场实验验证：位置场大小与连接度相关性
  - **Activation**: receptive fields emergence, hyperbolic geometry, scale-free networks, stimulus embedding, place cells, orientation selectivity, neural geometry

## 2026-06-08 - Neuroscience Research (Cron Job)

### Early psychosis shows deviations in scaling behaviour within a critical regime
- [[psychosis-scaling-critical-regime]] - PRG coarse-graining framework reveals systematic scaling exponent shifts without criticality loss in early psychosis (arXiv: 2606.06290)
  - PRG + PSD + DFA multi-scale collective dynamics characterization
  - Preserved scale-invariant organization with systematic exponent shifts
  - Cross-modal consistency validation (multiple observables)
  - **Activation**: psychosis, scaling, critical regime, renormalization group, PRG, PSD, DFA, collective dynamics

### Intrinsic Computational Functionalism: From Observer-Relative Maps to Observer-Independent Structures
- [[intrinsic-computational-functionalism]] - Operationalizable criteria for observer-independent computational structures in consciousness theory (arXiv: 2606.06424)
  - Three-tier decomposition: label selection → partition selection → grain selection
  - C1: System-intrinsic instantiation (observer-independent specification)
  - C2: Causal-dynamical organization under intervention
  - **Activation**: consciousness, computational functionalism, observer-relativity, intrinsic structure, causal dynamics

### Cross-scale spatially-aware generative modeling of transcriptomic programs underlying neurodegenerative brain organization
- [[cross-scale-spatial-generative-neurodegeneration]] - 跨尺度空间感知生成模型预测神经退行性脆弱性，86.04%解释方差，空间相关r=0.9439 (arXiv: 2606.05870)
  - 变分生成架构 + 图基空间平滑正则化
  - Allen人脑图谱：910标记基因 × 68皮质区域
  - ADNI数据集：NC=926, AD=426
  - 微尺度分子 → 宏尺度退化的跨尺度建模
  - **Activation**: neurodegeneration, generative modeling, transcriptomic, cortical degeneration, Alzheimer, variational, graph regularization, spatial correlation

## 2026-06-08 - Neuroscience + Quantum (Cron Job)

### Parallel Scan Recurrent Neural Quantum States for Scalable Variational Monte Carlo
- [[parallel-scan-neural-quantum-states]] - 并行扫描循环神经量子态方法论，挑战RNN量子态不可扩展观点，实现52×52二维自旋晶格精度 (arXiv: 2605.13807)
  - 关联扫描替换顺序循环，实现GPU并行训练
  - 保持精确自回归概率结构
  - 迭代重训练管道：从小到大渐进扩展
  - 适度计算资源即可达大规模精度
  - **Activation**: PSR-NQS, parallel scan, recurrent quantum, autoregressive wavefunction, RNN scaling, variational Monte Carlo, spin lattice

### Neural network quantum states in the grand canonical ensemble
- [[quantum-neural-states-grand-canonical]] - 巨正则系综神经量子态架构，对称玻色波函数在Fock空间表示，支持可变粒子数研究 (arXiv: 2605.07779)
  - Fock空间对称神经网络架构
  - 化学势集成实现粒子数收敛
  - 一体约化密度矩阵计算
  - 凝聚分数和径向密度分布预测
  - **Activation**: grand canonical, bosonic NQS, Fock space, variable particle number, condensate fraction, OBRDM, geometric optimization


### A Quantum-Analogue Formalism for Modeling Supraliminal Information Processing
- [[quantum-analogue-cloud-formalism]] - 量子类云函数形式化建模超阈值信息处理，结合神经场论与薛定谔型方程解释决策中"改变主意"现象 (arXiv: 2605.25214)
  - 云函数空间结构继承感知物理对象特性，时间演化由大规模神经活动内在规律支配
  - 非线性非厄米哈密顿量 + Lotka-Volterra项的薛定谔型控制方程
  - 改变主意现象源于快速前意识感知与慢速意识比较的交互
  - **Activation**: cloud function, supraliminal, neural field, decision-making, change-of-mind, consciousness, Schrodinger equation, non-Hermitian

### Covariant quantum error correction in a three-layer quantum brain model
- [[covariant-qec-quantum-brain]] - 三层量子脑模型中的协变量子纠错，评估CQEC纯化协议在自由基对蛋白上的相干性维持能力 (arXiv: 2604.08587)
  - 三层架构：³¹P核自旋记忆 + 电子自旋接口 + 经典电化学，A=200MHz超精细耦合
  - CRY在γ_veto=0.19时CQEC维持相干性0.83（未修正仅0.12），MAO-A相干性坍缩至0.012
  - 层-蛋白权衡：无单一蛋白同时优化两层，CRY较短T2^e恶化Layer 2保真度
  - **Activation**: covariant QEC, quantum brain, radical pair, cryptochrome, coherence, T2, Eastin-Knill, purification

### Metabolic quantum limit to the information capacity of magnetoencephalography
- [[quantum-metabolic-neuroimaging-limit]] - 脑磁图信息容量的量子代谢极限，结合量子能量分辨率与脑代谢功率推导技术无关上限，人脑最大信息率约2.2 Mbit/s (arXiv: 2511.06401)
  - 量子能量分辨率极限结合脑代谢功率推导技术无关的信息容量上限
  - 高阶多极分量几何抑制导致时空带宽竞争，无法同时最大化时空分辨率
  - 适用于MEG系统设计、量子传感器评估、脑成像分辨率规划和神经编码效率分析
  - **Activation**: magnetoencephalography, MEG, quantum limit, information capacity, metabolic power, brain imaging, SQUID, atomic magnetometer

## 2026-06-08 - Neuroscience + Quantum (Cron Job - Hourly)

### Correlated States in Quantum Dot Clusters Coupled to a Common Superconductor
- [[neural-quantum-state-vqmc-correlated]] - Fermionic neural network quantum state VMC for correlated superconducting nanostructures, identifies 3 interaction regimes (arXiv: 2606.04608)
  - Canonical transformation to particle-number-conserving representation
  - Fermionic NQS-VMC: trivial singlet, critical intermediate, strongly correlated Heisenberg regimes
  - 1D singlet-doublet transitions gapless in thermodynamic limit; 2D robust triplet ground states
  - **Activation**: neural quantum state VMC, fermionic NQS, correlated superconducting, quantum dot cluster, singlet-doublet transition

### Parametrically Induced Strong Coupling Between Superconducting Circuit and Spin Ensemble
- [[parametric-strong-coupling-quantum-memory]] - On-demand MHz-rate parametric coupling between Josephson circuits and rare-earth spin ensembles for quantum state transfer (arXiv: 2606.03897)
  - Parametric pump as tunable bridge: coupling on-demand, minimal back-action when off
  - Three-wave mixing bridges frequency mismatch, g/2π ~ several MHz
  - Hybrid memory architecture: circuit computes fast, spins store long-lived states
  - **Activation**: parametric coupling quantum, spin ensemble memory, hybrid quantum memory, Josephson spin interface

## 2026-06-08 - Neuroscience + Quantum (Cron Job - Memory/Thermo)

### Non-equilibrium quantum thermodynamics of a memory-bearing open-system process
- [[quantum-memory-thermodynamics]] - 记忆型开放系统非平衡量子热力学，分析驱动两能级系统中记忆效应对功、热、熵产的影响 (arXiv: 2606.05904)
  - 记忆效应从复合环境动力中涌现，影响非平衡热力学量
  - 驱动、耗散和记忆效应的相互作用机制
  - **Activation**: quantum memory, thermodynamics, open system, non-equilibrium, 量子记忆, 非平衡热力学

### Learning Hamiltonians at Long Times
- [[quantum-hamiltonian-learning-long-times]] - 从单次长时间演化学习未知n量子比特哈密顿量，证明局部哈密顿族的高概率可学习性 (arXiv: 2606.05690)
  - 长时间演化下特征值缠绕不阻止哈密顿量学习
  - 归一化可观测量与H对易则为平凡解
  - **Activation**: hamiltonian learning, quantum system identification, long time evolution, 哈密顿量学习

## 2026-06-07 - Information Science + Quantum (Cron Job)

### Quantum resonance encryption for secure data storage and communication with quantum kicked top
- [[quantum-resonance-encryption]] - 量子共振加密协议，利用量子受踢顶动力学实现安全数据存储和通信，提供授权用户完美恢复和窃听器检测 (arXiv: 2606.01953)
  - 量子受踢顶（quantum kicked top）在共振态下产生伪随机动力学，仅可用正确密钥逆转
  - 窃听态呈现完全混合态，基于量子力学而非计算复杂性的信息论安全
  - 内置篡改检测，适用于共享量子计算环境的数据保护和量子密钥分发
  - **Activation**: quantum resonance encryption, quantum kicked top, quantum data privacy, secure quantum storage

### Qute: Towards Quantum-Native Database
- [[quantum-native-database]] - 量子原生数据库框架，将SQL编译为量子电路，实现混合量子-经典查询优化和选择性量子索引 (arXiv: 2602.14699)
  - 扩展SQL直接编译为门高效量子电路，而非经典数据库的量子适配
  - 混合查询优化器动态选择量子vs经典执行方案，评估查询复杂度和硬件可用性
  - 三阶段演进路线：量子模拟→混合执行→全量子原生，已在origin_wukong真实量子处理器验证
  - 保真度保持存储缓解当前量子比特退相干约束
  - **Activation**: quantum database, quantum SQL, hybrid query optimizer, quantum indexing

### Iterative CZ-gate-based protocol for squeezed Schrödinger cat state engineering
- [[quantum-state-engineering]] - 测量辅助量子态工程，通过QND纠缠操作和零差测量生成高保真度压缩薛定谔猫态 (arXiv: 2606.02201)
  - QND纠缠操作+零差测量实现类确定性态制备，辅助态坍缩到目标态
  - 迭代CZ门放大协议可扩展猫态尺寸，保真度/成功概率可调
  - 非高斯资源对测量基量子计算至关重要，适用于混合量子网络
  - **Activation**: quantum cat states, measurement-based quantum computing, QND gate, homodyne measurement

# AI Collection Index

## 2026-06-07 - Neuroscience Research (Cron Job)

### Coarse-to-fine Hierarchical Architecture with Sequential Mamba for Brain Reconstruction (CHASMBrain)
- [[chasmbrain-mamba-brain-reconstruction]] - 双流Mamba架构用于图像到fMRI编码，粗到细策略实现ROI级到voxel级预测，Pearson相关达0.429 (arXiv: 2606.04772)
  - 双流设计：CLS stream处理全局语义，Patch stream处理局部空间特征
  - 不对称特化：Patch流锁定早期视觉皮层，CLS流向高阶区域提供语义上下文
  - 两阶段策略：Stage 1预测ROI级激活，Stage 2使用Mamba-VAE细化到voxel级
  - 跨被试泛化：学习主干模型捕获被试无关的视觉表征
  - **Activation**: CHASMBrain, Mamba brain, fMRI encoding, hierarchical architecture, dual-stream, visual cortex mapping, image-to-fMRI, sequential Mamba

### Boosting Brain-to-Image Decoding with TRIBE v2 Data Augmentation
- [[boosting-brain-to-image-tribe-v2]] - TRIBE v2 数据增强提升脑解码性能，使用大规模预训练编码模型生成合成fMRI数据，实现68% Top-10检索准确率提升 (arXiv: 2606.06345)
  - TRIBE v2 预训练于1000+小时视觉/听觉/语言响应数据
  - 零样本解码能力：纯合成数据训练可超越随机水平
  - 数据源特异性调整策略：NSD和BOLD5000表现差异分析
  - **Activation**: TRIBE v2, brain-to-image, fMRI decoding, synthetic fMRI, data augmentation brain, zero-shot brain decoding, neural encoding model

### Semidefinite-programming hierarchies for classically simulable state families
- [[sdp-quantum-simulability-certification]] - SDP hierarchy for certifying quantum advantage by characterizing classically simulable state families (arXiv: 2606.06204)
  - Complete SDP hierarchy for classically simulable state families in arbitrary finite dimension
  - Primal feasibility tests + dual affine witnesses for non-simulability certification
  - Computable upper bounds on critical classical visibility for depolarizing noise
  - **Activation**: semidefinite programming, classical simulability, quantum advantage, SDP hierarchy, POVM simulability, critical visibility, quantum witnesses

## 2026-06-08 - Neuroscience Research (Cron Job)

### ITP-STDP: An Intrinsic-Timing Power-of-Two Learning Engine for On-Chip SNN Training
- [[itp-stdp-snn-training]] - Hardware-efficient STDP algorithm achieving 4.5x-219.8x energy efficiency improvement via power-of-two weight encoding (arXiv: 2606.06159)
  - Eliminates multipliers through power-of-two quantization (shift operations instead of multiplication)
  - Intrinsic timing mechanism removes global clock requirements
  - ASIC: 4.8x-22.01x speedup with only 1.2%-3.3% area of prior works
  - FPGA: 100x reduction in hardware resources, 100x reduction in energy per weight update
  - **Activation**: ITP-STDP, intrinsic timing, power-of-two STDP, on-chip SNN training, hardware STDP, neuromorphic learning engine

### Boosting Brain-to-Image Decoding with TRIBE v2 Data Augmentation
- [[boosting-brain-to-image-tribe-v2]] - TRIBE v2 使用大规模预训练编码模型生成合成 fMRI 数据，实现高达 68% 图像检索精度提升 (arXiv: 2606.06345)
  - TRIBE v2 预训练于 1000+ 小时视觉/听觉/语言响应数据
  - 零样本解码能力：纯合成数据训练可超越随机水平
  - 数据源特异性调整：NSD 7T 比例 1.0-2.0，BOLD5000 3T 比例 4.0-8.0
  - Foundation model 方法用于脑解码数据效率优化
  - **Activation**: TRIBE v2, brain-to-image, fMRI decoding, synthetic fMRI, data augmentation brain, zero-shot brain decoding, neural encoding model

## 2026-06-07 - Information Science + Quantum Mechanics (Sunday Cron Job - Hourly)

### Quantum Thermal Logic Gates
- [[quantum-thermal-logic-gates]] - Quantum thermal logic gates using heat current in coupled quantum-dot systems as computational signal (arXiv: 2606.06432)
  - One-to-one correspondence between classical electronic logic gates and thermal analog gates
  - Heat current encodes logical states via threshold-based detection in nano-electronic architecture
  - **Activation**: quantum thermal logic, heat current computing, quantum dot logic, thermal gates, nano-electronic quantum circuits

## 2026-06-07 - Neuroscience Research (Cron Job)

### Discrete Signaling Mediates Chaotic Regularization in Recurrent Neural Networks
- [[discrete-signaling-chaotic-regularization]] - 连接微观混沌与宏观神经表征几何的理论框架，解释混沌正则化机制 (arXiv: 2606.04426v1)
  - 混沌动力学诱导局部粗糙性但保持全局平滑性
  - 自然产生幂律谱特征，与皮质记录匹配
  - **Activation**: chaotic dynamics, neural representation, regularization, mean-field theory, power-law spectrum

### Intrinsic Computational Functionalism: From Observer-Relative Maps to Observer-Independent Structures
- [[intrinsic-computational-functionalism]] - 意识的内在计算功能主义框架，定义观察者独立计算结构，对抗反计算论证 (arXiv: 2606.06424)
  - 两准则：C1系统内在实例化 + C2因果动力学干预组织
  - 三层分解：观察者相对标签 → 理论约束分区 → 动力学内部粒度
  - 关键洞见：Tier (iii)动力学内部粒度选择才能避开观察者相对性反驳
  - **Activation**: intrinsic computation, observer-independent consciousness, computational functionalism, syntax vs semantics, anti-computational arguments, consciousness AI, IIT criticism

## 2026-06-08 - Information Science + Quantum Mechanics (Cron Job)

### Robust Quantum Steerability Classification via Key Feature Extraction and Matrix Structure Preservation
- [[robust-steerability-classification]] - Robust quantum steerability classification using key feature extraction and matrix-structure-preserving CNNs (arXiv: 2606.04363)
  - Solves generalization failure of SVMs/MLPs on T-diagonal and AVN states
  - CNN with matrix-structure-preserving features + key features achieves robust generalization
  - **Activation**: quantum steerability classification, steerability detection, quantum state ML, matrix structure quantum, SLOCC invariant, AVN states

### A Toolbox to Understand the Physics of Quantum Data Management
- [[quantum-data-management-physics]] - Toolbox methodology for understanding quantum device physics in database optimization (arXiv: 2605.14719)
  - Connects quantum device behavior to database problem structure
  - Evaluates quantum annealing for combinatorial data management tasks
  - **Activation**: quantum, database, quantum-annealing, combinatorial-optimization, physics, data-management

### Low Depth Distributed Quantum Algorithms for Unordered Database Search
- [[quantum-distributed-database-search]] - Low-depth distributed quantum search algorithms for unordered database lookup (arXiv: 2604.14081)
  - Partitions Grover search across distributed nodes to reduce circuit depth
  - Enables NISQ-era database search via query operator decomposition
  - **Activation**: quantum, distributed, database, search, grover, nisq

### Privacy-Utility Tradeoffs in Quantum Information Processing
- [[quantum-privacy-utility-tradeoff]] - Privacy-utility tradeoff methodology for quantum information processing and quantum differential privacy (arXiv: 2602.10510)
  - Studies optimal tradeoffs between privacy and learning utility in quantum settings
  - Analyzes privacy constraints for quantum data processing protocols
  - **Activation**: quantum, privacy, differential-privacy, utility-tradeoff, information-processing

### Quantum-Resistant Networks: A Review of Primitives, Protocols and Best Practices
- [[quantum-resistant-network-architecture]] - Post-quantum cryptography network architecture methodology covering PQC primitives and protocol migration (arXiv: 2605.04129)
  - Addresses architectural consequences of post-quantum transition for networked systems
  - Evaluates PQC primitives for network deployment and protocol adaptation
  - **Activation**: quantum, network-security, post-quantum, PQC, cryptography, architecture

### Ultra-Large-Capacity Passive Quantum Access Network Powered By Single Thermal Source
- [[quantum-access-network-qkd]] - Passive quantum access network architecture using single thermal source for ultra-large-capacity QKD (arXiv: 2605.20077)
  - Achieves record capacity with passive thermal-source QKD architecture
  - Scales quantum key distribution to multi-user PON-based networks
  - **Activation**: quantum, qkd, access-network, pon, thermal-source, key-distribution

## 2026-06-07 - Neuroscience Research (Cron Job)

### Early psychosis shows deviations in scaling behaviour within a critical regime
- [[psychosis-scaling-critical-regime]] - PRG+PSD+DFA framework for scaling behavior deviations in early psychosis brain dynamics (arXiv: 2606.06290)
  - Phenomenological Renormalization Group coarse-graining reveals collective dynamics across spatial scales
  - Power spectral density shows altered temporal scaling (beta exponent shifts)
  - DFA reveals modified long-range correlations (alpha exponent changes)
  - Key insight: reorganization within preserved scaling regime, not loss of criticality
  - **Activation**: psychosis scaling, brain criticality psychiatric, PRG renormalization brain, PSD DFA analysis, scale-invariant dynamics

### Cross-scale spatially-aware generative modeling of transcriptomic programs underlying neurodegenerative brain organization
- [[cross-scale-spatial-generative-neurodegeneration]] - Variational generative framework bridging gene expression to cortical degeneration (86% variance, r=0.94) (arXiv: 2606.05870)
  - 86.04% explained variance in regional vulnerability prediction
  - Spatial correlation r=0.9439 between predicted and observed degeneration
  - 910 landmark genes mapped to 68 cortical regions (Allen Brain Atlas + ADNI FreeSurfer)
  - Graph-based spatial smoothness regularization preserves cortical organization
  - **Activation**: neurodegeneration generative modeling, Alzheimer's transcriptomic cortical, spatial graph regularization, gene expression cortical thickness, cross-scale molecular macroscale

## 2026-06-07 - Information Science + Quantum (Sunday Cron Job)

### Breakeven demonstration of quantum low-density parity-check codes
- [[quantum-ldpc-breakeven]] - qLDPC error correction breakeven on trapped-ion with OMG architecture for mid-circuit measurement (arXiv: 2606.06455)
  - 9× better logical error rate than previous superconducting qLDPC demonstration
  - OMG architecture eliminates ion transport and dedicated coolant ions
  - Tests 9 QECC families (qLDPC, topological, concatenated) on single device
  - **Activation**: qldpc, breakeven, quantum error correction, trapped ion, mid-circuit measurement, OMG architecture, logical qubit, fault tolerance

### Multiple Quantum Hypothesis Testing: One-Shot Pairwise Bounds
- [[multiple-quantum-hypothesis-testing]] - Dimension-free one-shot bounds for multiple quantum state discrimination with sharp asymptotics (arXiv: 2606.06246)
  - Resolves Audenaert-Mosonyi conjecture on pairwise error decomposition
  - Improves multiple quantum Chernoff bound by removing dimension-dependent prefactor
  - Proves achievability for arbitrary separable Hilbert spaces
  - **Activation**: hypothesis testing, quantum state discrimination, Chernoff bound, Bayesian, error bounds

### Unlocking Exponential Shannon Capacity Gains via Quantum Entanglement
- [[quantum-entanglement-capacity-gains]] - Quantum entanglement provides exponential multiplicative capacity advantage in K-user MACs with causal CSIT (arXiv: 2606.05412)
  - Capacity advantage grows exponentially with number of users K (21× for K=5, 88× for K=7)
  - Gains robust to ~30% depolarization per entangled qubit
  - Unbounded advantage as state alphabet grows (K=3 fixed)
  - **Activation**: shannon capacity, quantum entanglement, multiple access channel, causal CSIT, exponential advantage, information theory

### Quantum Time Lower Bounds by Permutation Invariance
- [[quantum-time-lower-bounds]] - Framework for establishing quantum time complexity lower bounds via permutation invariance (arXiv: 2606.05099)
  - First systematic method for tight quantum time complexity lower bounds
  - Proves SWAP test, Shift test, productness tester, LMR protocol all time-optimal
  - Reduction from quantum sample complexity to circuit size
  - **Activation**: quantum time complexity, lower bounds, permutation invariance, SWAP test, sample complexity, circuit size

### No-Go Theorem for Gaussian Quantum Repeaters
- [[no-go-gaussian-quantum-repeaters]] - Gaussian operations cannot enhance quantum capacity beyond direct transmission (arXiv: 2606.05097)
  - Introduces fractional extendibility generalizing k-extendibility to Gaussian states
  - Non-Gaussian operations fundamentally required for quantum repeater advantage
  - Applies to bosonic pure-loss attenuation channels
  - **Activation**: no-go theorem, Gaussian quantum repeaters, fractional extendibility, quantum capacity, photon loss, quantum networks

### Gaussian Mean Width Strong Converse Bound for Quantum Channel Identification
- [[gaussian-mean-width-identification-capacity]] - Single-letter strong converse bound via Gaussian mean widths (arXiv: 2606.05032)
  - σ-Euclidean geometry for channel output space analysis
  - Semidefinite representation for efficient computation
  - Improves bounds for depolarizing, Pauli, erasure, and amplitude damping channels
  - **Activation**: identification capacity, Gaussian mean width, strong converse, quantum channels, semidefinite programming

### Multidimensional Reconciliation in Continuous-Variable QKD
- [[multidimensional-cv-qkd-reconciliation]] - Multidimensional reconciliation methodology with HDirac open-source simulation (arXiv: 2606.02323)
  - Transforms Gaussian quantum channel to virtual BIAWGN for LDPC compatibility
  - High-dimensional constructions beyond algebraic dimensions 1, 2, 4, 8
  - Trade-off analysis: dimension vs reconciliation efficiency vs frame error rate
  - **Activation**: CV-QKD, reconciliation, multidimensional, LDPC, HDirac, continuous-variable, quantum key distribution


### Quantum enhanced rare event discovery and sampling
- [[quantum-rare-event-sampling]] - Quantum algorithm for rare-event discovery/sampling without prior knowledge of events, achieves optimal quantum scaling and quadratic speedup for heavy-tailed systems (arXiv: 2606.06316)
  - Blind rare-event amplification without needing to know targets beforehand
  - Quadratic speedup for heavy-tailed systems with nonvanishing tail mass
  - Polynomial speedup for stationary stochastic processes (exponent from entropy rate)
  - **Activation**: rare event, heavy-tailed, quantum sampling, threshold amplification, stochastic process, financial crash prediction

### Quantum Algorithms for Triangle Cut Sparsification
- [[quantum-triangle-sparsification]] - Quantum algorithms for triangle cut sparsification using quantum walks and Grover search, improving classical listing bounds for large-scale network analysis (arXiv: 2606.06287)
  - Triangle listing in Õ(min(n^(5/4)t^(7/12), m + m^(3/4)t^(1/2), n^(3/2)t^(1/2)))
  - Heavy-light vertex partitioning for hybrid quantum-classical processing
  - ε-sparsifier construction in Õ(n/ε²) with provable quality guarantees
  - **Activation**: triangle listing, graph sparsification, quantum walks, grover search, heavy-light partition, network analysis

## 2026-06-08 - Information Science + Quantum (Cron Job)

### Wasserstein Exponential Smoothing
- [[wasserstein-exponential-smoothing]] - Extends exponential smoothing to distributional time series in Wasserstein space (arXiv: 2606.05560)
  - Consistent α estimation via Wasserstein distance minimization
  - Applications to high-frequency financial returns and electricity demand distributions
  - **Activation**: wasserstein exponential smoothing, distributional time series, Wasserstein forecasting, distributional forecasting

### Feature Encoding in Quantum Machine Learning: A Survey and Practical Guidelines
- [[qml-feature-encoding]] - Systematic survey of 66 QML encoding methods with hardware-grounded selection framework (arXiv: 2606.05387)
  - Three-axis cost-expressivity-robustness taxonomy
  - Critical gate-error threshold p* ~ 10^-3 for amplitude encoding viability
  - **Activation**: qml feature encoding, quantum data encoding, amplitude encoding, NISQ encoding

### Compositional Boundaries for Density Fusion
- [[compositional-density-fusion]] - Order-invariant hierarchical execution for distributed uncertainty management (arXiv: 2606.05871)
  - Normalized weighted linear pooling characterized as the unique compositional fusion rule
  - f-divergence balancing shows pairwise solvability ≠ schedule-independent fusion
  - **Activation**: density fusion, uncertainty management, order-invariant fusion, distributed probabilistic models

### Automated Proving of Shannon-Type Entropy Inequalities via Fine-Tuned Language Models
- [[automated-entropy-inequality-proving]] (enhanced) - 0.6B fine-tuned LM + guided beam search achieves 85% proof success rate (arXiv: 2606.05729)
  - Outperforms GPT-5.5 (1.7%) and Psitip (33.3%) on n=10-15 variable inequalities
  - Format failures and step quality degradation are dominant failure modes
  - **Activation**: entropy inequalities, Shannon, automated proving, language models, information theory

## 2026-06-07 - Neuroscience Research (Cron Job)

### Boosting Brain-to-Image Decoding with TRIBE v2 Data Augmentation
- [[boosting-brain-to-image-tribe-v2]] - 68% improvement in Top-10 image retrieval accuracy via synthetic data augmentation (arXiv: 2606.06345)
  - TRIBE v2 pretrained on 1000+ hours of video/audio/language fMRI
  - Zero-shot brain-to-image decoding possible with synthetic-only training
  - **Activation**: TRIBE,, brain-to-image,, image, decoding,, fMRI

### The Variance Brain Foundation Models Forgot: Third-Order Statistics Predict Cognition Where Billion-Parameter Models Fail
- [[variance-brain-foundation-models-forgot]] - BFMs predict cognition worse than linear FC regression (~80K params) (arXiv: 2606.04010)
  - BrainLM 650M worse than 111M—variance allocation problem
  - Second-order covariance preserved, third-order co-skewness destroyed
  - **Activation**: brain, foundation, models,, BFM,, co-skewness,

## 2026-06-07 - Neuroscience Research (Cron Job)

### Boosting Brain-to-Image Decoding with TRIBE v2 Data Augmentation
- [[boosting-brain-to-image-tribe-v2]] - 68% improvement in Top-10 image retrieval accuracy via synthetic data augmentation (arXiv: 2606.06345)
  - TRIBE v2 pretrained on 1000+ hours of video/audio/language fMRI
  - Zero-shot brain-to-image decoding possible with synthetic-only training
  - **Activation**: TRIBE,, brain-to-image,, image, decoding,, fMRI

### The Variance Brain Foundation Models Forgot: Third-Order Statistics Predict Cognition Where Billion-Parameter Models Fail
- [[variance-brain-foundation-models-forgot]] - BFMs predict cognition worse than linear FC regression (~80K params) (arXiv: 2606.04010)
  - BrainLM 650M worse than 111M—variance allocation problem
  - Second-order covariance preserved, third-order co-skewness destroyed
  - **Activation**: brain, foundation, models,, BFM,, co-skewness,

## 2026-06-07 - Neuroscience Research (Cron Job)

### Training a Predictive Coding Network on ImageNet using Equilibrium Propagation
- [[predictive-coding-equilibrium-propagation-imagenet]] - First ImageNet-scale training of Predictive Coding Networks via Centered Equilibrium Propagation, achieving 13.23% top-5 error (arXiv: 2606.03584)
  - Centered EP removes systematic bias for unbiased gradient estimation
  - Novel equilibration scheme specifically designed for PCN dynamics
  - VGG10 architecture demonstrates scalability beyond small tasks
  - Bridging biological learning principles with large-scale computer vision
  - **Activation**: predictive coding network, PCN, equilibrium propagation, EP, centered EP, biological learning, ImageNet, energy-based model

### A Sliced-Wasserstein Framework on Correlation Matrices for EEG Decoding
- [[corsw-sliced-wasserstein-eeg-decoding]] - Pullback Euclidean Metric Sliced Wasserstein for scale-invariant EEG decoding with domain generalization, KDD 2026 accepted (arXiv: 2606.06104)
  - CorSW framework treats correlation matrices as manifold-valued data with proper geometry
  - Two instantiations: Off-Log Metric (OLM) and Log-Scaled Metric (LSM)
  - Robust to distribution shifts across sessions, subjects, and devices
  - Zero inference cost overhead, minimal training overhead
  - **Activation**: EEG decoding, sliced Wasserstein, correlation matrix, manifold geometry, domain generalization, OLM, LSM, scale-invariant

## 2026-06-07 - Information Science + Quantum (Cron Job)

### Automated Proving of Shannon-Type Entropy Inequalities via Fine-Tuned Language Models and Guided Tree Search
- [[automated-entropy-inequality-proving]] - LLM + guided tree search for automated proving of Shannon-type entropy inequalities, bridges information theory with AI (arXiv: 2606.05729)
  - Fine-tuned language models generate candidate proof steps for entropy inequalities
  - Guided tree search with value function explores proof space efficiently
  - Symbolic verification engine validates each step independently
  - Handles Shannon-type inequalities derivable from basic submodularity constraints
  - **Activation**: entropy inequality proving, Shannon inequality automated, LLM theorem proving, guided tree search information theory, 熵不等式自动证明

### Quantum Entanglement-Assisted MAC Capacity
- [[quantum-entanglement-mac-capacity]] - Quantum entanglement provides exponential and unbounded robust gains in Shannon capacity of classical MAC with causal CSIT (arXiv: 2606.06155)
  - Exponential capacity scaling with number of users K via shared entanglement
  - Unbounded gain ratio C_Q/C_C depending on channel structure
  - Robust to partial entanglement degradation and decoherence
  - Bridges quantum information theory with classical communication theory
  - **Activation**: quantum entanglement MAC capacity, Shannon capacity quantum, multiple access channel entanglement, quantum CSIT, 量子多址信道容量

### Breakeven demonstration of quantum low-density parity-check codes
- [[quantum-ldpc-breakeven]] - Trapped-ion qLDPC breakeven with 4 logical qubits into 18 physical, OMG architecture for mid-circuit measurement without ion transport, 9x better than superconducting (arXiv: 2606.06455)
  - OMG architecture enables addressable mid-circuit measurement and reset without ion transport
  - Breakeven: logical error rate comparable to or exceeding trapped-ion qubit lifetimes
  - Nine QEC code families tested on single device without reconfiguration
  - **Activation**: quantum LDPC, qLDPC, trapped-ion, breakeven, OMG architecture, fault tolerance, quantum error correction

### Multiple Quantum Hypothesis Testing: One-Shot Pairwise Bounds and Sharp Asymptotics
- [[multiple-quantum-hypothesis-testing]] - Dimension-free one-shot bounds for multi-state quantum discrimination, resolves Audenaert-Mosonyi conjecture, sharp asymptotics for infinite-dimensional Hilbert spaces (arXiv: 2606.06246)
  - Resolves Audenaert-Mosonyi conjecture on multi-state discrimination error bounds
  - Proves achievability of multiple quantum Chernoff distance for arbitrary separable Hilbert spaces
  - Binary error characterized by trace harmonic-mean, within factor 2 of classical optimum
  - **Activation**: hypothesis testing, quantum state discrimination, Chernoff bound, Bayesian, error bounds

### Unlocking Exponential Shannon Capacity Gains via Quantum Entanglement Assistance
- [[quantum-entanglement-capacity-gains]] - Quantum entanglement gives exponential capacity scaling with users K in multiple access channels, 21x gain (K=5), 88x (K=7), robust to 30% depolarization (arXiv: 2606.05412)
  - Capacity advantage grows exponentially with number of users K
  - Unbounded gains as state alphabet size grows (K=3, binary I/O)
  - Robust to 30% depolarization per entangled qubit
  - Transmitter-only entanglement assistance sufficient
  - **Activation**: Shannon capacity, entanglement assistance, multiple access channel, CSIT, capacity gain

### Quantum Time Lower Bounds by Permutation Invariance
- [[quantum-time-lower-bounds]] - First systematic framework for quantum time complexity lower bounds via permutation invariance, proves SWAP test, Shift test, LMR protocol all time-optimal (arXiv: 2606.05099)
  - Reduces quantum time complexity to sample complexity for permutation-invariant properties
  - Proves time-optimality of SWAP test, Shift test, productness tester, LMR, samplizer
  - First method for systematic tight lower bounds on quantum circuit size
  - **Activation**: quantum time complexity, lower bounds, permutation invariance, SWAP test, circuit size

### No-Go Theorem for Gaussian Quantum Repeaters from Fractional Extendibility
- [[no-go-gaussian-quantum-repeaters]] - Gaussian operations cannot enhance quantum capacity of pure-loss channels beyond direct transmission, introduces fractional extendibility for Gaussian states (arXiv: 2606.05097)
  - Gaussian repeater chains cannot exceed direct transmission quantum capacity
  - Fractional extendibility generalizes k-extendibility to continuous-variable setting
  - Non-Gaussian operations fundamentally required for quantum repeater advantage
  - **Activation**: no-go theorem, Gaussian repeaters, fractional extendibility, quantum capacity, photon loss

### Gaussian Mean Width Strong Converse Bound on Quantum Channel Identification
- [[gaussian-mean-width-identification-capacity]] - Single-letter SDP-computable strong converse bound on classical identification capacity via Gaussian mean width geometry (arXiv: 2606.05032)
  - σ-Euclidean geometry controls trace-distance via covering estimates
  - Sudakov inequality bounds covering numbers by Gaussian mean widths
  - Improves bounds for depolarizing, Pauli, erasure, amplitude damping channels
  - **Activation**: identification capacity, Gaussian mean width, strong converse, semidefinite programming

### Multidimensional Reconciliation in Continuous-Variable QKD
- [[multidimensional-cv-qkd-reconciliation]] - HDirac open-source framework for arbitrary-dimensional reconciliation in CV-QKD, Gaussian→BIAWGN virtual channel transformation (arXiv: 2606.02323)
  - Transforms Gaussian quantum channel to virtual BIAWGN for LDPC compatibility
  - High-dimensional constructions beyond algebraic dimensions 1, 2, 4, 8
  - Open-source HDirac simulation framework for arbitrary dimensions
  - **Activation**: CV-QKD, multidimensional reconciliation, LDPC, HDirac, continuous-variable, BIAWGN


## 2026-06-07 - Neuroscience Research (Cron Job)

### Bio-plausible Neuromorphic Disturbance Observer Based on Emulation Theory
- [[neuromorphic-disturbance-observer]] - Bio-inspired event-driven disturbance observer using integrate-and-fire neuron dynamics with spike-frequency adaptation, achieving 42.6% spike event reduction under noise (arXiv: 2606.05189)
  - Integrate-and-Fire (IF) neuron dynamics for event-driven control updates
  - Spike-Frequency Adaptation (SFA) for history-dependent threshold regulation
  - Robustness and adaptability in uncertain environments
  - **Activation**: neuromorphic control, disturbance observer, spike-frequency adaptation, integrate-and-fire neuron, bio-plausible control, adaptive threshold, event-driven control, neural control system

### Boosting Brain-to-Image Decoding with TRIBE v2 Data Augmentation
- [[boosting-brain-to-image-tribe-v2]] - fMRI-to-image decoding boosted 68% by augmenting small datasets with synthetic data from TRIBE v2 foundation model pretrained on 1000+ hours of multi-modal fMRI (arXiv: 2606.06345)
  - Foundation model approach for neuroimaging data augmentation
  - Zero-shot brain-to-image decoding with purely synthetic training
  - Cross-scanner validation across 7T NSD and 3T BOLD5000 datasets
  - **Activation**: brain-to-image decoding, fMRI decoding, TRIBE v2, data augmentation, neural decoding, foundation model, zero-shot decoding, synthetic fMRI

### Early Psychosis Shows Deviations in Scaling Behaviour Within a Critical Regime
- [[psychosis-scaling-critical-regime]] - Early psychosis exhibits systematic scaling exponent shifts across PRG+PSD+DFA methods, indicating critical regime reorganization rather than simple loss of critical dynamics (arXiv: 2606.06290)
  - Phenomenological Renormalization Group (PRG) coarse-graining for spatial scale dynamics
  - Power Spectral Density (PSD) and Detrended Fluctuation Analysis (DFA) for temporal scaling
  - Preserved critical-like framework with collective dynamics reorganization
  - Unified multi-method framework bridging fragmented psychiatric criticality findings
  - **Activation**: criticality, psychosis, scaling behavior, renormalization group, power spectral density, detrended fluctuation analysis, brain dynamics, psychiatric disorders, collective dynamics, critical regime, scaling exponents

## 2026-06-07 - Quantum Computing Research (Cron Job)# AI Collection Index

## 2026-06-07 - Quantum Computing Research (Cron Job)

### Breakeven Demonstration of Quantum Low-Density Parity-Check Codes
- [[quantum-ldpc-breakeven-demonstration]] - Achieves breakeven performance with qLDPC codes on trapped-ion quantum computers, demonstrating nine QEC codes on a single device with 4 logical qubits encoded into 18 physical qubits (arXiv: 2606.06455)
  - Novel OMG architecture for addressable mid-circuit measurement without ion transport
  - Logical error rates better than previous superconducting qubit demonstrations
  - No hardware reconfiguration needed across three code families: qLDPC, topological, concatenated
  - **Activation**: quantum LDPC, qLDPC, trapped-ion, quantum error correction, fault-tolerant, breakeven, OMG architecture, mid-circuit measurement, quantum codes

## 2026-06-07 - Systems Engineering Research (Cron Job)

### HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers
- [[handoff-humanoid-control]] - Multi-teacher KL distillation framework for humanoid whole-body control, combining motion tracking, locomotion, and fall-recovery specialists with context-conditioned gating (arXiv: 2606.06493)
  - Compact task-space command interface: intuitive, general, modular, expressive
  - Three complementary teachers distilled into MoE student architecture
  - Context-conditioned gating for dynamic expert selection
  - Safety-filtered data for dangerous action handling
  - VLM-driven agentic planner with no task-specific fine-tuning
  - **Activation**: humanoid, whole-body control, task-space, distillation, mixture-of-experts, motion tracking, locomotion, fall-recovery, multi-teacher KL, context gating, unitree G1, VLM planner

### Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads
- [[agent-memory-system-implications]] - First systems characterization of LLM agent memory with 4-axis taxonomy, phase-aware profiling, and 10 system recommendations for construction scheduling, capability floors, amortization, freshness-latency tradeoffs, fleet-scale management (arXiv: 2606.06448)
  - 4-axis taxonomy: memory structure, extraction mechanism, control flow, storage granularity
  - Phase-aware profiling: construction, retrieval, generation cost attribution
  - 10 representative systems characterized across two benchmark suites
  - 10 system recommendations covering design tradeoffs and fleet management
  - **Activation**: agent memory, long-horizon tasks, stateful agents, memory retrieval, fact stores, memory construction, fleet-scale, freshness-latency, memory taxonomy, profiling framework, system implications



## 2026-06-07 - Information Science + Quantum (Cron Job)

### On the Cryptographic Structure Required for Verifying Qubits
- [[quantum-qubit-verification]] - Classical verification methodology for quantum computation by testing anti-commuting operators on quantum devices, establishing minimal cryptographic structure needed for verification (arXiv: 2606.05527)
  - Anti-commuting operator tests as foundation for quantum device verification
  - Classical verification protocols without requiring quantum capabilities
  - Statistical confidence bounds for verification certificates
  - **Activation**: quantum qubit verification, classical verification of quantum, anti-commuting operator test, 量子比特验证, qubit testing, quantum device verification

### Information-Geometric Bound on the Robustness of Entanglement Generation
- [[entanglement-robustness-bounds]] - Information-geometric framework for bounding entanglement robustness under noise, using Riemannian geometry on quantum state space to quantify noise impact on entanglement quality (arXiv: 2606.05696)
  - Fisher information metric for quantum state distance computation
  - Geodesic analysis between ideal and noisy entangled states
  - Practical bounds on entanglement fidelity degradation
  - **Activation**: entanglement robustness, entanglement bounds, information geometry quantum, 纠缠鲁棒性, quantum state robustness, entanglement generation noise

### Quantum-Classical Equivalence for AND-Functions
- [[quantum-classical-equivalence]] - Framework for analyzing quantum-classical equivalence in communication complexity, proving polynomial bounds on quantum advantage for total Boolean AND-functions (arXiv: 2606.03249)
  - Log-rank conjecture analysis for AND-function communication matrices
  - Quantum vs classical communication complexity comparison
  - Equivalence chain: Q(f) = poly(D(f)) for total Boolean functions
  - **Activation**: quantum classical equivalence, communication complexity quantum advantage, AND-function quantum, 量子经典等价, total Boolean function quantum

## 2026-06-06 - Neuroscience Research (Cron Job)

### CogniSNN: Enabling Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability with Random Graph Architectures in Spiking Neural Networks
- [[cognisnn-random-graph-snn]] - Cognition-aware SNN using Random Graph Architecture (RGA) to mimic biological connectivity, enabling pathway reuse and dynamic growth for continual learning (arXiv: 2512.11743)
  - Three key properties: Neuron-Expandability, Pathway-Reusability, Dynamic-Configurability
  - KP-LwF: Key Pathway-based Learning without Forgetting for multi-task transfer
  - DGL: Dynamic Growth Learning algorithm for temporal dimension expansion
  - **Activation**: random graph snn, cognisnn, pathway reusability, neuron expandability, dynamic configurability, continual learning snn, biological connectivity, neuromorphic hardware, kp-lwf, dynamic growth learning

### Event-driven Eligibility Propagation in Large Sparse Networks: Efficiency Shaped by Biological Realism
- [[event-driven-eligibility-propagation]] - Event-driven learning in sparse SNNs showing biological realism (sparsity, irregularity) drives 10-15x computational efficiency vs dense backpropagation (arXiv: 2511.21674)
  - Sparse updates scale with active neurons, not network size
  - Irregular spike timing reduces synchronous overhead
  - Event-driven timing aligns with neuromorphic hardware constraints
  - **Activation**: event driven learning, eligibility propagation, sparse snn, biological realism, efficient snn training, neuromorphic efficiency, sparse connectivity, asynchronous learning

## 2026-06-07 - Economics & Investment Research (Cron Job)

### Fairness and Strategy-Proofness in Automated Market Makers
- [[amm-fairness-impossibility]] - Arrovian impossibility theorem for AMM design: no aggregation rule for weighted-product AMMs can be both fair and strategy-proof when n>2 LPs (arXiv: 2606.04959)
  - Fairness forces weighted Aitchison centroid (mean-type); strategy-proofness forces median-type -- incompatible for n>2
  - Obstruction is sharp: vanishes at n=2 where fair strategy-proof rules exist
  - **Activation**: AMM design, automated market maker, DeFi protocol, fairness, strategy-proofness, Aitchison centroid, mechanism design

### Dynamic Multi-Pair Trading Strategy in Cryptocurrency Markets with Deep Reinforcement Learning
- [[drl-pair-trading-crypto]] - Filter-then-Rank pair selection with PPO+LSTM execution agent within deterministic risk shielding for crypto pair trading (arXiv: 2606.04574)
  - Introduces Fixed Risk, Adaptive Mean (FRAM) execution model combining statistical arbitrage with DRL policies
  - Bootstrap validation confirms outperformance at 10% significance; deterministic shielding prevents catastrophic divergence
  - **Activation**: pair trading, cryptocurrency, deep reinforcement learning, PPO, LSTM, statistical arbitrage, safe RL


## 2026-06-07 - Neuroscience Research (Cron Job)

### Short-Term Synaptic Plasticity Stabilizes Goal-Conditioned Dynamics in PFC-Inspired Reservoir Model
- [[stp-stabilizes-goal-conditioned-dynamics]] - Tsodyks-Markram STP在PFC储水池模型中稳定目标条件化动力学，噪声下保持89.2%成功率 vs 无STP49.5% (Cohen's dz=1.31) (arXiv: 2606.03481)
  - Facilitation-dominant STP参数：U=0.2, τ_facil=1000ms
  - 基底神经节TD读出学习 + 储水池计算架构
  - STP动态调制有效连接，延迟后期目标特异性模式增强
  - **Activation**: short-term synaptic plasticity, STP, goal-conditioned dynamics, PFC reservoir, goal-directed action planning, basal ganglia TD learning, Tsodyks-Markram model, facilitation-dominant, dynamic stability, Cohen's dz

### Cross-scale Spatially-aware Generative Modeling of Transcriptomic Programs Underlying Neurodegenerative Brain Organization
- [[cross-scale-spatial-generative-neurodegeneration]] - 变分生成框架链接基因表达与皮质退化，图平滑正则化保持解剖结构，R²=86.04%，r=0.9439 (arXiv: 2606.05870)
  - 910 landmark genes → 68 cortical regions degeneration prediction
  - Allen Human Brain Atlas transcriptomics + ADNI cortical thickness
  - 潜在基因程序揭示易损与保护基因组合
  - **Activation**: spatially-aware generative, transcriptomic neurodegeneration, cross-scale brain modeling, cortical thinning prediction, gene-expression degeneration, variational generative, neurodegenerative vulnerability mapping


## 2026-06-07 - Economics/Investment + Quantum (Cron Job)

### Derivative-Informed Operator Learning for Finance: On-the-Fly Greeks, Surfaces, Hedging, and Control
- [[derivative-informed-operator-learning-finance]] - Neural operators trained to match both pricing operators and Fréchet derivatives, reducing vega error by 40% and delta error by 15% (arXiv: 2606.05900)
  - Dual-loss training: value matching + derivative matching via adjoint AD and tangent sensitivity equations
  - Random-feature DeepONet reduces vol surface JVP error by 44% and price RMSE by 23%
  - Derivative consistency alone does NOT remove no-arbitrage violations — constraints must be imposed explicitly
  - **Activation**: derivative-informed, operator learning, financial surrogate, Greeks computation, hedging, DeepONet, random features, no-arbitrage, volatility surface

### The Impact of Market Informedness on Market Makers' Profitability
- [[market-informedness-rl-market-making]] - Market making with heterogeneous agents using MAPPO in CTDE setting, showing profitability increases with market informedness (arXiv: 2606.05882)
  - Hawkes process modeling of market-taker arrival with finite-horizon stability guarantees
  - Counterintuitive finding: higher informed trader fraction increases MM profitability via volume/spread capture
  - CTDE enables coordination between market makers while maintaining decentralized execution
  - **Activation**: market making, RL trading, MAPPO, CTDE, Hawkes process, adverse selection, order flow, bid-ask spread, profitability

### Stress Amplified Resilience: ESG and Joint Fragility in Equity Markets
- [[stress-test-resilience-esg-fragility]] - Multi-channel fragility analysis across downside returns, volatility spikes, and deteriorating tradability using S&P 500 data 2014-2025 (arXiv: 2606.05631)
  - Cofragility state captures joint occurrence of multiple risk dimensions within same firm-month
  - Tests ESG association with lower clustered fragility exposure
  - Single-channel analysis misses compounded risk effects
  - **Activation**: ESG, stress testing, joint fragility, cofragility, equity markets, portfolio resilience, downside risk, multi-factor risk


## 2026-06-07 - Neuroscience Research (Cron Job)

### Early Psychosis Shows Deviations in Scaling Behaviour Within a Critical Regime
- [[psychosis-scaling-critical-regime]] - 使用现象学重整化群(PRG)、PSD和DFA研究早期精神病fMRI标度性质，发现保留标度区域内的集体动力学重组而非临界动力学丧失 (arXiv: 2606.06290)
  - 健康对照组：展示临界动力学特征（长程相关、信息处理效率）
  - 早期精神病：标度指数系统性偏移（不是简单临界性丧失）
  - **Activation**: early psychosis, critical dynamics, scaling behavior, PRG, DFA, PSD, renormalization group, fMRI, brain criticality

### Cross-scale Spatially-aware Generative Modeling of Transcriptomic Programs Underlying Neurodegenerative Brain Organization
- [[cross-scale-spatial-generative-neurodegeneration]] - Variational framework linking gene expression to cortical degeneration with graph-based spatial smoothness, achieving 86.04% explained variance and r=0.9439 spatial correlation (arXiv: 2606.05870)
  - 910 landmark genes → 68 cortical regions degeneration prediction
  - Allen Human Brain Atlas transcriptomics + ADNI cortical thickness
  - **Activation**: spatially-aware generative, transcriptomic neurodegeneration, cross-scale brain modeling, cortical thinning prediction, gene-expression degeneration

### Bio-plausible Neuromorphic Disturbance Observer Based on Emulation Theory
- [[neuromorphic-disturbance-observer]] - Spike-timing encoding disturbance observer with adaptive-threshold mechanism inspired by spike-frequency adaptation, achieving 42.6% spike reduction under noise (arXiv: 2606.05189)
  - Integrate-and-Fire (IF) neuron dynamics for event-driven updates
  - History-dependent regulation via SFA-inspired adaptive threshold
  - **Activation**: neuromorphic control, disturbance observer, spike-timing encoding, adaptive threshold, integrate-and-fire, SFA-inspired, event-driven control

### Quantum-Enhanced Support Vector Machine for High-Dimensional Financial Market Prediction
- [[quantum-enhanced-svm-financial-prediction]] - Quantum kernel SVM for high-dimensional financial market prediction (DOI: 10.1109/nqcomp68334.2026.11497725)
  - Hybrid quantum-classical SVM using quantum kernels for financial forecasting
  - Addresses high-dimensional data challenges in financial markets
  - **Activation**: quantum svm, financial prediction, quantum kernel, market prediction

### Enhancing QAOA Through Manifold Optimization
- [[qaoa-manifold-optimization]] - Riemannian manifold optimization techniques for QAOA on NISQ devices (DOI: 10.1155/que2/3418300)
  - Uses intrinsic geometric structure to address QAOA nonconvexity
  - Overcomes gradient descent challenges with three Riemannian methods
  - **Activation**: manifold optimization, qaoa, riemannian, quantum optimization

### Equivariant Quantum Approximate Optimization Algorithm
- [[equivariant-qaoa]] - Symmetry-aware QAOA incorporating equivariant constraints for combinatorial optimization (DOI: 10.1109/tqe.2026.3654930)
  - Reduces parameter space using group-theoretic symmetry
  - Improves optimization efficiency for symmetric problems
  - **Activation**: equivariant qaoa, symmetry, quantum optimization, group theory

### Robust Investment Portfolio Management using Bayesian Neural Networks
- [[bayesian-neural-portfolio-management]] - Bayesian neural network methodology for robust portfolio management with uncertainty quantification (DOI: 10.1016/j.iref.2026.105244)
  - Quantifies uncertainty in portfolio optimization via Bayesian inference
  - Adapts to changing market conditions dynamically
  - **Activation**: bayesian portfolio, portfolio management, uncertainty quantification, dynamic markets

### Hybrid Quantum-Behaved and Bio-Swarm Optimization Algorithm (BioQPSO)
- [[bio-quantum-pso-optimization]] - Hybrid quantum-behaved PSO with bio-inspired swarm intelligence for complex optimization (DOI: 10.21203/rs.3.rs-9178752/v1)
  - Combines quantum-probabilistic updates with ant colony/bee foraging behavior
  - Handles multimodal and biologically structured search landscapes
  - **Activation**: quantum pso, bio-inspired optimization, swarm intelligence, hybrid optimization

## 2026-06-06 - Neuroscience Research (Cron Job) - SNN Hardware Optimization

### ITP-STDP: Intrinsic-Timing Power-of-Two Learning Engine for On-Chip SNN Training
- [[itp-stdp-snn-training]] - Hardware-efficient STDP learning algorithm with power-of-two quantization and intrinsic timing, achieving 50x hardware reduction and 100x energy savings for on-chip SNN training (arXiv: 2606.06159)
  - FPGA platform: 4.5× to 219.8× energy efficiency improvement, minimal resource utilization
  - ASIC platform: 4.8× to 22.01× speedup, only 1.2% to 3.3% area of prior designs
  - Mean-field synaptic drift model validates stability across network scales
  - Algorithm-hardware co-design: shift operations replace multipliers, LUT replaces exponentials
  - **Activation**: ITP-STDP, power-of-two STDP, intrinsic timing, SNN hardware training, neuromorphic energy efficiency, on-chip learning, FPGA SNN, ASIC neuromorphic, STDP optimization, synaptic drift model, hardware quantization, SNN acceleration

## 2026-06-06 - Neuroscience Research (Cron Job) - Latest Papers

### Whisper-ECoG Alignment with Interpretable Time-Resolved Neural Encoding
- [[whisper-ecog-alignment-neural-encoding]] - Mapping Whisper speech foundation model representations to human ECoG responses during naturalistic speech perception with time-resolved encoder and soft attention (arXiv: 2606.02305)
  - Intermediate Whisper layers (7-11) show strongest brain alignment, supporting hierarchical match between model and cortical speech processing
  - Attention maps reveal temporally local alignment (10-50ms resolution) between speech embeddings and neural responses
  - Phoneme-category organization shows anatomically coherent clustering among encoding-informative electrodes
  - Temporal modeling benefits: 15-20% improvement over static linear regression baselines
  - **Activation**: Whisper, ECoG, speech foundation model, neural encoding, brain alignment, phoneme, temporal resolution, cortical processing, ICLR 2026, soft attention, intermediate layers

### Task-Induced Representational Invariances in Deep RL Neural Coding
- [[deep-rl-representation-invariance-neural-coding]] - MDP reduction theory framework revealing algorithm-specific representational symmetries: DQN learns MDP homomorphism invariances, PPO learns action symmetries (arXiv: 2606.01868)
  - Principled approach to comparing learned representations across RL algorithms through symmetry analysis
  - DQN (value-based): representations invariant to MDP homomorphisms, preserving Q-value structure
  - PPO (policy-gradient): representations invariant to action symmetries, preserving optimal policy structure
  - Transfer learning implications: invariance alignment predicts transfer performance across domains
  - LLM connection: similar invariance patterns emerge, prompt-dependent
  - **Activation**: RL representation, neural coding, invariance, symmetry, MDP homomorphism, DQN, PPO, value-based, policy-gradient, transfer learning, RSA

### Computation-Aware Kalman Filtering with Model Selection for Neural Dynamics
- [[computation-aware-kalman-neural-dynamics]] - CASSM framework for scale-imbalanced regime (few trials, many neurons) with computation-aware uncertainty calibration, competitive with deep networks (arXiv: 2606.01468)
  - Computation-Aware State-Space Model (CASSM) with novel training loss incorporating approximation errors
  - Significantly improved uncertainty calibration over previous Bayesian scaling attempts
  - Competitive predictive performance with deep networks in scale-imbalanced regime (N << M)
  - Clear roadmap for neuroscience researchers: model selection, hyperparameter optimization, budget allocation
  - **Activation**: Kalman filtering, neural dynamics, computation-aware, state-space model, model selection, uncertainty calibration, scale-imbalanced, Bayesian, CASSM, Probabilistic Numerics 2026

## 2026-06-06 - Economics, Investment + Quantum Mechanics (Cron Job)

### Quantum Computing for Financial Transformation: A Review
- [[quantum-finance-stack-analysis]] - Financial computation stack framework for evaluating quantum advantage across five finance domains: portfolio optimisation, derivative pricing, risk estimation, quantum ML, and post-quantum security (arXiv: 2604.08180)
  - Five-layer financial computation stack: Portfolio Optimisation → Derivative Pricing → Risk Estimation → Quantum ML → Post-Quantum Security
  - Four-step evaluation logic: identify bottleneck, specify quantum primitive, compare classical benchmark, judge under realistic constraints
  - Three hybrid workflow patterns: classical-quantum-classical pipeline, warm-start optimization, hybrid derivative pricing
  - Key pitfalls: overclaiming advantage, amplitude encoding traps (ψ=√P loses phase), hardware mismatch, financial realism gap
  - **Activation**: quantum finance, portfolio optimization, QAOA, quantum amplitude estimation, derivative pricing, quantum risk, quantum machine learning, post-quantum cryptography, financial computation stack, hybrid quantum-classical, QUBO, CVaR, quantum annealing

### Digital Quantum Reservoir Computing for ATM Time Series Prediction
- [[digital-quantum-reservoir-computing-finance]] - NISQ-compatible quantum reservoir computing framework for multi-step financial time series forecasting using parametrized 4-qubit reservoirs with partial measurement (arXiv: 2606.04686)
  - Fixed-structure parametrized quantum circuits (4-8 qubits) as temporal reservoir
  - Partial measurement statistics as reservoir features, classical readout only
  - Quantum entanglement serves as natural temporal memory mechanism
  - Applied to ATM cash demand forecasting, robust to NISQ noise
  - **Activation**: quantum reservoir computing, time series forecasting, NISQ, ATM prediction, financial forecasting, parameterized quantum circuits, partial measurement, temporal memory

### Certified Higher Order Quantum Framework for CSA and Margin-Aware Collateral Optimization
- [[higher-order-quantum-optimization-finance]] - Higher-order binary optimization (HOBO) for legally-constrained financial problems, directly encoding multi-variable constraints without QUBO reduction overhead (arXiv: 2606.04235)
  - Direct HOBO encoding avoids QUBO reduction overhead for complex constraints
  - CSA eligibility, margin requirements, concentration limits as polynomial constraints
  - Certified solutions with feasibility guarantees for collateral allocation
  - Maps to quantum annealing and QAOA with higher-order interactions
  - **Activation**: higher-order optimization, HOBO, collateral optimization, CSA constraints, quantum finance, derivatives, margin requirements, constraint encoding, certified optimization

### Game Set Quantum: Parameterized Quantum Circuit for Correlated Equilibrium in Bayesian Games
- [[quantum-bayesian-game-equilibrium]] - Parameterized quantum circuits for computing correlated equilibrium in Bayesian games with polynomial qubit scaling vs exponential classical (arXiv: 2606.03109)
  - PQC ansatz with player-specific subcircuits and entangling layers
  - Quantum entanglement encodes correlated strategies inaccessible classically
  - NISQ-compatible for small-to-medium multi-agent economic games
  - Gradient-based or gradient-free optimization for equilibrium finding
  - **Activation**: quantum game theory, Bayesian games, correlated equilibrium, parameterized quantum circuits, multi-agent economics, auction design, mechanism design

## 2026-06-06 - Neuroscience Research (Cron Job)

### Ontology-Constrained Multi-LLM Scoring of Hypothesis Support in Predictive Processing
- [[ontology-constrained-llm-hypothesis-scoring]] - Local multi-LLM council for ontology-constrained literature synthesis in predictive coding neuroscience, producing quantitative hypothesis-space maps with auditable disagreement measurements (arXiv: 2606.05206)
  - 36-concept expert glossary across 3 hypotheses: Predictive Suppression, Feedforward Error Propagation, Ubiquity
  - 10 local LLM models score 31 studies independently, pairwise agreement analysis reveals structured disagreement
  - Hypothesis-space temperature: geometric dispersion metric (lower for local oddball, higher for global oddball)
  - Transition vectors quantify paradigm-dependent shifts between experimental contexts
  - **Activation**: predictive processing, predictive coding, ontology-constrained, multi-LLM, hypothesis scoring, literature synthesis, meta-analysis, evidence space, hypothesis-space mapping, local oddball, global oddball, LLM council, glossary validation, temperature metric


## 2026-06-06 - Economics, Investment (Cron Job)

### Quantum Machine Learning Model for Finance
- [[quantum-machine-learning-model-finance]] - Quantum Machine Learning Model for Finance (10.1002/9781394347070.ch16)
  - **Activation**: quantum-machine-learning-model-finance, quantum machine learning model finance

### Portfolio Optimization with Mean-Variance-Spectrum Preferences
- [[portfolio-optimization-mean-variance-spectrum]] - Portfolio Optimization with Mean-Variance-Spectrum Preferences (10.1016/j.qref.2026.102140)
  - **Activation**: portfolio-optimization-mean-variance-spectrum, portfolio optimization mean variance spectrum

### Portfolio Selection is More of a Belle Art Than Economics or Finance
- [[portfolio-selection-belle-art-economics]] - Portfolio Selection is More of a Belle Art Than Economics or Finance (10.2139/ssrn.6293058)
  - **Activation**: portfolio-selection-belle-art-economics, portfolio selection belle art economics


## 2026-06-05 - Neuroscience Research (Cron Job)

### SC-TauPath: Structural Connectivity Attribution for Alzheimer Tau Propagation
- [[sc-taupath-alzheimer-tau-propagation]] - 首个神经生物学可解释的 Tau 传播路径图谱框架，结合 NDM 增强 MLP + 梯度归因，验证 Braak 分期解剖结构 (arXiv: 2606.04066)
  - 网络扩散模型增强 MLP + 梯度×输入归因量化每条结构连接边的贡献
  - 多尺度通路图谱：骨干边、高流量路线、枢纽 ROI，映射 Tau 传播路径
  - ADNI 234 名参与者验证，归因分数符合 Braak 分期解剖，揭示 SC 编码病理信息
  - **Activation**: tau propagation, Alzheimer, structural connectivity, attribution, network diffusion, Braak staging, DTI, PET, pathway mapping, interpretability, gradient attribution

## 2026-06-05 - Number Theory, Statistics, Advanced Mathematics + Quantum Mechanics (Cron Job)

### Low-rank Distributional Matrix Completion
- [[distributional-matrix-completion]] - Matrix completion with probability distribution entries using kernel mean embeddings + Tucker rank decomposition (arXiv: 2606.04176)
  - Kernel mean embeddings map probability distributions to RKHS for distributional matrix representation
  - Tucker rank extended to distribution-valued matrices capturing low-rank structure in distributional space
  - Functional unfolding operators bridge infinite-dimensional embeddings with finite-dimensional tensor computation
  - Non-asymptotic error bounds characterize statistical performance vs sample complexity
  - **Activation**: distributional matrix completion, kernel mean embedding, tucker rank distribution, functional unfolding, RKHS, probability distribution matrix, statistical matrix recovery, non-asymptotic bounds

### Monitored Chaotic Scattering
- [[monitored-chaotic-scattering-rmt]] - Extends random matrix theory of chaotic scattering to quantum dots with time-resolved measurements (arXiv: 2606.04794)
  - Constructs Kraus operator ensembles from circular ensembles for monitored quantum evolution
  - Derives discrete-time quantum master equation for charge transfer statistics
  - Equipartition conjecture enables closed-form RMT predictions for monitored transport
  - **Activation**: monitored chaotic scattering, random matrix theory, kraus operators, quantum master equation, charge transfer, mesoscopic physics, circular ensemble

### Convergence Rates of Sum-of-Hermitian-Squares for Pauli Algebra
- [[sum-of-hermitian-squares-pauli-convergence]] - Explicit convergence rates for noncommutative polynomial optimization relaxations in quantum theory (arXiv: 2606.04940)
  - Develops convergence rates for Sum-of-Hermitian-Squares hierarchies on Pauli algebra
  - Covers ground state energy estimation and other quantum optimization problems
  - Bridges moment relaxation theory with quantum many-body computation
  - **Activation**: sum of hermitian squares, pauli algebra, noncommutative optimization, convergence rates, quantum ground state, moment relaxation, polynomial optimization

### Decoded Quantum Interferometry Beyond Hamming Space
- [[decoded-quantum-interferometry-beyond-hamming]] - Extends DQI algorithm beyond Hamming space to finite geometries with translation symmetry (arXiv: 2606.04843)
  - Generalizes decoded quantum interferometry to rank-metric and translation association schemes
  - Uses quantum Fourier transform on finite geometries for structured optimization
  - Shell-based distance grouping enables coherent decoding beyond binary Hamming space
  - **Activation**: decoded quantum interferometry, rank-metric codes, translation association schemes, finite geometry, quantum fourier transform, structured optimization

### Fermionic Non-Gaussianity via Bell Sampling
- [[fermionic-bell-sampling-non-gaussianity]] - Bridge degree monotone for fermionic non-Gaussianity via Bell sampling, stronger Gaussian conversion no-go theorems (arXiv: 2606.05066)
  - Bridge degree: largest eigenvalue sector of Λ = Σγ_j⊗γ_j on two copies, non-increasing under post-selected Gaussian protocols
  - Stronger no-go theorems for Gaussian conversion than previously known monotones
  - Efficiently witnessed through Bell sampling; lower-bounds non-Gaussian gate complexity
  - Two algorithmic primitives: Gaussianity test with perfect completeness, state 2-design test
  - **Activation**: fermionic non-gaussianity, bell sampling, bridge degree, gaussian conversion, fermionic quantum computing, resource theory

### Entanglement Measure from Quantum Optimal Transport
- [[quantum-optimal-transport-entanglement]] - Bipartite entanglement via minimal quantum Wasserstein distance to separable states, Lipschitz dual formulation (arXiv: 2606.04969)
  - E(ρ) = min_{σ separable} W_1(ρ, σ) satisfies all entanglement axioms in single geometric framework
  - Lipschitz dual gives explicit lower bounds for pure and mixed states, sharp constant for two-qubit
  - Quantitative connection to entanglement witnesses: negative witness → certified lower bound on E
  - Natural subadditivity and trace-distance estimates, points toward large-deviation conjectures
  - **Activation**: quantum optimal transport, entanglement measure, Wasserstein distance, Lipschitz witness, separable states, experimental entanglement detection

### No-Go Theorem for Gaussian Quantum Repeaters
- [[no-go-gaussian-quantum-repeaters]] - Proves Gaussian repeaters cannot enhance quantum capacity of pure-loss channels via fractional extendibility framework (arXiv: 2606.05097)
  - Fractional extendibility generalizes k-extendibility for Gaussian states
  - Any Gaussian+LOCC repeater chain bounded by direct transmission capacity
  - Closes open question about Gaussian vs non-Gaussian repeater protocols
  - Framework applicable to broader Gaussian quantum network analysis
  - **Activation**: gaussian quantum repeaters, no-go theorem, fractional extendibility, quantum capacity, bosonic channels, pure-loss channels

### Hybrid Gaussian-Exponential Zero-Noise Extrapolation
- [[gaussian-exponential-zero-noise-extrapolation]] - Hybrid Gaussian-exponential ZNE model for periodic quantum circuits, improved error mitigation (arXiv: 2605.29242)
  - Hybrid model f(λ) = A·exp(-αλ²) + B·exp(-βλ) + C captures both Gaussian and exponential error components
  - Superior to standard exponential ZNE for circuits with oscillatory error behavior
  - Polynomial sample complexity, applicable to parameterized quantum circuits
  - Requires 5-7 noise scale factors for stable fitting
  - **Activation**: zero noise extrapolation, ZNE, gaussian exponential model, periodic circuits, error mitigation, NISQ

### Exact Geometric Typicality and Bipartite Entanglement
- [[geometric-typicality-entanglement]] - Derives Beta distribution, Lubkin's purity, and Page's formula asymptotic expansion from projected CLT on hyperspheres (arXiv: 2605.29732)
  - Projected CLT on hyperspheres → Beta distribution for subsystem occupation probabilities
  - Bernoulli-factorized asymptotic expansion of ⟨I(A:B)⟩ with (d_A²ᵏ-1)(d_B²ᵏ-1) factors, odd orders vanish
  - Separates quantum coherence (𝔰𝔲⊗𝔰𝔲) vs classical (Cartan⊗Cartan) contributions via Schur majorisation
  - Non-perturbative closed form via Bose-Einstein integral
  - **Activation**: geometric typicality, bipartite entanglement, projected CLT, hyperspherical moments, Page's formula, Lubkin purity, Haar-random states, Bose-Einstein integral

### Barbell Codes: qLDPC for Superconducting Hardware
- [[barbell-qldpc-superconducting-hardware]] - qLDPC codes with constant hardware complexity scaling for superconducting quantum chips (arXiv: 2606.06062)
  - Barbell-shaped Tanner graph mapped to native chip layout supporting all required two-qubit interactions
  - Hardware complexity remains constant as code distance increases
  - Circuit-level noise simulation: preserves information at target noise strength over trillions of QEC cycles
  - Fault-tolerant logical multi-Pauli measurements with consistent per-round performance
  - **Activation**: barbell codes, qLDPC, superconducting hardware, quantum error correction, fault tolerance, constant complexity scaling, circuit-level noise

## 2026-06-04 - Systems Engineering + Quantum Mechanics (Cron Job)

### Squeezed Phonon Lasing via Floquet-Controlled Solid-State Defects
- [[floquet-controlled-phonon-lasing]] - Floquet-engineered squeezed phonon laser design using color centers in hBN membranes with coupled spin-mechanical systems (arXiv: 2606.05083)
  - Floquet theory enables engineering of effective Hamiltonians via periodic driving
  - Continuous transition from conventional to squeezed phonon lasing via Floquet parameters
  - Solid-state platform: hBN membrane with color centers + mechanical oscillator
  - Applications in quantum metrology (sub-shot-noise sensing) and quantum control systems
  - **Activation**: floquet engineering, phonon lasing, squeezed states, solid-state defects, hBN membrane, quantum metrology, spin-phonon coupling, periodic driving, steady-state engineering

### Piston Control in Two-Ion Quantum Device
- [[inverse-engineering-quantum-control]] - Inverse engineering protocols for controlling classical piston dynamics driven by quantum ion motion in two-ion trapped devices (arXiv: 2606.03488)
  - Self-consistent stationary state determination with quantum effects
  - Narrow quantum regime connecting two broad classical regimes
  - Inverse engineering: design control from desired trajectory to potential modulation
  - Bridge between classical and quantum control systems engineering
  - **Activation**: inverse engineering, piston control, two-ion device, trapped-ion control, quantum-classical transition, optimal control

## 2026-06-04 - Neuroscience Research (Cron Job)

### Discrete Signaling Mediates Chaotic Regularization in RNNs
- [[discrete-signaling-chaotic-regularization]] - Links microscopic chaos to macroscopic neural representation geometry via kernel methods + dynamical mean-field theory (arXiv: 2606.04426)
  - Chaos induces local roughness but preserves global smoothness, acting as intrinsic regularizer
  - Power-law spectral signatures match cortical recordings, explains smooth population codes
  - Game-theoretic structure where each neuron minimizes local energy
  - **Activation**: chaotic regularization, discrete signaling, RNN dynamics, kernel methods, cortical recordings, population codes, neural representations, dynamical mean-field theory

### Competition, Stability, and Functionality in E-I Neural Circuits
- [[competition-stability-ei-circuits]] - Game-theoretic energetic framework for asymmetric E-I networks, extending energy-based models to biological circuits (arXiv: 2512.05252)
  - Each neuron as agent minimizing local energy in competitive game

### SoK: Post-Quantum Cryptography Implementation in Software Systems
- [[pqc-hot-framework]] - PQC-HOT model: Human-Organisation-Technology framework for systematic PQC implementation in software systems (arXiv: 2606.04669)
  - Reveals imbalance in PQC research: technological solutions dominate, human/organisational factors underexplored
  - PQC-HOT model: conceptual framework explaining HOT dimension interactions for implementation outcomes
  - NIST algorithms: ML-KEM, ML-DSA, SLH-DSA + HQC for algorithmic diversity
  - **Activation**: PQC implementation, post-quantum cryptography, quantum-safe migration, PQC-HOT model, NIST PQC, crypto agility

### Information-Geometric Bound on Entanglement Robustness
- [[qfi-entanglement-robustness]] - QFI bounds on concurrence reduction in entanglement generation under parameter uncertainty (arXiv: 2606.05696)
  - Direct connection: concurrence reduction bounded by quantum Fisher information (QFI) with respect to interaction parameter
  - Two interacting qubits: ΔC ≤ √(F_Q)·δθ
  - Trade-off: high QFI benefits sensing precision but increases entanglement sensitivity to fluctuations
  - **Activation**: quantum Fisher information, entanglement robustness, concurrence bounds, quantum network reliability, quantum sensing precision

### High-Rate Seedless Extractors for Device-Independent QKD
- [[seedless-di-qkd-extractors]] - Truncation-based seedless extractors achieving optimal rate of 1 key bit per singlet in DI-QKD (arXiv: 2605.31525)
  - Uses Bell violation as extractor promise instead of min-entropy
  - Truncation method reduces estimation variance, achieves optimal rate with vanishing fraction of rounds
  - Computationally efficient seedless extractors for privacy amplification
  - **Activation**: device-independent QKD, seedless extractor, privacy amplification, Bell violation, quantum key distribution

### Quantum Networks Using Diamond Color Defects
- [[diamond-quantum-networks]] - Comprehensive methodology for diamond NV/SiV centers as scalable quantum network nodes (arXiv: 2605.30005)
  - Excellent optical properties, fast spin-qubit control, long spin coherence times
  - Heterogeneous integration of diamond nanophotonics with photonic integrated circuits
  - Metropolitan-scale quantum network demonstrations with >50 km fiber entanglement
  - **Activation**: diamond color defects, NV center, SiV center, quantum network node, spin-photon interface, quantum repeater

### Coherent Room-Temperature Dipole Synchronization in Nanocavity Sheets
- [[room-temp-quantum-coherence]] - Room-temperature synchronized dipole state in plasmonic nanogap arrays with spatial coherence (arXiv: 2606.06490)
  - Spatial coherence across dipoles without temporal photon coherence or spectral narrowing
  - Driven-dissipative system: fast temporal decay but complex spatial correlations
  - Ultralow mode volumes, high Purcell enhancement, scalable ambient operation
  - **Activation**: room temperature quantum, plasmonic nanocavity, dipole synchronization, driven-dissipative quantum, Purcell enhancement

## 2026-06-08 - Deep Learning Research (Cron Job)

### Latent Reasoning with Normalizing Flows
- [[nf-cot-latent-reasoning-normalizing-flows]] - Normalizing flow framework for continuous thoughts preserving CoT advantages (KV-cache, likelihood estimation) (arXiv: 2606.06447v1)
  - TARFlow-style flow inside LLM backbone with dual-head generation
  - Exact likelihoods for latent thoughts, probabilistic left-to-right decoding
  - Policy-gradient optimization in latent reasoning space
  - **Activation**: latent reasoning, normalizing flows, CoT, continuous thoughts, reasoning optimization

### Compress-Distill: Reasoning Trace Compression for Efficient Knowledge Distillation
- [[compress-distill-reasoning-trace-compression]] - Post-hoc CoT trace compression achieving 18x efficiency with 96% accuracy retention (arXiv: 2606.05988v1)
  - Compresses reasoning traces to 8.6-21.0% original length before distillation
  - 2.0-7.6x training speedup, 3-19x shorter inference outputs
  - Model-compressed beats naive truncation (especially for smaller students)
  - **Activation**: reasoning distillation, trace compression, knowledge distillation, efficient training

### TailLoR: Protecting Principal Components in Parameter-Efficient Continual Learning
- [[tail-lor-spectral-continual-learning]] - Spectral LoRA routing adaptation to long-tail coordinates while protecting principal components (arXiv: 2606.06494v1)
  - Fixed singular bases U, V from pre-trained weights as reference frame
  - Soft spectral penalty discourages dominant direction updates
  - Low-rank update to singular value matrix Σ with interference reduction
  - **Activation**: continual learning, spectral decomposition, LoRA, principal components, adaptation

### You Only Index Once: Cross-Layer Sparse Attention with Shared Routing
- [[clsa-cross-layer-sparse-attention]] - 7.6x decoding speedup, 17.1x throughput at 128K context via shared routing index (arXiv: 2606.06467v1)
  - Token-level top-k selection computed once, reused across cross-decoder layers
  - Preserves fine-grained token selectivity while amortizing routing overhead
  - Joint optimization of pre-filling, KV-cache storage, long-context decoding
  - **Activation**: sparse attention, cross-layer, KV-sharing, routing index, long-context

### IA-RAG: Interval-Algebra-Driven Temporal Reasoning for Dynamic Knowledge Retrieval
- [[ia-rag-interval-algebra-temporal]] - Temporal RAG using Allen's Interval Algebra with Interval Event Units (IEUs) in Thematic Forest (arXiv: 2606.06044v1)
  - Models facts as time intervals with 13 Allen relations (before, meets, overlaps, etc.)
  - Sub-graph Time Tightening refines fuzzy temporal boundaries
  - Strong performance on complex compositional temporal reasoning benchmarks
  - **Activation**: temporal RAG, interval algebra, Allen relations, temporal reasoning, dynamic knowledge

### PSViT: A Methodology for Structurally Pruning Spiking Vision Transformers
- [[psvit-structured-pruning-spiking-vision]] - 22.4% memory saving structured pruning for SViT using sensitivity analysis (arXiv: 2606.03257v1)
  - Three-stage: uniform channel pruning → sensitivity analysis → fine-grained pruning
  - Hardware-agnostic: efficient on existing architectures vs. unstructured pruning
  - 70.3% accuracy without fine-tuning, 72.8% with fine-tuning (original 73.3%)
  - **Activation**: spiking vision transformer, structured pruning, neuromorphic efficiency, SViT

## 2026-06-08 - Neuroscience + Quantum Mechanics (Cron Job - Hourly)

### Breakeven demonstration of quantum low-density parity-check codes
- [[qldpc-breakeven-evaluation]] - Trapped-ion qLDPC breakeven with 4 logical qubits into 18 physical, OMG architecture for mid-circuit measurement without ion transport, 9x better than superconducting (arXiv: 2606.06455)
  - Demonstrates nine QEC codes (qLDPC, topological, concatenated) on single trapped-ion device without hardware reconfiguration
  - Achieves breakeven performance with logical error rates comparable to physical qubit lifetimes
  - Novel OMG (optical-metastable-ground) architecture for addressable mid-circuit measurement and reset
  - Eliminates need for ion transport or dedicated coolant ions, saving runtime and ion count
  - **Activation**: qLDPC evaluation, breakeven demonstration, quantum error correction, trapped-ion qubits, OMG architecture, fault tolerance

### Pretraining Recurrent Networks without Recurrence
- [[supervised-memory-training]] - Supervised Memory Training (SMT) for time-parallel RNN pretraining without BPTT, O(1) gradient path (arXiv: 2606.06479)
  - Decouples what to remember from how to update memory via one-step memory transition labels
  - Transformer-based encoder trained on predictive state objective acquires memory labels
  - Enables time-parallel RNN training with stable O(1) length gradient path without unrolling
  - Outperforms BPTT on language modeling and pixel sequence modeling tasks
  - **Activation**: RNN training, supervised memory, parallel training, predictive state, memory transition, BPTT replacement

### Equivariant Neural Belief Propagation
- [[equivariant-neural-belief-propagation]] - ENBP framework for SE(3)-symmetric probabilistic inference with Gaussian mixture messages, 98.9% conformational coverage (arXiv: 2606.06344)
  - Factor-graph with equivariant Gaussian mixture model messages transforming exactly under SE(3)
  - Rank-2 precision matrices via equivariant outer products with differentiable spectral decomposition
  - 100x faster than diffusion baselines at higher accuracy on GEOM-QM9/GEOM-Drugs
  - Converges on 15+ agent robotic inference where vanilla loopy BP diverges
  - **Activation**: equivariant neural belief propagation, SE(3) symmetry, Gaussian mixture model, factor-graph inference, conformational coverage, molecular modeling
## 2026-06-08 - Neuroscience + Quantum Mechanics (Cron Job - Hourly)

### Nonreversible Gauge Fields in Fokker-Planck Dynamics
- [[gauge-field-fokker-planck-dynamics]] - 非可逆规范场福克-普朗克动力学方法论：将保持稳态分布的扰动公式化为规范场，变形弛豫谱而不改变不变状态，连接超对称哈密顿量与神经网络学习 (arXiv: 2606.06412)
  - Gauge Field Formulation: 非可逆扰动保持稳态分布，规范场变形弛豫谱
  - Supersymmetric Hamiltonian: 打破细致平衡后FP算子成为非厄米超对称哈密顿量
  - Paired Eigenvalue Spectra: H和H†共享除零模式外的特征值
  - Neural Network Learning: 神经网络学习有限力加速收敛同时保持目标分布
  - **Activation**: gauge field, fokker-planck dynamics, supersymmetric hamiltonian, nonreversible perturbation, neural network learning, stationary distribution, spectral gap, non-hermitian dynamics, 规范场, 非厄米量子力学

### Quantum Vector Hopfield Network (Existing Skill Enhanced)
- [[quantum-vector-hopfield-network]] - 量子矢量Hopfield网络：模式由量子矢量自旋方向形成，量子动力学从自旋算符非对易性自然涌现，量子稳定化记忆模式 (arXiv: 2606.06597)
  - Quantum Vector Spins: 模式由量子矢量自旋方向形成
  - Intrinsic Quantum Dynamics: 量子动力学从自旋算符非对易性自然涌现
  - Enhanced Storage Capacity: 量子相干性提升存储容量
  - Quantum Stabilization: 量子效应稳定记忆模式抵抗热噪声
  - **Activation**: quantum hopfield network, vector spin, associative memory, quantum stabilization, memory capacity, non-commutativity, quantum many-body

### Quantum Correlations in QBism's Reconstruction Program
- [[quantum-correlations-qbism-reconstruction]] - QBism重构计划中的量子关联：qplex几何捕获两结果场景的Tsirelson界但不足以恢复全部量子关联约束 (arXiv: 2606.07485)
  - Qplex Geometry: 联合期望值表示为C-向量内积
  - CHSH Scenario: 共享内积结构限制最大值为Tsirelson界2√2
  - CGLMP Inequality: 允许代数最大值4，展现超量子关联
  - Reconstruction Limits: qplex几何捕获足够结构但不足以完全重构量子理论
  - **Activation**: qbism reconstruction, qplex geometry, chsh inequality, cglmp inequality, tsirelson bound, quantum correlations, superquantum, bell inequality
