## 2026-05-31 - Systems Engineering Research (Cron Job)

### BuilDyn: Excitation-Driven Data Generation for Building Thermal Dynamics
- [[excitation-driven-control-optimization]] - 激驱动数据生成框架用于建筑热动力学建模，通过定制化激策略扩展控制驱动状态空间，提升ML模型鲁棒性和泛化能力 (arXiv: 2605.29849)
  - 多频率激策略（步激、正弦、随机、复合）探索完整操作包络
  - 代表性建筑分布采样支持群体级模型训练
  - 故障检测准确率+15-25%，状态空间覆盖+200%
  - **Activation**: excitation strategy, building thermal control, data generation for control, thermal dynamics modeling

### Distributed NMPC for District Heating Networks
- [[excitation-driven-control-optimization]] - ADMM分布式非线性MPC用于区域供热网络，基于图建模的分布式协调方案平衡集中式性能与隐私保护 (arXiv: 2605.29841)
  - ADMM本地优化+双变量协调，仅分享流量决策不暴露内部状态
  - 图节点建模建筑热动力学，边建模管道传输延迟
  - 计算加速10x，性能差距<5%，隐私部分可观测性实现
  - **Activation**: distributed MPC, district heating network, ADMM optimization, privacy-preserving control, graph-based thermal modeling

## 2026-06-01 - Information Science + Quantum (Cron Job - Hourly)

### Meta-Quantum Ensemble Framework for Robust Network Intrusion Detection
- [[meta-quantum-ensemble]] - 混合量子经典集成学习框架，融合 QSVM 和 QNN 输出通过随机森林元学习器提升网络入侵检测性能 (arXiv: 2605.28879)
  - QSVM + QNN 双量子分支：基于不同学习机制的互补决策边界
  - 元学习器捕获量子分支间的一致/不一致模式
  - 在 TON IoT 和 CICIDS2017 上改进低 FPR 检测和可靠性指标
  - **Activation**: meta-quantum ensemble, quantum IDS, QSVM QNN fusion, hybrid quantum ensemble, quantum network security

### Quantum Subliminal Learning
- [[quantum-subliminal-learning]] - 量子模型隐式学习安全分析框架，检测通过公共接口继承的隐藏行为特征 (arXiv: 2605.29557)
  - 辅助通道和任务通道两种蒸馏路径分析
  - QNNs 保留大部分隐藏任务信号，而经典 NNs 几乎不传递
  - 统一几何图景：传输由教师漂移幅度和可见隐藏相关漂移比例控制
  - 量子模型供应链安全的具体威胁
  - **Activation**: quantum subliminal learning, QNN security, quantum model distillation, hidden behavior quantum
## 2026-05-31 - Neuroscience Research (Cron Job) - fMRI & BCI

### Brain-IT-VQA: From Brain Signals to Answers
- [[brain-it-vqa-fmri-visual-question-answering]] - fMRI 视觉问答框架，Brain Interaction Transformer 解码语言 tokens 并与语言模型集成回答视觉问题 (arXiv: 2605.29588)
  - Brain-IT-VQA framework：Brain Interaction Transformer 解码语言 tokens + 语言模型集成
  - NSD-VQA dataset：新基准，平均每图20问答对，20控制问题类别，解耦多层次视觉理解
  - 量化可解码的视觉/语义信息类型，分析不同脑区对问题类型的贡献
  - **Activation**: Brain-IT, fMRI VQA, visual question answering, brain decoding, NSD-VQA, language tokens from brain

### Embodied VR Feedback Reshapes Neural Representations to Support Continuous 3D Motor Imagery Decoding
- [[embodied-vr-feedback-3d-motor-imagery-bci]] - 具身 VR 反馈重塑神经表征支持连续 3D 运动想象解码，VR 性能 r=0.762 显著优于 screen r=0.672 (arXiv: 2605.29677)
  - 10 受试者 × 10 sessions，3D 虚拟肢体控制，CNN-LSTM decoder
  - VR 显著优势 8.9-13.0% (p<=0.002, d=1.42-2.05)，固定解码器泛化，本质上更可解码
  - 神络生理：sensorimotor-parietal 去同步增强，motor-frontal 功能连接增强，前部脑岛全波段参与，上顶叶耦合增加
  - **Activation**: embodied VR feedback, motor imagery BCI, 3D virtual limb control, VR vs screen feedback, continuous BCI, neural representations reshaping

### Neural-Behavioral Representation of Natural Whole-body Movement in Monkeys
- [[neural-behavioral-whole-body-movement-monkeys]] - 灵长类自然全身运动神经-行为表征框架，结合大规模硬膜外皮层信号与多视角动作捕捉，自回归编码器-解码器学习紧凑行为先验 (arXiv: 2605.29355)
  - 大规模 epidural cortical signals + multi-view motion capture 自由移动猴子
  - Autoregressive encoder-decoder 学习紧凑 behavior prior，无需显式物理约束
  - 准确且现实的 whole-body kinematics 重建，首个灵长类自然全身运动解码
  - **Activation**: neural-behavioral whole-body, monkey movement decoding, epidural cortical signals, motion capture, behavior prior, motor decoding primate

## 2026-05-31 - Neuroscience Research (Cron Job) - Brain Oscillation Framework
## 2026-05-31 - Information Science + Quantum (Cron Job)

### Elfs, transducers and quantum walks
- [[elfs-quantum-walk-transducers]] - Electric flow sampling methodology for quantum walk-based graph algorithms (arXiv: 2605.30013)
  - Zero-error transducer for implementing electric flow sampling (elfs)
  - Improved quantum walk algorithms for graph search and optimization
  - **Activation**: elfs quantum walk, electric flow sampling, quantum graph search, 量子游走电采样

### Programmable Dissipation via Partial Quantum Error Correction
- [[programmable-dissipation-qec]] - Error-correction cycle as programmable primitive for dissipative dynamics (arXiv: 2605.30217)
  - Logical noise turned into calibrated resource via partial QEC
  - Decoder/recovery rates tuned for desired dissipative dynamics
  - **Activation**: programmable dissipation, partial QEC, logical noise engineering

### Verifying Adversarial Robustness in Quantum Machine Learning
- [[qml-adversarial-robustness-verification]] - Formal framework for verifying adversarial robustness in QML (arXiv: 2605.29877)
  - Fidelity-based robustness lower bound computable from circuit structure
  - Comprehensive formal framework validated on NISQ hardware
  - **Activation**: QML adversarial robustness, quantum ML security, formal verification

### Alternative Adiabatic Quantum Dynamics
- [[alternative-adiabatic-quantum-dynamics]] - Gate-based adiabatic computing without time-dependent Hamiltonian simulation overhead (arXiv: 2605.30110)
  - General framework for deriving adiabatic-alternative algorithms
  - Gate-native implementations using standard quantum gate sets
  - **Activation**: alternative adiabatic quantum, adiabatic gate-based, quantum adiabatic dynamics

### Semidefinite Certificates for Pauli Hamiltonians
- [[semidefinite-certificates-pauli-hamiltonians]] - Explicit finite-level convergence rates for SDP hierarchies in quantum many-body systems (arXiv: 2605.29959)
  - Quantitative guarantees for accessible low hierarchy levels
  - k-local Hamiltonian problem certificates with concrete error bounds
  - **Activation**: semidefinite certificates Pauli, SDP quantum Hamiltonian, ground-state energy bounds

