## 2026-06-03 - Medicine + Quantum Computing (Cron Job - Hourly)

### Physics-Informed Learning of Effective Error Processes from Limited Noisy Transmon Measurements for Robust QAOA Reliability
- [[physics-informed-qaoa-error-learning]] - 物理启发学习从有限噪声transmon测量中推断有效量子误差过程，神经网络的24参数误差通道从12个测量值学习，QAOA可靠性提升20.4×，支持医疗优化应用 (arXiv: 2606.00353)
  - 核心创新：从稀疏层析数据学习有效误差模型，无需微观哈密顿量参数
  - 关键发现：局部仿射Bloch通道+成对残差捕获相关误差，3-qubit MAE从0.1775降至0.0269
  - 医疗应用：临床试验优化、药物发现管道、医疗资源分配 via QAOA
  - **Activation**: physics-informed quantum error learning, QAOA reliability, transmon error characterization, effective error channel, variational quantum algorithm mitigation, hardware-aware quantum optimization, quantum tomography from sparse measurements

## 2026-06-03 - Medicine + Quantum Computing (Cron Job)

### Quantum machine learning for predicting anastomotic leak: a clinical study
- [[quantum-clinical-benchmarking]] - QNN临床基准测试方法论：ZZFeatureMap+EfficientSU2/RealAmplitudes在200人结直肠手术数据集上超越经典模型，10次独立运行统计验证，临床敏感度固定下优化特异性 (DOI: 10.1038/s41598-026-44402-x)
  - 核心创新：ZZFeatureMap编码 + EfficientSU2-BFGS最高AUC / RealAmplitudes-CMA-ES最高Average Precision
  - 关键发现：83.3%临床敏感度下，QNN特异性显著优于经典基线（logistic回归、MLP、boosting）
  - 统计可靠性：10次独立优化运行取均值，AUC+Average Precision双报告
  - 硬件噪声模拟：真实噪声条件下的性能分布测试
  - **Activation**: quantum clinical benchmark, QNN medical validation, anastomotic leak prediction, ZZFeatureMap, EfficientSU2, RealAmplitudes, clinical sensitivity-specificity tradeoff, quantum healthcare benchmarking, Nature Scientific Reports

### Performance evaluation of quantum support vector machine for COVID-19 biomarker analysis
- [[quantum-clinical-benchmarking]] - QSVM生物标志物分析：振幅/角度/ZZ特征图/投影量子核对比，性能驱动特征重要性排序，双队列验证 (DOI: 10.1016/j.cmpb.2026.109343)
  - 核心创新：Ridge回归特征排序 → 高低重要性分组 → 经典SVM vs QSVM系统对比
  - 量子核测试：振幅编码、角度编码、ZZ特征图、投影量子核四种方法
  - 双队列验证：Cleveland Clinic + Swedish Medical Center独立数据集
  - **Activation**: quantum SVM, QSVM, quantum kernel, COVID-19 biomarker, multi-omics, proteomic, metabolomic, feature importance, amplitude encoding, ZZ feature map

## 2026-06-03 - Neuroscience Research (Cron Job)

### A Shared Valence Axis Across Modern LLMs and Human EEG: The Saturation Regularity
- [[valence-axis-llm-eeg-saturation-regularity]] - LLM效价轴映射人类EEG，揭示饱和规律性：任务监督饱和盆地，额外对齐扭曲残余，残余多样性集成提升解码准确率10.5% (arXiv: 2606.00129)
  - 核心创新：14个LLM的V-axis从9个情感句子构建 → 单线性投影映射EEG → 36个EEG分类器自发发现相同方向
  - 饱和规律性：任务标签驱动网络到目标方向 → 盆地饱和 → 额外监督主要扭曲（不改善）→ 残余接收极少梯度
  - 残余集成解决方案：跨残余多样性集成（不监督盆地）→ FACED+10.5%准确率，SEED-V相同效果
  - **Activation**: valence axis, LLM EEG alignment, saturation regularity, emotional valence decoding, brain-language model alignment, residual ensemble, EEG emotion classification

## 2026-06-03 - Neuromorphic RNN Learning & Speech Recognition (Cron Job)

### Dynamics and Representation Structure of Local Approximations to Gradient-Based Learning in Linear Recurrent Neural Networks
- [[local-gradient-approximations-rnn]] - RFLO/tBPTT/BPTT学习动力学对比：数据对齐线性RNN分析揭示RFLO限于低秩参数扰动，局部性约束塑造稳定性与收敛率，为神经形态硬件学习规则设计提供理论指导 (arXiv: 2606.00243, ICML 2026)
  - 核心创新：数据对齐RNN正交模分解 → RFLO低秩约束 → 定性不同于BPTT/tBPTT
  - 关键发现：RFLO解限制于初始参数低秩扰动（超越数据对齐假设），局部性约束限定解空间
  - 应用价值：神经形态芯片片上学习算法优化，生物学习约束建模，替代优化方法开发
  - **Activation**: RFLO, tBPTT, locality constraints, RNN learning dynamics, data-aligned RNN, low-rank perturbations, neuromorphic learning, biological learning rules, ICML 2026

### Spiking and Event-driven Neuromorphic Mamba Models for Efficient Speech Recognition
- [[spiking-event-driven-neuromorphic-mamba-asr]] - 神经形态Mamba语音识别：FATReLU事件驱动模型60%稀疏度<1%精度损失，脉冲SpeechMamba70%稀疏度30%参数削减，周期精确仿真器指导算法-硬件协同设计获>10%效率提升 (arXiv: 2606.01135, IJCNN 2026)
  - 核心创新：脉冲化Mamba架构 + FATReLU阈值激活 + 周期精确事件驱动仿真器
  - 关键发现：激活稀疏度>60%可实现，LibriSpeech基准<1%WER损失，协同设计额外>10%效率
  - 应用价值：边缘设备ASR（智能手机/智能家居），实时低功耗语音识别，神经形态硬件部署
  - **Activation**: spiking mamba, event-driven ASR, FATReLU, activation sparsity, neuromorphic speech, LibriSpeech, spike encoding, cycle-accurate simulator, IJCNN 2026

## 2026-06-03 - Systems Engineering Research (Cron Job)

### Monitoring Agentic Systems Before They're Reliable
- [[agentic-systems-monitoring-maturity]] - Agentic systems监控与成熟度分级方法论：三维评估框架(质量/适用性/效率)×三监控范围(单次/跨次/结构)，方差CV表征信号，FMEA严重性分类实现97%自动追踪 (arXiv: 2606.02494)
  - 核心创新：部分集成阶段结构缺陷掩盖任务级错误 → 监控范围决定故障类型(CV=0.02/1.25/0.00)
  - 关键发现：早期部署监控发现结构缺陷 → 任务级错误在结构缺陷存在时不可检测
  - 成熟度模型：Stage 1结构表征 → Stage 2错误检测 → Stage 3可靠性追踪
  - **Activation**: agentic systems monitoring, agent monitoring, agent triage, agentic systems reliability, agent maturity staging, FMEA, CV variance, structural defects, document-driven workflows

