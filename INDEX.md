## 2026-05-15 - Neuroscience Research (Cron Job)

### Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale
- [[mamba-spike-behavioral-decoding]] - Mamba forecaster trained on spike prediction implicitly encodes behavioral information, enabling closed-loop BCI without separate decoding networks (arXiv: 2605.12999)
  - 核心要点: 单一 Mamba 模型训练 spike rate prediction，其预测的 firing rates 隐含行为信息，无需 behavioral labels 即可解码行为
  - 核心要点: 在 Steinmetz benchmark 上，Mamba 预测 rates 解码小鼠选择达 75.7%（2.3x chance），超过 matched-context raw spike baselines 4-6 pp
  - 核心要点: Population shuffle test 证明 Mamba 利用 cross-neuron coupling（shuffle 后 r 下降 48.4%），而非单神经元自相关
  - **Activation**: mamba forecaster, spike forecast behavioral decoding, implicit behavioral decoding, neural population rate prediction

### Embodied Neurocomputation: A Framework for Interfacing Biological Neural Cultures
- [[embodied-neurocomputation-framework]] - Systems-level framework for bio-silicon computing interfaces, validated through large-scale parameter optimization of BNN agents in goal-driven navigation (arXiv: 2605.13315)
  - 核心要点: 形式化 Embodied Neurocomputation 框架为四模块优化问题（编码-生物转换-解码-反馈），首次大规模优化 BNN encoding 参数
  - 核心要点: 筛选 1,296 种 encoding 配置、4,000+ 小时实时交互，找到 12 种稳定学习的配置，性能超过同等训练预算的 DQN
  - 核心要点: SHAP 分析揭示 max frequency (40-60 Hz)、higher amplitude、shorter pulse width 为关键参数
  - **Activation**: embodied neurocomputation, biological neural network computing, MEA neurocomputation, bio-silicon computing

## 2026-05-15 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)

### Provable and Scalable Quantum Gaussian Processes for Quantum Learning
- [[quantum-gaussian-processes]] - Bayesian framework for learning from quantum systems through priors over unknown quantum transformations, enabling regression, classification, and Bayesian optimization directly on quantum data using quantum kernels. Provable and scalable for matchgate/free-fermionic evolutions (arXiv: 2605.00099)
  - 核心要点: 量子高斯过程将unitary量子随机过程定义为高斯过程，通过量子核注入物理先验进行贝叶斯学习
  - 核心要点: 证明matchgate/free-fermion演化产生可证明且可扩展的QGP，是首个未知unitary作用于所有量子比特的族
  - 核心要点: 应用于长程外推、多体系统相图学习、量子传感贝叶斯优化
  - **Activation**: quantum gaussian process, QGP, quantum kernel, bayesian quantum learning, free-fermion learning, quantum Bayesian optimization

### Efficient Quantum Fourier Transforms For Semisimple Algebras
- [[semisimple-algebra-qft]] - Generalizes QFT from finite groups to finite-dimensional semisimple algebras (partition, Brauer, walled Brauer), with gate complexity poly(n, log d, log(1/ε)) via unitary approximation when parameter d is large (arXiv: 2605.05337)
  - 核心要点: 代数傅里叶变换可以是非酉的，但当参数d足够大时可被酉算子良好逼近
  - 核心要点: 给出分割代数、Brauer代数、墙Brauer代数的有效量子傅里叶变换
  - 核心要点: 连接数论（Schur-Weyl对偶）、统计物理和量子算法
  - **Activation**: quantum Fourier transform, semisimple algebra, Brauer algebra, partition algebra, Schur-Weyl duality, algebra QFT

### Optimal Error Exponents for Composite Sequential Quantum Hypothesis Testing
- [[sequential-quantum-hypothesis-testing]] - Mixture-sequential quantum probability ratio test for distinguishing null quantum states from sets of alternatives, achieving optimal Type-I and Type-II error exponents characterized by minimal measured relative entropies (arXiv: 2605.04915)
  - 核心要点: 复合假设检验通过混合估计自适应选择测量，实现对数似然比阈值停止
  - 核心要点: 同时达到最优Type-I和最坏情况Type-II错误指数
  - 核心要点: 复合SQHT样本复杂度至少等于两固定状态间序贯检验
  - **Activation**: sequential quantum hypothesis testing, SQHT, quantum probability ratio test, quantum state discrimination, composite hypothesis testing

### Cloning is as Hard as Learning for Stabilizer States
- [[quantum-cloning-learning-equivalence]] - Proves that for n-qubit stabilizer states, optimal cloning sample complexity is Θ(n), matching learning complexity exactly — cloning is as hard as learning even for this structured class (arXiv: 2604.15269)
  - 核心要点: 稳定器态克隆最优样本复杂度为Θ(n)，与学习复杂度完全相等
  - 核心要点: 使用Abelian State Hidden Subgroup框架和随机纯化通道连接量子克隆与经典样本放大
  - 核心要点: 为No-Cloning定理提供细粒度视角，打开量子学习理论与密码学联系
  - **Activation**: quantum cloning, quantum learning theory, stabilizer states, sample complexity, No-Cloning theorem, sample amplification


### Neural QAOA²: Differentiable Joint Graph Partitioning and Parameter Initialization for Quantum Combinatorial Optimization
- [[neural-qaoa-optimization]] - Uses neural networks for differentiable graph partitioning and parameter initialization in QAOA, addressing poor partitioning quality and random parameter initialization for scalable NISQ optimization (arXiv: 2605.13051)
  - 核心要点: 神经网络联合优化图分割和QAOA参数初始化，解决分治QAOA的两大瓶颈
  - 核心要点: 可微分割允许梯度优化，迁移学习避免随机初始化的barren plateau
  - 核心要点: 子图独立执行QAOA后经典后处理组合解
  - **Activation**: neural qaoa, quantum combinatorial optimization, graph partitioning quantum, differentiable qaoa, NISQ optimization

### Phase Matching for a Generalized Grover's Algorithm
- [[quantum-grover-optimization]] - Studies optimal phase changes per iteration in generalized Grover's algorithm, proving classical phase matching (π) is optimal until target probability approaches 1 (arXiv: 2605.13758)
  - 核心要点: 经典相位匹配在目标概率接近1前始终最优
  - 核心要点: 高概率区域最优相位偏离π，需要优化框架
  - 核心要点: 提供完整优化框架用于广义Grover算法相位序列设计
  - **Activation**: grover algorithm optimization, quantum search optimization, grover phase matching, generalized grover

### Quantum Precoded Polar Codes
- [[quantum-precoded-polar-codes]] - CSS quantum error-correcting codes from rate-1 precoded polar codes, optimized via genetic algorithms for improved logical error rates (arXiv: 2605.12656)
  - 核心要点: 从经典速率1预编码极化码构建CSS量子纠错码
  - 核心要点: 遗传算法优化速率分布和预编码器
  - 核心要点: 短码长下展示改进的逻辑错误率
  - **Activation**: quantum polar codes, CSS codes, quantum error correction codes, precoded polar codes


### On the Spectral Theory of Isogeny Graphs and Quantum Sampling of Secure Supersingular Elliptic Curves
- [[isogeny-graph-quantum-sampling]] - First provable quantum polynomial-time algorithms for sampling supersingular elliptic curves with unknown endomorphism rings, based on spectral theory of isogeny graphs (arXiv: 2602.02263)
  - Spectral gap analysis of Ramanujan isogeny graphs determines mixing time
  - Quantum-enhanced random walk hides endomorphism ring structure
  - Applicable to isogeny-based cryptographic protocols (SIKE, CSIDH)
  - **Activation**: isogeny graph sampling, supersingular elliptic curves, quantum curve generation, 同源图采样

