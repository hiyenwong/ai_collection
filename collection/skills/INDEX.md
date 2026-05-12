## 2026-05-12 - Computer Science + Quantum Mechanics (Tuesday Cron Job)

### Can LLMs Solve Science or Just Write Code? Evaluating Quantum Solver Generation
- [[quantum-solver-evaluation]] - Q-SAGE迭代评估+等价RL量子电路合成+光子QNN算法优势评估+LUNA量子比特读出+CliNR噪声减少 (arXiv: 2605.07525)
  - Q-SAGE: 迭代评估LLM生成的量子求解器，执行+对比经典结果+反馈精炼
  - 等价RL架构: 单一策略跨不同量子比特数(6→30)实现Clifford电路合成，99.2%最优
  - 光子QNN算法优势: 2参数QNN vs 8参数ANN实现相同分类精度，计算有效维度
  - LUNA: LUT逻辑实现10.95x面积缩减、30%延迟降低的量子比特读出
  - CliNR: 中电路测量+ML引导稳定子选择，54%逻辑错误率降低
  - **Activation**: quantum solver evaluation, Q-SAGE, equivariant RL quantum, Clifford synthesis, photonic QNN, LUNA qubit readout, CliNR, mid-circuit measurement, quantum noise reduction, 量子求解器评估, 量子神经网络评估

### Photonic-Implemented Efficient Deep Quantum Neural Network
- [[photonic-deep-qnn]] - 光子芯片上的深度量子神经网络，通过虚拟希尔伯特空间扩展实现无需辅助量子比特的非线性激活 (arXiv: 2605.06397)
  - 输入复制+模式扩展在线性光子芯片上实现有效非线性激活
  - 消除物理辅助量子比特和测量诱导消耗，级联性优异
  - 展示两层QNN在非线性分类、图像生成、Gibbs态制备中的应用
  - **Activation**: photonic deep QNN, integrated photonics quantum neural network, Hilbert space expansion, ancilla-free QNN, 光子量子神经网络, virtual Hilbert space

### Lightweight Quantum Agent for Edge Systems
- [[lightweight-quantum-agent]] - 轻量级量子安全边缘AI代理，联合优化后量子密码(NOMA)和NOMA资源分配，线性复杂度O(N) (arXiv: 2604.25980)
  - 多阶段随机MINLP建模PQC静态功耗约束，Lyapunov优化解耦长期问题
  - O(N)线性复杂度NOMA功率分配算法，N=35时较SCA加速46倍
  - 维持队列稳定性和能耗约束，满足动态无线环境实时决策需求
  - **Activation**: lightweight quantum agent, edge AI PQC, NOMA resource allocation, Lyapunov optimization edge, 轻量级量子代理, post-quantum cryptography edge

### FPGA-Based Real-Time Quantum Error Correction Decoder
- [[fpga-quantum-decoder]] - FPGA神经网络解码器实现550ns确定性闭环延迟的实时表面码纠错 (arXiv: 2605.04892)
  - 124ns NN推理延迟，1.25μs QEC周期内完成反馈校正
  - 非Clifford电路中Pauli-frame不足时的中电路反馈校正
  - 实时解码逻辑性能与离线解码相当
  - **Activation**: FPGA quantum decoder, real-time QEC, surface code decoding, neural network decoder, low-latency quantum control, FPGA解码

### Neural-Powered Qubit Embedding for QUBO Problems
- [[neural-qubit-embedding]] - 神经网络解决Rydberg原子量子硬件的QUBO图嵌入问题，超越Gurobi求解器 (arXiv: 2605.04736)
  - 将QUBO问题映射为单位盘图嵌入，利用神经网络从不配置转换到可行配置
  - 量子比特物理放置匹配硬件Ising哈密顿量
  - **Activation**: neural qubit embedding, QUBO graph embedding, unit disk graph, Rydberg atom quantum, neutral atom embedding

### Quantum Hierarchical Reinforcement Learning
- [[quantum-hierarchical-rl]] - 变分量子电路实现的分层强化学习，混合option-critic架构节省66%可训练参数 (arXiv: 2605.03434)
  - 量子特征提取器超越经典基线，量子option-value估计存在架构瓶颈
  - 混合分层agent在标准基准环境中验证
  - **Activation**: quantum hierarchical RL, variational quantum circuits RL, option-critic quantum, quantum reinforcement learning, parameter-efficient quantum agent

---

## 2026-05-11 - Neuroscience Research (Cron Job)

### Universal Neural Propagator: Learning Time Evolution in Many-Body Quantum Systems
- [[universal-neural-propagator-quantum-dynamics]] - 单模型学习驱动协议到时间演化传播子的映射，实现跨哈密顿量和初态的量子动力学迁移模拟 (arXiv: 2605.05299)
  - 将学习对象从量子态转移到算子，实现跨哈密顿量和初态泛化
  - 完全自监督训练，2D驱动Ising模型验证
  - 精确对角化外推系统尺寸，可观测数据微调
  - **Activation**: neural propagator, quantum dynamics simulation, neural operator learning, quantum state evolution, UNP, universal propagator, quantum foundation model

### Neural Network Quantum States in the Grand Canonical Ensemble
- [[neural-network-quantum-states-grand-canonical]] - Fock空间中对称玻色子波函数的神经量子态架构，支持变粒子数系统 (arXiv: 2605.07779)
  - Fock空间神经网络架构，强制玻色子交换对称性
  - 化学势控制下收敛到物理玻色子数
  - 精确计算约化密度矩阵，获取凝聚态分数和径向密度分布
  - **Activation**: neural quantum states, grand canonical ensemble, bosonic wavefunctions, Fock space, variational Monte Carlo, NQS

### Globally Optimal Training of Spiking Neural Networks via Parameter Reconstruction
- [[globally-optimal-snn-parameter-reconstruction]] - 消除替代梯度近似误差：将并行前馈阈值网络凸化扩展到并行循环阈值网络，实现全局最优SNN训练 (arXiv: 2605.08022)
  - 循环阈值网络凸化，并行SNN作为结构化特例
  - 参数重构算法直接求解凸优化，消除跨层误差累积
  - 数据可扩展，可单独使用或与替代梯度训练结合
  - **Activation**: globally optimal SNN, parameter reconstruction, convex SNN training, surrogate gradient elimination, threshold network convexification

### Multi-Atlas Disentangled Connectivity Learning for Brain Disorder Identification
- [[madcle-multi-atlas-disentangled-connectivity]] - 多脑图谱解耦功能连接表示学习，通过跨图谱分布对齐实现鲁棒脑疾病分类 (arXiv: 2605.07026)
  - 多分支编码不同图谱FC矩阵，MMD对齐疾病相关表示
  - 解耦疾病信号、协变量因子和图谱特异性残差
  - 在ADNI和ADHD-200数据集上优于单图谱和多图谱基线
  - **Activation**: multi-atlas FC, disentangled connectivity, cross-atlas consistency, MADCLE, atlas parcellation heterogeneity

### CORE: Cross-site OOD Robust brain nEtwork
- [[core-cross-site-ood-brain-network]] - 跨站点OOD鲁棒脑网络学习框架，通过站点混杂因子解耦和瞬态通路动力学建模实现跨站点泛化 (arXiv: 2605.06050)
  - 站点感知混杂因子解耦，提取可复现诊断连接边
  - 线图组织实现通路级迁移建模
  - 先验引导的个体自适应门控保留个体变异性
  - **Activation**: cross-site OOD, brain network generalization, confounder decoupling, transient pathway dynamics, line graph brain

## 2026-05-11 - Neuroscience + Quantum Mechanics (Monday Cron - Round 3)

### Same Brain, Different Prediction: How Preprocessing Choices Undermine EEG Decoding Reliability
- [[eeg-preprocessing-reliability]] - EEG解码可靠性评估：预处理选择导致42%试次预测翻转，提出Walsh-Hadamard分解、预处理不确定性(PU)诊断、NA-PGI正则化 (arXiv: 2605.07212)
  - 预处理干预空间的形式化建模，2^7管线空间分析
  - PU捕获模型置信度之外的不稳定性维度
  - Walsh-Hadamard分解揭示敏感性在实践中近可加
  - **Activation**: eeg reliability, 预处理可靠性, preprocessing uncertainty, pipeline sensitivity, bci reliability, eeg decoding robustness

