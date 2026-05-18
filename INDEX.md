## 2026-05-18 - Neuroscience Research (Cron Job - Early Morning)
### REALM: Retrospective Encoder Alignment for LFP Modeling
- [[realm-lfp-retrospective-decoding]] - Causal LFP decoding via retrospective distillation from bidirectional Mamba-2 teacher, enabling spike-free BCI with reduced power/bandwidth (arXiv: 2605.14867)
  - Bidirectional Mamba-2 pretrained with masked autoencoding distilled to compact causal student
  - Outperforms causal AND non-causal LFP-based SOTA for behavior decoding
  - Significant parameter count and training time reduction
  - **Activation**: REALM, LFP decoding, retrospective distillation, causal neural decoding, Mamba neural model, wireless BCI

### Complex Brain Hypothesis
- [[complex-brain-hypothesis]] - Resolves entropy-content conundrum in consciousness: brain complexity (not entropy) indexes phenomenal richness, modulated by inference grain (arXiv: 2605.16146)
  - Fine-grained regime (HCPEs): loosened constraints amplify fluctuations → rich content, high complexity
  - Coarse-grained regime (MPEs): simpler model dissolves variety → contentless awareness, low complexity
  - Both show elevated entropy but differ in complexity and perturbational signatures
  - **Activation**: complex brain hypothesis, entropy-content conundrum, minimal phenomenal experience, consciousness complexity, free energy consciousness


### Code-Modulated Motion Visual Evoked Potential for BCI
- [[code-modulated-motion-vep-bci]] - Novel BCI paradigm using pseudo-random motion sequences instead of flickering for visual stimulation, achieving 85.67% accuracy in 4-class online BCI (arXiv: 2605.15801)
  - c-MVEP uses motion modulation with pseudo-random codes instead of luminance flicker
  - Comparable SNR to c-VEP but lower accuracy (85.67% vs 97.81%) and slower (2.61s vs 1.15s)
  - Provides flicker-free alternative for users sensitive to visual flicker (photosensitive epilepsy)
  - **Activation**: c-MVEP, motion VEP, code-modulated VEP, flicker-free BCI, visual evoked potential

### Clockless Asynchronous Neuromorphic Computing
- [[clockless-asynchronous-neuromorphic-computing]] - Clockless asynchronous neuromorphic computing on FPGAs using Boolean spiking neurons with autonomous time-continuous dynamics (arXiv: 2605.16114)
  - Boolean spiking neurons evolve continuously without global clock, eliminating clock tree power
  - Reconfigurable chip enables dynamic topology changes via FPGA interconnect reprogramming
  - Excitatory/inhibitory weights implemented as configurable delays and gates
  - **Activation**: clockless neuromorphic, asynchronous spiking, FPGA neuromorphic, Boolean spiking neuron

### VaCoAl: Algebro-Deterministic Hippocampal Memory
- [[vacoal-algebro-deterministic-memory]] - Algebro-deterministic hippocampal memory architecture using Galois-field LFSRs as substrate for vector hashing and TEM (arXiv: 2605.15652)
  - Galois-field LFSR provides deterministic alternative to random scaffold-to-hippocampus projections
  - Algebraically tractable model of multi-hop replay-fidelity decay
  - STDP-like path selection mechanism for memory consolidation
  - **Activation**: vacoal, algebro-deterministic memory, hippocampal memory, Galois-field LFSR, vector-hash

## 2026-05-18 - Neuroscience Research (Cron Job)

### Structure Abstraction and Generalization in a Hippocampal-Entorhinal Inspired World Model
- [[hippocampal-entorhinal-world-model]] - Brain-inspired hierarchical world model using HPC-MEC circuit for structure abstraction and generalization via velocity-driven path integration (arXiv: 2605.15733)
  - Inverse model for structural extraction from high-dimensional dynamics
  - HPC-MEC coupling dissociating relational structures (MEC) from episodic scenes (HPC)
  - **Activation**: hippocampal-entorhinal, world model, structure abstraction, path integration, grid cells, self-supervised learning

## 2026-05-18 - Neuroscience Research (Cron Job - Late Night)

### SpikeProphecy: A Large-Scale Benchmark for Autoregressive Neural Population Forecasting
- [[spikeprophecy-benchmark]] - 提出四维评估框架替代单一Pearson r，涵盖因果结构、潜变量恢复、预测精度、行为解码，覆盖小鼠/大鼠/猕猴多物种数据集 (arXiv: 2605.12992)
  - 批判当前仅用aggregate Pearson r评估神经群体模型的不足
  - 四维评估：因果结构(DAG相似度)、潜变量恢复(Procrustes/CCA)、多分辨率预测精度、行为解码R²
  - 四数据集跨物种验证：小鼠Neuropixels、大鼠多电极、猕猴多电极
  - **Activation**: spike prophecy, neural forecasting benchmark, spike forecaster evaluation, neural population benchmark
### Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale
- [[spike-forecast-behavioral-decoding]] - 单个Mamba forecaster仅在spike counts上自监督训练，隐层状态自然涌现行为表征，线性探针即达到专用decoder精度 (arXiv: 2605.12999)
  - 统一forecaster+decoder为单一模型，closed-loop BCI延迟和算力大幅降低
  - 自监督：无需行为标签，next-step spike prediction自然捕获task-relevant latent structure
  - per-session线性探针即可解码行为变量，精度媲美supervised decoder
  - **Activation**: spike forecast, behavioral decoding, Mamba neural, implicit neural representation, closed-loop BCI

## 2026-05-18 - Neuroscience + Quantum Mechanics (Cron Job - Hourly)

### Quantum Hyperdimensional Computing: A Foundational Paradigm for Quantum Neuromorphic Architectures
- [[quantum-hyperdimensional-computing]] - 将脑启发的高维计算(HDC)映射到量子操作：超向量→量子态、捆绑→LCU/OAA、绑定→相位预言、排列→QFT、相似度→Hadamard Test，在156-qubit IBM Heron r3验证 (arXiv: 2511.12664)
  - HDC五大核心操作映射到量子门：捆绑用LCU+OAA、绑定用相位预言、排列用QFT、相似度用Hadamard Test
  - 量子复杂度优势：捆绑O(log D)、绑定O(1)、相似度O(log D)，远超经典O(D)
  - log D量子比特存储D维向量，天然噪声鲁棒性
  - **Activation**: quantum hyperdimensional, QHDC, hyperdimensional quantum, quantum neuromorphic, HDC quantum mapping

### Quantum-EEGNet: Hybrid Quantum-Classical EEG Encoding
- [[quantum-eeg-encoding]] - QEEGNet将EEGNet卷积架构与量子变分层结合，探索跨任务/跨数据集的脑电编码泛化能力 (arXiv: 2503.00080)
  - EEGNet提取时空特征 → 量子变分层编码 → 分类输出
  - 跨认知和运动任务数据集评估，混合架构需进一步优化以充分发挥量子优势
  - 量子层以更少参数实现相当性能，但量子电路训练增加复杂度
  - **Activation**: QEEGNet, quantum EEG, quantum brain signal, quantum biomedical, hybrid quantum-classical neural network

### Quantum Neuroscience Patterns
- [[quantum-neuroscience-patterns]] - 量子计算与神经科学研究交叉模式汇总：QHDC、量子生成神经元模型、QEEGNet、Leggett-Garg神经动力学测试 (arXiv: 2511.12664, 2409.09125, 2503.00080, 2605.12126)
  - 量子超维计算：HDC操作映射到量子门原语
  - 量子生成模型：以更少参数捕获生物神经元时空相关性
  - Leggett-Garg测试：探测单神经元非扩散随机结构
  - **Activation**: quantum neuroscience, quantum brain, quantum neural networks, Leggett-Garg neural

## 2026-05-18 - Neuroscience Research (Cron Job)

### Mechanistic Interpretability of EEG Foundation Models via Sparse Autoencoders
- [[eeg-foundation-sae-interpretability]] - 使用TopK稀疏自编码器提取EEG基础模型的稀疏特征字典，通过临床概念探针量化单体语义性和纠缠度，实现概念操控和频率映射 (arXiv: 2605.13930v2)
  - SAE从EEG transformer embeddings提取稀疏字典，跨SleepFM/REVE/LaBraM架构鲁棒迁移
  - 概念操控揭示三种状态：可选择性操控、编码但纠缠、未编码
  - 频谱解码器将潜在操控映射回生理频率特征（慢波抑制、α波段恢复）
  - 年龄-病理纠缠：无法在不破坏另一概念的情况下抑制一个概念
  - **"Wrecking-ball"效应**：大操控幅度导致全局性能崩溃
  - **Activation**: EEG可解释性, 稀疏自编码器, EEG基础模型, 概念操控, 频谱解码

### On the Stability of Growth in Structural Plasticity
- [[structural-plasticity-growth-stability]] - 揭示神经网络生长操作并非剪枝的逆操作，发现"前向激活-后向饥饿"现象及新生单元集成稳定性问题 (arXiv: 2605.15435)
  - 新生单元前向参与计算但接收比既有单元弱得多的梯度信号
  - 在CNN等复杂架构中问题尤为显著，小MLP中不明显
  - 生长策略在最终精度上可达高位，但轨迹平均性能和重训后子网络均不如剪枝
  - 持续学习中生长策略的竞争力取决于新生单元是否有足够集成时间
  - **Activation**: 结构可塑性, 动态生长, 新生单元集成, 梯度饥饿, 持续学习

## 2026-05-18 - Neuroscience + Quantum Mechanics (Cron Job - Afternoon)

### Diagonal Adaptive Non-local Observables on Quantum Neural Networks
- [[diagonal-anos-qnn]] - 对角自适应非局域可观测量，将VQA可观测量复杂度从O(4^k)降至O(2^k)，同时保持完整表达能力 (arXiv: 2605.15410)
  - 对角矩阵是AN0空间的模酉相似典型代表，优化对角可观测量等价于优化全Hermitian空间
  - 测量端经典计算复杂度指数级降低，适用于VQE/QAOA等变分量子算法
  - **Activation**: diagonal ANO, adaptive non-local observable, quantum observable optimization, VQA measurement reduction, QNN observable design

### Quantum Neuromorphic Computing Patterns
- [[quantum-neuromorphic-patterns]] - 量子与神经形态计算交叉模式：量子脑模型、量子储层计算用于神经动力学、SPATE脉冲-相位编码 (arXiv: multiple)
  - 四种核心模式：脑启发的量子神经架构、量子储层计算处理神经信号、SPATE脉冲-相位量子编码、量子认知建模
  - 结合量子纠缠建模神经同步、使用变分量子电路实现类Hebbian学习
  - **Activation**: quantum neuromorphic, quantum brain, brain-inspired quantum, quantum reservoir computing neural, spiking quantum