### Tunneling Phase Diagram ML Framework
- [[tunneling-phase-diagram-ml]] - ML framework for decoupling quantum tunneling strength from kinetic isotope effects (arXiv: 2605.30165)
  - Decouples true tunneling from zero-point energy and classical effects
  - Reveals anomalous high KIE-low κ regimes spanning 30 orders of magnitude
  - **Activation**: tunneling phase diagram, kinetic isotope effect ML, quantum tunneling decoupling



### Brain Oscillation Synchronization Framework
- [[brain-oscillation-synchronization-framework]] - 脑网络振荡同步统一计算框架：整合Kuramoto相位动力学+自适应延迟塑性+信息通量优化的综合方法论 (arXiv: 2605.23520, 2605.14680, 2105.08288)
  - 核心机制：频率选择(延迟塑性)、递归共振(嵌入网络噪声)、同步社区(相位耦合)、信息最大化
  - 关键发现：髓鞘化作为学习机制、嵌入网络优化信息通量、同步不是目标而是约束
  - 应用场景：脑网络分析、神经调节建模、神经疾病动力学、BCI设计、神经形态硬件
  - **Activation**: brain oscillation, Kuramoto synchronization, delay plasticity, information flux, recurrence resonance, phase coupling, frequency selection, network attractor, cortical microcircuit, myelination learning

## 2026-05-31 - Neuroscience Research (Cron Job)

### Brain Learning Principles Utilizing Non-Ideal Factors
- [[brain-learning-non-ideal-factors]] - 脑学习利用非理想因素原则：噪声、异质性、结构不规则、分散可塑性、系统误差、混沌动力学作为进化设计原则而非缺陷，赋予鲁棒性、适应性和创造力 (arXiv: 2603.21542)
  - 六大非理想因素：噪声(探索资源)、异质性(多样性机制)、结构不规则(功能特化)、分散可塑性(分布式优化)、系统误差(归纳偏置)、混沌动力学(生成机制)
  - 反范式：缺陷→特征、完美→脆弱、集中→缓慢、稳定→缺乏创造力
  - 神经形态硬件设计指导：拥抱器件变异性、噪声随机计算、不规则架构
  - **Activation**: non-ideal factors, brain robustness, biological noise, neural heterogeneity, chaotic dynamics, decentralized plasticity, systematic errors, neuromorphic hardware, stochastic computing

## 2026-05-31 - Information Science + Quantum Mechanics (Cron Job)

### QML Adversarial Robustness Verification
- [[qml-adversarial-robustness-verification]] - Fidelity-based robustness verification framework for QML models with VeriQR tool and NISQ hardware validation (arXiv: 2605.29877)
  - Fidelity-based robustness lower bound from measurement outcomes (no full tomography)
  - SDP optimal bound for full model knowledge
  - VeriQR: first dedicated QML robustness verification software tool
  - **Activation**: QML robustness, quantum adversarial, QML verification, VeriQR, quantum machine learning robustness

### Quantum Cryptography Chain Rules
- [[quantum-crypto-chain-rules]] - Chain rules for conditional entropies in quantum cryptography security proofs with EAT framework (arXiv: 2605.29787)
  - New intermediate chain rule improving Rényi EAT for device-adjacent settings
  - Proves impossibility of natural DI chain rule tightening
  - Unified framework for comparing existing chain rules
  - **Activation**: quantum cryptography chain rules, EAT entropy accumulation, device-independent security, quantum conditional entropy

### Quantum Subliminal Learning
- [[quantum-subliminal-learning]] - Subliminal learning in quantum neural networks: hidden behavioral trait inheritance through public interfaces, architecture-dependent vulnerabilities (arXiv: 2605.29557)
  - Auxiliary channel: efficient subliminal learning for both classical NNs and QNNs
  - Task channel: architecture-dependent — classical NNs transmit little, QNNs retain most hidden-task signal
  - Unified geometric picture: transmission controlled by teacher drift magnitude × hidden-task visibility fraction
  - Security concern for quantum model supply chains, watermarking applications
  - **Activation**: quantum subliminal learning, model supply chain security, quantum distillation, hidden task inference, QNN security, teacher drift

### Programmable Dissipation via Partial QEC
- [[programmable-dissipation-qec]] - Repurpose QEC cycles as programmable primitives to engineer dissipators for open quantum system simulation (arXiv: 2605.30217)
  - Error-correction cycle induces logical CPTP map; decoder/recovery randomization generates controllable logical channels
  - Direct compilation of target dissipators without ancilla qubits for bath encoding
  - Accuracy criterion: code distance chosen so uncontrolled errors ≪ intended dissipation per step
  - Resource-efficient route to quantum simulation of open quantum systems
  - **Activation**: programmable dissipation, partial QEC, engineered dissipation, dissipator compilation, open quantum simulation, Kraus channel mixing

### Optimal Quantum Differential Privacy via Fisher Information Spectral Analysis
- [[quantum-differential-privacy-qfi]] - QFI度量建立的几何感知量子差分隐私框架，方向依赖噪声对齐QFI特征结构，实现epsilon~0.001等效效用vs经典DP的epsilon~4800 (arXiv: 2605.24166)
  - 核心要点 1: QFI对偶性——同时量化参数估计精度(计量学)和量子态可区分性(隐私)
  - 核心要点 2: 六条定理：最优噪声集中、混合态QFI分解、隐私-效用不确定关系、自适应QFI估计、QFI对齐组合律、硬件噪声隐私放大
  - 核心要点 3: QFI对齐组合律饱和于O(1) vs 标准组合律的O(k)
  - **Activation**: quantum differential privacy, QFI privacy, Fisher information DP, quantum privacy amplification, QFI spectral analysis, geometry-aware DP, hardware noise harnessing

### Precision and Privacy in Distributed Quantum Sensing: A Quantum Fisher Information Duality
- [[quantum-fisher-information-duality]] - 分布式量子传感中QFI对偶性：Heisenberg极限精度实现参数隐私，F_Q(w)+F_Q(v)<=N使得目标传感方向饱和时其他方向QFI为零 (arXiv: 2605.20765)
  - 核心要点 1: N量子比特探针态的QFI对偶约束，任意正交方向w,v满足F_Q(w^T theta)+F_Q(v^T theta)<=N
  - 核心要点 2: Heisenberg极限精度F_Q=N饱和边界同时强制所有其他独立方向QFI为零——即参数隐私条件
  - 核心要点 3: 赤道态(N=2)和GHZ态(N>=2)可达等式
  - **Activation**: quantum Fisher information duality, distributed quantum sensing, parameter privacy, Heisenberg limit, GHZ states, sensor network privacy, QFI bound

### Toward Covert Quantum Computing
- [[covert-quantum-computing]] - 隐蔽量子计算：多租户云平台中量子策略框架下的隐藏计算，离散等周不等式证明仅O(sqrt(n))边界量子比特提供检测信息 (arXiv: 2605.14325)
  - 核心要点 1: 引入隐蔽量子计算概念——adversaries无法检测不可访问QCU上的计算
  - 核心要点 2: 离散等周不等式推导：n量子比特电路中仅O(sqrt(n))边界量子比特提供检测信息
  - 核心要点 3: 在IQM 54-qubit和IBM 156-qubit上发现长程耦合边信道，削弱隐蔽性
  - **Activation**: covert quantum computing, multi-tenant quantum cloud, quantum crosstalk, isoperimetric inequality, side channel, quantum strategy framework, spatial isolation

