     1|

## 2026-05-28 - Quantum Computing Research (Cron Job)

### Neural Quantum Spectral Operator Learning for Solving Partial Differential Equations
- [[neural-quantum-spectral-operator-pde]] - First hybrid quantum-classical operator learning framework using Legendre-Galerkin weak formulation for parametric PDEs, Neural Variational Quantum Linear Solver (NVQLS) with sign ambiguity resolution and neural embedding encoding (arXiv: 2605.27408)
  - 核心创新：Legendre-Galerkin量子线性求解器 + 神经嵌入参数编码
  - 计算优势：理论复杂度降低 + 高维PDE量子加速潜力
  - 关键应用：参数化PDE求解、工程系统建模、实时代理模型
  - 实验验证：1D/2D PDE超越经典神经网络算子基线精度
  - **Activation**: quantum operator learning, VQLS, quantum PDE solver, quantum spectral method, neural embedding quantum, hybrid quantum-classical operator

## 2026-05-28 - Neuroscience Research (Cron Job)

### Brain State Transition Network Control: Structural Controllability and Energy Dynamics
- [[brain-state-transition-network-control]] - 脑状态转移动力学与网络控制方法论，基于网络控制理论计算平均可控性、模态可控性、最小控制能量等指标，研究脑网络状态转移的能量需求与动态特性 (理论框架)
  - 核心概念：网络可控性、平均可控性、模态可控性、最小控制能量
  - 关键应用：脑区功能角色分析、任务切换能量预测、神经调控策略设计
  - 节点角色分类：Integration Hub（前额叶/顶叶）、Specific Controller（感觉运动区）、Passive Node
  - 能量不对称性：状态转移具有方向不对称（某些状态易到达难退出）
  - **Activation**: brain state transition, network control, controllability, control energy, brain dynamics, structural connectome, functional connectome, 控制理论, 状态转移, 脑网络控制

### Neural Code Dynamics Analysis: Critical State, Information Geometry, and Dynamical Invariants
- [[neural-code-dynamics-analysis]] - 神经编码动力学分析框架，整合计算神经科学、机器学习和临界态理论，研究生物与人工神经网络编码表示动力学，涵盖临界脑假说、雪崩动力学、信息几何与动力学不变量 (综合框架)
  - 临界脑假说：雪崩幂律分布（α ≈ 1.5）、分支比率（σ ≈ 1）、Lyapunov 指数（λ ≈ 0）
  - 信息几何：Fisher 信息矩阵、Fisher-Rao 几何距离、表示曲率分析
  - 动力学不变量：Lyapunov 指数、Kolmogorov 复杂度、Hurst 指数、样本熵、Permutation 熵
  - 神经表示学习：RSA 对齐分析、表示距离度量、动态模式提取
  - 关键发现：临界态同时最大化信息传输和动态范围；不同认知状态临界指数可调
  - **Activation**: neural coding, dynamics analysis, critical brain hypothesis, avalanche dynamics, information geometry, dynamical invariants, neural representation, encoding dynamics, computational neuroscience

     2|## 2026-05-28 - Systems Engineering + Quantum (Cron Job)
     3|
     4|### Rigorous error bounds for dissipative thermal state preparation from weak system-bath coupling
     5|- [[dissipative-thermal-state-prep]] - Error-bounded thermal state preparation using collision models with J^2-controlled Lamb shift (arXiv: 2605.03011)
     6|  - Lamb shift error scales as J^2, tunable via system-bath coupling strength
     7|  - Randomized drive suppresses spectral resonances with many-body spectrum
     8|  - Practical protocol for NISQ hardware with shallow collision circuits
     9|  - **Activation**: thermal state preparation, dissipative lindbladian, collision model quantum, system-bath coupling error bounds
    10|
    11|### Ensemble Engineering to Overcome Destructive Cancellation in Quantum Measurements
    12|- [[ensemble-engineering-quantum]] - Mitigate destructive cancellation in NISQ measurements via engineered sampling distributions (arXiv: 2605.03729)
    13|  - Reformulate correlators in basis-resolved representation to expose cancellation structure
    14|  - Grover-type amplitude amplification and oracle-free shallow circuit constructions
    15|  - Trade-off between amplification strength and noise robustness on IBM 20-qubit processors
    16|  - **Activation**: quantum ensemble engineering, destructive cancellation, NISQ measurement efficiency
    17|
    18|### Trustworthy Quantum Machine Learning: A Roadmap for Reliability, Robustness, and Security
    19|- [[trustworthy-qml-roadmap]] - Comprehensive roadmap for trustworthy QML in the NISQ era (arXiv: 2511.02602)
    20|  - Covers reliability, robustness, and security for QML deployment
    21|  - Addresses probabilistic quantum mechanics risks and device noise
    22|  - Hybrid quantum-classical execution pipeline risk analysis
    23|  - **Activation**: trustworthy quantum ML, QML reliability, NISQ security, quantum robustness
    24|
    25|### Quantum Reliability
    26|- [[quantum-reliability-pathways]] - Framework for assessing reliability of quantum devices (arXiv: 2305.08461)
    27|  - Systematic metric for quantum reliability and its loss
    28|  - Extends classical reliability theory to quantum devices
    29|  - **Activation**: quantum reliability, quantum device assessment
    30|
    31|### Introduction to quantum control: From basic concepts to applications
    32|- [[quantum-control-engineering]] - Tutorial on classical electromagnetic field control of quantum systems (arXiv: 2512.04990)
    33|  - Use of classical EM fields to steer quantum system dynamics
    34|  - Exploits destructive/constructive interference for control targets
    35|  - **Activation**: quantum control, electromagnetic control, quantum steering
    36|
    37|### QBalance: Multi-Objective Workflow for Quantum Compilation
    38|- [[qbalance-quantum-workflow-optimization]] - Reproducible workflow for quantum compilation, noise suppression, and error mitigation (arXiv: 2605.02966)
    39|  - Multi-objective optimization of compilation strategy selection
    40|  - Noise suppression and error mitigation strategy selection
    41|  - **Activation**: quantum workflow optimization, compilation strategy, noise suppression
    42|
    43|### Towards Scalable Quaternary Message-Passing Decoding for QEC
    44|- [[scalable-quaternary-mp-qec-decoding]] - Quaternary Min-Sum decoder with dilution achieving 16% threshold up to distance 20 (arXiv: 2605.24177)
    45|  - Graph-dilution method for scalable MP decoding
    46|  - O(N log^2 d) worst-case complexity, outperforms BP-OSD at d=65
    47|  - **Activation**: quantum error correction decoding, message passing decoder, quaternary belief propagation
    48|
    49|### Operating a bistable qubit
    50|- [[operating-bistable-qubit]] - Adaptive feedback control for bistable qubit operation (arXiv: 2605.03187)
    51|
