# AI Collection Index

## 2026-06-05 - Neuroscience Research (Cron Job - Update)

### Formalizing the Binding Problem with Information-Theoretic Probing
- [[formalizing-binding-problem]] - Information-theoretic formalization of binding problem with probing method for measuring binding information in Vision Transformers (arXiv: 2606.03976)
  - Binding information quantified via mutual information between feature representations and object identity
  - Spatial tokens carry more binding information than [CLS] token in ViTs
  - Probing framework to diagnose feature misattribution in multi-object scenes
  - ICML 2026 publication from Konrad P. Kording's group
  - **Activation**: binding problem, feature binding, vision transformer, information theory, scene understanding, object attribution, binding probe, feature misattribution

## 2026-06-05 - Neuroscience Research (Cron Job)

### Learning sequence timing and control of replay speed in networks of spiking neurons
- [[stm-sequence-timing-replay]] - Spiking Temporal Memory (sTM) 扩展模型：振荡背景输入作为时钟信号实现序列时序编码和回放速度控制 (arXiv: 2605.22523)
  - 元素时长编码：顺序激活元素特异性神经元群体，跨越宽时间尺度
  - 振荡背景输入作为时钟信号：提供灵活鲁棒的速度控制机制
  - 回放速度与EEG/LFP振荡特征相关：清醒期快速回放，睡眠期慢速回放
  - 经历时间编码：独特稀疏的时空神经活动模式
  - **Activation**: sequence timing, replay speed, sTM, spiking temporal memory, oscillatory control, temporal encoding, sequence processing

## 2026-06-06 - 数论/统计学/高等数学 + 量子力学 (Cron Job)

### Penalty-free quantum optimization applied to lattice protein folding
- [[penalty-free-quantum-optimization]] - 无惩罚量子优化：通过冲突图重构和独立集混合器替代二次惩罚项，保证量子演化全程可行性 (arXiv: 2606.02104)
  - 冲突图编码约束：变量-值对作为节点，互斥关系作为边，合法解=独立集
  - MIS混合器替代横向场混合器：仅在独立集子空间内转移，全程保持可行性
  - 启发式局部搜索：用最多26量子比特子图折叠72长度蛋白质
  - **Activation**: penalty-free optimization, conflict graph, independent set mixer, QAOA, constrained quantum optimization

### High-fidelity neutral atom gates leveraging low-rank Hessian optimization
- [[low-rank-hessian-quantum-control]] - 低秩Hessian量子门校准：利用Hessian矩阵低秩特性，在主轴子空间进行闭环实验优化 (arXiv: 2606.05060)
  - Hessian特征值指数衰减：10-20个主轴方向捕获>95%保真度方差
  - N维波形→k维子空间投影：从1000+参数降至10-20参数
  - 171Yb CZ门99.59%原始保真度，对20%激光功率变化鲁棒
  - **Activation**: low-rank Hessian, quantum gate calibration, waveform optimization, subspace optimization, active subspace

# AI Collection Index


## 2026-06-06 - 数论/统计学/高等数学 + 量子力学 (Cron Job - Batch 2)

### Quantum Time Lower Bounds by Permutation Invariance
- [[quantum-time-lower-bounds]] - 置换不变性建立量子时间复杂度下界：首次系统建立量子电路规模的紧下界，证明SWAP测试、Shift测试、LMR协议的时间最优性 (arXiv: 2606.05099)
  - 核心框架：通过量子样本复杂度归约建立量子时间复杂度下界
  - 应用：SWAP测试纯度估计、Shift测试高阶泛函、LMR协议反射算子均为时间最优
  - **Activation**: quantum time complexity, permutation invariance, SWAP test, LMR protocol, quantum sample complexity, circuit lower bounds

