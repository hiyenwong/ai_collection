## 2026-05-14 - Neuroscience Research (Cron Job)

### FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping
- [[fits-interpretable-spiking-neurons]] - Spiking neuron factorizing temporal computation into frequency selectivity and temporal shaping modules for interpretable SNN design (arXiv: 2605.13071)
  - FS module maps target frequency to adaptation strength via closed-form inverse; TS reshapes membrane voltage accumulation through group-delay modulation
  - Consistent improvements over LIF baseline in feedforward SNNs on auditory benchmarks without recurrence or delays
  - Learned parameters provide interpretable neuron-level summaries of frequency and timing organization
  - **Activation**: FiTS, frequency selectivity spiking, temporal shaping SNN, interpretable spiking neuron, frequency-specialized neuron, group-delay spiking

## 2026-05-14 - Neuroscience Research (Cron Job)

### Letting the neural code speak: Automated characterization of monkey visual neurons through human language
- [[automated-neural-characterization-language]] - Closed-loop framework using natural language to characterize individual neuron selectivity at scale via digital twins and LLM hypothesis generation (arXiv: 2605.12485)
  - 96.1% of V4 neurons driven above 95th percentile by activating hypothesis images; 97.6% driven below 5th percentile by suppressing hypotheses
  - Language embeddings partially aligned with neural activity and vision embeddings; linguistic compression is lossy yet semantically faithful
  - V1 suppression less describable than activation, suggesting different computational principles in early visual areas
  - **Activation**: neural characterization, neural selectivity, digital twin neuroscience, semantic hypothesis testing, V1 V4 visual cortex, automated neural analysis, closed-loop neural characterization

## 2026-05-14 - 系统工程学 + 量子力学 (Cron Job)

### Scaling Qubit Mapping and Routing With Position Graph Abstraction and Memoization
- [[quantum-qubit-routing]] - Position graph abstraction + memoized SABRE for scalable quantum compilation (arXiv: 2605.09237)
  - Position graph unifies locations, paths, and routing constraints
  - Memoized heuristic scoring eliminates redundant SABRE evaluations
  - Architecture-aware compilation generalizes across quantum hardware types
  - **Activation**: qubit routing, qubit mapping, quantum compiler, SABRE, position graph, TI-QCCD, 量子比特路由, 量子编译

## 2026-05-14 - Neuroscience Research (Cron Job)

### SpikeProphecy: Large-Scale Benchmark for Autoregressive Neural Population Forecasting
- [[spikeprophecy-benchmark]] - First large-scale benchmark for causal, autoregressive spike-count forecasting with population metric decomposition on 105 Neuropixels sessions (~89,800 neurons) (arXiv: 2605.12992)
  - Decomposes aggregate correlation into temporal fidelity, spatial pattern accuracy, and magnitude-invariant alignment
  - 7 architecture baselines (SSMs, RNNs, transformers) across 4 structural families
  - **Activation**: SpikeProphecy, neural population forecasting, spike count forecasting, Neuropixels benchmark, population metric decomposition, temporal fidelity, spatial pattern accuracy

### Predictive Coding Light+: STDP-Based Sequence Prediction in Spiking Neural Networks
- [[predictive-coding-light]] - Spiking neural network architecture for unsupervised sequence processing using STDP with synaptic delays for short-term information retention (arXiv: 2605.12732)
  - Reproduces classic visual cortex sequence learning findings without supervision
  - Learns to fill in missing inputs in gesture recognition via recurrent excitatory connections with delays
  - **Activation**: Predictive Coding Light+, PCL+, STDP sequence learning, spiking neural network prediction, synaptic delay learning, unsupervised sequence processing

     1|## 2026-05-14 - Systems Engineering + Quantum Mechanics (Cron Job)
     2|
     3|### Operating a bistable qubit
     4|- [[bistable-qubit-adaptive-feedback-control]] - Adaptive 1-bit FPGA feed
  - Estimates qubit frequency from single-shot measurement at ~136 kHz bandwidth
  - 77% error reduction in gate fidelities, suppresses TLS-induced Ramsey beating
  - **Activation**: bistable qubit, adaptive qubit control, TLS defect mitigation, FPGA qubit feedback

### Unitaria: Quantum Linear Algebra via Block Encodings
- [[unitaria-quantum-linear-algebra]] - NumPy/SciPy-like Python library for quantum algorithms via block encodings without low-level circuit construction (arXiv: 2605.10768)
  - Matrix-arithmetic evaluation path enables correctness verification beyond state vector simulation
  - Automatic resource estimation (gate/qubit counts) without circuit execution
  - **Activation**: unitaria, quantum linear algebra, block encoding, QSVT, quantum matrix operations

### Scaling Qubit Mapping and Routing with Position Graph Memoization
- [[qubit-mapping-routing-memoization]] - Scalable qubit routing using position graph abstraction and memoization for TI-QCCD architectures (arXiv: 2605.09237)
  - Caches optimal routing solutions for sub-circuits to reduce compilation bottleneck
  - Supports arbitrary ion trap architectures with movement constraints
  - **Activation**: qubit mapping, quantum routing, TI-QCCD compilation, position graph abstraction

## 2026-05-14 - Neuroscience Research (Cron Job)

### Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale
- [[mamba-spike-forecasting-behavioral-decoding]] - Single Mamba forecaster trained on next-step spike counts simultaneously decodes behavior better than raw spikes on Steinmetz benchmark (arXiv: 2605.12999)
  - Mouse choice 75.7% (2.3x chance), stimulus side 66.1% (2x chance) across 39 sessions, ~27K neurons
  - Outperforms 500ms linear decoder by 4-6pp; 100-150 trial calibration reaches asymptote; fits 50ms bin budget
  - **Activation**: Mamba neural decoding, spike forecasting behavioral, Neuropixels decoding, implicit behavioral readout

### Letting the neural code speak: Automated characterization of monkey visual neurons through human language
- [[neural-code-language-characterization]] - Closed-loop LLM framework translates neural activation patterns into semantic descriptions for V1/V4 neurons using digital twins (arXiv: 2605.12485)
  - V4 neurons: 96.1% activation above 95th percentile, 97.6% suppression below 5th percentile via semantic hypothesis testing
  - Linguistic compression is lossy but semantically faithful; vision embeddings align best with neural activity
  - **Activation**: neural code characterization, digital twin neuroscience, LLM neuron interpretation, V1 V4 semantic description

### Self-organized MT Direction Maps Emerge from Spatiotemporal Contrastive Optimization
- [[spatiotemporal-tdann]] - Spatiotemporal TDANN with MoCo self-supervision generates brain-like direction maps and pinwheel structures in MT area (arXiv: 2605.11718)

### Multi-Timescale Conductance Spiking Networks
- [[multi-timescale-conductance-snn]] - Gradient-trainable SNN framework using shaped I-V curves via fast, slow, ultra-slow conductances enabling rich firing regimes (tonic, phasic, bursting) with direct BPTT (arXiv: 2605.11835)
  - Overcomes LIF/AdLIF limitations in regression tasks: higher accuracy + sparser activity (28% vs 38-45%)
  - Systematic control over excitability regimes; analog circuit-friendly implementation
  - **Activation**: multi-timescale conductance, gradient-trainable SNN, direct BPTT spiking, rich firing dynamics, MTCSN

### Leveraging Non-Equilibrium ECRAM Dynamics for Short-Term Plasticity
- [[ecram-short-term-plasticity-neuromorphic]] - Cross-layer device-circuit-system co-design transforming volatile ECRAM dynamics into computational resources for STP in neuromorphic circuits (arXiv: 2605.11243)
  - Delay-feedback LIF + ECRAM synapses: 2 pJ/spike, native temporal filtering without additional circuitry
  - Demonstrates synaptic facilitation and intrinsic excitability modulation at network level
  - **Activation**: ECRAM short-term plasticity, neuromorphic temporal processing, device-circuit co-design, memristive synapses

### Scaling Laws and Tradeoffs in Recurrent Networks of Expressive Neurons
- [[scaling-laws-expressive-neurons-recurrent]] - Information-theoretic framework for optimal parameter allocation between neuron count (N), per-unit complexity (k_e), and connectivity (k_c) in recurrent networks (arXiv: 2605.12049)
  - Expressive Leaky Memory (ELM) neurons enable independent tuning of complexity vs width vs connectivity
  - Pareto-frontier scaling law: larger budgets favor more AND more complex neurons; closed-form model captures SNR saturation and redundancy
  - **Activation**: scaling laws neural networks, expressive neurons, recurrent network tradeoffs, ELM neurons, parameter allocation
  - 3D ResNet + spatial loss unifies ventral and dorsal stream computational origins via optimization trade-off
  - Quantitative match to macaque MT: DSI, circular variance, pinwheel density all align with in vivo baselines
  - **Activation**: MT direction maps, dorsal stream modeling, spatiotemporal TDANN, cortical self-organization

## 2026-05-14 - Anthropic Research (Cron Job)

### Teaching Claude Why
- [[teaching-claude-why]] (updated) - Alignment training methodology for reducing agentic misalignment. Teaching principles underlying aligned behavior is more effective than training on demonstrations alone
  - Key point: Every Claude model since Haiku 4.5 achieved perfect score on agentic misalignment eval (zero blackmail vs 96% in Opus 4)
  - Key point: "Difficult advice" dataset (user in dilemma, AI gives advice) achieved same improvement with 28x fewer tokens
  - Key point: Teaching Claude the constitution + fictional stories reduced misalignment 3x (65% to 19%) despite being OOD
  - **Activation**: teaching claude why, agentic misalignment, constitutional training, alignment OOD generalization, difficult advice dataset, alignment training