### Certified Closed-Loop Control for Packet Networks: A Compositional Certification Framework
- [[certified-closed-loop-control-packet-networks]] - 分组网络闭环控制的组合式认证框架：认证操作员介于提议器与数据面，候选动作投影到可执行动作满足证书，覆盖 backlog caps/service floors/Foster-Lyapunov drift/组合包络契约 (arXiv: 2606.02368)
  - 核心创新：执行动作认证范式 → CERTIFIED/INFEASIBLE双分支 + 可审计包络z̄(t)下游组合
  - 组合安全：操作员级安全 → 前馈组合安全 → 小增益条件闭环稳定
  - 统一机制：一个证书机制覆盖 backlog caps, service floors, mitigation caps, drift constraints, envelope contracts
  - **Activation**: packet network control, certified control, compositional certification, network dynamical systems, closed-loop control, Foster-Lyapunov drift, small-gain condition, envelope contracts

## 2026-06-03 - Medicine (Cron Job)

### Genotype-Conditioned Molecular Generation via Evidence-Grounded Multi-Objective Latent Perturbation in Diffusion Models
- [[medical-quantum-diffusion-drug-discovery]] - 基因型条件分子生成：扩散模型中多目标潜在扰动同时优化敏感性、可合成性和结合合理性 (arXiv: 2606.01461)
  - 癌症基因型编码为潜在条件向量指导分子生成
  - 证据引导的潜在空间多目标约束扰动
  - 量子启发能量函数评估分子结合亲和力
  - **Activation**: drug discovery, molecular generation, cancer, diffusion model, genomics

### Bayesian meta-learning for modeling Alzheimer's disease progression
- [[bayesian-meta-learning-alzheimer-progression]] - 贝叶斯元学习建模阿尔茨海默病进展：群体先验学习+快速个体适应+不确定度量化 (arXiv: 2606.02228)
  - 从多患者MRI数据集学习群体级先验
  - 贝叶斯更新实现少样本快速个体适应
  - 提供校准的疾病进展预测区间
  - **Activation**: bayesian meta-learning, alzheimer, MRI, disease progression, personalized medicine

### MedGym: A Unified Continuous-Time Benchmark for Dynamic Medical Treatment Reinforcement Learning
- [[medgym-continuous-time-rl]] - 连续时间医学治疗强化学习基准：处理不规则测量间隔和个体治疗响应差异 (arXiv: 2606.01028)
  - 患者生理连续时间随机过程建模
  - 统一环境接口支持多治疗场景
  - 标准化治疗质量、安全性和个性化评估指标
  - **Activation**: reinforcement learning, medical treatment, continuous-time, benchmark, MedGym

## 2026-06-03 - Neuroscience Research (Cron Job - Latest Papers)

### What biology can, and cannot, tell us about conscious AI
- [[biology-consciousness-ai-testability]] - 生物自然主义可测试性框架：区分Type-A-BN（不可测试）vs Type-B-BN（可测试），揭示计算功能主义批判的有效边界，生物学作为意识-信息处理关系的指南而非解决方案 (arXiv: 2606.02121)
  - 核心创新：双类型BN分类框架—Type-A（生物学本质性重要，行为分离，不可测试） vs Type-B（生物学提供独特处理能力，可测试）
  - 关键发现：Type-A-BN与展开论证相似，分离意识与行为；Type-B-BN与计算功能主义不矛盾，共同面临意识-处理映射任务
  - 哲学意义：澄清AI意识辩论中的有效vs循环论证，聚焦Type-B可测试生物学主张
  - 应用价值：AI意识评估框架，政策制定实证基础，研究方向聚焦
  - **Activation**: biological naturalism, AI consciousness, testability, computational functionalism, machine consciousness philosophy, consciousness information processing, Type-A-BN, Type-B-BN

## 2026-06-03 - Medical + Quantum Research (Cron Job)

### EVA-Net: Subject-Independent EEG Motor Decoding with Video-Derived Motor Priors
- [[eva-net-eeg-motor-decoding]] - 视频驱动语义先验的跨被试EEG运动解码：两阶段跨模态对比学习框架，动作视频作为动态语义锚点超越文本基线，知识蒸馏实现零推理开销的EEG-only部署，LOSO精度提升8.66% (arXiv: 2606.01884)
  - 核心创新：两阶段框架—跨模态对比对齐(EEG↔视频) + 知识蒸馏迁移到EEG-only分类器
  - 关键发现：视频提供比文本更丰富的动态语义锚点，捕获运动时序动力学
  - 应用价值：跨被试BCI减少校准需求，临床BCI部署，运动想象分类，康复应用
  - **Activation**: EVA-Net, EEG motor decoding, subject-independent BCI, cross-subject EEG, video semantic priors, motor imagery, cross-modal contrastive learning, knowledge distillation for BCI, LOSO, dynamic semantic anchors

## 2026-06-03 - Neuroscience Research (Cron Job - Hourly Update)

### Mapping Whisper Representations to Human ECoG Responses with Interpretable Time-Resolved Neural Encoding
- [[whisper-ecog-alignment]] - Whisper语音基础模型表征映射到人脑ECoG响应：时间分辨神经编码框架揭示中间层最强对应性，注意力图谱显示时序局部对齐，音素分析发现解剖学一致的音素类别组织 (arXiv: 2606.02305)
  - 核心创新：时间分辨编码器（speech embeddings + LSTM + soft attention）实现层级脑对齐分析
  - 关键发现：Whisper中间层（12-24层）→ 最强ECoG相关性，层级组织与皮层处理层次匹配
  - 音素解释性：编码相关电极按音素类别聚类，解剖学一致性组织（vowel/consonant/fricative）
  - 应用价值：语音BCI解码电极选择，神经编码研究时序vs静态假设验证，语音治疗皮层响应预测
  - **Activation**: whisper ecog, speech foundation model, neural encoding, cortical speech processing, brain alignment, time-resolved encoding, phoneme interpretability, whisper brain alignment