### Extremely slow scaling of minimal Hamming distance in quantum sampling data
- [[hamming-distance-quantum-sampling]] - 量子采样数据中最小汉明距离的极慢标度分析：为量子霸权验证和随机电路采样基准提供新的统计检验工具 (arXiv: 2606.04558)
  - 发现量子采样数据中最小汉明距离的极慢标度行为模式
  - 应用于量子霸权验证：统计假设检验区分量子与经典分布
  - **Activation**: hamming distance, quantum sampling, quantum supremacy verification, random circuit sampling, statistical hypothesis testing

### QPredSGG: Hybrid Quantum Predicate Learning for Long-Tailed Scene Graph Generation
- [[quantum-predicate-learning-sgg]] - 混合量子谓词学习用于长尾场景图生成：4量子比特QP-Head实现256倍参数压缩，mR@100从41.1%提升至57.25% (arXiv: 2606.04689)
  - 振幅嵌入+强纠缠层：4096维特征压缩至16维量子兼容表示，仅96个可训练参数
  - 长尾关系分类：57.25% mean recall@100，比经典CFEN基准提升16个百分点
  - **Activation**: quantum predicate learning, scene graph generation, long-tail classification, amplitude embedding, quantum neural network, hybrid quantum-classical

### Circuit-Level Noise Estimation via Shuttling in Plaquette Circuits
- [[circuit-level-noise-estimation]] - 基于穿梭操作的量子纠错电路级噪声估计：在plaquette电路中系统化表征和量化不同噪声源 (arXiv: 2606.04629)
  - 穿梭测量协议：隔离和量化表面码架构中的不同噪声源
  - 电路级误差建模：为量子纠错码提供更精确的误差模型
  - **Activation**: circuit-level noise, noise estimation, quantum error correction, plaquette circuits, surface code, shuttling measurement


## 2026-06-05 - Neuroscience Research (Cron Job)

### Competition, Stability, and Functionality in Excitatory-Inhibitory Neural Circuits
- [[competition-stability-functionality-ei-networks]] - Game-theoretic energetic framework for asymmetric E-I networks, extends energy-based models with competitive dynamics where each neuron minimizes individual energy (arXiv: 2512.05252)
  - Game-theoretic interpretation: each neuron = rational agent optimizing individual energy
  - Small-gain theorem provides stability guarantees for asymmetric E-I circuits
  - Wilson-Cowan and lateral inhibition models revisited with competitive dynamics
  - Cortical columns as contrast enhancers via hierarchical E/I interplay
  - **Activation**: excitatory-inhibitory, game-theoretic neural dynamics, asymmetric networks, E-I balance, lateral inhibition, cortical columns, competitive dynamics, neural stability

### The Variance Brain Foundation Models Forgot
- [[variance-brain-foundation-models-forgot]] - Brain foundation model variance allocation problem - third-order statistics (co-skewness) predict cognition where billion-parameter models fail (arXiv: 2606.04010)
  - Per-cumulant analysis reveals BFMs destroy co-skewness while preserving covariance
  - Linear co-skewness subspace FC method exceeds all BFMs without pretraining/GPU
  - Scale paradox: BrainLM 650M predicts cognition worse than 111M version
  - Bottleneck identified as pretraining objective, not architecture
  - **Activation**: brain foundation models, variance allocation, third-order statistics, co-skewness, functional connectivity, BFM critique, linear methods, cognition prediction

### Functional Ensembles as Units of Computation in Deep Spiking Networks
- [[functional-ensembles-deep-spiking-networks]] - 1FC groups enable rare high-cofiring events for reliable encoding in SNN, functional connectivity preserved from biological cortex (arXiv: 2606.00073)
  - First-order functionally-connected (1FC) groups: neurons with significant pairwise correlations from previous layer
  - Aggregate cofiring predicts downstream responses via ReLU-like relationship with gain scaling
  - Reliable encoding emerges only during infrequent high 1FC cofiring events
  - Disruption under noise/adversarial perturbations enables targeted layer diagnostics
  - **Activation**: functional ensembles, 1FC groups, SNN functional connectivity, rare cofiring, ensemble encoding, deep spiking networks

