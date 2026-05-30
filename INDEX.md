

## 2026-05-30 - Economics, Investment + Quantum (Cron Job)

### Quantum Reinforcement Learning for Dynamic Portfolio Optimization
- [[quantum-rl-dynamic-portfolio]] - 量子强化学习(VQC)实现动态组合优化，QDDPG/QDQN量子变体比经典深度RL参数更少但性能相当 (arXiv: 2601.18811)
  - 核心要点 1: VQC替代经典神经网络作为策略/价值函数近似器，量子电路利用希尔伯特空间实现紧凑表征
  - 核心要点 2: 量子DDPG(连续动作)和量子DQN(离散动作)两种架构，在真实金融数据上与经典基线竞争
  - **Activation**: quantum reinforcement learning, QRL portfolio, VQC trading agent, QDDPG, QDQN, 量子强化学习, 动态组合优化

### Optimizing Carbon Credit Portfolios with QAOA+ZNE on IBM Quantum Hardware
- [[qaoa-zne-portfolio]] - QAOA结合零噪声外推(ZNE)在IBM量子硬件上优化88变量碳信用组合，超越经典贪心基线 (arXiv: 2602.09047)
  - 核心要点 1: ZNE误差缓解对NISQ硬件至关重要，通过门折叠和Richardson外推将噪声外推至零
  - 核心要点 2: 多目标优化(碳封存+生物多样性+社会影响)编码为QUBO，QAOA+ZNE在真实硬件上验证
  - **Activation**: QAOA ZNE, zero noise extrapolation, error mitigation, carbon credit portfolio, ESG quantum, 误差缓解, 碳信用组合

### Exponentially Fast Solution State Preparation for the Heat Equation and its use for Option Pricing
- [[quantum-option-pricing-heat-equation]] - 指数级加速热方程量子态制备，用于期权定价，路径依赖衍生品具有指数量子优势 (arXiv: 2605.28950)
  - 核心要点 1: 将Black-Scholes PDE转化为热方程，量子设备上直接制备解态
  - 核心要点 2: 路径依赖期权（亚式、障碍、回望）实现指数级量子比特优势
  - **Activation**: quantum option pricing, heat equation, Black-Scholes, 期权定价, 衍生品定价

### A Quantum Algorithm for Simulating Nonunitary Dynamics Governed by Nonautonomous Linear ODEs
- [[quantum-nonautonomous-ode-simulation]] - 量子算法模拟非自治ODE非幺正动力学，通过SVD分解将传播子写为酉算子之和 (arXiv: 2605.29052)
  - 核心要点 1: 解决量子硬件只能执行幺正变换的限制，实现非幺正动力学模拟
  - 核心要点 2: 应用于经济建模中的非自治线性微分方程
  - **Activation**: quantum ODE, nonunitary dynamics, economic modeling, 量子微分方程, 经济建模

### HPC-vQPU: A Service-Export Architecture for Virtual QPUs on Batch-Scheduled HPC Systems
- [[hpc-vqpu-architecture]] - 批调度HPC系统上虚拟QPU服务导出架构，保持拓扑/门/校准语义 (arXiv: 2605.28845)
  - 核心要点 1: 桥接HPC批调度环境与量子软件交互式后端接口之间的鸿沟
  - 核心要点 2: 在队列延迟和系统扩展中保持量子硬件语义完整性
  - **Activation**: hpc quantum, virtual qpu, batch scheduling, 虚拟量子处理器, HPC架构

### Additive binding energies in asphalt on a quantum processor via QSCI
- [[quantum-pave-chemistry]] - QuantumPave混合量子经典工作流，用量子中心超算计算材料结合能 (arXiv: 2605.27640)
  - 核心要点 1: 量子处理器采样主导电子构型，经典HPC执行对角化
  - 核心要点 2: NISQ兼容的量子化学实用方案，无需容错量子计算
  - **Activation**: quantum chemistry, QSCI, binding energy, quantum-centric supercomputing, 量子化学


## 2026-05-30 - Economics & Investment + Quantum (Cron Job)

### Change-point estimation for Weibull time series with copula-based Markov models
- [[weibull-change-point-detection]] - Copula-based Markov chain methodology for offline change-point estimation in financial time series with Weibull marginals (arXiv: 2605.29541)
  - Models nonlinear serial dependence in nonnegative financial data (volumes, durations, volatility)
  - Separates marginal Weibull distribution from copula dependence structure
  - **Activation**: change-point detection, weibull time series, copula markov, financial regime detection, volatility breaks

### From Classical Optimization to Bayesian Integration: Systematic Portfolio Management
- [[bayesian-portfolio-integration]] - Systematic portfolio management comparing classical mean-variance to Bayesian integration methods on 10 US stocks (arXiv: 2605.29413)
  - Covers Markowitz, Black-Litterman, Bayesian shrinkage, hierarchical risk parity
  - Expanding window walk-forward validation with realistic transaction costs
  - **Activation**: portfolio optimization, bayesian portfolio, systematic investing, asset allocation, mean-variance, Black-Litterman

### Exponentially Fast Solution State Preparation for the Heat Equation and its use for Option Pricing
- [[quantum-option-pricing-heat-equation]] - Exponentially fast quantum algorithm for heat equation solution state preparation with European option pricing applications (arXiv: 2605.28950)
  - Quantum state preparation achieves exponential speedup for diffusion process encoding
  - Exponential qubit advantage over quantum Monte Carlo for path-dependent options
  - **Activation**: quantum option pricing, heat equation quantum, Black-Scholes quantum, quantum PDE, derivative pricing

