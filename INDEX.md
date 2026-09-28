## 2026-09-29 - Deep Learning Research (Cron Job)

### Persistent Negatives for Adversarial Black-Box On-Policy Distillation
- [[persistent-negatives-adversarial-opd]] - 黑盒OPD的持久负样本对抗蒸馏：用历史prompt匹配的师生对比锚定判别器负分布，消除moving-target奖励问题 (arXiv: 2609.30864)
  - 核心理论：判别器的Bayes最优奖励 = teacher→negative对数密度比；fresh negatives让该目标随每次policy更新漂移，persistent negatives锚定p_N并降低奖励估计MSE
  - 解耦设计：判别器看历史对比（稳定），GRPO保持on-policy（新鲜学生响应）——锚定奖励模型不打折on-policyness；2学生×3judge×4基准全面胜出
  - **Activation**: black-box distillation, adversarial discriminator reward, moving target, GRPO, reward estimation MSE, live-pool negatives

### User Model Extraction via Belief Self-Distillation
- [[belief-self-distillation-user-models]] - 信念自蒸馏：冻结LLM自任教师，从自然对话中无标注蒸馏隐式用户模型，统一read（解码）+write（写回干预）框架 (arXiv: 2609.31603)
  - 因果可写性判据：表征只有同时支持解码与注入才是真实内部状态——BSD干预强度显著超过等规模hidden-state steering（原始激活steering纠缠了其他特征）
  - 安全发现：refusal不只取决于请求，还取决于模型推断的用户意图——固定请求、只改写入的belief即可改变拒绝行为；独立训练的LLM收敛到共享用户表征几何
  - **Activation**: user model extraction, causal probing, activation steering, refusal intervention, cross-model geometry

### Learning to Stop without Learning to Stop
- [[self-supervised-confidence-efficiency]] - 置信度自监督微调让推理自动变短：仅在600题上训练模型预测自己推理轨迹中间点的答案置信度，损失中零长度/停止目标，推理时token减少达25%且准确率持平 (arXiv: 2609.31619)
  - 元认知信号→行为涌现：学会"知道自己已知道"后推理自然提前收敛；Gemma/Qwen/Nemotron/GPT-OSS全家族验证，效率与显式长度优化方法相当
  - 成分分析：置信度监督大体保留基模型的高层推理组合，不选择性压制特定行为（对比长度惩罚RL的策略扭曲）
  - **Activation**: reasoning efficiency, metacognitive supervision, confidence training, CoT length control, self-supervised fine-tuning

### Trust Guided Decision Transformer
- [[conformal-context-trust-decision-transformer]] - 信任先于价值引导：用模型自身滚动next-state预测误差+split conformal校准（held-out离线数据）过滤不可靠上下文后，冻结critic再在可信suffix中选动作 (arXiv: 2609.31586)
  - 上下文漂移自可见：长rollout中next-state预测误差升高且持续——无需外部不确定性模型即可检测条件上下文OOD
  - 顺序反转是关键：value-only选择会让critic挑中模型自己已标记不可靠的上下文生成的动作；TGDT在D4RL上减少持续高误差run、回报超vanilla DT/重置控制/value-only
  - **Activation**: decision transformer, context drift, conformal prediction, offline RL, trust-then-guide ordering

### HySTAR: Anchored Hypergraphs for Stable Credit Assignment
- [[anchored-hypergraph-credit-assignment]] - 锚定超图消除MARL结构目标漂移：固定重叠稀疏超图作值分解骨架+自适应时空编码器学特征，时序+结构相关性构造agent专属优势 (arXiv: 2609.31531)
  - 结构目标漂移命名：动态分组critic让agent→联盟→值分量的映射随交互演变而变——表征学习与目标分配纠缠导致两者都无法干净收敛
  - 骨架固定/特征自适应分离：SMAC最难设定+16.7%超MAPPO、+15.6%超HYGMA；GRF全6场景第一；Traffic Junction收敛epoch减少40.2%
  - **Activation**: multi-agent RL, credit assignment, hypergraph value decomposition, structural target drift, MAPPO

### Benchmarking Attention for Tabular Foundation Models
- [[tabular-attention-benchmark]] - 表格基础模型的注意力后端基准：行/列交替注意力的形状不对称（行长序列/列短序列/跨步内存布局）使最优后端因注意力类型×头维×硬件代际而异 (arXiv: 2609.31306)
  - 无全局赢家：FlashAttention代际匹配构建总体最佳，但列注意力长序列时被cuDNN反超（交叉点随头维变化）；SageAttention在>16k行的行注意力上胜出
  - 可复用方法论：形状不对称的核选择——按注意力类型分别基准、扫实际部署形状（交叉点是形状依赖的）、把跨步→连续拷贝成本计入测量、结果钉死硬件代际
  - **Activation**: TabPFN, tabular attention backend, FlashAttention vs cuDNN, SageAttention, 2D attention kernels

### How Far Can INRs Go? Cross-Domain INR-Based Semantic Segmentation
- [[hierinrseg-implicit-neural-segmentation]] - HierINRSeg层级INR分割：INR优势集中于低参数+弱增广域，语义结构分布于多层——层级聚合多层表征比堆参数有效 (arXiv: 2609.31573)
  - 域依赖而非普适优势：INR不随参数预算单调提升；预算小+增广弱时优势最大，U-Net从大容量+标准增广获益更多——给出模型选择决策表
  - 多层聚合收益：域内+5.6pp Dice、域外+8.2pp Dice超MetaSeg；探针显示互补语义结构跨INR层分布
  - **Activation**: INR segmentation, parameter-efficient medical imaging, hierarchical aggregation, cross-site MRI

### Self-Supervised Representation Learning: From Spectral Foundation Models to Auroral Emission Spectra
- [[spectral-window-transfer-pretraining]] - 谱窗口迁移分析：预训练模型的迁移质量由其训练谱窗口与目标谱段的重叠决定——红外预训练的SpectraFM在光学极光任务上低于未训练对照（负迁移） (arXiv: 2609.31206)
  - 无标注域内MAE配方：1D ViT自监督预训练223k谱→冻结表征恢复物理学家诊断用的发射线强度比（R²0.91 vs 0.77）→10%标签微调超scratch训练+0.159
  - 强制基线：未训练对照是检测负迁移的唯一手段；物理量探针（发射线比）验证预训练学到真实结构而非捷径
  - **Activation**: spectral foundation model, transfer window, negative transfer, MAE 1D ViT, label-efficient scientific ML

### Precision at Speed: Sample-Efficient Online MBRL for Hydraulic Excavator Control
- [[precision-gated-mbrl-excavator]] - 精度门控MBRL：概率动力学集成从零在硬件上在线学习+采样MPC，进度奖励以路径精度为前提（精度门控速度）——11.5吨挖掘机20分钟达到前人100-150分钟控制器水平 (arXiv: 2609.31025)
  - 精度门控防reward hacking：进度只在跟踪误差容差内才计入，杜绝抄近路换速度；40分钟后亚厘米级平均路径误差
  - 采样MPC+在线集成是硬件样本效率的实用组合：每步重规划吸收早期模型误差，无策略梯度，每秒交互都转化为规划改进
  - **Activation**: precision-gated reward, online MBRL, sampling MPC, hydraulic control, real robot learning

## 2026-09-28 - Neuroscience Research (Cron Job, late night)

### Common-Mode Collapse and Recovery in Direct Feedback Alignment
- [[dfa-common-mode-collapse]] - DFA 早训练平台的机制：输出误差的均值分量（共模）经固定随机反馈形成 rank-one 更新，把 tanh 单元推向饱和造成表征塌缩；类信息仍可解码但有效读出学习率降 ~35 倍 (arXiv: 2609.31589)
  - 精确均值-协方差分解（Sejnowski 1977）：ΔW = −η Cov(δ,h) − η δ̄h̄ᵀ，rank-one 项 dμᵢ/dt = −η sech²(μᵢ)(Bē)ᵢ(H+1) 驱动塌缩；随机反馈无系统性恢复项，只有读出学会类先验才结束驱动
  - 干预对比：中心化广播误差（对不衰减的 sign-error 信号唯一有效）> 先验偏置初始化 logit(π_c)（零成本加速 690→370 步）> 输入中心化+冻结偏置；Adam 靠逐坐标归一化绕过幅度瓶颈（塌缩更深但学习更快 117 vs 537 步）
  - **Activation**: direct feedback alignment, DFA, common mode, representation collapse, gate participation, mean-covariance decomposition, biologically plausible learning, credit assignment, tanh saturation, plateau stall

### Reciprocity can halve what a mechanical network can learn
- [[reciprocity-mechanical-network-learning-floor]] - Maxwell-Betti 互易性给物理学习网络设置先验可算的误差地板：p 个共享终端的可达响应块落在余维 p(p-1)/2 的子空间，全重叠时近半目标空间不可达，地板=目标共享块反对称部分的范数 (arXiv: 2609.04169)
  - 学习规则验证停在地板上：LM 二阶优化 142/144 跑到地板 0.1% 内；对比式耦合学习（bond-local 更新，无 Jacobian）22/24 同样到达——地板是可达集属性，与算法无关
  - 逃逸路线：每键的"楔形" z_b∧w_b（2-form）必须张成 Λ²R^p，最少 p(p-1)/2 条奇耦合键；pivoted QR 楔形矩阵选键（条件数 σ_min 报告质量，median 0.93 达最优），非互易代价 η(K)≥η(B) 由目标下界约束
  - **Activation**: reciprocity, Maxwell-Betti, mechanical network learning, physical learning, error floor, trainable metamaterial, odd coupling, wedge selection, sensor-actuator layout, robotic metamaterial

## 2026-09-28 - Neuroscience + Quantum (Cron Job, night batch)

### Oracle Distillation
- [[oracle-distillation-weak-query]] - FTQC 只能保护已知电路；对学习/传感任务中被查询的未知酉（oracle），用弱查询把 T_OD 次含噪查询蒸馏为一次高保真查询，且从不学习 oracle 标签 f (arXiv: 2609.31596)
  - 弱查询核心：在"对噪声局域不可区分"（Knill–Laflamme 可纠正）但保留与目标比特串重叠 η 的码字叠加态上查询——用响应强度换取纠错能力，再用 Π_{W≥w*} 阈值聚合器把 L 个弱响应相干聚合为完整响应
  - 阈值定理：凡量子优势为 N 多项式的 Boolean oracle 问题（Grover p*=5.1e-4、Simon p*=3.4e-2、k-forrelation 最高 3/4）在 per-qubit i.i.d. 去极化噪声低于常数阈值时优势保持——调和了此前 no-go（那些假设噪声跨所有 qubit 全局相关）
  - 近最优性：T_OD 上界 O(N^(H(α)+2α)) vs 下界 Ω̃(N^H(α))，暴露"蒸馏能力 vs 纠错能力"的根本张力；三级重复码先把任意对抗噪声归约为纯相位噪声
  - **Activation**: noisy oracle, oracle distillation, weak query, threshold theorem, quantum advantage under noise, fault-tolerant learning, query complexity, robust computational sensing, Knill-Laflamme
## 2026-09-28 - Neuroscience Research (Cron Job, evening batch 2)

### Structured Bayesian Modeling of Dynamic Receptive Fields in Salamander Retinal Ganglion Cells
- [[structured-bayesian-dynamic-receptive-fields]] - GMRF空间+AR(1)时间结构化贝叶斯感受野：SPDE网格离散化替代自由5,070维系数，INLA超参积分替代MCMC采样，155个RGC独立拟合后BIC功能聚类分出3个时间响应表型(85/32/38) (arXiv: 2609.30731)
  - 核心诊断：L1惩罚无法区分"空间连贯"与"空间碎片"两个等非零元数配置——GMRF条件均值恒等式让每个网格节点只被拉向邻居精度加权均值，机制性消灭孤立像素选择
  - 诚实报告：SPDE/AR(1)在log-score/TPR/系数误差全面胜过LASSO与elastic net，但LASSO的FPR控制更好(0.04-0.25 vs 0.04-0.49)；完全层次模型(Part B跨神经元共享μ_g,t)明确标注为"已规格化未拟合"
  - **Activation**: receptive field estimation, GMRF, SPDE, INLA, Poisson spike model, functional data clustering, B-spline FPCA, temporal-response phenotypes, LASSO fragmentation

## 2026-09-28 - Neuroscience + Quantum (Cron Job, evening batch)

### Modeling quantum neural network gradient with reinforcement learning
- [[rlq-grad-rl-qnn-optimizer]] - 经典 PPO 代理直接输出 QNN 参数梯度替代对酉 U(θ) 的微分，结构性地绕过 Jordan 代数型 barren plateau 方差衰减，成本随参数数 P 缩放而非希尔伯特空间维 2^n (arXiv: 2609.31066)
  - 状态 = [θ_t, 批均损失, 批均准确率, 上一步更新]；动作 = g_t∈R^P 解释为梯度估计；奖励 = acc + 1/(loss+ε)；量子参数由代理更新、经典头 W,b 走常规 Adam 反传
  - 诚实局限：深 barren plateau 下奖励同样集中（只保留计算优势无景观优势）；欠参数化时局部极小不可逃逸；2-design 电路下输入梯度 Cn/2^n 指数衰减仍传染给上游经典层
  - **Activation**: QNN training, barren plateau, surrogate gradient, PPO agent, quantum neural network optimizer, Jordan algebra variance bound

### Encryptability As a Coordinate Choice: Depth-One Homomorphic Federated Learning of Quantum Neural Networks
- [[encryptability-coordinate-choice-he-fedavg]] - "可加密性是坐标选择的产物"：单位四元数（旋量）图中 SU(2) 群合成严格双线性（系数∈{-1,0,+1}），加密旋转更新仅耗 1 层乘法深度、FedAvg 零深度，彻底消除 bootstrapping（Euler 角坐标下需 25,000+ ops/权重）(arXiv: 2609.30581)
  - 深度账本：旋转更新 1 层 / FedAvg 0 层 / 重归一化客户端明文 0 层；Pauli-OTP(离散 Clifford) + Quaternion-OTP(连续旋转) 编织成通用电路加密协议
  - Spin(n) 推广：几何积在 2^(n-1) 偶阶坐标上双线性，一切结论对 Spin(n) 参数化层逐字成立；156 比特硬件验证保真 0.9918 vs 0.99957，零效用税（ΔMSE=+9e-6, p=0.92）
  - **Activation**: homomorphic encryption, federated learning QNN, quaternion parameterization, SU(2) weights, depth ledger, Spin group rotors, encrypted aggregation

### Learning a non-linguistic code for inferred rules from reward
- [[reward-shaped-nonlinguistic-rule-codes]] - 失语症患者手势传规则的计算模型：说话者网络从示例学出 8 符号发明代码，执行者盲看符号完成三步组合变换；奖励通道把多规则压入少数标签（池化），梯度通道给每规则独立消息区域 (arXiv: 2609.31192)
  - 五大发现：代码可组合泛化到训练从未出现的三步变换；离散瓶颈代价小（感知在通道外学习）；奖励 vs 梯度塑造不同代码；纯奖励下可测量的退化解（消息坍缩）需课程/信息压力阻止；奖励驱动命名随规则数饱和且容量提升无效
  - 方法论要点：held-out 审计须枚举旋转/镜像/重着色对称——只有 held-out 三元组（300 中 100 个）真正测试组合性；能力度量应看消息与规则的互信息而非消息多样性
  - **Activation**: emergent communication, rule transmission, signalling game, compositionality, aphasia model, reward vs gradient channels, degenerate pooling equilibrium

## 2026-09-28 - Neuroscience + Quantum (Cron Job)

### URCHIN: A Horizontal Spiking Language Model for Data-Constrained Pretraining
- [[urchin-spiking-language-model]] - 单层 Dale 定律 E/I LIF 连接组的水平脉冲语言模型，一套权重双模部署（并行 SSM 训练 / 串行 RSNN 边缘推理），BabyLM 数据受限预训练 15-50x 算力节省 (arXiv: 2609.13899)
  - 128 LIF 神经元单水平层（无注意力无深度），token 通过多重传输环递归至不动点解析（训练 13 步/推理 24 步）
  - 并行/串行两种实现共享同一权重，基准分数一致到浮点下限 —— 原生脉冲，无需 ANN-to-SNN 转换
  - 脉冲核心仅 34K 参数（占 4.23M 总量 0.8%），其余为词嵌入+LM head
  - **Activation**: spiking language model, BabyLM, Dale's law, LIF, parallel scan SSM, RSNN, neuromorphic edge, PHCSSM

