## 2026-05-13 - Neuroscience Research (Cron Job)

### Cortico-cerebellar modularity as an architectural inductive bias for efficient temporal learning
- [[cortico-cerebellar-modularity-rnn]] - RNN augmented with cerebellar-inspired feedforward module achieves faster learning via fixed cortical reservoir + adaptive cerebellar readout (arXiv: 2605.10356)
  - Heterogeneous modularity: cortical RNN acts as fixed reservoir, cerebellar module drives learning
  - Freezing cortex after warmup preserves efficiency — structural inductive bias for temporal learning
  - **Activation**: cortico-cerebellar, cerebellar RNN, CB-RNN, modular RNN, temporal learning

### Encoding and Decoding Temporal Signals with Spiking Bandpass Wavelets
- [[spiking-bandpass-wavelet-encoding]] - Recasts spike encoders as time-causal wavelet frames with reconstruction error bounds, bridging SNN encoding with signal processing theory (arXiv: 2605.09770)
  - Spike encoding reformulated as wavelet transform with quantitative bandwidths
  - Signal reconstruction up to quantization error, RMSE comparable to continuous wavelets
  - **Activation**: spiking wavelet, spike encoding, temporal signal encoding, bandpass wavelet

## 2026-05-13 - Neuroscience Research (Cron Job)

### Spiking Bandpass Wavelet Encoding
- [[spiking-bandpass-wavelet-encoding]] - Spike encoders reformulated as time-causal wavelet frames with quantitative bandwidth guarantees (arXiv: 2605.09770)
  - Bridges neuromorphic spike encoding with classical signal processing via bandpass wavelet decomposition
  - Time-causal kernels enable real-time event generation with theoretical reconstruction bounds
  - **Activation**: spike encoding, wavelet-based spiking, neuromorphic encoding, event-based temporal representation, bandpass filtering with spikes

### Cortico-Cerebellar RNN Architecture for Temporal Learning
- [[cortico-cerebellar-rnn]] - CB-RNN augments RNNs with cerebellar feedforward module; cortex as fixed reservoir, cerebellum drives learning efficiency (arXiv: 2605.10356)
  - Key finding: freezing recurrent core after minimal training preserves superior learning — cortex functions as fixed reservoir
  - Heterogeneous modular architectures provide powerful structural inductive bias for temporal tasks
  - **Activation**: cortico-cerebellar, CB-RNN, cerebellar RNN, fixed reservoir, heterogeneous modularity, temporal learning

### Joint Sparse Coding and Temporal Dynamics for Context Reconfiguration
- [[sparse-temporal-context-reconfiguration]] (existing) - Sparsity + temporal dynamics enable lifelong learning without auxiliary heuristics (arXiv: 2605.10178)
  - Mouse mPFC + computational networks show sparse coding reduces cross-context interference
  - SNNs naturally exhibit both properties, improved retention without replay or regularization
  - **Activation**: sparse coding, temporal dynamics, context reconfiguration, catastrophic forgetting prevention

## 2026-05-14 - Medicine + Quantum Computing (Cron Job)

Today's topic: Medicine (Wednesday) + daily quantum mechanics. arXiv scan found 15 papers. 1 new paper imported to KG (2605.09691). 1 new skill created.

### Quantum Circuit Simulation of Compartmental Drug Dynamics
- [[quantum-circuit-drug-dynamics]] - Quantum circuit simulation of PK/PD models using variational algorithms (arXiv: 2605.09691)
  - Reformulates compartmental PK/PD ODEs as open quantum systems via Lindblad master equation
  - Implements PennyLane quantum circuits for drug dynamics simulation
  - Variational quantum algorithms for population-level parameter estimation
  - **Activation**: quantum drug dynamics, quantum pharmacokinetics, population PK/PD quantum, pennylane drug simulation

### Papers Scanned (no new skills needed - covered by existing)
- **2605.08324** - FQPDR: Federated QNN for Diabetic Retinopathy → existing [[fqpdr-medical-detection]]
- **2605.06727** - Medical Imaging with Cold-Atom Reservoir Computing → existing [[cold-atom-reservoir-computing]]
- **2604.24597** - Quantum Kernel Advantage in Medical Foundation Models → existing [[quantum-kernel-medical-embeddings]]
- **2604.16953** - Hybrid QNN for Breast Cancer Thermographic Classification → existing [[hybrid-quantum-medical-classification]]
- **2604.22903** - Adaptive Hybrid Quantum-Classical Feature Fusion → existing [[hybrid-quantum-classical-nn]]
- **2604.20438** - Quantum-Enhanced RNN for Battery State of Health → existing [[quantum-neural-hybrid]]
- **2605.10458** - QT-Net: AI Models in Atomic Chemical Space → existing [[quantum-drug-discovery]]
- **2605.09691** - Quantum Circuit Drug Dynamics (NEW) → [[quantum-circuit-drug-dynamics]] ✓

### Knowledge Graph Status
- Entities: 842 (836 → 842, added 6 keyword entities)
- Relations: 2910 (2904 → 2910, added 6 HAS_KEYWORD relations)
- Vectors: 813
- Paper 2605.09691 imported with keywords: quantum circuit, drug dynamics, pharmacokinetics, variational quantum, population PK/PD, pennylane

### PageRank Top Papers (quantum + medicine)
1. [173] Quantum computing and AI: status and perspectives (PR=0.0040)
2. [362] Quantum computing revolution in healthcare: systematic review (PR=0.0039)
3. [193] Quantum Circuit-Based Learning Models (PR=0.0035)
4. [348] Quantum Computing in Personalized Medicine (PR=0.0021)
5. [188] Qubit-Based Framework for QML (PR=0.0017)
6. [347] Quantum Generative Learning for Medical Image Generation (PR=0.0015)
7. [272] Applications of quantum computing in clinical care (PR=0.0015)


## 2026-05-13 - Neuroscience Research (Cron Job)

### Synced 15 neuroscience standalone skills to ai_collection
Today's arXiv scan (q-bio.NC + cs.NE, May 12) found 29+ papers across both categories. All papers covered by existing skills. Primary value: synced 15 standalone neuroscience skills that were created separately but not yet in the ai_collection project.

#### Papers Scanned (May 12, 2026)
- **2605.10356** - Cortico-cerebellar modularity for temporal learning → [[cortico-cerebellar-modularity-rnn]]
- **2605.10178** - Joint sparse coding and temporal dynamics → [[sparse-temporal-context-reconfiguration]]
- **2605.09770** - Spiking Bandpass Wavelets for temporal signals → [[spiking-bandpass-wavelet-encoding]]
- **2605.10505** - Multilevel Interactive Equilibrium in NeuroAI → [[multilevel-interactive-equilibrium-neuroai]]
- **2605.10679** - Spiking Recurrent Cells on FPGA → [[spiking-recurrent-cells-fpga-accelerator]]
- **2605.09409** - Predictive/feedback signals for language representations → [[predictive-feedback-signals-language-representations]]
- **2605.09243** - How Much is Brain Data Worth for ML → [[brain-data-value-scaling-laws]]

#### Synced Skills
- [[behavior-vlm-neuroscience]] - Behavior VLM for neuroscience understanding
- [[brain-digital-twins-execution]] - Brain digital twins execution semantics
- [[brain-inspired-capture-visual-decoding]] - Brain-inspired visual capture
- [[cognitive-circuit-breaker-ai-reliability]] - Cognitive circuit breaker for AI reliability
- [[cold-atom-reservoir-computing]] - Cold atom reservoir computing
- [[core-cross-site-ood-brain-network]] - CORE cross-site OOD robust brain network
- [[frequency-matching-snn-mmwave]] - Frequency matching SNN for mmWave sensing
- [[fsfm-selective-forgetting-agent-memory]] - Selective forgetting agent memory
- [[higher-order-brain-interactions-o-information]] - Higher-order brain interactions via O-information
- [[neuroscience]] - Comprehensive neuroscience skill
- [[organic-quantum-reservoir-computing]] - Organic quantum reservoir computing
- [[qml-spiking-encoding]] - QML spiking encoding
- [[spiking-phase-quantum-encoding]] - Spiking phase quantum encoding
- [[topological-signal-processing-brain-networks]] - Topological signal processing for brain networks
- [[universal-neural-propagator]] - Universal neural propagator
- [[brain-data-value-scaling-laws]] - Mathematical framework for brain data value in ML
- [[sparse-temporal-context-reconfiguration]] - Joint sparse coding and temporal dynamics for context reconfiguration


## 2026-05-13 - Neuroscience Research (Cron Job)

### Joint sparse coding and temporal dynamics support context reconfiguration
- [[sparse-temporal-context-reconfiguration]] - 稀疏编码与时间动力学协同实现上下文重构，揭示大脑如何在适应新环境时不遗忘旧知识，为终身学习提供无辅助机制的抗遗忘方案 (arXiv: 2605.10178)
  - 小鼠mPFC显示情境依赖的稀疏编码减少跨情境干扰
  - 网络活动的时间动力学进一步增强情境可分离性
  - 脉冲神经网络(SNN)天然具备双重属性，无需回放缓冲或正则化即可抵抗灾难性遗忘
  - **Activation**: sparse coding, temporal dynamics, context reconfiguration, lifelong learning, catastrophic forgetting

## 2026-05-13 - Medicine + Quantum Mechanics (Cron Job)

### FQPDR: Federated Quantum Neural Network for Privacy-preserving Early Detection of Diabetic Retinopathy
- [[federated-quantum-medical-diagnosis]] - Combines federated learning with quantum neural networks for privacy-preserving medical image diagnosis without centralizing patient data (arXiv: 2605.08324)
  - Each client trains local QNN, shares only model parameters with server
  - Lightweight: 4-6 qubits, 10-20 trainable parameters sufficient
  - Validated on E-Ophtha and Retina MNIST for microaneurysm detection
  - Cross-evaluation efficiency demonstrates robustness across clients
  - **Activation**: federated quantum, privacy-preserving medical AI, federated QNN, distributed quantum diagnosis, patient data privacy quantum

### FQPDR: Federated Quantum Medical Detection Skill
- [[fqpdr-medical-detection]] - Three-layer federated QNN architecture for privacy-preserving early disease detection combining FL, QNN, and quantum kernel refinement (arXiv: 2605.08324)
  - Federated learning layer: local QNN training on private hospital data
  - Quantum neural network layer: lightweight PQC with 8-12 qubits for medical image features
  - Two-tier comparison framework for validating quantum advantage in medical imaging
  - **Activation**: federated quantum neural network, FQPDR, privacy-preserving medical diagnosis, quantum kernel medical imaging

### Medical Imaging Classification with Cold-Atom Reservoir Computing using Auto-Encoders and Surrogate-Driven Training
- [[surrogate-gradient-quantum-reservoir-medical]] - Overcomes non-differentiable quantum measurement barrier using differentiable surrogate models enabling end-to-end backprop through quantum reservoir (arXiv: 2605.06727)
  - Guided auto-encoder produces compact representations optimized for quantum reservoir
  - Latent vectors encoded as Rydberg Hamiltonian pulse detuning parameters
  - Joint optimization: classification accuracy + auto-encoder reconstruction
  - Outperforms PCA and unguided autoencoders for polyp detection
  - **Activation**: surrogate quantum training, quantum reservoir medical, gradient barrier quantum, Rydberg Hamiltonian encoding, cold-atom reservoir

### Algorithmic Advantage on a Gate-Based Photonic Quantum Neural Network
- [[photonic-quantum-neural-advantage]] - Proves QNNs with 2 parameters solve tasks requiring ANNs with 4x+ parameters, deployed on six-qubit photonic processor (arXiv: 2605.10801)
  - Effective dimension (Fisher-based) as generalization capacity measure
  - 100% accuracy on XOR where matched ANN fails at random guessing
  - Gradient-free optimization robust to photon loss and phase errors
  - Both online and offline learning settings validated on hardware
  - **Activation**: photonic QNN advantage, quantum effective dimension, gate-based quantum classifier, variational quantum classifier, QNN expressivity

### Cold-Atom Reservoir Computing for Efficient ML
- [[cold-atom-reservoir-computing]] - Neutral-atom arrays as physical reservoirs encoding data into Rydberg Hamiltonian, reading out via quantum measurements for efficient classification (arXiv: 2605.06727)
  - N atoms provide 2^N dimensional Hilbert space with natural nonlinearity
  - Rydberg blockade creates intrinsic nonlinear response
  - Scalable to 100+ qubits with current neutral-atom platforms
  - Energy-efficient physical computation without digital simulation
  - **Activation**: cold atom reservoir, neutral atom computing, Rydberg reservoir, quantum reservoir machine, atom array ML

## 2026-05-13 - Neuroscience Research (Cron Job)

### Joint Sparse Coding and Temporal Dynamics Support Context Reconfiguration
- [[sparse-temporal-context-reconfiguration]] - Identifies how sparsity reduces cross-context interference and temporal dynamics enhance context separability for stable lifelong learning without catastrophic forgetting (arXiv: 2605.10178)
  - mPFC recordings + computational networks: sparse activation + temporal evolution enable clean context switching
  - SNNs show superior lifelong learning retention without auxiliary heuristics (no replay, no EWC needed)
  - Dual constraint (sparsity + temporal) creates energy-efficient pathway for stable adaptation
  - **Activation**: context reconfiguration, catastrophic forgetting prevention, sparse coding neural, temporal dynamics separation, lifelong learning SNN, mPFC context switching

