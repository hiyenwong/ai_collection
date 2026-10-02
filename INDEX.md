## 2026-10-03 - Neuroscience Research (Cron Job)

### Stochastic Dynamics of Large-Scale Motif-Embedded Spiking Neuronal Networks
- [[motif-embedded-spiking-networks]] - 局部motif排列与全局拓扑（ER/SF）如何共同塑造噪声驱动相干共振的因子分解仿真框架 (arXiv: 2610.00616, 配套 2610.00597)
  - 四架构因子设计（ER/ERM/SF/SFM，突触数严格匹配）：motif嵌入使相干共振SNR*提升且最优噪声D*左移，ER背景下增益更大（+10.7% vs +2.9%），SF背景绝对相干远超ER（SNR*≈74 vs 29）
  - Rewiring证明排列≠强度：保留突触数量/权重重排M2/M3c使相干性最大下降，重排M3a/M4反而提升；hub消融三元组（hub/node/edge匹配对照）证明SF优势部分依赖hub完整性（SNR* 20→11）
  - 密度vs强度不对称：提高连接概率使ER/SF收敛（同质化），提高耦合强度放大两者分离；M2(双向对)>M3c(二型循环FFL)>M3b>M3a>M4的motif相干排序跨拓扑稳定，M2/M3c高频双脉冲与高相干关联
  - **Activation**: network motifs, coherence resonance, spiking neuronal networks, scale-free topology, izhikevich, hub ablation, motif rewiring, stochastic dynamics, signal transmission

### MEG-Mamba: A Scalable State-Space Foundation Model for Magnetoencephalography
- [[meg-mamba-ssm-foundation]] - 首个Mamba-3骨干的MEG生成式基础模型：92-token因果tokenizer+parcel/session嵌入+冻结骨干LoRA刺激条件化 (arXiv: 2610.00746)
  - 效率数量级提升：22 vs 400 GPU-hours预训练、4s vs 0.32s上下文，生成保真度超越MEG-GPT（band-power相关r≥0.93全频段）；3.4M参数、87h Cam-CAN静息态
  - 可解释嵌入：parcel嵌入PCA无监督恢复皮层空间组织，session嵌入（token unigram/bigram特征MLP）编码被试年龄且支持新记录零样本推理
  - 任务条件化：multi-hot boxcar刺激嵌入+零初始化LoRA rank16（仅167k参数=5%）注入Mamba输入/输出投影，对预训练和微调均未见的被试生成逼真任务诱发时频响应
  - **Activation**: meg foundation model, mamba state-space, neural signal tokenizer, autoregressive generation, lora conditioning, generative fidelity, brain dynamics simulation, session embedding

## 2026-10-03 - Economics, Investment × Quantum (Cron Job)

### On the generic structures of the protocols for quantum auction and quantum summation and their relation
- [[quantum-auction-summation-reductions]] - 量子密封拍卖与量子安全求和相互归约：指数竞赛密钥 K=U^(1/x) 使清盘价满足 Pr[p<m]=(m/B)^S 只依赖总和，O(S²log(1/δ)) 轮最优（相干访问 O(Slog(1/δ))）；反向复合密钥 κ=B_max·b+π(i) 的阈值析取搜索定位价格+中标者 (arXiv: 2606.27693)
  - 核心洞见：①两类 SMC 任务共享同一运算结构（阈值指示函数上的求和预言机），归约是结构性的不保成本；②泄漏陷阱——Shi & Li 无拍卖行协议析取子程序按原文泄露占用计数（m=2 时 31.7% 轮公开值为 00，实测硬件反例），一行标签修改修复；③公开中标者身份=泄露全部输入；④再编码攻击：查询消耗量子编码，投标方可无检测调整有效出价，固定查询集（2L−1 阈值）恢复密封性
  - 硬件验证（ibm_kingston 156q）：N=4 五个出价向量含平局全部正确；470 场拍卖 Bell 轮单次宇称错误 12.4–16.7% 但 16-shot 多数投票 3354 轮全对，ML 95% CI 全含真值 S；去相干对照证明析取查询依赖傅里叶相位相干性
  - **Activation**: quantum auction, quantum summation, secure multi-party computation SMC, sealed-bid auction, exponential race, threshold disjunction, auctioneer-free auction, amplitude estimation, composite key search, re-encoding attack

## 2026-10-03 - Neuroscience Research (Cron Job)

### Inferring Multi-Timescale Neural Dynamics with Switching Linear Dynamical Systems
- [[mts-slds-multi-timescale-switching]] - MTS-SLDS：从群体记录中恢复 regime 特定潜态时间尺度——多滞后矩初始化（Poisson log 矩转换 Buesing 谱学习）+ regime-conditioned Laplace EM（每 regime 独立高斯状态矩，防止跨 regime 统计混合），特征值直接读出 τ=-Δt/log|λ| (arXiv: 2610.01786)
  - 核心发现：轨迹重构与时间尺度恢复可解离——切换 Poisson 实验两者 held-out R²=0.82 相当时，MTS-SLDS 时间尺度误差 11% vs SLDS 44%，regime 准确率 0.95 vs 0.54；V4 固视三时间尺度 26.4/49.5/120.2ms（ACF 池化把两个快带压成一个有效衰减）；S2 到达运动 regime 188ms（主动）vs 99ms（被动），与行为衰减 168/86ms 对应而 SLDS 无法区分（117/108ms）
  - 方法论模式：①A_k 更新矩差异是关键——RC 版 M_{t,k}=Σξ_t(i,k)E_{q^ik}[x_t x_{t-1}⊤]（期望以 regime 对为条件）vs 因子化版只有标量权重；②多滞后初始化：K-means 滑窗 ACF 描述子临时分割 → Poisson 元素级 log(1+Cov/μμ) 矩转换 → 同 regime 滞后区间正则化回归；③判别式验证：合成 ground truth 谱 MAPE + 打乱对照 + 行为时间相关
  - **Activation**: neural timescales, switching linear dynamical systems, regime-conditioned Laplace EM, multi-lag moment initialization, Poisson moment conversion, eigenvalue timescale recovery, V4 fixation, somatosensory reaching, trajectory reconstruction dissociation

### Spiking neural networks for streaming qubit readout
- [[snn-streaming-qubit-readout]] - 流式 SNN 超导量子比特读出：LIF 网络按 100-200ns 时间块顺序处理频率复用 IQ 迹线、在读出窗口内持续更新 5 比特指派（F_geom 0.9084 vs 匹配滤波 0.8960、全迹 ANN 0.9100），QAT 8-bit 仅损 5e-4，hls4ml 综合每步 31-52ns < 100ns 块时长实现采集期间连续推理 (arXiv: 2610.02129)
  - 核心模式：①局部 L5 + 累积 C5 分块特征（ADC 端平均）；②LIF 可学习 β + 减法 reset + 膜积累无衰减读出，bitwise BCE，surrogate gradient；③QAT 累加器必须截断+wrap（rounding/saturation 拖慢前向 pass）——ap_fixed<18,8>；④64-dim SNN 串扰矩阵最干净（最大非对角 0.0130）；⑤q2 是数据集内在瓶颈（F_22≈0.48）不可 ML 消除
  - 诚实披露：C5 增益主要是容量效应（参数量）而非信息论内容；延迟报告仅含 SNN 内核不含解调/传输；流式 SNN 准确率天花板略低于全迹 ANN 是换实时性的权衡
  - **Activation**: streaming qubit readout, spiking neural networks FPGA, superconducting qubits, frequency-multiplexed readout, crosstalk correction, hls4ml, quantisation-aware training, geometric mean assignment fidelity, QEC real-time syndrome