## 2026-05-18 - Neuroscience Research (Cron Job - Late)

### The Complex Brain Hypothesis: Resolving the Entropy-Content Conundrum in Minimal Phenomenal Experience
- [[complex-brain-hypothesis]] - 提出复杂度假说解决熵-内容悖论：细粒度(HCPEs)与粗粒度(MPEs)意识状态区分 (arXiv: 2605.16146)
  - 复杂脑假说(CBH)修正熵脑假说(EBH)，用复杂度而非熵指数现象丰富度
  - 两机制：细粒度(致幻剂-内容增殖)与粗粒度(冥想/5-MeO-DMT-内容消解)，均可升熵但现象学相反
  - 预测扰动签名(PCI)差异，MPEs为意识计算理论的关键测试案例
  - **Activation**: complex brain hypothesis, entropic brain, minimal phenomenal experience, consciousness entropy, Friston consciousness, 5-MeO-DMT, meditation consciousness

## 2026-05-18 - Neuroscience Research (Cron Job)

### NeuroTrain: Surveying Local Learning Rules for Spiking Neural Networks with an Open Benchmarking Framework
- [[neurotrain-local-learning-snn-benchmarking]] - SNN训练算法全面分类与开源基准测试框架 (arXiv: 2605.15058)
  - 覆盖6类SNN训练方法：代理梯度BP、局部学习规则、三因子学习、生物可塑性、ANN-SNN转换、非标准优化
  - 基于snnTorch的统一模块化基准测试框架，支持多维度评估（准确率/效率/生物合理性/硬件适配性）
  - **Activation**: NeuroTrain, SNN benchmarking, local learning rules, surrogate gradient, three-factor learning

### Dual-axis attribution of zebrafish tectal microcircuits for energy-efficient and robust neurocomputing
- [[dual-axis-zebrafish-circuits]] - 斑马鱼被盖微电路双轴归因：能效信息处理与鲁棒稳定性的功能分离 (arXiv: 2605.13924)
  - 生物神经回路子结构沿两计算轴分工：能效信息处理 vs 鲁棒性保持稳定
  - 构建斑马鱼视网膜被盖有向图，量化验证功能特异性分离
  - **Activation**: zebrafish tectal, dual-axis attribution, retinotectal, energy-efficient neurocomputing


## 2026-05-18 - Neuroscience + Quantum Mechanics (Cron Job - Evening)

### Exploring Biological Neuronal Correlations with Quantum Generative Models
- [[quantum-biological-neural-correlations]] - 量子生成模型捕获生物神经元活动的时空相关性，比经典方法参数更少 (arXiv: 2409.09125)
  - 量子生成框架生成具有时空相关性的合成神经元数据
  - 比经典方法所需可训练参数更少
  - **Activation**: quantum generative neural, biological neuronal correlation, quantum neuroscience, synthetic neural data

### Global Mean-Amplitude Enhanced Spiking Neural Network Coherent Ising Machine
- [[global-mean-amplitude-snn-cim]] - 全局平均振幅反馈增强SNN相干Ising机，Max-Cut成功率提升27% (arXiv: 2509.13917)
  - 物理驱动的振幅稳定化防止振荡发散
  - Max-Cut问题成功率比传统SNN-CIM提升27%
  - 在交通分配问题上验证了通用性
  - **Activation**: coherent ising machine, GFSNN-CIM, mean-amplitude feedback, spiking neural optimizer, Max-Cut SNN

### Solving Classical and Quantum Spin Glasses with Deep Boltzmann Quantum States
- [[quantum-spin-glass-boltzmann]] - 深度玻尔兹曼量子态结合神经量子态与玻尔兹曼机架构高效表示受阻挫量子系统 (arXiv: 2605.15899)
  - 结合神经量子态与玻尔兹曼机架构
  - 高效处理由无序和能量受挫产生的指数级局部能量极小值
  - 同时适用于经典和量子自旋玻璃问题
  - **Activation**: deep boltzmann quantum, spin glass neural, frustrated quantum system, neural quantum state

## 2026-05-18 - Neuroscience Research (Cron Job)

### Bridging Silicon and the Hippocampus: Algebro-Deterministic Memory "VaCoAl" as a Substrate for Vector-HaSH and TEM
- [[vacoul-hdc-sram-cam-ai]] - 海马体记忆机制与超维计算的代数桥梁，将DG模式分离和CA3模式完成映射到CAM硬件 (arXiv: 2605.15652)
  - VaCoAl 为 Vector-HaSH 和 TEM 提供代数对象，用伽罗瓦域 LFSR 替代随机投影
  - 路径积分置信比率首次为多跳回放保真度衰减提供代数可溯模型
  - **Activation**: hippocampus, hyperdimensional computing, CAM, Vector-HaSH, TEM, memory consolidation, dentate gyrus

### Scalable neuromorphic computing from autonomous spiking dynamics in a clockless reconfigurable chip
- [[clockless-asynchronous-neuromorphic-computing]] - 基于无时钟异步FPGA的脉冲神经架构，实现超低功耗神经形态计算 (arXiv: 2605.16114)
  - 布尔脉冲神经元在无时钟数字电路中自主演化，无需专用神经形态芯片
  - 在商用FPGA上实现，功耗显著低于传统数字实现
  - **Activation**: clockless, asynchronous, neuromorphic, FPGA, spiking neuron, energy-efficient

## 2026-05-18 - Neuroscience + Quantum Mechanics (Cron Job)

### Elastic Spiking Transformers for Efficient Gesture Understanding
- [[elastic-spiking-transformer-matryoshka]] - Matryoshka-style elastic Spiking Transformer with runtime-adaptive width/attention head slicing for deployment across hardware budgets without retraining (arXiv: 2605.13869)
  - Single universal model dynamically slices network width and attention heads at inference time
  - Reducing active neurons also lowers spike firing rates, yielding proportional reductions in synaptic operations
  - Evaluated on CIFAR10/100, CIFAR10-DVS, and EHWGesture clinical gesture understanding dataset
  - **Activation**: elastic spiking transformer, Matryoshka spiking network, runtime-adaptive SNN, dynamic width spiking, gesture understanding SNN

### Evaluating Container Orchestration for Neuromorphic Workloads in Virtual Edge Environments
- Paper on deploying SNN workloads with Kubernetes in edge environments (arXiv: 2605.15866)
  - SNN workloads highly sensitive to resource availability (0.5 CPU cores → 47.6x latency increase)
  - K3d default round-robin routing introduces significant tail latency under replica scaling
  - Provides baseline for deploying neuromorphic workloads in containerized edge environments
  - **Activation**: neuromorphic kubernetes, SNN edge deployment, container orchestration SNN

### Control-Plane Openness in Near-Term Quantum Computing
- Survey of 13 commercial quantum vendors across 4 modalities on control-plane openness (arXiv: 2605.15233)
  - IBM removed pulse-level control from production QPUs in Feb 2025
  - Mid-tier superconducting vendors and neutral-atom platforms moving toward more openness
  - Documents what the field has lost as access landscape has shifted
  - **Activation**: quantum control plane, quantum vendor survey, pulse-level access

## 2026-05-18 - Neuroscience Research (Cron Job)

### Scalable Learning in Structured Recurrent Spiking Neural Networks without Backpropagation
- [[structured-recurrent-snn-backprop-free]] - Structured recurrent SNN architecture using local plasticity, WTA teaching signals, and three-factor learning for backprop-free scalable training (arXiv: 2605.00402)
  - Core: Structured multi-layer recurrent SNN with locally dense layers and sparse small-world long-range projections
  - Learning: Three-factor rule with WTA teaching, random broadcast alignment, and modulatory gating via eligibility traces
  - **Activation**: structured recurrent SNN, backprop-free learning, three-factor learning, WTA teaching, eligibility traces, neuromodulatory

### UniBCI: Towards a Unified Pretrained Model for Invasive Brain-Computer Interfaces
- [[unibci-invasive-foundation-model]] - Unified foundation model for invasive BCI using context-conditioned tokenization and hierarchical Interval-Area Attention across species and brain regions (arXiv: 2605.00061)
  - Core: Context-Conditioned Spatio-Temporal (CST) tokenization embedding neural signals with metadata into shared space
  - Architecture: Hierarchical IAA combining linear attention (interval-level) and sliding-window attention (area-level)
  - Pretraining: Self-supervised masked signal reconstruction on multi-species, multi-subject, multi-paradigm corpus
  - **Activation**: UniBCI, invasive BCI, neural foundation model, CST tokenization, Interval-Area Attention, IAA, masked reconstruction

## 2026-05-18 - Neuroscience + Quantum Mechanics (Cron Job)

### Consciousness as Uncommon Self-Knowledge: A Synergistic Information Framework
- [[uncommon-self-knowledge-consciousness]] - 将意识定义为系统对自身携带的协同信息，基于PID分解 (arXiv: 2605.13884)
  - USK = 自指向协同信息，只存在于子系统联合观测中
  - 区分意识与元认知，解决IIT/GWT/HOT反例
  - **Activation**: consciousness, USK, synergistic information, PID, metacognition

### QSeqSim: A Symbolic Simulator for Qiskit While Loops Using Sequential Quantum Circuits
- [[qseqsim-quantum-while-loops]] - Qiskit量子while循环符号模拟器，填补迭代量子程序仿真空白 (arXiv: 2605.14881)
  - 将量子while循环转换为有界顺序电路
  - 符号化状态表示，高效处理测量分支
  - **Activation**: QSeqSim, quantum while loops, sequential circuits, Qiskit
## 2026-05-18 - QPINN with Trainable Embeddings (Cron Job)

### A QPINN Framework with Quantum Trainable Embeddings for the Lid-Driven Cavity Problem
- [[qpinn-trainable-embeddings]] - QPINN framework using QNN-based trainable embeddings for PDE solving (arXiv: 2605.13892)
  - Core: QNN learns data-adaptive quantum feature maps instead of classical fixed encoding
  - Results: Stable training, competitive accuracy, significantly fewer parameters than classical PINNs
  - **Activation**: QPINN, quantum PINN, quantum trainable embeddings, quantum PDE solver

## 2026-05-18 - Neuroscience + Quantum Mechanics (Cron Job)

### Leggett–Garg Tests in Neural Dynamics: Probing Non-Diffusive Stochastic Structure in Single Neurons
- [[leggett-garg-neural-dynamics]] - LGI testing methodology to distinguish diffusive vs persistent stochastic models in neural dynamics (arXiv: 2605.12126)
  - LGI as temporal analogue of Bell constraints for neural dynamics
  - Persistent stochastic (Kac-type) models can violate LGI; diffusive models always satisfy it
  - Conservative interpretation: violation indicates non-Markovian memory, not quantum coherence
  - **Activation**: leggett-garg neural, temporal correlations neuron, non-diffusive neural dynamics, quantum-like neural testing