### Short-Term Synaptic Plasticity Stabilizes Goal-Conditioned Dynamics
- [[stp-stabilizes-goal-conditioned-dynamics]] - STP in PFC-inspired reservoir model achieves 42% noise robustness improvement for multistep goal-directed action planning (arXiv: 2606.03481)
  - 噪声下成功率：无 STP 75.8% → 49.5%，有 STP 91.8% → 89.2%
  - STP 保留行动可用的目标条件化动力学，动态调制有效连接性
  - 易化主导时间常数范围关联高成功率，非固定循环缩放解释
  - 目标特异性连接模式随时间增强，延迟期后期信息最可用
  - **Activation**: short-term plasticity, STP, goal-conditioned dynamics, PFC reservoir, action planning, noise robustness, dynamic connectivity, Tsodyks-Markram

## 2026-06-04 - Systems Engineering + Quantum Mechanics (Cron Job)

## 2026-06-05 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)

### High-fidelity neutral atom gates leveraging low-rank Hessian optimization
- [[low-rank-hessian-quantum-gate-calibration]] - Low-rank Hessian optimization for calibrating high-fidelity multi-qubit quantum gates (arXiv: 2606.05060)
  - 利用量子控制景观的低秩结构加速多量子比特门校准
  - 通过Hessian特征分解实现高维参数空间的降维优化
  - **Activation**: low-rank Hessian, quantum gate calibration, neutral atom gates, high-fidelity gates

### Minimax Private Estimation of Smooth Optimal-Transport Maps
- [[differential-private-optimal-transport-estimation]] - Differentially private estimation of smooth optimal transport maps (arXiv: 2606.04683)
  - 基于小波密度估计器的差分隐私最优传输映射估计
  - 利用平滑OT映射的稳定性界实现极小极大最优率
  - **Activation**: differential privacy, optimal transport, private estimation, wavelet density

### Fermionic non-Gaussianity via Bell sampling
- [[fermionic-non-gaussianity-bell-sampling]] - Monotones and quantum algorithms for fermionic non-Gaussianity via Bell sampling (arXiv: 2606.05066)
  - 基于Bell采样和费米子协方差算子本征结构的非高斯性度量
  - 解锁费米子量子平台完全计算能力的关键资源量化方法
  - **Activation**: fermionic quantum computing, Bell sampling, non-Gaussianity monotones, covariance operator

### Squeezed Phonon Lasing via Floquet-Controlled Solid-State Defects
- [[floquet-controlled-phonon-lasing]] - Floquet-engineered squeezed phonon laser design using color centers in hBN membranes with coupled spin-mechanical systems (arXiv: 2606.05083)
  - Floquet theory enables engineering of effective Hamiltonians via periodic driving
  - Continuous transition from conventional to squeezed phonon lasing via Floquet parameters
  - Solid-state platform: hBN membrane with color centers + mechanical oscillator
  - Applications in quantum metrology (sub-shot-noise sensing) and quantum control systems
  - **Activation**: floquet engineering, phonon lasing, squeezed states, solid-state defects, hBN membrane, quantum metrology, spin-phonon coupling, periodic driving, steady-state engineering

### Piston Control in Two-Ion Quantum Device
- [[inverse-engineering-quantum-control]] - Inverse engineering protocols for controlling classical piston dynamics driven by quantum ion motion in two-ion trapped devices (arXiv: 2606.03488)
  - Self-consistent stationary state determination with quantum effects
  - Narrow quantum regime connecting two broad classical regimes
  - Inverse engineering: design control from desired trajectory to potential modulation
  - Bridge between classical and quantum control systems engineering
  - **Activation**: inverse engineering, piston control, two-ion device, trapped-ion control, quantum-classical transition, optimal control