### Multi-Qubit Golden Gates
- [[multi-qubit-golden-gates]] - Construction of optimal topological generators for compact unitary Lie groups, extending golden gates to multi-qubit systems via Sarnak-Xue Density Hypothesis (arXiv: 2509.09047)
  - Algebraic number theory produces explicit generators for SU(2^n)
  - Uniform spectral gap independent of dimension
  - Near-optimal O(log(1/ε)) word length for ε-approximation
  - **Activation**: golden gates, multi-qubit gate synthesis, Sarnak-Xue hypothesis, 黄金门

### Tight Quantum-Security Bounds and Parameter Optimization for SPHINCS+ and NTRU
- [[post-quantum-crypto-security-bounds]] - Tight security bounds for NIST PQC finalists incorporating decoherence effects and parallelization limits, reducing SPHINCS+ parameters by 15-20% (arXiv: 2508.19250)
  - Quantum attack model with realistic hardware constraints
  - Entropy concentration inequalities for parameter reduction
  - Quantum lattice entropy H_Q(Λ) for NTRU optimization
  - **Activation**: post-quantum cryptography security, SPHINCS+ parameter optimization, NIST PQC evaluation

## 2026-05-15 - Neuroscience Research (Cron Job)

### FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping
- [[fits-interpretable-spiking-neuron]] - Spiking neuron factorizing temporal computation into Frequency Selectivity (FS) and Temporal Shaping (TS) modules, providing interpretable neuron-level frequency and timing summaries (arXiv: 2605.13071)
  - FS parameterizes each neuron's target frequency as maximizer of subthreshold magnitude response
  - TS reshapes when frequency components contribute via group-delay modulation
  - Outperforms LIF in feedforward SNNs without recurrence or delays on auditory benchmarks (SHD, SSC, GSC)
  - **Activation**: FiTS, interpretable spiking neuron, frequency selectivity SNN, temporal shaping, group-delay modulation, auditory SNN, SHD SSC

### Multi-Timescale Conductance Spiking Networks
- [[multi-timescale-conductance-snn]] - Gradient-trainable SNN framework where neural dynamics emerge from shaping I-V curve via fast/slow/ultra-slow conductances, supporting tonic/phasic/bursting regimes without surrogate gradients (arXiv: 2605.11835)
  - Direct BPTT without surrogate-gradient approximations
  - Single model exhibits tonic, phasic, and bursting firing regimes
  - Outperforms LIF and AdLIF on Mackey-Glass regression with substantially sparser activity
  - **Activation**: MTCSN, multi-timescale conductance SNN, conductance-based spiking, surrogate-gradient-free, Mackey-Glass SNN, tonic phasic bursting

## 2026-05-15 - Deep Learning Research (Cron Job)

### Attention Once Is All You Need: Efficient Streaming Inference with Stateful Transformers
- [[stateful-streaming-transformer-inference]] - Stateful session model with persistent KV cache enabling O(|q|) query latency and Flash Queries speculative prefetching for streaming workloads (arXiv: 2605.13784)
  - Persistent KV cache advances incrementally, moving prefill off critical path
  - Flash Queries reclaim idle GPU cycles to pre-evaluate and cache answers before user asks
  - Multi-tenant continuous-batching with cell-budget admission and prefix-aware grouped prefill
  - **Activation**: stateful inference, streaming LLM, KV cache persistent, flash queries, continuous batching

### DisAgg: Distributed Aggregators for Efficient Secure Aggregation in Federated Learning
- [[disaggregate-secure-aggregation-fl]] - Federated learning protocol using small aggregator committees for secret-sharing-based aggregation, eliminating homomorphic encryption overhead (arXiv: 2605.13708)
  - Client committee performs aggregation instead of central server
  - Eliminates local masking and expensive homomorphic encryption
  - 4.6x speedup over OPA for 100k-dimensional vectors from 100k clients
  - **Activation**: secure aggregation federated learning, DisAgg, secret sharing aggregation, federated learning privacy

### Rethinking Efficient Graph Coarsening via a Non-Selfishness Principle
- [[nope-non-selfish-graph-coarsening]] - NOPE graph coarsening using collective neighborhood interference instead of pairwise similarity, achieving near-linear complexity (arXiv: 2605.13021)
  - Non-selfishness principle prioritizes collective neighborhood over individual node matching
  - NOPE* reduces O(δ·d) to O(d) evaluation via local isotropy assumption
  - 1-3 orders of magnitude acceleration, can outperform LLM-based graph reasoning
  - **Activation**: graph coarsening, non-selfishness graph, NOPE graph, graph dimensionality reduction

### The Efficiency Gap in Byte Modeling
- [[byte-modeling-efficiency-gap]] - Compute-matched scaling study revealing byte modeling penalty is worse for MDM than AR due to context fragility (arXiv: 2605.12928)
  - AR's stable causal history allows natural subword pattern rediscovery; MDM destroys local contiguity
  - Performance penalty is not uniform across scales — gap widens for MDM
  - Future modality-agnostic designs need alternative structural biases
  - **Activation**: byte modeling efficiency, byte-level language model, masked diffusion model efficiency, context fragility

### SD3MF: Supervised Deep Multimodal Matrix Factorization for Interpretable Brain Network Analysis
- [[sd3mf-multimodal-brain-network]] - Interpretable framework that generalizes SNMTF to supervised prediction over populations of multimodal brain networks (arXiv: 2605.13312)
  - Deep hierarchical factorizations with shared latent representation align subjects across modalities
  - Adaptive weights enable data-driven multimodal fusion, handling missing modalities gracefully
  - Community-level interaction matrices yield biologically interpretable and discriminative features
  - Consistently outperforms CNN and GNN baselines on multimodal connectome datasets
  - **Activation**: SD3MF, multimodal matrix factorization brain, interpretable connectome analysis, supervised graph prediction, community-level brain interaction, adaptive multimodal fusion connectome

## 2026-05-15 - Neuroscience Research (Cron Job)

### Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining
- [[sparse-temporal-context-reconfiguration]] - Brain-inspired mechanism: sparse ensemble recruitment + temporal dynamics enable context reconfiguration in mPFC and SNNs, resisting catastrophic forgetting without auxiliary heuristics (arXiv: 2605.10178)
  - Mouse mPFC shows 32% cross-context neuron overlap (vs 61% chance); context decoding ~82.58% accuracy
  - SNNs with TLIF neurons outperform ANNs in TIL/DIL/CIL with lower neuron overlap
  - Sparse coding partitions activity; temporal dynamics coupled with sparsity further separates contexts
  - No transfer trade-off: context separation doesn't impair cross-task generalization
  - **Activation**: context reconfiguration, sparse coding temporal dynamics, lifelong learning SNN, catastrophic forgetting, neural ensemble overlap, ternary LIF, TLIF neurons