## 2026-10-02 - Number Theory, Statistics, Mathematics × Quantum (Cron Job)

### Uniqueness, Cramér–Rao Efficiency and Concentration Bounds for Quantum U-Statistics
- [[quantum-u-statistics-efficiency]] - Dasgupta-Warsi-Chatterjee 证明量子 U-统计量是多项式泛函估计中唯一无偏置换不变估计量，且渐近达到量子 Cramér–Rao 极限——无需自适应测量或预层析 (arXiv: 2609.08745)
  - 核心结果：①边际核-梯度等价 ∇f(ρ)=m·O^sym_{B,1}（置换不变核的偏迹=泛函导数）；②唯一性：置换不变算子空间由 {A^⊗n} 张成，任意两个无偏不变扩展之差恒为零；③方差展开 Var(U_{n,k})=Var(∇f)/n+O(1/n²)，首项恰为多参数 SLD QCRB；④Bures χ² 散度估计：λ_min(σ)≥δ 谱条件充分不必要，弱化为 Var(∇χ²_B) 有界（Lyapunov 积分表示 χ²_B=2∫Tr[(ρe^{−τσ})²]dτ−1）
  - 有限样本理论：交叠子集映射到相交图 + Cayley 生成树计数 r^{r−2} 控制高阶连通矩 → 方差敏感 MGF 界 → 闭式 Bernstein 型集中不等式；中偏差原理（MDP）：εₙ=n^{−α} (1/3<α<1/2) 时尾部纯高斯、仅由 QFI Var(∇f) 支配；数值稳定测试参数 s*=ε/(√(nV)+2√(Aε)+2Bε) 有理化避免灾难性消去
  - **Activation**: quantum U-statistic, Cramér-Rao efficiency, permutation-invariant kernel, marginal kernel gradient, Hoeffding decomposition, Bernstein concentration, moderate deviation principle, Bures chi-square divergence, quantum Fisher information, polynomial functional estimation

## 2026-10-02 - Neuroscience Research (Cron Job)

### Association Profile Conditioning in a Set-Temporal Transformer for Cross-Session Intracortical Motor Decoding
- [[apst-association-profile-frozen-bci]] - APST：冻结权重的跨会话颅内运动解码——从少量带标签校准试验闭式估计每单元 4-D 行为关联轮廓（方向调谐 cos/sin 或 SVD 压缩 EMG/速度关联，统一 4 维接口），经 FiLM（零初始化）条件化置换不变集合注意力编码器 + 滑窗因果 Transformer 流式解码，无需目标会话梯度 (arXiv: 2609.39080)
  - 核心结果：DANDI688 held-out 速度 R² 0.78/0.81（Sub-C/Sub-M）vs activity-only 0.40/0.58；FALCON M1/M2/H1 = 0.65/0.42/0.44，M2、H1 为无梯度方法最优；8 试验校准超 16 试验 RNN 微调，校准成本 <22M MACs vs 微调 383–1195 亿 forward MACs（5 个数量级）；最远会话（138 天后）0.58 vs RNN-FT 0.48
  - 方法论模式：①闭式轮廓 <15k ops（方向调谐 vs 高维 SVD 投影到源关联 V₄ 基，同一 4-D 接口跨任务共享）；②双条件位点（校准期缓存身份 + 流式 token 拼接），adaLNZero 零初始化使 FiLM 为纯残差；③profile-shuffle 消融跌破 activity-only（0.00/0.03）证明轮廓是单元级身份而非会话级摘要；④source 训练期 whole-unit dropout + 集合注意力槽查询处理任意单元集漂移；⑤滑窗 KV cache 有界流式状态 O(R)
  - **Activation**: cross-session intracortical decoding, frozen-weight BCI, association profile, FALCON benchmark, few-shot calibration, unit drift, permutation-invariant set attention, directional tuning, SVD-compressed profile, sliding-window causal transformer

### Large Language Model-Guided Evolutionary Discovery of Native Neural Architectures for Spiking Sequence Modeling
- [[openarchevo-native-snn-discovery]] - OpenArchEvo：LLM 在开放程序空间中进化可执行 SNN 架构代码（受接口/因果性/脉冲投影三重约束），三视图表征（代码 CodeBLEU + 设计意图 embedding + 21 维行为指纹）同时支撑新颖性估计与性能预测，TabPFN-2.5 代理 + NSGA-II 双目标（预测性能×新颖性）分配昂贵训练预算 (arXiv: 2609.40258)
  - 核心发现：ANN→SNN 直接移植欠用脉冲计算（97 对架构 ANN/SNN 排名仅部分一致）；发现的 NeuroGate 在 WikiText-103 达 26.4 PPL（超 ANN DeltaNet 的 27.5），LoopMem 估算算术能耗比稠密 Transformer 低 50.6×；发现机制=脉冲活动依赖的递归状态更新控制与输出门控
  - 可复用管线：可执行约束检查（18% 编译失败+3% 因果检查拦截）→ 指纹近重复筛除（30%）→ 代理预测 → 多岛进化内环/训练外环，全程 132 V100-days；SWSP（二值脉冲的样本级模式计数）+ FireRate + 5 种零成本代理构成 7 个初始化时探针，代理研究 Kendall τ 从 0.46 升至 0.76
  - **Activation**: LLM-guided architecture search, spiking sequence modeling, evolutionary NAS, open program space, three-view novelty, behavioral fingerprint, TabPFN surrogate, NSGA-II, spike-activity-dependent gating, native SNN architecture

### Arithmetic of the sync basin for pulse-coupled oscillators
- [[arithmetic-sync-basin-pulse-coupled-oscillators]] - 脉冲耦合振荡器同步盆地的精确数论结构：线性充电曲线（γ=0，泄漏型与活跃型动力学边界）处同步概率由 N 的素因子分解控制——素数 N 有闭形式 P_sync=1−1/N^N，一般 N 归约为均匀整数"词"计数 P_sync=A_{N,1}/N^N，复合 N 渐近 1−P_sync∼C_m·N^{−(m−1)}（m=最小素因子），为分形/riddled/tentacled 盆地图谱新增"算术盆地" (arXiv: 2609.01668)
  - 等大小原理（EXACT）：线性充电下 Poincaré 回归映射为纯平移，逃逸吸收要求各簇脉冲分数相等 → 非同步结局仅为均分 N 的等簇，结局数=d(N)（N=100 时 9 个 vs 先验 1.9×10⁸ 个划分）；凸充电 γ<0（对应二次/指数 IF 神经元加速发放区）N≤5 有精确有理函数解，γ=0 处全部解跳跃突变
  - 方法论模式：①连续盆地体积→离散字计数（动力学仅依赖小数部分秩序，整数"词"上结局恒定）；②素数 N 仅剩全单例逃逸（体积 1/N^N）；③复合 N 的 lpf(N) 决定主导非同步信道（N=15: sync 99.785%、(5)³ 2.14e−3）；④算术结构是充电非线性临界现象而非脉冲耦合普遍性质（fragility is the message）
  - **Activation**: pulse-coupled oscillators, synchronization basin, prime factorization sync, equal-size principle, convex charging, integrate-and-fire, cluster states, return map translation, exotic basin geometry, cardiac rhythm robustness