### Solving Classical and Quantum Spin Glasses with Deep Boltzmann Quantum States
- [[deep-boltzmann-quantum-states]] - Combines Deep Boltzmann Machine architectures with neural quantum states to solve frustrated quantum spin glass problems (arXiv: 2605.15899)
  - DBM as variational ansatz for quantum wavefunctions with complex-valued amplitudes
  - Handles sign problem through complex-valued network parameters
  - Variational Monte Carlo with stochastic reconfiguration for natural gradient descent
  - **Activation**: deep boltzmann quantum states, quantum spin glass, neural quantum states, variational quantum, frustrated systems

### Thermodynamic Networks: Harnessing Non-Equilibrium Steady States for Computation
- [[thermodynamic-networks]] - Framework for autonomous physics-based computation using non-equilibrium steady states in thermodynamic networks (arXiv: 2605.15985)
  - Computation through thermodynamic relaxation processes between finite reservoirs
  - Autonomous, clockless, energy-efficient computation paradigm
  - Connects thermodynamics with information processing
  - **Activation**: thermodynamic networks, non-equilibrium computation, autonomous computing, physical computation

### Born-rule statistical dynamical quantum phase transitions under measurement
- [[born-rule-quantum-phase-transitions]] - Studies dynamical quantum phase transitions (DQPTs) through Born-rule measurement statistics analyzing nonanalytic changes in return probability (arXiv: 2605.16029)
  - DQPTs occur at critical times where Loschmidt echo rate function is nonanalytic
  - Connects quantum measurement theory with dynamical critical phenomena
  - Statistical ensemble of measurements reveals DQPT signatures
  - **Activation**: dynamical quantum phase transition, born rule, loschmidt echo, fidelity dynamics, quantum measurement

### SpikeProphecy: A Large-Scale Benchmark for Autoregressive Neural Population Forecasting
- [[spikeprophecy-benchmark]] - First large-scale benchmark for spike-count forecasting with population metric decomposition (arXiv: 2605.12992)
  - Decomposes aggregate Pearson r into temporal fidelity, spatial pattern accuracy, magnitude-invariant alignment
  - 105 Neuropixels sessions, 89,800 neurons, 7 architecture baselines
  - Reveals brain-region predictability hierarchy + sub-Poisson evaluation floor
  - **Activation**: spike forecasting benchmark, neural population forecasting, population metric decomposition, Neuropixels benchmark

### Neural Fields for NV-Center Inverse Sensing (NeTMY)
- [[netmy-neural-field-nv-sensing]] - Coordinate neural field for NV-center quantum sensor inverse problems with physics-faithful reconstruction (arXiv: 2605.13988)
  - Tensor power-summed dipolar operator exposes center-collapse failure in free-density optimization
  - NeTMY uses annealed positional encoding + multiscale optimization + sparsity gating
  - Parameterization smooths gradient updates, mitigating center-collapse pathology
  - **Activation**: NV center sensing, neural field inverse problem, quantum sensor reconstruction, NeTMY

## 2026-05-18 - Anthropic Research (Cron Job)

### Teaching Claude why (Updated)
- [[teaching-claude-why]] - Alignment training methodology: teaching principles beats teaching demonstrations; difficult advice dataset achieves 28x token efficiency
  - Four lessons: direct training doesn't generalize, principled OOD training works, teaching "why" beats "what", data quality/diversity crucial
  - NEW: Alignment improvements persist through RL fine-tuning; diverse training environments significantly improve generalization
  - Difficult advice dataset: put user in dilemma, train AI to give aligned advice — 28x fewer tokens, better OOD generalization
  - **Activation**: agentic misalignment, alignment training, OOD generalization, constitutional AI, honeypot resistance, difficult advice, RL persistence

## 2026-05-18 - Neuroscience Research (Cron Job)

### NeuroGAN-3D: Enhancing Intrinsic Functional Brain Networks via High-Fidelity 3D Generative Super-Resolution
- [[neurogan-3d]] - 3D GAN for super-resolution of rs-fMRI spatial maps, enabling precise functional unit localization (arXiv: 2605.08373)
  - First 3D GAN specifically designed for rs-fMRI spatial map enhancement
  - Significantly outperforms conventional interpolation baselines
  - Preserves biologically meaningful connectivity patterns at higher resolution
  - **Activation**: NeuroGAN, fMRI super-resolution, 3D generative neuroimaging, volumetric brain maps, rs-fMRI enhancement

### Prior Elicitation for Bayesian Estimation of Single-Subject Connectivity Networks
- [[prior-elicitation-connectivity]] - Bayesian priors on correlation matrices with expert-informed hyperparameters for single-subject FC inference (arXiv: 2605.02587)
  - Novel Bayesian priors on correlation matrices with interpretable hyperparameters
  - Distributional (not point) connectivity weights with uncertainty quantification
  - Significance testing via posterior credible sets — only 2nd Bayesian FC model for single-subject
  - **Activation**: Bayesian functional connectivity, prior elicitation, single-subject FC, distributional connectivity weights, credible sets brain network

### KAP-CPD: Kernel Aggregation for Change-Point Detection in Dynamic Networks
- [[kap-cpd]] - Multi-kernel aggregation for change-point detection in dynamic brain networks, with fast analytic variant (arXiv: 2605.14463)
  - Kernel-agnostic: aggregates multiple kernels to adapt to diverse change patterns
  - Distribution-free: no assumptions about network distribution
  - KAPf-CPD analytic variant for scalable long-sequence processing
  - **Activation**: KAP-CPD, change-point detection, dynamic brain networks, kernel aggregation, time-varying functional connectivity

## 2026-05-12 - Systems Engineering Research (Cron Job)

### HySecTwin: A Knowledge-Driven Digital Twin Framework Augmented with Hybrid Reasoning for Cyber-Physical Systems
- [[hysectwin-digital-twin-cps]] - Semantic modelling + hybrid (deterministic + fuzzy) reasoning for CPS threat det (arXiv: 2605.11682)
  - Semantic modelling + hybrid (deterministic + fuzzy) reasoning for CPS threat detection
  - 21.5% faster detection with sub-ms sync, MITRE ATT&CK-aligned explainable alerts
  - **Activation**: digital twin, CPS security, semantic reasoning, threat detection, knowledge graph

## 2026-05-14 - Systems Engineering Research (Cron Job)

### Refactoring-as-Propositions: Proved Refactoring of Hybrid Systems via Proved Refinements
- [[refactoring-as-propositions]] - Use dRL to prove α ⊑ β (refinement), then transfer existing safety proofs [α]φ → (arXiv: 2605.15001)
  - Use dRL to prove α ⊑ β (refinement), then transfer existing safety proofs [α]φ → [β]φ
  - Modular proof decomposition reduces full-system re-verification to local change proofs
  - **Activation**: CPS refactoring, formal verification, differential refinement logic, hybrid systems, dRL

     1|### Quantum-EEGNet for Cross-Task EEG Encoding with Quantum Machine Learning
- [[quantum-eeg-encoding]] - Hybrid quantum-classical neural network integrating variational quantum circuits into EEGNet for brain signal decoding (arXiv: 2407.19214, 2503.00080)
  - QEEGNet = EEGNet backbone + VQC layers with angle encoding
  - Outperforms EEGNet on BCI IV 2a, more noise-robust
  - Cross-dataset generalization requires task-specific tuning
  - **Activation**: quantum EEG, QEEGNet, quantum BCI, hybrid quantum neural


## 2026-05-18 - Neuroscience + Quantum (Cron Job)
     2|
     3|### Quantum Hyperdimensional Computing: a foundational paradigm for quantum neuromorphic architectures
     4|- [[quantum-hyperdimensional-computing]] - Quantum-native Hyperdimensional Computing mapping brain-inspired operations onto quantum primitives (arXiv: 2511.12664)
     5|  - HDC bundling → LCU + Oblivious Amplitude Amplification
     6|  - HDC binding → Quantum phase oracles
     7|  - HDC permutation → Quantum Fourier Transform
     8|  - HDC similarity → Hadamard Test for state fidelity
     9|  - Validated on 156-qubit IBM Heron r3; no variational training needed
    10|  - **Activation**: quantum hyperdimensional computing, QHDC, quantum neuromorphic, HDC quantum, quantum vector symbolic, brain-inspired quantum
    11|
    12|     1|### Quantum-EEGNet for Cross-Task EEG Encoding with Quantum Machine Learning
- [[quantum-eeg-encoding]] - Hybrid quantum-classical neural network integrating variational quantum circuits into EEGNet for brain signal decoding (arXiv: 2407.19214, 2503.00080)
  - QEEGNet = EEGNet backbone + VQC layers with angle encoding
  - Outperforms EEGNet on BCI IV 2a, more noise-robust
  - Cross-dataset generalization requires task-specific tuning
  - **Activation**: quantum EEG, QEEGNet, quantum BCI, hybrid quantum neural


## 2026-05-18 - Neuroscience + Quantum (Cron Job)
    13|     2|
    14|     3|### GKSL Dynamics for Quantum-Like Cognition
    15|     4|- [[gksl-quantum-cognition]] - Open quantum systems framework (GKSL/Lindblad master equation) for quantum-like modeling of cognition and decision-making, with cognitive beat detection (arXiv: 2604.18643)
    16|     5|  - GKSL master equation models mental state evolution as dissipative process in Hilbert space
    17|     6|  - Active vs Passive Hamiltonian regimes distinguish cognitive agency from classical rationality
    18|     7|  - Cognitive beats: spectral signature of internal deliberation between competing flows of mind
    19|     8|  - **Activation**: GKSL dynamics, quantum-like cognition, Lindblad equation, cognitive beats, decision making, open quantum systems
    20|     9|
    21|    10|### Quantum-EEGNet for Cross-Task EEG Encoding with Quantum Machine Learning
- [[quantum-eeg-encoding]] - Hybrid quantum-classical neural network integrating variational quantum circuits into EEGNet for brain signal decoding (arXiv: 2407.19214, 2503.00080)
  - QEEGNet = EEGNet backbone + VQC layers with angle encoding
  - Outperforms EEGNet on BCI IV 2a, more noise-robust
  - Cross-dataset generalization requires task-specific tuning
  - **Activation**: quantum EEG, QEEGNet, quantum BCI, hybrid quantum neural


