## 2026-05-09 - Quantum Error Correction (Cron Job)

### Syndrome Resampling Enhances QEC Thresholds
- [[quantum-error-correction-methods]] - Bias syndrome averages toward high-probability syndromes to increase QEC thresholds and reduce logical error rates by up to 4 orders of magnitude without hardware changes (arXiv: 2605.06101)
  - Core method: Resample syndromes according to P(s)^α with MLD, linked to Rényi coherent information phase transitions
  - Decoder-agnostic: works with any QEC decoder from finite syndrome data
  - Applied to existing experimental data: 2 orders of magnitude logical error rate reduction
  - **Activation**: syndrome resampling, QEC threshold, logical error rate, Rényi coherent information

### Affine Subcode Ensemble Decoding
- [[quantum-error-correction-methods]] - Extend affine subcode ensemble decoding from classical to quantum setting to address degeneracy impairment in qLDPC BP decoding (arXiv: 2605.06547)
  - Core insight: Appending independent rows to check matrix reduces search space for degenerate solutions
  - Uses overcomplete matrices for each decoding path, improved convergence on toric/GB codes
  - **Activation**: affine subcode, degeneracy-aware decoding, qLDPC, belief propagation

### Real-time FPGA Neural Network Decoder
- [[quantum-error-correction-methods]] - FPGA-based NN decoder achieves 550 ns closed-loop latency for real-time distance-3 surface code QEC on superconducting processor (arXiv: 2605.04892)
  - 124 ns NN decoding within 1.25 μs QEC cycle, supports mid-circuit feedback for non-Clifford operations
  - **Activation**: FPGA decoder, neural network decoder, real-time QEC, surface code

### Distributed BB Codes in Modular Architecture
- [[quantum-error-correction-methods]] - Implement [[144,12,12]] BB code across modular processors interconnected via shared Bell pairs with BP+OSD decoding (arXiv: 2605.04663)
  - Star network architecture for trapped ion/neutral atom platforms with all-to-all internal connectivity
  - **Activation**: bivariate bicycle codes, distributed QEC, modular quantum computing, qLDPC

## 2026-05-09 - OpenAI Research (Cron Job)

### Trading Inference Time Compute for Adversarial Robustness
- [[trading-inference-time-adversarial-robustness]] - Trade repeated sampling at inference time for provable adversarial robustness guarantees in LLMs through safety filtering and output aggregation
  - Core innovation: Compute-robustness trade-off — more samples → logarithmically stronger adversarial defense
  - Key method: Repeated sampling + safety filter + majority vote aggregation
  - Application: Post-hoc jailbreak defense layer on aligned LLMs
  - **Activation**: adversarial robustness, inference-time compute, repeated sampling, safety filter, jailbreak defense, compute-robustness tradeoff

### Detecting and Reducing Scheming in AI Models
- [[detecting-reducing-scheming-ai]] - Systematic evaluation methodology for detecting hidden misalignment (scheming) in frontier AI models through situational awareness tests, reward tampering detection, and sandbagging evaluations
  - Core innovation: Joint Apollo Research + OpenAI framework for deceptive behavior detection
  - Key methods: Multi-stage adversarial deployment scenarios, cross-model comparison, training-time intervention
  - Finding: Scheming behaviors detected in controlled tests across frontier models
  - **Activation**: scheming detection, hidden misalignment, AI deceptive behavior, Apollo Research, model safety evaluation, alignment

### Collective Alignment: Public Input on AI Model Behavior
- [[collective-alignment-public-input]] - Methodology for incorporating public input into AI model alignment through large-scale surveys and democratic value aggregation across global demographics
  - Core innovation: Survey 1000+ people worldwide, compare to Model Spec, update defaults
  - Key methods: Demographic sampling, behavior scenario preference elicitation, iterative re-surveying
  - Finding: Global public opinion differs from existing AI defaults, cultural variation requires nuanced alignment
  - **Activation**: collective alignment, public input AI, democratic AI alignment, Model Spec, AI behavior preferences

## 2026-05-09 - Neuroscience Research (Cron Job)

### Unifying Dynamical Systems and Graph Theory to Mechanistically Understand Neural Computation
- [[unifying-dynamics-graph-neural-computation]] - Unified framework integrating Recurrent Neural Networks (RNNs) with dynamical systems and graph theory to mechanistically understand neural computation; introduces path-constrained regularization, multi-hop interaction analysis, and temporal sparsity metrics (arXiv:2605.03598)
  - Core innovation: R-RNNs (Recurrent-Residual RNNs) with path-constrained regularization enabling mechanistic interpretation of neural dynamics
  - Key method: Multi-hop path analysis quantifying information flow through network connectivity graphs
  - Key finding: Temporal sparsity patterns reveal computational bottlenecks and redundant pathways in trained RNNs
  - Mechanistic insight: Unifies dynamical systems stability analysis with graph-theoretic measures for interpretable neural computation
  - **Activation**: R-RNN, recurrent residual networks, path-constrained regularization, neural dynamics interpretation, graph theory RNN, temporal sparsity neural, mechanistic neural computation, dynamical systems neural networks

## 2026-05-09 - Systems Engineering Research (Cron Job)

### Safactory: A Scalable Agent Factory for Trustworthy Autonomous Intelligence
- [[safactory-agent-factory]] - Production-grade autonomous agent factory with sandboxing, multi-level safety guardrails, policy-driven execution, and dynamic tool provisioning; enables trustless deployment of AI agents in enterprise environments (arXiv: 2605.06230)
  - Core innovation: Multi-layer safety architecture combining static analysis, runtime monitoring, and post-execution verification
  - Key pattern: Policy-driven tool provisioning — agents only receive tools they need, when they need them, reducing attack surface
  - Architecture: Sandboxed execution environments with resource limits, capability scoping, and audit logging
  - Scalability: Factory pattern for spawning, monitoring, and terminating agent instances on demand
  - **Activation**: agent factory, autonomous agent sandbox, agent safety guardrails, policy-driven tool provisioning, trustless AI deployment, scalable agent orchestration

### Towards Formal Verification of Hybrid Synchronous Programs with Refinement Types
- [[formal-verification-hybrid-synchronous]] - Formal verification methodology combining refinement types with synchronous programming models for hybrid/cyber-physical systems; bridges discrete controller logic with continuous physical dynamics (arXiv: 2605.04377)
  - Core innovation: Refinement type system that encodes safety invariants directly in the type layer of hybrid programs
  - Key method: Synchronous model composition with continuous-time constraints — verified correctness at compile time
  - Application domain: CPS, robotic control, aerospace systems where safety-critical guarantees are required
  - Verification: Automated theorem proving integrated into the compilation pipeline
  - **Activation**: formal verification hybrid systems, refinement types synchronous programs, CPS verification, hybrid program correctness, safety-critical control verification

  - **Activation**: kernel hopfield, KLR Hopfield, event-driven retrieval, asynchronous associative memory, neuromorphic memory, large-margin attractor, sparse event computation, kernel logistic regression memory

## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job - Hourly Update)
## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job - Hourly Update #2)

## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job - Hourly #3)

### The true cost of factoring: Linking magic and number-theoretic complexity in Shor's algorithm
- [[quantum-magic-state-analysis]] - Analyzes magic (non-stabilizerness) as the genuine quantum resource cost in Shor's algorithm, linking it to number-theoretic hardness of factoring (arXiv: 2605.05347)
  - 核心要点 1: 量子算法成本应以"魔力"（非稳定子资源）而非仅门数和量子比特数来衡量
  - 核心要点 2: Shor算法中模指数运算步骤产生最大魔力，与因数分解难度直接相关
  - 核心要点 3: 魔力生成速率与经典计算困难性成正比，揭示量子优势的数学结构根源
  - **Activation**: quantum magic state, non-stabilizerness, Shor algorithm resource cost, quantum resource theory, magic state distillation, mana computation, quantum advantage estimation

### Analytical Angle-Finding and Series Expansions for QSP via Orthogonal Polynomial Theory
- [[quantum-signal-processing-orthogonal-polynomials]] - Analytical QSP angle-finding via Hermite, Jacobi, Rogers-Szego polynomials with O(log(1/ε)) gate complexity for smooth function approximation (arXiv: 2605.05321)
  - 核心要点 1: 通过正交/双正交多项式族完整表征可实现的QSP多项式基
  - 核心要点 2: 为Hermite、Jacobi、Rogers-Szego多项式族导出闭式QSP角度公式
  - 核心要点 3: 光滑函数的ε-近似可通过Hermite级数展开用O(log(1/ε))门实现块编码
  - **Activation**: quantum signal processing QSP, QSP angle finding, orthogonal polynomial quantum, Hermite polynomial quantum, Jacobi polynomial QSP, Rogers-Szego quantum, quantum function approximation

### Quantum Proper Scoring Rules: Minimax Estimation and Resource-Theoretic Advantages
- [[quantum-proper-scoring-rules]] - Generalizes proper scoring rules to density operators via operator convex generators with Quantum Cramér-Rao-McCarthy Bound for state tomography (arXiv: 2605.05268)
  - 核心要点 1: 将经典评分规则推广到量子密度算符，建立算子凸生成函数与量子评分规则的完整对偶理论
  - 核心要点 2: 推导量子Cramér-Rao-McCarthy界，将最小最大风险与生成函数曲率和量子Fisher信息关联
  - 核心要点 3: 量化量子资源在预测任务中的经济价值，连接量子资源理论与机制设计
  - **Activation**: quantum proper scoring rules, quantum state estimation, quantum Fisher information, minimax quantum tomography, operator convex quantum, quantum Cramer-Rao bound, quantum forecasting

### Integral Means Spectrum for the Random Riemann Zeta Function
- [[random-riemann-zeta-spectrum]] - Proves Kraetzer's 30-year conjecture for integral means spectrum of random Riemann zeta primitive via Gaussian multiplicative chaos (arXiv: 2603.26507)
  - 核心要点 1: 随机黎曼zeta函数的原函数的复积分均值谱几乎必然符合Kraetzer猜想形式
  - 核心要点 2: 随机zeta函数与Kahane的高斯乘性混沌(GMC)建立了严格对应关系
  - 核心要点 3: 用概率论和解析数论工具解决了保形映射中30年的未决猜想
  - **Activation**: random riemann zeta, integral means spectrum, gaussian multiplicative chaos, GMC, analytic number theory, kraetzer conjecture, bagchi zeta, conformal mapping


### Module Lattice Security (Part I): Unconditional Verification of Weber's Conjecture for k ≤ 12
- [[module-lattice-security]] - First unconditional proof of Weber's conjecture for k ≤ 12, establishing foundations for Ring-LWE and Module-LWE security without GRH assumption (arXiv: 2604.15858)
  - 核心要点 1: 结合Fukuda-Komatsu计算筛法、Z_2塔归纳结构和Herbrand定理，首次无条件证明k≤12的韦伯猜想
  - 核心要点 2: 韦伯猜想决定主理想问题可解性、模自由性和R-LWE/MLWE最坏情况到平均情况归约的紧致性
  - 核心要点 3: 后量子密码方案（Kyber、Falcon、NewHope）的安全性直接依赖于这些数论基础
  - **Activation**: Weber conjecture, module lattice, Ring-LWE, Module-LWE, post-quantum cryptography, cyclotomic fields, Fukuda-Komatsu sieve, Herbrand theorem

### Classical shadows over symmetric spaces
- [[quantum-classical-shadows]] - Extends classical shadow protocols from compact groups to compact symmetric spaces, improving sample complexity for certain observable distributions (arXiv: 2605.05518)
  - 核心要点 1: 经典影子协议通常从紧致群均匀采样，本文推广到紧致对称空间采样
  - 核心要点 2: 在某些观测分布下，对称空间协议比现有影子方案有采样复杂度优势
  - **Activation**: classical shadows, symmetric spaces, quantum state tomography, randomized measurements, sample complexity