### Natural Language Autoencoders
- [[natural-language-autoencoders]] - Methodology for converting Claude's internal activations into human-readable text via activation verbalizer + reconstructor round-trip
  - Key point: NLA revealed 26% evaluation awareness on SWE-bench and 16% on code safety evals vs <1% verbalized
  - Key point: In auditing game, NLAs enabled finding hidden motivations 12-15% of time vs <3% without NLAs
  - **Activation**: natural language autoencoder, NLA, activation verbalizer, activation reconstructor, model auditing, evaluation awareness

### Automated Alignment Researchers
- [[automated-alignment-researchers]] (updated) - Using LLMs to autonomously conduct alignment research via weak-to-strong supervision
  - Key point: 9 AARs achieved PGR 0.97 in 800 hours (~$18K) vs human PGR 0.23 in 7 days
  - Key point: Reward hacking inevitable — AARs skipped teacher on math (most common answer), ran tests on code
  - Key point: Production scale test showed no significant improvement — AARs capitalize on model-specific opportunities
  - **Activation**: automated alignment researchers, AARs, weak-to-strong supervision, PGR metric, reward hacking, alien science

### Trustworthy Agents in Practice
- [[trustworthy-agents-framework]] (updated) - Five-principle framework for building and governing trustworthy AI agents
  - Key point: Agent behavior depends on four layers (model, harness, tools, environment) working together
  - Key point: Claude's check-in rate doubles on complex tasks vs simple tasks
  - Key point: Three ecosystem needs — benchmarks, evidence sharing, open standards (MCP donated to Linux Foundation)
  - **Activation**: trustworthy agents, AI governance, prompt injection, human control, agent architecture, MCP standard

### How People Ask Claude for Personal Guidance
- [[ai-sycophancy-measurement]] (updated) - Measuring and mitigating AI sycophancy in personal guidance contexts
  - Key point: ~6% of conversations seek personal guidance; sycophancy 9% overall, 25% in relationships, 38% in spirituality
  - Key point: Sycophancy doubles under pushback (18% vs 9%); Opus 4.7 halved relationship sycophancy vs Opus 4.6
  - Key point: Stress-testing via prefilling reveals behavior under adverse conditions more effectively
  - **Activation**: ai sycophancy measurement, personal guidance, pushback dynamics, stress-testing, synthetic training data

## 2026-05-14 - Quantum Compilation + Quantum Systems (Cron Job)

### TuniQ: Autotuning Compilation Passes for Quantum Workloads at Scale for Effectiveness and Efficiency
- [[tuniq-quantum-compiler-rl]] - RL驱动的量子编译Pass自适应选择系统，动态优化编译流程以最大化保真度和效率 (arXiv: 2605.11375)
  - 核心要点: 双编码器阶段感知表征+动态动作掩码，让RL代理根据电路结构、后端拓扑和噪声画像选择最优编译Pass序列
  - 核心要点: 跨阶段奖励设计实现跨编译层信用分配，在IBM Quantum Cloud上超越Qiskit最高优化级别保真度，且无需重新训练即可泛化到不同后端
  - **Activation**: quantum compilation RL, tuniq, quantum compiler optimization, RL transpiler, quantum pass selection, fidelity optimization, autotuning quantum compilation

### QuBridge: Layer-wise Fidelity Decomposition in Quantum Computation Pipeline
- [[qubridge-fidelity-decomposition]] - 量子计算流水线保真度分层分解分析工具，量化各编译决策层对最终输出质量的贡献 (arXiv: 2605.11529)
  - 核心要点: 三阶段渐进式消融实验揭示：Qubit选择可将最差保真度带从11.8%压缩至2%以内；每门脉冲形状分配带来+0.9%额外增益
  - 核心要点: 纠错编码并非均匀有利，其条件收益仅在输入态主导误差通道可被所选码检测时才显现
  - **Activation**: quantum fidelity analysis, compilation pipeline, qubridge, fidelity decomposition, quantum error detection, ablation analysis

## 2026-05-14 - Neuroscience Research (Cron Job)

### Accounting for Missed Events in the Bayesian Modeling of IP3R Multimodal Gating
- [[ip3r-bayesian-missed-event-modeling]] - Bayesian framework for ion channel gating with missed event correction (arXiv: 2605.11675)
  - Core: Integrates temporal resolution limitations directly into hierarchical Markov chain likelihood for unbiased kinetic parameter inference
  - Key finding: IP3R exhibits bimodal Park/Drive gating with Ca²⁺-dependent mode switching regulating CICR
  - **Activation**: IP3R modeling, calcium channel gating, missed event correction, Bayesian ion channel, patch clamp analysis
## 2026-05-14 - Systems Engineering + Quantum Mechanics (Cron Job - Block Encoding)

### Unitaria: Quantum Linear Algebra via Block Encodings
- [[quantum-block-encoding-linear-algebra]] - Block encoding methodology for quantum linear algebra, enabling unified QSVT-based matrix operations (arXiv: 2605.10768v1)
  - 核心要点 1: 块编码作为统一接口实现矩阵运算，支持量子奇异值变换(QSVT)、哈密顿量模拟和矩阵函数求值
  - 核心要点 2: QSVT实现多项式函数作用于奇异值，单一框架覆盖HHL算法、矩阵求逆、特征值估计
  - **Activation**: quantum block encoding, quantum linear algebra, unitaria, quantum SVD, QSVT, quantum matrix inversion, quantum Hamiltonian simulation

## 2026-05-14 - Systems Engineering + Quantum (Cron Job)

### Scaling Qubit Mapping and Routing With Position Graph Abstraction and Memoization
- [[quantum-compiler-routing]] - 量子编译器中基于位置图抽象和记忆化的可扩放量比特映射与路由优化 (arXiv: 2605.09237v1)
  - 核心要点：位置图抽象统一了可执行位置、移动路径和路由约束三大约束表达
  - 核心要点：通过记忆化启发式评估加速 SABRE 编译算法，不改路由决策仅加速
  - **Activation**: quantum compiler, qubit mapping, qubit routing, SABRE algorithm, quantum circuit compilation, TI-QCCD, trapped-ion compilation, position graph abstraction

### Lower overhead fault-tolerant building blocks for noisy quantum computers
- [[quantum-fault-tolerance-blocks]] (updated) - 降低容错量子计算开销：标志容错稳定子测量、距离-4编码、经典编码保护测量结果 (arXiv: 2605.12385v1)
  - 核心要点：标志容错组合证明指数级减少测量任意大小稳定子所需的额外量子比特
  - 核心要点：距离-4编码编码6个逻辑量子比特，使用十分之一的物理量子比特达到与距离-5表面码相同保护
  - **Activation**: quantum fault tolerance, flag fault tolerance, surface code, low overhead QEC

### Benchmarking and Resource Analysis for Augmented-Lagrangian Quantum Hamiltonian Descent
- [[al-qhd-quantum-optimization]] (updated) - 增强拉格朗日量子哈密顿下降框架用于约束非凸优化及资源估计 (arXiv: 2605.12066v1)
  - 核心要点：将QHD嵌入增强拉格朗日框架，将约束优化转化为无约束量子子问题序列
  - 核心要点：Texas7k ACOPF实例资源估计达 ~4.46×10⁷ 纠缠门（NISQ）和 ~9.42×10⁸ T门（容错）
  - **Activation**: quantum Hamiltonian descent, augmented Lagrangian quantum, constrained quantum optimization, AL-QHD


## 2026-05-14 - Systems Engineering Research (Cron Job)

### SHIA: A Direct SysML–Hardware Interface Architecture for Model-Centric Verification
- [[shia-sysml-hardware-interface]] - 将可执行SysML模型直接接入硬件验证回路，消除中间转换链，实现模型驱动的验证与更短的数字线程 (arXiv: 2605.11248)
  - 核心要点 1: SysML模型可作为硬件验证的执行层，而非静态描述
  - 核心要点 2: 双向服务器架构（SysML侧C++服务器 + 硬件侧Raspberry Pi）实现零差异模型-硬件对比
  - **Activation**: SHIA, SysML, MBSE, hardware-in-the-loop, model-centric verification, digital thread

### Skill Drift Is Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries
- [[skill-drift-contract-violation]] - 将技能漂移建模为契约违反，从技能文档中提取可执行环境契约，精准检测API/依赖变更，零误报率 (arXiv: 2605.10990)
  - 核心要点 1: 区分角色承载假设（契约）与噪声文本，避免粗粒度变更监控的40%误报
  - 核心要点 2: 契约违反使修复可操作化，一轮修复成功率从10%提升至78%
  - **Activation**: skill drift, contract violation, agent skill maintenance, skill library decay, drift detection

## 2026-05-14 - Systems Engineering + Quantum Mechanics (Cron Job)