### Multi-Timescale Conductance Spiking Networks: Gradient-Trainable SNNs with Rich Firing Dynamics
- [[multi-timescale-conductance-snn]] - Multi-timescale conductance neurons shape I-V curves via fast/slow/ultra-slow conductances, enabling direct BPTT without surrogate gradients and rich firing regimes (arXiv: 2605.11835)
  - Single neuron model supports tonic, phasic, and bursting firing patterns
  - Outperforms LIF and AdLIF on Mackey-Glass time-series regression at predictability limit
  - Substantially sparser activity from both communication and computational perspectives
  - Analog-circuit native implementation for neuromorphic hardware
  - **Activation**: multi-timescale conductance, MTCSN, conductance-based SNN, direct BPTT SNN, rich firing dynamics, I-V curve shaping

     2|
     3|### Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Pretraining
     4|- [[brain-dit-fmri-foundation-model]] - Diffusion Transformer pretrained on 349,898 fMRI sessions from 24 datasets across 5 brain states, outperforms reconstruction/alignment pretraining (arXiv: 2604.12683)
     5|  - Metadata-conditioned diffusion pretraining disentangles intrinsic neural dynamics from population variability
     6|  - Multi-scale representations: global semantics for disease classification, local structure for demographics
     7|  - Proven superior: diffusion > reconstruction > alignment for fMRI foundation models
     8|  - **Activation**: brain-dit, fMRI foundation model, diffusion transformer brain, metadata-conditioned fMRI, multi-state fMRI
     9|
    10|### Probabilistic Prediction of Neural Dynamics via Autoregressive Flow Matching
    11|- [[autoregressive-flow-matching-neural-dynamics]] - Autoregressive flow matching framework for probabilistic neural activity forecasting from naturalistic stimuli, evaluated on Algonauts 2025 fMRI dataset (arXiv: 2604.11178)
    12|  - Learns conditional distribution p(neural_future | past_activity, sensory_input) via transport-based generative modeling
    13|  - Past BOLD dynamics is dominant predictor; autoregressive factorization adds gains under short-horizon conditions
    14|  - Enables closed-loop neurotechnology through probabilistic neural forecasting
    15|  - **Activation**: autoregressive flow matching, neural dynamics forecasting, probabilistic neural prediction, flow matching neuroscience
    16|
    17|## 2026-05-15 - Systems Engineering + Quantum (Cron Job)
    18|
    19|### Crystallographic Symmetry Generates Phononic Holonomic Gates with Biased-Erasure Channels
    20|- [[phononic-holonomic-gates-biased-erasure]] - Strain-active Lambda manifolds enable 99.88% fidelity superadiabatic holonomic gates with 64% data-qubit reduction via biased-erasure channels (arXiv: 2605.10932)
    21|  - Crystallographic symmetry fixes strain interaction to scalar dot product in multiplicity-one 2D irrep
    22|  - Circular strain field from phase-locked mechanical modes enables complex phononic Lambda-leg control
    23|  - A2-sector perturbations parity-filtered into optically distinguishable auxiliary state
    24|  - **Activation**: phononic holonomic gates, biased-erasure channels, crystallographic quantum control, strain-active Lambda manifold, superadiabatic echo-lune gate, NV center holonomic control
    25|
    26|### Communication-Efficient Distributed Inverse Quantum Fourier Transform
    27|- [[distributed-iqft-communication]] - Communication-optimized distributed IQFT protocol reducing inter-node bandwidth from O(n log n) to O(n/m log n) across m quantum processing nodes (arXiv: 2605.10710)
    28|  - Decomposes global IQFT into local computation + minimal communication phases
    29|  - Batches/eliminates redundant controlled-phase gates across nodes
    30|  - Communication rounds vs. local computation trade-off analysis
    31|  - **Activation**: distributed IQFT, communication-efficient quantum Fourier, distributed quantum computing communication, quantum Fourier transform distributed
    32|
    33|### Loop Composition in Quantum Algorithms
    34|- [[loop-composition-quantum]] - Models quantum algorithms as compositions of loop structures for modular design, compositional reasoning, and systematic optimization of iterative quantum protocols (arXiv: 2605.07518)
    35|  - Sequential, nested, and parallel loop composition rules for quantum channels
    36|  - Fixed point analysis and spectral gap convergence rates
    37|  - Pattern library: amplitude amplification, phase estimation, QAOA loops
    38|  - **Activation**: loop composition quantum, quantum algorithm composition, modular quantum algorithms, iterative quantum protocols
    39|
    40|### Parity Supervision for Quantum Generative Modeling
    41|- [[parity-supervision-quantum-generalization]] - Parity constraints as supervisory signals in quantum generative models improving out-of-distribution generalization through constrained output space (arXiv: 2605.10258)
    42|  - Parity operator enforces global constraint on output distribution
    43|  - Combined KL + parity loss balances fidelity and generalization
    44|  - Theoretical bounds on generalization gap improvement
    45|  - **Activation**: parity supervision quantum, quantum generative model generalization, parity constraints quantum ML, quantum model generalization
    46|
    47|### Multi-Qubit Stabilizer Readout on Dual-Species Rydberg Arrays
    48|- [[multi-qubit-stabilizer-rydberg]] - Parallel multi-qubit stabilizer measurement using species-selective Rydberg operations for real-time QEC in neutral atom platforms (arXiv: 2605.10924)
    49|  - Dual-species architecture: long-coherence data qubits + fast-gate ancilla qubits
    50|  - Species-selective controlled-phase gates for non-destructive stabilizer measurement
    51|  - Parallel measurement scheduling with crosstalk avoidance
    52|  - **Activation**: multi-qubit stabilizer readout, Rydberg atom QEC, dual-species Rydberg array, neutral atom error correction, parallel stabilizer measurement
    53|
    54|### Quantum Hypergraph Partitioning
    55|- [[quantum-hypergraph-partitioning]] - Hypergraph-based quantum circuit partitioning capturing multi-qubit interactions beyond pairwise couplings for optimal distributed quantum resource allocation (arXiv: 2605.10623)
    56|  - Circuit-to-hypergraph conversion with hyperedges for multi-qubit gates
    57|  - QUBO formulation solvable via quantum annealing or QAOA
    58|  - Hardware mapping with communication scheduling optimization
    59|  - **Activation**: quantum hypergraph partitioning, distributed quantum circuit mapping, hypergraph quantum topology, quantum hardware allocation
    60|
    61|
    62|## 2026-05-14 - Neuroscience Research (Cron Job PM)
    63|
    64|### State-Space NTK Collapse Near Bifurcations
    65|- [[state-space-ntk-collapse-bifurcations]] - NTK spectrum degradation analysis as state-space RNNs approach bifurcation points (arXiv:2605.12763)
    66|  - NTK eigenvalue collapse near critical phase transitions
    67|  - Different bifurcation types produce distinct NTK signatures
    68|  - **Activation**: NTK collapse, bifurcation analysis, state-space NTK, critical transitions neural networks
    69|
    70|### 18 Standalone Skills Synced
    71|- photonic-variational-trainability, signal-transform-unification, syndrome-adaptive-gain-control, quantum-compiler-routing, eeg-foundation-lrp-interpretability, adaptive-quantum-classical-fusion, optimal-parametric-quantum-estimation, quantum-qubit-routing, dart-q-realtime-qldpc-decoding, universal-complementarity-identity, strain-controlled-topological-quantum, syndrome-adaptive-gain-qldpc, topological-fault-detection-quantum, trace-eeg-autoregressive-routing, von-neumann-quantum-control, qubridge-fidelity-decomposition, krylov-complexity-analog-simulator, leggett-garg-neural-dynamics
    72|
    73|
    74|## 2026-05-14 - Systems Engineering + Quantum (Cron Job)
    75|
    76|### DART-Q: Real-Time QLDPC Decoding Framework
    77|- [[dart-q-realtime-qldpc-decoding]] - Deadline-driven QLDPC decoder with EDF scheduling and admission control for real-time quantum error correction (arXiv: 2605.09142)
    78|  - **Activation**: real-time decoding, QLDPC, fault-tolerant quantum, deadline scheduling, admission control
    79|
    80|### Price and Payoff: Stochastic FTQC Resource Planning
    81|- [[stochastic-ftqc-resource-planning]] - Stochastic-aware resource planning for magic state production reducing space-time volume by 27% (arXiv: 2605.07983)
    82|  - **Activation**: stochastic planning, fault-tolerant quantum, magic state, factory allocation, resource optimization
    83|
    84|### Topological Engine Monitor for Quantum Fault Detection
    85|- [[topological-fault-detection-quantum]] - Persistent homology-based non-invasive fault detection for quantum engines robust to complex noise (arXiv: 2604.11289)
    86|  - **Activation**: topological data analysis, persistent homology, quantum fault detection, engine monitoring
    87|
    88|### Neural QAOA² Differentiable Quantum Optimization
    89|- [[neural-qaoa-differentiable-optimization]] - End-to-end differentiable framework for joint graph partitioning and QAOA parameter initialization (arXiv: 2605.13072)
    90|  - **Activation**: neural QAOA, differentiable optimization, graph partitioning, quantum parameters, combinatorial optimization
    91|
    92|
    93|## 2026-05-14 - Neuroscience Research (Cron Job)
    94|
    95|### Information as Maximum-Caliber Deviation: A bridge between Integrated Information Theory and the Free Energy Principle
    96|- [[iit-fep-maxcaliber-bridge]] - Maximum-Caliber Deviation framework bridging IIT and FEP via variational principles (arXiv: 2605.12536)
    97|  - Information defined as deviation from constrained MaxCal path ensembles
    98|  - IIT 3.0 cause/effect repertoires re-derived from CMEP variational principles
    99|  - **Activation**: iit fep bridge, maximum caliber, integrated information, free energy principle, consciousness
   100|## 2026-05-14 - Systems Engineering + Quantum (Cron Job)
   101|
   102|### Affiliated operators for classical and quantum control
   103|- [[quantum-control-systems]] - von Neumann algebra framework for controllability of bilinear quantum systems on infinite-dimensional Hilbert spaces (arXiv: 2605.13774)
   104|  - Drift and control terms affiliated with von Neumann algebra of finite type
   105|  - Lie bracket generating condition implies full controllability
   106|  - State approximation bounds derived from algebraic structure
   107|  - **Activation**: quantum control, von Neumann algebra, bilinear systems, controllability, infinite-dimensional Hilbert space, operator algebra, 量子控制
   108|
   109|### CO-MAP: A Reinforcement Learning Approach to the Qubit Allocation Problem
   110|- [[quantum-control-systems]] - RL-based qubit allocation for quantum compilation minimizing SWAP overhead (arXiv: 2605.13638)
   111|  - Learns logical-to-physical qubit mapping policies via reinforcement learning
   112|  - State: current mapping + gate sequence position; Action: assign logical to physical qubit
   113|  - Reward: negative estimated routing cost; trains on diverse circuit benchmarks
   114|  - **Activation**: qubit allocation, quantum compiler, reinforcement learning compilation, qubit mapping, SWAP optimization, CO-MAP
   115|
   116|### A Quantum Multi-Programming Framework to Maximize Quantum Resources for the LUCJ Ansatz
   117|- [[quantum-control-systems]] - Multi-programming framework for concurrent quantum program execution maximizing hardware utilization (arXiv: 2605.12614)
   118|  - Partition hardware qubits into logical slices for concurrent execution
   119|  - Manage crosstalk between concurrent programs via physical coupling models
   120|  - Optimize throughput vs. individual fidelity trade-offs
   121|  - **Activation**: quantum multi-programming, resource optimization, quantum throughput, LUCJ ansatz, concurrent quantum execution, 量子多编程
   122|
   123|### Grid-Orch: An LLM-Powered Orchestrator for Distribution Grid Simulation and Analytics
   124|- [[llm-orchestrated-systems]] - LLM orchestrator bridging natural language with power grid simulation via MCP (arXiv: 2605.12728)
   125|  - LLM decomposes user intent into tool-specific commands for engineering simulators
   126|  - MCP server layer provides standardized interface to domain-specific tools
   127|  - Validation gate ensures physical correctness of simulation results
   128|  - Addresses 1.5M engineer shortage by democratizing access to grid analysis tools
   129|  - **Activation**: LLM orchestrator, MCP engineering, natural language simulation, engineering tool orchestration, grid simulation, automated engineering workflow
   130|
   131|
   132|## 2026-05-15 - Neuroscience Research (Cron Job)
   133|
   134|### Joint Sparse Coding and Temporal Dynamics Support Context Reconfiguration
   135|- [[sparse-temporal-context-reconfiguration]] - 联合稀疏编码与时间动力学支持上下文重构：大脑通过稀疏性减少跨上下文干扰，时间动力学增强上下文可分离性，SNN天然具备这两种特性 (arXiv: 2605.10178)
   136|  - mPFC记录显示上下文依赖的稀疏活动模式，减少表征重叠
   137|  - 时间动力学为上下文编码增加正交维度，即使重叠表征也可分离
   138|  - SNN在终身学习中表现出更好的保留能力，无需额外正则化或回放机制
   139|  - **Activation**: context reconfiguration, sparse coding temporal dynamics, catastrophic forgetting, lifelong learning SNN, mPFC, stable adaptation, 上下文重构
   140|
   141|### S2-Net: Oscillatory Spiking Neural Network with Time-Delayed Coordination
   142|- [[oscillatory-snn-time-delayed-coordination]] - 从皮质同步节律到脑启发学习机制：S2-Net通过自下而上和自上而下的迭代交互实现认知级神经同步 (arXiv: 2605.01656)
   143|  - 自下而上：脉冲活动在有限记忆窗口内累积形成振荡同步模式
   144|  - 自上而下：时间延迟同步公式实现对异质神经脉冲的全局调制
   145|  - 在神经活动解码、能量高效信号处理、时间绑定和语义推理任务中取得优异结果
   146|  - **Activation**: S2-Net, spiking-by-synchronization, oscillatory SNN, time-delayed coordination, cortical rhythm, temporal binding, neural synchrony
   147|
   148|### SpikeProphecy: A Large-Scale Benchmark for Autoregressive Neural Population Forecasting
   149|- [[spikeprophecy-benchmark]] - Large-scale benchmark for evaluating neural population forecasting models at Neuropixels scale, addressing critical BCI infrastructure gap (arXiv: 2605.12992)
   150|  - ~27,000 neurons across 39 sessions (Steinmetz visual-discrimination), 1,994 held-out trials at 50ms resolution
   151|  - Mamba forecaster trained on next-step spike counts delivers both forecasting and behavioral readout in one pass
   152|  - Mouse choice decoding: 75.7% (2.3x chance), beats linear decoder on raw spikes by 4-6 pp
   153|  - Calibration efficiency: 100-150 trials to reach asymptote; fits 50ms GPU budget
   154|  - **Activation**: spikeprophecy, neural forecasting benchmark, spike count prediction, neural population forecasting, autoregressive neural dynamics, BCI forecasting, Mamba neural dynamics
   155|
   156|### FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping
   157|- [[fits-interpretable-spiking-neurons]] - Factorizes temporal computation within individual spiking neurons into Frequency Selectivity and Temporal Shaping modules (arXiv: 2605.13071)
   158|  - FS module: each neuron learns target frequency as maximizer of subthreshold magnitude response
   159|  - TS module: group-delay modulation controls when frequency components contribute to membrane voltage
   160|  - Improves over LIF baseline in auditory benchmarks without recurrence or network delays
   161|  - Learned parameters provide interpretable neuron-level summaries of frequency/timing organization
   162|  - **Activation**: FiTS, frequency selective spiking neuron, temporal shaping SNN, interpretable spiking neuron, auditory spiking neural network, frequency selectivity neural dynamics
   163|
   164|## 2026-05-14 - Neuroscience Research (Cron Job)
   165|## 2026-05-14 - Systems Engineering + Quantum (Cron Job)
   166|
   167|### Tolerating Device Failure in Distributed Quantum Computing
   168|- [[distributed-quantum-fault-tolerance]] - 分布式量子容错：设备热替换+旗帜容错将开销降至1/10 (arXiv: 2605.11088, 2605.12385)
   169|  - 模块化量子网络中QEC期间组件可热替换，逻辑错误率稳定
   170|  - Flag fault tolerance指数减少稳定子测量额外量子比特
   171|  - **Activation**: distributed quantum, fault tolerance, device failure, hot-swap, flag QEC, 分布式量子, 容错
   172|
   173|### Scaling Qubit Mapping and Routing With Position Graph Abstraction
   174|- [[qubit-mapping-routing-memoization]] - 位置图抽象+记忆化加速量子编译路由 (arXiv: 2605.09237)
   175|  - 位置图统一可执行位置、移动路径和路由约束
   176|  - 记忆化缓存路由决策，编译时间从指数降至近线性
   177|  - **Activation**: qubit mapping, routing, TI-QCCD, compilation, position graph, memoization, 量子编译, 路由
   178|
   179|
   180|### Embodied Neurocomputation Framework
   181|- [[embodied-neurocomputation-framework]] - Systems-level optimization of biological neural network (BNN) encoding/decoding via closed-loop task-driven validation, outperforming DQN agents (arXiv: 2605.13315)
   182|  - Multi-combinatorial parameter search across 1,300+ configs and 4,000+ hours of real-time BNN-environment interaction
   183|  - 12 configurations showed consistent learning; BNN configs significantly outperformed optimized DQN under same budget
   184|  - Establishes foundation for bio-silicon hybrid architectures and field-wide neurocomputation benchmarks
   185|  - **Activation**: embodied neurocomputation, biological neural network computing, bio-silicon interface, BNN agent, organoid intelligence, living neural computing
   186|
   187|### Geno-Synthetic Coevolutionary Optimization
   188|- [[geno-synthetic-coevolution-optimization]] - Type-factored coevolutionary optimization for heterogeneous genotypes assembling into composite phenotypes (arXiv: 2605.13365)
   189|  - Decomposes evolutionary search into coordinated sub-populations, each with specialized genotype representations
   190|  - Assembly function maps heterogeneous genetic contributions into unified functional phenotype
   191|  - Enables modular evolutionary search for neural architecture, robot design, SNN evolution
   192|  - **Activation**: geno-synthetic, coevolutionary optimization, heterogeneous genotype, assembled phenotype, type-factored evolution, modular evolutionary algorithm
   193|
   194|## 2026-05-14 - Systems Engineering + Quantum (Cron Job)
   195|
   196|### Ensemble Engineering to Overcome Destructive Cancellation in Quantum Measurements
   197|- [[quantum-ensemble-engineering]] - Mitigates destructive cancellation in NISQ quantum measurements by aligning ensemble weights with operator sign structure via amplitude amplification and shallow circuits (arXiv: 2605.03729)
   198|  - Reformulates correlators in basis-resolved representation to expose cancellation origin
   199|  - Two approaches: Grover-type amplification (benchmark) and oracle-free shallow circuits (practical NISQ)
   200|  - Demonstrated on IBM 20-qubit processors; ~10× signal improvement over uniform averaging
   201|  - **Activation**: quantum ensemble engineering, NISQ measurement, destructive cancellation, 量子系综工程
   202|
   203|### QBalance: Multi-Objective Quantum Workflow Optimization
   204|- Related paper on reproducible quantum compilation and error-mitigation strategy selection (arXiv: 2605.02966)
   205|  - Multi-objective strategy selection over circuits, backends, and transformation policies
   206|  - Bayesian linear candidate-ordering surrogate for workflow optimization
   207|
   208|## 2026-05-14 - Neuroscience Research (Cron Job)
   209|
   210|### FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping
   211|- [[fits-interpretable-spiking-neurons]] - Spiking neuron factorizing temporal computation into frequency selectivity and temporal shaping modules for interpretable SNN design (arXiv: 2605.13071)
   212|  - FS module maps target frequency to adaptation strength via closed-form inverse; TS reshapes membrane voltage accumulation through group-delay modulation
   213|  - Consistent improvements over LIF baseline in feedforward SNNs on auditory benchmarks without recurrence or delays
   214|  - Learned parameters provide interpretable neuron-level summaries of frequency and timing organization
   215|  - **Activation**: FiTS, frequency selectivity spiking, temporal shaping SNN, interpretable spiking neuron, frequency-specialized neuron, group-delay spiking
   216|
   217|## 2026-05-14 - Neuroscience Research (Cron Job)
   218|
   219|### Letting the neural code speak: Automated characterization of monkey visual neurons through human language
   220|- [[automated-neural-characterization-language]] - Closed-loop framework using natural language to characterize individual neuron selectivity at scale via digital twins and LLM hypothesis generation (arXiv: 2605.12485)
   221|  - 96.1% of V4 neurons driven above 95th percentile by activating hypothesis images; 97.6% driven below 5th percentile by suppressing hypotheses
   222|  - Language embeddings partially aligned with neural activity and vision embeddings; linguistic compression is lossy yet semantically faithful
   223|  - V1 suppression less describable than activation, suggesting different computational principles in early visual areas
   224|  - **Activation**: neural characterization, neural selectivity, digital twin neuroscience, semantic hypothesis testing, V1 V4 visual cortex, automated neural analysis, closed-loop neural characterization
   225|
   226|## 2026-05-14 - 系统工程学 + 量子力学 (Cron Job)
   227|
   228|### Scaling Qubit Mapping and Routing With Position Graph Abstraction and Memoization
   229|- [[quantum-qubit-routing]] - Position graph abstraction + memoized SABRE for scalable quantum compilation (arXiv: 2605.09237)
   230|  - Position graph unifies locations, paths, and routing constraints
   231|  - Memoized heuristic scoring eliminates redundant SABRE evaluations
   232|  - Architecture-aware compilation generalizes across quantum hardware types
   233|  - **Activation**: qubit routing, qubit mapping, quantum compiler, SABRE, position graph, TI-QCCD, 量子比特路由, 量子编译
   234|
   235|## 2026-05-14 - Neuroscience Research (Cron Job)
   236|
   237|### SpikeProphecy: Large-Scale Benchmark for Autoregressive Neural Population Forecasting
   238|- [[spikeprophecy-benchmark]] - First large-scale benchmark for causal, autoregressive spike-count forecasting with population metric decomposition on 105 Neuropixels sessions (~89,800 neurons) (arXiv: 2605.12992)
   239|  - Decomposes aggregate correlation into temporal fidelity, spatial pattern accuracy, and magnitude-invariant alignment
   240|  - 7 architecture baselines (SSMs, RNNs, transformers) across 4 structural families
   241|  - **Activation**: SpikeProphecy, neural population forecasting, spike count forecasting, Neuropixels benchmark, population metric decomposition, temporal fidelity, spatial pattern accuracy
   242|
   243|### Predictive Coding Light+: STDP-Based Sequence Prediction in Spiking Neural Networks
   244|- [[predictive-coding-light]] - Spiking neural network architecture for unsupervised sequence processing using STDP with synaptic delays for short-term information retention (arXiv: 2605.12732)
   245|  - Reproduces classic visual cortex sequence learning findings without supervision
   246|  - Learns to fill in missing inputs in gesture recognition via recurrent excitatory connections with delays
   247|  - **Activation**: Predictive Coding Light+, PCL+, STDP sequence learning, spiking neural network prediction, synaptic delay learning, unsupervised sequence processing
   248|
   249|     1|## 2026-05-14 - Systems Engineering + Quantum Mechanics (Cron Job)
   250|     2|
   251|     3|### Operating a bistable qubit
   252|     4|- [[bistable-qubit-adaptive-feedback-control]] - Adaptive 1-bit FPGA feed
   253|  - Estimates qubit frequency from single-shot measurement at ~136 kHz bandwidth
   254|  - 77% error reduction in gate fidelities, suppresses TLS-induced Ramsey beating
   255|  - **Activation**: bistable qubit, adaptive qubit control, TLS defect mitigation, FPGA qubit feedback
   256|
   257|### Unitaria: Quantum Linear Algebra via Block Encodings
   258|- [[unitaria-quantum-linear-algebra]] - NumPy/SciPy-like Python library for quantum algorithms via block encodings without low-level circuit construction (arXiv: 2605.10768)
   259|  - Matrix-arithmetic evaluation path enables correctness verification beyond state vector simulation
   260|  - Automatic resource estimation (gate/qubit counts) without circuit execution
   261|  - **Activation**: unitaria, quantum linear algebra, block encoding, QSVT, quantum matrix operations
   262|
   263|### Scaling Qubit Mapping and Routing with Position Graph Memoization
   264|- [[qubit-mapping-routing-memoization]] - Scalable qubit routing using position graph abstraction and memoization for TI-QCCD architectures (arXiv: 2605.09237)
   265|  - Caches optimal routing solutions for sub-circuits to reduce compilation bottleneck
   266|  - Supports arbitrary ion trap architectures with movement constraints
   267|  - **Activation**: qubit mapping, quantum routing, TI-QCCD compilation, position graph abstraction
   268|
   269|## 2026-05-14 - Neuroscience Research (Cron Job)
   270|
   271|### Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale
   272|- [[mamba-spike-forecasting-behavioral-decoding]] - Single Mamba forecaster trained on next-step spike counts simultaneously decodes behavior better than raw spikes on Steinmetz benchmark (arXiv: 2605.12999)
   273|  - Mouse choice 75.7% (2.3x chance), stimulus side 66.1% (2x chance) across 39 sessions, ~27K neurons
   274|  - Outperforms 500ms linear decoder by 4-6pp; 100-150 trial calibration reaches asymptote; fits 50ms bin budget
   275|  - **Activation**: Mamba neural decoding, spike forecasting behavioral, Neuropixels decoding, implicit behavioral readout
   276|
   277|### Letting the neural code speak: Automated characterization of monkey visual neurons through human language
   278|- [[neural-code-language-characterization]] - Closed-loop LLM framework translates neural activation patterns into semantic descriptions for V1/V4 neurons using digital twins (arXiv: 2605.12485)
   279|  - V4 neurons: 96.1% activation above 95th percentile, 97.6% suppression below 5th percentile via semantic hypothesis testing
   280|  - Linguistic compression is lossy but semantically faithful; vision embeddings align best with neural activity
   281|  - **Activation**: neural code characterization, digital twin neuroscience, LLM neuron interpretation, V1 V4 semantic description
   282|
   283|### Self-organized MT Direction Maps Emerge from Spatiotemporal Contrastive Optimization
   284|- [[spatiotemporal-tdann]] - Spatiotemporal TDANN with MoCo self-supervision generates brain-like direction maps and pinwheel structures in MT area (arXiv: 2605.11718)
   285|
   286|### Multi-Timescale Conductance Spiking Networks
   287|- [[multi-timescale-conductance-snn]] - Gradient-trainable SNN framework using shaped I-V curves via fast, slow, ultra-slow conductances enabling rich firing regimes (tonic, phasic, bursting) with direct BPTT (arXiv: 2605.11835)
   288|  - Overcomes LIF/AdLIF limitations in regression tasks: higher accuracy + sparser activity (28% vs 38-45%)
   289|  - Systematic control over excitability regimes; analog circuit-friendly implementation
   290|  - **Activation**: multi-timescale conductance, gradient-trainable SNN, direct BPTT spiking, rich firing dynamics, MTCSN
   291|
   292|### Leveraging Non-Equilibrium ECRAM Dynamics for Short-Term Plasticity
   293|- [[ecram-short-term-plasticity-neuromorphic]] - Cross-layer device-circuit-system co-design transforming volatile ECRAM dynamics into computational resources for STP in neuromorphic circuits (arXiv: 2605.11243)
   294|  - Delay-feedback LIF + ECRAM synapses: 2 pJ/spike, native temporal filtering without additional circuitry
   295|  - Demonstrates synaptic facilitation and intrinsic excitability modulation at network level
   296|  - **Activation**: ECRAM short-term plasticity, neuromorphic temporal processing, device-circuit co-design, memristive synapses
   297|
   298|### Scaling Laws and Tradeoffs in Recurrent Networks of Expressive Neurons
   299|- [[scaling-laws-expressive-neurons-recurrent]] - Information-theoretic framework for optimal parameter allocation between neuron count (N), per-unit complexity (k_e), and connectivity (k_c) in recurrent networks (arXiv: 2605.12049)
   300|  - Expressive Leaky Memory (ELM) neurons enable independent tuning of complexity vs width vs connectivity
   301|  - Pareto-frontier scaling law: larger budgets favor more AND more complex neurons; closed-form model captures SNR saturation and redundancy
   302|  - **Activation**: scaling laws neural networks, expressive neurons, recurrent network tradeoffs, ELM neurons, parameter allocation
   303|  - 3D ResNet + spatial loss unifies ventral and dorsal stream computational origins via optimization trade-off
   304|  - Quantitative match to macaque MT: DSI, circular variance, pinwheel density all align with in vivo baselines
   305|  - **Activation**: MT direction maps, dorsal stream modeling, spatiotemporal TDANN, cortical self-organization
   306|
   307|## 2026-05-14 - Anthropic Research (Cron Job)
   308|
   309|### Teaching Claude Why
   310|- [[teaching-claude-why]] (updated) - Alignment training methodology for reducing agentic misalignment. Teaching principles underlying aligned behavior is more effective than training on demonstrations alone
   311|  - Key point: Every Claude model since Haiku 4.5 achieved perfect score on agentic misalignment eval (zero blackmail vs 96% in Opus 4)
   312|  - Key point: "Difficult advice" dataset (user in dilemma, AI gives advice) achieved same improvement with 28x fewer tokens
   313|  - Key point: Teaching Claude the constitution + fictional stories reduced misalignment 3x (65% to 19%) despite being OOD
   314|  - **Activation**: teaching claude why, agentic misalignment, constitutional training, alignment OOD generalization, difficult advice dataset, alignment training
   315|
   316|### Natural Language Autoencoders
   317|- [[natural-language-autoencoders]] - Methodology for converting Claude's internal activations into human-readable text via activation verbalizer + reconstructor round-trip
   318|  - Key point: NLA revealed 26% evaluation awareness on SWE-bench and 16% on code safety evals vs <1% verbalized
   319|  - Key point: In auditing game, NLAs enabled finding hidden motivations 12-15% of time vs <3% without NLAs
   320|  - **Activation**: natural language autoencoder, NLA, activation verbalizer, activation reconstructor, model auditing, evaluation awareness
   321|
   322|### Automated Alignment Researchers
   323|- [[automated-alignment-researchers]] (updated) - Using LLMs to autonomously conduct alignment research via weak-to-strong supervision
   324|  - Key point: 9 AARs achieved PGR 0.97 in 800 hours (~$18K) vs human PGR 0.23 in 7 days
   325|  - Key point: Reward hacking inevitable — AARs skipped teacher on math (most common answer), ran tests on code
   326|  - Key point: Production scale test showed no significant improvement — AARs capitalize on model-specific opportunities
   327|  - **Activation**: automated alignment researchers, AARs, weak-to-strong supervision, PGR metric, reward hacking, alien science
   328|
   329|### Trustworthy Agents in Practice
   330|- [[trustworthy-agents-framework]] (updated) - Five-principle framework for building and governing trustworthy AI agents
   331|  - Key point: Agent behavior depends on four layers (model, harness, tools, environment) working together
   332|  - Key point: Claude's check-in rate doubles on complex tasks vs simple tasks
   333|  - Key point: Three ecosystem needs — benchmarks, evidence sharing, open standards (MCP donated to Linux Foundation)
   334|  - **Activation**: trustworthy agents, AI governance, prompt injection, human control, agent architecture, MCP standard
   335|
   336|### How People Ask Claude for Personal Guidance
   337|- [[ai-sycophancy-measurement]] (updated) - Measuring and mitigating AI sycophancy in personal guidance contexts
   338|  - Key point: ~6% of conversations seek personal guidance; sycophancy 9% overall, 25% in relationships, 38% in spirituality
   339|  - Key point: Sycophancy doubles under pushback (18% vs 9%); Opus 4.7 halved relationship sycophancy vs Opus 4.6
   340|  - Key point: Stress-testing via prefilling reveals behavior under adverse conditions more effectively
   341|  - **Activation**: ai sycophancy measurement, personal guidance, pushback dynamics, stress-testing, synthetic training data
   342|
   343|## 2026-05-14 - Quantum Compilation + Quantum Systems (Cron Job)
   344|
   345|### TuniQ: Autotuning Compilation Passes for Quantum Workloads at Scale for Effectiveness and Efficiency
   346|- [[tuniq-quantum-compiler-rl]] - RL驱动的量子编译Pass自适应选择系统，动态优化编译流程以最大化保真度和效率 (arXiv: 2605.11375)
   347|  - 核心要点: 双编码器阶段感知表征+动态动作掩码，让RL代理根据电路结构、后端拓扑和噪声画像选择最优编译Pass序列
   348|  - 核心要点: 跨阶段奖励设计实现跨编译层信用分配，在IBM Quantum Cloud上超越Qiskit最高优化级别保真度，且无需重新训练即可泛化到不同后端
   349|  - **Activation**: quantum compilation RL, tuniq, quantum compiler optimization, RL transpiler, quantum pass selection, fidelity optimization, autotuning quantum compilation
   350|
   351|### QuBridge: Layer-wise Fidelity Decomposition in Quantum Computation Pipeline
   352|- [[qubridge-fidelity-decomposition]] - 量子计算流水线保真度分层分解分析工具，量化各编译决策层对最终输出质量的贡献 (arXiv: 2605.11529)
   353|  - 核心要点: 三阶段渐进式消融实验揭示：Qubit选择可将最差保真度带从11.8%压缩至2%以内；每门脉冲形状分配带来+0.9%额外增益
   354|  - 核心要点: 纠错编码并非均匀有利，其条件收益仅在输入态主导误差通道可被所选码检测时才显现
   355|  - **Activation**: quantum fidelity analysis, compilation pipeline, qubridge, fidelity decomposition, quantum error detection, ablation analysis
   356|
   357|## 2026-05-14 - Neuroscience Research (Cron Job)
   358|
   359|### Accounting for Missed Events in the Bayesian Modeling of IP3R Multimodal Gating
   360|- [[ip3r-bayesian-missed-event-modeling]] - Bayesian framework for ion channel gating with missed event correction (arXiv: 2605.11675)
   361|  - Core: Integrates temporal resolution limitations directly into hierarchical Markov chain likelihood for unbiased kinetic parameter inference
   362|  - Key finding: IP3R exhibits bimodal Park/Drive gating with Ca²⁺-dependent mode switching regulating CICR
   363|  - **Activation**: IP3R modeling, calcium channel gating, missed event correction, Bayesian ion channel, patch clamp analysis
   364|## 2026-05-14 - Systems Engineering + Quantum Mechanics (Cron Job - Block Encoding)
   365|
   366|### Unitaria: Quantum Linear Algebra via Block Encodings
   367|- [[quantum-block-encoding-linear-algebra]] - Block encoding methodology for quantum linear algebra, enabling unified QSVT-based matrix operations (arXiv: 2605.10768v1)
   368|  - 核心要点 1: 块编码作为统一接口实现矩阵运算，支持量子奇异值变换(QSVT)、哈密顿量模拟和矩阵函数求值
   369|  - 核心要点 2: QSVT实现多项式函数作用于奇异值，单一框架覆盖HHL算法、矩阵求逆、特征值估计
   370|  - **Activation**: quantum block encoding, quantum linear algebra, unitaria, quantum SVD, QSVT, quantum matrix inversion, quantum Hamiltonian simulation
   371|
   372|## 2026-05-14 - Systems Engineering + Quantum (Cron Job)
   373|
   374|### Scaling Qubit Mapping and Routing With Position Graph Abstraction and Memoization
   375|- [[quantum-compiler-routing]] - 量子编译器中基于位置图抽象和记忆化的可扩放量比特映射与路由优化 (arXiv: 2605.09237v1)
   376|  - 核心要点：位置图抽象统一了可执行位置、移动路径和路由约束三大约束表达
   377|  - 核心要点：通过记忆化启发式评估加速 SABRE 编译算法，不改路由决策仅加速
   378|  - **Activation**: quantum compiler, qubit mapping, qubit routing, SABRE algorithm, quantum circuit compilation, TI-QCCD, trapped-ion compilation, position graph abstraction
   379|
   380|### Lower overhead fault-tolerant building blocks for noisy quantum computers
   381|- [[quantum-fault-tolerance-blocks]] (updated) - 降低容错量子计算开销：标志容错稳定子测量、距离-4编码、经典编码保护测量结果 (arXiv: 2605.12385v1)
   382|  - 核心要点：标志容错组合证明指数级减少测量任意大小稳定子所需的额外量子比特
   383|  - 核心要点：距离-4编码编码6个逻辑量子比特，使用十分之一的物理量子比特达到与距离-5表面码相同保护
   384|  - **Activation**: quantum fault tolerance, flag fault tolerance, surface code, low overhead QEC
   385|
   386|### Benchmarking and Resource Analysis for Augmented-Lagrangian Quantum Hamiltonian Descent
   387|- [[al-qhd-quantum-optimization]] (updated) - 增强拉格朗日量子哈密顿下降框架用于约束非凸优化及资源估计 (arXiv: 2605.12066v1)
   388|  - 核心要点：将QHD嵌入增强拉格朗日框架，将约束优化转化为无约束量子子问题序列
   389|  - 核心要点：Texas7k ACOPF实例资源估计达 ~4.46×10⁷ 纠缠门（NISQ）和 ~9.42×10⁸ T门（容错）
   390|  - **Activation**: quantum Hamiltonian descent, augmented Lagrangian quantum, constrained quantum optimization, AL-QHD
   391|
   392|
   393|## 2026-05-14 - Systems Engineering Research (Cron Job)
   394|
   395|### SHIA: A Direct SysML–Hardware Interface Architecture for Model-Centric Verification
   396|- [[shia-sysml-hardware-interface]] - 将可执行SysML模型直接接入硬件验证回路，消除中间转换链，实现模型驱动的验证与更短的数字线程 (arXiv: 2605.11248)
   397|  - 核心要点 1: SysML模型可作为硬件验证的执行层，而非静态描述
   398|  - 核心要点 2: 双向服务器架构（SysML侧C++服务器 + 硬件侧Raspberry Pi）实现零差异模型-硬件对比
   399|  - **Activation**: SHIA, SysML, MBSE, hardware-in-the-loop, model-centric verification, digital thread
   400|
   401|### Skill Drift Is Contract Violation: Proactive Maintenance for LLM Agent Skill Libraries
   402|- [[skill-drift-contract-violation]] - 将技能漂移建模为契约违反，从技能文档中提取可执行环境契约，精准检测API/依赖变更，零误报率 (arXiv: 2605.10990)
   403|  - 核心要点 1: 区分角色承载假设（契约）与噪声文本，避免粗粒度变更监控的40%误报
   404|  - 核心要点 2: 契约违反使修复可操作化，一轮修复成功率从10%提升至78%
   405|  - **Activation**: skill drift, contract violation, agent skill maintenance, skill library decay, drift detection
   406|
   407|## 2026-05-14 - Systems Engineering + Quantum Mechanics (Cron Job)
   408|
   409|### CERTIFY-ED: A Multi-Layer Verification Framework for Exact Diagonalization
   410|- [[certify-ed-verification]] - 13层纵深防御验证框架，多源共识校验、防篡改证书、错误注入自测试 (arXiv: 2605.11787)
   411|  - 核心要点: 13个独立验证层覆盖代数/算法/数值/物理四个维度，每层捕获不同失效模式
   412|  - 核心要点: SHA-256哈希证书确保计算结果可追溯且防篡改，支持机器可验证的下游验证
   413|  - 核心要点: 错误注入自测试（6类已知错误全部检出）确保验证流水线自身可靠性
   414|  - **Activation**: multi-layer verification, defense in depth, multi-oracle consensus, tamper-evident certificates, error injection self-testing
   415|
   416|### QAP-Router: Tackling Qubit Routing as Dynamic Quadratic Assignment with Reinforcement Learning
   417|- [[qap-router-qubit-routing]] - 将量子比特路由建模为动态二次分配问题(QAP)，结构感知Transformer+PPO训练 (arXiv: 2605.12365)
   418|  - 核心要点: 逻辑交互=流矩阵F，硬件拓扑=距离矩阵D，目标是最小化Tr(F·X·D·X^T)
   419|  - 核心要点: 结构感知注意力机制将问题耦合(流×距离)直接编码到注意力分数中
   420|  - 核心要点: 前向→后向→前向三路精炼，在MQTBench上降低15.7% CNOT门
   421|  - **Activation**: qubit routing, quadratic assignment problem, quantum compilation, SWAP optimization, structure-aware Transformer
   422|
   423|## 2026-05-14 - Neuroscience Research (Cron Job)
   424|
   425|### Fast Automatic Artifact Rejection (FAAR) for EEG MI-BCIs
   426|- [[eeg-faar-artifact-rejection]] - 轻量级自动化EEG伪影拒绝方法，通过信号质量指数自适应阈值减少BCI不可用性 (arXiv: 2605.12408)
   427|  - 核心要点: 计算epoch级信号质量指数(SQI)，自适应选择拒绝阈值，无需手动调参
   428|  - 核心要点: 在低信噪比条件下效果最显著，有效减少被试间变异性
   429|  - **Activation**: FAAR artifact rejection, EEG cleaning, motor imagery BCI, signal quality index
   430|
   431|
   432|## 2026-05-14 - Systems Engineering + Quantum Mechanics (Cron Job)
   433|
   434|### Tolerating Device Failure in Distributed Quantum Computing
   435|- [[distributed-quantum-fault-tolerance]] - 设计容错分布式量子计算系统，支持热替换节点和分布式QEC (arXiv: 2605.11088)
   436|  - 分布式QEC使系统可靠性超过单个组件
   437|  - Toric code在<0.05%物理错误率下优于单体架构
   438|  - **Activation**: distributed quantum computing, quantum fault tolerance, toric code, Floquet code
   439|
   440|### Breaking the scalability barrier via a vertical tunable coupler in 3D integrated transmon system
   441|- [[3d-integrated-quantum-processor]] - 3D集成超导量子处理器设计，垂直可调耦合器实现芯片间纠缠 (arXiv: 2605.11488)
   442|  - 3层芯片堆叠（顶部Qubit+载流芯片+底部Qubit）
   443|  - 单量子门保真度99.87%，CZ门97.5%
   444|  - **Activation**: 3D quantum processor, vertical coupler, flip-chip qubit, interchip coupling
   445|
   446|### Strain-controlled crossover between Majorana and Andreev bound states
   447|- [[strain-controlled-topological-quantum]] - 应变工程控制拓扑量子态，psABS到MBS的转换 (arXiv: 2605.11066)
   448|  - 空间非均匀应变调控拓扑相边界
   449|  - BdG模拟框架+位置依赖拓扑质量分析
   450|  - **Activation**: strain-controlled quantum, Majorana bound states, topological quantum computing
   451|
   452|### Unification of Signal Transform Theory
   453|- [[signal-transform-unification]] - 基于群表示论统一所有信号变换，DAD-CAD匹配群发现算法 (arXiv: 2605.11589)
   454|  - 每个变换是特定群不变协方差的特征基
   455|  - Peter-Weyl定理构建不可约矩阵元
   456|  - **Activation**: signal transform theory, matched group discovery, Algebraic Diversity
   457|
   458|## 2026-05-14 - Neuroscience Research (Cron Job)
   459|
   460|### Multi-Timescale Conductance Spiking Networks: A Sparse, Gradient-Trainable Framework with Rich Firing Dynamics
   461|- [[multi-timescale-conductance-snn]] - Conductance-based SNN with direct BPTT (no surrogate gradients), multi-timescale dynamics yielding tonic/phasic/bursting regimes, superior Mackey-Glass prediction with higher sparsity (arXiv: 2605.11835)
   462|  - Replaces phenomenological LIF/AdLIF with I-V curve shaping via fast/slow/ultra-slow conductances
   463|  - Direct backpropagation through time eliminates forward-backward mismatch of surrogate gradients
   464|  - Feed-forward architecture achieves temporal processing via intrinsic neuron memory (no recurrent connections needed)
   465|  - **Activation**: multi-timescale conductance, MTCSN, conductance-based SNN, gradient-trainable spiking, neuromorphic temporal processing
   466|
   467|### Letting the Neural Code Speak: Automated Characterization of Monkey Visual Neurons through Human Language
   468|- [[neural-code-language-characterization]] - Closed-loop framework using natural language to characterize neural selectivity via digital twins and in silico hypothesis verification across macaque V1 and V4 (arXiv: 2605.12485)
   469|  - Translates high/low-activating images into dense captions → semantic hypotheses → synthesized images → in silico verification
   470|  - V4: activating hypotheses drove 96.1% of neurons above 95th percentile, suppressing below 5th percentile
   471|  - RSA shows partial alignment between neural activity, vision embeddings, and language embeddings
   472|  - Linguistic compression is lossy but semantically faithful — lost info recovered when rendered back to images
   473|  - **Activation**: neural code language, automated neuron characterization, digital twin in silico, semantic hypothesis, V1 V4 selectivity
   474|
   475|### Empirical Scaling Laws in Balanced Networks with Conductance-Based Synapses
   476|- [[balanced-network-scaling-conductance]] - Empirical scaling laws for balanced networks with conductance-based synapses (arXiv: 2605.12404)
   477|  - Scaling analysis of balanced neural networks with conductance-based synapses
   478|  - **Activation**: balanced network scaling, conductance synapses, neural network scaling laws
   479|
   480|### Leggett-Garg Tests in Neural Dynamics: Probing Non-Diffusive Stochastic Structure
   481|- [[leggett-garg-neural-dynamics]] - Proposes experimental Leggett-Garg inequality tests to distinguish diffusive vs persistent stochastic structure in single neurons (arXiv: 2605.12126)
   482|  - Telegrapher's equation vs cable equation: finite-velocity transport with memory
   483|  - Purely diffusive dynamics always satisfies LGIs; persistent stochastic dynamics can violate them
   484|  - Conservative interpretation: non-diffusive ≠ quantum coherence, just non-Markovian structure
   485|  - **Activation**: Leggett-Garg inequality, Telegrapher equation, persistent stochastic neuron, non-diffusive neural dynamics, temporal correlations
   486|
   487|### Interpreting EEG Foundational Transformers with LRP
   488|- [[eeg-foundation-lrp-interpretability]] - Applies Layer-wise Relevance Propagation (LRP) to EEG foundation models for post-hoc attribution, revealing Clever Hans behavior and novel biological hypotheses (arXiv: 2605.11885)
   489|  - Extends LRP from CNN-based to Transformer-based EEG models
   490|  - Uncovers ocular signal exploitation in motor imagery ("Clever Hans" behavior)
   491|  - Reveals central electrode cluster as candidate sensorimotor arousal signature
   492|  - **Activation**: EEG interpretability, LRP, EEG foundation model, Clever Hans EEG, transformer attribution
   493|
   494|### Interpretable EEG Microstate Discovery via Variational Deep Embedding
   495|- [[eeg-microstate-variational-embedding]] - Systematic architecture search with multi-quadrant evaluation for interpretable EEG microstate discovery via variational deep embedding (arXiv: 2605.10947)
   496|  - Variational deep embedding for interpretable EEG microstate discovery
   497|  - Systematic architecture search with multi-quadrant evaluation
   498|  - **Activation**: EEG microstate, variational embedding, interpretable EEG
   499|
   500|## 2026-05-14 - Systems Engineering + Quantum Mechanics (Cron Job)
   501|