### Breaking QAOA's Fixed Target Hamiltonian Barrier: A Fully Connected Quantum Boltzmann Machine via Bilevel Optimization
- [[quantum-boltzmann-machine-qaoa]] - 全连接量子玻尔兹曼机通过双层优化扩展QAOA架构，单层(p=1)实现95.6%保真度，噪声鲁棒性强 (arXiv: 2605.07473)
  - 内环：正相能量最小化（QAOA电路）
  - 外环：负相对比散度（优化目标哈密顿量结构参数）
  - 2x噪声下目标态概率仍为最高（0.3859）
  - **Activation**: quantum boltzmann machine, QBM, QAOA extension, 量子玻尔兹曼机, bilevel quantum optimization, quantum contrastive divergence

## 2026-05-11 - Neuroscience + Quantum Mechanics (Monday Cron - Round 2)

### Exchange-Only Silicon Spin Qubits: PINN Optimised Pulse Sequences
- [[pinn-quantum-pulse-optimization]] - 两阶段PINN框架优化硅自旋量子比特脉冲，最大化噪声平均门保真度 (arXiv: 2605.03056)
  - Stage I: 噪声平均门保真度最大化（迭代1-100粗搜索）
  - Stage II: 门级保真度精炼，添加鲁棒性惩罚
  - 物理约束：将含交换哈密顿量的薛定谔方程直接嵌入损失函数
  - **Activation**: PINN quantum control, exchange-only spin qubits, charge noise optimization, silicon quantum computing, pulse optimization, gate fidelity

### Quantum-Tunnelling Oscillators for Cognitive Modelling
- [[quantum-cognitive-tunnelling-oscillators]] - 量子隧穿振荡器建模认知决策，光学错觉感知与群体决策的量子力学代理 (arXiv: 2604.03940)
  - 将认知代理建模为量子力学系统，选择通过隧穿而非概率转移
  - 光学错觉感知：感知态作为希尔伯特空间基态，感知切换为量子隧穿
  - 群体决策：耦合量子隧穿振荡器网络涌现集体现象
  - **Activation**: quantum tunnelling oscillator, cognitive modelling, quantum cognition, optical illusion perception, group decision making, context-dependent transitions

## 2026-05-11 - Neuroscience + Quantum Mechanics (Monday Cron - Round 1)

### Toward Magnetic-Field-Free Quantum Computing in Engineered Organic Materials: 3-Layer Quantum Brain Hypothesis
- [[three-layer-quantum-brain]] - 三层量子脑假说：核自旋记忆→电子自旋界面→经典电化学，无磁场有机量子计算 (arXiv: 2605.00026)
  - 提出4条无磁场量子计算路径（黄酮-硝基自由基对、PTM自由基阵列、SVILC类比、SSH孤子）
  - CQEC在16个路径×算法对上显著提升(p<10⁻⁵)，Bernstein-Vazirani实现7.6-31×量子优势
  - 层-蛋白质权衡：CRY核T₂长但电子T₂短，MAO-A反之
  - **Activation**: three-layer quantum brain, CQEC, radical-pair qubit, cryptochrome quantum, organic quantum computing, SVILC, magnetic-field-free quantum

### The Physical Basis of Information Flow in Neural Matter: Thermocoherent Perspective
- [[thermocoherent-cognitive-dynamics]] - 热相干框架建模神经物质信息流，耦合热流与离域相干信息 (arXiv: 2604.04069)
  - 关系资源（纠缠、量子失谐、经典关联）可作为神经组织中隐藏的物理资源
  - 离子通道、氢键质子网络、芳香π电子架构、富磷酸基序为可能底物
  - 非宏观量子认知声明，而是可证伪的微观资源偏置跨尺度协调框架
  - **Activation**: thermocoherent effect, information flow neural matter, relational resources, Mpemba neural, cross-scale neural coordination

### GKSL Dynamics for Quantum-Like Models of Cognition and Decision Making
- [[gksl-quantum-cognition]] - 开放量子系统GKSL主方程建模认知决策，含认知节拍分析 (arXiv: 2604.18643)
  - 主动/被动哈密顿量区分：非对换=认知代理的数学签名
  - 认知节拍：Liouvillian通道间的结构张力产生二次慢调制，映射犹豫/承诺时机
  - 可稳定非纳什均衡结果（如囚徒困境）
  - **Activation**: GKSL, Lindblad, quantum cognition, cognitive beats, open quantum systems, decision making, non-Nash equilibrium

### Training Single-Electron and Single-Photon Stochastic Physical Neural Networks
- [[stochastic-physical-neural-networks]] - 随机物理神经网络训练，单电子/单光子神经元实现>97% MNIST精度 (arXiv: 2604.10861)
  - 电子实现：量子点单电子隧穿；光子实现：单光子源驱动模式
  - 关键发现：向后传递使用经验输出（非真概率）实现更高精度
  - 高噪声和模型不确定性下保持鲁棒性
  - **Activation**: stochastic PNN, physical neural network, single-electron neuron, single-photon neuron, empirical backward pass

## 2026-05-10 - Information Science + Quantum Mechanics (Sunday Cron - Round 3)

### Syndrome resampling enhances quantum error correction thresholds
- [[syndrome-resampling-qec]] - 重采样综合征提升QEC阈值，无需额外硬件即可降低逻辑错误率4个数量级 (arXiv: 2605.06101)
  - 利用低概率综合征易导致逻辑失败的特性，偏向最可能综合征提高保真度
  - 建立Rényi相干信息与综合征概率分布幂次的直接联系
  - 适用于任何解码器，可从有限综合征数据实现
  - 表面码：逻辑错误率降低多达4个数量级
  - **Activation**: syndrome resampling, QEC threshold, Rényi coherent information, decoder-agnostic QEC, logical fidelity improvement, syndrome biasing

### OBLIQ-Bench: Exposing Overlooked Bottlenecks in Modern Retrievers
- [[oblique-retrieval-benchmark]] - 揭示现代检索器在隐式和潜在查询上的瓶颈 (arXiv: 2605.06235)
  - 定义倾斜查询(oblique query)：寻找实例化潜在模式而非匹配显式关键词的文档
  - 揭示检索-验证不对称性：LLM可验证相关性但检索管线无法召回
  - 五种倾斜搜索问题的基准测试套件
  - **Activation**: oblique retrieval, latent pattern search, implicit query, OBLIQ-Bench, retrieval bottleneck, verification asymmetry


### Affine Subcode Ensemble Decoding for Degeneracy-Aware Quantum Error Correction
- [[affine-subcode-ensemble-decoding]] - 仿射子集集成解码改进QLDPC码BP解码的收敛性 (arXiv: 2605.06547)
  - 将QLDPC码分解为仿射子集，对每个子集独立运行BP解码并集成结果
  - 显式处理简并性(degeneracy)问题，解决传统BP忽略等效错误模式的缺陷
  - 适用于CSS码、超图积码、双变量双线性码等各类QLDPC码
  - **Activation**: quantum error correction, QLDPC decoding, belief propagation, degeneracy, ensemble decoding, affine subcode, quantum LDPC

## 2026-05-10 - Information Science (Cron Job)

### EMO: Pretraining Mixture of Experts for Emergent Modularity
- [[emo-emergent-moe-modularity]] - 文档级专家池共享实现MoE模块化部署 (arXiv: 2605.06663)
  - 文档内token共享专家池，实现语义级专家特化
  - 25%专家保留仅1%性能损失，支持内存受限部署
  - **Activation**: emo moe, emergent modularity, mixture of experts modularity, composable MoE, modular LLM deployment

### UniPool: A Globally Shared Expert Pool for Mixture-of-Experts
- [[unipool-shared-expert-moe]] - 全局共享专家池替代逐层专家所有权 (arXiv: 2605.06665)
  - 池级辅助损失实现专家利用率均衡，NormRouter提供稳定路由
  - 专家参数可按深度亚线性增长，41.6%-66.7%预算匹配vanilla MoE
  - **Activation**: unipool, shared expert pool, pool-level MoE, global expert budget, NormRouter


