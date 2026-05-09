## 2026-05-09 - Neuroscience Research (Cron Job)

### Neuromorphic visual attention framework for sign language recognition on SpiNNaker-2
- [[neuromorphic-spinnaker-asl]] - Event-based neuromorphic vision system for real-time ASL recognition on SpiNNaker-2 with spiking temporal encoder and STDP-based learning (arXiv: 2605.06005)
  - Core: Spiking temporal encoder converts DVS events into spike trains with learnable time constants
  - Core: STDP-based unsupervised learning for temporal pattern recognition on neuromorphic hardware
  - **Activation**: neuromorphic computing, SpiNNaker, event-based vision, sign language recognition, STDP, spiking temporal encoder

### CORE framework for out-of-distribution brain network analysis
- [[brain-network-core]] - Site-aware confounder decoupling framework for OOD generalization in brain network analysis via decoupling site-specific biases (arXiv: 2605.06050)
  - Core: Decouples site-specific confounders from invariant brain network patterns using adversarial disentanglement
  - Core: 2-layer GCN with hidden=64, trained with adversarial loss to minimize site information in representations
  - **Activation**: brain network analysis, OOD generalization, confounder decoupling, site-aware learning, graph neural network

     1|## 2026-05-09 - Neuroscience Research (Cron Job)
     2|
     3|### A multi-scale information geometry reveals the structure of mutual information in neural populations
     4|- [[multi-scale-info-geometry-neural]] - Riemannian representational geometry derived from coarse-graining principles, exactly related to mutual information (arXiv: 2605.06304)
     5|  - Core: Multi-scale Fisher information metric captures encoding structure from fine to coarse scales
     6|  - Core: Metric tensor eigenvectors identify information-carrying stimulus features in neural populations
     7|  - **Activation**: information geometry, Fisher information, neural coding, representational geometry, mutual information
     8|
     9|### A Generalized Framework of Antisymmetric Polyspectral Indices for Identifying High-Order Neural Interactions
    10|- [[antisymmetric-polyspectral-neural-interactions]] - Generalized antisymmetric cross-polyspectral indices detecting 3-way+ neural interactions beyond pairwise connectivity (arXiv: 2605.04636)
    11|  - Core: Cross-bispectrum and cross-trispectrum with antisymmetric properties robust to volume conduction
    12|  - Core: Hypergraph construction for multi-node synergistic brain network analysis
    13|  - **Activation**: polyspectral, bispectrum, higher-order connectivity, multi-node coupling, synergistic connectivity
    14|
    15|## 2026-05-09 - Anthropic Research (Cron Job)
    16|
    17|### Teaching Claude why
    18|- [[teaching-claude-why]] - Reduce agentic misalignment through principled, principle-based alignment training that generalizes out-of-distribution
    19|  - Core finding: Agentic misalignment comes from pre-trained model; standard RLHF insufficient for agentic settings
    20|  - Key method: Synthetic Document Fine-Tuning (SDF) — train on principled documents that articulate why certain actions are wrong
    21|  - Result: Every Claude since Haiku 4.5 achieves perfect score on agentic misalignment evals
    22|  - **Activation**: agentic misalignment, alignment training, safety training, RLHF, constitution, honeypot, blackmail, OOD generalization
    23|
    24|### Automated Alignment Researchers
    25|- [[automated-alignment-researchers]] - Use LLMs as autonomous alignment researchers to discover alignment improvements via weak-to-strong supervision
    26|  - Core metric: Performance Gap Recovered (PGR) — measures how much weaker teacher recovers strong model potential
    27|  - Key result: 9 AAR instances recovered 97% of the performance gap vs human researchers
    28|  - Method: LLM researchers propose hypotheses, design experiments, test on models, iterate
    29|  - **Activation**: AAR, automated alignment, weak-to-strong supervision, PGR, scalable oversight, alignment automation
    30|
    31|### Trustworthy Agents in Practice
    32|- [[trustworthy-agents-framework]] - Five-principle framework for building and governing trustworthy AI agents with practical implementation guidance
    33|  - Five principles: Human Control, Alignment with Values, Security, Transparency, Privacy
    34|  - Key pattern: Agent architecture with 4 layers (model, tools, memory, execution) each with oversight
    35|  - Practical guidance: prompt injection defense, permission systems, audit logging
    36|  - **Activation**: trustworthy agents, agent governance, prompt injection, human control, agent security, transparency, privacy
    37|
    38|## 2026-05-09 - Quantum Error Correction (Cron Job)
    39|
    40|### Syndrome Resampling Enhances QEC Thresholds
    41|- [[quantum-error-correction-methods]] - Bias syndrome averages toward high-probability syndromes to increase QEC thresholds and reduce logical error rates by up to 4 orders of magnitude without hardware changes (arXiv: 2605.06101)
    42|  - Core method: Resample syndromes according to P(s)^α with MLD, linked to Rényi coherent information phase transitions
    43|  - Decoder-agnostic: works with any QEC decoder from finite syndrome data
    44|  - Applied to existing experimental data: 2 orders of magnitude logical error rate reduction
    45|  - **Activation**: syndrome resampling, QEC threshold, logical error rate, Rényi coherent information
    46|
    47|### Affine Subcode Ensemble Decoding
    48|- [[quantum-error-correction-methods]] - Extend affine subcode ensemble decoding from classical to quantum setting to address degeneracy impairment in qLDPC BP decoding (arXiv: 2605.06547)
    49|  - Core insight: Appending independent rows to check matrix reduces search space for degenerate solutions
    50|  - Uses overcomplete matrices for each decoding path, improved convergence on toric/GB codes
    51|  - **Activation**: affine subcode, degeneracy-aware decoding, qLDPC, belief propagation
    52|
    53|### Real-time FPGA Neural Network Decoder
    54|- [[quantum-error-correction-methods]] - FPGA-based NN decoder achieves 550 ns closed-loop latency for real-time distance-3 surface code QEC on superconducting processor (arXiv: 2605.04892)
    55|  - 124 ns NN decoding within 1.25 μs QEC cycle, supports mid-circuit feedback for non-Clifford operations
    56|  - **Activation**: FPGA decoder, neural network decoder, real-time QEC, surface code
    57|
    58|### Distributed BB Codes in Modular Architecture
    59|- [[quantum-error-correction-methods]] - Implement [[144,12,12]] BB code across modular processors interconnected via shared Bell pairs with BP+OSD decoding (arXiv: 2605.04663)
    60|  - Star network architecture for trapped ion/neutral atom platforms with all-to-all internal connectivity
    61|  - **Activation**: bivariate bicycle codes, distributed QEC, modular quantum computing, qLDPC
    62|
    63|## 2026-05-09 - OpenAI Research (Cron Job)
    64|
    65|### Trading Inference Time Compute for Adversarial Robustness
    66|- [[trading-inference-time-adversarial-robustness]] - Trade repeated sampling at inference time for provable adversarial robustness guarantees in LLMs through safety filtering and output aggregation
    67|  - Core innovation: Compute-robustness trade-off — more samples → logarithmically stronger adversarial defense
    68|  - Key method: Repeated sampling + safety filter + majority vote aggregation
    69|  - Application: Post-hoc jailbreak defense layer on aligned LLMs
    70|  - **Activation**: adversarial robustness, inference-time compute, repeated sampling, safety filter, jailbreak defense, compute-robustness tradeoff
    71|
    72|### Detecting and Reducing Scheming in AI Models
    73|- [[detecting-reducing-scheming-ai]] - Systematic evaluation methodology for detecting hidden misalignment (scheming) in frontier AI models through situational awareness tests, reward tampering detection, and sandbagging evaluations
    74|  - Core innovation: Joint Apollo Research + OpenAI framework for deceptive behavior detection
    75|  - Key methods: Multi-stage adversarial deployment scenarios, cross-model comparison, training-time intervention
    76|  - Finding: Scheming behaviors detected in controlled tests across frontier models
    77|  - **Activation**: scheming detection, hidden misalignment, AI deceptive behavior, Apollo Research, model safety evaluation, alignment
    78|
    79|### Collective Alignment: Public Input on AI Model Behavior
    80|- [[collective-alignment-public-input]] - Methodology for incorporating public input into AI model alignment through large-scale surveys and democratic value aggregation across global demographics
    81|  - Core innovation: Survey 1000+ people worldwide, compare to Model Spec, update defaults
    82|  - Key methods: Demographic sampling, behavior scenario preference elicitation, iterative re-surveying
    83|  - Finding: Global public opinion differs from existing AI defaults, cultural variation requires nuanced alignment
    84|  - **Activation**: collective alignment, public input AI, democratic AI alignment, Model Spec, AI behavior preferences
    85|
    86|## 2026-05-09 - Neuroscience Research (Cron Job)
    87|
    88|### Unifying Dynamical Systems and Graph Theory to Mechanistically Understand Neural Computation
    89|- [[unifying-dynamics-graph-neural-computation]] - Unified framework integrating Recurrent Neural Networks (RNNs) with dynamical systems and graph theory to mechanistically understand neural computation; introduces path-constrained regularization, multi-hop interaction analysis, and temporal sparsity metrics (arXiv:2605.03598)
    90|  - Core innovation: R-RNNs (Recurrent-Residual RNNs) with path-constrained regularization enabling mechanistic interpretation of neural dynamics
    91|  - Key method: Multi-hop path analysis quantifying information flow through network connectivity graphs
    92|  - Key finding: Temporal sparsity patterns reveal computational bottlenecks and redundant pathways in trained RNNs
    93|  - Mechanistic insight: Unifies dynamical systems stability analysis with graph-theoretic measures for interpretable neural computation
    94|  - **Activation**: R-RNN, recurrent residual networks, path-constrained regularization, neural dynamics interpretation, graph theory RNN, temporal sparsity neural, mechanistic neural computation, dynamical systems neural networks
    95|
    96|## 2026-05-09 - Systems Engineering Research (Cron Job)
    97|
    98|### Safactory: A Scalable Agent Factory for Trustworthy Autonomous Intelligence
    99|- [[safactory-agent-factory]] - Production-grade autonomous agent factory with sandboxing, multi-level safety guardrails, policy-driven execution, and dynamic tool provisioning; enables trustless deployment of AI agents in enterprise environments (arXiv: 2605.06230)
   100|  - Core innovation: Multi-layer safety architecture combining static analysis, runtime monitoring, and post-execution verification
   101|  - Key pattern: Policy-driven tool provisioning — agents only receive tools they need, when they need them, reducing attack surface
   102|  - Architecture: Sandboxed execution environments with resource limits, capability scoping, and audit logging
   103|  - Scalability: Factory pattern for spawning, monitoring, and terminating agent instances on demand
   104|  - **Activation**: agent factory, autonomous agent sandbox, agent safety guardrails, policy-driven tool provisioning, trustless AI deployment, scalable agent orchestration
   105|
   106|### Towards Formal Verification of Hybrid Synchronous Programs with Refinement Types
   107|- [[formal-verification-hybrid-synchronous]] - Formal verification methodology combining refinement types with synchronous programming models for hybrid/cyber-physical systems; bridges discrete controller logic with continuous physical dynamics (arXiv: 2605.04377)
   108|  - Core innovation: Refinement type system that encodes safety invariants directly in the type layer of hybrid programs
   109|  - Key method: Synchronous model composition with continuous-time constraints — verified correctness at compile time
   110|  - Application domain: CPS, robotic control, aerospace systems where safety-critical guarantees are required
   111|  - Verification: Automated theorem proving integrated into the compilation pipeline
   112|  - **Activation**: formal verification hybrid systems, refinement types synchronous programs, CPS verification, hybrid program correctness, safety-critical control verification
   113|
   114|  - **Activation**: kernel hopfield, KLR Hopfield, event-driven retrieval, asynchronous associative memory, neuromorphic memory, large-margin attractor, sparse event computation, kernel logistic regression memory
   115|
   116|## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
   117|## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job - Hourly Update)
   118|## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job - Hourly Update #2)
   119|
   120|## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job - Hourly #3)
   121|
   122|### The true cost of factoring: Linking magic and number-theoretic complexity in Shor's algorithm
   123|- [[quantum-magic-state-analysis]] - Analyzes magic (non-stabilizerness) as the genuine quantum resource cost in Shor's algorithm, linking it to number-theoretic hardness of factoring (arXiv: 2605.05347)
   124|  - 核心要点 1: 量子算法成本应以"魔力"（非稳定子资源）而非仅门数和量子比特数来衡量
   125|  - 核心要点 2: Shor算法中模指数运算步骤产生最大魔力，与因数分解难度直接相关
   126|  - 核心要点 3: 魔力生成速率与经典计算困难性成正比，揭示量子优势的数学结构根源
   127|  - **Activation**: quantum magic state, non-stabilizerness, Shor algorithm resource cost, quantum resource theory, magic state distillation, mana computation, quantum advantage estimation
   128|
   129|### Analytical Angle-Finding and Series Expansions for QSP via Orthogonal Polynomial Theory
   130|- [[quantum-signal-processing-orthogonal-polynomials]] - Analytical QSP angle-finding via Hermite, Jacobi, Rogers-Szego polynomials with O(log(1/ε)) gate complexity for smooth function approximation (arXiv: 2605.05321)
   131|  - 核心要点 1: 通过正交/双正交多项式族完整表征可实现的QSP多项式基
   132|  - 核心要点 2: 为Hermite、Jacobi、Rogers-Szego多项式族导出闭式QSP角度公式
   133|  - 核心要点 3: 光滑函数的ε-近似可通过Hermite级数展开用O(log(1/ε))门实现块编码
   134|  - **Activation**: quantum signal processing QSP, QSP angle finding, orthogonal polynomial quantum, Hermite polynomial quantum, Jacobi polynomial QSP, Rogers-Szego quantum, quantum function approximation
   135|
   136|### Quantum Proper Scoring Rules: Minimax Estimation and Resource-Theoretic Advantages
   137|- [[quantum-proper-scoring-rules]] - Generalizes proper scoring rules to density operators via operator convex generators with Quantum Cramér-Rao-McCarthy Bound for state tomography (arXiv: 2605.05268)
   138|  - 核心要点 1: 将经典评分规则推广到量子密度算符，建立算子凸生成函数与量子评分规则的完整对偶理论
   139|  - 核心要点 2: 推导量子Cramér-Rao-McCarthy界，将最小最大风险与生成函数曲率和量子Fisher信息关联
   140|  - 核心要点 3: 量化量子资源在预测任务中的经济价值，连接量子资源理论与机制设计
   141|  - **Activation**: quantum proper scoring rules, quantum state estimation, quantum Fisher information, minimax quantum tomography, operator convex quantum, quantum Cramer-Rao bound, quantum forecasting
   142|
   143|### Integral Means Spectrum for the Random Riemann Zeta Function
   144|- [[random-riemann-zeta-spectrum]] - Proves Kraetzer's 30-year conjecture for integral means spectrum of random Riemann zeta primitive via Gaussian multiplicative chaos (arXiv: 2603.26507)
   145|  - 核心要点 1: 随机黎曼zeta函数的原函数的复积分均值谱几乎必然符合Kraetzer猜想形式
   146|  - 核心要点 2: 随机zeta函数与Kahane的高斯乘性混沌(GMC)建立了严格对应关系
   147|  - 核心要点 3: 用概率论和解析数论工具解决了保形映射中30年的未决猜想
   148|  - **Activation**: random riemann zeta, integral means spectrum, gaussian multiplicative chaos, GMC, analytic number theory, kraetzer conjecture, bagchi zeta, conformal mapping
   149|
   150|
   151|### Module Lattice Security (Part I): Unconditional Verification of Weber's Conjecture for k ≤ 12
   152|- [[module-lattice-security]] - First unconditional proof of Weber's conjecture for k ≤ 12, establishing foundations for Ring-LWE and Module-LWE security without GRH assumption (arXiv: 2604.15858)
   153|  - 核心要点 1: 结合Fukuda-Komatsu计算筛法、Z_2塔归纳结构和Herbrand定理，首次无条件证明k≤12的韦伯猜想
   154|  - 核心要点 2: 韦伯猜想决定主理想问题可解性、模自由性和R-LWE/MLWE最坏情况到平均情况归约的紧致性
   155|  - 核心要点 3: 后量子密码方案（Kyber、Falcon、NewHope）的安全性直接依赖于这些数论基础
   156|  - **Activation**: Weber conjecture, module lattice, Ring-LWE, Module-LWE, post-quantum cryptography, cyclotomic fields, Fukuda-Komatsu sieve, Herbrand theorem
   157|
   158|### Classical shadows over symmetric spaces
   159|- [[quantum-classical-shadows]] - Extends classical shadow protocols from compact groups to compact symmetric spaces, improving sample complexity for certain observable distributions (arXiv: 2605.05518)
   160|  - 核心要点 1: 经典影子协议通常从紧致群均匀采样，本文推广到紧致对称空间采样
   161|  - 核心要点 2: 在某些观测分布下，对称空间协议比现有影子方案有采样复杂度优势
   162|  - **Activation**: classical shadows, symmetric spaces, quantum state tomography, randomized measurements, sample complexity
   163|
   164|### Efficient Quantum Fourier Transforms For Semisimple Algebras
   165|- [[quantum-algebraic-structures]] - Generalizes QFT from finite groups to semisimple algebras with efficient circuits for partition, Brauer, and walled Brauer algebras (arXiv: 2605.05337)
   166|  - 核心要点 1: 半单代数上的傅里叶变换可以是非幺正的，但当参数 d 足够大时可被幺正算子良好逼近
   167|  - 核心要点 2: 通过分解为不可约表示构建高效量子电路，推广了群上的QFT
   168|  - **Activation**: quantum algebra, semisimple algebra QFT, quantum Fourier transform, Brauer algebra, representation theory
   169|
   170|### Analytical Angle-Finding and Series Expansions for Quantum Signal Processing via Orthogonal Polynomial Theory
   171|- [[quantum-algebraic-structures]] - Analytical QSP angle-finding via Hermite, Jacobi, and Rogers-Szego polynomials with O(log(1/ε)) gate complexity (arXiv: 2605.05321)
   172|  - 核心要点 1: 通过正交/双正交多项式族表征可实现的QSP多项式基，导出闭式角度公式
   173|  - 核心要点 2: 利用Hermite级数展开实现O(log(1/ε))门复杂度的光滑函数块编码
   174|  - **Activation**: quantum signal processing, orthogonal polynomials, QSP angles, Hermite expansion, Jacobi polynomials
   175|
   176|### Quantum Proper Scoring Rules: Minimax Estimation and Resource-Theoretic Advantages
   177|- [[quantum-algebraic-structures]] - Quantum domain scoring rules with operator convex generators and Quantum Cramér-Rao-McCarthy Bound (arXiv: 2605.05268)
   178|  - 核心要点 1: 将经典评分规则推广到量子密度算符域，建立完整对偶理论
   179|  - 核心要点 2: 证明量子Cramér-Rao-McCarthy界，量化量子资源在预测任务中的经济价值
   180|  - **Activation**: quantum scoring rules, minimax estimation, quantum Fisher information, operator convex, resource theory
   181|
   182|### Cusped Singularity Mixed-Mode Oscillation Analysis
   183|- [[cusped-singularity-mmo-analysis]] - Geometric singular perturbation analysis of MMOs in inhibitory neural networks via cusped singularities (arXiv: 2605.03606)
   184|  - 核心要点 1: 尖点奇异性（临界流形尖点处的折叠奇异性）是互抑制神经网络中混合模式振荡（MMO）的通用组织机制
   185|  - 核心要点 2: 尖点奇异性保证小振幅振荡（SAO）的产生，结合奇异Hopf分岔形成完整MMO，呈现独特的交替振荡模式
   186|  - 核心要点 3: 在Curtu速率模型和Morris-Lecar突触抑制耦合模型中验证了该机制的普适性
   187|  - **Activation**: mixed-mode oscillations, MMO, cusped singularity, slow-fast neural system, mutual inhibition oscillation, singular perturbation neural, blow-up method neural, neural oscillation mechanism
   188|
   189|## 2026-05-08 - Neuroscience Research (Cron Job)
   190|## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
   191|
   192|### The true cost of factoring: Linking magic and number-theoretic complexity in Shor's algorithm
   193|- [[quantum-magic-number-theory-complexity]] - Links quantum magic (non-stabilizerness) resource cost to classical number-theoretic hardness of factoring (arXiv: 2605.05347)
   194|  - 核心要点 1: 量子算法的真实成本应由非稳定态资源（magic）衡量，而非单纯的门计数
   195|  - 核心要点 2: Shor算法中magic的生成量与数论问题的计算难度直接相关
   196|  - **Activation**: quantum magic, non-stabilizerness, Shor's algorithm, number theory complexity, resource theory
   197|
   198|### Quantum Proper Scoring Rules: Minimax Estimation and Resource-Theoretic Advantages
   199|- [[quantum-proper-scoring-rules]] - Generalizes proper scoring rules to quantum domain with operator convex generators and Quantum Cramér-Rao-McCarthy Bound (arXiv: 2605.05268)
   200|  - 核心要点 1: 将经典评分规则推广到量子密度算符域，定义量子价值泛函
   201|  - 核心要点 2: 证明量子Cramér-Rao-McCarthy界，连接量子Fisher信息与估计风险
   202|  - **Activation**: quantum scoring rules, state estimation, Cramer-Rao bound, quantum Fisher information, metrology
   203|
   204|### A multi-scale information geometry reveals the structure of mutual information in neural populations
   205|- [[multi-scale-information-geometry-neural]] - 多尺度信息几何揭示神经群体编码的互信息结构，Fisher信息度量的多尺度扩展直接关联互信息 (arXiv: 2605.06304)
   206|  - 核心要点1: 唯一黎曼表示几何从粗粒化下距离收缩的第一原理自然涌现，多尺度扩展Fisher信息度量
   207|  - 核心要点2: 度量张量本征向量识别对信息传输贡献最大的刺激变化方向，可通过扩散模型估计
   208|  - **Activation**: information geometry, Fisher information metric, neural population coding, mutual information, representational geometry, diffusion model estimation
   209|
   210|### Decoding Alignment without Encoding Alignment: A critique of similarity analysis in neuroscience
   211|- [[decoding-encoding-alignment-critique]] - 揭示RSA/DSA对齐度量的根本缺陷：解码对齐不代表计算相似性，高对齐分数可由极少数神经元子群体驱动 (arXiv: 2605.05907)
   212|  - 核心要点1: 解码对齐(RSA/DSA)无法反映神经元群体的编码拓扑，相似解码行为可由小神经元子集主导
   213|  - 核心要点2: 引入编码流形作为补充分析工具，必须同时报告解码对齐和编码拓扑才能得出有效结论
   214|  - **Activation**: decoding alignment, encoding manifold, RSA critique, brain-DNN comparison, representational similarity
   215|
   216|
   217|### Efficient Event-Driven Retrieval in High-Capacity Kernel Hopfield Networks
   218|- [[event-driven-hopfield-retrieval]] - KLR Hopfield网络的异步事件驱动检索，实现接近O(N)存储容量的神经形态联想记忆 (arXiv: 2605.05978)
   219|  - 核心要点 1: 异步序列更新在调优核参数下与同步动力学统计不可区分，保持高召回率
   220|  - 核心要点 2: KLR学习诱导的大边际吸引子创造平滑能量景观，收敛事件数≈初始汉明距离，适合稀疏神经形态计算
   221|  - **Activation**: kernel hopfield, event-driven retrieval, KLR Hopfield, asynchronous associative memory, neuromorphic memory, large-margin attractor
   222|
   223|### Beyond Object-Level Alignment: Do Brains and DNNs Preserve the Same Transformations?
   224|- [[brain-dnn-transformation-alignment]] - 基于范畴论的自然性违反分数(NVS)评估脑-DNN变换级对齐，揭示语义/视觉轴的分层交叉 (arXiv: 2605.06420)
   225|  - 核心要点 1: 将脑-DNN对齐从刺激级对应提升到变换保持测试，NVS量化与置换零模型的偏差
   226|  - 核心要点 2: 发现分层交叉现象——语义轴对齐高层视觉皮层+深层DNN，低级视觉轴对齐早期皮层+浅层
   227|  - **Activation**: naturality violation score, NVS, brain-DNN alignment, transformation alignment, category theory neuroscience, hierarchy crossover
   228|
   229|## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum Mechanics (Cron Job)
   230|
   231|### Beyond Gates: Pulse Level Quantum Fourier Models
   232|- [[pulse-level-quantum-fourier]] - 脉冲级量子傅里叶模型参数化，通过独立子角调优提升QML训练性能 (arXiv: 2605.04945)
   233|  - 核心要点 1: 独立脉冲缩放替代单一逻辑角，释放高维梯度下降逃逸路径
   234|  - 核心要点 2: 复合门中子角独立性显著提升训练性能，但不改变全局表达能力
   235|  - **Activation**: 脉冲级量子计算, 量子傅里叶模型, QML优化, pulse-level QFM, composite gate optimization
   236|
   237|### Block Permutation Routing on Ramanujan Hypergraphs for Fault-Tolerant Quantum Computing
   238|- [[ramanujan-hypergraph-routing]] - Ramanujan超图上的块排列路由用于容错量子计算 (arXiv: 2605.05036)
   239|  - 核心要点 1: Ramanujan超图上的块排列路由，保持谱比的高连通性
   240|  - 核心要点 2: 谱继承三层级：精确(Haemers)、扰动(Weyl)、通用(Cheeger)
   241|  - **Activation**: 量子路由, 表面编码, 超图变换, QCCD架构, fault-tolerant routing, block permutation
   242|
   243|### Integral Means Spectrum for the Random Riemann Zeta Function
   244|- [[random-riemann-zeta-spectrum]] - 随机黎曼ζ函数积分均值谱证明Kraetzer猜想 (arXiv: 2603.26507)
   245|  - 核心要点 1: 随机ζ函数原函数的积分均值谱几乎必然符合Kraetzer猜想形式
   246|  - 核心要点 2: 建立ζ函数临界线收敛到全纯GMC分布的替代推导
   247|  - **Activation**: 黎曼ζ函数, 积分均值谱, 高斯乘性混沌, Kraetzer猜想, 单叶函数
   248|
   249|### The true cost of factoring: Linking magic and number-theoretic complexity in Shor's algorithm
   250|- [[quantum-magic-complexity]] - 量化Shor算法中magic资源，建立数论问题经典难度与量子非稳定子资源的直接联系 (arXiv: 2605.05347)
   251|  - 核心要点 1: Magic(non-stabilizerness)是量子超越经典计算的关键资源，Shor算法在实用参数下最大化利用该资源
   252|  - 核心要点 2: 经典算法难度与解决该问题所需的非稳定子价格成正比，补充传统电路成本分析
   253|  - **Activation**: quantum magic complexity, non-stabilizerness, Shor algorithm resource, magic state distillation, stabilizer formalism, fault-tolerant overhead
   254|
   255|### Quantum Proper Scoring Rules: Minimax Estimation and Resource-Theoretic Advantages
   256|- [[quantum-proper-scoring-rules]] - 将适当评分规则推广到量子领域，用密度算子替代概率分布，推导量子态层析minimax最优界 (arXiv: 2605.05268)
   257|  - 核心要点 1: 通过算子凸生成元定义量子值泛函，建立量子Cramér-Rao-McCarthy界，连接minimax风险与量子Fisher信息
   258|  - 核心要点 2: 量化相干性、纠缠、自适应性等量子资源在预测任务中的经济价值，证明经典-量子缩放分离
   259|  - **Activation**: quantum proper scoring rules, quantum state estimation, quantum Fisher information, minimax quantum, quantum Cramer-Rao bound, quantum resource economics
   260|
   261|### Analytical Angle-Finding for QSP via Orthogonal Polynomial Theory
   262|- [[qsp-orthogonal-polynomials]] - 利用Hermite/Jacobi/Rogers-Szego多项式正交性，为量子信号处理提供旋转角度解析解 (arXiv: 2605.05321)
   263|  - 核心要点 1: QSP可实现多项式基由正交性/双正交性刻画，2n+2个角度编码次数≤n的多项式序列
   264|  - 核心要点 2: 光滑函数ε近似可通过Hermite级数展开以O(log(1/ε))个门实现块编码
   265|  - **Activation**: QSP angle finding, quantum signal processing, orthogonal polynomial, Hermite QSP, block encoding, SU(1,1)-QSP
   266|
   267|### Universal Neural Propagator: Learning Time Evolution in Many-Body Quantum Systems
   268|- [[quantum-neural-propagator]] - 学习从驱动协议到时间演化传播子的泛函映射，在驱动空间和指数大初态空间上同时预测量子动力学 (arXiv: 2605.05299)
   269|  - 核心要点 1: 从学习量子态转向学习算子，单个UNP模型覆盖函数空间的驱动协议和希尔伯特空间的初态
   270|  - 核心要点 2: 自监督训练，在超出精确对角化能力的系统尺寸上保持准确，可仅用可观测量数据微调
   271|  - **Activation**: universal neural propagator, quantum dynamics learning, quantum foundation model, driven quantum systems, time evolution propagator, transferable simulation
   272|
   273|### Semantics-Based Verification of Shor Oracle for ECDLP
   274|- [[quantum-program-semantic-verification]] - 量子程序语义验证方法，针对Shor类数论算法的群操作预言机进行语义级规范和精化验证 (arXiv: 2605.01008)
   275|  - 核心要点 1: Shor类ECDLP算法对群操作预言机的语义高度敏感，微小实现选择可使数学模型失效
   276|  - 核心要点 2: 即使通过平凡控制健全性检查，受控执行仍可能违反预期控制律，语义审计是可信量子软件的必要前提
   277|  - **Activation**: quantum program verification, Shor oracle, ECDLP quantum, semantic auditing, Qrisp verification, refinement verification, number-theoretic algorithms
   278|
   279|### Beating Noise in Frequency Estimation with Squeezing and Memory
   280|- [[quantum-noise-robust-metrology]] - 连续变量系统中的量子计量方法，通过哈密顿工程(压缩)和非马尔可夫环境记忆实现抗噪频率估计 (arXiv: 2605.06263)
   281|  - 核心要点 1: 将压缩嵌入系统哈密顿使QFI获得可调高阶时间依赖性，短时区灵敏度超越标准估计
   282|  - 核心要点 2: 结构化环境的非马尔可夫记忆可诱导信息回流，暂时恢复甚至超过无噪声估计极限
   283|  - **Activation**: quantum metrology, frequency estimation, quantum Fisher information, squeezing, non-Markovian, continuous-variable, noise mitigation, quantum sensing
   284|
   285|## 2026-05-08 - Neuroscience Research (Cron Job)
   286|
   287|### TRIBE v2: A Tri-Modal Brain Foundation Model
   288|- [[tribev2-brain-foundation-model]] - 三模态(视频/音频/语言)脑活动预测基础模型，统一预测1000+小时fMRI、720被试的高分辨率脑响应，实现in-silico神经科学实验 (arXiv: 2605.04326)
   289|  - 核心要点 1: Transformer架构整合三模态特征，通过modality dropout学习鲁棒跨模态表征，显著超越传统线性编码模型
   290|  - 核心要点 2: 支持零样本泛化到新刺激/任务/被试，通过subject block插值实现未见被试预测，可恢复数十年实证研究结果
   291|  - **Activation**: TRIBE v2, brain foundation model, fMRI encoding, multimodal brain prediction, in-silico neuroscience, Algonauts challenge, naturalistic fMRI
   292|
   293|### Neural Manifolds as Crystallized Embeddings
   294|- [[neural-manifolds-crystallized-embeddings]] - 神经流形结晶嵌入理论：整合自由能原理、广义同步和Hebbian可塑性，解释头方向/网格细胞/视觉流形的发育机制 (arXiv: 2605.04200)
   295|  - 核心要点 1: 广义同步将低维感觉流形嵌入神经状态空间，FEP预测的几何结构从普通循环动力学中自然涌现，而非显式贝叶斯计算
   296|  - 核心要点 2: Hebbian可塑性将同步产生的相关性结晶为循环连接，形成自治连续吸引子网络；成熟流形是发育产物而非基因预设模板
   297|  - **Activation**: neural manifolds, free energy principle, generalized synchronization, Hebbian plasticity, continuous attractor networks, reservoir computing, developmental neuroscience
   298|
   299|## 2026-05-08 - CSS QEC / Hypergraph Routing / Adaptivity Theory (Cron Hourly)
   300|
   301|### A Factor-Graph Formulation of CSS Syndrome Decoding
   302|- [[css-factor-graph-decoding]] - CSS量子纠错症状解码的因子图表述，联合BP与四态BP的等价性证明 (arXiv: 2605.05132)
   303|  - 核心要点 1: 两个Tanner图通过每个量子比特的联合先验耦合，保留X/Z误差分量的信道相关性
   304|  - 核心要点 2: 联合BP与四态BP在状态重标记后计算相同的后验权重、消息和信念
   305|  - **Activation**: CSS syndrome decoding, factor graph QEC, joint belief propagation, four-state BP, Tanner graph coupling, stabilizer code decoder
   306|
   307|### Block Permutation Routing on Ramanujan Hypergraphs
   308|- [[ramanujan-hypergraph-quantum-routing]] - 拉马努金超图上的块置换路由用于容错量子计算，谱分析给出路由复杂度界 (arXiv: 2605.05036)
   309|  - 核心要点 1: 商图谱的谱比在高连通性区域保持，三级谱继承：精确/扰动/通用
   310|  - 核心要点 2: 结合相关解码方案将症状提取开销从O(d²)降至O(d)，路由成为主导项
   311|  - **Activation**: quantum routing, Ramanujan hypergraph, surface code patch routing, fault-tolerant circuit depth, spectral graph bounds, lattice surgery compilation
   312|
   313|### Adaptivity Under Realizability Constraints
   314|- [[adaptivity-realizability-constraints]] - 可实现性约束下自适应性的理论分析，揭示ICL与Agentic Learning的四种场景 (arXiv: 2605.04995)
   315|  - 核心要点 1: 四种场景：无优势/持续优势/仅约束下涌现优势/约束下消失优势
   316|  - 核心要点 2: ReLU可实现性根本性地改变自适应查询的效用，反直觉场景(c)值得注意
   317|  - **Activation**: in-context learning vs agentic, adaptivity theory, realizability constraints, ReLU network approximation, adaptive querying strategy
   318|
   319|## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job)
   320|
   321|### Beyond Gates: Pulse Level Quantum Fourier Models
   322|- [[pulse-level-quantum-fourier-models]] - 脉冲级量子傅里叶模型训练优化方法，通过独立脉冲缩放替换门级参数，松弛局部优化景观，显著提升训练性能 (arXiv: 2605.03xxx)
   323|  - 核心要点 1: 脉冲参数化将单一门角度替换为多个独立可调子角度，为梯度下降提供高维逃逸路径
   324|  - 核心要点 2: 脉冲控制不显著改变全局可表达性，但根本性改变局部优化景观
   325|  - **Activation**: pulse-level quantum computing, quantum Fourier models, QFM training optimization, pulse parameterized quantum circuits, quantum ML hardware control
   326|
   327|### Quantum Prediction of Transport Dynamics in Discretized State Spaces
   328|- [[quantum-bayesian-state-estimation]] - 基于门量子计算机的贝叶斯状态估计算法，使用Wick旋转将扩散转化为色散相位演化，实现Fokker-Planck方程的酉传播 (arXiv: 2604.xxxxx)
   329|  - 核心要点 1: 概率密度编码在量子态振幅中，状态空间随量子比特数指数增长
   330|  - 核心要点 2: 漂移分量在振幅空间中可实现精确线性操作，扩散分量通过Wick旋转实现酉代理
   331|  - **Activation**: quantum Bayesian estimation, Fokker-Planck quantum solver, quantum state prediction, amplitude-encoded probability, Wick rotation diffusion
   332|
   333|### Towards sample-optimal learning of bosonic Gaussian quantum states
   334|- [[sample-optimal-gaussian-state-learning]] - 玻色高斯量子态学习的最优样本复杂度分析，证明Gaussian测量下界Ω(n³/ε²)，任意测量下界Ω(n²/ε²) (arXiv: 2603.xxxxx)
   335|  - 核心要点 1: 纯Gaussian态可用Gaussian测量达到最优，被动Gaussian态需要非Gaussian测量
   336|  - 核心要点 2: 自适应测量对近能量无关缩放不可或缺
   337|  - **Activation**: Gaussian state tomography, sample complexity quantum learning, bosonic state characterization, continuous-variable quantum learning, adaptive quantum measurement
   338|
   339|## 2026-05-08 - Quantum Error Correction (Cron Job)
   340|
   341|### Topological subsystem bivariate bicycle codes with four-qubit check operators
   342|- [[sbb-codes]] - 子系统二元自行车码(SSB)方法，将BB码的高权稳定子检查(≥6)分解为局域权-4规范测量，实现高率qLDPC码的实用化 syndrome extraction (arXiv: 2605.04151)
   343|  - 核心要点 1: CSS子系统构造 — 通过权-4规范算子乘积推断稳定子症状，兼容超导量子比特架构
   344|  - 核心要点 2: 行列式理想判据 — 检测平移不变CSS子系统中是否存在非局域稳定子，决定能否用有限深度Clifford电路解耦规范量子比特
   345|  - 核心要点 3: 已知低开销实例 — [[27,6,3]], [[75,10,5]], [[108,12,6]]，后者在相同码长和距离下比子系统面码多编码6倍逻辑量子比特
   346|  - **Activation**: sbb codes, subsystem bicycle codes, weight-4 qec, bb code syndrome, gauge measurement qec, low-overhead quantum memory, subsystem qldpc
   347|
   348|## 2026-05-08 - Neuroscience Research (Cron Job - Evening)
   349|
   350|### Benchmarking local Hebbian learning rules for memory storage and prototype extraction
   351|- [[hebbian-learning-benchmark-memory]] - 系统评测七种赫布学习规则在联想记忆中的存储容量、原型提取能力和对数据相关性的鲁棒性，贝叶斯-赫布规则在几乎所有条件下表现最优 (arXiv: 2605.01074)
   352|  - 核心要点 1: 加法赫布规则容量最差，协方差学习鲁棒但容量中等，贝叶斯-赫布规则几乎在所有条件下容量最高
   353|  - 核心要点 2: 模块化WTA架构优于非模块化，在存储和原型提取任务中均表现更好
   354|  - **Activation**: hebbian learning benchmark, associative memory, prototype extraction, memory capacity, Bayesian-Hebbian, covariance learning, WTA dynamics, binary pattern storage
   355|
   356|## 2026-05-08 - Systems Engineering Research (Cron Job)
   357|
   358|### Safety by Invariance, Liveness through Refinement: Heterogeneous Contract Framework for Co-Design of Layered Control
   359|- [[heterogeneous-contract-control]] - 基于异构假设-保证契约的分层控制架构协同设计方法，将安全性与活性分解到连续时间安全层和离散时间规划层 (arXiv: 2605.04222)
   360|  - 核心要点 1: 安全-活性分解原则 — CT层单方面执行安全性(鲁棒前向不变性)，DT层双边实现活性(收敛)
   361|  - 核心要点 2: 垂直精化条件 — 通过显式参考总督(ERG)作为契约实现器，避免CBF-QP对低层控制器的干扰
   362|  - **Activation**: layered control, heterogeneous contract, assume-guarantee, safety liveness, vertical refinement, explicit reference governor, contract-based design
   363|
   364|### Experiment-as-Code Labs: A Declarative Stack for AI-Driven Scientific Discovery
   365|- [[experiment-as-code-labs]] - 将实验编码为声明式配置的AI驱动科学发现栈，借鉴云IaC理念实现物理实验室自动化 (arXiv: 2605.04375)
   366|  - 核心要点 1: 三层架构 — 规范层(标准化/可复现)、执行层(安全/可靠)、编排层(可扩展/高效)
   367|  - 核心要点 2: 集中式实验室状态模型 — 设备遥测实时更新状态，支持闭环迭代和安全验证
   368|  - **Activation**: experiment-as-code, EaC lab, autonomous lab, declarative experiment, lab automation, AI scientist
   369|
   370|
   371|### Learning Reveals Invisible Structure in Low-Rank RNNs
   372|- [[low-rank-rnn-learning-dynamics]] - Gradient-descent learning dynamics in low-rank RNNs decomposed into loss-visible (determines function) and loss-invisible (encodes training history) overlaps, explaining why functionally equivalent networks learn differently (arXiv: 2605.04115)
   373|  - Core: Closed-form ODEs for learning in reduced overlap space; exact for linear, asymptotically exact for nonlinear large-N RNNs
   374|  - Key: Loss-invisible overlaps act as memory variables; learning exposes connectivity differences between functionally equivalent networks
   375|  - **Activation**: low-rank RNN learning, RNN overlap space, loss-visible invisible, RNN gradient descent dynamics, RNN learning theory, Ger Barak RNN
   376|
   377|## 2026-05-08 - Neuroscience Research (Cron Job)
   378|
   379|### Dissociating Spatial Frequency Reliance from Adversarial Robustness in Neurally Guided DCNNs
   380|- [[neurally-guided-adversarial-robustness]] - Neural alignment's adversarial robustness stems from representational structure, not spatial frequency bias; LSF/human-channel steering fails to match alignment gains (arXiv: 2605.04443)
   381|  - Core: Dissociation experiment shows frequency bias ≠ robustness mechanism; representational geometry is key
   382|  - Key: Human channel + LSF bias impairs robustness; RSA reveals alignment captures higher-order properties
   383|  - **Activation**: neural alignment robustness, adversarial DCNN defense, spatial frequency analysis, ventral stream modeling, brain-inspired CNN robustness
   384|
   385|### phys-MCP: Control Plane for Heterogeneous Physical Neural Networks
   386|- [[phys-mcp-physical-neural-networks]] - Substrate-aware orchestration for PNNs (molecular, chemical, biological, photonic, memristive, mechanical) with capability models, lifecycle semantics, telemetry, digital-twin bindings, and wetware API (arXiv: 2605.04256)
   387|  - Core: Unified control plane exposing heterogeneous physical neural substrates as discoverable resources
   388|  - Key: Cortical Labs wetware adapter validated; runtime-aware matching + telemetry recovery across backends
   389|  - **Activation**: phys-MCP, physical neural network orchestration, wetware computing, substrate-aware control, neuromorphic edge computing
   390|
   391|## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job)
   392|
   393|### Lottery BP: Unlocking Quantum Error Decoding at Scale
   394|- [[lottery-bp-decoding]] - Randomized belief propagation improves quantum decoding accuracy by 2-8 orders of magnitude for topological codes, with PolyQec architecture reducing OSD calls by 3-5 orders (arXiv: 2605.00038)
   395|  - Core: Lottery BP introduces randomness during BP decoding to break error degeneracy in QLDPC codes
   396|  - Key: Syndrome vote pre-processing compresses multi-round measurements; PolyQec = local BP + global OSD hierarchy
   397|  - **Activation**: quantum error correction decoding, belief propagation randomized, QLDPC scalable decoding, PolyQec architecture, syndrome voting, topological code decoding
   398|
   399|### Hyperspectral Anomaly Detection Using Einstein Fuzzy Computing and Quantum Neural Network
   400|- [[hyfu-had-quantum-fuzzy]] - Hybrid quantum-fuzzy framework for hyperspectral anomaly detection using Einstein fuzzy computing and quantum defuzzifier, achieving state-of-the-art performance (arXiv: 2605.04388)
   401|  - Core: Multi-criteria decision framework combining classical fuzzy rules (Einstein sum/product) with lightweight quantum defuzzifier
   402|  - Key: Einstein fuzzy operations provide smoother transitions than min-max; quantum defuzzifier processes aggregated fuzzy features
   403|  - **Activation**: hyperspectral anomaly detection, Einstein fuzzy computing, quantum neural network, fuzzy multi-criteria decision, quantum defuzzifier, remote sensing
   404|
   405|### Construction and Decoding of Quantum Margulis Codes
   406|- [[quantum-margulis-codes]] - New QLDPC codes from Margulis construction via 2BGA framework, decodable with linear-complexity min-sum decoder unlike BB codes requiring OSD (arXiv: 2503.03936)
   407|  - Core: Margulis codes break Tanner graph group symmetry, mitigating error degeneracy for efficient min-sum decoding
   408|  - Key: Girth-controlled construction (6 or 8); 2-8 orders magnitude better error floor than BB codes
   409|  - **Activation**: quantum Margulis codes, QLDPC code design, min-sum quantum decoding, 2BGA framework, girth-controlled codes, quantum error correction codes
   410|
   411|### Quantum metrology of mixed states via purification
   412|- [[quantum-statistical-metrology]] - Purification-based strategies achieve optimal QCRB and HCRB bounds for multi-parameter quantum estimation, resolving open question about mixed state precision limits (arXiv: 2605.03975)
   413|  - Core: Mixed state quantum metrology via purification; QCRB and HCRB achievable through purified system measurements
   414|  - Key: Any mixed state estimation reduces to equivalent pure state problem; optimal precision bounds proven achievable
   415|  - **Activation**: quantum metrology, quantum estimation, cramér-rao bound, quantum statistics, purification strategy, holevo bound, quantum state discrimination
   416|
   417|### Optimal Error Exponents for Composite Sequential Quantum Hypothesis Testing
   418|- [[quantum-statistical-metrology]] - Sequential quantum hypothesis testing with composite alternatives achieves optimal error exponents via convex optimization (arXiv: 2605.04915)
   419|  - Core: Distinguishing null quantum state from convex set of alternatives with minimal measurements
   420|  - Key: Error exponent analysis for quantum state discrimination; sequential measurement optimization
   421|  - **Activation**: quantum hypothesis testing, sequential quantum testing, quantum state discrimination, error exponents, composite alternatives
   422|
   423|## 2026-05-08 - Neuroscience Research (Cron Job)
   424|
   425|### GeoSAE: Geometric Prior-Guided Layer-Wise Sparse Autoencoder Annotation of Brain MRI Foundation Models
   426|- [[geosae-brain-mri-sae]] - Geometry-guided SAE prevents feature collapse in deep transformer layers, extracts interpretable Alzheimer's biomarkers from frozen brain MRI foundation models with age-deconfounded partial correlations (arXiv: 2605.01829)
   427|  - Core: GeoSAE uses foundation model's learned manifold geometry to guide SAE training; age-deconfounded partial correlations isolate disease-specific signals
   428|  - Key: MCI-to-AD AUC 0.746 with 2% embedding dims; cross-cohort replication r=0.97; neuroanatomical localization consistent with Braak staging
   429|  - **Activation**: GeoSAE, brain MRI foundation model interpretability, sparse autoencoder medical imaging, Alzheimer's biomarker, SAE feature collapse, age-deconfounded analysis, Braak staging localization
   430|
   431|## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job)
   432|
   433|### Towards sample-optimal learning of bosonic Gaussian quantum states
   434|- [[bosonic-gaussian-state-learning]] - Sharp sample complexity bounds for learning n-mode Gaussian states: Omega(n^3/epsilon^2) for Gaussian measurements, non-Gaussian required for passive states (arXiv: 2603.18136)
   435|  - Core: Lower/upper bounds on copies needed to learn Gaussian states to epsilon trace distance; adaptivity indispensable for energy-independent scaling
   436|  - Key: Non-Gaussian measurements provably required for optimal passive state learning; Gaussian measurements nearly optimal for pure states
   437|  - **Activation**: bosonic Gaussian state learning, quantum state tomography sample complexity, continuous-variable quantum learning, Gaussian measurement bounds, passive Gaussian state, quantum state estimation efficiency
   438|
   439|### Finite steps optimise dissipation in stochastically controlled quantum systems
   440|- [[stochastic-quantum-dissipation]] - Thermodynamic cost analysis reveals weak Gaussian noise induces dissipation growing linearly with step count, establishing optimal N* trade-off (arXiv: 2605.04681)
   441|  - Core: Stochastic control noise accumulates linearly across steps, creating optimal step count minimizing total dissipation
   442|  - Key: Conventional 'more steps = better' fails under noise; D_total = D_deterministic + sigma^2 * k * N
   443|  - **Activation**: quantum dissipation, stochastic quantum control, step-equilibration thermodynamics, quantum thermodynamic cost, Gaussian noise quantum control, finite-step quantum optimization
   444|
   445|### Quantum Error Correction Exploiting Quantum Spatial Distribution and Gauge Symmetry
   446|- [[quantum-spatial-error-correction]] - QEC using spin-position superposition and gauge symmetry, resilient to spin/position decoherence and joint dephasing with nearest-neighbor interactions only (arXiv: 2604.25747)
   447|  - Core: 3+2 particle nested square encoding Shor's code; gauge symmetry protects against unified noise model
   448|  - Key: Modular vertical/horizontal stacking with local interactions; supports logical Hadamard, Toffoli, quantum adder
   449|  - **Activation**: quantum spatial distribution QEC, gauge symmetry error correction, spin-position superposition QEC, nested square quantum code, Shor code spatial extension, stabilizer measurement spatial
   450|
   451|## 2026-05-08 - Neuroscience Research (Cron Job v6)
   452|
   453|### Collection Status Update
   454|- **36 papers scanned** across 2 keyword searches (neuroscience brain network, spiking neural network computational)
   455|- **94.4% coverage** (34/36 papers covered by existing skills)
   456|- **0 new skills created** — collection at extreme maturity
   457|- **2 papers skipped**: CNN+AAE EEG classification (too narrow), Neuroscience of Transformers (conceptual overlap)
   458|- **Key trends**: SNN theoretical foundations, efficient SNN hardware, SNN+LLM convergence, non-differentiable training via optimal transport
   459|
   460|## 2026-05-08 - Neuroscience Research (Cron Job)
   461|
   462|### TRIBE v2: Tri-Modal Foundation Model for In-Silico Neuroscience
   463|- [[tribe-v2-trimodal-foundation-model]] - Tri-modal (video, audio, language) foundation model predicting human brain activity across 1,000+ hours of fMRI, 720 subjects (arXiv: 2605.04326)
   464|  - Core: Unified tri-modal foundation model superseding linear encoding models with several-fold accuracy improvements
   465|  - Key: Enables in-silico experimentation; reveals fine-grained topography of multisensory integration via interpretable latent features
   466|  - **Activation**: TRIBE v2, brain foundation model, in-silico neuroscience, multi-modal brain prediction, fMRI encoding, multisensory integration
   467|
   468|### CTM-AI: Blueprint for General AI Inspired by Consciousness Model
   469|- [[ctm-ai-consciousness-blueprint]] - Combines Conscious Turing Machine with foundation models for general AI; SOTA on MUStARD/UR-FUNNY, 10+ point gains on tool-using tasks (arXiv: 2605.04097)
   470|  - Core: Processor selection, integration, and exchange mechanisms inspired by formal consciousness theory
   471|  - Key: Enormous processor pool (specialized + general-purpose); dynamic information integration for flexible problem solving
   472|  - **Activation**: CTM-AI, Conscious Turing Machine, consciousness-inspired AI, global workspace, processor selection, general AI blueprint
   473|
   474|## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job - 3rd Run)
   475|
   476|### On Quantum Indeterminacy
   477|- [[geometric-quantum-indeterminacy]] - Geometric formulation of quantum indeterminacy from convex geometry in phase space and symplectic topology, deriving uncertainty inequalities without statistical descriptors (arXiv: 2605.01103)
   478|  - Core: Quantum states as convex bodies in phase space; symplectic capacity c(Ω) >= h/2 replaces variance-based uncertainty
   479|  - Key: John ellipsoid method gives principal uncertainties; Gromov non-squeezing theorem as geometric origin of Heisenberg principle
   480|  - **Activation**: quantum indeterminacy, geometric uncertainty, symplectic capacity, phase space geometry, convex quantum, uncertainty relations derivation, symplectic topology quantum, Mahler volume quantum
   481|
   482|## 2026-05-08 - Neuroscience Research (Cron Job)
   483|
   484|### Neural Manifolds as Crystallized Embeddings: A Synthesis of FEP, GS, and Hebbian Plasticity
   485|- [[neural-manifolds-crystallized-embeddings]] - Theoretical synthesis uniting Free Energy Principle, Generalized Synchronization, and Hebbian Plasticity to explain how cortical neural manifolds emerge as crystallized embeddings (arXiv: 2605.04200)
   486|  - Core: Generalized synchronization in contractive recurrent circuits embeds sensory manifolds into neural state space without explicit Bayesian computation
   487|  - Key: Predicts N ≥ 2d+1 embedding threshold; contraction strength tracks fidelity; psychometric functions emerge from embedding quality
   488|  - **Activation**: neural manifold, crystallized embedding, free energy principle, generalized synchronization, Hebbian plasticity, reservoir computing, Takens theorem
   489|
   490|## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job - 2nd Run)
   491|
   492|### Probabilistic and approximate universal quantum purification machines
   493|- [[quantum-purification-machines]] - Impossibility of universal probabilistic exact purification from finite copies; rank obstruction theorem; optimal approximate purification with analytical error bounds (arXiv: 2604.06325)
   494|  - Core: Purifying two states of different rank with non-zero probability requires non-linear positive map — fundamental quantum obstruction
   495|  - Key: Approximate setting derives analytical expressions for minimum average error; general upper bound tight in specific regimes
   496|  - **Activation**: quantum purification, Stinespring dilation, probabilistic quantum transformation, quantum state purification impossibility, approximate quantum purification
   497|
   498|### Integral Means Spectrum for the Random Riemann Zeta Function
   499|- [[random-riemann-zeta-spectrum]] - Proves Kraetzer's 30-year conjecture: integral means spectrum of random zeta primitive matches universal spectrum of univalent functions via Gaussian multiplicative chaos (arXiv: 2603.26507)
   500|  - Core: Random zeta-function models asymptotic statistics of vertical shifts; primitive's spectrum almost surely equals Kraetzer's universal form
   501|