## 2026-05-18 - Neuroscience Research (Cron Job)
    22|    11|
    23|    12|### REALM: Retrospective Encoder Alignment for LFP Modeling
    24|    13|- [[realm-lfp-retrospective-decoding]] - Retrospective distillation framework enabling high-performance causal LFP decoding for BCIs using Mamba-2 teacher-student architecture (arXiv: 2605.14867)
    25|    14|  - Bidirectional Mamba-2 teacher pretrained via masked autoencoding across sessions, distilled to causal student for real-time deployment
    26|    15|  - LFP-only models achieve competitive decoding performance with 2x parameter reduction and 10x faster training
    27|    16|  - **Activation**: LFP decoding, BCI, Mamba-2, knowledge distillation, causal decoder, wireless BCI, spike vs LFP
    28|    17|
    29|    18|### SpikeProphecy: Large-Scale Benchmark for Neural Population Forecasting
    30|    19|- [[spikeprophecy-benchmark]] - First large-scale benchmark for autoregressive spike-count forecasting with population metric decomposition on 105 Neuropixels sessions (arXiv: 2605.12992)
    31|    20|  - Decomposes evaluation into temporal fidelity (pop_rate_r), spatial pattern accuracy (spatial_r), and magnitude-invariant alignment (cosine_sim)
    32|    21|  - Reveals brain-region predictability hierarchy consistent across 7 architectures, sub-Poisson evaluation floor, and negative KL distillation result
    33|    22|  - **Activation**: spike forecasting, neural population, Neuropixels, metric decomposition, SSM, closed-loop BCI, digital twin
    34|    23|
    35|    24|### Quantum-EEGNet for Cross-Task EEG Encoding with Quantum Machine Learning
- [[quantum-eeg-encoding]] - Hybrid quantum-classical neural network integrating variational quantum circuits into EEGNet for brain signal decoding (arXiv: 2407.19214, 2503.00080)
  - QEEGNet = EEGNet backbone + VQC layers with angle encoding
  - Outperforms EEGNet on BCI IV 2a, more noise-robust
  - Cross-dataset generalization requires task-specific tuning
  - **Activation**: quantum EEG, QEEGNet, quantum BCI, hybrid quantum neural


## 2026-05-18 - Neuroscience Research (Cron Job)
    36|    25|
    37|    26|### Extended E-I Network Chaos-Synchrony Theory
    38|    27|### Quantum-EEGNet for Cross-Task EEG Encoding with Quantum Machine Learning
- [[quantum-eeg-encoding]] - Hybrid quantum-classical neural network integrating variational quantum circuits into EEGNet for brain signal decoding (arXiv: 2407.19214, 2503.00080)
  - QEEGNet = EEGNet backbone + VQC layers with angle encoding
  - Outperforms EEGNet on BCI IV 2a, more noise-robust
  - Cross-dataset generalization requires task-specific tuning
  - **Activation**: quantum EEG, QEEGNet, quantum BCI, hybrid quantum neural


## 2026-05-18 - Neuroscience + Quantum (Cron Job)
    39|    28|
    40|    29|### Parallel Scan Recurrent Neural Quantum States
    41|    30|- [[parallel-scan-neural-quantum-states]] - Parallel scan (prefix-sum) recurrence for GPU-parallelizable neural quantum state training in variational Monte Carlo (arXiv: 2605.13807)
    42|    31|  - Replaces O(N) sequential autoregressive sampling with O(log N) parallel scan
    43|    32|  - Enables 2D spin lattices up to 52x52 matching QMC accuracy with modest compute
    44|    33|  - Associative recurrence reformulation as critical design requirement
    45|    34|  - **Activation**: parallel scan NQS, neural quantum state, variational Monte Carlo, recurrent wave function, PSR-NQS, spin lattice simulation
    46|    35|
    47|    36|### Leggett-Garg Tests in Neural Dynamics
    48|    37|- [[leggett-garg-neural-dynamics]] - Leggett-Garg temporal correlation testing for distinguishing diffusive from non-diffusive stochastic neural dynamics (arXiv: 2605.12126)
    49|    38|  - Leggett-Garg inequality testing for temporal correlations in single neurons
    50|    39|  - Kac-type finite-velocity processes vs Wiener diffusive models
    51|    40|  - Conservative interpretation: violation ≠ quantum coherence, but against diffusive description
    52|    41|  - **Activation**: Leggett-Garg inequality, neural dynamics testing, Kac process, Telegrapher equation, non-diffusive neural models
    53|    42|
    54|    43|### Physics Guided Generative Optimization for Trotter Suzuki Decomposition
    55|    44|- [[physics-guided-generative-optimization]] - Generate-and-evaluate loop for quantum circuit optimization combining diffusion models, PINN feedback, and GNN encoding (arXiv: 2605.13268)
    56|    45|  - Conditional diffusion model proposes term grouping and formula order
    57|    46|  - PINN provides differentiable fidelity feedback for NISQ compilation
    58|    47|  - REINFORCE + Pareto tracking for hybrid discrete-continuous training space
    59|    48|  - **Activation**: generative quantum optimization, Trotter Suzuki decomposition, PINN feedback quantum, diffusion model circuit
    60|    49|
    61|    50|### Neural Fields for NV-Center Inverse Sensing
    62|    51|- [[neural-fields-quantum-sensing]] - Neural field methodology for quantum sensor inverse problems using amortization-free coordinate neural fields (arXiv: 2605.13988)
    63|    52|  - Coordinate neural field coupled to differentiable NV forward model
    64|    53|  - Tensor power-summed dipolar operator prevents center-collapse failure
    65|    54|  - Annealed positional encoding with multiscale optimization and sparsity gating
    66|    55|  - **Activation**: NV center sensing, quantum sensor inverse problem, neural field physics, differentiable quantum model
    67|    56|
    68|    57|- [[ei-network-chaos-synchrony-theory]] - Extends SCS chaos theory to E/I structured recurrent networks with target-specific inhibition, revealing three dynamical regimes and chaos suppression by coherent oscillations (arXiv: 2605.14916)
    69|    58|  - Target-specific inhibition breaks E-I balance, organizing phase diagram into inhibition-dominated (quiescent/async chaos), excitation-dominated (sync chaos/coherent oscillations)
    70|    59|  - Coherent oscillations actively suppress chaotic fluctuations — no coexistence regime
    71|    60|  - **Activation**: E-I network chaos, excitatory inhibitory balance, SCS theory extension, target-specific inhibition, chaos synchrony transition, dynamical mean field neural
    72|    61|
    73|    62|### Embodied Neurocomputation Framework
    74|    63|- [[embodied-neurocomputation-framework]] - Systems-level framework for interfacing biological neural cultures with silicon computing via closed-loop task-driven validation, achieving 12 successful configs out of 1,300 tested (arXiv: 2605.13315)
    75|    64|  - BNNs outperform DQN under matched interaction budgets for odor-gradient navigation tasks
    76|    65|  - Multi-combinatorial encoding/decoding optimization requires Bayesian or evolutionary strategies
    77|    66|  - **Activation**: biological neural network computation, BNN encoding decoding, bio-silicon hybrid, embodied neurocomputation, living neural computing
    78|    67|
    79|    68|### REALM: Retrospective Encoder Alignment for LFP Modeling
    80|    69|- REALM uses retrospective distillation to bridge offline-to-online LFP decoding, achieving 2× parameter reduction and 10× faster training while outperforming SOTA causal/non-causal methods (arXiv: 2605.14867)
    81|    70|  - Bidirectional Mamba-2 teacher → causal student via representation alignment + task supervision
    82|    71|  - Enables real-time wireless implantable BCI without spike signals
    83|    72|  - **Activation**: REALM, LFP modeling, retrospective distillation, causal neural decoding, wireless BCI, Mamba neural signal
    84|    73|
    85|    74|### Cortical Microcircuit Information Flux Optimization
    86|    75|- Reverse-engineering study showing cortical layer 5 embedding networks enhance information flux via effective biases and Recurrence Resonance, preventing attractor trapping (arXiv: 2605.14680)
    87|    76|  - Embedding network shifts core neurons to higher-entropy regime and supplies stochastic fluctuations
    88|    77|  - Optimized biases can emerge from simple self-organization principles
    89|    78|  - **Activation**: cortical microcircuit, information flux, recurrence resonance, reverse engineering neural network, cortical layer 5
    90|    79|
    91|    80|
    92|    81|### Quantum-EEGNet for Cross-Task EEG Encoding with Quantum Machine Learning
- [[quantum-eeg-encoding]] - Hybrid quantum-classical neural network integrating variational quantum circuits into EEGNet for brain signal decoding (arXiv: 2407.19214, 2503.00080)
  - QEEGNet = EEGNet backbone + VQC layers with angle encoding
  - Outperforms EEGNet on BCI IV 2a, more noise-robust
  - Cross-dataset generalization requires task-specific tuning
  - **Activation**: quantum EEG, QEEGNet, quantum BCI, hybrid quantum neural


## 2026-05-18 - 神经科学 + 量子力学 (Cron Job)
    93|    82|
    94|    83|### Rogue Variable Theory: A Quantum-Compatible Cognition Framework
    95|    84|- [[quantum-compatible-cognition-framework]] - 量子兼容认知框架，建模前事件认知状态和潜在解释竞争 (arXiv: 2601.00466)
    96|    85|  - 核心要点: Mirrored Personal Graph (MPG) 映射认知状态到希尔伯特空间
    97|    86|  - 核心要点: Rosetta Stone Layer (RSL) 实现跨用户认知状态比较
    98|    87|  - 核心要点: Rogue Operator 谱分析识别认知偏离方向
    99|    88|  - **Activation**: rogue variable theory, RVT, quantum cognition, pre-event states, cognitive complementarity
   100|    89|
   101|    90|### Natural Intelligence: the information processing power of life
   102|    91|- [[natural-intelligence-bio-ops]] - 量化生物系统信息处理能力，估计地球生命总计算量 (arXiv: 2506.16478)
   103|    92|  - 核心要点: 人体每秒执行 ~10^22 bio-ops，超过全球所有计算机总和
   104|    93|  - 核心要点: 大脑仅占总生物计算的一小部分
   105|    94|  - **Activation**: natural intelligence, bio-ops, biological computation, 生物信息处理
   106|    95|
   107|    96|### Quantum effects in the brain: A review
   108|    97|- [[quantum-effects-in-brain-review]] - 量子效应在大脑中的可能性评估框架 (arXiv: 1910.08423)
   109|    98|  - 核心要点: 系统评估量子生物学在神经科学中的证据
   110|    99|  - 核心要点: 退相干时间 vs 生物时间尺度是核心判据
   111|   100|  - **Activation**: quantum effects brain, quantum biology, microtubule quantum, 量子脑效应
   112|   101|
   113|   102|### Quantum-EEGNet for Cross-Task EEG Encoding with Quantum Machine Learning