### A Residual-Based Quantum Linear System Algorithm with Dynamic Stopping and Applications to Elliptic PDEs
- [[residual-based-qlsa-dynamic-stopping]] - 基于残差的量子线性系统算法，通过残差寄存器实现动态停止条件，减少量子电路门数和演化时间 (arXiv: 2605.06414)
  - 增强动力学设计引入残差变量，测量残差寄存器可实时判断收敛状态而无需重构解向量
  - 对光滑右端项，动态停止可减少演化时间和门计数，降低硬件误差累积风险
  - 适用于离散椭圆PDE求解，PDE依赖尺度与平方根条件数缩放相当
  - **Activation**: quantum linear system, QLSA, dynamic stopping, residual register, elliptic PDE, quantum convergence, a posteriori error

### Quantum Proper Scoring Rules: Minimax Estimation and Resource-Theoretic Advantages
- [[quantum-proper-scoring-rules]] - 量子proper scoring rules方法论，将经典评分规则扩展到量子领域，实现量子激励机制设计 (arXiv: 2605.05268)
  - Quantum Value Functionals通过operator convex generators建立proper quantum scoring rules
  - Quantum Cramér-Rao-McCarthy Bound连接minimax risk与QFI
  - **Activation**: quantum scoring, proper scoring rules, quantum Fisher information, quantum incentives

### The true cost of factoring: Linking magic and number-theoretic complexity in Shor's algorithm
- [[quantum-magic-resource-analysis]] - 量化magic state作为量子资源的方法论，连接数论复杂度与量子资源需求 (arXiv: 2605.05347)
  - Magic (non-stabilizerness)量化作为基础量子资源度量
  - Shor算法在实际相关区域最大化利用magic资源
  - **Activation**: magic state, non-stabilizerness, quantum resource theory, Shor algorithm

### A Factor-Graph Formulation of CSS Syndrome Decoding: Joint BP and Four-State BP
- [[css-syndrome-decoding]] - CSS量子纠错syndrome decoding的factor graph公式化方法 (arXiv: 2605.05132)
  - CSS syndrome decoding建模为两个耦合Tanner图的binary factor graph
  - Joint BP与four-state BP在重标记和边缘化后等价
  - **Activation**: CSS code, syndrome decoding, belief propagation, quantum error correction

### QML Framework-Agnostic Design
- [[qml-framework-agnostic-design]] - 框架无关的量子机器学习设计方法论，通过抽象层实现跨平台兼容和算法可移植性
  - 核心要点: 定义硬件无关的量子ML抽象接口，支持在不同量子后端间无缝迁移
  - 核心要点: 采用中间表示(IR)层解耦算法逻辑与物理实现，降低框架锁定风险
  - **Activation**: framework-agnostic QML, quantum ML portability, quantum abstraction layer, cross-platform quantum

## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)

### Beyond Gates: Pulse Level Quantum Fourier Models
- [[pulse-level-quantum-fourier-models]] - 脉冲级量子傅里叶模型(QFM)用于量子机器学习，超越门电路分解实现更丰富的频率谱 (arXiv: 2605.04945)
  - 核心要点: QFM在脉冲级操作而非门级分解，访问更丰富的频率集合，提供更强的表达能力
  - 核心要点: 频率谱由哈密顿量本征值差决定，脉冲级控制可绕过门分解开销直接优化
  - **Activation**: quantum Fourier model, QFM, pulse-level quantum ML, quantum machine learning Fourier, 脉冲级量子傅里叶模型, quantum feature space

### Analytical Angle-Finding for Quantum Signal Processing via Orthogonal Polynomials
- [[quantum-signal-processing-orthogonal-poly]] - 通过正交多项式理论实现QSP显式角度计算，光滑函数O(log(1/ε))门复杂度的块编码 (arXiv: 2605.05321)
  - 核心要点: QSP多项式基通过正交性/双正交性刻画，推导Hermite、Jacobi、Rogers-Szego多项式的显式QSP角度
  - 核心要点: 利用Hermite级数展开实现光滑函数的O(log(1/ε))门块编码，适用于Hamiltonian simulation和量子特征映射
  - **Activation**: quantum signal processing, QSP angles, orthogonal polynomials QSP, Hermite polynomials quantum, Jacobi polynomials quantum, Rogers-Szego, block-encoding, quantum function approximation

### Distributed Shor's Algorithm on Modular Atomic Processors
- [[modular-quantum-shor-compilation]] - 半百万量子比特模块化处理器上Shor算法分布式编译，2048位RSA分解仅16%时间开销 (arXiv: 2605.03951)
  - 核心要点: CPU启发的模块化架构，通过Bell pair分发和流水线优化实现跨模块通信与模块内时钟率的最佳平衡
  - 核心要点: 首个端到端大规模整数分解模拟，证明模块化架构在~50万量子比特规模下的可行性
  - **Activation**: Shor algorithm compilation, modular quantum processor, distributed quantum factoring, RSA quantum attack, Bell pair communication, atomic qubit architecture, quantum cryptography

### From Classical to Quantum-Mechanical Data Assimilation
- [[quantum-mechanical-data-assimilation]] - 量子力学数据同化(QMDA)结合动力系统与量子计算进行状态估计 (arXiv: 2605.04881)
  - 核心要点: 转移算子框架统一经典DATO和量子QMDA方法，量子态编码实现指数级状态空间压缩
  - 核心要点: QMDA在预测步使用幺正演化、更新步使用量子测量，读出开销是量子优势的关键限制
  - **Activation**: quantum data assimilation, QMDA, DATO, quantum state estimation, transfer operator dynamics, 量子数据同化

---

## 2026-05-07 - Systems Engineering + Quantum Computing (Cron Job - 23:00)

### SpinTune: RL-Based Quantum Sensor Network Reliability
- [[spintune-quantum-sensor-reliability]] - 强化学习优化动态解耦脉冲序列提升量子传感器网络可靠性 (arXiv: 2605.04416)
  - 核心要点: 使用RL代理学习环境噪声谱并自适应选择最优DD脉冲序列，替代固定CPMG/XY序列
  - 核心要点: 实现量子-经典混合计算管道，量子传感器测量+经典RL优化DD序列+实时自适应噪声
  - **Activation**: spintune, quantum sensor reliability, dynamical decoupling optimization, DD pulse sequence, quantum decoherence mitigation, 量子传感器可靠性

### Neural-Powered Qubit Embedding for Quantum Annealing
- [[neural-qubit-embedding]] - 神经网络解决量子退火器QUBO问题的图嵌入/minor embedding问题 (arXiv: 2605.04736)
  - 核心要点: 使用GNN学习QUBO问题图表示，通过匹配层将逻辑变量分配到硬件量子比特，构建链式连接
  - 核心要点: 单位盘图建模硬件连接性，优化链长和连通性平衡，避免链重叠
  - **Activation**: qubit embedding, quantum annealer embedding, QUBO mapping, minor graph embedding, unit disk graph, quantum annealing connectivity

### Factor-Graph CSS Syndrome Decoding for Quantum Error Correction
- [[css-syndrome-decoding]] - 基于因子图的CSS码综合征解码，联合BP与四态BP算法 (arXiv: 2605.05132)
  - 核心要点: 将CSS码后验概率建模为二元因子图，两个Tanner图通过每个量子比特的联合先验耦合
  - 核心要点: 四态BP跟踪完整Pauli分布{I,X,Z,Y}，比独立X/Z解码更准确地处理Y=XZ相关性
  - **Activation**: css syndrome decoding, quantum error correction decoding, factor graph decoding, belief propagation QEC, Tanner graph quantum, CSS码译码

---

## 2026-05-07 - Systems Engineering + Quantum Computing (Cron Job - 13:00)

### QBalance: Multi-Objective Quantum Workflow Optimization
- [[qbalance-quantum-workflow-optimization]] - 多目标量子工作流优化方法论，系统化NISQ编译/噪声抑制/误差缓解策略选择 (arXiv: 2605.02966)
  - 核心要点: 将NISQ工作流建模为有限多目标策略选择问题，涵盖加权目标函数、非支配Pareto选择、生存乘积误差代理、贝叶斯候选排序
  - 核心要点: QBalance提供可复现编排模型，集成Qiskit pass-manager/SABRE/ZNE/动态解耦，但bandit仅排序不减少评估次数
  - **Activation**: qbalance, quantum workflow optimization, NISQ strategy selection, quantum compilation multi-objective, quantum error mitigation