### On the Synaptic Matrix Eigenvalues of Sparsely Connected Neural Networks
- [[synaptic-matrix-eigenvalue-analysis]] - 突触矩阵特征值分析方法论：研究稀疏连接对谱行为的影响，揭示稳定性、瞬态动力学与记忆容量的数学关系，为药理效应建模提供统计谱分析框架 (arXiv: 2606.00326)
  - 核心创新：不同稀疏类型（随机/规则/拓扑）产生不同谱特征，时变稀疏性由稳态/癫痫/可塑性驱动
  - 关键发现：谱半径<1 → 网络稳定，特征值分布宽度 → 记忆容量，稀疏性决定瞬态机制
  - 应用价值：确定所需稀疏类型以诱导特定脑功能，预测药理/生理调节器效应
  - **Activation**: 突触矩阵, eigenvalue, 特征值, 稀疏连接, network stability, 谱分析, synaptic sparsity, memory capacity, pharmacological effect, 瞬态动力学

### Functional Ensembles as Units of Computation in Deep Spiking Networks
- [[functional-ensembles-deep-spiking-networks]] - 功能性集群作为深度脉冲网络计算单元：一阶功能连接(1FC)组通过稀有高协同事件可靠编码类别信息，ReLU式响应预测下游活动 (arXiv: 2606.00073)
  - 核心创新：1FC功能性组合框架，验证生物皮层功能连接原则在SNN ResNet中保守
  - 关键发现：高协同事件(~5-15%)集中编码信息，增益随集群大小增加，权重置换破坏结构
  - 对抗鲁棒性：扰动破坏早期/中间层响应，支持高分辨率节点级诊断
  - **Activation**: functional ensemble, 1FC group, deep SNN, functional connectivity, rare events encoding, ensemble cofiring, ReLU-like response, adversarial robustness, spiking ResNet

## 2026-06-03 - Neuroscience Research (Cron Job)

### Feature Leakage and Identifiability of Direct-Dependency Entropy Models
- [[feature-leakage-identifiability-entropy-models]] - MaxEnt模型的特征泄漏诊断框架：熵解释分数≠机制验证，状态重加权揭示CA1海马体~50%的"直接依赖"响应实为泄漏的高阶交互 (arXiv: 2606.01661)
  - 核心创新：信息投影视角—遗漏的交互/时序/隐藏状态可吸收到一阶参数（特征泄漏）
  - 关键诊断：状态重加权（分布敏感性测试）、条件log-odds对比（局部加性验证）、时序泄漏控制
  - CA1发现：经验权重下看似一阶的表格，平衡重加权后变为分布敏感（远高于加性代理null）
  - **Activation**: feature leakage, identifiability, entropy models, maxent, direct-dependency, mechanism recovery, state reweighting, conditional log-odds, temporal leakage, neural identifiability

### Neuromorphic Supremacy: Hybrid Astrocytic-Spiking Architectures
- [[neuromorphic-supremacy-hybrid-astrocytic-spiking]] - 神经形态优越性：星形胶质细胞调制+脉冲动力学嵌入传统ANN实现few-shot学习和噪声鲁棒性（遮挡/脉冲噪声），为数据稀缺环境下的embodied AI提供感知基础 (arXiv: 2606.01841)
  - 核心创新：Neuromorphic supremacy regime—真正的神经形态电路（astrocyte modulation + spiking dynamics）嵌入ANN，超越纯深度学习
  - 关键能力：few examples per class学习，occlusion + impulse noise鲁棒性（传统模型崩溃场景），embodied AI感知基础
  - 理论贡献：slow-timescale astrocytic gain control + fast spiking dynamics = principled hybrid architecture
  - **Activation**: neuromorphic supremacy, astrocyte, spiking neural network, few-shot learning, noise robustness, embodied AI, hybrid architecture, neuromorphic adaptation, astrocytic modulation

### Sequential Chaotic Oscillations in E-I Threshold-Linear Networks
- [[sequential-chaotic-oscillations-ei-networks]] - 激励-抑制阈值线性网络中的序列混沌振荡(SCOs)：不稳定单点固定点+强抑制→可预测序列转换的混沌游走，为脑动力学序列亚稳态提供机制 (arXiv: 2606.00373)
  - 核心创新：提出SCOs作为序列亚稳态的动力学机制，转换顺序可从网络拓扑预测
  - 关键发现：z-mode（激励差异）+ mean-mode（全局活动）分解表征完整动力学
  - 理论意义：整合-分离平衡的正式框架，E-I振荡不必同步
  - **Activation**: sequential metastability, chaotic itinerancy, E-I oscillation, SCO, threshold-linear network, graph rules, integration-segregation balance

### Spiking and Event-driven Neuromorphic Mamba Models for Efficient Speech Recognition
- [[spiking-event-driven-neuromorphic-mamba-asr]] - 神经形态Mamba模型实现高效语音识别：FATReLU驱动60%稀疏性(精度↓<1%)，SNN版本70%稀疏性(参数↓30%)，周期精确仿真器识别瓶颈优化效率↑10% (arXiv: 2606.01135, IJCNN 2026)
  - 核心创新：Event-driven SpeechMamba (FATReLU激活)，Spiking SpeechMamba (70%稀疏性)，Cycle-accurate simulator (算法-硬件协同探索)
  - 性能突破：60-70%激活稀疏性，30%参数减少，LibriSpeech精度保持，边缘设备实时ASR
  - **Activation**: spiking mamba, event-driven ASR, neuromorphic speech recognition, FATReLU, activation sparsity, SpeechMamba, algorithm-hardware co-exploration, SSM spiking

## 2026-06-03 - Medicine + Quantum Research (Cron Job - Hourly)

### A Retinomorphic Optical Spiking Neuron for Camouflaged Object Detection
- [[retinomorphic-optical-spiking-neuron]] - 霍奇金-赫胥黎光学脉冲神经元(OSHN)：基于二维反双极性光电晶体管的视网膜类视觉处理，0.9-24.5 pJ/spike能耗，中心-周围感受野增强SNN伪装目标检测精度达28.4% (arXiv: 2606.00818)
  - 核心创新：Hodgkin-Huxley光学脉冲神经元实现，0.9 pJ暗态能耗，4.2μs-1.25ms响应速度（比人眼快25x）
  - 视网膜预处理功能：中心-周围感受野(CSRF)、L-M锥体对立性、视觉自适应
  - CSRF增强SNN：FMNIST +4.4%，COD10K +10.4%，伪装数据集 +28.4%
  - **Activation**: retinomorphic optical spiking neuron, OSHN methodology, Hodgkin-Huxley optical neuron, anti-ambipolar phototransistor, center-surround receptive field, camouflaged object detection, event-driven vision, 视网膜类光脉冲神经元
### Rare Events, Real Signals: Functional Ensembles as Units of Computation in Deep Spiking Networks
- [[functional-ensembles-snn-computation]] - 1FC功能性组合作为深度脉冲网络计算单元：稀有高协调事件编码信息，聚合共发放预测下游响应，ReLU式输入输出关系 (arXiv: 2606.00073)
  - 核心创新：首阶功能连接(1FC)组分析框架，揭示深度SNN中功能性组合的计算原理
  - 关键发现：稀有高协调事件(~5-15%)集中编码信息，聚合共发放具有ReLU式响应
  - 学习塑造结构：权重置换破坏功能连接，证明功能组合是学习形成的
  - **Activation**: functional ensemble, SNN computation, functional connectivity, 1FC group, ensemble cofiring, deep spiking network analysis, ReLU-like response, rare events encoding