### Hybrid Gaussian-exponential zero-noise extrapolation for periodic circuits
- [[hybrid-qnz-zero-noise-extrapolation]] - Hybrid Gaussian-exponential ZNE using CLT on Pauli transfer for NISQ error mitigation (arXiv: 2605.29242)
  - Proves noise amplification factor approaches log-normal distribution under Pauli diagonal errors
  - Augments standard exponential ZNE with Gaussian variance corrections for periodic circuits
  - **Activation**: zero-noise extrapolation, ZNE, noise extrapolation, gaussian exponential noise model, pauli error mitigation, periodic circuit noise, NISQ error mitigation

### Spectral Fusion for Early State Exclusion in Quantum Spin Chains
- [[spectral-fusion-quantum-state-transfer]] - Spectral analysis of perfect state transfer and early state exclusion in symmetric quantum spin chains (arXiv: 2606.04353)
  - Maps spin chain dynamics to Jacobi matrix eigenvalue distributions and eigenvector symmetry
  - Identifies conditions where state overlap vanishes before first PST occurrence
  - **Activation**: perfect state transfer, PST, quantum spin chain, early state exclusion, jacobi matrix, spectral analysis quantum, quantum information transport

### Monitored chaotic scattering
- [[monitored-chaotic-scattering-rmt]] - Extends random matrix theory of chaotic scattering to monitored quantum dots via Kraus operator ensembles (arXiv: 2606.04794)
  - Constructs Kraus operators from circular ensembles for time-resolved measurement
  - Derives discrete-time quantum master equation for charge transfer with equipartition conjecture
  - **Activation**: monitored chaotic scattering, random matrix theory scattering, kraus operators circular ensemble, quantum master equation scattering, charge transfer statistics, quantum dot monitoring

### Decoded Quantum Interferometry Beyond Hamming Space
- [[decoded-quantum-interferometry-beyond-hamming]] - Extends DQI beyond Hamming space to translation association schemes for structured optimization on finite geometries (arXiv: 2606.04843)
  - Generalizes DQI coherent decoding to finite geometries with translation symmetry
  - Points partitioned into shells by distance; quantum Fourier transform adapted to association scheme's character group
  - **Activation**: decoded quantum interferometry, DQI, Hamming space extension, translation association scheme, Bose-Mesner algebra, rank-metric optimization

### Convergence Rates of Sum-of-Hermitian-Squares for Pauli Algebra
- [[sum-of-hermitian-squares-pauli-convergence]] - Explicit convergence rates for SoHS hierarchies over Pauli algebra enabling accuracy guarantees for noncommutative polynomial optimization (arXiv: 2606.04940)
  - First explicit convergence rates for SoHS over Pauli algebra: O(d^2 * n / k) for n-qubit Hamiltonians
  - Enables principled selection of relaxation order vs. computational budget for ground state energy estimation
  - **Activation**: sum-of-hermitian-squares, SoHS, Pauli algebra convergence, noncommutative polynomial optimization, moment relaxation, ground state energy, SDP hierarchy

### Twirled Perfect Tensor Networks
- [[twirled-perfect-tensor-networks]] - Novel class of computationally covariant holographic tensor networks motivated by the Python's Lunch Conjecture (arXiv: 2605.23670)
  - Twirled perfect tensors reduce complexity while maintaining holographic duality properties
  - Complexity scales with bottleneck area rather than bulk volume, matching PLC predictions
  - **Activation**: twirled perfect tensor, python's lunch conjecture, holographic tensor network, computational covariance, black hole interior, tensor network complexity


## 2026-06-04 - Neuroscience Research (Cron Job)

### Discrete Signaling Mediates Chaotic Regularization in RNNs
- [[discrete-signaling-chaotic-regularization]] - Links microscopic chaos to macroscopic neural representation geometry via kernel methods + dynamical mean-field theory (arXiv: 2606.04426)
  - Chaos induces local roughness but preserves global smoothness, acting as intrinsic regularizer
  - Power-law spectral signatures match cortical recordings, explains smooth population codes
  - Game-theoretic structure where each neuron minimizes local energy
  - **Activation**: chaotic regularization, discrete signaling, RNN dynamics, kernel methods, cortical recordings, population codes, neural representations, dynamical mean-field theory