### Oscillatory Spiking Neural Network with Time-Delayed Coordination (S2-Net)
- [[oscillatory-snn-time-delayed-coordination]] - Brain-inspired S2-Net where cognition-level neural synchrony emerges from iterative bottom-up/top-down interactions between spiking dynamics and oscillatory synchronization (arXiv: 2605.01656)
  - Bottom-up: oscillatory patterns emerge from spike history over finite memory window
  - Top-down: time-delayed synchronization modulates heterogeneous neural spiking for distributed systems
  - Validated on neural activity decoding, energy-efficient signal processing, temporal binding, and semantic reasoning
  - **Activation**: S2-Net, spiking-by-synchronization, oscillatory SNN, time-delayed coordination, cortical rhythm modeling, temporal binding SNN

     1|## 2026-05-13 - Neuroscience Research (Cron Job)
     2|
     3|### How Much is Brain Data Worth for Machine Learning?
     4|- [[brain-data-value-scaling-laws]] - Mathematical framework quantifying brain data value for ML training, deriving scaling laws and brain-to-task data exchange rates (arXiv: 2605.09243)
     5|  - BEFS two-stage estimator: brain encoding model + task learning with brain feature regularization
     6|  - Exchange rates depend on brain-task alignment, neural SNR, latent dimension, and task sample regime
     7|  - Budget optimization: when and how much brain data to collect vs task labels
     8|  - **Activation**: brain data value, neural data worth, brain distillation, brain-regularized learning, neuroAI data collection
     9|
    10|### FLUX: Geometry-Aware Longitudinal Flow Matching with Mixture of Experts
    11|- [[flux-longitudinal-flow-matching]] - Framework for reconstructing trajectories from unpaired biological snapshots while discovering latent regime transitions (arXiv: 2605.08648)
    12|  - Three-stage training: metric learning, bend network, MoE velocity field with Gumbel-Softmax routing
    13|  - Geometry-aware paths keep trajectories on data manifolds vs Euclidean shortcuts
    14|  - Validated on widefield calcium imaging (neural learning regimes) and single-cell differentiation
    15|  - **Activation**: longitudinal flow matching, geometry-aware transport, biological trajectory reconstruction, regime discovery
    16|
    17|## 2026-05-12 - Computer Science + Quantum Mechanics (Cron Job)
    18|## 2026-05-14 - Medicine + Quantum (Cron Job)
    19|
    20|### Hybrid Quantum-Classical Medical Diagnosis Pipelines
    21|- [[hybrid-quantum-medical-diagnosis]] - Hybrid quantum-classical ML pipelines for medical image classification and diagnosis
    22|  - HQCNN: classical CNN + quantum variational classification layer (4-16 qubits)
    23|  - CV-QNN: continuous-variable quantum neural networks using photonic Gaussian gates
    24|  - Federated learning with tensor-network frontends + MPC-secured aggregation + quantum refinement
    25|  - **Activation**: quantum medical diagnosis, hybrid quantum ML, HQNN, medical image classification, CV-QNN, federated quantum learning
    26|
    27|
    28|### Communication-Efficient Distributed Inverse Quantum Fourier Transform
    29|- [[distributed-iqft-communication]] - Distributed iQFT with communication horizon pruning reduces inter-node quantum communication from O(P^2) to O(P) (arXiv: 2605.10710)
    30|  - 核心要点: 基于阈值修剪策略的通信视界利用受控相位旋转指数衰减特性，安全省略远程门
    31|  - 核心要点: 每节点纠缠资源消耗饱和为常数值，全局通信复杂度从二次降至线性
    32|  - 核心要点: iQFT作为Shor、HHL等量子算法的关键构建块，此技术直接提升分布式量子计算的实用性
    33|  - **Activation**: distributed iQFT, communication horizon pruning, distributed quantum computing, quantum network communication, scalable QFT, quantum teleportation optimization, distributed Shor algorithm
    34|## 2026-05-12 - Neuroscience Research (Cron Job)
    35|
    36|### NeuralBench: A Unifying Framework to Benchmark NeuroAI Models
    37|- [[neuralbench-unified-neuroai-benchmark]] - Unified NeuroAI benchmarking across 36 EEG tasks, 14 architectures, 94 datasets (arXiv: 2605.08495)
    38|  - Core finding: Foundation models only marginally outperform task-specific models
    39|  - Extensible design for MEG/fMRI integration
    40|  - **Activation**: neuralbench, neuroai benchmark, brain model evaluation, EEG benchmark
    41|
    42|### How Much is Brain Data Worth for Machine Learning?
    43|- [[brain-data-value-scaling-laws]] - Mathematical scaling laws for brain data value in ML (arXiv: 2605.09243)
    44|  - Derives exchange rates between neural samples and task labels
    45|  - Analyzes distribution shift robustness via brain regularization
    46|  - **Activation**: brain data value, neural data worth, brain-regularized learning, neuroai scaling laws
    47|
    48|
    49|## 2026-05-13 - Neuroscience Research (Cron Job)
    50|
    51|### Energy-Efficient Implementation of Spiking Recurrent Cells on FPGA
    52|- [[snn-fpga-hardware-software-codesign]] - FPGA加速器实现SRC神经元SNN，通过分段线性近似移除tanh/exp运算，4bit量化实现0.45mJ/推理 (arXiv: 2605.10679)
    53|  - 核心要点: SRC神经元在生物合理性和硬件成本之间取得平衡，通过数学简化消除浮点运算
    54|  - 核心要点: 权重直接存储在LUT寄存器中无需适配，VHDL全硬件实现
    55|  - 核心要点: 4bit量化+44张图像trace仍保持92.89%准确率，能耗仅0.45mJ/数字
    56|  - **Activation**: SNN FPGA, spiking recurrent cell SRC, neuromorphic hardware accelerator, SNN energy efficiency
    57|
    58|### Frequency Matching in Spiking Neural Networks for mmWave Sensing
    59|- [[frequency-matching-snn-mmwave]] - 基于频率匹配原理的SNN毫米波感知方法，LIF动力学提供天然低通滤波抑制高频噪声，精度提升6.22% (arXiv: 2605.09983)
    60|  - 核心要点: LIF神经元膜电位积分天然等效于低通滤波器，膜衰减因子τ决定有效带宽
    61|  - 核心要点: 频率匹配准则——将LIF带宽与数据判别性频谱内容匹配，实现机制-数据对齐
    62|  - 核心要点: 4个mmWave数据集验证：平均精度+6.22%，能耗降低3.64×
    63|  - **Activation**: frequency matching SNN, LIF low-pass filter, mmWave spiking network, membrane decay factor, edge sensing, mechanism-data alignment
    64|
    65|## 2026-05-12 - Neuroscience Research (Cron Job)
    66|
    67|### Predictive and feedback signals differently shape the formation of group-level and individualized language representations
    68|- [[predictive-feedback-signals-language-representations]] - Multi-signal model: prediction shapes group-level neural architecture, feedback explains individual differences in language learning (arXiv: 2605.09409)
    69|  - Prediction model explains most unique neural variance despite feedback-based task
    70|  - Feedback model best predicts individual generalization outcomes on Day 7
    71|  - **Activation**: language learning, predictive coding, feedback signals, brain-model alignment, individual differences
    72|
    73|## 2026-05-12 - Computer Science + Quantum Mechanics (Cron Job)
    74|
    75|### Qlustering for Data Clustering via Network-Based Quantum Transport
    76|- [[qlustering-quantum-clustering]] - Unsupervised clustering via steady-state quantum transport in open quantum networks, inferring cluster assignments from terminal current observables (arXiv: 2605.10844)
    77|  - Data encoded as input states, cluster assignments inferred from GKSL steady-state output currents
    78|  - No full state tomography required - uses accessible transport observables
    79|  - Noise-robust across broad dephasing strengths; benchmarked on QM9 and Iris
    80|  - **Activation**: quantum clustering, GKSL transport, steady-state quantum clustering, tomography-free quantum learning
    81|
    82|### MAGIQ: A Post-Quantum Multi-Agentic AI Governance System with Provable Security
    83|- [[magiq-post-quantum-agent-governance]] - Multi-agent AI governance with post-quantum cryptographic protocols and UC security proofs (arXiv: 2605.06933)
    84|  - Policy definition and enforcement for agent-to-agent sessions using PQC primitives
    85|  - Session-based enforcement with message attribution accountability
    86|  - Formally proven correct via Universal Composability framework
    87|  - **Activation**: post-quantum agent governance, MAGIQ, UC framework multi-agent, PQC agent security
    88|
    89|### Compositional Quantum Heuristics for Max-Clique Detection
    90|- [[compositional-quantum-heuristics]] - Mitigating barren plateaus via compositional quantum models with group-invariant loss functions (arXiv: 2605.07611)
    91|  - Assembles larger quantum models from smaller trainable subcomponents
    92|  - Symmetry-induced inductive bias via group-invariant loss functions
    93|  - Recursive hybrid quantum-classical heuristic inspired by QIRO
    94|  - **Activation**: compositional quantum circuits, barren plateau mitigation, permutation-equivariant QGNN, QIRO
    95|
    96|### A passive self-correcting quantum memory in three dimensions
    97|- [[passive-quantum-memory-3d]] - 自纠错量子记忆设计，3D Pauli稳定子哈密顿量实现指数级记忆寿命 (arXiv: 2605.10943)
    98|  - 递归哈密顿量变换降低维度同时保留逻辑编码
    99|  - 能垒工程设计使热误差指数抑制
   100|  - **Activation**: self-correcting quantum memory, 3D stabilizer, passive quantum memory
   101|
   102|### The Complexity of Stoquastic Sparse Hamiltonians
   103|- [[hamiltonian-complexity-stoquastic]] - StoqMA复杂度类分析框架，稀疏哈密顿量分类与模拟方法 (arXiv: 2605.02845)
   104|  - Stoquastic哈密顿量无符号问题，可用量子蒙特卡洛模拟
   105|  - StoqMA位于MA和QCMA之间的复杂度类
   106|  - **Activation**: stoquastic Hamiltonian, Hamiltonian complexity, StoqMA
   107|
   108|### Multi-Prover Interactive Proof Systems with Leakage
   109|- [[multi-prover-interactive-proofs]] - 多证明者交互证明系统泄漏分析，MIP/MIP*复杂度类与纠缠证明 (arXiv: 2605.09872)
   110|  - MIP=NEXP，MIP*=RE（含共享纠缠）
   111|  - 泄漏模型影响证明系统可靠性
   112|  - **Activation**: multi-prover interactive proofs, MIP protocols, MIP*
   113|
   114|### Equivariant Reinforcement Learning for Clifford Quantum Circuit Synthesis
   115|- [[equivariant-rl-quantum-circuit-synthesis]] - Symplectic-equivariant RL synthesizes Clifford circuits by reducing symplectic matrix to identity (arXiv: 2605.10910)
   116|  - RL agent discovers gate sequences with equivariant network respecting Sp(2n, F_2) symmetry
   117|  - Better sample efficiency and generalization to larger qubit counts
   118|  - **Activation**: quantum circuit synthesis, Clifford group, equivariant neural networks, RL quantum control
   119|## 2026-05-13 - Neuroscience Research (Cron Job)
   120|
   121|### Partial Annealing and Pattern Decorrelation in Associative Neural Networks
   122|- [[partial-annealing-pattern-decorrelation]] - 部分退火框架实现联想神经网络模式去相关，通过双温度双时间尺度分离实现最大存储容量αc=1 (arXiv: 2605.10304)
   123|  - 核心要点: 双温度双时间尺度框架耦合快速神经元动态与慢速突触动态，引入类副本参数n调节快慢分离
   124|  - 核心要点: 负值n诱导存储模式渐进去相关，减少干扰，促进正交配置，达到理论最大存储容量
   125|  - 核心要点: 在有偏模式场景下恢复检索能力，优于标准去相关方法，为记忆组织提供自适应机制
   126|  - **Activation**: partial annealing, pattern decorrelation, associative memory, Hopfield model, two-temperature framework, memory capacity
   127|
   128|### Moving MRI: Imaging a Moving Body with a Moving Magnet
   129|- [[moving-mri-brain-imaging]] - 移动MRI系统，同步移动受试者和扫描仪实现运动中的脑成像，为前庭功能研究开辟新范式 (arXiv: 2605.09267)
   130|  - 核心要点: 将无液氦超导磁体、梯度线圈和RF线圈作为整体安装在气动倾斜平台上，最小化相对运动
   131|  - 核心要点: 在大鼠活体实验中成功实现重复倾斜运动期间的脑部成像，表征了倾斜引起的场偏移伪影
   132|  - 核心要点: 为自然主义前庭功能研究奠定基础，未来可扩展到人类系统
   133|  - **Activation**: moving MRI, mMRI, vestibular imaging, motion artifact, naturalistic neuroimaging, superconducting magnet
   134|
   135|## 2026-05-13 - Computer Science + Quantum Computing (Cron Job)
   136|
   137|### Equivariant Reinforcement Learning for Clifford Quantum Circuit Synthesis
   138|- [[equivariant-rl-clifford]] - 使用等变强化学习综合Clifford量子线路，单策略跨不同量子比特数量，99.2%实例达到最优 (arXiv: 2605.10910)
   139|  - 核心要点: 置换等变神经网络架构对量子比特重标记保持不变，实现跨量子比特数泛化
   140|  - 核心要点: 智能体在毫秒级找到偏离最优仅一个双量子比特门的线路
   141|  - 核心要点: 对称性约束指数级缩小有效搜索空间，无需重新训练即可部署
   142|  - **Activation**: equivariant RL, quantum circuit synthesis, Clifford circuits, RL quantum, permutation equivariant, qubit routing, quantum compilation
   143|
   144|### ML-Guided Clifford Noise Reduction for Hamiltonian Simulations
   145|- [[ml-clifford-noise-reduction]] - ML引导的Clifford噪声降低框架，通过中间电路测量实现54%逻辑错误率降低 (arXiv: 2605.06792)
   146|  - 核心要点: 结合辛transvection Trotter综合、CliNR编码和Shor式稳定子验证
   147|  - 核心要点: ML学习选择最优验证稳定子，超越随机选择
   148|  - 核心要点: 设备匹配噪声模型，自适应硬件噪声特征
   149|  - **Activation**: quantum noise reduction, Clifford noise, CliNR, stabilizer verification, mid-circuit measurement, ML quantum verification
   150|
   151|### Photonic QNN Algorithmic Advantage
   152|- [[photonic-qnn-algorithmic-advantage]] - 光子量子神经网络展现超越经典ANN的算法优势，单参数对收敛而ANN失败 (arXiv: 2605.10801)
   153|  - 核心要点: 有效维度分析量化QNN表达能力，同等参数下QNN优于ANN
   154|  - 核心要点: 光子QNN以单对可训练参数实现100%准确率和0.04损失
   155|  - 核心要点: 量子干涉创造复杂决策边界，低参数 regime 优势最显著
   156|  - **Activation**: photonic QNN, quantum neural network advantage, effective dimension QNN, quantum classifier, photonic quantum, QNN vs ANN
   157|## 2026-05-12 - Neuroscience Research (Cron Job)
   158|### PRM: Explainable RNN for P300-based BCIs
   159|- [[prm-explainable-rnn-p300-bci]] - 后循环模块(PRM)增强RNN架构的P300分类性能与可解释性，实现全局/局部双重可解释性分析 (arXiv: 2605.10121)
   160|  - 核心要点: PRM作为RNN附加层，实现性能提升9%的同时输出时空重要性图，与P300神经生理学描述一致
   161|  - 核心要点: 全局可解释性识别相关脑区和关键时间区间，局部可解释性解析单次决策的时空模式
   162|  - 核心要点: 可泛化至运动想象、SSVEP、认知负荷评估等EEG任务
   163|  - **Activation**: PRM, P300 BCI, explainable RNN EEG, post-recurrent module, transparent BCI, EEG explainability, P300 classification
   164|
   165|### DANCE: Detect and Classify Events in EEG
   166|- [[dance-eeg-event-detection-classification]] - 端到端集合预测框架，直接从原始未对齐EEG信号中联合检测和分类神经事件 (arXiv: 2605.10688)
   167|  - 核心要点: 将神经解码重构为集合预测问题（受DETR启发），无需onset-informed分割即可实现事件检测和分类
   168|  - 核心要点: CNN+Perceiver+Decoder架构在10个异质数据集上验证，6种模态（打字、癫痫、语音、运动想象、P300、伪影），共235万事件
   169|  - 核心要点: 癫痫监测达到新SOTA，BCI任务准确率与onset-informed模型持平
   170|  - **Activation**: DANCE, EEG event detection, set prediction EEG, asynchronous neural decoding, event-based EEG classification, Meta AI EEG, seizure detection EEG
   171|
   172|## 2026-05-12 - Computer Science + Quantum Computing (Cron Job)
   173|
   174|### Compositional Quantum Heuristics for Max-Clique Detection
   175|- [[compositional-quantum-heuristics]] - 组合式量子启发式方法，通过小组件组装大模型缓解barren plateau问题 (arXiv: 2605.07611)
   176|  - 核心要点: 构建群不变损失函数引入对称性诱导偏置，改善梯度行为和泛化
   177|  - 核心要点: 排列等变量子GNN用于图组合优化，QIRO启发的递归混合搜索
   178|  - **Activation**: compositional quantum, barren plateau mitigation, quantum GNN, QIRO, group-invariant loss, permutation-equivariant quantum, max-clique quantum
   179|
   180|### The power of entanglement in distributed quantum machine learning
   181|- [[entanglement-distributed-qml]] - 纠缠在分布式量子机器学习中的作用，CHSH博弈类比提升分类准确率 (arXiv: 2605.03864)
   182|  - 核心要点: 预建立纠缠解决远程节点相干时间约束，纠缠-准确率呈倒U型关系
   183|  - 核心要点: 过度纠缠减少参数空间有效维度，需优化纠缠量与结构
   184|  - **Activation**: distributed quantum ML, entanglement classification, quantum internet ML, CHSH quantum learning, entanglement resource optimization
   185|
   186|### An Extremely Coarse Feedback Signal is Sufficient for Learning Human-Aligned Visual Representations
   187|- [[coarse-feedback-visual-alignment]] - 极粗粒度监督信号（仅2-8个类别）即可训练出与灵长类视觉皮层高度对齐的神经网络表征 (arXiv: 2605.05556)
   188|  - 核心要点: 2类粗监督匹配1000类在猕猴V1/人早期视觉的对齐度，8类匹配IT/腹侧流
   189|  - 核心要点: 粗监督模型在THINGS行为相似度对齐上超越所有测试模型（含CLIP、DINOv2等）
   190|  - 核心要点: 仅需1% ImageNet数据的粗监督模型在行为对齐上超过100%数据训练的1000类模型
   191|  - **Activation**: coarse supervision brain alignment, visual representation granularity, RSA neural alignment, brain-aligned vision models, supervisory signal coarseness, human perceptual similarity
   192|
   193|### Persistent Memory Through Triple-Loop Consolidation in a Non-Gradient Dissipative Cognitive Architecture
   194|- [[triple-loop-consolidation-non-gradient-memory]] - 非梯度耗散认知架构中的三重循环记忆巩固机制，在状态持续销毁的情况下实现持久记忆 (arXiv: 2603.27188)
   195|  - 核心要点: Deep Memory机制通过记录-播种-重入三重循环实现非梯度持久记忆
   196|  - 核心要点: 离散MoE路由是因果前提（MI=1.10 vs 0.001），连续播种优于单次播种
   197|  - 核心要点: 在~970次模拟中R=0.984，显著优于Hopfield和ESN基线，功能平行于海马巩固
   198|  - **Activation**: dissipative memory, non-gradient consolidation, deep memory mechanism, triple-loop consolidation, MoE gating memory, persistent memory neuromorphic, hippocampal consolidation parallel
   199|
   200|## 2026-05-12 - Neuroscience Research (Cron Job)
   201|### PRM: Explainable RNN for P300-based BCIs
   202|- [[prm-explainable-rnn-p300-bci]] - 后循环模块(PRM)增强RNN架构的P300分类性能与可解释性，实现全局/局部双重可解释性分析 (arXiv: 2605.10121)
   203|  - 核心要点: PRM作为RNN附加层，实现性能提升9%的同时输出时空重要性图，与P300神经生理学描述一致
   204|  - 核心要点: 全局可解释性识别相关脑区和关键时间区间，局部可解释性解析单次决策的时空模式
   205|  - 核心要点: 可泛化至运动想象、SSVEP、认知负荷评估等EEG任务
   206|  - **Activation**: PRM, P300 BCI, explainable RNN EEG, post-recurrent module, transparent BCI, EEG explainability, P300 classification
   207|
   208|### Globally Optimal Training of Spiking Neural Networks via Parameter Reconstruction
   209|- [[globally-optimal-snn-parameter-reconstruction]] - 将凸优化扩展到递归阈值网络的SNN全局最优训练方法，避免代理梯度近似误差 (arXiv: 2605.08022)
   210|  - 核心要点: 扩展前馈阈值网络凸化理论到并行递归阈值网络，SNN为其结构化特例
   211|  - 核心要点: 参数重构算法避免代理梯度跨层累积近似误差
   212|  - 核心要点: 可单独使用或与代理梯度联合使用，具数据可扩展性和架构鲁棒性
   213|  - **Activation**: globally optimal SNN training, parameter reconstruction, surrogate gradient alternatives, convex SNN optimization, threshold network convexification, large-scale SNN training
   214|
   215|### Encoding and Decoding Temporal Signals with Spiking Bandpass Wavelets
   216|- [[spiking-bandpass-wavelet-encoding]] - 将脉冲编码器重构为时间因果小波帧的信号处理方法，具有量化带宽和重建误差界 (arXiv: 2605.09770)
   217|  - 核心要点: 脉冲编码与经典信号处理理论桥接，赋予定量带宽和重建误差界
   218|  - 核心要点: 小波保持脉冲表示的稀疏性和局部性，重建误差与连续小波变换相当
   219|  - 核心要点: 可直接映射到神经形态硬件，适用于ECG、音频等时序信号重建
   220|  - **Activation**: spiking bandpass wavelets, spike encoding, temporal signal reconstruction, neuromorphic encoding, causal wavelet frames, event-based signal processing
   221|
   222|## 2026-05-12 - Computer Science + Quantum Computing (Cron Job)
   223|
   224|### Qlustering for Data Clustering via Network-Based Quantum Transport
   225|- [[quantum-transport-clustering]] - 基于GKSL主方程稳态量子传输的无监督聚类方法，通过终端电流读数直接推断簇分配，避免全态层析 (arXiv: 2605.10844)
   226|  - 核心要点: 数据编码为输入态，簇分配从稳态输出电流推断，无需全态层析
   227|  - 核心要点: 经典数据准备 + 量子传输动力学 + 经典聚类分配的混合工作流
   228|  - 核心要点: 对退相干强度具有广泛鲁棒性，电流是量子设备的原生可观测量
   229|  - **Activation**: quantum clustering, qlustering, GKSL clustering, quantum transport learning, open quantum network clustering, steady-state quantum ML, tomography-free readout
   230|
   231|### Equivariant Reinforcement Learning for Clifford Quantum Circuit Synthesis
   232|- [[equivariant-rl-clifford]] - 基于量子排列等变神经网络的RL方法合成Clifford量子电路，单策略跨任意量子比特数，99.2%最优电路发现率 (arXiv: 2605.10910)
   233|  - 核心要点: 对量子比特排列等变的策略网络，单策略适用于所有量子比特数量
   234|  - 核心要点: 每实例毫秒级找到最优电路（误差在1个双量子比特门内）
   235|  - 核心要点: 使用辛矩阵（stabilizer tableau）表示Clifford态进行高效RL训练
   236|  - **Activation**: equivariant RL quantum, clifford circuit synthesis, qubit permutation equivariant, quantum circuit compilation, RL quantum synthesis, stabilizer tableau optimization, size-agnostic quantum policy
   237|
   238|### Compositional Quantum Heuristics for Max-Clique Detection
   239|- [[compositional-quantum-heuristics]] - 组合式量子启发式方法解决QML中的barren plateau问题，通过子组件组合和对称性归纳偏差提升梯度行为 (arXiv: 2605.07611)
   240|  - 核心要点: 将大型量子模型分解为小型可训练子组件，避免barren plateau
   241|  - 核心要点: 构建群不变损失函数引入对称性归纳偏差，改善泛化能力
   242|  - 核心要点: 递归混合量子-经典启发式，用量子模型指导经典搜索
   243|  - **Activation**: compositional quantum heuristics, barren plateau mitigation, quantum ML composition, group-invariant loss function, permutation-equivariant QGNN
   244|
   245|### Breaking QAOA's Fixed Target Hamiltonian Barrier: A Fully Connected QBM via Bilevel Optimization
   246|- [[quantum-boltzmann-machine-bilevel]] - 通过双层优化架构打破QAOA固定目标哈密顿量限制，实现全连接量子玻尔兹曼机 (arXiv: 2605.07473)
   247|  - 核心要点: 内层训练模拟QAOA电路正相能量最小化，外层优化目标哈密顿量结构参数
   248|  - 核心要点: 单层(p=1)即达到0.9559测量概率，具有显著噪声鲁棒性
   249|  - 核心要点: 分块学习策略在10次测量下生成目标量子态网格图像
   250|  - **Activation**: quantum boltzmann machine, QBM bilevel optimization, QAOA extension, quantum generative model, bilevel quantum optimization
   251|
   252|### Loop Composition in Quantum Algorithms
   253|- [[loop-composition-quantum]] - 量子算法中的循环组合方法论，用量子行走在控制流图上建模分支+循环，实现变时Grover搜索最优复杂度 (arXiv: 2605.07518)
   254|  - 核心要点: 标准量子电路模型（直线程序）无法有效处理变长子例程的叠加
   255|  - 核心要点: 量子行走分支组合加入循环建模后恢复最优复杂度界
   256|  - 核心要点: 程序控制流建模对量子算法设计至关重要
   257|  - **Activation**: loop composition quantum, quantum algorithm control flow, branching composition quantum, quantum walk algorithm design, variable-time quantum search
   258|
   259|
   260|## 2026-05-12 - Neuroscience Research (Cron Job)
   261|### PRM: Explainable RNN for P300-based BCIs
   262|- [[prm-explainable-rnn-p300-bci]] - 后循环模块(PRM)增强RNN架构的P300分类性能与可解释性，实现全局/局部双重可解释性分析 (arXiv: 2605.10121)
   263|  - 核心要点: PRM作为RNN附加层，实现性能提升9%的同时输出时空重要性图，与P300神经生理学描述一致
   264|  - 核心要点: 全局可解释性识别相关脑区和关键时间区间，局部可解释性解析单次决策的时空模式
   265|  - 核心要点: 可泛化至运动想象、SSVEP、认知负荷评估等EEG任务
   266|  - **Activation**: PRM, P300 BCI, explainable RNN EEG, post-recurrent module, transparent BCI, EEG explainability, P300 classification
   267|
   268|### Joint Sparse Coding and Temporal Dynamics Support Context Reconfiguration
   269|- [[sparse-temporal-context-reconfiguration]] - 联合稀疏编码和时序动力学支持上下文重配置，在小鼠mPFC和SNN中发现防止灾难性遗忘的核心机制 (arXiv: 2605.10178)
   270|  - 核心要点: 稀疏编码减少跨上下文干扰，时序动力学增强上下文可分离性
   271|  - 核心要点: SNN天然具备两种属性，无需辅助启发式即可实现终身学习中的稳定保留
   272|  - **Activation**: sparse coding, temporal dynamics, context reconfiguration, catastrophic forgetting, lifelong learning, SNN
   273|
   274|### Cortico-Cerebellar Modularity as an Architectural Inductive Bias for Efficient Temporal Learning
   275|- [[cortico-cerebellar-modular-rnn]] - 皮层-小脑模块化架构作为高效时序学习的归纳偏置，CB-RNN中小脑模块驱动学习效率而皮层核心充当固定储层 (arXiv: 2605.10356)
   276|  - 核心要点: 异质模块化架构在时序任务上学习更快、性能更高，超越参数匹配的基线
   277|  - 核心要点: 最小训练后冻结皮层核心，将后续学习委托给小脑模块仍保持优越效率
   278|  - **Activation**: cortico-cerebellar, CB-RNN, cerebellar module, cortical core, temporal learning, modular architecture
   279|
   280|### Globally Optimal Training of Spiking Neural Networks via Parameter Reconstruction
   281|- [[globally-optimal-snn-parameter-reconstruction]] - 通过参数重建实现SNN全局最优训练，消除代理梯度近似误差 (arXiv: 2605.08022)
   282|  - 核心要点: 将前馈阈值网络凸化理论扩展到并行循环阈值网络，证明LIF-SNN是其结构化特例
   283|  - 核心要点: 通过枚举可实现的脉冲激活模式构建有限脉冲字典，在字典上求解凸优化问题
   284|  - **Activation**: globally optimal SNN training, SNN parameter reconstruction, convex SNN, surrogate gradient free, recurrent threshold network convexification
   285|
   286|### Same Brain, Different Prediction: How Preprocessing Choices Undermine EEG Decoding Reliability
   287|- [[same-brain-different-prediction]] - EEG预处理选择对解码可靠性的影响，高达42%试次预测会因预处理不同而翻转 (arXiv: 2605.07212)
   288|  - 核心要点: 将预处理选择建模为反事实干预空间，在2^7=128个管线上评估预测稳定性
   289|  - 核心要点: 提出预处理不确定性(PU)度量和Walsh-Hadamard分解揭示预处理步骤的近可加性
   290|  - **Activation**: EEG preprocessing reliability, prediction stability, counterfactual preprocessing, EEG pipeline comparison, BCI robustness
   291|
   292|
   293|## 2026-05-12 - Systems Engineering Research (Cron Job)
   294|
   295|### Distributionally Robust Data-Driven Predictive Control for Stochastic LTI Systems
   296|- [[dr-data-driven-predictive-control]] - 分布鲁棒数据驱动预测控制，结合Wasserstein模糊集实现未知扰动分布下的鲁棒控制 (arXiv: 2605.07589)
   297|  - 核心要点: 从输入输出轨迹数据直接构建预测器，无需系统辨识
   298|  - 核心要点: 使用Wasserstein距离构建模糊集，提供有限样本性能保证
   299|  - **Activation**: distributionally robust control, data-driven MPC, Wasserstein, subspace predictive control, stochastic LTI
   300|
   301|## 2026-05-12 - Computer Science (Cron Job)
   302|
   303|### Beyond Gates: Pulse Level Quantum Fourier Models
   304|- [[pulse-level-quantum-computing]] - 脉冲级量子计算突破门抽象层限制，直接操作硬件微波参数，通过子角度分解显著改善变分量子算法训练景观 (arXiv: 2605.04945)
   305|  - 核心要点: 脉冲形状不改变全局表达能力，但根本性改变局部优化景观
   306|  - 核心要点: 独立脉冲缩放将单一逻辑角度替换为多个独立可调子角度
   307|  - 核心要点: 放松门级参数化的刚性单项式耦合，为梯度下降提供高维逃逸路径
   308|  - **Activation**: pulse-level quantum computing, QFM pulse parameterization, variational quantum algorithm optimization, Fourier quantum model, quantum control optimization
   309|
   310|### Advances in Quantum Learning Theory with Bosonic Systems
   311|- [[quantum-learning-theory]] - 连续变量量子学习理论综述，研究CV系统状态学习的样本复杂度边界、高斯/非高斯态学习、高斯性检验 (arXiv: 2605.08082)
   312|  - 核心要点: 给出CV态之间基于协方差矩阵的迹距离边界
   313|  - 核心要点: 非高斯态学习样本复杂度受能量约束影响
   314|  - 核心要点: 高斯态与非高斯态学习的样本复杂度标度不同
   315|  - **Activation**: quantum learning theory, continuous-variable quantum systems, bosonic quantum ML, quantum state tomography, sample complexity analysis
   316|
   317|### Quantum-enhanced Large Language Models on Quantum Hardware via Cayley Unitary Adapters
   318|- [[quantum-cayley-llm-adapters]] - 量子增强 LLM 微调方法，使用 Cayley 参数化酉适配器克服经典内存限制 (arXiv: 2605.05914)
   319|  - 核心要点: Cayley 变换参数化酉矩阵，仅训练量子适配器参数
   320|  - 核心要点: 在真实量子硬件上验证，非仅仿真
   321|  - **Activation**: quantum-enhanced llm, cayley adapter, unitary adapter, quantum fine-tuning
   322|
   323|### Scalable Quantum Reservoir Computing over Distributed Quantum Architectures
   324|- [[quantum-reservoir-computing]] - 量子 reservoir computing 时间序列预测，无需反向传播，分布式架构可扩展 (arXiv: 2605.04991)
   325|  - 核心要点: 量子系统动力学作为计算 reservoir，仅训练经典读取层
   326|  - 核心要点: 四种架构变体：单量子位、多量子位、分布式、混合
   327|  - **Activation**: quantum reservoir computing, time series forecasting, distributed quantum
   328|
   329|### Quantum Software Architecture Framework (QSAF)
   330|- [[quantum-software-architecture]] - 混合量子经典系统组件化架构框架，34 种可复用量子电路模式 (arXiv: 2605.01800)
   331|  - 核心要点: 从电路级设计到系统级推理的转变
   332|  - 核心要点: 识别 34 种可复用量子电路组件和架构模式
   333|  - **Activation**: quantum software architecture, hybrid quantum-classical, quantum component
   334|
   335|## 2026-05-12 - Neuroscience Research (Cron Job)
   336|### PRM: Explainable RNN for P300-based BCIs
   337|- [[prm-explainable-rnn-p300-bci]] - 后循环模块(PRM)增强RNN架构的P300分类性能与可解释性，实现全局/局部双重可解释性分析 (arXiv: 2605.10121)
   338|  - 核心要点: PRM作为RNN附加层，实现性能提升9%的同时输出时空重要性图，与P300神经生理学描述一致
   339|  - 核心要点: 全局可解释性识别相关脑区和关键时间区间，局部可解释性解析单次决策的时空模式
   340|  - 核心要点: 可泛化至运动想象、SSVEP、认知负荷评估等EEG任务
   341|  - **Activation**: PRM, P300 BCI, explainable RNN EEG, post-recurrent module, transparent BCI, EEG explainability, P300 classification
   342|
   343|### Globally Optimal Training of Spiking Neural Networks via Parameter Reconstruction
   344|- [[globally-optimal-snn-parameter-reconstruction]] - Closed-form reconstruction of SNN parameters from trained ANN, eliminating surrogate gradient approximations (arXiv: 2605.08022)
   345|  - 核心要点 1: 首次证明任意 ReLU-ANN 存在等价 SNN，通过闭式参数重构实现全局最优训练，消除代理梯度近似误差
   346|  - 核心要点 2: 重构公式 W_SNN = W_ANN / (T * theta) 保证训练精度可继承自 ANN，无需 BPTT
   347|  - 核心要点 3: 相比代理梯度方法，具有精确梯度、全局最优、训练稳定、计算成本低四大优势
   348|  - **Activation**: globally optimal SNN training, SNN parameter reconstruction, surrogate gradient free SNN, ANN to SNN conversion, exact SNN training
   349|
   350|### Dynamical Mechanisms of Flexible Phase-Locking in Cortical Theta Oscillators
   351|- [[flexible-phase-locking-cortical-theta]] - Computational neuroscience analysis of how cortical theta oscillators flexibly phase-lock to inputs across wide timescale ranges (arXiv: 2605.08014)
   352|  - 核心要点 1: 听觉皮层 theta 振荡器通过内禀频率自适应、增益调制、多时间尺度整合实现灵活锁相
   353|  - 核心要点 2: 使用相位响应曲线 (PRC) 和 Arnold 舌头分析量化锁相区域和动态机制
   354|  - 核心要点 3: 宽范围夹带 (~2-12 Hz)、非对称响应、噪声鲁棒性支持语音处理和听觉流分离
   355|  - **Activation**: cortical theta oscillations, flexible phase-locking, auditory cortex dynamics, phase response curve, Arnold tongue analysis, speech neural tracking
   356|
   357|### Direct-to-Event Spiking Neural Network Transfer
   358|- [[direct-to-event-snn-transfer]] - Transfer pretrained direct-coded SNNs to energy-efficient event-based execution (arXiv: 2605.07207)
   359|  - 核心要点 1: 首次系统化研究直接编码 SNN 到事件驱动的迁移问题，填补 SNN 部署能量效率差距
   360|  - 核心要点 2: 提出 Self-Knowledge Distillation (SKD) 方法，基于 KL 散度蒸馏保留跨域性能
   361|  - 核心要点 3: 信息论分析揭示编码映射导致的信息损失、跨层尖峰分布偏移、权重激活统计失配三大挑战
   362|  - **Activation**: SNN energy efficiency, direct-to-event transfer, event-based SNN, neuromorphic deployment, SNN coding conversion
   363|
   364|### Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
   365|- [[zero-shot-imagined-speech-meg]] - Three-stage pipeline mapping imagined MEG to listened MEG for zero-shot imagined speech decoding (arXiv: 2605.08075)
   366|  - 核心要点 1: 利用配对想象的/聆听的 MEG 数据训练跨条件映射模型，解决想象语音数据稀缺问题
   367|  - 核心要点 2: 三阶段流程 — (1) 想象→聆听 MEG 映射 (2) 纯聆听对比词解码器 (3) 零样本想象语音解码
   368|  - 核心要点 3: 使用训练音乐家改善时间对齐，多嵌入策略评估（语义/声学/语音）
   369|  - **Activation**: imagined speech decoding, MEG BCI, cross-condition neural mapping, speech neuroprosthetics
   370|
   371|### DoLQ: Discovering ODEs with LLM-Based Qualitative & Quantitative Evaluation
   372|- [[dolq-ode-discovery-llm]] - Multi-agent symbolic regression using LLM scientist for combined domain knowledge + numerical evaluation (arXiv: 2605.07323, ICML 2026)
   373|  - 核心要点 1: 三代理架构 — Sampler 提议候选 ODE、Parameter Optimizer 优化系数、Scientist Agent 用 LLM 进行定性+定量评估
   374|  - 核心要点 2: 超越纯数值指标的科学发现 — 引入领域知识评估物理合理性
   375|  - 核心要点 3: 在多维 ODE 基准上超越现有方法，更准确地恢复真实符号项
   376|  - **Activation**: ODE discovery, symbolic regression, LLM scientific discovery, equation discovery
   377|
   378|
   379|### Quantization Robustness from Dense Representations of Sparse Functions in Kernel Associative Memory
   380|- [[kernel-hopfield-attractor-geometry]] - Geometric analysis of attractor boundaries and storage capacity in kernel Hopfield networks via quantization/pruning experiments (arXiv: 2604.20333)
   381|  - 核心要点 1: KLR Hopfield 网络在低精度量化下保持鲁棒性，但对剪枝高度敏感 — "稀疏函数、密集表示"原理
   382|  - 核心要点 2: 基于自发对称破缺和 Walsh 分析的几何解释，揭示鲁棒表示的底层几何原则
   383|  - 核心要点 3: 为硬件高效的核关联记忆提供实用路径，为神经系统鲁棒表示提供几何洞察
   384|  - **Activation**: kernel Hopfield, KLR associative memory, attractor basin geometry, quantization robustness, sparse function dense representation
   385|
   386|## 2026-05-12 - Computer Science + Quantum Mechanics (Cron Job)
   387|
   388|### Compositional Quantum Heuristics for Max-Clique Detection
   389|- [[compositional-quantum-heuristics]] - Compositional quantum model assembly to avoid barren plateaus, using group-invariant loss functions and permutation-equivariant quantum GNNs (arXiv: 2605.07611)
   390|  - 核心要点 1: 通过将大型量子模型分解为小型可训练子组件的组合方法，避免 QML 中的 barren plateau 问题
   391|  - 核心要点 2: 群不变损失函数与对称性诱导的归纳偏差，将有效参数搜索空间缩小 |G| 倍
   392|  - 核心要点 3: 排列等变量子图神经网络 + 递归混合量子-经典启发式框架，解决最大团检测等组合优化问题
   393|  - **Activation**: barren plateau, quantum composition, compositional QML, quantum graph neural network, max-clique, group-invariant loss, symmetry-induced bias, permutation-equivariant, recursive quantum heuristic, quantum subcircuit assembly
   394|
   395|### Quantum-Inspired Tunneling Optimization for Non-Convex ML
   396|- [[quantum-tunneling-optimization]] - Quantum-inspired evolutionary optimization (QIEO) using superposition-inspired probabilistic encoding and simulated tunneling to escape local optima in non-convex ML landscapes (arXiv: 2605.07947)
   397|  - 核心要点 1: 量子叠加启发的概率编码（每个基因是概率振幅对 [α, β]），保持对整个解空间的同步探索
   398|  - 核心要点 2: 量子隧穿模拟穿过能量势垒，克服经典优化器（ADAM/GA/DE/IHT）陷入局部最优的问题
   399|  - 核心要点 3: 在稀疏信号恢复和鲁棒回归基准上超越所有经典方法，混合探索+利用策略是关键
   400|  - **Activation**: non-convex optimization, local optima escape, quantum tunneling optimizer, sparse signal recovery, robust regression, quantum evolutionary algorithm, superposition-inspired encoding, QIEO
   401|
   402|### Quantum Boltzmann Machine via Bilevel Optimization
   403|- [[quantum-boltzmann-bilevel]] - Extends QAOA circuit to bilevel optimization for fully connected Quantum Boltzmann Machine, overcoming classical BM partial connectivity and QAOA fixed Hamiltonian limitations (arXiv: 2605.07473)
   404|  - 核心要点 1: 双层优化框架 — 外层学习最优目标哈密顿量，内层优化 QAOA 电路参数（自由能最小化）
   405|  - 核心要点 2: 全连接 Ising 型哈密顿量参数化，经典受限玻尔兹曼机因配分函数不可计算而无法实现
   406|  - 核心要点 3: 隐式微分穿过内层解实现端到端训练，量子电路提供高效采样替代经典吉布斯采样
   407|  - **Activation**: quantum Boltzmann machine, QAOA, bilevel optimization, fully connected Boltzmann, quantum generative model, energy-based quantum model, quantum sampling, quantum annealing, Hamiltonian learning
   408|
   409|### QuanForge: Mutation Testing for Quantum Neural Networks
   410|- [[quanforge-qnn-testing]] - Mutation testing framework for QNN robustness analysis with 9 mutation operators and statistical mutation killing (arXiv: 2604.20706)
   411|  - 核心要点 1: 统计突变杀死方法 — 用假设检验处理量子测量的随机性，提供可靠的突变杀死标准
   412|  - 核心要点 2: 9种突变算子 — 5种门级（省略、插入、替换、复制、重排序）+ 3种参数级（扰动、丢弃、缩放）+ 1种测量级
   413|  - 核心要点 3: 系统化突变生成算法可定位量子电路脆弱区域，区分不同测试套件的有效性
   414|  - **Activation**: quantum testing, QNN testing, mutation testing, quantum circuit robustness, quantum ML evaluation, 量子测试, 量子神经网络测试
   415|
   416|### SPATE: Spiking-Phase Adaptive Temporal Encoding for QML
   417|- [[qml-spiking-encoding]] - Spike-based temporal encoding for quantum machine learning, bridging neuromorphic computing with QML via phase-encoded qubits (arXiv: 2604.11022)
   418|  - 核心要点 1: 脉冲编码捕获输入数据的时间动态，解决传统QML静态编码无法处理时序数据的问题
   419|  - 核心要点 2: 相位编码量子比特使量子系统能原生处理时间依赖模式
   420|  - 核心要点 3: 三阶段流程 — 脉冲生成 → 相位编码 → 量子处理，将神经形态范式与QML桥接
   421|  - **Activation**: spiking quantum encoding, QML temporal encoding, spike encoding quantum, neuromorphic quantum computing, 脉冲量子编码
   422|
   423|### QIEO: Quantum-Inspired Evolutionary Optimization
   424|- [[quantum-inspired-optimization]] - Quantum-inspired evolutionary optimization using superposition-inspired probability amplitudes and quantum rotation gates for non-convex ML landscapes (arXiv: 2605.07947)
   425|  - 核心要点 1: 量子叠加启发的概率振幅编码 [α, β] 保持全局搜索视野，优于传统进化算法
   426|  - 核心要点 2: 量子旋转门更新概率分布，量子干涉平衡探索与利用
   427|  - 核心要点 3: 在稀疏信号恢复和鲁棒回归基准上超越 ADAM/GA/DE/IHT 等经典方法
   428|  - **Activation**: quantum-inspired optimization, QIEO, non-convex optimization, global search evolutionary, escaping local minima, 量子启发优化, 量子进化优化
   429|
   430|### Gated QKAN-FWP: Quantum-inspired Sequence Learning
   431|- [[gated-qkan-fwp]] - Quantum Fast Weight Programmers with variational quantum Kolmogorov-Arnold Networks for scalable sequence learning (arXiv: 2605.06734)
   432|  - 核心要点 1: 量子快速权重编程器 (QFWP) 从输入动态生成权重矩阵，替代固定RNN权重
   433|  - 核心要点 2: 变分量子 Kolmogorov-Arnold Networks (QKAN) 将 1D 函数替换为参数化量子电路
   434|  - 核心要点 3: 门控机制控制快权重信息流，量子启发时序编码捕获长程依赖
   435|  - **Activation**: quantum sequence learning, QKAN, fast weight programmer, quantum-inspired RNN, temporal encoding quantum, 量子序列学习
   436|### Normalizing Trajectory Models
   437|- [[normalizing-trajectory-models]] - Few-step generative modeling with exact likelihood via normalizing flows + parallel trajectory prediction (arXiv: 2605.08078)
   438|  - 核心要点 1: 将每个反向去噪步骤建模为条件归一化流，保持精确似然训练框架
   439|  - 核心要点 2: 浅层可逆块 + 深层并行轨迹预测器架构，端到端可训练
   440|  - 核心要点 3: 自蒸馏机制 — 在模型自身分数上训练的轻量级去噪器实现4步高质量采样
   441|  - **Activation**: normalizing trajectory, flow matching, few-step generation, diffusion distillation, trajectory modeling, exact likelihood generation
   442|
   443|### Advances in Quantum Learning Theory with Bosonic Systems
   444|- [[quantum-cv-learning-theory]] - Quantum learning theory for continuous-variable systems: sample complexity, Gaussian state learning, trace distance bounds (arXiv: 2605.08082)
   445|  - 核心要点 1: 综述 CV 系统量子学习理论 — 非高斯态和高斯态的样本复杂度分析
   446|  - 核心要点 2: 基于协方差矩阵的迹距离界，实现无需完整层析的态比较
   447|  - 核心要点 3: 高斯性测试协议与高效高斯过程学习
   448|  - **Activation**: quantum learning theory, continuous variable, bosonic systems, Gaussian states, quantum tomography, sample complexity quantum
   449|
   450|### Unlocking Vacuum Entanglement
   451|- [[vacuum-entanglement-extraction]] - Vacuum entanglement extraction protocols via local operations for distributed quantum computing and networking (arXiv: 2605.08076)
   452|  - 核心要点 1: 量子场真空态中的纠缠可通过局部操作提取，无需预共享纠缠对
   453|  - 核心要点 2: 提取效率取决于探测器间距、相互作用时间和耦合强度
   454|  - 核心要点 3: 应用于分布式量子计算和量子网络的纠缠分发
   455|  - **Activation**: vacuum entanglement, entanglement harvesting, quantum field theory communication, distributed quantum computing, quantum networking
   456|
   457|
   458|## 2026-05-12 - Neuroscience Research (Cron Job)
   459|### PRM: Explainable RNN for P300-based BCIs
   460|- [[prm-explainable-rnn-p300-bci]] - 后循环模块(PRM)增强RNN架构的P300分类性能与可解释性，实现全局/局部双重可解释性分析 (arXiv: 2605.10121)
   461|  - 核心要点: PRM作为RNN附加层，实现性能提升9%的同时输出时空重要性图，与P300神经生理学描述一致
   462|  - 核心要点: 全局可解释性识别相关脑区和关键时间区间，局部可解释性解析单次决策的时空模式
   463|  - 核心要点: 可泛化至运动想象、SSVEP、认知负荷评估等EEG任务
   464|  - **Activation**: PRM, P300 BCI, explainable RNN EEG, post-recurrent module, transparent BCI, EEG explainability, P300 classification
   465|
   466|### Pan-FM: A Pan-Organ Foundation Model with Saliency-Guided Masking for Missing Robustness
   467|- [[pan-fm-pan-organ-foundation]] - Multi-organ foundation model pre-trained on 7 organs with Saliency-Guided Masking for realistic missing-organ scenarios (arXiv: 2605.07055)
   468|  - 核心要点 1: 七器官统一骨干网络，处理真实世界中非随机缺失 (MNAR) 的多模态医学影像数据
   469|  - 核心要点 2: Saliency-Guided Masking (SGM) 自适应掩蔽主导器官，防止捷径学习偏差
   470|  - 核心要点 3: 在 UK Biobank 上 13 个疾病类别和 14 个单一疾病实体上优于单器官和多器官基线
   471|  - **Activation**: pan-organ foundation model, missing organ robustness, saliency-guided masking, multimodal biomedical imaging, dominant-organ shortcut learning
   472|
   473|### DoLQ: ODE Discovery with LLM-Based Evaluation
   474|- [[dolq-ode-discovery-llm]] - Multi-agent framework for discovering ODEs from data using LLM-based qualitative + quantitative evaluation, accepted at
   475|
   476|... [OUTPUT TRUNCATED - 634 chars omitted out of 50634 total] ...
   477|
   478|xity for certain observable distributions (arXiv: 2605.05518)
   479|   346|   213|   160|  - 核心要点 1: 经典影子协议通常从紧致群均匀采样，本文推广到紧致对称空间采样
   480|   347|   214|   161|  - 核心要点 2: 在某些观测分布下，对称空间协议比现有影子方案有采样复杂度优势
   481|   348|   215|   162|  - **Activation**: classical shadows, symmetric spaces, quantum state tomography, randomized measurements, sample complexity
   482|   349|   216|   163|
   483|   350|   217|   164|### Efficient Quantum Fourier Transforms For Semisimple Algebras
   484|   351|   218|   165|- [[quantum-algebraic-structures]] - Generalizes QFT from finite groups to semisimple algebras with efficient circuits for partition, Brauer, and walled Brauer algebras (arXiv: 2605.05337)
   485|   352|   219|   166|  - 核心要点 1: 半单代数上的傅里叶变换可以是非幺正的，但当参数 d 足够大时可被幺正算子良好逼近
   486|   353|   220|   167|  - 核心要点 2: 通过分解为不可约表示构建高效量子电路，推广了群上的QFT
   487|   354|   221|   168|  - **Activation**: quantum algebra, semisimple algebra QFT, quantum Fourier transform, Brauer algebra, representation theory
   488|   355|   222|   169|
   489|   356|   223|   170|### Analytical Angle-Finding and Series Expansions for Quantum Signal Processing via Orthogonal Polynomial Theory
   490|   357|   224|   171|- [[quantum-algebraic-structures]] - Analytical QSP angle-finding via Hermite, Jacobi, and Rogers-Szego polynomials with O(log(1/ε)) gate complexity (arXiv: 2605.05321)
   491|   358|   225|   172|  - 核心要点 1: 通过正交/双正交多项式族表征可实现的QSP多项式基，导出闭式角度公式
   492|   359|   226|   173|  - 核心要点 2: 利用Hermite级数展开实现O(log(1/ε))门复杂度的光滑函数块编码
   493|   360|   227|   174|  - **Activation**: quantum signal processing, orthogonal polynomials, QSP angles, Hermite expansion, Jacobi polynomials
   494|   361|   228|   175|
   495|   362|   229|   176|### Quantum Proper Scoring Rules: Minimax Estimation and Resource-Theoretic Advantages
   496|   363|   230|   177|- [[quantum-algebraic-structures]] - Quantum domain scoring rules with operator convex generators and Quantum Cramér-Rao-McCarthy Bound (arXiv: 2605.05268)
   497|   364|   231|   178|  - 核心要点 1: 将经典评分规则推广到量子密度算符域，建立完整对偶理论
   498|   365|   232|   179|  - 核心要点 2: 证明量子Cramér-Rao-McCarthy界，量化量子资源在预测任务中的经济价值
   499|   366|   233|   180|  - **Activation**: quantum scoring rules, minimax estimation, quantum Fisher information, operator convex, resource theory
   500|   367|   234|   181|
   501|   368|   235|   182|### Cusped Singularity Mixed-Mode Oscillation Analysis
   502|   369|   236|   183|- [[cusped-singularity-mmo-analysis]] - Geometric singular perturbation analysis of MMOs in inhibitory neural networks via cusped singularities (arXiv: 2605.03606)
   503|   370|   237|   184|  - 核心要点 1: 尖点奇异性（临界流形尖点处的折叠奇异性）是互抑制神经网络中混合模式振荡（MMO）的通用组织机制
   504|   371|   238|   185|  - 核心要点 2: 尖点奇异性保证小振幅振荡（SAO）的产生，结合奇异Hopf分岔形成完整MMO，呈现独特的交替振荡模式
   505|   372|   239|   186|  - 核心要点 3: 在Curtu速率模型和Morris-Lecar突触抑制耦合模型中验证了该机制的普适性
   506|   373|   240|   187|  - **Activation**: mixed-mode oscillations, MMO, cusped singularity, slow-fast neural system, mutual inhibition oscillation, singular perturbation neural, blow-up method neural, neural oscillation mechanism
   507|   374|   241|   188|
   508|   375|   242|   189|## 2026-05-08 - Neuroscience Research (Cron Job)
   509|   376|   243|   190|## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
   510|   377|   244|   191|
   511|   378|   245|   192|### The true cost of factoring: Linking magic and number-theoretic complexity in Shor's algorithm
   512|   379|   246|   193|- [[quantum-magic-number-theory-complexity]] - Links quantum magic (non-stabilizerness) resource cost to classical number-theoretic hardness of factoring (arXiv: 2605.05347)
   513|   380|   247|   194|  - 核心要点 1: 量子算法的真实成本应由非稳定态资源（magic）衡量，而非单纯的门计数
   514|   381|   248|   195|  - 核心要点 2: Shor算法中magic的生成量与数论问题的计算难度直接相关
   515|   382|   249|   196|  - **Activation**: quantum magic, non-stabilizerness, Shor's algorithm, number theory complexity, resource theory
   516|   383|   250|   197|
   517|   384|   251|   198|### Quantum Proper Scoring Rules: Minimax Estimation and Resource-Theoretic Advantages
   518|   385|   252|   199|- [[quantum-proper-scoring-rules]] - Generalizes proper scoring rules to quantum domain with operator convex generators and Quantum Cramér-Rao-McCarthy Bound (arXiv: 2605.05268)
   519|   386|   253|   200|  - 核心要点 1: 将经典评分规则推广到量子密度算符域，定义量子价值泛函
   520|   387|   254|   201|  - 核心要点 2: 证明量子Cramér-Rao-McCarthy界，连接量子Fisher信息与估计风险
   521|   388|   255|   202|  - **Activation**: quantum scoring rules, state estimation, Cramer-Rao bound, quantum Fisher information, metrology
   522|   389|   256|   203|
   523|   390|   257|   204|### A multi-scale information geometry reveals the structure of mutual information in neural populations
   524|   391|   258|   205|- [[multi-scale-information-geometry-neural]] - 多尺度信息几何揭示神经群体编码的互信息结构，Fisher信息度量的多尺度扩展直接关联互信息 (arXiv: 2605.06304)
   525|   392|   259|   206|  - 核心要点1: 唯一黎曼表示几何从粗粒化下距离收缩的第一原理自然涌现，多尺度扩展Fisher信息度量
   526|   393|   260|   207|  - 核心要点2: 度量张量本征向量识别对信息传输贡献最大的刺激变化方向，可通过扩散模型估计
   527|   394|   261|   208|  - **Activation**: information geometry, Fisher information metric, neural population coding, mutual information, representational geometry, diffusion model estimation
   528|   395|   262|   209|
   529|   396|   263|   210|### Decoding Alignment without Encoding Alignment: A critique of similarity analysis in neuroscience
   530|   397|   264|   211|- [[decoding-encoding-alignment-critique]] - 揭示RSA/DSA对齐度量的根本缺陷：解码对齐不代表计算相似性，高对齐分数可由极少数神经元子群体驱动 (arXiv: 2605.05907)
   531|   398|   265|   212|  - 核心要点1: 解码对齐(RSA/DSA)无法反映神经元群体的编码拓扑，相似解码行为可由小神经元子集主导
   532|   399|   266|   213|  - 核心要点2: 引入编码流形作为补充分析工具，必须同时报告解码对齐和编码拓扑才能得出有效结论
   533|   400|   267|   214|  - **Activation**: decoding alignment, encoding manifold, RSA critique, brain-DNN comparison, representational similarity
   534|   401|   268|   215|
   535|   402|   269|   216|
   536|   403|   270|   217|### Efficient Event-Driven Retrieval in High-Capacity Kernel Hopfield Networks
   537|   404|   271|   218|- [[event-driven-hopfield-retrieval]] - KLR Hopfield网络的异步事件驱动检索，实现接近O(N)存储容量的神经形态联想记忆 (arXiv: 2605.05978)
   538|   405|   272|   219|  - 核心要点 1: 异步序列更新在调优核参数下与同步动力学统计不可区分，保持高召回率
   539|   406|   273|   220|  - 核心要点 2: KLR学习诱导的大边际吸引子创造平滑能量景观，收敛事件数≈初始汉明距离，适合稀疏神经形态计算
   540|   407|   274|   221|  - **Activation**: kernel hopfield, event-driven retrieval, KLR Hopfield, asynchronous associative memory, neuromorphic memory, large-margin attractor
   541|   408|   275|   222|
   542|   409|   276|   223|### Think-Aloud Reshapes Automated Cognitive Model Discovery Beyond Behavior
   543|- [[think-aloud-cognitive-model-discovery]] - 通过Think-Aloud协议增强自动认知模型发现，超越纯行为数据捕捉决策过程中的推理和元认知 (arXiv: 2605.05091)
   544|  - Think-Aloud口头报告作为额外数据约束，显著提升认知模型发现的可解释性和准确性
   545|  - 纯行为数据无法区分的竞争模型可通过语言报告有效区分
   546|  - **Activation**: think-aloud protocol, cognitive model discovery, verbal protocol analysis, decision-making cognition
   547|
   548|### Beyond Object-Level Alignment: Do Brains and DNNs Preserve the Same Transformations?
   549|   410|   277|   224|- [[brain-dnn-transformation-alignment]] - 基于范畴论的自然性违反分数(NVS)评估脑-DNN变换级对齐，揭示语义/视觉轴的分层交叉 (arXiv: 2605.06420)
   550|   411|   278|   225|  - 核心要点 1: 将脑-DNN对齐从刺激级对应提升到变换保持测试，NVS量化与置换零模型的偏差
   551|   412|   279|   226|  - 核心要点 2: 发现分层交叉现象——语义轴对齐高层视觉皮层+深层DNN，低级视觉轴对齐早期皮层+浅层
   552|   413|   280|   227|  - **Activation**: naturality violation score, NVS, brain-DNN alignment, transformation alignment, category theory neuroscience, hierarchy crossover
   553|   414|   281|   228|
   554|   415|   282|   229|## 2026-05-08 - Number Theory, Statistics, Advanced Mathematics + Quantum Mechanics (Cron Job)
   555|   416|   283|   230|
   556|   417|   284|   231|### Beyond Gates: Pulse Level Quantum Fourier Models
   557|   418|   285|   232|- [[pulse-level-quantum-fourier]] - 脉冲级量子傅里叶模型参数化，通过独立子角调优提升QML训练性能 (arXiv: 2605.04945)
   558|   419|   286|   233|  - 核心要点 1: 独立脉冲缩放替代单一逻辑角，释放高维梯度下降逃逸路径
   559|   420|   287|   234|  - 核心要点 2: 复合门中子角独立性显著提升训练性能，但不改变全局表达能力
   560|   421|   288|   235|  - **Activation**: 脉冲级量子计算, 量子傅里叶模型, QML优化, pulse-level QFM, composite gate optimization
   561|   422|   289|   236|
   562|   423|   290|   237|### Block Permutation Routing on Ramanujan Hypergraphs for Fault-Tolerant Quantum Computing
   563|   424|   291|   238|- [[ramanujan-hypergraph-routing]] - Ramanujan超图上的块排列路由用于容错量子计算 (arXiv: 2605.05036)
   564|   425|   292|   239|  - 核心要点 1: Ramanujan超图上的块排列路由，保持谱比的高连通性
   565|   426|   293|   240|  - 核心要点 2: 谱继承三层级：精确(Haemers)、扰动(Weyl)、通用(Cheeger)
   566|   427|   294|   241|  - **Activation**: 量子路由, 表面编码, 超图变换, QCCD架构, fault-tolerant routing, block permutation
   567|   428|   295|   242|
   568|   429|   296|   243|### Integral Means Spectrum for the Random Riemann Zeta Function
   569|   430|   297|   244|- [[random-riemann-zeta-spectrum]] - 随机黎曼ζ函数积分均值谱证明Kraetzer猜想 (arXiv: 2603.26507)
   570|   431|   298|   245|  - 核心要点 1: 随机ζ函数原函数的积分均值谱几乎必然符合Kraetzer猜想形式
   571|   432|   299|   246|  - 核心要点 2: 建立ζ函数临界线收敛到全纯GMC分布的替代推导
   572|   433|   300|   247|  - **Activation**: 黎曼ζ函数, 积分均值谱, 高斯乘性混沌, Kraetzer猜想, 单叶函数
   573|   434|   301|   248|
   574|   435|   302|   249|### The true cost of factoring: Linking magic and number-theoretic complexity in Shor's algorithm
   575|   436|   303|   250|- [[quantum-magic-complexity]] - 量化Shor算法中magic资源，建立数论问题经典难度与量子非稳定子资源的直接联系 (arXiv: 2605.05347)
   576|   437|   304|   251|  - 核心要点 1: Magic(non-stabilizerness)是量子超越经典计算的关键资源，Shor算法在实用参数下最大化利用该资源
   577|   438|   305|   252|  - 核心要点 2: 经典算法难度与解决该问题所需的非稳定子价格成正比，补充传统电路成本分析
   578|   439|   306|   253|  - **Activation**: quantum magic complexity, non-stabilizerness, Shor algorithm resource, magic state distillation, stabilizer formalism, fault-tolerant overhead
   579|   440|   307|   254|
   580|   441|   308|   255|### Quantum Proper Scoring Rules: Minimax Estimation and Resource-Theoretic Advantages
   581|   442|   309|   256|- [[quantum-proper-scoring-rules]] - 将适当评分规则推广到量子领域，用密度算子替代概率分布，推导量子态层析minimax最优界 (arXiv: 2605.05268)
   582|   443|   310|   257|  - 核心要点 1: 通过算子凸生成元定义量子值泛函，建立量子Cramér-Rao-McCarthy界，连接minimax风险与量子Fisher信息
   583|   444|   311|   258|  - 核心要点 2: 量化相干性、纠缠、自适应性等量子资源在预测任务中的经济价值，证明经典-量子缩放分离
   584|   445|   312|   259|  - **Activation**: quantum proper scoring rules, quantum state estimation, quantum Fisher information, minimax quantum, quantum Cramer-Rao bound, quantum resource economics
   585|   446|   313|   260|
   586|   447|   314|   261|### Analytical Angle-Finding for QSP via Orthogonal Polynomial Theory
   587|   448|   315|   262|- [[qsp-orthogonal-polynomials]] - 利用Hermite/Jacobi/Rogers-Szego多项式正交性，为量子信号处理提供旋转角度解析解 (arXiv: 2605.05321)
   588|   449|   316|   263|  - 核心要点 1: QSP可实现多项式基由正交性/双正交性刻画，2n+2个角度编码次数≤n的多项式序列
   589|   450|   317|   264|  - 核心要点 2: 光滑函数ε近似可通过Hermite级数展开以O(log(1/ε))个门实现块编码
   590|   451|   318|   265|  - **Activation**: QSP angle finding, quantum signal processing, orthogonal polynomial, Hermite QSP, block encoding, SU(1,1)-QSP
   591|   452|   319|   266|
   592|   453|   320|   267|### Universal Neural Propagator: Learning Time Evolution in Many-Body Quantum Systems
   593|   454|   321|   268|- [[quantum-neural-propagator]] - 学习从驱动协议到时间演化传播子的泛函映射，在驱动空间和指数大初态空间上同时预测量子动力学 (arXiv: 2605.05299)
   594|   455|   322|   269|  - 核心要点 1: 从学习量子态转向学习算子，单个UNP模型覆盖函数空间的驱动协议和希尔伯特空间的初态
   595|   456|   323|   270|  - 核心要点 2: 自监督训练，在超出精确对角化能力的系统尺寸上保持准确，可仅用可观测量数据微调
   596|   457|   324|   271|  - **Activation**: universal neural propagator, quantum dynamics learning, quantum foundation model, driven quantum systems, time evolution propagator, transferable simulation
   597|   458|   325|   272|
   598|   459|   326|   273|### Semantics-Based Verification of Shor Oracle for ECDLP
   599|   460|   327|   274|- [[quantum-program-semantic-verification]] - 量子程序语义验证方法，针对Shor类数论算法的群操作预言机进行语义级规范和精化验证 (arXiv: 2605.01008)
   600|   461|   328|   275|  - 核心要点 1: Shor类ECDLP算法对群操作预言机的语义高度敏感，微小实现选择可使数学模型失效
   601|   462|   329|   276|  - 核心要点 2: 即使通过平凡控制健全性检查，受控执行仍可能违反预期控制律，语义审计是可信量子软件的必要前提
   602|   463|   330|   277|  - **Activation**: quantum program verification, Shor oracle, ECDLP quantum, semantic auditing, Qrisp verification, refinement verification, number-theoretic algorithms
   603|   464|   331|   278|
   604|   465|   332|   279|### Beating Noise in Frequency Estimation with Squeezing and Memory
   605|   466|   333|   280|- [[quantum-noise-robust-metrology]] - 连续变量系统中的量子计量方法，通过哈密顿工程(压缩)和非马尔可夫环境记忆实现抗噪频率估计 (arXiv: 2605.06263)
   606|   467|   334|   281|  - 核心要点 1: 将压缩嵌入系统哈密顿使QFI获得可调高阶时间依赖性，短时区灵敏度超越标准估计
   607|   468|   335|   282|  - 核心要点 2: 结构化环境的非马尔可夫记忆可诱导信息回流，暂时恢复甚至超过无噪声估计极限
   608|   469|   336|   283|  - **Activation**: quantum metrology, frequency estimation, quantum Fisher information, squeezing, non-Markovian, continuous-variable, noise mitigation, quantum sensing
   609|   470|   337|   284|
   610|   471|   338|   285|## 2026-05-08 - Neuroscience Research (Cron Job)
   611|   472|   339|   286|
   612|   473|   340|   287|### TRIBE v2: A Tri-Modal Brain Foundation Model
   613|   474|   341|   288|- [[tribev2-brain-foundation-model]] - 三模态(视频/音频/语言)脑活动预测基础模型，统一预测1000+小时fMRI、720被试的高分辨率脑响应，实现in-silico神经科学实验 (arXiv: 2605.04326)
   614|   475|   342|   289|  - 核心要点 1: Transformer架构整合三模态特征，通过modality dropout学习鲁棒跨模态表征，显著超越传统线性编码模型
   615|   476|   343|   290|  - 核心要点 2: 支持零样本泛化到新刺激/任务/被试，通过subject block插值实现未见被试预测，可恢复数十年实证研究结果
   616|   477|   344|   291|  - **Activation**: TRIBE v2, brain foundation model, fMRI encoding, multimodal brain prediction, in-silico neuroscience, Algonauts challenge, naturalistic fMRI
   617|   478|   345|   292|
   618|   479|   346|   293|### Neural Manifolds as Crystallized Embeddings
   619|   480|   347|   294|- [[neural-manifolds-crystallized-embeddings]] - 神经流形结晶嵌入理论：整合自由能原理、广义同步和Hebbian可塑性，解释头方向/网格细胞/视觉流形的发育机制 (arXiv: 2605.04200)
   620|   481|   348|   295|  - 核心要点 1: 广义同步将低维感觉流形嵌入神经状态空间，FEP预测的几何结构从普通循环动力学中自然涌现，而非显式贝叶斯计算
   621|   482|   349|   296|  - 核心要点 2: Hebbian可塑性将同步产生的相关性结晶为循环连接，形成自治连续吸引子网络；成熟流形是发育产物而非基因预设模板
   622|   483|   350|   297|  - **Activation**: neural manifolds, free energy principle, generalized synchronization, Hebbian plasticity, continuous attractor networks, reservoir computing, developmental neuroscience
   623|   484|   351|   298|
   624|   485|   352|   299|## 2026-05-08 - CSS QEC / Hypergraph Routing / Adaptivity Theory (Cron Hourly)
   625|   486|   353|   300|
   626|   487|   354|   301|### A Factor-Graph Formulation of CSS Syndrome Decoding
   627|   488|   355|   302|- [[css-factor-graph-decoding]] - CSS量子纠错症状解码的因子图表述，联合BP与四态BP的等价性证明 (arXiv: 2605.05132)
   628|   489|   356|   303|  - 核心要点 1: 两个Tanner图通过每个量子比特的联合先验耦合，保留X/Z误差分量的信道相关性
   629|   490|   357|   304|  - 核心要点 2: 联合BP与四态BP在状态重标记后计算相同的后验权重、消息和信念
   630|   491|   358|   305|  - **Activation**: CSS syndrome decoding, factor graph QEC, joint belief propagation, four-state BP, Tanner graph coupling, stabilizer code decoder
   631|   492|   359|   306|
   632|   493|   360|   307|### Block Permutation Routing on Ramanujan Hypergraphs
   633|   494|   361|   308|- [[ramanujan-hypergraph-quantum-routing]] - 拉马努金超图上的块置换路由用于容错量子计算，谱分析给出路由复杂度界 (arXiv: 2605.05036)
   634|   495|   362|   309|  - 核心要点 1: 商图谱的谱比在高连通性区域保持，三级谱继承：精确/扰动/通用
   635|   496|   363|   310|  - 核心要点 2: 结合相关解码方案将症状提取开销从O(d²)降至O(d)，路由成为主导项
   636|   497|   364|   311|  - **Activation**: quantum routing, Ramanujan hypergraph, surface code patch routing, fault-tolerant circuit depth, spectral graph bounds, lattice surgery compilation
   637|   498|   365|   312|
   638|   499|   366|   313|### Adaptivity Under Realizability Constraints
   639|   500|   367|   314|- [[adaptivity-realizability-constraints]] - 可实现性约束下自适应性的理论分析，揭示ICL与Agentic Learning的四种场景 (arXiv: 2605.04995)
   640|   501|   368|   315|  - 核心要点 1: 四种场景：无优势/持续优势/仅约束下涌现优势/约束下消失优势
   641|   502|   369|   316|  - 核心要点 2: ReLU可实现性根本性地改变自适应查询的效用，反直觉场景(c)值得注意
   642|   503|   370|   317|  - **Activation**: in-context learning vs agentic, adaptivity theory, realizability constraints, ReLU network approximation, adaptive querying strategy
   643|   504|   371|   318|
   644|   505|   372|   319|## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job)
   645|   506|   373|   320|
   646|   507|   374|   321|### Beyond Gates: Pulse Level Quantum Fourier Models
   647|   508|   375|   322|- [[pulse-level-quantum-fourier-models]] - 脉冲级量子傅里叶模型训练优化方法，通过独立脉冲缩放替换门级参数，松弛局部优化景观，显著提升训练性能 (arXiv: 2605.03xxx)
   648|   509|   376|   323|  - 核心要点 1: 脉冲参数化将单一门角度替换为多个独立可调子角度，为梯度下降提供高维逃逸路径
   649|   510|   377|   324|  - 核心要点 2: 脉冲控制不显著改变全局可表达性，但根本性改变局部优化景观
   650|   511|   378|   325|  - **Activation**: pulse-level quantum computing, quantum Fourier models, QFM training optimization, pulse parameterized quantum circuits, quantum ML hardware control
   651|   512|   379|   326|
   652|   513|   380|   327|### Quantum Prediction of Transport Dynamics in Discretized State Spaces
   653|   514|   381|   328|- [[quantum-bayesian-state-estimation]] - 基于门量子计算机的贝叶斯状态估计算法，使用Wick旋转将扩散转化为色散相位演化，实现Fokker-Planck方程的酉传播 (arXiv: 2604.xxxxx)
   654|   515|   382|   329|  - 核心要点 1: 概率密度编码在量子态振幅中，状态空间随量子比特数指数增长
   655|   516|   383|   330|  - 核心要点 2: 漂移分量在振幅空间中可实现精确线性操作，扩散分量通过Wick旋转实现酉代理
   656|   517|   384|   331|  - **Activation**: quantum Bayesian estimation, Fokker-Planck quantum solver, quantum state prediction, amplitude-encoded probability, Wick rotation diffusion
   657|   518|   385|   332|
   658|   519|   386|   333|### Towards sample-optimal learning of bosonic Gaussian quantum states
   659|   520|   387|   334|- [[sample-optimal-gaussian-state-learning]] - 玻色高斯量子态学习的最优样本复杂度分析，证明Gaussian测量下界Ω(n³/ε²)，任意测量下界Ω(n²/ε²) (arXiv: 2603.xxxxx)
   660|   521|   388|   335|  - 核心要点 1: 纯Gaussian态可用Gaussian测量达到最优，被动Gaussian态需要非Gaussian测量
   661|   522|   389|   336|  - 核心要点 2: 自适应测量对近能量无关缩放不可或缺
   662|   523|   390|   337|  - **Activation**: Gaussian state tomography, sample complexity quantum learning, bosonic state characterization, continuous-variable quantum learning, adaptive quantum measurement
   663|   524|   391|   338|
   664|   525|   392|   339|## 2026-05-08 - Quantum Error Correction (Cron Job)
   665|   526|   393|   340|
   666|   527|   394|   341|### Topological subsystem bivariate bicycle codes with four-qubit check operators
   667|   528|   395|   342|- [[sbb-codes]] - 子系统二元自行车码(SSB)方法，将BB码的高权稳定子检查(≥6)分解为局域权-4规范测量，实现高率qLDPC码的实用化 syndrome extraction (arXiv: 2605.04151)
   668|   529|   396|   343|  - 核心要点 1: CSS子系统构造 — 通过权-4规范算子乘积推断稳定子症状，兼容超导量子比特架构
   669|   530|   397|   344|  - 核心要点 2: 行列式理想判据 — 检测平移不变CSS子系统中是否存在非局域稳定子，决定能否用有限深度Clifford电路解耦规范量子比特
   670|   531|   398|   345|  - 核心要点 3: 已知低开销实例 — [[27,6,3]], [[75,10,5]], [[108,12,6]]，后者在相同码长和距离下比子系统面码多编码6倍逻辑量子比特
   671|   532|   399|   346|  - **Activation**: sbb codes, subsystem bicycle codes, weight-4 qec, bb code syndrome, gauge measurement qec, low-overhead quantum memory, subsystem qldpc
   672|   533|   400|   347|
   673|   534|   401|   348|## 2026-05-08 - Neuroscience Research (Cron Job - Evening)
   674|   535|   402|   349|
   675|   536|   403|   350|### Benchmarking local Hebbian learning rules for memory storage and prototype extraction
   676|   537|   404|   351|- [[hebbian-learning-benchmark-memory]] - 系统评测七种赫布学习规则在联想记忆中的存储容量、原型提取能力和对数据相关性的鲁棒性，贝叶斯-赫布规则在几乎所有条件下表现最优 (arXiv: 2605.01074)
   677|   538|   405|   352|  - 核心要点 1: 加法赫布规则容量最差，协方差学习鲁棒但容量中等，贝叶斯-赫布规则几乎在所有条件下容量最高
   678|   539|   406|   353|  - 核心要点 2: 模块化WTA架构优于非模块化，在存储和原型提取任务中均表现更好
   679|   540|   407|   354|  - **Activation**: hebbian learning benchmark, associative memory, prototype extraction, memory capacity, Bayesian-Hebbian, covariance learning, WTA dynamics, binary pattern storage
   680|   541|   408|   355|
   681|   542|   409|   356|## 2026-05-08 - Systems Engineering Research (Cron Job)
   682|   543|   410|   357|
   683|   544|   411|   358|### Safety by Invariance, Liveness through Refinement: Heterogeneous Contract Framework for Co-Design of Layered Control
   684|   545|   412|   359|- [[heterogeneous-contract-control]] - 基于异构假设-保证契约的分层控制架构协同设计方法，将安全性与活性分解到连续时间安全层和离散时间规划层 (arXiv: 2605.04222)
   685|   546|   413|   360|  - 核心要点 1: 安全-活性分解原则 — CT层单方面执行安全性(鲁棒前向不变性)，DT层双边实现活性(收敛)
   686|   547|   414|   361|  - 核心要点 2: 垂直精化条件 — 通过显式参考总督(ERG)作为契约实现器，避免CBF-QP对低层控制器的干扰
   687|   548|   415|   362|  - **Activation**: layered control, heterogeneous contract, assume-guarantee, safety liveness, vertical refinement, explicit reference governor, contract-based design
   688|   549|   416|   363|
   689|   550|   417|   364|### Experiment-as-Code Labs: A Declarative Stack for AI-Driven Scientific Discovery
   690|   551|   418|   365|- [[experiment-as-code-labs]] - 将实验编码为声明式配置的AI驱动科学发现栈，借鉴云IaC理念实现物理实验室自动化 (arXiv: 2605.04375)
   691|   552|   419|   366|  - 核心要点 1: 三层架构 — 规范层(标准化/可复现)、执行层(安全/可靠)、编排层(可扩展/高效)
   692|   553|   420|   367|  - 核心要点 2: 集中式实验室状态模型 — 设备遥测实时更新状态，支持闭环迭代和安全验证
   693|   554|   421|   368|  - **Activation**: experiment-as-code, EaC lab, autonomous lab, declarative experiment, lab automation, AI scientist
   694|   555|   422|   369|
   695|   556|   423|   370|
   696|   557|   424|   371|### Learning Reveals Invisible Structure in Low-Rank RNNs
   697|   558|   425|   372|- [[low-rank-rnn-learning-dynamics]] - Gradient-descent learning dynamics in low-rank RNNs decomposed into loss-visible (determines function) and loss-invisible (encodes training history) overlaps, explaining why functionally equivalent networks learn differently (arXiv: 2605.04115)
   698|   559|   426|   373|  - Core: Closed-form ODEs for learning in reduced overlap space; exact for linear, asymptotically exact for nonlinear large-N RNNs
   699|   560|   427|   374|  - Key: Loss-invisible overlaps act as memory variables; learning exposes connectivity differences between functionally equivalent networks
   700|   561|   428|   375|  - **Activation**: low-rank RNN learning, RNN overlap space, loss-visible invisible, RNN gradient descent dynamics, RNN learning theory, Ger Barak RNN
   701|   562|   429|   376|
   702|   563|   430|   377|## 2026-05-08 - Neuroscience Research (Cron Job)
   703|   564|   431|   378|
   704|   565|   432|   379|### Dissociating Spatial Frequency Reliance from Adversarial Robustness in Neurally Guided DCNNs
   705|   566|   433|   380|- [[neurally-guided-adversarial-robustness]] - Neural alignment's adversarial robustness stems from representational structure, not spatial frequency bias; LSF/human-channel steering fails to match alignment gains (arXiv: 2605.04443)
   706|   567|   434|   381|  - Core: Dissociation experiment shows frequency bias ≠ robustness mechanism; representational geometry is key
   707|   568|   435|   382|  - Key: Human channel + LSF bias impairs robustness; RSA reveals alignment captures higher-order properties
   708|   569|   436|   383|  - **Activation**: neural alignment robustness, adversarial DCNN defense, spatial frequency analysis, ventral stream modeling, brain-inspired CNN robustness
   709|   570|   437|   384|
   710|   571|   438|   385|### phys-MCP: Control Plane for Heterogeneous Physical Neural Networks
   711|   572|   439|   386|- [[phys-mcp-physical-neural-networks]] - Substrate-aware orchestration for PNNs (molecular, chemical, biological, photonic, memristive, mechanical) with capability models, lifecycle semantics, telemetry, digital-twin bindings, and wetware API (arXiv: 2605.04256)
   712|   573|   440|   387|  - Core: Unified control plane exposing heterogeneous physical neural substrates as discoverable resources
   713|   574|   441|   388|  - Key: Cortical Labs wetware adapter validated; runtime-aware matching + telemetry recovery across backends
   714|   575|   442|   389|  - **Activation**: phys-MCP, physical neural network orchestration, wetware computing, substrate-aware control, neuromorphic edge computing
   715|   576|   443|   390|
   716|   577|   444|   391|## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job)
   717|   578|   445|   392|
   718|   579|   446|   393|### Lottery BP: Unlocking Quantum Error Decoding at Scale
   719|   580|   447|   394|- [[lottery-bp-decoding]] - Randomized belief propagation improves quantum decoding accuracy by 2-8 orders of magnitude for topological codes, with PolyQec architecture reducing OSD calls by 3-5 orders (arXiv: 2605.00038)
   720|   581|   448|   395|  - Core: Lottery BP introduces randomness during BP decoding to break error degeneracy in QLDPC codes
   721|   582|   449|   396|  - Key: Syndrome vote pre-processing compresses multi-round measurements; PolyQec = local BP + global OSD hierarchy
   722|   583|   450|   397|  - **Activation**: quantum error correction decoding, belief propagation randomized, QLDPC scalable decoding, PolyQec architecture, syndrome voting, topological code decoding
   723|   584|   451|   398|
   724|   585|   452|   399|### Hyperspectral Anomaly Detection Using Einstein Fuzzy Computing and Quantum Neural Network
   725|   586|   453|   400|- [[hyfu-had-quantum-fuzzy]] - Hybrid quantum-fuzzy framework for hyperspectral anomaly detection using Einstein fuzzy computing and quantum defuzzifier, achieving state-of-the-art performance (arXiv: 2605.04388)
   726|   587|   454|   401|  - Core: Multi-criteria decision framework combining classical fuzzy rules (Einstein sum/product) with lightweight quantum defuzzifier
   727|   588|   455|   402|  - Key: Einstein fuzzy operations provide smoother transitions than min-max; quantum defuzzifier processes aggregated fuzzy features
   728|   589|   456|   403|  - **Activation**: hyperspectral anomaly detection, Einstein fuzzy computing, quantum neural network, fuzzy multi-criteria decision, quantum defuzzifier, remote sensing
   729|   590|   457|   404|
   730|   591|   458|   405|### Construction and Decoding of Quantum Margulis Codes
   731|   592|   459|   406|- [[quantum-margulis-codes]] - New QLDPC codes from Margulis construction via 2BGA framework, decodable with linear-complexity min-sum decoder unlike BB codes requiring OSD (arXiv: 2503.03936)
   732|   593|   460|   407|  - Core: Margulis codes break Tanner graph group symmetry, mitigating error degeneracy for efficient min-sum decoding
   733|   594|   461|   408|  - Key: Girth-controlled construction (6 or 8); 2-8 orders magnitude better error floor than BB codes
   734|   595|   462|   409|  - **Activation**: quantum Margulis codes, QLDPC code design, min-sum quantum decoding, 2BGA framework, girth-controlled codes, quantum error correction codes
   735|   596|   463|   410|
   736|   597|   464|   411|### Quantum metrology of mixed states via purification
   737|   598|   465|   412|- [[quantum-statistical-metrology]] - Purification-based strategies achieve optimal QCRB and HCRB bounds for multi-parameter quantum estimation, resolving open question about mixed state precision limits (arXiv: 2605.03975)
   738|   599|   466|   413|  - Core: Mixed state quantum metrology via purification; QCRB and HCRB achievable through purified system measurements
   739|   600|   467|   414|  - Key: Any mixed state estimation reduces to equivalent pure state problem; optimal precision bounds proven achievable
   740|   601|   468|   415|  - **Activation**: quantum metrology, quantum estimation, cramér-rao bound, quantum statistics, purification strategy, holevo bound, quantum state discrimination
   741|   602|   469|   416|
   742|   603|   470|   417|### Optimal Error Exponents for Composite Sequential Quantum Hypothesis Testing
   743|   604|   471|   418|- [[quantum-statistical-metrology]] - Sequential quantum hypothesis testing with composite alternatives achieves optimal error exponents via convex optimization (arXiv: 2605.04915)
   744|   605|   472|   419|  - Core: Distinguishing null quantum state from convex set of alternatives with minimal measurements
   745|   606|   473|   420|  - Key: Error exponent analysis for quantum state discrimination; sequential measurement optimization
   746|   607|   474|   421|  - **Activation**: quantum hypothesis testing, sequential quantum testing, quantum state discrimination, error exponents, composite alternatives
   747|   608|   475|   422|
   748|   609|   476|   423|## 2026-05-08 - Neuroscience Research (Cron Job)
   749|   610|   477|   424|
   750|   611|   478|   425|### GeoSAE: Geometric Prior-Guided Layer-Wise Sparse Autoencoder Annotation of Brain MRI Foundation Models
   751|   612|   479|   426|- [[geosae-brain-mri-sae]] - Geometry-guided SAE prevents feature collapse in deep transformer layers, extracts interpretable Alzheimer's biomarkers from frozen brain MRI foundation models with age-deconfounded partial correlations (arXiv: 2605.01829)
   752|   613|   480|   427|  - Core: GeoSAE uses foundation model's learned manifold geometry to guide SAE training; age-deconfounded partial correlations isolate disease-specific signals
   753|   614|   481|   428|  - Key: MCI-to-AD AUC 0.746 with 2% embedding dims; cross-cohort replication r=0.97; neuroanatomical localization consistent with Braak staging
   754|   615|   482|   429|  - **Activation**: GeoSAE, brain MRI foundation model interpretability, sparse autoencoder medical imaging, Alzheimer's biomarker, SAE feature collapse, age-deconfounded analysis, Braak staging localization
   755|   616|   483|   430|
   756|   617|   484|   431|## 2026-05-08 - Number Theory, Statistics + Quantum Mechanics (Cron Job)
   757|   618|   485|   432|
   758|   619|   486|   433|### Towards sample-optimal learning of bosonic Gaussian quantum states
   759|   620|   487|   434|- [[bosonic-gaussian-state-learning]] - Sharp sample complexity bounds for learning n-mode Gaussian states: Omega(n^3/epsilon^2) for Gaussian measurements, non-Gaussian required for passive states (arXiv: 2603.18136)
   760|   621|   488|   435|  - Core: Lower/upper bounds on copies needed to learn Gaussian states to epsilon trace distance; adaptivity indispensable for energy-independent scaling
   761|   622|   489|   436|  - Key: Non-Gaussian measurements provably required for optimal passive state learning; Gaussian measurements nearly optimal for pure states
   762|   623|   490|   437|  - **Activation**: bosonic Gaussian state learning, quantum state tomography sample complexity, continuous-variable quantum learning, Gaussian measurement bounds, passive Gaussian state, quantum state estimation efficiency
   763|   624|   491|   438|
   764|   625|   492|   439|### Finite steps optimise dissipation in stochastically controlled quantum systems
   765|   626|   493|   440|- [[stochastic-quantum-dissipation]] - Thermodynamic cost analysis reveals weak Gaussian noise induces dissipation growing linearly with step count, establishing optimal N* trade-off (arXiv: 2605.04681)
   766|   627|   494|   441|  - Core: Stochastic control noise accumulates linearly across steps, creating optimal step count minimizing total dissipation
   767|   628|   495|   442|  - Key: Conventional 'more steps = better' fails under noise; D_total = D_deterministic + sigma^2 * k * N
   768|   629|   496|   443|  - **Activation**: quantum dissipation, stochastic quantum control, step-equilibration thermodynamics, quantum thermodynamic cost, Gaussian noise quantum control, finite-step quantum optimization
   769|   630|   497|   444|
   770|   631|   498|   445|### Quantum Error Correction Exploiting Quantum Spatial Distribution and Gauge Symmetry
   771|   632|   499|   446|- [[quantum-spatial-error-correction]] - QEC using spin-position superposition and gauge symmetry, resilient to spin/position decoherence and joint dephasing with nearest-neighbor interactions only (arXiv: 2604.25747)
   772|   633|   500|   447|  - Core: 3+2 particle nested square encoding Shor's code; gauge symmetry protects against unified noise model
   773|   634|   501|