- [[quantum-eeg-encoding]] - Hybrid quantum-classical neural network integrating variational quantum circuits into EEGNet for brain signal decoding (arXiv: 2407.19214, 2503.00080)
  - QEEGNet = EEGNet backbone + VQC layers with angle encoding
  - Outperforms EEGNet on BCI IV 2a, more noise-robust
  - Cross-dataset generalization requires task-specific tuning
  - **Activation**: quantum EEG, QEEGNet, quantum BCI, hybrid quantum neural


## 2026-05-18 - Neuroscience Research (Cron Job)
   114|   103|
   115|   104|### BiSpikCLM: Binary Spiking Causal Language Model
   116|   105|- [[bispikclm-binary-spiking-llm]] - First fully binary spiking MatMul-free causal language model with Softmax-Free Spiking Attention and Spike-Aware Alignment Distillation (arXiv: 2605.13859)
   117|   106|  - SFSA eliminates softmax and floating-point ops in autoregressive language modeling, using binary spike-based computation
   118|   107|  - SpAD distills ANN→SNN across 4 levels (embeddings, attention maps, intermediate features, logits); 1.3B model trained with only 5.6% tokens
   119|   108|  - **Activation**: BiSpikCLM, binary spiking LLM, softmax-free spiking attention, spike-aware distillation, spiking language model, event-driven NLP
   120|   109|
   121|   110|### ASTDP-GAD: Neuromorphic Graph Anomaly Detection
   122|   111|- [[astdp-gad-neuromorphic-graph-anomaly]] - Adaptive Spiking Temporal Dynamics Plasticity framework combining spiking GNNs with STDP learning for energy-efficient anomaly detection in dynamic networks (arXiv: 2605.13863)
   123|   112|  - Six innovations: adaptive LIF spike encoding, LIFGAT with lateral inhibition, event-driven hypergraph memory, spike rate contrast pooling, adaptive STDP layers, multi-scale temporal fusion
   124|   113|  - Theoretical guarantees: LIFGAT universal approximation, STDP stable convergence, hypergraph prototype convergence, 5× variance reduction
   125|   114|  - **Activation**: ASTDP-GAD, spiking graph neural network, neuromorphic anomaly detection, STDP graph learning, LIF graph attention, event-driven graph anomaly
   126|   115|
   127|   116|### HormoneT5: Hormone-inspired Emotion Layer for Transformers
   128|   117|- [[hormone-t5-emotion-layer]] - Biologically-inspired Hormone Emotion Block augmenting transformers with six continuous hormone-like values via per-hormone attention heads for emotionally-appropriate response generation (arXiv: 2605.13858)
   129|   118|  - Six hormone dimensions (dopamine/serotonin/oxytocin/cortisol/adrenaline/endorphin) computed through orthogonal query attention with temperature scaling
   130|   119|  - Multi-objective training: seq2seq loss + hormone prediction with margin penalties + diversity regularization achieving 85%+ per-hormone accuracy
   131|   120|  - **Activation**: HormoneT5, HELT, hormone emotion layer, affective computing transformer, endocrine-inspired AI, emotional language models, bio-inspired emotion modeling
   132|   121|
   133|   122|### State-Space NTK Collapse Near Bifurcations
   134|   123|- [[state-space-ntk-collapse-bifurcations]] - Local theory of gradient descent near bifurcations via state-space neural tangent kernel (sNTK), showing sNTK collapses to rank-one operators matching classical normal forms (arXiv: 2605.12763)
   135|   124|  - Near codimension-1 bifurcations, sNTK reduces to rank-one operator in bifurcation-relevant channel
   136|   125|  - Low-rank natural gradient resolves learning instability near bifurcations with minimal overhead
   137|   126|  - **Activation**: state-space NTK, sNTK collapse, bifurcation learning dynamics, RNN training bifurcation, normal form learning theory, neural tangent kernel recurrent
   138|   127|
   139|   128|### Empirical Scaling Laws in Balanced Networks with Conductance-Based Synapses
   140|   129|- [[balanced-network-scaling-conductance]] - Cancellation effect between conductance-based synapses and spike time correlations produces realistic membrane potential variability (arXiv: 2605.12404)
   141|   130|  - Current-based + correlations overestimate variability; conductance-based alone underestimates
   142|   131|  - Both assumptions together yield moderate, realistic Vm variance across network sizes
   143|   132|  - **Activation**: balanced network conductance synapse, membrane potential variability, E/I balanced network, spike time correlation, cortical variability modeling
   144|   133|
   145|   134|### Quantum-EEGNet for Cross-Task EEG Encoding with Quantum Machine Learning
- [[quantum-eeg-encoding]] - Hybrid quantum-classical neural network integrating variational quantum circuits into EEGNet for brain signal decoding (arXiv: 2407.19214, 2503.00080)
  - QEEGNet = EEGNet backbone + VQC layers with angle encoding
  - Outperforms EEGNet on BCI IV 2a, more noise-robust
  - Cross-dataset generalization requires task-specific tuning
  - **Activation**: quantum EEG, QEEGNet, quantum BCI, hybrid quantum neural


## 2026-05-18 - Information Science + Quantum (Cron Job)
   146|   135|
   147|   136|### Toward Covert Quantum Computing
   148|   137|- [[covert-quantum-computing]] - Information-theoretic covertness analysis for multi-tenant quantum cloud computing, using discrete isoperimetric inequalities and quantum-strategy framework (arXiv: 2605.14325)
   149|   138|  - Only O(√n) border qubits provide detection information to adversary in planar layout
   150|   139|  - Long-range crosstalk from drive/control lines breaks covertness beyond nearest-neighbor model
   151|   140|  - **Activation**: covert quantum computing, quantum cloud security, quantum crosstalk, quantum side channel, QCU privacy, quantum isolation
   152|   141|
   153|   142|### Wavelet Variance Equipartition as Threshold for World-Model Quality and Quantum Kernel TN-Simulability
   154|   143|- [[wavelet-variance-equipartition-quantum]] - Physics-grounded metric for world-model latent space quality using wavelet scaling exponent α=1/2 as sharp boundary for quantum kernel classical simulability via tensor network contraction (arXiv: 2605.11557)
   155|   144|  - Wavelet scaling exponent α≈1/2 mirrors Kolmogorov inertial range, providing optimal representation quality diagnostic
   156|   145|  - Sharp phase transition at α=1/2 determines classical simulability of amplitude-encoded quantum kernels
   157|   146|  - **Activation**: wavelet variance equipartition, quantum kernel simulability, wavelet scaling exponent, tensor network contraction, world model quality, Kolmogorov inertial range
   158|   147|
   159|   148|### A Toolbox to Understand the Physics of Quantum Data Management
   160|   149|- [[quantum-data-management-toolbox]] - Physics-informed spectral analysis toolbox for evaluating quantum annealing in data management problems through energy gaps and eigenstate structure (arXiv: 2605.14719)
   161|   150|  - Spectral properties inaccessible from hardware measurements essential for understanding computational hardness
   162|   151|  - Bridging quantum computing and database research via physics-informed co-design framework
   163|   152|  - **Activation**: quantum data management, quantum annealing database, spectral analysis quantum, quantum-classical co-design, quantum optimization Hamiltonian
   164|   153|
   165|   154|## 2026-05-17 - Neuroscience Research (Cron Job)
   166|   155|
   167|   156|### NeuroTrain: SNN Training Survey & Benchmarking Framework
   168|   157|- [[neurotrain-local-learning-snn-benchmarking]] - Comprehensive taxonomy and open-source benchmarking framework for SNN training algorithms, covering surrogate-gradient, local/three-factor learning, plasticity, and ANN-to-SNN conversion (arXiv: 2605.15058)
   169|   158|  - First unified taxonomy spanning 6 major SNN training paradigms with computational principles and locality analysis
   170|   159|  - Releases NeuroTrain: snnTorch-based open framework for reproducible benchmarking across datasets, architectures, and training regimes
   171|   160|  - **Activation**: neurotrain, SNN training taxonomy, local learning rules, surrogate gradient, three-factor learning, snnTorch benchmarking
   172|   161|
   173|   162|### Transport Mean Field for SNN Population Dynamics
   174|   163|- [[transport-mean-field-snn]] - 基于传输方程的SNN群体动力学解析理论，从初始电压分布推导脉冲率涨落，突破传统均值场稳态假设 (arXiv: 2605.14319)
   175|   164|  - Transport solution to advection equation replaces asymptotic steady-state mean field approaches
   176|   165|  - Captures firing rate fluctuations from dynamic interaction of initial conditions, time-varying inputs, and coupling
   177|   166|  - **Activation**: transport mean field, firing rate fluctuations, Fokker-Planck, LIF dynamics, neural population, initial density effects
   178|   167|
   179|   168|### Selective Alignment Knowledge Distillation for SNNs
   180|   169|- [[sealkd-snn-knowledge-distillation]] - Addresses SNN-ANN performance gap by selectively aligning class-level and temporal knowledge during distillation, correcting erroneous timesteps while preserving useful temporal dynamics (arXiv: 2605.14252)
   181|   170|  - Equalizes competing logits at erroneous timesteps rather than forcing uniform alignment
   182|   171|  - Reweights temporal alignment by confidence and inter-timestep similarity
   183|   172|  - **Activation**: selective alignment KD, SeAl-KD, SNN knowledge distillation, timestep-aware distillation
   184|   173|
   185|   174|### Dual-axis Zebrafish Circuit Attribution
   186|   175|- [[dual-axis-zebrafish-circuits]] - 斑马鱼顶盖微环路双轴归因框架，通过SNN消融量化子回路在能量效率和鲁棒性中的独立计算角色，并迁移至ANN架构 (arXiv: 2605.13924)
   187|   176|  - ns_TIN subcircuit: spike-efficient internal information gate (low spike footprint, measurable influence on prediction error)
   188|   177|  - superficial_TIN subcircuit: highest robustness sensitivity, feedback-like stabilization role
   189|   178|  - **Activation**: dual-axis attribution, zebrafish tectal circuit, energy-efficient architecture, robust neural network, SNN ablation
   190|   179|
   191|   180|### FiTS: Interpretable Spiking Neurons via Frequency Selectivity and Temporal Shaping
   192|   181|- [[fits-interpretable-spiking-neuron]] - SNN neuron factorizing temporal computation into Frequency Selectivity (FS) and Temporal Shaping (TS) modules, enabling learnable frequency preferences and group-delay modulation (arXiv: 2605.13071)
   193|   182|  - FS parameterizes each neuron's target frequency as maximizer of subthreshold magnitude response
   194|   183|  - TS reshapes when frequency components contribute to membrane voltage through group-delay modulation
   195|   184|  - **Activation**: FiTS, frequency selectivity spiking neuron, interpretable SNN, temporal shaping, group-delay modulation
   196|   185|
   197|   186|### NERVE: Network-Aware Brain FC Tokenization
   198|   187|- [[nerve-brain-fc-tokenization]] - Self-supervised FC representation learning via bilinear tokenization that respects brain network organization, reducing parameter complexity from quadratic to linear (arXiv: 2605.14048)
   199|   188|  - Bilinear factorization embeds heterogeneous network-pair patches while preserving network identity
   200|   189|  - Validated on ABCD, PNC, CCNP cohorts for behavior/psychopathology prediction with stable transferable representations
   201|   190|  - **Activation**: NERVE, brain FC tokenization, bilinear factorization, masked autoencoder brain, network-aware FC, self-supervised fMRI
   202|   191|
   203|   192|## 2026-05-17 - Neuroscience Research (Cron Job)
   204|   193|
   205|   194|### Multi-Timescale Conductance Spiking Networks
   206|   195|- [[multi-timescale-conductance-snn]] - Gradient-trainable spiking networks using multi-timescale conductances for energy-aware temporal processing, outperforming LIF and AdLIF without surrogate gradients (arXiv: 2605.11835)
   207|   196|  - I-V curve shaping via fast/slow/ultra-slow conductances enables rich firing regimes (tonic, phasic, bursting) in single model
   208|   197|  - Direct backpropagation through time without surrogate-gradient approximations
   209|   198|  - **Activation**: multi-timescale conductance, MTC-SNN, conductance spiking, gradient-trainable SNN, I-V curve shaping
   210|   199|
   211|   200|### Embodied Neurocomputation Framework
   212|   201|- [[embodied-neurocomputation]] - Systems-level framework for interfacing biological neural cultures with task-driven validation, BNN outperforms silicon DQN in closed-loop navigation (arXiv: 2605.13315)
   213|   202|  - First large-scale parameter optimization of BNN encoding configurations (~1,300 configs, 4,000+ hours)
   214|   203|  - 12 configurations demonstrated consistent learning, surpassing optimized DQN under same budget
   215|   204|  - **Activation**: embodied neurocomputation, biological neural networks, bio-silicon hybrid, BNN neurocomputation
   216|   205|
   217|   206|## 2026-05-17 - Information Science + Quantum (Cron Job)
   218|   207|
   219|   208|### Quantum Complexity in Gravity, QFT, and Quantum Information Science
   220|   209|- [[quantum-complexity-definitions]] - Bridges quantum information theory, many-body physics, QFT, and holography to unify definitions of quantum complexity (arXiv: 2503.10753)
   221|   210|  - Multiple complexity definitions: circuit complexity, geometric (unitary group geodesics), and dynamical (state/operator spreading via tensor networks)
   222|   211|  - Proposes relationship between boundary complexity and gravitational observables via AdS/CFT correspondence
   223|   212|  - **Activation**: quantum complexity, random quantum circuits, unitary geodesics, tensor network complexity, holographic complexity, AdS/CFT
   224|   213|
   225|   214|### Information-Theoretic Authenticated Private Information Retrieval
   226|   215|- [[information-theoretic-pir]] - Protocol enabling clients to privately retrieve database items with information-theoretic privacy and authenticity guarantees against malicious adversaries (arXiv: 2604.01551)
   227|   216|  - Achieves unconditional security: server learns nothing about retrieved item, client verifies response integrity
   228|   217|  - O(sqrt(n)) communication complexity using error-correcting codes and polynomial commitments
   229|   218|  - **Activation**: private information retrieval, aPIR, information-theoretic security, privacy-preserving retrieval, authenticated PIR
   230|   219|
   231|   220|### Quantum complexity in gravity, quantum field theory, and quantum information science
   232|   221|- [[quantum-complexity-definitions]] - Bridges quantum information theory, many-body physics, QFT, and holography to unify definitions of quantum complexity (arXiv: 2503.10753)
   233|   222|  - Multiple complexity definitions: circuit complexity, geometric (unitary group geodesics), and dynamical (state/operator spreading via tensor networks)
   234|   223|  - Proposes relationship between boundary complexity and gravitational observables via AdS/CFT correspondence
   235|   224|  - **Activation**: quantum complexity, random quantum circuits, unitary geodesics, tensor network complexity, holographic complexity, AdS/CFT
   236|   225|
   237|   226|### Information-Theoretic Authenticated Private Information Retrieval
   238|   227|- [[information-theoretic-pir]] - Protocol enabling clients to privately retrieve database items with information-theoretic privacy and authenticity guarantees against malicious adversaries (arXiv: 2604.01551)
   239|   228|  - Achieves unconditional security: server learns nothing about retrieved item, client verifies response integrity
   240|   229|  - O(sqrt(n)) communication complexity using error-correcting codes and polynomial commitments
   241|   230|  - **Activation**: private information retrieval, aPIR, information-theoretic security, privacy-preserving retrieval, authenticated PIR
   242|   231|
   243|   232|### Quantum-EEGNet for Cross-Task EEG Encoding with Quantum Machine Learning