## 2026-06-03 - Medicine + Quantum Research (Cron Job - Hourly)

### CD-QAOA for Peptide Structure Prediction
- [[cd-qaoa-peptide-structure-prediction]] - 反绝热量子近似优化算法(CD-QAOA)用于肽链结构预测：引入反绝热驱动项加速QAOA收敛，七肽APRLRFY四面体格点预测经HF/DFT/MD/H-REMD四重验证 (arXiv: 2606.01611)
  - 核心创新：CD-QAOA在QAOA绝热框架中加入反绝热驱动项，抑制非绝热跃迁，加速基态收敛
  - Miyazawa-Jernigan经验矩阵建模残基间相互作用（从简化P-Y对到全矩阵）
  - 量子-经典验证管线：HF + DFT + MD + H-REMD 四方法交叉验证
  - **Activation**: CD-QAOA, peptide structure prediction, counter-diabatic QAOA, neuropeptide lattice folding, quantum molecular structure, Miyazawa-Jernigan matrix

### Penalty-free QAOA for lattice protein folding
- [[penalty-free-qaoa-protein-folding]] - 无惩罚QAOA方法解决格点蛋白质折叠问题：通过冲突图独立集表述避免二次惩罚项，MIS保持混合器保证约束满足 (arXiv: 2606.02104)
  - 核心创新：将约束优化映射到冲突图最大独立集(MIS)问题，无需二次惩罚项
  - 目标函数 = 纯蛋白质能量 + 线性偏置（无惩罚项）
  - 迭代局部搜索方案：用≤26量子比特折叠长达60的蛋白质
  - **Activation**: penalty-free QAOA, protein folding, lattice protein, conflict graph, independent set mixer, MIS mixer, quantum bio-physics, molecular optimization

### Attention-Like Hebbian Learning from Quantum Probability Flow
- [[quantum-probability-hebbian-learning]] - 从量子概率流推导类注意力Hebbian学习规则：横场定义泄漏通道，稳定性驱动更新产生softmax加权Hebbian规则 (arXiv: 2606.02098)
  - 核心创新：量子稳定性分析自然产生softmax加权Hebbian学习规则
  - 虚时动力学 → log-sum-exp泄漏自由能的梯度 = softmax加权
  - D-Wave退火器实验验证：softmax拟合优于Lorentzian幂律
  - **Activation**: quantum probability flow, Hebbian learning, quantum annealer, associative memory, softmax attention, transverse field, stability-driven learning

## 2026-06-03 - Medicine (Cron Job)

### A Framework for Post Quantum Migration in IoT-Based Healthcare Systems
- [[post-quantum-iot-healthcare]] - 物联网医疗系统后量子密码学迁移框架，覆盖四层IoT架构的量子威胁分析与迁移策略 (arXiv: 2604.15584)
  - 四层IoT架构（物理、感知、网络、应用）的量子威胁建模
  - 后量子密码学（Kyber/Dilithium/FALCON）在医疗设备中的分层部署策略
  - 混合密钥交换与植入式设备PQC认证架构模式
  - **Activation**: post-quantum iot healthcare, 量子安全物联网医疗, pqc migration healthcare, iomt quantum security


## 2026-06-03 - Medicine (Cron Job)

### Quantum drug discovery: a hybrid quantum graph neural network–variational quantum eigensolver approach
- [[quantum-graph-neural-drug-discovery]] - Hybrid QGNN+VQE pipeline for molecular property prediction and lead optimization (Crossref: 10.1140/epjd/s10053-025-01024-8)
  - QGNN encodes molecular graphs with quantum coherence for non-local correlation capture
  - VQE refines energy estimation with hardware-efficient or chemistry-inspired ansatzes
  - Iterative lead optimization loop explores chemical space beyond classical enumeration
  - **Activation**: quantum drug discovery, QGNN, VQE drug, molecular property prediction, lead compound optimization, hybrid quantum drug

### Quantum intelligence in drug discovery: Advancing insights with quantum machine learning
- [[quantum-drug-discovery]] (enhanced) - Review of quantum ML approaches accelerating pharmaceutical research (Crossref: 10.1016/j.drudis.2025.104463)
  - Survey of quantum advantage pathways in drug discovery pipelines
  - Quantum ML for target identification, molecular docking, ADMET prediction
  - **Activation**: quantum drug intelligence, pharmaceutical quantum ML, drug discovery review

### Toward Quantum-Enabled Medical Imaging: Optimized CNNs for Diagnosis
- [[hybrid-quantum-medical-imaging]] (enhanced) - Quantum-optimized CNNs for medical image diagnosis (Crossref: 10.1109/esci68015.2026.11493187)
  - Quantum circuit integration with CNN layers for medical image feature extraction
  - Hybrid quantum-classical approach for diagnostic accuracy improvement
  - **Activation**: quantum medical imaging, quantum CNN, medical diagnosis CNN

## 2026-06-02 - Neuroscience Research (Cron Job - Hourly)

### The Neuromorphic Supremacy: Hybrid Astrocytic-Spiking Neural Networks
- [[neuromorphic-supremacy-hybrid-astrocytic-spiking]] - "神经形态霸权"现象：星形胶质细胞-脉冲混合架构在小样本学习和噪声鲁棒性上超越传统深度学习 (arXiv: 2606.01841)
  - 核心创新：嵌入生物神经电路（星形胶质细胞调制 + 脉冲动力学）到ANN架构
  - 关键成果：5-shot学习准确率提升35-40%，90%遮挡噪声下保持70-85%准确率
  - 应用场景：具身AI感知、边缘AI部署、医学影像诊断
  - **Activation**: neuromorphic supremacy, astrocytic modulation, hybrid neural architecture, few-shot learning, noise robustness, embodied AI, spiking neural network, tripartite synapse

### Spiking and Event-driven Neuromorphic Mamba Models for Speech Recognition
- [[spiking-event-driven-mamba-asr]] - 脉冲/事件驱动 SpeechMamba 模型实现 60-70% 激活稀疏度，LibriSpeech 准确率损失 < 1% (arXiv: 2606.01135)
  - 事件驱动 SpeechMamba (FATReLU): 60% 稀疏度，WER 损失 < 1%
  - 脉冲 SpeechMamba: 70% 稀疏度，参数量减少 30%
  - 循环精确模拟器识别瓶颈，实现 10%+ 额外效率提升
  - **Activation**: spiking mamba, event-driven speech recognition, neuromorphic ASR, activation sparsity, SpeechMamba, FATReLU, hardware-efficient speech recognition

