## 2026-05-29 - Neuroscience Research (Cron Job)

### Meta-Cognitive Memory Policy Optimization for Long-Horizon LLM Agents
- [[mmpo-metacognitive-memory-policy]] - Belief Entropy 作为自监督代理优化 LLM agents 内存策略，在 1.75M-token 上下文保持 97.1% 性能 (arXiv: 2605.30159)
  - 引入 Belief Entropy 量化隐任务状态不确定性
  - 提供细粒度内存级监督而非仅 outcome-based RL
  - 防止信念偏差导致的长期推理崩溃
  - **Activation**: memory policy optimization, belief entropy, long-horizon LLM agent

### Embodied VR Feedback Reshapes Neural Representations for 3D Motor Imagery BCI
- [[embodied-vr-feedback-3d-motor-imagery-bci]] - 具身 VR 反馈在连续 3D 运动想象 BCI 中达到 76.2% 相关性，显著优于屏幕反馈 (arXiv: 2605.29677)
  - 具身空间反馈产生更可解码且可泛化的神经表征
  - VR 引起更强的感觉运动-顶叶去同步化
  - 激活前岛叶（具身自我意识）和顶叶耦合
  - **Activation**: embodied VR feedback, 3D motor imagery BCI, continuous BCI

### Mind-Omni: Unified Multi-Task Framework for Brain-Vision-Language
- [[mind-omni-brain-vision-language-unified]] - 首个统一 7 个 BCI 编码/解码任务的离散扩散框架，Brain Tokenizer 实现跨模态交互 (arXiv: 2605.29591)
  - Brain Tokenizer 将连续脑信号转化为离散 tokens
  - 离散扩散实现脑-视觉-语言统一建模
  - BQA 数据集解锁神经推理能力
  - **Activation**: Mind-Omni, Brain Tokenizer, brain vision language model
     1|
     2|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
     3|
     4|### Prime Number Identification Demonstrated with Quantum Processors
     5|- [[quantum-prime-identification]] - 量子处理器上基于纠缠动力学的素数识别协议，链接素性与傅里叶分量 (arXiv: 2605.28964)
     6|  - 核心要点: 从论文提炼的复用技能模式
     7|  - **Activation**: quantum, prime, identification
     8|
     9|### Quantum encodings that preserve persistent homology
    10|- [[quantum-persistent-homology-encoding]] - 保持持久同调拓扑特征的量子数据编码方法 (arXiv: 2605.28927)
    11|  - 核心要点: 从论文提炼的复用技能模式
    12|  - **Activation**: quantum, persistent, homology
    13|
    14|### Quantum Markovian Dynamics from a Double Covariance Stochastic Framework
    15|- [[quantum-markovian-stochastic-framework]] - 双协方差随机框架推导量子马尔可夫动力学的亚量子理论 (arXiv: 2605.29508)
    16|  - 核心要点: 从论文提炼的复用技能模式
    17|  - **Activation**: quantum, markovian, stochastic
    18|
    19|### A hidden bottleneck in classical and quantum linear reservoir computing
    20|- [[quantum-linear-reservoir-bottleneck]] - 线性和量子线性储备计算中的隐藏瓶颈分析 (arXiv: 2605.29071)
    21|  - 核心要点: 从论文提炼的复用技能模式
    22|  - **Activation**: quantum, linear, reservoir
    23|
    24|### Exponentially Fast Solution State Preparation for the Heat Equation and its use for Option Pricing
    25|- [[quantum-option-pricing-heat-equation]] - 热方程指数快解态制备在金融期权定价中的应用 (arXiv: 2605.28950)
    26|  - 核心要点: 从论文提炼的复用技能模式
    27|  - **Activation**: quantum, option, pricing
    28|
    29|## 2026-05-29 - Neuroscience Research (Cron Job)
    30|
    31|### Mind-Omni: A Unified Multi-Task Framework for Brain-Vision-Language Modeling via Discrete Diffusion
    32|- [[mind-omni-brain-vision-language-unified]] - 首个统一脑-视觉-语言建模框架，通过Brain Tokenizer将异构脑信号转换为离散token，实现跨模态生成与理解 (arXiv: 2605.29591)
    33|  - 核心：Brain Tokenizer标准化连续脑信号为离散token，discrete diffusion paradigm实现跨模态交互
    34|  - 核心：统一7个编码/解码任务，建立神经活动基础模型范式，性能媲美专用模型
    35|  - **Activation**: Mind-Omni, brain vision language, neural tokenizer, discrete diffusion BCI, multimodal brain modeling, brain foundation model
    36|
    37|### Neural-Behavioral Representation of Natural Whole-body Movement in Monkeys
    38|- [[neural-behavioral-whole-body-movement-monkeys]] - 自由移动猴子的自然全身运动解码框架，结合大规模硬膜皮层信号与多视角运动捕捉 (arXiv: 2605.29355)
    39|  - 核心：自回归编码器-解码器学习紧凑行为先验，无需显式物理约束即可生成准确全身运动
    40|  - 核心：分布式感觉/运动区域皮层信号解码自然全身运动，首个无约束全身运动解码
    41|  - **Activation**: neural-behavioral, whole-body movement, monkey kinematics, epidural signals, motion capture decoding, behavior prior
    42|
    43|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics (Cron Job)
    44|
    45|### Learning to Maximize Quantum Neural Network Expressivity via Effective Rank
    46|- [[effective-rank-qnn-expressivity]] - Introduces effective rank (kappa) as quantitative measure of QNN expressivity, capturing independent variational parameters (arXiv: 2506.15375)
    47|  - Core: Effective rank measures true degrees of freedom in parameterized quantum circuits
    48|  - Low kappa correlates with barren plateau severity; serves as pre-training ansatz diagnostic
    49|  - **Activation**: effective rank, QNN expressivity, variational circuit design, barren plateau
    50|
    51|### On the Dynamical Lie Algebras of Quantum Approximate Optimization Algorithms
    52|- [[dynamical-lie-algebra-qaoa]] - Analyzes QAOA expressivity and optimization landscape through dynamical Lie algebra dimension (arXiv: 2407.12587)
    53|  - Core: DLA dimension determines reachable unitary space, barren plateau presence, and classical simulability
    54|  - Graph-dependent scaling: different problem structures yield different DLA dimensions
    55|  - **Activation**: dynamical Lie algebra, QAOA analysis, quantum circuit expressivity, variational algorithm theory
    56|
    57|### Emergent Operational Entanglement Graphs and Sub-Quadratic Authentication Scaling
    58|- [[emergent-entanglement-graphs]] - Studies emergent entanglement structures in quantum networks enabling sub-quadratic QKD authentication (arXiv: 2605.27434)
    59|  - Core: Operational entanglement graphs differ from physical topology due to swapping/purification
    60|  - Graph properties provide security certificates and optimize authentication overhead
    61|  - **Activation**: entanglement graphs, QKD authentication, quantum network topology, quantum communication security
    62|
    63|### EFaaS: A Quantum-Classical Serverless Entangled Scheduler for Hybrid Variational Algorithms
    64|- [[qlass-serverless-entangled-scheduler]] - Serverless orchestration of quantum circuit evaluations for hybrid variational algorithms (arXiv: 2605.27540)
    65|  - Core: Treats quantum circuit evaluations as serverless functions with entanglement-aware scheduling
    66|  - Reduces classical-quantum communication overhead through batching and adaptive parallelism
    67|  - **Activation**: quantum serverless, EFaaS, hybrid variational scheduling, quantum-classical orchestration
    68|
    69|### Improved sample complexity bound for sample-based Lindbladian simulation
    70|- [[lindblad-sample-complexity]] - 林德布拉德模拟的显式非渐近采样复杂度界，维数依赖从 O(d²t²/ε) 改进到 O(d·||L||²t²/ε) (arXiv: 2605.30301)
    71|  - 核心要点：对随机 Lindblad 算子，当 ||L||²_∞ = O(1/d) 时采样复杂度与维数无关 O(t²/ε)
    72|  - 核心要点：显式非渐近界 n*_d(t,ε) ≤ ((2d+3)/8)||L||²_∞(t²/ε)
    73|  - **Activation**: Lindbladian simulation, sample complexity quantum, Wave Matrix Lindbladization, open quantum system, 林德布拉德模拟
    74|
    75|### Koopman-von Neumann Molecular Dynamics for Green-Kubo Transport Coefficients
    76|- [[koopman-quantum-molecular-dynamics]] - 将经典分子动力学的 Green-Kubo 输运系数表述为量子算法读出问题 (arXiv: 2605.30142)
    77|  - 核心要点：NVE/NVT 动力学导出为希尔伯特空间上的幺正演化，网格误差随寄存器位数指数衰减
    78|  - 核心要点：目标精度 ε 仅需 O(log(1/ε)) 量子位，实现对数级量子位缩放
    79|  - **Activation**: Koopman-von Neumann, Green-Kubo, quantum molecular dynamics, transport coefficient, KvN quantum algorithm
    80|
    81|### Quantum Synchronization of Fock States
    82|- [[quantum-synchronization-fock-states]] - 玻色模式的量子同步，展示负 Wigner 函数稳态下的 Arnold tongue 相位锁定 (arXiv: 2605.30271)
    83|  - 核心要点：非经典态可与外部驱动实现相位锁定，相滑移概率指数衰减
    84|  - 核心要点：从 Lindblad 时间演化中提取相滑移率的新方法
    85|  - **Activation**: quantum synchronization, Fock states, Lindblad evolution, phase slip rate, Arnold tongue
    86|
    87|### Qubit-efficient variational algorithm for nuclear structure
    88|- [[qubit-efficient-vqe-nuclear]] - VQE 中三种量子位映射策略比较，用于核基态研究 (arXiv: 2605.30261)
    89|  - 核心要点：比较粒子基、Slater 行列式基、量子位高效映射在 10B 核上的资源需求
    90|  - 核心要点：扩展到 12C 核，在噪声模拟器上运行高达 26 量子位电路
    91|  - **Activation**: VQE nuclear structure, qubit-efficient mapping, variational quantum eigensolver, nuclear ground state
    92|
    93|### Overcoming the Matrix-Product-State Encoding Barrier via DMRG-Guided PITE
    94|- [[mps-dmrg-encoding-quantum]] - 三阶段基态准备框架：DMRG 获取 MPS 后经 MPD 编码到量子寄存器 (arXiv: 2605.30141)
    95|  - 核心要点：MPS 编码期间中心键 Schmidt 秩呈 logistic 增长，拐点 L* 标记高效编码边界
    96|  - 核心要点：概率虚时演化 (PITE) 减少编码残差
    97|  - **Activation**: MPS encoding, DMRG, probabilistic imaginary-time evolution, ground state preparation, quantum state preparation
    98|
    99|
   100|## 2026-05-29 - Neuroscience Research (Cron Job)
   101|