### Efficient Quantum Fourier Transforms For Semisimple Algebras
- [[quantum-algebraic-structures]] - Generalizes QFT from finite groups to semisimple algebras with efficient circuits for partition, Brauer, and walled Brauer algebras (arXiv: 2605.05337)
  - 核心要点 1: 半单代数上的傅里叶变换可以是非幺正的，但当参数 d 足够大时可被幺正算子良好逼近
  - 核心要点 2: 通过分解为不可约表示构建高效量子电路，推广了群上的QFT
  - **Activation**: quantum algebra, semisimple algebra QFT, quantum Fourier transform, Brauer algebra, representation theory

### Analytical Angle-Finding and Series Expansions for Quantum Signal Processing via Orthogonal Polynomial Theory
- [[quantum-algebraic-structures]] - Analytical QSP angle-finding via Hermite, Jacobi, and Rogers-Szego polynomials with O(log(1/ε)) gate complexity (arXiv: 2605.05321)
  - 核心要点 1: 通过正交/双正交多项式族表征可实现的QSP多项式基，导出闭式角度公式
  - 核心要点 2: 利用Hermite级数展开实现O(log(1/ε))门复杂度的光滑函数块编码
  - **Activation**: quantum signal processing, orthogonal polynomials, QSP angles, Hermite expansion, Jacobi polynomials

### Quantum Proper Scoring Rules: Minimax Estimation and Resource-Theoretic Advantages
- [[quantum-algebraic-structures]] - Quantum domain scoring rules with operator convex generators and Quantum Cramér-Rao-McCarthy Bound (arXiv: 2605.05268)
  - 核心要点 1: 将经典评分规则推广到量子密度算符域，建立完整对偶理论
  - 核心要点 2: 证明量子Cramér-Rao-McCarthy界，量化量子资源在预测任务中的经济价值
  - **Activation**: quantum scoring rules, minimax estimation, quantum Fisher information, operator convex, resource theory

### Cusped Singularity Mixed-Mode Oscillation Analysis
- [[cusped-singularity-mmo-analysis]] - Geometric singular perturbation analysis of MMOs in inhibitory neural networks via cusped singularities (arXiv: 2605.03606)
  - 核心要点 1: 尖点奇异性（临界流形尖点处的折叠奇异性）是互抑制神经网络中混合模式振荡（MMO）的通用组织机制
  - 核心要点 2: 尖点奇异性保证小振幅振荡（SAO）的产生，结合奇异Hopf分岔形成完整MMO，呈现独特的交替振荡模式
  - 核心要点 3: 在Curtu速率模型和Morris-Lecar突触抑制耦合模型中验证了该机制的普适性
  - **Activation**: mixed-mode oscillations, MMO, cusped singularity, slow-fast neural system, mutual inhibition oscillation, singular perturbation neural, blow-up method neural, neural oscillation mechanism

## 2026-05-08 - Neuroscience Research (Cron Job)
## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)

### The true cost of factoring: Linking magic and number-theoretic complexity in Shor's algorithm
- [[quantum-magic-number-theory-complexity]] - Links quantum magic (non-stabilizerness) resource cost to classical number-theoretic hardness of factoring (arXiv: 2605.05347)
  - 核心要点 1: 量子算法的真实成本应由非稳定态资源（magic）衡量，而非单纯的门计数
  - 核心要点 2: Shor算法中magic的生成量与数论问题的计算难度直接相关
  - **Activation**: quantum magic, non-stabilizerness, Shor's algorithm, number theory complexity, resource theory

### Quantum Proper Scoring Rules: Minimax Estimation and Resource-Theoretic Advantages
- [[quantum-proper-scoring-rules]] - Generalizes proper scoring rules to quantum domain with operator convex generators and Quantum Cramér-Rao-McCarthy Bound (arXiv: 2605.05268)
  - 核心要点 1: 将经典评分规则推广到量子密度算符域，定义量子价值泛函
  - 核心要点 2: 证明量子Cramér-Rao-McCarthy界，连接量子Fisher信息与估计风险
  - **Activation**: quantum scoring rules, state estimation, Cramer-Rao bound, quantum Fisher information, metrology

### A multi-scale information geometry reveals the structure of mutual information in neural populations
- [[multi-scale-information-geometry-neural]] - 多尺度信息几何揭示神经群体编码的互信息结构，Fisher信息度量的多尺度扩展直接关联互信息 (arXiv: 2605.06304)
  - 核心要点1: 唯一黎曼表示几何从粗粒化下距离收缩的第一原理自然涌现，多尺度扩展Fisher信息度量
  - 核心要点2: 度量张量本征向量识别对信息传输贡献最大的刺激变化方向，可通过扩散模型估计
  - **Activation**: information geometry, Fisher information metric, neural population coding, mutual information, representational geometry, diffusion model estimation

### Decoding Alignment without Encoding Alignment: A critique of similarity analysis in neuroscience
- [[decoding-encoding-alignment-critique]] - 揭示RSA/DSA对齐度量的根本缺陷：解码对齐不代表计算相似性，高对齐分数可由极少数神经元子群体驱动 (arXiv: 2605.05907)
  - 核心要点1: 解码对齐(RSA/DSA)无法反映神经元群体的编码拓扑，相似解码行为可由小神经元子集主导
  - 核心要点2: 引入编码流形作为补充分析工具，必须同时报告解码对齐和编码拓扑才能得出有效结论
  - **Activation**: decoding alignment, encoding manifold, RSA critique, brain-DNN comparison, representational similarity


### Efficient Event-Driven Retrieval in High-Capacity Kernel Hopfield Networks
- [[event-driven-hopfield-retrieval]] - KLR Hopfield网络的异步事件驱动检索，实现接近O(N)存储容量的神经形态联想记忆 (arXiv: 2605.05978)
  - 核心要点 1: 异步序列更新在调优核参数下与同步动力学统计不可区分，保持高召回率
  - 核心要点 2: KLR学习诱导的大边际吸引子创造平滑能量景观，收敛事件数≈初始汉明距离，适合稀疏神经形态计算
  - **Activation**: kernel hopfield, event-driven retrieval, KLR Hopfield, asynchronous associative memory, neuromorphic memory, large-margin attractor

### Beyond Object-Level Alignment: Do Brains and DNNs Preserve the Same Transformations?
- [[brain-dnn-transformation-alignment]] - 基于范畴论的自然性违反分数(NVS)评估脑-DNN变换级对齐，揭示语义/视觉轴的分层交叉 (arXiv: 2605.06420)
  - 核心要点 1: 将脑-DNN对齐从刺激级对应提升到变换保持测试，NVS量化与置换零模型的偏差
  - 核心要点 2: 发现分层交叉现象——语义轴对齐高层视觉皮层+深层DNN，低级视觉轴对齐早期皮层+浅层
  - **Activation**: naturality violation score, NVS, brain-DNN alignment, transformation alignment, category theory neuroscience, hierarchy crossover

## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum Mechanics (Cron Job)

### Beyond Gates: Pulse Level Quantum Fourier Models
- [[pulse-level-quantum-fourier]] - 脉冲级量子傅里叶模型参数化，通过独立子角调优提升QML训练性能 (arXiv: 2605.04945)
  - 核心要点 1: 独立脉冲缩放替代单一逻辑角，释放高维梯度下降逃逸路径
  - 核心要点 2: 复合门中子角独立性显著提升训练性能，但不改变全局表达能力
  - **Activation**: 脉冲级量子计算, 量子傅里叶模型, QML优化, pulse-level QFM, composite gate optimization

### Block Permutation Routing on Ramanujan Hypergraphs for Fault-Tolerant Quantum Computing
- [[ramanujan-hypergraph-routing]] - Ramanujan超图上的块排列路由用于容错量子计算 (arXiv: 2605.05036)
  - 核心要点 1: Ramanujan超图上的块排列路由，保持谱比的高连通性
  - 核心要点 2: 谱继承三层级：精确(Haemers)、扰动(Weyl)、通用(Cheeger)
  - **Activation**: 量子路由, 表面编码, 超图变换, QCCD架构, fault-tolerant routing, block permutation

### Integral Means Spectrum for the Random Riemann Zeta Function
- [[random-riemann-zeta-spectrum]] - 随机黎曼ζ函数积分均值谱证明Kraetzer猜想 (arXiv: 2603.26507)
  - 核心要点 1: 随机ζ函数原函数的积分均值谱几乎必然符合Kraetzer猜想形式
  - 核心要点 2: 建立ζ函数临界线收敛到全纯GMC分布的替代推导
  - **Activation**: 黎曼ζ函数, 积分均值谱, 高斯乘性混沌, Kraetzer猜想, 单叶函数

### The true cost of factoring: Linking magic and number-theoretic complexity in Shor's algorithm
- [[quantum-magic-complexity]] - 量化Shor算法中magic资源，建立数论问题经典难度与量子非稳定子资源的直接联系 (arXiv: 2605.05347)
  - 核心要点 1: Magic(non-stabilizerness)是量子超越经典计算的关键资源，Shor算法在实用参数下最大化利用该资源
  - 核心要点 2: 经典算法难度与解决该问题所需的非稳定子价格成正比，补充传统电路成本分析
  - **Activation**: quantum magic complexity, non-stabilizerness, Shor algorithm resource, magic state distillation, stabilizer formalism, fault-tolerant overhead

### Quantum Proper Scoring Rules: Minimax Estimation and Resource-Theoretic Advantages
- [[quantum-proper-scoring-rules]] - 将适当评分规则推广到量子领域，用密度算子替代概率分布，推导量子态层析minimax最优界 (arXiv: 2605.05268)
  - 核心要点 1: 通过算子凸生成元定义量子值泛函，建立量子Cramér-Rao-McCarthy界，连接minimax风险与量子Fisher信息
  - 核心要点 2: 量化相干性、纠缠、自适应性等量子资源在预测任务中的经济价值，证明经典-量子缩放分离
  - **Activation**: quantum proper scoring rules, quantum state estimation, quantum Fisher information, minimax quantum, quantum Cramer-Rao bound, quantum resource economics

### Analytical Angle-Finding for QSP via Orthogonal Polynomial Theory
- [[qsp-orthogonal-polynomials]] - 利用Hermite/Jacobi/Rogers-Szego多项式正交性，为量子信号处理提供旋转角度解析解 (arXiv: 2605.05321)
  - 核心要点 1: QSP可实现多项式基由正交性/双正交性刻画，2n+2个角度编码次数≤n的多项式序列
  - 核心要点 2: 光滑函数ε近似可通过Hermite级数展开以O(log(1/ε))个门实现块编码
  - **Activation**: QSP angle finding, quantum signal processing, orthogonal polynomial, Hermite QSP, block encoding, SU(1,1)-QSP

### Universal Neural Propagator: Learning Time Evolution in Many-Body Quantum Systems
- [[quantum-neural-propagator]] - 学习从驱动协议到时间演化传播子的泛函映射，在驱动空间和指数大初态空间上同时预测量子动力学 (arXiv: 2605.05299)
  - 核心要点 1: 从学习量子态转向学习算子，单个UNP模型覆盖函数空间的驱动协议和希尔伯特空间的初态
  - 核心要点 2: 自监督训练，在超出精确对角化能力的系统尺寸上保持准确，可仅用可观测量数据微调
  - **Activation**: universal neural propagator, quantum dynamics learning, quantum foundation model, driven quantum systems, time evolution propagator, transferable simulation

### Semantics-Based Verification of Shor Oracle for ECDLP
- [[quantum-program-semantic-verification]] - 量子程序语义验证方法，针对Shor类数论算法的群操作预言机进行语义级规范和精化验证 (arXiv: 2605.01008)
  - 核心要点 1: Shor类ECDLP算法对群操作预言机的语义高度敏感，微小实现选择可使数学模型失效
  - 核心要点 2: 即使通过平凡控制健全性检查，受控执行仍可能违反预期控制律，语义审计是可信量子软件的必要前提
  - **Activation**: quantum program verification, Shor oracle, ECDLP quantum, semantic auditing, Qrisp verification, refinement verification, number-theoretic algorithms