### End-to-End PDE-Based Quantum Algorithms for Multi-Asset Option Pricing under Local and Stochastic Volatility
- [[quantum-pde-option-pricing]] - End-to-end quantum PDE framework for multi-asset European option pricing under local-volatility Black-Scholes and Heston models (arXiv: 2605.26610)
  - Polynomial improvement N^(d/2) for Black-Scholes, N^d for Heston vs finite-difference baselines
  - End-to-end gate complexity analysis with Clifford+T resource estimates
  - **Activation**: quantum PDE option pricing, multi-asset options, Heston model quantum, finite-difference quantum, Clifford+T

### Insurance Pricing Optimization via Off-Policy Evaluation
- [[quantum-off-policy-evaluation-pricing]] - Insurance pricing as decision-making problem using off-policy evaluation with kernelized IPS estimator (arXiv: 2605.28327)
  - Neural network policy optimization outperforms existing techniques
  - Quantum RL and quantum off-policy evaluation applicable
  - **Activation**: insurance pricing, off-policy evaluation, quantum RL pricing, kernelized IPS


## 2026-05-30 - Systems Engineering Research (Cron Job)

### Optimization of Predictive Maintenance Schedules under Uncertainty: A Scenario-Based Theoretical Framework
- [[predictive-maintenance-uncertainty-scenario]] - Scenario-based optimization framework integrating calendar, usage, and RUL-based maintenance information (arXiv: 2605.30222)
  - Unified finite-horizon decision framework for multi-asset maintenance scheduling
  - Expected-cost and tail-risk criteria for comparing maintenance schedules
  - Integrates heterogeneous information sources: calendar intervals, usage limits, RUL estimates
  - **Activation**: predictive maintenance optimization, maintenance scheduling uncertainty, scenario-based maintenance, RUL-based scheduling, multi-asset maintenance

### BuilDyn: Excitation-Driven Data Generation for Building Thermal Dynamics Modeling and Control
- [[buildyn-thermal-dynamics-control]] - Excitation-driven data generation framework for control-oriented building thermal modeling (arXiv: 2605.29849)
  - Customizable excitation strategies for systematic state-space exploration
  - Sampling from representative building distributions for transfer learning
  - Python interface for ML pipeline integration and foundation model development
  - **Activation**: building thermal dynamics, excitation-driven data, control-oriented modeling, building ML training data, BuilDyn framework


## 2026-05-30 - Neuroscience Research (Cron Job) - Part 6

### Benchmarking Positional Encoding Strategies for Transformer-Based EEG Foundation Models
- [[eeg-transformer-positional-encoding-benchmark]] - 首次系统基准测试EEG foundation models的位置编码策略，SPE适用于运动想象，ACPE跨任务性能更一致 (arXiv: 2605.29754)
  - 核心要点 1: 位置编码策略任务依赖，SPE在运动想象任务中表现优异但情感识别较弱
  - 核心要点 2: ACPE (Asymmetric Conditional Positional Encoding) 显示更一致的跨任务性能
  - **Activation**: EEG transformer, foundation model, positional encoding, SPE, ACPE, motor imagery, emotion recognition, benchmark

### Embodied Virtual Reality Feedback Reshapes Neural Representations to Support Continuous Three-Dimensional Motor Imagery Decoding
- [[embodied-vr-feedback-3d-motor-imagery-bci]] - 首次系统研究 embodied VR feedback 对连续3D运动想象BCI解码的影响，VR比屏幕反馈提升8.9-13.0% (arXiv: 2605.29677)
  - 核心要点 1: VR反馈产生更可解码和可泛化的神经表征，CNN-LSTM解码器达r=0.762
  - 核心要点 2: 增强的感觉运动-顶叶去同步化，更强的运动-额叶功能连接
  - **Activation**: embodied VR feedback, motor imagery BCI, 3D decoding, neurorehabilitation, CNN-LSTM decoder


## 2026-05-30 - Neuroscience Research (Cron Job) - Part 5

### MIRAGE: Adaptive Multimodal Gating for Whole-Brain fMRI Encoding
- [[mirage-multimodal-fmri-encoding]] - State-of-the-art framework predicting whole-brain fMRI responses via native multimodal backbone and adaptive layer-wise gating (arXiv: 2605.29850)
  - Natively multimodal features consistently outperform post-hoc unimodal aggregation
  - Interpretable modality attention traces distinct anatomical patterns across cortex
  - Transformer brain encoder with subject-specific linear heads
  - **Activation**: fMRI encoding, multimodal brain prediction, MIRAGE, brain encoding, naturalistic stimuli, adaptive gating

### Treatment-Conditioned Diffusion for Forecasting Neurodegenerative Disease Progression
- [[treatment-conditioned-diffusion-neurodegenerative-progression]] - Novel diffusion framework predicting high-fidelity future brain states conditioned on DaTscan and levodopa treatment (arXiv: 2605.29932)
  - Transformer encoder for non-linear pharmacological dynamics
  - Multi-weight ROI mask focusing on biologically critical areas
  - 14.0% lower MSE, 7.2% lower MAE, 4.9% higher SSIM vs baseline
  - **Activation**: neurodegenerative, disease progression, Parkinson, diffusion, longitudinal neuroimaging, DaTscan, treatment-conditioned

## 2026-05-30 - Neuroscience Research (Cron Job)

### Large language models reorganize representational geometry during in-context learning
- [[llm-icl-representational-geometry-reorganization]] - Geometric account of in-context learning linking neuroscience untangling perspective to LLM behavior (arXiv: 2605.28854)
  - ICL effectiveness depends on online untangling of task-relevant representations
  - Geometric reorganization increases separability during in-context examples
  - LLMs use prototype-like algorithm with evidence integration
  - **Activation**: ICL, in-context learning, representational geometry, untangling, prototype, LLM neuroscience

## 2026-05-30 - Neuroscience Research (Cron Job) - Part 4