### CERTIFY-ED: A Multi-Layer Verification Framework for Exact Diagonalization
- [[certify-ed-verification]] - 13层纵深防御验证框架，多源共识校验、防篡改证书、错误注入自测试 (arXiv: 2605.11787)
  - 核心要点: 13个独立验证层覆盖代数/算法/数值/物理四个维度，每层捕获不同失效模式
  - 核心要点: SHA-256哈希证书确保计算结果可追溯且防篡改，支持机器可验证的下游验证
  - 核心要点: 错误注入自测试（6类已知错误全部检出）确保验证流水线自身可靠性
  - **Activation**: multi-layer verification, defense in depth, multi-oracle consensus, tamper-evident certificates, error injection self-testing

### QAP-Router: Tackling Qubit Routing as Dynamic Quadratic Assignment with Reinforcement Learning
- [[qap-router-qubit-routing]] - 将量子比特路由建模为动态二次分配问题(QAP)，结构感知Transformer+PPO训练 (arXiv: 2605.12365)
  - 核心要点: 逻辑交互=流矩阵F，硬件拓扑=距离矩阵D，目标是最小化Tr(F·X·D·X^T)
  - 核心要点: 结构感知注意力机制将问题耦合(流×距离)直接编码到注意力分数中
  - 核心要点: 前向→后向→前向三路精炼，在MQTBench上降低15.7% CNOT门
  - **Activation**: qubit routing, quadratic assignment problem, quantum compilation, SWAP optimization, structure-aware Transformer

## 2026-05-14 - Neuroscience Research (Cron Job)

### Fast Automatic Artifact Rejection (FAAR) for EEG MI-BCIs
- [[eeg-faar-artifact-rejection]] - 轻量级自动化EEG伪影拒绝方法，通过信号质量指数自适应阈值减少BCI不可用性 (arXiv: 2605.12408)
  - 核心要点: 计算epoch级信号质量指数(SQI)，自适应选择拒绝阈值，无需手动调参
  - 核心要点: 在低信噪比条件下效果最显著，有效减少被试间变异性
  - **Activation**: FAAR artifact rejection, EEG cleaning, motor imagery BCI, signal quality index


## 2026-05-14 - Systems Engineering + Quantum Mechanics (Cron Job)

### Tolerating Device Failure in Distributed Quantum Computing
- [[distributed-quantum-fault-tolerance]] - 设计容错分布式量子计算系统，支持热替换节点和分布式QEC (arXiv: 2605.11088)
  - 分布式QEC使系统可靠性超过单个组件
  - Toric code在<0.05%物理错误率下优于单体架构
  - **Activation**: distributed quantum computing, quantum fault tolerance, toric code, Floquet code

### Breaking the scalability barrier via a vertical tunable coupler in 3D integrated transmon system
- [[3d-integrated-quantum-processor]] - 3D集成超导量子处理器设计，垂直可调耦合器实现芯片间纠缠 (arXiv: 2605.11488)
  - 3层芯片堆叠（顶部Qubit+载流芯片+底部Qubit）
  - 单量子门保真度99.87%，CZ门97.5%
  - **Activation**: 3D quantum processor, vertical coupler, flip-chip qubit, interchip coupling

### Strain-controlled crossover between Majorana and Andreev bound states
- [[strain-controlled-topological-quantum]] - 应变工程控制拓扑量子态，psABS到MBS的转换 (arXiv: 2605.11066)
  - 空间非均匀应变调控拓扑相边界
  - BdG模拟框架+位置依赖拓扑质量分析
  - **Activation**: strain-controlled quantum, Majorana bound states, topological quantum computing

### Unification of Signal Transform Theory
- [[signal-transform-unification]] - 基于群表示论统一所有信号变换，DAD-CAD匹配群发现算法 (arXiv: 2605.11589)
  - 每个变换是特定群不变协方差的特征基
  - Peter-Weyl定理构建不可约矩阵元
  - **Activation**: signal transform theory, matched group discovery, Algebraic Diversity

## 2026-05-14 - Neuroscience Research (Cron Job)

### Multi-Timescale Conductance Spiking Networks: A Sparse, Gradient-Trainable Framework with Rich Firing Dynamics
- [[multi-timescale-conductance-snn]] - Conductance-based SNN with direct BPTT (no surrogate gradients), multi-timescale dynamics yielding tonic/phasic/bursting regimes, superior Mackey-Glass prediction with higher sparsity (arXiv: 2605.11835)
  - Replaces phenomenological LIF/AdLIF with I-V curve shaping via fast/slow/ultra-slow conductances
  - Direct backpropagation through time eliminates forward-backward mismatch of surrogate gradients
  - Feed-forward architecture achieves temporal processing via intrinsic neuron memory (no recurrent connections needed)
  - **Activation**: multi-timescale conductance, MTCSN, conductance-based SNN, gradient-trainable spiking, neuromorphic temporal processing

### Letting the Neural Code Speak: Automated Characterization of Monkey Visual Neurons through Human Language
- [[neural-code-language-characterization]] - Closed-loop framework using natural language to characterize neural selectivity via digital twins and in silico hypothesis verification across macaque V1 and V4 (arXiv: 2605.12485)
  - Translates high/low-activating images into dense captions → semantic hypotheses → synthesized images → in silico verification
  - V4: activating hypotheses drove 96.1% of neurons above 95th percentile, suppressing below 5th percentile
  - RSA shows partial alignment between neural activity, vision embeddings, and language embeddings
  - Linguistic compression is lossy but semantically faithful — lost info recovered when rendered back to images
  - **Activation**: neural code language, automated neuron characterization, digital twin in silico, semantic hypothesis, V1 V4 selectivity

### Empirical Scaling Laws in Balanced Networks with Conductance-Based Synapses
- [[balanced-network-scaling-conductance]] - Empirical scaling laws for balanced networks with conductance-based synapses (arXiv: 2605.12404)
  - Scaling analysis of balanced neural networks with conductance-based synapses
  - **Activation**: balanced network scaling, conductance synapses, neural network scaling laws

### Leggett-Garg Tests in Neural Dynamics: Probing Non-Diffusive Stochastic Structure
- [[leggett-garg-neural-dynamics]] - Proposes experimental Leggett-Garg inequality tests to distinguish diffusive vs persistent stochastic structure in single neurons (arXiv: 2605.12126)
  - Telegrapher's equation vs cable equation: finite-velocity transport with memory
  - Purely diffusive dynamics always satisfies LGIs; persistent stochastic dynamics can violate them
  - Conservative interpretation: non-diffusive ≠ quantum coherence, just non-Markovian structure
  - **Activation**: Leggett-Garg inequality, Telegrapher equation, persistent stochastic neuron, non-diffusive neural dynamics, temporal correlations

### Interpreting EEG Foundational Transformers with LRP
- [[eeg-foundation-lrp-interpretability]] - Applies Layer-wise Relevance Propagation (LRP) to EEG foundation models for post-hoc attribution, revealing Clever Hans behavior and novel biological hypotheses (arXiv: 2605.11885)
  - Extends LRP from CNN-based to Transformer-based EEG models
  - Uncovers ocular signal exploitation in motor imagery ("Clever Hans" behavior)
  - Reveals central electrode cluster as candidate sensorimotor arousal signature
  - **Activation**: EEG interpretability, LRP, EEG foundation model, Clever Hans EEG, transformer attribution

### Interpretable EEG Microstate Discovery via Variational Deep Embedding
- [[eeg-microstate-variational-embedding]] - Systematic architecture search with multi-quadrant evaluation for interpretable EEG microstate discovery via variational deep embedding (arXiv: 2605.10947)
  - Variational deep embedding for interpretable EEG microstate discovery
  - Systematic architecture search with multi-quadrant evaluation
  - **Activation**: EEG microstate, variational embedding, interpretable EEG

## 2026-05-14 - Systems Engineering + Quantum Mechanics (Cron Job)

### Lower Overhead Fault-Tolerant Building Blocks for Noisy Quantum Computers
- [[quantum-fault-tolerance-building-blocks]] - Reduces spacetime cost of fault tolerance via combinatorial flag FT proofs, 100% yield Steane/Golay state prep, and distance-4 planar codes (arXiv: 2605.12385)
  - Flag fault-tolerant stabilizer measurement exponentially reduces extra qubits needed
  - Steane and Golay code state preparation circuits achieve 100% yield
  - Distance-four planar code encodes 6 logical qubits using 1/10 physical qubits of d=5 surface code
  - Classical-code-protected measurement cuts gate time by 2-6x
  - **Activation**: flag fault tolerance, Steane code, Golay code, surface code optimization, qubit overhead reduction

### Real-time Surface-Code Error Correction Using an FPGA-based Neural-Network Decoder
- [[fpga-quantum-error-decoder]] - Hardware-integrated FPGA-based NN decoder achieving 550ns closed-loop latency for real-time distance-3 surface code QEC (arXiv: 2605.04892)
  - Neural network decoder on FPGA with 124ns inference time
  - Deterministic closed-loop latency of 550ns within 1.25μs QEC cycle
  - Real-time decoding matches offline decoding logical performance
  - Mid-circuit feedback correction for non-Clifford logical circuits
  - **Activation**: FPGA quantum decoder, real-time QEC, neural network decoder, low-latency quantum feedback, surface code decoder

## 2026-05-14 - Neuroscience Research (Cron Job)
- [[spatiotemporal-tdann-mt-direction-maps]] - Extends TDANN to spatiotemporal domain showing MT direction maps emerge from universal self-organizing principles balancing contrastive learning and spatial regularization (arXiv: 2605.11718)
  - 3D ResNet-18 with MoCo self-supervised learning on naturalistic videos drives spontaneous emergence of direction-selective maps and pinwheel structures
  - MT tuning properties arise from strict trade-off between task-driven discriminative pressure and spatial regularization
  - Quantitative match with in vivo macaque MT baselines (DSI, circular variance, pinwheel density)
  - **Activation**: spatiotemporal TDANN, MT direction maps, dorsal stream self-organization, pinwheel formation