### Constraint Preserving XY-Mixers under Trotterized Adiabatic Evolution
- [[constraint-preserving-quantum-optimization]] - 约束保持量子优化方法论，XY混合器与Trotter化绝热演进 (arXiv: 2605.02465)
  - 核心要点: 约束局域性决定XY混合器有效性 - 全局约束用Pauli-X，局部分块用XY混合器
  - 核心要点: Trotter误差取决于单个约束结构而非总问题规模，TAE+结构感知混合器设计提供鲁棒替代方案
  - **Activation**: quantum optimization constraints, XY-mixer, Trotterized adiabatic, constraint-preserving quantum, QAOA constraints

### Hardware-Efficient Quantum Optimization for Transportation Networks
- [[quantum-transportation-optimization]] - 硬件高效交通网络量子优化，AQC-QAOA混合方法 (arXiv: 2604.26175)
  - 核心要点: AQC压缩绝热演进前段为浅电路+变分层，减少双量子门深度同时保持可行解发现率
  - 核心要点: 量子算法作为交通决策工作流中的候选生成器，标准QAOA有效利用AQC初始化
  - **Activation**: quantum transportation, AQC-QAOA, compressed adiabatic evolution, quantum vehicle routing, hardware-efficient quantum

### Quantum Subgroup Discovery for Network Security
- [[quantum-subgroup-discovery]] - 量子增强子群发现用于网络安全和可解释入侵检测 (arXiv: 2604.27153)
  - 核心要点: 首次将子群发现表述为QUBO优化，QAOA在IBM硬件上求解，发现独特子群达99.6%精度
  - 核心要点: NISQ缩放边界确立 - QAOA在10-20量子比特有效，25+比特噪声主导信号
  - **Activation**: quantum subgroup discovery, quantum intrusion detection, QAOA network security, WRAcc optimization, NISQ scaling boundary

---

## April 26, 2026 - Neuroscience Research Update (Cron Job - Late Morning)

### New Skills from arXiv Research (3 papers)

#### A Critical Assessment of the Brain Criticality Hyp...
- [[memory-induced-long-range-order-brain-criticality]] - **NEW** (2604.21071)
  - MILRO (Memory-Induced Long-Range Order) phase as alternative to critical point for explaining scale-invariant neural cor...
  - **Activation**: brain criticality, milro, scale-invariant, neural correlations, memory-induced

#### A neural operator framework for data-driven discov...
- [[neural-operator-stability-receptivity]] - **NEW** (2604.19465)
  - Neural operator framework for data-driven discovery of stability and receptivity in physical systems
  - **Activation**: neural operator, stability analysis, receptivity, fluid dynamics, data-driven discovery

#### Neuroscience Inspired Graph Operators Towards Edge...
- [[neuroscience-inspired-graph-virtual-sensing]] - **NEW** (2604.16722)
  - Neuroscience-inspired graph operators for edge-deployable virtual sensing of irregular time series
  - **Activation**: neuroscience inspired, graph operators, virtual sensing, edge deployable, irregular time series

---

### Research Statistics
- **Total Papers Scanned**: 59 from arXiv
- **New Skills Created**: 3
- **Collection Coverage**: 684+ existing skills
- **Keywords**: neuroscience, brain network, neural dynamics, spiking neural network

---

## April 26, 2026 - Neuroscience Research Update (Morning)

### New Skills from Latest arXiv Research (8 papers)

#### Hierarchical Critical Brain Dynamics
- [[hierarchical-critical-brain-dynamics]] - **NEW** Hierarchical organization of critical brain dynamics (arXiv:2604.21832)
  - Phenomenological renormalization group approaches
  - Criticality signatures vary systematically along anatomical hierarchies
  - Measure-dependent organization (static vs dynamic exponents in opposite directions)
  - Validated on mouse visual cortex and hippocampus
  - **Activation**: brain criticality, hierarchical organization, renormalization group, visual cortex, hippocampus

#### Brain-Inspired Capture for Visual Decoding
- [[brain-inspired-capture-evidence-driven]] - **NEW** BI-Cap: Neuromimetic perceptual simulation for EEG visual decoding (arXiv:2604.17927)
  - Three brain-inspired components: hierarchical feature extraction, evidence-driven accumulation, adaptive temporal integration
  - Mimics primate ventral visual stream processing
  - Drift-diffusion model inspired decision dynamics
  - **Activation**: brain-inspired capture, neuromimetic perceptual simulation, EEG visual decoding, ventral visual stream, evidence accumulation

#### Cross-Region Alignment Pattern (CRAP) Analysis
- [[brain-alignment-crap-analysis]] - **NEW** Exposing vulnerability in model-brain alignment (arXiv:2604.21780)
  - Models can achieve high alignment without biologically plausible computations
  - Cross-region patterns reveal true vs spurious alignment
  - Stricter evaluation framework for ANN-brain comparisons
  - **Activation**: model-brain alignment, CRAP analysis, cross-region patterns, biological plausibility testing

#### Brain Criticality Assessment Framework
- [[brain-criticality-assessment]] - **NEW** Critical assessment of brain criticality hypothesis (arXiv:2604.21071)
  - Multi-modal data integration (electrophysiology, fMRI, calcium imaging)
  - Identifies finite-size effects, sampling biases, methodological issues
  - Framework to distinguish true vs apparent criticality
  - **Activation**: brain criticality, criticality assessment, multi-modal neuroimaging, methodological validation

#### EEG2Vision: Multimodal Visual Reconstruction
- [[eeg2vision-multimodal-reconstruction]] - **NEW** 2D visual reconstruction from EEG via cross-modal CLIP alignment (arXiv:2604.08063)
  - Three-stage framework: transformer encoder, contrastive CLIP alignment, diffusion generation
  - Novel temporal attention mechanism for dynamic neural responses
  - State-of-the-art reconstruction quality
  - **Activation**: EEG2Vision, EEG visual reconstruction, cross-modal neural decoding, diffusion models for EEG

#### GFlowState: Training Visualization
- [[gflowstate-training-visualization]] - **NEW** Visual analytics for Generative Flow Network training (arXiv:2604.21830)
  - Real-time monitoring of training states and flow distributions
  - Diagnoses mode collapse, insufficient exploration, reward hacking
  - Interactive dashboards for GFlowNet researchers
  - **Activation**: GFlowState, GFlowNet visualization, generative flow networks, training visualization

#### Parametric Oscillator Neuromorphic Computing
- [[parametric-oscillator-neuromorphic]] - **NEW** Neuromorphic computing via parametrically-driven MEMS oscillators (arXiv:2604.21861)
  - Frequency conversion implements weighted synaptic connections
  - Intrinsic nonlinear dynamics enable STDP and reservoir computing
  - Validated with MEMS resonators for ultra-low power
  - **Activation**: parametric oscillators, neuromorphic MEMS, frequency conversion neuromorphic, spiking oscillator networks

#### CNN-AAE EEG Classification
- [[cnn-aae-eeg-classification]] - **NEW** EEG classification via CNN + Adversarial Autoencoder (arXiv:2604.04313)
  - AAE learns robust latent representations, filtering noise and artifacts
  - CNN classifier operates on latent space
  - Improved performance in low SNR conditions
  - **Activation**: CNN AAE EEG, adversarial autoencoder EEG, EEG classification, motor imagery recognition

---

## April 26, 2026 - Neuroscience Research (Cron Job)

### New Skills from Latest arXiv Research

#### YANA: FPGA-based Neuromorphic Accelerator
- [[yana-neuromorphic-simulation]] - **NEW** Bridging the neuromorphic simulation-to-hardware gap (arXiv:2604.03432)
  - Five-stage event-driven processing pipeline
  - Supports arbitrary SNN topologies via point-to-point connections
  - Resource efficient: 740 LUTs, 918 registers, 7 BRAMs, 24 URAMs per core
  - Up to 2^17 synapses, 2^10 neurons on AMD Kria KR260
  - **Activation**: YANA, FPGA, neuromorphic accelerator, SNN hardware, event-driven, AMD Kria

