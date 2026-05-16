## 2026-05-16 - Economics, Investment + Quantum Mechanics (Cron Job - 15:00)

### Learning PDEs for Portfolio Optimization with Quantum Physics-Informed Neural Networks
- [[quantum-pinn-portfolio-optimization]] - 量子物理信息神经网络求解组合优化PDE，将HJB方程编码为量子电路残差损失 (arXiv: 2604.03346)
  - 核心要点：用量子参数化电路作为价值函数ansatz，量子纠缠自然捕获跨资产相关性
  - 核心要点：通过参数平移规则计算PDE残差梯度，兼容NISQ设备浅层电路
  - 核心要点：可扩展到含交易成本、跳跃扩散市场等无解析解的高维场景
  - **Activation**: quantum PINN portfolio, QPINN finance, quantum PDE portfolio optimization, HJB quantum neural network, quantum stochastic control PDE

### Quantum Temporal Convolutional Neural Networks for Equity Prediction (Updated)
- [[quantum-tcnn-equity-prediction]] - 量子时间卷积神经网络横截面股票收益预测，JPX数据集Sharpe比率0.538，超越经典基线72% (arXiv: 2512.06630)
  - 核心要点：时间编码器提取多尺度技术指标模式，量子卷积层利用叠加/纠缠增强特征表示
  - 核心要点：参数量少于经典等效模型，有效抑制过拟合

### Quantum Computing for Financial Transformation (Review Updated)
- [[quantum-finance-stack-analysis]] - 金融计算五层堆栈：组合优化、衍生品定价、风险估计、量子ML、后量子密码学 (arXiv: 2604.08180)
  - 核心要点：近期最强案例是精心设计的混合量子-经典工作流
  - 核心要点：组合优化最可信（组合复杂性是约束成本），振幅估计对重复期望评估最有效

## 2026-05-16 - Economics, Investment + Quantum Mechanics (Cron Job - Hourly)

### Constrained Counterdiabatic Quantum Approximate Optimization Algorithm for Portfolio Optimization
- [[cd-qaoa-portfolio-optimization]] - 约束反绝热QAOA算法在固定电路深度下超越XY/Grover/惩罚混合器，实现更优组合优化近似比 (arXiv: 2605.06858)
  - 核心要点：通过嵌套对易子生成近似绝热规范势，融入变分ansatz提升约束满足
  - 核心要点：在固定深度p下，CCD-QAOA一致优于标准XY-mixer、Grover-mixer和惩罚式QAOA
  - **Activation**: CD-QAOA, counterdiabatic QAOA, constrained portfolio optimization, adiabatic gauge potential, XY mixer QAOA, quantum portfolio selection

### Two-Step QAOA for Portfolio Optimization
- [[two-step-qaoa-portfolio]] - 两步QAOA方法：经典筛选+量子优化，在NISQ设备上实现大规模组合优化 (arXiv: 2605.06858)
  - 核心要点：第一步用经典方法筛选候选资产子集，第二步在缩减空间运行QAOA分配权重
  - 核心要点：显著降低电路深度需求，同时保持与全量子方法相当的解质量
  - **Activation**: two-step QAOA, hybrid portfolio screening, NISQ portfolio optimization, classical quantum portfolio, asset subset screening

### 2026-05-16 - Economics, Investment + Quantum Mechanics (Cron Job - Afternoon)

### Hybrid Quantum Genetic Algorithm for Portfolio Optimization
- [[quantum-genetic-portfolio-optimization]] - 混合量子遗传算法在组合优化中比经典GA收敛更快，同时保持更高种群多样性 (arXiv: 2604.11667)
  - 核心要点：量子叠加态表示投资组合候选，通过量子旋转门演化向更优解
  - 核心要点：比暴力搜索显著更少的评估次数达到全局最优
  - **Activation**: quantum genetic algorithm portfolio, HQGA optimization, quantum evolutionary finance, 混合量子遗传组合优化