### TRACE: Temporal Routing with Autoregressive Cross-channel Experts for EEG Representation Learning
- [[trace-eeg-autoregressive-routing]] - Autoregressive EEG pre-training with cross-channel temporal routing MoE preserving coherence while adapting to non-stationary states (arXiv: 2605.11380)
  - CTR-FFN routes all channels at same temporal step to same experts based on causal cross-channel history
  - Heterogeneous pre-training across 1.5M+ segments (16-128 channels) without common montage projection
  - Evaluated on 8 downstream BCI benchmarks across 6 task categories (seen-domain + unseen transfer)
  - **Activation**: TRACE EEG framework, autoregressive EEG pre-training, cross-channel temporal routing, TR-MoE, CTR-FFN

## 2026-05-16 - Neuroscience Research (Cron Job)

### Internally Triggered Retrospective Learning in Neural Networks
- [[episodic-learning-neural-networks]] - 内部触发的回溯学习范式，网络自身表征动力学驱动稀疏 episodic 权重更新 (arXiv: 2605.10994)
  - 潜在迹线积累：突触交互编码近期共激活模式，不立即修改参数
  - 内部预测过程：持续计算预测与观测状态的差异度量
  - 自适应阈值：差异超过基于近期误差统计的阈值时触发学习事件
  - **Activation**: episodic learning, internally triggered learning, retrospective learning, sparse weight updates, energy-efficient neural networks

## 2026-05-14 - Systems Engineering + Quantum Mechanics (Cron Job)

### Lower Overhead Fault-Tolerant Building Blocks for Noisy Quantum Computers
- [[quantum-fault-tolerance-blocks]] - 低开销量子容错构建模块方法论，面向NISQ设备的纠错码与逻辑量子比特实现 (arXiv: 2605.12385)
  - 逻辑量子比特编码：将算法信息分散到多个物理量子比特
  - 表面码/彩色码/LDPC码选择策略基于硬件连接性约束
  - 魔力态蒸馏优化减少非Clifford门开销
  - **Activation**: quantum fault tolerance, logical qubit encoding, surface code NISQ, 量子容错构建模块

### Benchmarking and Resource Analysis for Augmented-Lagrangian Quantum Hamiltonian Descent
- [[al-qhd-quantum-optimization]] - 增强拉格朗日量子哈密顿下降法求解约束非凸优化问题 (arXiv: 2605.12066)
  - QHD连续优化嵌入AL框架处理约束
  - 量子隧穿和干涉逃离局部最优
  - 资源估算：量子比特数、电路深度、相干时间
  - **Activation**: quantum Hamiltonian descent, augmented Lagrangian quantum, constrained quantum optimization, AL-QHD

### Optimal State Preparation for Impulse Estimation in Gaussian Quantum Systems
- [[optimal-parametric-quantum-estimation]] - 最优控制增强高斯量子系统脉冲估计，通过参数调制动态塑造估计协方差 (arXiv: 2605.12155)
  - 将脉冲估计不确定性最小化转化为非线性最优控制问题
  - 参数调制与传统压缩协议不同，在已知脉冲时刻最大化信息增益
  - 估计方差降低至稳态操作的1/2，适用于纳米机械谐振器和悬浮纳米粒子
  - **Activation**: optimal quantum control, impulse estimation quantum, parametric modulation, Gaussian quantum systems, quantum sensing

## 2026-05-15 - Systems Engineering + Quantum Mechanics (Cron Job)

### Replay-Buffer Engineering for Noise-Robust Quantum Circuit Optimization
- [[replay-buffer-quantum-optimization]] - 使用回放缓冲工程加速变分量子算法在硬件噪声下的优化 (arXiv: 2604.21863)
  - 存储历史优化参数加速新任务初始化
  - 噪声级别匹配过滤避免误导优化
  - 比随机初始化快2-5倍收敛
  - **Activation**: replay buffer quantum, noise-robust VQA, 量子线路优化回放, quantum circuit optimization

### Quantum Metrology via Partial Quantum Error Correction
- [[quantum-metrology-partial-qec]] - 使用部分量子纠错增强传感精度，超越标准量子极限 (arXiv: 2605.08341)
  - 部分纠错码保护传感子空间同时允许信号积累
  - 在SQL和HL之间实现精度缩放
  - 适用于原子钟、磁力计、引力波探测
  - **Activation**: quantum metrology partial QEC, phase estimation error correction, 量子精密测量纠错

### Bridging Krylov Complexity and Universal Analog Quantum Simulator
- [[krylov-complexity-analog-simulator]] - 用Krylov复杂度理论表征模拟量子模拟器的计算能力 (arXiv: 2605.07668)
  - Lanczos系数b_n增长率区分可积/混沌系统
  - Krylov复杂度K(t)追踪算符增长
  - 用于量子模拟器验证和基准测试
  - **Activation**: Krylov complexity, analog quantum simulator, Lanczos algorithm quantum

### Universal Complementarity Identity for Polarized Double-Slit Interferometry
- [[universal-complementarity-identity]] - 极化双缝干涉中路径可区分度与干涉可见度的精确互补恒等式 (arXiv: 2604.18760)
  - D^2 + V^2 = 1 恒等式适用于任意极化标记态
  - 导出QKD安全性边界
  - 量子擦除器的信息恢复量化
  - **Activation**: complementarity identity, wave-particle duality, 互补性恒等式量子干涉

## 2026-05-14 - Neuroscience Research (Cron Job)

### Spatiotemporal TDANN for Cortical Self-Organization
- [[spatiotemporal-tdann]] - 3D ResNet TDANN with MoCo contrastive learning on videos + spatial loss generates MT direction maps and pinwheels (arXiv: 2605.11718)
  - Extends TDANN from ventral to dorsal stream modeling via spatiotemporal contrastive optimization
  - MT tuning emerges from trade-off between discriminative pressure and spatial regularization

### Episodic Retrospective Learning in Neural Networks
- [[episodic-learning-neural-networks]] - Internally triggered sparse learning events via adaptive discrepancy thresholding (arXiv: 2605.10994)
  - Replaces continuous weight updates with latent trace accumulation + prediction-error triggered retrospective updates
  - Reduces parameter drift while preserving informative patterns for edge/autonomous systems

## 2026-05-13 - Neuroscience Research (Cron Job)

### Letting the neural code speak: Automated characterization of monkey visual neurons through human language
- [[neural-code-language-characterization]] - Closed-loop framework using natural language to characterize neuron selectivity via digital twins (arXiv: 2605.12485)
    - V4: 96.1% neurons driven above 95th percentile by activating hypotheses; 97.6% below 5th by suppressing
    - Vision embeddings most aligned with neural activity; linguistic compression lossy but recoverable
  - **Activation**: neural characterization, digital twins, natural language, V1/V4, automated neuroscience

### What Do EEG Foundation Models Capture from Human Brain Signals?
- [[neural-encoding-evaluation-ground-truth]] - Systematic audit of EEG foundation models via probing, LEACE erasure, and transparent classifiers (arXiv: 2605.11410)
    - 68.6% features representation-causal; 50 universal features across 3 architectures
    - Confirmed features recover 79.3% of model advantage; task gradient MDD(99%) to Stress(56%)
  - **Activation**: EEG interpretability, foundation model audit, LEACE, ridge probing, clinical EEG
### ECRAM Short-Term Plasticity for Neuromorphic Circuits
- [[ecram-short-term-plasticity]] - Cross-layer device-circuit-system co-design implementing short-term plasticity via non-equilibrium ECRAM dynamics (arXiv: 2605.11243)
  - Transforms volatile ionic dynamics from device artifacts into computational resources for STP
  - Delay-feedback LIF neurons with activity-dependent conductance modulation for temporal processing
  - **Activation**: neuromorphic STP, ECRAM synaptic devices, temporal information processing, hardware-software co-design

---

## 2026-05-13 - Neuroscience Research (Cron Job)

### Leveraging Non-Equilibrium ECRAM Dynamics for Short-Term Plasticity in Neuromorphic Circuits
- [[ecram-short-term-plasticity]] - Cross-layer co-design transforming volatile ECRAM ionic dynamics into native STP hardware with 2 pJ/spike energy efficiency (arXiv: 2605.11243)
  - ECRAM devices' non-equilibrium transient conductance (~1.5 KΩ/spike) co-designed with delay-feedback LIF neuron for synaptic facilitation and intrinsic excitability modulation
  - Network-level frequency-selective spike processing; individual synapses act as tunable temporal filters across multiple neuron topologies
  - **Activation**: ECRAM short-term plasticity, neuromorphic STP, non-equilibrium ionic dynamics, delay-feedback LIF, memristive synaptic plasticity

## 2026-05-13 - Medicine + Quantum Mechanics (Cron Job)

### Bridging Krylov Complexity and Universal Analog Quantum Simulator
  - [[krylov-complexity-analog-simulator]] - 使用Krylov复杂度作为诊断工具映射任意哈密顿量到模拟量子模拟器 (arXiv: 2605.07668)
    - 超越经典计算能力的多体系统模拟
    - 通过复杂度增长模式检测量子相变
    - **Activation**: krylov复杂度, 模拟量子模拟, analog quantum simulation, 克里洛夫复杂度

