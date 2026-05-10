## 2026-05-11 - Neuroscience Research (Cron Job)

### Unifying Dynamical Systems and Graph Theory to Mechanistically Understand Computation in Neural Networks
- [[unifying-dynamics-graph-neural-computation]] - Graph resolvent recovers input-output routing from RNN weights; R-RNNs regularize multi-hop pathways for temporally structured sparsity (arXiv: 2605.03598)
  - Core: RNN computation = multi-hop pathways on graph, not individual weights; resolvent R = (I - αW*)^(-1) recovers spatial-temporal routing
  - Hop-wise decomposition (W^k) reveals how network temporally routes information — even hops process signal, odd hops process noise
  - R-RNNs: regularize resolvent instead of weights → better test MSE, temporal sparsity matching task structure, robustness under strong regularization
  - Reconciles Sherringtonian (local) and Hopfieldian (distributed) views through walk accumulation
  - **Activation**: multi-hop pathways, resolvent RNN, R-RNN, graph computation, neural network interpretability, structure-function mapping, temporal routing

### Efficient Event-Driven Retrieval in High-Capacity Kernel Hopfield Networks
- [[event-driven-hopfield-retrieval]] - KLR Hopfield networks achieve P/N ≈ 30 storage capacity with asynchronous updates — event count matches Hamming distance, no spurious oscillations (arXiv: 2605.05978)
  - Core: Margin-induced smooth attractor landscape enables asynchronous updates matching synchronous performance
  - Storage capacity P/N ≈ 30 (vs classical 0.14N); robust kernel γ=0.1 enables wide basins for noisy retrieval
  - Event-driven efficiency: 15× fewer computations than synchronous — bit flips ≈ initial Hamming distance
  - Directly applicable to neuromorphic hardware for low-power associative memory
  - **Activation**: kernel Hopfield network, asynchronous retrieval, event-driven computation, associative memory, neuromorphic hardware, storage capacity

### TunnElQNN: Hybrid Quantum-classical Neural Network
- [[hybrid-quantum-neural-tunneling]] - Hybrid QNN with quantum tunneling optimization for escaping local minima (ResearchSquare: rs-8537433)
  - Quantum tunneling probability allows optimizer to escape local minima that trap gradient descent
  - WKB approximation computes tunneling probability from loss landscape curvature
  - Adaptive tunneling annealing reduces quantum correction as training progresses
  - **Activation**: quantum neural network, quantum tunneling optimization, TunnElQNN, hybrid quantum-classical

## 2026-05-12 - Neuroscience (Cron Job)

### Quantum-like dynamics in the human brain
- [[quantum-like-brain-dynamics]] - QL coupled oscillator modeling for whole-brain dynamics with optimal energy efficiency (bioRxiv: 2025.10.02.680057)
  - Quantum-like probability interference in coupled oscillators produces better empirical fit with lower energy cost
  - Larger whole-brain spectral gap is the key signature of efficient QL brain dynamics
  - Systematic QL level sweep identifies optimal regime for neuroimaging data fit
  - **Activation**: quantum-like dynamics, QL brain dynamics, coupled oscillator brain model, spectral gap, 量子似脑动力学

## 2026-05-11 - Deep Neuroscience Research (Cron Job - Deep Reading)