### Indefinite Causal Order Reverses the Real-Complex Hierarchy
- [[indefinite-causal-order-real-complex]] - 不定因果序下实数量子理论比复数量子理论实现更严格的过程关联，逆转了确定因果序下的层级关系 (arXiv: 2605.30238)
  - 核心要点 1: 过程矩阵框架下研究对称性约束对局部操作的限制
  - 核心要点 2: 锐二分法：有限酉对称性不产生新关联，实数量子理论产生严格更多的过程关联
  - 核心要点 3: 不定因果序下实数量子理论>复数量子理论，与确定因果序下结论相反
  - **Activation**: indefinite causal order, process matrix, real quantum theory, complex quantum theory, symmetry constraints, quantum foundations, causal indefiniteness

## 2026-05-31 - Deep Learning Research (Cron Job)

### Draft-OPD: On-Policy Distillation for Speculative Draft Models
- [[draft-opd-speculative-distillation]] - On-policy distillation for speculative decoding draft models with replay from verification-exposed error positions (arXiv: 2605.29343)
  - Target-assisted rollout for stable continuations during training
  - Error position replay focuses training on draft-induced errors
  - 5× lossless acceleration, 23% improvement over EAGLE-3
  - **Activation**: speculative decoding, draft model, EAGLE, DFlash, acceptance length, on-policy distillation

### SAAS: Self-Aware Reinforcement Learning for Over-Search Mitigation
- [[saas-self-aware-agentic-search]] - Dynamic self-awareness that regulates search behavior without compromising accuracy (arXiv: 2605.29796)
  - Search boundary modeling via contrastive rollouts
  - Boundary-aware reward module with trajectory-level penalties
  - Stage-wise optimization avoids reward hacking
  - **Activation**: over-search, agentic search, search boundary, self-awareness, reasoning, multi-hop

### RiM: Reasoning in Memory - Working Memory for Latent Reasoning
- [[rim-reasoning-in-memory]] - Latent reasoning with memory blocks replacing autoregressive generation, single forward pass (arXiv: 2605.30343)
  - Two-stage curriculum: grounding phase then refinement phase
  - Fixed memory blocks unlock working-memory capacity
  - Matches/exceeds latent reasoning methods without autoregressive thoughts
  - **Activation**: latent reasoning, working memory, memory blocks, test-time compute

### CGPO: Critic-Guided Diffusion Policy Optimization
- [[cgpo-critic-guided-diffusion-policy]] - Training-free guidance in diffusion policy denoising, balances exploration-exploitation (arXiv: 2605.30056)
  - Steers actions toward high-value regions via critic network
  - Uses guided actions as regression objectives
  - SOTA on MuJoCo locomotion, first real-world diffusion RL (Franka robot arm)
  - **Activation**: diffusion policy, critic guidance, MuJoCo, robotics, exploration exploitation

## 2026-05-31 - Information Science + Quantum (Cron Job)

### Programmable Dissipation via Partial Quantum Error Correction
- [[programmable-dissipation-qec]] - 将量子纠错循环视为可编程原语，将逻辑噪声转化为校准耗散资源，解码器/恢复比控制耗散强度 (arXiv: 2605.30217)
  - 核心要点 1: QEC循环诱导逻辑CPTP映射，通过控制解码器/恢复比α编程耗散强度
  - 核心要点 2: 连续极限下逼近Lindbladian动力学，耗散率γ(α)由部分QEC参数可调
  - 核心要点 3: 支持故障容忍耗散态制备、噪声即资源计算、目标耗散工程设计
  - **Activation**: programmable dissipation, partial qec, logical cptp map, decoder recovery ratio, lindbladian engineering, fault tolerant dissipation, open quantum dynamics, noise as resource, syndrome dependent recovery

### Boosting Uncloneable Encryption in Microcrypt
- [[uncloneable-encryption-microcrypt]] - 从一次性安全单比特不可克隆加密扩展到多次安全多比特不可克隆加密的归约方法 (arXiv: 2605.27647)
  - 核心要点 1: t→t′不可克隆比特可提升为m次安全不可克隆加密
  - 核心要点 2: 最小化不可克隆加密存在的假设条件
  - 核心要点 3: 对称密钥加密的强不可克隆不可区分性形式化
  - **Activation**: uncloneable encryption, microcrypt, quantum cryptography, ciphertext cloning prevention, symmetric key quantum encryption

### Non-Clifford Crosstalk Noise in Surface Codes
- [[non-clifford-crosstalk-surface-codes]] - 混合稳定子-张量网络模拟技术捕获表面码中非Clifford串扰噪声的完整动力学 (arXiv: 2605.29514)
  - 核心要点 1: 超越传统非相干噪声模型，捕获含噪声量子系统的完整动力学
  - 核心要点 2: 混合稳定子-张量网络方法实现经典可扩展模拟
  - 核心要点 3: 含噪声纠错协议的阈值分析
  - **Activation**: non-clifford crosstalk, surface codes, hybrid stabilizer tensor network, noise simulation, qec threshold, fault tolerant analysis

### Simple Power Analysis on Post-Quantum Cryptosystems
- [[spa-post-quantum-cryptosystems]] - 简单功耗分析(SPA)评估后量子编码理论密码系统(McEliece/BIKE)的物理安全性 (arXiv: 2605.17116)
  - 核心要点 1: 低成本设备SPA攻击评估代码基KEM的物理实现安全性
  - 核心要点 2: 经典结构攻击通过适当密钥尺寸可被消除但物理侧信道仍有效
  - 核心要点 3: 后量子密码部署的侧信道防护需求
  - **Activation**: simple power analysis, post-quantum cryptography, mceliece, bike kem, side channel, physical security, code based cryptography

### Quantum-Safe 6G PQC Evaluation
- [[quantum-safe-6g-pqc-evaluation]] - Practical evaluation methodology for deploying NIST-standardized Post-Quantum Cryptography in 6G/IoT networks (arXiv: 2605.06881)
  - Benchmarks ML-KEM/Kyber, ML-DSA/Dilithium, and Falcon on heterogeneous platforms
  - Ciphertext/signature size expansion critically impacts handshake reliability at edge
  - Three deployment patterns: hybrid handshake, size-optimized, asynchronous PQC
  - **Activation**: quantum-safe 6G, PQC deployment, NIST post-quantum, ML-KEM, ML-DSA, Falcon, quantum-secure networks

### Quantum-Secure PUF via Silicon Photonics
- [[quantum-secure-puf-silicon-photonics]] - Quantum readout protocol for Physical Unclonable Functions using SiN MZI meshes with equal error rates as low as 10^-14 (arXiv: 2605.14959)
  - Maximally mixed quantum states conceal unitary transformation from eavesdropping
  - Single-photon detection + Monte Carlo security analysis
  - CMOS-compatible silicon nitride fabrication for scalable deployment
  - **Activation**: quantum PUF, physical unclonable function, silicon photonics security, quantum authentication, hardware security