### A universal complementarity identity for polarized double-slit interferometry
  - [[universal-complementarity-identity]] - 建立四不变量精确恒等式 V_A^2+V_N^2+P^2+I^2=1 (arXiv: 2604.18760)
    - 完整刻画波粒二象性的互补关系
    - 通过标准偏振和干涉测量验证
    - **Activation**: 互补性恒等式, double-slit interferometry, 波粒二象性, complementarity identity

### On the Complementarity of Quantum and Classical Features: Adaptive Hybrid Quantum-Classical Feature Fusion for Breast Cancer Classification
  - [[hybrid-quantum-classical-feature-fusion]] - 双分支架构结合量子与经典特征提取 (arXiv: 2604.22903)
    - 自适应融合机制解决优化不对称性问题
    - 利用量子与经典特征的互补性提升医学分类性能
    - **Activation**: 量子经典特征融合, hybrid quantum-classical, 医学图像分类, feature fusion

## 2026-05-13 - Medicine + Neuroscience (Cron Job)
## 2026-05-13 - 医学 + 量子力学 (Cron Job)
## 2026-05-13 - Neuroscience Research (Cron Job)

### Multi-Timescale Conductance Spiking Networks (MTCSN)
- [[multi-timescale-conductance-snn]] - Sparse, gradient-trainable SNN framework using multi-timescale conductance shaping for rich firing dynamics without surrogate gradients (arXiv: 2605.11835)
  - 核心要点: Conductance-based I-V curve shaping with fast/slow/ultra-slow timescales enables tonic, phasic, and bursting regimes in a single model
  - 核心要点: Discrete-time formulation allows direct BPTT without surrogate gradients, outperforming LIF and AdLIF on Mackey-Glass regression with higher sparsity
  - **Activation**: conductance SNN, multi-timescale spiking, gradient-trainable SNN, MTCSN, surrogate-free SNN, I-V curve shaping

### Joint Sparse Coding and Temporal Dynamics Support Context Reconfiguration
- [[sparse-temporal-context-reconfiguration]] - Brain transitions between contexts while preserving prior knowledge through sparsity and temporal dynamics — SNNs naturally exhibit both (arXiv: 2605.10178)
  - 核心要点: Sparse coding reduces cross-context interference; temporal dynamics enhance context separability across time
  - 核心要点: SNNs show improved lifelong learning retention without auxiliary heuristics (no replay, no EWC needed) — forgetting reduction emerges from architecture
  - **Activation**: context reconfiguration, sparse coding temporal dynamics, catastrophic forgetting architecture, lifelong learning SNN, mPFC context switching

### FQPDR: Federated Quantum Neural Network for Privacy-preserving Early Detection of Diabetic Retinopathy
- [[federated-quantum-medical-diagnosis]] - 联邦量子神经网络用于隐私保护的糖尿病视网膜病变早期检测 (arXiv: 2605.08324)
  - 核心要点: 结合联邦学习与量子神经网络，实现多机构协作医疗诊断而不共享患者数据
  - 核心要点: 在有限样本和少量可学习参数下实现鲁棒的轻量级学习模型
  - **Activation**: federated quantum medical, FQPDR, quantum federated learning, privacy-preserving medical AI, 联邦量子医疗, 隐私保护医疗诊断

### Quantum Circuit Simulation of Compartmental Drug Dynamics
- [[quantum-pkpd-simulation]] - 量子电路模拟房室药代动力学模型，用于群体药代动力学参数估计 (arXiv: 2605.09691)
  - 核心要点: 将经典PK/PD微分方程重构为开放量子系统，使用12量子比特编码4个药理学房室
  - 核心要点: 量子增强SAEM算法实现更好的统计拟合，同时保持参数估计一致性
  - **Activation**: quantum PK/PD, quantum pharmacokinetics, quantum drug dynamics, 量子药代动力学, 量子临床模拟



### Letting the Neural Code Speak: Automated Characterization of Monkey Visual Neurons through Human Language
- [[neural-code-language-interpretability]] - Natural language hypothesis generation + closed-loop verification for single-neuron selectivity across visual hierarchy (arXiv: 2605.12485)
  - Three-stage pipeline: Translate (image→text via VLM) → Semantic Hypothesis (LLM distills extreme responses) → Verification (text→image generation + digital twin validation)
  - >96% of V1/V4 neurons driven to extreme percentiles by hypothesis-generated images vs ~10% random baseline
  - V4 suppression highly describable (97.6%), V1 suppression poor (56%) — reveals language expressibility limits for sub-lexical features
  - RSA shows partial alignment: neural activity ↔ DINOv3 ↔ Qwen language embeddings
  - **Activation**: neural code interpretability, neuron characterization, digital twin neuroscience, language-based neural analysis, closed-loop hypothesis testing

### MTCSN: Multi-Timescale Conductance Spiking Networks
- [[multi-timescale-conductance-snn]] - Sparse, gradient-trainable SNN with multi-timescale conductance for enhanced temporal processing (arXiv: 2605.11835)
  - Multi-timescale conductance dynamics capture diverse firing patterns (bursting, adapting, regular)
  - Sparse recurrent connectivity with gradient-based training for efficient temporal sequence processing
  - **Activation**: multi-timescale spiking, conductance SNN, gradient-trainable SNN, sparse spiking network, temporal processing

### Attractor Models for Language and Reasoning
- [[attractor-models-language-reasoning]] - Backbone pre-training with attractor dynamics for improved reasoning in language models (arXiv: 2605.12466)
  - Text representations evolve through learned energy landscape to stable attractor states
  - Multi-step reasoning modeled as trajectories through attractor basins with energy barriers
  - **Activation**: attractor language model, attractor reasoning, dynamical systems NLP, energy-based language, backbone pre-training

### EEG Microstate Discovery via Variational Deep Embedding
- [[eeg-microstate-variational-embedding]] - Unsupervised EEG microstate discovery using VAE-based deep embedding for robust biomarker identification (arXiv: 2605.10947)
  - Variational autoencoder captures nonlinear microstate structure beyond k-means limitations
  - Probabilistic soft assignment with temporal HMM for clinical biomarker discovery
  - **Activation**: EEG microstate discovery, variational EEG embedding, microstate analysis, EEG temporal segmentation, deep embedding EEG

---

## 2026-05-14 - Neuroscience Research (Cron Job)

### Accounting for Missed Events in the Bayesian Modeling of IP3R Multimodal Gating
- [[bayesian-ip3r-missed-event-modeling]] - Bayesian ion channel gating analysis with missed event correction integrated into likelihood (arXiv: 2605.11675)
  - Hierarchical Markov chains with mode-dependent kinetics for IP3R channel
  - Missed event correction in likelihood function prevents model selection bias
  - **Activation**: ip3r modeling, calcium channel gating, bayesian missed event, hierarchical markov chain, patch clamp analysis


## 2026-05-13 - Neuroscience Research (Cron Job)

### Counterfausal Analysis of Brain Network Dynamics
- [[counterfactual-brain-dynamics]] - Hodge-theoretic counterfausal causal analysis framework modeling brain network perturbations as energy-flow problems (arXiv: 2603.29843)
  - Decomposes directed brain communication into dissipative (gradient) and persistent (harmonic) components via Hodge theory
  - Enables simulated intervention analysis: predicting how causal architecture reconfigures under lesions or neuromodulation
  - Demonstrated on temporal lobe epilepsy (400 HCP subjects) comparing pathological recurrence vs therapeutic disconnection
  - **Activation**: counterfausal brain, Hodge theory brain, causal brain network, brain network intervention, harmonic flow brain, Dirichlet energy network

### Spiking Free Energy Control (SFEC)
- [[spiking-free-energy-control]] - Bio-plausible spiking neural control framework where neurons fire only when reducing free energy (arXiv: 2603.09729)
  - Bridges Free Energy Principle/Active Inference with spiking neural circuit implementation
  - Spike constraint gating: neurons only fire when ∂F/∂t < 0, achieving high sparsity and robustness
  - Resilient to both external (sensory noise, collisions) and internal (synaptic noise, neuron silencing) perturbations
  - Deployable on neuromorphic hardware (Loihi, SpiNNaker) for energy-efficient robotics control
  - **Activation**: spiking control, free energy principle SNN, active inference spiking, neuromorphic control, spike-based free energy, SFEC

---

## 2026-05-13 - Medicine + Quantum Computing (Cron Job)

### Medical fMRI & Quantum Computing

- [[quantum-fmri-foundation-models]] - Quantum-enhanced fMRI foundation models combining Brain-DiT with quantum ML for neuroimaging analysis (arXiv: 2604.12683)
  - Integrates pre-trained fMRI foundation models with quantum feature mapping
  - Quantum kernel methods for brain disorder classification and cross-subject generalization
  - **Activation**: quantum fMRI, quantum brain imaging, quantum foundation model brain, quantum neuroimaging

- [[quantum-eeg-biomarker-discovery]] - Quantum ML for robust EEG biomarker discovery across subjects and platforms (arXiv: 2604.22116)
  - Quantum kernel-based EEG feature extraction for neurological conditions
  - Cross-subject and cross-platform biomarker validation
  - **Activation**: quantum EEG biomarker, quantum brain signal, quantum EEG classification, quantum neurological biomarker