#### Frequency-Aware Epileptic Seizure Detection with GCN
- [[eeg-gcn-epileptic-seizure-detection]] - **NEW** GCN-based seizure detection in separate frequency bands (arXiv:2604.00163)
  - Five frequency bands: delta, theta, alpha, lower beta, higher beta
  - Eleven discriminative features per band
  - GCN models spatial dependencies among EEG electrodes
  - 99.01% overall accuracy on CHB-MIT dataset
  - **Activation**: seizure detection, EEG, graph CNN, frequency bands, epilepsy, interpretability

#### DMOSOPT: Multi-Objective Optimization for Neural Dynamics
- [[dmosopt-neural-dynamical-systems]] - **NEW** Joint surrogate learning for neural system optimization (arXiv:2603.20984)
  - Unified surrogate model learns objectives, constraints, and sensitivities
  - Handles binary feasible/infeasible constraint partitions
  - Gradient guidance where traditional methods fail
  - Validated at supercomputing scale with fewer evaluations
  - **Activation**: multi-objective optimization, surrogate model, neural dynamics, parameter optimization, constraints

#### PINN for Neuronal Parameter Estimation
- [[pinn-neuronal-parameter-estimation]] - **NEW** Physics-informed neural networks for neuron state/parameter estimation (arXiv:2603.08742)
  - Joint reconstruction of unobserved states and biophysical parameters
  - Robust to poor initialization
  - Works with partial observations over short windows
  - Demonstrated on Morris-Lecar and respiratory neuron models
  - **Activation**: PINN, parameter inference, state reconstruction, neuronal systems, multiscale dynamics

#### Brain-Like Algorithm Constraints
- [[brain-like-algorithm-constraints]] - **NEW** How biological constraints shape learned algorithms (arXiv:2601.02063)
  - Simple biological details constrain algorithm selection
  - Nonnegative firing and resource budgets break symmetries
  - Produces interpretable single-neuron responses
  - Bridges computational neuroscience and AI interpretability
  - **Activation**: brain-like algorithms, biological constraints, symmetry breaking, mechanistic interpretability

#### LearnAD: Neuro-Symbolic Alzheimer's Classification
- [[learnad-neuro-symbolic-alzheimers]] - **NEW** Interpretable rules for Alzheimer's prediction from brain MRI (arXiv:2601.00877)
  - Two-stage: statistical/GNN feature selection + FastLAS symbolic learning
  - Fully interpretable rules match GNN accuracy
  - Neuro-symbolic approach improves interpretability
  - Applications: clinical decision support, biomarker discovery
  - **Activation**: neuro-symbolic, Alzheimer's disease, interpretable rules, brain networks, GNN

---

## April 24, 2026 - Neuroscience Research (Cron Job)

### BrainCast: Spatio-Temporal fMRI Forecasting
- [[braincast-spatiotemporal-fmri-forecasting]] - Whole-brain fMRI time series prediction via spatial interaction awareness + temporal feature refinement (arXiv:2603.13361)
  - Three-module architecture: SIA, TFR, SPA for joint spatio-temporal modeling
  - Trained on HCP resting-state and task fMRI data
  - **Activation**: fmri, forecasting, brain network, time series, spatio-temporal, HCP, functional connectivity

### DECODE: Dual-Enhanced Conditioned Diffusion for EEG
- [[decode-dual-enhanced-conditioned-diffusion-eeg]] - Semantic language conditioning + temporal dynamics for event-specific EEG generation (arXiv:2603.16885)
  - MAE = 0.626 μV over 75-step horizons on real driving EEG data
  - Zero-shot generalization via natural language descriptions
  - **Activation**: eeg, diffusion, forecasting, language model, BCI, semantic conditioning, Langevin dynamics

### JEDI: Jointly Embedded Neural Dynamics Inference
- [[jedi-jointly-embedded-neural-dynamics]] - Hierarchical shared embedding over RNN weights for cross-task neural dynamics (arXiv:2603.10489)
  - Learns condition-specific embeddings modulating RNN dynamics
  - Recovers fixed point structures and eigenspectrum features
  - Validated on motor cortex recordings during monkey reaching
  - **Activation**: neural dynamics, RNN, embedding, motor cortex, multi-task, fixed points, hierarchical model

### Taming Epilepsy: Mean Field Control via GK-MFG
- [[taming-epilepsy-mean-field-control]] - Graph-regularized Koopman Mean-Field Game for seizure suppression (arXiv:2603.18035)
  - Reservoir computing for Koopman operator linearization
  - APAC-Net for distributional control with PLV graph constraints
  - **Activation**: epilepsy, seizure, mean field game, Koopman operator, reservoir computing, EEG, brain control

### Behavior-dLDS: Decomposed Linear Dynamical Systems
- [[behavior-dlds-decomposed-linear-dynamical]] - Disentangles behavior-generating from internal computation neural subsystems (arXiv:2603.05612)
  - Scales to tens of thousands of neurons
  - Applied to zebrafish hindbrain positional homeostasis
  - **Activation**: LDS, linear dynamical systems, behavior, decomposition, zebrafish, neural population, latent dynamics

### Unified Brain-to-Text Decoding (Mandarin Chinese)
- [[unified-brain-text-decoding-mandarin]] - Cross-modal speech production/perception decoding for Mandarin via LLM (arXiv:2603.12628)
  - 7B-parameter LLM post-training for Pinyin-to-sentence reconstruction
  - Sentence-level decoding from single-character training data
  - **Activation**: brain-to-text, speech decoding, Mandarin, Chinese, LLM, production, perception, cross-modal

### Neural Dynamics-Informed Pre-trained Brain Network
- [[neural-dynamics-informed-pretrained-brain-network]] - Personalized brain functional network construction replacing pre-defined atlases (arXiv:2603.07524)
  - Pre-trained framework for heterogeneous neural activity representations
  - Evaluated across 18 datasets for virtual modulation and abnormal circuit detection
  - **Activation**: personalized, brain functional network, pre-trained, neural dynamics, brain parcellation

### Firing Rate Neural Networks for Model Predictive Control
- [[firing-rate-nn-model-predictive-control]] - Translates MPC into firing rate networks via projected gradient on dual (arXiv:2603.25959)
  - Contraction theory ensures stability; sparse networks for biological plausibility
  - Validated on inverted pendulum (cart-pole) control task
  - **Activation**: firing rate, model predictive control, MPC, planning, sparse network, contraction theory


File unchanged since last read. The content from the earlier read_file result in this conversation is still current — refer to that instead of re-reading.

## Neuroscience (New April 2026)

### mistake-gated-continual-learning
Mistake-gated learning for energy and memory efficient continual learning. Synaptic updates strictly gated by current and past classification errors, reducing updates by 50-80%. Biologically plausible, inspired by human negativity bias and error-related negativity (ERN). From arXiv:2604.14336v1.

**Activation**: mistake gating, continual learning, energy efficient, error-gated plasticity, negativity bias, ERN, synaptic update reduction

### neural-reference-resolution-program-code
Neural architectures for resolving references in program code using sequence-to-sequence models with direct and indirect indexing by permutation. Outperforms baselines in robustness and scalability, handling examples 10x longer. From arXiv:2604.14073v1.

**Activation**: neural code reference resolution, decompilation, sequence-to-sequence indexing, permutation indexing, program analysis

### gene-sharing-network-generative-model
Generative model for bipartite gene-sharing networks explaining evolutionary patterns in viruses and mobile genetic elements. Captures scale-free gene degree and exponential genome degree distributions via horizontal gene transfer, gene capture, and loss processes. From arXiv:2604.13963v1.

**Activation**: gene-sharing network, bipartite network evolution, viral genome evolution, pangenome modeling, horizontal gene transfer

### snn-working-memory-heterogeneous-delays
Working memory implementation in Spiking Neural Networks using heterogeneous synaptic delays. Recurrent SNN architecture with multi-delay synapses (D=41) for storing temporal patterns. From arXiv:2604.14096v1.

**Activation**: SNN working memory, synaptic delays, recurrent spiking, temporal pattern storage