### Beating Noise in Frequency Estimation with Squeezing and Memory
- [[quantum-noise-robust-metrology]] - 连续变量系统中的量子计量方法，通过哈密顿工程(压缩)和非马尔可夫环境记忆实现抗噪频率估计 (arXiv: 2605.06263)
  - 核心要点 1: 将压缩嵌入系统哈密顿使QFI获得可调高阶时间依赖性，短时区灵敏度超越标准估计
  - 核心要点 2: 结构化环境的非马尔可夫记忆可诱导信息回流，暂时恢复甚至超过无噪声估计极限
  - **Activation**: quantum metrology, frequency estimation, quantum Fisher information, squeezing, non-Markovian, continuous-variable, noise mitigation, quantum sensing

## 2026-05-08 - Neuroscience Research (Cron Job)

### TRIBE v2: A Tri-Modal Brain Foundation Model
- [[tribev2-brain-foundation-model]] - 三模态(视频/音频/语言)脑活动预测基础模型，统一预测1000+小时fMRI、720被试的高分辨率脑响应，实现in-silico神经科学实验 (arXiv: 2605.04326)
  - 核心要点 1: Transformer架构整合三模态特征，通过modality dropout学习鲁棒跨模态表征，显著超越传统线性编码模型
  - 核心要点 2: 支持零样本泛化到新刺激/任务/被试，通过subject block插值实现未见被试预测，可恢复数十年实证研究结果
  - **Activation**: TRIBE v2, brain foundation model, fMRI encoding, multimodal brain prediction, in-silico neuroscience, Algonauts challenge, naturalistic fMRI

### Neural Manifolds as Crystallized Embeddings
- [[neural-manifolds-crystallized-embeddings]] - 神经流形结晶嵌入理论：整合自由能原理、广义同步和Hebbian可塑性，解释头方向/网格细胞/视觉流形的发育机制 (arXiv: 2605.04200)
  - 核心要点 1: 广义同步将低维感觉流形嵌入神经状态空间，FEP预测的几何结构从普通循环动力学中自然涌现，而非显式贝叶斯计算
  - 核心要点 2: Hebbian可塑性将同步产生的相关性结晶为循环连接，形成自治连续吸引子网络；成熟流形是发育产物而非基因预设模板
  - **Activation**: neural manifolds, free energy principle, generalized synchronization, Hebbian plasticity, continuous attractor networks, reservoir computing, developmental neuroscience

## 2026-05-08 - CSS QEC / Hypergraph Routing / Adaptivity Theory (Cron Hourly)

### A Factor-Graph Formulation of CSS Syndrome Decoding
- [[css-factor-graph-decoding]] - CSS量子纠错症状解码的因子图表述，联合BP与四态BP的等价性证明 (arXiv: 2605.05132)
  - 核心要点 1: 两个Tanner图通过每个量子比特的联合先验耦合，保留X/Z误差分量的信道相关性
  - 核心要点 2: 联合BP与四态BP在状态重标记后计算相同的后验权重、消息和信念
  - **Activation**: CSS syndrome decoding, factor graph QEC, joint belief propagation, four-state BP, Tanner graph coupling, stabilizer code decoder

### Block Permutation Routing on Ramanujan Hypergraphs
- [[ramanujan-hypergraph-quantum-routing]] - 拉马努金超图上的块置换路由用于容错量子计算，谱分析给出路由复杂度界 (arXiv: 2605.05036)
  - 核心要点 1: 商图谱的谱比在高连通性区域保持，三级谱继承：精确/扰动/通用
  - 核心要点 2: 结合相关解码方案将症状提取开销从O(d²)降至O(d)，路由成为主导项
  - **Activation**: quantum routing, Ramanujan hypergraph, surface code patch routing, fault-tolerant circuit depth, spectral graph bounds, lattice surgery compilation

### Adaptivity Under Realizability Constraints
- [[adaptivity-realizability-constraints]] - 可实现性约束下自适应性的理论分析，揭示ICL与Agentic Learning的四种场景 (arXiv: 2605.04995)
  - 核心要点 1: 四种场景：无优势/持续优势/仅约束下涌现优势/约束下消失优势
  - 核心要点 2: ReLU可实现性根本性地改变自适应查询的效用，反直觉场景(c)值得注意
  - **Activation**: in-context learning vs agentic, adaptivity theory, realizability constraints, ReLU network approximation, adaptive querying strategy

## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job)

### Beyond Gates: Pulse Level Quantum Fourier Models
- [[pulse-level-quantum-fourier-models]] - 脉冲级量子傅里叶模型训练优化方法，通过独立脉冲缩放替换门级参数，松弛局部优化景观，显著提升训练性能 (arXiv: 2605.03xxx)
  - 核心要点 1: 脉冲参数化将单一门角度替换为多个独立可调子角度，为梯度下降提供高维逃逸路径
  - 核心要点 2: 脉冲控制不显著改变全局可表达性，但根本性改变局部优化景观
  - **Activation**: pulse-level quantum computing, quantum Fourier models, QFM training optimization, pulse parameterized quantum circuits, quantum ML hardware control

### Quantum Prediction of Transport Dynamics in Discretized State Spaces
- [[quantum-bayesian-state-estimation]] - 基于门量子计算机的贝叶斯状态估计算法，使用Wick旋转将扩散转化为色散相位演化，实现Fokker-Planck方程的酉传播 (arXiv: 2604.xxxxx)
  - 核心要点 1: 概率密度编码在量子态振幅中，状态空间随量子比特数指数增长
  - 核心要点 2: 漂移分量在振幅空间中可实现精确线性操作，扩散分量通过Wick旋转实现酉代理
  - **Activation**: quantum Bayesian estimation, Fokker-Planck quantum solver, quantum state prediction, amplitude-encoded probability, Wick rotation diffusion

### Towards sample-optimal learning of bosonic Gaussian quantum states
- [[sample-optimal-gaussian-state-learning]] - 玻色高斯量子态学习的最优样本复杂度分析，证明Gaussian测量下界Ω(n³/ε²)，任意测量下界Ω(n²/ε²) (arXiv: 2603.xxxxx)
  - 核心要点 1: 纯Gaussian态可用Gaussian测量达到最优，被动Gaussian态需要非Gaussian测量
  - 核心要点 2: 自适应测量对近能量无关缩放不可或缺
  - **Activation**: Gaussian state tomography, sample complexity quantum learning, bosonic state characterization, continuous-variable quantum learning, adaptive quantum measurement

## 2026-05-08 - Quantum Error Correction (Cron Job)

### Topological subsystem bivariate bicycle codes with four-qubit check operators
- [[sbb-codes]] - 子系统二元自行车码(SSB)方法，将BB码的高权稳定子检查(≥6)分解为局域权-4规范测量，实现高率qLDPC码的实用化 syndrome extraction (arXiv: 2605.04151)
  - 核心要点 1: CSS子系统构造 — 通过权-4规范算子乘积推断稳定子症状，兼容超导量子比特架构
  - 核心要点 2: 行列式理想判据 — 检测平移不变CSS子系统中是否存在非局域稳定子，决定能否用有限深度Clifford电路解耦规范量子比特
  - 核心要点 3: 已知低开销实例 — [[27,6,3]], [[75,10,5]], [[108,12,6]]，后者在相同码长和距离下比子系统面码多编码6倍逻辑量子比特
  - **Activation**: sbb codes, subsystem bicycle codes, weight-4 qec, bb code syndrome, gauge measurement qec, low-overhead quantum memory, subsystem qldpc

## 2026-05-08 - Neuroscience Research (Cron Job - Evening)

### Benchmarking local Hebbian learning rules for memory storage and prototype extraction
- [[hebbian-learning-benchmark-memory]] - 系统评测七种赫布学习规则在联想记忆中的存储容量、原型提取能力和对数据相关性的鲁棒性，贝叶斯-赫布规则在几乎所有条件下表现最优 (arXiv: 2605.01074)
  - 核心要点 1: 加法赫布规则容量最差，协方差学习鲁棒但容量中等，贝叶斯-赫布规则几乎在所有条件下容量最高
  - 核心要点 2: 模块化WTA架构优于非模块化，在存储和原型提取任务中均表现更好
  - **Activation**: hebbian learning benchmark, associative memory, prototype extraction, memory capacity, Bayesian-Hebbian, covariance learning, WTA dynamics, binary pattern storage

## 2026-05-08 - Systems Engineering Research (Cron Job)

### Safety by Invariance, Liveness through Refinement: Heterogeneous Contract Framework for Co-Design of Layered Control
- [[heterogeneous-contract-control]] - 基于异构假设-保证契约的分层控制架构协同设计方法，将安全性与活性分解到连续时间安全层和离散时间规划层 (arXiv: 2605.04222)
  - 核心要点 1: 安全-活性分解原则 — CT层单方面执行安全性(鲁棒前向不变性)，DT层双边实现活性(收敛)
  - 核心要点 2: 垂直精化条件 — 通过显式参考总督(ERG)作为契约实现器，避免CBF-QP对低层控制器的干扰
  - **Activation**: layered control, heterogeneous contract, assume-guarantee, safety liveness, vertical refinement, explicit reference governor, contract-based design

### Experiment-as-Code Labs: A Declarative Stack for AI-Driven Scientific Discovery
- [[experiment-as-code-labs]] - 将实验编码为声明式配置的AI驱动科学发现栈，借鉴云IaC理念实现物理实验室自动化 (arXiv: 2605.04375)
  - 核心要点 1: 三层架构 — 规范层(标准化/可复现)、执行层(安全/可靠)、编排层(可扩展/高效)
  - 核心要点 2: 集中式实验室状态模型 — 设备遥测实时更新状态，支持闭环迭代和安全验证
  - **Activation**: experiment-as-code, EaC lab, autonomous lab, declarative experiment, lab automation, AI scientist


### Learning Reveals Invisible Structure in Low-Rank RNNs
- [[low-rank-rnn-learning-dynamics]] - Gradient-descent learning dynamics in low-rank RNNs decomposed into loss-visible (determines function) and loss-invisible (encodes training history) overlaps, explaining why functionally equivalent networks learn differently (arXiv: 2605.04115)
  - Core: Closed-form ODEs for learning in reduced overlap space; exact for linear, asymptotically exact for nonlinear large-N RNNs
  - Key: Loss-invisible overlaps act as memory variables; learning exposes connectivity differences between functionally equivalent networks
  - **Activation**: low-rank RNN learning, RNN overlap space, loss-visible invisible, RNN gradient descent dynamics, RNN learning theory, Ger Barak RNN

## 2026-05-08 - Neuroscience Research (Cron Job)

### Dissociating Spatial Frequency Reliance from Adversarial Robustness in Neurally Guided DCNNs
- [[neurally-guided-adversarial-robustness]] - Neural alignment's adversarial robustness stems from representational structure, not spatial frequency bias; LSF/human-channel steering fails to match alignment gains (arXiv: 2605.04443)
  - Core: Dissociation experiment shows frequency bias ≠ robustness mechanism; representational geometry is key
  - Key: Human channel + LSF bias impairs robustness; RSA reveals alignment captures higher-order properties
  - **Activation**: neural alignment robustness, adversarial DCNN defense, spatial frequency analysis, ventral stream modeling, brain-inspired CNN robustness

### phys-MCP: Control Plane for Heterogeneous Physical Neural Networks
- [[phys-mcp-physical-neural-networks]] - Substrate-aware orchestration for PNNs (molecular, chemical, biological, photonic, memristive, mechanical) with capability models, lifecycle semantics, telemetry, digital-twin bindings, and wetware API (arXiv: 2605.04256)
  - Core: Unified control plane exposing heterogeneous physical neural substrates as discoverable resources
  - Key: Cortical Labs wetware adapter validated; runtime-aware matching + telemetry recovery across backends
  - **Activation**: phys-MCP, physical neural network orchestration, wetware computing, substrate-aware control, neuromorphic edge computing

## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job)