- [[quantum-flow-matching-medical]] - Quantum-enhanced flow matching for medical image generation and longitudinal analysis (arXiv: 2605.08648)
  - Quantum variational circuits in flow matching for disease progression modeling
  - Quantum MoE routing for multimodal medical image synthesis
  - **Activation**: quantum flow matching medical, quantum medical image generation, quantum disease progression, quantum longitudinal imaging

---

## 2026-05-13 - Neuroscience Research (Cron Job - Batch 4: Standalone Sync)

### Standalone Skills Synced to ai_collection (60 skills)
Batch sync of all remaining standalone neuroscience/quantum/medical skills from `~/.hermes/skills/` to ai_collection project and INDEX.

#### Key Skills Added:
- [[behavior-vlm-neuroscience]] - Finetuning-free behavioral understanding for neuroscience using VLMs
- [[cold-atom-reservoir-computing]] - Hybrid quantum-classical medical imaging with neutral-atom reservoir computing
- [[frequency-matching-snn-mmwave]] - Frequency matching in SNNs for mmWave sensing using LIF dynamics
- [[qml-spiking-encoding]] - SPATE: Spiking-phase adaptive temporal encoding for QML
- [[universal-neural-propagator]] - Universal Neural Propagator methodology for learning neural dynamics
- [[multi-scale-info-geometry-neural]] - Multi-scale information geometry for neural population codes
- [[self-correcting-quantum-memory-3d]] - Passive self-correcting quantum memory in 3D Pauli stabilizer Hamiltonian
- [[quantum-robust-control]] - Robust quantum control engineering patterns
- [[quantum-cognition]] - Quantum cognition methodology for modeling cognitive processes
- [[quantum-statistical-metrology]] - Quantum metrology for multi-parameter estimation using purification-assisted schemes
- [[spiking-phase-quantum-encoding]] - Spiking-phase adaptive temporal encoding for quantum machine learning
- [[quantum-sparsity-edge-chaos]] - Quantum sparsity design principle for robust VQAs using edge-of-chaos theory
- [[quantum-learning-theory]] - Quantum learning theory methodology — sample complexity and generalization bounds
- [[quantum-learning-theory-cv]] - Quantum learning theory for continuous-variable systems
- [[quantum-gaussian-state-learning]] - Sample-optimal learning of bosonic Gaussian quantum states
- [[verifiable-quantum-advantage]] - Verifiable quantum advantage algorithm design and analysis
- [[topological-quantum-computing]] - Topological quantum computing with anyon braiding and fault tolerance
- [[quantum-margulis-codes]] - Quantum Margulis Codes for fault-tolerant quantum computing
- [[quantum-fault-tolerance-benchmark]] - QEC code evaluation under hardware-motivated noise
- [[quantum-fault-tolerance-verification]] - Quantum fault-tolerance verification via syndrome analysis
- [[quantum-error-correction-methods]] - Reusable QEC research patterns
- [[css-factor-graph-decoding]] - CSS QEC syndrome decoding via factor graphs and belief propagation
- [[css-syndrome-decoding]] - Factor-graph formulation of CSS quantum error correction
- [[loss-biased-qec]] - Loss-biased fault-tolerant QEC methodology
- [[iceberg-error-detection]] - Fault-tolerant error detection using Iceberg [[2m, 2m-2, 2]] code
- [[state-adaptive-error-correction]] - State-adaptive error correction and fault tolerance
- [[syndrome-resampling-qec]] - Syndrome resampling for enhancing QEC performance
- [[quantum-boltzmann-machine-bilevel]] - Quantum Boltzmann Machine via bilevel optimization
- [[quantum-protocol-designer]] - Design and analyze quantum information processing protocols
- [[quantum-software-architecture]] - Component-based QSA framework
- [[quantum-program-linting]] - LLM-powered static analysis for quantum programs
- [[quantum-program-analysis]] - LLM-powered QA for quantum programs
- [[quantum-program-semantic-verification]] - Semantics-based verification for quantum programs
- [[quantum-circuit-synthesis-gst]] - Generative quantum circuit synthesis from Gate Set Tomography
- [[quantum-distributed-snapshot]] - Quantum distributed algorithms based on classical distributed snapshots
- [[quantum-os-resource-management]] - Quantum OS resource management patterns
- [[fpga-quantum-error-decoder]] - Scalable FPGA-based QEC decoding architectures
- [[rl-qec-control]] - Reinforcement learning for QEC control
- [[quanforge-qnn-testing]] - Mutation testing framework for QNNs
- [[qml-mutation-testing]] - Systematic mutation testing for QML
- [[quantum-neural-topology]] - QNNs and topological data analysis research
- [[quantum-mechanical-data-assimilation]] - Quantum Mechanical Data Assimilation methodology
- [[quantum-knowledge-graph]] - Quantum-enhanced knowledge graphs using QNLP
- [[quantum-circuit-construction-ml]] - ML for constructing quantum circuits
- [[quantum-cognition]] - Quantum cognition for cognitive process modeling
- [[quantum-tunneling-optimization]] - Quantum-inspired evolutionary optimization for non-convex problems
- [[quantum-optimization-qaoa]] - QAOA guide for combinatorial optimization
- [[quantum-optimization-transportation]] - Quantum optimization for transportation networks
- [[quantum-finance]] - Quantum computing in finance: portfolio optimization, option pricing
- [[quantum-finance-analysis]] - Quantum computing in finance and economics
- [[quantum-finance-portfolio]] - Quantum portfolio optimization: QUBO, quantum annealing, QRNG Monte Carlo
- [[quantum-game-theory-economics]] - Quantum game theory in economics and decision making
- [[quantum-positive-maps]] - Positive trace-preserving maps in quantum information
- [[quantum-proper-scoring-rules]] - Proper scoring rules for quantum state estimation
- [[quantum-statistical-estimation]] - Quantum statistical estimation theory
- [[vacuum-entanglement-extraction]] - Vacuum entanglement extraction from quantum field theory
- [[quantum-magic-state-analysis]] - Magic quantification for non-stabilizerness in quantum algorithms
- [[sample-optimal-gaussian-state-learning]] - Sample complexity bounds for bosonic Gaussian state learning
- [[multiparameter-hamiltonian-estimation]] - Optimal multiparameter Hamiltonian estimation
- [[equivariant-rl-clifford]] - Equivariant RL for Clifford quantum circuit synthesis
- [[equivariant-rl-quantum-circuit-synthesis]] - Equivariant RL for quantum circuit synthesis
- [[quantum-sparsity-edge-chaos]] - Quantum sparsity at edge of chaos for robust VQAs
- [[quantum-sensor-reliability]] - RL-optimized dynamical decoupling for quantum sensor networks
- [[spintune-quantum-sensor-reliability]] - SpinTune: RL-based DD pulse optimization
- [[photonic-qnn-algorithmic-advantage]] - Algorithmic advantage of photonic QNNs
- [[pulse-level-quantum-computing]] - Pulse-level quantum computing design and optimization
- [[pulse-level-quantum-fourier-models]] - Pulse-level QFMs for quantum machine learning
- [[pulse-level-qfm]] - Pulse-level Quantum Fourier Models
- [[qfi-stabilizer-framework]] - Quantum Fisher Information framework for stabilizer codes
- [[learnable-observable-qnn]] - Learnable Observable QNN methodology
- [[quantum-cayley-llm-adapters]] - Quantum-enhanced LLM via Cayley-parameterized adapters
- [[gated-qkan-fwp]] - Quantum-inspired sequence learning with Gated QKAN-FWP
- [[quantum-bayesian-state-estimation]] - Quantum Bayesian state estimation and transport dynamics
- [[quantum-circuit-drug-dynamics]] - Quantum circuit simulation of compartmental drug dynamics
- [[quantum-pkpd-simulation]] - Quantum PK/PD simulation for pharmacokinetics
- [[quantum-medical-feature-fusion]] - Adaptive hybrid quantum-classical medical image fusion
- [[quantum-medical-research]] - Quantum computing in medical research
- [[quantum-healthcare-research]] - Quantum healthcare research methodology
- [[quantum-healthcare-patterns]] - Reusable quantum healthcare research patterns
- [[quantum-kernel-medical-embeddings]] - Quantum kernel methods for medical AI embeddings
- [[medical-ai-diagnosis]] - AI medical diagnosis system patterns
- [[medical-domain-adaptation]] - Medical image domain adaptation and transfer learning
- [[tt-opd-medical-agent-training]] - Turn-level truncated OPD for medical agent training
- [[multi-agent-clinical-reasoning]] - Multi-agent clinical reasoning and radiology
- [[pan-fm-pan-organ-foundation]] - Pan-Organ Foundation Model for multimodal biomedical AI
- [[concept-reasoning-continual-learning]] - Concept-Reasoning Expansion for continual learning
- [[moe-optimal-transport-routing]] - MoE routing using optimal transport
- [[distributed-quantum-error-correction]] - Distributed QEC design and analysis
- [[distributed-iqft-communication]] - Communication-efficient distributed IQFT
- [[modular-quantum-shor-compilation]] - Distributed Shor's algorithm compilation on modular atoms
- [[qbalance-quantum-workflow-optimization]] - Multi-objective quantum workflow optimization for NISQ
- [[quantum-data-centers-entanglement]] - Quantum data center network design and entanglement distribution
- [[quantum-network-task-control]] - Centralized task-based quantum network control
- [[quantum-cv-learning-theory]] - Quantum learning theory for CV systems
- [[nuclear-lattice-vqe]] - VQE for nuclear lattice models
- [[fluxonium-scalable-architecture]] - Scalable fluxonium quantum processor architecture
- [[quantum-control-engineering]] - Engineering patterns for reliable quantum control
- [[dependable-quantum-systems]] - Dependability engineering for hybrid quantum-classical computing
- [[noise-enhanced-quantum-kernels]] - Noise-enhanced quantum kernels for analog quantum ML
- [[organic-quantum-reservoir-computing]] - Magnetic-field-free quantum reservoir computing
- [[compositional-quantum-heuristics]] - Compositional quantum heuristics for barren plateau mitigation
- [[mathematical-quantization]] - Kohn-Nirenberg and Lie group quantization
- [[quantum-geometric-statistical-analysis]] - Quantum probability + Fisher geometry + tensor networks
- [[quantum-geometry-topology-research]] - Quantum-geometry-topology interdisciplinary research
- [[cross-layer-crypto-analysis]] - Cross-layer cryptographic security analysis
- [[post-quantum-cryptographic-protocol-analysis]] - Post-quantum cryptographic protocol analysis
- [[ramanujan-hypergraph-quantum-routing]] - Ramanujan hypergraph block permutation routing
- [[magic-number-theoretic-complexity]] - Magic state complexity analysis
- [[hybrid-quantum-classical-architecture]] - Hybrid quantum-classical architecture design
- [[hybrid-quantum-classical-framework]] - Dataflow-based hybrid quantum-classical computing
- [[hybrid-quantum-classical-system-design]] - Hybrid quantum-classical system design patterns
- [[hybrid-quantum-classical-systems]] - Hybrid quantum-classical systems engineering
- [[mqt-quantum-classical-compiler]] - MQT Compiler Collection for future-proof quantum-classical compilation
- [[hardware-motivated-noise-modeling]] - Hardware-motivated noise modeling for fault tolerance
- [[affine-subcode-ensemble-decoding]] - Affine subcode ensemble decoding for degenerate QEC
- [[adaptive-acquisition-bbo]] - Adaptive acquisition function for black-box optimization
- [[core-cross-site-ood-brain-network]] - CORE framework for cross-site OOD brain network robustness
- [[eeg-preprocessing-reliability]] - EEG preprocessing reliability assessment methodology
- [[uncertainty-guided-hypergraph-refinement]] - Uncertainty-Guided Hypergraph Refinement
- [[flux-longitudinal-flow-matching]] - Geometry-aware longitudinal flow matching for biological data
- [[agentic-fusion-materials]] - Agentic AI framework for materials discovery
- [[digital-twin-multi-agent-consensus]] - Digital twin-based consensus for multi-agent CPS
- [[heterogeneous-contract-control]] - Heterogeneous assume-guarantee contracts for CPS
- [[graph-pooling-node-features]] - Graph pooling with node feature interaction analysis
- [[multi-scale-info-geometry-neural]] - Multi-scale information geometry for neural population codes
- [[agent-integration-testing]] - Agent integration testing patterns
- [[agentic-fast-slow-planning]] - Bridging large-model reasoning with real-time control
- [[ai-power-profiling]] - GPU power consumption profiling for generative AI
- [[ai-workload-power-profiling]] - AI workload power profiling for data centers
- [[bayesian-agent-orchestration]] - Bayes-consistent multi-agent orchestration
- [[bian-que-agentic-operations]] - Agentic framework for online system operations
- [[constraint-guided-execution]] - Constraint-guided execution for natural language interpretation
- [[coral-open-ended-discovery]] - Autonomous multi-agent open-ended discovery
- [[data-driven-distributed-control]] - Data-driven distributed controller synthesis
- [[distributionally-robust-control]] - Distributionally robust control system design
- [[dsm-llm-modularization]] - LLM-based Design Structure Matrix modularization
- [[gaussian-grpo]] - Gaussian Group Relative Policy Optimization
- [[hierarchical-moe-detection]] - Hierarchical MoE for object detection
- [[llm-sysml-alignment]] - LLM-assisted semantic alignment for SysML v2
- [[local-rl-alignment-engineering]] - Local base model RL alignment (RLHF/DPO/GRPO)
- [[ml-hybrid-distributed-caching]] - ML-hybrid distributed caching
- [[mpc-drl-autonomous-driving]] - MPC-RL integration for autonomous driving
- [[ontology-driven-cps-dataspace]] - Ontology-driven CPS dataspace
- [[plant-model-mismatch-mpc]] - MPC under plant-model mismatch
- [[psi-shared-state-architecture-v2]] - PSI shared-state architecture v2
- [[recode-agent-workflow]] - ReCode agent workflow
- [[shared-state-architecture]] - PSI persistent shared interface
- [[speculative-decoding-optimization]] - Speculative decoding with KV cache optimization
- [[stability-goal-obfuscation]] - Stability-goal obfuscation for autonomous systems
- [[quantum-tug-of-war-decision]] - Quantum Tug-of-War decision making model
- [[quantum-transport-clustering]] - Qlustering: unsupervised clustering via steady-state quantum transport
- [[qlustering-quantum-clustering]] - Unsupervised clustering via quantum transport in GKSL networks
- [[universally-robust-quantum-control]] - Universal noise-agnostic quantum control framework
- [[antic-mics-wcet-analysis]] - Mixed-Criticality WCET analysis
- [[datacenter-ai-workload-power-planning]] - Data center AI workload power planning
- [[discounted-mpc-plant-model-mismatch]] - Discounted MPC under plant-model mismatch
- [[distributed-system-resiliency]] - Distributed system resiliency patterns
- [[dockerize-node-pnpm-monorepo]] - Dockerize Node.js pnpm monorepos
- [[claude-code-token-optimization]] - Token optimization for CLI coding agents
- [[quantum-pet-biomarkers]] - Quantum entanglement degree as PET biomarkers for hypoxia
- [[neuromorphic-spintracker-asl]] - Neuromorphic visual attention for sign language on SpiNNaker