### DPF-based Error-Detecting IT-PIR over Rings
- [[dpf-error-detecting-pir-rings]] - Efficient Distributed Point Function based error-detecting Information-Theoretic PIR over ring structures (arXiv: 2604.00411)
  - Information-theoretic privacy with cryptographic error detection
  - Ring-based construction for efficiency over field-based approaches
  - Tolerates adversarial servers with algebraic verification
  - **Activation**: private information retrieval, DPF, IT-PIR, ring cryptography, secure database query

## 2026-05-30 - Neuroscience Research (Cron Job) - SNN Architecture Innovation

### CogniSNN: Enabling Neuron-Expandability, Pathway-Reusability, and Dynamic-Configurability with Random Graph Architectures in Spiking Neural Networks
- [[cognisnn-random-graph-snn]] - 随机图架构SNN实现神经元可扩展性、路径可复用性和动态可配置性，KP-LwF多任务迁移+DGL动态生长算法，SOTA性能 (arXiv: 2512.11743)
  - 核心要点 1: 随机图架构打破传统链式层级结构，模仿生物神经元随机互联特征
  - 核心要点 2: 改进纯脉冲残差机制+自适应池化策略解决深层路径退化问题
  - 核心要点 3: KP-LwF选择性复用关键神经路径，DGL算法沿时间维度动态增长神经元和突触
  - **Activation**: cognisnn, random graph snn, pathway reusability, dynamic growth, kp-lwf, neuromorphic hardware, continual learning, brain-inspired architecture, stochastic connectivity

### Event-driven Eligibility Propagation in Large Sparse Networks: Efficiency Shaped by Biological Realism
- [[event-driven-eligibility-propagation]] - 事件驱动eligibility propagation扩展，生物真实约束塑造效率，连续动力学+严格局部性+稀疏连接，百万神经元规模学习 (arXiv: 2511.21674)
  - 核心要点 1: 时间驱动转为事件驱动，仅处理脉冲事件，稀疏网络开销骤降
  - 核心要点 2: 三大生物约束：连续动力学、严格局部性（突触仅用局部信息）、稀疏连接（10%连接概率）
  - 核心要点 3: Neuromorphic MNIST成功训练，跨越机器学习与计算神经科学的桥梁
  - **Activation**: event-driven e-prop, eligibility trace, sparse snn, biologically plausible, local plasticity, neuromorphic hardware, scalability, recurrent snn, synaptic tag

## 2026-05-30 - Neuroscience Research (Cron Job) - Embodied VR Feedback

### Embodied VR Feedback Reshapes Neural Representations to Support Continuous Three-Dimensional Motor Imagery Decoding
- [[embodied-vr-feedback-reshapes-neural-representations]] - VR反馈重塑神经表征支持3D运动想象BCI解码，性能提升13% (arXiv: 2605.29677v1)
  - VR反馈优于Screen反馈（r=0.762 vs 0.672），Cohen's d=1.42-2.05大效应
  - 固定解码器证明VR引发更可解码神经表征，非适应性差异
  - Sensorimotor-parietal去同步化增强，Anterior insula广泛参与所有频段
  - **Activation**: embodied vr feedback, vr bci, 3d motor imagery, neural representations, continuous bci, sensorimotor decoding

## 2026-05-30 - Economics, Investment + Quantum (Cron Job) - Actuarial Runtime

### Foundations of a Time-Consistent Counterfactual Actuarial Runtime for Autonomous AI Agents
- [[actuarial-runtime-ai-agents]] - 自主AI代理的精算运行时框架，每个副作用动作携带时间一致的逆事实风险通行费，预动作交易层替代事后责任保险 (arXiv: 2605.26508)
  - 核心要点 1: 四个结构性结果——逆事实通行费恒等式、不可分割性质、不可逆权威溢价、保守运行时门限定理
  - 核心要点 2: 承保边界设计决定系统的防博弈能力，边界越大决策越少但博弈风险越高
  - 核心要点 3: 将高概率风险包络转化为执行动作预算保证，提供数学担保
  - **Activation**: actuarial runtime, AI agent safety, counterfactual risk, time-consistent risk, per-action insurance, risk toll, underwriting boundary, 精算运行时, 自主AI安全

## 2026-05-30 - Economics, Investment + Quantum (Cron Job) - Part 4

### End-to-End PDE-Based Quantum Algorithms for Multi-Asset Option Pricing
- [[quantum-pde-option-pricing]] - 端到端量子PDE框架求解多维期权定价，处理Black-Scholes和Heston模型，N=2^n网格点实现指数加速 (arXiv: 2605.26610)
  - 核心要点 1: 将定价PDE通过有限差分离散化为线性系统，用量子线性系统算法(QLSA)求解
  - 核心要点 2: 端到端分析包含编码、求解、读出所有子程序，提供显式复杂度界
  - **Activation**: quantum option pricing, quantum PDE solver, Black-Scholes quantum, Heston model quantum, multi-asset option, 量子期权定价, 量子PDE

### Learning Quantum-Samplers for Stochastic Processes with Quantum Sequence Models
- [[quantum-stochastic-sampling]] - 量子序列模型学习随机过程，递归量子电路处理指数级概率向量，加速风险分析和重要性采样 (arXiv: 2603.24069)
  - 核心要点 1: n量子比特表示2^n维概率分布，递归结构捕获时间依赖性
  - 核心要点 2: 应用于金融风险分析、重要性采样和蒙特卡洛加速
  - **Activation**: quantum stochastic process, quantum risk analysis, quantum importance sampling, quantum sequence model, quantum recurrent circuit, 量子随机过程

## 2026-05-30 - Economics, Investment + Quantum (Cron Job) - Part 3

### PortBench: A Correlation-Aware, Full-Pipeline Benchmark for LLM-Driven Portfolio Management
- [[portbench-llm-portfolio-benchmark]] - LLM组合管理基准测试，双层评估（静态QA+动态分配流水线），CEPS衡量误差传播，90%的LLM无法跑赢等权分配 (arXiv: 2605.27887)
  - 核心要点 1: 现有基准忽略跨资产相关性且未评估完整PM决策流水线
  - 核心要点 2: CEPS量化流水线各阶段推理误差的复合效应，揭示程序合规≠性能
  - 核心要点 3: 压力制度测试是关键——正常条件下表现良好的模型在危机中可能崩溃
  - **Activation**: LLM portfolio benchmark, PortBench, CEPS, correlation-aware PM, stress regime testing, 大模型投资组合, 组合管理基准

### Regime-Based Portfolio Allocation Using Hidden Markov Models and Reinforcement Learning
- [[hmm-rl-regime-portfolio-allocation]] - HMM检测3种市场制度+RL优化配置，超越SPY基准且回撤更低 (arXiv: 2605.27848)
  - 核心要点 1: BIC选择3种制度（低波/过渡/高波），不同制度下主导资产不同
  - 核心要点 2: HMM提供可解释的制度标签，RL在制度内优化配置，两者结合透明且高性能
  - **Activation**: HMM portfolio, regime detection, RL allocation, hidden markov model, tactical asset allocation, 制度检测, 马尔可夫模型

## 2026-05-30 - Economics, Investment + Quantum (Cron Job)