- [[quantum-eeg-encoding]] - Hybrid quantum-classical neural network integrating variational quantum circuits into EEGNet for brain signal decoding (arXiv: 2407.19214, 2503.00080)
  - QEEGNet = EEGNet backbone + VQC layers with angle encoding
  - Outperforms EEGNet on BCI IV 2a, more noise-robust
  - Cross-dataset generalization requires task-specific tuning
  - **Activation**: quantum EEG, QEEGNet, quantum BCI, hybrid quantum neural


## 2026-05-18 - Information Science + Quantum (Cron Job)
   244|   233|
   245|   234|### New approaches to almost i.i.d. information theory
   246|   235|- [[almost-iid-quantum-information]] - Alternative frameworks for quantum information analysis using Wasserstein distance and k-body marginals, relaxing i.i.d. assumption (arXiv: 2605.15114)
   247|   236|  - Quantum Wasserstein distance defines almost-i.i.d. states beyond strict independence
   248|   237|  - Strict hierarchical relationship between Wasserstein and k-body marginal definitions
   249|   238|  - **Activation**: almost i.i.d., quantum Wasserstein distance, k-body marginals, non-i.i.d. quantum protocols
   250|   239|
   251|   240|### Wavelet Variance Equipartition as a Threshold for World-Model Quality and Quantum Kernel TN-Simulability
   252|   241|- [[wavelet-variance-equipartition-quantum]] - Physics-grounded spectral metric for assessing world-model quality and quantum kernel tensor network simulability (arXiv: 2605.11557)
   253|   242|  - Wavelet variance equipartition identifies threshold for latent space structural fidelity
   254|   243|  - Links world-model quality to quantum kernel tensor network simulability
   255|   244|  - **Activation**: wavelet variance equipartition, world-model quality, quantum kernel simulability, spectral analysis
   256|   245|
   257|   246|### ORCHID: Orchestrated Reduction Consensus for Hash-based Integrity in Distributed Ledgers
   258|   247|- [[orchid-distributed-consensus]] - Bio-inspired consensus protocol mapping neuroscientific binding problem to distributed ledger integrity (arXiv: 2605.12211)
   259|   248|  - Maps neural binding problem to distributed consensus coordination
   260|   249|  - Hierarchical orchestrated reduction with hash-based integrity verification
   261|   250|  - **Activation**: ORCHID consensus, bio-inspired consensus, distributed ledger integrity, hash-based verification
   262|   251|
   263|   252|### HQTN-SER: Speech Emotion Recognition with Hybrid Quantum Tensor Networks
   264|   253|- [[hqtn-speech-emotion-quantum]] - Hybrid quantum tensor network combining quantum tensor networks with classical ML for robust speech emotion recognition (arXiv: 2605.14523)
   265|   254|  - Tensor train decomposition compresses high-dimensional audio features
   266|   255|  - Quantum-enhanced expressivity captures subtle emotional cues under recording variability
   267|   256|  - **Activation**: HQTN speech emotion, quantum tensor network SER, hybrid quantum-classical emotion recognition
   268|   257|
   269|   258|### Failure-Guided Fuzzing for Hybrid Quantum-Classical Programs
   270|   259|- [[failure-guided-quantum-fuzzing]] - Two-phase failure-guided fuzzing for VQE/QAOA programs using concolic seeds + local parameter mutation (arXiv: 2605.14219)
   271|   260|  - Models hybrid inputs as pairs of classical optimizer hyperparameters and quantum circuit parameters
   272|   261|  - Two-phase strategy: seed discovery (concolic) + local fuzzing around failure points
   273|   262|  - Local fuzzing is main driver of improvement; concolic seed discovery helps VQE but unstable for QAOA
   274|   263|  - **Activation**: quantum fuzzing, HQC testing, failure-guided fuzzing, hybrid quantum testing, VQE debugging
   275|   264|
   276|   265|## 2026-05-17 - Neuroscience Research (Cron Job)
   277|   266|
   278|   267|### BiSpikCLM: A Spiking Language Model integrating Softmax-Free Spiking Attention and Spike-Aware Alignment Distillation
   279|   268|- [[bispikclm-binary-spiking-llm]] - First fully binary spiking MatMul-free causal language model with Softmax-Free Spiking Attention and Spike-Aware Alignment Distillation (arXiv: 2605.13859)
   280|   269|  - SFSA replaces softmax causal attention with spike-based Hadamard-masked integer dot product, eliminating all FP operations in attention
   281|   270|  - SpAD distillation enables training with only 5.6% of standard tokens (10B vs 180B), achieving 42.19% accuracy at 4.16% energy cost of OPT-1.3B
   282|   271|  - **Activation**: BiSpikCLM, binary spiking LLM, softmax-free attention, spiking NLP, MatMul-free language model, SFSA, spike-aware distillation
   283|   272|
   284|   273|### REALM: Retrospective Encoder Alignment for LFP Modeling
   285|   274|- [[realm-lfp-retrospective-decoding]] - First LFP-only foundation model for causal behavior decoding via retrospective distillation from bidirectional Mamba-2 teacher (arXiv: 2605.14867)
   286|   275|  - 3-stage pipeline: self-supervised CMAE pretraining → retrospective distillation → fine-tuning; achieves SOTA LFP decoding with 2× parameter reduction and 10× faster convergence
   287|   276|  - First real-time LFP decoder deployed on edge hardware (Jetson Orin Nano, RPi 5), enabling wireless implantable BCI without spike signals
   288|   277|  - **Activation**: REALM, LFP decoding, causal neural decoding, retrospective distillation, Mamba-2 BCI, wireless BCI, offline-to-online neural decoding
   289|   278|
   290|   279|## 2026-05-17 - Neuroscience Research (Cron Job)
   291|   280|
   292|   281|### Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale
   293|   282|- [[mamba-spike-forecaster-bci]] - Mamba state-space model trained on spike counts implicitly decodes behavior without supervised labels (arXiv: 2605.12999)
   294|   283|  - Single Mamba forecaster trained only on next-step Poisson rate prediction simultaneously forecasts neural dynamics AND decodes behavior
   295|   284|  - Predicted rates carry more behavioral info than raw spike counts (75.7% choice decoding vs ~70% linear baseline on Steinmetz benchmark)
   296|   285|  - **Activation**: mamba spike forecaster, behavioral decoding, BCI closed-loop, Neuropixels decoding, neural population forecasting
   297|   286|
   298|   287|### Letting the Neural Code Speak: Automated Characterization of Monkey Visual Neurons through Human Language
   299|   288|- [[neural-code-language-interpretability]] - LLM-driven closed-loop framework generates and verifies semantic hypotheses for neuron selectivity (arXiv: 2605.12485)
   300|   289|  - Gemini 3.0 Pro + Imagen 4.0 + digital twins create testable natural language descriptions of what each V1/V4 neuron encodes
   301|   290|  - Hypothesis-generated images drove 96.1% of V4 neurons above 95th percentile of natural-image responses (vs 10% random baseline)
   302|   291|  - **Activation**: neural code speak, semantic hypothesis, neuron characterization, language-based interpretability, digital twin visual cortex
   303|   292|
   304|   293|---
   305|   294|
   306|   295|
   307|   296|### NeuroTrain: Surveying Local Learning Rules for Spiking Neural Networks with an Open Benchmarking Framework
   308|   297|- [[neurotrain-snn-benchmarking]] - Comprehensive SNN training algorithm taxonomy and open benchmarking framework spanning surrogate-gradient, local/three-factor learning, predictive coding, and neuromodulated plasticity (arXiv: 2605.15058)
   309|   298|  - First unified taxonomy of SNN training algorithms with standardized benchmarking
   310|   299|  - Local learning rules achieve competitive accuracy with significantly lower memory than backprop
   311|   300|  - **Activation**: SNN, spiking neural network, local learning, benchmarking, surrogate gradient, STDP, three-factor learning, predictive coding
   312|   301|
   313|   302|### Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale
   314|   303|- [[mamba-spike-population-forecaster]] - Single Mamba forecaster trained on next-step spike counts simultaneously predicts neural activity and decodes behavior, outperforming linear decoders on raw spikes (arXiv: 2605.12999)
   315|   304|  - Mamba's predicted rates decode mouse choice at 75.7% (2.3x chance) and stimulus side at 66.1% (2x chance)
   316|   305|  - ~100-150 trial calibration brings readout within 1-2pp of asymptote; fits 50ms bin budget on workstation GPUs
   317|   306|  - **Activation**: Mamba, spike forecasting, behavioral decoding, Neuropixels, closed-loop BCI, visual discrimination
   318|   307|
   319|   308|### Self-organized MT Direction Maps Emerge from Spatiotemporal Contrastive Optimization
   320|   309|- [[spatiotemporal-tdann-mt-direction-maps]] - Spatiotemporal TDANN framework showing MT direction maps emerge from self-supervised contrastive learning with spatial regularization, unifying ventral and dorsal stream self-organization (arXiv: 2605.11718)
   321|   310|  - Model reproduces macaque MT DSI, circular variance, and pinwheel density (~3.14/mm2) from naturalistic video alone
   322|   311|  - MT tuning properties emerge from trade-off between discriminative pressure and spatial regularization
   323|   312|  - **Activation**: TDANN, MT cortex, direction selectivity, self-organization, MoCo, visual cortex, dorsal stream
   324|   313|
   325|   314|### Are Cortical Microcircuits Optimized for Information Flux? - A Simulation-based Reverse Engineering Study
   326|   315|- [[cortical-microcircuit-information-flux]] - Simulation-based reverse engineering of cortical microcircuits using mutual information between network states to evaluate structural optimization (arXiv: 2605.14680)
   327|   316|  - Cortical-like connectivity with E/I balance significantly outperforms random networks for information flux
   328|   317|  - Demonstrates evolutionary optimization of neural architecture for information processing capacity
   329|   318|  - **Activation**: cortical microcircuit, information flux, E/I balance, reverse engineering, mutual information, layer 5
   330|   319|
   331|   320|## 2026-05-17 - Information Science + Quantum (Cron Job)
   332|   321|
   333|   322|### Toward Covert Quantum Computing
   334|   323|- [[covert-quantum-computing]] - Privacy-preserving multi-tenant quantum computation framework analyzing adversarial detection, spatial isolation, and crosstalk side channels (arXiv: 2605.14325)
   335|   324|  - Only O(√n) border qubits provide detection information under nearest-neighbor crosstalk model
   336|   325|  - Long-range coupling from drive/control lines creates exploitable side channels
   337|   326|  - **Activation**: covert quantum computing, quantum privacy, multi-tenant security, crosstalk
   338|   327|
   339|   328|### Energy efficiency of quantum computers
   340|   329|- [[quantum-energy-efficiency]] - Framework defining energy efficiency metric for quantum computers as algorithms-per-joule, enabling cross-platform comparison of superconducting, trapped-ion, neutral-atom, and photonic platforms (arXiv: 2605.15090)
   341|   330|  - Energy efficiency = N algorithms executed / E joules consumed
   342|   331|  - Accounts for full hardware stack: cryogenics, control electronics, error correction
   343|   332|  - **Activation**: quantum energy efficiency, quantum power consumption, platform comparison
   344|   333|
   345|   334|### A Toolbox to Understand the Physics of Quantum Data Management
   346|   335|- [[quantum-data-management-toolbox]] - Physics-based framework mapping quantum device behavior to database problem structure, evaluating quantum annealing for query optimization and data management (arXiv: 2605.14719)
   347|   336|  - Maps QUBO formulations to quantum annealer connectivity constraints
   348|   337|  - Provides classical baselines for quantum advantage assessment
   349|   338|  - **Activation**: quantum data management, quantum database, quantum annealing QUBO
   350|   339|
   351|   340|### CyberAId: AI-Driven Cybersecurity for Financial Service Providers
   352|   341|- [[cyberaid-ai-security-framework]] - Hybrid multi-agent AI security framework combining LLM subagents with SIEM/XDR telemetry, privacy-preserving federation, and quantum authentication for financial services (arXiv: 2605.01892)
   353|   342|  - Specialist subagents reason over classical telemetry rather than replacing it
   354|   343|  - Four falsifiable design principles with bounded human-in-the-loop autonomy
   355|   344|  - **Activation**: AI cybersecurity, multi-agent SOC, collaborative defense, SIEM LLM
   356|   345|## 2026-05-17 - 信息学/量子力学 (Cron Job)
   357|   346|
   358|   347|### QAP-Router: Tackling Qubit Routing as Dynamic Quadratic Assignment with Reinforc
   359|   348|- [[qap-router-tackling-qubit-routing-dynamic]] - Qubit routing is a fundamental problem in quantum compilation, known to be NPhard (arXiv: 2605.12365)
   360|   349|  - Core methodology from recent arxiv paper
   361|   350|  - Category: quant-ph
   362|   351|  - **Activation**: quantum, learning, network, gate, routing
   363|   352|## 2026-05-17 - 信息学/量子力学 (Cron Job)
   364|   353|
   365|   354|### CERTIFY-ED: A Multi-Layer Verification Framework for Exact Diagonalization of Qu
   366|   355|- [[certify-ed-multi-layer-verification-framework-exact]] - Exact diagonalization (ED) is a workhorse technique in computational quantum many-body physics, but  (arXiv: 2605.11787)
   367|   356|  - Core methodology from recent arxiv paper
   368|   357|  - Category: cond-mat.str-el
   369|   358|  - **Activation**: quantum, algorithm, machine, verification
   370|   359|## 2026-05-17 - Information Science (Cron Job)
   371|   360|
   372|   361|### Failure-Guided Fuzzing for Hybrid Quantum-Classical Programs
   373|   362|- [[failure-guided-quantum-fuzzing]] - Two-phase failure-guided fuzzing for VQE/QAOA programs using concolic seeds + local parameter mutation (arXiv: 1188)
   374|   363|  - Local fuzzing around non-convergent seeds drives most improvement over random testing
   375|   364|  - Concolic seed discovery effective for VQE, less stable for QAOA
   376|   365|  - **Activation**: quantum fuzzing, HQC testing, failure-guided fuzzing, hybrid quantum testing
   377|   366|
   378|   367|
   379|   368|### Toward Covert Quantum Computing
   380|   369|- [[quantum-information-security]] - 多租户量子云平台中的隐蔽计算与侧信道分析模式 (arXiv: 2605.14325)
   381|   370|  - O(√n) 边界量子比特提供泄露信息，但长程耦合超越边界假设
   382|   371|  - 使用量子策略框架建模自适应对手的检测能力
   383|   372|  - 控制线泄漏导致空间隔离策略失效
   384|   373|  - **Activation**: covert quantum computing, crosstalk, side channel, spatial isolation
   385|   374|
   386|   375|### Failure-Guided Fuzzing for Hybrid Quantum-Classical Programs
   387|   376|- [[quantum-information-security]] - 混合量子-经典程序的两阶段失败导向模糊测试方法 (arXiv: 2605.14219)
   388|   377|  - 先搜索非收敛种子再局部模糊电路参数的两阶段策略
   389|   378|  - 失败引导局部模糊测试是改进随机测试的主要驱动力
   390|   379|  - 合解种子发现对 VQE 有效但对 QAOA 不稳定
   391|   380|  - **Activation**: quantum fuzzing, HQC testing, VQE, QAOA, concolic testing
   392|   381|
   393|   382|
   394|   383|### Blind Quantum Computation on a Modular Superconducting Processor
   395|   384|- [[blind-quantum-computation]] - 盲量子计算方法论，实现云端量子计算中算法/输入/输出的信息论安全 (arXiv: 2605.14656v1)
   396|   385|    - 基于测量基量子计算的UBQC协议，客户端仅需有限量子能力即可委托计算
   397|   386|    - 模块化超导处理器架构实现分布式盲计算，降低单模块量子比特需求
   398|   387|  - **Activation**: blind quantum computation, secure quantum cloud, quantum privacy, delegated quantum computing, UBQC, measurement-based quantum computing
   399|   388|### New approaches to almost i.i.d. information theory
   400|   389|- [[almost-iid-quantum-information]] - Strict hierarchy of almost i.i.d. quantum state definitions (Wasserstein, k-body marginals, Mazzola) (arXiv: 1165)
   401|   390|  - Establishes strict separation between three definitions of "almost i.i.d." quantum states
   402|   391|  - Quantum Wasserstein distance bridges gap between physical relevance and mathematical tractability
   403|   392|  - **Activation**: almost i.i.d. quantum, quantum Wasserstein distance, k-body marginals
   404|   393|
   405|   394|## 2026-05-17 - Information Science + Quantum (Cron Job) - Update
   406|   395|
   407|   396|### QLAM: A Quantum Long-Attention Memory Approach to Long-Sequence Token Modeling
   408|   397|- [[qlam-quantum-attention-memory]] - 量子长注意力记忆方法，利用量子叠加实现长程依赖建模，降低注意力复杂度 (arXiv: 2605.13833v1)
   409|   398|    - 量子叠加态并行编码所有token对注意力分数，振幅放大提取重要长程依赖
   410|   399|    - 混合经典-量子架构：经典编码局部特征，量子模块处理长程依赖
   411|   400|  - **Activation**: quantum attention, QLAM, long sequence quantum, quantum memory, long-range dependencies, quantum transformer
   412|   401|
   413|   402|
   414|   403|
   415|   404|## 2026-05-17 - Neuroscience Research (Cron Job)
   416|   405|
   417|   406|### NeuroTrain: Surveying Local Learning Rules for Spiking Neural Networks with an Open Benchmarking Framework
   418|   407|- [[neurotrain-snn-benchmarking]] - 首次统一SNN训练算法分类体系，发布开源snnTorch基准测试框架 (arXiv: 2605.15058v1)
   419|   408|    - 覆盖代理梯度反传、局部学习、三因子规则、ANN转SNN、非标准优化五大类
   420|   409|    - 揭示生物合理性-计算效率-任务性能的权衡三角关系
   421|   410|  - **Activation**: SNN training, neurotrain, surrogate gradient, local learning rules, three-factor learning, ANN-to-SNN conversion, snnTorch benchmarking
   422|   411|
   423|   412|### REALM: Retrospective Encoder Alignment for LFP Modeling
   424|   413|- [[realm-lfp-retrospective-decoding]] - 回顾性蒸馏框架实现因果LFP行为解码，适用于无线植入BCI (arXiv: 2605.14867v1)
   425|   414|    - 双向Mamba-2教师模型掩码自编码预训练，蒸馏至紧凑因果学生模型
   426|   415|    - 参数量减半、训练时间减少10倍，性能超越因果/非因果LFP SOTA
   427|   416|  - **Activation**: LFP decoding, REALM, retrospective distillation, causal BCI, local field potential, Mamba neural decoding, spike-free decoding
   428|   417|
   429|   418|### Approximate Macroscopic Dynamics of Spiking Neural Networks Based on Solutions to the Transport Equation
   430|   419|- [[approximate-macroscopic-dynamics-snn-transport]] - 通过输运方程解析推导SNN群体放电率波动涌现机制 (arXiv: 2605.14319v1)
   431|   420|    - 基于输运解而非传统均值场假设，捕获时变输入下的放电率波动
   432|   421|    - 揭示初始电压分布、时变输入与网络耦合的动态交互
   433|   422|  - **Activation**: macroscopic dynamics, transport equation, firing rate fluctuations, Fokker-Planck, mean field, integrate-and-fire
   434|   423|
   435|   424|
   436|   425|## 2026-05-17 - Systems Engineering Research (Cron Job)
   437|   426|
   438|   427|### Sheaves as a Means of Maintaining Consistency in Model-based Systems Engineering
   439|   428|- [[sheaf-consistency-mbse]] - 用层论(presheaf/sheaf condition)建模MBSE多视图一致性，仅检查pairwise interface compatibility即可证明全局一致性 (arXiv: 2605.08609)
   440|   429|    - Sheaf condition等价于pairwise overlap compatibility，全局一致性可简化为O(N²)检查
   441|   430|    - Limit-preserving functors派生属性继承一致性保证，Lean 4+Mathlib机器验证
   442|   431|    - 适用于CPS架构设计：电气/热/机械/软件多工程视图一致性管理
   443|   432|  - **Activation**: sheaf theory MBSE, model-based systems engineering consistency, multi-view architecture, CPS design consistency, category theory systems engineering, presheaf design spaces, 层论系统一致性
   444|   433|
   445|   434|## 2026-05-17 - Neuroscience Research (Cron Job)
   446|   435|
   447|   436|### Multiple mechanisms of rhythm switching in recurrent neural networks with adaptive time constants
   448|   437|- [[rhythm-switching-adaptive-time-constants-rnn]] - RNNs with neuron-specific learnable time constants exhibit multiple mechanisms for rhythm switching across frequency bands (arXiv: 2605.14388v1)
   449|   438|    - Time constant specialization creates multi-scale temporal basis in RNNs
   450|   439|    - Cross-frequency coupling emerges naturally from heterogeneous time constants
   451|   440|  - **Activation**: rhythm switching, adaptive time constants, RNN oscillations, multi-frequency, leaky integrator
   452|   441|
   453|   442|### Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale
   454|   443|- [[implicit-behavioral-decoding-spike-forecasts]] - Mamba forecaster trained on spike counts implicitly learns behaviorally-relevant representations (arXiv: 2605.12999v1)
   455|   444|    - Single Mamba model delivers both neural forecasts and behavioral readouts in one pass
   456|   445|    - Predicted rates enable better behavioral decoding than raw spikes
   457|   446|  - **Activation**: behavioral decoding, spike forecasting, Mamba, Neuropixels, closed-loop BCI
   458|   447|
   459|   448|
   460|   449|## 2026-05-17 - Information Science + Quantum (Cron Job)
   461|   450|
   462|   451|### Universal quantum resource distillation via composite generalised quantum Stein's lemma
   463|   452|- [[quantum-resource-distillation]] - 量子资源蒸馏/对称性分析的统一框架 (arXiv: 2605.15174)
   464|   453|    - 复合广义量子Stein引理建立统一的资源蒸馏速率
   465|   454|    - 所有量子资源理论的信息论量统一控制蒸馏效率
   466|   455|    - 适用于纠缠/魔态/相干性蒸馏协议设计
   467|   456|  - **Activation**: quantum resource distillation, quantum Stein's lemma, entanglement distillation, magic state distillation, 量子资源蒸馏
   468|   457|
   469|   458|### Non-Invertible Symmetries on Tensor-Product Hilbert Spaces and Quantum Cellular Automata
   470|   459|- [[quantum-cellular-automata-symmetries]] - 量子资源蒸馏/对称性分析的统一框架 (arXiv: 2605.15194)
   471|   460|    - 可实现的融合范畴对称性必须是弱积分的(FPdim=√n)
   472|   461|    - 量子元胞自动机(QCA)提供对称性细化分类机制
   473|   462|    - 非可逆对称性作为拓扑码逻辑算子的新视角
   474|   463|  - **Activation**: quantum cellular automata, non-invertible symmetry, fusion category, 量子元胞自动机, 非可逆对称性
   475|   464|
   476|   465|
   477|   466|## 2026-05-17 - Neuroscience Research (Cron Job)
   478|   467|
   479|   468|### REALM: Retrospective Encoder Alignment for LFP Modeling
   480|   469|- [[realm-lfp-retrospective-decoding]] - First LFP-only foundation model using retrospective distillation for causal real-time BCI decoding (arXiv: 2605.14867)
   481|   470|  - 核心要点: Bidirectional Mamba-2 teacher → causal Mamba-2 student via representation alignment + task supervision
   482|   471|  - 核心要点: 2× parameter reduction, 10× training speedup, deployable on Jetson Orin Nano / Raspberry Pi 5
   483|   472|  - **Activation**: LFP decoding, brain-computer interface, local field potentials, REALM, causal neural decoding, knowledge distillation BCI
   484|   473|
   485|   474|### Are cortical microcircuits optimized for information flux?
   486|   475|- [[cortical-microcircuit-information-flux-optimization]] - Simulation-based reverse engineering reveals how cortical core-periphery architecture enhances information flux via bias + recurrence resonance (arXiv: 2605.14680)
   487|   476|  - 核心要点: Embedded Core Model (ECM) shows peripheral neurons provide effective biases and stochastic fluctuations that shift core into higher-entropy regime
   488|   477|  - 核心要点: Self-organizing bias principle drives neurons toward maximal entropy, exceeding biological embedding performance
   489|   478|  - **Activation**: cortical microcircuit, information flux, reverse engineering neural networks, core-periphery architecture, recurrence resonance
   490|   479|
   491|   480|
   492|   481|
   493|   482|## 2026-05-17 - Information Science + Quantum Mechanics (Cron Job)
   494|   483|
   495|   484|### New approaches to almost i.i.d. information theory
   496|   485|- [[almost-iid-quantum-information]] - Methodology for analyzing almost i.i.d. quantum states via Wasserstein distance and k-body marginals (arXiv: 2605.15114)
   497|   486|  - Three hierarchical definitions: k-body marginals, quantum Wasserstein, Mazzola et al. notion
   498|   487|  - Strict separation proven with explicit counterexamples
   499|   488|  - **Activation**: almost iid quantum, quantum wasserstein distance, quantum information theory non-iid, 量子信息论
   500|   489|
   501|