### Competition, Stability, and Functionality in E-I Neural Circuits
- [[competition-stability-ei-circuits]] - Game-theoretic energetic framework for asymmetric E-I networks, extending energy-based models to biological circuits (arXiv: 2512.05252)
  - Each neuron as agent minimizing local energy in competitive game

### SoK: Post-Quantum Cryptography Implementation in Software Systems
- [[pqc-hot-framework]] - PQC-HOT model: Human-Organisation-Technology framework for systematic PQC implementation in software systems (arXiv: 2606.04669)
  - Reveals imbalance in PQC research: technological solutions dominate, human/organisational factors underexplored
  - PQC-HOT model: conceptual framework explaining HOT dimension interactions for implementation outcomes
  - NIST algorithms: ML-KEM, ML-DSA, SLH-DSA + HQC for algorithmic diversity
  - **Activation**: PQC implementation, post-quantum cryptography, quantum-safe migration, PQC-HOT model, NIST PQC, crypto agility

### Information-Geometric Bound on Entanglement Robustness
- [[qfi-entanglement-robustness]] - QFI bounds on concurrence reduction in entanglement generation under parameter uncertainty (arXiv: 2606.05696)
  - Direct connection: concurrence reduction bounded by quantum Fisher information (QFI) with respect to interaction parameter
  - Two interacting qubits: ΔC ≤ √(F_Q)·δθ
  - Trade-off: high QFI benefits sensing precision but increases entanglement sensitivity to fluctuations
  - **Activation**: quantum Fisher information, entanglement robustness, concurrence bounds, quantum network reliability, quantum sensing precision

### High-Rate Seedless Extractors for Device-Independent QKD
- [[seedless-di-qkd-extractors]] - Truncation-based seedless extractors achieving optimal rate of 1 key bit per singlet in DI-QKD (arXiv: 2605.31525)
  - Uses Bell violation as extractor promise instead of min-entropy
  - Truncation method reduces estimation variance, achieves optimal rate with vanishing fraction of rounds
  - Computationally efficient seedless extractors for privacy amplification
  - **Activation**: device-independent QKD, seedless extractor, privacy amplification, Bell violation, quantum key distribution

### Quantum Networks Using Diamond Color Defects
- [[diamond-quantum-networks]] - Comprehensive methodology for diamond NV/SiV centers as scalable quantum network nodes (arXiv: 2605.30005)
  - Excellent optical properties, fast spin-qubit control, long spin coherence times
  - Heterogeneous integration of diamond nanophotonics with photonic integrated circuits
  - Metropolitan-scale quantum network demonstrations with >50 km fiber entanglement
  - **Activation**: diamond color defects, NV center, SiV center, quantum network node, spin-photon interface, quantum repeater

### Coherent Room-Temperature Dipole Synchronization in Nanocavity Sheets
- [[room-temp-quantum-coherence]] - Room-temperature synchronized dipole state in plasmonic nanogap arrays with spatial coherence (arXiv: 2606.06490)
  - Spatial coherence across dipoles without temporal photon coherence or spectral narrowing
  - Driven-dissipative system: fast temporal decay but complex spatial correlations
  - Ultralow mode volumes, high Purcell enhancement, scalable ambient operation
  - **Activation**: room temperature quantum, plasmonic nanocavity, dipole synchronization, driven-dissipative quantum, Purcell enhancement

## 2026-06-08 - Deep Learning Research (Cron Job)

### Latent Reasoning with Normalizing Flows
- [[nf-cot-latent-reasoning-normalizing-flows]] - Normalizing flow framework for continuous thoughts preserving CoT advantages (KV-cache, likelihood estimation) (arXiv: 2606.06447v1)
  - TARFlow-style flow inside LLM backbone with dual-head generation
  - Exact likelihoods for latent thoughts, probabilistic left-to-right decoding
  - Policy-gradient optimization in latent reasoning space
  - **Activation**: latent reasoning, normalizing flows, CoT, continuous thoughts, reasoning optimization