### A Tutorial on Portfolio Selection with Quantum Computing
- [[quantum-portfolio-optimization-qaoa]] - 量子计算在投资组合优化中的系统方法论，涵盖QUBO建模、QAOA算法、约束保持混合器、误差缓解技术 (arXiv: 2312.02173)
  - 核心要点 1: 将Markowitz均值-方差投资组合模型转化为QUBO形式，使用惩罚项处理预算和基数约束
  - 核心要点 2: 约束保持混合器(XY-mixer)比传统X-mixer更优，自动保持在可行子空间，减少不可行解
  - 核心要点 3: NISQ时代建议浅层电路+ZNE误差缓解+绝热参数初始化，避免Barren Plateau问题
  - **Activation**: quantum portfolio, QAOA portfolio, QUBO modeling, XY-mixer, constraint-preserving mixer, NISQ finance, 量子投资组合, 量子金融

## 2026-05-30 - Neuroscience Research (Cron Job) - Part 7

### Neural-Behavioral Representation of Natural Whole-body Movement in Monkeys
- [[neural-behavioral-whole-body-movement-monkeys]] - 首个框架结合大规模硬膜外皮质信号与多视角运动捕捉解码自然全身体运动，无需显式物理约束即可重建真实运动轨迹 (arXiv: 2605.29355v1)
  - 核心要点 1: 大规模硬膜外电极阵列覆盖感觉运动相关区域，多视角同步捕捉重建完整身体骨架
  - 核心要点 2: 自回归编码器-解码器学习紧凑行为先验，皮质信号条件化解码器生成准确运动轨迹
  - **Activation**: whole-body movement, motor decoding, primate neuroscience, neural-behavioral representation, behavior prior, epidural signals, motion capture

### Brain-IT-VQA: From Brain Signals to Answers
- [[brain-it-vqa-fmri-visual-question-answering]] - fMRI视觉问答突破框架，解码语言tokens并集成语言模型，创建NSD-VQA基准数据集 (arXiv: 2605.29588v1)
  - 核心要点 1: 扩展Brain-IT架构，直接从fMRI脑信号解码语言tokens，实现视觉问答
  - 核心要点 2: 创建NSD-VQA基准数据集，每张图像~20个问答对，20个控制类别，可解释评估
  - **Activation**: Brain-IT-VQA, fMRI VQA, brain signals to answers, NSD-VQA, brain decoding language

### Embodied Virtual Reality Feedback Reshapes Neural Representations for 3D Motor Imagery BCI
- [[embodied-vr-feedback-3d-motor-imagery-bci]] - VR反馈显著优于屏幕反馈(r=0.762 vs 0.672)，首个系统研究具身VR反馈重塑神经表征用于连续3D运动想象BCI (arXiv: 2605.29677v1)
  - 核心要点 1: VR反馈比屏幕反馈提升8.9-13.0%解码性能，效应量d=1.42-2.05，固定解码器无需重训练即可保持优势
  - 核心要点 2: 神经生理学发现VR增强感觉运动-顶叶去同步化、运动-额叶功能连接、前岛叶全域频段激活、顶叶耦合增强
  - **Activation**: VR feedback BCI, motor imagery, embodied feedback, 3D decoding, CNN-LSTM decoder, neurorehabilitation

### Misalignment Between Backpropagation and the Hierarchy of Brain Responses to Images
- [[backpropagation-brain-hierarchy-misalignment]] - 反向传播梯度与大脑视觉层级不匹配，使用fMRI+MEG证明时空组织偏离生物学机制 (arXiv: 2605.28693v1)
  - 核心要点 1: 梯度能预测脑信号，但其计算顺序和空间分布与大脑处理层级不符
  - 核心要点 2: 深度网络与大脑共享相似表征内容，但使用根本不同的学习机制
  - **Activation**: backpropagation brain, brain hierarchy, gradient misalignment, fMRI MEG, DINOv3

## 2026-05-30 - Economics, Investment + Quantum (Cron Job)

### Quantum Optimization Beyond QUBO for Industrial Logistics and Scheduling
- [[hubo-quantum-optimization]] - Higher-Order Unconstrained Binary Optimization (HUBO) reduces qubit requirements vs QUBO for logistics/scheduling, but increases circuit depth via higher-order terms (arXiv: 2605.30252)
  - HUBO captures complex constraints (correlated scheduling rules) impossible in standard QUBO form
  - Fundamental trade-off: fewer qubits through compact encoding vs deeper circuits from k-local interaction terms
  - Validated via bias-field digitized counterdiabatic quantum optimization on capacitated vehicle routing
  - **Activation**: HUBO, higher-order optimization, beyond QUBO, industrial logistics, scheduling, qubit-depth trade-off, CVRP

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

### Higher-Order Portfolio Optimization with QAOA
- [[quantum-portfolio-optimization]] - QAOA首次将高阶矩(偏度/峰度)纳入量子组合优化，超越传统均值-方差框架 (arXiv: 2509.01496)
  - 核心要点 1: 将偏度(3阶)和峰度(4阶)编码为QUBO高阶项，QAOA电路实现复杂风险建模
  - 核心要点 2: 包含高阶矩带来更好的风险调整后收益，多项式深度缩放
  - **Activation**: QAOA higher-order portfolio, quantum skewness kurtosis, 高阶矩组合优化

### End-to-End Portfolio Optimization with Quantum Annealing
- [[quantum-portfolio-optimization]] - 端到端量子退火组合优化流水线，混合均值-方差+Sharpe比率目标在NISQ硬件上可行 (arXiv: 2504.08843)
  - 核心要点 1: 经典预处理+QUBO编码+量子退火求解+后处理验证的完整流水线
  - 核心要点 2: 在当前NISQ设备上验证混合量子-经典方法对金融决策问题的可行性
  - **Activation**: quantum annealing portfolio, hybrid quantum classical finance, 量子退火组合优化


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
  100|  - Handles realistic budget and risk constraints with XY-mixer Hamiltonian
  100|  - **Activation**: counterdiabatic QAOA, portfolio optimization, adiabatic gauge potential, constrained quantum optimization
  100|
  100|### Constraint Preserving XY-Mixers under Trotterized Adiabatic Evolution
  100|- [[constraint-preserving-quantum-mixers]] (enhanced) - XY-mixer design methodology under Trotterized adiabatic evolution for constrained quantum optimization (arXiv: 2605.02465)
  100|  - Constraint locality analysis for XY-mixer Hamiltonian design
  100|  - Trotterized adiabatic evolution preserves feasibility throughout optimization
  100|  - **Activation**: constraint preserving mixers, XY-mixer, Trotterized evolution, constrained quantum optimization
  100|
  100|     1|
### A Penalty-Free Pipeline for Direct Quantum-Annealer Portfolio Optimization
- [[quantum-annealer-pipeline-audit]] - 量子退火组合优化审计：标准惩罚编码QUBO在当前D-Wave设备失败（链断裂率83-92%），混合服务QPU仅占0.7%运行时间 (arXiv: 2605.17628, 2605.17623)
  - 核心要点 1: 基数惩罚项产生密集秩一矩阵使逻辑图完全连接，导致Pegasus/Zephyr拓扑链断裂率极高
  - 核心要点 2: D-Wave LeapHybridCQM虽匹配Gurobi最优解，但QPU仅0.034秒/5秒预算(0.7%)，量子贡献边缘化
  - **Activation**: quantum annealer audit, penalty-free qubo, d-wave pipeline, chain-break fraction, 量子退火审计, 无惩罚qubo