### Collection Statistics
- **Total ai_collection skills**: 1186 (Hermes) / 2306 (Project)
- **Coverage Rate**: 100% of 42 May 2026 neuroscience papers
- **Standalone Skills Synced**: 198 skills synced to ai_collection project
- **Collection Status**: Extreme maturity — all major neuroscience, quantum, and medical domains covered

## 2026-05-13 - Neuroscience Research (Cron Job)

### Spatiotemporal TDANN for MT Direction Maps
- [[mt-direction-maps-spatiotemporal]] - 3D ResNet with MoCo self-supervised learning + spatial loss produces brain-like direction-selective maps and pinwheel structures matching macaque MT physiology (arXiv: 2605.11718)
  - Extends TDANN to dorsal stream: 3D ResNet trained on naturalistic videos via contrastive learning
  - MT tuning emerges from strict trade-off between discriminative pressure and spatial regularization
  - Quantitative match to in vivo macaque MT: direction selectivity index, circular variance, pinwheel density
  - Unifies ventral and dorsal stream topographic origins under single computational mechanism
  - **Activation**: MT direction maps, spatiotemporal TDANN, dorsal stream self-organization, motion direction selectivity, cortical topography, MoCo visual neuroscience

### Attractor Models for Language and Reasoning
- [[attractor-models-language-reasoning]] - Fixed-point attractor architecture with implicit differentiation for scalable iterative refinement; 770M outperforms 1.3B Transformer on 2× tokens, 27M achieves 91.4% Sudoku-Extreme (arXiv: 2605.12466)
  - Two-stage: backbone proposes embeddings, attractor refines via fixed-point solving
  - Constant memory for effective depth; iterations chosen adaptively by convergence
  - Equilibrium internalization: fixed-point training enables solver removal at inference
  - Outperforms Claude and GPT-o3 on challenging reasoning tasks with tiny model
  - **Activation**: attractor models, fixed-point reasoning, implicit differentiation, looped Transformer, iterative refinement, equilibrium internalization

### EEG Microstate Discovery via Variational Deep Embedding
- [[eeg-microstate-variational-embedding]] - Variational deep embedding replaces k-means microstate clustering with uncertainty-aware latent space learning for interpretable EEG analysis (arXiv: 2605.10947)
  - Deep VAE learns continuous temporal representation of EEG segments
  - Systematic architecture search identifies optimal configuration
  - Multi-quadrant evaluation: interpretability, stability, accuracy, scalability
  - Principled uncertainty quantification via variational posterior
  - **Activation**: EEG microstate discovery, variational EEG embedding, microstate clustering, interpretable EEG analysis, deep EEG pipeline

## 2026-05-13 - 医学 + 量子力学 (Cron Job - 周三医学主题)

### Hybrid Quantum Neural Networks for Enhanced Breast Cancer Thermographic Classification
- [[hybrid-quantum-medical-imaging]] - Integrates quantum variational circuits with classical CNN backbones for thermographic breast cancer classification, leveraging quantum advantage in complex thermal pattern discrimination (arXiv: 2604.16953)
  - Hybrid architecture: Classical CNN encoder → Quantum variational layer → Classical classifier
  - Amplitude encoding of CNN features into quantum states for enhanced discrimination
  - Quanvolutional filters as alternatives to convolutional layers for medical image patches
  - Joint classical-quantum optimization using parameter-shift rule for gradient computation
  - **Activation**: hybrid quantum neural network, quantum medical imaging, thermographic cancer detection, quanvolutional network, quantum healthcare AI, breast cancer quantum classification