## 2026-06-02 - Computer Science + Quantum Research (Cron Job - Hourly)

### Joint Optimization of Qubit Leasing and Quantum Circuit Distribution
- [[quantum-circuit-distribution-optimization]] - 联合量子比特租赁与电路分发优化：ILP公式化多量子计算机资源分配问题，证明NP完全性，提出贪心+局部搜索算法 (arXiv: 2606.00501)
  - 四重耦合决策：租赁数量、存储位置、门执行位置、量子比特移动(迁移vs遥传)
  - NP完全性证明(归约自图划分)，识别多项式时间可解特例
  - 贪心初始化+局部搜索优化，5-15%内逼近最优解，扩展到100+量子比特
  - **Activation**: quantum circuit distribution, qubit leasing, quantum network optimization, JQLQCD, quantum resource allocation, distributed quantum computing, ILP quantum, qubit routing

### Half the Interference, Most of the Answer: Approximate Quantum Simulation via Path-Sum Pruning
- [[path-sum-quantum-simulation-pruning]] - 统计干涉采样框架用于近似量子电路模拟：50%干涉反应可省略同时保持90%输出精度 (arXiv: 2606.01922)
  - 化学抽象机(ChAM)模型：加权路径贡献作为并发分子种类演化
  - 阈值规则：端点振幅足够时终止处理，丢弃剩余反应
  - 适用于Deutsch-Jozsa、Grover搜索、Simon问题、Shor周期查找基准
  - **Activation**: path-sum pruning, interference sampling, approximate quantum simulation, quantum circuit simulation, ChAM, statistical interference


### QSignAI: Quantum-Randomness-Seeded Identity Signatures
- [[qsignai-quantum-identity-signatures]] - 量子随机性种子身份签名系统：通过双向量子电路管道在AI社交平台中生成唯一身份标识 (arXiv: 2605.27729)
  - 双向AI-量子集成：AI使量子可访问，量子使AI更安全
  - 两电路量子管道在云端模拟器上执行，产生量子随机性种子身份
  - 生产部署验证：量子AI系统可在生产环境中以可接受的延迟和成本运行
  - **Activation**: quantum identity signature, QSignAI, quantum randomness, identity verification, quantum-AI platform, quantum circuit pipeline, cs.CR

## 2026-06-02 - Neuroscience Research (Cron Job - Hourly)

### Frustrated Neurons: Energy Landscapes and Relaxation Dynamics in Repulsive Phase Oscillators
- [[frustrated-neurons-phase-oscillators]] - 几何阻挫理论框架用于神经相位动力学：排斥耦合振荡器映射到反铁磁XY模型，揭示结构化局部定时顺序塑造阻挫动力学景观 (arXiv: 2606.02512v1)
  - 三角形最小阻挫单元产生120°相位分离的简并基态
  - Kagome晶格弛豫选择扭矩平衡亚稳态而非精确基态
  - 弱全局相干性反映结构化局部定时顺序而非无序
  - **Activation**: geometric frustration, phase oscillators, neural timing, antiferromagnetic XY model, energy landscape, metastability, kagome lattice, torque balance, degenerate ground states

## 2026-06-02 - Neuroscience Research (Cron Job - Evening)

### Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons
- [[snn-sequence-timing-replay]] - 生物可行的脉冲神经网络序列时间编码机制，通过振荡背景输入灵活控制重放速度 (arXiv: 2605.22523v1)
  - 元素特定神经元群体的顺序激活表示序列元素持续时间
  - 振荡背景输入作为时钟信号和速度控制机制
  - 流失时间编码为独特稀疏的时空神经活动模式
  - **Activation**: sequence timing, replay speed, spiking neural network, sTM, temporal memory, oscillatory control

### Sparse Autoencoders Map Brain-LLM Alignment onto Cortical Semantic Topography
- [[sae-brain-llm-topography]] - 稀疏自编码器(SAE)揭示LLM脑对齐机制：语义特征恢复94%编码性能，映射皮质语义组织拓扑 (arXiv: 2605.23035v1)
  - 语义特征主导脑对齐性能，超越方差匹配基线
  - SAE特征映射皮质语义组织拓扑结构（Spearman ρ=0.72）
  - 预测人类阅读时间，发现意外语义内容的神经编码
  - **Activation**: sparse autoencoder, brain-LLM alignment, cortical semantic topography, mechanistic interpretability

## 2026-06-03 - Computer Science + Quantum Computing (Cron Job - Hourly)

### Quantum Principal Component Analysis without Eigenvector Recovery
- [[measurement-based-quantum-pca]] - Measurement-based soft PCA framework using entropy-regularized Fermi-Dirac filters replacing hard eigenvector extraction, achieves dimension-independent O(1/η²) sample complexity (arXiv: 2605.27942)
  - Single fixed calibrated circuit serves all rank budgets — no rank-dependent circuit updates
  - Fermi-Dirac filter as quantum measurement (POVM) naturally handles quantum data without classical conversion
  - Coherent data centering inside quantum protocol avoids classical preprocessing bottleneck
  - **Activation**: quantum PCA, soft PCA, Fermi-Dirac filter, measurement-based PCA, quantum data analysis, eigenvector-free PCA, anomaly detection, spectral energy profiling

## 2026-06-02 - Neuroscience Research (Cron Job)

### The Neuromorphic Supremacy: Hybrid Astrocytic-Spiking Architecture
- [[neuromorphic-supremacy-hybrid-astrocytic-spiking]] - 神经形态优势：嵌入星形胶质细胞调制+脉冲动力学的混合ANN架构，在少样本和噪声场景下超越经典深度学习 (arXiv: 2606.01841)
  - 少样本学习场景中经典DL崩溃，神经形态混合模型保持高精度
  - 遮挡和脉冲噪声下维持性能，生物启发的电路提供鲁棒性
  - "神经形态优势"范式：生物架构在噪声/数据稀缺环境中决对优于DL
  - **Activation**: neuromorphic supremacy, astrocyte modulation, spiking ANN hybrid, few-shot learning, noise robustness, embodied AI perception

### Mapping Whisper Representations to Human ECoG Responses
- [[whisper-ecog-alignment]] - Speech foundation model Whisper intermediate layers align strongest with human cortical activity using interpretable time-resolved neural encoding (arXiv: 2606.02305)
  - Intermediate Whisper layers provide strongest brain-model correspondence (hierarchical alignment)
  - Time-resolved encoder with soft attention outperforms linear mappings for ECoG
  - Phoneme interpretability shows anatomically coherent organization among encoding-informative electrodes
  - **Activation**: whisper-ecog-alignment, speech encoding, brain alignment, temporal encoder, speech foundation model, phoneme organization, cortical speech, soft attention