### neuromorphic-spiking-ring-attractor
Neuromorphic Spiking Ring Attractor for proprioceptive joint-state estimation. Continuous attractor network with spiking neurons for robotic control using DYNAP-SE2. From arXiv:2604.14021v1.

**Activation**: ring attractor, spiking attractor, proprioceptive estimation, continuous attractor network

### spiking-memristor-multimodal
Multi-modal spiking functionalities in memristive neurons. Implements Time-to-First-Spike (TTFS), spike count, and firing rate encoding using Ag/HZO memristors for versatile neuromorphic hardware. From arXiv:2604.11780v1.

**Activation**: memristive neuron, TTFS encoding, multi-modal spiking, Ag/HZO memristor

### brain-digital-twins-execution-semantics
Brain digital twins execution semantics framework bridging computational neuroscience models and neuromorphic implementations. Formal execution semantics preserving temporal dynamics and causal relationships. From arXiv:2604.13574v1.

**Activation**: brain digital twin, execution semantics, neuro-neuromorphic, brain model execution

### sparse-neural-connectivity-recovery
Recover sparse neural connectivity from partial measurements using covariance-based approach with Granger-causality refinement. For neural circuit reconstruction from limited electrophysiological recordings. From arXiv:2603.18497v1.

**Activation**: sparse neural connectivity, covariance-based inference, Granger causality, circuit reconstruction

### ember-hybrid-snn-llm-architecture
EMBER hybrid cognitive architecture combining 220,000-neuron SNN with LLM. Uses STDP for continual learning without catastrophic forgetting. Places LLM as replaceable reasoning engine within persistent SNN memory substrate. From arXiv:2604.12167v1.

**Activation**: EMBER, hybrid SNN LLM, cognitive architecture, continual learning, brain-inspired AI

### maximum-heterogeneity-distributed-systems
Unifying principle showing maximum heterogeneity optimizes productivity in distributed systems. Applies to neural networks (efficient coding), economics (comparative advantage), and computing (resource allocation). From arXiv:2604.07602v1.

**Activation**: maximum heterogeneity, distributed systems, specialization, diversity optimization, efficient coding

### neuromorphic-spiking-ring-attractor
Neuromorphic Spiking Ring Attractor for proprioceptive joint-state estimation. Continuous attractor network with spiking neurons for robotic control. From arXiv:2604.14021v1.

**Activation**: ring attractor, spiking attractor, proprioceptive estimation, continuous attractor network

### dnn-guided-pso-optimization
Deep Neural Network-guided Particle Swarm Optimization for dynamic environments. DNNs predict optimum movements and detect environment changes. From arXiv:2604.14064v1.

**Activation**: DNN-guided PSO, dynamic optimization, particle swarm optimization, neural-guided optimization



---

## April 20, 2026 (Late Night) - Neuroscience Research

### NeuroFlow: Unified Visual Encoding-Decoding
- [[neuroflow-unified-visual-encoding-decoding]] - First unified fMRI↔natural image bidirectional mapping framework using Flow Matching (arXiv:2604.04338)
  - Cross-subject alignment module for individual heterogeneity
  - State-of-the-art on NSD dataset for both encoding and decoding
  - **Activation**: neuroflow, fMRI encoding decoding, visual reconstruction, flow matching, cross-subject alignment, brain-computer interface

### BrainCoDec: Meta-Learning In-Context Brain Decoding
- [[meta-learning-in-context-brain-decoding]] - Training-free cross-subject brain decoding via meta-learning in-context (arXiv:2604.04356)
  - Zero-shot adaptation to new subjects without training
  - Unified brain signal decoding foundation framework
  - **Activation**: braincodec, meta-learning, in-context learning, cross-subject decoding, zero-shot BCI, foundation framework

### Brain-DiT v5: Universal Multi-State fMRI Foundation Model
- [[brain-dit-fmri-foundation-model-v5]] - Heterogeneous modality integration + multi-scale temporal modeling (arXiv:2604.04856)
  - Unified fMRI foundation model supporting multi-state/multi-modal input
  - Heterogeneous modality integration for different acquisition protocols
  - Multi-scale temporal modeling from milliseconds to minutes
  - **Activation**: brain-dit v5, fMRI foundation model, heterogeneous modality, multi-scale temporal, universal brain model

### Dual-Timescale Memory: Spiking Neuron-Astrocyte Networks
- [[dual-timescale-memory-spiking-neuron-astrocyte-network-efficient]] - Neuron-astrocyte dual-timescale memory for efficient spatio-temporal learning (arXiv:2604.14361)
  - Fast neuronal timescale (ms) + slow glial timescale (sec)
  - Biology-inspired memory system mimicking hippocampal function
  - Efficient temporal pattern recognition
  - **Activation**: dual-timescale memory, neuron-astrocyte network, spatio-temporal learning, hippocampal memory, glial modulation



## April 18, 2026 Additions (Cron Job - Latest Neuroscience Research)

### SNN Quantization & Deployment
- [[snn-quantization-beyond-accuracy]] - Earth Mover's Distance for evaluating SNN quantization quality beyond accuracy (arXiv:2604.14487)

### Spiking Neural Networks & Noise
- [[noisy-snn-learning]] - Noise-driven learning in SNNs, leveraging stochasticity as computational resource (arXiv:2604.12060)

### SNN Working Memory
- [[snn-working-memory-heterogeneous-delays-v3]] - Working memory with heterogeneous synaptic delays in SNNs v3 (arXiv:2604.14096v3)

### Spiking Transformer
- [[wta-spiking-transformer-language]] - Winner-Take-All Spiking Transformer for energy-efficient language modeling (arXiv:2604.15004)

### Brain Foundation Models
- [[brain-mri-foundation-models]] - Self-supervised learning for brain MRI foundation models (arXiv:2604.15334)
- [[brain-mri-foundation-clinical]] - Brain MRI foundation model clinical deployment framework from FOMO25 (arXiv:2604.15334)
- [[brain-omnifunctional-foundation-model]] - Brain-OF omnifunctional foundation model for fMRI, EEG and neural signals (arXiv:2604.13373)

### Brain Digital Twins
- [[brain-digital-twins-execution-semantics-v3]] - Brain digital twins execution semantics v3 - bridging models to neuromorphic implementations (arXiv:2604.13574)

## April 17, 2026 Additions (Cron Job - Neuroscience Skills)

### New Skills from Latest arXiv Research (April 17, 2026)

#### SNN Working Memory with Heterogeneous Delays (v3)
- [[snn-working-memory-heterogeneous-delays-v3]] - **NEW** Working memory in recurrent SNNs with heterogeneous synaptic delays (arXiv:2604.14096v1, April 2026)
  - Weight tensor W ∈ R^(N×N×D) with D=41 delays per synapse
  - Surrogate-gradient backpropagation through time
  - Spiking Motifs representation for temporal patterns
  - F1 score of 1.0 on synthetic benchmarks
  - Energy-efficient neuromorphic implementation
  - **Activation**: working memory SNN, heterogeneous synaptic delays, spiking motifs, temporal pattern storage, recurrent SNN

#### MAGNet: Multi-Scale Adaptive Graph Network
- [[magnet-brain-structure-function-gnn]] - **NEW** Multi-scale adaptive graph attention for brain structure-function learning (arXiv:2603.29967v1, March 2026)
  - Source-Based Morphometry from structural MRI
  - Multi-head graph attention for structure-function coupling
  - Multi-scale hierarchical feature extraction
  - Transformer-style GNN architecture
  - Applications: Alzheimer's detection, cognitive state prediction
  - **Activation**: MAGNet, brain structure-function, graph neural network, brain imaging, cognitive insight, brain disorder diagnosis

#### Continual Learning for fMRI Brain Disorder Diagnosis
- [[continual-learning-fmri-brain-disorder]] - **NEW** Continual learning framework for fMRI-based brain disorder diagnosis (arXiv:2604.14259v1, April 2026)
  - Functional connectivity matrices generative replay
  - Prevents catastrophic forgetting in multi-site scenarios
  - VAE-based generator for synthetic FC matrices
  - Privacy-preserving (no raw data storage)
  - Task-incremental learning across clinical sites
  - **Activation**: continual learning, fMRI, brain disorder diagnosis, functional connectivity, generative replay, catastrophic forgetting