## 2026-05-18 - Neuroscience + Quantum Mechanics (Cron Job - Evening)

### The Collapse of Unentangled Stoquastic Merlin-Arthur Proof Systems
- [[quantum-merlin-arthur-proof]] - Proves StoqMA(k)=StoqMA: unentanglement gives no additional power to stoquastic verification, separating entanglement from interference role via positive de Finetti theorem (arXiv: 2605.16249)
  - Separation of entanglement and interference in stoquastic Merlin-Arthur verification
  - Positive value-based de Finetti theorem for separately symmetric extensions
  - Spectral relaxation realized as one-witness stoquastic verifier
  - **Activation**: stoquastic, Merlin-Arthur, StoqMA, de Finetti theorem, entanglement detection, quantum verification

### Local Softmax and Global Weights in Non-Boolean Event Structures
- [[non-boolean-event-softmax]] - Shows single-valuedness on shared atoms collapses generalized softmax to admissible-weight polytope parametrization, with exotic weights reachable beyond classical/quantum bounds (arXiv: 2605.16248)
  - Local normalization does not imply global probability weight in non-Boolean event structures
  - Consistent connectedness / no-disturbance as critical collapsing constraint
  - Exotic weights exceeding quantum bounds reachable without no-disturbance
  - **Activation**: non-boolean event structures, generalized softmax, consistent connectedness, no-disturbance, contextuality, exotic weights
