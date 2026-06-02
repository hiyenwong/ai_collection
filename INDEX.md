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