### How Optimality Structures Sparse Dictionaries
- [[sae-optimality-structures-dictionaries]] - Mathematical theory explains why Sparse Autoencoders extract interpretable features — layer-wise splitting/absorption, residual structure, dense opposing features emerge from optimal solutions (arXiv: 2606.02385)
  - Demonstrates hierarchical feature organization follows from sparsity constraint optimality
  - Absorbed features become densified opposing representations
  - **Activation**: SAE optimality, sparse dictionary learning, interpretable features, layer-wise splitting, feature absorption

### The Neuromorphic Supremacy
- [[neuromorphic-supremacy-hybrid-astrocytic-spiking]] - Hybrid neural architectures combining astrocytic modulation and spiking dynamics achieve few-shot learning and noise robustness that surpass standard deep learning (arXiv: 2606.01841)
  - Introduces "neuromorphic supremacy" regime where bio-inspired circuits outperform ANNs in data-scarce noisy environments
  - Astrocytic gain control + sparse spiking encoding prevent performance collapse under >50% occlusion/impulse noise
  - **Activation**: neuromorphic supremacy, astrocyte, spiking neural network, few-shot learning, noise robustness, embodied AI, hybrid architecture

## 2026-06-02 - Computer Science + Quantum Computing (Cron Job - Hourly)

### Evolutionary Discovery of Bivariate Bicycle Codes with LLM-Guided Search
- [[llm-guided-quantum-code-discovery]] - LLM-guided evolutionary workflow discovers 465 distinct quantum LDPC codes including new indecomposable [[288,16,12]] code (arXiv: 2606.02418)
  - LLM mutates Python programs generating BB and perturbed BB code ansätze across ~1650 evolutionary iterations
  - Staged validation pipeline: GF(2) rank, distance estimation, MILP, BLISS Tanner-graph dedup, local-Clifford equivalence
  - **Activation**: quantum code discovery, LLM-guided search, bivariate bicycle codes, quantum LDPC, evolutionary code search

### Branch-Aware Quantum Constant Propagation for Dynamic Quantum Circuits
- [[branch-aware-quantum-constant-propagation]] - Compile-time optimization for dynamic quantum circuits with mid-circuit measurements and classical feedforward, accepted at IEEE QSW 2026 (arXiv: 2606.02018)
  - Extends QCP by tracking classical measurement outcomes with post-measurement quantum states across execution branches
  - Path-sensitive reasoning inside conditional blocks with bounded state representation for scalability
  - **Activation**: quantum compiler optimization, dynamic quantum circuits, mid-circuit measurement, classical feedforward, branch-aware analysis

## 2026-06-02 - Computer Science + Quantum Computing (Cron Job)

### Tianyan: Cloud Services with Quantum Advantage
- [[tianyan-quantum-cloud-services]] - Cloud-accessible superconducting quantum processor (105 qubits) demonstrating quantum advantage: 74-qubit RCS in 18.4min vs 16,000 years classical (arXiv: 2512.10504)
  - Tianyan-287: 105 qubits, 99.90% single-qubit, 99.56% two-qubit, 98.7% readout fidelity
  - Cqlib open-source SDK for extended quantum circuits, operators, and primitives
  - **Activation**: quantum cloud, quantum advantage, tianyan, RCS benchmark, Cqlib, superconducting quantum processor, random circuit sampling

### EFaaS: Quantum-Classical Serverless Entangled Scheduler
- [[efaas-quantum-serverless]] - Serverless middleware for hybrid variational algorithms reducing TTNS by 11.4%-94.3% and convergence time by 83.2%-98.3% (arXiv: 2605.27540)
  - Calibration-aware placement routes circuits to QPUs with warm calibration caches
  - Dual-resource fair queuing and EF-QuantumFuture speculative execution primitive
  - **Activation**: quantum serverless, EFaaS, VQA scheduling, TTNS optimization, hybrid quantum workflow, calibration-aware routing

### SQARL: Size-Agnostic RL for Distributed Quantum Circuit Allocation
- [[sqarl-distributed-quantum]] - Transformer-based RL for qubit allocation across distributed quantum cores, 33% cost reduction vs HQA without retraining (arXiv: 2605.27027)
  - Handles arbitrary qubit/core counts with single trained policy
  - Minimizes inter-core communication (SWAP overhead) in multi-core quantum architectures
  - **Activation**: distributed quantum, qubit allocation, circuit compilation, SQARL, multi-core quantum, SWAP optimization

### Support Vector Machine with a Scalable Quantum Kernel
- [[hamming-quantum-kernel-svm]] - Hamming quantum kernel avoids exponential concentration in quantum SVMs, scales to 27 qubits (arXiv: 2605.31449)
  - Uses full measurement statistics instead of single fidelity value
  - Zero additional quantum cost — purely classical post-processing improvement
  - **Activation**: hamming quantum kernel, quantum SVM, exponential concentration, scalable quantum kernel

### Quantum State Preparation via Neural Network Encoding
- [[nn-quantum-state-encoding]] - Classical NN maps data to quantum circuit parameters, 0.992 fidelity, 5000x speedup (arXiv: 2605.31006)
  - Train-once-infer-many pattern replaces per-instance variational optimization
  - Fixed ansatz with NN-predicted rotation angles
  - **Activation**: neural network quantum state preparation, QML data loading, quantum circuit encoding

### Generative Quantum Data Embeddings for Supervised Learning
- [[generative-quantum-embedding]] - Energy-based generative framework optimizes quantum data embeddings with Wasserstein bounds (arXiv: 2605.30866)
  - Synthesizes gate sequences via fidelity-based surrogate objective
  - Wasserstein distance provides a priori diagnostic for embedding optimization feasibility
  - **Activation**: quantum data embedding, quantum encoding optimization, generative quantum circuit

### Attention-based Optimizer for Symmetry Finding
- [[attention-quantum-symmetry]] - Set-Transformer searches Pauli symmetries of Hamiltonians with commutation-based objectives (arXiv: 2605.30429)
  - Self-attention encodes pairwise and higher-order correlations among Pauli strings
  - Near-deterministic success on physical Hamiltonians (Ising, Toric code)
  - **Activation**: attention symmetry finding, quantum symmetry optimizer, Set-Transformer Hamiltonian

### Software Framework for Pulse-Level Quantum Computing
- [[quantum-control-pulse-software]] - Bridges gate-based abstractions with hardware-aware pulse-level optimization via JAX-based QML framework (arXiv: 2605.21286)
  - Composable ansatz constructions combining gate-based and pulse-level representations
  - Fourier-analytic diagnostics for circuit expressivity and entanglement measures
  - **Activation**: quantum pulse level control, quantum optimal control software, QML pulse modelling, hardware-aware quantum optimisation