#### Brain Digital Twins Execution Semantics (v3)
- [[brain-digital-twins-execution-semantics-v3]] - **NEW** Brain digital twins execution semantics and neuro-neuromorphic systems (arXiv:2604.13574v1, April 2026)
  - Physically constrained executability framework
  - Execution semantics preservation across platforms
  - Cross-platform: CPU → GPU → Neuromorphic (Loihi, TrueNorth)
  - Formal model specification with state transitions
  - Semantic interoperability for brain models
  - **Activation**: brain digital twins, execution semantics, neuromorphic systems, neuro-neuromorphic, brain model execution

### Foundation Models & fMRI (NEW - April 17, 2026)
- [[brain-dit-universal-multi-state-fmri]] - **NEW** Brain-DiT universal multi-state fMRI foundation model (arXiv:2604.12683v1)
  - Pretrained on 349,898 sessions from 24 datasets
  - Covers resting, task, naturalistic, disease, sleep states
  - Metadata-conditioned diffusion pretraining with DiT
  - Multi-scale representations (fine-grained + global)
  - **Activation**: brain-dit, fMRI foundation model, multi-state brain, metadata-conditioned pretraining, diffusion transformer brain

### Developmental Neuroscience (NEW - April 17, 2026)
- [[developmental-minimal-neural-circuits]] - **NEW** Developmental generation of minimal neural circuits (arXiv:2604.15143v1)
  - Cortical neurogenesis from single stem cell simulation
  - Gene regulatory rules from mouse scRNA-seq
  - 85 neurons from 5,000 cells (1.7%) with dense connectivity
  - 90%+ MNIST accuracy after single epoch
  - Domain-general substrate (40.53% CIFAR-10)
  - **Activation**: developmental neurogenesis, minimal neural circuits, gene regulatory networks, structural priors

### Brain Digital Twins (NEW - April 17, 2026)
- [[brain-digital-twins-execution-semantics-v2]] - **NEW** Brain digital twins execution semantics framework (arXiv:2604.13574v1)
  - Physically constrained executability taxonomy
  - Execution regimes: offline → co-simulation → digital twins → neuro-neuromorphic
  - Semantic interoperability for brain models
  - Hybrid-time correctness
  - **Activation**: brain digital twins, execution semantics, neuromorphic systems, neuro-neuromorphic, hybrid-time

### Spiking Neural Networks & Working Memory (NEW - April 17, 2026)
- [[snn-working-memory-heterogeneous-delays-v2]] - **NEW** Working memory in recurrent SNNs with heterogeneous synaptic delays (arXiv:2604.14096v1)
  - Recurrent SNN with D=41 delay steps per synapse
  - 3D weight tensor W ∈ R^(N×N×D) implementation
  - Eligibility propagation for supervised learning
  - Biological alignment with prefrontal cortex dynamics
  - **Activation**: working memory SNN, heterogeneous synaptic delays, eligibility propagation, temporal pattern storage

- [[neuromorphic-spiking-ring-attractor-v2]] - **NEW** Neuromorphic spiking ring-attractor for proprioceptive joint-state estimation (arXiv:2604.14021v1)
  - Intel Loihi neuromorphic processor implementation
  - Continuous attractor with E/I balanced populations
  - Muscle spindle feedback integration
  - Energy-efficient robotic control (1000x power reduction)
  - **Activation**: spiking ring attractor, proprioceptive estimation, Loihi neuromorphic, continuous attractor, joint-state encoding

## April 17, 2026 (Evening) - Neuroscience Research Summary

### Brain-AI Alignment & VLM Robustness
- [[vlm-visual-cortex-alignment-robustness]] - V1-V3 visual cortex alignment shields VLMs from sycophantic manipulation (arXiv:2604.13803v1, April 15, 2026)
  - Early visual cortex alignment is reliable negative predictor of sycophancy (r = -0.441)
  - Strongest effect for existence denial attacks (r = -0.597, p = 0.040)
  - 12 VLMs evaluated (6 architecture families, 256M-10B parameters)
  - Brain alignment measured via fMRI predictivity on Natural Scenes Dataset
  - **Activation**: visual cortex, V1 V2 V3, brain alignment, sycophancy, adversarial robustness, fMRI predictivity, neural encoding

### Representation Theory
- [[representation-usefulness-framework]] - Representation use and usability across philosophy, neuroscience, cognitive science, and AI (arXiv:2604.13829v1, April 15, 2026)
  - Four aspects: information, usefulness, format usability, actual usage
  - Cross-disciplinary integration of representation concepts
  - Information carrying is necessary but NOT sufficient
  - Representations are for action, not just mirroring the world
  - **Activation**: representation theory, mental representation, cognitive representation, neural representation, embodied cognition, situated cognition, AI representation

### EEG & Visual Attention BCI
- [[eeg-visual-attention-decoding]] - Eccentricity confound in EEG-based visual attention decoding (arXiv:2604.15223v1, April 16, 2026)
  - Visual eccentricity affects neural responses in gaze-fixated paradigms
  - Neural tracking works under gaze fixation but degrades with eccentricity
  - Coupling strength alone doesn't reflect attention levels
  - Match-mismatch decoding with eccentricity control
  - **Activation**: EEG attention decoding, visual attention BCI, eccentricity confound, neural tracking, gaze fixation, natural video viewing

### Complex Systems & Network Dynamics
- [[heterophily-synergistic-interdependencies]] - Heterophily as generative mechanism for self-organized synergy (arXiv:2604.11545v1, April 13, 2026)
  - Heterophily is minimal local adaptive mechanism for synergy emergence
  - Weakens pairwise dependencies while inducing high-order dependencies
  - Spin-glass model with co-evolving couplings
  - Applications: brain networks, societies, ecosystems
  - **Activation**: heterophily synergy, self-organized interdependencies, high-order dependencies, neural synergy, adaptive networks

### Other SNN Research
- [[snn-internal-noise-analysis]] - Analysis of additive and multiplicative noise in SNNs with filtering strategies (arXiv:2604.13612)
- [[self-sustained-neural-population]] - Self-sustained neuron populations without external stimulus using Hodgkin-Huxley and STDP (arXiv:2604.13719)

### Mistake-Gated Continual Learning (NEW - April 18, 2026)
- [[mistake-gated-continual-learning]] - **NEW** Error-gated synaptic plasticity reduces updates by 50-80%. Inspired by human negativity bias and error-related negativity (ERN). Biologically plausible, no extra hyperparameters. From arXiv:2604.14336v1.
  - Only update synaptic weights when prediction error occurs
  - Memorized version gates on current AND past classification errors
  - Reduces storage buffer requirements for online learning
  - Suitable for incremental learning and neuromorphic deployment
  - **Activation**: mistake gating, continual learning, error-gated plasticity, negativity bias, ERN, energy efficient learning

### Brain Digital Twins & Neuromorphic Systems
- [[brain-digital-twins-execution]] - Execution semantics framework for brain models to neuromorphic implementations (arXiv:2604.13574)

### Previous Additions

### Brain Decoding & fMRI
- [[meta-learning-in-context-enables-training-free-cross-subject]] - Training-free cross-subject brain decoding using meta-learning in-context learning
- [[computational-lesions-multilingual-language-models-separate]] - Computational lesions in multilingual LLMs for brain alignment analysis

### EEG & Visual Reconstruction
- [[eeg2vision-multimodal-eeg-based-framework-visual-reconstruction]] - Multimodal EEG-based framework for 2D visual reconstruction

### Brain-to-Speech
- [[brain-to-speech-prosody-feature-engineering-transformer-based-reconstruction]] - Brain-to-speech synthesis with prosody feature engineering

### Memory & Embodied AI
- [[human-inspired-context-selective-multimodal-memory-social-robots]] - Human-inspired context-selective multimodal memory for social robots

## April 16, 2026 Additions

### Brain Decoding & fMRI
- [[meta-learning-in-context-brain-decoding-v3]] - Zero-shot cross-subject fMRI decoding using meta-learning

### Distributed Systems & Theory
- [[maximum-heterogeneity-principle-v2]] - Principle of Maximum Heterogeneity across biology, economics, computing