### Disentangling Computation in Multi-Task Neural Networks with the Green's Operator
- [[greens-operator-multitask-rnn]] - 有限视界 Green's 算子 P_[DhF]^-1 全局映射扰动源→下游响应，任务级/时间级双约简揭示多任务 RNN 的计算复用与训练中涌现的时序路由 (arXiv: 2609.40292)
  - 核心发现：相同活动轨迹+相同特征谱的系统可有完全不同的扰动路由（三角玩具模型精确推导 lag-k 响应 c(a^k-b^k)/(a-b)）；15 任务 leaky RNN 上 Green 相似度恢复已知 motif 块结构（8-trial 公平比较 AUC 0.920 vs 隐状态协方差 0.852、增益谱 0.785），置换零假设 0.812±0.017 (p=2e-4)
  - 方法论模式：①前向递推 y=Pu 与伴随递推 z=J*z+v 矩阵自由估计（代价线性于视界），支撑随机化 SVD/低秩摘要，永不构造 T²N² 全算子；②D_θh=-P·D_θF 表明学习算子是全局响应几何的参数选择草图；③训练后 MemoryPro 长程响应占比 0.353 vs ReactPro 0.017（初始化均 ~5e-4）——训练按持久性需求组织时序路由
  - 诚实局限：一阶+有限视界，约简必丢信息；任务级组织跨模型不稳定；DMC/DNMC 谱相同但响应方向大异；控制任务方差后与梯度对齐相关性不再唯一 → 不声称预测迁移
  - **Activation**: Green's operator, multitask RNN, perturbation routing, task reuse, matrix-free randomized SVD, adjoint recurrence, response geometry, Lyapunov complement, NeurReps 2026

### How much of fly walking is written in the wiring?
- [[connectome-wiring-specificity-null-models]] - 果蝇连接组固定权重模型的预注册嵌套重连零模型检验：节律是泛化的（重连网络更节律），拮抗肌协调才是布线特异的——Sherrington 交互神经支配直接写入连接组 (arXiv: 2609.38665)
  - 核心发现：真实 MaleCNS 拮抗分数 S=0.312 超过全部 40 个重连网络（最高 0.144），MANC 0.173/0.128 vs ≤0.084，两个独立连接组同向复制；交互神经支配指数真实 0.48/0.38 vs 所有重连 <0；跨池重分配 premotor 输入（强度中位变化 <4%）即废除协调
  - 方法论模式：①嵌套零模型族（density→cell role→degree→leg block→lineage block→leg×lineage，每族 5 网）逐级保留结构；②仅 3 个全局参数扫描后冻结，解剖学接口（DNg100 输入/运动神经元池输出）；③预注册声明水平+60s 新噪声 20 次确认+精确再生验证（4,692 记录）；④协调集中位于 thorax–coxa 关节且持续数分钟
  - 可迁移教训：连接组模型产生某行为 ≠ 布线特异；测布线特异性要看协调（模式形成）而非节律；修剪充分性测试与重连特异性测试回答不同问题
  - **Activation**: connectome null models, rewired networks, wiring specificity, reciprocal innervation, antagonist coordination, Drosophila walking, pre-registered criteria, fixed-weight rate model, MaleCNS, MANC
## 2026-10-02 - Number Theory × Quantum (Cron Job)

### The twisted convolution identity and ghost r-SICs from finite quantum dilogarithms
- [[ghost-r-sic-twisted-convolution]] - Appleby-Flammia-Kopp 将 Radchenko-Wheeler 有限五边形关系证明从 rank-1 主形式推广到全部 rank-r admissible tuples，无条件证明 ghost r-SIC 存在性 (arXiv: 2609.39192)
  - 核心结果：对满足 r<(d−1)/2 且 (d²−1)/(r(d−r))∈ℤ 的正整数 d,r，存在 d² 个 rank-r 子空间构成非 Hermitian equichordal 配置（ghost r-SIC）；Stark 猜想下经 Galois 共轭升级为真正 Hermitian r-SIC
  - 方法论模式：①惯例字典桥接（RW 的 F_γ^± 与 AFK 的 Shintani-Faddeev cocycle ש 显式换算，Rademacher 不变量 Ψ(γ) 为桥）；②rank-1→rank-r 提升用有限交换群特征理论+子群对偶 H/H^∨；③无条件核心+条件升级分离（ghost 无条件，Hermitian 需 Stark 的 Galois 自同构）；④幂等性编码为上链特殊值的二次型消失条件（TCI ⟺ Π̃²=rΠ̃）
  - 关键引理链：L^m = r_{j,m}L − r_{j,m−1}I（Fibonacci 型递推）、L^{2m+1}−I = d_{j,m}L^m(L−I)、det(L−I) = −(d^j−3)
  - **Activation**: ghost SIC, twisted convolution identity, finite quantum dilogarithm, pentagon relation, equichordal, rank-r SIC-POVM, Shintani-Faddeev cocycle, character theory lift, Stark conjecture Galois

## 2026-10-01 - OpenAI Research (Cron Job)