## 2026-05-13 - Medicine + Quantum Mechanics (Cron Job)

Today's topic: Medicine (Wednesday) + daily quantum mechanics. arXiv scan found 3 new papers. 90 duplicates cleaned from KG. 3 new skills created.

### FQPDR: Federated Quantum Neural Network for Privacy-preserving Early Detection of Diabetic Retinopathy
- [[federated-quantum-medical]] - 联邦量子神经网络用于医疗隐私保护诊断 (arXiv: 2605.08324v1)
  - 联邦学习 + 量子神经网络实现跨机构医疗诊断，不共享原始患者数据
  - 用于糖尿病性视网膜病变早期检测，微动脉瘤检测
  - **Activation**: federated quantum learning, 联邦量子学习, FQPDR, medical privacy, privacy-preserving diagnosis

### Quantum Kernel Advantage over Classical Collapse in Medical Foundation Model Embeddings
- [[quantum-kernel-advantage]] - 量子核方法在医疗基础模型嵌入中的优势 (arXiv: 2604.24597v1)
  - 在MIMIC-CXR胸片上使用QSVM + 冻结医疗基础模型嵌入证明量子核优势
  - 两阶公平比较框架：MedSigLIP-448, RAD-DINO, ViT-patch32
  - **Activation**: quantum kernel, QSVM, medical foundation model, MIMIC-CXR, quantum advantage

### Quantum Drug Discovery Pipeline (Updated)
- [[quantum-drug-discovery]] - 量子药物发现流水线 (Updated 2026-05-13)
  - 整合量子计算到药物开发全流程：分子模拟→靶点预测→PK/PD建模→临床试验优化
  - PennyLane量子电路模拟房室PK/PD模型
  - **Activation**: quantum drug discovery, PK/PD modeling, PennyLane, clinical trial optimization