### The Cost of Quantum Resistance in Blockchain
- [[quantum-resistant-blockchain-economics]] - 后量子密码学过渡到区块链系统的经济影响分析，提出基于哈希的提交-揭示替代方案 (arXiv: 2605.06853)
  - 核心要点：SPHINCS+签名使区块链签名数据增加40-125倍，比特币每天增加约4GB
  - 核心要点：哈希提交-揭示方案在保持安全性的同时将近链上数据维持在当前水平
  - **Activation**: post-quantum blockchain cost, quantum resistant blockchain economics, SPHINCS+ blockchain overhead, hash commit reveal blockchain

### Quantum Computing for Financial Transformation
- [[quantum-finance-stack-analysis]] - 金融计算堆栈框架，系统化评估量子计算在金融五大领域（组合优化、衍生品定价、风险估计、量子ML、后量子密码学）的适用性 (arXiv: 2604.08180)
  - 核心要点：五层堆栈架构——组合优化(QAOA)、衍生品定价(振幅估计)、风险估计(稀有事件分析)、量子ML(任务依赖)、后量子密码学(战略必需)
  - 核心要点：近期最强案例是混合量子-经典工作流，而非纯量子优势声明
  - **Activation**: quantum finance stack, portfolio optimization quantum, derivative pricing quantum, risk estimation quantum, post-quantum cryptography finance, hybrid quantum workflows

### Quantum Temporal Convolutional Neural Networks for Equity Prediction
- [[quantum-tcnn-equity-prediction]] - 量子时间卷积神经网络用于横截面股票收益率预测，结合量子电路层与时间卷积网络 (arXiv: 2512.06630)
  - 核心要点：因果卷积保持时间顺序，量子电路层捕获非线性特征交互
  - 核心要点：使用秩信息系数(IC)评估预测能力，对比纯经典TCNN基线
  - **Activation**: quantum TCNN equity prediction, quantum temporal convolution stock, cross-sectional return prediction, quantum neural network finance

### Quantum Reservoir Computing for Stock Forecasting
- [[quantum-reservoir-stock-forecasting]] - 量子储备池计算方法用于股票市场走势预测，利用量子动力学系统处理时序金融数据 (arXiv: 2602.13094)
  - 核心要点：储备池固定不变，仅训练经典读出层，训练极简
  - 核心要点：量子纠缠自然产生丰富的特征混合，对噪声数据鲁棒
  - **Activation**: quantum reservoir computing stock, QRC forecasting, quantum dynamical system finance, stock movement prediction quantum

# 2026-05-16 - Neuroscience Research (Cron Job)

### Approximate Macroscopic Dynamics of Spiking Neural Networks Based on Solutions to the Transport Equation
- [[transport-mean-field-snn-dynamics]] - Transport-based mean field theory for SNN population dynamics (arXiv: 2605.14319)
  - Derives firing rate fluctuations from transport solutions to Fokker-Planck equation
  - Bridges microscopic integrate-and-fire to macroscopic population dynamics
  - **Activation**: transport equation, mean field, Fokker-Planck, firing rate fluctuations, SNN dynamics

### Multiple mechanisms of rhythm switching in recurrent neural networks with adaptive time constants
- [[rhythm-switching-adaptive-time-constants-rnn]] - Rhythm switching mechanisms in RNNs with learnable time constants (arXiv: 2605.14388)
  - Three coexisting mechanisms: subpopulation turnover, baseline shifts, phase reorganization
  - High-frequency rhythms dominated by short-time-constant neuron subpopulations
  - **Activation**: rhythm switching, adaptive time constants, RNN dynamics, frequency bands, functional differentiation


## 2026-05-15 - Number Theory, Statistics, Mathematics + Quantum (Cron Job)