### Spiking Temporal Memory: Sequence Timing and Replay Speed Control
- [[stm-sequence-timing-replay]] - Spiking Temporal Memory (sTM) model that learns sequence element timing via sequential population activation, with oscillatory background controlling replay speed (arXiv: 2605.22523)
  - Duration encoded by sequential activation of element-specific neuronal populations
  - Oscillatory background inputs serve as clock signal for flexible speed control
  - Replay speed correlates with EEG/LFP oscillatory characteristics during wakefulness vs. sleep
  - **Activation**: sequence timing, replay speed, sTM, spiking temporal memory, oscillatory control, temporal encoding

### Lattice Field Theory for Neural Networks
- [[lattice-field-theory-neurons]] - Physics-grounded Lattice Field Theory (LFT) framework interpreting BCI spike rasters, extending Maximum Entropy with time evolution and Free Energy Principle connections (arXiv: 2604.05251)
  - Neural activity as field variables on discrete lattice structure
  - Time evolution included in Maximum Entropy model → Free Energy Principle variant
  - Tailored for chronic multi-site BCI recordings, single neuron spike rasters
  - **Activation**: lattice field theory, LFT, neural field, maximum entropy, BCI interpretation, spike raster, free energy

## 2026-05-30 - Economics & Investment + Quantum Finance (Cron Job)

### Insurance Pricing Optimization via Off-Policy Evaluation
- [[quantum-off-policy-evaluation-pricing]] - Quantum off-policy evaluation methodology for insurance pricing and financial decision optimization using quantum IPS estimators and variational quantum policies (arXiv: 2605.28327)
  - Formulates pricing as decision-making problem using off-policy evaluation and stochastic control
  - Kernelized IPS estimator exploits local structure in action space for variance reduction
  - Neural network policy optimization outperforms existing techniques in controlled environment
  - Quantum amplitude estimation provides O(1/ε) vs O(1/ε²) sample complexity for IPS
  - **Activation**: quantum pricing, off-policy evaluation, quantum OPE, insurance pricing, quantum IPS, quantum reinforcement learning pricing

### HQFS: Hybrid Quantum Classical Financial Security
- [[quantum-finance-pipeline]] - End-to-end hybrid quantum-classical pipeline integrating VQC forecasting, QUBO annealing, and post-quantum signing for financial risk systems
  - VQC (Variational Quantum Circuit) forecasting replaces classical prediction layer
  - Penalty-free CQM formulation avoids dense rank-one cardinality penalty matrices that cause 83%+ chain breaks
  - Post-quantum cryptography signing for audit-ready compliance
  - QPU access time only 0.7% of total runtime; quantum used for solution space exploration
  - Qutrit neural networks (3-state) outperform qubit-based and classical ANNs in stock prediction
  - **Activation**: quantum finance pipeline, VQC forecasting, QUBO annealing, portfolio optimization quantum, post-quantum finance, qutrit neural network, quantum option pricing

### Dynamic Circuit Compilation Optimization
- [[dynamic-circuit-compile-optimization]] - Compile-time optimization for dynamic quantum circuits reducing classical feedforward by ~50% using static analysis and probabilistic circuit representation (arXiv: 2605.28439)
  - Static analysis symbolically executes circuit propagating classical info alongside quantum state
  - Probabilistic circuit model enables rewriting mid-circuit measurements as unitary operations
  - ~50% feedforward reduction on random circuits, higher in favorable settings
  - Accepted at ISC High Performance 2026
  - **Activation**: dynamic circuit optimization, compile-time quantum circuit, mid-circuit measurement reduction, classical feedforward optimization, probabilistic circuit model, quantum compiler latency, low-latency quantum trading

### Representation Signatures and Risk-Feedback Alignment in LLM Trading Agents
- [[llm-trading-agent-alignment]] - Behavioral alignment and representation dynamics of LLM trading agents — pre-failure signatures (embedding drift, effective-rank contraction), risk-feedback alignment without fine-tuning, and correlation blind spot detection (arXiv: 2605.28850)
  - Planning embeddings drift from normal-state centroids before failures
  - Effective-rank contraction persists across embedding types (hash, LSA, Transformer, hidden-state probes)
  - Structured risk feedback acts as external alignment signal without fine-tuning
  - LLM rationales justify concentrated coupled-asset exposure that risk layer clips
  - **Activation**: llm trading agent, risk feedback alignment, pre-failure detection, representation drift, behavioral alignment, financial llm diagnostics, correlation blind spot

### Exponentially Fast Solution State Preparation for the Heat Equation and its use for Option Pricing
- [[quantum-option-pricing-heat-equation]] - Exponentially fast quantum state preparation for the heat equation with application to European option pricing under Black-Scholes model (arXiv: 2605.28950)
  - Quantum algorithm achieves exponential speedup in state preparation for heat equation solutions
  - Direct application to option pricing under classical Black-Scholes framework
  - Enables efficient quantum simulation of diffusion processes in quantitative finance
  - **Activation**: quantum option pricing, heat equation quantum, black-scholes quantum, diffusion simulation, exponential speedup state prep, quantum PDE finance

## 2026-05-30 - Neuroscience Research (Cron Job) - Part 3

### Brain-IT-VQA: From Brain Signals to Answers
- [[brain-it-vqa-fmri-visual-question-answering]] - First framework for visual question answering from fMRI using Brain Interaction Transformer, substantially outperforming existing methods with new NSD-VQA benchmark dataset (arXiv: 2605.29588)
  - Brain-IT decodes language tokens from brain activity, integrates with LLM for VQA
  - NSD-VQA provides 20 controlled question-answer pairs per image across 20 categories
  - Quantifies decodable visual/semantic information and brain region contributions
  - **Activation**: fMRI VQA, brain decoding, visual question answering, Brain Transformer, brain representations, semantic decoding

## 2026-05-30 - Neuroscience Research (Cron Job) - Part 2
## 2026-05-30 - Economics & Investment (Cron Job)