### GPT-Red: Unlocking Self-Improvement for Robustness
- [[gpt-red-self-play-red-teaming]] - OpenAI 自动化红队模型 GPT-Red：自博弈 RL 中攻击者与多样防御者池同时训练（零和奖励：攻击者以"诱发有效失败"得分，防御者以"抵御攻击+完成原任务"得分），防御者变强迫使攻击者发现更强攻击；生成的对抗数据注入生产模型训练（GPT-5.6 训练后对 GPT-Red 直接注入失败率仅 0.05%），攻击者模型与部署隔离只转移鲁棒性 (https://openai.com/index/unlocking-self-improvement-gpt-red/)
  - 关键协议：每个场景环境显式 threat model（攻击者可控面+成功判据）；评估四件套——held-out 新场景泛化（间接注入 arena 84% vs 人类 13%）、simulate-then-attack 实机迁移（Vendy 售货机案例全部 3 个恶意目标达成）、held-out 数据外泄套件（比 prompted 基线更有效且更省 token）、能力保持检查（鲁棒性≠拒答，通用能力不受损）
  - 发现新攻击类"Fake Chain-of-Thought"：GPT-5.1 上 >95% 成功率 → GPT-5.6 Sol 上 <10%，展示红队-加固飞轮的单调收敛
  - **Activation**: automated red-teaming, self-play adversarial training, prompt injection robustness, GPT-Red, attacker-defender RL, adversarial data generation

### Towards safety cases for frontier AI training
- [[frontier-training-safety-cases]] - OpenAI 安全案例方法论：借鉴航空/核电的证据驱动安全论证，要求在继续任何前沿 RL 训练运行之前完成结构化安全文档；技术栈三支柱=对齐（模型不想做未授权行为）+遏制（做了也难越界）+监控（伤害前捕获）(https://openai.com/index/towards-safety-cases-for-frontier-ai-training/)
  - 对齐训练护栏五件套：自动化数据集审查（agent 修复可被 reward hack 的 RL 环境）+人工数据集审查+grader 调优（惩罚环境利用行为）+prior run 追踪分析（分类器验证 grader）+对齐度量评估
  - 核心立场：安全案例是"论证"而非合规清单——每条风险声明必须溯源到可测量证据（评估/分析/红队结果）；能力涌现使过往安全不自动迁移，每个 run 须重新论证
  - **Activation**: safety case, frontier training safety, RL training governance, pre-training safety review, alignment containment monitoring, evidence-based safety argument

## 2026-10-01 - Neuroscience Research V (Cron Job)

### Causal pieces: analysing and improving spiking neural networks piece by piece
- [[causal-pieces-snn-expressivity]] - SNN 表达力理论框架：输入×参数空间按"同一子网络引发输出脉冲"分区为 causal pieces，piece 数给出近似误差下界 ‖Φ−g‖>c·ζ⁻²·p^(−1/2)（对任意不连续行为有效），是首个不要求正权重、不回避脉冲不连续性的 SNN 表达力度量 (arXiv: 2504.14015)
  - 反直觉初始化洞见：非零均值权重分布才能最大化 piece 数（Sparre Andersen 随机游走定理给出大方差下界），文献普遍借用 ANN 零均值初始化恰恰次优；初始化时训练样本落入的 piece 数与最终精度强相关（log-linear r=0.70→0.92），差初始化训练后 piece 数反而下降、难恢复
  - 正权重 SNN（仿生，皮层 80% 兴奋性）：每神经元权和>阈值即全局 Lipschitz→覆盖数泛化界；lognormal 正初始化+线性读出在 Yin-Yang/MNIST/EuroSAT 达全连接 ANN 水平；piece 数随深度 logistic 饱和而非 ReLU 式指数
  - **Activation**: causal pieces, SNN expressivity, spiking neural network, single-spike coding, TTFS, nLIF, weight initialization, Sparre Andersen, Lipschitz continuity, positive weights, covering number, approximation bound, spike-time discontinuity

### Better Behavioral Prediction, More Faithful Model Ablations? Evidence from Sequential Choice
- [[ablation-response-fidelity-behavioral-models]] - 消融忠实性验证协议：合成 bandit（已知生成器）证明"预测更好"≠"消融响应更忠实"——LLaMA/GRU/Transformer donor 奖励替换响应仅 0.08-0.46 nats 而 oracle 2.067；RW 预测最差但响应最忠实（响应向量误差 0.407 vs 0.501-0.592）(arXiv: 2609.36097)
  - 三操作必须区分：G=choice-only 重训练收益 / donor derangement 置换（固定预测器 teacher-forced 一步评估）/ 带符号概率响应向量误差 E[½Σ|v_p−v_o|]（不允许跨动作抵消）；spatial 任务中 LLaMA 反而全面胜 RW——排序是任务×管线经验属性，无必然灵活性-忠实性权衡
  - 可复用校准流程：报告 intact+perturbed 绝对值而非相对百分比；有受控模拟器时同 histories 同操作下对比概率响应+同族 fitted 参考+简单 pooled 基线；"模型不看 X 也预测好→人不依赖 X"类推断的通用反例
  - **Activation**: input ablation, behavioral model validation, response fidelity, oracle calibration, donor replacement, sequential choice, cognitive modeling, Centaur, LLaMA behavioral prediction, reward learning, mechanism recovery, prediction vs explanation

## 2026-10-01 - Systems Engineering x Quantum: Chiplet Compiler (Cron Job)

### QBX: A Compiler for 2-local Qubit Hamiltonian Simulation on Quantum Chiplets
- [[qbx-chiplet-hamiltonian-compiler]] - 首个面向chiplet架构的2-local哈密顿量模拟编译器：Pauli字符串按Trotter置换自由度聚合成多目标受控门经highway执行，ILP/METIS分层映射最小化跨片通信 (arXiv: 2609.33997)
  - 核心洞察：同类型(XX/YY/ZZ)共享qubit的2-local Pauli strings可聚合为Pauli set（Trotter公式置换不变），Pauli block按ZZ→YY→XX排序最大化highway复用；两个复用定理——control-empty（目标间门隔开即可复用）与cross-Y（控制上恰一个Y gate时Y+X修正复用）均有态矢量正确性证明
  - 五级流水线：Pauli图分割（ILP/CPLEX→METIS兜底）→ set orchestrator（二次分配ILP，通信矩阵×chiplet距离）→ Pauli block调度（O(Nc·m·n)贪心，Steiner树Mehlhorn算法选highway路径）→ SABRE片内映射 → 电路生成；关键工程决策：调度必须在映射之后（否则highway路径冲突）
  - 结果：深度较Qiskit降8.9×、较t|ket⟩降53.2×、较MECH降1.69×（eff-CNOT 1.08×）；较2QAN快19.54×且深度低1.13×（2QAN的O(m⁴)调度在24h超时）；SABRE映射产生2.54×跨片通信量/2.66×更大距离；异构错误成本模型 eff_CNOT = #on + 7.4·#cross + 0.7·#meas
  - **Activation**: chiplet architecture, quantum compiler, Hamiltonian simulation, Pauli string aggregation, highway mechanism, multi-target controlled gates, qubit mapping, METIS partitioning, quadratic assignment, Steiner tree, QAOA compilation, Ising model, heterogeneous coupling cost, modular quantum computing

## 2026-10-01 - Systems Engineering Research (Cron Job)

### Control and Estimation Co-Design via Envelope-Theorem Gradients
- [[contest-envelope-codesign]] - plant/传感/执行/估计器放入单一两阶段优化，设计梯度直接从内层SDP对偶变量经包络定理读出，免KKT隐式微分 (arXiv: 2609.36090)
  - 包络梯度：∇θJ*=∂θL(z*,μ*,S*,θ)，正则条件(A.I)-(A.IV)下精确；唯一性破坏时退化为Clarke次梯度（下降方向仍有效）——方法优雅降级不崩溃；复杂度O(rx²) vs KKT隐式微分O(rx⁶)
  - 三内层变体统一：LQG控制/估计SDP互为转置对偶（Jacobians从LMI对偶块读）；H∞最小-γ对偶集值需fixed-γ+epigraph slack恢复精确；非线性eKF信息状态线性化→凸MPC，梯度从costates读（近似）
  - HVDC案例：协同droop调参+4传感器≈固定droop+15传感器的估计质量，砍73%遥测——纯传感器选择无法表述此权衡（droop重塑估计器跟踪的动力学）；四案例J_sc降幅5.6%-39.5%
  - **Activation**: control co-design, estimation co-design, sensor placement, actuator design, bilevel optimization, envelope theorem, SDP dual gradient, LQG, H-infinity, sensor selection, information architecture, MDO

### Invariance is Compositional for Continuous-time Systems: From Sleekness to Lebesgue Density
- [[compositional-invariance-lebesgue]] - 首个双向（充要）组合不变性定理：互联系统全局安全⟺各子系统在邻居耦合输入下局部安全，验证复杂度从R^n不可数边界点降至2N标量检查 (arXiv: 2609.36539)
  - 技术核心：tangential Lebesgue-density弱于经典sleekness（ sleek⟹稠密，逆命题为假，凸集免费），足以保证∏T_Ki=T_K，从而同步局部序列合成全局等价
  - 100-DGU直流微电网（k=6环拓扑）：每DGU标量一阶droop模型，K_i=[47.2,48.6]V电压带，200个标量不等式完成全网安全证书，复杂度线性于N且与拓扑无关；此前后所有assume-guarantee框架只有充分方向
  - 诊断能力：局部检查失败⟹全局必不安全且可定位故障子系统——充分性-only框架无此能力；限制：需Cartesian积安全集+Lipschitz动力学，耦合集取邻居整个安全集可能保守
  - **Activation**: forward invariance, compositional safety, interconnected systems, assume-guarantee, tangent cone, contingent cone, sleekness, networked control, DC microgrid, safety certificate, scalable verification, CPS safety
## 2026-10-01 - Systems Engineering x Quantum (Cron Job)

### Fewer Qubits, Better Choices: Coupling-Aware Sub-QUBO Selection for Quantum-Assisted Traffic Zone Partitioning
- [[coupling-aware-subqubo-selection]] - 大QUBO分解为硬件尺寸子问题时，1-opt最优点上单变量impact排序全盲（所有单翻转都是代价），改进全部藏在耦合矩阵K里；DkS选择器从二阶翻转空间展开导出prize-collecting densest-k-subgraph目标，贪心选强负耦合+个体便宜的q个变量 (arXiv: 2609.32627)
  - Philadelphia 1525区域网络：DkS q=16 胜 random q=64——4倍设备容量补不回弱选择策略；真实路网邻接（vs质心几何邻接，改62%边）再放大优势1.6-1.9x；量子求解比例0%→100%固定选择轨迹时目标逐位相同——增益全部来自经典选择规则（诚实负结果）
  - 硬件瓶颈是耦合项数不是qubit数：q=120稠密(7260项)编译器282s拒绝，70%稀疏化(5118项)成功且ratio 0.9981；编译时间 ~1.5e-4*terms^1.89s(R2=0.999)，~2500项处超过QPU成本；wall-clock被排队主导（QPU占比仅5.7%，39x波动），报告必须用provider用量记录
  - 界L(S)<=F(S)<=U(S)免求解器调用预判子问题价值，停止规则用L不用U（U在收敛后仍虚高）；种子分数必须含"单翻"选项M_ij=max(-a_i-a_j-K_ij, -a_i, -a_j)否则贪心在无联合盈利对时卡死；禁忌罚tau(t+1)=0.8tau(t)+1_S记忆~5轮，5轮无改进才停（13-14轮空后第15轮恢复收益）
  - **Activation**: sub-QUBO, QUBO decomposition, hybrid quantum-classical optimization, variable selection, densest subgraph, flip-space expansion, qbsolv, coupling-aware selection, traffic zone partitioning, working set selection, compilation bottleneck, term count
## 2026-10-01 - Neuroscience Research IV (Cron Job)

### Multi-Depth Temporal Fusion for Feedforward, Locally Trained Spiking Neural Networks
- [[mdtf-temporal-fusion-local-snn]] - 全局部学习SNN架构：局部STDP下被中间层抑制的特征永久丢失，深度问题变为"时间证据路由"。MDTF用H=[P,Δres,Δagree]融合：保留浅层P码+TopK稀疏残差Δres+跨深度时间一致性门控Δagree(|I(i)-D(i)|≤m_agree才保留)，深特征需与中间码时间对齐才被信任 (arXiv: 2609.37047)
  - 完全局部训练在困难任务碾压传统STDP/R-STDP基线：Fashion-MNIST +18.2pp、CIFAR-10 +29.2pp、N-MNIST +73pp(基线缺事件前端)；前端消融显示simple latency编码MNIST仅9.8%(=随机)，完整早视觉前端(去相关+极性分离+校准)达96.7%——局部学习下前端即表征
  - 多原型R-STDP读出：时间走廊margin奖励(违例越大更新越强，替代二值reward)+仅top-K竞争类稀疏anti-STDP惩罚(稳定性关键)；spike-budget Pareto分析：仅保留最早X%事件重训读出仍 graceful degradation，早期强事件携带集中信息
  - **Activation**: spiking neural network, local learning, STDP, R-STDP, time-to-first-spike, TTFS, temporal fusion, residual routing, event-based vision, neuromorphic, layerwise training, population coding, spike sparsity

### Receptive-field-constrained stimulus optimization for human early and intermediate visual cortex
- [[rf-constrained-mei-visual-cortex]] - 人类V1-hV4体素级MEI合成：小pRF使无约束优化失效，解法=pRF约束编码模型内建后梯度穿透优化。RF-DiVE(SD v2.1逐步去噪brain-guidance scale 300)生成自然图像，RF-GO(Fourier相位梯度上升)生成纹理图像，每体素1000种子取top-10 (arXiv: 2609.36391)
  - 生成/排序/测试三模型分离是有效性关键：RF-GO在自家编码器下difference score更高但对独立测试编码器泛化更差(DINO后端尤甚)——生成器选择塑造MEI外观与跨模型泛化，跨方法共同特征才是真调谐
  - 所有方法所有脑区MEI预测响应均超最强自然图像(NSD/LAION配对体素检验)；行为验证n=32：hV4 MEI被判定比V1更多3D形态(自然图无此效应)——合成MEI暴露自然图像挖掘不到的选择性
  - **Activation**: most-exciting-input, MEI, receptive field, pRF, voxelwise encoding model, fMRI, stimulus optimization, diffusion-guided generation, gradient ascent visualization, natural scenes dataset, V1 hV4, feature visualization
## 2026-10-01 - Neuroscience Research III (Cron Job)

### Flattening the Connectome Spectrum: A Spectral Filter for FC Induces a Pretraining Target for fMRI Encoders
- [[fc-spectral-flattening-fmri-pretraining]] - KRR能打败所有脑基础模型的原因：correlation kernel隐式用特征值加权特征向量重叠(⟨Σ_a^α,Σ_b^α⟩_F=Σλ_i^α μ_j^α(v_iᵀu_j)²)，raw FC谱失准。逐被试FC^α=VD^αVᵀ幂律压平谱(α*=0.35)后KRR在5数据集/11分区/6目标全面匹配或超越基线 (arXiv: 2609.37642)
  - 同一组特征向量换权重：top-20模式raw 0.544→flattened 0.610，纯特征值加权增益；100个随机滤波器无一超过0.621，30参数binned/MLP学习滤波器过拟合内层CV反而更差(0.586/0.579 vs 0.624)——简单幂律赢
  - kernel形式无关(per-subject基底才是关键)：Pearson/cosine/dot-product差0.0006，共享PCA基底需~200分量才追平自选top-20(0.610)；三重等价解释=SPD测地线(log-EU与affine-invariant在此路径重合)+热核+谱滤波
  - 蒸馏预训练：fMRI-BERT学生窗口 vs 全录音teacher vec(FC^α*)，对齐Gram矩阵K_s=EEᵀ/K_t=ZZᵀ(免正样本免增强)，162数据集约4000小时fMRI，10×少参数打平最佳BFM，短扫描/小队列/fingerprinting全面胜出(0.762→0.895)
  - **Activation**: functional connectivity, eigenvalue recalibration, spectral filter, kernel ridge regression, fMRI phenotype prediction, brain foundation model, distillation pretraining, connectome spectrum, fingerprinting, kernel target alignment, SPD geodesic, heat kernel

### Traversing the solution space of neural networks with Hessian Null Space Continuation
- [[hessian-null-space-continuation]] - 单个训练网络周围藏着高维函数保持自由度：function-matching loss的Hessian近似零空间(λ_i≤μ_rel·λ₁)内移动几乎不改输入输出但内部表征剧变。HNC=零空间平步θ̃=θ+ηd+GD恢复函数交替迭代，可软投影(I+H/μ)⁻¹∇φ向任意目标φ转向 (arXiv: 2609.38081)
  - ViT-S/16 ImageNet：权重范数只动1.3%、top-1掉<1%，但端点表征与anchor的CKA相似度低于所有独立训练模型甚至随机初始化ViT——Platonic表征趋同可能是optimizer偏置采样窄解集的证据而非任务决定的唯一表征
  - RL双杀：Plume Tracking滑到羽流边缘平滑追踪(替代surge-cast，OOD稀疏气味/换风向下反超anchor)；Boat Race暴露reward-hacking策略(单箭头格反复进出刷proxy reward零净进度)——好策略附近就藏着奖励设计欠指定
  - 几何测量：有效零空间比例随宽度增、随类别数减；归一化曲率dᵀHd/(nC)任务越难越大——大模型局部解更多但训练收敛到更少(调和Huang2025与Huh 2024矛盾)
  - **Activation**: mode connectivity, Hessian null space, function-preserving traversal, representational degeneracy, loss landscape geometry, reward hacking exposure, CKA steering, model editing, implicit bias, Platonic representation hypothesis, alternative solutions
## 2026-10-01 - Systems Engineering × Quantum III (Cron Job)

### Circuit-level benchmarks of GKP-concatenated qLDPC Codes
- [[gkp-qldpc-circuit-benchmarks]] - 统一三噪声层级仿真框架对比GKP内码×qLDPC外码(BB vs tricycle)级联方案：码容量→方差聚合→调度解析电路级噪声，analog-informed BP-OSD在每个模型每个码族都优于硬判决 (arXiv: 2609.35282)
  - 4组件处理栈：内层GKP纠正产出二进制Pauli转移+连续可靠性LLR；Tanner边作为SUM门执行外码综合征提取；analog信息(折叠残差z)保留为解码器先验而非二元舍入丢弃
  - 核心系统工程洞见：外码性能不能只看块参数(n,k,d)——校验权重、Tanner结构、门调度深度、SUM门位移传播、解码器先验共同决定有效外码噪声；BB电路级analog交叉点σ≈0.212(10.46dB)优于tricycle 0.142(13.94dB)
  - 可复用工作流：外码仅通过CSS校验矩阵H_X,H_Z接入(全管线码族无关)→码容量模型廉价筛选σ窗口→方差聚合捕获权重依赖暴露→调度解析电路验证后才可做FT声明；硬判决/analog在同一采样噪声实现上配对比较
  - **Activation**: GKP code, qLDPC, BB code, tricycle code, bosonic error correction, analog-informed decoding, BP-OSD, circuit-level noise, syndrome extraction, displacement propagation, squeezing threshold, finite-size crossing, concatenated codes, fault tolerance benchmark

## 2026-10-01 - Neuroscience Research II (Cron Job)

### Neural Structural Reasoner: A Brain-inspired Architecture for Reasoning over Structured Knowledge
- [[neural-structural-reasoner]] - 关系结构直接编码在四层耦合神经元群(实体LE/推理LZ/关系LR/组合LC)的连接里做KG多跳推理：Heaviside门控+路径积分式状态转移，对称Oja规则学关系等价，三步闭环检测r_p∘r_q⇒r_k组合规则；静态图有精确闭式解Alg.3（邻接矩阵稀疏积S=A_ri·A_rj），Nations 3秒训练 (arXiv: 2609.36620)
  - 推理=离散可读激活序列：LR一次迭代检索等价关系(equivalence置信度=激活值)→LZ动力学路径积分→LE读出尾实体，激活轨迹即计算过程，错误可在发散步审计；max/sum路径支持度聚合（验证集选模式）
  - 涌现双重潜在结构：组合规则置信度区分语义稳定桥(exportbooks+releconomicaid→embassy=0.93)vs高频共现(embassy²失败)；W_ZZ连接PCA无监督恢复Nations冷战地缘 blocs
  - 诚实报告：数据集依赖性（Nations/YAGO近最优0.814/0.589，Kinship弱0.652），卖点=精度/3秒级训练效率/原生可解释性三角权衡；局限：离散符号三元组、组合规则发现组合爆炸
  - **Activation**: knowledge graph reasoning, link prediction, relational structure, path integration, Hebbian learning, Oja rule, compositional rule, brain-inspired architecture, interpretable reasoning, Tolman-Eichenbaum, cognitive map, entity relation, multi-hop inference

### Context-dependent time-series prediction via HyperReservoirs
- [[hyperreservoir-context-dependent-readout]] - 上下文不该改表征而该改解码：主reservoir(观测动力学)+小context reservoir(纯上下文驱动)，双线性读出ψ=[h_R;h_H;h_H⊗h_R]使W_eff(h_H)=W_R+Σh_H,m·B_m成为上下文参数化的仿射读出族，全部仍单次ridge回归零反向传播 (arXiv: 2609.34847)
  - 三种上下文注入点taxonomy：输入级(context-input ESN)/状态级(full-matrix Conceptor C_k=R_k(R_k+γ⁻²I)⁻¹)/读出级(HyperReservoir)——Conceptor假设regime可由状态分布区分，时间缩放ṡ=ν·f(s)保持轨道几何故慢/快Conceptor对齐(S_C=0.813)时状态级调制失效
  - 共享吸引子不同速度任务最大优势：HyperReservoir全三任务最低cNMSE，同吸引子场景Conceptor比朴素ESN差一个数量级；Augmented>Concat/Strict消融证明加性+双线性缺一不可
  - 严格对照协议可复用：总reservoir维数恒定N+M=120、M验证选5-10足够（非单调：context reservoir过大反而损害）、R_ctx错误上下文替换比最小=真正功能使用上下文、跨regime共享归一化防预处理泄漏regime身份
  - **Activation**: reservoir computing, echo state network, context-dependent prediction, bilinear readout, hypernetwork, Conceptor, temporal scaling, multifunctionality, regime switching, time series prediction, physical reservoir, ridge regression

## 2026-10-01 - Systems Engineering × Quantum II (Cron Job)

### The Overlap Gap Property: Separating Quantum and Quantum-Inspired Approximate Optimization Algorithms
- [[ogp-separating-quantum-inspired-optimization]] - OGP刚性分离两类算法：MF-AOA嵌入有限记忆AMP框架被Gamarnik-Jagannath定理阻塞，QAOA以超多项式深度穿越OGP屏障；发现参数schedule在屏障附近从绝热跳变到非绝热的不可微点 (arXiv: 2609.35131)
  - 模式1 有限记忆AMP归约：经典启发式迭代写成U^t=F_t(J(·,f_t(U^0..U^{t-1})),U^0..U^{t-1})，旋转矩阵正交性给出Lipschitz K=2√T（与N无关），催化场仿射项max s²(1-s)=4/27 → 直接继承OGP阻碍定理
  - 模式3 深度临界点：N=15实例p*≈28处approximation ratio出现kink，最优(γ,β)从线性绝热schedule跳到非绝热分支；按(p−p*,F_p−E_OGP)对齐所有实例证明是共性而非涨落；换优化目标为ground-state overlap则kink消失
  - 资源估计：N=50需p≈250层穿屏障，但IBM Heron相干极限p_T2=13–33（T2=300µs,t_2Q=200ns,D_p=G_p/(Δ+1)）→ 当前超导硬件在到达OGP屏障前耗尽相干时间；TTS=p/P_p在有限深度(28–52)取最优，盲目加深适得其反
  - **Activation**: overlap gap property, OGP, QAOA depth barrier, MF-AOA, AMP obstruction, adiabatic non-adiabatic transition, clustered solution space, Max-4-XORSAT, resource estimation, coherence limit, quantum advantage boundary

## 2026-10-01 - Neuroscience Research (Cron Job)

### NeuroDyn-EEG: An Interpretable Pre-trained Model for EEG Based on Neural Dynamics
- [[neurodyn-eeg-neural-dynamics-pretrained]] - 用90节点双时间尺度Jansen-Rit神经质量模型生成合成"参数-EEG"对做预训练，从19导头皮EEG直接反演90个AAL脑区×11个生物物理参数场+全局延迟，仅2.43M参数在PD31/MDD全面超越LaBraM/BrainOmni等基础模型 (arXiv: 2609.36773)
  - 确定性SBI点估计：MAE损失在先验×仿真器分布下收敛到分量条件中位数（后验点摘要），避开NPE全后验估计的巨大仿真预算和SBC校准开销；反演网络=多尺度时域conv+leadfield伪逆源空间分支+频谱分支+节点自注意/交叉注意
  - 疾病参数签名：AD65以C1（锥体→兴奋性中间神经元连接，37/90区，DMN/边缘/皮层-丘脑，支持AD失连接综合征）为主；MDD以θ（群体放电阈值，23/90区，前额-边缘，E/I失衡）为主——FDR校正后的"参数×脑区"假设检验替代纯分类
  - 诚实局限：sigmoid族参数(θ,β,rmax)可辨识性天花板r≈0.7；1/f粉噪是最坏噪声源；生成式生物物理约束过滤伪迹导致TUAB广义异常检测偏弱；闭环重建一致性≠唯一可辨识性
  - **Activation**: neural mass model, Jansen-Rit, simulation-based inference, EEG foundation model, interpretable EEG, parameter inversion, source localization, leadfield, AAL atlas, Alzheimer EEG, depression biomarker, FDR case-control

## 2026-10-01 - Systems Engineering × Quantum (Cron Job)

### Quantum Monte Carlo Tree Search with Fixed Confidence
- [[quantum-mcts-fixed-confidence]] - 量子MCTS定置信度识别：lazy-measurement原则+几何阈值消除+QMC叶子估计，查询复杂度对有效难度从二次降到线性（近最优），Hybrid按(α,η)成本公式逐叶切换经典/量子 (arXiv: 2609.33132)
  - 三设计支柱：lazy measurement（每轮只测一次防态坍缩破坏优势）、QMC子程序 O((1/α)log(1/η)) vs Hoeffding O(1/α²)、γr=2⁻ʳ阈值消除+ηr=δ/(2Lr²)逐叶置信预算
  - 匹配界：上界 O(Σ 1/dℓ,ε) 与下界（新序列量子相位测试技术，pivotal leaves）在一致关键实例上对数因子内匹配；Lichess深度11树Hybrid 11.7M查询胜QMCTS 35.1M/CMCTS 47.1M；IBM真机4.5×优势
  - 姊妹篇2609.35511（量子随机博弈expectiminimax嵌套）：去随机化多级MC望远镜求和+相干二分搜索，两个二次加速(√deg, ε⁻¹)在嵌套中同时存活——RMSE↔uniform转换引理是组合关键
  - **Activation**: quantum MCTS, fixed confidence, lazy measurement, quantum query complexity, best arm identification, threshold elimination, hybrid classical-quantum, expectiminimax, multilevel Monte Carlo, coherent binary search

## 2026-09-30 - Medicine × Quantum II (Cron Job)

### Hybrid quantum-classical attention for histopathology-based molecular profiling
- [[qdsm-quantum-attention-molecular-profiling]] - 用量子衍生双随机矩阵(QDSM)替换transformer的softmax注意力，从常规H&E病理图像预测基因表达，29个TCGA队列验证、小队列增益最大 (arXiv: 2609.21115)
  - 核心结构对应：双随机矩阵=幺正过程振幅平方——量子硬件是这一注意力原语的天然来源；IBM量子处理器单独复现了QDSM原语
  - 选择性再分布而非均匀提升：QDSM把预测精度在基因/通路间重新分配（部分肿瘤改善、部分恶化）；肾上腺皮质癌中优先改善的基因富集于总生存期不良关联——分子推断命中预后相关生物学
  - Leave-one-cancer-out混合效应分解：基线分子特征预测部分基因级收益，残差识别癌症特异性程序；跨队列迁移诚实报告：胰腺癌上未一致改善
  - **Activation**: quantum attention, doubly stochastic matrix, QDSM, histopathology, gene expression prediction, molecular triage, TCGA, small cohort, precision oncology

### Improving Sample Efficiency in Peptide-HLA Binding Prediction with HQNN
- [[hqnn-peptide-hla-binding]] - 并行量子特征提取器+量子分类头的HQNN做肽-HLA结合预测（新抗原识别关键步骤），参数匹配对照下全训练规模胜出且数据越少优势越大 (arXiv: 2609.19642)
  - 低数据优势曲线判据：量子增益随训练集缩小而扩大是归纳偏置有效的指纹——平坦或收窄则宣告失败；多源生物特征编码分载到并行浅PQC分支（NISQ友好+可消融）
  - 噪声感知仿真预检：真实硬件噪声下仅轻度退化=NISQ可行；诚实边界：仅测试2个HLA等位基因，数据充足时经典CNN仍占优——量子价值仅限低数据场景
  - **Activation**: peptide-HLA binding, neoantigen, immunoinformatics, HQNN, sample efficiency, low-data regime, quantum feature extractor, parameter-matched baseline

### Experimental evidence of generalization in quantum ML in small-data regime
- [[qcnn-small-data-generalization]] - 硬件兼容QCNN（中途测量+经典前馈）小数据泛化实验证据：10个训练样本即可学习；45参数匹配下QCNN学会而经典CNN停留在随机 (arXiv: 2609.24666)
  - 编码瓶颈审计：2×2→512×512跨分辨率transpile暴露主导约束——振幅编码省比特但深度爆炸、角度编码浅但比特爆炸，真实瓶颈是数据编码而非优化
  - 诚实三角：参数匹配赢、无约束经典基线(2.5万参数)在数据充足时仍最强、BreastMNIST上QCNN未超越但用少数量级参数持续高于随机——报告交叉点而非只报赢面
  - **Activation**: QCNN, small-data generalization, amplitude encoding, angle encoding, mid-circuit measurement, Caro bounds, encoding bottleneck, BreastMNIST

## 2026-09-29 - Neuroscience × Quantum late batch (Cron Job, pending sync)

### Certified Mixing Analysis of the Drosophila CNS Connectome
- [[connectome-synapse-flow-certified-mixing]] - 果蝇CNS连接组随机游走混合证书：Dobrushin系数+谱隙认证混合时间边界，识别近闭集与边界集 (arXiv: 2609.33054)
  - **Activation**: connectome, random walk, Dobrushin coefficient, spectral gap, mixing time, certified bounds

### High-Rank Connectivity Scaffolds in Recurrent Neural Networks
- [[high-rank-connectivity-scaffolds-rnn]] - 高秩RNN连接支架：SVD分解区分核心支架与冗余模式，支架决定路径整合等任务的泛化与纠错 (arXiv: 2609.35207)
  - **Activation**: low-rank RNN, high-rank connectivity, singular value decomposition, path integration, mode decomposition, core scaffold

### Purin — Split Synaptic Efficacy + Bounded Short-Term Factor for ANNs
- [[purin-synaptic-efficacy-ann]] - 短时程突触可塑性注入标准CNN：分裂突触效能+有界短期因子，稳态调节提升小样本鲁棒性 (arXiv: 2609.31235)
  - **Activation**: short-term plasticity, synaptic efficacy, CNN, homeostatic regulation, small-sample robustness

## 2026-09-30 - Neuroscience Research (Cron Job)

### A neural network that maintains and retrieves memories based on context
- [[context-modulated-emrnn-memory]] - PFC式上下文双重调制记忆：低秩门控共享RNN连接（工作记忆）+ 缓冲区显式存储上下文做content×context乘性检索（情景记忆），测试期无标签贝叶斯推断上下文，fMRI/人类"aha"检索数据双重验证 (arXiv: 2609.37791)
  - 调制位置是第一性设计变量：调制循环动力学(WM)远胜输入/输出调制（脑对齐 0.0087 vs 0.0039/0.0053, t(32)>9, FDR p<.0001）；低秩门控共享W0优于每上下文独立连接——轨迹更直(tortuosity t(19)=5.5)、维度更低、上下文端点更正交
  - 分工加速律：EM缓冲区显式存储π后，键值系统无需隐式学上下文，人类式检索快4倍（r=0.2 @22 iter vs 94）；但增益依赖检索选择性（softmax τ=0.1，τ↑或无softmax退化为基线）；单WM调制反而伤检索(0.207 vs 0.265)——机制收益以全系统为条件；门控检索分数而非key/query变换(0.139 vs 0.283)
  - **Activation**: context modulation, low-rank RNN gating, working memory, episodic memory, key-value memory buffer, Bayesian context inference, PFC hippocampus, naturalistic fMRI, RSM similarity, memory-augmented network

### An adaptive fractional state links circuit mechanisms to cortical dynamics across the visual hierarchy
- [[adaptive-fractional-state-cortical-dynamics]] - AF态：重尾超扩散+长程记忆+振荡共存的皮层工作态，双分数均场理论(bFNS)统一5种经典随机描述，把"层级时间尺度"升级为(a,b)动力学regime平面 (arXiv: 2609.37355)
  - 反直觉判据：LFP超扩散(a=0.62>0.5)与浅谱(b=-1.75>-2)对高斯过程是矛盾的（高斯超扩散要求b≤-2）——唯一解是重尾增量（κ=0.35 vs 傅里叶代理0, p<1e-20）产生超扩散、长程记忆产生浅谱，非高斯与非马尔可夫必须同时存在
  - 层级二维轴：视皮层自下而上扩散指数a降(0.62→0.51)、谱指数b升(-1.75→-1.57)反向联动（L2/3 Kendall τ_a=-0.40, τ_b=+0.60），电路机制=有效抑制渐进减弱（I:E比δ），时间分数阶β主导位移方向；深层消失且L6符号反转——浅层特有
  - **Activation**: adaptive fractional state, bFNS, bi-fractional mean field, superdiffusion, MAD increment exponent, cortical hierarchy, Neuropixels, E:I balance, exploration-exploitation, anomalous diffusion

### Which Attention Heads are like the Human Head? Not the Ones that Compute
- [[brain-alignment-causal-dissociation-attention-heads]] - 脑对齐≠因果重要：17个LLM上脑对齐注意力头的移除损害不足FV头的1/3（12.8pp@24.5% vs 42.6pp@12.5%），对齐捕获的是"模型怎么读刺激"而非"怎么解题" (arXiv: 2609.37991)
  - 两族注意profile：novelty头盯独特元素、与人类注视全模型正相关(ρ=.373)但移除比随机消融伤害更小（潜在spandrel，softmax强制分配注意）；repetition头与概念表征共变(ρ=.45)但移除后模式信息仍100%可解码
  - 可复用审计协议：对齐分+因果分独立计算→交叉相关→两排序消融对随机基线，报告解离——诚实负结果范式；指令微调会翻转对齐-概念关系（Qwen instruct全负）
  - **Activation**: brain-AI alignment, causal ablation, attention head interpretability, FRP EEG, function vectors, concept vectors, novelty heads, spandrel, alignment audit

## 2026-09-30 - Medicine × Quantum (Cron Job)

### Quantum Diffusion Models for Medical Image Analysis
- [[dtqw-diffusion-medical-imaging]] - 量子行走前向扩散 + 经典U-Net反向去噪的混合量子扩散模型，在真实IBM NISQ硬件上验证 (arXiv: 2609.31070)
  - 反直觉设计：NISQ设备噪声被用作前向过程收敛的必要资源（纯幺正DTQW可逆、永不收敛到均匀先验，退相干补上缺失的耗散项），无需纠错
  - 加性行走扩展：DTQW固定从|0⟩出发、采样结果加到各像素初始值（mod 2^Nq），一次量子运行摊销到全部像素——绕过其他QML医学工作卡死的输入编码尺寸瓶颈
  - 结果诚实解读：KL散度全数据集优于经典对照（FractureMNIST3D上KL 0.011 vs 0.047，FID 89.7 vs 100.1），2D的FID较差但Inception-v3特征本身不适合医学数据；αt调度的CE+KL混合损失（高t学分布、低t学结构）
  - **Activation**: quantum diffusion model, DTQW, discrete-time quantum walk, noise-as-resource, additive-walk scaling, medical image generation, NISQ forward process, BloodMNIST, BraTS2020, FractureMNIST3D

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