### Compress-Distill: Reasoning Trace Compression for Efficient Knowledge Distillation
- [[compress-distill-reasoning-trace-compression]] - Post-hoc CoT trace compression achieving 18x efficiency with 96% accuracy retention (arXiv: 2606.05988v1)
  - Compresses reasoning traces to 8.6-21.0% original length before distillation
  - 2.0-7.6x training speedup, 3-19x shorter inference outputs
  - Model-compressed beats naive truncation (especially for smaller students)
  - **Activation**: reasoning distillation, trace compression, knowledge distillation, efficient training

### TailLoR: Protecting Principal Components in Parameter-Efficient Continual Learning
- [[tail-lor-spectral-continual-learning]] - Spectral LoRA routing adaptation to long-tail coordinates while protecting principal components (arXiv: 2606.06494v1)
  - Fixed singular bases U, V from pre-trained weights as reference frame
  - Soft spectral penalty discourages dominant direction updates
  - Low-rank update to singular value matrix Σ with interference reduction
  - **Activation**: continual learning, spectral decomposition, LoRA, principal components, adaptation

### You Only Index Once: Cross-Layer Sparse Attention with Shared Routing
- [[clsa-cross-layer-sparse-attention]] - 7.6x decoding speedup, 17.1x throughput at 128K context via shared routing index (arXiv: 2606.06467v1)
  - Token-level top-k selection computed once, reused across cross-decoder layers
  - Preserves fine-grained token selectivity while amortizing routing overhead
  - Joint optimization of pre-filling, KV-cache storage, long-context decoding
  - **Activation**: sparse attention, cross-layer, KV-sharing, routing index, long-context

### IA-RAG: Interval-Algebra-Driven Temporal Reasoning for Dynamic Knowledge Retrieval
- [[ia-rag-interval-algebra-temporal]] - Temporal RAG using Allen's Interval Algebra with Interval Event Units (IEUs) in Thematic Forest (arXiv: 2606.06044v1)
  - Models facts as time intervals with 13 Allen relations (before, meets, overlaps, etc.)
  - Sub-graph Time Tightening refines fuzzy temporal boundaries
  - Strong performance on complex compositional temporal reasoning benchmarks
  - **Activation**: temporal RAG, interval algebra, Allen relations, temporal reasoning, dynamic knowledge

### PSViT: A Methodology for Structurally Pruning Spiking Vision Transformers
- [[psvit-structured-pruning-spiking-vision]] - 22.4% memory saving structured pruning for SViT using sensitivity analysis (arXiv: 2606.03257v1)
  - Three-stage: uniform channel pruning → sensitivity analysis → fine-grained pruning
  - Hardware-agnostic: efficient on existing architectures vs. unstructured pruning
  - 70.3% accuracy without fine-tuning, 72.8% with fine-tuning (original 73.3%)
  - **Activation**: spiking vision transformer, structured pruning, neuromorphic efficiency, SViT

## 2026-06-08 - Neuroscience + Quantum Mechanics (Cron Job - Hourly)

### Breakeven demonstration of quantum low-density parity-check codes
- [[qldpc-breakeven-evaluation]] - Trapped-ion qLDPC breakeven with 4 logical qubits into 18 physical, OMG architecture for mid-circuit measurement without ion transport, 9x better than superconducting (arXiv: 2606.06455)
  - Demonstrates nine QEC codes (qLDPC, topological, concatenated) on single trapped-ion device without hardware reconfiguration
  - Achieves breakeven performance with logical error rates comparable to physical qubit lifetimes
  - Novel OMG (optical-metastable-ground) architecture for addressable mid-circuit measurement and reset
  - Eliminates need for ion transport or dedicated coolant ions, saving runtime and ion count
  - **Activation**: qLDPC evaluation, breakeven demonstration, quantum error correction, trapped-ion qubits, OMG architecture, fault tolerance