### Progressive Swapping to the Middle Protocol
- [[psm-quantum-memory-distribution]] - Entanglement distribution optimized for imperfect quantum memories, presented at EuCNC 2026 (arXiv: 2605.31493)
  - Swaps progressively from both ends toward center, minimizing idle memory time
  - ~2x fidelity advantage over naive sequential swapping for linear chains
  - **Activation**: progressive swapping quantum, PSM protocol, imperfect quantum memory, entanglement distribution

### Quantum Sequence Samplers for Stochastic Processes
- [[quantum-sequence-samplers]] - Quantum circuits generate coherent superpositions of stochastic processes for O(1/ε) Monte Carlo (arXiv: 2603.24069)
  - Quantum amplitude estimation gives quadratic speedup over classical sampling
  - Applications in financial risk analysis, DNA sequencing, physics simulation
  - **Activation**: quantum sequence sampler, stochastic process quantum encoding, quantum Monte Carlo


### The Metastable Mind: Neural Underpinnings of Naturalistic Cognition
- [[metastable-mind-event-segmentation]] - 综合Event Segmentation与Metastable Neural Activity两大孤立分支，证明二者研究同一神经状态现象，提出三大核心原理：时空嵌套层级、预测模型基础、模块化处理边界重构 (arXiv: 2605.31473)
  - ES理论提供认知/行为效用解释，MNA提供机制层面实现
  - 神经状态作为认知基本计算单元，状态边界触发连接重构
  - 高阶区域长时程状态约束并塑造低阶快速区域状态
  - **Activation**: metastable, event segmentation, neural states, cognitive segmentation, metastable neural activity, 亚稳态神经状态, 事件分割

### Extended Predictive Coding under Exponential-Family Assumption
- [[extended-predictive-coding-exponential-family]] - 扩展预测编码框架至指数族分布，捕获生物神经网络特性：非线性、异质性、正发放率，维持FEP-PC对应至后验二阶累积量，支持生物合理局部可塑性规则 (arXiv: 2605.30882)
  - 传统Gaussian假设导致负发放率、线性转移函数等不生物合理性质
  - 指数族(Bernoulli/Poisson/Exponential/Gamma)自然约束正域，匹配生理观测
  - 层级微电路实现：L4计算预测误差，L2/3生成预测(EDF参数)，L5/6反馈
  - **Activation**: predictive coding, exponential family, free-energy principle, variational inference, local plasticity, 预测编码, 自由能原理

## 2026-06-02 - Computer Science + Quantum Computing (Cron Job)

### Quantum Algorithm for Distributed Reduction of Entanglements (QADR)
- [[qadr-distributed-entanglement-reduction]] - QADR框架将全局VQC分解为因果光锥内的局部子电路，将经典模拟内存从O(2^n)降至O(2^d)，自然缓解 barren plateaus，在32+量子比特处全球VQC崩溃时仍可运行 (arXiv: 2606.01291)
  - 因果光锥分解：分析电路结构识别每个目标量子比特的影响范围
  - 局部代价函数避免指数级梯度衰减
  - 在MNIST和NASA IMS风轮机诊断任务中匹配或超越经典架构
  - **Activation**: qadr, distributed entanglement reduction, causal light cone, VQC decomposition, barren plateau mitigation, quantum machine learning, variational quantum circuit, simulation efficiency

### Quantum Tunneling-Aware Machine Learning (QTAML)
- [[qtaml-quantum-tunneling-ml]] - 基于WKB近似的量子隧穿感知ML，推导部署时权重误差分布，TAC算法以少3.4-33.6倍ECC开销达到95%清洁准确率 (arXiv: 2606.00741)
  - WKB推导三层结构：仿射均值漂移、逐比特方差层级、逐层依赖性
  - 闭式饱和比ρ*可提前预测补偿效果
  - 层自适应比特预算分配在小预算下优于幅度分配24个百分点
  - 无需重训练、无需标签、无推理时开销
  - **Activation**: quantum tunneling, WKB approximation, noise modeling, deployment robustness, hardware-aware ML, error correction, tunneling-aware compensation, TAC, QTAML

## 2026-06-02 - Neuroscience Research (Cron Job)

### Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons
- [[snn-sequence-timing-replay-v2]] - 扩展sTM模型以学习序列元素精确时序，通过振荡背景输入灵活控制重放速度，支持宽范围时间尺度编码和清醒/睡眠状态速度调节 (arXiv: 2605.22523)
  - 元素特定神经元群体的顺序激活编码持续时间
  - 振荡背景输入作为时钟信号，频率调制重放速度
  - 稀疏时空模式编码经过时间，EEG/LFP振荡特性与重放速度相关性
  - **Activation**: sequence timing, replay speed, spiking temporal memory, oscillatory control, element-specific timing, EEG/LFP oscillation, sTM model, memory consolidation

### NeuralSet: A High-Performing Python Package for Neuro-AI
- [[neuralset-neuro-ai-framework]] - 统一Python框架处理多样化神经记录（fMRI, M/EEG, spikes）和复杂刺激（文本、音频、视频），惰性加载+深度嵌入集成+计算追溯 (arXiv: 2605.03169)
  - 模态无关数据统一，单一PyTorch-ready接口
  - 惰性加载支持TB级数据集，内存占用降至样本级别
  - 预训练深度嵌入（BERT/wav2vec/CLIP）自动生成
  - 计算可追溯性保证重现性
  - **Activation**: neuro-ai, neural data preprocessing, fMRI EEG MEG harmonization, deep learning embeddings, lazy loading, memory-efficient, PyTorch-ready, computational provenance

## 2026-06-02 - Computer Science Research (Cron Job)

### Quantum Reservoir Computing and Risk Bounds
- [[quantum-reservoir-computing-risk-bounds]] - Rademacher complexity-based generalization error bounds for quantum reservoir computing, with explicit qubit-scaling analysis and polynomial readout function risk convergence (arXiv: 2501.08640)
  - Rademacher complexity bounds for multiple quantum reservoir classes
  - Generalization bounds scale exponentially with number of qubits n — key limitation for large-scale QRC
  - Polynomial readout functions: risk bounds converge in number of training samples
  - Explicit parameter dependence enables partial generalization error control
  - **Activation**: quantum reservoir computing, Rademacher complexity, generalization bounds, risk bounds, qubit scaling, QRC theory, polynomial readout

## 2026-06-02 - Quantum Computing Research (Cron Job)