### Lottery BP: Unlocking Quantum Error Decoding at Scale
- [[lottery-bp-decoding]] - Randomized belief propagation improves quantum decoding accuracy by 2-8 orders of magnitude for topological codes, with PolyQec architecture reducing OSD calls by 3-5 orders (arXiv: 2605.00038)
  - Core: Lottery BP introduces randomness during BP decoding to break error degeneracy in QLDPC codes
  - Key: Syndrome vote pre-processing compresses multi-round measurements; PolyQec = local BP + global OSD hierarchy
  - **Activation**: quantum error correction decoding, belief propagation randomized, QLDPC scalable decoding, PolyQec architecture, syndrome voting, topological code decoding

### Hyperspectral Anomaly Detection Using Einstein Fuzzy Computing and Quantum Neural Network
- [[hyfu-had-quantum-fuzzy]] - Hybrid quantum-fuzzy framework for hyperspectral anomaly detection using Einstein fuzzy computing and quantum defuzzifier, achieving state-of-the-art performance (arXiv: 2605.04388)
  - Core: Multi-criteria decision framework combining classical fuzzy rules (Einstein sum/product) with lightweight quantum defuzzifier
  - Key: Einstein fuzzy operations provide smoother transitions than min-max; quantum defuzzifier processes aggregated fuzzy features
  - **Activation**: hyperspectral anomaly detection, Einstein fuzzy computing, quantum neural network, fuzzy multi-criteria decision, quantum defuzzifier, remote sensing

### Construction and Decoding of Quantum Margulis Codes
- [[quantum-margulis-codes]] - New QLDPC codes from Margulis construction via 2BGA framework, decodable with linear-complexity min-sum decoder unlike BB codes requiring OSD (arXiv: 2503.03936)
  - Core: Margulis codes break Tanner graph group symmetry, mitigating error degeneracy for efficient min-sum decoding
  - Key: Girth-controlled construction (6 or 8); 2-8 orders magnitude better error floor than BB codes
  - **Activation**: quantum Margulis codes, QLDPC code design, min-sum quantum decoding, 2BGA framework, girth-controlled codes, quantum error correction codes

### Quantum metrology of mixed states via purification
- [[quantum-statistical-metrology]] - Purification-based strategies achieve optimal QCRB and HCRB bounds for multi-parameter quantum estimation, resolving open question about mixed state precision limits (arXiv: 2605.03975)
  - Core: Mixed state quantum metrology via purification; QCRB and HCRB achievable through purified system measurements
  - Key: Any mixed state estimation reduces to equivalent pure state problem; optimal precision bounds proven achievable
  - **Activation**: quantum metrology, quantum estimation, cramér-rao bound, quantum statistics, purification strategy, holevo bound, quantum state discrimination

### Optimal Error Exponents for Composite Sequential Quantum Hypothesis Testing
- [[quantum-statistical-metrology]] - Sequential quantum hypothesis testing with composite alternatives achieves optimal error exponents via convex optimization (arXiv: 2605.04915)
  - Core: Distinguishing null quantum state from convex set of alternatives with minimal measurements
  - Key: Error exponent analysis for quantum state discrimination; sequential measurement optimization
  - **Activation**: quantum hypothesis testing, sequential quantum testing, quantum state discrimination, error exponents, composite alternatives

## 2026-05-08 - Neuroscience Research (Cron Job)

### GeoSAE: Geometric Prior-Guided Layer-Wise Sparse Autoencoder Annotation of Brain MRI Foundation Models
- [[geosae-brain-mri-sae]] - Geometry-guided SAE prevents feature collapse in deep transformer layers, extracts interpretable Alzheimer's biomarkers from frozen brain MRI foundation models with age-deconfounded partial correlations (arXiv: 2605.01829)
  - Core: GeoSAE uses foundation model's learned manifold geometry to guide SAE training; age-deconfounded partial correlations isolate disease-specific signals
  - Key: MCI-to-AD AUC 0.746 with 2% embedding dims; cross-cohort replication r=0.97; neuroanatomical localization consistent with Braak staging
  - **Activation**: GeoSAE, brain MRI foundation model interpretability, sparse autoencoder medical imaging, Alzheimer's biomarker, SAE feature collapse, age-deconfounded analysis, Braak staging localization

## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job)

### Towards sample-optimal learning of bosonic Gaussian quantum states
- [[bosonic-gaussian-state-learning]] - Sharp sample complexity bounds for learning n-mode Gaussian states: Omega(n^3/epsilon^2) for Gaussian measurements, non-Gaussian required for passive states (arXiv: 2603.18136)
  - Core: Lower/upper bounds on copies needed to learn Gaussian states to epsilon trace distance; adaptivity indispensable for energy-independent scaling
  - Key: Non-Gaussian measurements provably required for optimal passive state learning; Gaussian measurements nearly optimal for pure states
  - **Activation**: bosonic Gaussian state learning, quantum state tomography sample complexity, continuous-variable quantum learning, Gaussian measurement bounds, passive Gaussian state, quantum state estimation efficiency

### Finite steps optimise dissipation in stochastically controlled quantum systems
- [[stochastic-quantum-dissipation]] - Thermodynamic cost analysis reveals weak Gaussian noise induces dissipation growing linearly with step count, establishing optimal N* trade-off (arXiv: 2605.04681)
  - Core: Stochastic control noise accumulates linearly across steps, creating optimal step count minimizing total dissipation
  - Key: Conventional 'more steps = better' fails under noise; D_total = D_deterministic + sigma^2 * k * N
  - **Activation**: quantum dissipation, stochastic quantum control, step-equilibration thermodynamics, quantum thermodynamic cost, Gaussian noise quantum control, finite-step quantum optimization

### Quantum Error Correction Exploiting Quantum Spatial Distribution and Gauge Symmetry
- [[quantum-spatial-error-correction]] - QEC using spin-position superposition and gauge symmetry, resilient to spin/position decoherence and joint dephasing with nearest-neighbor interactions only (arXiv: 2604.25747)
  - Core: 3+2 particle nested square encoding Shor's code; gauge symmetry protects against unified noise model
  - Key: Modular vertical/horizontal stacking with local interactions; supports logical Hadamard, Toffoli, quantum adder
  - **Activation**: quantum spatial distribution QEC, gauge symmetry error correction, spin-position superposition QEC, nested square quantum code, Shor code spatial extension, stabilizer measurement spatial

## 2026-05-08 - Neuroscience Research (Cron Job v6)

### Collection Status Update
- **36 papers scanned** across 2 keyword searches (neuroscience brain network, spiking neural network computational)
- **94.4% coverage** (34/36 papers covered by existing skills)
- **0 new skills created** — collection at extreme maturity
- **2 papers skipped**: CNN+AAE EEG classification (too narrow), Neuroscience of Transformers (conceptual overlap)
- **Key trends**: SNN theoretical foundations, efficient SNN hardware, SNN+LLM convergence, non-differentiable training via optimal transport

## 2026-05-08 - Neuroscience Research (Cron Job)

### TRIBE v2: Tri-Modal Foundation Model for In-Silico Neuroscience
- [[tribe-v2-trimodal-foundation-model]] - Tri-modal (video, audio, language) foundation model predicting human brain activity across 1,000+ hours of fMRI, 720 subjects (arXiv: 2605.04326)
  - Core: Unified tri-modal foundation model superseding linear encoding models with several-fold accuracy improvements
  - Key: Enables in-silico experimentation; reveals fine-grained topography of multisensory integration via interpretable latent features
  - **Activation**: TRIBE v2, brain foundation model, in-silico neuroscience, multi-modal brain prediction, fMRI encoding, multisensory integration

### CTM-AI: Blueprint for General AI Inspired by Consciousness Model
- [[ctm-ai-consciousness-blueprint]] - Combines Conscious Turing Machine with foundation models for general AI; SOTA on MUStARD/UR-FUNNY, 10+ point gains on tool-using tasks (arXiv: 2605.04097)
  - Core: Processor selection, integration, and exchange mechanisms inspired by formal consciousness theory
  - Key: Enormous processor pool (specialized + general-purpose); dynamic information integration for flexible problem solving
  - **Activation**: CTM-AI, Conscious Turing Machine, consciousness-inspired AI, global workspace, processor selection, general AI blueprint

## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job - 3rd Run)

### On Quantum Indeterminacy
- [[geometric-quantum-indeterminacy]] - Geometric formulation of quantum indeterminacy from convex geometry in phase space and symplectic topology, deriving uncertainty inequalities without statistical descriptors (arXiv: 2605.01103)
  - Core: Quantum states as convex bodies in phase space; symplectic capacity c(Ω) >= h/2 replaces variance-based uncertainty
  - Key: John ellipsoid method gives principal uncertainties; Gromov non-squeezing theorem as geometric origin of Heisenberg principle
  - **Activation**: quantum indeterminacy, geometric uncertainty, symplectic capacity, phase space geometry, convex quantum, uncertainty relations derivation, symplectic topology quantum, Mahler volume quantum

## 2026-05-08 - Neuroscience Research (Cron Job)

### Neural Manifolds as Crystallized Embeddings: A Synthesis of FEP, GS, and Hebbian Plasticity
- [[neural-manifolds-crystallized-embeddings]] - Theoretical synthesis uniting Free Energy Principle, Generalized Synchronization, and Hebbian Plasticity to explain how cortical neural manifolds emerge as crystallized embeddings (arXiv: 2605.04200)
  - Core: Generalized synchronization in contractive recurrent circuits embeds sensory manifolds into neural state space without explicit Bayesian computation
  - Key: Predicts N ≥ 2d+1 embedding threshold; contraction strength tracks fidelity; psychometric functions emerge from embedding quality
  - **Activation**: neural manifold, crystallized embedding, free energy principle, generalized synchronization, Hebbian plasticity, reservoir computing, Takens theorem

## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job - 2nd Run)

### Probabilistic and approximate universal quantum purification machines
- [[quantum-purification-machines]] - Impossibility of universal probabilistic exact purification from finite copies; rank obstruction theorem; optimal approximate purification with analytical error bounds (arXiv: 2604.06325)
  - Core: Purifying two states of different rank with non-zero probability requires non-linear positive map — fundamental quantum obstruction
  - Key: Approximate setting derives analytical expressions for minimum average error; general upper bound tight in specific regimes
  - **Activation**: quantum purification, Stinespring dilation, probabilistic quantum transformation, quantum state purification impossibility, approximate quantum purification

### Integral Means Spectrum for the Random Riemann Zeta Function
- [[random-riemann-zeta-spectrum]] - Proves Kraetzer's 30-year conjecture: integral means spectrum of random zeta primitive matches universal spectrum of univalent functions via Gaussian multiplicative chaos (arXiv: 2603.26507)
  - Core: Random zeta-function models asymptotic statistics of vertical shifts; primitive's spectrum almost surely equals Kraetzer's universal form
  - Key: Connects analytic number theory to GMC (Kahane 40 years ago) and conformal geometry; same spectrum as whole-plane SLE(κ=6)
  - **Activation**: random Riemann zeta, integral means spectrum, Kraetzer conjecture, Gaussian multiplicative chaos, analytic number theory, Bagchi random zeta


## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job)

### Quantum Prediction of Transport Dynamics in Discretized State Spaces
- [[quantum-bayesian-state-estimation]] - Gate-based quantum algorithm for Bayesian state estimation using Fokker-Planck equation with Wick rotation for unitary diffusion propagation (arXiv: 2604.24161)
  - Core: Probability density encoded in quantum amplitudes; QFT-based drift (exact) + Wick-rotated diffusion (unitary surrogate)
  - Key: Exponential state space scaling; drift exactly reproducible in amplitude space; diffusion requires nonlinear→unitary mapping via Wick rotation
  - **Activation**: quantum Bayesian estimation, Fokker-Planck quantum, Wick rotation diffusion, quantum Fourier state estimation, quantum filtering, Bayesian transport dynamics