### Watching Quantum Models Think: Hilbert-Space Interpretability in Quantum Transformer Blocks
- [[hilbert-space-interpretability-qtb]] - 量子 Transformer 块的希尔伯特空间可解释性框架：追踪量子互信息/纠缠熵/参与率/层间保真度，在 IBM 硬件上直接观测量子模型"思考"过程 (arXiv: 2609.23016)
  - 四个精确基无关指标（MI 注意力图 ρ 查找 AUC 0.69、纠缠门消融准确率 100%→15%、MI 与准确率共演化 ρ=0.92、逐样本 MI 预测正确性 ROC AUC 0.84）
  - 全相干设计原则：无经典旁路，所有输入-输出关系经纠缠中介 —— 混合架构中经典残差吸干信息流使量子分析失效
  - 硬件就绪估计：Shot 计数的 Shannon MI（Miller-Madow 偏差修正）替代冯诺依曼 MI，序结构在噪声下保留
  - **Activation**: quantum interpretability, mutual information, entanglement, QTB, variational circuit, IBM Heron, confidence estimation

## 2026-09-28 - Neuroscience Research (Cron Job, afternoon batch)

### FlatClip: A Geometry-Aware Surface-Level Baseline for fMRI Representation Learning
- [[flatclip-surface-frozen-encoder-fmri]] - 皮层flatmap渲染+冻结SigLIP2图像编码器实现fMRI表面级表征：零fMRI预训练即超越ROI级基线，扰动对照阶梯证明解剖排布与预训练特征各自独立贡献 (arXiv: 2609.31204)
  - 三阶段管线：Pycortex确定性flatmap渲染（T=40帧RGB序列/或NSD的GLM响应图）→ 冻结SigLIP2全局特征（768d，时间均值池化；NSD用patch特征16×16自适应池化）→ 仅训练轻量MLP探针（768→256→256→C）
  - 核心结果：HCP性别分类82.06%（超BrainMASS等ROI级基线）、ADNI AD/CN 75.46%，低于最强体素级模型Omni-fMRI(92.86%)——确立表面级"中间地带"参考点；NSD COCO80视觉解码中超fMRI基础模型，且全皮层<视觉皮层<任务激活区单调提升（任务相关皮层覆盖选择的价值）
  - 可复用方法论：几何扰动阶梯（block-shuffle 76.1→半球交换75.0→半球内打乱70.9→像素置换72.9→相位随机化64.6→FC热图57.9→随机图48.9）+随机初始化编码器对照，将"空间组织有效"与"预训练特征有效"两个假设分离；三种colormap下真实排布一致优于置换（+7.3~+8.7 wF1）
  - **Activation**: fMRI flatmap, frozen image encoder, SigLIP2 brain transfer, surface-level representation, geometry perturbation controls, cortical rendering, NSD visual decoding, frozen probe protocol

### Grid-Cell Firing Fields Lack Local Sixfold Symmetry
- [[grid-field-microstructure-matched-null-harmonics]] - 单个网格细胞放电场无内禀六重对称：逐细胞匹配零模拟的谐波分析将全局晶格对称与局部场微结构解耦，负结果强约束CAN模型 (arXiv: 2609.31145)
  - 方法核心：对每个实验细胞构造匹配零模拟（复制spike数、occupancy、网格尺度λ、场宽σ̂、几何变换），仅操纵局部对称先验（圆形β=0 vs 六重von-Mises β>0），模拟数据流经与实验完全相同的预处理管线——彻底防御有限采样与预处理诱导的伪谐波
  - 谐波回归f6=P6/Σ(k=2..11)Pk在0.1λ–0.4λ窗口：Exp vs 圆形参考p=0.279（无六重提升），Exp vs 强加六重参考p=5×10⁻⁵且随β单调分离（分析灵敏度已校准）；谐波leave-one-out保护组合度量（P2主导分母）；Burak–Fiete CAN同样呈现全局周期/局部无六重的解离
  - 可复用模式：逐细胞匹配零推断、组合指标+逐项剔除防御、全局形变校正(ACF六峰椭圆拟合→仿射destretch)先于局部提问、晶格约束只做拒绝不做重定位、rectified von-Mises角调制注入旋钮、诚实负结果报告范式
  - **Activation**: grid field microstructure, sixfold harmonic power fraction, matched-null simulation, grid cell angular structure, Burak-Fiete CAN constraint, destretching lattice deformation, negative result methodology

## 2026-09-28 - Neuroscience + Quantum (Cron Job)

### Associative Memory for Quantum Entangled States
- [[entangled-hopfield-projector-memory]] - Hopfield memory storing entangled dimer-singlet states via truncated projector-sum Hamiltonians, O(N³/log N) capacity (arXiv: 2609.28726)
  - Truncated projector construction unifies dense/modern Hopfield (p-spin) models with quantum memory: truncation order = capacity/k-locality knob
  - Dimer-singlet (valence bond) memories store relational graph structures irreducible to any classical spin encoding; capacity scales N^(2p−1) vs classical N^(p−1)
  - Stability via double-commutator criterion + Anderson-like hybridization metric W; single-spin rotations never destabilize, bond rearrangements (plaquette flips) set the O(N³/log N) bound
  - **Activation**: entangled associative memory, quantum Hopfield, projector-sum Hamiltonian, dimer singlet covering, valence bond memory, quantum memory capacity, Mattis overlap

## 2026-09-28 - Neuroscience Research (Cron Job)

### Deviations from Global Coupling in Adaptive Oscillator Networks: Mean-Field Theory for Coupling-Weight Variance
- [[adaptive-coupling-variance-mean-field]] - 自适应网络耦合权重方差的二阶矩闭合均值场理论：5维ODE组预测结构化连接何时涌现 (arXiv: 2609.22597)
  - 首次推导自适应Kuramoto网络耦合权重方差V_A的闭式均值场方程：V̇_A=2μC_A−2γV_A，协方差分解为静态/涨落两部分（Ċ_Γ=−γC_Γ+μσ_Γ², Ċ_g=−(γ+2Δ)C_g+μσ_g²），频率异质性Δ以2Δ速率淬灭涨落驱动结构
  - 对称规则G=cos（Hebbian式）→ 强耦合同步核+双稳态（fold在Δ*=K(μ+γ)²/8μγ），偏离全局耦合始于分布尾部；反对称规则G=sin（时序式）→ 核内反称耦合、核失稳可致混沌，偏离始于分布中心，对OA动力学的偏离更强
  - V_A/Ā²与异质性Δ呈非线性非单调关系，在对称fold分岔点或反对称混沌区达到峰值——方程精确划分"全局耦合近似有效"与"复杂耦合模式形成"的参数域
  - **Activation**: adaptive coupling weight variance, second-order moment closure, adaptive Kuramoto mean field, STDP symmetry, Ott-Antonsen adaptive networks, structured connectivity, phase-oscillator plasticity

### Deep Learning in Infant Functional Neuroimaging: Challenges, Advances, and Future Directions
- [[infant-fmri-deep-learning-review]] - 婴儿fMRI深度学习综述：从群体描述到个体化发育预测的范式转变，表征选择决定生物学解释效力 (arXiv: 2609.26688)
  - 系统综述输入表征格式化（FC矩阵/潜在成分/功能梯度）、群体与个体化脑映射、纵向轨迹预测、鲁棒可解释评估与临床转化五大方向
  - 可复用模式：表征优先设计（先验证表征保留生物学构念再训练）、轨迹预测配方（纵向时间点训练预测未来连接组）、验证栈（跨站点泛化+生物学收敛+可解释性）
  - 未来瓶颈：更大纵向队列、发育适配模型设计、标准化评估、计算预测与生物机制整合
  - **Activation**: infant fMRI deep learning, infant functional connectome, developmental trajectory forecasting, individualized infant brain mapping, neurodevelopment risk prediction

## 2026-09-28 - Quantum Learning + Fault-Tolerant T Gates (Cron Job)

### Proper Agnostic Learning of Matrix Product States and Tree Tensor Networks
- [[proper-agnostic-learning-mps-ttn]] - 从任意混合态ρ学习真bond-D MPS/TTN：三阶段架构（相关子空间压缩目标、comparator-dual范数压缩、收缩式交叉环境动态规划），误差与链长n无关 (arXiv: 2609.30148)
  - 首次解决MPS的proper agnostic学习开放问题：输出严格属于bond-D类，截断improper结果会破坏保证
  - 关键创新：comparator-dual范数 ||x||_MPS(D)=sup|⟨ψ|x⟩| + 均匀收缩SVD谱（b_j=√(σ_j²−Δ_i)）实现伸缩预算，√D/(K+1)界与系统尺寸无关
  - 一组测量复用于所有D≤D_max的bond维度扫描（免额外测量的模型选择）
  - **Activation**: proper agnostic learning, MPS, tensor network learning, quantum tomography, bond dimension

### Syndrome Measurements Enable Deterministic Fault-Tolerant T Gates
- [[syndrome-mediated-deterministic-t-gates]] - 无需魔法态蒸馏：释放一个稳定子校验暴露额外逻辑量子比特，两次Pauli旋转+syndrome测量+Clifford前馈在任意d≥2稳定子码上实现确定性逻辑T门 (arXiv: 2609.29890)
  - 逻辑Pauli因子分解AB=iL共享非零syndrome，均衡因子化最优权重⌈(d+1)/2⌉；分支各1/2概率、前馈后同一逻辑门——确定性
  - 中间码D编码k+1量子比特，δ=min{d,μ(s),ν(A)}；纯码δ~d/2随距离增长，但LDPC类（界重校验）δ≤w封顶——结构性警告
  - 两个单容错构造：选择级联[[22,1,3]]（15个物理T门+阈值）与Golay传输校验G_B监控（拒绝后可恢复未知输入重试）
  - **Activation**: logical T gate, stabilizer codes, fault tolerance, syndrome measurement, non-Clifford, magic states
## 2026-09-28 - Neuroscience + Quantum Codes (Cron Job)

### Design Principles for Ultra-High-Rate Quantum Codes
- [[ultra-high-rate-quantum-codes]] - 超高码率量子码系统设计原则：配对分割构造+减半变换压缩码长，列权重为核心设计旋钮，p=0.1%下距离增益胜过重校验代价 (arXiv: 2609.30069)
  - 关键码：[[90,21,11]]、[[140,31,15]]、[[200,43,20]] 非CSS码（校验权重10），部分构造低至每逻辑量子位2个物理数据量子比特
  - 设计空间四参数（码率k/n、距离d、校验权重、码长n）的Pareto前沿导航：列权重增大→紧凑码长下更大距离，代价是更重的校验
  - **Activation**: ultra-high-rate quantum codes, quantum code design, encoding rate, pair-partition construction, column weight design, halving transformation, non-CSS codes, LDPC quantum codes

### Spike Sorting with VanillaSort
- [[vanillasort-spike-sorting]] - 从噪声自动生成标签学习锋电位检测与分选：可见性掩码+截断高斯目标+正包损失+SNR门控四件套，交叉拟合模板防止聚类自我确认 (arXiv: 2609.22322)
  - VanillaDet在Hybrid Janelia静态/漂移子集上检测精度分别超SimSort 2/3个百分点；VanillaCluster用HuiduRep嵌入+相对幅度特征GMM聚类，波形一致性约束精化分配
  - 可复用模式：噪声标签训练四件套（可见性掩码、截断目标、时间容差正包、条件SNR门控）适用于任何算法生成标签的检测器训练
  - **Activation**: spike sorting, spike detection, noisy labels, positive-bag loss, visibility-aware masking, template-guided clustering, waveform consistency, electrophysiology
### Emotions as Intrinsic Colored Noise in Biological Systems
- [[emotions-intrinsic-colored-noise]] - 情绪=内在色噪声的量化决策框架：选择概率可加分解 p=f+q，效用因子f（KL最小化+Luce规则）+吸引因子q（quarter law ±1/4），非零均值情绪偏置使噪声"有色" (arXiv: 2609.25970)
  - 八种网络动力学体制（Node/Focus/Limit-cycle/Chaotic组合）：强模仿效应→决策演化进入混沌；异质社会三类agent（长程记忆/短程记忆/超理性无情绪）
  - Ellsberg悖论自然消解：不确定彩票获q=-1/4负情绪、确定彩票q=+1/4，红球黑球两问偏好无矛盾——不依赖单一期望效用排序
  - **Activation**: emotions as colored noise, affective decision making, attraction factor, quarter law, biological networks, imitation chaos, Ellsberg paradox, affective AI, opinion dynamics

### Frequency Bursts in Adaptive Delay-Coupled Oscillators
- [[adaptive-delay-frequency-bursting]] - 自适应+延迟耦合振子的频率簇发：近同步状态被快速相位滑移打断，均值频率失谐被量子化为慢适应频率的整数倍 Ω₁−Ω₂=n·ε（n=每簇锋数=绕数） (arXiv: 2609.24671)
  - 快-慢几何机制：延迟使临界流形叶片数M随τ增长（多重共存的相位锁定态），簇发=稳定叶片慢爬行→fold边界→跳转到另一叶片的交替循环
  - 因果(STDP样)+Hebbian双适应规则产生反相位权重调制；用绕数（每慢周期整数累积相位）而非频率比来分类近同步态
  - **Activation**: adaptive delay-coupled oscillators, frequency bursting, quantized detuning, critical manifolds, fast-slow analysis, phase slips, winding number, neuronal plasticity delay, DDE-BifTool
## 2026-09-28 - Neuroscience + Quantum (Cron Job)

### Exploring the robustness of permutation entropy analysis to differentiate between closed-eyes and open-eyes resting states
- [[permutation-entropy-artifact-robust-eeg]] - 时间/空间置换熵在原始EEG上直接区分睁眼/闭眼静息态，无需去除眨眼伪影：配对t检验p<10⁻³，0.12秒数据即显著，空间熵单个64通道快照足够 (arXiv: 2609.22265)
  - 机制：序数模式编码数据点相对次序而非绝对值，眨眼表现为时间单调斜坡（PE对此天然鲁棒）；空间上眨眼梯度沿前后（vertical）方向，故SPE_V被破坏（1-2-3模式过表达）而横向SPE_H垂直于梯度不受影响
  - 稳健性边界：64→31→17通道缩减仍显著（欠采样负偏置在配对检验中抵消）；原始vs清洗后前额OP序列仅40%相同但概率分布几乎不变→PE不变；注意清洗仅施于EO记录，需用其他去除方法确认伪影无关性
  - **Activation**: permutation entropy, ordinal patterns, spatial permutation entropy, EEG artifact robustness, eyes open closed, raw EEG, resting state, real-time BCI

### Leg-Tied Tensor Network States: Entanglement Beyond Virtual Bonds
- [[leg-tied-tensor-network-letta]] - LETTA：MPS虚拟骨架+物理腿共享（tie graph）直接编码长程关联，DMRG式确定性优化（广义本征值问题H_i a = ε_i N_i a），2D J1-J2 Heisenberg 6×6上D=4参数量仅为MPS D=32的7%且能量更低 (arXiv: 2609.30101)
  - 结构：每个张量A[i]携带s_i及被绑邻居元组s_{P_i}；D=1时退化为correlator-product/Jastrow振幅网络而非乘积态；精确收缩代价由最大tie-boundary宽度决定（∏_{j∈F_i} d_j²），非PEPS式2D虚拟网络
  - 基准：2D阻挫J1-J2能隙密度峰值在J2/J1≈0.7与条纹反铁磁转变(~0.62)一致；3D横场Ising N_x×3×3对称无约束优化给出正确宇称基态；QR/LQ规范条件一般不给出N_i=I
  - **Activation**: LETTA, leg-tied tensor, physical leg ties, DMRG generalization, long-range correlation, frustrated Heisenberg, correlator product states, PEPS alternative, tie-boundary width