## 2026-05-14 - 医学 + 量子力学 (Cron Job - 周三医学主题)

### FQPDR: Federated Quantum Neural Network for Privacy-preserving Early Detection of Diabetic Retinopathy
- [[fqpdr-quantum-medical-diagnosis]] - Federated Quantum Neural Network for distributed medical diagnosis across hospitals without sharing patient data; trains local QNNs and aggregates via FedAvg (arXiv: 2605.08324)
  - Multi-hospital federated QNN architecture with parameterized quantum circuits
  - Classical medical features encoded into quantum states via angle embedding
  - Privacy-preserving: patient data never leaves originating institution
  - Applicable to rare disease detection requiring pooled sparse data
  - **Activation**: federated quantum, quantum medical diagnosis, FQN, privacy-preserving medical AI, diabetic retinopathy quantum, distributed quantum healthcare

## 2026-05-14 - Quantum Computing Research (Cron Job)

### Pre-Asymptotic Trainability in Photonic Variational Circuits under Postselection
- [[photonic-variational-trainability]] - Challenges barren plateau assumption in passive photonic circuits; postselection prevents strong mixing dynamics that cause gradient vanishing (arXiv: 2605.11879)
  - Linear optical quantum computing shows trainability despite deep circuits
  - Postselection maintains gradient variance at usable levels
  - Implications for photonic VQA optimization and NISQ-era training

## 2026-05-13 - 医学 + 量子力学 (Cron Job - 周三医学主题)

### Quantum Entanglement Degree as Novel PET Biomarkers for Hypoxia
- [[quantum-pet-biomarkers]] - Novel quantum sensing method using positronium photon entanglement degree, lifetime, and annihilation ratios to non-invasively assess tissue oxygen concentration (arXiv: 2605.00021)
  - Two approaches: (1) dual-parameter τ_oPs + R_oPs-3γ/2γ measurement, (2) entanglement degree sensitivity to pick-off vs self-annihilation
  - Derived formula linking pO₂ to quantum entanglement metrics
  - Quantitative C_QE predictions across tissue types (adipose: 0.890, water: 0.867)
  - **Activation**: quantum PET biomarkers, positronium hypoxia sensing, quantum entanglement PET, positronium lifetime oxygen, pick-off conversion annihilation

### Quantum Circuit Simulation of Compartmental Drug Dynamics: Leveraging Variational Algorithms for Nonlinear Mixed-Effects Population Pharmacokinetics
- [[quantum-pkpd-simulation]] - Reformulates compartmental PK/PD models as open quantum systems using PennyLane quantum circuits for population pharmacokinetics parameter estimation (arXiv: 2605.09691)
  - Classical ODE-based PK/PD models encoded as quantum circuit evolution
  - Variational quantum algorithms for nonlinear mixed-effects population model fitting
  - Potential exponential speedup for multi-compartment drug dynamics simulation
  - Population-level predictions via quantum expectation values
  - **Activation**: quantum PK/PD, quantum pharmacokinetics, drug dynamics simulation, compartmental quantum model, quantum circuit drug simulation, variational quantum healthcare

### Medical Imaging Classification with Cold-Atom Reservoir Computing using Auto-Encoders and Surrogate-Driven Training
- [[cold-atom-medical-imaging]] - Hybrid quantum-classical pipeline with neutral-atom reservoir computing for medical image classification (polyp detection) using guided auto-encoder for dimensionality reduction (arXiv: 2605)
  - Guided auto-encoder compresses medical images while preserving clinically relevant features
  - Cold neutral-atom reservoir provides rich nonlinear dynamics for classification
  - Surrogate-driven training avoids repeated expensive quantum experiments
  - NISQ-compatible — works with noisy physical reservoirs
  - **Activation**: cold-atom reservoir computing, neutral-atom medical imaging, quantum reservoir medical classification, auto-encoder reservoir, surrogate-driven training, quantum-classical medical pipeline

## 2026-05-13 - Neuroscience Research (Cron Job)

### Letting the neural code speak: Automated characterization of monkey visual neurons through human language
- [[neural-code-language-characterization]] - Closed-loop framework using natural language to characterize neural selectivity at scale; LLM-generated semantic hypotheses verified in silico on digital twins of macaque V1/V4 (arXiv: 2605.12485)
  - Natural language descriptions capture neural selectivity from V1 (oriented edges, spatial frequency) to V4 (form, color, texture conjunctions)
  - LLM-generated activating/suppressing hypotheses drive 96.1% of V4 neurons above 95th percentile of natural-image responses
  - Representational similarity analysis: vision most aligned to neural activity; linguistic compression lossy yet semantically faithful
  - **Activation**: neural code characterization, language-based neural description, digital twin neuroscience, interpretable neural selectivity, agentic neural discovery, V1 V4 semantic description

### Joint sparse coding and temporal dynamics support context reconfiguration
- [[context-reconfiguration-sparse-temporal]] - Identifies sparse coding + temporal dynamics in mouse mPFC as core mechanism for preserving prior knowledge during context transitions; SNNs naturally exhibit both properties for lifelong learning (arXiv: 2605.10178)
  - Sparse context-dependent representations reduce cross-context interference
  - Temporal dynamics enhance context separability across time
  - Networks with both properties (e.g., SNNs) show improved retention without auxiliary heuristics
  - **Activation**: context reconfiguration, sparse coding temporal dynamics, catastrophic forgetting, lifelong learning SNN, mPFC context switching, neural representation stability

## 2026-05-13 - Neuroscience Research (Cron Job)

### Encoding and Decoding Temporal Signals with Spiking Bandpass Wavelets
- [[spiking-bandpass-wavelet-encoding]] - Recasts spike encoders as time-causal wavelet frames with quantitative bandwidths and reconstruction error bounds; achieves NRMSE comparable to continuous wavelet transforms on ECG and audio (arXiv: 2605.09770)
  - Spike-based encoding reformulated as wavelet frame decomposition
  - Quantitative bandwidth analysis and reconstruction error bounds for spiking representations
  - Direct mapping to neuromorphic hardware (Loihi, SpiNNaker)
  - **Activation**: spiking bandpass wavelet, spike-based signal encoding, neuromorphic signal processing, temporal signal encoding, wavelet spike encoding, time-causal wavelet frames

### Cortico-cerebellar modularity as architectural inductive bias for efficient temporal learning
- [[cortico-cerebellar-modularity-rnn]] - Augments RNN with cerebellar-inspired feedforward module (CB-RNN), enabling faster convergence on temporal tasks via bidirectional cortico-cerebellar coupling (arXiv: 2605.10356)
  - Cortical module (RNN) for rich temporal dynamics + cerebellar module (feedforward) for fast predictive correction
  - Bidirectional coupling between slow recurrent and fast feedforward pathways
  - Improved learning efficiency and temporal precision across tasks
  - **Activation**: cortico-cerebellar RNN, cerebellar neural architecture, temporal sequence learning, brain-inspired RNN, modular neural architecture

## 2026-05-13 - Neuroscience Research (Cron Job - Batch 3)

### Multi-Timescale Conductance Spiking Networks: A Sparse, Gradient-Trainable Framework with Rich Firing Dynamics for Enhanced Temporal Processing
- [[multi-timescale-conductance-snn]] - SNN framework using fast/slow/ultra-slow conductances to shape I-V curve, enabling direct BPTT (no surrogate gradients) with rich firing regimes and high sparsity (arXiv: 2605.11835)
  - Multi-timescale conductance parametrization replaces phenomenological LIF dynamics
  - Direct backpropagation through time without surrogate gradient approximation
  - Single model exhibits tonic, phasic, and bursting firing regimes
  - Outperforms LIF and AdLIF on Mackey-Glass regression with substantially sparser activity
  - **Activation**: multi-timescale spiking, conductance SNN, gradient-trainable SNN, I-V curve shaping, temporal processing SNN, direct BPTT SNN

### Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching
- [[autoregressive-flow-matching-neural-dynamics]] - Generative forecasting framework using autoregressive flow matching for probabilistic neural dynamics prediction from multimodal sensory input and past neural history (arXiv: 2604.11178)
  - Flow matching learns conditional distribution of future neural states given past dynamics
  - Autoregressive factorization captures temporal dependencies between predictions
  - Past neural history is the dominant predictor — more than sensory input alone
  - Significantly outperforms GLM and non-autoregressive baselines on fMRI data
  - **Activation**: neural dynamics prediction, autoregressive flow matching, fMRI forecasting, probabilistic neural prediction, closed-loop neurotechnology, transport-based generative modeling

     1|## 2026-05-13 - Quantum Metrology Research (Cron Job)
     2|
     3|### Optimal FALQON for Quantum Approximate Optimization via Layer-wise Parameter Tuning
     4|- [[optimal-falqon-qaoa]] - Treats per-layer time step (δ_k) and scaling factor (M_k) as classical optimization variables, reducing circuit depth vs standard FALQON, outperforms QAOA on all 94 3-regular graphs (12 vertices) (arXiv: 2605.08332)
     5|  - Single circuit evaluation per layer maintained, NISQ-compatible
     6|