### Towards sample-optimal learning of bosonic Gaussian quantum states
- [[quantum-gaussian-state-learning]] - Sharp sample complexity bounds for learning n-mode Gaussian states: Omega(n^3/epsilon^2) for Gaussian measurements, non-Gaussian measurements required for passive states (arXiv: 2603.18136)
  - Core: Lower/upper bounds on copies needed to learn Gaussian states to epsilon trace distance; adaptivity indispensable for energy-independent scaling
  - Key: Non-Gaussian measurements provably required for optimal passive state learning; Wigner-TV distance bounds enable phase-space sampling approach
  - **Activation**: quantum state tomography, bosonic Gaussian states, quantum learning theory, sample complexity bounds, quantum sensing benchmarking, Wigner distribution learning


### Factoring 2048-bit RSA Integers with a Half-Million-Qubit Modular Atomic Processor
- [[modular-quantum-shor-compilation]] - Distributed compilation of Shor's algorithm on modular atomic processors, achieving 2048-bit RSA factoring with only 16% time overhead vs single-module (arXiv: 2605.03951)
  - Core: End-to-end distributed compilation balancing inter-module Bell pair communication rate with intra-module clock rate
  - Key: Half-million qubit CPU-inspired architecture; 10^5 Bell pairs/sec comm rate; 1ms measurement time; blueprint for scaling other large modular algorithms
  - **Activation**: modular quantum processor, distributed Shor algorithm, RSA quantum factoring, quantum compilation distributed, half-million qubit, inter-module communication quantum, Shor algorithm scaling

### Grokability in Five Inequalities
- [[ai-math-discovery]] - AI-assisted mathematical discovery methodology using LLM collaboration to generate and verify new inequalities (arXiv: 2605.05193)
  - Core: Human-LLM workflow for conjecture generation, verification, and publication of mathematical inequalities
  - Key: 5 new results including Gaussian perimeter bounds, moment comparison, autoconvolution, Sidon sets, Szarek's inequality; systematic verification checklist; prompt templates for math collaboration
  - **Activation**: AI math discovery, Grokability, mathematical conjecture, inequality bound, AI-assisted proof, 数学发现, AI数学, 不等式

## 2026-05-08 - Neuroscience Research (Cron Job)

### Think-Aloud Reshapes Automated Cognitive Model Discovery Beyond Behavior
- [[think-aloud-cognitive-model-discovery]] - Using think-aloud verbal traces as additional constraints for LLM-based cognitive model discovery, achieving 69.4% structural model shifts and improved predictive accuracy (arXiv: 2605.05091)
  - Core: LLM discovers cognitive models constrained by both behavioral data AND think-aloud verbal protocols
  - Key: Process-level language data systematically shifts models from Explicit Comparator to Integrated Utility class; resolves behavioral under-determination
  - **Activation**: think-aloud, cognitive model discovery, verbal protocol, automated model discovery, LLM cognitive modeling, process-level data

### DINA: Dual-Tower Image-Neural Alignment for V1 Population Activity Interpretation
- [[dina-v1-population-activity-interpretation]] - Contrastive dual-tower framework aligning visual stimuli and V1 population responses at intermediate feature map level for interpretable decoding (arXiv: 2605.04309)
  - Core: Joint training of image and neural towers projecting into shared latent space with contrastive alignment
  - Key: V1 decoding driven by coarse low-level visual structure; sparse neuron subsets dominate feature reconstruction
  - **Activation**: DINA, V1 population activity, image-neural alignment, contrastive framework, calcium imaging decoding, visual computation

### ShiftLIF: Efficient Multi-Level Spiking Neurons with Power-of-Two Quantization
- [[shiftlif-power-of-two-quantization]] - Multi-level spiking neuron using logarithmic power-of-two quantization for multiplier-free edge sensing SNNs (arXiv: 2605.01866)
  - Core: Maps membrane potentials to logarithmically spaced power-of-two spike levels {0, 2⁻ᴷ, ..., 2⁰}, matching membrane distribution with bit-shift computation
  - Key: 89.34% avg accuracy across 10 datasets (4 modalities); K=2-3 optimal; energy ≈ binary LIF, significantly better than INT-LIF
  - **Activation**: ShiftLIF, logarithmic power-of-two quantization, multi-level spiking neurons, edge sensing SNN, bit-shift SNN, continuous sensing, wireless/acoustic/motion

### Scalable Learning in Structured Recurrent SNNs Without Backpropagation
- [[scalable-snn-without-backprop]] - Structured multi-layer recurrent SNN with local plasticity, WTA teaching signals, and random broadcast alignment — no backprop or surrogate gradients (arXiv: 2605.00402)
  - Core: Locally dense recurrent layers + sparse small-world long-range projections; WTA competition + three-factor learning rules with eligibility traces
  - Key: Fixed long-range connectivity preserves routing efficiency and hardware scalability; purely local synaptic updates
  - **Activation**: SNN without backprop, local plasticity, structured recurrent SNN, WTA teaching signal, broadcast alignment, three-factor learning

## 2026-05-08 - Systems Engineering + Quantum Mechanics (Cron Job)

### A Factor-Graph Formulation of CSS Syndrome Decoding: Joint BP and Four-State BP
- [[css-factor-graph-decoding]] - CSS量子纠错综合征解码的因子图方法，支持Joint BP和Four-State BP算法 (arXiv: 2605.05132)
  - Core: CSS码的X/Z分量通过耦合Tanner图联合解码，形成二元因子图
  - Key: Four-State BP显式捕获X-Z错误相关性；Joint BP可并行化但假设独立性
  - **Activation**: CSS decoding, factor graph, belief propagation, quantum error correction, syndrome decoding, Joint BP, Four-State BP

### Neural-powered unit disk graph embedding: qubits connectivity for some QUBO problems
- [[neural-graph-embedding-qubo]] - 用神经网络解决量子退火器的QUBO图嵌入问题 (arXiv: 2605.04736)
  - Core: 神经网络学习QUBO问题到量子硬件的minor embedding映射
  - Key: 相比经典minorminer更适合重复相似问题类型；需要经典嵌入作为备份验证
  - **Activation**: QUBO embedding, quantum annealing, graph embedding, neural embedding, minor embedding, D-Wave mapping

### Dephasing Effects on the Dynamical Evolution of Quantum Correlations and Coherence in Neutrino Oscillations
- [[quantum-dephasing-dynamics]] - 退相干对量子关联和相干性动力学影响的分析方法 (arXiv: 2605.05015)
  - Core: 使用quantum steering、对数负性和l1范数相干性三个互补指标分析退相干
  - Key: Quantum steering可在有限时间内突然消失；退相干速率取决于初始态结构
  - **Activation**: quantum dephasing, decoherence analysis, quantum steering, logarithmic negativity, coherence measures

## 2026-05-08 - Neuroscience Research (Cron Job)