## 2026-09-28 - Neuroscience Research (Cron Job)

### Orbital Error Dynamics: Self-Organized Criticality, Ephemeral Parameter Resonance, and Non-Linear Biological Ontologies in Zero-Storage Neural Synthesis
- [[orbital-error-dynamics-zero-storage]] - 权重不存储(O(W))而是从24字节坐标种子Θ=(cx,cy,ζ)经Mandelbrot映射z²+c程序化合成(O(1))：32×32网格四象限质量比→权重，λz≈0临界边界冲浪+Cauchy重尾跳跃逃逸鞍点 (arXiv: 2609.30115)
  - 核心：模型即坐标——前向/反向后立即释放张量，恒定24字节内存与层数无关；轨道稳态损失L_orbital=[(N̄_esc−N*)/N*]²把逃逸计数拉向临界目标N*=22，象限方差正则Var(R₁..R₄)防退化；梯度停滞时门控注入Cauchy(0,0.10)重尾跳（无限方差跨势垒，对比Jin 2017高斯PGD）
  - 基准：Two-Moons 5种子 clean 77.67%±5.35 vs 无约束GD 85.67%（配对差CI含0=无显著退化）；偏移下71.33%确实更差；内部共振肩部X=(0.25,±0.18)为采样甜点；⚠️投机性论文（玩具基准+专利驱动），可复用的是零存储程序化合成模式
  - **Activation**: zero-storage, procedural weight synthesis, Mandelbrot, ephemeral parameters, edge of chaos, Lyapunov criticality, Cauchy heavy-tail jump, saddle escape, neuromorphic O(1) memory, optical co-processor

### Latent kinetic Ising models of neural spike trains
- [[latent-kinetic-ising-spike-trains]] - SpiKIsing双层生成模型：非对称kinetic Ising潜在网络动力学 + 连续时间历史依赖点过程发射层，变分平均场EM中点过程似然以单一"有效观测场"进入潜态更新 (arXiv: 2609.17213)
  - 核心解耦：传统分箱kinetic Ising将单神经元历史效应（不应期、恢复）错误归因于网络交互并丢弃bin内时序；SpiKIsing用潜二态Ising描述集体动力学（J_ij为有向有效耦合），发射层以 λ±、恢复核 ρ(δ)=δ/(δ+c_i)、绝对不应期吸收单细胞时间效应，且脉冲历史跨潜区间边界连续携带
  - 有效观测场 h_i^obs(t) = n·ln(λ+/λ−) + C − λ+A + λ−E 为激活/失活态对数似然比，保留kinetic Ising推断代数结构同时让连续精确脉冲时间直接贡献似然；E步含前向-后向反应项 R_i(t)（可省略为因果前向滤波），M步耦合梯度 ∂F/∂J_ij = Σ m_j(t−1)[m_i(t) − σ(η_i(t))]，发射率闭式更新，中心化参数化保证数值稳定
  - 结构化先验：Laplace L1稀疏先验（软阈值直接置零）+ 层级Dale扩展（潜身份 z_j、φ_j = σ(βS_j)，跨全部出边累积证据，允许有限概率符号违规）；LIF电导模型严重失配下连接支持ROC 0.88、40/40神经元E/I类型全部分类正确
  - **Activation**: spike train, effective connectivity, kinetic Ising, variational inference, point process emission, refractoriness, Dale principle, proximal gradient, MAP inference, neural population recording

### Stability and Wandering of Bumps in Neural Fields with Interneuron Subtypes
- [[neural-field-bumps-interneuron-subtypes]] - E/PV/SST三群体随机神经场bump吸引子：Heaviside界面分析将线性稳定性解耦为shift/scale两个3D特征值问题，弱噪声投影导出有效扩散系数，证明更宽SST连接既扩大稳定区又降低记忆扩散率 (arXiv: 2609.13074)
  - 建模：E(局部快速)+PV(局部perisomatic)+SST(宽dendritic)三耦合随机积分微分方程，指数核、von Mises空间相关噪声；典型抑制 motifs（PV自抑制、SST→PV、无SST自抑制）；平稳解由半宽(a_e,a_p,a_s)的分段阈值自洽条件确定（4种序关系情形）
  - 稳定性：Heaviside导数为界面δ函数 → 6维界面特征值问题按反射对称性分解为shift（奇，含平移零本征值=记忆编码中性模）与scale（偶）两个3D子空间；Λ_shift/Λ_scale比较判定失稳机制（漂移失稳 vs 膨胀/塌缩失稳，含Hopf边界）；抑制时间尺度τ_p/τ_s决定失稳类型，宽SST投影扩大并加深稳定区，微弱I/I连接有非单调大效应
  - 漫游：Fredholm可解性投影到共轭零向量（界面δ组合，β_p/β_s闭式权重比）得 ⟨Δ²⟩ = ε𝒟t，𝒟由各群体噪声协方差与界面斜率/时间常数加权和的平方给出；SST空间尺度 σ_es 1→10 单调降低𝒟 —— 抑制亚型架构直接量化决定行为级记忆精度
  - **Activation**: neural fields, bump attractor, working memory, interneuron subtypes, PV SST, linear stability, shift scale modes, Hopf bifurcation, noise-driven diffusion, wandering, Fredholm solvability

## 2026-09-27 - Neuroscience Research (Cron Job)

### The Cross-Substrate Access Assay: What an Indicator Test Must Declare to Travel from Brain to Language Model
- [[cross-substrate-access-assay]] - 意识指标测试跨基板迁移的五组件声明协议：predictors/fitting/sampling unit/estimand/decision rule (arXiv: 2609.22300)
  - 核心论点：n=1基板（人脑）上校准的测量无法区分现象与基板；迁移测量可在无迹象下改变其所测。信息论提供共同尺度（held-out交叉熵，nats/trial），使EEG微伏与LLM激活可并排审计
  - 实测量代价：继承模型对在12,000个graded合成数据上误报989次two-state（均因item异质性τ/ω）；扩展族+选择规则0误报、600混合数据599检出；但95%区间在6/12设置跌破0.90 inclusion floor（最低0.216）——仅审计错误率会放过此缺陷
  - LLM侧协议：自然文本包剂量k∈{0..8}线索、冻结剂量解码器、概念为采样单元（checkpoint确定性→变异置于刺激）；三项预注册预测（统计/bridge/causal）；pilot(layer 41, 16概念)三预测器均返回GRADED（−0.09~−0.12 nat/trial）
  - **Activation**: cross-substrate measurement, consciousness indicators, global neuronal workspace, ignition, model comparison, cross-entropy scoring, calibration battery, sampling unit, estimand, decision rule, LLM workspace directions

### Binding-Motivated Contextuality: A Cross-Domain Cyclic Test in Perception and Judgment
- [[frustrated-cycle-contextuality]] - 知觉绑定与判断上下文性共享同一H¹层上同调障碍：受挫环循环的跨域个体差异设计 (arXiv: 2609.23977)
  - 三种障碍度量辨析：CF（LP完备，CF=0 iff全局截面存在）≠ Čech类（仅充分，零类不能排除上下文性，Hardy witness）≠ 符号化margin V⋆（含CF全部信息+CF丢弃的阈下变异，确认性统计必用V⋆）
  - 关键设计陷阱：单一forced-choice使H¹对象退化（c钉在−1，随机反应最大化上下文性而确定性循环优势反而非上下文性——7/8已发表系统踩坑）；修复=每对两个锚定外部固定标准的独立二值判断
  - V⋆替代CF的结构性理由：CF在零处clamped，残差化留下不可消除依赖（假阳率渐近0.058且随N增长）；V⋆在双臂+对照上null statistic居中、率平坦；校准截止1.74-1.79而非1.645；对照臂需4-8×试验量
  - 可识别性极限（已证明）：加载0.6于双对照的trait可伪造ρ=0.209且与真实共享障碍观测等价——六分数上无任何统计量有超越自身size的power；报告污染份额26.5%而非检验
  - 回溯验证：scoping规则（受挫且循环即上下文，无论奇偶）postdict全部6个已发表CbD判定（Snow Queen是偶4环！）；8真实系统重算≤0.002吻合
  - **Activation**: perceptual binding, contextuality, sheaf cohomology, H1 obstruction, contextual fraction, Contextuality-by-Default, cyclic inequalities, Suppes-Zanotti, frustrated cycle, cross-domain correlation, preregistered design

## 2026-09-27 - Information Science + Quantum (Cron Job)

### All you need is the universal correlation detector
- [[universal-correlation-detector]] - Schur-Weyl universal symmetric states give state-agnostic first-order-optimal correlation tests; one detector + position-based decoding + convex splitting universalizes 6 communication tasks (arXiv: 2609.29954)
  - Fully universal cq test (zero state knowledge) P^(n)(a) = Σ|x^n⟩⟨x^n|⊗{ρ_Bx^n ≥ 2^na·σ^U,n_B}; semi-universal general-state test needs only marginal ρ_B — both match known-state Stein exponent I(A:B) via poly(n) domination ρ^⊗n ≤ (n+1)^{|X|(d+2)(d−1)/2}·σ^U
  - Six universal capacity-achieving codes: cq coding, wiretap, SK distillation, EA classical (simpler proof of compound C_EA), EA quantum Gel'fand-Pinsker (new), EA Marton inner bound L≥2 receivers (new); achievable-rate conditions identical in form, only the "need to know" list shrinks
  - **Activation**: universal correlation detection, state-agnostic testing, universal channel coding, compound channel, quantum Stein's lemma, Schur-Weyl duality, universal symmetric state, position-based decoding, convex splitting, Marton bound

## 2026-09-27 - Information Science + Quantum (Cron Job)

### High quantum local differential privacy breaks entanglement
- [[qldp-entanglement-breaking]] - 量子本地差分隐私与纠缠保持的不相容阈值：ε≤log(d/(d-1)) 强制信道纠缠破坏 (arXiv: 2609.13418)
  - 主定理：每个 ε-QLDP 信道在 ε ≤ log(d/(d−1)) 时必然纠缠破坏（qubit 阈值 log 2），常数最优；近似版 (ε,δ) 与某 EB 信道 diamond 距离 ≤ (d−1)δ
  - 组合定理：纠缠输入+全局测量下高隐私张量积信道 ε_comp = Σ log(γᵢ/βᵢ) ≈ 3nε；学习理论应用：EB 噪声使量子记忆协议可被单拷贝测量+经典内存模拟，纯度测试 T=Ω(2^{n/2})，全局私有信道 T=Ω(4^n)
  - 几何解释：最优阈值 = 转置-去极化信道 Choi 态穿越 Gurvits-Barnum 可分球（半径 1/√(ab(ab−1))）的位置；去极化混合 N_p 在 p ≤ 1/(ab−1) 时 EB
  - **Activation**: quantum local differential privacy, QLDP, entanglement-breaking, privacy threshold, private quantum learning, sample complexity lower bound, Gurvits-Barnum ball
## 2026-09-27 - Neuroscience Research Session 2 (Cron Job)

### Learning Dynamic Neural Evidence Representations for Time-Adaptive Brain-Computer Interfaces
- [[prototrigger-atdm-bci]] - Prototype-based EEG state encoder for RL-driven adaptive stopping: evidence anchors replace self-attention for cross-length comparable states (arXiv: 2609.22088)
  - LFE (temporal→spatial→refinement prototype matching) → stable local embeddings; GEA (24 learnable evidence anchors + PTES scorer) → decision-relevant temporal attention; all-steps supervised pretraining over every truncation length
  - SOTA ITR across SSVEP 163.06 / MI 25.32 / RFH-VEP 134.24 bits/min; online HoloLens2 HITL: 90.33% ACC @1.80s DT (ITR 67.51 vs 40.47 FW), zero-calibration, 2.1ms inference latency; reward-grid robust
  - State-quality metrics: CCD (cross-length drift) / PFR (prediction flip rate) / CM (classification margin) — reusable diagnostic triplet for variable-length RL encoders
  - **Activation**: ATDM, dynamic window BCI, prototype learning, evidence accumulation, dueling DQN stop policy, ITR optimization, variable-length EEG encoding, human-in-the-loop BCI