### Pretraining Recurrent Networks without Recurrence
- [[supervised-memory-training]] - Supervised Memory Training (SMT) for time-parallel RNN pretraining without BPTT, O(1) gradient path (arXiv: 2606.06479)
  - Decouples what to remember from how to update memory via one-step memory transition labels
  - Transformer-based encoder trained on predictive state objective acquires memory labels
  - Enables time-parallel RNN training with stable O(1) length gradient path without unrolling
  - Outperforms BPTT on language modeling and pixel sequence modeling tasks
  - **Activation**: RNN training, supervised memory, parallel training, predictive state, memory transition, BPTT replacement

### Equivariant Neural Belief Propagation
- [[equivariant-neural-belief-propagation]] - ENBP framework for SE(3)-symmetric probabilistic inference with Gaussian mixture messages, 98.9% conformational coverage (arXiv: 2606.06344)
  - Factor-graph with equivariant Gaussian mixture model messages transforming exactly under SE(3)
  - Rank-2 precision matrices via equivariant outer products with differentiable spectral decomposition
  - 100x faster than diffusion baselines at higher accuracy on GEOM-QM9/GEOM-Drugs
  - Converges on 15+ agent robotic inference where vanilla loopy BP diverges
  - **Activation**: equivariant neural belief propagation, SE(3) symmetry, Gaussian mixture model, factor-graph inference, conformational coverage, molecular modeling
## 2026-06-08 - Neuroscience + Quantum Mechanics (Cron Job - Hourly)

### Nonreversible Gauge Fields in Fokker-Planck Dynamics
- [[gauge-field-fokker-planck-dynamics]] - 非可逆规范场福克-普朗克动力学方法论：将保持稳态分布的扰动公式化为规范场，变形弛豫谱而不改变不变状态，连接超对称哈密顿量与神经网络学习 (arXiv: 2606.06412)
  - Gauge Field Formulation: 非可逆扰动保持稳态分布，规范场变形弛豫谱
  - Supersymmetric Hamiltonian: 打破细致平衡后FP算子成为非厄米超对称哈密顿量
  - Paired Eigenvalue Spectra: H和H†共享除零模式外的特征值
  - Neural Network Learning: 神经网络学习有限力加速收敛同时保持目标分布
  - **Activation**: gauge field, fokker-planck dynamics, supersymmetric hamiltonian, nonreversible perturbation, neural network learning, stationary distribution, spectral gap, non-hermitian dynamics, 规范场, 非厄米量子力学

### Quantum Vector Hopfield Network (Existing Skill Enhanced)
- [[quantum-vector-hopfield-network]] - 量子矢量Hopfield网络：模式由量子矢量自旋方向形成，量子动力学从自旋算符非对易性自然涌现，量子稳定化记忆模式 (arXiv: 2606.06597)
  - Quantum Vector Spins: 模式由量子矢量自旋方向形成
  - Intrinsic Quantum Dynamics: 量子动力学从自旋算符非对易性自然涌现
  - Enhanced Storage Capacity: 量子相干性提升存储容量
  - Quantum Stabilization: 量子效应稳定记忆模式抵抗热噪声
  - **Activation**: quantum hopfield network, vector spin, associative memory, quantum stabilization, memory capacity, non-commutativity, quantum many-body

### Quantum Correlations in QBism's Reconstruction Program
- [[quantum-correlations-qbism-reconstruction]] - QBism重构计划中的量子关联：qplex几何捕获两结果场景的Tsirelson界但不足以恢复全部量子关联约束 (arXiv: 2606.07485)
  - Qplex Geometry: 联合期望值表示为C-向量内积
  - CHSH Scenario: 共享内积结构限制最大值为Tsirelson界2√2
  - CGLMP Inequality: 允许代数最大值4，展现超量子关联
  - Reconstruction Limits: qplex几何捕获足够结构但不足以完全重构量子理论
  - **Activation**: qbism reconstruction, qplex geometry, chsh inequality, cglmp inequality, tsirelson bound, quantum correlations, superquantum, bell inequality