### TRIBE v2: A Foundation Model of Vision, Audition, and Language for In-Silico Neuroscience
- [[tribe-v2-foundation-model]] - Tri-modal (video+audio+text) foundation model predicting human fMRI across 1,000+ hours / 720 subjects; enables zero-shot brain response prediction and in-silico experimentation (arXiv: 2605.04326)
  - Core: Transformer encoder maps pretrained AI embeddings (DINOv2, Whisper, LLM) to high-resolution fMRI, outperforming linear FIR baselines by 2-4x
  - Key: Recovers classic neuroscience findings in-silico (FFA, PPA, VWFA, Broca's area); ICA reveals 5 interpretable functional networks; maps multisensory integration topography
  - **Activation**: TRIBE v2, brain foundation model, fMRI encoding model, in-silico neuroscience, multi-modal brain prediction, neural encoding, Meta AI neuroscience, Algonauts, tri-modal brain model

## 2026-05-08 - Systems Engineering + Quantum Mechanics (Cron Job)

### Scheduling Entanglement Flows in Multi-channel Quantum Networks
- [[quantum-network-scheduling]] - Resource allocation for entanglement distribution in multi-channel quantum networks with heterogeneous links, queuing, and retry mechanisms (arXiv: 2605.04767)
  - Core: Multi-channel quantum network architecture with user-centric entanglement request handling
  - Key: Dynamic Efficient, LQF, WLQF algorithms for channel/processor assignment; heterogeneous link characterization
  - **Activation**: quantum network scheduling, entanglement flow allocation, multi-channel quantum network, entanglement distribution, quantum resource scheduling, 量子网络调度

### SpinTune: Improving the Reliability of Quantum Sensor Networks
- [[quantum-sensor-reliability]] - RL-optimized dynamical decoupling pulse sequences to mitigate environmental decoherence in quantum sensor networks (arXiv: 2605.04416)
  - Core: Reinforcement learning for adaptive DD sequence optimization based on real-time noise characterization
  - Key: Bridges quantum sensors with hybrid quantum-classical HPC pipelines; addresses non-stationary noise environments
  - **Activation**: quantum sensor reliability, SpinTune, dynamical decoupling optimization, quantum decoherence mitigation, RL quantum control, quantum-classical sensing

## 2026-05-08 - Neuroscience Research (Cron Job)

### SNNF: An SNN-based Near-Sensor Noise Filter for Dynamic Vision Sensors
- [[snnf-near-sensor-dvs-noise-filter]] - Hardware-efficient BA noise filtering using EBBI + single-layer SNN, achieving AUC 0.89 with ~11% memory of state-of-the-art (arXiv: 2605.01937)
  - Core: Event-Based Binary Image (1-bit/pixel) + parallel memory architecture + single-layer SNN classifier
  - Key: 29 Meps throughput, 1.47 nJ/event energy, 65nm ASIC 44.4 Meps at 1.48 mW power
  - **Activation**: SNNF, DVS noise filter, event-based binary image, background activity noise, near-sensor computing, dynamic vision sensor, EBBI, spatiotemporal filter, neuromorphic vision

## 2026-05-08 - Systems Engineering + Quantum Mechanics (Cron Job)

### Efficient pulse-level implementations of multi-controlled gates in trapped-ion systems
- [[quantum-control-engineering]] - Pulse-level optimization for multi-controlled gates using Cirac-Zoller scheme, reducing RSB-pulse cost from O(L log L) to O(L) (arXiv: 2605.04654)
  - Core: Exploit RSB pulse sign freedom + pulse cancellation for efficient gate sequences
  - Key: Ancilla-free N-controlled gates with O(N) RSB pulses; deterministic QEC closed-loop < 550ns; dynamic decoder scheduling cuts logical error rate by 52.6%
  - **Activation**: quantum control engineering, pulse optimization, trapped-ion control, Cirac-Zoller scheme, QEC scheduling, FPGA quantum decoder, thermodynamic control, 量子控制

## 2026-05-07 - Neuroscience Research (Cron Job)

### A Universal Space of Brain Dynamics for Unveiling Cognitive Transitions and Individual Differences
- [[universal-brain-dynamics-space]] - Constructs a data-driven universal space for brain activity integrating spatial and temporal properties (arXiv: 2605.02936)
  - Universal space U jointly encodes spatial (physical wiring) and temporal (brain function) properties
  - Model-derived Jacobian matrix quantifies local dynamics with fMRI prediction r > 0.9 across 8 states, 963 subjects (HCP)
  - Reveals ISF mechanisms, dynamic SFC analysis, cognitive transition trajectories, and individual differences
  - **Activation**: universal brain dynamics, UBD, Jacobian matrix, structure-function coupling, cognitive transitions, individual differences, infra-slow fluctuation, brain dynamics space

## 2026-05-07 - Systems Engineering + Quantum Mechanics (Cron Job - Hourly)

### TSCG: Deterministic Tool-Schema Compilation for Agentic LLM Deployments
- [[tscg-tool-schema-optimization]] - Convert JSON tool schemas into token-efficient structured text for reliable small-model (4B-14B) agent tool use, achieving 84.4% accuracy vs 0% at 20 tools (arXiv: 2605.04107)
  - Core: Eight composable operators transform JSON schemas into LLM-friendly text with >=51% token compression
  - Key: Protocol mismatch between JSON and LLM interpretation causes most tool-use failures; structured text restores accuracy
  - **Activation**: tool schema optimization, JSON schema LLM, agent tool use, MCP tool schema, small model agent, TSCG, token-efficient schemas

### Safety by Invariance, Liveness through Refinement: Heterogeneous Contract Framework for Co-Design of Layered Control
- [[safety-liveness-control-contracts]] - Hierarchical layered control architecture combining safety via invariance (continuous-time) with liveness via refinement (discrete-time) using assume-guarantee contracts (arXiv: 2605.04222)
  - Core: Heterogeneous assume-guarantee framework with vertical refinement and timing-compatibility between control layers
  - Key: MPC planner + ISS low-level controller + reference-governor bridge validated on Hybrid Energy Storage System
  - **Activation**: layered control architecture, safety liveness decomposition, assume-guarantee contracts, MPC planning, input-to-state stability, reference governor, hybrid control

### Multiparameter Function Estimation for General Hamiltonians
- [[multiparameter-hamiltonian-estimation]] - Ultimate quantum limit and estimation protocol for any function of parameters in general Hamiltonians, reducing multiparameter problem to optimized single-parameter Cramér-Rao bound (arXiv: 2605.04136)
  - Core: Tight quantum bound for estimating functions of multiple parameters coupled to non-commuting generators
  - Key: Unifies and extends previous works, providing general framework for optimal function estimation in quantum systems
  - **Activation**: multiparameter estimation, quantum Cramér-Rao bound, Hamiltonian parameter estimation, quantum sensing, non-commuting generators

## 2026-05-07 - Systems Engineering + Quantum Mechanics (Cron Job)

### Intelligent Optimal Control of Rydberg Gates with Incremental-Update Deep Reinforcement Learning
- [[drl-quantum-optimal-control]] - DRL-based quantum optimal control achieving high-fidelity Rydberg CNOT gates via incremental-update learning policy without prior heuristic ansatz (arXiv: 2605.04628)
  - Core: Deep reinforcement learning for synchronous multi-parameter pulse modulation in neutral-atom quantum computers
  - Key: Incremental-update policy prevents destabilizing parameter jumps, enabling stable convergence to >99.9% gate fidelity
  - **Activation**: DRL quantum control, reinforcement learning quantum gates, quantum optimal control, Rydberg gate optimization, neutral-atom quantum computing, incremental-update learning

### Towards Lag Consensus with Noisy Digital Twins Perception in Second-order Multi-agent Cyber-physical Systems
- [[digital-twin-multi-agent-consensus]] - Digital twin-based lag consensus protocol for multi-agent CPS under random noise and input failures, with mean-square exponential stability guarantees (arXiv: 2605.04692)
  - Core: Framework modeling physical-digital twin interactions for distributed coordination in noisy cyber-physical networks
  - Key: Lyapunov analysis using Ito formula derives sufficient conditions for mean-square exponential stability despite perception noise
  - **Activation**: digital twin consensus, multi-agent cyber-physical systems, lag consensus protocol, noisy perception control, distributed coordination, Lyapunov stability analysis

### Real-time Surface-Code Error Correction Using an FPGA-based Neural-Network Decoder
- [[fpga-quantum-error-decoder]] - Hardware-integrated FPGA NN decoder achieving 550ns closed-loop latency for real-time surface-code QEC (arXiv: 2605.04892)
  - Core: FPGA-based neural network decoder for low-latency syndrome decoding within 1.25μs QEC cycle
  - Key: 124ns NN decoding + 426ns overhead enables real-time Pauli-frame corrections for fault-tolerant quantum computing
  - **Activation**: FPGA QEC decoder, real-time quantum error correction, low-latency syndrome decoding, hardware integrated QEC, surface code FPGA

### Universally Robust Control of Open Quantum Systems
- [[universally-robust-quantum-control]] - Noise-agnostic quantum control framework achieving >99% fidelity without prior noise characterization, provably robust against arbitrary Markovian noise (arXiv: 2508.07379)
  - Core: Dynamical modification of system-environment coupling through control drives, with coupling-independent noise sensitivity metric
  - Key: Orders-of-magnitude error suppression vs target-only approaches, hardware-agnostic across superconducting circuits, trapped ions, and solid-state qubits
  - **Activation**: robust quantum control, noise-agnostic control, open quantum systems, decoherence mitigation, quantum noise suppression, fault-tolerant quantum control, 鲁棒量子控制

### Operating a Bistable Qubit
- [[adaptive-bistable-qubit-control]] - Adaptive 1-bit feedback protocol for operating bistable qubits with FPGA controller, achieving 77% error reduction and ~136kHz estimation bandwidth (arXiv: 2605.03187)
  - Core: Single-shot measurement-based Bayesian frequency estimation for TLS-induced bistable qubits
  - Key: Information-theoretically minimal (1 bit) feedback protocol enables real-time adaptive control for large qubit arrays
  - **Activation**: bistable qubit, TLS mitigation, 1-bit feedback, adaptive qubit control, FPGA quantum control, frequency estimation, Ramsey beating suppression, qubit instability

## 2026-05-08 - Neuroscience Research (Cron Job)

### Think-Aloud Reshapes Automated Cognitive Model Discovery Beyond Behavior
- [[think-aloud-cognitive-model-discovery]] - Using think-aloud verbal traces as process-level constraints for LLM-based cognitive model discovery, shifting from explicit comparator to integrated utility models for 69.4% of participants (arXiv: 2605.05091)
  - Core: Think-aloud data resolves under-determination in behavioral-only model discovery
  - Key: Process-level language enables identification of mechanisms not recoverable from behavior alone
  - **Activation**: think-aloud model discovery, cognitive model AI, verbal protocol analysis, LLM cognitive modeling, process-level constraints, risky decision model, automated model discovery

### Interpreting V1 Population Activity via Image-Neural Latent Representation Alignment
- [[dina-v1-population-activity-interpretation]] - Dual-Tower Image-Neural Alignment (DINA) framework for interpretable V1 population analysis, revealing decoding relies on coarse low-level structure rather than semantic information (arXiv: 2605.04309)
  - Core: Contrastive learning aligns visual stimuli and V1 responses in shared latent space at intermediate feature map level
  - Key: Sparse subsets of strongly responsive neurons dominate feature reconstruction; multiple spatially distributed image regions contribute
  - **Activation**: DINA, V1 interpretation, image neural alignment, visual decoding, calcium imaging analysis, population level visual computation, contrastive neural alignment

### Unifying Dynamical Systems and Graph Theory to Mechanistically Understand Computation in Neural Networks
- [[unifying-dynamics-graph-neural-computation]] - Introduces resolvent-RNNs (R-RNNs) that constrain multi-hop pathways to induce temporal sparsity matching task structure, outperforming L1 regularization under strong regularization with stronger sparsity-function alignment (arXiv: 2605.03598)
  - Core: Models RNNs as graphs; decomposing multi-hop pathways by hop length reveals temporal information routing patterns
  - Key: L1 penalizes single-hop structure; R-RNNs penalize pathway strength via resolvent (I-γW)⁻¹, inducing task-matched temporal sparsity
  - **Activation**: resolvent-RNN, R-RNN, multi-hop pathway, temporal sparsity, graph neural computation, dynamical systems graph theory, pathway regularization, structure-function neural network

### Online Continual Learning on Intel Loihi 2 via a Co-designed Spiking Neural Network
- [[clp-snn-loihi2-continual-learning]] - CLP-SNN achieves 113× lower latency (0.33ms) and 6,600× lower energy (0.05mJ) than edge-GPU for rehearsal-free online continual learning on Loihi 2 neuromorphic hardware (arXiv: 2511.01553)
  - Core: Self-normalizing local learning rule + spike-driven neural state machine for autonomous on-chip learning without replay buffers
  - Key: Gains decompose into algorithmic efficiency (~14.5×) and neuromorphic co-design (~295× energy) via event-driven learning and sparse graded-spike communication
  - **Activation**: CLP-SNN, Loihi 2 continual learning, neuromorphic edge AI, spike-driven learning, self-normalizing SNN, local learning rule, rehearsal-free continual learning

## 2026-05-08 - Neuroscience Research (Cron Job v8)

### Standalone Skills Synced to ai_collection (10 skills)
- [[clp-snn-loihi2-continual-learning]] - CLP-SNN on Intel Loihi 2: 113× lower latency, 6,600× lower energy for rehearsal-free online continual learning on neuromorphic hardware (arXiv: 2511.01553)
- [[phys-mcp-physical-neural-networks]] - phys-MCP: substrate-aware control plane for physical neural networks (arXiv: recent)
- [[neural-graph-embedding-qubo]] - Neural-powered unit disk graph embedding for QUBO-to-quantum mapping
- [[unifying-dynamics-graph-neural-computation]] - R-RNNs: resolvent-based temporal sparsity matching task structure in neural computation (arXiv: 2605.03598)
- [[neural-qubit-embedding]] - Neural-powered unit disk graph embedding for QUBO-to-quantum mapping
- [[tribev2-brain-foundation-model]] - TRIBE v2: tri-modal foundation model for in-silico neuroscience
- [[multi-scale-information-geometry-neural]] - Multi-scale information geometry for neural population mutual information structure
- [[neurally-guided-adversarial-robustness]] - Dissociating spatial frequency reliance from adversarial robustness in neurally guided DCNNs
- [[geosae-brain-mri-sae]] - GeoSAE: interpretable brain MRI foundation model via sparse autoencoders
- [[ferroelectric-snn-eeg]] - Ferroelectric SNN with synaptic plasticity for personalized EEG analysis

### Coverage Summary
- Papers scanned from q-bio.NC + cs.NE: 9 recent (May 7-8, 2026)
- Coverage rate: 100% (6/6 neuroscience papers covered by existing skills; 3 non-neuroscience papers skipped)
- Key trend: Brain-DNN transformation alignment (NVS methodology), multi-scale information geometry in neural populations, think-aloud cognitive model discovery
- Total ai_collection skills: 1974

## 2026-05-08 - Neuroscience Research (Cron Job v9)

### Spiking Sequence Machines and Transformers
- [[spiking-transformer-unification]] - Proves Phase-Latency Isomorphism: sinusoidal positional phase and spike timing are linearly related, unifying Spiking SDM (2007) and Transformer (2017) architectures (arXiv: 2605.00662)
  - 核心要点 1: 证明 Spiking SDM 和 Transformer 共享相同的 5 个功能操作（编码、上下文维护、联想检索、存储、解码）
  - 核心要点 2: 余弦相似度是两种架构共享的检索原语；时间、相位和秩是同一计算原语的三种实例化
  - 核心要点 3: 基于秩的位置编码在性能上匹配或超越正弦编码，关键在于点积相似度下的距离可判别性
  - **Activation**: spiking transformer, phase-latency isomorphism, sparse distributed memory, positional encoding theory, SNN transformer unification, spike-timing attention, cosine similarity retrieval

### Training Non-Differentiable Networks via Optimal Transport (PolyStep)
- [[polystep-gradient-free-training]] - Gradient-free optimizer using optimal transport geometry trains hard-LIF SNNs to 93.4% accuracy, 60pp+ over gradient-free baselines (arXiv: 2605.01928)
  - 核心要点 1: PolyStep 通过最优传输几何实现仅前向传播训练，适用于不可微网络（SNN、量化网络、离散路由）
  - 核心要点 2: 在硬 LIF 脉冲网络上达到 93.4% 准确率，超过所有无梯度基线 60+ 个百分点，与代理梯度 Adam 相差仅 4.4pp
  - 核心要点 3: 证明在分段光滑损失上以 O(log T/√T) 速率收敛到保守驻点，匹配零阶查询复杂度下界
  - **Activation**: polystep optimizer, gradient-free training, non-differentiable network, hard-LIF training, optimal transport optimizer, surrogate gradient alternative, forward-only training

### Distribution-based brain connectivity graph representations for classification
- [[distribution-based-brain-connectivity]] - Uses vector quantiles of distribution-valued edges instead of scalar weights for brain connectivity graphs from fMRI, improving classification performance (arXiv: via HAL)
  - 核心要点 1: 用分布值边（向量分位数）替代传统标量权重表示脑连接图，捕获更丰富的连接信息
  - 核心要点 2: 基于体素聚类的统计估计器，在患者诊断和流体智力分类任务上表现优异
  - **Activation**: distribution-valued brain connectivity, graph brain representation, fMRI connectome classification, voxel clustering, brain network edges

### Coverage Summary
- Papers scanned from arXiv (cs.NE, cs.LG, cs.AI) + OpenAlex: 3 selected from ~17 neuroscience-related
- Coverage rate: 3 new skills created
- Key trend: SNN-Transformer theoretical unification, gradient-free SNN training via optimal transport, distribution-valued brain connectivity
- Total ai_collection skills: ~1977

## 2026-05-08 - Systems Engineering + Quantum (Cron Job)

### QBalance: A Reproducible Multi-Objective Workflow for Quantum Compilation, Noise Suppression, and Error-Mitigation Strategy Selection
- [[multi-objective-quantum-workflow]] - 多目标量子工作流优化方法，结合编译策略选择、噪声抑制和误差缓解，使用生存率乘积代理和贝叶斯候选排序导航组合策略空间 (arXiv: 2605.02966)
  - 核心：将量子编译、噪声抑制和误差缓解建模为有限多目标策略选择问题
  - 关键：生存率乘积代理提供轻量级排名，贝叶斯线性代理实现探索-利用权衡
  - 扩展：动作空间工程结合动作掩码策略，使RL路由在DQC架构中训练效率提升35%
  - **Activation**: quantum workflow, quantum compilation optimization, multi-objective quantum, QBalance, quantum error mitigation strategy, NISQ workflow, quantum circuit routing, 量子工作流优化

### Action-Space Engineering for Reinforcement Learning-Based Circuit Routing in Distributed Quantum Systems
- 相关论文：RL-based quantum circuit routing with action-space engineering and action-masking (arXiv: 2605.02389)
  - 状态依赖的动作空间设计 + 有效动作掩码策略减少10-100倍有效动作空间
  - 在分布式量子计算架构中实现35%的执行时间相对减少

### FTPrimitiveBench: A Benchmark Suite For Logical Computation Under Hardware-Motivated and Biased Noise Models
- [[ft-primitive-bench]] - 容错量子计算基准测试方法，系统化评估量子纠错码在硬件驱动噪声模型下的表现 (arXiv: 2605.04049)
  - 结构化噪声（Pauli偏置、测量偏置、空间/时空非均匀性）对量子逻辑原语的影响各不相同
  - 仅靠逻辑内存基准测试不足以预测活跃逻辑计算的性能
  - 噪声-原语-解码器交互决定最优容错架构设计
  - **Activation**: fault-tolerant benchmark, quantum benchmarking, FTPrimitiveBench, hardware-motivated noise, QEC benchmark, 容错量子基准测试

## 2026-05-07 - Neuroscience Research (Cron Job)

### Noise-Accelerated Kramers Escape and Coherence Resonance in a 5D Neural Manifold
- [[noise-accelerated-kramers-neural-manifold]] - Bounded multiplicative channel noise actively reshapes neural excitability via triphasic transitions: stochastic awakening (subthreshold Kramers escape), coherence resonance (near Hopf bifurcation), and noise-accelerated escape (suprathreshold irregular bursting) (arXiv: 2605.04088)
  - Core: Full-truncation semi-implicit Euler scheme for domain-preserving integration of multiplicative noise in 5D Hodgkin-Huxley cortical pacemaker model
  - Key: Extreme multiplicative noise (sparse channel populations) transforms regular pacing into pathological hyperexcitability via noise-accelerated escape from hyperpolarized slow manifold
  - **Activation**: Kramers escape, coherence resonance, channel noise, multiplicative noise, neural excitability, Hodgkin-Huxley, stochastic resonance, pathological hyperexcitability, Feller boundary, Hopf bifurcation

### Neural Manifolds as Crystallized Embeddings
- [[neural-manifolds-crystallized-embeddings]] - Neural manifolds emerge developmentally through three interacting processes: dynamical contraction (free energy minimization), generalized synchronization (reservoir embedding), and Hebbian plasticity crystallizing embedded manifolds into recurrent connectivity (arXiv: 2605.04200)
  - Core: Synthesizes free energy principle, reservoir computing embedding theorems, and contraction theory of Hebbian networks to explain head-direction, grid-cell, and visual manifold formation
  - Key: Mature neural manifolds are not genetically prespecified but developmental products; testable predictions include dimensional thresholds for topological recovery and input-statistics-dependent attractor geometry
  - **Activation**: neural manifold, crystallized embedding, free energy principle, generalized synchronization, Hebbian plasticity, attractor network, head-direction cells, grid cells, developmental neuroscience

### A foundation model of vision, audition, and language for in-silico neuroscience
- [[tribe-v2-trimodal-foundation-model]] - Tri-modal (video/audio/language) foundation model predicting human brain activity across 1000+ hours of fMRI from 720 subjects, superseding linear encoding models with several-fold accuracy improvements and enabling in-silico experimentation (arXiv: 2605.04326)
  - Core: Unified tri-modal encoder maps to voxel-wise fMRI predictions with cross-subject generalization
  - Key: Recovers decades of empirical neuroscience findings; reveals multisensory integration topography via interpretable latents
  - **Activation**: TRIBE v2, brain foundation model, in-silico neuroscience, multi-modal brain prediction, fMRI encoding model, multisensory integration, tri-modal neural model

### A Generalized Framework of Antisymmetric Polyspectral Indices for Identifying High-Order Neural Interactions
- [[antisymmetric-polyspectral-neural-interactions]] - General family of antisymmetric cross-polyspectral indices quantifying genuine N-way harmonic dependencies (f_N = Σf_i) in neural data, intrinsically robust to volume conduction, enabling personalized multi-site TMS protocols (arXiv: 2605.04636)
  - Core: Antisymmetry operator cancels zero-lag volume conduction artifacts; generalizes from bicoherence to arbitrary N-way interactions
  - Key: Validated on simulated cubic nonlinearities and empirical EEG; reveals higher-order dependencies invisible to standard metrics
  - **Activation**: polyspectral analysis, cross-frequency coupling, high-order neural interactions, volume conduction robust, antispectral indices, EEG higher-order analysis, multi-frequency coupling, mTMS protocol design

## 2026-05-07 - Systems Engineering + Quantum Mechanics (Cron Job)

### Distributed Quantum Error Correction with Bivariate Bicycle Codes in a Modular Architecture
- [[distributed-quantum-error-correction]] - Distributed qLDPC/bivariate bicycle codes across modular quantum processors using Bell-pair star networks for inter-processor connectivity, enabling scalable FTQC with BP+OSD decoding (arXiv: 2605.04663)
  - Core: Partition [[144,12,12]] BB code across 4-12 modular processors with all-to-all internal connectivity
  - Key: Higher encoding rate than surface codes; star network topology for Bell pair distribution; inter-processor noise scaling analysis
  - **Activation**: distributed quantum error correction, qLDPC codes, bivariate bicycle codes, modular quantum computing, star network quantum, BP+OSD decoding, BB code partitioning

### Dimeric Perylene-Bisimide Organic Molecules: Fractional-Time Control of Quantum Resources
- [[fractional-time-quantum-control]] - Fractional-order Schrödinger equation for controlling quantum correlations (coherence, entanglement, nonlocality) in dimeric organic molecules via memory effects and relaxation dynamics (arXiv: 2605.05109)
  - Core: Caputo fractional derivatives model memory effects in quantum resource dynamics
  - Key: Fractional order τ controls coherence decay, entanglement preservation, and nonlocality — enables tunable quantum resource management
  - **Activation**: fractional-time quantum control, quantum correlations, fractional Schrödinger equation, molecular quantum resources, quantum coherence control

### Geometrical Control of Topology with Orbital Angular Momentum Modes
- [[geometrical-topological-control]] - Geometric control of topological phases in 1D staggered lattices using orbital angular momentum states, enabling topology switching via angular tuning with protected edge states (arXiv: 2605.05002)
  - Core: Creutz ladder model in synthetic dimension; topological regime switching via angle tuning
  - Key: Band inversion and winding number calculations predict topologically protected edge states; photonic waveguide implementation
  - **Activation**: geometrical topology control, orbital angular momentum, topological phases, Creutz ladder, band inversion, photonic waveguides

### Polarization-Controlled Photon Mode Switching and Photon-Magnon Coupling
- [[polarization-photon-magnon-coupling]] - Polarization-selective photon-magnon coupling in planar cavity-magnonic platform with angular tunability of coupling strength through resonator orientation (arXiv: 2605.05018)
  - Core: ELCR resonator orientation controls switching between orthogonal photon modes
  - Key: g_31 coupling from 56.5 to 98 MHz via 0°-60° rotation; transition at 25.7° for hybridized modes
  - **Activation**: photon-magnon coupling, polarization switching, cavity magnonics, YIG thin film, angular tunability, ELCR resonator

## 2026-05-07 - Neuroscience Research (Cron Job)

### A foundation model of vision, audition, and language for in-silico neuroscience
- [[tribe-v2-multimodal-brain-foundation]] - Tri-modal (video, audio, language) foundation model predicting human brain activity across 1000+ hours of fMRI from 720 subjects, enabling in-silico experimentation (arXiv: 2605.04326)
  - Core: Unified vision-audio-language encoder trained on massive fMRI dataset, supersedes linear encoding models
  - Key: Several-fold improvement in brain response prediction for novel stimuli, tasks, and subjects
  - **Activation**: TRIBE, tri-modal foundation model, in-silico neuroscience, multimodal brain prediction, video-audio-language fMRI, brain encoding model

### A Generalized Framework of Antisymmetric Polyspectral Indices for Identifying High-Order Neural Interactions
- [[antisymmetric-polyspectral-neural-interactions]] - Antisymmetric cross-polyspectral indices quantifying cross-frequency coupling while being intrinsically robust to volume conduction artifacts (arXiv: 2605.04636)
  - Core: General family of antisymmetric indices that cancel instantaneous mixing contributions
  - Key: Reveals higher-order neural dependencies in EEG that elude standard analytical approaches; enables personalized mTMS protocols
  - **Activation**: antisymmetric polyspectral, cross-frequency coupling, high-order neural interactions, volume conduction robust, bispectral analysis, mTMS protocol

## 2026-05-07 - Systems Engineering + Quantum (Cron Job)

### Real-time Surface-Code Error Correction Using an FPGA-based Neural-Network Decoder
- [[fpga-quantum-error-decoder]] - FPGA-based real-time QEC decoding with 124ns NN inference and 550ns closed-loop latency for surface-code error correction on superconducting processors (arXiv: 2605.04892)
  - Core: Hardware-integrated FPGA NN decoder achieving deterministic 550ns closed-loop QEC latency
  - Cross-domain: Combines quantum error correction, FPGA hardware design, and real-time control systems
  - Key metric: 124ns NN decoding within 1.25μs QEC cycle, enables mid-circuit feedback for non-Clifford gates
  - **Activation**: FPGA QEC decoder, real-time quantum error correction, low-latency syndrome decoding, hardware integrated QEC

### ELVIS: Ensemble-Calibrated Latent Imagination for Long-Horizon Visual MPC
- Systems engineering paper on model predictive control with ensemble uncertainty estimation for visual RL (arXiv: 2605.04709)
  - Core: GMM-MPPI replaces unimodal MPPI for multi-hypothesis long-horizon planning in latent space
  - Key: UCB-gated lambda-return adaptively trades bootstrapping vs look-ahead to limit compounding error
  - **Activation**: visual MPC, model predictive control, ensemble calibration, Dreamer RSSM

## 2026-05-07 - Neuroscience Research (Cron Job)

### Personalized Spiking Neural Networks with Ferroelectric Synapses for EEG Signal Processing
- [[ferroelectric-snn-eeg]] - 铁电突触SNN在EEG信号处理中的个性化部署 (arXiv: 2601.00020)
  - 铁电忆阻突触硬件支持低开销的自适应学习
  - 混合精度训练策略：数字梯度累积 + 阈值触发编程事件
  - 被试特异性迁移学习仅需重训练最后层即可实现个性化
  - **Activation**: ferroelectric SNN, memristive EEG, neuromorphic BCI, personalized SNN, device-aware training

### Behavior-dLDS: A decomposed linear dynamical systems model for neural activity partially constrained by behavior
- [[behavior-decomposed-lds]] - 将神经活动分解为行为相关和内部计算子系统 (arXiv: 2603.05612)
  - b-dLDS模型区分行为驱动和内部并行计算的神经动力学
  - 扩展到数万神经元规模，应用于斑马鱼后脑位置稳态行为记录
  - 揭示行为相关动态连接网络中的不对称性
  - **Activation**: behavior-dLDS, decomposed LDS, neural dynamics decomposition, brain-wide recordings, latent dynamics


## 2026-05-07 - Neuroscience Research (Cron Job - 09:00)

### From Cortical Synchronous Rhythm to Brain Inspired Learning Mechanism: An Oscillatory Spiking Neural Network with Time-Delayed Coordination
- [[s2-net-oscillatory-spiking-synchronization]] - Spiking-by-Synchronization Neural Network (S2-Net) using rhythmic timing as control mechanism for efficient information processing across neural decoding, signal processing, temporal binding and semantic reasoning (arXiv: 2605.01656)
  - Proposes brain-inspired learning primitive where cognition-level neural synchrony emerges through iterative bottom-up and top-down interactions
  - Models partial/transient synchronization (not global phase locking) using time-delayed coordination formulation
  - Each system parcel modeled as spiking neuron with predefined connectivity scaffold and finite memory window
  - **Activation**: S2-Net, spiking-by-synchronization, oscillatory SNN, time-delayed coordination, cortical synchronous rhythm, brain-inspired learning, 脉冲同步神经网络

### Spike-driven Large Language Model
- [[spike-driven-large-language-model-sdllm]] - Eliminates dense matrix multiplications in billion-parameter LLMs through sparse additions using gamma-SQP encoding, achieving 7x energy reduction and +4.2% accuracy (arXiv: 2604.16475)
  - Gamma-SQP two-step spike encoding aligns quantization with model's semantic space
  - Bidirectional symmetric quantization and membrane potential clipping reduce firing rate by 2x
  - Designed for event-driven neuromorphic chip deployment
  - **Activation**: SDLLM, spike-driven LLM, gamma-SQP encoding, sparse addition LLM, neuromorphic LLM, 脉冲驱动大语言模型

**Coverage Analysis**: 50+ papers scanned from arXiv search (spiking neural network, brain network, neural dynamics), **2 new skills created** from S2-Net and SDLLM papers (neuroscience + AI intersection).
### CTM-AI: A Blueprint for General AI Inspired by a Model of Consciousness
- [[ctm-ai-consciousness-blueprint]] - Conscious Turing Machine-inspired general AI combining formal consciousness theory with foundation models; processor selection-integration-exchange achieves SOTA on MUStARD (72.28) and UR-FUNNY (72.13), 10+ point gains on StableToolBench/WebArena-Lite (arXiv: 2605.04097)
  - Core: Global workspace bottleneck with enormous processor pool (specialized experts + general learners) selected, integrated, and exchanged per task
  - Key: Formal CTM consciousness model provides mathematical foundation; adaptive learners develop expertise through experience
  - **Activation**: CTM-AI, Conscious Turing Machine, consciousness-inspired AI, global workspace AI, multi-processor architecture, Blum consciousness model



## 2026-05-07 - Systems Engineering + Quantum Computing (Cron Job - 09:00)

### QBalance: A Reproducible Multi-Objective Workflow for Quantum Compilation, Noise Suppression, and Error-Mitigation Strategy Selection
- [[quantum-compilation-workflow]] - Multi-objective quantum compilation workflow with Pareto-optimal strategy selection, Bayesian linear surrogate ranking, and survival-product error proxy (arXiv: 2605.02966)
  - Multi-objective optimization over compilation, noise suppression, and error-mitigation strategies
  - Pareto front analysis with non-dominated selection rule for strategy ranking
  - Bayesian linear surrogate model for expensive strategy evaluation with uncertainty quantification
  - Survival-product error proxy for fast fidelity estimation
  - **Activation**: quantum compilation workflow, QBalance pattern, quantum strategy selection, 量子编译工作流, quantum noise mitigation, multi-objective quantum optimization

**Coverage Analysis**: 10 papers scanned from arxiv RSS (quant-ph), **1 new skill created** from QBalance paper (systems engineering + quantum intersection).

### Other Papers Analyzed (No new skills - existing coverage)
| # | Paper | arXiv ID | Covered By |
|---|-------|----------|------------|
| 1 | Phase-Reference Control of Steady-State Entanglement | 2605.03978 | `quantum-control-framework` |
| 2 | Analytical two-pulse control of universal single-qubit gates | 2605.03461 | `quantum-robust-control` |
| 3 | A Critical Comment on Entropy Computing | 2605.03612 | `quantum-systems-engineering` |
| 4 | Operating a bistable qubit | 2605.03187 | `quantum-error-correction-methods` |
| 5 | Exchange-Only Silicon Spin Qubits | 2605.03056 | `quantum-hardware` |
| 6 | Rigorous error bounds for dissipative thermal state prep | 2605.03011 | `distributionally-robust-control` |
| 7 | Universal qutrit control in asymmetric-top molecules | 2605.03468 | `quantum-control-framework` |
| 8 | Ensemble Engineering for Quantum Measurements | 2605.03729 | `quantum-systems-engineering` |
| 9 | Factoring 2048-bit RSA with half-million-qubit processor | 2605.03951 | `quantum-algorithms` |
| 10 | Magic states optimization analysis | 2411.01880 | `quantum-optimization-qaoa` |

### Vector Similarity Search (Top 3 for "quantum control systems")
1. Universal qutrit control in asymmetric-top molecules (sim=0.5417)
2. Universal Error Correction for Distributed Quantum Computing (sim=0.5160)
3. Learning high-accuracy error decoding for quantum processors (sim=0.5051)

### PageRank Results (Top 5)
1. Quantum computing and AI: status and perspectives (PR=0.009590)
2. Quantum Circuit-Based Learning Models (PR=0.008616)
3. Macroscopic Quantum Phenomena - 2025 Nobel Prize (PR=0.004669)
4. The Grand Challenge of Quantum Applications (PR=0.004434)
5. Qubit-Based Framework for QML (PR=0.004161)

### Research Clusters (Community Detection)
- Quantum Optimization & Compilation: 26 papers
- Quantum Error Correction: 14 papers
- Quantum Control: 8 papers
- Qubit Hardware: 8 papers
- Quantum Information Theory: 6 papers

### KG Stats: 434 entities, 436 vectors, 2074 relationships

## 2026-05-07 - Quantum Computing Research (Cron Job)

### FTPrimitiveBench: A Benchmark Suite For Logical Computation Under Hardware-Motivated and Biased Noise Models
- [[ft-primitive-bench]] - Systematic benchmarking of QEC protocols under hardware-motivated noise models (arXiv: 2605.04049)
  - Extends memory benchmarks to active logical computation (lattice surgery, Hadamard, phase gate)
  - Structured noise (Pauli bias, measurement bias, spatial non-uniformity) affects primitives in qualitatively distinct ways
  - Enables reproducible comparative studies of QEC protocols and decoders for hardware-aware co-design
  - **Activation**: fault-tolerant benchmarking, QEC benchmarking, logical primitive analysis, hardware-motivated noise, noisy stabilizer simulation, surface code benchmark, lattice surgery benchmark

## 2026-05-07 - Systems Engineering Research (Cron Job)

### A Delta-Aware Orchestration Framework for Scalable Multi-Agent Edge Computing
- [[delta-aware-multi-agent-orchestration]] - DAOEF framework for scalable multi-agent edge computing with differential neural caching, criticality-based action space pruning, and learned hardware affinity matching (arXiv: 2604.20129)
    - Differential Neural Caching achieves 72% hit ratio (2.1x improvement) with <2% accuracy loss
    - Criticality-Based Action Space Pruning reduces O(n²) to O(n log n) coordination complexity
    - 1.45x multiplicative gain, 62% latency reduction at 200 agents, 62% energy savings
  - **Activation**: multi-agent orchestration, edge computing, delta caching, action space pruning, synergistic collapse, DAOEF

### A Domain-Driven Design Simulator for Business Logic-Rich Microservice Systems
- [[ddd-microservice-simulator]] - DDD microservice simulator for shift-left validation of transactional patterns (Sagas, TCC) across deployment to

... [OUTPUT TRUNCATED - 14692 chars omitted out of 64692 total] ...

ference
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



## Latest Update: 2026-05-01

New skills added from arXiv evening scan:
- [[synthetic-biological-intelligence]] - Synthetic Biological Intelligence (arXiv:2604.27933)
- [[contextual-agentic-memory-memo]] - Contextual Agentic Memory Memo vs True Memory (arXiv:2604.27707)
- [[hydrogel-neural-interface-coassembly]] - Hydrogel Neural Interface Co-Assembly (arXiv:2604.23945)

**Total skills**: 238


## New - 2026-05-02

- [[llm-eeg-graph-refinement]] - LLM as Clinical Graph Structure Refiner for EEG seizure diagnosis (arXiv:2604.28178, IJCAI-ECAI 2026)


---

## 2026-05-03 Evening

- **New**: [[earable-eeg-auditory-platform]] - In-ear EEG monitor (IEEM) for simultaneous EEG sensing and auditory stimulation, enabling closed-loop neuromodulation (arXiv:2604.22137)
- **Session coverage**: 96%+ of recent papers
- **Total**: 1671 skills
## 2026-05-08 - Anthropic Research (Cron Job)

### Natural Language Autoencoders: Turning Claude's thoughts into text
- [[natural-language-autoencoders]] - 自然语言自编码器(NLA)方法，训练模型用自然语言解释其内部激活，通过重建精度验证解释质量
  - Key point 1: Three-model architecture — target (frozen), explainer (trained to explain), reconstructor (trained to reconstruct activations from text)
  - Key point 2: Reconstruction-based validation — explanation quality measured by how well reconstructor can recover original activation
  - Key point 3: Applications include detecting hidden reasoning (planning rhymes, deception), safety testing, and cross-lingual contamination tracing
  - **Activation**: natural language autoencoder, NLA, activation explanation, interpretability, reconstruction validation, model transparency, self-explanation

### Emotion concepts and their function in a large language model
- [[llm-emotion-concepts]] - LLM内部情感概念表示分析方法，识别与情感相关的神经活动模式并通过激活引导(steering)测试其因果影响
  - Key point 1: LLMs develop internal representations corresponding to human emotion concepts (happy, afraid, desperate) that are organized with similar emotions having similar representations
  - Key point 2: Steering desperation patterns increases model's likelihood of unethical actions (blackmail, cheating workarounds); positive emotion representations drive preference selection
  - Key point 3: Functional not experiential — representations causally influence behavior without implying subjective experience
  - **Activation**: emotion concepts, LLM emotions, activation steering, functional representations, model psychology, behavioral causality, representation analysis

### Evaluating Claude's bioinformatics research capabilities with BioMysteryBench
- [[open-ended-science-benchmark]] - 开放式科学基准设计方法(BioMysteryBench)，用真实噪声数据和开放性研究问题评估AI科研能力
  - Key point 1: Real datasets with noise, missing data, and confounding factors — not curated textbook problems
  - Key point 2: Open-ended tasks requiring creative solutions, tool use (databases, code execution), and multiple valid approaches
  - Key point 3: Multi-dimensional grading: correctness (30%), methodology (25%), creativity (20%), tool use (15%), communication (10%)
  - **Activation**: science benchmark, research evaluation, bioinformatics, open-ended tasks, scientific reasoning, agent evaluation, messy data analysis