### Financially Guided Deep Portfolio Optimization
- [[deep-portfolio-optimization-framework]] - End-to-end deep learning portfolio optimization that directly optimizes differentiable surrogates of Sharpe ratio, Omega ratio, CVaR, and Risk Parity, bypassing predict-then-optimize paradigm (arXiv: 2605.28853)
  - AttentionLSTM with Omega-CVaR-RiskParity loss achieves best out-of-sample performance on S&P 500
  - Expanding-window walk-forward validation with realistic bid-ask costs and quarterly rebalancing
  - **Activation**: portfolio optimization deep learning, differentiable portfolio, Sharpe ratio neural network, CVaR portfolio, Omega ratio portfolio



### Embodied Virtual Reality Feedback Reshapes Neural Representations to Support Continuous Three-Dimensional Motor Imagery Decoding
- [[embodied-vr-feedback-3d-motor-imagery-bci]] - First systematic investigation of embodied VR feedback for continuous 3D motor imagery BCI, with 8.9-13.0% improvement over screen feedback (arXiv: 2605.29677)
  - VR feedback elicits inherently more decodable and generalisable neural representations
  - CNN-LSTM decoder achieves r=0.762 correlation under VR vs r=0.672 under screen
  - Neurophysiological: stronger sensorimotor-parietal desynchronisation, enhanced motor-frontal connectivity
  - **Activation**: embodied VR feedback, motor imagery BCI, 3D decoding, neurorehabilitation, continuous BCI

### Neural-Behavioral Representation of Natural Whole-body Movement in Monkeys
- [[neural-behavioral-whole-body-movement-monkeys]] - First framework combining large-scale epidural cortical signals with multi-view motion capture to decode unconstrained whole-body kinematics in primates (arXiv: 2605.29355)
  - Behavior prior learning via autoregressive encoder-decoder model
  - Decodes accurate/realistic whole-body movement without explicit physics constraints
  - Novel proof-of-concept for natural whole-body movement decoding
  - **Activation**: whole-body movement, motor decoding, primate neuroscience, behavior prior, motion capture

## 2026-05-30 - Neuroscience Research (Cron Job)

### Comprehensive Neural Dynamics Analysis Methodology
- [[neural-dynamics-analysis-methodology]] - Unified framework integrating neural population decoding, brain network dynamics, neural criticality assessment, spiking neural network dynamics, and connectome computational analysis (Synthesized from multiple recent arXiv papers)
  - Neural population decoding: dimensionality reduction, temporal dynamics, cross-subject generalization
  - Brain network dynamics: dynamic connectivity, control theory, Kuramoto oscillators, tensor decomposition
  - Neural criticality assessment: power-law distributions, branching ratio, Griffiths phase
  - Spiking neural network dynamics: LIF models, synchrony, oscillations, E/I balance
  - Connectome computational analysis: graph metrics, hub identification, GNN, optimal transport
  - **Activation**: neural dynamics, computational neuroscience, brain networks, neural population, spiking networks, criticality, connectome analysis, 神经动力学分析方法论

### Common Noise-Induced Group-Level Synchronization Between Uncoupled Groups of Oscillators
- [[noise-induced-oscillator-synchronization]] - Proves common noise synchronizes uncoupled oscillator groups via Kuramoto order parameter; phase density evolution mapping explains collective dynamics without inter-group coupling (arXiv: 2605.29529)
  - Complex Kuramoto order parameter R(t) synchronizes across groups sharing identical noise
  - Phase density evolution derivation: common noise creates correlated collective phases
  - Neurophysiological implication: shared input explains functional connectivity without anatomical connections
  - **Activation**: noise-induced synchronization, Kuramoto model, oscillator dynamics, common noise, phase density evolution, neural synchronization

## 2026-05-30 - Economics, Investment + Quantum (Cron Job)

### End-to-End PDE-Based Quantum Algorithms for Multi-Asset Option Pricing under Local and Stochastic Volatility
- [[quantum-pde-option-pricing]] - End-to-end quantum PDE framework for European option pricing achieving polynomial speedup N^{d/2} (BS) and N^d (Heston) over classical baselines (arXiv: 2605.26610)
  - Finite-difference discretization on spatial grids with explicit Clifford+T resource accounting
  - Gate complexity O~(d^2 N^{2+d/2}) for local-vol BS, O~(d^2 N^{d+2}) for Heston
  - **Activation**: quantum PDE option pricing, quantum Black-Scholes, quantum Heston model, multi-asset derivatives, finite-difference quantum, 量子期权定价

### A Penalty-Free Pipeline for Direct Quantum-Annealer Portfolio Optimization
- [[penalty-free-quantum-annealing-portfolio]] (enhanced) - Drops cardinality penalty from QUBO, enforcing constraints via classical post-processing; reduces chain-break from 71-92% to 0.04% (arXiv: 2605.17628)
  - Dense penalty term makes logical graph complete regardless of covariance structure
  - Objective-only QUBO + classical cardinality enforcement yields lower-energy feasible portfolios
  - **Activation**: penalty-free quantum annealing, quantum portfolio optimization, D-Wave QUBO, cardinality constraints

### Parameterized 4-Qubit EWL Quantum Game Circuits with Dirac-Solow-Swan Hamiltonian for Innovation Recommender Systems
- [[ewl-quantum-game-economics]] - 4-qubit EWL quantum game circuit mapping measurement probabilities to Dirac-Solow-Swan Hamiltonian for disruptive innovation forecasting in quadruple helix ecosystems (arXiv: 2605.18080)
  - Only 22 gates, circuit depth 11, NISQ-compatible
  - Calibrated from EC CORDIS funding data for real-world recommender scoring
  - **Activation**: EWL quantum game, Dirac-Solow-Swan Hamiltonian, quantum recommender system, quadruple helix, 量子博弈论经济学

### Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization
- [[quantum-hybrid-audit]] - Audit methodology for decomposing hybrid quantum-classical optimization workflows, measuring actual quantum contribution vs classical overhead (arXiv: 2605.17623)
  - QPU access time is only 0.7% of 5-second wall-clock budget in D-Wave hybrid solver
  - Hybrid matches Gurobi MIQP optimum on all 54 provable instances despite minimal quantum time
  - Quantum Contribution Index (QCI) framework for investment decision support
  - **Activation**: quantum hybrid audit, D-Wave hybrid analysis, quantum contribution measurement, hybrid solver decomposition, 量子混合审计

### Noise-Induced Landscape Distortion in QAOA for Constrained Binary Optimization
- [[qaoa-landscape-audit]] - Landscape Span Compression (LSC) metric for device-agnostic audit of QAOA hardware noise impact, predicting optimization failure before expensive quantum runs (arXiv: 2604.19426)
  - LSC = 1 - (observed_span/ideal_span); LSC > 0.7 indicates near barren plateau
  - Empirically validated on IBM quantum hardware for constrained QUBO problems
  - Pre-run diagnostic saves quantum compute resources by predicting failure
  - **Activation**: qaoa landscape audit, landscape span compression, qaoa noise analysis, quantum barren plateau detection, 量子优化景观审计