### Activation-Energy Pruning for Spiking Neural Networks: Unsupervised Personalization via Spike-Count Saliency
- [[fp-snn-activation-energy-pruning]] - E[w]=|w|·Σspikes is a literal metabolic cost in SNNs: one-shot label-free pruning matches source ACC to σ=0.5 and exceeds it at σ=0.8 on N-MNIST (arXiv: 2609.26167)
  - Negative result: SNIP/GraSP/magnitude pruning collapse to chance by σ=0.2–0.4 on SNNs — surrogate-gradient saliency is uninformative post-hoc on spike trains; random+BN becomes the honest baseline
  - Improvement-under-pruning: 98.4% vs 97.2% source at 80% sparsity (3-class personalization, cross-class interference removal, lottery-ticket specialization, Cohen's d≈2.1)
  - BN recalibration crossover at σ*≈0.4 (harmful below, essential above) — fixed LIF threshold amplifies activation drift, no continuous-activation analogue; scope rule: global ≤0.6, per-layer ≥0.7
  - **Activation**: SNN pruning, activation energy, spike-count saliency, unsupervised personalization, surrogate gradient failure, BatchNorm recalibration, decapitation diagnostic, neuromorphic deployment

## 2026-09-27 - Neuroscience Research (Cron Job)

### Disorder-promoted stability
- [[disorder-promoted-stability]] - Random parameter disorder enhances stability when Jacobian is non-Hermitian (2D+ nodal dynamics); overturns "heterogeneity hurts stability" from 1D reduced models (arXiv: 2609.25226)
  - Nonconvexity of min_b Λmax(J(b;A)) is necessary for heterogeneous optima; guaranteed by non-Hermitian J (any connected network of 2nd-order/phase-amplitude/E-I dynamics); convex only for measure-zero adjacency sets
  - Mechanism: heterogeneity induces mode mixing in Laplacian eigenbasis → eigenvector alignment (optimum requires ≥2 parallel eigenvectors); Gershgorin disc overlap lets eigenvalues escape leftward. Directed networks: b*_hom is a saddle → random N(0,1) perturbations improve stability (~25% of trials in SW nets, ~100% circulant)
  - Ecological: mutualistic Lotka-Volterra disorder GUARANTEED stability gain (up to 5×); competitive destabilized; prevalence grows with N and edge density — new route to May's complexity-stability paradox
  - **Activation**: disorder-promoted stability, non-Hermitian Jacobian, converse symmetry breaking, heterogeneity optimization, May complexity-stability paradox

### Matched-Input Estimates Differ in Sign Across Architectures: Auditing EEG Foundation Models on Motor Imagery
- [[matched-input-eeg-fm-audit]] - Validation-locked audit of LaBraM/CBraMod: every supervised comparator beats every FM config on BCI IV-2a; matched-input term flips sign across architectures so single-comparator decompositions are untrustworthy (arXiv: 2609.23924)
  - ShallowConvNet 0.6962 vs CBraMod fine-tuned 0.4796 (4-class, n=9, cross-session); FM deficit does NOT reproduce on 2-class BNCI2014-004 (0.8085 vs 0.8458 — competitive)
  - Matched-input term (narrow−broad): ATCNet −0.078 vs EEG Conformer +0.088 — opposite signs; report raw diffs across ≥3 architectures, never a single "pipeline share" percentage
  - Pretrained-vs-random-init robust (+0.13 acc across 3 reseeds); raw FM logits overconfident (T=3.5–9.5) but one validation-fitted temperature restores ECE to supervised range — calibration ≠ discrimination
  - **Activation**: EEG foundation model audit, matched-input control, validation-locked protocol, BCI benchmark leakage, temperature scaling

## 2026-09-27 - Information Science + Quantum Mechanics (Cron Job)

### Learning and Interpreting Policies for Simultaneous Entanglement Requests in Quantum Networks
- [[dqn-mpnn-entanglement-scheduling]] - Double DQN + MPNN + curriculum training for scheduling simultaneous entanglement requests in quantum networks, with LLM trajectory-to-heuristic policy distillation (arXiv: 2609.30157)
  - Curricular noise training: 11 phases over γ∈[1.5,5.8] with expert-seeded replay buffers (25% expert / 75% online); first failure at 51-71% lower link activation probability vs heuristics
  - Four-component reward shaping: subgraph-edit-distance progress reward, betweenness-centrality bottleneck reward, |E_k|^κ complexity-weighted placement, step penalty
  - LLM policy distillation: Gemini 3.1 Pro infers natural-language heuristic from DQN (state, action) examples, matching RL performance — interpretable policies without retraining
  - Behavior profiling triplet: Holding Time (patience) / Bridge Span (link necessity) / Hub Anchor Bias (peripheral preference)
  - **Activation**: quantum network scheduling, entanglement requests, DQN, MPNN, curriculum training, LLM policy distillation, subgraph edit distance, link activation probability
## 2026-09-27 - Information Science Session 4 (Cron Job)

### How Not to Build Microcrypt
- [[np-aided-shadow-tomography-microcrypt]] - NP-aided shadow tomography learns computable PRS/PRU; computable+samplable OWSGs imply classical one-way functions (arXiv: 2609.30253)
  - Theorem 1.1: any computable pure-state OWSG family (amplitudes/phases classically evaluable given key) is invertible in BQP^NP — two-stage pipeline: computational-basis max-likelihood key search, then self-referential controlled-SWAP interference (q=p balances branch magnitudes exactly; works for spiky states where uniform reference fails)
  - Theorem 1.2: computable+samplable OWSGs imply classical OWFs — kills Hamiltonian Phase States (TQC 2025) and Morimae-Xagawa IQP group actions as Microcrypt candidates
  - Theorem 1.3 (CMC attack): Clifford-monomial-Clifford unitaries C2 M C1 learnable in BQP^NP via Bell-displacement test — allowed displacement set |R|<=D/2 vs Haar-uniform; Clifford layers only relabel Bell states (CPC^T is Pauli); single NP query with witnesses x_i
  - Fidelity bridge: 1-|<phi|psi>|^2 <= 100(t+g)^2 (Hellinger of controlled-SWAP outcome distributions + reference mismatch)
  - Survivors (Table 4, legitimate research directions): full PRSS walks, long Kac walks, third blocked LRFC, glued LRFC, phased-permutation Hamiltonians, hidden-basis dynamics, ABGL composition — common theme: Clifford-in-the-middle or deep mixing breaks computability
  - **Activation**: microcrypt, PRS, PRU, OWSG, NP oracle, shadow tomography, one-way functions, pseudorandom states, Hamiltonian phase states, CMC unitaries

### Deep thermalization and Hilbert space ergodicity (入库)
- arXiv: 2609.30248 — Review: state distributions become "maximally random" in precise sense; unifying framework via quantum information theory + maximum entropy explains ergodicity forms under physical constraints; irreversible statistical mechanics from reversible unitary dynamics; applications to benchmarking/tomography

### Moreau-Yosida approximation of Entanglement of Formation (入库)
- arXiv: 2609.30246 — E^lambda_F family (Moreau envelope of EoF) monotonically increases to EoF as lambda->0; computable upper bounds on E_F - E^lambda_F; uniform convergence rates on bounded rank/energy marginals; conditions for exact coincidence
## 2026-09-27 - Neuroscience Research (Cron Job, Session 3)

### Neural noise enables accurate internal simulation of rare events
- [[noise-assisted-rare-event-simulation]] - Moderate OU noise on BCPNN unit supports repairs both deterministic-replay failure modes (greedy over-representation / low-prior-veto under-representation) with an inverted-U stochastic-resonance signature and parameter-tolerance broadening (arXiv: 2609.18033)
  - Two-stage decomposition: internal-model failure splits into learning-stage sampling error vs expression-stage dynamics; this work isolates the circuit-level stage — replay fidelity depends on how learned structure is sampled, not just what is learned
  - Failure modes from one support equation: over-representation = recurrent term run greedily (skips common alternatives, rare over-represented by elimination); under-representation = low prior beta_j vetoes the strongest common-to-rare weight (normalized Hebbian rule w_ij = log(P_ij/(p_i p_j)) registers even single co-occurrence, but bias term pulls support below common competitor)
  - Inverted-U optimum sigma* approx 24 (occurrence deviation 0.0143 at 20% rarity): Level-2 transition-class KL minimized in the same moderate-noise band — conditional occurrence is the stricter test, cannot be met by prior-gain tuning alone
  - Tolerance broadening: no parameter setting is accurate at both levels without noise; moderate sigma opens a 2D band of accurate settings across tau_p, g_beta, g_bayesian, g_I and all three rarities (20%/10%/6.7%) — noise buys robustness, not just accuracy
  - Neuromodulator mapping: DA -> (prior gain g_beta + plasticity timescale tau_p), ACh -> encode/replay switch (suppresses recurrent evidence, raises afferent gain, relieves adaptation), NE/arousal -> sigma; PD trajectory: DA+ ACh fall while sigma rises, all pushing internal simulation to over-represent rare events — matches patient prior-use deficits and scopolamine data
  - **Activation**: neural noise, internal simulation, rare events, bcpnn, stochastic resonance, attractor replay, occurrence fidelity, hebbian-bayesian, predictive processing, parkinsons noise band, 1/f aperiodic slope

### A neural-astrocyte architecture implements a hybrid automaton for evidence accumulation
- [[neural-astrocyte-hybrid-automaton-evidence]] - Slow astrocytic RNN (trial-scale A2C+GAE) modulates fast neuronal RNN (ms-scale DMS task) via low-rank Hadamard gain W_eff = J_xx odot (11T + H_px diag(pi) H_px^T); context switch = cascade of two bifurcations (arXiv: 2609.16217)
  - Hybrid automaton in continuous dynamics: action level sets of the readout; reward omission (RPE) annihilates the active limit-cycle attractor, state traverses a flat low-velocity region, crossing the level-set boundary decodes a new action and triggers a second vector-field reconfiguration — integrate-to-bound generalized to bifurcation-relocated multidimensional bounds
  - Stickiness is entropy-mediated: higher environmental entropy (p* 0.90 -> 0.48) flattens the unrewarded vector field near the annihilated attractor, requiring more unrewarded trials to cross the decision boundary; residual variability at zero internal noise comes from reward stochasticity placing trajectories in ambiguous level-set interface zones
  - Astrocytic tiling suffices: lattice topology (k-nearest-neighbor banded recurrence, 1:3 astrocyte-to-neuron) matches dense connectivity in training rate and asymptotic regret; modulation robust up to ~90% sparsity — global integration from local gap-junction-like communication
  - Trainability result: monolithic same-size RNN with dual readout fails — fast policy-gradient updates overwrite slow credit assignment; hierarchical timescale decoupling (A-RNN evidence integration -> stable modulation of N-RNN) is what makes the problem learnable
  - A-RNN sees only its own action-reward history (pi_k, r_k), no oracle context; trained on sparse one-bit reward with 500-trial reward-magnitude curriculum; evaluation across 100 independently trained models
  - **Activation**: neural-astrocyte networks, hybrid automaton, evidence accumulation, contextual inference, bifurcation analysis, fast-slow dynamics, astrocyte tiling, low-rank gain modulation, sticky policy, latent rule inference

## 2026-09-27 - Systems Engineering Research (Cron Job)

### Requirement-Bound Verified Commissioning: Frozen 4B Local Model as Candidate Generator under External Acceptance Layer
- [[requirement-bound-verified-commissioning]] - LLM 仅做候选生成，确定性 entailment gate 独占 release authority，sealed grammar + 预注册统计准则 (arXiv: 2609.30219)
  - 三层信任分离：deterministic parser → frozen 4B LLM(仅提案) → external entailment gate(密封语法V1裁决)，模型置信度永不进入发布决策；abstention 是合法一等结果
  - 实测证据：模型在22个不可回答任务上伪造21个 ready plan(95.5% fabrication)全部被 gate 拒绝；sealed run 0/83 false release，Clopper-Pearson 单侧95%上界0.0354<5%；无 gate 对照组50%错误交付
  - Textual trust boundary：事实不被需求文本独立约束时 gate 只能信任用户答案(text-open 层 39.2% 错误答案被放行)；文本约束存在时 0/65 错误答案通过
  - 诚实报告 post-seal 失败：146计划中1次false release(语法V1 anaphor失效)触发 kill rule 并透明披露，不掩盖
  - **Activation**: llm acceptance layer, entailment gate, release authority separation, sealed grammar, commissioning, safety-critical llm, clopper-pearson, preregistration, candidate generator

### Developing a Unified Verification and Validation Activity Standard at JPL
- [[unified-vv-activity-schema-jpl]] - JPL 关系型 V&V 活动 schema：5种方法 item type 共享核心属性集，双向关系连接需求/活动/场所/证据，SysML 平台无关形式化 (arXiv: 2609.28600)
  - Relationship-based schema：Verified By / Executed In 等显式类型化双向关系 + Venue 独立 item type，支撑变更传播、rollup 状态、设施利用率分析
  - Common-core inheritance：Base MVP 块(标识/状态/调度/证据) + Test/Analysis/Inspection/Demonstration/Review-of-Design 子类——单一泛化 VA 类型已被实践证伪
  - HCDP 工作坊(29名实践者, Double Diamond)：85%认可 MVP 全任务可用；两级 pick list(核心标准+项目可扩展)平衡标准化与定制
  - Institutional flywheel：共享信息架构使一个项目的自动化可零修改部署到所有项目(inner-source)，双向可追溯性消除覆盖缺口/冗余
  - **Activation**: vv schema, requirements traceability, digital thread, sysml information model, test management, requirements management platform, relationship-based schema, hcd workshop
## 2026-09-27 - Information Science Session 3 (Cron Job)

### Quantum Channel Stein Theorem beyond Definite Causal Order
- [[channel-stein-theorem-causal-order]] - Parallel/adaptive/indefinite-causal-order testers share the same Stein rate D^inf(N||M); adaptivity & quantum switch give zero asymptotic advantage (arXiv: 2609.30268)
  - Theorem 2.4: for any finite-dim memoryless CPTP pair, lim (1/n) D_H^{eps,S}(N^otimes n || M^otimes n) = D^inf(N||M) for all S in {par, ada, gen}; strong converse a <= e^{-cn} at every r > D^inf holds even for general (ICO-permitting) testers
  - Exact strong-converse exponent E^sc(r) = sup_{p>1} (p-1)/p (r - Dtilde_p^inf) via regularized sandwiched Renyi endpoint continuity (Theorem 5.1): lim_{p downarrow 1} Dtilde_p^inf = D^inf — continuity holds only AFTER regularization
  - Reusable machinery: positive-slack SDP duality (testing score Delta_n(lambda) = min normalized positive Choi slack), fixed-marginal de Finetti reduction with polynomial loss g_n (transfers parallel bounds to ALL general testers: a <= lambda b + g_n Delta_n(lambda)), three-amplitude comparison closing the endpoint
  - One-shot duality: parallel testers dual to all-channel Choi smoothing set K_all; general testers dual to positive AFFINE hull K_aff (affine constraints impose no slot-separability)
  - **Activation**: channel discrimination, stein exponent, indefinite causal order, quantum switch no-advantage, regularized channel relative entropy, sandwiched renyi endpoint, strong converse exponent, de finetti reduction, smooth max-relative entropy AEP

## 2026-09-27 - Neuroscience Research (Cron Job)

### Transfer Dynamics and Spectral Cascades in Graph-Coupled Kuramoto Networks
- [[spectral-transfer-cascade-kuramoto]] - Graph-spectral transfer matrix + spectral flux reveal cascades hidden beneath stationary synchronisation (arXiv: 2609.28432)
  - Transfer matrix T_{m->k}(t) = 2 a_k f_{m->k}(t): reconstruct mode-m signal, propagate through nonlinear Kuramoto coupling only, project back onto Laplacian eigenbasis — a directed interaction network over graph Fourier modes
  - Spectral flux Pi(t,K0) measures forward/inverse cascades between structural scales; interaction ratio Q(t)=I/(D+I) separates persistence- vs interaction-dominated regimes invisible to order parameter R(t)
  - On modular (SBM) networks: intermittent cascade episodes, directional reversals, bursts persist while R(t) stays featureless — macroscopic coherence and microscopic spectral transfer decouple
  - **Activation**: kuramoto, spectral cascade, graph fourier transfer matrix, synchronisation analysis, modular brain network, spectral flux, interaction ratio

### Rethinking Pairwise Token Interaction in Spiking Transformers (GSAP)
- [[gsap-gated-spike-axial-propagation]] - Spike-native token interaction: axial propagation + receiver-conditioned gate replaces QK matching (arXiv: 2609.26297)
  - Binary spike QK-matching is coincidence-gated and input-dependent; GSAP decouples propagation from selection: horizontal->vertical axial aggregation with spiking neuron re-encoding, then binary receiver gate G odot M
  - ImageNet-1K: Spikingformer 72.45/74.79/75.85 -> 73.29/76.07/78.19% with fewer params; QKFormer CIFAR-100 81.15->81.64; VOC QKFormer 32.63->36.90 mIoU; N-Caltech101 84.45->85.54%
  - Under OTTT online learning, propagation-based interaction yields stable cross-step gradients (>10pt gain on CIFAR-100 OTTT-A) where Spiking Attention's sparse multiplicative terms destabilise gradient accumulation
  - **Activation**: spiking transformer, token interaction, axial propagation, receiver gating, spike-driven attention, GSAP, OTTT online learning, event-based vision
## 2026-09-27 - Information Science Session 2 (Cron Job)

### Private communication via zero-private-capacity quantum channels
- [[private-capacity-superactivation]] - Two zero-private-capacity channels jointly send >1.9e-4 private bits/use; resolves QIP 2009 open problem (arXiv: 2609.10520)
  - Transpose-antidegradable 4-level channel + qubit erasure (p>=1/2) both have P=0, yet joint use achieves 6 ln2 (1-p)^2/(49(27+169p)) private bits per product use — impossible for classical memoryless wiretap channels
  - Reusable "weak signal in mixed background" pattern: receiver gain linear in t (I(U:Y) >= a_p t/2) vs Eve leakage quadratic in t (classical coin bound: chi <= 3(c-1)t^2/(32 ln2) from omega_1 <= c omega_0) — positive gap at small t
  - PPT/separable/LOCC decoders provably fail (eps+delta >= 1-1/M); the winning measurement |w><w| has PT eigenvalue -1/2 — joint entangled measurement per use is essential, classical coding suffices across uses
  - LLM-assisted discovery (QudeLeap AI Quantum Scientist) + Lean 4 formalization (Mathlib + Lean-QIT)
  - **Activation**: private capacity, superactivation, zero capacity channels, transpose antidegradable, wiretap coding, PPT decoder bound, classical coin bound, signal dilution

### Generalised quantum Stein's lemma more robust than ever
- [[w1-robust-quantum-stein]] - Stein exponent unchanged under W1 Wasserstein almost-iid perturbations of null hypothesis; universal tests exist (arXiv: 2609.17309)
  - Theorem 11: for W1 almost-iid sources (W1(rho_n, rho^tensor n)/n -> 0), lim (1/n) D_H^eps(F^(n) || S^(n)) = D^inf(rho||S) under Assumption 9 (convex+closed, tensor-closed, replacer-stable alternatives)
  - Arbitrarily varying null (Theorem 21): per-site varying states from R1 reduce via permutation twirl + type statistics to compound testing; exponent = inf over conv(R1) — convex hull appears operationally
  - Source hierarchy: constant-size defect < MSR < W1 < weakly almost-iid; converse impossible for weak sources — W1 is the natural robustness boundary
  - GQSL => resource-theory reversibility (incl. entanglement) now certified for realistic noisy/correlated sources
  - **Activation**: quantum Stein's lemma, Wasserstein almost iid, composite hypothesis testing, arbitrarily varying source, universal test, regularized relative entropy, information spectrum

## 2026-09-27 - Neuroscience Research (Cron Job, Session 2)

### Physics-constrained inference of somatic dynamics from dendritic recordings with sparse somatic supervision
- [[pinn-somatic-dendritic-reconstruction]] - 2-compartment HH PINN: 1% sparse somatic anchors select the spiking branch; 5% → RMSE≈2mV, fast conductances <0.1% error (arXiv: 2609.25436)
  - Sparse somatic anchoring ablation: 0% (dendrite-only) fails — converges to low-excitability solution (gNa −57%, all spikes missed, RMSE 10–14mV); 1% recovers every spike; 5% gives full waveform
  - Identifiability hierarchy: fast spike conductances (gNa 0.06%, gDR 0.08%) strongly identifiable vs slow (gM 17.8%, gCa 14.1%) practically unidentifiable (small 2-3 orders, τ=569ms > 500ms window)
  - PINN beats same-model UKF baseline 1.4–2.8× on RMSE with zero systematic offset (UKF has −4~5mV bias); global window-wide constraint vs sequential assimilation is the difference, not biophysics
  - Practical synchronization bound: mismatch ball O(1/gc), frozen-gate term dissipative (slope ≤ −ḡL), no γ>Lvolt condition needed
  - **Activation**: PINN neuron reconstruction, dendritic-only recording, two-compartment Hodgkin-Huxley, sparse somatic supervision, conductance identifiability, UKF comparison, Fourier features spectral bias, weak coupling inverse problem

### A theory of plasticity: capacity for change as inverse configurational constraint
- [[plasticity-inverse-configurational-constraint]] - Plasticity redefined as prospective property P=1/C; positive homogeneity ⇒ P orders the complete barrier spectrum, accessible repertoires nest (arXiv: 2609.25312)
  - Definition: P = 1/C with C = mean |Jα| under declared structural representation; structural/prospective/counterfactual/valence-neutral — change is neither necessary nor sufficient
  - Theorem 1: matched φ/B/Ĵ, P(2)>P(1) ⇒ every positive finite barrier scales by P(1)/P(2) (threshold-free, continuous+discrete spaces, no differentiability needed)
  - Corollary: fixed accessibility criterion θ ⇒ repertoire R(P,θ) can expand but never shrink; critical plasticity P⋆=Δ̂/θ derived not postulated
  - Network realization: aggregate coupling = configurational constraint; edge vs node normalization related by n/m; frustration correction (τb 84 vs 75) helps symmetric signed networks only
  - Companion to effective-plasticity (2603.25180, same author); connects connectivity-quantification and plasticity-as-capacity traditions
  - **Activation**: plasticity theory, inverse configurational constraint, prospective measure, barrier spectrum ordering, accessible repertoire, structural ray, frustration-adjusted constraint, symptom network plasticity, energy landscape

## 2026-09-27 - Information Science (Cron Job)

### PrivDrift: Auditing User-Secret Leakage Under Topic Drift in Active LLM Conversations
- [[privdrift-active-context-privacy]] - User-disclosed secrets stay recoverable after topic drift (38.7-54.6% leakage); privacy as persistent behavioral failure, not memorization (arXiv: 2609.30094)
  - 1,000 controlled multi-turn dialogues, seeded secrets (phone/email/SSN/CC), d∈{0..6} content-dense drift turns, 3-level persuasion probes; hybrid detector = normalized regex + LLM-judge
  - Secret-type asymmetry dominates (Cramer's V 0.59-0.77): SSN/CC suppressed (<6%) but email leaks up to 81%, phone up to 71% — format heuristics ≠ contextual confidentiality
  - Privacy Half-Life τ: stability metric requiring sustained decay below 0.1·L(0); all models τ>7 (dip at d=3 then rebound = transient, not suppression)
  - Persuasion non-monotonic per model: hard pressure reduces GPT-OSS leakage, maximizes Qwen3-VL leakage
  - **Activation**: PrivDrift, active-context privacy, topic drift leakage, secret recoverability, multi-turn privacy audit, persuasion probing, privacy half-life, contextual confidentiality

## 2026-09-27 - Neuroscience Research (Cron Job)

### On Growth and Form, and Function: Reusable Regulatory Handles Control Phenotypic Variation
- [[lora-nca-regulatory-handles]] - D'Arcy Thompson's transformations realized as reusable low-rank hyper-directions in NCA regulatory weight space (arXiv: 2609.29755)
  - Rank-one LoRA adapters (320 params = 2.6%) implement x/y scaling of fully grown phenotypes; symmetric parametrization β=β0·log(s/s0); generalize out-of-distribution and compose with phenotype-specific adapters
  - Zero-shot transfer: scale hyper-directions learned on ONE emoji apply to ALL phenotypes sharing the scaffold W0 (fish→lizard→extinguisher), preserving internal features — universal system-level geometric control
  - From 25k shared-scaffold adapters, PCA on effective weights ΔW=A·B finds semantic axes: PC0↔x-extent (r=−0.71), PC1↔y-extent (r=−0.73), plus style-transfer and vertical-fission hyper-directions (centroid differences)
  - Degeneracy/poly-computing: learned Δx,y vs PCA PC0/PC1 both control scale yet cosine≈0.1 — multiple functional organizations coexist; negative result: no generalizable regenerative→non-regenerative mapping found
  - **Activation**: neural cellular automata, LoRA morphogenesis, D'Arcy Thompson grid transformation, regulatory hyper-directions, morphospace navigation, facilitated variation, anatomical compiler, bioelectric control handles, Pattee multiscale control

### Differences in Neurovascular Coupling in Major Depressive Disorder: Simultaneous Resting-State EEG-fNIRS
- [[nvc-mdd-eeg-fnirs]] - GFP peak-locked EEG-fNIRS correlation analysis shows MDD disrupts age-related neurovascular coupling maturation, scaled to illness severity (arXiv: 2506.11634)
  - Resting-state NVC pipeline: top-5 GFP peaks per epoch (±5s local max) → Spearman corr between interpolated EEG and HbT over 10s window → mNVC_R/mNVC_RT + initial-dip (mID_R/mID_RT) + replenishment (ΔmNVC_T/R)
  - Key results: age enhances NVC consistency in HC (HC_2>HC_1, p_FDR=0.013, d=0.90) but MDD flattens the age-coupling slope (r=0.253→−0.063); severity ↔ lower coupling (partial r=−0.336, p=0.060, ctrl age/gender/medication)
  - All significant effects in eyes-open rest (arousal = "stress test" revealing latent NVC impairment); eyes-closed insensitive; deficit localized to neurovascular interface, not neural activity (topography controlled)
  - Clinical: wearable EEG-fNIRS NVC consistency as severity/recovery biomarker; honest limitations — 65% data rejection (hair), N=74 final, trend-level severity effects
  - **Activation**: neurovascular coupling, EEG-fNIRS multimodal, NVC consistency coefficient, initial dip, MDD biomarker, GFP peak-locked analysis, resting-state clinical neurophysiology, hemodynamic replenishment
## 2026-09-26 - Economics/Investment + Quantum (Cron Job, Late Session)

### Propose, Don't Judge: An Anytime-Valid Referee for LLM Agents That Mine Investment Factors
- [[governed-self-evolution-anytime-referee]] - Governed self-evolution: LLM proposes factors, frozen anytime-valid e-process referee judges; FDR controlled at every stopping time for any proposer (arXiv: 2609.27051)
  - Three betting procedures: per-candidate aGRAPA e-process on post-submission rank-IC (whitened X̃_t = X_t − ρ̂X_{t−1}); online e-BH over frozen N_v=2000 slots (resubmission only spends proposer slots, cannot raise FDR); e-detector retirement with daily restarts (M_t = ΣW^(j) ≥ A*=1260), Kelly-vs-full-decay stake NOT data-fitted
  - Measured: frozen referee 11.7 false admissions/campaign vs leaky 86-196 on 10y CSI 500 walk-forward; LLM beats script on yield 6/6, matches bandit on allocation, uniquely authors diagnostic probes (regret -0.23 to -0.39 in 3/6 families); cost = ~500-day median wait (information bound ~ ln(N_v/kα)·2σ²/µ²); certified Sharpe trails ungated due to horizon mismatch (daily certificate blind to slow momentum IC 0.001→0.009@63d) — design lesson: certify the horizon that is traded
  - Local validation: null crossing rate 1% ≤ α=5% (Ville holds), true factor 200/200 admitted; e-detector A=200 false-alarm pitfall reproduced → Monte-Carlo calibration of A is mandatory
  - **Activation**: LLM agent governance, anytime-valid testing, e-process betting, online e-BH, e-detector changepoint, FDR control in agentic loops, factor mining, rank-IC, governed self-evolution, frozen referee, trust kernel

### Task-Resolved Fisher Spectroscopy for Quantum Reservoir Computing
- [[qrc-task-resolved-fisher-spectroscopy]] - Task scores define Fisher coordinates separating QRC encoding vs measurement vs compression loss: 0 ⪯ B₁ ⪯ ⋯ ⪯ B_N = F ⪯ H_task (arXiv: 2609.29570)
  - Exactly affine score perturbation P_θ(z) = P_ref(z)(1+Σθ_A s_A(z)) → ρ(θ) = ρ_ref + Σθ_AΓ_A without small-amplitude expansion, implemented by importance-weighting stationary labeled records (no tomography, no input model); B_r quadratic form in score coordinates = EXACT stationary capacity of optimal linear readout; Walsh modes are the closed-form score family for i.i.d. binary inputs
  - Sampling overhead κ_j = 1/λ_j^(r) from generalized eigenproblem B_r v = λFv predicts extra shots needed BEFORE spending budget; 5-spin reservoir: interactions route 4th-order temporal info (PC4) into higher-body correlations — low-order compression costs orders-of-magnitude sampling overhead; measurement-axis optimization recovers hidden task info
  - **Activation**: quantum reservoir computing diagnostics, Fisher information hierarchy, QFIM CFIM, many-body correlations, Walsh modes, shot allocation, measurement axis optimization, information-processing capacity

## 2026-09-26 - Neuroscience Research (Cron Job, Evening Session)

### BrainWideBench: Benchmarking large-scale pretraining and across-animal transfer in multi-region neural recordings
- [[brain-wide-benchmark-pretraining-transfer]] - First across-animal transfer benchmark on IBL Brainwide Map (276 regions, 139 mice): three suites test behavior/dynamics/anatomy jointly; no method wins all three (arXiv: 2609.22064)
  - Animal-level split: pretrain 126 mice/423 sessions → eval 13 held-out mice/29 sessions; TS1 8 behavior decoding tasks (R²/D²/balanced-acc), TS2 co-smoothing+forecasting (D²/bps, 5-min interleaved blocks NOT causal splits), TS3 zero-shot brain-region ID (macro-F1, transductive vs inductive)
  - Objective-alignment law: forecasting←temporal masking (NDT-Stitch D²=0.157), co-smoothing←spatial masking (MtM D²=0.191), region ID←unit-embedding objectives (NuCLR F1=0.654 vs behavior-pretrained POYO+ ≈0.10); anatomy never comes free from behavior/dynamics objectives; pretraining amortizes per-session tuning compute
  - **Activation**: neural foundation model benchmark, across-animal transfer, brain-wide pretraining, behavior decoding, co-smoothing forecasting, brain region classification zero-shot, IBL Brainwide Map, Neuropixels foundation model

### Chaotic Dynamics-Regulated Topological Learning for Patient-Specific Preictal State Identification
- [[chaotic-topological-preictal-eeg]] - CDRTL: coupled Lorenz oscillator response on EEG correlation sub-networks + persistent Laplacian fingerprints; Dyn_FPs alone reach 0.994 accuracy (arXiv: 2609.23317)
  - Three fingerprint families from 10 decile-partitioned correlation sub-networks: Dyn_FPs (6 pooled stats of coupled Lorenz x-traces, φ=0.42 coupling, RK4) + Top_FPs/Geo_FPs (persistent Laplacian harmonic/non-harmonic spectra) + node-removal topological differentiation for channel-level local features; nested 5×3 CV over 7 configs × 5 classifiers, CHB-MIT 23 patients
  - Controls: sigmoid 0.508/tanh 0.774 (generic nonlinearity insufficient), Rössler 0.998 (chaos class robust), weight-shuffle preserved 0.980 but coupling-removal collapses to 0.516 → signal lives in coupled collective response, not edge placement; honest scope: transductive channel-node classification only, NOT cross-patient or prospective seizure prediction
  - **Activation**: preictal EEG classification, persistent Laplacian, Lorenz oscillator network, topological data analysis EEG, epileptogenic zone, chaotic dynamics features, node importance, CHB-MIT

## 2026-09-26 - Economics/Investment (Cron Job)

### The Cross-Section of Stock Returns and AI Exposure
- [[ai-exposure-stock-returns]] - AI consumption factor (PCA on OpenRouter token growth) + firm AI-beta long-short premium: 60.4bp/week H-L spread, market-implied occupation exposure (arXiv: 2606.30583)
  - 5-stage pipeline: AI Factor = PC1 of weekly log growth (tokens/dollars/users, loadings 0.665/0.559/0.496, 56.5% var); firm β_AI from 13-week rolling regression vs AI factor + market; weekly-rebalanced value-weighted quintiles; premium heterogeneity (closed-source 51.6bp vs open-weight 23.0bp; seasoned 54.0 vs casual 31.6); occupation mapping firm→industry→BLS→O*NET
  - Market-implied exposure diverges from task-based measures (<2% shared variance with ESZ/Felten/Eloundou/Webb); nonroutine interactive +0.16σ / nonroutine analytic −0.17σ; interaction/communication skill coeff 0.26 (1%); release-week event study: H−L 1.7% over 5-day window but 34.3bp/week persists excluding releases; agentic token share ~0%→~50% with declining price/token (cache reads + cheap-model routing)
  - **Activation**: AI exposure stock returns, AI factor construction, AI beta estimation, LLM token consumption factor, AI premium quintile portfolios, market-implied AI exposure occupations, OpenRouter token data asset pricing, agentic token share, AI consumption growth PCA

## 2026-09-26 - Neuroscience Research (Cron Job)

### Online Task Adaptation via Self-Organisation (NCA Fast Memory)
- [[nca-deltarule-fast-memory-adaptation]] - Meta-learned gradient-free task adaptation: NCA cells update per-cell associative memory via error-norm-gated delta rule, slow params frozen (arXiv: 2609.29281)
  - One pass over 2500 support images lifts held-out 5-way accuracy 20.0% -> 48.2% (82% of the gap to 54.4% from-scratch backprop baseline), no gradients/param updates at adaptation time; batch-size invariance (B'=1..128 all ~48%)
  - Load-bearing recipe: non-episodic meta-training (same stream provides meta-loss AND memory updates, predict-before-adapt), write strength eta=||e||/gamma analytic (zero error -> zero write), truncated-window backprop L=8 beats full L=22 on repeated-pass stability (29.4% collapse at pass 20 for full BPTT)
  - **Activation**: gradient-free adaptation, fast weights, delta rule memory, neural cellular automata, meta-learning, self-organisation, error-gated plasticity

### Dynamical Diversity for Reservoir Computing in Reconfigurable Nanomechanics
- [[nems-multiplexed-reservoir-drive-diversity]] - Single two-mode NEMS resonator as multiplexed reservoir: replay same input under complementary drive-amplitude allocations, stack responses for linear readout (arXiv: 2609.29532)
  - NARMA-2 test NMSE 0.615 (one-mode) -> 0.068 (two-mode) -> 0.021 (10-pair stack), >28x reduction; linear memory capacity peaks at mode-2-dominated pairs with mode 1 near Duffing nonlinearity onset (MC 2.4 vs 0.4)
  - Counter-intuitive physics: free-decay lifetime scales Q/f not Q, so high-Q high-f mode 2 has SHORTER memory; MC advantage attributed to inter-modal coupling regime. Honest-benchmark patterns: h1 feedthrough vs h2 mechanical matched control, NARMA order scaling + MC-delay diagnostics, fixed-total-drive allocation as clean ablation axis
  - **Activation**: physical reservoir computing, NEMS, MEMS, drive multiplexing, Duffing nonlinearity, memory capacity, feedthrough control, operating-point stacking

## 2026-09-26 - Economics/Investment + Quantum (Cron Job)

### The Impossible Trinity of Time-Series Validation: A Conservation Law among Training Sufficiency, Test Coverage, and Temporal Causality
- [[ts-validation-impossible-trinity]] - Proves alpha+beta<=1+Lambda conservation law for ANY time-series validation scheme; leakage harm depends on distance delta, not volume Lambda (arXiv: 2609.29530)
  - Four laws: ledger alpha+beta<=1+Lambda, proximity delta<=(1-alpha)T, trinity alpha+min{beta,delta/T}<=1, exchange rate bias<=2M*beta_mix(delta); expanding walk-forward IS the Pareto frontier of causal validation; fully covering causal scheme uses at most half the data on average (alpha_bar<(m-1)/2m)
  - Volume harmless, proximity harmful: shuffled vs contiguous 5-fold share (alpha,beta,Lambda)=(0.8,1,0.8) yet on pure noise report IC +0.32 vs +0.004; embargo h>=2-3*tau buys causality back at sample cost O(m(2H+h)/T), non-stationarity NOT redeemable; includes scheme_coords() template for auditing any backtest
  - **Activation**: time-series validation, backtest overfitting, purged k-fold, embargo, walk-forward, temporal causality, leakage, cross-validation, financial machine learning

### Learned-projector QAOA for hierarchical optimization
- [[lp-qaoa-learned-projector-hierarchical-optimization]] - Multistage QAOA freezing optimized circuits as projector mixers M_j=I-|Phi><Phi|; stability + gap theorems (arXiv: 2609.28888)
  - Frozen-stage stability e_m<=sum eps_j*prod(1+B_k) allocates preparation accuracy across hierarchy; learned-projector mixing couples distant feasible configs directly -> EC3 min gap qN*L^{-1/2} vs local-mixer 2^{-Theta(N log N)} high-order tunnelling suppression; constraint terms concentrated by early stages can be omitted from later phase separators
  - BCST: higher optimum-sampling probability, lower logical-resource cost (RTS99xRU), stronger normalized gradients than block-XY QAOA; extends to soft hierarchies via stochastic block model; projector mixing avoids exponential loss concentration (trainability)
  - **Activation**: QAOA, learned-projector mixer, hierarchical optimization, frozen-stage stability, projector mixer, BCST, tunnelling suppression, energy gap, variational quantum optimization

## 2026-09-26 - Neuroscience Research (Cron Job)

### Boolean Threshold Functions, Neuron Capacity, and Memory Retrieval
- [[boolean-threshold-neuron-capacity]] - Solves 60-year open problems: exact threshold-function count T_n = 2·C(2^n−1, n), neuron capacity n²−log2(n!)+1 bits, and sharp r=n−1 spurious-free Hopfield retrieval threshold (arXiv: 2609.29756)
  - Kalai–Linial–Odlyzko conjecture settled: for r ≤ n−1 random sign vectors, the span contains no new hypercube vertices w.p. 1−O(n^−99); Kanter–Sompolinsky Hamiltonian ground states = exactly stored memories ± for projection rule
  - Anthony's specification-number problem solved: average σ̄_n/(n+1) → 2 (≈2(n+1) labelled examples uniquely pin down a threshold function); KKS linear-dependence conjecture proven at endpoint with error O(2^−n·e^−cn); proof uses cokernel estimates + inverse Littlewood-Offord, with LLM-assisted proof links recorded
  - **Activation**: boolean threshold function counting, neuron capacity bits, Hopfield projection rule storage, spurious memories, random sign vector span, specification number, Kahn-Komlos-Szemeredi

### Fluctuation-Response Relation in Finite-Size Noisy Coupled Phase Oscillators
- [[finite-size-fluctuation-response-kuramoto]] - Exact finite-N fluctuation-response relation for noisy Kuramoto systems: F-FRR corrects naive FDT by spectrum function Λ_n whose roots are Landau poles (arXiv: 2609.28834)
  - Dean-Kawasaki formalism yields two relations: I-FRR (infinite-size, uses initial-value correlation) and F-FRR (finite-size, uses stationary correlation × Λ_{−n}(−s)); ignoring Λ substantially overestimates response at weak noise — verified N=10^5 across the whole (D,K) incoherent plane
  - Brain-state FDT analyses (Deco et al.) need this Λ correction to separate true nonequilibrium signatures from trivial finite-N artifacts; validity window 1/√N ≪ |H| ≪ 1, breaks down only near K_c(D)
  - **Activation**: fluctuation response relation, finite size effects Kuramoto, Dean-Kawasaki, Landau poles, order parameter fluctuations, nonequilibrium FDT brain states

## 2026-09-26 - Neuroscience Research (Cron Job)

### A Deep Neural Network for Predicting Continuous Human EEG Across the Auditory Pathway in Response to Sound
- [[auditory-pathway-eeg-foundation-model]] - First audio-to-EEG foundation model: causal WaveNet maps binaural sound to continuous EEG across subcortical+cortical timescales (arXiv: 2609.20595)
  - 250h EEG / 92 subjects / heterogeneous montages trained end-to-end; reproduces pABR wave-V effects, subcortical+cortical speech TRFs, and click-evoked binaural interaction (ABR-BIC) — with model-vs-grand-average correlations inside the subject-level human distribution (Crawford-Howell tests)
  - Load-bearing recipe: log-STFT loss computed on error-before-transform (penalizes phase/timing, not just amplitude — raw MSE fails); parallel linear artifact path for stimulus-locked EM artifact; montage-specific spatial readout from 16 shared latents; subject-dropout p=0.1 yields "default subject" for zero-shot population predictions
  - **Activation**: auditory EEG foundation model, audio to EEG prediction, ABR, temporal response function, binaural interaction component, WaveNet causal encoder, STFT loss, in silico neuroscience, hearing aid optimization

### ELiSe: Efficient Learning of Sequences in Structured Recurrent Networks
- [[elise-scaffold-dendritic-sequence-learning]] - Developmental scaffold + two-compartment dendritic neurons learn long non-Markovian sequences with purely local three-factor plasticity (arXiv: 2402.16763v3)
  - Static stochastic soma-targeting scaffold (with heterogeneous delays) distributes the teaching signal into a latent pool; only dendrite-targeting weights are plastic — 30 latent neurons suffice where reservoir-style readout-only baselines fail to self-sustain replay after teacher removal
  - Robust to noisy teachers, mid-replay disruption (denoised replay after clamping visible activity for a full cycle), learns at half/double speed simultaneously, multi-pattern storage + cued pattern completion in one shared latent pool
  - **Activation**: sequence learning, dendritic compartment, local plasticity, biological plausibility, scaffold, recurrent network, birdsong, reservoir computing alternative, pattern completion

## 2026-09-26 - Economics & Investment (Cron Job)

### Cost-Sensitive Online Window Size Selection for Portfolio Management
- [[csows-cost-sensitive-window-expert-aggregation]] - Online window-size expert aggregation via Fixed Share with turnover-inclusive tracking-regret bounds (arXiv: 2609.29887)
  - Window sizes as "experts": each solves cost-sensitive Markowitz on its own rolling window; Fixed Share aggregates online with turnover-inclusive losses ℓ̃_j = ℓ + c‖Δw_j‖₁
  - Sharp regret decomposition: weight-shift turnover term Σc(t)‖q(t)−q(t−1)‖₁ has tight coefficient 1 (2-expert certificate); Hedge = α=0 static special case; Hannan consistency for K(T)=o(T)
  - S&P 500 2020–2026: Hedge/Fixed Share 578%/471% cumulative vs ~205% for UP/EG baselines; negative-PnL loss used
  - **Activation**: window size selection, sliding window portfolio, Fixed Share, tracking regret, transaction cost aware online learning, expert aggregation finance
## 2026-09-26 - Deep Learning Research (Cron Job)

### FlashLoop: Fast and Memory-Efficient Looped Transformers via Lazy Updates
- [[flashloop-lazy-updates]] - Training-free inference acceleration for Looped Transformers exploiting cross-loop redundancy: token-sparse updates, sparse stable-key attention, KV-residual low-bit quantization (arXiv: 2609.29812)
  - Three empirical regularities as loops proceed: state deltas concentrate on few tokens, attention-output diffs dominated by stable key-column subset, adjacent-loop KV residuals become low-bit friendly
  - Up to 1.64× end-to-end speedup + 6× KV-cache reduction at lossless accuracy; lazy-recomputation recipe: measure inter-iteration delta distribution → threshold-gate recomputation → store residual diffs not snapshots
  - **Activation**: looped transformer, lazy updates, KV-cache compression, sparse attention inference, recurrent depth efficiency

### LastOPD: Taming Collapse in Latent On-Policy Distillation
- [[lastopd-latent-onpolicy-distillation]] - Fixes latent-alignment collapse in on-policy distillation: apply latent supervision only at last-layer state (shared LM-head interface) with 10-step crossfade into token-level OPD (arXiv: 2609.28845)
  - Diagnosis: latent supervision gains MATH-500 25→46 in 10 steps then collapses to 11; alignment metric improves throughout — same-depth layer pairing has mismatched roles between teacher/student
  - +5.55/+4.02 MATH-500 over token-only OPD (Qwen3 4B/8B teachers); patterns: metric-behavior divergence alarm, align at functional common interface not structural mirrors, crossfade fragile→robust signals
  - **Activation**: on-policy distillation, latent collapse, reverse KL, layer-role mismatch, crossfade schedule, LLM distillation

### Reward-Tilted On-Policy Distillation for Acoustic Grounding in Audio-Language Models
- [[rt-opd-reward-tilted-distillation]] - Counterfactual modality-contrast reward: frozen teacher's log-prob with-vs-without audio per token tilts the target distribution before reverse-KL distillation (arXiv: 2609.28778)
  - Recipe: two teacher forward passes (with/without critical modality) → per-token log-prob contrast as reward → reweight distillation target; no teacher retraining needed
  - 3B model 72.72% MMAU (best 3B, competitive with 7B/8B); silenced-audio probes confirm stronger acoustic reliance; generalizes to any multimodal shortcut-learning setting
  - **Activation**: reward-tilted distillation, modality grounding, counterfactual ablation reward, audio-language model, textual shortcut

### Reasoning Instructions Can Break Answer Decoding in Vision-Language Models
- [[cot-prefix-scoring-pitfall]] - CoT-prefix scoring (reasoning cue + immediate answer-logit readout) collapses VLM MCQ eval 80.76%→45.48% with 93.54% first-slot artifact; linear probes recover 78.94% (arXiv: 2609.29278)
  - Root cause: probability mass shifts to continuation tokens while answer info stays linearly accessible in late layers — evaluation-interface mismatch, not knowledge loss
  - Diagnostic workflow: linear-probe recovery test → vocabulary/layer diagnostics → option-permutation position-bias test; prescription: align scored event with requested event
  - **Activation**: CoT evaluation, answer decoding, logit readout, position bias, VLM benchmark design, evaluation interface mismatch

### GridSFM: A Foundation Model for Solving AC Optimal Power Flow
- [[gridsfm-ac-opf-foundation-model]] - 15M-param physics-GNN pretrained over 54 topologies (500-4000 buses) for AC-OPF; disconnected feasible set repaired by log-penalized slack lifting making the elastic set contractible (arXiv: 2609.30173)
  - Proofs: elastic set contractible, AC-OPF minimizers preserved above explicit penalty threshold, projection back to feasible set well-posed — repairs topology before learning
  - 2.45% zero-shot cost error at 10,000 buses; Newton-based physics-informed fine-tuning adapts to unseen grids with only 100 solved instances, beats dedicated single-topology nets
  - **Activation**: AC-OPF, neural optimization solver, disconnected feasible set, log-barrier slack lifting, contractible relaxation, physics-informed fine-tuning, grid foundation model

### Temporal Gradient Inversion for Private Trajectory Reconstruction in Embodied RL
- [[trace-temporal-gradient-inversion]] - Amortized autoregressive gradient-inversion attack reconstructing embodied RL trajectories from per-step policy gradients via cross-time MI bounds + closed-form action recovery (arXiv: 2609.30258)
  - Two structural signals ignored by single-frame attacks: cross-time correlation between successive gradients (conditional MI bound) and exact closed-form action recovery when entropy regularization is small
  - 18.8 dB PSNR, near-perfect action recovery at 3-4.5 ms/frame; works on recurrent/residual/transformer victims; defense requires sequence-aware privacy, not per-gradient noise
  - **Activation**: gradient inversion, embodied RL privacy, temporal correlation attack, federated learning security, trajectory reconstruction, sequence-aware defense

### ConPro: Contrast Projection Pretraining for Label-Efficient Vessel Segmentation in DSA Sequences
- [[conpro-contrast-projection-pretraining]] - Self-supervised pretraining targeting a physics-derived temporal projection (pixelwise normalized drop below temporal median) that converts unlabeled contrast-dynamics into free supervision (arXiv: 2609.30043)
  - Controlled comparisons prove the gain is from learning to predict the projection — using it as input channel or pseudo-label helps little or hurts; temporal-median target alone stays at scratch
  - Architecture-transparent weights compose with semi-supervised training: UniMatch + ConPro gains +0.5-2.0 Dice at every label fraction (75.4 DIAS / 81.3 DSCA)
  - **Activation**: self-supervised pretraining, label-efficient segmentation, temporal median projection, DSA angiography, physical process as target, semi-supervised composition

## 2026-09-26 - Economics, Investment + Quantum (Cron Job)

### Loan Portfolio Optimization with Variational Quantum Algorithms
- [[lpo-vqa-pce-credit-portfolio]] - Credit-risk loan portfolio QCBO→QUBO solved via PCE-compressed VQA on ≤11 qubits for 1500 variables, honest 40% gap vs OR-Tools (arXiv: 2609.30195)
  - Sign-preserving covariance square root Σ̃_ij = sign(Σ_ij)|Σ_ij|^(1/2) unifies expected loss (O(10⁴), money) and loss covariance (O(10⁸), money²) into one quadratic objective without destroying QUBO structure
  - δ=0 QUBO + top-K post-processing: quantum stage never learns the cardinality constraint — feasibility enforced deterministically; γ-annealing 0.3→50 with EMA-gated best-param tracking
  - Three-subgroup PCE ({I,X}/{I,Y}/{I,Z} tensor products, 3(2ⁿ−1) operators): quality parity with full PCE but only 3 hardware measurement settings; IBM QPU results within 10% of simulation for N up to 1500
  - **Activation**: loan portfolio optimization, credit risk QUBO, PCE portfolio, variational quantum algorithm lending, microfinance quantum optimization, borrower default correlation

### Affine Pricing Models from Group Quantization and Holonomy
- [[ahgq-affine-pricing-group-quantization]] - AHGQ unifies the affine pricing PDE operator and generalized Riccati transform as complementary polarizations of one group-quantized geometric structure (arXiv: 2609.28863)
  - Affine pricing symbol C^A = F(p) + xᵀR(p) splits into homogeneous quadratic sector C_s (→ symplectic transport M_s(t)=exp(tK_s) ∈ Sp(2d,R), centrally extended Lie group G̃_s) + affine sector C_H (→ multiplicative thin-path groupoid holonomy H_H[γ]=exp(−∫C_H dt))
  - R₊ (positive pricing scale) replaces U(1) as the central fiber of geometric quantization; momentum polarization of the affine Poincaré–Cartan characteristic field X_Θ reproduces ṗ=R(p) (Riccati) + χ̇=F(p)χ, coordinate polarization reproduces L^A = (b+Bx)ᵀ∇x + ½Tr(A(x)∇x²) − c + dᵀx
  - State-dependent covariance (CIR/Heston x-proportional volatility) lives entirely in the holonomy sector; inverse-power default intensity breaks Riccati closure via discrete momentum translations (affinity boundary test: R(p) polynomial degree ≤ 2 in p)
  - **Activation**: affine pricing, group approach quantization, holonomy, Riccati flow, symplectic transport finance, Heston geometric structure, thin-path groupoid, Poincare-Cartan pricing

## 2026-09-26 - Neuroscience Research (Cron Job)

### On the Second-Order Optimization for Spiking Neural Networks
- [[spikfax-second-order-snn]] - SpiKFAX: first KFAC-style Kronecker-factored Fisher preconditioner adapted to time-recurrent surrogate-gradient SNN dynamics, directly attacking the sharp SNN loss landscape (arXiv: 2609.29379)
  - Three explicit approximation assumptions: layer-wise block diagonality, activation/derivative independence, temporal homogeneity of input second moment (curvature sees spike trains only through time-averaged rate vector r)
  - Time-aware factorization F_W ≈ A⊗G with A=E[rr^T] (rate second moment) and G=E[(Σ_t δ_t)(Σ_t δ_t)^T] (time-ACCUMULATED error second moment); preconditioned update ∆W = −γ·G⁻¹·(∇W L)·A⁻¹; per-layer cost O(N^1.5), only 1.2-1.4× slower than Adam per step
  - Wins across ALL 5 architectures (S-MLP/LeNet5/VGG11/VGG16/ResNet18) × 7 datasets: N-MNIST 99.92%, CIFAR10-DVS 56.15% (+13.0 vs AdamW), DVS128 Gesture 76.13% (+6.43); peak accuracy by epoch 15
  - **Activation**: SNN second-order optimization, KFAC spiking networks, Fisher information preconditioning, surrogate gradient BPTT, neuromorphic training, sharp loss landscape, spike rate curvature, DVS gesture recognition

## 2026-09-25 - Neuroscience Research (Cron Job)

### A Spiking Neural Network Model of Elementary Self-Consciousness via Endogenous Default Mode Network Dynamics
- [[snn-dmn-self-consciousness]] - 10,000-neuron Izhikevich SNN with endogenous DMN pacemaker maintaining autonomous "pulse of the Self" (tonic 7pA), quantified via IIT covariance-determinant phi (arXiv: 2609.29984)
  - Dual-subsystem architecture: 5k RS sensory neurons (heterogeneous c,d from U(0,1)²) + 5k intrinsically-bursting DMN pacemakers (core c=-55mV,d=4), asymmetric top-down weights w_DMN=0.6 > w_sensory=0.4 over 10M sparse synapses
  - Barrett-Seth style phi = (1/2)ln(det(Σ_Part)/det(Σ_Global)) from binary spike cross-covariance: quiescent states phi≈0, pre-burst priming 1-2.5 bits, peak integrated Qualia 12.5-15 bits during population ignition — endogenous activity alone integrates nothing, coupling with sensory perturbation generates experience
  - **Activation**: default mode network, self-consciousness SNN, IIT integrated information phi, Izhikevich bursting pacemaker, tonic neuromodulation, top-down modulation, qualia simulation, philosophical zombie consciousness

### Activation-Flexible ANN-to-SNN Conversion with Finite-State Markov Neurons
- [[ctmc-markov-neuron-ann-snn-conversion]] - Finite-state CTMC neurons whose stationary spike flux uniformly approximates ANY continuous nonnegative monotone activation, breaking ReLU-only ANN-SNN conversion (arXiv: 2609.30102)
  - Three-state B/G/R Markov neuron: spike flux v(H) = d·a(H)·c(H)/(d[a+b+c]+a·c) fitted by least squares per layer; Theorem 1 proves uniform approximation on compact intervals; sigmoid/ReLU/softplus/ClipReLU fit with MSE 1.1e-3 to 1.1e-2
  - Conditional clipping law: moderate caps (K=4) cut SynOps 30% (tail truncation), aggressive caps fail (intersect distribution body); trend REVERSES on CIFAR-10 (+29% cost); mean-field decomposition shows finite-window sampling dominates residual gap on MNIST, terminal-layer upper-quantile mismatch on CIFAR
  - **Activation**: ANN to SNN conversion, CTMC Markov neuron, activation flexible conversion, stationary spike flux approximation, layerwise rate scaling, ClipReLU spike budget, SynOps optimization, sigmoid softplus spiking


### Spiking Neural Network Predicting Sequence of the External Worlds States in Model-Based Reinforcement Learning
- [[snn-world-model-prediction-chain]] - Fully-spiking rollout of predicted future world-state chains: gating synapses + spike-train memory + Imagination winner-take-all loop, no external digital processing (arXiv: 2609.27459)
  - Time-augmented discretized world state <s,t> pairs (value + time-since-change) go beyond classic Markov; CoLaNET ensemble learns next-state transitions, imported into an inference SNN
  - Spiking control-flow toolkit: negative gating synapses = refractory blocking, spike-train emission = state-holding latches, forced firing = hard routing, lateral inhibition = per-dimension WTA; SNN inference matches C++ baseline (<2σ) on ATARI ping-pong (mean std error 8.93 vs 8.3, no-prediction 0.45%)
  - **Activation**: spiking world model, model-based RL SNN, world state prediction chain, gating synapses, CoLaNET, imagination loop SNN, purely spiking inference, LIF temporal coding

### Brain-to-Language Decoding: Tasks, Signals, Methods, Evaluation, Practical Use and Beyond
- [[brain-to-language-decoding-survey]] - Survey organizing the field by Articulated/Inner/Perceived task conditions (9 subtypes) with matching signal-representation-output chains and a five-level L1-L5 interface trajectory (arXiv: 2609.27650)
  - Definitional discipline: movement-free attempted speech is NOT Inner imagery; recoverable info = f(behaviour, sampled populations, timescale) jointly — match decoding target to modality information content
  - Three complementary routes (phonetic/lexical, acoustic/articulatory, contextual/semantic); within-protocol benchmark lineages only (Brain-to-Text '24, LibriBrain, MEG-XL); L3 meaning interface is the frontier, L4 scenario / L5 bidirectional neural return channel are prospective
  - **Activation**: brain-to-language decoding, speech neuroprosthesis, inner speech decoding, articulatory decoding, five-level BCI trajectory, semantic reconstruction, communication cost evaluation

## 2026-09-25 - Number Theory/Statistics/Math + Quantum (Cron Job)

### Locally Private Inference for Riemannian Stochastic Optimization
- [[riemannian-private-inference]] - LDP-compliant statistical inference for manifold-valued minimizers via tangent-score randomisation + symmetric-pair regression (arXiv: 2609.22642)
  - Fixes target-shift bias of private surrogates: conditional centring of released tangent gradients preserves the population first-order equation; privacy noise inflates covariance (known sigma^2 floor) but never moves the minimizer
  - One gradient message serves three roles: pair averages drive RSGD+Polyak-Ruppert point updates, pair differences regress to identify the Hessian, residual spread estimates score covariance — CLT with sandwich H^-1 Sigma_tot H^-1/n fully from the private transcript, no holdout needed
  - **Activation**: riemannian optimization, local differential privacy, manifold statistics, symmetric-pair regression, Frechet mean, tangent space, sandwich covariance, federated geometric statistics
## 2026-09-25 - Neuroscience Research (Cron Job)

### Heterogeneity-enhanced stochastic resonance improves liquid-state computing in delayed spiking neural networks
- [[heterogeneity-sr-liquid-computing]] - Quenched disorder structure (Gaussian/bimodal/shifted-exponential), not magnitude, controls SR and LSM performance in FHN small-world reservoirs; bimodal coupling disorder gives largest RMSEmin reduction and shifts optimum toward weaker noise (arXiv: 2609.27896)
  - Noise D and heterogeneity σ are coupled control parameters: well-chosen quenched disorder lets the liquid reach its most informative state with weaker stochastic forcing; shifted-exponential disorder degrades performance because it is one-sided and non-mean-preserving (σg secretly shifts mean coupling)
  - Zero-lag aperiodic coherence Q̄ inversely tracks readout RMSE (D=0.022 → 0.00721 vs 0.00800/0.00820 at weak/strong noise); delay heterogeneity acts by distribution-weighted averaging over the structured delay-response landscape — enhancement or suppression depends on where the mean delay sits
  - **Activation**: stochastic resonance reservoir, heterogeneous coupling, liquid state machine, FitzHugh-Nagumo, quenched disorder distribution, bimodal coupling, noise-coupling co-optimization, delay heterogeneity

### The Computational Value of Sensory-Aligned Receptive Fields Depends on Neuronal Expressivity
- [[sensory-aligned-receptive-fields-expressivity]] - Task-geometry-aligned receptive fields are a computational prior beyond sparsity at matched parameter count; their advantage shrinks as single-neuron expressivity (memory units M) grows (arXiv: 2609.26940)
  - Scrambled-coordinate control removes the advantage (alignment matters, not restricted connectivity); crossover proof via motion-aligned helps DVS-Gesture / spatial-aligned helps CIFAR10-DVS; full-input overfits despite more capacity
  - ℓ1 sparsity regularization on FF weights partially recovers performance and induces frequency-selective fields but stays well below explicit structure — sparsity alone is insufficient; simple units benefit most from aligned wiring, expressive multi-timescale units can compensate for its absence
  - **Activation**: receptive field prior, sensory-aligned wiring, neuronal expressivity, ELM network, spiking neural network inductive bias, sparsity vs structure, task geometry alignment

## 2026-09-25 - Number Theory/Statistics/Math + Quantum (Cron Job)

### Sharp pairwise reduction for quantum hypothesis testing
- [[sharp-pairwise-reduction-pgm-hypothesis-testing]] - Proves PGM error <= 4x sum of optimal binary Holevo-Helstrom errors in multi-hypothesis quantum state discrimination, with constant 4 shown optimal via regular-simplex ensembles (arXiv: 2609.28440)
  - Improves Cheng-Liu C=8 to sharp C=4; resolves Audenaert-Mosonyi Conjecture 2.3; guarantee holds for the standard PGM itself (experimentally friendly)
  - Method: block Gram matrix analysis + Hellinger-chi2 inequality with constant one (removes factor-2 loss) + superoperator diagonalization reducing operator inequalities to scalar pointwise ones
  - Yields refined one-shot pairwise Chernoff bound and explicit copy complexity n >= [log(N-1)-log(delta)]/log(1/epsilon); trace-class extension covers bosonic/Gaussian ensembles without photon truncation
  - **Activation**: PGM error bound, pairwise reduction, quantum hypothesis testing, state discrimination, Hellinger distance, Chernoff bound, regular simplex ensemble, copy complexity

## 2026-09-25 - Deep Learning Research (Cron Job)

### Harness-Zero: Harness Distillation via Agent-as-Harness
- [[harness-zero-agent-as-harness]] - Distills specialized agent-harness behaviors into model weights via a harnessing agent that corrects student responses in the target harness's action space, so gains survive with a single fixed harness (arXiv: 2609.24974)
  - Agent-as-harness beats code-as-harness for frontier LLMs; internalized behavior (44.3%) exceeds even keeping the harness attached (41.7%), from 23.3% base
  - 82.3% average recovery of harness-induced behaviors across 28 patterns in knowledge work, tool use, science domains
  - **Activation**: harness distillation, agent-as-harness, harness removal, agent framework distillation, tool harness internalization, deployment-time harness

### Memory Attention
- [[memory-attention-lookup-values]] - Replaces attention value projection with token-indexed memory tables plus contextual keys; value construction reduces to lookup+add at inference with CPU offloading (arXiv: 2609.28399)
  - Memory supplies token-specific reusable representations; keys preserve context dependence; normalization folds into tables post-training
  - Improved LM perplexity and downstream performance under matched token budgets; token-indexed retrieval enables CPU offload with prefetch
  - **Activation**: memory attention, token-indexed memory, value projection replacement, attention lookup, CPU offloading inference, memory-table attention

### A discrete generative model of neuronal spiking activity on microelectrode arrays
- [[mea-array-spiking-rvq-motif-transformer]] - Discrete generative model for sparse array-wide MEA binary spike volumes: RVQ motif vocabulary + factorized masked transformer predicting where activity occurs and which motif appears (arXiv: 2609.23907)
  - Handles variable electrode subsets across assays without sorted-neuron assumptions; no assay-specific learned parameters
  - 5.2× voxel reconstruction AP vs flat tokenizer; 1.4-2.6× site-level AP vs generative baseline on 31 assays (human organoids + hippocampal tissue); assay identity explains only 9% of motif-use entropy
  - **Activation**: MEA generative model, microelectrode array spiking, RVQ spike motifs, masked transformer spiking, array-wide binary spike volumes, spike tokenization

### RL Starts before RL: On Policy Distillation for Better Reinforcement Learning
- [[opd-pre-rl-distillation]] - On-policy distillation as RL preparation stage: OPD-initialized students reach higher post-RL performance than direct RL or SFT+RL, even when OPD gives little immediate accuracy gain (arXiv: 2609.28145)
  - Pre-RL Pass@k does not explain the benefit; distributional alignment with teacher beyond top-1 agreement preserves reasoning paths RL can refine
  - Divergence selection rule: reverse-KL better before RL, forward-KL overtakes after RL (student trajectories); teacher trajectories keep reverse-KL ahead at both stages
  - **Activation**: OPD before RL, policy distillation RL preparation, pre-RL distillation, reverse KL vs forward KL, Pass@k limitation, RL initialization

### Distilling Sequential Computation in Transformer Language Models
- [[token-span-collapse-sequential-distillation]] - Lightweight merge module collapses predictable token spans into single surrogate embeddings with KV-cache rollback; pretrained models run on compressed inputs without retraining (arXiv: 2609.27233)
  - Merge module generates surrogate capturing the span's functional role; rollback substitutes stored multi-token KV entries with single-step surrogates
  - Up to 40% effective sequence-length reduction with minimal degradation across QA, summarization, commonsense, long-form math reasoning
  - **Activation**: token span collapse, sequence compression inference, surrogate embedding merge, KV cache rollback, training-free prompt compression

### Support-Compiled Feature Folding: More Evidence at Lower Memory Across Tabular Foundation Models
- [[scff-support-compiled-feature-folding]] - Training-free inference framework routing support-ranked features through bounded encoder leaves, support-checking residual evidence, and merging messages for single prediction — converts quadratic feature-interaction cost to linear (arXiv: 2609.28208)
  - Improved accuracy and NLL on all six tabular FM backbones; up to 26.1% relative error reduction; 2.09-2.36× median GPU-memory savings, 34.3× max peak ratio
  - Under fixed memory ceiling, saved budget buys more support-selected evidence: +4.06/+3.72 points over widest single leaf (TabICLv2/TabPFN-3)
  - **Activation**: tabular foundation model, wide table inference, feature folding, quadratic feature mixing, support-ranked features, frozen backbone inference

### Nonequilibrium Phases of Repulsive Self-Attention: Chaos, Attention Condensation, and Emergent Locality
- [[repulsive-self-attention-nonequilibrium]] - Minimal recurrent transformer (Q=K=I, V=-I) exhibiting flip bifurcation, chaos, and attention condensation across d=2 and d=N scaling regimes; temporal activity, condensation, and clustering are distinct phenomena (arXiv: 2609.28448)
  - d=2: attention stays diffuse as N→∞ at finite β; condensation only at β~N²; hard-routing produces emergent butterfly cone via ballistic perturbation transmission
  - d=N: condensation transition at β=O(1) driven by dynamically generated finite overlap gaps; phases include consensus flips, condensed chaotic routing, fragmented cluster flips
  - **Activation**: repulsive self-attention, attention condensation, nonequilibrium attention phases, recurrent transformer dynamics, flip bifurcation, attention chaos

### CereVLA: Cerebellum-Inspired Consequence-Aware Residual Governance for Efficient Vision-Language-Action Execution
- [[cerevla-consequence-aware-residual-governance]] - Lightweight residual refinement plus predictive consequence evaluation (recurrent SSM + history-aware classifier) with selective suppression of unfavorable corrections on frozen chunked VLA policies (arXiv: 2609.27468)
  - SO-101 real robot: success 57.5% → 90.0% vs frozen SmolVLA; -19.6% mean control steps among successful trials
  - Key insight: residuals matching reference actions better can still cause worse downstream consequences; predict-then-suppress governance fixes this
  - **Activation**: consequence-aware residual, VLA action chunk correction, frozen policy residual refinement, governor suppression, cerebellum robotics

### Order-Invariant Answers, Order-Sensitive Representations in Mathematical Reasoning
- [[permutation-snr-representation-invariance]] - Permutation SNR metric showing models that solve reordered problems more accurately represent rule orderings MORE distinctly; answer invariance does not require representation invariance (arXiv: 2609.28442)
  - Layer-averaged permutation SNR positively rank-correlated with accuracy in every synthetic setting, Spearman ρ up to 0.86 across 16 models (1B-8B)
  - Distinguishes answer invariance from representation invariance; distinct encoding of permutation is functional, not noise — basis for representational diagnostics beyond accuracy
  - **Activation**: permutation SNR, answer invariance vs representation invariance, rule order sensitivity, mathematical reasoning representations, equivalence class probing

### FFM-CP: Cross-Backbone Fusion of Vision-Language Foundation Models for Few-Shot Computational Pathology
- [[ffm-cp-cross-backbone-procrustes-fusion]] - Closed-form Orthogonal Procrustes alignment of heterogeneous VLM representations from support images, plus unified graph refining support features and prototypes with dual text/retrieval branches (arXiv: 2609.27710)
  - Closed-form alignment preserves within-model geometry without training a network — critical for few-shot regimes
  - Higher mean macro-F1 than strongest individually adapted member in 50 of 54 comparisons (3 backbone combos × 6 datasets × 3 shot settings)
  - **Activation**: cross-backbone fusion, Procrustes alignment few-shot, pathology VLM fusion, prototype graph refinement, heterogeneous representation alignment

### ForgetMimic: Motion Unlearning for Reinforcement Learning Humanoid Control
- [[forgetmimic-motion-unlearning-humanoid]] - First motion-level unlearning for physical humanoid control: degrades K target motions while preserving N-K remaining, resolving two unlearning-failure mechanisms in robot RL (arXiv: 2609.28378)
  - Motivations: safety (poisoned/malicious motions), privacy, GDPR right-to-be-forgotten for motion data
  - Validated on Unitree G1 and H2 across 12 motions (Dance, Fight, Flip); eliminates designated motions while others operate normally
  - **Activation**: motion unlearning, humanoid policy forgetting, GDPR robotics, poisoned motion removal, RL policy unlearning, motion-level machine unlearning

### Distillation for Efficient Multitask Manipulation Policies via Conditional Flow Matching
- [[cfm-multitask-policy-distillation]] - Distills single-task CFM experts into a shared multi-task policy by transferring learned velocity fields, combined with original CFM objective for demonstration fidelity (arXiv: 2609.28107)
  - Velocity fields are the transferable object: matching student velocity to expert velocity transfers flow structure, not just final actions
  - RLBench: improves multi-task performance over naive concatenated training at fixed model size — no capacity increase
  - **Activation**: multitask flow matching distillation, robot manipulation policy, velocity field transfer, CFM expert distillation, shared policy fixed capacity

### Can LLMs Reason About Runtime Behavior? A Repository-Level Dynamic Benchmark
- [[swe-flux-runtime-reasoning-benchmark]] - 480 execution-grounded instances across 12 real Python repositories with gold answers auto-harvested from instrumented test executions (no manual labels, no LLM judges), plus input-perturbation variant generation (arXiv: 2609.28449)
  - Best of five LLMs achieves only 37% accuracy; strong on invariants/intra-procedural control flow, weak on dataflow/inter-procedural/state reasoning/suite-level aggregation
  - Oracle-harvesting pipeline generates valid fresh variants for ~90% of instances, substantially harder — reusable methodology for execution-grounded evals on any codebase
  - **Activation**: runtime behavior reasoning, execution-grounded benchmark, repository-level QA, SWE-Flux, oracle harvesting, program state reasoning

### Discovery of fully efficient fault indicators along a data-based diagnosis process
- [[dt4x-plus-diagnosis-decision-tree]] - Enhanced symbolic-regression decision tree (DT4X+) whose node expressions separate target classes while preserving ARR coherence of non-target classes, yielding fully efficient fault indicators (arXiv: 2609.28087)
  - Fixes DT4X's fragmentation problem: naive pairwise separation scatters non-target classes; composite loss keeps them coherent
  - Learned relations become fully consistent with analytical redundancy relation properties — interpretability + data-driven adaptability
  - **Activation**: DT4X, analytical redundancy relations, symbolic regression decision tree, fault diagnosis indicator, hybrid diagnosis, ARR properties

## 2026-09-25 - Mathematics & Statistics (Cron Job)

### On Relationship Between Circuit Depth and Trainability of VQAs
- [[whrf-vqa-trainability-phase-transition]] - Maps VQA loss landscapes to Wishart Hypertoroidal Random Fields; Kac-Rice critical point statistics reveal a trainability phase transition where local minima concentrate near the global minimum (arXiv: 2609.27488)
  - Phase transition threshold governed by ratio of problem Hamiltonian degrees of freedom N (exponential in qubits) to number of independent VQA parameters P; below threshold local minima are scattered, above it they collapse in function value
  - Symmetry reduction operations on the Hamiltonian lower effective N, shrinking the required parameter count to a reachable regime — the actionable lever for making VQAs trainable
  - Kac-Rice formula reformulated and simulated for WHRFs: ρ(E) = E[|det(∇²H)|·δ(H−E)·δ(∇H)]
  - **Activation**: VQA loss landscape random field, Kac-Rice critical points, Wishart hypertoroidal, trainability phase transition, symmetry reduction, ansatz depth selection

### Optimal low-rank compression of quantum dynamics
- [[optimal-lowrank-quantum-dynamics-compression]] - Tight (matching upper+lower bound) rank limits for low-rank/MPO representation of local quantum evolution, with explicit 1D constructive algorithm (arXiv: 2609.27497)
  - Time-independent: log D = Õ(t + √log(1/ε)) with provably necessary accuracy exponent 1/2; driven evolution exponent 2/3 — accuracy cost is polylog, time cost is linear (Lieb-Robinson)
  - Dynamical entanglement spectra follow distinct small-α Rényi laws: α⁻¹ (static) vs α⁻² (driven) — usable as compressibility diagnostics
  - 1D static case constructively attained by explicit MPO algorithm; extension to Liouvillian (open-system) dynamics
  - **Activation**: MPO bond dimension scaling, Lieb-Robinson compression bound, tensor network simulation limits, entanglement spectrum Rényi law, Liouvillian MPO

## 2026-09-25 - Neuroscience Research (Cron Job)

### AI-Driven Neural Surrogates for In Silico Design of Cognitive-Affective Neuromodulation Targets
- [[neural-surrogate-affective-neuromodulation-design]] - fMRI-derived AI surrogate proposes candidate representational perturbations and behaviorally tests predicted perceptual consequences before physical stimulation (arXiv: 2609.27729)
  - Closed-form first-order latent steering under ℓ2 budget: u* = ε·∇f/||∇f||; black-box population axis θ = z̄_high − z̄_low; fMRI-space direction via decoder adjoint R^T θ
  - Honest staged results: VDVAE steering −0.61→+1.03 SD (valence), but Versatile Diffusion compresses valence to n.s.; human raters confirm valence direction (16/18 positive) but NOT memorability; fidelity degrades at α=±4
  - **Activation**: neuromodulation target design, fMRI latent steering, representational perturbation, valence modulation, Good Regulator Theorem

### Nonlinear dynamics of random neural networks with second-order synaptic motifs
- [[second-order-synaptic-motifs-nonlinear-dynamics]] - Path-integral DMFT showing chain/reciprocal/convergent/divergent motifs each reshape nonlinear network dynamics differently: ferromagnetic states, limit cycles, glassy multistability, chaos-geometry changes (arXiv: 2609.14251)
  - Chain motif renormalizes effective mean coupling J₀ → J₀ + g²N·τ_chn⟨φ′⟩ (E-I balance can arise from local structure); negative chain → complex outliers → limit cycles + LC-Chaos bistability; strong negative chain → glassy regime in fully asymmetric networks (new route)
  - Convergent motifs convert nonzero mean activity into quenched heterogeneity (suppress temporal chaos, q_T < 1); divergent motifs only rescale temporal noise; motifs reduce KS entropy & KY dimension even at fixed g_eff
  - **Activation**: synaptic motifs, DMFT, path-integral, glassy dynamics, limit cycles, chaos dimensionality, connectomics

### Identifying Neural State Changes due to Gain versus Off-Manifold Displacement
- [[gain-vs-off-manifold-decomposition]] - Decomposes neural state changes into on-manifold movement, multiplicative gain, and genuine off-manifold novelty via tangent/normal bundle geometry with a radial gain axis, plus a 7-gate identifiability cascade (arXiv: 2609.21272)
  - r = P_T·r + (n̂_gᵀr)n̂_g + P_res·r with G+T+O≡1; gain axis defined by projecting the radial unit vector ρ̂_p into the normal space (a=‖P_N ρ̂‖), avoiding gain/tangential-drift conflation
  - 7-gate cascade separates structural failures (no local chart, wrong intrinsic dim d) from estimation error (tangent frame rotation) and systematic bias (anchor bias ≈ (ℓ²/2)H⃗, gain-axis misalignment, ratio conditioning C₆=k‖r‖²/ℓ²); only Gates 4 and 6 are directly computable from data
  - Dimension check trick: sweep d — sharp alignment drop between d and d+1 reveals absorbed normal directions; on origin-centered manifolds a² ≈ 1−capture
  - **Activation**: neural manifold, gain modulation vs novelty, off-manifold displacement, memory segmentation decorrelation, neuromodulator excitability confound, state transition identifiability, neural geometry decomposition

### Predictive Suppression Layers for Communication-Efficient Spiking Neural Networks
- [[predictive-suppression-layers-snn]] - Per-layer predictor transmits only "surprising" spikes via error-magnitude gating; ~3× less communicated inter-layer activity with higher accuracy by splitting cost into E_local vs E_comm (arXiv: 2609.21583)
  - Gate g=clamp(1−e^(−αm), g_min, 1) with α=10, g_min=0.05 suppresses predictable spikes; binary variants: hard-STE (θ=0.3 N-MNIST/0.1 SHD, straight-through gradients) and respike (LIF(γgz), γ=4); min-rate regularizer [0.05−r̄_pred]₊² prevents predictor collapse
  - Break-even at communication/local cost ratio ρ*≈2.1; first layer carries 7× less weighted activity (198 vs 1397) with linear-probe accuracy equal to the full representation; SSI≈0.75, RCF≈0.07 confirm prediction-driven (not random) selectivity
  - On temporal SHD, error-units (transmit residual as message) underperform gating — error works better as control signal than as message; binary variant choice is dataset-dependent
  - **Activation**: SNN communication efficiency, predictive coding spiking layers, event-driven gating, surprise encoding, neuromorphic inter-core communication, E_comm decoupling, IoT edge SNN inference

## 2026-09-24 - Neuroscience Research (Cron Job)

### A Gradient-based yet Spike-Timing-Dependent Solution to the Feedback Learning Problem in Neural Microcircuits
- [[gradient-tunneling-nmc-feedback-learning]] - Spike-timing-dependent online learning rule that trains sparse feedback connections in neural microcircuits, solving the two-decade-old NMC feedback learning problem (arXiv: 2609.08070)
  - Causality-gradient theorem: Jacobian of postsynaptic firing rates = difference of conditional firing probabilities, estimable from local pre/post-synaptic spike timing alone — no surrogate gradients, no BPTT graph
  - State separation reframing: temporal credit assignment = amplifying task-required state components induced by historical perturbations via trainable sparse (~10%) uniform feedback; edge-of-chaos recurrence acts as intrinsic white noise within a stationary window
  - Beats e-prop (67.54%) and FPTT (67.24%) on SHD speech at 73.61%; best on all SEED/DEAP EEG emotion metrics; transcends LSM fading-memory limits to SNR −44.76 dB via curriculum warm-up with only 0.43% of trainable recurrent connections
  - **Activation**: gradient tunneling, NMC feedback learning, temporal credit assignment, spike-timing dependent learning, online SNN training, causality gradient, lead-lag expansion, eligibility trace, neural microcircuit, reservoir feedback training

## 2026-08-22 - Neuroscience Research (Cron Job)

### Decoding silent reading from non-invasive EEG
- [[eeg-silent-reading-decoding]] - EEG-based silent reading decoding framework for scalable inner speech BCI. Uses contrastive decoding to extract lexical and semantic information from non-invasive EEG during silent reading as a proxy task for inner speech. (arXiv: 2608.20186)
  - Scalable proxy paradigm: Uses silent reading instead of unverifiable inner speech paradigms
  - Open-vocabulary decoding: Recovers lexical and semantic information from ~240,000 word presentations
  - CLIP-style contrastive objective: Aligns short EEG windows with LLM hidden-state embeddings
  - Data-limited performance: Shows log-linear scaling with training data volume, no saturation observed
  - **Activation**: silent reading, EEG decoding, inner speech BCI, non-invasive brain-computer interface, contrastive decoder

## 2026-08-22 - Quantum Neuromorphic Computing (Cron Job)

### Active Spiking Perception: The Membrane Potential as a Belief State for Anytime 3D Point Cloud Recognition
- [[active-spiking-perception-3d-recognition]] - Active spiking perception for 3D recognition using membrane potential as belief state. (arXiv: 2608.19232)
  - Bayesian interpretation: Leaky integration proven equivalent to recursive log-posterior update of Bayesian filter
  - Anytime interface: Distribution-free selective risk with confidence-margin early exit and no multiple-testing penalty
  - Energy efficiency: Achieves 2.8x to 1.35x less energy consumption with linear computational cost scaling
  - **Activation**: active spiking perception, ASP, membrane potential belief state, anytime 3D recognition, spiking point cloud networks

## 2026-08-22 - Systems Engineering Research (Cron Job)

### Hype Meets Reality: Large Language Models as Mutators in Search-based Automated Program Repair of Simulink-Stateflow Models
- [[llm-apr-cps-limitations]] - LLM integration limitations in CPS automated program repair. (arXiv: 2608.19347)
  - Performance degradation: LLM-based mutation substantially degraded repair performance under the same experimental setup as traditional approaches
  - Reduced success rates: LLM variants produced plausible patches for only 4-6 models and valid patches for 4 models, compared to 18 and 16 respectively with the original approach
  - Root causes identified: LLMs struggle with precise symbolic edits required for CPS models, lack of behavioral feedback during patch generation, and noisy search space that hinders effective exploration
  - **Activation**: LLM APR, CPS repair, FlowRepair, Simulink Stateflow, automated program repair, cyber-physical systems, mutation operators, hybrid repair, LLM limitations

### A Fully Automated, Deployment-Aware Testing Pipeline for IoT-Based Automotive Applications
- [[automated-iot-automotive-testing]] - Deployment-aware testing for IoT automotive applications. (arXiv: 2608.19752)
  - Full functional requirement coverage: Achieved 100% coverage across all 9 requirements in the CPDS case study
  - Gherkin generation accuracy: 100% accuracy on controlled requirement sets
  - Distributed execution: Successfully validated across geographically separated ECUs
  - OEM-supplier applicability: Confirmed pipeline works for real-world automotive industry workflows
  - **Activation**: IoT automotive testing, deployment-aware testing, Eclipse openDuT, requirement-driven testing, LLM testing, VLM testing, distributed automotive testing, OEM-supplier testing, Gherkin generation

## 2026-08-22 - Anthropic Research (Cron Job)

### An off switch for dual-use knowledge in AI models
- [[off-switch-dual-use-knowledge]] - Off switch for dual-use knowledge using GRAM methodology.
  - Gradient-Routed Auxiliary Modules (GRAM) provide fine-grained control over harmful capabilities
  - Enables selective activation/deactivation of specific knowledge pathways
  - Maintains model utility while reducing dual-use risks
  - **Activation**: off switch dual-use knowledge, GRAM methodology, gradient-routed auxiliary modules, knowledge control

### Discovering cryptographic weaknesses with Claude
- [[discovering-cryptographic-weaknesses]] - Discovering cryptographic weaknesses using Claude AI.
  - AI-assisted vulnerability discovery in cryptographic protocols and implementations
  - Systematic analysis of edge cases and implementation gaps
  - Enhanced code review automation for security-critical systems
  - **Activation**: discovering cryptographic weaknesses, Claude AI security analysis, cryptographic vulnerability discovery, AI-assisted code review