### Universal quantum resource distillation via composite generalised quantum Stein's lemma
- [[quantum-resource-distillation]] - Universal framework for quantum resource distillation via composite quantum Stein's lemma, establishing fundamental limits on resource conversion rates (arXiv: 2605.15174)
  - Core: Quantum resource theories with free states F, free operations O; distillation rate bounded by Stein's bound R* = inf_σ∈F D(ρ||σ)
  - Composite settings: Rate = min_k inf_{σ∈F_k} D(ρ||σ) over union of convex free state families
  - Applications: Entanglement distillation, coherence theory, quantum thermodynamics
  - **Activation**: quantum resource distillation, quantum Stein's lemma, entanglement distillation rate, resource conversion, composite hypothesis testing

### QSeqSim: A Symbolic Simulator for Qiskit While Loops Using Sequential Quantum Circuits
- [[quantum-symbolic-simulation]] - Symbolic simulation methodology for quantum circuits with unbounded iteration (while loops) via sequential quantum circuits (arXiv: 2605.14881)
  - Core: Represents while-loop quantum programs symbolically as SQCs, enabling simulation of unbounded iteration
  - Convergence analysis: Truncation at K iterations with error ≤ (1-p)^K for exit probability p
  - Applications: Adaptive quantum algorithms, quantum error correction with repeated syndrome measurement
  - **Activation**: quantum while loop, symbolic quantum simulation, Qiskit sequential circuit, QSeqSim, quantum program verification

### Scalable self-testing of generic multipartite quantum states
- [[scalable-quantum-self-testing]] - Device-independent certification of multipartite quantum states from observed statistics alone (arXiv: 2605.15106)
  - Core: Self-testing identifies quantum state |ψ⟩ and measurements {M} from correlations P(a|x) up to local isometries
  - Bell functional construction: β(P) ≥ β_Q - ε implies ε-close to target state
  - Robustness bounds: Graph states O(√ε), GHZ states O(ε^{1/4}), cluster states O(√ε)
  - **Activation**: quantum self-testing, device-independent certification, multipartite entanglement verification, Bell inequality certification, scalable self-testing


## 2026-05-14 - Systems Engineering + Quantum (Cron Job)

### QBalance: A Reproducible Multi-Objective Workflow for Quantum Compilation, Noise Suppression, and Error-Mitigation Strategy Selection
- [[qbalance-workflow-optimization]] - Multi-objective quantum workflow optimization with Pareto strategy selection, survival-product error proxy, and Bayesian surrogate ordering (arXiv: 2605.02966)
  - Core: Weighted objective (fidelity/cost/time/reproducibility) for NISQ quantum compilation strategy selection
  - Pareto-optimal non-dominated selection across compilation, noise suppression, and error mitigation strategies
  - Bayesian linear surrogate + Thompson sampling for expensive strategy evaluation ordering
  - **Activation**: qbalance, quantum workflow optimization, quantum compilation strategy, noise suppression selection, error mitigation, multi-objective quantum


### Dynamic Quantum-Assisted Co-Design of Control Tuning and Lyapunov Stability Synthesis
- [[quantum-control-systems]] - Joint quantum-classical co-design framework for nonlinear system control with Lyapunov stability certificates (arXiv: 2605.04296)
  - Quantum search over controller-stability product space for simultaneous optimization
  - Bridges QAOA/VQE quantum optimization with classical Lyapunov synthesis
  - Exponential speedup for certain control design space exploration problems
  - **Activation**: quantum control, Lyapunov stability synthesis, quantum-assisted control, nonlinear system control, 量子控制合成


### Symplectic H2 Model Reduction for High-Dimensional Linear Quantum Systems
- [[quantum-control-systems]] - Structure-preserving model order reduction for quantum systems using symplectic balancing (arXiv: 2605.11817)
  - Preserves canonical commutation relations during reduction
  - H2 norm-optimal approximation with symplectic structure guarantees
  - **Activation**: quantum model reduction, symplectic H2, quantum system approximation