### QuCtrl-BELL: Compiler-Driven Sub-Microsecond Feedback Control Stack
- [[quantum-compiler-feedback]] - 编译器驱动的亚微秒反馈控制栈，用于可扩展量子计算。通过Python嵌入式DSL、六阶段转译流水线和跨板同步（<700ns延迟），解决硬件耦合与软件模块化的权衡 (arXiv: 2605.22433)
  - 六阶段转译：CFG构建→SSA转换→活性分析→图着色寄存器分配→代码生成→步序表生成
  - 控制流解耦：将循环/分支/同步与硬件状态数据分离
  - RISC-V + PXIe部署验证：确定性时序和模块化可编程性
  - **Activation**: quantum compiler feedback, sub-microsecond quantum control, compiler-driven quantum, QuCtrl-BELL, trapped-ion control stack, DSL quantum programming

### VF-QCTRL: Physics-Informed LLM for General Quantum Control
- [[vf-qctrl-llm-quantum-control]] - 物理信息大语言模型框架用于通用量子控制，结合符号推理与优化提出解析控制ansätze并通过反馈迭代精炼，QCTRL-Bench涵盖16个任务 (arXiv: 2605.26021)
  - 符号+数值混合：LLM提出解析脉冲序列，数值优化精炼参数
  - 训练免费：无需微调，跨多种量子系统通用
  - 可解释性：直接从自然语言提示生成物理可解释的解析协议
  - **Activation**: physics-informed LLM quantum control, VF-QCTRL, analytic control ansatz, symbolic quantum control, LLM quantum protocol design, QCTRL-Bench

### Adaptive RL for Robust Open Quantum System Control
- [[rl-quantum-control]] - 多任务SAC强化学习框架用于开放量子系统控制，跨51种哈密顿量变体学习最优脉冲序列，RIM分析显示对脉冲幅度扰动和退相干率变化优于GRAPE (arXiv: 2605.26925)
  - 多任务SAC同时学习最优脉冲序列和问题特定的演化时间T和脉冲段数N
  - 渐进式训练哈密顿量集扩展实现未训练哈密顿量的泛化
  - 鲁棒性不保真度量(RIM)分析验证优于传统优化方法
  - **Activation**: RL quantum control, multi-task SAC quantum, robust open quantum control, adaptive quantum pulse learning, reinforcement learning quantum optimization