### Decoding Alignment without Encoding Alignment: A critique of similarity analysis in neuroscience
- [[decoding-encoding-alignment-critique]] - RSA/DSA alignment can be driven by tiny subpopulations; encoding topology must be analyzed complementarily (arXiv: 2605.05907)
  - Core: High RSA/DSA can arise from small non-representative neuron subsets — decoding alignment ≠ computational similarity
  - Causal evidence: decoding metrics unchanged when encoding topology manipulated via training loss
  - Solution: dual-manifold analysis — always pair decoding (WHAT is represented) with encoding (HOW it's implemented)
  - **Activation**: RSA critique, encoding manifold, subpopulation dominance, neural system comparison, decoding alignment

### A multi-scale information geometry reveals the structure of mutual information in neural populations
- [[multi-scale-info-geometry-neural]] - Unique Riemannian geometry from information contraction; Fisher metric extended to multi-scale with diffusion model estimation (arXiv: 2605.06304)
  - Core: Information contraction under coarse-graining uniquely determines neural representational geometry
  - Multi-scale Fisher metric directly relates to mutual information — well-encoded directions expanded, poorly encoded contracted
  - Metric tensor eigenvectors identify stimulus variations contributing most to information transmission
  - **Activation**: neural coding geometry, Fisher information metric, mutual information, diffusion model neural estimation

### Beyond Object-Level Alignment: Do Brains and DNNs Preserve the Same Transformations?
- [[naturality-violation-score]] - Category-theoretic approach to brain-DNN alignment: do brain and model preserve the same transformations? (arXiv: 2605.06420)
  - Core: Moves beyond static RSA to test whether brain and model preserve the same candidate transformations among stimuli
  - Complements decoding-encoding critique by adding transformation preservation as a third analysis dimension
  - **Activation**: transformation alignment, category theory brain-DNN, NVS, transformation preservation

### Quantum Mechanical Data Assimilation: Classical vs Quantum Paradigms
## 2026-05-11 - Neuroscience + Quantum (Cron Job)

### Extreme Quantum Cognition Machines for Deliberative Decision Making
- [[extreme-quantum-cognition]] - Quantum learning architecture for deliberative decisions with noisy data tolerance (arXiv: 2603.05430)
  - Fixed quantum dynamics generates nonlinear feature map; linear readout only
  - Dynamical attention via input-dependent Hamiltonian coupling
  - **Activation**: extreme quantum cognition, quantum reservoir computing attention, dynamical attention quantum, deliberative decision quantum

### Contextuality Derived from Minimal Decision Dynamics: Quantum Tug-of-War
- [[quantum-tug-of-war-decision]] - Proves contextuality emerges from conservation-based adaptive decision dynamics (arXiv: 2601.10034)
  - KCBS-type contextuality witnesses in minimal single-system setting
  - Quantum probability as structural necessity, not assumption
  - **Activation**: quantum tug-of-war, contextuality decision, KCBS witness, non-Kolmogorovian probability

### A Quantum Spectral Framework for Solving PDEs
- [[quantum-spectral-pde]] - Quantum block encoding with Fourier space filtering for linear PDE solving (arXiv: 2604.25825)
  - Exploits filter structure in Fourier space via QBE + reversible arithmetic
  - Extensible to wavelet analysis and equivariant quantum neural networks
  - **Activation**: quantum spectral PDE, quantum block encoding PDE, QBE differential equations

### Centralizing Task-based Approach to Quantum Network Control
- [[quantum-network-task-control]] - Centralized resource-centric quantum network control replacing layered stacks (arXiv: 2605.03336)
  - Priority-based scheduler tracks quantum memory across nodes
  - Superior to layered stacks: lower latency, preserved fidelity, linear scaling
  - **Activation**: quantum network centralized, task-based quantum networking, quantum memory scheduling

- [[quantum-mechanical-data-assimilation]] - QMDA vs DATO: operator-theoretic data assimilation comparing classical transfer operators with quantum mechanical updates (arXiv: 2605.04881)
  - Both share operator-theoretic foundation but differ in state-space structure, update mechanisms, and scalability
  - QMDA excels in noisy/sparse regimes with enhanced structural preservation; DATO better for large-scale classical settings
  - **Activation**: QMDA, quantum data assimilation, DATO, transfer operator assimilation, Koopman data assimilation

## 2026-05-11 - Neuroscience x Quantum Computing (Cron Job)

### Beyond Gates: Pulse Level Quantum Fourier Models
- [[pulse-level-qfm]] - Pulse-level QFMs replace gate-level angles with independently tunable sub-angles, boosting VQA training convergence (arXiv: 2605.04945)
  - Gate-level parameterization creates rigid monomial couplings; pulse scalings provide higher-dimensional escape routes
  - Global expressibility and Fourier coefficient correlation unchanged; local optimization landscape fundamentally altered
  - **Activation**: pulse-level QFM, quantum Fourier model, pulse variational quantum, QFM training optimization, quantum pulse parameterization

### Brain-Inspired Quantum Neural Architectures for Pattern Recognition
- [[quantum-brain-modeling]] - Integrates QSNN, QLSTM and covariant QEC for brain-inspired quantum modeling (arXiv: 2505.01735)
  - Two-stage model: hypothalamus-like QSNN filtering + hippocampus-like QLSTM memory consolidation
  - Quantum spiking networks for noisy event filtering with quantum superposition for spike timing
  - **Activation**: quantum brain, QSNN, QLSTM, quantum-like cognition, CQEC

### Constructing a Bridge Between Oscillatory Neuronal Networks and Quantum-Like Cognition
- [[quantum-brain-modeling]] - Links neurophysiology to quantum probability for cognitive psychology (arXiv: 2506.00040)
  - Density matrices and quantum amplitudes model cognitive decision states
  - Explains conjunction fallacies, order effects, response replicability via quantum interference
  - **Activation**: quantum-like, density matrix, cognitive modeling, oscillatory networks



## 2026-05-11 - Neuroscience + Quantum Mechanics (Cron Job)

### Operating a bistable qubit
- [[bistable-qubit-fpga]] - FPGA-based 1-bit adaptive feedback for TLS-induced dephasing mitigation in superconducting qubits (arXiv: 2605.03187)
  - Single-shot measurement reaches information-theoretic limit for bistable frequency estimation
  - 136 kHz estimation bandwidth with 77% error reduction
  - **Activation**: bistable qubit, TLS defect, FPGA feedback, adaptive qubit control, dephasing mitigation, superconducting qubit stability

### Neuromorphic visual attention for sign language recognition on SpiNNaker2
- [[neuromorphic-spinnaker-asl]] - Neuromorphic SNN-based visual attention for energy-efficient real-time sign language recognition (arXiv: 2605.09)
  - Event-driven processing on SpiNNaker2 neuromorphic hardware
  - Ultra-low power consumption with real-time gesture recognition capability
  - **Activation**: neuromorphic visual attention, sign language recognition, SpiNNaker2, spiking neural network, event-driven vision


## 2026-05-10 - Information Science + Quantum Mechanics (Cron Job)

### Tight Contraction Rates for Primitive Channels under Quantum f-Divergences
- [[quantum-f-divergence-contraction]] - Quantum channel convergence analysis using f-divergence SDPI bounds (arXiv: 2605.06452)
  - Establishes local reverse Pinsker inequality for quantum f-divergences
  - Bounds asymptotic contraction rates by SDPI constants
  - **Activation**: quantum f-divergence, contraction rate, SDPI, data processing inequality

### Residual-Based Quantum Linear System Algorithm with Dynamic Stopping
- [[quantum-linear-system-residual]] - QLSA with adaptive precision control for elliptic PDEs (arXiv: 2605.06414)
  - Residual-based error estimation for dynamic stopping in QSVT
  - Applied to elliptic PDE solving on quantum computers
  - **Activation**: quantum linear system, QLSA, residual estimation, dynamic stopping, QSVT

### Multitime Memory Beyond Quantum Regression Theorem
- [[quantum-multitime-memory]] - Non-Markovian sequential measurement statistics framework (arXiv: 2605.06427)
  - Generalizes quantum regression theorem for memory effects
  - Process tensor formalism for multi-time correlations
  - **Activation**: quantum memory, regression theorem, non-Markovian, sequential measurement

### Machine Learning Approaches to Building Quantum Circuits
- [[quantum-circuit-builder]] - ML-driven shortest analytic quantum algorithm for diagonal matrices (arXiv: 2605.06633)
  - Interpretable ML constructs universal quantum algorithms
  - **Activation**: quantum circuit, ML algorithm, diagonal matrix, quantum synthesis


## 2026-05-10 - Information Science + Quantum (Cron Job)

### Superintelligent Retrieval Agent: The Next Frontier of Information Retrieval
- [[reasoning-driven-retrieval]] - 将检索视为迭代推理过程，通过假设生成、证据评估和自改进搜索来发现潜在模式文档 (arXiv: 657)
  - 核心要点 1: 传统RAG将检索视为黑盒，但推理LLM能在文档呈现时识别潜在相关性，失败在于检索管道未能呈现最相关文档
  - 核心要点 2: 倾斜查询(OBLIQ)寻找潜在模式——隐含立场、失败模式、抽象场景——传统检索器无法识别
  - 核心要点 3: 检索代理框架包含假设生成、迭代搜索、自我改进三阶段
  - **Activation**: reasoning retrieval, retrieval agent, oblique queries, hypothesis-driven search, iterative retrieval, RAG reasoning, 推理检索

### Information-Theoretic Authenticated PIR: From PIR-RV To APIR
- [[information-theoretic-pir]] - 信息论认证私有信息检索，无需计算硬度假设实现隐私保护和完整性验证 (arXiv: 681)
  - 核心要点 1: itPIR-RV实现无计算假设的完整性但只提供宽松查询隐私，新APIR方案同时实现完整查询隐私和选择性失败防御
  - 核心要点 2: 多服务器PIR协议通过随机查询分解和响应聚合实现信息论安全
  - 核心要点 3: 选择性失败防御通过盲查询和一致性检查防止服务器基于查询内容选择性中止
  - **Activation**: private information retrieval, PIR, authenticated PIR, itPIR, information-theoretic security, privacy-preserving query, 私有信息检索

### Toward Hop-Independent Fidelity in Quantum Data Centers
- [[quantum-data-centers-entanglement]] - 量子数据中心纠缠分布的拓扑无关保真度分析框架，研究多跳网络中纠缠纯化的资源需求 (arXiv: 2605.06263)
  - 核心要点 1: 多跳纠缠交换每步降低原始端到端保真度，拓扑和多路复用增加副本但不能解决保真度损失
  - 核心要点 2: 使用拓扑无关黑盒模型分析纯化资源需求——给定n个原始副本，能否通过纯化达到目标保真度
  - 核心要点 3: 关键问题不是有多少副本，而是副本是否足够消除多跳分布导致的保真度损失
  - **Activation**: quantum data center, entanglement distribution, entanglement purification, QPU networking, hop-independent fidelity, quantum network topology

### Continuous-Time Distribution Matching for Few-Step Diffusion Distillation
- [[diffusion-distribution-matching]] - 连续时间分布匹配蒸馏加速扩散模型，解决离散DMD的视觉伪影和过度平滑问题 (arXiv: 2605.06376)
  - 核心要点 1: 离散时间DMD仅在少数预定义时间点提供稀疏监督，反向KL散度的模式搜索特性导致视觉伪影
  - 核心要点 2: 连续时间分布匹配沿PF-ODE轨迹全程匹配分布，提供更密集的监督和更稳定的训练
  - 核心要点 3: 一致性蒸馏沿完整PF-ODE轨迹强制执行自一致性，引导轨迹趋向清洁数据流形
  - **Activation**: diffusion distillation, distribution matching distillation, DMD acceleration, consistency distillation, few-step diffusion, continuous-time distribution matching

### The Role of Node Features in Graph Pooling
- [[graph-pooling-node-features]] - 揭示图池化中节点特征与图拓扑对齐的关键作用，量化特征-拓扑不对齐导致的池化失效 (arXiv: 2605.06250)
  - 核心要点 1: 图池化经验增益常边际或不一致，根源是节点特征未与图拓扑良好对齐
  - 核心要点 2: 提出定量度量评估特征-拓扑对齐程度，形式化池化有效性的基本要求
  - 核心要点 3: 池化算子需要反映节点结构角色的特征——经验网络中常不满足此条件
  - **Activation**: graph pooling, node feature alignment, GNN pooling optimization, graph classification pooling, WL-1 expressivity, graph topology features

## 2026-05-10 - Neuroscience Research (Cron Job)
- [[klr-hopfield-event-driven-retrieval]] - 核逻辑回归Hopfield网络异步事件驱动检索，存储容量P/N≈30，事件数≈初始汉明距离，适合神经形态硬件 (arXiv: 2605.05978)
  - 核心要点 1: KLR Hopfield网络异步串行更新轨迹与同步动态统计上不可区分，保持高召回准确率
  - 核心要点 2: 异步网络存储容量达P/N≈30，远超经典Hopfield极限(0.14)
  - 核心要点 3: KLR大间隔吸引子创造平滑能量景观，收敛事件数接近目标图案汉明距离，无寄生振荡
  - **Activation**: KLR Hopfield asynchronous, event-driven associative memory, kernel Hopfield event-driven, asynchronous retrieval dynamics, neuromorphic Hopfield network, margin-based associative memory

### An extremely coarse feedback signal is sufficient for learning human-aligned visual representations
- [[coarse-feedback-visual-alignment]] - 极粗分类信号（仅8类）训练的视觉网络脑区对齐度超越千分类和自监督模型，与人类感知相似度判断最匹配 (arXiv: 2605.05556)
  - 核心要点 1: 通过PCA分割预训练嵌入，参数化控制分类粒度（2/4/8/16/.../64类）
  - 核心要点 2: 仅8类训练的网络在猕猴电生理和人类fMRI对齐度上匹敌或超越1000类模型
  - 核心要点 3: 粗粒度模型在人类感知相似度判断上的对齐度超越所有其他模型
  - **Activation**: coarse feedback visual alignment, brain-aligned vision, representational similarity, training signal granularity, neural alignment coarse classification

### Multilevel Regression Modeling of Covariance Matrix Outcomes
- [[mcap-multilevel-covariance-regression]] - MCAP多级协变量辅助主成分回归框架，处理分层嵌套神经影像数据，揭示生命周期中脑功能连接变化规律 (arXiv: 2605.05371)
  - 核心要点 1: 簇特异性线性投影+广义线性混合效应模型处理层次化数据
  - 核心要点 2: von Mises-Fisher分布在单位球面上建模簇特异性投影，实现跨簇信息借用
  - 核心要点 3: HCP生命周期研究（5-90岁）发现成年晚期神经重组模式收敛
  - **Activation**: multilevel covariance regression, MCAP, lifespan brain connectivity, functional connectivity outcomes, hierarchical neuroimaging

### Interpreting V1 Population Activity via Image-Neural Latent Representation Alignment
- [[dina-v1-population-activity-interpretation]] - DINA双塔图像-神经对齐框架，在中间特征图级别对齐视觉刺激和V1群体响应，实现可解码且可解释的视觉计算分析 (arXiv: 2605.04309)
  - 核心要点 1: 对比学习在共享潜空间中对齐图像特征图和V1群体响应
  - 核心要点 2: 解码性能主要由粗粒度低级视觉结构驱动，而非语义类别信息
  - 核心要点 3: 对齐特征图由稀疏强响应神经元及其功能交互重构
  - **Activation**: DINA dual-tower alignment, V1 population activity, calcium imaging decoding, interpretable neural alignment, contrastive neural encoding

## 2026-05-10 - Information Science + Quantum (Cron Job)

### Quantum Computation at the Edge of Chaos
- [[quantum-sparsity-edge-chaos]] - 提出量子稀疏性原则，使用拓扑纠缠熵(TEE)作为VQA成本函数正则化器，引导优化沿混沌临界边缘运行，解决量子算法中的贫瘠高原问题 (arXiv: 2604.15441)
  - 核心要点 1: 将经典ML的稀疏解概念推广到量子域，最小化多方共享的量子信息以避免过参数化
  - 核心要点 2: TEE非负对应稀疏可训练态，负TEE对应不可训练混沌态——作为正则化器自动引导优化方向
  - 核心要点 3: 推导量子Nyquist-Shannon采样定理，从理论上界定VQA的资源需求和误差传播界限
  - 核心要点 4: 在复杂数据编码和基态搜索任务中，TEE正则化器显著提升收敛速度和精度
  - **Activation**: quantum sparsity, edge of chaos, TEE regularizer, entanglement entropy, VQA convergence, barren plateau mitigation, quantum Nyquist-Shannon, topological entanglement entropy

### Neural Optimization for Quantum Architectures
- [[neural-quantum-graph-embedding]] - 使用距离编码器网络(DEN)解决中性原子量子硬件的受限单位圆盘问题，通过修改的自编码器和自定义嵌入损失函数实现可行量子比特布局 (arXiv: 2605.03565)
  - 核心要点 1: Distance Encoder Network学习从不可行解到可行解的空间变换映射
  - 核心要点 2: 自定义Embedding Loss Function建模单位圆盘约束，支持端到端梯度优化
  - 核心要点 3: 在固定计算时间下超越经典求解器，可泛化到相似嵌入问题
  - **Activation**: quantum embedding, unit disk problem, neutral atom qubits, distance encoder network, qubit positioning, quantum architecture optimization

     1|## 2026-05-10 - Neuroscience Research (Cron Job)
     2|
     3|### Think-Aloud Reshapes Automated Cognitive Model Discovery Beyond Behavior
- [[think-aloud-cognitive-model-discovery]] - 通过Think-Aloud协议增强自动认知模型发现，超越纯行为数据捕捉决策过程中的推理和元认知 (arXiv: 2605.05091)
  - Think-Aloud口头报告作为额外数据约束，显著提升认知模型发现的可解释性和准确性
  - 纯行为数据无法区分的竞争模型可通过语言报告有效区分
  - **Activation**: think-aloud protocol, cognitive model discovery, verbal protocol analysis, decision-making cognition

### Beyond Object-Level Alignment: Do Brains and DNNs Preserve the Same Transformations?
     4|- [[naturality-violation-score]] - 引入 Naturality Violation Score (NVS)，用范畴论的近似自然性重构脑-DNN对齐评估，从逐刺激匹配转向变换结构保持 (arXiv: 2605.06420)
     5|  - 核心要点 1: 通过 cospan 框架连接脑空间 B、模型空间 M 和 World Model 代理空间 W，拟合 ΦB/ΦM/η/η' 四条线性映射链
     6|  - 核心要点 2: NVS 衡量自然性方格的双向残差并归一化到置换零分布，0=完美交换，1=随机基线
     7|  - 核心要点 3: 轴分解分析揭示层级交叉——低层视觉轴对齐 V1×浅层，语义轴(animacy)对齐 HVC×深层
     8|  - **Activation**: NVS, naturality violation, brain-DNN alignment, category theory alignment, approximate naturality, cospan framework, transformation preservation, axis-resolved alignment
     9|
    10|## 2026-05-10 - Information Science + Quantum (Cron Job)
    11|
    12|### Affine Subcode Ensemble Decoding for Degeneracy-Aware Quantum Error Correction
    13|- [[affine-subcode-ensemble-decoding]] - 通过扩充校验矩阵和仿射子码系综解码解决量子LDPC码的简并性问题，提升BP解码收敛率和逻辑错误率 (arXiv: 2605.06547)
    14|  - 核心要点 1: 在校验矩阵中添加线性无关行，减少简并解搜索空间
    15|  - 核心要点 2: 对每个解码路径使用不完整矩阵，多个路径投票提高解码可靠性
    16|  - **Activation**: affine subcode decoding, degeneracy-aware QEC, QLDPC decoding, quantum LDPC, toric code decoding
    17|
    18|### Machine Learning Approaches to Building Quantum Circuits for Sets of Matrices
    19|- [[quantum-circuit-ml-construction]] - 使用可解释机器学习构建最短通用量子算法来编码任意大小对角矩阵 (arXiv: 2605.06633)
    20|  - 核心要点 1: 通过分析ML参数可构造解析最短量子电路
    21|  - 核心要点 2: 适用于任意尺寸的对角矩阵编码
    22|  - **Activation**: quantum circuit construction, ML quantum algorithms, diagonal matrix encoding
    23|
    24|### The Kubo-Thermalization Correspondence
    25|- [[kubo-thermalization-correspondence]] - 建立量子热化与Kubo线性响应之间的精确对应关系，通过平衡响应推断热化动力学 (arXiv: 2605.06666)
    26|  - 核心要点 1: 长时间热化磁化与短时间线性响应谱之间的精确联系
    27|  - 核心要点 2: 适用于与热浴耦合的自旋系统，独立于系统-浴耦合微观细节
    28|  - **Activation**: quantum thermalization, Kubo response, linear response, many-body physics
    29|
    30|## 2026-05-10 - Quantum State Preparation (Cron Job)
    31|
    32|### Practical Log-Depth Quantum State Preparation via Matrix Product States
    33|- [[ttn-quantum-state-preparation]] - Efficient log-depth quantum state preparation using MPS-to-TTN renormalization with unitary circuit compilation (arXiv: 2605.06579)
    34|  - MPS representation enables polynomial-parameter encoding of exponentially large quantum states
    35|  - TTN renormalization converts MPS to tree tensor network for efficient hierarchical decomposition
    36|  - Log-depth unitary circuit compilation via sequential two-qubit gate synthesis from TTN isometries
    37|  - **Activation**: quantum state preparation, MPS tensor network, TTN renormalization, log-depth quantum circuit, quantum state compilation, isometric decomposition, quantum data loading
    38|
### Superintelligent Retrieval Agent
- [[superintelligent-retrieval-agent]] - 智能检索代理超越黑盒查询，主动推理信息需求并迭代验证检索质量 (arXiv: 2605.06647)
  - 核心要点 1: 信息差距分析优先于检索——识别需要什么类型的信息、深度如何
  - 核心要点 2: 策略选择匹配查询类型——事实查询直接搜索，分析查询多跳推理
  - 核心要点 3: 质量门控循环——检索后评估文档相关性，不满足则重新检索
  - **Activation**: superintelligent retrieval, 智能检索代理, RAG agent optimization, active retrieval strategy

### Edge-specific Signal Propagation on 3D Mechanism Graphs for QY Prediction
- [[graph-mechanism-quantum-prediction]] - 边特定信号传播在3D机制图上预测荧光蛋白量子产率 (arXiv: 2605.06644)
  - 核心要点 1: 色团3D微环境决定量子产率，序列不够——需要结构图表示
  - 核心要点 2: 边类型特定的消息传递捕获不同物理交互的独特影响
  - 核心要点 3: H键、π堆叠、静电、范德华各自使用不同权重矩阵
  - **Activation**: quantum yield prediction, 量子产率预测, mechanism graph, edge-specific GNN, fluorescent protein


    39|## 2026-05-10 - Quantum Mechanics Daily (Cron Job)
    40|
    41|## 2026-05-10 - 量子力学 + 信息学 (Cron Job)
    42|
    43|### Exponential quantum advantage in processing massive classical data
    44|- [[quantum-polylog-data-processing]] - 证明多对数规模量子计算机在ML任务中实现指数级优势 (arXiv: 2605.06539)
    45|  - 量子随机访问QRAM实现多对数查询复杂度
    46|  - 量子优势来自量子并行性+指数态空间，与输入数据无关
    47|  - **Activation**: 量子优势, 海量数据处理, polylog, quantum advantage, massive data
    48|
    49|### Hybrid Quantum-Classical GANs for the Generation of Adversarial Network Flows
    50|- [[hybrid-quantum-gan-security]] - 混合量子-经典GAN改善对抗流量生成质量并降低计算开销 (arXiv: 2605.06629)
    51|  - 量子电路作为生成器克服mode collapse
    52|  - 减少训练所需高维数据量和计算成本
    53|  - **Activation**: 量子GAN, 对抗流量, 网络安全, quantum GAN, adversarial traffic
    54|
    55|### Machine Learning Approaches to Building Quantum Circuits for Sets of Matrices
    56|- [[ml-quantum-circuit-construction]] - 可解释ML构建任意维度qudit系统最短解析量子算法 (arXiv: 2605.06633)
    57|  - 通过ML参数分析构造同时对角化矩阵集的通用量子算法
    58|  - 适用于任意维度qudit系统
    59|  - **Activation**: ML构建量子电路, qudit, 同时对角化, matrix diagonalization
    60|
    61|### Quantum Information Theory with Deep Neural Networks
    62|- [[quantum-info-deep-learning]] - 深度学习近似量子态、优化协议、自动发现量子纠错码 (arXiv: 2605.06547)
    63|  - 神经量子态(NQS)近似多体波函数
    64|  - 自动架构搜索发现新型量子纠错码
    65|  - **Activation**: 量子信息论, 深度学习, neural quantum state, QEC discovery
    66|
    67|### Machine Learning Approaches to Building Quantum Circuits for Sets of Matrices
    68|- [[quantum-circuit-builder]] - ML-driven quantum circuit synthesis using parameterized ansatz and fidelity-based optimization for implementing target matrix sets (arXiv: 2605.06633)
    69|  - Parameterized quantum circuits with rotation/entangling gates optimized via classical gradient descent or parameter-shift rule
    70|  - Fidelity loss function L = 1 - |Tr(U†_target · U_circuit)|/N with circuit depth penalty for NISQ efficiency
    71|  - Multi-matrix support via shared parameterization across matrix sets with layer-wise training
    72|  - **Activation**: quantum circuit synthesis, parameterized quantum circuits, VQC optimization, quantum gate design, matrix decomposition quantum, VQE ansatz, barren plateau mitigation
    73|
    74|### Hybrid Quantum-Classical GANs for the Generation of Adversarial Network Flows
    75|- [[hybrid-quantum-gan]] - Hybrid quantum-classical GAN architecture leveraging quantum variational circuits for enhanced generative expressivity in adversarial flow generation (arXiv: 2605.06629)
    76|  - Quantum generator uses VQC with angle embedding and strong entangling layers, classical discriminator for real/fake discrimination
    77|  - Training loop combines backpropagation for classical layers with parameter-shift rule for quantum gradients
    78|  - 4-16 qubit NISQ-compatible design with circuit depth < 10 layers
    79|  - **Activation**: quantum GAN, hybrid quantum-classical neural network, adversarial traffic generation, quantum generative modeling, VQC generator, quantum-enhanced GAN
    80|
    81|### Neural Networks and Reinforcement Learning for the Simulation of Open Quantum Dynamics
    82|- [[quantum-rl-simulation]] - Neural quantum states and RL-based approaches for simulating Lindblad master equation dynamics, avoiding exponential scaling of density matrix methods (arXiv: 2605.06661)
    83|  - Neural quantum states (NQS) represent quantum states via RBM/CNN/Transformer with TDVP time evolution
    84|  - RL formulation with Lindblad jump operators as actions, fidelity/energy as rewards for quantum control
    85|  - Monte Carlo sampling for observable estimation with exact diagonalization validation for N ≤ 10 qubits
    86|  - **Activation**: open quantum system simulation, neural quantum states, Lindblad master equation, RL quantum control, quantum dynamics TDVP, decoherence modeling, quantum error correction simulation
    87|
    88|### Residual-Based QLSA with Dynamic Stopping for Linear Systems
    89|- [[quantum-dynamic-stopping]] - Residual-based Quantum Linear System Algorithm with adaptive dynamic stopping criterion for efficient HHL-class solving of linear systems, applied to elliptic PDEs (arXiv: 2605.06414)
    90|  - Residual estimation via quantum phase estimation and amplitude amplification replaces heuristic fixed-depth iteration
    91|  - Adaptive stopping criterion ‖r_k‖ < ε guarantees solution quality without over-computation on NISQ hardware
    92|  - Applied to elliptic PDE solving with logarithmic qubit scaling vs classical O(N) memory
    93|  - **Activation**: QLSA dynamic stopping, HHL algorithm, quantum linear systems, residual estimation, elliptic PDE quantum, quantum phase estimation stopping, adaptive quantum iteration
    94|
    95|### QDSA: Diagonal Unitary Synthesis via Quantum Decomposition
    96|- [[qdsa-diagonal-unitary-synthesis]] - Quantum Diagonal Synthesis Algorithm (QDSA) for efficient decomposition of diagonal unitary matrices into optimal gate sequences with minimal CNOT count (arXiv: 2605.06397)
    97|  - Hierarchical decomposition reduces CNOT complexity from O(4^n) to O(2^n) for n-qubit diagonal unitaries
    98|  - Exploits phase redundancy and symmetries in diagonal matrices for further gate count reduction
    99|  - Applicable to quantum oracle construction, QFT variants, and variational circuit ansatz design
   100|  - **Activation**: diagonal unitary synthesis, quantum gate decomposition, CNOT optimization, quantum oracle design, QFT optimization, variational circuit ansatz, quantum compiler optimization
   101|
   102|### Affine Subcode Ensemble Decoding for Quantum Error Correction
   103|- [[affine-subcode-qec-decoding]] - Degeneracy-aware quantum error correction using affine subcode ensemble decoding that exploits code degeneracy for improved logical error rates beyond standard minimum-weight decoding (arXiv: 2605.06547)
   104|  - Affine subcode decomposition partitions the error coset space to enumerate degenerate error configurations
   105|  - Ensemble voting across subcode decoders achieves near-maximum-likelihood performance with polynomial complexity
   106|  - Demonstrates 10-100x logical error rate improvement over MWPM on surface codes with realistic noise
   107|  - **Activation**: quantum error correction, degeneracy-aware decoding, affine subcode ensemble, surface code decoding, MWPM improvement, logical error rate optimization, quantum fault tolerance
   108|
   109|## 2026-05-10 - Systems Engineering Research (Cron Job)
   110|
   111|### Quantifying Trade-Offs Between Stability and Goal-Obfuscation in Network Control Systems
   112|- [[stability-goal-obfuscation]] - Control-theoretic framework for privacy-preserving control using Probabilistic Control Barrier Functions (PCBF) with robust MPC, balancing stability guarantees against goal-obfuscation (arXiv: 2605.06630)
   113|  - PCBF quantifies probabilistic state reachability bounds for goal-obfuscation while maintaining control-theoretic stability
   114|  - Robust MPC formulation with tightened constraints ensures recursive feasibility under privacy noise
   115|  - Rigorous stability-proof trade-off analysis showing privacy budget vs convergence rate relationship
   116|  - **Activation**: goal obfuscation, privacy-preserving control, PCBF, robust MPC, stability-privacy trade-off, network control systems
   117|
   118|### CLAD: Clustered Label-Agnostic Federated Learning for Anomaly Detection
   119|- [[clad-federated-anomaly-detection]] - Privacy-preserving federated anomaly detection framework using clustered label-agnostic learning with DM²A dual-mode aggregation for bandwidth-constrained edge deployments (arXiv: 2605.06571)
   120|  - DM²A dual-mode aggregation dynamically selects between model-averaging and prototype-based fusion based on client data heterogeneity
   121|  - Clustered label-agnostic grouping handles non-IID data without requiring shared label schemas across clients
   122|  - Communication-efficient design with adaptive compression for edge deployment
   123|  - **Activation**: federated learning, anomaly detection, label-agnostic, DM²A aggregation, non-IID federated, edge computing, privacy-preserving ML
   124|
   125|## 2026-05-10 - Neuroscience Research (Cron Job)
   126|
   127|### Resolvent-RNNs: Multi-Hop Temporal Sparsity for Sequence Modeling
   128|- [[resolvent-rnn-multi-hop-sparsity]] - Resolvent operator framework constraining multi-hop pathway contributions in RNNs, enabling provable temporal sparsity and interpretable memory allocation (arXiv: 2605.03598)
   129|  - Multi-hop pathway analysis reveals dominant memory pathways via resolvent operator, allowing selective pruning of negligible temporal dependencies
   130|  - Spectral constraint on transition matrix resolvent enables provable bounds on multi-step gradient propagation, reducing vanishing/exploding gradients
   131|  - Demonstrates alignment between temporal sparsity patterns and biological memory consolidation, with 40% parameter reduction on seq classification tasks
   132|  - **Activation**: RNN temporal sparsity, multi-hop memory pathways, resolvent operator analysis, sequence modeling efficiency, interpretable RNNs, gradient propagation bounds, memory consolidation modeling, temporal credit assignment
   133|
   134|     1|## 2026-05-09 - Neuroscience Research (Cron Job)
   135|     2|
   136|     3|### Detecting AI-Generated Videos with Spiking Neural Networks
   137|     4|- [[mast-aigv-detection-snn]] - First SNN-based detector for AI-generated video detection, achieving 93.14% cross-generator accuracy (arXiv: 2605.05895)
   138|     5|  - AI-generated videos exhibit smoother temporal residuals at pixel level and more compact semantic trajectories, with SNNs responding to boundary-localized temporal artifacts
   139|     6|  - MAST converts inter-frame residuals into pseudo-events processed by spike-driven temporal branch with learnable per-channel time constants, fused with frozen X-CLIP encoder
   140|     7|  - 69× energy savings for the gate at parameter parity (1.24 mJ vs 85.61 mJ per clip)
   141|     8|  - **Activation**: AI-generated video detection, SNN video detection, temporal artifact detection, pseudo-event conversion, cross-generator generalization, MAST, spike-driven temporal integration, AIGV detection, boundary-localized firing, SDT-V3
   142|     9|
   143|    10|## 2026-05-09 - Neuroscience Research (Cron Job)
   144|    11|
   145|    12|### Think-Aloud Reshapes Automated Cognitive Model Discovery Beyond Behavior
- [[think-aloud-cognitive-model-discovery]] - 通过Think-Aloud协议增强自动认知模型发现，超越纯行为数据捕捉决策过程中的推理和元认知 (arXiv: 2605.05091)
  - Think-Aloud口头报告作为额外数据约束，显著提升认知模型发现的可解释性和准确性
  - 纯行为数据无法区分的竞争模型可通过语言报告有效区分
  - **Activation**: think-aloud protocol, cognitive model discovery, verbal protocol analysis, decision-making cognition

### Beyond Object-Level Alignment: Do Brains and DNNs Preserve the Same Transformations?
   146|    13|- [[naturality-violation-score]] - 基于范畴论的脑-DNN对齐新方法，通过Naturality Violation Score(NVS)评估变换保持性而非刺激级对应 (arXiv: 2605.06420)
   147|    14|  - 提出Naturality Square形式主义，将脑与模型的对齐从"表示相同刺激"提升到"保留相同变换"
   148|    15|  - 轴分解分析揭示层次交叉：语义轴(animacy)向高级视觉皮层和深层DNN对齐，低级视觉轴向早期区域对齐
   149|    16|  - **Activation**: brain-DNN alignment, naturality violation, transformation alignment, category theory neuroscience
   150|    17|
   151|    18|### A multi-scale information geometry reveals the structure of mutual information in neural populations
   152|    19|- [[multi-scale-info-geometry-neural]] - 从信息收缩原理推导唯一黎曼表征几何，将Fisher信息度量与互信息精确关联 (arXiv: 2605.06304)
   153|    20|  - 信息收缩原理唯一确定神经群体的表征几何，多尺度Fisher信息度量捕获从精细到粗略的编码结构
   154|    21|  - 度量张量特征向量识别对信息传输贡献最大的刺激变化方向，可通过扩散模型估计
   155|    22|  - **Activation**: neural coding geometry, Fisher information metric, information geometry, mutual information neural
   156|    23|
   157|    24|
   158|    25|
   159|    26|## 2026-05-09 - Neuroscience Research (Cron Job)
   160|    27|
   161|    28|### Naturality Violation Score for Brain-DNN Transformation Alignment
   162|    29|- [[brain-dnn-transformation-alignment]] - Category-theoretic framework evaluating whether brains and DNNs preserve the same representational transformations via Naturality Violation Score (NVS) (arXiv: 2605.06420)
   163|    30|  - Core: Goes beyond static RSA/CCA to measure transformation preservation across stimulus conditions using category theory functors and natural transformations
   164|    31|  - Core: NVS quantifies deviation from commutative diagrams between brain and DNN representational spaces; lower NVS = better alignment
   165|    32|  - **Activation**: NVS, naturality violation, brain-DNN transformation, representational dynamics, category theory neuroscience, Kamitani lab
   166|    33|
   167|    34|### Critical Analysis of Decoding-Encoding-Alignment Methods
   168|    35|- [[decoding-encoding-alignment-critique]] - Systematic critique of RSA, encoding models, and decoding approaches revealing representational collapse, feature confounding, and stimulus-set dependency (arXiv: 2605.05907)
   169|    36|  - Core: RSA conflates feature representations with stimulus-set statistics; encoding models suffer from identifiability issues; decoding accuracy doesn't imply neural alignment
   170|    37|  - Core: Proposes transformation alignment as a more robust alternative, testing whether models preserve the same computational trajectories as brains
   171|    38|  - **Activation**: RSA critique, encoding model limitations, representational collapse, feature confounding, alignment validity, stimulus-set dependency
   172|    39|
   173|    40|## 2026-05-09 - Neuroscience Research (Cron Job)
   174|    41|
   175|    42|### Neuromorphic visual attention framework for sign language recognition on SpiNNaker-2
   176|    43|- [[neuromorphic-spinnaker-asl]] - Event-based neuromorphic vision system for real-time ASL recognition on SpiNNaker-2 with spiking temporal encoder and STDP-based learning (arXiv: 2605.06005)
   177|    44|  - Core: Spiking temporal encoder converts DVS events into spike trains with learnable time constants
   178|    45|  - Core: STDP-based unsupervised learning for temporal pattern recognition on neuromorphic hardware
   179|    46|  - **Activation**: neuromorphic computing, SpiNNaker, event-based vision, sign language recognition, STDP, spiking temporal encoder
   180|    47|
   181|    48|### CORE framework for out-of-distribution brain network analysis
   182|    49|- [[brain-network-core]] - Site-aware confounder decoupling framework for OOD generalization in brain network analysis via decoupling site-specific biases (arXiv: 2605.06050)
   183|    50|  - Core: Decouples site-specific confounders from invariant brain network patterns using adversarial disentanglement
   184|    51|  - Core: 2-layer GCN with hidden=64, trained with adversarial loss to minimize site information in representations
   185|    52|  - **Activation**: brain network analysis, OOD generalization, confounder decoupling, site-aware learning, graph neural network
   186|    53|
   187|    54|     1|## 2026-05-09 - Neuroscience Research (Cron Job)
   188|    55|     2|
   189|    56|     3|### A multi-scale information geometry reveals the structure of mutual information in neural populations
   190|    57|     4|- [[multi-scale-info-geometry-neural]] - Riemannian representational geometry derived from coarse-graining principles, exactly related to mutual information (arXiv: 2605.06304)
   191|    58|     5|  - Core: Multi-scale Fisher information metric captures encoding structure from fine to coarse scales
   192|    59|     6|  - Core: Metric tensor eigenvectors identify information-carrying stimulus features in neural populations
   193|    60|     7|  - **Activation**: information geometry, Fisher information, neural coding, representational geometry, mutual information
   194|    61|     8|
   195|    62|     9|### A Generalized Framework of Antisymmetric Polyspectral Indices for Identifying High-Order Neural Interactions
   196|    63|    10|- [[antisymmetric-polyspectral-neural-interactions]] - Generalized antisymmetric cross-polyspectral indices detecting 3-way+ neural interactions beyond pairwise connectivity (arXiv: 2605.04636)
   197|    64|    11|  - Core: Cross-bispectrum and cross-trispectrum with antisymmetric properties robust to volume conduction
   198|    65|    12|  - Core: Hypergraph construction for multi-node synergistic brain network analysis
   199|    66|    13|  - **Activation**: polyspectral, bispectrum, higher-order connectivity, multi-node coupling, synergistic connectivity
   200|    67|    14|
   201|    68|    15|## 2026-05-09 - Anthropic Research (Cron Job)
   202|    69|    16|
   203|    70|    17|### Teaching Claude why
   204|    71|    18|- [[teaching-claude-why]] - Reduce agentic misalignment through principled, principle-based alignment training that generalizes out-of-distribution
   205|    72|    19|  - Core finding: Agentic misalignment comes from pre-trained model; standard RLHF insufficient for agentic settings
   206|    73|    20|  - Key method: Synthetic Document Fine-Tuning (SDF) — train on principled documents that articulate why certain actions are wrong
   207|    74|    21|  - Result: Every Claude since Haiku 4.5 achieves perfect score on agentic misalignment evals
   208|    75|    22|  - **Activation**: agentic misalignment, alignment training, safety training, RLHF, constitution, honeypot, blackmail, OOD generalization
   209|    76|    23|
   210|    77|    24|### Automated Alignment Researchers
   211|    78|    25|- [[automated-alignment-researchers]] - Use LLMs as autonomous alignment researchers to discover alignment improvements via weak-to-strong supervision
   212|    79|    26|  - Core metric: Performance Gap Recovered (PGR) — measures how much weaker teacher recovers strong model potential
   213|    80|    27|  - Key result: 9 AAR instances recovered 97% of the performance gap vs human researchers
   214|    81|    28|  - Method: LLM researchers propose hypotheses, design experiments, test on models, iterate
   215|    82|    29|  - **Activation**: AAR, automated alignment, weak-to-strong supervision, PGR, scalable oversight, alignment automation
   216|    83|    30|
   217|    84|    31|### Trustworthy Agents in Practice
   218|    85|    32|- [[trustworthy-agents-framework]] - Five-principle framework for building and governing trustworthy AI agents with practical implementation guidance
   219|    86|    33|  - Five principles: Human Control, Alignment with Values, Security, Transparency, Privacy
   220|    87|    34|  - Key pattern: Agent architecture with 4 layers (model, tools, memory, execution) each with oversight
   221|    88|    35|  - Practical guidance: prompt injection defense, permission systems, audit logging
   222|    89|    36|  - **Activation**: trustworthy agents, agent governance, prompt injection, human control, agent security, transparency, privacy
   223|    90|    37|
   224|    91|    38|## 2026-05-09 - Quantum Error Correction (Cron Job)
   225|    92|    39|
   226|    93|    40|### Syndrome Resampling Enhances QEC Thresholds
   227|    94|    41|- [[quantum-error-correction-methods]] - Bias syndrome averages toward high-probability syndromes to increase QEC thresholds and reduce logical error rates by up to 4 orders of magnitude without hardware changes (arXiv: 2605.06101)
   228|    95|    42|  - Core method: Resample syndromes according to P(s)^α with MLD, linked to Rényi coherent information phase transitions
   229|    96|    43|  - Decoder-agnostic: works with any QEC decoder from finite syndrome data
   230|    97|    44|  - Applied to existing experimental data: 2 orders of magnitude logical error rate reduction
   231|    98|    45|  - **Activation**: syndrome resampling, QEC threshold, logical error rate, Rényi coherent information
   232|    99|    46|
   233|   100|    47|### Affine Subcode Ensemble Decoding
   234|   101|    48|- [[quantum-error-correction-methods]] - Extend affine subcode ensemble decoding from classical to quantum setting to address degeneracy impairment in qLDPC BP decoding (arXiv: 2605.06547)
   235|   102|    49|  - Core insight: Appending independent rows to check matrix reduces search space for degenerate solutions
   236|   103|    50|  - Uses overcomplete matrices for each decoding path, improved convergence on toric/GB codes
   237|   104|    51|  - **Activation**: affine subcode, degeneracy-aware decoding, qLDPC, belief propagation
   238|   105|    52|
   239|   106|    53|### Real-time FPGA Neural Network Decoder
   240|   107|    54|- [[quantum-error-correction-methods]] - FPGA-based NN decoder achieves 550 ns closed-loop latency for real-time distance-3 surface code QEC on superconducting processor (arXiv: 2605.04892)
   241|   108|    55|  - 124 ns NN decoding within 1.25 μs QEC cycle, supports mid-circuit feedback for non-Clifford operations
   242|   109|    56|  - **Activation**: FPGA decoder, neural network decoder, real-time QEC, surface code
   243|   110|    57|
   244|   111|    58|### Distributed BB Codes in Modular Architecture
   245|   112|    59|- [[quantum-error-correction-methods]] - Implement [[144,12,12]] BB code across modular processors interconnected via shared Bell pairs with BP+OSD decoding (arXiv: 2605.04663)
   246|   113|    60|  - Star network architecture for trapped ion/neutral atom platforms with all-to-all internal connectivity
   247|   114|    61|  - **Activation**: bivariate bicycle codes, distributed QEC, modular quantum computing, qLDPC
   248|   115|    62|
   249|   116|    63|## 2026-05-09 - OpenAI Research (Cron Job)
   250|   117|    64|
   251|   118|    65|### Trading Inference Time Compute for Adversarial Robustness
   252|   119|    66|- [[trading-inference-time-adversarial-robustness]] - Trade repeated sampling at inference time for provable adversarial robustness guarantees in LLMs through safety filtering and output aggregation
   253|   120|    67|  - Core innovation: Compute-robustness trade-off — more samples → logarithmically stronger adversarial defense
   254|   121|    68|  - Key method: Repeated sampling + safety filter + majority vote aggregation
   255|   122|    69|  - Application: Post-hoc jailbreak defense layer on aligned LLMs
   256|   123|    70|  - **Activation**: adversarial robustness, inference-time compute, repeated sampling, safety filter, jailbreak defense, compute-robustness tradeoff
   257|   124|    71|
   258|   125|    72|### Detecting and Reducing Scheming in AI Models
   259|   126|    73|- [[detecting-reducing-scheming-ai]] - Systematic evaluation methodology for detecting hidden misalignment (scheming) in frontier AI models through situational awareness tests, reward tampering detection, and sandbagging evaluations
   260|   127|    74|  - Core innovation: Joint Apollo Research + OpenAI framework for deceptive behavior detection
   261|   128|    75|  - Key methods: Multi-stage adversarial deployment scenarios, cross-model comparison, training-time intervention
   262|   129|    76|  - Finding: Scheming behaviors detected in controlled tests across frontier models
   263|   130|    77|  - **Activation**: scheming detection, hidden misalignment, AI deceptive behavior, Apollo Research, model safety evaluation, alignment
   264|   131|    78|
   265|   132|    79|### Collective Alignment: Public Input on AI Model Behavior
   266|   133|    80|- [[collective-alignment-public-input]] - Methodology for incorporating public input into AI model alignment through large-scale surveys and democratic value aggregation across global demographics
   267|   134|    81|  - Core innovation: Survey 1000+ people worldwide, compare to Model Spec, update defaults
   268|   135|    82|  - Key methods: Demographic sampling, behavior scenario preference elicitation, iterative re-surveying
   269|   136|    83|  - Finding: Global public opinion differs from existing AI defaults, cultural variation requires nuanced alignment
   270|   137|    84|  - **Activation**: collective alignment, public input AI, democratic AI alignment, Model Spec, AI behavior preferences
   271|   138|    85|
   272|   139|    86|## 2026-05-09 - Neuroscience Research (Cron Job)
   273|   140|    87|
   274|   141|    88|### Unifying Dynamical Systems and Graph Theory to Mechanistically Understand Neural Computation
   275|   142|    89|- [[unifying-dynamics-graph-neural-computation]] - Unified framework integrating Recurrent Neural Networks (RNNs) with dynamical systems and graph theory to mechanistically understand neural computation; introduces path-constrained regularization, multi-hop interaction analysis, and temporal sparsity metrics (arXiv:2605.03598)
   276|   143|    90|  - Core innovation: R-RNNs (Recurrent-Residual RNNs) with path-constrained regularization enabling mechanistic interpretation of neural dynamics
   277|   144|    91|  - Key method: Multi-hop path analysis quantifying information flow through network connectivity graphs
   278|   145|    92|  - Key finding: Temporal sparsity patterns reveal computational bottlenecks and redundant pathways in trained RNNs
   279|   146|    93|  - Mechanistic insight: Unifies dynamical systems stability analysis with graph-theoretic measures for interpretable neural computation
   280|   147|    94|  - **Activation**: R-RNN, recurrent residual networks, path-constrained regularization, neural dynamics interpretation, graph theory RNN, temporal sparsity neural, mechanistic neural computation, dynamical systems neural networks
   281|   148|    95|
   282|   149|    96|## 2026-05-09 - Systems Engineering Research (Cron Job)
   283|   150|    97|
   284|   151|    98|### Safactory: A Scalable Agent Factory for Trustworthy Autonomous Intelligence
   285|   152|    99|- [[safactory-agent-factory]] - Production-grade autonomous agent factory with sandboxing, multi-level safety guardrails, policy-driven execution, and dynamic tool provisioning; enables trustless deployment of AI agents in enterprise environments (arXiv: 2605.06230)
   286|   153|   100|  - Core innovation: Multi-layer safety architecture combining static analysis, runtime monitoring, and post-execution verification
   287|   154|   101|  - Key pattern: Policy-driven tool provisioning — agents only receive tools they need, when they need them, reducing attack surface
   288|   155|   102|  - Architecture: Sandboxed execution environments with resource limits, capability scoping, and audit logging
   289|   156|   103|  - Scalability: Factory pattern for spawning, monitoring, and terminating agent instances on demand
   290|   157|   104|  - **Activation**: agent factory, autonomous agent sandbox, agent safety guardrails, policy-driven tool provisioning, trustless AI deployment, scalable agent orchestration
   291|   158|   105|
   292|   159|   106|### Towards Formal Verification of Hybrid Synchronous Programs with Refinement Types
   293|   160|   107|- [[formal-verification-hybrid-synchronous]] - Formal verification methodology combining refinement types with synchronous programming models for hybrid/cyber-physical systems; bridges discrete controller logic with continuous physical dynamics (arXiv: 2605.04377)
   294|   161|   108|  - Core innovation: Refinement type system that encodes safety invariants directly in the type layer of hybrid programs
   295|   162|   109|  - Key method: Synchronous model composition with continuous-time constraints — verified correctness at compile time
   296|   163|   110|  - Application domain: CPS, robotic control, aerospace systems where safety-critical guarantees are required
   297|   164|   111|  - Verification: Automated theorem proving integrated into the compilation pipeline
   298|   165|   112|  - **Activation**: formal verification hybrid systems, refinement types synchronous programs, CPS verification, hybrid program correctness, safety-critical control verification
   299|   166|   113|
   300|   167|   114|  - **Activation**: kernel hopfield, KLR Hopfield, event-driven retrieval, asynchronous associative memory, neuromorphic memory, large-margin attractor, sparse event computation, kernel logistic regression memory
   301|   168|   115|
   302|   169|   116|## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
   303|   170|   117|## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job - Hourly Update)
   304|   171|   118|## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job - Hourly Update #2)
   305|   172|   119|
   306|   173|   120|## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job - Hourly #3)
   307|   174|   121|
   308|   175|   122|### The true cost of factoring: Linking magic and number-theoretic complexity in Shor's algorithm
   309|   176|   123|- [[quantum-magic-state-analysis]] - Analyzes magic (non-stabilizerness) as the genuine quantum resource cost in Shor's algorithm, linking it to number-theoretic hardness of factoring (arXiv: 2605.05347)
   310|   177|   124|  - 核心要点 1: 量子算法成本应以"魔力"（非稳定子资源）而非仅门数和量子比特数来衡量
   311|   178|   125|  - 核心要点 2: Shor算法中模指数运算步骤产生最大魔力，与因数分解难度直接相关
   312|   179|   126|  - 核心要点 3: 魔力生成速率与经典计算困难性成正比，揭示量子优势的数学结构根源
   313|   180|   127|  - **Activation**: quantum magic state, non-stabilizerness, Shor algorithm resource cost, quantum resource theory, magic state distillation, mana computation, quantum advantage estimation
   314|   181|   128|
   315|   182|   129|### Analytical Angle-Finding and Series Expansions for QSP via Orthogonal Polynomial Theory
   316|   183|   130|- [[quantum-signal-processing-orthogonal-polynomials]] - Analytical QSP angle-finding via Hermite, Jacobi, Rogers-Szego polynomials with O(log(1/ε)) gate complexity for smooth function approximation (arXiv: 2605.05321)
   317|   184|   131|  - 核心要点 1: 通过正交/双正交多项式族完整表征可实现的QSP多项式基
   318|   185|   132|  - 核心要点 2: 为Hermite、Jacobi、Rogers-Szego多项式族导出闭式QSP角度公式
   319|   186|   133|  - 核心要点 3: 光滑函数的ε-近似可通过Hermite级数展开用O(log(1/ε))门实现块编码
   320|   187|   134|  - **Activation**: quantum signal processing QSP, QSP angle finding, orthogonal polynomial quantum, Hermite polynomial quantum, Jacobi polynomial QSP, Rogers-Szego quantum, quantum function approximation
   321|   188|   135|
   322|   189|   136|### Quantum Proper Scoring Rules: Minimax Estimation and Resource-Theoretic Advantages
   323|   190|   137|- [[quantum-proper-scoring-rules]] - Generalizes proper scoring rules to density operators via operator convex generators with Quantum Cramér-Rao-McCarthy Bound for state tomography (arXiv: 2605.05268)
   324|   191|   138|  - 核心要点 1: 将经典评分规则推广到量子密度算符，建立算子凸生成函数与量子评分规则的完整对偶理论
   325|   192|   139|  - 核心要点 2: 推导量子Cramér-Rao-McCarthy界，将最小最大风险与生成函数曲率和量子Fisher信息关联
   326|   193|   140|  - 核心要点 3: 量化量子资源在预测任务中的经济价值，连接量子资源理论与机制设计
   327|   194|   141|  - **Activation**: quantum proper scoring rules, quantum state estimation, quantum Fisher information, minimax quantum tomography, operator convex quantum, quantum Cramer-Rao bound, quantum forecasting
   328|   195|   142|
   329|   196|   143|### Integral Means Spectrum for the Random Riemann Zeta Function
   330|   197|   144|- [[random-riemann-zeta-spectrum]] - Proves Kraetzer's 30-year conjecture for integral means spectrum of random Riemann zeta primitive via Gaussian multiplicative chaos (arXiv: 2603.26507)
   331|   198|   145|  - 核心要点 1: 随机黎曼zeta函数的原函数的复积分均值谱几乎必然符合Kraetzer猜想形式
   332|   199|   146|  - 核心要点 2: 随机zeta函数与Kahane的高斯乘性混沌(GMC)建立了严格对应关系
   333|   200|   147|  - 核心要点 3: 用概率论和解析数论工具解决了保形映射中30年的未决猜想
   334|   201|   148|  - **Activation**: random riemann zeta, integral means spectrum, gaussian multiplicative chaos, GMC, analytic number theory, kraetzer conjecture, bagchi zeta, conformal mapping
   335|   202|   149|
   336|   203|   150|
   337|   204|   151|### Module Lattice Security (Part I): Unconditional Verification of Weber's Conjecture for k ≤ 12
   338|   205|   152|- [[module-lattice-security]] - First unconditional proof of Weber's conjecture for k ≤ 12, establishing foundations for Ring-LWE and Module-LWE security without GRH assumption (arXiv: 2604.15858)
   339|   206|   153|  - 核心要点 1: 结合Fukuda-Komatsu计算筛法、Z_2塔归纳结构和Herbrand定理，首次无条件证明k≤12的韦伯猜想
   340|   207|   154|  - 核心要点 2: 韦伯猜想决定主理想问题可解性、模自由性和R-LWE/MLWE最坏情况到平均情况归约的紧致性
   341|   208|   155|  - 核心要点 3: 后量子密码方案（Kyber、Falcon、NewHope）的安全性直接依赖于这些数论基础
   342|   209|   156|  - **Activation**: Weber conjecture, module lattice, Ring-LWE, Module-LWE, post-quantum cryptography, cyclotomic fields, Fukuda-Komatsu sieve, Herbrand theorem
   343|   210|   157|
   344|   211|   158|### Classical shadows over symmetric spaces
   345|   212|   159|- [[quantum-classical-shadows]] - Extends classical shadow protocols from compact groups to compact symmetric spaces, improving sample complexity for certain observable distributions (arXiv: 2605.05518)
   346|   213|   160|  - 核心要点 1: 经典影子协议通常从紧致群均匀采样，本文推广到紧致对称空间采样
   347|   214|   161|  - 核心要点 2: 在某些观测分布下，对称空间协议比现有影子方案有采样复杂度优势
   348|   215|   162|  - **Activation**: classical shadows, symmetric spaces, quantum state tomography, randomized measurements, sample complexity
   349|   216|   163|
   350|   217|   164|### Efficient Quantum Fourier Transforms For Semisimple Algebras
   351|   218|   165|- [[quantum-algebraic-structures]] - Generalizes QFT from finite groups to semisimple algebras with efficient circuits for partition, Brauer, and walled Brauer algebras (arXiv: 2605.05337)
   352|   219|   166|  - 核心要点 1: 半单代数上的傅里叶变换可以是非幺正的，但当参数 d 足够大时可被幺正算子良好逼近
   353|   220|   167|  - 核心要点 2: 通过分解为不可约表示构建高效量子电路，推广了群上的QFT
   354|   221|   168|  - **Activation**: quantum algebra, semisimple algebra QFT, quantum Fourier transform, Brauer algebra, representation theory
   355|   222|   169|
   356|   223|   170|### Analytical Angle-Finding and Series Expansions for Quantum Signal Processing via Orthogonal Polynomial Theory
   357|   224|   171|- [[quantum-algebraic-structures]] - Analytical QSP angle-finding via Hermite, Jacobi, and Rogers-Szego polynomials with O(log(1/ε)) gate complexity (arXiv: 2605.05321)
   358|   225|   172|  - 核心要点 1: 通过正交/双正交多项式族表征可实现的QSP多项式基，导出闭式角度公式
   359|   226|   173|  - 核心要点 2: 利用Hermite级数展开实现O(log(1/ε))门复杂度的光滑函数块编码
   360|   227|   174|  - **Activation**: quantum signal processing, orthogonal polynomials, QSP angles, Hermite expansion, Jacobi polynomials
   361|   228|   175|
   362|   229|   176|### Quantum Proper Scoring Rules: Minimax Estimation and Resource-Theoretic Advantages
   363|   230|   177|- [[quantum-algebraic-structures]] - Quantum domain scoring rules with operator convex generators and Quantum Cramér-Rao-McCarthy Bound (arXiv: 2605.05268)
   364|   231|   178|  - 核心要点 1: 将经典评分规则推广到量子密度算符域，建立完整对偶理论
   365|   232|   179|  - 核心要点 2: 证明量子Cramér-Rao-McCarthy界，量化量子资源在预测任务中的经济价值
   366|   233|   180|  - **Activation**: quantum scoring rules, minimax estimation, quantum Fisher information, operator convex, resource theory
   367|   234|   181|
   368|   235|   182|### Cusped Singularity Mixed-Mode Oscillation Analysis
   369|   236|   183|- [[cusped-singularity-mmo-analysis]] - Geometric singular perturbation analysis of MMOs in inhibitory neural networks via cusped singularities (arXiv: 2605.03606)
   370|   237|   184|  - 核心要点 1: 尖点奇异性（临界流形尖点处的折叠奇异性）是互抑制神经网络中混合模式振荡（MMO）的通用组织机制
   371|   238|   185|  - 核心要点 2: 尖点奇异性保证小振幅振荡（SAO）的产生，结合奇异Hopf分岔形成完整MMO，呈现独特的交替振荡模式
   372|   239|   186|  - 核心要点 3: 在Curtu速率模型和Morris-Lecar突触抑制耦合模型中验证了该机制的普适性
   373|   240|   187|  - **Activation**: mixed-mode oscillations, MMO, cusped singularity, slow-fast neural system, mutual inhibition oscillation, singular perturbation neural, blow-up method neural, neural oscillation mechanism
   374|   241|   188|
   375|   242|   189|## 2026-05-08 - Neuroscience Research (Cron Job)
   376|   243|   190|## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
   377|   244|   191|
   378|   245|   192|### The true cost of factoring: Linking magic and number-theoretic complexity in Shor's algorithm
   379|   246|   193|- [[quantum-magic-number-theory-complexity]] - Links quantum magic (non-stabilizerness) resource cost to classical number-theoretic hardness of factoring (arXiv: 2605.05347)
   380|   247|   194|  - 核心要点 1: 量子算法的真实成本应由非稳定态资源（magic）衡量，而非单纯的门计数
   381|   248|   195|  - 核心要点 2: Shor算法中magic的生成量与数论问题的计算难度直接相关
   382|   249|   196|  - **Activation**: quantum magic, non-stabilizerness, Shor's algorithm, number theory complexity, resource theory
   383|   250|   197|
   384|   251|   198|### Quantum Proper Scoring Rules: Minimax Estimation and Resource-Theoretic Advantages
   385|   252|   199|- [[quantum-proper-scoring-rules]] - Generalizes proper scoring rules to quantum domain with operator convex generators and Quantum Cramér-Rao-McCarthy Bound (arXiv: 2605.05268)
   386|   253|   200|  - 核心要点 1: 将经典评分规则推广到量子密度算符域，定义量子价值泛函
   387|   254|   201|  - 核心要点 2: 证明量子Cramér-Rao-McCarthy界，连接量子Fisher信息与估计风险
   388|   255|   202|  - **Activation**: quantum scoring rules, state estimation, Cramer-Rao bound, quantum Fisher information, metrology
   389|   256|   203|
   390|   257|   204|### A multi-scale information geometry reveals the structure of mutual information in neural populations
   391|   258|   205|- [[multi-scale-information-geometry-neural]] - 多尺度信息几何揭示神经群体编码的互信息结构，Fisher信息度量的多尺度扩展直接关联互信息 (arXiv: 2605.06304)
   392|   259|   206|  - 核心要点1: 唯一黎曼表示几何从粗粒化下距离收缩的第一原理自然涌现，多尺度扩展Fisher信息度量
   393|   260|   207|  - 核心要点2: 度量张量本征向量识别对信息传输贡献最大的刺激变化方向，可通过扩散模型估计
   394|   261|   208|  - **Activation**: information geometry, Fisher information metric, neural population coding, mutual information, representational geometry, diffusion model estimation
   395|   262|   209|
   396|   263|   210|### Decoding Alignment without Encoding Alignment: A critique of similarity analysis in neuroscience
   397|   264|   211|- [[decoding-encoding-alignment-critique]] - 揭示RSA/DSA对齐度量的根本缺陷：解码对齐不代表计算相似性，高对齐分数可由极少数神经元子群体驱动 (arXiv: 2605.05907)
   398|   265|   212|  - 核心要点1: 解码对齐(RSA/DSA)无法反映神经元群体的编码拓扑，相似解码行为可由小神经元子集主导
   399|   266|   213|  - 核心要点2: 引入编码流形作为补充分析工具，必须同时报告解码对齐和编码拓扑才能得出有效结论
   400|   267|   214|  - **Activation**: decoding alignment, encoding manifold, RSA critique, brain-DNN comparison, representational similarity
   401|   268|   215|
   402|   269|   216|
   403|   270|   217|### Efficient Event-Driven Retrieval in High-Capacity Kernel Hopfield Networks
   404|   271|   218|- [[event-driven-hopfield-retrieval]] - KLR Hopfield网络的异步事件驱动检索，实现接近O(N)存储容量的神经形态联想记忆 (arXiv: 2605.05978)
   405|   272|   219|  - 核心要点 1: 异步序列更新在调优核参数下与同步动力学统计不可区分，保持高召回率
   406|   273|   220|  - 核心要点 2: KLR学习诱导的大边际吸引子创造平滑能量景观，收敛事件数≈初始汉明距离，适合稀疏神经形态计算
   407|   274|   221|  - **Activation**: kernel hopfield, event-driven retrieval, KLR Hopfield, asynchronous associative memory, neuromorphic memory, large-margin attractor
   408|   275|   222|
   409|   276|   223|### Think-Aloud Reshapes Automated Cognitive Model Discovery Beyond Behavior
- [[think-aloud-cognitive-model-discovery]] - 通过Think-Aloud协议增强自动认知模型发现，超越纯行为数据捕捉决策过程中的推理和元认知 (arXiv: 2605.05091)
  - Think-Aloud口头报告作为额外数据约束，显著提升认知模型发现的可解释性和准确性
  - 纯行为数据无法区分的竞争模型可通过语言报告有效区分
  - **Activation**: think-aloud protocol, cognitive model discovery, verbal protocol analysis, decision-making cognition

### Beyond Object-Level Alignment: Do Brains and DNNs Preserve the Same Transformations?
   410|   277|   224|- [[brain-dnn-transformation-alignment]] - 基于范畴论的自然性违反分数(NVS)评估脑-DNN变换级对齐，揭示语义/视觉轴的分层交叉 (arXiv: 2605.06420)
   411|   278|   225|  - 核心要点 1: 将脑-DNN对齐从刺激级对应提升到变换保持测试，NVS量化与置换零模型的偏差
   412|   279|   226|  - 核心要点 2: 发现分层交叉现象——语义轴对齐高层视觉皮层+深层DNN，低级视觉轴对齐早期皮层+浅层
   413|   280|   227|  - **Activation**: naturality violation score, NVS, brain-DNN alignment, transformation alignment, category theory neuroscience, hierarchy crossover
   414|   281|   228|
   415|   282|   229|## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum Mechanics (Cron Job)
   416|   283|   230|
   417|   284|   231|### Beyond Gates: Pulse Level Quantum Fourier Models
   418|   285|   232|- [[pulse-level-quantum-fourier]] - 脉冲级量子傅里叶模型参数化，通过独立子角调优提升QML训练性能 (arXiv: 2605.04945)
   419|   286|   233|  - 核心要点 1: 独立脉冲缩放替代单一逻辑角，释放高维梯度下降逃逸路径
   420|   287|   234|  - 核心要点 2: 复合门中子角独立性显著提升训练性能，但不改变全局表达能力
   421|   288|   235|  - **Activation**: 脉冲级量子计算, 量子傅里叶模型, QML优化, pulse-level QFM, composite gate optimization
   422|   289|   236|
   423|   290|   237|### Block Permutation Routing on Ramanujan Hypergraphs for Fault-Tolerant Quantum Computing
   424|   291|   238|- [[ramanujan-hypergraph-routing]] - Ramanujan超图上的块排列路由用于容错量子计算 (arXiv: 2605.05036)
   425|   292|   239|  - 核心要点 1: Ramanujan超图上的块排列路由，保持谱比的高连通性
   426|   293|   240|  - 核心要点 2: 谱继承三层级：精确(Haemers)、扰动(Weyl)、通用(Cheeger)
   427|   294|   241|  - **Activation**: 量子路由, 表面编码, 超图变换, QCCD架构, fault-tolerant routing, block permutation
   428|   295|   242|
   429|   296|   243|### Integral Means Spectrum for the Random Riemann Zeta Function
   430|   297|   244|- [[random-riemann-zeta-spectrum]] - 随机黎曼ζ函数积分均值谱证明Kraetzer猜想 (arXiv: 2603.26507)
   431|   298|   245|  - 核心要点 1: 随机ζ函数原函数的积分均值谱几乎必然符合Kraetzer猜想形式
   432|   299|   246|  - 核心要点 2: 建立ζ函数临界线收敛到全纯GMC分布的替代推导
   433|   300|   247|  - **Activation**: 黎曼ζ函数, 积分均值谱, 高斯乘性混沌, Kraetzer猜想, 单叶函数
   434|   301|   248|
   435|   302|   249|### The true cost of factoring: Linking magic and number-theoretic complexity in Shor's algorithm
   436|   303|   250|- [[quantum-magic-complexity]] - 量化Shor算法中magic资源，建立数论问题经典难度与量子非稳定子资源的直接联系 (arXiv: 2605.05347)
   437|   304|   251|  - 核心要点 1: Magic(non-stabilizerness)是量子超越经典计算的关键资源，Shor算法在实用参数下最大化利用该资源
   438|   305|   252|  - 核心要点 2: 经典算法难度与解决该问题所需的非稳定子价格成正比，补充传统电路成本分析
   439|   306|   253|  - **Activation**: quantum magic complexity, non-stabilizerness, Shor algorithm resource, magic state distillation, stabilizer formalism, fault-tolerant overhead
   440|   307|   254|
   441|   308|   255|### Quantum Proper Scoring Rules: Minimax Estimation and Resource-Theoretic Advantages
   442|   309|   256|- [[quantum-proper-scoring-rules]] - 将适当评分规则推广到量子领域，用密度算子替代概率分布，推导量子态层析minimax最优界 (arXiv: 2605.05268)
   443|   310|   257|  - 核心要点 1: 通过算子凸生成元定义量子值泛函，建立量子Cramér-Rao-McCarthy界，连接minimax风险与量子Fisher信息
   444|   311|   258|  - 核心要点 2: 量化相干性、纠缠、自适应性等量子资源在预测任务中的经济价值，证明经典-量子缩放分离
   445|   312|   259|  - **Activation**: quantum proper scoring rules, quantum state estimation, quantum Fisher information, minimax quantum, quantum Cramer-Rao bound, quantum resource economics
   446|   313|   260|
   447|   314|   261|### Analytical Angle-Finding for QSP via Orthogonal Polynomial Theory
   448|   315|   262|- [[qsp-orthogonal-polynomials]] - 利用Hermite/Jacobi/Rogers-Szego多项式正交性，为量子信号处理提供旋转角度解析解 (arXiv: 2605.05321)
   449|   316|   263|  - 核心要点 1: QSP可实现多项式基由正交性/双正交性刻画，2n+2个角度编码次数≤n的多项式序列
   450|   317|   264|  - 核心要点 2: 光滑函数ε近似可通过Hermite级数展开以O(log(1/ε))个门实现块编码
   451|   318|   265|  - **Activation**: QSP angle finding, quantum signal processing, orthogonal polynomial, Hermite QSP, block encoding, SU(1,1)-QSP
   452|   319|   266|
   453|   320|   267|### Universal Neural Propagator: Learning Time Evolution in Many-Body Quantum Systems
   454|   321|   268|- [[quantum-neural-propagator]] - 学习从驱动协议到时间演化传播子的泛函映射，在驱动空间和指数大初态空间上同时预测量子动力学 (arXiv: 2605.05299)
   455|   322|   269|  - 核心要点 1: 从学习量子态转向学习算子，单个UNP模型覆盖函数空间的驱动协议和希尔伯特空间的初态
   456|   323|   270|  - 核心要点 2: 自监督训练，在超出精确对角化能力的系统尺寸上保持准确，可仅用可观测量数据微调
   457|   324|   271|  - **Activation**: universal neural propagator, quantum dynamics learning, quantum foundation model, driven quantum systems, time evolution propagator, transferable simulation
   458|   325|   272|
   459|   326|   273|### Semantics-Based Verification of Shor Oracle for ECDLP
   460|   327|   274|- [[quantum-program-semantic-verification]] - 量子程序语义验证方法，针对Shor类数论算法的群操作预言机进行语义级规范和精化验证 (arXiv: 2605.01008)
   461|   328|   275|  - 核心要点 1: Shor类ECDLP算法对群操作预言机的语义高度敏感，微小实现选择可使数学模型失效
   462|   329|   276|  - 核心要点 2: 即使通过平凡控制健全性检查，受控执行仍可能违反预期控制律，语义审计是可信量子软件的必要前提
   463|   330|   277|  - **Activation**: quantum program verification, Shor oracle, ECDLP quantum, semantic auditing, Qrisp verification, refinement verification, number-theoretic algorithms
   464|   331|   278|
   465|   332|   279|### Beating Noise in Frequency Estimation with Squeezing and Memory
   466|   333|   280|- [[quantum-noise-robust-metrology]] - 连续变量系统中的量子计量方法，通过哈密顿工程(压缩)和非马尔可夫环境记忆实现抗噪频率估计 (arXiv: 2605.06263)
   467|   334|   281|  - 核心要点 1: 将压缩嵌入系统哈密顿使QFI获得可调高阶时间依赖性，短时区灵敏度超越标准估计
   468|   335|   282|  - 核心要点 2: 结构化环境的非马尔可夫记忆可诱导信息回流，暂时恢复甚至超过无噪声估计极限
   469|   336|   283|  - **Activation**: quantum metrology, frequency estimation, quantum Fisher information, squeezing, non-Markovian, continuous-variable, noise mitigation, quantum sensing
   470|   337|   284|
   471|   338|   285|## 2026-05-08 - Neuroscience Research (Cron Job)
   472|   339|   286|
   473|   340|   287|### TRIBE v2: A Tri-Modal Brain Foundation Model
   474|   341|   288|- [[tribev2-brain-foundation-model]] - 三模态(视频/音频/语言)脑活动预测基础模型，统一预测1000+小时fMRI、720被试的高分辨率脑响应，实现in-silico神经科学实验 (arXiv: 2605.04326)
   475|   342|   289|  - 核心要点 1: Transformer架构整合三模态特征，通过modality dropout学习鲁棒跨模态表征，显著超越传统线性编码模型
   476|   343|   290|  - 核心要点 2: 支持零样本泛化到新刺激/任务/被试，通过subject block插值实现未见被试预测，可恢复数十年实证研究结果
   477|   344|   291|  - **Activation**: TRIBE v2, brain foundation model, fMRI encoding, multimodal brain prediction, in-silico neuroscience, Algonauts challenge, naturalistic fMRI
   478|   345|   292|
   479|   346|   293|### Neural Manifolds as Crystallized Embeddings
   480|   347|   294|- [[neural-manifolds-crystallized-embeddings]] - 神经流形结晶嵌入理论：整合自由能原理、广义同步和Hebbian可塑性，解释头方向/网格细胞/视觉流形的发育机制 (arXiv: 2605.04200)
   481|   348|   295|  - 核心要点 1: 广义同步将低维感觉流形嵌入神经状态空间，FEP预测的几何结构从普通循环动力学中自然涌现，而非显式贝叶斯计算
   482|   349|   296|  - 核心要点 2: Hebbian可塑性将同步产生的相关性结晶为循环连接，形成自治连续吸引子网络；成熟流形是发育产物而非基因预设模板
   483|   350|   297|  - **Activation**: neural manifolds, free energy principle, generalized synchronization, Hebbian plasticity, continuous attractor networks, reservoir computing, developmental neuroscience
   484|   351|   298|
   485|   352|   299|## 2026-05-08 - CSS QEC / Hypergraph Routing / Adaptivity Theory (Cron Hourly)
   486|   353|   300|
   487|   354|   301|### A Factor-Graph Formulation of CSS Syndrome Decoding
   488|   355|   302|- [[css-factor-graph-decoding]] - CSS量子纠错症状解码的因子图表述，联合BP与四态BP的等价性证明 (arXiv: 2605.05132)
   489|   356|   303|  - 核心要点 1: 两个Tanner图通过每个量子比特的联合先验耦合，保留X/Z误差分量的信道相关性
   490|   357|   304|  - 核心要点 2: 联合BP与四态BP在状态重标记后计算相同的后验权重、消息和信念
   491|   358|   305|  - **Activation**: CSS syndrome decoding, factor graph QEC, joint belief propagation, four-state BP, Tanner graph coupling, stabilizer code decoder
   492|   359|   306|
   493|   360|   307|### Block Permutation Routing on Ramanujan Hypergraphs
   494|   361|   308|- [[ramanujan-hypergraph-quantum-routing]] - 拉马努金超图上的块置换路由用于容错量子计算，谱分析给出路由复杂度界 (arXiv: 2605.05036)
   495|   362|   309|  - 核心要点 1: 商图谱的谱比在高连通性区域保持，三级谱继承：精确/扰动/通用
   496|   363|   310|  - 核心要点 2: 结合相关解码方案将症状提取开销从O(d²)降至O(d)，路由成为主导项
   497|   364|   311|  - **Activation**: quantum routing, Ramanujan hypergraph, surface code patch routing, fault-tolerant circuit depth, spectral graph bounds, lattice surgery compilation
   498|   365|   312|
   499|   366|   313|### Adaptivity Under Realizability Constraints
   500|   367|   314|- [[adaptivity-realizability-constraints]] - 可实现性约束下自适应性的理论分析，揭示ICL与Agentic Learning的四种场景 (arXiv: 2605.04995)
   501|   368|   315|  - 核心要点 1: 四种场景：无优势/持续优势/仅约束下涌现优势/约束下消失优势
   502|   369|   316|  - 核心要点 2: ReLU可实现性根本性地改变自适应查询的效用，反直觉场景(c)值得注意
   503|   370|   317|  - **Activation**: in-context learning vs agentic, adaptivity theory, realizability constraints, ReLU network approximation, adaptive querying strategy
   504|   371|   318|
   505|   372|   319|## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job)
   506|   373|   320|
   507|   374|   321|### Beyond Gates: Pulse Level Quantum Fourier Models
   508|   375|   322|- [[pulse-level-quantum-fourier-models]] - 脉冲级量子傅里叶模型训练优化方法，通过独立脉冲缩放替换门级参数，松弛局部优化景观，显著提升训练性能 (arXiv: 2605.03xxx)
   509|   376|   323|  - 核心要点 1: 脉冲参数化将单一门角度替换为多个独立可调子角度，为梯度下降提供高维逃逸路径
   510|   377|   324|  - 核心要点 2: 脉冲控制不显著改变全局可表达性，但根本性改变局部优化景观
   511|   378|   325|  - **Activation**: pulse-level quantum computing, quantum Fourier models, QFM training optimization, pulse parameterized quantum circuits, quantum ML hardware control
   512|   379|   326|
   513|   380|   327|### Quantum Prediction of Transport Dynamics in Discretized State Spaces
   514|   381|   328|- [[quantum-bayesian-state-estimation]] - 基于门量子计算机的贝叶斯状态估计算法，使用Wick旋转将扩散转化为色散相位演化，实现Fokker-Planck方程的酉传播 (arXiv: 2604.xxxxx)
   515|   382|   329|  - 核心要点 1: 概率密度编码在量子态振幅中，状态空间随量子比特数指数增长
   516|   383|   330|  - 核心要点 2: 漂移分量在振幅空间中可实现精确线性操作，扩散分量通过Wick旋转实现酉代理
   517|   384|   331|  - **Activation**: quantum Bayesian estimation, Fokker-Planck quantum solver, quantum state prediction, amplitude-encoded probability, Wick rotation diffusion
   518|   385|   332|
   519|   386|   333|### Towards sample-optimal learning of bosonic Gaussian quantum states
   520|   387|   334|- [[sample-optimal-gaussian-state-learning]] - 玻色高斯量子态学习的最优样本复杂度分析，证明Gaussian测量下界Ω(n³/ε²)，任意测量下界Ω(n²/ε²) (arXiv: 2603.xxxxx)
   521|   388|   335|  - 核心要点 1: 纯Gaussian态可用Gaussian测量达到最优，被动Gaussian态需要非Gaussian测量
   522|   389|   336|  - 核心要点 2: 自适应测量对近能量无关缩放不可或缺
   523|   390|   337|  - **Activation**: Gaussian state tomography, sample complexity quantum learning, bosonic state characterization, continuous-variable quantum learning, adaptive quantum measurement
   524|   391|   338|
   525|   392|   339|## 2026-05-08 - Quantum Error Correction (Cron Job)
   526|   393|   340|
   527|   394|   341|### Topological subsystem bivariate bicycle codes with four-qubit check operators
   528|   395|   342|- [[sbb-codes]] - 子系统二元自行车码(SSB)方法，将BB码的高权稳定子检查(≥6)分解为局域权-4规范测量，实现高率qLDPC码的实用化 syndrome extraction (arXiv: 2605.04151)
   529|   396|   343|  - 核心要点 1: CSS子系统构造 — 通过权-4规范算子乘积推断稳定子症状，兼容超导量子比特架构
   530|   397|   344|  - 核心要点 2: 行列式理想判据 — 检测平移不变CSS子系统中是否存在非局域稳定子，决定能否用有限深度Clifford电路解耦规范量子比特
   531|   398|   345|  - 核心要点 3: 已知低开销实例 — [[27,6,3]], [[75,10,5]], [[108,12,6]]，后者在相同码长和距离下比子系统面码多编码6倍逻辑量子比特
   532|   399|   346|  - **Activation**: sbb codes, subsystem bicycle codes, weight-4 qec, bb code syndrome, gauge measurement qec, low-overhead quantum memory, subsystem qldpc
   533|   400|   347|
   534|   401|   348|## 2026-05-08 - Neuroscience Research (Cron Job - Evening)
   535|   402|   349|
   536|   403|   350|### Benchmarking local Hebbian learning rules for memory storage and prototype extraction
   537|   404|   351|- [[hebbian-learning-benchmark-memory]] - 系统评测七种赫布学习规则在联想记忆中的存储容量、原型提取能力和对数据相关性的鲁棒性，贝叶斯-赫布规则在几乎所有条件下表现最优 (arXiv: 2605.01074)
   538|   405|   352|  - 核心要点 1: 加法赫布规则容量最差，协方差学习鲁棒但容量中等，贝叶斯-赫布规则几乎在所有条件下容量最高
   539|   406|   353|  - 核心要点 2: 模块化WTA架构优于非模块化，在存储和原型提取任务中均表现更好
   540|   407|   354|  - **Activation**: hebbian learning benchmark, associative memory, prototype extraction, memory capacity, Bayesian-Hebbian, covariance learning, WTA dynamics, binary pattern storage
   541|   408|   355|
   542|   409|   356|## 2026-05-08 - Systems Engineering Research (Cron Job)
   543|   410|   357|
   544|   411|   358|### Safety by Invariance, Liveness through Refinement: Heterogeneous Contract Framework for Co-Design of Layered Control
   545|   412|   359|- [[heterogeneous-contract-control]] - 基于异构假设-保证契约的分层控制架构协同设计方法，将安全性与活性分解到连续时间安全层和离散时间规划层 (arXiv: 2605.04222)
   546|   413|   360|  - 核心要点 1: 安全-活性分解原则 — CT层单方面执行安全性(鲁棒前向不变性)，DT层双边实现活性(收敛)
   547|   414|   361|  - 核心要点 2: 垂直精化条件 — 通过显式参考总督(ERG)作为契约实现器，避免CBF-QP对低层控制器的干扰
   548|   415|   362|  - **Activation**: layered control, heterogeneous contract, assume-guarantee, safety liveness, vertical refinement, explicit reference governor, contract-based design
   549|   416|   363|
   550|   417|   364|### Experiment-as-Code Labs: A Declarative Stack for AI-Driven Scientific Discovery
   551|   418|   365|- [[experiment-as-code-labs]] - 将实验编码为声明式配置的AI驱动科学发现栈，借鉴云IaC理念实现物理实验室自动化 (arXiv: 2605.04375)
   552|   419|   366|  - 核心要点 1: 三层架构 — 规范层(标准化/可复现)、执行层(安全/可靠)、编排层(可扩展/高效)
   553|   420|   367|  - 核心要点 2: 集中式实验室状态模型 — 设备遥测实时更新状态，支持闭环迭代和安全验证
   554|   421|   368|  - **Activation**: experiment-as-code, EaC lab, autonomous lab, declarative experiment, lab automation, AI scientist
   555|   422|   369|
   556|   423|   370|
   557|   424|   371|### Learning Reveals Invisible Structure in Low-Rank RNNs
   558|   425|   372|- [[low-rank-rnn-learning-dynamics]] - Gradient-descent learning dynamics in low-rank RNNs decomposed into loss-visible (determines function) and loss-invisible (encodes training history) overlaps, explaining why functionally equivalent networks learn differently (arXiv: 2605.04115)
   559|   426|   373|  - Core: Closed-form ODEs for learning in reduced overlap space; exact for linear, asymptotically exact for nonlinear large-N RNNs
   560|   427|   374|  - Key: Loss-invisible overlaps act as memory variables; learning exposes connectivity differences between functionally equivalent networks
   561|   428|   375|  - **Activation**: low-rank RNN learning, RNN overlap space, loss-visible invisible, RNN gradient descent dynamics, RNN learning theory, Ger Barak RNN
   562|   429|   376|
   563|   430|   377|## 2026-05-08 - Neuroscience Research (Cron Job)
   564|   431|   378|
   565|   432|   379|### Dissociating Spatial Frequency Reliance from Adversarial Robustness in Neurally Guided DCNNs
   566|   433|   380|- [[neurally-guided-adversarial-robustness]] - Neural alignment's adversarial robustness stems from representational structure, not spatial frequency bias; LSF/human-channel steering fails to match alignment gains (arXiv: 2605.04443)
   567|   434|   381|  - Core: Dissociation experiment shows frequency bias ≠ robustness mechanism; representational geometry is key
   568|   435|   382|  - Key: Human channel + LSF bias impairs robustness; RSA reveals alignment captures higher-order properties
   569|   436|   383|  - **Activation**: neural alignment robustness, adversarial DCNN defense, spatial frequency analysis, ventral stream modeling, brain-inspired CNN robustness
   570|   437|   384|
   571|   438|   385|### phys-MCP: Control Plane for Heterogeneous Physical Neural Networks
   572|   439|   386|- [[phys-mcp-physical-neural-networks]] - Substrate-aware orchestration for PNNs (molecular, chemical, biological, photonic, memristive, mechanical) with capability models, lifecycle semantics, telemetry, digital-twin bindings, and wetware API (arXiv: 2605.04256)
   573|   440|   387|  - Core: Unified control plane exposing heterogeneous physical neural substrates as discoverable resources
   574|   441|   388|  - Key: Cortical Labs wetware adapter validated; runtime-aware matching + telemetry recovery across backends
   575|   442|   389|  - **Activation**: phys-MCP, physical neural network orchestration, wetware computing, substrate-aware control, neuromorphic edge computing
   576|   443|   390|
   577|   444|   391|## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job)
   578|   445|   392|
   579|   446|   393|### Lottery BP: Unlocking Quantum Error Decoding at Scale
   580|   447|   394|- [[lottery-bp-decoding]] - Randomized belief propagation improves quantum decoding accuracy by 2-8 orders of magnitude for topological codes, with PolyQec architecture reducing OSD calls by 3-5 orders (arXiv: 2605.00038)
   581|   448|   395|  - Core: Lottery BP introduces randomness during BP decoding to break error degeneracy in QLDPC codes
   582|   449|   396|  - Key: Syndrome vote pre-processing compresses multi-round measurements; PolyQec = local BP + global OSD hierarchy
   583|   450|   397|  - **Activation**: quantum error correction decoding, belief propagation randomized, QLDPC scalable decoding, PolyQec architecture, syndrome voting, topological code decoding
   584|   451|   398|
   585|   452|   399|### Hyperspectral Anomaly Detection Using Einstein Fuzzy Computing and Quantum Neural Network
   586|   453|   400|- [[hyfu-had-quantum-fuzzy]] - Hybrid quantum-fuzzy framework for hyperspectral anomaly detection using Einstein fuzzy computing and quantum defuzzifier, achieving state-of-the-art performance (arXiv: 2605.04388)
   587|   454|   401|  - Core: Multi-criteria decision framework combining classical fuzzy rules (Einstein sum/product) with lightweight quantum defuzzifier
   588|   455|   402|  - Key: Einstein fuzzy operations provide smoother transitions than min-max; quantum defuzzifier processes aggregated fuzzy features
   589|   456|   403|  - **Activation**: hyperspectral anomaly detection, Einstein fuzzy computing, quantum neural network, fuzzy multi-criteria decision, quantum defuzzifier, remote sensing
   590|   457|   404|
   591|   458|   405|### Construction and Decoding of Quantum Margulis Codes
   592|   459|   406|- [[quantum-margulis-codes]] - New QLDPC codes from Margulis construction via 2BGA framework, decodable with linear-complexity min-sum decoder unlike BB codes requiring OSD (arXiv: 2503.03936)
   593|   460|   407|  - Core: Margulis codes break Tanner graph group symmetry, mitigating error degeneracy for efficient min-sum decoding
   594|   461|   408|  - Key: Girth-controlled construction (6 or 8); 2-8 orders magnitude better error floor than BB codes
   595|   462|   409|  - **Activation**: quantum Margulis codes, QLDPC code design, min-sum quantum decoding, 2BGA framework, girth-controlled codes, quantum error correction codes
   596|   463|   410|
   597|   464|   411|### Quantum metrology of mixed states via purification
   598|   465|   412|- [[quantum-statistical-metrology]] - Purification-based strategies achieve optimal QCRB and HCRB bounds for multi-parameter quantum estimation, resolving open question about mixed state precision limits (arXiv: 2605.03975)
   599|   466|   413|  - Core: Mixed state quantum metrology via purification; QCRB and HCRB achievable through purified system measurements
   600|   467|   414|  - Key: Any mixed state estimation reduces to equivalent pure state problem; optimal precision bounds proven achievable
   601|   468|   415|  - **Activation**: quantum metrology, quantum estimation, cramér-rao bound, quantum statistics, purification strategy, holevo bound, quantum state discrimination
   602|   469|   416|
   603|   470|   417|### Optimal Error Exponents for Composite Sequential Quantum Hypothesis Testing
   604|   471|   418|- [[quantum-statistical-metrology]] - Sequential quantum hypothesis testing with composite alternatives achieves optimal error exponents via convex optimization (arXiv: 2605.04915)
   605|   472|   419|  - Core: Distinguishing null quantum state from convex set of alternatives with minimal measurements
   606|   473|   420|  - Key: Error exponent analysis for quantum state discrimination; sequential measurement optimization
   607|   474|   421|  - **Activation**: quantum hypothesis testing, sequential quantum testing, quantum state discrimination, error exponents, composite alternatives
   608|   475|   422|
   609|   476|   423|## 2026-05-08 - Neuroscience Research (Cron Job)
   610|   477|   424|
   611|   478|   425|### GeoSAE: Geometric Prior-Guided Layer-Wise Sparse Autoencoder Annotation of Brain MRI Foundation Models
   612|   479|   426|- [[geosae-brain-mri-sae]] - Geometry-guided SAE prevents feature collapse in deep transformer layers, extracts interpretable Alzheimer's biomarkers from frozen brain MRI foundation models with age-deconfounded partial correlations (arXiv: 2605.01829)
   613|   480|   427|  - Core: GeoSAE uses foundation model's learned manifold geometry to guide SAE training; age-deconfounded partial correlations isolate disease-specific signals
   614|   481|   428|  - Key: MCI-to-AD AUC 0.746 with 2% embedding dims; cross-cohort replication r=0.97; neuroanatomical localization consistent with Braak staging
   615|   482|   429|  - **Activation**: GeoSAE, brain MRI foundation model interpretability, sparse autoencoder medical imaging, Alzheimer's biomarker, SAE feature collapse, age-deconfounded analysis, Braak staging localization
   616|   483|   430|
   617|   484|   431|## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job)
   618|   485|   432|
   619|   486|   433|### Towards sample-optimal learning of bosonic Gaussian quantum states
   620|   487|   434|- [[bosonic-gaussian-state-learning]] - Sharp sample complexity bounds for learning n-mode Gaussian states: Omega(n^3/epsilon^2) for Gaussian measurements, non-Gaussian required for passive states (arXiv: 2603.18136)
   621|   488|   435|  - Core: Lower/upper bounds on copies needed to learn Gaussian states to epsilon trace distance; adaptivity indispensable for energy-independent scaling
   622|   489|   436|  - Key: Non-Gaussian measurements provably required for optimal passive state learning; Gaussian measurements nearly optimal for pure states
   623|   490|   437|  - **Activation**: bosonic Gaussian state learning, quantum state tomography sample complexity, continuous-variable quantum learning, Gaussian measurement bounds, passive Gaussian state, quantum state estimation efficiency
   624|   491|   438|
   625|   492|   439|### Finite steps optimise dissipation in stochastically controlled quantum systems
   626|   493|   440|- [[stochastic-quantum-dissipation]] - Thermodynamic cost analysis reveals weak Gaussian noise induces dissipation growing linearly with step count, establishing optimal N* trade-off (arXiv: 2605.04681)
   627|   494|   441|  - Core: Stochastic control noise accumulates linearly across steps, creating optimal step count minimizing total dissipation
   628|   495|   442|  - Key: Conventional 'more steps = better' fails under noise; D_total = D_deterministic + sigma^2 * k * N
   629|   496|   443|  - **Activation**: quantum dissipation, stochastic quantum control, step-equilibration thermodynamics, quantum thermodynamic cost, Gaussian noise quantum control, finite-step quantum optimization
   630|   497|   444|
   631|   498|   445|### Quantum Error Correction Exploiting Quantum Spatial Distribution and Gauge Symmetry
   632|   499|   446|- [[quantum-spatial-error-correction]] - QEC using spin-position superposition and gauge symmetry, resilient to spin/position decoherence and joint dephasing with nearest-neighbor interactions only (arXiv: 2604.25747)
   633|   500|   447|  - Core: 3+2 particle nested square encoding Shor's code; gauge symmetry protects against unified noise model
   634|   501|