### Quenching Speculation in Quantum Markets via Entangled Neural Traders
- [[quantum-market-entanglement]] - 量子市场稳定机制：交易者估值间量子纠缠消除投机崩溃中的病理纳什均衡 (arXiv: 2602.06367)
  - 核心要点 1: RL代理用量子关联量子比特编码估值稳定价格并增加净财富
  - 核心要点 2: 量化的p-guessing博弈显示纠缠消除驱动市场崩溃的病理纳什均衡
  - **Activation**: quantum market stabilization, entangled neural traders, quantum economics, market collapse, 量子市场稳定

### Quantum Reservoir Computing for Stock Movement Forecasting
- [[quantum-reservoir-finance]] - 量子储备库计算(QRC)用≤6量子比特实现股票趋势分类>86%准确率，跨超导和离子阱平台通用 (arXiv: 2602.13094)
  - 核心要点 1: 小规模量子系统作为非线性储备库提取金融时间序列特征，经典读出层训练
  - 核心要点 2: 20家量子板块上市公司2020-2025年数据验证，超导和离子阱平台表现相当
  - **Activation**: quantum reservoir computing, QRC finance, stock forecasting, 量子储备库, 股票预测

### Basis-Adaptive Sparse-State Simulation of Quantum Circuits
- [[basis-adaptive-sparse-simulation]] - 基自适应稀疏态量子电路模拟方法，通过动态旋转量子比特基保持振幅聚集，在相同内存预算下提升一个数量级的态重叠度 (arXiv: 2605.27285)
  - 核心要点 1: 固定基稀疏模拟器在纠缠增长时保真度急剧下降；BASS在每次截断前将量子比特旋转到单量子比特约化密度矩阵特征基，保持振幅聚集
  - 核心要点 2: k/PR_Z比值（稀疏预算/计算参与比）是判断自适应基是否有优势的关键指标
  - 核心要点 3: 在结构化电路（砖墙电路）上显著超越固定基方法；在无序Ising电路上提升约10倍态重叠度
  - **Activation**: basis adaptive sparse simulation, quantum circuit simulation, BASS algorithm, sparse state truncation, natural orbital, 基自适应模拟, 量子电路经典模拟

## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
  100|     2|
  100|     3|### Algorithms with Polynomially-Improved Approximation Factors for the 2→q Norm
  100|     4|- [[norm-approximation-algorithms]] - Multiplicative weight update algorithm for matrix 2→q norm approximation with polynomial improvement over spectral methods, applications to hypercontractivity and quantum separability (arXiv: 2605.25303)
  100|     5|  - MWU framework achieves O(n^{1/4-δ}) vs prior O(n^{1/4} log d)
  100|     6|  - Applications: hypercontractivity testing, quantum separability certification, small-set expansion
  100|     7|  - **Activation**: matrix norm approximation, 2-to-q norm, operator norm, hypercontractivity, multiplicative weight update, quantum separability
  100|     8|
  100|     9|### Bell's Theorem: Why Probability Factorisation Fails
  100|    10|- [[bell-probability-factorization]] - Statistical foundations of Bell's theorem showing why joint probability factorization P(A,B|a,b,λ)=P(A|a,λ)P(B|b,λ) fails in quantum systems (arXiv: 2605.29589)
  100|    11|  - Factorization assumption incompatible with quantum entanglement
  100|    12|  - CHSH inequality as statistical diagnostic for non-classical correlations
  100|    13|  - **Activation**: Bell theorem, probability factorization, quantum nonlocality, CHSH inequality, joint distributions
  100|    14|
  100|    15|### Comparing Classical Simulation and Sample-Based Learning of Quantum Systems
  100|    16|- [[quantum-ml-simulation-learning-comparison]] - Empirical framework comparing simulability vs learnability for quantum systems via Born-rule statistics (arXiv: 2605.28986)
  100|    17|  - Simulation (from classical description) and learning (from measurement samples) need not coincide
  100|    18|  - Provides complexity-theoretic and empirical methodology for quantum advantage verification
  100|    19|  - **Activation**: quantum simulation vs learning, sample-based quantum learning, simulability learnability, Born-rule statistics
  100|    20|
  100|    21|### Analytic Properties of the Jost Functions via the Poincaré-Picard Theorem
  100|    22|- [[jost-function-analytic-ode]] - ODE-theoretic analysis of Jost function analyticity for quantum scattering and complex energy plane continuation (arXiv: 2605.28859)
  100|    23|  - Applies Poincaré-Picard theorem to parameter-dependent radial Schrödinger equation
  100|    24|  - Bridges mathematical analysis (ODE theory) with quantum scattering physics
  100|    25|  - **Activation**: jost function, quantum scattering, analytic continuation, Poincaré-Picard, complex energy plane
  100|    26|
  100|    27|### HyperPrecision: High-Precision Numerical Evaluation of Multivariate Hypergeometric Functions
  100|    28|- [[hypergeometric-high-precision-evaluation]] - Mathematica package for high-precision evaluation of Horn-type hypergeometric functions via Pfaffian systems, applicable to QFT, string theory, number theory, and statistics (arXiv: 2605.30216)
  100|    29|  - Automatic Pfaffian system construction from hypergeometric function definition
  100|    30|## 2026-05-29 - Neuroscience Research (Cron Job)
  100|    31|
  100|    32|### A Deep Learning Model of Mental Rotation Informed by Interactive VR Experiments
  100|    33|- [[deep-learning-mental-rotation-vr]] - Longitudinal subcortical shape analysis with cognitive associations in aging (arXiv: 2605.29703)
  100|    34|  - Equivariant neural encoder for 3D spatial representations
  100|    35|  - Neuro-symbolic object encoder combining perception + reasoning
  100|    36|  - Interactive VR experiments for human behavioral validation
  100|    37|  - **Activation**: mental rotation, spatial cognition, VR, neuro-symbolic, equivariant networks
  100|    38|
  100|    39|### Subcortical Shape Variations and Their Associations with Cognition Across the 8th Decade of Life
  100|    40|- [[subcortical-shape-cognition-aging]] - Longitudinal analysis of subcortical morphology + cognition (arXiv: 2605.29703)
  100|    41|  - Shape-based analysis captures subtle aging patterns missed by volumetry
  100|    42|  - Lothian Birth Cohort 1936: 9-year trajectory (age 70-79)
  100|    43|  - Regional specificity: hippocampal head → memory, thalamus → processing speed
  100|    44|  - **Activation**: subcortical morphology, brain aging, cognitive decline, shape analysis
  100|    45|
  100|    46|  - One-dimensional contour restriction reduces multivariate PDE to ODE for efficient evaluation
  100|    47|  - **Activation**: hypergeometric, pfaffian, high-precision, horn-type, mathematica, multivariate, laurent expansion, quantum field theory
  100|    48|
  100|    49|### On modular forms of rational weight satisfying the canonical second-order linear modular differential equation
  100|    50|- [[modular-forms-kaneko-zagier-classification]] - Complete classification of rational weights for Kaneko-Zagier differential equation admitting modular forms solutions (arXiv: 2605.23383)
  100|    51|  - Transforms KZ equation to hypergeometric form, constructs monodromy representation matrices
  100|    52|  - Stringent commutativity constraints limit admissible weights to specific set
  100|    53|  - **Activation**: modular forms, kaneko-zagier, differential equation, monodromy, hypergeometric, rational weight, congruence subgroup
  100|    54|
  100|    55|### Iterative maps emerging from cohomological structure of primes
  100|    56|- [[prime-cohomological-iterative-maps]] - Prime gaps described by iterative maps with cohomological structure linking to statistical and quantum mechanics (arXiv: 2605.17622)
  100|    57|  - Iterative map predicts primary growth of successive primes
  100|    58|  - Residual fluctuations encode well-defined cohomological structure
  100|    59|  - **Activation**: prime numbers, cohomology, iterative maps, statistical mechanics, quantum mechanics, prime gaps
  100|    60|
  100|    61|### A Uniform Random-Lattice Tail Bound for the SVP Kissing-Profile Parameter
  100|    62|- [[svp-lattice-tail-bound]] - Dimension-uniform tail bound for SVP kissing-profile parameter with implications for quantum algorithms and post-quantum cryptography (arXiv: 2605.21966)
  100|    63|  - μ_n{γ(L) > T} ≤ C·T^{-1} for Haar-Siegel random lattices, uniformly in dimension
  100|    64|  - γ(L) = 2^{o(n)} with high probability for random lattices
  100|    65|  - **Activation**: SVP, shortest vector problem, lattice, tail bound, quantum algorithms, post-quantum cryptography
  100|    66|
  100|    67|### Hadamard product of convex functions and Jackson operator
  100|    68|- Note: Jackson operator q-theory skill already exists; no new skill needed (arXiv: 2605.18412)
  100|    69|
  100|    70|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
  100|    71|
  100|    72|### Wasserstein Least Squares: A Canonical Regression Method for Probability Distributions
  100|    73|- [[wasserstein-least-squares-regression]] - Distributional regression via optimal transport, achieving n^{-1/2} rate with exponential improvement for Wasserstein barycenters (arXiv: 2605.30266)
  100|    74|  - Canonical extension of Euclidean least squares to probability distribution space via convex analysis
  100|    75|  - Template deformation model enables n^{-1/2} estimation rate; exponential barycenter improvement
  100|    76|  - **Activation**: Wasserstein regression, distributional regression, optimal transport, probability distributions, Wasserstein barycenter, template deformation
  100|    77|
  100|    78|### Improved Sample Complexity Bound for Sample-Based Lindbladian Simulation
  100|    79|- [[lindbladian-sample-complexity]] - Sharp dichotomy between typical-case O(t²/ε²) and worst-case Ω(d⁴t²/ε²) for quantum Lindbladian simulation (arXiv: 2605.30301)
  100|    80|  - WML algorithm with trace condition determines typical vs worst case
  100|    81|  - Random Lindblad operators satisfy typical case with high probability
  100|    82|  - **Activation**: Lindbladian simulation, sample complexity, quantum channels, open quantum systems, WML algorithm, random matrix theory
  100|    83|
  100|    84|## 2026-05-29 - Neuroscience Research (Cron Job)
  100|    85|
  100|    86|### Domain-Informed Multi-Objective Framework for EEG Channel Selection in Motor Imagery BCIs
  100|    87|- [[domain-informed-moeeg-channel-selection-bci]] - Multi-objective optimization combining spatial relevance (Gaussian kernel) + functional discriminability (ERD) for compact EEG channel selection (arXiv: 2605.29943)
  100|    88|  - NSGA-II/MOPSO/MOEA/D algorithms achieve 87%, 71%, 75%, 65% on Physionet, OpenBMI, HighGamma, BCIIV-2A
  100|    89|  - 87% dimensionality reduction (64→8 channels), sensorimotor cortex prioritization
  100|    90|  - **Activation**: EEG channel selection, motor imagery BCI, multi-objective optimization, Pareto front, ERD, sensorimotor cortex
  100|    91|
  100|    92|### Learning Robust and Task-Invariant Functional Representation from fMRI through Siamese Self-Supervised Learning
  100|    93|- [[brainsimsiam-self-supervised-fmri]] - BrainSimSiam lightweight self-supervised framework for cross-task generalization without large-scale pretraining (arXiv: 2605.28990)
  100|    94|  - Positive-only contrastive learning, stop-gradient mechanism, outperforms supervised baselines
  100|    95|  - +15% ADHD accuracy, -8% age regression MSE, comparable to foundation models with 90% less compute
  100|    96|  - **Activation**: self-supervised fMRI, Siamese learning, BrainSimSiam, positive-only contrastive, cross-task generalization
  100|    97|
  100|    98|## 2026-05-29 - Neuroscience Research (Cron Job)
  100|    99|
  100|   100|### LLM ICL Representational Geometry Reorganization
  100|   101|- [[llm-icl-representational-geometry-reorganization]] - ICL models reorganize representations dynamically via prototype comparison (arXiv: 2605.28854)
  100|   102|  - RDM correlation increases during untangling tasks
  100|   103|  - Eigenvalue spectrum separates task information
  100|   104|  - **Activation**: ICL, representational geometry, prototypes, untangling, RDM correlation, online learning
  100|   105|
  100|   106|### Brain-IT-VQA: From Brain Signals to Answers
  100|   107|- [[brain-it-vqa-fmri-visual-question-answering]] - Brain-IT-VQA framework for VQA from fMRI, decodes language tokens from brain activity (arXiv: 2605.29588)
  100|   108|  - Token-level decoding outperforms pixel reconstruction
  100|   109|  - NSD-VQA benchmark with 20 controlled question categories
  100|   110|  - **Activation**: Brain-IT, VQA, fMRI decoding, brain question answering, NSD-VQA
  100|   111|
  100|   112|
  100|   113|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
  100|   114|
  100|   115|### Paper 2605.29052
  100|   116|- [[quantum-nonautonomous-ode-simulation]] - 量子算法模拟非自治ODE非幺正动力学，通过SVD分解将传播子写为酉算子之和 (arXiv: 2605.29052)
  100|   117|  - quantum ODE
  100|   118|  - nonunitary dynamics
  100|   119|  - SVD dilation
  100|   120|  - quantum simulation
  100|   121|  - **Activation**: quantum ODE, nonunitary dynamics, SVD dilation, quantum simulation
  100|   122|
  100|   123|### Paper 2605.28892
  100|   124|- [[funessian-process-non-markovian]] - Funessian过程：正可分非马尔可夫过程，初始状态记忆贯穿演化，互信息表征非马尔可夫性 (arXiv: 2605.28892)
  100|   125|  - non-Markovian
  100|   126|  - memory effect
  100|   127|  - Chapman-Kolmogorov
  100|   128|  - ergodicity breaking
  100|   129|  - **Activation**: non-Markovian, memory effect, Chapman-Kolmogorov, ergodicity breaking
  100|   130|
  100|   131|### Paper 2605.29130
  100|   132|- [[mersenne-numbers-doubling-map]] - 梅森数与倍角映射动力学联系，无需显式计算即可求因子的替代Lucas-Lehmer方法 (arXiv: 2605.29130)
  100|   133|  - Mersenne numbers
  100|   134|  - doubling map
  100|   135|  - prime testing
  100|   136|  - dynamical systems
  100|   137|  - **Activation**: Mersenne numbers, doubling map, prime testing, dynamical systems
  100|   138|
  100|   139|### Paper 2605.28906
  100|   140|- [[quantum-classical-uncertainty-electromagnetism]] - 经典与量子电磁理论统一不确定关系ΔrΔk≥5/2，适用于光束和单光子 (arXiv: 2605.28906)
  100|   141|  - uncertainty relations
  100|   142|  - electromagnetism
  100|   143|  - classical-quantum correspondence
  100|   144|  - **Activation**: uncertainty relations, electromagnetism, classical-quantum correspondence
  100|   145|
  100|   146|### Paper 2605.28974
  100|   147|- [[quantum-ml-statistics-invariant-theory]] - 基于quiver不变量理论的iPCA模型MLE存在性检验算法，连接统计学与不变量理论 (arXiv: 2605.28974)
  100|   148|  - MLE existence
  100|   149|  - invariant theory
  100|   150|  - quiver representation
  100|   151|  - iPCA
  100|   152|  - **Activation**: MLE existence, invariant theory, quiver representation, iPCA
  100|   153|
  100|   154|### Paper 2605.28931
  100|   155|- [[quantum-ml-ground-state-measurement]] - SIC-POVM测量空间量子基态变分学习，自回归GRU编码概率分布+物理性约束 (arXiv: 2605.28931)
  100|   156|  - quantum ground state
  100|   157|  - SIC-POVM
  100|   158|  - variational learning
  100|   159|  - autoregressive neural network
  100|   160|  - **Activation**: quantum ground state, SIC-POVM, variational learning, autoregressive neural network
  100|   161|
  100|   162|## 2026-05-29 - Neuroscience Research (Cron Job)
  100|   163|
  100|   164|### Graph Neural Network Reveals the Cortical Morphology of Local Brain Aging in Normal Cognition and Alzheimer's Disease
  100|   165|- [[gnn-cortical-morphology-brain-aging]] - GNN-based local brain age estimation from cortical morphology (arXiv: 2601.10912)
  100|   166|  - High-resolution (1.37mm) vertex-level aging pattern analysis
  100|   167|  - Identifies association cortices aging in CN, widespread MCI patterns, comprehensive AD cortical aging
  100|   168|  - Links regional LBA gaps to neuropsychological measures
  100|   169|  - **Activation**: brain age, cortical morphology, GNN, Alzheimer, cognitive impairment, aging patterns
  100|   170|
  100|   171|     1|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics (Cron Job)
  100|   172|     2|
  100|   173|     3|### End-to-End Formalization of Quantum Error Correction
  100|   174|     4|- [[qec-formal-verification]] - 量子纠错码端到端形式化验证方法论，SAT验证约简+机器检查距离证明 (arXiv: 2605.16523)
  100|   175|     5|  - 稳定子码理论完整形式化（线性代数、Pauli群、二元辛表示）
  100|   176|     6|  - 距离认证问题通过验证SAT约简机器检查
  100|   177|     7|  - BitVec编码将变量数从O(n)降至O(√n)
  100|   178|     8|  - **Activation**: quantum error correction formal verification, stabilizer code distance proof, machine-checked quantum verification, qLDPC certification, QECC end-to-end formalization
  100|   179|     9|
  100|   180|
  100|   181|    10|### Best-First Ordered Statistics Decoding of Quantum LDPC Codes
  100|   182|    12|- [[bf-osd-qldpc-decoding]] - BF-OSD遍历错误候选空间按似然降序，1/100查询预算达到BP+OSD同等性能 (arXiv: 2605.25777)
  100|   183|    13|  - Best-First OSD替代暴力枚举，优先级队列按似然排序
  100|   184|    14|  - 固定BP迭代次数后调用OSD，而非等待收敛
  100|   185|    15|  - 全电路级噪声下特别有效，BP不可靠时优势明显
  100|   186|    16|  - **Activation**: quantum error correction, QLDPC decoding, BF-OSD, belief propagation, ordered statistics decoding
  100|   187|    17|
  100|   188|    18|### Quantum Mechanics: Problems and Paradoxes
  100|   189|    19|- [[quantum-foundations-probability]] - 量子力学基础公理体系：概率起源、Planck常数本质、波函数本体论、测量问题 (arXiv: 2605.30067)
  100|   190|    20|  - 量子理论公理体系形式化
  100|   191|    21|  - 经典振荡器+热浴→量子行为对应模型
  100|   192|    22|  - 概率振幅本质与Born规则推导
  100|   193|    23|  - **Activation**: quantum foundations, quantum probability, measurement problem, wave function ontology, axiom system
  100|   194|    24|
  100|   195|    25|### Entropy-Governed Speedup for Quantum Algorithms on Local Hamiltonians
  100|   196|    26|- [[entropy-governed-quantum-speedup]] (enhanced) - 利用熵结构超越Grover界的量子算法，在深度-d状态上实现更低能量估计 (arXiv: 2605.18241)
  100|   197|    27|  - 输出态能量不超过深度-d态的最小能量
  100|   198|    28|  - 区分强纠缠态与经典可描述态
  100|   199|    29|  - **Activation**: quantum algorithm speedup, local Hamiltonian, entropy-governed, Grover bound
  100|   200|    30|
  100|   201|
  100|   202|### Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization
  100|   203|- [[quantum-finance-stack]] (enhanced) - Audit reveals D-Wave hybrid QPU contributes only 0.7% of wall-clock time; 99% classical decomposition, identical solutions across all budgets showing determinism (arXiv: 2605.17623)
  100|   204|  - QPU mean access time 0.034s out of 5s budget on 54 instances (N=10-640)
  100|   205|  - Cardinality penalty creates dense rank-one term collapsing density benchmark axis
  100|   206|  - Constraint-native interface = classical pipeline + tiny QPU contribution, not quantum sampling win
  100|   207|  - **Activation**: dwave hybrid audit, quantum portfolio benchmark, QPU time analysis, constraint-native, classical decomposition, 量子组合优化审计
  100|   208|
  100|   209|### Quantum Portfolio Optimization: An Extensive Benchmark
  100|   210|- [[quantum-finance-stack]] (enhanced) - 250-instance benchmark (up to 1000 assets): MIP solves all in seconds, classical heuristics outperform QA/QAOA (arXiv: 2509.17876)
  100|   211|  - Only very limited room for quantum advantage in portfolio optimization
  100|   212|  - Problem-tailored heuristic consistently outperforms quantum approaches for fixed runtime
  100|   213|  - **Activation**: quantum portfolio benchmark, MIP vs quantum annealing, QAOA comparison, 量子组合优化基准
### Quantum-Inspired Qutrit Neural Networks for Financial Forecasting
- [[quantum-qutrit-neural-financial-forecasting]] - 量子三态(Qutrit)神经网络用于实时金融预测，比ANN和Qubit网络训练更快、表现更好 (arXiv: 2605.29413)
  - 核心要点 1: Qutrit使用3态量子叠加态(|0⟩熊/|1⟩中性/|2⟩牛)，每神经元信息容量log₂(3)≈1.58比特
  - 核心要点 2: 3×3酉矩阵门提供比2×2更丰富的特征混合能力，特别适合三分类预测目标
  - **Activation**: qutrit neural network, QQTN, quantum financial forecasting, 3-state quantum ML, stock prediction