### Constrained Counterdiabatic Quantum Approximate Optimization Algorithm for Portfolio Optimization
- [[constrained-counterdiabatic-qaoa-portfolio]] (enhanced) - CCD-QAOA with approximate adiabatic gauge potentials from nested commutators for constrained portfolio optimization (arXiv: 2605.06858)
   100|  - Incorporates counterdiabatic terms into variational ansatz for improved convergence
   101|  - Handles realistic budget and risk constraints with XY-mixer Hamiltonian
   102|  - **Activation**: counterdiabatic QAOA, portfolio optimization, adiabatic gauge potential, constrained quantum optimization
   103|
   104|### Constraint Preserving XY-Mixers under Trotterized Adiabatic Evolution
   105|- [[constraint-preserving-quantum-mixers]] (enhanced) - XY-mixer design methodology under Trotterized adiabatic evolution for constrained quantum optimization (arXiv: 2605.02465)
   106|  - Constraint locality analysis for XY-mixer Hamiltonian design
   107|  - Trotterized adiabatic evolution preserves feasibility throughout optimization
   108|  - **Activation**: constraint preserving mixers, XY-mixer, Trotterized evolution, constrained quantum optimization
   109|
   110|     1|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
   111|     2|
   112|     3|### Algorithms with Polynomially-Improved Approximation Factors for the 2→q Norm
   113|     4|- [[norm-approximation-algorithms]] - Multiplicative weight update algorithm for matrix 2→q norm approximation with polynomial improvement over spectral methods, applications to hypercontractivity and quantum separability (arXiv: 2605.25303)
   114|     5|  - MWU framework achieves O(n^{1/4-δ}) vs prior O(n^{1/4} log d)
   115|     6|  - Applications: hypercontractivity testing, quantum separability certification, small-set expansion
   116|     7|  - **Activation**: matrix norm approximation, 2-to-q norm, operator norm, hypercontractivity, multiplicative weight update, quantum separability
   117|     8|
   118|     9|### Bell's Theorem: Why Probability Factorisation Fails
   119|    10|- [[bell-probability-factorization]] - Statistical foundations of Bell's theorem showing why joint probability factorization P(A,B|a,b,λ)=P(A|a,λ)P(B|b,λ) fails in quantum systems (arXiv: 2605.29589)
   120|    11|  - Factorization assumption incompatible with quantum entanglement
   121|    12|  - CHSH inequality as statistical diagnostic for non-classical correlations
   122|    13|  - **Activation**: Bell theorem, probability factorization, quantum nonlocality, CHSH inequality, joint distributions
   123|    14|
   124|    15|### Comparing Classical Simulation and Sample-Based Learning of Quantum Systems
   125|    16|- [[quantum-ml-simulation-learning-comparison]] - Empirical framework comparing simulability vs learnability for quantum systems via Born-rule statistics (arXiv: 2605.28986)
   126|    17|  - Simulation (from classical description) and learning (from measurement samples) need not coincide
   127|    18|  - Provides complexity-theoretic and empirical methodology for quantum advantage verification
   128|    19|  - **Activation**: quantum simulation vs learning, sample-based quantum learning, simulability learnability, Born-rule statistics
   129|    20|
   130|    21|### Analytic Properties of the Jost Functions via the Poincaré-Picard Theorem
   131|    22|- [[jost-function-analytic-ode]] - ODE-theoretic analysis of Jost function analyticity for quantum scattering and complex energy plane continuation (arXiv: 2605.28859)
   132|    23|  - Applies Poincaré-Picard theorem to parameter-dependent radial Schrödinger equation
   133|    24|  - Bridges mathematical analysis (ODE theory) with quantum scattering physics
   134|    25|  - **Activation**: jost function, quantum scattering, analytic continuation, Poincaré-Picard, complex energy plane
   135|    26|
   136|    27|### HyperPrecision: High-Precision Numerical Evaluation of Multivariate Hypergeometric Functions
   137|    28|- [[hypergeometric-high-precision-evaluation]] - Mathematica package for high-precision evaluation of Horn-type hypergeometric functions via Pfaffian systems, applicable to QFT, string theory, number theory, and statistics (arXiv: 2605.30216)
   138|    29|  - Automatic Pfaffian system construction from hypergeometric function definition
   139|    30|## 2026-05-29 - Neuroscience Research (Cron Job)
   140|    31|
   141|    32|### A Deep Learning Model of Mental Rotation Informed by Interactive VR Experiments
   142|    33|- [[deep-learning-mental-rotation-vr]] - Longitudinal subcortical shape analysis with cognitive associations in aging (arXiv: 2605.29703)
   143|    34|  - Equivariant neural encoder for 3D spatial representations
   144|    35|  - Neuro-symbolic object encoder combining perception + reasoning
   145|    36|  - Interactive VR experiments for human behavioral validation
   146|    37|  - **Activation**: mental rotation, spatial cognition, VR, neuro-symbolic, equivariant networks
   147|    38|
   148|    39|### Subcortical Shape Variations and Their Associations with Cognition Across the 8th Decade of Life
   149|    40|- [[subcortical-shape-cognition-aging]] - Longitudinal analysis of subcortical morphology + cognition (arXiv: 2605.29703)
   150|    41|  - Shape-based analysis captures subtle aging patterns missed by volumetry
   151|    42|  - Lothian Birth Cohort 1936: 9-year trajectory (age 70-79)
   152|    43|  - Regional specificity: hippocampal head → memory, thalamus → processing speed
   153|    44|  - **Activation**: subcortical morphology, brain aging, cognitive decline, shape analysis
   154|    45|
   155|    46|  - One-dimensional contour restriction reduces multivariate PDE to ODE for efficient evaluation
   156|    47|  - **Activation**: hypergeometric, pfaffian, high-precision, horn-type, mathematica, multivariate, laurent expansion, quantum field theory
   157|    48|
   158|    49|### On modular forms of rational weight satisfying the canonical second-order linear modular differential equation
   159|    50|- [[modular-forms-kaneko-zagier-classification]] - Complete classification of rational weights for Kaneko-Zagier differential equation admitting modular forms solutions (arXiv: 2605.23383)
   160|    51|  - Transforms KZ equation to hypergeometric form, constructs monodromy representation matrices
   161|    52|  - Stringent commutativity constraints limit admissible weights to specific set
   162|    53|  - **Activation**: modular forms, kaneko-zagier, differential equation, monodromy, hypergeometric, rational weight, congruence subgroup
   163|    54|
   164|    55|### Iterative maps emerging from cohomological structure of primes
   165|    56|- [[prime-cohomological-iterative-maps]] - Prime gaps described by iterative maps with cohomological structure linking to statistical and quantum mechanics (arXiv: 2605.17622)
   166|    57|  - Iterative map predicts primary growth of successive primes
   167|    58|  - Residual fluctuations encode well-defined cohomological structure
   168|    59|  - **Activation**: prime numbers, cohomology, iterative maps, statistical mechanics, quantum mechanics, prime gaps
   169|    60|
   170|    61|### A Uniform Random-Lattice Tail Bound for the SVP Kissing-Profile Parameter
   171|    62|- [[svp-lattice-tail-bound]] - Dimension-uniform tail bound for SVP kissing-profile parameter with implications for quantum algorithms and post-quantum cryptography (arXiv: 2605.21966)
   172|    63|  - μ_n{γ(L) > T} ≤ C·T^{-1} for Haar-Siegel random lattices, uniformly in dimension
   173|    64|  - γ(L) = 2^{o(n)} with high probability for random lattices
   174|    65|  - **Activation**: SVP, shortest vector problem, lattice, tail bound, quantum algorithms, post-quantum cryptography
   175|    66|
   176|    67|### Hadamard product of convex functions and Jackson operator
   177|    68|- Note: Jackson operator q-theory skill already exists; no new skill needed (arXiv: 2605.18412)
   178|    69|
   179|    70|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
   180|    71|
   181|    72|### Wasserstein Least Squares: A Canonical Regression Method for Probability Distributions
   182|    73|- [[wasserstein-least-squares-regression]] - Distributional regression via optimal transport, achieving n^{-1/2} rate with exponential improvement for Wasserstein barycenters (arXiv: 2605.30266)
   183|    74|  - Canonical extension of Euclidean least squares to probability distribution space via convex analysis
   184|    75|  - Template deformation model enables n^{-1/2} estimation rate; exponential barycenter improvement
   185|    76|  - **Activation**: Wasserstein regression, distributional regression, optimal transport, probability distributions, Wasserstein barycenter, template deformation
   186|    77|
   187|    78|### Improved Sample Complexity Bound for Sample-Based Lindbladian Simulation
   188|    79|- [[lindbladian-sample-complexity]] - Sharp dichotomy between typical-case O(t²/ε²) and worst-case Ω(d⁴t²/ε²) for quantum Lindbladian simulation (arXiv: 2605.30301)
   189|    80|  - WML algorithm with trace condition determines typical vs worst case
   190|    81|  - Random Lindblad operators satisfy typical case with high probability
   191|    82|  - **Activation**: Lindbladian simulation, sample complexity, quantum channels, open quantum systems, WML algorithm, random matrix theory
   192|    83|
   193|    84|## 2026-05-29 - Neuroscience Research (Cron Job)
   194|    85|
   195|    86|### Domain-Informed Multi-Objective Framework for EEG Channel Selection in Motor Imagery BCIs
   196|    87|- [[domain-informed-moeeg-channel-selection-bci]] - Multi-objective optimization combining spatial relevance (Gaussian kernel) + functional discriminability (ERD) for compact EEG channel selection (arXiv: 2605.29943)
   197|    88|  - NSGA-II/MOPSO/MOEA/D algorithms achieve 87%, 71%, 75%, 65% on Physionet, OpenBMI, HighGamma, BCIIV-2A
   198|    89|  - 87% dimensionality reduction (64→8 channels), sensorimotor cortex prioritization
   199|    90|  - **Activation**: EEG channel selection, motor imagery BCI, multi-objective optimization, Pareto front, ERD, sensorimotor cortex
   200|    91|
   201|    92|### Learning Robust and Task-Invariant Functional Representation from fMRI through Siamese Self-Supervised Learning
   202|    93|- [[brainsimsiam-self-supervised-fmri]] - BrainSimSiam lightweight self-supervised framework for cross-task generalization without large-scale pretraining (arXiv: 2605.28990)
   203|    94|  - Positive-only contrastive learning, stop-gradient mechanism, outperforms supervised baselines
   204|    95|  - +15% ADHD accuracy, -8% age regression MSE, comparable to foundation models with 90% less compute
   205|    96|  - **Activation**: self-supervised fMRI, Siamese learning, BrainSimSiam, positive-only contrastive, cross-task generalization
   206|    97|
   207|    98|## 2026-05-29 - Neuroscience Research (Cron Job)
   208|    99|
   209|   100|### LLM ICL Representational Geometry Reorganization
   210|   101|- [[llm-icl-representational-geometry-reorganization]] - ICL models reorganize representations dynamically via prototype comparison (arXiv: 2605.28854)
   211|   102|  - RDM correlation increases during untangling tasks
   212|   103|  - Eigenvalue spectrum separates task information
   213|   104|  - **Activation**: ICL, representational geometry, prototypes, untangling, RDM correlation, online learning
   214|   105|
   215|   106|### Brain-IT-VQA: From Brain Signals to Answers
   216|   107|- [[brain-it-vqa-fmri-visual-question-answering]] - Brain-IT-VQA framework for VQA from fMRI, decodes language tokens from brain activity (arXiv: 2605.29588)
   217|   108|  - Token-level decoding outperforms pixel reconstruction
   218|   109|  - NSD-VQA benchmark with 20 controlled question categories
   219|   110|  - **Activation**: Brain-IT, VQA, fMRI decoding, brain question answering, NSD-VQA
   220|   111|
   221|   112|
   222|   113|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
   223|   114|
   224|   115|### Paper 2605.29052
   225|   116|- [[quantum-nonautonomous-ode-simulation]] - 量子算法模拟非自治ODE非幺正动力学，通过SVD分解将传播子写为酉算子之和 (arXiv: 2605.29052)
   226|   117|  - quantum ODE
   227|   118|  - nonunitary dynamics
   228|   119|  - SVD dilation
   229|   120|  - quantum simulation
   230|   121|  - **Activation**: quantum ODE, nonunitary dynamics, SVD dilation, quantum simulation
   231|   122|
   232|   123|### Paper 2605.28892
   233|   124|- [[funessian-process-non-markovian]] - Funessian过程：正可分非马尔可夫过程，初始状态记忆贯穿演化，互信息表征非马尔可夫性 (arXiv: 2605.28892)
   234|   125|  - non-Markovian
   235|   126|  - memory effect
   236|   127|  - Chapman-Kolmogorov
   237|   128|  - ergodicity breaking
   238|   129|  - **Activation**: non-Markovian, memory effect, Chapman-Kolmogorov, ergodicity breaking
   239|   130|
   240|   131|### Paper 2605.29130
   241|   132|- [[mersenne-numbers-doubling-map]] - 梅森数与倍角映射动力学联系，无需显式计算即可求因子的替代Lucas-Lehmer方法 (arXiv: 2605.29130)
   242|   133|  - Mersenne numbers
   243|   134|  - doubling map
   244|   135|  - prime testing
   245|   136|  - dynamical systems
   246|   137|  - **Activation**: Mersenne numbers, doubling map, prime testing, dynamical systems
   247|   138|
   248|   139|### Paper 2605.28906
   249|   140|- [[quantum-classical-uncertainty-electromagnetism]] - 经典与量子电磁理论统一不确定关系ΔrΔk≥5/2，适用于光束和单光子 (arXiv: 2605.28906)
   250|   141|  - uncertainty relations
   251|   142|  - electromagnetism
   252|   143|  - classical-quantum correspondence
   253|   144|  - **Activation**: uncertainty relations, electromagnetism, classical-quantum correspondence
   254|   145|
   255|   146|### Paper 2605.28974
   256|   147|- [[quantum-ml-statistics-invariant-theory]] - 基于quiver不变量理论的iPCA模型MLE存在性检验算法，连接统计学与不变量理论 (arXiv: 2605.28974)
   257|   148|  - MLE existence
   258|   149|  - invariant theory
   259|   150|  - quiver representation
   260|   151|  - iPCA
   261|   152|  - **Activation**: MLE existence, invariant theory, quiver representation, iPCA
   262|   153|
   263|   154|### Paper 2605.28931
   264|   155|- [[quantum-ml-ground-state-measurement]] - SIC-POVM测量空间量子基态变分学习，自回归GRU编码概率分布+物理性约束 (arXiv: 2605.28931)
   265|   156|  - quantum ground state
   266|   157|  - SIC-POVM
   267|   158|  - variational learning
   268|   159|  - autoregressive neural network
   269|   160|  - **Activation**: quantum ground state, SIC-POVM, variational learning, autoregressive neural network
   270|   161|
   271|   162|## 2026-05-29 - Neuroscience Research (Cron Job)
   272|   163|
   273|   164|### Graph Neural Network Reveals the Cortical Morphology of Local Brain Aging in Normal Cognition and Alzheimer's Disease
   274|   165|- [[gnn-cortical-morphology-brain-aging]] - GNN-based local brain age estimation from cortical morphology (arXiv: 2601.10912)
   275|   166|  - High-resolution (1.37mm) vertex-level aging pattern analysis
   276|   167|  - Identifies association cortices aging in CN, widespread MCI patterns, comprehensive AD cortical aging
   277|   168|  - Links regional LBA gaps to neuropsychological measures
   278|   169|  - **Activation**: brain age, cortical morphology, GNN, Alzheimer, cognitive impairment, aging patterns
   279|   170|
   280|   171|     1|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics (Cron Job)
   281|   172|     2|
   282|   173|     3|### End-to-End Formalization of Quantum Error Correction
   283|   174|     4|- [[qec-formal-verification]] - 量子纠错码端到端形式化验证方法论，SAT验证约简+机器检查距离证明 (arXiv: 2605.16523)
   284|   175|     5|  - 稳定子码理论完整形式化（线性代数、Pauli群、二元辛表示）
   285|   176|     6|  - 距离认证问题通过验证SAT约简机器检查
   286|   177|     7|  - BitVec编码将变量数从O(n)降至O(√n)
   287|   178|     8|  - **Activation**: quantum error correction formal verification, stabilizer code distance proof, machine-checked quantum verification, qLDPC certification, QECC end-to-end formalization
   288|   179|     9|
   289|   180|    10|
   290|   181|    11|### Best-First Ordered Statistics Decoding of Quantum LDPC Codes
   291|   182|    12|- [[bf-osd-qldpc-decoding]] - BF-OSD遍历错误候选空间按似然降序，1/100查询预算达到BP+OSD同等性能 (arXiv: 2605.25777)
   292|   183|    13|  - Best-First OSD替代暴力枚举，优先级队列按似然排序
   293|   184|    14|  - 固定BP迭代次数后调用OSD，而非等待收敛
   294|   185|    15|  - 全电路级噪声下特别有效，BP不可靠时优势明显
   295|   186|    16|  - **Activation**: quantum error correction, QLDPC decoding, BF-OSD, belief propagation, ordered statistics decoding
   296|   187|    17|
   297|   188|    18|### Quantum Mechanics: Problems and Paradoxes
   298|   189|    19|- [[quantum-foundations-probability]] - 量子力学基础公理体系：概率起源、Planck常数本质、波函数本体论、测量问题 (arXiv: 2605.30067)
   299|   190|    20|  - 量子理论公理体系形式化
   300|   191|    21|  - 经典振荡器+热浴→量子行为对应模型
   301|   192|    22|  - 概率振幅本质与Born规则推导
   302|   193|    23|  - **Activation**: quantum foundations, quantum probability, measurement problem, wave function ontology, axiom system
   303|   194|    24|
   304|   195|    25|### Entropy-Governed Speedup for Quantum Algorithms on Local Hamiltonians
   305|   196|    26|- [[entropy-governed-quantum-speedup]] (enhanced) - 利用熵结构超越Grover界的量子算法，在深度-d状态上实现更低能量估计 (arXiv: 2605.18241)
   306|   197|    27|  - 输出态能量不超过深度-d态的最小能量
   307|   198|    28|  - 区分强纠缠态与经典可描述态
   308|   199|    29|  - **Activation**: quantum algorithm speedup, local Hamiltonian, entropy-governed, Grover bound
   309|   200|    30|
   310|   201|
   311|### Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization
   312|- [[quantum-finance-stack]] (enhanced) - Audit reveals D-Wave hybrid QPU contributes only 0.7% of wall-clock time; 99% classical decomposition, identical solutions across all budgets showing determinism (arXiv: 2605.17623)
   313|  - QPU mean access time 0.034s out of 5s budget on 54 instances (N=10-640)
   314|  - Cardinality penalty creates dense rank-one term collapsing density benchmark axis
   315|  - Constraint-native interface = classical pipeline + tiny QPU contribution, not quantum sampling win
   316|  - **Activation**: dwave hybrid audit, quantum portfolio benchmark, QPU time analysis, constraint-native, classical decomposition, 量子组合优化审计
   317|
   318|### Quantum Portfolio Optimization: An Extensive Benchmark
   319|- [[quantum-finance-stack]] (enhanced) - 250-instance benchmark (up to 1000 assets): MIP solves all in seconds, classical heuristics outperform QA/QAOA (arXiv: 2509.17876)
   320|  - Only very limited room for quantum advantage in portfolio optimization
   321|  - Problem-tailored heuristic consistently outperforms quantum approaches for fixed runtime
   322|  - **Activation**: quantum portfolio benchmark, MIP vs quantum annealing, QAOA comparison, 量子组合优化基准
   323|
   324|### Hot-Starting Quantum Portfolio Optimization
   325|- [[hotstart-quantum-portfolio]] (enhanced) - Restricts search to compact Hilbert space around continuous optimum, reducing qubits and outperforming on D-Wave Advantage (arXiv: 2510.11153)
   326|  - Compact Hilbert space QUBO: O(N log δ) qubits vs O(N log M) standard
   327|  - Integrates relaxed continuous solution insights into discrete quantum search
   328|  - **Activation**: hot-start QUBO, quantum portfolio warm-start, compact Hilbert space, reduced qubit portfolio, 量子组合优化热启动
   329|
   330|### A Quantum Reservoir Computing Approach to Quantum Stock Movement Forecasting
   331|- [[quantum-reservoir-stock-forecasting]] (enhanced) - QRC with ≤6 qubits achieves >86% accuracy on 20 quantum-sector stock trend predictions, platform-agnostic (arXiv: 2602.13094)
   332|  - Predicts daily closing volumes (2020-2025) and minute-by-minute out-of-market volumes
   333|  - Optimal reservoir parameters identified; works on superconducting circuits and trapped ions
   334|  - **Activation**: quantum reservoir computing, QRC stock forecasting, quantum time-series prediction, small-scale quantum ML, 量子储备池计算股票预测
   335|
   336|

## 2026-05-30 - Hybrid Quantum Financial Security (Cron Job - Skill Created)

### HQFS: Hybrid Quantum Classical Financial Security with VQC Forecasting, QUBO Annealing, and Audit-Ready Post-Quantum Signing
- [[hybrid-quantum-financial-security]] - 端到端混合量子-经典金融安全管道，集成VQC预测、QUBO退火和后量子密码签名，统一金融风险管理中的预测与优化 (arXiv: 2602.16976)
  - 核心要点 1: VQC变分量子电路用于时间序列预测，捕获经典模型遗漏的非线性市场模式
  - 核心要点 2: QUBO退火整合真实市场约束（手数、仓位上限、行业限制），后量子签名确保审计合规
  - **Activation**: hybrid quantum finance, VQC forecasting, QUBO annealing, post-quantum finance, financial risk pipeline, HQFS, 混合量子金融, VQC预测, 后量子密码