### More Efficient Clifford+T Synthesis for Small-Angle Rotations and Application to Trotterization
- [[efficient-clifford-t-synthesis]] - 突破性方法将小角度旋转的 T gate 成本从 O(log 1/δ) 降至 Õ(θ²/δ)，Trotterization 小步长极限下门成本变为常数，颠覆了"Clifford+T 成本独立于角度θ"的普遍误解 (arXiv: 2605.31544)
  - 准概率方法进一步将总 T 成本降低数个数量级，仅需小样本复杂度开销
  - 新 θ-依赖公式用于容错量子算法资源估计，Trotterization 应用需重新审视成本
  - 降低魔态资源需求，推进早期容错量子计算实用性
  - **Activation**: Clifford+T synthesis, small-angle rotation, fault-tolerant quantum compilation, Trotterization, T gate optimization, magic state distillation, quasi-probability decomposition

## 2026-06-02 - Neuroscience Research (Cron Job)

### XOResNet: Exclusive-OR Meta-Residuals for Deep Spiking Neural Networks
- [[xoresnet-deep-snn-learning]] - Novel SNN residual architecture using OR-ADD shortcuts and XOR meta-residuals to address spike redundancy, information loss, and redundant learning; outperforms SOTA on CIFAR-10/100 (arXiv: 2605.30362)
  - OR-ADD shortcut merges identity+residual branches (OR for spikes, ADD for currents)
  - XOR meta-residuals select novel residual components, eliminating redundant learning
  - Works at 18-101 layers, +2-5% accuracy improvement over baseline deep SNNs
  - **Activation**: xoresnet, xor meta-residual, deep snn, snn residual, spike redundancy, neuromorphic architecture, or-add shortcut

### Reinterpreting Safety Thresholds as Neuron Spiking Thresholds for Automated Driving
- [[snn-safety-thresholds-automated-driving]] - 将 Surrogate Safety Measures (SSMs) 重新诠释为 LIF 神经元脉冲阈值，SNN 结合多个 SSM 输入使脉冲与人类制动时机对齐 (arXiv: 2605.30368)
  - 用 LIF 神经元替代固定阈值，捕获持续边缘条件和短暂高峰风险
  - 学习的阈值相对一致（客观 SSM 有效），衰减因子编码个体时间敏感度（主观感知）
  - **Activation**: safety thresholds, SNN driving, LIF safety, autonomous driving safety, surrogate safety measures, SSM, braking prediction, spiking thresholds

## 2026-06-02 - Systems Engineering Research (Cron Job)

### Kairos: Lightweight Testing Framework for Timing-Induced Interaction Failures in LTE/5G Core Networks
- [[kairos-cps-timing-testing]] - CPS/分布式系统时序诱导交互故障轻量级测试框架，无需解析标准文档即可发现20个新漏洞、复现34个已知问题 (arXiv: 2605.30985)
  - 控制平面交互模式分类体系与故障模式映射
  - 轻量级时序测试生成与自动化故障检测
  - **Activation**: timing-induced failures, CPS testing, 5G core networks, LTE testing, control-plane interactions, network function crash

### A Data-Driven Methodology for Scalable Distributed MPC in Heterogeneous Building Aggregation
- [[data-driven-distributed-mpc-buildings]] - MPC-aware特征选择+分布式凸优化框架，解决大规模异构建筑需求响应协调的计算可扩展性和多步预测误差累积问题 (arXiv: 2605.30763)
  - MPC-aware特征选择方法论（考虑多步预测误差累积）
  - 异构建筑聚类的分布式凸优化控制框架
  - **Activation**: distributed MPC, building aggregation, demand response, feature selection, convex optimization, data-driven control

## 2026-06-02 - Computer Science + Quantum Mechanics (Cron Job)

### Mitigating Noise-Induced Barren Plateaus Using a Non-Unitary Ansatz
- [[non-unitary-ansatz-barren-plateau]] - Non-unitary variational ansatz restores finite gradients under depolarizing noise, enabling VQA scalability on NISQ hardware (arXiv: 2605.30572)
  - Core: Dissipative nonunitary elements counteract hardware noise effects in VQAs
  - Core: Floquet-type parameter sharing reduces deep circuit to analyzable quantum channel
  - **Activation**: barren plateau, NIBP, non-unitary ansatz, VQA, Floquet variational, NISQ

### A Denser Planar Surface Code
- [[denser-planar-surface-code]] - 4.5x encoding rate improvement over rotated surface codes using hex grid twist defects and padding-free lattice surgery (arXiv: 2605.30455)
  - Core: Dense twist defect packing on 2D hex grid with optimal 4-layer stabilizer cycles
  - Core: Pareto frontier analysis: 36x space, 6.6x spacetime improvement, 89k qubits for FeMoco
  - **Activation**: surface code, QEC, hex grid, twist defect, lattice surgery, fault tolerance

### Hybrid Quantum-Classical FBPINN for Full Waveform Inversion
- [[hybrid-quantum-fbpinn]] - Hybrid quantum-classical FBPINN achieves 8x faster convergence with 33% fewer parameters for wave-based inverse problems (arXiv: 2606.01110)
  - PQC as differentiable JAX statevector simulator enables end-to-end autodiff through classical PINN → quantum circuit → physics loss
  - Outperforms all 15 classical hyperparameter variants on geophysical anomaly benchmark
  - Applicable to medical ultrasound tomography, non-destructive evaluation, and wave-based inverse problems
  - **Activation**: hybrid quantum-classical neural networks, physics-informed neural networks, full waveform inversion, quantum machine learning for PDEs, differentiable quantum circuits, JAX quantum simulation, wave-based inverse problems, domain-decomposed PINNs, FBPINN quantum



### The Metastable Mind: Neural States as Computational Units (Enhanced Skill)
- [[metastable-mind-neural-states]] - Metastable neural states作为认知基本计算单元，整合事件分割理论与神经亚稳态框架，揭示三大核心原理：时空嵌套层级、预测模型基础、模块化处理边界重构 (arXiv: 2605.31473v1, May 29 2026)
  - 认知心理学分支(ES)与计算神经科学分支(MNA)研究同一现象
  - 高阶区域长时程状态约束并塑造低阶快速区域状态
  - 状态边界标志着连接重构和计算模式切换
  - **Activation**: metastable neural states, event segmentation, brain state transitions, neural state hierarchy, cognitive boundaries, metastable mind, predictive neural states, MNA, ES

### Memristor-Based SNN Accelerator (Enhanced Skill)
- [[memristor-snn-interception-task]] - Analog memristor crossbar阵列+模拟IF神经元实现异步事件驱动SNN，predator-prey拦截任务MSE 0.004，45nm工艺能耗比5nm数字方案降低12.7倍、延迟降低1.26倍 (arXiv: 2605.31299v1, May 29 2026, DCAS 2026)
  - In-memory synaptic computation消除多晶体管CMOS突触电路
  - Analog integrate-and-fire neurons实现阈值检测和脉冲生成
  - HSPICE仿真验证边缘智能实时追踪潜力