### Spiking Neural Networks
- [[snn-working-memory-heterogeneous-delays-v2]] - Working memory with heterogeneous synaptic delays in SNNs
- [[parallelized-hierarchical-connectome-phc]] - PHC framework for spatiotemporal spiking SSMs

### Neural Control
- [[neuromodulation-rhythmic-pattern-control-v2]] - Neuromodulation for CPG rhythmic pattern transitions

## April 18, 2026 Additions (Cron Job - Latest Neuroscience Research)

### EEG & Seizure Detection
- [[irene-eeg-seizure-detection]] - Information Bottleneck-guided EEG Seizure Detection via Self-Supervised Learning. Jointly learns denoised dynamic graph structures and informative spatial-temporal representations. Accepted at IEEE ICHI 2026. (arXiv:2604.01595)

### SNN Quantization & Deployment
- [[snn-quantization-beyond-accuracy]] - Earth Mover's Distance for evaluating SNN quantization quality beyond accuracy (arXiv:2604.14487)

### Spiking Neural Networks & Noise
- [[noisy-snn-learning]] - Noise-driven learning in SNNs, leveraging stochasticity as computational resource (arXiv:2604.12060)

### SNN Working Memory
- [[snn-working-memory-heterogeneous-delays-v3]] - Working memory with heterogeneous synaptic delays in SNNs v3 (arXiv:2604.14096v3)

### Spiking Transformer
- [[wta-spiking-transformer-language]] - Winner-Take-All Spiking Transformer for energy-efficient language modeling (arXiv:2604.15004)


## 2026-04-19 Update - New Skills

### warped-hierarchical-modular-neural-network
- **Title**: Relaxing Warped Spaces — Generalized Hierarchical Modular Neural Networks
- **Description**: Generalized hierarchical and modular dynamical neural network model with warped state space dynamics, enabling flexible topology and adaptive modular organization
- **Keywords**: warped spaces, hierarchical, modular, dynamical neural networks, state space, topology

### nonlinear-separation-principle
- **Title**: Nonlinear Separation Principle for Recurrent Neural Networks using Contraction
- **Description**: Nonlinear separation principle for RNNs using contraction theory, enabling separation of dynamics into task-relevant and task-irrelevant components
- **Keywords**: contraction theory, RNN, separation principle, dynamics, control

### thermocoherent-neural-dynamics
- **Title**: Thermocoherent Framework for Information Flow in Neural Matter
- **Description**: Thermocoherent framework analyzing neural dynamics through information-theoretic and thermodynamic lenses
- **Keywords**: thermodynamics, information flow, neural dynamics, coherence


## 2026-04-21 Update - New Neuroscience Skills (Cron Job)

### wasserstein-hebbian-plasticity
- **Title**: A Wasserstein Geometric Framework for Hebbian Plasticity
- **Author**: Ulrich Tan
- **Description**: Memory states modeled as probability measures evolving through Wasserstein mini-batch gradient descent. Bridges optimal transport theory with synaptic plasticity mechanisms.
- **arXiv**: 2604.16052v1
- **Keywords**: wasserstein geometry, hebbian learning, optimal transport, probability measures, gradient flow, synaptic plasticity

### ember-hybrid-snn-llm-architecture
- **Title**: EMBER: Autonomous Cognitive Behaviour from Learned SNN Dynamics in Hybrid LLM Architecture
- **Author**: William Savage
- **Description**: Experience-Modulated Biologically-inspired Emergent Reasoning - integrates learned SNN dynamics as memory and reasoning system with LLM. Bidirectional modulation between systems.
- **arXiv**: 2604.12167v1
- **Keywords**: hybrid llm snn, EMBER, experience modulation, autonomous cognition, emergent reasoning, biologically inspired

### kuramoto-phase-encoding
- **Title**: Kuramoto Oscillatory Phase Encoding: Neuro-inspired Synchronization for Improved Learning Efficiency
- **Authors**: Mingqing Xiao, Yansen Wang, Dongqi Han, Caihua Shan, Dongsheng Li
- **Description**: Phase-based neural encoding using Kuramoto oscillator dynamics for feature binding and temporal coordination. Synchronization dynamics for improved learning efficiency.
- **arXiv**: 2604.07904v1
- **Keywords**: kuramoto model, phase encoding, KoPE, oscillator synchronization, feature binding, neuro-inspired learning

### autoregressive-flow-matching-neural
- **Title**: Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching
- **Authors**: Nicole Rogalla, Yuzhen Qin, Mario Senden, Ahmed El-Gazzar, Marcel van Gerven
- **Description**: Forecasts neural activity in response to naturalistic stimuli using autoregressive flow matching. Generates realistic neural activity trajectories with uncertainty quantification.
- **arXiv**: 2604.11178v1
- **Keywords**: flow matching, neural dynamics prediction, autoregressive, probabilistic forecasting, naturalistic stimuli

### working-memory-recurrent-spiking-neural-networks
- **Title**: Working Memory in Recurrent SNN with Heterogeneous Synaptic Delays
- **Author**: Laurent U Perrinet
- **Description**: Working memory implemented using heterogeneous synaptic delays as computational resource. Memory encoded in delay structure rather than persistent firing.
- **arXiv**: 2604.14096v1
- **Keywords**: working memory, heterogeneous delays, recurrent SNN, temporal pattern storage, delay-based coding

### intrinsic-neurosynaptic-spiking-memristive
- **Title**: Intrinsic Neuro-Synaptic Spiking Dynamics in Self-Organizing Memristive Networks
- **Description**: Self-organizing memristive networks generating neuronal population dynamics through intrinsic neuro-synaptic dynamics. Emergent spiking behaviors without external control.
- **arXiv**: 2604.18015
- **Keywords**: memristive networks, self-organizing, spiking dynamics, neuro-synaptic, emergent behavior, neuromorphic

### ember-autonomous-cognitive-behaviour-learned-spiking
- **Title**: EMBER: Autonomous Cognitive Behaviour from Learned Spiking Network Dynamics
- **Author**: William Savage
- **Description**: Experience-Modulated Biologically-inspired Emergent Reasoning - learned SNN dynamics enabling autonomous cognitive behaviour in hybrid architecture.
- **arXiv**: 2604.12167
- **Keywords**: EMBER, autonomous cognition, spiking networks, learned dynamics, experience modulation

### integer-state-dynamics
- **Title**: Integer-State Dynamics of Quantized Spiking Neural Networks
- **Description**: Analysis of quantized SNN dynamics showing integer-state representations enable efficient hardware implementation while preserving computational properties.
- **arXiv**: 2604.01042
- **Keywords**: quantized SNN, integer states, hardware implementation, spike quantization, energy-efficient

### continual-learning-fmri-generative-replay
- **Title**: Continual Learning for fMRI-Based Brain Disorder Diagnosis Using Generative Replay
- **Description**: Continual learning framework using generative replay for fMRI brain disorder diagnosis. Prevents catastrophic forgetting across multiple diagnostic tasks.
- **arXiv**: 2604.14259
- **Keywords**: continual learning, fMRI, generative replay, brain disorder, catastrophic forgetting

### energy-based-neurocomputation
- **Title**: Energy-Based Dynamical Models for Neurocomputation, Learning, and Control
- **Description**: Unified energy-based framework connecting dynamical systems theory, neurocomputation, and optimal control. Energy functionals as organizing principle.
- **arXiv**: 2604.05042
- **Keywords**: energy-based models, neurocomputation, dynamical systems, learning rules, optimal control

### tta-eeg-foundation-models
- **Title**: Test-Time Adaptation for EEG Foundation Models
- **Description**: Test-time adaptation methods for EEG foundation models enabling rapid calibration-free deployment across subjects and sessions.
- **arXiv**: 2604.16926
- **Keywords**: test-time adaptation, EEG, foundation model, cross-subject, calibration-free

### learning-hippo-biologically-detailed-ca3
- **Title**: Learning Hippocampus: Biologically Detailed CA3 Auto-Associative Memory
- **Authors**: Daniele Corradetti, Renato Corradetti
- **Description**: Biologically detailed CA3 auto-associative memory model enabling learning through hippocampal-inspired mechanisms with realistic neuron dynamics.
- **arXiv**: 2604.20679
- **Keywords**: hippocampus, CA3, auto-associative memory, biologically detailed, learning

