## 2026-10-10 - Neuroscience Research (Cron Job)

### CoHyFuse: Condition-wise Hypergraph Fusion with Global Connectome in Task-fMRI
- [[cohyfuse-condition-hypergraph-taskfmri]] - 任务态决定超图关联结构本身：每个任务条件独立构建 top-K_q 超图（同一 ROI 在不同条件加入不同 ROI-集超边），注意力融合 + 全session FC 双分支 (arXiv: 2610.05913)
  - 条件级 FC（跨 block 池化 TR 后 Pearson+Fisher-z）→ FC-profile 行向量编码 → 以负欧氏距离的 top-K_q 邻域定义超边（E=V，锚点自隶属=1，其余 K_q·softmax(s/τ_q)，τ_q 可学习）；K_q 按条件独立搜索，最优 (ENC,DISC,REC)=(50,45,5)——编码/分心需宽邻域、回忆需窄邻域，任何共享 K 都显著劣化
  - AABC N=1074：FACENAME 流体认知 FCC 预测 7.83±0.10 MAE / R²=0.439（超 TA-GAT，bootstrap p=0.004）；VISMOTOR 年龄预测 R²=0.592；CMI-HBN ADHD 三分类 72.0% mAUC（+4.0 pts 超 STNAGNN）；操作子对照证明超图关联聚合本身有价值（同输入 GCN 8.13/GAT 8.07 vs HGNN 7.83）
  - 遮挡归因定位 DIST 条件为预测主驱动（SAN–FPN 与 within-SAN 动机），DIST 子网络强度–FCC 关联最强 r=0.36 且经年龄/运动校正存活（FDR q≤0.018）；混淆对照：age/sex/FD-only 模型 R²=0.25
  - **Activation**: task-fMRI, hypergraph neural network, condition-wise FC, incidence matrix, brain-behavior prediction, ADHD classification, K_q neighborhood, SAN-FPN, brain network, Yeo-7

### Sedima: Cross-Run Hierarchical Insight Memory for Evolutionary Search Agents
- [[sedima-hierarchical-insight-memory-evolutionary-search]] - LLM 进化搜索的持久三层洞察记忆：原始轨迹→蒸馏洞察→语义聚类（注意力加权质心），写后读前两个 hook 即插即用，不改任何搜索算子 (arXiv: 2610.02361)
  - Level 1 原始轨迹（step/适应度差/评估报告，不解释）→ Level 2 LLM 蒸馏为问题级（首次评估）与变更级（每次父→子）洞察并回链证据 → Level 3 余弦≥0.80 入簇否则新建；质心用非参数注意力权重 w_i=softmax(s_i/τ)（s_i 为成员间平均余弦中心性，τ=0.10，τ→∞ 退化为均值池化）
  - 检索：查询嵌入→top-3 簇（余弦≥0.60）→每簇 top-3 洞察→保留簇级与洞察级分数→附最多 2 条原始轨迹→LLM 合成 3 条建议（2500 token 封顶）；无簇过阈值则回退原始 prompt（记忆严格可加性）
  - 20/20 模型-harness-基准组合全部胜出（符号检验 p=1.9e-6；GPT-5.4/DeepSeek V4 Pro/Gemini 3 Pro/Qwen 3.7 Max/Qwen 3 Coder × OpenEvolve/ShinkaEvolve）；AlgoTune +5.5%、ALE-Bench LITE +6.6%（固定 100 候选预算），平均节省 32.3% 迭代达基线最优；弱模型获益最大（Qwen 3 Coder +11.0%）
  - 冷 vs 同域热 vs 跨域热记忆（1.67/1.75/1.70）分离地证明持久性与跨问题家族迁移；随机检索对照≈无记忆（1.62 vs 1.61）证明增益来自相关检索而非 prompt 填充
  - **Activation**: evolutionary search, LLM agent memory, insight distillation, cross-run transfer, semantic clustering, OpenEvolve, program synthesis, experience reuse, attention-weighted centroid
## 2026-10-10 - Economics & Investment (Cron Job, evening)

### Robust distortion riskmetrics under Wasserstein ambiguity
- [[distortion-riskmetric-wasserstein-dro]] - 解决公开问题：仅用 Wasserstein 球作模糊集、对无凸性/单调性/连续性假设的 distortion riskmetric 类做 DRO，给出三层求解序列 (arXiv: 2610.09622)
  - 层级1 凸化精确性判据（Thm 1）：把非凹 distortion 换成凹包络保持最坏值 ⟺ 参考分位数 G0⁻¹ 在包络间隙区 I_h 上平坦（p>1）；不平坦时现有凸方法是严格上界，"额外保守性"是方法伪影
  - 层级2 正则化序列（Thm 2）：S_h(ε)=lim_{η↓0} S_{h_η}(ε)，最坏分布子列弱收敛到 F*（h≠h* 时 sup 可不取到，left-VaR 为典例）；层级3 显式近似+可计算误差界（Thm 3）：零优化构造 P_ε，误差界 O(ε^−min{p−1,1})，绝对连续 h 时 O(ε)
  - 鲁棒性价格线性于半径：S_{h*}(ε)=ρ_{h*}(G0)+ε·‖ψ_{h*}‖_{p'}（分位密度对偶范数定价）；投资组合应用：椭球基准下 d 维问题坍缩为 1-D 最坏值评估 + SOCP 外层（每个组合面对同一 1-D 问题、不同有效半径 ε‖ω‖_{r'}/s_ω）
  - **Activation**: distortion riskmetric, wasserstein ambiguity, distributionally robust optimization, nonconvex risk measure, concave envelope, convexification exactness, signed choquet integral, VaR, RVaR, prospect theory distortion, deviation measure, robust portfolio selection, SOCP, regularization sequence, error bounds

## 2026-10-10 - Neuroscience Research (Cron Job, night)

### Multimodal Physiological Decoding Reveals Individualized Arousal Dynamics in Closed-Loop Neurofeedback
- [[peripheral-arousal-decoder-yerkes-dodson]] - 外周生理信号（HR/HRV/呼吸/EDA/瞳孔）解码唤醒优于 EEG（93.0% vs 85.2% vs FBCSP 79.8% AUC），且唯一恢复 Yerkes-Dodson 倒 U 曲线——提出"效度先于精度"的闭环解码器标准 (arXiv: 2610.04113)
  - LC-NE 系统直接驱动自主神经输出，外周信号是其原生效器读出；EEG 叠加仅 +1.2 AUC 点，Integrated Gradients 显示 EEG 归因近零（还规避 gamma 频段 EMG 混淆）；FBCSP 解码器学的是任务难度而非分级唤醒（optimum 随难度漂移 62→76，闭环控制变量失准）
  - 闭环重新框架化：BCI/sham/silence 条件的唤醒轨迹无差异（p>0.10）但 Faller 实验有 +7s 性能收益 → 反馈机制是"关键时刻定点调节"而非持续水平位移；时变最优轨迹 â(t)（随任务难度上升）+ 偏离指标预测性能（r=−0.28~-0.24）；基线 HRV+gamma 表型分层个性化控制带宽（敏感组 ×1.5 SD、耐受组 ×2.5 SD，Cohen's d 1.21→1.32 / 0.85→1.10）；驻留时间中位数 6s 为反应式 tVNS 干预（2–5s 起效）提供可行性
  - **Activation**: arousal decoding, peripheral physiological signals, yerkes-dodson, closed-loop neurofeedback, heart rate variability, lc-ne, tvns, personalized control band, bci, neurofeedback mechanism

### The Score Is Not the Structure: Brain Alignment and Cross-Lingual Transfer
- [[correspondence-score-audit-alignment]] - 表征相似度分数的三重审计：内容消融（打乱目标恢复 83–92% 的脑对齐 CKA 分数）、仪器检查（探针精度随类型学距离 r=−074 共变）、推理单位（Mantel 实体置换 p=0.0006→0.155）(arXiv: 2610.03827)
  - k/n 基线定律：两个 rank-k 子空间在 n 句子上的 CKA ≈ k/n（实测 rank 32/64/128/256 处 0.051/0.102/0.204/0.409，误差<1%）——任何对 rank-k 目标的 CKA 必须随附 k/n 基线，rank 256 时零对齐基线即 0.41；脑特异增量仅 +0.03~0.07（可分离地真实但极小）
  - 跨语言案例：探针在 4/17 语言处于随机水平（Hindi/Urkish/Turkish/Arabic——恰为最远端语言），仪器与预测变量构造性共线 → 梯度不可辨识；语言内 steering +6.21 nats 证明干预有效，但按语言（而非 272 对）作单位时距离梯度效应消失（p=0.155）；审计后脑对齐在 BLiMP 上无增益（等价界 [−0.4,+1.4]），四个 null 解释（噪声/调参/规模/惰性）全部被排除
  - **Activation**: cka, brain alignment audit, representational similarity, probe reliability, mantel test, cross-lingual transfer, shuffled target control, rank-k baseline, alignment training objective, correspondence validity

## 2026-10-10 - Neuroscience Research (Cron Job, evening)

### Understanding Latent-Dimension Scaling in Dynamical-System Learning through Spectral Reliability
- [[koopman-spectral-residual-scaling]] - Koopman autoencoder 用 spectral-residual loss（ResDMD 相对残差）替代 latent-prediction loss，使 latent dimension 扩展可靠地降低 rollout 误差 (arXiv: 2610.11866)
  - 谱污染诊断：一步预测误差下降但 rollout 失败，源于伪特征对散布在高残差区；spectral-residual loss 用 held-out 批评估候选特征对的相对残差，强制特征值落位低残差区（谱可靠性）
  - 6 个混沌系统 30/30 案例中位 VRMSE 更低（N₀→16N₀ 降幅 10%–76% vs 2%–52%），VPT 全系统全维度更长（1.06–5.21×）且随维度非降；理论：有界 Koopman 算子下学习字典空间最小残差逐点收敛到全空间下确界
  - **Activation**: koopman autoencoder, spectral reliability, relative residual, resdmd, spectral pollution, latent dimension scaling, rollout error, pseudospectrum, spurious eigenpair, neural latent dynamics

### Stochastic resonance in adaptive dynamical networks
- [[adaptive-coupling-stochastic-resonance]] - 自适应耦合（含 memristive 实现）作为随机共振的柔性控制旋钮：γ 可增强/抑制 SR 并将最优噪声强度平移约 2 个数量级 (arXiv: 2610.11367)
  - 三种耦合族统一框架（现象学局部×2、全局、三次 memristor）：增强-抑制对 γ 呈共振式（局部 γ≈10⁻²、全局 γ≈0.2 最优）；机制 = ⟨σ⟩ 随 γ/D 单调升而振荡幅度不变 → 自适应动力学等效于强度 ⟨σ⟩ 的静耦合
  - 拓扑权衡：全局耦合峰值 SNR 更高但过峰后抑制更陡；memristive b 参数效应随总强度 s 翻转（弱 s 增强SR、强 s 抑制SR）；σ 的衰减项 −ασ 不可或缺（否则耦合无界增长+极端多稳态）
  - **Activation**: stochastic resonance, adaptive coupling, memristive coupling, bistability, snr curve, optimal noise intensity, coupling topology, noise-induced dynamics, short-term plasticity mapping

## 2026-10-10 - Neuroscience Research (Cron Job)

### From Communication to Computation in Neurons-on-a-Chip: Neurotopomorphic Computing
- [[ic3-neurotopomorphic-neurons-chip]] - IC³ 框架：制造前先在仿真中筛选活体神经元电路拓扑——稀疏定向链击败全连接网络 (arXiv: 2610.06065)
  - 反直觉核心结果：IC³（动力学 0.60 + 通信 0.30 + 结构 0.10 八观测量加权指数）和 TE 均与分类任务负相关（ρ −0.73~−0.81）；Sequential Chain 和 Microchannel Diode 仅招募 1/3 可达神经元却取得最高解码分——约束传播反而保住输入区分度
  - 九架构基准（15 神经元 Izhikevich，20 seeds/架构）：结构可达 ≠ 功能招募（差 0.264）；潜伏期对物理路径延迟超线性（β=1.68）；out-closeness 越高响应概率越低；扩展 readout 到全网无任何增益（下游活动冗余）；无训练条件下九架构均无 fading memory（η²=0.029）——输入保真与持久性对递归的需求不同
  - **Activation**: neurons-on-a-chip, neurotopomorphic computing, ic3 framework, microfluidic neural circuit, reservoir computing substrate, transfer entropy, network architecture design, bio-spike computing, in silico screening

## 2026-10-10 - Neuroscience Research (Cron Job)

### The Dichotomy Between Pattern Recognition and Step-by-Step Reasoning
- [[debruijn-pattern-recognition-reasoning]] - De Bruijn DAG 统一模式识别与逐步推理的光谱理论 (arXiv: 2610.09186)
  - 推理轨迹 = De Bruijn 图 DAG 子图上的路径；覆盖全部边所需路径数是总轨迹数中消失的小份额 → 样本复杂度 ∝ 边数幂律，短轨迹即可推广到更长任务
  - 状态发射频率权衡：k=1 高精度但扰动下脆弱（26.4%），k=∞ 退化为模式识别但鲁棒（79.4%）；Qwen3-14B/32B 在 15% 滑动窗下保留 >75% GSM8K/MATH-500/GPQA 精度——更大模型隐式 c 更小
  - **Activation**: de bruijn, pattern recognition, step-by-step reasoning, chain-of-thought structure, state emission, reasoning robustness, sliding window attention, sample efficiency reasoning

### Interplay between Excitability and Noise in Analog Spiking Neurons
- [[cmos-analog-neuron-noise-reliability]] - CMOS 模拟脉冲神经元 jitter regime + 热力学不确定关系 (arXiv: 2610.06720)
  - 工业瞬态噪声 SPICE（65nm, 4-fJ/spike, V_DD=200mV）复现 Mainen-Sejnowski 1995：恒定阈上激励 → 振荡 regime，jitter 线性累积；时变阈下激励 → 兴奋性 regime，受控状态转移大幅抑制 jitter
  - TUR 刻画可靠性-耗散权衡：rate-coding 受热力学下界物理约束，temporal/event coding 规避 TUR 获得噪声免疫——神经形态芯片可靠性预算=能耗预算
  - **Activation**: cmos analog neuron, spike timing jitter, excitability regime, thermodynamic uncertainty relation, neuromorphic noise, mainen sejnowski, transient noise simulation, rate vs temporal coding
## 2026-10-10 - Neuroscience Research (Cron Job, afternoon)

### Heterarchy in the Brain: Control as a Spectrum, Not a Chain of Command
- [[heterarchy-brain-control-spectrum]] - 层级控制是把"时间有限的配置"误读为"架构"；控制是关系性、过程特异的，环（cycle）使任何等级分配失效 (arXiv: 2610.04643)
  - 组合失败论证：控制器地位只相对特定过程成立（前提1）；每个元素同时参与多个过程（前提2）；关系成环（前提3）——单个环即击败一切 level assignment。互惠布线≠异层级，需要的是互惠约束（结构彼此塑造对方学什么/表达什么）
  - 控制光谱 = 动态解耦度（行为依赖历史/内部状态/预期后果的程度）；无仲裁者选择：可用时间内率先进入承诺态的回路主导——紧迫性偏好短路径弱解耦回路；约束反应窗到几百毫秒 → 被试表达明知错误的练习反应
  - 方法论批判：模块度最大化预设近可分解性（循环论证）；杏仁核直连 40% PFC 但一步间接达 90%，FC 由 communicability 而非直连预测；会话平均 FC 可能对应系统从未处于的配置
  - 可测试签名：(a) 成对主导影响跨情境反转 (b) 互惠约束（塑造对方学习/表达）(c) 跨情境关系成环——一次可靠反转即否证稳定成对排序
  - **Activation**: heterarchy, brain control hierarchy, cortico-subcortical, dynamical decoupling, effective connectivity reversal, communicability, reciprocal constraint, control spectrum urgency

### Stability of Phase-locked States of Weakly Coupled Izhikevich Neurons
- [[izhikevich-weak-coupling-phase-model]] - 首个化学突触耦合 Izhikevich 神经元的相位模型：discontinuous SNIC / 同宿 / 亚临界 Hopf 三条起始路径 + Class/Type 解离带 (arXiv: 2610.04025)
  - 三条 spiking 起始路径按 b 分层：b<b_dSNH≈1.51 discontinuous SNIC（Class I）；1.51<b<3 重置诱导的鞍-同宿产生双稳带（E₂+大振幅环共存，Class II）；b>3 亚临界 Hopf——平滑子系统无稳定极限环，全部环都由 reset 再注入产生
  - 关键解离：Type I→II iPRC 转换的 b 值远低于 Class I→II 激发性转换 → 存在显著解离带（Class I 激发性 + Type II iPRC）——同步性质由 iPRC 决定而非 F-I 曲线；远离起始点时 iPRC 负叶收缩
  - 锁相结果：b<0.5 仅 in-phase 稳定；b≥0.6 且近起始电流 → in-phase 与 anti-phase 双稳共存；更大 I_app 反相位失稳。降低 β（慢突触衰减）→ |H| 增大收敛加快；小 d 扩展反相位稳定域。全网络仿真全部与相位模型预测一致
  - 实现要点：伴随方程在 reset 面必须加 saltation 跳变条件，否则 iPRC 负叶被静默破坏 → 一切稳定性结论失效
  - **Activation**: izhikevich phase model, weakly coupled oscillators, iPRC discontinuous, phase locking anti-phase, saltation condition reset, bogdanov takens, saddle homoclinic spiking onset, adaptation synchronization
## 2026-10-10 - Economics & Investment (Cron Job)

### Adversarial Training for Deep Hedging in Nonstationary Markets
- [[wrap-adversarial-deep-hedging]] - WRAP 双预算 DRO：φ-散度重加权（场景概率）+ 各向异性 OT 路径扰动（轨迹）正交分解，非平稳市场深度对冲 Far-CVaR 降 19.7% (arXiv: 2610.07162)
  - 漂移感知参考分布：N_eff(w)=1/Σw² 与漂移指数 D_p(w)=(Σw_n(N−n+1)^p)^{1/p} 的取舍，截断多项式闭式最优权重，半径 ε_ϱ=D_p(w)ϱ+O(N_eff^{−ν}) 覆盖下一期分布
  - 联合一阶展开 V=L̄+Υε+√(2/φ''(1))σ√τ：传输项 Υ∝损失对路径扰动的敏感度（场景内），重加权项 σ∝跨轨迹损失离散度（场景间）——显式攻击 = 一个概率乘子 + 一条扰动轨迹/样本，免解内层上确界
  - 实验：非平稳 Heston 中 φ-only −9.6%、OT-only −13.1%、WRAP −19.2%（远期 CVaR）；漂移权重改善全部方法；真实股票 GAD（AAPL 等 5 只亚式期权）10 组合全胜单预算法但增益股间差异大（6/10 降测试熵风险）
  - **Activation**: deep hedging, nonstationary market, distributionally robust optimization, adversarial reweighting, wasserstein transport, drift-aware weights, phi-divergence, two-budget ambiguity, path perturbation, oce risk measure

### Who Leads and Who Collects: Algorithmic Collusion in Markets of Heterogeneous Language Models
- [[heterogeneous-llm-collusion-bertrand]] - 跨厂商异构 LLM 定价合谋实验：组成即处理变量，租金分配反转价格领导权 (arXiv: 2610.11256)
  - 四家最便宜档模型（Gemini/Claude/GPT/DeepSeek）× 4 厂商 logit Bertrand × 11 组合格 × 20 runs × 200 期 = 176k 次调用：同质 Claude/Gemini 市场达垄断租金 72–79%，DeepSeek 24%，GPT 价格漂移超垄断价永不收敛（病理而非竞争）
  - 结构性结论：混合本身不降低合谋（含 Gemini 更合谋、含 Claude 更不合谋）；稳定性由最不稳定者决定（2 家 GPT 使任何市场不收敛）；租金传递序 DeepSeek > Claude > Gemini > GPT 反转锚定排名——锚高价者报复概率仅 0.18–0.22，跟随者低 6¢ 拿走销量
  - 方法论：Δ 利润指数必须搭配价格指数 Δ_p + 5 类结果分类（否则把超垄断定价误判为竞争）；多峰结果 → 全非参数推断（置换检验，run 为单位）；组成 composition 应作为独立处理变量
  - **Activation**: algorithmic collusion, heterogeneous LLM agents, logit Bertrand, price leadership, market composition treatment, tacit collusion, antitrust liability, LLM strategic disposition benchmark

### Multi-period Mean-Expectile Portfolio Optimization under Wasserstein Ambiguity
- [[mean-expectile-wasserstein-dro-portfolio]] - Envelope 定理把最坏 expectile 化为不动点根 → Wasserstein DRO 多期组合精确重构为 4 个 LP (arXiv: 2610.11917)
  - Expectile 是唯一 coherent + elicitable 的风险度量但缺 RU 表示：包络定理 Psi(q)=sup_F[E_F[L]+kappa*E_F(L-q)+]-q 唯一根 + 两段仿射被积函数（斜率差 Delta=kappa_tau 内生）→ 标准对偶 4 个 O(N) 约束 LP
  - 四结构性质：内生阻尼鲁棒性价格（CVaR 固定 1/(1-alpha)，expectile 随超出频率 m/N 衰减）；决策依赖退化阈值 rho_crit(x)；零半径精确恢复；ground metric 选隐式正则——l_inf→集中、l_1→促分散、l_2→SOCP
  - FTSE 90 成分股 3341 样本外日：expectile 在全部 9 参数格 Sharpe 胜过完全匹配 CVaR（rho≥0.005 显著）
  - **Activation**: expectile, wasserstein ambiguity, distributionally robust portfolio, elicitable risk measure, ground metric, price of robustness, degeneracy threshold

### Risk Ceilings and Development Deadlines: Pacing AI under Uncertain Safety Productivity
- [[risk-ceiling-dev-deadline-ai-pacing]] - AI 监管经济学：风险上限与开发期限的可联合承诺性 = 安全生产率门槛 + 客户服务成本 (arXiv: 2610.11093)
  - 危害 lambda=[h(F)+k(F)Fdot]e^{-S} 分解状态/步危害，安全知识 S 以 log-降幅计价；紧 ceiling 要求 takeoff 末端知识存量下界 → 两承诺相容仅当排除弱研究（生产率 bound）
  - learn-then-replay 近最优：常数产出+纯状态风险下仅比必要 bound 多 3.3% 生产率；保证由客户服务支付（7.5 月学习 = 5 年服务价值 4.1%，2 年口径 52%）
  - 固定配置规则（floors/pauses/lag）定日期不定风险，效应随生产率变号——quarter-yield 时 ceiling 反而提高灾难概率 20.1 点；Weitzman 工具选择类比：ceiling=数量工具，配置=价格工具
  - **Activation**: ai regulation, pacing frontier ai, hazard ceiling, development deadline, safety research productivity, learn-then-replay, instrument choice, catastrophic risk

### Measure Now, Mitigate Later: Virtual Error Cancellation for Logical Quantum Circuits
- [[virtual-error-cancellation-logical-circuits]] - 逻辑误差消除 VEC：纯经典后处理 + 双解码器扇区签名权重，免噪声层析免改电路，d=7 抑制 >3 个数量级 (arXiv: 2610.12400)
  - 无偏条件 E[w(s)]=1 + E[w(s)p_alpha(s)]=0 强制负权重；最优滤波器 w*=1-pbar^T Sigma^-1(p(s)-pbar)，开销 C*=1+pbar^T Sigma^-1 pbar；粗粒化下界 K>=M+1 扇区且质心构成非退化单纯形
  - 双解码器划分：实时 MWPM × 离线 MPS 一致→consensus（份额 1-O(p_L)）、分歧→4^n-1 方向扇区；对比矩阵 V 对角占优 → Lévy-Desplanques 闭式权重（w_I>1 放大共识、w_Q<0 抵消争议 shot）
  - 同调间隙谱标度：gapped（解耦 CSS 解码）C*-1=O(p^{(d-1)/2}) 差、gapless（Y 耦合联合解码/gauge 码）C*-1=O(p_L) 最优 η→1（vs logical PEC η≈4、单解码器 η=2）；syndrome 傅里叶保真度 + Jensen 修正收缩估计器 + 对称群参数绑定实现免标定噪声学习
  - **Activation**: logical error mitigation, virtual error cancellation, syndrome records, dual decoder, coarse-grained sectors, homological gap, sampling overhead, postselection bias

### FactorBench: A Portfolio-Aware Benchmark for Automated Factor Mining
- [[factorbench-portfolio-aware-factor-mining]] - 9 种自动因子挖掘方法 × 5 市场 × ~5000 因子：搜索范式的进步不转化为下游价值 (arXiv: 2610.06947)
  - 三层次评估契约：因子层（执行契约→可评分性→日度截面 IC→训练期定向冻结→风格中性化残差 IC）；池层（池内冗余/跨方法趋同/Alpha101 相似度）；组合层（统一选择→等权/验证IC/ridge 组合→多头+美元中性多空含成本回测）
  - 核心诊断：原始 IC ≠ alpha——风格中性化后 R&D-Agent 残差 IC 从 0.0253 崩塌至 0.0011（"风格租借"）；AlphaQCM 保留最多（0.0191→0.0175）且换手最低；LLM 因子池比非 LLM 更接近已发表 Alpha101；Alpha101 本身成本后仍有竞争力
  - 判别规则：long-only CAGR 22-31% 对所有方法都好看（弱判别）；long-short Sharpe（−0.087 至 0.679）才是区分性测试；GP 从与控制变量同源的价量变量中"重新发现"风格
  - **Activation**: factor mining benchmark, residual IC, style exposure neutralization, factor pool distinctness, Alpha101, LLM factor agents, after-cost long-short portfolio, temporal generalization

### When Does Interference Help Learning? Kernel Geometry as a Pre-Experimental Test for Photonic Reservoir Computing
- [[photonic-reservoir-kernel-geometry]] - 几何界定可学什么，对齐决定学到什么：任务无关 kernel 双指标（g + alignment）预实验协议调和四项矛盾实验 (arXiv: 2610.11360)
  - 光谱展宽机制：干涉的带符号振幅相消→涨落去相关→同一方差散布到约 2 倍维度（90% trace：K_Q 61 维 vs K_C 33 维）；g>1 只证明资源存在，不保证具体任务受益
  - g(V) 超线性旋钮（N=2 精确线性 g−1=(s/2)V）；硬件典型可见度 V=0.864 保留 80.3%；S=3×10⁴ shots 即达精确算术；g·λ_min(K_C)≈常数 → 只能在匹配 n 下比较 g（任务级优势免疫：g 降 5.6× 优势不变）
  - 凸性定理排除内部最优：s_K(V) 对任意标记凸（Cauchy-Schwarz 交叉项 s_X≤√(s_Q s_C)）→ 任何报告的可区分性内部最优必是 readout 效应或噪声
  - 盲预测复现 Joly null（预测 +0.015 < 涨落 ±0.017，与发表值差 <10%）；决策规则：g 大且 A_Q>A_C 才值得上硬件
  - **Activation**: photonic reservoir computing, kernel geometry, geometric difference, kernel-target alignment, boson sampling feature maps, HOM visibility, pre-experimental protocol, quantum advantage reconciliation

## 2026-10-09 - Mathematics + Quantum (Cron Job)

### Geometry-optimized hyperbolic codes for modular fault-tolerant quantum architectures
- [[hyperbolic-surface-code-geometry-optimization]] - 自对偶素域 {p,p} 双曲表面码穷举搜索：优选周期边识别在固定资源下倍增码距（η×4），拓扑感知模块化编译满足 RSB/KaHyPar 全部违反的几何约束 (arXiv: 2610.10948)
  - PSL(2,q) 商群构造 + 面顶点对合自对偶，p∈{5,6,7,8}×q<60 穷举 2,304 生成对 → 全局最优 {6,6} [[51330,17112,10]] η≈33.34（vs toric η=1 ×33、vs 双曲 Floquet ×6.65）
  - 核心规则：码距是紧致化（商群生成轨道）的属性而非仅局部镶嵌——{7,7} q=41 不同周期识别给 d=4/6/8，零成本倍增 d、四倍 η；{5,5}/{7,7} 有限序列实现 Delfosse log² 标度（R²>0.996）
  - 拓扑感知编译：对偶图最远播种 + 圆盘条件拒绝 → ≤80 qubit 平面模块；RSB 连通率仅 1.8–11.2%、Mt-KaHyPar 全部违反几何约束；αp 远程门噪声模型下三倍远程错误仅将阈值 0.22%→0.17–0.18%
  - **Activation**: hyperbolic surface code, periodic identification, PSL(2,q), systole optimization, modular compilation, topological disk partitioning, remote gate noise, circuit-level threshold

### Moment Optimization in the Navascues-Pironio-Acin Hierarchy
- [[npa-moment-selection-synergy]] - NPA 矩选择重构为预算感知组合子集选择：边际协同诊断 Δ(S_k) 零成本监测饱和，RBM+REINFORCE（Gumbel top-k）在硬过渡区比 PT 近 5 个数量级 (arXiv: 2607.14755)
  - I3322 暴力真值：改进集中在尖锐过渡窗 5<k≤19，最优 k 子集不能由 (k−1) 最优扩张——贪心全程卡 NPA1 平台；Δ 峰值= 真饱和点（k=8），边际成本平台是陷阱
  - 171 条 (4,4,2,2) Bell 不等式：过渡起始 k≈9–33，"NPA2 bound" 混淆不同收敛体制 → 矩选择式优于层级式；SDP 评估成本低于暴力两个数量级
  - Heisenberg 链：物理局域基对能量可压缩（p=0.3 分数已胜全 NPA2）但对长程关联量不可压缩；NPA4 扩池+局域解暖启动将 C_N/2 认证间隙 7.13e-5→≈1e-6（~100×）
  - **Activation**: NPA hierarchy, moment selection, SDP relaxation budget, synergy diagnostic, RBM REINFORCE, parallel tempering warm start, Bell inequality convergence, ground-state certification
## 2026-10-09 - Neuroscience Research (Cron Job)

### Rethinking the Tradeoff Between Temporal Encoding and Nonlinear Computation in Spiking Language Models (Spora)
- [[spora-binary-temporal-spiking-attention]] - 二进制位值脉冲编码 UBS/BBS：T 个脉冲携带 T bits 容量（vs 计数读出 O(log₂T)），全注意力运算化为移位+累加 (arXiv: 2610.10933)
  - 核心分离：读出权重固定为 2 的幂（保算术结构），阈值+条件衰减 α 拟合输入分区（差分进化+局部细化）；BBS 符号分离+可学尺度 s 可融合进线性权重
  - exp(x/√d) = 2^(x/(√d·ln2)) → UBS 整数指数码 + 幂移位近似 Softmax；核心注意力能耗 116.3→1.71 µJ/层（−98.53%），全模型 11.17 vs 51.41 mJ（4.6×）
  - GLUE：T=4 达 80.9 avg / 44.1 CoLA MCC（超 SpikeLM +1.2/+6.2），T=6 达 82.3/47.4；等预算对比 Static-QAT（同 15 符号态）+6.43 MCC——时间码胜过同字母大小静态量化器
  - **Activation**: spiking language model, binary spike encoding, UBS, BBS, shift-based attention, temporal encoding capacity, accumulation-and-shift

### SPD-MetaFormer is what you need for small-data brain decoding
- [[spd-metaformer-uniform-frechet-brain-decoding]] - 诊断发现 MAtt/GBWAtt 流形注意力学到的权重近均匀（熵≥0.998），证明短序列小数据下均匀 Fréchet 混合即可，注意力可整体移除 (arXiv: 2610.10952)
  - 三重证据：归一化分配熵 H/log m ≥ 0.9988；锁定均匀权重（训练+评估全程）均值差 ≤0.36 分且所有配对 CI 含零；逆对数得分 s=1/(1+log(1+d)) 有界 → 单位温度下任意权重比 ≤ e（结构性限制对比度）
  - 架构：局部协方差记忆 token + 单摘要态角色分离；均匀 LE Fréchet 均值混合器（闭式 exp(Σlog/m)）→ 门控测地线更新 S#_αU → 共享单参数谱收缩 Φ_ρ(M)=M+ρ(tr(M)/d)I（条件数不增，学到版 Ledoit-Wolf）
  - MI 75.44 / SSVEP 70.79 / ERN 82.53 AUC / ABIDE fMRI 79.14，全面超 GBWAtt 等已发表基线；全路径对照证明几何处理链（而非卷积前端或均匀混合本身）贡献性能
  - **Activation**: SPD manifold, Fréchet mean, MetaFormer, EEG decoding, covariance token, manifold attention audit, spectral shrinkage

## 2026-10-09 - Mathematics + Quantum (Cron Job)

### Quantum-Enhanced Inference of Conditional Future Probabilities with Reduced Memory Cost
- [[mrqpe-memory-reduced-quantum-probability]] - 同维度下截断量子模型偏差远低于经典模型，联合 QAE 采样加速实现稀有事件概率估计双优势 (arXiv: 2610.10756)
  - 量子记忆态无需线性独立（D_q < D_c），截断量子模型而非经典模型：偏差地板从不可逾越降为可穿越；纠缠尾 Grover 构造（S_χ 仅作用输出，A/A†/S₀ 须含记忆全寄存器）
  - 8-state 环上游走 D̃=4：经典地板 ~1e-6（N→∞），量子 N≈2e4 穿越地板；16-state 时 ~3000 样本穿越 8e-4 地板；Quantinuum 级噪声下 2-qubit 截断模型胜过精确 3-qubit（门少噪声少）
  - **Activation**: amplitude estimation, state preparation, memory bias variance, rare event, quantum Monte Carlo, model compression

### Quantum non-Markovian response spectra
- [[quantum-nonmarkovian-response-spectra]] - 响应矩阵 R[h,y] 仅凭可访问系统干预即可揭示环境记忆时间结构，介于因果断裂检测与指数代价 process tensor 断层之间 (arXiv: 2610.10684)
  - Markovian ⇒ 秩 1 基线；秩>1 与奇异谱暴露记忆结构/时间位置/reset 存活性；恢复条件下秩与谱匹配 process tensor 无需完整断层
  - 负见证值（SDP 于可分过程上搜索）排除经典前馈记忆模型；条目独立评估 → 并行组装；Ising 基准响应熵跟踪 MPO 键熵
  - **Activation**: non-Markovian memory, process tensor, causal break, response matrix, witness SDP, correlated noise, tomography-free

### On PPT entanglement distillation
- [[ppt-entanglement-distillation]] - PPT 信道纠缠蒸馏的正则化公式与两个单字母逆界，证明 E_d,PPT 可严格小于正则化 Rains 界 (arXiv: 2610.12454)
  - 正则化 POVM 泛函 L∞(ρ)=sup_n L(ρ^⊗n)/n 给出精确可达率；限制到投影测量即回收 Rans 原始界
  - 3×3 Werner 态（反对称权重 25/26）认证分离：0.5836 ≤ E_d,PPT ≤ 0.6211 < R∞=0.64766，否定 Regula et al. (NJP 2019) 猜想
  - 两个逆界技术：算子二次型（张量稳定假设 + little noncommutative Grothendieck 整体应用只损失 1/(2n) 比特）vs 解析族（Hirschman 强化 Hadamard 三线定理 + 环面调和测度边界权）
  - 忠实负性下界 E_d,PPT(ρ) ≥ 1 − h₂(N(ρ)/(1/2+1/(d+1)))，量化"每个 NPT 态皆可 PPT 蒸馏"
  - **Activation**: PPT channels, entanglement distillation, Rains bound, negativity, strong converse, Werner states

### Exact value and rigidity of the 2×3 magic rectangle
- [[magic-rectangle-rigidity]] - 2×3 魔术矩形非定域博弈精确值 (1+√(2/3))/2 与全刚性分类，SoS 证书+会议矩阵自测试 (arXiv: 2610.12001)
  - 精确平方和分解 2rI−S：正系数残差之和给出所有交换算子表示的上界，等式条件确定测量代数
  - 刚性：每个最优策略含 4 维最大纠缠对，会议矩阵（MMᵀ=3I）构造两正交基；NPA 1+AB 层（almost-quantum）已精确
  - 完美预测阈值 β₀=(2+√(2/3))/3：超出 δ 时猜测概率/最小熵/von Neumann 熵皆 Θ(δ) 线性阶
  - 等价于隐藏全输入宇称的 3 比特随机存取码，解决 Chailloux–Kerenidis–Kundu–Sikora 三比特公开问题（1/2+1/√6≈0.908248，修正 Roy–Pan 预印本 0.902369）
  - **Activation**: nonlocal games, rigidity, self-testing, sum-of-squares, conference matrix, random access codes, quantum side information


### Entanglement entropy and magic of ZX-diagrams
- [[zx-diagram-entanglement-magic-bounds]] - Flow 驱动的 ZX-图范式分解，无需张量缩并即可给出纠缠熵双向界与 stabilizer extent 上界 (arXiv: 2610.12447)
  - 范式 |ψ⟩ = U_N···U_1|G⟩ 将图态骨架（F₂ 秩纠缠，可广延）与非 Clifford Pauli gadget（加性有界贡献）分离
  - S ≤/≥ rank_F2(Γ_AB) ± Σ h₂(sin²(φᵢ/2))；魔法界 M ≤ 2Σ log₂(√(1−|sinφᵢ|)+√(1−|cosφᵢ|))，Clifford 极限精确
  - 四步预处理（gadget 融合/stabilizer 融合/Clifford 拆分/单侧排除）；随机电路 300 实现零违例，Trotter 电路 64 步首违例
  - **Activation**: zx-calculus, entanglement entropy bound, magic estimation, stabilizer extent, pauli gadget, graph state, pyzx

### High-Rate Concatenated Quantum Error-Correcting Codes for Qudits
- [[qudit-many-hypercube-qec-codes]] - MHC 码推广到素数维 qudit，LLMD 阈值随 q 单调翻倍至 10.0%（q=13），q-ary 熵竞争分析 (arXiv: 2610.11225)
  - [[6^L, 4^L, 2^L]]_q 级联构造（F_q ≅ Z_q 限素数 q）；逻辑错误率对信道熵 H_q 作图时 level-2 曲线坍缩为单曲线
  - syndrome 丰富度（error-floor 区 +）vs 典型错误权重 ξ=n·ε/(d/2)（waterfall 区 −）的熵竞争解释阈值增强
  - q ≥ 5 出现 waterfall 区（指数>4 超码距估计），q=13 阈值 10.0% vs qubit 5.1%
  - **Activation**: qudit, qudit qec, many-hypercube, concatenated quantum code, llmd decoder, q-ary entropy, waterfall regime, qudit ftqc
## 2026-10-09 - Neuroscience Research (Cron Job)

### If the Brain Were So Simple: Information Enthalpy and the IEP Metric
- [[information-enthalpy-potential]] - 信息焓理论：结构化信息资源最大化作为与 FEP 自由能最小化互补的神经驱动器，IEP 复合度量（熵加权 shuffled-LZC 冗余 + 多尺度统计复杂度）可从脉冲 raster 量化结构化信息供给，直接解决 dark-room 问题 (arXiv: 2610.11142)
  - 信息焓 H_I = κ·Φ_π(C_r, C_st, Γ)：预测资源超曲面（吞吐/存储/结构可用性三重约束下的预测信息上确界），κ 取 Landauer 极限 k_B·T·ln2；存储容量漏斗动力学 C_st,t=(1−α_t)C_st,t−1+C_r,t−1，保留窗口 T_cap=1/α_t 限定预测视界
  - IEP(X) = (1−β)·R^(α)(S̃) + β·C_MS(S̃)：R 为 LZC 短语数对 shuffle 替代子的冗余得分、H_sym^α 熵权惩罚平凡重复，C_MS 为 block-permutation 替代子按 log₂B 积分的尺度持久性 AUC；PSC 权重复制高结构 epoch
  - 验证：Mandelbrot/Julia/Dragon 分形 raster 与 SSC 语音 cochlea 脉冲的 IEP 高于三种随机化对照（permute-time/Bernoulli/permute-all）；n-body 驱动器交互框架给出五态临界景观（亚临界/超临界/超同步/去耦噪声/近临界），高 IEP 输入推动系统趋向临界
  - **Activation**: information enthalpy, IEP, structured information, free energy principle, dark-room problem, neural criticality, lempel-ziv complexity, permutation statistical complexity, intrinsic motivation, dishbrain, closed-loop stimulation

### Learning Infinite Context Windows in Recurrent Architectures via Spatial Neural Computing
- [[spatial-neural-computing-pde-rnn]] - SpatialRNN: PDE-medium (wave-equation) recurrence proven equivalent to a structured ∞-order RNN with robust marginal stability, eliminating vanishing/exploding gradients at fixed parameter count (arXiv: 2610.10690)
  - Medium state ψ_t exactly equals convolution over entire hidden history (W_k = W·W_{k-1} + W̃·W_{k-2} impulse response); O(1) inference memory, 4 fixed matrices
  - Key theorem: block-triangular W/W̃ + symmetric blocks + norm bound ‖W_i‖² + Φ̄‖B_i‖²‖W_ψ,i‖² < 2α_i² locks gradient eigenvalues to circles |λ|=α_i for ALL input-dependent nonlinearities — structurally impossible for any finite-order RNN/HORNN (incl. orthogonal/LSTM/GRU)
  - psMNIST 96.3% with 4-10× fewer params than LSTM/GRU/coRNN; copy task ~99% at all lengths; symplectic α=1 blocks allow exact backward state reconstruction → O(1) BPTT memory
  - **Activation**: spatial neural computing, PDE recurrence, infinite-order RNN, marginal stability, vanishing gradient, traveling waves, wave equation, Störmer-Verlet, selective forgetting, recurrent architecture design

### Cross-Species Representation Learning Aligns Mouse and Human Neural Dynamics and Tracks Clinical Drug Efficacy
- [[cross-species-contrastive-biomarker]] - Dual-rule contrastive learning builds a mouse↔human latent space organized by biological state; frozen geometry retrospectively ranks clinical drug efficacy (ρ=0.87) from mouse EEG drug-response alone (arXiv: 2610.11222)
  - Alignment rule (same biological state pulled together across species, gradient-reversal species suppression) + separation rule (different states pushed apart regardless of species); hierarchy preserves disease-model heterogeneity rather than collapsing it
  - Drug effect = displacement along conserved disease→healthy axis in frozen space: valproate/ganaxolone rescue, failed drugs don't; tiagabine moves AWAY from rescue in absence-like AY9944 (matching known clinical aggravation) while rescuing PTZ
  - Generalizes across modality + aetiology: Fmr1-KO mouse electrophysiology ↔ human 16p11.2 CNV scalp EEG recovers shared hyperexcitability dimension (duplication > deletion > control)
  - **Activation**: cross-species translation, dual-rule contrastive, EEG biomarker, preclinical drug efficacy, translational neurophysiology, supervised contrastive learning, disease manifold, patient affinity, frozen representation

### Lyapunov Spectrum of Random Neural Networks
- [[lyapunov-spectrum-random-neural-networks]] - Full N→∞ Lyapunov spectrum of the Sompolinsky chaotic random rate network via minimum-norm tangent response + cavity method, solving the 1988 open problem (arXiv: 2610.12426)
  - Finite-N identity: cumulative exponent distribution F(s) = trace of one-step response of the minimum-norm solution of shifted tangent dynamics (dichotomy projector), then cavity/DMFT reduces to a self-consistent single-site problem over gain trajectories
  - Establishes extensive chaos analytically: D_KY/N = 1 − F(s_KY), h_KS/N = ∫₀^∞ sF'(s)ds are O(1); recovers circular-law spectrum at fixed point and Sompolinsky/Molgedey λ_max as limits
  - Validated against QR simulations (N=4096, g=3/5, δ=0.05–0.5); first frontier-AI-derived long-open physics result (GPT-6 Astra 100-min autonomous derivation + Claude Opus 5.5 code/text, full prompt published)
  - **Activation**: Lyapunov spectrum, random neural network, Sompolinsky model, attractor dimension, Kaplan-Yorke, entropy rate, extensive chaos, cavity method, dichotomy projector, tangent dynamics

### Mean Field Theory Based on the Spike Time Response Curve for Synchronization Within and Between Two Alternating Populations of Neural Oscillators with Delays
- [[strc-mean-field-alternating-populations]] - STRC mean-field theory extended to two alternating E-I oscillator populations with delayed biexponential synapses; drops phase, uses tonic/phasic decomposition to predict 1:1 locking existence and stability at gamma/ripple frequencies (arXiv: 2610.10977)
  - Tonic (infinite-train minimum conductance) + phasic single-cycle decomposition replaces instantaneous phase-resetting when synaptic duration exceeds network period and pulses summate across cycles
  - Two-eigenvalue stability criteria in pure time units: λ₁ = (1−M'_{A,B})·(within-cluster term), λ₂ = cross-population product; positive MRC slope stabilizes, negative destabilizes — selects which of two intersections survives
  - Key mechanism: shunted I-clusters that cannot self-synchronize (eigenvalue 1.511) are stabilized by reciprocal E coupling (factor ~0.5) — explains E-I generation of ~190 Hz ripples with precisely-timed interneuron assemblies (Huang 2024 optogenetics)
  - **Activation**: spike time response curve, STRC mean field, biexponential synapse, gamma oscillation, ripple oscillation, E-I population locking, conduction delay, synchrony stability, interval response curve

### Neural Decoding as Cognitive Inference
- [[cognitive-inference-neural-decoding]] - 将神经解码重构为受脑内禀先验约束的认知推断：温度缩放 PoE 融合观测表征 o 与皮层几何本征模态先验 u 得到 meta-neural 语义表征 z，在 208 天神经漂移下保持稳定解码 (arXiv: 2610.11923)
  - 推断公式 p(z|o,u) ∝ p(o|z)^(1/To)·p(z|u)^(1/Tu)，z = ω_o·o + ω_u·u 精度加权融合；先验=HCP 32k 表面 Laplace–Beltrami 本征模态（每半球 1000 阶），独立于认知内容构造，按模态（BEM 前向/ECoG 触点最近顶点/fNIRS 通道中点）映射到传感器空间
  - 核心实证：跨会话表征相似度 0.393→0.803 (ECoG 208 天)，位移降低 3–5 倍；语义归因集中于 ~84mm 长波长模态 (ρ=−0.82)；零样本跨被试解码超过 LaBraM/BrainOmni/CBraMod
  - 扩展到内部心理状态：OPM-MEG 想象言语语义相关 0.567 (3 类 48% vs 33%)；自发思维清晰度/生动度/效价预测全超 NeuroSTORM；共享影片去共享成分后残余个体主观相关仍 5/5 维度显著
  - **Activation**: neural decoding, Bayesian brain, cognitive inference, meta-neural semantic representation, cortical geometric eigenmode, neural drift, cross-session decoding, product of experts, imagined speech, internal mentation

### Similar Predictive Fit but Different Latent Dynamics
- [[fit-structure-dissociation-latent-dynamics]] - 个性化 mLTD 潜动态模型揭示拟合-结构解离：癫痫与非癫痫组 held-out 似然完全一致 (−0.991 vs −0.992, p=0.95) 但学习到的转移依赖图密度 62.6% vs 35.4% (p=1.1e-7) (arXiv: 2610.10850)
  - 管线：冻结 CNN–Transformer EEG 基础模型 (TUEG 18,800h 预训练) → 全局 k-means 共享潜状态 (k=4/6) → 每被试独立 mLTD (group-lasso 跨滞后稀疏化, L≤10) → 有向转移依赖图 W_n；W_n 是预测依赖强度非马尔可夫转移概率
  - 双轴评估方法论：预测有效性 (held-out CV LL + next-state AUROC) 与学习动态结构 (依赖密度/自依赖/图特征) 必须分开报告与检验——每滞后拟合均匹配 (p≥0.37) 而结构差异稳健
  - 临床信号：W_n 标量特征分类 AUROC 0.697 (k=4)/0.677 (k=6)；k=4 零模型 29/99 vs 8/99 部分贡献密度差但排除零模型后仍显著 (0.665/0.722)
  - **Activation**: personalized latent dynamics, mLTD, transition-dependency graph, fit-structure dissociation, patient world model, EEG foundation model, epilepsy, TUEP
## 2026-10-09 - Mathematics + Quantum (Cron Job, Friday)

### Quantum codes in the Lee metric
- [[quantum-codes-lee-metric]] - Qudit stabilizer codes for small-shift noise: Lee weight = clock distance min(x, q-x), [[9,1,5]] corrects two X/Z errors where Hamming needs 11 qubits (arXiv: 2610.04834)
  - Joint metric counts Y as weight 2 (bit/phase flips independent); perfect Golomb-Welch CSS families; Eastin-Knill FAILS in Lee metric (perfect Z_10 2-qudit code has continuous transversal gates)
  - Exact Z_q-CSS = multimode GKP correspondence (1 Lee weight = elementary displacement); Clifford Lee-spread = max symplectic column norm; Gray map qubitization sends Z4 Cliffords to level-3 hierarchy (smallest = CLY [[4,1,2]])
  - Lee-LDPC obstruction: energy barrier + noncommuting witnesses O(n) uniformly in q (geometry-of-numbers transference) — large qudit Hilbert space buys no LDPC distance
  - Helical repetition codes (a·x_j = b·x_{j+1}): Lee distance exponential in n; exponentially long memory at any fixed T via energetic confinement (evades Peierls 1D no-SSB, q grows with n) and entropic flat-logical-direction bottlenecks; HGP → 2D local CSS self-correcting for Z errors
  - **Activation**: Lee metric, qudit codes, small-shift noise, Lee-LDPC, helical repetition code, GKP discretization, Gray map qubitization, high-temperature quantum memory

### Quartic Certificates for Pure-State Tomography with Pauli Measurements
- [[quartic-certificate-pure-state-tomography]] - Omitted Pauli support with no commuting zero-sum four-set certifies universal UDA via quartic e4 positivity — finite combinatorial test replaces state-space optimization; exact 3-qubit characterization with 945 minimal failing sets (arXiv: 2610.12320)
  - Kernel criterion: UDP fails iff rank-2 kernel element; UDA fails iff inertia (1,*); e4(A) > 0 forces ≥2 positive AND ≥2 negative eigenvalues → cannot be a pure-vs-anything difference
  - Theorem 1: four-set-free ⇒ e4 ≥ [d(d-2)/8]·Σa_u⁴ > 0 — certification by binary addition + symplectic commutation only; Theorem 2 (n=3): also necessary, all failing sets one Clifford orbit of {IIZ, IZI, ZII, ZZZ} hiding |000⟩ vs |111⟩
  - Theorem 3: commuting omitted supports ⇒ UDP ≡ UDA for any n (Clifford-diagonalize; criterion span_F2 S_Z = F_2^n); n≥4 separation requires noncommuting set containing a four-set
  - **Activation**: UDP, UDA, pure-state tomography, Pauli measurement design, quartic certificate, four-set-free, measurement kernel, Clifford orbit

## 2026-10-08 - Systems Engineering + Quantum (Cron Job, Hour 19)

### QuSema: Detecting Silent Bugs in Quantum Libraries via Quantum-knowledge-enhanced Agents
- [[qusema-semantic-oracle-bug-detection]] - Agentic testing that finds non-crash "silent bugs" in Qiskit/PennyLane using domain semantics + docs as a source-level semantic oracle; 40 new developer-confirmed bugs, 30 silent (arXiv: 2610.10258)
  - All 20 historical silent bugs are API-local (localized to first API transforming valid input into invalid output) — justifies source-level semantic analysis instead of execution oracles
  - Three-stage workflow: contextual unit prep (code segment + docs + call relations) → defect-hypothesis generation from quantum-semantic constraints with execution validation → valid-API triggering and bug qualification
  - QuSema+DeepSeek (15.67/20 relocations, $162) beats Claude Code+Fable 5 (14.67, $425) and Codex+GPT-5.6-Sol (13.33, $117); Opus 5 config 16.00 at $1,603 — 98% of performance at 10% cost
  - **Activation**: quantum library testing, silent bug, semantic oracle, agentic testing, Qiskit, PennyLane, defect hypothesis, API-local defect

### Divide et Impera quantum neural networks for modular hybrid computing architectures
- [[divide-et-impera-modular-qnn]] - Split a wide QNN circuit into k small sub-VQCs plus a classical stitching MLP — same parameter count, fits qubit limits, robust to noise on real EV-charging/air-quality tasks (arXiv: 2610.09623)
  - z = concat of VQC_j(x_Ij) embeddings + shallow MLP stitching; parameter-neutral when regular ansatz partitions features; PCA + sliding-window auto-partitioning when no semantic grouping exists
  - Temporal features in separate circuits beats unified-state processing; two-qubit gate error defines the noise cut-off region (noiseless 53.86 → depolarizing 60.8 → bit-flip 68)
  - Design principle for modular quantum architectures interconnected via high-speed links — computation distributes across multiple cheap QPU calls
  - **Activation**: quantum neural network, qubit limit, divide and conquer, modular hybrid QNN, VQC ensemble, PCA sliding window, distributed quantum computing

### Large-scale Repository Engineering via Agent-Native Reusable Code Primitives
- [[code-primitives-lego-repository-engineering]] - Code Primitives = reusable components with resident LLMs that self-assess relevance and ADAPT themselves; LEGO orchestrates them to build whole repositories (+61.4% over GPT-5.6-terra alone) (arXiv: 2610.09079)
  - Primitive P=(impl, interface contract, dependency closure, carried validation tests, provenance, resident LLM); median 214 lines, 4 symbols, 9 tests; CodeFace library of 1,424 validated primitives
  - Reuse by adaptation not invocation: primitives emit cross-component requirement propagation µ_i→j; LEGO's diagnosis loop localizes failures and reactivates only affected primitives
  - Improves all 13 evaluated backbones (+0.1474 mean); beats OpenHands by 57.3% and Claude Code by 56.2% at matched backbones; GPT-OSS-20B adaptation retains 95.1% score at 24% lower cost
  - **Activation**: repository-scale code generation, code reuse by adaptation, agent-native components, resident LLM, LEGO framework, primitive collaboration, requirement propagation

# AI Collection Index

## 2026-10-08 - Neuroscience Research (Cron Job, Hour 19)

### Do Generative Priors Align with Human Naturalness Perception?
- [[generative-priors-naturalness-alignment]] - Zero-shot paired directional loss differences of 25 image/video generators track human naturalness ratings (r=.84 faces, .64 scenes), beating encoders and IQA (arXiv: 2610.09928)
  - Content-preserving relational interventions (Thatcher eye/mouth flips, Kubric shadow/reflection/light-direction mirroring) + paired subtraction u = L(mod)−L(orig) bypass the density confounds that kill raw single-image losses (correlation −.20 to .24)
  - Sensitivity and human alignment dissociate along denoising schedules: alignment peaks EARLIER than violation sensitivity in 20/25 (Thatcher) and 25/25 (Illumination) models — human-like judgment resolves at intermediate noise levels, not clean ones
  - Aligns with generation benchmarks (Elo ρ=.827, VBench ρ=.929) even after controlling for sensitivity; failure mode identified: reflection hue shifts (humans penalize, models don't; scaling amplifies sensitivity without fixing alignment)
  - **Activation**: generative priors, naturalness perception, Thatcher effect, paired relational intervention, directional loss difference, denoising loss landscape, psychophysics of generative models

### Brain alignment of reasoning and action representations from vision-language and action models during naturalistic gameplay
- [[vlm-lam-gameplay-brain-alignment]] - First VLM/LAM brain-encoding study on interactive Atari fMRI: prompt gains concentrate 2-2.5x in frontal-parietal/motor cortex; variance partitioning reveals VLM prompt-symmetric vs LAM action-dominant organization (arXiv: 2605.19352)
  - TR-aligned 4-frame trailing windows + action/reasoning prompts + per-layer last-token embeddings + ridge encoding (4 hemodynamic lags, LORO CV) — reusable protocol for aligning foundation-model internals with gameplay fMRI
  - Equal whole-brain accuracy masks reorganization: LAM action-unique variance 25.6% vs reasoning −8.2% (redundant), strongest in SMA (u_A=34%); VLM balanced (12.4% vs 9.5%) — raw accuracy is blind to representational structure, variance decomposition is required
  - VLMs/LAMs beat EMPA/DDQN RL baselines even at matched feature dimensionality (8/64/1024, saturation at 64); Qwen3.5 CoT-trace readouts align WORSE than final-answer (r=.012 vs .031) unless mean-pooled
  - **Activation**: VLM brain alignment, large-action model, Atari gameplay fMRI, voxel-wise encoding, variance partitioning, action vs reasoning prompts, world models, naturalistic gameplay encoding

## 2026-10-08 - Neuroscience Research (Cron Job)

### CircuitATLAS: Agentic reasoning over a systems neuroscience knowledge graph for target discovery in circuitopathies
- [[circuitatlas-agentic-kg-target-discovery]] - Circuit-first drug target discovery: 3.83M-node KG + evidence-gated multi-agent workflow + MCP lab-in-the-loop, validated in vivo on ATP1A3 (arXiv: 2610.09643)
  - Anti-shortcut design: disease→gene/protein edges deliberately EXCLUDED from the discovery graph; molecular agent reasons from measurable phenotypes through circuits/cell types to control points that are unaltered in disease
  - Deterministic narrowing (1701-term lexicon, 400-char co-occurrence, 57.7M candidates) with LLM as semantic VERIFIER only (quotation + confidence per edge); 17.8% Opus-5 audit disagreement → inference-time re-verification on edges a reasoning chain depends on
  - Three evidence layers as typed quantitative edges: literature (5.31M LLM-extracted), Human Cell Atlas (~129k EXPRESSES edges with expression fraction/magnitude/specificity), in-house multimodal in vivo (EEG/ephys/pose/photometry with effect sizes + stats)
  - ATP1A3 case: interneuron-restricted expression abolished 4-AP-evoked beta/gamma response (fold 11.16→1.33, Cliff's δ=−1.0); structure-guided campaign excluded cardiotonic steroid pocket as anti-target; docking predicts binding NOT polarity → thallium-flux polarity screen as next uncertainty-resolving experiment
  - **Activation**: circuitopathies, target discovery, systems neuroscience knowledge graph, agentic reasoning, evidence-gated workflow, MCP lab-in-the-loop, anti-shortcut graph design, phenotype-to-circuit reasoning, ATP1A3

### A Geometry-Based Capacity Theory for Finite-Feature Associative Memory
- [[geometry-capacity-associative-memory]] - Retrieval interference splits into finite-feature noise ~(N−1)/R (fix: more features) vs structural interference Σ K_ij² (fix: change representation); fit-free capacity prediction from measured embedding geometry (arXiv: 2610.09056)
  - Cosine law C_i(R) ≈ [1 + Σ_{j≠i} K_ij² + (N−1)/R]^(−1/2); infinite-R ceiling C_∞ exact for orthogonal values; correlated values require joint key-kernel + value-Gram analysis (a_i = Σ_j K_ij G_ji, b_i = Σ K_ij K_iℓ G_jℓ)
  - PCA whitening REDUCES dimension 2048→256 while RAISING ceiling 0.65→1.0 — nominal dimension and effective rank are insufficient descriptors; kernel scale can reverse capacity rankings
  - Capacity boundary R/N ≈ (1/C*² − 1)^(−1) (9.26 for C*=0.95) converts measured geometry into memory-sizing estimates; ceilings unreachable by increasing R alone are flagged
  - Validated on synthetic + ResNet/ViT/DINOv2/CLIP embeddings + SynthRAD MRI–CT + 445 clinical NCCT–CTA; covariance-aware variant brackets empirical RAW↔WHITENED crossover in all 20 subsets (MAE −84.5%)
  - **Activation**: associative memory capacity, Hebbian memory, kernel geometry, retrieval interference, fast-weight/linear-attention capacity, whitening intervention, memory sizing, cross-modal retrieval
## 2026-10-08 - Systems Engineering + Quantum (Cron Job, Hour 10)

### Automated reduction of fault-tolerant circuits
- [[fault-equivalent-circuit-reduction]] - BFS over fault-equivalent rewrites cuts ancillas/CNOTs while FT properties are inherited by transitivity — no per-candidate re-verification (arXiv: 2610.09749)
  - Enabling rules (restricted commutation / basis swap / target swap) only restructure to expose Bell-pair reductions; each composite transition removes exactly 1 ancilla + 1 CNOT → strictly decreasing cost bounds search depth
  - Bell-pair reduction constraints: factorized U⊗V evolution of the pair + eliminated outcome feeds a parity only (classical record relabeling, not postselection)
  - [[7,1,3]] Shor-style syndrome extraction: 30→18 ancilla preps, 54→42 CNOTs per round, logical error −21% @ p=1e-3 (−13…−23% over two decades); Steane dynamic SE: 391 candidates → sequential race (α=0.05) → 4 ancillas + 14 CNOTs, −15% under depol idle 3p/10
  - Flags decoded via conditioned lookup tables (no shot rejection) → unconditional rates; near-quadratic log-log slopes 1.94–1.97 prove no first-order failure mode
  - **Activation**: fault-equivalent rewrites, ZX-calculus edge-flip noise, Bell-pair reduction, syndrome extraction circuit optimization, Steane code, flag decoding, ancilla reduction, sequential race selection

### Efficient Estimation of Logical Sensitivities Through Fault-Counting
- [[fault-counting-logical-sensitivity]] - Score-function estimator extracts ALL logical sensitivities ν_i = ∂p_L/∂p_i from one Monte Carlo run at one noise point, 1-2 orders fewer shots than finite differences (arXiv: 2610.10531)
  - ν_i = E[L(E)·∂log Pr_p(E)/∂p_i] — only failing shots contribute; per-fault components (s = 268/1526/4544 at d=3/5/7) enable post-hoc aggregation: error budgets, spatial heatmaps (bulk > boundary), per-round resolution
  - Variance ratio Var(FD)/Var(Diff) ≈ 2s/(a²·E[M_i²|L]); advantage scales quadratically with error-type count; no step-size bias at all
  - Free by-products: local effective distance d̂ = 2ν̂p/p_L − 1; sensitivity-guided Newton-Raphson traces threshold contours in s-dim noise space in O(K^(s−1)) points (factor K over grids), model-agnostic distance crossings
  - Generic to any independently sampled mechanism: Pauli, leakage, erasure, correlated, non-Clifford; REINFORCE-style log-score transfers beyond QEC
  - **Activation**: logical sensitivity, error budget analysis, threshold contour, surface code noise model, Monte Carlo gradient estimation, score function, Stim simulation, effective distance diagnostic

## 2026-10-08 - Systems Engineering + Quantum (Cron Job, Hour 9)

### Standard estimators cannot represent fault-tolerant workloads at measured error rates
- [[ft-resource-estimation-uncertainty-propagation]] - Evidence-based priors through 5 surface-code cost models: resource estimates must be intervals + censored fractions, not points (arXiv: 2610.10490)
  - Measured 2Q error median 4e-3 (4x the 1e-3 planning convention) widens 90% physical-qubit interval ~40x, lifts median 4.6x
  - 5 cost models disagree by stable factor 2.0; Azure QRE & Qualtran agree to ~10% but censor 80-100% of evidence space (distance cap 50 / fixed factory feasible only to ~1.7e-3)
  - AES-256 T-count 6.07e43 overflows Azure's 64-bit counter outright; censoring measured as a headline result via missing-not-zero adapters
  - Shapley effects under copula dependence (not Sobol); pre-registered 3-layer evaluation (OSF 3d9m2), sensitivity-weighted coverage ~99%
  - **Activation**: fault-tolerant resource estimation, uncertainty quantification, surface code cost model, evidence-based prior, Shapley sensitivity, censoring envelope, post-quantum cryptography migration

### Benchmarking Modular Optimization Strategies for Parameterized Quantum Circuits
- [[modular-pqc-optimizer-benchmark]] - Factorize VQA optimization: search-direction estimators (PSR/SPSA/PGPE/OCP) x update rules (SGD/Adam/RMSprop) paired independently across 4 workloads (arXiv: 2610.10254)
  - No component dominates: PGPE-SGD best mean MaxCut, FiniteDiff-RMSprop best mean VQE, OCP-RMSprop best mean classifier accuracy (seed consistency, not peaks)
  - Update rule flips outcome at fixed estimator: Iris RMSprop 100% vs SGD 75-80% at matched 52,800 circuits; QCNN OCP 100% needs 404,800 circuits vs PGPE-Adam 97.5% at 17,600 (23x)
  - Three-level cost accounting: objective eval != logical circuit != shots; equal step counts never mean equal budgets
  - Terminal vs best-observed diverge on hardware in 3/4 runs; finite-shot VQE below FCI is selection bias, not physics
  - **Activation**: parameterized quantum circuit optimization, search-direction estimator, SPSA, PGPE, observable curvature preconditioning, QAOA optimizer, VQE optimizer, finite-shot cost
## 2026-10-08 - Neuroscience Research (Cron Job, Hour 17)

### Many Brains, One Geometry: A Shared Visual-Semantic Space for Cross-Dataset fMRI Decoding
- [[braid-fmri-cross-dataset-clip-decoding]] - 单一 ROI-token Transformer 联合训练 8 个 fMRI 数据集（MOSAIC 93 被试、43 万试次），映射到共享 CLIP ViT-B/32 空间，零样本迁移 +92.1% (arXiv: 2610.09352)
  - 379 个 ROI 各配独立 2 层 MLP tokenizer（吸收各 ROI 维度差异）+ ROI 身份嵌入 + 可选被试嵌入 S_i——共享 4 层 Transformer，被试条件化只是单个加性向量，禁用即得 participant-agnostic 编码器
  - Multi-positive InfoNCE：同一刺激跨被试/数据集重复出现时按同刺激集合均匀目标做对称交叉熵，杜绝 false-negative 互斥；logit scale 学习（init 1/0.07, cap 15）
  - 零样本协议：整个目标数据集+全部被试留出，participant embedding 全程禁用，源池累积扩充——7/7 目标数据集正增益（NSD +92.1%）
  - 几何验证超越检索精度：matched > same-cluster (+0.094) > different-cluster (+0.043) 相似度层级跨数据集保持；语义簇质心 RDM 跨数据集 Spearman 0.61–0.88
  - 消融：腹侧视觉 −4.8pp、早期视觉 −3.5pp 主导；人物肖像依赖腹侧、网球动作依赖腹侧+顶叶+早期、火车依赖早期视觉——类别特异贡献
  - **Activation**: cross-dataset fMRI decoding, ROI tokenization, CLIP alignment, multi-positive contrastive, participant embedding, zero-shot transfer, MOSAIC, semantic geometry RDM

## 2026-10-08 - Neuroscience Research (Cron Job, Hour 16)

### Feedback to the primary visual cortex is highly concentrated on the central visual field representation
- [[v1-feedback-eccentricity-magnification]] - CPD 理论首个直接解剖证据：狨猴 12 个 V1 逆行示踪位点显示反馈/前馈比随离心度幂律下降（V2 α=1.5、腹侧流 α=1.6、背侧流 α=0.6），叠加皮层放大因子后中央视野反馈优势达 ~1000× (arXiv: 2610.09983)
  - N̂(E)=N_region/N_LGN 示踪剂归一化：以同一注射的 LGN 前馈计数为基准归一，消除注射扩散/摄取差异——将受混杂的绝对计数转为稳健的反馈放大因子 M_feedback(E)
  - 腹侧流主导中央视野反馈、背侧流主导外周（N_ventral/N_dorsal α=0.96）——与"what/where"分工在反馈环路中同样成立；非视觉皮层反馈 α≈0（负控制）
  - 推翻"V1 表面计算均匀"经典观点：细胞密度/柱尺寸/LGN 传入密度跨 V1 近似均匀，唯反馈环路例外——视觉皮层需沿层级 × 中央-外周二轴组织
  - 解释外周视觉错觉（反转深度、翻转倾斜）：外周因缺乏反馈查询而可见，中央在 backward masking 干扰反馈后才显现
  - **Activation**: feedback magnification factor, central-peripheral dichotomy, retrograde tracer normalization, eccentricity power law, ventral stream feedback, cortical magnification, V1, marmoset connectome

### MovieSTAGE: Scene, Transition, and Global Encoding for Movie-fMRI ADHD Classification
- [[moviestage-scene-transition-global-fmri]] - 事件对齐多尺度 movie-fMRI 分类：场景级超图 + 相邻场景无符号 ∆FC 重构 + 全片 FC 三分支融合，CMI-HBN 260 被试三任务 AUROC 0.69/0.73/0.75 全超基线；人工标注叙事分区胜过时长匹配随机分区与 GSBS 固定数分段 (arXiv: 2610.09306)
  - 短窗 FC 必用 Ledoit–Wolf 收缩；超边由 FC-profile 余弦相似度 top-K 锚点构造（K=6），可学习超边权重 Softplus 保证正值
  - 关键设计：转换分支用 |∆FC| 无符号幅值——不假设跨被试/ROI 对的符号方向一致，只编码重构幅度（可移植到睡眠分期/任务切换/癫痫起搏任何"重构幅度即信号"场景）
  - 评估协议金标准：10×5 折完整 OOF + 被试级聚类 bootstrap/置换检验（每被试重复预测为一簇）+ Holm 逐族校正——杜绝跨折伪重复
  - 消融：全局分支单独最强（0.68），三分支融合 0.75 且全胜两分支组合——条件性互补而非冗余；最强组间差异在 T5 情绪转换处（ADHD 的 FPN–DMN/DMN–DMN 重构幅度更大，FDR q<0.05）
  - **Activation**: movie-fMRI, event-aligned representation, hypergraph neural network, unsigned FC reconfiguration, narrative segmentation, ADHD classification, CMI-HBN, out-of-fold prediction, subject-cluster bootstrap

## 2026-10-08 - Systems Engineering × Quantum (Cron Job, Hour 8)

### Geodesic-Based Optimal Control for Leakage Suppression in Superconducting Qubits
- [[geodesic-optimal-control-leakage-qubits]] - Sub-Riemannian geodesic pulse synthesis with built-in smooth-envelope constraint beats DRAG-F and DRAG-L simultaneously (arXiv: 2610.09666)
  - Sigmoid envelope S(t) baked into the geodesic equation itself; 17ns Rx(pi/2) saturates thermal limits: F=0.9996, L1=1.08e-5
  - iSWAP: 0.9548@79.5ns control-free -> 0.9942@86ns via geodesic real-time dressed-frequency corrections; SW+RWA reduces coupler architecture to SU(9)
  - **Activation**: leakage suppression, DRAG, geodesic optimal control, pulse synthesis, tunable coupler, iSWAP

### Non-Orthogonal Amplitude Amplification for Hybrid CV-DV Quantum Processors
- [[noaa-nonorthogonal-amplitude-amplification]] - Amplitude amplification when the CV-assisted reflection is exact but non-selective; fidelity ceiling eta is projector-bound (arXiv: 2610.09353)
  - F = eta*P_L decomposition: phase schedules only improve transfer P_L; ceiling eta requires a more selective projector; cumulative weighted-overlap ratio R gates fidelity
  - Squeezed ancilla (eps 0.1 -> 8.21e-21) trades overlap against mismatch sensitivity (e^r growth); degree-60 HQSP erf-passband filter absorbs energy-estimate mismatch
  - Beats RUS for small |psi0| with mismatch; RUS already optimal at large amplitudes
  - **Activation**: amplitude amplification, non-orthogonal states, CV-DV, HQSP, fidelity ceiling, squeezed ancilla, state preparation
## 2026-10-08 - Neuroscience Research (Cron Job, Hour 8)

### A Connectome Test of the Fly Hashing Algorithm
- [[flyhash-connectome-lsh-test]] - 果蝇哈希算法连接组实测：四个电镜连接组 + 保度重接线 null，实测配对无一致检索优势（中位 -1.6%），优势本质是"每激活单元"而非"每操作" (arXiv: 2610.09114)
  - 2017 Science 模式可复现（MNIST k=4 时 3.1× AP@200），但等投影算力下实值高斯 LSH 在所有数据集/维度上更优——fly hash 的适用场景是激活单元昂贵（神经形态/稀疏硬件）而非算力昂贵
  - Curveball 保度 null：7 半球中 6 个配对结构显著偏离 null（Qz 最高 17.8）但结构不带来检索收益；hemibrain 的"例外"源于弱连接（≥2 突触阈值后 Q 也超 null）
  - 均衡 fan-out 在全部 7 半球提升检索（+3.9%~+6.4%）而均衡每细胞输入降低之；但 fan-out 偏斜跨四动物保守（ρ 中位 0.86，跨度 17×）且突触计数放大而非抵消偏斜——生物学代价换其他功能（先天效价/新异性检测）
  - 方法学金矿：per-active-cell vs per-operation 预算核算、AP@n 必须计入 miss、协议溯源表、非预注册的 null 集规模诚实标注
  - **Activation**: fly hash, locality-sensitive hashing, connectome null model, degree-preserving rewiring, Kenyon cell fan-out, curveball randomization, sparse binary projection, winner-take-all hash

### Scaling subjects in cross-modal alignment: video decoding with EEG foundation model
- [[eeg-video-subject-scaling-law]] - EEG 视频解码被试规模律：S≈50 起始点之上对数线性增长无饱和（每翻倍 +0.0244 r），此前"扩被试无用"结论是范围限制而非矛盾 (arXiv: 2610.09287)
  - HBN 10→1863 被试阶梯（超先前文献一个数量级）：S<50 时无任何 arm 显著超过未训练编码器（1.4×阈值）——先前文献恰好全部位于该区间（最大队列 48）
  - 预训练初始化（REVE）比容量更关键：每翻倍增速 1.5–1.7× 于随机初始化两深度，唯一在 S>701 仍转化被试为检索精度的 arm，且以 1/2.4 算力达更优 optimum（26.6 vs 63.3 PFLOPs）
  - 未训练 floor 高达 r=0.105（最佳值的 1/3）——绝对分数必须相对 floor 解读；跨任务零样本检索全程贴 chance（负控制成立），失效的是 EEG 投影头而非编码器表征
  - soft-target CLIP（冻结 V-JEPA-2 教师窗-窗相似度定义梯度目标）优于硬目标 CLIP 与场景掩码损失；随机初始化 arm 的"饱和"属于协议（optimum 撞预算上界）而非被试轴
  - **Activation**: EEG foundation model, subject scaling, cross-modal contrastive, movie decoding, scaling law onset, REVE, V-JEPA-2, naturalistic stimuli, pretraining initialisation

## 2026-10-08 - Systems Engineering + Quantum (Cron Job, Hour 7)

### Cross-Validation of Open-Source Quantum Network Simulators
- [[cross-validation-quantum-network-simulators]] - Cross-validation methodology for QuISP vs SeQUeNCe quantum network simulators (arXiv: 2610.09322)
  - Discrepancy triage framework: real design difference / valid simplification / bug — this exercise produced numerous bug fixes in both simulators
  - Constant timing ratio ~4.2x (three-way vs two-way handshake); fidelity agrees under identical error params; asymmetric MIM link shows BSA-placement-dependent divergence (QuISP) vs placement-insensitivity (SeQUeNCe)
  - **Activation**: quantum network simulator, QuISP, SeQUeNCe, cross-validation, entanglement distribution benchmark

### Numerically exact simulation of open quantum networks with strong system-bath couplings using comb tensor network path integrals
- [[ctempo-comb-tensor-network-path-integrals]] - CTEMPO/CCTEMPO comb tensor network path integrals for non-Markovian quantum networks (arXiv: 2610.10259)
  - Contraction-order insight: contracting system propagators row-by-row (causal + early) reduces bond dimension from hundreds-thousands to single/low-double digits, 10-100x faster than TEMPO/PT-MPO
  - Comb topology: many-body density matrix MPO backbone + per-site CTEMPO teeth, cost linear in chi; solves 7-site FMO complex (62-peak spectral density, previously infeasible); N=20 quantum dot superradiance reveals novel intermediate scaling regime
  - **Activation**: non-Markovian simulation, TEMPO, process tensor, path integral tensor network, bond dimension compression, FMO complex
## 2026-10-08 - Neuroscience Research (Cron Job, Hour 7)

### Connectome-Based Modeling of Mutation-Specific Amyloid-β Aggregation in Familial Alzheimer's Disease
- [[mutation-specific-amyloid-connectome-diffusion]] - 突变感知 Aβ 聚集-碎裂模型耦合连接组图扩散：实验核酸化得分以 exp(NSμ) 乘子注入单一反应通道，在 540 节点 Budapest 连接组上分离分子动力学与拓扑贡献 (arXiv: 2610.09583)
  - 动力学定时钟、拓扑定地图：20 个保度随机连接组全部保持突变排序（timing/peak/AUC ρ=1）但摧毁区域模式（空间 Spearman 仅 0.19–0.35）；距离-到达耦合 ρ≈0.92
  - E22G (Arctic) 8.80 vs WT 110.67 模型时间单位跨界，累计寡聚体 AUC 最大；A2V 最慢——后果源于实验核酸化表型映射而非临床严重度排序
  - 全局敏感性：时间由单体产生(-0.654)/转换(+0.601)/初级成核(-0.411)驱动，扩散尺度 ρ 对 timing≈0 但对空间传播 +0.317——报告 timing/AUC 排序（后验下稳定），峰值幅度排序不可信（仅 36% draw 复原）
  - ABC-SMC 合成恢复验证 32 维摘要统计可复原生成值并暴露 k_sec↔k_conv 补偿性权衡；CLE 反应级噪声下 ensemble 中位数保序而单条轨迹重叠
  - **Activation**: mutation-aware aggregation kinetics, connectome graph diffusion, network spreading model, familial AD variants, ABC-SMC parameter recovery, Chemical Langevin, degree-preserving null, wiring versus kinetics separation

### Structure alone supports efficient visual computation in the Drosophila visual system
- [[connectome-only-message-passing-fly-vision]] - 连接组独占模型：果蝇全脑接线 + 解剖眼前端固定，仅学有界突触增益，结构本身支持 Weber 比率数量判别等视觉计算 (arXiv: 2610.10023)
  - 固定图+Voronoi 眼（R7 种子镶嵌，200nm 光谱移位映射 RGB）：色觉 100%（未训练 92%）、形状 64%、数量判别随 Weber 比率 64%→85%——近似数系统签名，与真实果蝇行为一致
  - 四级接线约束 null 系综：非约束/剪枝到同预算/全局长度分箱/每神经元分箱；等接线预算下生物连接组始终最优——演化高效操作点，非约束重连以膨胀接线成本换取更高精度
  - 传播动力学先于任务指标：非约束图第 2 步全脑饱和（含 Kenyon 细胞），生物与约束系综渐进传播（3 步 ~80%）——长程突触加速扩散解释精度差
  - tanh(θ) 增益界定 ±突触计数内，等价 Hebbian 强度适应；只读 Kenyon 细胞均值→线性单元；PyG MessagePassing 骨架可直接复用
  - **Activation**: connectome-only model, message passing, wiring economy, null ensemble at matched cost, approximate number system, Voronoi ommatidia, Kenyon cell readout, structure-function isolation

## 2026-10-08 - Systems Engineering x Quantum Research (Cron Job, Hour 6)

### Design-Time Conformance Checking for Pulse-Level Quantum Control
- [[design-time-conformance-pulse-quantum-control]] - 设计时一致性检查器 qconform：脉冲程序在运行前对照"证据引用式能力描述符"判定可实现性，精确有理数算术 + 覆盖清单 + 修复预测 (arXiv: 2610.10427)
  - 证据引用描述符：每条硬件约束都指向黑盒探测调查目录（605 QICK + 193 Qblox probes），gate 脚本拒绝证据不可解析的描述符——散文契约会漂移，机器契约不会
  - 精确算术：时长=有理时间基的整数计数，频率/相位/幅度=精确分数；vendor 双精度混频器减法让正好在上限的请求变成 860.1600000000001 MHz 被拒——网格检查免疫浮点伪影；单通道双时钟（599.04 vs 430.08 MHz）必须双网格
  - 修复即判决：silent mutation（频率折叠到 Nyquist 镜像偏 860 MHz、增益寄存器回绕、readout 半偶舍入）在运行前暴露为 pass-with-repairs；26 类覆盖清单区分 checked/unchecked——空泛通过 vs 已验证通过
  - 差分测试：边界梯（远低于/恰低于/恰好/恰高于/远高于）+ 预算梯 + 间距梯 + 分辨率梯 + 随机组合，9 类裁决只有 unsound（检查器接受而 vendor 拒绝）计入健全性；1263 runs / 969 programs / 0 unsound passes；版本 pin 是健全性声明的一部分——最老 QICK release 产生 90 个 unsound pass
  - 复发缺陷模式"解析但从未执行"（3 次）：post_mixer 标志被解析但检查器从不查询 → 构建期 tripwire 强制检查器读取解析器填充的每个描述符字段，首次运行又发现 3 个潜在实例
  - **Activation**: pulse-level conformance checking, capability descriptor, evidence citation, exact rational arithmetic, coverage manifest, differential testing triage, silent repair detection, version-pinned soundness, QICK Qblox, design-time verification

## 2026-10-08 - Systems Engineering x Quantum Research (Cron Job, Hour 5)

### Simultaneous Circuit Tests for Finite Reversible Models of Quantum Control
- [[simultaneous-circuit-tests-finite-reversible-control]] - 有限可逆量子控制模型的联合认证：一个共享控制器+制备律必须复现整族电路概率，共享表 MILP 精确可行性 + 逐电路拟合与联合拟合的严格分离 (arXiv: 2610.06984)
  - R_ind ≤ R(W) 可严格分离：4-frame 例子每条电路单独都能以 <1/4 误差拟合，但任何单一允许表都无法同时拟合两条
  - 464-frame 精确基准：证词控制器在阈值 1/3 下撑过 192 个重复块，第 193 块穷举排除全部允许控制器（概率带+单射+匹配可扩三重剪枝，41595 节点，Q(√2,√3,√5,√7,i) 精确算术）
  - 有限窗口谱障碍：周期轨迹追不上无理频率振荡，窗口 D > (κ_M+C)/(a/2−δ) 即证差异；有限 shot 认证 r_N=√(log(2m/α)/2N)
  - 浮点求解器失败不构成排除证明；排除证书是类相对的——放宽类即失效，证词在任何更大类中仍是证词
  - **Activation**: simultaneous certification, finite reversible model, shared-table feasibility, exclusion certificate, certified horizon, finite-shot certification, quantum control memory bound

### Resource-Aware Grover Search for Minimum Vertex Cover
- [[resource-aware-grover-minimum-vertex-cover]] - 三种 Grover MVC oracle 设计按硬件约束选型：Dicke-Parallel（均衡）/ Edge-Counting（省 qubit）/ Edge-Centric（结构化稀疏图省深度省迭代）(arXiv: 2610.07252)
  - 三瓶颈框架：搜索空间 2^n vs C(n,k)、oracle 宽度（DP 计数 O(n²) ancilla）、总深度 D_search ≈ R·D_iter 需联合优化
  - Edge-Counting：⌈log₂(m+1)⌉ 可逆计数器替代 per-edge 标志位——紧 qubit 预算首选，代价是串行深度
  - Edge-Centric：每边一 qubit 选端点，基态天然构成合法覆盖（可行性检查消失）；内部边产生编码多重性 μ(C*)=2^|Ein|，提高标记态分数 → 减少迭代
  - 选型判据：稀疏核-外围结构→Edge-Centric（Σ2^|Ein|/2^m > C(n,k)/2^n）；稠密大 m→Dicke-Parallel；MCX 综合深度非单调（20-ctrl 4797 vs 24-ctrl 4405）是伪影不是负载属性
  - **Activation**: Grover oracle design, minimum vertex cover, Dicke state, edge-centric encoding, qubit width reduction, reversible counting, Wallace tree, marked-state fraction

## 2026-10-08 - Neuroscience Research (Cron Job)

### SpecBraM: What Should an EEG Foundation Model Predict? Masked Band-Power Prediction versus Waveform Reconstruction
- [[specbram-band-power-eeg-fm]] - EEG FM pretext target should be band power, not waveform: phase is ancillary, spectral energy is what sleep labels depend on (arXiv: 2610.07484)
  - Controlled 2×2 tokenizer×target study (2,388h TUEG, 3 seeds): band-power target beats raw/band-waveform reconstruction by +1.6–2.8 BA pts (strict linear probe), +4.7–7.3 pts with 1% labels, on every seed; target effect > tokenizer effect
  - Theory: stationary-Gaussian analysis — periodogram sufficient, phase ancillary; Var[log P]≈1/m state-independent; Bayes risk splits into reducible state uncertainty + irreducible patch innovation (waveform loss wastes gradient on the latter)
  - Fixed-target anti-collapse: learnable target filters shrink to zero (loss→4e-4, features dead) — never co-learn the target extractor
  - Honest negatives: no gain on motor imagery (spatially-localized µ/β), vigilance (ocular artifact dominates low bands; 4Hz high-pass restores lead), gap vanishes after full fine-tuning — target matters most for frozen/low-label deployment
  - **Activation**: EEG pretraining objective, masked prediction target, band power pretext, sleep staging foundation model, phase ancillarity, LaBraM CBraMod alternative

### Neuromotor Hierarchy Network: Physiological Inductive Biases for Robust Generalization in sEMG Decoding
- [[neuromotor-hierarchy-network-semg]] - Physiology-guided hierarchy infers a 32-primitive latent neuromotor state from wrist sEMG, factoring out recording variability (arXiv: 2610.07713)
  - Four-stage causal pipeline: partial whitening without PCA rotation (measurement adapter) → TDS encoder with multi-timescale adaptive gain → non-negative drives + geometric-kernel FIR integration → Henneman-graded allocation softmax((d+β)/θ)⊙d
  - emg2pose: −0.52% to −2.84% angular error vs Hadidi et al. best with 48.4% fewer params; emg2qwerty: −19.4% zero-shot / −30.4% fine-tuned beam CER vs SplashNet-Upscale with 65.9% fewer params (0.88M vs 5.06M)
  - Mechanistic findings: pose = distributed multi-primitive composites; typing = recurring key-specific primitive combinations; uniform-allocation ablation costs +3.94° AE / +42 CER pts → decoding reads relative allocation, not total drive
  - **Activation**: sEMG decoding, hand pose estimation, motor primitives, muscle synergy, cross-user generalization, Henneman size principle, emg2pose, emg2qwerty

## 2026-10-08 - Quantum Computing Research (Cron Job)

### Quantum Algorithms for Multivariable Polynomial Transformations
- [[multivariable-polynomial-quantum-synthesis]] - 多变量非对易矩阵多项式的完整合成理论：紧凑系数递归 → 残差坐标 → SDP 缺陷证书 → Douglas 因子 → 量子电路，QSP/SVT 的多变量推广 (arXiv: 2610.08714)
  - 联合块访问模型（diagonal/row/column 布局）下，任意度 D 压缩多项式以 O(D/√τ) 次查询、β ≤ (1+τ)‖p‖ 归一化合成；row 输入恰好 D 次查询达下界
  - 残差坐标（r ≤ s+1 维）压缩指数级词表：hereditary positivity 分离论证证明该空间内 SDP 证书完备（β²E†E − P†P = S + Φ(T)），ellipsoid 发现多项式位复杂度
  - 通道级提升：coherent Kraus 上的多项式映射允许 Kraus 历史间相干干涉；causal Choi 数据可编译为固定阶量子 comb
  - Worked example (1+x₁x₂)/4 全数值验证 17/17 PASS：证书恒等式、四个块 vs 论文 Eq. 3.20 逐位匹配、严格压缩性、范数界
  - **Activation**: multivariable QSP, noncommuting polynomial synthesis, Schur-Agler certificate, joint block encoding, quantum channel transformation, 多变量量子信号处理

## 2026-10-08 - Reinforcement Learning Research (Cron Job)

### BoT-GRPO: Efficient Process-Reward RL for Reasoning via Bag-of-Token Aggregation
- [[bot-grpo-bag-of-token-aggregation]] - GRPO 扩展到 token 级奖励：跨 rollout 收集全部 token rewards，按来源序列长度倒数加权后做组统计，per-token advantage 免 critic，drop-in 替换 GRPO (arXiv: 2610.09804)
  - 长度不变聚合消除长序列统计主导；per-token 优势只需跨 rollout 聚合统计"中心化"，无需逐位置 value network
  - React 代码生成 80% compile 达速 1.9× faster；AIME Pass@k 最高 +8.1pp 且步数减半；收敛快于 GSPO/DAPO/PURE
  - 奖励模型配方：稳定性 > 丰富性——clean, bounded, stable 细粒度信号一致加速，noisy 信号使训练停滞
  - **Activation**: process reward model, token-level reward, GRPO variant, critic-free RL, PRM integration, LLM reasoning RL

### COPC: Coupled Off-Policy Correction for Asynchronous LLM Reinforcement Learning
- [[copc-coupled-off-policy-correction]] - 异步 LLM RL 双通道修正：policy 侧 token 级 ratio masking + advantage 侧对 TD residual 双侧 clipped-ratio 加权，修正被忽视的 advantage staleness (arXiv: 2610.09597)
  - 理论：两通道误差不可分离——交互项产生乘性偏差，平方 policy weight 放大 advantage 不确定性；单侧修正参数最优值随另一侧反转
  - Tool-integrated 数学推理与搜索超最强异步基线；搜索任务全程稳定而多数异步基线后期 collapse；64-step staleness 下增益保持
  - 开销低：相对异步 PPO 几乎无 step-time 额外开销，保留对同步 PPO 1.7× 加速
  - **Activation**: asynchronous RL, stale trajectories, advantage staleness, off-policy correction, async PPO, training collapse

### DARS: Dependency-Aware Reward Shaping for Agentic Reinforcement Learning
- [[dars-dependency-aware-reward-shaping]] - 终局奖励下 step 级信用：谓词+前置依赖图上势能塑形，verify/invalidate/repair 标注产生带符号 per-step reward，与 GiGPO/ARPO/AEPO 即插即用 (arXiv: 2610.01207)
  - 折扣规则：已验证谓词按到最近被破坏前置的图距离折扣（依赖损坏上游贬值，独立分支不受影响）；invalidated 需重新验证恢复信用
  - Potential-based 塑形不改最优策略；失败 episode 不再零信号，中间进度产生塑形奖励
  - ALFWorld +10pp over GiGPO（同预算同 harness）；WebShop/Search-R1 提升；蒸馏 8B 标注器 ≈ API 标注器，可脱离 frontier judge
  - **Activation**: reward shaping, step-level credit, agentic RL, dependency graph, potential-based shaping, sparse reward

## 2026-10-08 - Systems Engineering Research (Cron Job)

### Byzantine-Tolerant Causal Unicast with Constant Message Space Overhead
- [[byzantine-causal-unicast-constant-overhead]] - O(1) message overhead Byzantine causal ordering via SPS invariant + isolated per-peer queues + cascading evictions (arXiv: 2610.07368)
  - Sender Permission to Send (SPS): causality enforced at sender, dependency vectors never transmitted -> O(1) network message size, trading O(n²) local space
  - Isolated-Buffer Optimistic Model: per-peer U/Q queues confine Byzantine damage (ACK/PERMIT withholding, flooding, replay all neutralized by LD filter + capacity-triggered force-eviction)
  - Congestion-Relaxed Causal Delivery (CRCD): quantified safety relaxation that reduces to Weak Safety when no evictions occur — deterministic liveness without crypto, impossible-trinity navigation pattern
  - **Activation**: byzantine fault tolerance, causal ordering, distributed systems, message complexity, liveness, SPS invariant, protocol design

### A Validated Dataset and Benchmark for Coherent Multi-Diagram SysML Models (SEMAADB)
- [[sysml-coherent-multidiagram-benchmark]] - 15,000-diagram multi-view SysML coherence benchmark: shared-entity-anchored generation + typed-graph repair/update metrics (arXiv: 2610.07356)
  - Shared entity model as consistency anchor: one canonical name/relation list drives all 5 views (Requirement/BD/Activity/StateMachine/Sequence); 5-step automatic validation + 100-context human-verified core
  - Typed-graph evaluation: exact repair = adherence + preservation; cross-diagram update scored by tuple-level P/R/F1 — immune to formatting noise
  - Key findings: syntax repair ~99.8% (solved) but semantic repair 64.3% max; remove-requirement only 8–9% (absence errors >> substitution errors); update Addition collapses to ~40% — set-level reasoning ≠ rendering
  - **Activation**: MBSE, SysML, systems engineering, benchmark design, LLM evaluation, multi-view consistency, diagram repair, dataset construction

## 2026-10-08 - Systems Engineering + Quantum (Cron Job, Hour 2)

### SAFESHIELD: A Decision-Organization Framework for Deployment-Time Safety of Small Language Models
- [[safeshield-decision-organization-safety]] - Deployment safety as organized, auditable decision stages (admission/routing/evidence/release) with controlled coordination ablations (arXiv: 2610.07276)
  - Responsibility-oriented decomposition at commit points; omitted decisions become implicit permissive defaults; coordination = gating + policy conditioning + evidence propagation, removable while mechanisms stay intact
  - Coordination ablations: severing admission gating (reject recorded but not enforced) drops harmful interception 81.5%->54.0% (McNemar p=1.8e-11); withholding upstream evidence from release drops release accuracy 96.0%->69.5% (p=2.3e-14) while conditional faithfulness of released responses is unchanged -> evidence improves release-decision correctness, not response quality
  - Decision Traces record PASS alongside interventions, localizing failures to the first visible decision point; HarmBench ASR 0.25% full vs 16.5% with both safety stages removed
  - **Activation**: deployment-time safety, guardrail organization, safety decision stages, admission routing evidence release, decision trace audit, SLM safety, runtime guardrails, coordination ablation

### Quantum Entangled Multimodal Fusion Networks (QEMFN): Resource-Aware Hybrid Vision-Language Fusion via Trainable Entanglement
- [[qemfn-entangled-multimodal-fusion]] - Trainable paired cross-modal CZ entanglement as fusion inductive bias, beating parameter-matched classical baselines on COCO-5k (arXiv: 2610.08216)
  - Frozen CLIP embeddings -> 6+6 qubit angle encoding -> L=4 layers of trainable rotations + intra-modal CZ + paired cross-modal CZ (V_i<->T_i, O(nq) gates not O(nq^2)) -> 24 local+correlator observables; 96 quantum params; R@1 68.9 vs dequantized paired-topology control 68.2
  - Correlate-control-intervene evidence ladder: entanglement entropy vs R@1 raw Spearman 0.88, epoch-detrended partial 0.56, loss-controlled 0.49 (beats classical CKA 0.41); interventions (freeze/randomize/remove/regularize entangling gates) all reduce both entropy and performance
  - Meyer-Wallach 0.61, expressibility 0.09, gradient variance tracks local-cost barren-plateau bound (local Pauli-Z observables, not global cost); real superconducting hardware 63.8 R@1 at 8192 shots, +ZNE 65.1; deployment = dual-encoder ANN + top-K quantum reranking
  - **Activation**: quantum multimodal fusion, trainable entanglement, paired cross-modal CZ gates, meyer-wallach entangling capability, barren plateau local observables, quantum reranking, dequantized baseline comparison, vision-language retrieval

## 2026-10-08 - Neuroscience Research (Cron Job)

### Synapse Loss Estimation for the BrainScaleS Wafer-scale Neuromorphic System
- [[brainscales-synapse-loss-estimation]] - Binomial-cascade probability method predicts max lossless SNN size and synapse loss when mapping networks to crossbar neuromorphic hardware (arXiv: 2610.07321)
  - Method 1 (bottom-up): per-target Binomial(n,p) → F^N all-targets product → max-synapse distribution → half-row demand convolution over 4 patterns → E[drivers] → capacity division (224 drivers × 59 usable addresses per HICANN)
  - Method 2 (top-down): survival-function marginal gains ΔS(k) per half row, sorted-descending greedy allocation of 4D half rows; loss ν = S_lost/(S_realized+S_lost); driver limit (224/routing source) dominates over on-wafer routing
  - Theory matches MappingTool reality >20K neurons; 6–16K actual loss is HIGHER due to synapse-driver switch sparsity (1 of 8); full 6-bit in-synapse decoding (BrainScaleS-2) supports larger lossless networks at silicon-area cost
  - **Activation**: neuromorphic, synapse loss, BrainScaleS, crossbar, wafer-scale, SNN mapping, hardware-software codesign, address decoding, routing resource, binomial estimate

### Time-multiplexed layer reuse for physical neural networks
- [[tidal-net-time-multiplexed-pnn]] - TIDAL-Net: periodic cycling through L_W physical weight banks over L_T time steps builds deep effective networks on PNNs whose weights reprogram slowly (arXiv: 2511.00044)
  - Intermediate regime between stateless RNN (L_W=1) and time-variable DNN (L_W=L_T); exploits timescale separation T_swt ≪ T_upd — fast bank switching vs slow weight programming; per-step latency T_MM + max(T_swt, T_state)
  - L_W=2 already beats RNN limit on SVHN/NLP; pure repetition (fixed L_W, larger L_T) improves performance without adding parameters, until RNN-like degradation at excess depth
  - Platform fit: MZI/MRR photonic (µs thermal tuning vs ps MVM) best; MTJ crossbar good; SLM (ms) poor — design rule: persistent banks + fast routing when parameter-setting is slower than inference dynamics
  - **Activation**: physical neural network, PNN, time-multiplexing, weight sharing, weight tying, photonic neural network, MZI, MRR, MTJ, hardware scaling, timescale separation, TIDAL-Net

### Replica Fragmentation and Glassy Dynamics in Parity Learning
- [[replica-fragmentation-glassy-parity-learning]] - Replica-overlap observables (m, q_self, q_cross) diagnose glassy fragmentation of Transformer learning runs into memorization/retreat/recovery regimes (arXiv: 2610.08503)
  - Self-cross gap chi_SG = q_self - q_cross = exact prediction variance across seeds sharing one training set; separates confident memorization (chi_SG large, tail acc at chance) from transient retreat-recovery cycles (brief Nishimori-gap lags)
  - Residual geometry (anti-correlated obtuse pairs x near-ultrametricity) puts the three regimes in non-overlapping regions; retreat is a trajectory phenomenon invisible to gradient/Hessian endpoint diagnostics
  - Learning-rate cosine decay after acquisition (matched pairs) cuts retreat from 29/84 to 5/84 and preserves high accuracy in 79/84 runs
  - **Activation**: replica fragmentation, glassy learning dynamics, self-cross gap, Nishimori gap, memorization vs generalization, retreat-recovery, parity learning, ensemble disagreement, learning frontier

### Classifications in modular restricted Boltzmann machines
- [[modular-rbm-hopfield-dual-classification]] - HM-RBM duality extended to L coupled Hopfield modules = RBM assembly with coupled hidden layers; class-mean weights are a proven CD-1 fixed point (arXiv: 2610.08612)
  - Theorem 1: planted empirical-mean weights are fixed point in mean of supervised CD-1 for any L, with residual drift split into 4 channels (thermal / dataset entropy / mini-batch / finite-size N^-1/2), margin condition lambda(L-1) < 1
  - Planted weights are also an attractor: CD-1 from zero/random init converges to them; hard task = joint classification + disentanglement of mixtures, success region matches modular-HM theory, verified via Hungarian assignment
  - **Activation**: modular RBM, HM-RBM duality, coupled hidden layers, anti-Hebbian competition, supervised contrastive divergence, planted weights, pattern disentanglement, memristor Boltzmann machines


## 2026-10-08 - Systems Engineering x Quantum (Cron Job)

### Entanglement Swapping Scheduling for Quantum Repeater Chains under Decoherence during Classical Communications
- [[repeater-swapping-scheduling-decoherence]] - Memory exposure model for heralding-induced decoherence; finds optimal repeater count and swapping schedule (arXiv: 2610.07991)
  - Memory exposure Θ = cumulative storage-time sum (not wall-clock) governs Werner decay: w_final = w0^(N+1)·exp(-Θ/τ)
  - Interior optimal repeater count exists (metro 60km: N=1-2; 500km: N≈10-11 at τ=100-150ms); repeater density is a design variable, not maximized
  - Parallel scheduling wins short chains/high-rate region; hybrid block strategy wins long-distance; no single strategy optimal across regimes
  - **Activation**: quantum repeater, entanglement swapping, swapping scheduling, memory decoherence, heralding delay, entanglement rate

### Protecting bosonic codes from ancilla-induced errors with continuous-variable flags
- [[cv-flags-bosonic-ancilla-errors]] - CV flag oscillator records continuous ancilla-decay errors in phase space for heterodyne-estimation + feedback correction (arXiv: 2610.07139)
  - Record-don't-prevent: auxiliary oscillator phase-space position encodes jump-time error; feedback undoes it up to a code stabilizer, discretizing continuous errors
  - CR(θ) all-orders with 1 flag; CD(β) all-orders with 2 χ-matched flags; flag driven by same dispersive toolbox as protected gates (zero new ingredients)
  - Cat-code parity bit-flip 5e-7 at |ζ|²=100 (>3 orders suppression); sBs-GKP lifetime 4ms→450ms (within 1.5x of noiseless-ancilla bound); robust to η<1, flag loss, Kerr, finite pulses
  - **Activation**: bosonic QEC, cat code, GKP code, ancilla decay, continuous-variable flag, heterodyne measurement, circuit QED
## 2026-10-08 - Systems Engineering + Quantum (Cron Job)

### Fault-tolerant resource estimation for ground-state preparation via Lindblad simulation
- [[lindblad-ground-state-resource-estimation]] - Lindblad基态制备的容错资源估算：严格误差界+小系统经验校准+Qualtran门级编译，经验参数比最坏情况界省6个数量级 (arXiv: 2610.08667)
  - 36-site Hubbard模型一个时间单元需 7.7×10⁸ T门（经验参数）vs 3.3×10¹⁵（严格界）；能量滤波积分（H演化）主导成本，总成本 ∝ 混合时间²
  - 弹性加权误差预算（可复用模式）：70%→Lindblad步长τ（线性成本）、15%→滤波积分求积（多项对数）、10%→H-Trotter、1%→跳算符Trotter、4%→旋转合成（指数抑制）
  - 有效能隙替换：目标误差超过谱隙时用 Δ_eff=max(ε_target, Δ) 折叠标度指数；单辅助量子dilation+随机跳算符采样避免辅助比特开销
  - 关键发现：Lindblad动力学的收缩性对设备噪声无保护作用（"算法级纠错"不成立）；Trotter在实践尺度上胜过QSVT（前置常数主导）
  - **Activation**: Lindblad simulation, ground state preparation, resource estimation, fault-tolerant, T gate count, error budget, Qualtran, Hubbard model, Pauli-based computation, dissipative dynamics
## 2026-10-08 - Neuroscience Research (Cron Job)

### Neural Fields Encode Adaptation Geometry
- [[neural-fields-adaptation-geometry]] - 切线核适应几何 + 顺序拟合记忆：重构误差之外的 INR 权重双重属性 (arXiv: 2610.07253)
  - 适应几何：用每个 prior 自身的 tangent kernel K_c 构建 Mahalanobis 线性化评分 E^lin，可预测有限预算非线性适应的排序（Spearman 0.955）；换用别类 kernel 全部 8 个设置退化 — (µ_c, K_c) 配对本身携带信息
  - 顺序拟合记忆：θ_t^seq = Adapt(θ_{t-1}^seq, u_t) 让权重携带 Mori–Zwanzig 记忆；不同历史 + 完全相同终点观测下，端点权重线性探针恢复隐藏速度符号 68.6%（观测本身严格 50%）
  - 统一机制：保留率 ρ_i(s) = (1−ηκ_i)^s — 大特征值模式易写易被覆盖，小特征值模式难写但持久；拟合预算存在下游任务峰值（200 步 69.4% > 1000 步 60.1%）
  - **Activation**: neural fields, INR, tangent kernel, sequential fitting, warm start, Mori-Zwanzig, memory retention, regime classification

## 2026-10-08 - Neuroscience Research (Cron Job)

### ReGraph: A Computational Account of Emergent Generalization in the "what" and "where" Dual Visual Streams
- [[regraph-dual-stream-generalization]] - 双视觉流图模型证明：关系泛化结构（grid-like 六边形表征）沿背侧流逐层涌现，源于M/P视网膜二分的三个生物学归纳偏置（非海马de novo产物） (arXiv: 2610.07962)
  - 三偏置缺一不可：流不对称编码（时间/空间分辨率）、MHSA动态邻接侧向连接、背→腹门控调制；trait-symmetric消融掉到69.78 vs 完整74.57
  - Grid-like基仅在ReGraph背侧流单调涌现（L1→L4: 0→15.3%），标准基线（VideoMAE/TimeSformer/SlowFast）均无；基消融致OOD精度L3-4骤降（+7~14pp），证明其为可复用路由模板
  - 腹侧流上下文不变性非独立计算而是经门控g开后从背侧流显式导入——跨流调制机制证据
  - **Activation**: dual visual stream, grid-like representation, dorsal ventral, relational generalization, entorhinal cortex, MHSA dynamic adjacency, context-invariant, brain-inspired architecture, gridness, SSV2

### CANDLE: Cortical Null-Space Decomposition for Noninvasive Brain Source Imaging
- [[candle-null-space-source-imaging]] - 学习式EEG源成像：仅学习个体lead-field矩阵的零空间先验（range空间解析恢复），1113个个体化皮层几何+26k统计脑图Jansen-Rit仿真训练，零样本迁移到颅内刺激定位与致痫区估计 (arXiv: 2610.07824)
  - 范围-零空间分解将病态逆问题学习自由度限制在测量不可定的子空间：x̂ = L⁺D(Y) + x̂_null，几何约束按构造保持
  - 全脑仿真器：神经质量模型+结构连接耦合，NeuroVault 26,273统计图聚类为源先验调制兴奋增益——可复用的sim-to-real数据引擎
  - Kimi Delta Attention骨干+GAU+时间倒归一化；模拟HD95 37.3mm超LCMV/sLORETA/ConvDip/DeepSIF/GBF；角色分离损失防止去噪/零空间估计器职责坍缩
  - **Activation**: EEG source imaging, null space learning, ill-posed inverse problem, lead-field matrix, BEM, neural mass model, Jansen-Rit, sim-to-real, epilepsy localization, subject-specific geometry, ESI

## 2026-10-08 - 系统工程学×量子 (Cron Job)

### Demonstration of Parallel Multi-QPU Execution for Fragment-Based Quantum Chemistry Using On-Premises Hardware
- [[parallel-multi-qpu-fragment-quantum-chemistry]] - 首个真实多QPU硬件上的分片量子化学并行化演示：FMO2+QWFS在3台室温金刚石Quoll上，shot-parallel效率93.6%，fragment-parallel修正后95.2%，异构噪声下参数策略决定精度 (arXiv: 2610.07702)
  - 负载均衡公式 N_i=N·R_i/ΣR_j 按设备实测采样率分配shots；SPAM校正后合并计数；He₂–He₁₄全簇化学精度内（1.4e-3 a.u.）
  - 关键陷阱：单机优化的电路参数迁移到三QPU异构采样时dimer全部不收敛（误差>1 a.u.）；设备专属参数或联合优化可恢复——NISQ噪声补偿不跨设备迁移
  - fragment-parallel原始效率75%源于原型接口缺作业取消（非硬件/方法缺陷），修正后95.17%；活动图逐作业诊断法可复用
  - **Activation**: multi-QPU, parallel quantum, FMO, QWFS, distributed quantum, shot parallelism, heterogeneous NISQ, load balancing, quantum chemistry workflow, HPC-QPU

### Model Predictive Control for Safety-Critical Systems Using Taylor's Theorem with Lagrange Remainder
- [[mpc-taylor-lagrange-remainder-safety]] - MPC-TLR：用精确Taylor展开+Lagrange积分余项表达安全函数未来值，必要充分条件替代递归class-K链，m个调参压缩为1个裕度δ（δ≥近似误差ε_M保安全） (arXiv: 2610.06976)
  - ZOH下用M+1中间态+数值求积近似余项；单轮unicycle避障实验中比DHOCBF/DC更安全、比HOCBF更不保守（可行性率更高）
  - 控制输入覆盖度分析：TLR/HOCBF全部N个输入进约束 vs DC/DHOCBF仅N−m_d+1——短时域（N≈m_d）时是方法选型关键判据
  - 诚实边界：TLR约束是数值近似，但四方法共享离散化误差软肋，无一对连续时间闭环提供无误差保证；inter-sampling安全是开放问题
  - **Activation**: MPC safety, control barrier function, high-order CBF, Taylor-Lagrange remainder, safety-critical control, zero-order hold, safety margin tuning, receding horizon

## 2026-10-07 - Neuroscience Research (Cron Job)

### A Time-Resolved Framework for Quantifying Neuronal Network State Transitions
- [[eiu-compositional-mea-state-transitions]] - EIU组合分析：电极×短时段三分法（兴奋/抑制/不变）+载体对照数据驱动阈值+2-simplex时间轨迹，放大MEFR等常规指标的细微药理/光遗传响应 (arXiv: 2610.08392)
  - 归一化对比度Δξ=(ξj−ξb)/(ξj+ξb)配合载体对照5%/95%分位阈值，将每个电极-片段分类为E/I/U状态，组成向量落在单纯形上（R=E+I响应度，η=log(E/I)方向平衡）
  - 4-AP预期兴奋实际表现为活动降低：初始短暂变化后进行性MFR下降（脱敏/稳态抑制样），24h洗脱后可逆——常规聚合指标完全掩盖该非单调时间剖面
  - EIU变换显著提升mean ISI和MFR的Cohen's d；D_KL已具强判别力则无进一步增益（R有界饱和）；双环谷氨酸基准显示不同细胞组成培养收敛到不同响应平台
  - **Activation**: MEA, electrophysiology, network state transitions, EIU, compositional analysis, firing rate, ISI distribution, in-vitro, 4-AP, optogenetic, drug screening

### Sensor Geometry as a Flow-Matching Prior for Multi-Channel Brain Signals
- [[graph-matern-flow-matching-eeg]] - 图-Matérn源先验：仅从传感器3D坐标建k-NN图取Laplacian特征向量，按(1+τλ)^−α配权作为flow matching源分布，零新增参数，PSD-KL降12-17%（密集导联最高40%） (arXiv: 2610.08355)
  - 消融证明增益来自物理坐标图的稀疏局部特征向量本身：打乱位置/随机正交基/经验协方差特征向量全部劣于各向同性噪声——"错误方向集中方差比无结构更糟"
  - 频谱只需平滑且满秩（热核谱保增益1.38，硬低通失败71.4因为可逆drift无法凭空创造缺失方差）；全连接图失效，图必须稀疏局部
  - 同一构造不变应用于MEG(−6%)、患者特异ECoG网格(−34-40%)、交通传感器网络(−11%)；Mumtaz-MDD下游增强使平衡准确率60.8%→83.3%（少数类召回0.28→0.79）
  - **Activation**: flow matching, EEG generation, graph Matérn, sensor geometry, source prior, volume conduction, data augmentation, SF2M, stochastic interpolants, PSD-KL

## 2026-10-07 - 医学×量子 (Cron Job)

### Linear Fitness Subspace in Protein Language Models Enables Sample-Efficient Directed Evolution
- [[linear-fitness-subspace-directed-evolution]] - LFS假设：突变引起的残基级表征变化中存在紧凑的、assay特异的线性子空间，SGES在子空间内做代理建模+不确定性估计+采集，样本高效定向进化 (arXiv: 2610.07607)
  - 位点差分坐标(site-delta)比绝对嵌入更有效：PLM表征变化中恢复低维线性子空间，少量标注即可线性访问适应度
  - 控制实验隔离增益来源：PCA/随机投影/标签打乱PLS/经典突变特征均逊于fitness-aligned site-delta坐标，证明子空间非任意降维
  - 预算感知搜索循环：每条标注双重服务（拟合代理+锐化子空间），10²-10³ oracle预算下击败zero-shot PLM和ML引导基线
  - **Activation**: directed evolution, protein language model, fitness landscape, sample-efficient optimization, oracle budget, surrogate model, drug discovery, PLM

## 2026-10-07 - 医学×量子 (Cron Job)

### Neural Petri flows for chemical reactions
- [[neural-petri-flow-chemical-reactions]] - 对任意权重都保持Petri网语义的架构：守恒(射击形式m'=m+Cσ)与使能规则硬接线为无参数层，仅学习速率律，化学反应三任务统一为射击向量读出 (arXiv: 2610.08750)
  - 硬接线不变量模式：守恒定律强制射击形式、非负性强制使能规则 → 理论强制部分做成无参数层，可学习容量只留给真正自由的部分(速率律)
  - 最小射击向量零样本基线：未训练的min-‖σ‖₁就把atom mapping做到88.8%(Golden)/88.7%(EnzymeMap)，超过RXNMapper(85.6%/77.9%)
  - 一个潜在对象多个读出：atom mapping、反应分类、正向预测统一为同一射击向量σ上的三个任务，跨任务一致性免费获得
  - **Activation**: Petri net, chemical reaction, conservation law, rate law learning, atom mapping, reaction classification, forward prediction, valence

## 2026-10-07 - Neuroscience Research (Cron Job)

### Neural networks as decision trees: an analytical solution for learning and neural selectivity
- [[activation-region-decision-tree-networks]] - ReLU网络在梯度学习不动点处分解为激活区域上的局部线性回归，低误差极限收敛到各区域最小二乘解——等价于一棵决策树（路由=激活模式划分，叶子=区域仿射变换） (arXiv: 2610.08228)
  - MAP树（Main Activation Pattern trees）数值恢复隐路由结构：用决策树从输入预测主导激活模式；编码Gram矩阵按区域分块分解，导出神经选择性几何并组织成亚群体，预测与模拟网络+两套实证神经数据（Reinert/Hajnal）吻合
  - 神经baseline调控激活模式多样性=学习分辨率旋钮：低baseline粗粒度泛化表征 ↔ 高baseline细粒度表达表征（泛化代价），连续权衡
  - **Activation**: activation regions, piecewise-linear networks, decision tree interpretation, least-squares decomposition, neural selectivity, MAP trees, encoding model, ReLU, representational geometry, recurrent equilibrium

### Common-Mode Errors Limit Low-Timestep Deep Spiking Q-Networks
- [[common-mode-compensation-spiking-q-networks]] - 低时间步SNN的Q值误差跨动作共模分量占主导，经TD bootstrap的max操作自我强化——辅助ANN替换共模分量，推理时完全移除零开销 (arXiv: 2610.07808)
  - 共模/差模误差分解：e_cm=跨动作均值误差、e_dm=相对差误差；CliffWalking精确Q*验证移除共模收益远大于差模；低T下共模RMSE≫差模（ANN则平衡）
  - CMC-DSQN：Q_CMC = Q_SNN − mean_a(Q_SNN) + Q_ANN(s)，贪心选择对逐状态常数不变⇒推理只用SNN；MiniAtar/Atari T=2超SOTA DSQN约20%、T=4超ANN基线
  - **Activation**: spiking Q-network, common-mode error, TD bootstrapping, low timestep, auxiliary ANN, energy-efficient RL, DQN, error decomposition, neuromorphic deployment

## 2026-10-07 - Medicine + Quantum Mechanics Research (Cron Job)

### Variational Quantum Attention for Molecular Graph Learning
- [[edge-aware-quantum-attention-molecular-graphs]] - VQC 只替换 GATv2 的 attention scorer：原子+邻居+键加性融合后振幅编码进 6-7 qubit，Pauli-Z 期望×可学习缩放作为 logit，消息传递/读出保持经典 (arXiv: 2610.04588)
  - BBBP 全部 6 个 ansatz 一致提升（AUC 0.6808→0.7157），5 个 scaffold-split 任务与 GATv2 竞争力相当且参数少 0.5-1.3%；无单一 ansatz 跨任务占优，深度最优 1-3 块（诚实负结果：更深反而退化）
  - Verubecestat BACE1 系列：QGAT 活性排序 Spearman 0.8264 vs 0.7954，IG 归因与报道 SAR 方向一致（5-氟吡啶正贡献 vs GATv2 负贡献）；两模型均漏掉氟苯基氟效应（~5×效力）——归因分析协议 SME+IG+activity-cliff 可复用
  - **Activation**: variational quantum attention, molecular graph, QGAT, GATv2, amplitude encoding, Pauli-Z logit, drug discovery, BACE1, BBBP, SAR attribution, integrated gradients, scaffold split, quantum machine learning

### Anthropic: Claude-shaped science (BootLoops)
- 知识图谱摄入（无新 skill）— Matthew Schwartz 提出"Claude 形状问题"方法论：寻找精确、重代码、可验证的计算问题而非阻抗失配的概念问题；BootLoops harness 完成 30 个 Feynman 椭圆积分（15 个首次计算）并跨域迁移至生态学（解决 Etienne 方程，BCI 岛树种周转率超中性理论 4.5×）与群体遗传学（1000 Genomes 57 亿突变对分析发现基因转换证据）；36 篇稿件/18 领域/19 合作者；专家雕塑循环：AI 技术正确→专家不满但重定向→共同雕塑成有意义的科学
  - **Activation**: ai-for-science, impedance mismatch, semi-numerical bootstrap, expert sculpting loop, convex hull of science
### QuPID: Quantum Parameter-Efficient Input-Dependent Retrieval Adaptation for Medical RAG
- [[qupid-quantum-retrieval-adaptation]] - 共享酉保真度检索不可训练（U†U=I 使排序与训练无关）；改用测量读出向量余弦相似度+数据重上传，60 参数击败 5.25M 参数 adapter/LoRA (arXiv: 2609.33351)
  - 退化陷阱命题：任何对 query 和 archive 两侧施加同一输入无关酉的保真度检索设计均不可训练，与 ansatz 能力无关；修复=输入相关电路（重上传）或比较测量统计量而非态叠加
  - 测量读出 z∈R^40（单比特+近邻 Pauli 期望）为输入调制二次特征图，60 参数共享指定 40 个满秩形式；重上传尺度 α 控制 Fourier 带宽=表达力旋钮；√(p/n) 泛化界激励小容量
  - 无标签对比适配（SimCLR 式、病理保留增强、τ=0.07、参数移位精确梯度）；经典模拟训练+GPU 固定参数推理，无需量子硬件；ChestX-ray14 P@5 +0.116，512 样本时对 retuned adapter 领先最大（+0.040）；诚实框架：对同预算经典 rotation-plane head 仅 +0.023（512 时 CI 含零）——优势是容量效率而非量子计算
  - **Activation**: quantum retrieval adaptation, medical RAG, fidelity degeneracy, data re-uploading, measurement readout retrieval, label-free contrastive adaptation, ChestX-ray14, MURA, LoRA alternative, low-data retrieval, amplitude encoding

### SLT: Robust Quantum Neural Networks for Noisy-Label Medical Image Classification via Supermartingale-based Label Transition
- [[supermartingale-label-transition-qnn]] - 将 QNN 预测分布熵减过程建模为上鞅，用单调性作为稳定性门控锚无关噪声转移矩阵更新——把 Born 规则导致的光滑性从缺陷转为稳定化归纳偏置 (arXiv: 2607.16293)
  - 稳定性门控：只在熵减过程单调稳定处精炼转移矩阵 T，过滤噪声驱动振荡；前向损失校正 L=CE(T·p_θ(x),ỹ) 无需锚点；收敛到稳态有证明
  - MedMNIST 5 数据集（Breast/Pneumonia/Retina/Derma/Blood）× 3 噪声类型 × 10/30/50% 比率，胜过 CE/Forward/6 个锚无关基线（T-Revision/Dual-T/VolMinNet/TVR/BLTM/CCR）；50% 噪声下 Breast 52.24%、Pneumonia 83.90% F1
  - 消融：经典 NN 温度缩放部分复现 QNN 光滑性效果——证实光滑性是操作稳定器而非量子特有计算；可复用模式：把模型弱点变成调度信号
  - **Activation**: noisy-label QNN, label noise correction, supermartingale, anchor-free transition matrix, medical image classification noise, small-data quantum, F1 robustness, MedMNIST, loss correction convergence, entropy reduction stabilization



## 2026-10-07 - Neuroscience Research (Cron Job)

### Efficiency and robustness partition the solution space for memory in recurrent networks
- [[efficiency-robustness-rnn-solution-space]] - 权重效率选低秩线吸引子 vs 活动效率选高秩非规范链式暂态放大，噪声鲁棒性与活动效率根本对立；中间活动效率+噪声训练最佳复现ALM错位编码 (arXiv: 2610.04697)
  - 最小刺激回忆任务双成本扫描：lambda->inf 选 W=alpha*c*cT 边缘稳定秩1解（与任务训练网络 simplicity bias 一致），lambda->0 选前馈链 A=-aI+kGamma 达活动下界 pi*tau/N；有效秩随 lambda->0 幂律增长（Arnoldi/Krylov 基验证）
  - 活动高效解产生错位编码：方差最大模态与因果最大模态强解离（扰动响应量化），解释 ALM 低方差残差方向超比例行为影响；伴随范数积分预测噪声敏感度，非线性 RNN 定性复现同样权衡
  - **Activation**: RNN solution space, weight efficiency, activity efficiency, noise robustness, low-rank dynamics, transient amplification, misaligned coding, ALM, Pareto frontier, nonnormal dynamics

### Recurrent network dynamics explain the time course of perceptual grouping in natural scenes
- [[gammanet-perceptual-grouping-recurrent]] - GammaNet（4层hGRU+C-RBP局部学习）在自然图像分割训练中涌现感知分组：增强活动从线索传播，动态未用RT训练即预测人类反应时间方差19.7%（噪声上限19.8%） (arXiv: 2610.05419)
  - 两阶段分组：早期沿局部边界证据扩散（内部边缘近线索时延迟2.3 timesteps），后期高层语义反馈跨内部边缘建立全局物体表征；线索-边缘距离交互效应显著（p=0.048）
  - IoU 0.74 vs SAM 0.81（参数8M vs 632M）；每训练样本隐式编码大量 same-different 配对监督；3层消融显著退化证明多尺度必要性
  - **Activation**: perceptual grouping, GammaNet, hGRU, incremental grouping, object-based attention, C-RBP local learning, human RT prediction, natural scenes, recurrent processing, visual cortex feedback

### From the Drosophila Visual Connectome to General-Purpose Computer Vision
- [[connectome-informed-flyvision-general-vision]] - 果蝇视觉连接组计算基序（ON/OFF对偶stem+三阶段循环图混合+种群交互）作为CV归纳偏置，3.7M参数在ImageNet达66.53%、胸片超ResNet18（92.76% vs 91.56%，参数少3.8×） (arXiv: 2610.08418)
  - 保守基序+容量缩放协议：Compact/Base/Large共享54张量checkpoint schema（strides与循环步数为执行超参而非状态张量）；BrainAGE扩展用共享2D编码器处理24张三轴切片+置信度调制高斯投票融合，MRI脑龄MAE 5.98年（R²=0.868）
  - 诚实负结果：迁移效应架构依赖（MNIST→CIFAR对FlyVision无效P=0.664、对ResNet18有害P=0.034、对LeNet有益P<0.001）；皮肤病学基准先做SHA-256内容审计（306重复组/37矛盾标签/63泄漏隔离）
  - **Activation**: connectomics, inductive bias, drosophila, ON/OFF pathways, recurrent graph mixing, parameter efficiency, brain-inspired architecture, medical imaging, multi-view MRI, transfer learning

### Confidence-Ordering Reversal under Contextual Priors in Neural Decoding
- [[confidence-ordering-reversal-contextual-priors]] - contextual prior融合后置信度排序反转：深排位（rank 21-50）残差误差获得更大fused margin（AUROC 0.39<0.5），46.6%的融合后误差位于反转区，重校准无法修复——需分离保留local/prior/fused三路分数 (arXiv: 2610.08229)
  - margin形成机制：repair需先闭合初始赤字G⁰ₜ故被m(s̃ₜ)≤α·Δπₜ−G⁰ₜ上界约束，residual误差可在两个错误候选间自由拉开差距；因果干预（仅变α）验证提高融合权重将正排序推向更深排位，且word-level LM prior下在准确率增益达峰后仍持续移动
  - 解法：prior自身margin在融合前读取于rank 21-50达AUROC 0.937；15特征全估计器correctness AUROC 0.954 vs 0.872，选择性输出emission 56.7%→74.5%（92%覆盖率，集合大小5.2）
  - **Activation**: neural decoding, BCI confidence, shallow fusion, repair-separation AUROC, selective prediction, MEG, language model prior, confidence calibration, error identifiability

## 2026-10-07 - Deep Learning Research (Cron Job)

### Base Models Can Reason By Taking a Cue From Training Data
- [[token-cue-reasoning-base-models]] - 起始token线索解锁base模型推理：".\n\nOkay"让Olmo-3-7B MATH-500从42%→78%，"Alright,"让Qwen3-14B从72%→87%，RL增益大部分来自让线索更可能出现 (arXiv: 2610.06851)
  - 三大机制发现：RL主要是让cues更可能出现（固定cues即恢复大部分增益）；causal data interventions可把任意词（如"chicken"）改造成有效推理线索或消除已有线索效果；不同cues的隐状态表征对应训练集不同文档类型
  - 可复用模式：cued评估（固定起始token隔离能力与倾向）、cue搜索（约束解码枚举候选）、safety案例——不同cues触发不同refusal/compliance行为
  - **Activation**: base model reasoning, token cues, reasoning elicitation, RL training data attribution, prompt prefix engineering, refusal behavior analysis

### RAISED: Self-Distillation for Robustness to Prompt Injection in LLM Agents
- [[raised-prompt-injection-self-distillation]] - 自生成工具场景+自蒸馏（student匹配teacher在clean/injected双轨迹上的clean-context行为），防间接注入且保住良性utility (arXiv: 2610.06401)
  - 识别既有防御两大缺陷机制：输出分布漂移（benign场景行为改变）+良性拒绝失效（拒绝执行工具输出指示的合法步骤）
  - 关键设计：监督信号始终是clean轨迹的teacher分布，应用到clean+injected两种输入→对攻击不变但无行为漂移
  - 防御评估三轴协议：攻击成功率、agentic基准utility、良性拒绝率（+分布漂移KL作早期预警）
  - **Activation**: prompt injection defense, tool-use agent security, self-distillation robustness, output distribution drift, benign refusal failure mode

### What Matters for Latent Reasoning with Flow Matching (FLaRe)
- [[flare-latent-reasoning-flow-matching]] - 潜空间思考五要求框架（useful/diverse/explainable/refinable/efficient）+流匹配配方：97%显式CoT精度、1/4延迟；现有方法靠捷径/蒸馏/逐token模仿多不合格 (arXiv: 2610.06666)
  - 五探针审计：反事实消融测useful、重采样熵测diverse、解码CoT忠实性测explainable、计算-scaling曲线测refinable、延迟-精度Pareto测efficient
  - 配方四要素：潜空间编码内容与塑形、flow训练位置、答案readout、最终阶段用模型自己verified thoughts训练（替代外部CoT蒸馏）
  - **Activation**: latent reasoning, flow matching LLM, continuous space reasoning, silent CoT, latent thought probes, refinable inference design

## 2026-10-06 - High-Utility arXiv Papers (Cron Job)

### Aligning Multimodal Patient Evidence with Biomedical Knowledge Graphs for Clinical LLMs
- [[aligning-multimodal-patient-evidence-with-biomedical]] - Clinical questions often depend on linking a patient's multimodal evidence to external biomedical knowledge, yet existing predictive systems rarely represent such links explicitly, so they can neither... (arXiv: 2610.06685v1)
  - Category: neuroscience

### MemPilot: Orchestrating On-Demand Multimodal Memory Curation for LLM Agents
- [[mempilot-orchestrating-on-demand-multimodal-memory-curation]] - Memory has become integral to the LLM agent ecosystem, supporting information retention and reuse across interactions. However, most existing agent memory systems construct memory in a query-agnostic ... (arXiv: 2610.06830v1)
  - Category: multi-agent-rl

### BazaarBench: Delegation Safety in Decentralized C2C Marketplaces Run by LLM Agents
- [[bazaarbench-delegation-safety-in-decentralized-c2c]] - In decentralized consumer-to-consumer (C2C) marketplaces, people list goods, negotiate with strangers, and rate one another, so trust rests on reputation. Large language model (LLM) agents now act for... (arXiv: 2610.06748v1)
  - Category: multi-agent-rl

### BrainTRACE: Tracing Longitudinal, Multimodal, and Volumetric Evidence in Brain MRI Clinical Reasoning
- [[braintrace-tracing-longitudinal-multimodal-and-volumetric]] - Brain MRI interpretation is a longitudinal clinical reasoning problem: radiologists compare serial studies, integrate information across MRI sequences, localize findings within volumetric anatomy, and... (arXiv: 2610.06571v1)
  - Category: neuroscience

### CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling
- [[clift-conformal-self-verification-for-web-agent]] - Open-source web agents are now strong enough to execute realistic browser tasks, but training them with reinforcement learning still depends on weak supervision: binary task success is too sparse for ... (arXiv: 2610.06829v1)
  - Category: multi-agent-rl

### FREA: A Multi-Source Expert Benchmark for Reaction Feasibility Verification
- [[frea-a-multi-source-expert-benchmark-for]] - As generative models and AI agents propose chemical reactions at a scale beyond expert review, feasibility verifiers decide which proposals enter synthesis planning. But do their decisions agree with ... (arXiv: 2610.06614v1)
  - Category: multi-agent-rl

### Can Agent Harnesses and Inference Engines Hear Each Other? The HEAR Protocol for Agentic LLM Serving
- [[can-agent-harnesses-and-inference-engines]] - LLM agents increasingly execute complex workflows involving multi-turn reasoning, tool use, and parallel agents. Efficient serving requires decisions that span two layers with complementary informatio... (arXiv: 2610.06597v1)
  - Category: multi-agent-rl

### SimForcing: Distilling Simulation Motion Priors into Real-Domain Robot World Models
- [[simforcing-distilling-simulation-motion-priors-into]] - Action-conditioned robot world models must respond precisely to robot trajectories while preserving realistic visual dynamics, yet learning both from heterogeneous robot videos remains challenging. Si... (arXiv: 2610.06598v1)
  - Category: multi-agent-rl

### GCTAuto-encoder: A Cross modal Framework for Security Flaw Detection in IoT Networks
- [[gctauto-encoder-a-cross-modal-framework-for]] - IoT encompasses diverse physical entities, from smart home devices to autonomous vehicles, creating a complex environment with heterogeneous security models. This heterogeneity makes IoT sub-systems v... (arXiv: 2610.06517v1)
  - Category: neuroscience

### Learning to Read the Contextual Tokens in Diffusion Transformers
- [[learning-to-read-the-contextual-tokens]] - Multimodal Diffusion Transformers (MM-DiTs) jointly process visual and textual representations throughout generation. These models repeatedly update the text tokens through multimodal attention, formi... (arXiv: 2610.06844v1)
  - Category: nlp-llm

### Mind the Accent Gap: British Accent Robustness in Speech-Driven Financial Voice Assistants
- [[mind-the-accent-gap-british-accent]] - AI voice assistants often use Automatic Speech Recognition (ASR) with LLM-based reasoning, yet existing systems struggle with regional British accents, including Scottish, Irish, and Welsh accents, si... (arXiv: 2610.06587v1)
  - Category: nlp-llm

### RealtimeWAM: One-Step Asynchronous World Action Models
- [[realtimewam-one-step-asynchronous-world-action-models]] - World Action Models (WAMs) incorporate visual representations from video generation backbones to guide action prediction. Recent efficient WAMs adopt Mixture-of-Transformers (MoT) architectures and co... (arXiv: 2610.06617v1)
  - Category: nlp-llm

### SOL: Measuring Gaps between Text Distributions by Double Sliced Wasserstein Metrics
- [[sol-measuring-gaps-between-text-distributions]] - Evaluating text generation requires measuring how well the generated distribution matches the data distribution. For autoregressive models, this is done by the perplexity. Diffusion and flow-based lan... (arXiv: 2610.06513v1)
  - Category: nlp-llm

### Topology-Informed Prompt-Conditioned Universal Segmentation of Uterine Structures from Ultrasound and MRI
- [[topology-informed-prompt-conditioned-universal-segmentation-of-uterine]] - Multi-structure segmentation of the uterus is important for computer-assisted screening, diagnosis, and treatment planning of uterine diseases, where ultrasound and MRI provide complementary clinical ... (arXiv: 2610.06494v1)
  - Category: multi-agent-rl

### Back to the Future: Rethinking EDA Infrastructure for Agentic Systems in Chip Design Verification
- [[back-to-the-future-rethinking-eda]] - The unprecedented computational scale of modern artificial intelligence depends on complex, multi-billion-transistor Systems-on-Chip, yet the workflows that verify these chips remain stubbornly manual... (arXiv: 2610.06790v1)
  - Category: multi-agent-rl

### Decoupling Time and Space: A Temporally Conditioned Refinement for EEG Source Imaging
- [[decoupling-time-and-space-a-temporally]] - Electroencephalography (EEG) offers millisecond temporal resolution, but inferring underlying neural sources is a severely ill-posed spatial inverse problem. While deep learning has advanced spatial r... (arXiv: 2610.06726v1)
  - Category: neuroscience

### Reading the Mood: Emotion-Guided Book-to-Music Recommendation via CGANs and LLMs
- [[reading-the-mood-emotion-guided-book-to-music-recommendation]] - Background music that matches the mood of a text has been shown to make readers feel more immersed and improve their reading experience, motivating recommender systems that pair books with mood-matche... (arXiv: 2610.06703v1)
  - Category: neuroscience

### Conditional Flow Matching for Single-Neuron Electrophysiology: Capturing Multimodal Responses Across Stimuli
- [[conditional-flow-matching-for-single-neuron-electrophysiology]] - Neurons of the brain exhibit a rich repertoire of electrophysiology dynamics with the same repeated stimulus eliciting very different voltage responses from the same cell. One common approach in bioph... (arXiv: 2610.06520v1)
  - Category: neuroscience

### Recursive Video In-Context Learning for Agentic Robot
- [[recursive-video-in-context-learning-for-agentic]] - LLM agents that orchestrate frozen vision-language-action (VLA) policies improve across episodes through text memory, which records what the agent did but not how the task is done. A demonstration vid... (arXiv: 2610.06843v1)
  - Category: multi-agent-rl

### Out-of-control Hamiltonian Learning
- [[out-of-control-hamiltonian-learning]] - Learning the Hamiltonian of a many-body system from its dynamics is a central task in quantum science, yet the algorithms with the strongest provable guarantees assume some level of quantum control--f... (arXiv: 2610.06709v1)
  - Category: quantum

## 2026-10-06 - Neuroscience Research (Cron Job)

### Causal discovery identifies pathways linking physical activity to dementia risk in the UK BioBank
- [[llm-guided-causal-discovery-dementia]] - LLM五阶段特征选择漏斗（预筛→4模型评分→专家agent复审→排序→人工策展）把UKB全字典压到39变量再做PC因果发现+SEM链式中介：抑郁是核心可调制通路 (arXiv: 2610.02221)
  - 4个GPT系模型+多领域专家persona独立打分聚合（阈值0.60），配合背景知识结构约束（人口学变量强制无父、痴呆强制汇聚点）+非参数bootstrap报告每条边的结构稳定性
  - MVPA→抑郁→痴呆中介15.06%（男19.31%/女12.27%）；5年排除窗后男性中介占比升至60.8%、直接效应消失；步行速度链仅3.13%；心血管/CKD长程通路bootstrap稳定性仅0.07-0.10被诚实标注为弱证据
  - **Activation**: LLM feature selection, causal discovery, PC algorithm, chain mediation, UK Biobank, dementia pathways, epidemiology LLM agents

### Embodied Neurocomputation: Interfacing Biological Neural Cultures with Scaled Task-Driven Validation
- [[embodied-neurocomputation-framework]] - 生物神经培养皿的编码参数首个大规模优化：Optuna分布式HPO+26个CL1 MEA培养物筛1,300组合，12个可学习配置在同交互预算下击败调优DQN 1.18-1.25× (arXiv: 2605.13315)
  - y_t=[d∘b∘e](x_t)四模块形式化；率编码6参数(F_min/F_max/幅度/脉宽/tick率/每步tick数)；SHAP显示最大刺激频率主导(40-60Hz最优)、高幅度2.5µA+短脉宽40µs+快交互
  - 分布式练习>连续练习：5×30步+2分钟休息胜过1×150步，学习从第3集涌现；Permuted+Matched Media消融证实生物贡献(p<0.001)；CL1硬件功耗中位数22.7W
  - **Activation**: BNN encoding optimization, bio-silicon hybrid, CL1 MEA, embodied neurocomputation, living neural computing, stimulation parameter search

## 2026-10-06 - 计算机科学 + 量子力学 (Cron Job)

### SpiderCSS: Scalable Fault-Tolerant CSS State Preparation
- [[spidercss-fault-tolerant-css-state-preparation]] - ZX-calculus fault-equivalent rewrites compile FT CSS state-prep circuits by construction, no verification needed (arXiv: 2610.03714)
  - 任意CSS码容错态制备多项式编译：理想化ZX图出发，仅用fault-equivalent重写（普通unfusion破坏FT性，Lemma II.18），FT由构造保证
  - SpiderCat 3-ary分解给出可证最优CAT态CNOT数 + MDSF路由 + 4种目标可选调度（depth/width/lifetime）；vs FaO: CNOT −53.8%、深度~10×、LER −90%、接受率+9.5%，d≤15全多项式
  - **Activation**: fault-tolerant state preparation, CSS codes, ZX-calculus, fault-equivalent rewrites, CAT states, SpiderCat

### Prospective Hindsight: Self-Calibrating Reinforcement Learning via Prediction-Reality Gaps
- [[prospective-hindsight-self-calibrating-rl]] - RL前自评与事后验证差距做surprise重加权(1+αξ)·loss，校准作为优化副产物涌现 (arXiv: 2610.02740)
  - CS/OF/US/AF四格校准分类学：off-diagonal（过自信失败OF+欠自信成功US）= surprise；stop-gradient标量门控，唯一超参α，α=0精确退化为baseline
  - 精确残差恒等式 R(θ)=c(θ)·M(θ)（surprise残差=误校准集平均损失×误校准率=Brier分数）；自熄灭退火机制；Science Q&A OFR 34.2%→20.9%，选择而非梯度质量驱动增益
  - **Activation**: RLVR calibration, prediction-reality gap, surprise-weighted advantage, overconfident failure, LUPI, GRPO calibration

### VenusRL: A Fully Disaggregated Agentic RL System
- [[venusrl-disaggregated-agentic-rl-system]] - 按critical-group优先调度+模板键页共享池，端到端agentic RL训练加速4.24× (arXiv: 2610.03286)
  - 训练步被完整GROUP阻塞而非GPU空闲：长度预测启发式识别最可能解锁下一步的组，优先级贯穿批准入/KV驻留/跨worker编排三层
  - template-keyed页池按(模板,偏移)共享物理帧（免内容扫描），lazy CoW隔离；动态内存admission+迁移逃生舱；vs Slime/RollFlash/ThunderAgent 1.06-4.24×
  - **Activation**: agentic RL training system, critical group scheduling, length-prediction heuristic, template-keyed page pool, KV cache residency, sandbox memory stranding

## 2026-10-06 - Neuroscience Research (Cron Job)

### Autoregressive Frontier Expansion: Growing Trees with Graph Machine Learning
- [[frontier-expansion-tree-generation]] - 迭代前沿扩展联合生成神经元/树形态的拓扑+几何：SO(2)-等变GNN+flow matching逐层生长，构造性100%有效树 (arXiv: 2609.38506)
  - 每层两步：frontier expansion（预测每个活动叶节点分叉Γ∈{0,1}或终止）+ localisation（父相对偏移C），移位后合并为单一条件分布 pθ(Cℓ,Γℓ|T̃ℓ)；Γ∈{−1,+1}对称化使采样阈值=0；K=10 Euler步
  - SO(2)-EGNN：不变边特征(轴向dᵢⱼ+垂直ρᵢⱼ+方位角ψ+倾角φ)+局部坐标系(fᵥ,sᵥ,û)由父分支方向继承、与输入共旋转⇒等变输出；树边消息传递+每两层induced-set attention跨深度传信息；soma根一次创建k≤23个初级树突（rank one-hot区分共享frame的兄弟）
  - MICrONS 26,469皮层神经元+3,386棵植物树：构造性100%有效树 vs SemlaFlow 76.6%/12.5%；∆MMD²=0.0393 vs 0.2521/0.8436；密度0.876覆盖0.798；F=64仅1.57M参数仍胜22.3M基线；采样快20×（D20树0.617s vs 12.317s）；TMD持续同调条件化使生成跟随目标（91%比随机配对近）
  - **Activation**: neuron morphology generation, dendritic arbor synthesis, frontier expansion, flow matching 3D, SO(2) equivariant GNN, TMD persistence conditioning, MICrONS, branching structure generator, connectome augmentation

### Response Variability and Stability in Human Reasoning
- [[reasoning-pattern-energy-geometry]] - 推理模式=度量空间间映射f:(X,dX)→(Y,dY)，p-energy(Dirichlet能量推广)量化个体响应变异性：高能量仅在初始错误时预测改进 (arXiv: 2610.03008)
  - 任务编码入H₆：量词→(普遍性,极性)双比特嵌入atmosphere理论，格→(传递性,方向)嵌入TransSet；响应入H₄且NVC映射原点、O响应最近NVC（嵌入PHM O-heuristic）——理论驱动编码胜one-hot（ΔAIC=−25）
  - 局部2-energy E²(f;x)=平均邻居响应距离²=个体×任务级变异性分数；k-means聚出3类推理者（正确低能量0.307/高能量0.471/方向偏好0.389），PC1↔能量PC2↔方向
  - GLMM关键发现：C×E²交互β=−0.438***——高能量翻转效应：初始正确高能量→重测保留率降(OR 0.72，非系统化运气)；初始错误高能量→改进概率升(OR 1.41，不稳定态易修复)；"稳定错误"者难改进。模式稳定性：1_{i=j} LMM β=−2.44***，个体推理模式是跨时间稳定的指纹
  - **Activation**: reasoning pattern distance, response variability metric, p-energy cognitive modeling, syllogism analysis, GLMM test-retest, metric geometry psychology, individual differences clustering, Dirichlet energy behavior

## 2026-10-06 - Quantum QEC + CS (Cron Job)

### Homological Thresholds in Randomly Monitored Quantum Error-Correcting Codes
- [[homological-percolation-monitored-qec]] - 随机Pauli测量下QEC码逻辑存活阈值分两类：几何渗流(toric, ν=4/3) vs 同调渗流(color, ν=1.2073新普适类) (arXiv: 2610.02310)
  - 逻辑支持判据：测量算符乘积（稳定子等价下）支撑非平凡逻辑Pauli ⟺ 逻辑信息丢失；色码弦在三叉结点分叉 → 非路径连通性
  - 1.4M比特模拟引擎：face-syndrome F2二元消元(~32×存储节省) + 二项卷积技巧（逐比特加入 → 单次运行出全概率曲线）
  - 阈值不等式：γc ≥ rc（渗流阈值下界弱测量学习阈值）；MW解码阈值 ≥ qP(μlog)；Wen/toric-Y 全 r 达最优 1/2
  - **Activation**: homological percolation, monitored QEC codes, random Pauli measurements, coherent information, color code critical exponents, Nishimori thresholds, measurement-induced transitions

### Fault-tolerant and Fully Addressable Unitary Logical Gates via Round-Robin Sparsification
- [[round-robin-sparsification-addressable-gates]] - 2DTI qLDPC码可寻址容错横向逻辑CZ：RR电路+稳定子形变逐列稀疏化 → 深度3与码距无关 (arXiv: 2610.03594)
  - Cylinder trick取O(d)不相交等权逻辑代表元（Z-对称性半格圆柱内稳定子乘积分解为两个等价逻辑）；交替α↔β逐列共轭消CZ²
  - vs gross code surgery：~4×时空开销降低、~5×LER影响降低；memory-like O(p^d) 缩放 d=3..9 验证
  - 实证教训：cHGP3 naive tCZ距离降d/2但LER与满d优化版几乎不可分（高权错误组合多重性主导）→ 渐近距离≠实际LER
  - **Activation**: addressable logical gates, qLDPC transversal CZ, round-robin sparsification, cylinder trick, stabilizer deformations, gross code gates

## 2026-10-06 - Neuroscience Research (Cron Job)

### Self-Repairing Recurrent Ensembles for Real-Time Recovery from Distribution Shift
- [[rtr-ftl-self-repairing-ensembles]] - 掩码RNN集成+Kalman融合共识自监督：传感器漂移/故障/噪声下的实时免专家自修复 (arXiv: 2610.03249)
  - 每个成员只看随机掩码后的观测子集（可见率0.5-0.7）制造多样性；高斯输出经顺序Kalman增益融合，困惑成员报高方差自动降权；融合均值作为自监督标签，按 (1−k̄²) 权重把困惑成员拉回共识——TTRL从离散多数票转置到连续动作分布
  - RFLO（RTRL的生物合理近似，去非局域Jacobian项+固定随机反馈B）每步出梯度，无BPTT回放缓冲，控制循环内实时更新；同一套机制换标签源即得RTR-IIL（专家在场时全在线EnsembleDAgger）
  - 关键结论：鲁棒性来自掩码诱导的多样性而非集成或融合本身——全可见集成同样漂移下崩溃且无法恢复；传感器偏移/完全故障/渐增噪声三种shift均恢复至接近原性能（brax ant/halfcheetah/humanoid，10 seeds）
  - **Activation**: recurrent policy self-repair, Kalman fusion ensemble, RFLO online gradient, distribution shift recovery, follow-the-leader consensus, random observation masking, RTR-IIL online imitation, test-time adaptation control

### Toward Controlling Biology with Language: Offline Learning of Prompt-Conditioned Interventions for Cells, Organoids, and Biobots
- [[offline-vlm-judged-language-to-intervention]] - 存档+VLM裁判离线学习语言→干预映射：xenobot自然语言接口80%留出准确率 vs 66.7% chance (arXiv: 2610.02247)
  - 湿实验室配对数据太贵→固定存档(101批次真实电刺激时长×PRE/POST轨迹)当离线数据集；VLM零样本裁判打分(轨迹与prompt匹配度, 3333对一次性算完)，全程零新实验零人工标注
  - 每prompt拟合logistic曲线 r̂_p(d) 化为可微目标 d†(p)，反向传播训练P2I网络(SBERT冻结编码→每行为类别一个sigmoid头，防止对立目标梯度干扰)；backprop/REINFORCE/CMA-ES三个优化器共享同一奖励表交叉验证最优
  - VLM裁判必须看原始位置轨迹而非预计算速度（r=0.843 vs 0.49-0.66，逼真推断反而更可靠）；112配置网格搜索做了200次置换检验防p-hacking；数值替代目标训练loss相同但GT2崩到59.1%（低于chance）——VLM奖励非冗余
  - **Activation**: language-controlled biology, VLM-as-judge reward, offline archive learning, prompt-to-intervention, xenobot bioelectric control, zero-shot reward validation, contextual bandit living systems

## 2026-10-06 - 计算机科学 + 量子力学 (Cron Job)

### All Work And No Play Makes Jack a Dull Boy: Understanding and Preventing Catastrophic Strategy Collapse in RLVR
- [[rlvr-strategy-collapse-mesh-learning]] - RLVR后训练的灾难性策略崩溃：策略容量收缩理论与Mesh Learning防护 (arXiv: 2610.02835)
  - 策略=轨迹耦合核等价类（Fisher分数内积K_ij），与人类可识别解法对齐；Thm1非崩溃态下GRPO/DAPO/GSPO必然把概率质量集中到单策略，Thm2非平凡准确率需要最低策略容量（幂律），两者冲突=准确率悬崖的机制解释；Thm3固定KL/JS惩罚在ΔR/β≥C_D时必然失效
  - Mirrored Entanglement Index（MEI=‖Σv_i‖²/Σ‖v_i‖²，纯前向logit梯度）在精度悬崖前提前越过3σ阈值(1.013)，轻量在线预警；Mesh Learning=Coach Prompting（离线教练LLM生成m=4策略前缀、loss-mask、推理时自提策略）+策略平衡正则（对冻结参考策略的softmax(z−z_ref)均匀JS，μ=1e-5，平移不变只控相对增长）
  - AIME26上Qwen3-4B 43.3%→56.7%（+13.4pp）、Phi +11.5pp，AIME25/26、MATH-500、GPQA、LiveCodeBench全面胜过GRPO/DAPO/GSPO/+KL/+JS五个基线，Pass@k增益保持
  - **Activation**: RLVR strategy collapse, GRPO late-stage collapse, MEI warning signal, mesh learning, coach prompting, strategy balancing regularization, LLM post-training stability, reasoning diversity

### Efficient fidelity simulation of high-rate magic distillation circuits
- [[affine-diagonal-fidelity-simulation]] - 仿射-对角电路（X/CNOT/T/CCZ层级门）的精确容错保真度模拟：反向传播使非Clifford演化从重叠中消去 (arXiv: 2610.03605)
  - 基准测试比完全模拟容易：引理1传播Pauli错降一级（UPU†∈X·D^(ℓ−1)），引理2传播错交换子降两级，ℓ=3时交换子是Z型Pauli→syndrome分布在仿射空间s₀+V⊥上精确均匀采样（高斯消元），逻辑保真度退化为stabilizer态重叠
  - O(n³T)每Monte Carlo样本且与逻辑量子比特数无关→解锁高码率：[[27,3,3]] tricycle三块深度2 CCZ幻态工厂优化，共享ancilla块Z-syndrome提取+metacheck修复最优（infidelity~1e-7量级），并验证Pauli-twirl近似无大偏差；ℓ=4给出无偏稳定子校验估计器
  - 覆盖hypercube-IQP（[[8,3,2]]，预计算n^2.51）、transversal-T/常深CCZ的rainbow/GBP/sheaf qLDPC、魔态cultivation检验（H_XY、Steane H态的K=SH框架变换）与带前馈的传送门
  - **Activation**: affine-diagonal circuits, Clifford hierarchy error propagation, syndrome sampling, magic state factory benchmarking, tricycle code, qLDPC CCZ, exact FT simulation, Pauli twirl validation, high-rate codes

### Breaking the chain: geometry-native state preparation with ASPIRE
- [[aspire-geometry-native-state-preparation]] - 按纠缠几何而非1D链序选门：RQMI评分+最大权匹配+Procrustes精修的MPS近似态制备 (arXiv: 2610.03528)
  - 每对候选qubit做一次4×4本征分解同时得到最优解纠缠门与可移除互信息R_ij（门=把ρ_ij本征向量按序映射到计算基）；按路由成本归一化R̃=R/c（3 CNOT+每SWAP加3）后阈值过滤，Edmonds blossom最大权匹配并行层，重算迭代至预算B
  - 理论保证：总关联T=ΣS(ρ_a)即到积态的相对熵距离，不相交门精确可加（Prop1贪心坐标下降）；残差单点marginal给出保真度证书ε*≤Λ/(2−Λ)≤T/2（系数Λ/4紧）；位置置换不变性免于snake-mapping病态
  - 全连通ASPIRE在⌈log₂N⌉层精确制备GHZ_N（最优，staircase需N−1）；Bell对晶格比MPD少数量级门；heavy-hex原生门无SWAP网络仍胜MPD+路由；早期容错区以远低于精确制备的T数饱和到应用可用保真度（QPE guide state场景）
  - **Activation**: MPS state preparation, matrix product disentangler, removable quantum mutual information, entanglement geometry, maximum weight matching, hardware-native compilation, QPE guide states, amplitude encoding, Procrustes optimization

## 2026-10-06 - Neuroscience Research (Cron Job)

### Emergent Topology of Optimal Networks for Synchrony
- [[synchrony-optimal-network-emergent-topology]] - 预算约束下同步最优网络的涌现拓扑：可微图优化发现稀疏/二部/细长/极端同邻性四大结构印记，构造性理论给出配对函数ν⁻(ω)与变分强度分配s(ω)，同步阈值消失+r~1-b⁻²幂律 (arXiv: 2509.18279, v4 2026-10-02)
  - 预算映射Aij=Nb(Pij²+Pji²)/ΣP²kl保证对称非负精确预算，torchdiffeq全可微计算图对⟨r⟩做autodiff梯度上升——"用NN训练硬件做最优网络科学"；五大振子模型（Kuramoto/Sakaguchi/摆方程/Stuart-Landau/混沌Rössler）一致涌现四印记
  - 构造性理论：ωg(ω)dω=±νg(ν)dν自洽方程的两个分支ν⁺(快配快,次优)与ν⁻(快负配慢正,全局最优)，梯度优化独占收敛ν⁻，统一了文献中冲突的数值观察；强耦合闭式解s(ω)∝b|ω|/(χ|ω−ν|^{1/3})首次解析解释"快振子分更多耦合资源"
  - 临界预算bc=(2/max H)∫₀^∞ωg(ω)dω可计算，r=rc+κ(b−bc)^{1/2}方根临界标度，强耦合1−r=χ³/4b²；最优网络证明无同步阈值（预算集中于战略边，无需发散节点强度）
  - 欧洲大陆电网实证：固定拓扑按长度成本σ重配权重，σ→1优化解收敛到经验配置（电网部分被同步优化解释）；同成本下Δr=0.164提升主要来自将耦合从短线路移向长线路——长距离输电相对其同步价值投资不足
  - **Activation**: synchrony-optimal network, coupling budget allocation, differentiable network optimization, monophily, bipartite frequency pairing, Kuramoto optimal topology, power grid swing equations, emergent network design, optimal network science
## 2026-10-05 - 神经科学 + 量子纠错 (Cron Job)

### Dark Signals in the Brain: Augment Brain Network Dynamics to the Complex-valued Field
- [[complex-valued-dark-signals-brain-dynamics]] - Hilbert变换"暗信号"作为共轭动量，将脑动力学提升为复值哈密顿场，薛定谔样方程建模全脑活动 (arXiv: 2509.24715)
  - 复值提升使线性短时程预测相关系数 0.12→0.82，非线性非平衡拟合 0.47→0.88
  - 哈密顿量 H 给出有向有效连接、层级内禀时间尺度；静息→任务重构 = 全局缩放 + 定向重连
  - **Activation**: complex-valued brain dynamics, Hilbert transform, Hamiltonian neural ODE, effective connectivity, fMRI/EEG generative model

### What Must a Quantum-Memory Decoder Know About Temporally Correlated Noise?
- [[temporal-noise-calibration-qec-decoder]] - 相同syndrome统计的两种时间相关噪声模型需要不同逻辑校正：解码器校准损失可达1/2，校准成本Θ(θ^-d_X) (arXiv: 2610.03545)
  - frozen-sign vs redrawn-sign 对抗对：单interval统计相同但相干积累不同——噪声不可知解码器的单元测试
  - 2个自由interval再提取可将校准成本从 Θ(θ^-d_X) 指数级降至 Θ(θ^-2)
  - **Activation**: temporally correlated noise, QEC decoder calibration, coherent error accumulation, syndrome extraction scheduling, non-Markovian noise

## 2026-10-05 - Neuroscience Research (Cron Job)
### NeuroLens: Learning Latent Embeddings of Neural Semantics from Chronic Recordings
- [[neurolens-jepa-chronic-recordings]] - JEPA自监督框架从慢性神经记录学习去噪表征：潜空间预测分离表征可塑性与电极漂移，校准签名神经元身份支持零梯度跨session适配 (arXiv: 2610.02864)
  - Day-adaptive cross-attention encoder：41维生理签名（FR stats+ACG+population coupling）经MLP生成neuron embedding注入token，替代固定ID实现未见神经元迁移；Utah array通道改用hypernetwork FiLM按天条件化
  - SIGReg特征函数正则（匹配各向同性高斯）防坍缩，替代启发式stop-gradient；因果transformer AR predictor跨天共享参数强制稳定预测结构
  - 实证：IBL 53天Neuropixels choice解码+6% vs causal NDT，latent effective rank跨天稳定（NDT随神经元丢失下降）；人类ALS语音sentence-embedding解码+38%，GF模式（64 calibration trials零梯度）仍超SPINT/POSSM
  - **Activation**: JEPA, chronic recordings, representation drift, neural population nonstationarity, few-shot BCI, cross-attention encoder, effective rank, self-supervised neural decoding, calibration-based neuron identity

### Parallel Time-Aligned Spiking Self-Attention for Consistent Integer-Valued Training and Spike-Driven Inference
- [[pt-ssa-temporal-interaction-mismatch]] - SFA/I-LIF压缩训练与脉冲推理的算子级失配TIM：O_train含全部跨时间三元组Q_iK_j^TV_k而O_inference只保留对角项，SDT-V3在ImageNet掉27.78pp；PT-SSA重建D个虚拟脉冲切片按时间对齐并行计算注意力再求和，gap降至0.06pp (arXiv: 2610.03291)
  - 脉冲重建X_d=1[C_X>d]全并行+单位STE梯度路由（D虚拟步梯度求和聚合到压缩激活）；Adaptive PT-SSA每块学一个标量θ_l=exp(clip(a,-8,8))等价调节SFA有效阈值，LSQ式1/√(MD)梯度缩放
  - 算子级验证：D=4相对L2误差7.41→1.6e-4（SFA）；SSA gap随D恶化（D=8时26.99→15+pp）而PT-SSA全D稳定<0.3pp——发放计数守恒≠算子等价
  - Triton-fused内核逐tile重建-计算-累加避免物化重建张量，吞吐仅比I-LIF SSA低5.4%（5797 sample/s），比recurrent LIF SSA快2.91×；ImageNet-1K 74.53% spike-driven Top-1
  - **Activation**: spiking transformer, temporal interaction mismatch, train-inference consistency, SFA, I-LIF, spike-driven attention, virtual time step expansion, adaptive firing threshold, Triton kernel

### A Distinct Communication Strategies Model of the Double Empathy Problem
- [[double-empathy-dyadic-feedback-collapse]] - 首个 double empathy problem 机制模型：言语/非言语通道偏好差异经"感知缺口→防御性↑→共情输出↓"正反馈环即可复现共情崩溃；Jury 稳定性判据 L > (1−λ_A)(1−λ_NT)，环增益 L = 0.0072(ρ_A+1)(1−D_A/100)(1−D_NT/100)，ρ_A（言语输出衰减比）双重脆弱=更低激活阈值+更强耦合 (arXiv: 2602.02562)
  - 核心要点：120 组仿真 16.7% 崩溃全部在 ρ_A≥1.0；双稳态（D*≈0 健康态 vs D*≈80 崩溃态）由 separatrix 分隔，稳定盆地大小近似反比于环增益（L 翻倍≈盆地减半）；ρ=0.5→+35.45% 盆地，ρ=2.0→−34.33%
  - 核心要点：崩溃轨迹瞬态特征值超 1（λ_max=1.105@step8）驱动爆发增长后回落<1——崩溃态局部稳定不可逆；轨迹形似 Kindleberger 大萧条螺旋；4 个可证伪预测+测量协议（c_p 因子设计回归、ρ 压力诱导衰减比、D[0] 假反馈操纵、纵向三阶段 dyad 设计）
  - **Activation**: double empathy problem, dyadic social coupling, empathy collapse, feedback loop, Jury stability, loop gain, separatrix, channel preference mismatch, autism, computational social neuroscience, 可证伪社会动力学模型

### Reduced Hodgkin-Huxley models based on the correlation between sodium and potassium gating variables
- [[reduced-hodgkin-huxley-gating-correlation]] - 用 h ≃ c(I)−n 门控相关（FitzHugh 1961 遗产，c 是电流依赖的修正）把 4D HH 降到 3D/2D 且保持 Bautin 余维2 分岔结构（I_SNLC/I₁/I₂ 三点对齐），并推导动作电位传播统一幂律 v = a/(C_m·R^b)，b=0.55/0.52/0.66 (4D/3D/2D) (arXiv: 2402.19185)
  - 核心要点：消去方向性关键——快门控 m 可绝热消去（m→m_∞ 保有振荡），慢门控 n 不可（n→n_∞ 退化成无 Hopf 全稳态模型）；c_3D(I)=I^−0.0674、c_2D(I)=I^−0.078 幂律依赖刺激
  - 核心要点：传播存在性区间 R∈[R_m0,R_M0]，内部更窄区间产生周期尖峰列、边缘区间只传单个孤波尖峰后回静息；轴突中段注入产生双向尖峰对撞湮灭——突触前信号可"诞生于中段"；周期幂律 per∝I^−0.35~−0.49
  - **Activation**: Hodgkin-Huxley reduction, gating variable correlation, action potential propagation speed, cable equation, Bautin bifurcation, solitary spike, axon internal resistivity, neuron model simplification, HH 降维

## 2026-10-05 - 神经科学×量子力学 (Cron Job)

### Existence of an infinite family of IIT substrates with arbitrarily large Phi
- [[iit-infinite-family-exclusion]] - XOR 环基底：N≥8 且 3∤N 时每单元取自身+两个顺时针邻居的 XOR，在所有状态满足排他公理（complex，φ_s≥4），全 1 态 Φ≥2^⌊N²/8⌋·(1/2)^N/(2N)−1 即 log₂Φ=Ω(N²)——首个 Φ 增长的无限族；全部定理（除 Prop 6.2 外）Lean 4 内核认证，人类战略指导+LLM 逐文件证明 (arXiv: 2610.02219)
  - 核心要点：损伤计数归约 φ_s(θ)=dmg(θ)——XOR 确定性动力学下排他性的嵌套优化精确归约为组合计数；屏蔽见证分区（删除单元移除活输入使弧头免于损伤）证明真子系统 φ_s<4；区分=恰好是弧（N(N−3)+1 个，41/71/89/131@N=8,10,11,13 穷举验证），公共单元的 |F|≥N²/8 个区分的子集全为 relation → Φ≥(2^|F|−1−|F|)·c
  - 核心要点：F₂-循环矩阵 C=I+P+P² 可逆 ⟺ 3∤N（1+x+x² 的根为三次单位原根）；稀疏均匀局部规则即可产生天文级 Φ（N=40 时 1.8e46）——反驳"大 Φ 需要密集连接"；形式验证无法发现错误猜想（原双指数猜想被"不可约部分全是弧"推翻）——"主要风险是对无法支撑结论的对象做正确推理"
  - 本地复现：循环矩阵可逆性 37/37 例吻合；区分计数与 Φ 下界数值（8.85/35.6/2.05e3/2.68e7/1.83e46）与论文全部精确一致
  - **Activation**: integrated information theory, IIT 4.0, Phi lower bound, exclusion postulate, XOR cycle, circulant matrix F2, Lean 4 formal verification, AI-assisted proof, consciousness substrate, damage count reduction, shielded witness partition

### Generalization of Transformer-Based Neural Quantum States via In-Context Learning
- [[nqs-transformer-icl-generalization]] - Transformer NQS 的首个 ICL 泛化理论：逐点 MSE 随上下文样本数 N 与深度 L 双重反比下降，所需深度与系统规模线性相关（连续 nD / 离散 nd），秩一密度算符扩展到全量子态物理约束界；证明链=通用特征表示→Lasso 稀疏系数→Transformer 逐层实现非精确近端梯度→误差可加复合 (arXiv: 2610.03463)
  - 核心要点：深度=优化迭代数、样本数=样本量，乘积驱动 MSE ∝ 1/(NL)；线性深度-规模关系来自系数空间稀疏性而非希尔伯特空间维度；sigmoid 注意力（非 softmax）对可证 ICL 泛化已足够
  - 核心要点：ICL 即隐式优化——任何回归型 ICL 主张可通过"展示权重使 attention+FF 层执行已知收敛优化器（近端梯度）"证明；实/虚分解参数化的对称性诱导偏置是开放问题；架构预算规则 L=Θ(nD) 或 Θ(nd)
  - **Activation**: neural quantum states, transformer ICL, generalization bound MSE, rank-one density operator, proximal gradient Lasso, depth linear scaling, quantum many-body ML, in-context learning theory, NQS architecture budget



### Cup and Cap Topological Neural Network
- [[cup-cap-topological-neural-network]] - 用代数拓扑的 cup（升）/cap（降）积替代 boundary operator+Hodge Laplacian，突破 ∂²=0 导致的"单层只能跨一维"限制：节点0-cochain 一步 cup 到三角形 2-cochain 再 cap 回节点，单层完成 node→triangle→node 信息往返 (arXiv: 2610.03169)
  - 核心要点：cap(ξ̂⌢α¹) 退化为图 Laplacian 作用的标准 GNN 传播是 CCNN 特例；三角形消息项 T[r]=Σa_rsm·f(χ_sm)·(θ[s]+θ[m]−2θ[r]) 显式实现"节点被其所在团簇对面边调制"；Faskowitz 2020 脑 edge signals（ξ[rs]=θ[r]θ[s]）本质就是 cup product 特例
  - 核心要点：TopoBench 20数据集（Clique Lifting）8/20 胜过 SCN/SCCN/SCCNN 全部 simplicial 基线、13/20 处于全域最优 1σ 内；Pubmed 89.74 超全域最优、MUTAG 82.55、ZINC 0.55 显著超 SCCNN 0.36；Amazon 上 simplicial 基线 OOM 而 CCNN 正常运行
  - **Activation**: topological deep learning, cup product, cap product, Hodge Laplacian limitation, triangle message passing, simplicial complex neural network, higher-order brain network, 脑网络高阶结构, clique lifting

### Contrastive Neural Embeddings Reveal Individual Traits Beyond Conversational Role
- [[contrastive-embedding-retraining-nulls]] - 分组数据对比嵌入必须用"重训练零假设"：组内恒定标签是组身份的粗粒化，冻结嵌入置换检验p=0.001而逐置换重训练编码器p=0.50——同一数据同一标签相差三个数量级；CEBRA流形按个体组织（说话/听话角色解码=0.474 vs 0.501 chance，同个体跨角色余弦相似度0.957），参与者级AQ从身份感知零假设中分离(p=0.0099)但仅"分级"而非"分区"流形(silhouette=-0.167) (arXiv: 2610.03410)
  - 核心要点：冻结嵌入置换只检验"学到的几何是否恰好包含标签分区"，编码器学到组身份时必然显著——它检验几何而非标签；重训练置换检验"任意重新分组能否产生可比几何"
  - 核心要点：诊断工具=球面混合结构/类内散度追踪身份而非特质、球面KS统计量、跨条件余弦相似度；结论：dyadic标签设计无法独立于dyad身份识别神经相关物，需要组内变化标签的设计
  - **Activation**: contrastive embedding permutation test, retraining null, CEBRA dyad decoding, group identity confound, hyperscanning inference, retrain-per-permutation control, 分组对比嵌入零假设

### Aggregate accuracy conceals concentrated temporal vulnerability in a spiking speech classifier
- [[snn-temporal-vulnerability-census]] - SNN时间脆弱性穷举普查：保留SpikeSCR冻结分类器725,070个相邻bin单计数扰动邻域的全部预测——均匀采样期望准确率反而从84.00%升到84.54%（净改善掩盖伤害），但13/84初始正确utterance存在adverse邻居且5个source承载93.21%的有害扰动；穷举普查揭示聚合指标无法区分的"发生率-浓度-内部变化-执行依赖"四维结构 (arXiv: 2610.03155)
  - 核心要点：四分类结果taxonomy（class-preserved 96.44% / adverse 0.71% / corrective 0.63% / lateral 1.25%），flip rate混淆有害/有益/错→错转移；margin与adverse率负相关(ρ=-0.5688)但margin/梯度排序都漏掉不同稀有source，梯度前缀定位全部13个脆弱source仅需73.45%普查成本
  - 核心要点：执行契约必报——batch-256 vs singleton差0.26pp但617/9,981标签翻转；padding改344个标签；批序反转改531个标签，机制=q/k路径将[B,h,T,d]重塑为[T,B,N]使不同source进入同一膜电位lane的时间轴（跨source耦合），联合q/k隔离恢复逐位序不变性；两个种子replica准确率几乎相同但类变化计数差5.21倍
  - **Activation**: spiking network temporal robustness, spike retiming vulnerability, exhaustive perturbation census, batch-order dependence LIF, source-level bootstrap, 执行契约, adjacent-bin neighborhood, spiking speech commands
## 2026-10-05 - 神经科学×量子力学 (Cron Job)

### A Path Integral Model of Cognition
- [[path-integral-cognition-projector-hamiltonian]] - 认知的路径积分模型：目标导向认知 = 投影哈密顿量下的虚时演化；双重括号流=GKSL耗散子(跳变算子=投影算子，实测验证恒等式 -[P,[P,ρ]]=2·L[P]ρ)；Wick旋转把非幺正下降映射为幺正演化+精确离散路径积分（oracle=势能、扩散投影=动能）；意识连续统=系统-探针耦合强度，弱耦合Markovian极限恢复Asano的GKSL模型、强耦合给投射性可报告态固定 (arXiv: 2607.24807)
  - 实测发现（test_pathintegral_skill.py）：投影算子下的双重括号流是纯dephasing流——保持布居、杀死相干、对与P对易的态（如最大混合态）不动；目标导向的concentration需要归一化ITE项 dρ/dτ=-(Hρ+ρH)/2+⟨H⟩ρ（H=I-P_target），验证support→1.0
  - 模式提炼：Pattern A 投影哈密顿目标编码（目标概念→子空间正交投影→交换子流优化）；Pattern B 交换子即梯度（谱约束流形上无需推导梯度）；Pattern C Wick旋转对偶（优化↔采样互转）；Pattern D 耦合强度连续统作现象学轴（离散范畴→连续参数的可测试模型）
  - **Activation**: 认知路径积分, 投影哈密顿量, double-bracket flow, 虚时演化, GKSL, 量子认知, 意识建模, Wick rotation, Hilbert-Schmidt cost, spectrahedron optimization, path integral cognition, projector Hamiltonian

### How many labels can a biological oscillator carry? A quality-factor screen for proposed information carriers
- [[oscillator-q-factor-label-capacity-screen]] - 基质无关的Q因子筛查：谱可分辨性单独特地约束标签容量 M ≤ Q = 2πντ（线宽-相干时间关系），任何被提议的生物振荡子信息载体只需两个已发表数字即可评估——皮层30GHz微波场提案 Q=0.19（线宽超载波5倍，连1个标签都装不下），补救方案（驱动发射体需共振腔）被提案自身几何禁止，代谢功率超预算5-9个数量级 (arXiv: 2608.10560)
  - 六项次级判据：双侧持续窗口（标签必须同时可读出AND可重写）、代谢预算、读出耦合、噪声底vs标签间隔、标签间串扰；决策规则：Q<2直接光谱层面否决（二进制需要2个标签），无需进入机制辩论
  - 代码已实测（test_qfactor_skill.py）：30GHz案例复现Q=0.1998与论文一致；40Hz gamma振荡子(τ=100ms) Q≈25.1→25个标签可分辨
  - 模式提炼：两数字杀伤测试（机制争议前先跑不等式界）、几何自否证检查（提案自身的几何禁止其补救机制）、双侧持续窗口（可读+可重写双约束适用于任何静默记忆/突触权重/蛋白质态载体）
  - **Activation**: Q因子, 生物振荡子, 信息载体容量, 线宽, 相干时间, 微管, 内源性电磁场, 量子生物学, 神经信息载体, oscillator Q factor, label capacity, linewidth coherence, EM field brain theories, two-number kill test

### Learning While Inferring: Local and Parallel Learning for Edge SNNs across Sensing Modalities
- [[bsd-bidirectional-spike-distillation]] - 边缘SNN边推理边学习：BSD用互不相交的前向（刺激驱动）+反向（目标驱动）双网络，仅在中间表征处做局部对齐损失，前向推理/反向推理/分阶段更新三者并行，部署时只留前向分支 (arXiv: 2610.03149)
  - 25个SOUL基准（5种感知模态）平均精度只落后匹配BP基线3.8pp；训练延迟0.72×、训练能耗0.36×；学到表征可免replay直接少样本类增量学习
  - 设计规则：对齐点之前的图不相交是核心（任何跨阶段反向边都会重新引入串行化瓶颈）；反向分支可用特权输入教师；局部损失需对称避免向目标分支坍缩
  - **Activation**: on-device learning, spiking neural network, local learning, bidirectional distillation, edge intelligence, learning while inferring, few-shot incremental, SNN边缘部署

### Gaussian Fisher Information Is Superadditive
- [[gaussian-fisher-superadditivity]] - 高斯测量的量子Fisher信息超可加：独立模式的联合读出优于分开测量——线性探测器只见半个相空间，两模式的"选哪一半"成为资源；Bell homodyne（50:50分束器+双homodyne）把heterodyne空端口的真空噪声换成第二个模式的信号 (arXiv: 2610.02625)
  - 严格上界 (√2−1)²=17.157%；热模式同温增益"不可能"猜想被推翻：任意频率差打开温度窗口，频率比3.318处增益峰值12.699%（此时Bell homodyne为最优高斯测量）
  - 硬件零门槛：两个耦合谐振器+双homodyne，或相位保持放大器的idler频带直接喂同一热源；适用微波测温/轴子搜寻等精度受限场景
  - **Activation**: quantum Fisher information, Gaussian measurement, Bell homodyne, heterodyne, superadditivity, quantum metrology, thermal sensing, collective readout, idler port

## 2026-10-05 - Neuroscience Research (Cron Job)

### Neural Data Needs Semantic Tokenization: Behavioral Events as Boundaries of Session-Transferable Tokens
- [[tws-state-tokenization-neural-data]] - 神经数据需要语义token化：以行为事件间population流形状态为token单元（无neuron/session embedding），跨session零适配解码，冻结后跨物种迁移 (arXiv: 2610.03001)
  - per-neuron token = 闭词汇表（跨session neuron overlap≈0 → POYO/CEBRA/NEDS在held-out session全部坍塌到chance）；TWS在53个IBL held-out session上movement MCC 0.565、RT R² 0.402，POYO预训练含这些session仍为0.000
  - Algorithm 1: event-time soft sigmoid gates（2个全session共享可训练offset Δ）→ state加权population平均 → 共享标量编码器 + 无位置编码cross-attention（置换不变）→ Gram-Schmidt得Grassmannian Gr(2,256) token → 6 tokens小CNN混token；几何不关键（跳过GS差异<0.01），不变量才关键
  - 冻结mice训练→macaque Utah array仅linear probe: reach direction MCC 0.232（event time本身仅0.011）；5个带标签session的probe超过全session训练的baseline 5×；1/4 units仍保留83%解码
  - 边界消融：jitter σ=5bins→−7%，fixed/random边界→−62~70%，错误边界+40 epochs训练无法修复（<正确边界random init）；Type A（共享子空间）变量保留、Type B（per-session解码方向）变量不保证——设计代价
  - **Activation**: 神经数据token化, 跨session解码, population manifold token, Grassmannian token, neuron-free tokenizer, cross-session generalization, neural foundation model, IBL, Utah array transfer, permutation invariance

### Chaotic Griffiths phase in neuron map networks
- [[chaotic-griffiths-phase-neuron-map-networks]] - 混沌Griffith斯相新机制：拓扑无序非必要，仅局部神经元参数淬火无序（Chialvo map的k∈[0.026,0.03]）即可在全局耦合网络产生扩展临界区间，与small-world叠加时相干态被完全抑制 (arXiv: 2610.03344)
  - 三相判据管线（可复用）：排序+single-linkage识别瞬时cluster（阈值δ_N用D/S轨迹双条件标定，D轨迹p_t<0.10且S轨迹p_t>0.90达95%时间）→ p_t涨落σ(p)>0.12判混沌GP → cluster尺寸幂律P(s)~s^−α（α随ε单调）+ 正Lyapunov指数数N₊~N^β反常标度（β≈0，规则CML为线性）
  - 同质极限A=0无混沌GP；A→1时ε区间单调加宽——内在动力学异质性是独立于结构连接的扩展临界性机制，与拓扑无序协同（small-world下GP延至ε∈[0.4,1.0]，S相完全消失）
  - 生物学意义：真实神经元兴奋性/阈值本质多样 → "大脑无需fine-tuning到临界点"的第二解释路径（结构异质性与动力学异质性互补维持扩展临界区间）
  - **Activation**: 混沌Griffiths相, 淬火无序, 参数异质性, 扩展临界性, Chialvo map, cluster size power law, Lyapunov subextensive scaling, chaotic Griffiths phase, quenched disorder, extended criticality

### Clustering without clusters: the meta-criterion and centroid reliability mistake continuous dynamics for discrete states
- [[eeg-microstate-cluster-illusion]] - EEG微状态"离散态"证据的证伪：meta-criterion在四个已知无簇的混沌吸引子(Lorenz/Rössler/Hindmarsh-Rose/Wilson-Cowan)上照样给出K*=4-8的伪最优簇数，LEMON静息态EEG的GFP峰经HDBSCAN+持久同调证实是单一连通结构而非簇 (arXiv: 2610.02220)
  - 两大论证同时被证伪：K-means质心在连通吸引子上同样落入高度可复现区域（跨run最近邻z-score检验）；Cartool七判据meta-criterion（DB/DB导数/修改KL/Point-Biserial/PB导数/Silhouette/Silhouette导数，rank变换后取七峰中位数）对任何连续吸引子都报告4-8
  - 决定性TDA管线（可复用）：HDBSCAN min-cluster-size扫描(0.25-12%n)+ε=0.35×中位距离；ripser Vietoris-Rips H0持久同调——真簇表现为β0平台、连续体为单调平滑衰减；61维合成高斯blob对照正确恢复K，LEMON 203被试EEG(2-20Hz, 61通道, 8.4k-13.7k GFP峰/被试)呈单簇0%噪声+平滑衰减
  - 单一HDBSCAN簇质心反投影=微状态C/alpha拓扑（神经生理学有效，非伪影）；结论：微状态分析应重新定位为symbolic dynamics（对连续流的划分选择），"最优簇数"可能是ill-posed问题——任何新簇数判据都应先跑Lorenz/Rössler负对照证伪测试
  - **Activation**: EEG微状态, 微状态聚类, meta-criterion, GFP峰, HDBSCAN, 持久同调, 拓扑数据分析, symbolic dynamics, 簇数选择, 负对照验证, LEMON dataset, centroid reproducibility, 混沌吸引子, Betti数

### Structural-Functional Brain Connectivity Generation via Multimodal Hypergraph-based Flow Matching
- [[hypergraph-flow-matching-connectome-generation]] - MHG-FM：首个超图+流匹配的SC-FC联合连接组生成/双向翻译框架——固定群体超边incidence矩阵做HGNN消息传递先验、Dual Cross-Attention双向SC↔FC融合、VAE潜空间条件流匹配替代扩散链，采样比匹配扩散骨干快8倍(32 vs 250 NFE, 106ms/样本) (arXiv: 2610.02722)
  - 超图构建（确定性、训练中固定）：SC超边=群体均值>0.01的解剖连接；FC超边=4 motif组(triangle clique |r|>0.7、hub-spoke top80%度连k*=8最强相关、kNN k=5/10)+跨被试30%多数投票；生成目标始终是N×N邻接矩阵而非超图本身
  - 模态dropout p=0.25使零填充输入成为in-distribution→推理时FC→SC/SC→FC翻译只需单次确定性前向（无需ODE重采样、无需重训练）；FC→SC r=0.941全指标最优，SC→FC r=0.573（结构约束但不唯一决定功能，不对称难度符合预期）
  - 关键教训：扩散骨干MHG-DiT矩阵级SC指标更高但度/社区结构坍塌(Deg-W1 10.05 vs FM 0.498)——Pearson r单独评估生成连接组具有误导性，必须配Deg-W1/NMI/ARI(置换平均)/|ΔMI|耦合间隙等拓扑指标；消融证实HGNN>成对GNN(全指标)、DCA交叉注意力→更小耦合间隙、AdaLN>加性时间条件
  - **Activation**: 连接组生成, SC-FC耦合, 超图神经网络, 流匹配, 跨模态翻译, 生成模型, HCP-YA, DTI tractography, rs-fMRI, Dual Cross-Attention, 变分自编码器, modality dropout, 拓扑保真度评估, connectome generation, hypergraph flow matching

## 2026-10-05 - Neuroscience + Quantum Research (Cron Job)

### Learning SYK Hamiltonians
- [[syk-hamiltonian-learning-mean-field]] - 首个稠密随机平均场哈密顿量学习的常数温度保证：SYK每个四次相互作用重叠Θ(n³)个其他项、局域性工具全部失效，用平均场无序性替代局域性 (arXiv: 2610.02178)
  - 样本高效算法（任意固定β>0，N=n^{O(1+β)}ε⁻²log(n/ζ)）: 最大熵约化→log配分函数在真实耦合处的强凸性（Hessian Lipschitz+边界论证，凸性只需在随机目标点成立）；BKM协方差恒等式替代准局域算子+局部旋转机制，局部淬火Petz Rényi比值Z_A/Z替代能量泄漏界
  - 拟多项式时间算法（小常数β）: 一阶求逆——重标后期望映射线性阶为恒等，需消除Θ(n^{-1/2})二次偏差；低阶多项式代理（Taylor展开分母(1+Δ)⁻¹≈1−Δ，β展开截断度O(log n)）+加权矩估计‖Δ‖_{2,s}≤C_s n⁻¹（s=15→超收缩控制L¹⁶）+低度校准
  - Wick展开+Kotecký–Preiss聚合物展开控制配分函数矩；退火→淬火通过交换指标+高斯集中论证；SYK被猜想无复本对称破缺相变（对比SK模型β=1相变），可学习性揭示了混沌模型的结构
  - **Activation**: SYK, Hamiltonian learning, Gibbs state, mean-field, all-to-all interactions, strong convexity, log-partition function, Bogoliubov-Kubo-Mori, Kotecky-Preiss, Wick expansion, Petz Renyi power, quantum simulator calibration

### Large-scale factor analysis shows machine intelligence is only partially interpretable
- [[llm-benchmark-factor-analysis]] - 迄今最宽LLM智能心理测量学分析（13,251分数×1,618模型×456基准）：g因子最多解释70.8%方差（最佳插补器仅25.7%），内容相似基准不聚类，g与标准"推理"基准不同——机器智能仅部分可解释 (arXiv: 2609.36515)
  - 超稀疏MNAR矩阵管道: 三种稠密化策略（C列优先保知名基准/R行优先保重测模型/S对称）+6种插补器（SoftImpute/kNN/missForest/单侧矩阵补全/USVT/相关矩阵恢复），R²≥0.2门控（列分层20%掩码）
  - 分层因子分析: EFA(minres)+promax斜交旋转+Schmid-Leiman双因子变换→ω_h量化g方差占比；并行分析选因子数；标签凝聚分析用覆盖四分位分层零模型（2000次置换）+BH FDR检验"能力"标签是否真实聚类
  - 反射模型（潜在g因果）不可支持；互惠主义（mutualist，能力互相因果的网络，无公共原因）是更好模型——若成立，"训练中瞄准g"不可行，泛化只能靠暴力覆盖任务空间
  - **Activation**: LLM benchmark, factor analysis, g factor, omega hierarchical, Schmid-Leiman bifactor, MNAR imputation, label cohesion, mutualism, psychometrics, benchmark design, evaluation validity

### Floquet-Universal Hamiltonian Simulation
- [[floquet-universal-hamiltonian-simulation]] - Floquet模拟完整构造理论：周期驱动哈密顿量（有限Fourier级数、幅值比∈[1,2]）可合成Lie(S)中任意哈密顿量；S Floquet-通用⟺S生成完全李代数——与通用门集分类一致，受限带宽光滑驱动不损失计算能力 (arXiv: 2610.01878)
  - 实用优势: 时不变合成的相互作用强度比多项式缩放且有no-go定理[CMP18]，Floquet只需频率缩放、强度全O(1)——周期驱动已被实验实现[Jot+14;Cho+20;Koy+25]
  - 效率定理: k-局域格点哈密顿量（非对易图常数色数）以全幅值O(1)+全频率poly(n)模拟；机制=交换族内频率系数复用+常数相移（Lemma 55）
  - 证明机器: 设计驱动使Magnus展开低阶项消失+最新尾部界[ACO25]+留数/代数几何归约到自由结合代数→李代数的规范投影；给定目标哈密顿量，驱动参数由线性代数计算导出；直接导出Floquet物理量的BQP完全性与QMA硬度
  - **Activation**: Floquet, periodic driving, Hamiltonian simulation, Lie closure, Magnus expansion, quasienergy, lattice Hamiltonian, chromatic number, BQP-complete, QMA-hard, quantum simulator design

## 2026-10-05 - Neuroscience Research (Cron Job)

### NeuroLens: Learning Latent Embeddings of Neural Semantics from Chronic Recordings
- [[neurolens-jepa-chronic-recordings]] - JEPA自监督框架从慢性神经记录学习去噪表征：潜空间预测分离表征可塑性与电极漂移，校准签名神经元身份支持零梯度跨session适配 (arXiv: 2610.02864)
  - Day-adaptive cross-attention encoder：41维生理签名（FR stats+ACG+population coupling）经MLP生成neuron embedding注入token，替代固定ID实现未见神经元迁移；Utah array通道改用hypernetwork FiLM按天条件化
  - SIGReg特征函数正则（匹配各向同性高斯）防坍缩，替代启发式stop-gradient；因果transformer AR predictor跨天共享参数强制稳定预测结构
  - 实证：IBL 53天Neuropixels choice解码+6% vs causal NDT，latent effective rank跨天稳定（NDT随神经元丢失下降）；人类ALS语音sentence-embedding解码+38%，GF模式（64 calibration trials零梯度）仍超SPINT/POSSM
  - **Activation**: JEPA, chronic recordings, representation drift, neural population nonstationarity, few-shot BCI, cross-attention encoder, effective rank, self-supervised neural decoding, calibration-based neuron identity

### Parallel Time-Aligned Spiking Self-Attention for Consistent Integer-Valued Training and Spike-Driven Inference
- [[pt-ssa-temporal-interaction-mismatch]] - SFA/I-LIF压缩训练与脉冲推理的算子级失配TIM：O_train含全部跨时间三元组Q_iK_j^TV_k而O_inference只保留对角项，SDT-V3在ImageNet掉27.78pp；PT-SSA重建D个虚拟脉冲切片按时间对齐并行计算注意力再求和，gap降至0.06pp (arXiv: 2610.03291)
  - 脉冲重建X_d=1[C_X>d]全并行+单位STE梯度路由（D虚拟步梯度求和聚合到压缩激活）；Adaptive PT-SSA每块学一个标量θ_l=exp(clip(a,-8,8))等价调节SFA有效阈值，LSQ式1/√(MD)梯度缩放
  - 算子级验证：D=4相对L2误差7.41→1.6e-4（SFA）；SSA gap随D恶化（D=8时26.99→15+pp）而PT-SSA全D稳定<0.3pp——发放计数守恒≠算子等价
  - Triton-fused内核逐tile重建-计算-累加避免物化重建张量，吞吐仅比I-LIF SSA低5.4%（5797 sample/s），比recurrent LIF SSA快2.91×；ImageNet-1K 74.53% spike-driven Top-1
  - **Activation**: spiking transformer, temporal interaction mismatch, train-inference consistency, SFA, I-LIF, spike-driven attention, virtual time step expansion, adaptive firing threshold, Triton kernel

## 2026-10-05 - Neuroscience Research (Cron Job)

### Continual Reinforcement Learning with Neuroevolution
- [[neuroevolution-continual-rl-stability-plasticity]] - 神经进化在持续RL中最优：ES最一致实现稳定-可塑性权衡，机制是参数空间探索偏向宽返回景观邻域，跨任务邻域重叠率预测LA−F权衡 (arXiv: 2610.01583)
  - ES在8/18设置中LA−F最佳，GA在10/18设置学习准确率最高；PPO及ReDo/TRAC/C-CHAIN变体要么失去可塑性要么以稳定性换可塑性
  - 共享邻域（ϵ=0.1扰动下同时解决两任务的分数）与LA−F的Spearman相关ρ=0.77（NE 0.90, RL 0.70）；ES邻域比PPO宽2.3-3.9倍
  - RL可塑性损失症状（休眠神经元累积、权重漂移）在NE中不出现——源于梯度优化而非非平稳性；novelty search使DeepSea动作图重获率11%→57%（收益在elite不在centroid）
  - **Activation**: continual RL, neuroevolution, evolution strategies, stability-plasticity tradeoff, plasticity loss, return landscape neighborhood, population-based training, forgetting

### MorphAtt: A Neuromorphic Accelerator for Efficient Multi-Head Attention Processing in Spiking Vision Transformers
- [[morphatt-spiking-vision-transformer-accelerator]] - SViT注意力ASIC：Q(KᵀV)重排将复杂度O(N²D)→O(ND²)，二值脉冲AND+popcount免乘法器，32nm下20.3-29.1 TOPS/W@39-55mW (arXiv: 2609.33207)
  - SpikeQKV→SpikeAtten→RepConv级联架构+模块间缓冲消除片外访存；LIF取τ=2用右移代替除法；注意力引擎仅209µW（比乘法器注意力省96%，单操作12fJ vs 500fJ）
  - 门控累加+sleep模式：Query MSB=0或KᵀV行全零时旁路切换功耗；支持SDTv2重参数化卷积仅增3.3%功耗
  - 功耗分布：SpikeQKV 51.6% > 片上存储44.6% > RepConv 3.2% > SpikeAtten 0.6%——免乘法后注意力近免费，LIF生成与存储才是优化重点
  - **Activation**: spiking vision transformer, neuromorphic ASIC, multiplier-free attention, AND-popcount, edge AI, SDTv2, reparameterization convolution, SViT accelerator

## 2026-10-05 - Neuroscience Research (Cron Job)

### Walshness: an intrinsic neural-network representability metric for quantum states
- [[walshness-nqs-representability]] - 量子态NQS可表示性的内在度量：Walshness低⟺紧凑神经网络表示，最优基选择=经典自旋模型能量最小化，恢复并推广Marshall符号规则 (arXiv: 2610.00505)
  - Wᶻ_α[ψ]=(1/α)log E_{r∼p_ψ}[e^{α|r|₁}]——Walsh谱质量集中在低阶模式⟺少体结构；内在W_α对所有局域SU(2)基取最小
  - Proposition 1: 基优化映射为经典自旋哈密顿量能量最小化（每site一个n̂ⱼ向量，耦合=多体关联⟨σⱼ₁···σⱼₖ⟩），TFIM最优基自发破缺平移对称（周期2交错）
  - Theorem 1/2 (双边): MLP宽度n^O(ω)深度O(logω)可表示低Walshness态；近最大Walshness⟹深度Ω(log n)不可避免；RBM用乘法Walshness（log ψ的）
  - 实证: TFIM g=0.2用Walshness最小基训练MLP-NQS，infidelity降低数个数量级；混合场toric code同样大幅改善
  - **Activation**: neural quantum states, NQS representability, Walshness, optimal basis, Marshall sign rule, sign structure, quantum state complexity

### Brain-SAD: A Brain-Inspired Safe Autonomous Driving Control Framework with Dynamic Fear-Oriented Constraint on Dual-Policy
- [[brain-sad-fear-oriented-dual-policy]] - 恐惧信号驱动的动态约束+双策略仲裁安全驾驶框架：在线恐惧信号解除约束与离线训练分布的耦合，替代静态Lagrangian/固定投影边界 (arXiv: 2609.38016)
  - 现有Constrained RL缺陷：soft方法的动作代价是静态state→cost映射，hard方法的可行域边界来自离线演示——约束↔训练场景强耦合
  - 杏仁核恐惧反应机制：场景感知→动态恐惧信号f(scene)→在线仲裁长期策略（常规交互）vs短期策略（紧急防撞），同时作为长期策略的动态约束
  - 可复用模式：学习型风险头调制拉格朗日乘子/投影边界（替代固定值）；带迟滞的双阈值门控防策略振荡；防御策略需过采样near-miss数据
  - **Activation**: safe reinforcement learning, fear-oriented constraint, dual policy, safe autonomous driving, dynamic action cost, amygdala, constrained RL distribution shift

### Sequential Capacity of Quantum Processes with Finite Memory
- [[sequential-capacity-quantum-processes]] - 固定内存量子过程的自适应可测试容量定律 C_γ(K)=Θ(K log₂((K+1)/γ))，量子相干干预比经典固定基测量多出对数级容量 (arXiv: 2610.02068)
  - 相位树构造：单控制量子比特 + Möbius/Boolean 反演签名查询 (s∈{−1,0,1}^K) 隔离子集和的逐位二进制，精确 0/1 响应
  - 噪声定律：残差相位翻转概率 e(q)=min(qI,qZ)+min(qX,qY) 决定容量 Θ(RT·log₂[1+min(T,1/e)])——纯横向翻转 e=0 不损失增强
  - 经典程序下界 Θ(T log T) vs 量子程序 O(T) qubits：容量与模拟程序大小是独立资源
  - **Activation**: sequential capacity, fat-shattering dimension, quantum process testing, finite memory, adaptive tester, residual phase-flip

### Null-model treatment of the sensory-motor boundary changes an evolutionary connectome comparison
- [[boundary-preserving-null-connectome]] - 果蝇连接组进化实验中标准随机化null在感觉-运动边界注入1000×直连捷径，翻转比较结论；边界保持null将差异收缩到±0.10等价界内 (arXiv: 2609.39248)
  - 标准null(列shuffle/保度swap)使嗅觉→运动直连输出 0.012%→10.6%，中位路径 3突触→1突触——null"保度"却改变了功能决定性的宏观性质
  - 因果移植闭环：捷径移植+0.44适应度(10/10种子)、剂量响应、内部-only sham与边界sham双双无效应——效应就是捷径本身
  - **Activation**: connectome null model, boundary-preserving null, degree-preserving swap, sensory-motor boundary, transplant experiment, equivalence bound

### Future Video Generation Better Aligns with the Human Visual Cortex than Observed Video
- [[future-video-generation-visual-cortex-alignment]] - AR视频扩散模型的"未来生成"表征比观测视频本身更对齐人类视觉皮层，预测编码的脑-AI对齐直接证据 (arXiv: 2609.38819)
  - 未来token表征在全部5个视觉分区unique contribution超过观测视频(p=0.002)，优势沿视觉层级增长(MT+ 0.436 vs 0.363)
  - 未来生成在**最噪声步**(s=0)对齐最佳——未承诺的多可能未来态与贝叶斯神经编码一致；重建在中段步峰值(细节精修)
  - STG层放大实验：人类偏好与层对齐度相关r=0.75 (p=0.029)，神经对齐→行为验证闭环
  - **Activation**: brain alignment, video diffusion, predictive coding, fMRI encoding, autoregressive, variance partitioning

### Field closure, ice neurons, and when a dendrite is a motif
- [[field-closure-ice-neurons-dendritic-motifs]] - 场闭合(γ)将冰神经元(Mullins-Sekerka生长极限)变成真正的动力学motif——ephaptic反馈是有生物神经元与冰的分界线 (arXiv: 2610.00184)
  - FHN界面态经γψ源项写回外场，γ=0谱分解为独立的MS生长支+FHN支；有限γ使长波侧重塑、开启孤立阈值以下的γ驱动Hopf区
  - 冻结树motif检测：一阶超额核Q₁=z_out^T(βG_eph)z_in，40个最大ephaptic对承载99.9%贡献——直接场捷径而非轮廓
  - 80种子系综：Q₁>0在所有树上成立(中位1.1×10⁻³)；亚阈值下"闭合几乎就是传输"(4.7×)，spike幅值下只是修正
  - **Activation**: dendritic computation, ephaptic coupling, morphogenesis, motif detection, FitzHugh-Nagumo, cable theory

### Dense auto-hetero associative memories applied to noisy communication channels
- [[dense-auto-hetero-associative-disentanglement]] - 密集高阶Hebbian耦合让模块化Hopfield网络在K=Θ(N)线性负载下实现模式解缠：把"混合态"从检索错误变成计算原语 (arXiv: 2609.32605)
  - 核心设计律 2<P≤D：容量由最低耦合阶决定，P>2消除模式慢噪声、P≤D压制模块噪声，自洽方程只需Mattis磁化序参量（Guerra插值+RS），相图中解缠区边界与负载无关
  - 吸引子解码通信协议：token↔三元模式混合+PRNG掩码(XOR密钥流)，解码即解缠动力学；60%块擦除仍无误码、80%擦除仅百分之几错误——优雅降级优于常规信道编码的悬崖式失败
  - **Activation**: pattern disentanglement, dense Hopfield, high-order Hebbian, attractor decoding, mixture states, blind source separation, communication channel

### Where Does Randomness Matter in Neural Cellular Automata?
- [[nca-train-vs-execution-randomness]] - 受控分离NCA训练/执行随机性：异步更新是优化辅助而非运行必需——10/10异步训练模型可4096步全确定执行 (arXiv: 2609.36797)
  - 精确二阶矩准则：P_{t+1}(ω)=d_α(ω)P_t(ω)+[α(1−α)/N^d]Σ|â|²P_t——随机掩码阻尼均值模但注入方差，均值检验误判4/25个配置
  - 等质量对比：grow训练8/10长程脱靶，persist/regenerate全部保持；损伤恢复仅regenerate(+85%~99%)——重建损失、局部谱、微扰增长各只回答部分问题
  - **Activation**: neural cellular automata, asynchronous update, persist recipe, second-moment criterion, retention vs repair, update mask

## 2026-10-04 - Information Science + Quantum (Cron Job)

### Interpreting Reasoning of LLMs via Partial Information Decomposition (SLIDER)
- [[slider-pid-llm-reasoning]] - PID 分解推理步骤的 answer-相关信息为 unique/redundant/synergistic，Step-RRI = Red − η·max{Uni,Syn} 检测重复推理，Trajectory-RRI 引导 SFT 数据选择 (arXiv: 2610.00571)
  - PRMBench 冗余检测 +10 分超过 embedding-similarity/InfoGain 基线；Theorem 2: 重复步骤 Uni=Syn=0 故 RRI>0
  - 低 Trajectory-RRI 训练数据微调 Qwen2.5-7B：推理效率与平均 RRI 相关 ρ=−0.97，任务性能保持
  - **Activation**: partial information decomposition, PID, Step-RRI, Trajectory-RRI, repetitive reasoning, reasoning interpretability, fine-tuning data selection, PRMBench

### Quantum state preparation for weighted d-DNNF
- [[quantum-state-prep-ddnnf]] - 加权 d-DNNF 描述的量子态可线性时间编译为 O(|D|) 门电路：证书超对称逐层生长 + ancilla 反计算 (arXiv: 2610.02094)
  - 知识编译语言（determinism+decomposability）成为量子态加载前端：贝叶斯网络/概率数据库/加权模型计数均可 d-DNNF 编译
  - 比 weighted FBDD (Phe 2025) 指数级更 succinct；2-d-DNNF fan-out-2 归约只损失 log 因子
  - **Activation**: quantum state preparation, QSP, d-DNNF, knowledge compilation, model counting, certificate superposition, succinct representation, quantum data loading

### Submodularity of entropy under quantum convolution
- [[quantum-convolution-submodular-entropy]] - 量子卷积熵增益的多拟阵几何：亚模扩展到整个子集格，机械化导出卷积 SSA、量子 Ruzsa 三角不等式、Plünnecke–Ruzsa 不等式族 (arXiv: 2609.40211)
  - 量子倍增常数 δ_q[ρ] 控制所有 m-重卷积熵增长，指数 m−1 最优（计算基对角态已达到）
  - 证明模式：辅助态边际熵归约 —— 把多输入卷积熵编码为单一辅助态的边际熵，化为标准 SSA 应用
  - **Activation**: quantum convolution, von Neumann entropy, submodular, polymatroid, Ruzsa triangle inequality, Plünnecke-Ruzsa, doubling constant, additive combinatorics, entropy inequalities

## 2026-10-04 - Neuroscience Research (Cron Job)

### Attraction to hierarchical feature memory explains orientation bias
- [[hierarchical-feature-memory-orientation-bias]] - 均匀编码精度下层级复合特征记忆即可复现 anti-cardinal bias 与序列依赖，推翻效率编码标准解释 (arXiv: 2609.40204)
  - 反射吸引：incongruent 圆相关为负——序列吸引由前反应及其 cardinal 镜像反射的复合特征主导（复合记忆痕迹=层级再激活指纹）
  - 跨半视野测试分离低层（空间特异）与高层（空间抽象）影响；von Mises 混合模型零调参复现全部 anti-cardinal 偏差；EEG ERP 同时相似于反射朝向
  - **Activation**: serial dependence, orientation bias, anti-cardinal, compound feature memory, von Mises mixture, hemifield, efficient coding critique, hierarchical reactivation, circular correlation

### Belief-Based Maximum Occupancy Principle and Active Inference
- [[belief-mop-active-inference-bellman]] - MOP 扩展到 POMDP 信念空间 + EFE 的 Bellman 价值迭代重构：MOP 联合达成探索与生存，EFE 两者由精度 d 互斥交换 (arXiv: 2609.39342)
  - EFE 树搜索→带 γ 折扣的 Bellman 方程：信念离散化(∆=0.1)+线性插值，深度线性代价，时间平稳策略；信念传播与 VFE 最小化数学等价
  - MOP 策略熵随内部能量自适应分档(E>15 广探索/E≤15 直奔食物)且零超参；survival-occupancy 平面上 MOP 单点落在 EFE 的 d-权衡迹之外
  - 终止态路径熵塌缩隐式产生生存倾向——Kiefer 约束熵最大化统一视角：MOP 与 EFE 的差异仅在保命约束显式 vs 隐式
  - **Activation**: active inference, maximum occupancy principle, expected free energy, Bellman value iteration, POMDP belief state, intrinsic motivation, exploration-survival tradeoff, empowerment comparison, path entropy

## 2026-10-04 - Information Science / Quantum Security & Inference (Cron Job)

### Learnt Attacks on Quantum Key Distribution under Channel Noise and Device Drift
- [[learnt-attacks-qkd-channel-drift]] - 约束 MDP 攻击者量化设备漂移下 QKD 自适应窃听：RL 攻击 Holevo 0.348 vs 固定电路 0.135（零检测，98% DP 上界）(arXiv: 2610.01792)
  - OU 过程建模信道噪声漂移 + 每块 abort 预算约束 + 门结构/角度联合搜索 → 紧凑离散动作集，RL 良定义且可迁移无模板噪声（振幅阻尼）
  - 平稳噪声对照：基不对称增益变号 → 自适应本质是追踪漂移；反制方向为随漂移率自适应的时变检测阈值
  - **Activation**: QKD eavesdropping, channel noise drift, constrained MDP, RL attack circuits, Holevo information, device-independent E91, BB84, Ornstein-Uhlenbeck, security analysis, recalibration cadence

### QuanVI: Score-based Variational Inference via Quantum Maximally Mixed States
- [[quanvi-score-variational-inference]] - 简并低能子空间用最大化混合态替换本征向量 + MPO 压缩密度算符，解决 score-VI 参数爆炸与本征态非唯一性 (arXiv: 2609.39164)
  - Fisher 散度目标 → ρ 的线性迹泛函；子空间旋转不变性消除基依赖震荡；DMRG 风格 sweep 优化 O(n·χ²) 参数
  - 高维贝叶斯后验（非高斯）上验证：特征值 score-VI 震荡处 QuanVI 收敛；键维 χ 控制精度-成本前沿
  - **Activation**: score-based variational inference, Fisher divergence, maximally mixed state, degenerate subspace, MPO tensor network, DMRG sweep, Bayesian posterior approximation, non-Gaussian targets, density operator optimization

## 2026-10-04 - Information Science / Quantum Cryptography (Cron Job)

### Time-Space Lower Bounds for Breaking Quantum Cryptography
- [[quantum-timespace-trace-moment]] - 迹矩方法证明 QROM 预处理攻击时间-空间下界：S 比特建议+T 查询破二进制相位态概率 O((T²+√ST)/N)，量子密码安全空间 N² vs 经典 N (arXiv: 2610.02101)
  - 三步流水线：建议态成功概率 → PSD 矩阵 Y_R 的期望算子范数 → 迹矩 E Tr(Y_R^{2S}) → 压缩预言机纯化（度数=数据库增长，Ŷ^S 支撑 ≤2S 条目）
  - 小数据库界 ⟨φ|Ŷ|φ⟩ ≤ O((1+T²+√ℓ)/K)：重行 ℓ/(Kh) + 命中库 ℓ/(KN) + h+1 相干历史 Cauchy–Schwarz，h=√ℓ；1OWS 紧于 S=0（Grover）与 T=0（√S 副本+对称子空间测试）
  - 中心化矩阵技巧将 PRG 区分优势归入同一管线：ε ≤ O(T²/N+√(ST/N))，改进 Liu23 的 O(T/√N+(ST/N)^{1/3})；1PRS@T=0 紧界 O(√S/N)
  - 可复用：建议=算子范数、矩阶=寄存器大小、度数=数据库增长、重采样/交换混合（综合问题 O((T²+(T+1)log 2M)/K)）
  - **Activation**: time-space tradeoff, quantum random oracle model, compressed oracle, trace moment method, preprocessing attacks, one-way states, pseudorandom states, non-uniform security, operator norm random matrix

## 2026-10-04 - Information Science / Quantum Pseudorandomness (Cron Job)

### On the Pseudorandomness of Simple Quantum Processes
- [[design-pseudorandom-separation]] - 反驳量子 HMMR 猜想并首次分离多项式阶酉设计与伪随机酉：矩匹配≠伪随机性，最大扰乱≠Haar 行为 (arXiv: 2610.02100)
  - 掺杂 Clifford 局部行走：概率 1/m 非 Clifford Z 旋转，T=O_t(n²log²n) 步成自适应 t-design 误差 exp(−Ω(log²n))，但 O_t(log²n) 查询可区分——Clifford twirl 不动点空间维数与 n 无关 [GNW21]，常数维子空间用掺杂谱界
  - FB 系综分离任意多项式阶（1≤t≤2^{n/4-4}）：U=F·B，F 植入 2t-wise 独立相位态于不变子空间 span(|+⟩^⊗n)，B 在正交补 Haar——PFC 置换插入 + CSBH25 正算子分析得无平方根损失 design 误差
  - 区分器：重复查询产生同一相位态副本，ABDY23 导数测量每副本一条种子线性方程，Weil 特征和界 + 高斯消元 O(n^t) 查询定种子
  - 物理警示：t=Θ(n) 最大扰乱（min-entropy 距最大 8 比特）仍可 O(n²) 查询区分；新猜想 6.1：局部系综 t=Θ(n) design 或为 PRU 真阈值
  - **Activation**: unitary designs, pseudorandom unitaries, Gowers conjecture, quantum HMMR, doped Clifford circuits, phase state learning, derivative measurement, information scrambling, maximal scrambling, black hole physics
## 2026-10-04 - Neuroscience Research (Cron Job)

### NeuronDiscover: Agent-in-Twin for Mechanistic Discovery in Neuronal Microenvironments with World Action Models
- [[neurondiscover-agent-in-twin]] - Agent-in-Twin 机制发现：联合机制-差异信念对抗孪生混淆的自主实验设计 (arXiv: 2609.35338)
  - 孪生混淆：真实机制改变与数字孪生误差在稀疏观测中签名相同，预测精度无法裁决机制主张
  - 类型化+范围化 MIOY 图（机制-干预-观测-结果）：观测节点永不解释物理端点，假支持 13.5%→5.0%
  - 联合机制-差异 EIG > 插件 EIG（3.8 vs 2.9 关系/世界）；可辨识性地板 Λ(E)≻0 先于信息增益
  - **Activation**: twin confounding, agent-in-twin, mechanistic discovery, MIOY graph, world action model, bayesian experiment design

### FAST-Brain: A Flow-Aligned Spatio-Temporal Surrogate Brain Model
- [[fast-brain-flow-aligned-fmri-surrogate]] - 流对齐直接干净信号预测的 rs-fMRI 代理脑模型，逼近误差按内在维数 d 缩放 (arXiv: 2609.34354)
  - flow matching 直接预测干净 BOLD 而非噪声/速度场，速度解析恢复：V=(Ŷ−Z)/max(1−τ,τ0)
  - 定理：低维子空间下贝叶斯最优去噪器因子化 F*(Z)=A·f(A⊤Z)，误差 ~√(dP) 与环境维数 N 无关
  - 双解码器：RoPE Transformer（时间）+ 可学习多项式图滤波多图 GCN（SC/纤维长度/功能网络），零初始化课程
  - HCP: FC corr 0.726→0.938, MAE 0.199→0.073；EC AUROC 0.999
  - **Activation**: flow matching, fmri surrogate, BOLD generation, clean-signal prediction, digital twin brain, graph convolution

## 2026-10-04 - Information Science / Quantum Communication (Cron Job)

### An exponential separation between entanglement-assisted and unassisted one-way quantum communication
- [[entanglement-assisted-subgroup-membership]] - 纠缠辅助经典通信 vs 无辅助量子通信的首个总函数指数分离：O(log n) 经典比特+Θ(n) EPR 对 vs Θ(n^{1/3}) 量子比特 (arXiv: 2610.02099)
  - 上界：有界阶子群成员问题 Memb_{G,k} 的纠缠辅助协议——Alice 远程制备左陪集态均匀混合 ρ（rank-[G:H] 平坦态，RSP 代价 log|H| 比特），Bob 用右乘 U_g 做 Hadamard 测试，tr(ρU_g)∈{1,0} 判定 g∈H；通信 O(log k) 而非 O(log|G|)
  - 下界：ShiftEq 秩零问题（Hidden Matching 的群论推广）+ 矩方法——min-max/top-本征向量论证在 Bob POVM 无界维时失效，正是模型分离点；独立相位 ζ^{φ_s} 解耦后矩阵矩不等式 + Fourier 域谱间隙 ‖(I-P)K‖∞ = 1/D
  - 群实例：广义 Heisenberg 群 H_{2^r}(F_3)（中心 ζ 阶 3，Weyl 对易 X_uY_v=ω^{u·v}Y_vX_u 强制 D=3^{2^r}），得 Ω(2^r)=Ω(n^{1/3})；否定 Newman 定理的纠缠模拟，Shi–Zhu 2^{O(C)} 模拟渐近最优
  - **Activation**: entanglement-assisted communication, subgroup membership, remote state preparation, coset state Hadamard test, one-way communication complexity, moment method lower bound, Heisenberg group irrep, representation theory dimension, communication separation
## 2026-10-04 - Neuroscience Research (Cron Job)

### How much of fly walking is written in the wiring?
- [[fly-walking-wiring-specificity]] - 连接组接线特异性检验方法学：节奏是通用的，拮抗肌协调才是写入接线的；Sherrington 交互神经支配直接编码于果蝇腿运动连接组 (arXiv: 2609.38665)
  - 固定权重（符号化突触计数）率模型，MaleCNS+MANC 双独立连接组，132 设置网格扫描+冻结+60s 多窗口确认；六族嵌套重连零模型（密度→细胞角色→度→腿块→谱系块→腿×谱系）
  - 核心结果：9-14/30 重连网络节律性 ≥ 真实网络（最高 0.90 vs 0.32），但 0/30 达到真实拮抗协调（0.312 vs max 0.144）；交互神经支配指数 0.48/0.38 vs 全部重连网络为负
  - 因果检验：跨池重分配前运动输入（强度仅变 2-4%）即废除协调而保留节律——协调取决于前运动输入分配给哪个拮抗池，非输入强度；协调集中于胸-髋关节（0.71 vs 0.09）
  - 可复用清单：模式读出（相位关系）而非振荡读出、预注册声明级别、双连接组复制、结构签名验证、强度/剂量匹配因果扰动
  - **Activation**: connectome specificity, wiring specificity, null model connectome, antagonist coordination, reciprocal innervation, central pattern generator, fly walking, degree-preserving rewiring, Maslov-Sneppen

### Neuromorphic Pseudo-Random Number Generators with a Low Power Hardware Implementation
- [[neuromorphic-prng-balanced-chaotic-snn]] - 平衡混沌 SNN 作为低功耗伪随机数发生器：spike-chaos 区制 LIF 网络经动态查找表变换通过全部 NIST SP-800-22 测试，FPGA 实现 3-5 mW/120kbps (arXiv: 2610.00719)
  - 硬件友好修改：权重二值化 ±g/√N（每神经元恰 N/2 正负）、参数量化为 2^k 幂（全移位-加法、无乘法器）；ISI CV≈0.99 确认 Poisson 样放电、单脉冲删除/单权重翻转去相关轨迹
  - 区制选择：rate-chaos（耦合过大）因长时自相关产生劣质比特流，NIST 通过数与 CV 强负相关 (ρ=-0.8147)；须选低 CV Poisson 样 spike-chaos 区，N≥128
  - 比特提取：朴素脉冲索引编码因相对不应期失败；动态查找表 y_n=mod(y_{n−1}+s_n,N), b_n=L(y_n) 混合全网历史；Dieharder 短程相关用两遍 XOR 成对抽取白化消除
  - 性能：与 LCG/BBS/Mersenne Twister 可比（~50% 比特流全过 15 项 NIST）；O(2^N²) 唯一实例可经抑制性偏置禁用神经元重配置；同一硬件块兼作储备池计算加速器；诚实定位为统计 RNG 而非 CSPRNG
  - **Activation**: pseudo-random number generator, neuromorphic PRNG, balanced network chaos, spike chaos, rate chaos, NIST SP-800-22, entropy source hardware, FPGA SNN, stochastic computing, edge computing randomness

### Controllable Stochastic Quantization Encoding for Adversarially Robust Spiking Neural Networks
- [[sqe-stochastic-quantization-snn-robust]] - 随机量化编码 SQE：单一量化尺度 N 在 Poisson 编码 (N=1) 与直接编码 (N→∞) 之间连续插值，Var≤1/(4N²) 精确控制编码随机性，输入层对抗防御与训练层防御可叠加 (arXiv: 2610.01558)
  - 核心定理：无偏性 𝔼[s]=x、随机性上界 1/(4N²)、N=1 退化为 Poisson、N→∞ 退化为 direct——SQE 是统一两种标准编码的一般框架；STE 直通梯度训练
  - 实验：CIFAR-10 RAT 训练平均鲁棒精度 16.58%→30.51% (+17% on WRN-16)，APGD10 达 43.41%；黑盒鲁棒性≈Poisson (74.95% vs 76.15%) 但干净精度高 ~6%；与 AT/RAT/SR/TGO 全部可组合
  - **Activation**: stochastic quantization encoding, SNN adversarial robustness, Poisson encoding, direct encoding, input encoding defense, quantization scale, straight-through estimator, population coding

### Synaptic placement reflects shared input in Drosophila descending neurons
- [[dn-synaptic-placement-shared-input]] - 连接组拓扑↔亚细胞几何对应：果蝇下行神经元中，同时接触 partner DN 的源神经元输入比其他输入平均近 9.4μm (MaleCNS) / 8.0μm (FlyWire) 于 partner 输入位点 (arXiv: 2610.00690)
  - 方法学：三边前馈配置 (source→partner+receiver, partner→receiver) 映射到接收神经元树枝上的相对突触位置；双比较设计 (between-source n=13,318 / within-source n=922 receivers) + 三站点参考集标准化消除最近邻距离的样本量偏差；两独立连接组 (雄/雌) + C. elegans 跨物种复制
  - 次要发现：共享输入与空间重叠对 DN 互连提供互补预测信息 (held-out log loss 各降 3%/10%)；top-5 共享源贡献 ~90% cosine overlap；AN19B014 电路中源经独立突触前位点接触两 DN——排除了单 bouton 假象
  - **Activation**: synaptic placement, connectomics, Drosophila, descending neurons, shared input, feedforward motif, subcellular organization, physical network models, skeleton path distance

### Increasing Width Allows Greedy Layer-wise Training to Rival End-to-End Backpropagation in Self-Supervised Learning
- [[width-compensation-local-learning]] - 宽度补偿受限信用分配：32× 宽 Conv4 贪心逐层自监督训练反超端到端 backprop (arXiv: 2610.00753)
  - 核心发现：贪心逐层训练随宽度增益不成比例放大（Conv4 1×→32× 贪心 +14.76pts vs 端到端 +7.97pts；Conv8 1×→16× 是 +12.01 vs +0.07），宽浅架构下局部学习可媲美/超越全局误差传播——为大脑"浅而宽"架构提供功能性解释
  - 机制：Wakhloo 表征几何框架的 SSF/SNF 分解——端到端训练的 signal-signal factorization 在 epoch~160 达峰后持续退化（SSL 损失不显式保护类别结构），贪心训练的 SSF/SNF 随每层冻结单调上升并最终反超；Barlow Twins 损失在大宽度下与下游精度脱钩
  - **Activation**: greedy layer-wise training, local learning, credit assignment, network width, biologically plausible learning, Barlow Twins, representational geometry, SSF, SNF, shallow wide architecture

### Selection rules for the harmonic spectroscopy of animal decisions
- [[harmonic-spectroscopy-animal-decisions]] - 线索几何=测量仪器：决策景观按衍射振幅分解为动物内在谱×结构因子，对称性施加选择规则，跨物种验证 (arXiv: 2610.00990)
  - 核心公式：H(φ) = -Σ K_n Re[F_n e^{inφ}]，F_n = Σ w_j e^{-inΘ_j}；p 重对称线索阵列湮灭所有非 p 倍数谐波（三线索 120° 响应从 n=3 开始）；两线索间距扫描 Δ=180°/n 处切凹口；可检测性定律预测第三谐波需 13-652× 观测时间——解释文献一谐波"天花板"
  - 实验验证：果蝇二谐波在预测凹口 90° 处变号 (实测 91.1°)、三目标队列凹口移至 118.2°；果蝇罗盘 EPG 神经元上对称场景压制禁戒矩 (10/10)、破坏对称即恢复 (10/10)——选择规则同时读出于行为与神经表征；高斯 bump 胜过方 bump (15/15)；一谐波不可能产生妥协→选择分岔，高谐波经 n² 权重主导转变
  - **Activation**: harmonic spectroscopy, decision spectrum, cue geometry, selection rules, ring attractor, structure factor, angular landscape, collective behavior, occupancy estimator, fluctuation-dissipation

## 2026-10-04 - Information Science + Quantum (Cron Job)

### Quantum State Routing and Perfect State Transfer on Signed Graphs under Environmental Noise
- [[szegedy-signed-graph-quantum-routing]] - 符号图 Szegedy 量子游走实现免测量量子路由：边符号 π 相移精确消除背散射，哑铃图 D₂m,₀,₂n 单边换向即达 PST F=1.0 (arXiv: 2609.39890)
  - 零背散射引理 p(e⃗)=1/2 ⟺ (Uα)e⃗⁻¹,e⃗=0；桥边 σ=−1 时 τ=m+1+n 完美传态，σ=+1 变存储环——二进制拓扑规范符号取代连续参数调谐
  - 噪声视界（经典阈值 F=2/3）：幅阻 τmax≈0.4055/λ 跳（λ=0.02 时约20跳），相位阻尼 τmax≈1.0986/p 跳（约55跳，2倍距离，F 饱和于 1/2 底）
  - **Activation**: quantum routing, signed graph, Szegedy quantum walk, perfect state transfer, topological router, back-scattering, dumbbell graph, glued trees

### Adaptivity is all you need: Optimal stabilizer learning using just single-copy measurements
- [[adaptive-single-copy-stabilizer-learning]] - 自适应单拷贝 Clifford 测量以 Θ(n) 样本学任意 n 比特 stabilizer 态，纯经典反馈即追平双拷贝 Bell 采样 (arXiv: 2610.02031)
  - 核心循环：两次独立计算基测量差分采样 u=x+y，CNOT 层 F_u 将采样到的 X 型 stabilizer 压到单 pivot 比特且不破坏已对角化生成元，随机 H/H·S 猜测以 1/2 概率增 dim D；E[T]<2n+4
  - 扩展：k 比特量子内存下测试代价 Θ(n−k+1/ε)；stabilizer nullity ≤r（含 t 个 T 门掺杂电路）O(n·2^r) 单拷贝可学；非自适应单拷贝需 Ω(n²)——自适应是消除二次差距的关键
  - **Activation**: stabilizer learning, adaptive single-copy, Bell difference sampling, Clifford measurements, stabilizer nullity, T-doped states, sample complexity

## 2026-10-03 - Systems Engineering Research (Cron Job)

### Data-to-Certificates (D2C): Koopman Supereigenfunctions for Stability, Safety, and Control
- [[koopman-supereigenfunction-d2c]] - 绕过模型辨识，直接从轨迹数据学不等式型证书：超本征函数 K_f φ ≤ λφ 定义指数增长包络，统一稳定性/收缩/安全认证与QP控制综合 (arXiv: 2610.00178)
  - 核心松弛：Koopman本征函数的谱等式 K_f φ = λφ 单边化为 K_f φ ≤ λφ——表征从"精确演化"变为"包络上界"，与Lyapunov/势垒函数天然兼容；速率恢复Lyapunov指数（λ̂=2χ̂）
  - 三种数据驱动构造：①正预解式 φ_λ=∫₀^∞ e^{−λt} g(s_t(x))dt（探针g∈F₊直映证书，截断误差 Me^{−(λ−ω)T}‖g‖）②Gramian切丛证书 M_λ=∫e^{−2λt}YᵀQY dt（λ>χ_max，收缩度量是特例）③MET/QR本征方向 φ_i=(q_iᵀv)²（Benettin迭代）
  - 安全风险探针：状态约束→非负风险r(x)=Σρ(g_i)，证书=折扣未来风险；零安全探针下 φ_{λ,T}=0⟺[0,T]全程安全；探针谱系（指示/铰链/softplus/指数）权衡连续性与边界裕度
  - 控制综合：点态凸QP argmin ½uᵀRu s.t. (K_G Ψ)u ⪯ −(Λ−B)Ψ——结构同CLF/CBF-QP但约束由算子理论导出、可从数据计算；在线仅需短rollout的局部值+梯度，随状态维度可扩展
  - **Activation**: Koopman operator, supereigenfunction, data-driven certificates, stability certification, safety certificate, contraction metric, resolvent, D2C, uncertainty propagation envelope

### The Geometry of Time: Horizon-Independent Feasibility and Repair for STL
- [[stl-geometric-feasibility-repair]] - STL可行性检查完全解耦时间视界：Bhat-Bernstein定常积分的解析逆把时间窗映射为t=0空间水平集，可行性=单次多面体包含评估，不可行时Farkas对偶证书+闭式时间修复 (arXiv: 2610.00199)
  - 时间↔空间双射：μ̇=−c·sgn(μ)|μ|^β（非Lipschitz有限时间收敛）⟹ τ_s=μ₀^{1−β}/(c(1−β))，逆映射把[a,b]窗口解析为空间边界 μ₀=(μ^{1−β}+c(1−β)T)^{1/(1−β)}；常速极限 β→0⁺ 得线性预算 I_F=v_max·T_F
  - 几何指称语义：STL→可微水平集场 ⟦ψ⟧（LSE软min/max组合），F/G算子=空间捕获盆地S_{b−a}与安全缓冲B_{b−a}的向后前像 Pre_a；多面体编译定理：仿射谓词+线性动力学下 Ax(0)≤b_eff ⟺ ⟦ψ⟧(x(0))≥0（流传播 a_iᵀ=g_iᵀe^{Fa} 保持仿射几何，LSE梯度=softmax→对偶向量y）
  - 诊断与修复：不可行时Farkas引理产出对偶y≥0隔离最小冲突谓词+空间缺口r（无需组合slack优化），闭式修复 ΔT*=r^{1−β}/(c(1−β))（4.17m→1.83s使UAV任务可实现）
  - 保证与性能：健全性（10⁴次蒙特卡洛0%假阳性）、完备性间隙 δ=ln k/η 可调、视界无关复杂度（N=10,000仍<0.25ms，嵌套深度p=32不变；MILP在N≥1000达120s超时）、570×快于Gurobi；限制：仿射谓词+线性动力学（非线性需局部线性化）、c=‖u‖∞最坏情形漂移界保守
  - **Activation**: signal temporal logic, STL feasibility, temporal repair, horizon-independent, Bhat-Bernstein settling time, Farkas certificate, polyhedral compilation, backward reachable set, MILP alternative

## 2026-10-03 - Neuroscience Research (Cron Job, Round 2)

### Removing Timing Shortcuts Improves Non-Invasive Brain-to-Text
- [[simpleb2t-timing-shortcut-brain-to-text]] - 词对齐B2T联合解码的时间捷径：重叠窗口泄露词时长，合成信号（零脑信息）复现d'Ascoli全部增益（22.0% vs 22.3%），独立解码+观测聚合+LLM重打分使WER降至36.6% (arXiv: 2609.40359)
  - 捷径机制：3秒固定窗口从连续MEG按词onset提取，相邻窗口共享90.6%样本，相对位移d=argmin SSD可平凡恢复词间interval（与词时长r=0.90），联合编码=免费获得每个词的时长先验；99.9996%相邻对重叠
  - 五条件证据链：Joint(MEG) 22.3% ≈ Joint(合成) 22.0% > Timing-only 22.9%对照 > Isolated(MEG) 9.5% > Isolated(合成) 5.8%——增益几乎全来自时间非脑信号；d'Ascoli 9数据集中仅有的2个逐词等时阅读协议恰好是联合解码无增益的仅有的2个（跨论文一致性验证）
  - SimpleB2T配方：20M参数CNN+MLP逐窗口独立编码（砍掉200M transformer）→ softmax温度化 p_brain → k观测一致性加权聚合 A_i(w)=(1+αr_i)u_i^T e_w/T（α=2）→ beam search 200 + Qwen3-8B base重打分 λ=0.5；k=5时WER 36.6%（侵入式里程碑25.6%），SMR 26%；oracle beam内选择可达16.4%（瓶颈在排序非生成）
  - 关键洞见：捷径移除后聚合与LLM先验才有效（联合模型下聚合只是更好地估计时长、LLM重打分接近LM-only）；脑证据补动词、LLM补功能词（74.3%+73.8%→36.6%互补）；任务导向prompt 36.6% vs 通用prompt 55.2%
  - **Activation**: brain-to-text decoding, word-aligned B2T, timing shortcut, shortcut learning BCI, MEG speech decoding, overlapping window leakage, LLM rescoring, synthetic control, LibriBrain

### Not all solutions are created equal: functional vs representational similarity dissociation
- [[functional-representational-dissociation-linear-networks]] - 两层线性网络解流形完整解析：GLS/LSS（task-agnostic表征，几乎任意）vs MRNS/MWNS（task-specific，唯一RSM），功能与表征完全可解离，且只有参数噪声鲁棒性（非输入噪声/泛化误差）迫使task-specific表征 (arXiv: 2609.38998)
  - 解流形参数化（Thm 3.1）：Ω1=√QSV^T+Γ1Pi+Γ2Pu、Ω2=√USQ⁺+Ψ+Γ3(I−HH⁺)——核心映射+无关/零空间投影+干涉修正项Ψ/Φ，输入空间三分（relevant P_r / irrelevant P_i / unobserved P_u）；嵌套 MWNS⊂MRNS⊂LSS⊂GLS 逐级削减自由度
  - 表征分类学：GLS/LSS 的 RSM 依赖任意 Q/Γ1（可在保持函数下摆出"大象"形表征）；MRNS RSM=ONO^TN、MWNS RSM=X^TV√SV^TX 由训练数据唯一决定——task-specific 但两者不同（跨类型同函数RSA不完美）
  - 三大分析结论：①线性可预测性由solution type驱动非functional alignment（task-agnostic高秩源预测task-specific低秩目标最差，within-function可比across-function低）②固定解码器在解流形随机游走中迅速退化——表征漂移≠功能变化，只是功能等价类内重参数化③稳定性-可塑性困境在网络层面不成立
  - 噪声选择定理：输入噪声期望损失∝‖Ω2Ω1‖²_F→选LSS（仍task-agnostic）；参数噪声期望损失∝‖Ω1X‖²+‖Ω2‖²→仅MRNS/MWNS最小化→task-specific——参数鲁棒性（低范数隐式正则）是脑-模型表征对齐的候选选择压力
  - 非线性扩展：ReLU四不变换（置换/缩放/nuisance神经元/复制+输入零空间）精确保函数；MNIST网络隐藏激活可augmented-Lagrangian重塑为"双大象"且保持全部训练标签；经验结果镜像线性理论（input-null对输入噪声敏感、scaled/nuisance/duplicate对参数噪声敏感）
  - **Activation**: representational similarity analysis, RSA caveats, solution manifold, task-specific representations, parameter noise robustness, linear predictivity, representational drift, brain model alignment, stability-plasticity

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

## 2026-10-03 - Economics/Investment + Quantum (Cron Job, Round 2)

### Quantum Advantage for Two-Party Differential Privacy
- [[guarded-coherent-two-party-qdp]] - 信息论量子协议突破经典双方DP精度壁垒：O(1)误差 vs Ω(√n)，守卫相干往返+equal-Gram刚性 (arXiv: 2610.02113)
  - Klauck诚实模型下，O(n)量子通信实现纯ε-QDP且 E|d̂−d| < 2/sinh ε + γ，无需计算假设/可信设置/先验纠缠；经典同模型需Ω(√n)误差
  - Equal-Gram刚性原理：非正交消息保持相同Gram矩阵 → CPTP补输出状态与输入无关（Stinespring证明）；经典转录复制（McGregor下界根源）在量子中物理不可能
  - 守卫分支模式：小概率κ=γ/(n+γ)输入无关回退分支使近似刚性变精确；精确hockey-stick散度校准给出α*>ε，近似DP误差严格更小；PC模型无分离、RR恶意模型量子协议被攻破——优势边界诚实标注
  - **Activation**: two-party differential privacy, quantum communication advantage, hamming distance privacy, guarded coherent round trip, equal-Gram rigidity, Klauck honest model, hockey-stick divergence QDP, quantum differential privacy protocol

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
## 2026-10-03 - OpenAI Research (Cron Job)

### Disrupting a coordinated model-distillation campaign
- [[adversarial-distillation-defense]] - Detect, attribute, and disrupt coordinated campaigns extracting protected model reasoning.
  - Threat model: no encryption break — operators manipulate model interactions (cross-conversation encrypted-reasoning replay, compaction exploitation) to surface hidden chain-of-thought; 16k requests/4k users spike, 15k+ user cluster
  - Detection: reasoning-visibility invariant matrix, replay-path red-team probing, prompt-pattern clustering across account graphs, responsible-disclosure intake (arXiv:2608.09867)
  - Layered response: investigate scope first → account enforcement → close cross-boundary replay paths (user/workspace/org/model-family) → third-party provider coordination → Frontier Model Forum sharing
  - Residual risks: partner-hosted deployments, tool-output channels carrying reasoning beyond visible text
  - **Activation**: adversarial distillation, protected reasoning extraction, chain-of-thought theft, reasoning replay attack, model security monitoring, distillation campaign disruption

### A model guide for the GPT-6 family
- [[practical-guide-building-gpt-6]] (Obsidian only, no skill - product guide) - Production playbook for GPT-6 model selection and long-running agent workflows.
  - Model ladder: Astra (hardest reasoning) / 6.1 Sol (complex coding, computer use) / Luna (focused tasks at scale); reasoning effort Low→Max as intelligence/price dial
  - Production: prompt caching (up to 95% input discount), compaction for long context, parallelize independent tasks, Fast/Ultrafast modes
  - Long-running agents: steering, async tool calls, delegation; explicit decision boundaries replacing blanket "always ask" rules
  - **Activation**: GPT-6 model selection, reasoning effort tuning, prompt caching, AGENTS.md best practices

## 2026-10-05 - Deep Learning Research (Cron Job)

### CARM: Cancellation-Aware Response Masking for LLM Reinforcement Learning
- [[carm-cancellation-aware-response-masking]] - LLM RL序列级off-policy掩码的符号对消缺陷与绝对值修正：几何均值log-ratio正负抵消掩盖双向漂移，|log-ratio|均值根除 (arXiv: 2610.02039)
  - 带符号对数比可跨token位置抵消——策略某段大涨另一段大跌仍被判on-policy；CARM取绝对值后平均，接受响应满足带外token比例与带外平均对数距离的联合界
  - 即插即用替换现有masking rule（TIS/GM），不改训练循环；AIME+BeyondAIME mean@16 +3.13pp，代码基准pass@1 +2.88pp
  - **Activation**: response masking, off-policy RL, LLM reinforcement learning, sequence filtering, policy drift, importance ratio, PPO filtering, GRPO

### Harnessing Domain Specialists in Multimodal Mixture-of-Experts for Efficient Adaptation
- [[expertlens-moe-domain-specialist-adaptation]] - 多模态MoE专家自发语义专化：ExpertLens免数据从router权重解码专家领域标签，选择性微调仅更新21.7-47.0%参数 (arXiv: 2610.02123)
  - 稀疏路由涌现语义modularity（数学/医学/遥感专家分化），router weights解码为词表token即得专家语义画像，无需前向数据
  - 相关专家子集微调匹配或超全参数微调，平均4.0x训练加速，全面优于LoRA——"效率稀疏性→语义模块化→高效适配"因果链
  - **Activation**: mixture-of-experts, expert specialization, router interpretation, efficient fine-tuning, selective expert tuning, MoE adaptation, semantic modularity

### Decoding Looped Transformers Better for (Almost) Free
- [[loopcd-contrastive-decoding-looped-transformers]] - Looped Transformer免训练对比解码：早期循环=弱模型、最终=强模型天然构成weak-strong对，对比引导解码可减半循环数 (arXiv: 2610.02185)
  - LoopCD-Logits在logit空间p_final^(1+α)/p_early^α（一次额外输出pass）；LoopCD-Hidden在隐状态外推（零输出开销）；完全training-free
  - Ouro-2.6B-Thinking AIME 2024 pass@1 61.88%→73.33%；Huginn HumanEval 22.56%→31.71%；剪半循环仍超全深度基线，前向FLOPs降22.5%-48.2%
  - **Activation**: looped transformer, contrastive decoding, inference acceleration, recurrent depth, weak-strong pairs, training-free decoding, inference FLOPs reduction

### Bellman Meets Lyapunov: Unsupervised Reinforcement Learning via Mastering Chaos
- [[f-cip-controllable-information-production-unsupervised-rl]] - 无监督RL内在动机去变量选择：F-CIP仅由系统动力学定义CIP目标，无监督涌现平衡/可控性原语，配简单速度奖励即得协调步态 (arXiv: 2610.02012)
  - 现有IM目标都要选信息变量（把专家知识从奖励转移到变量选择）；F-CIP的CIP目标只依赖dynamics，RL原生兼容，可与现有actor-critic直接组合
  - 单独训练涌现balancing、controllability maintenance原语行为；+forward-velocity奖励产生hopping/running步态（通常需奖励工程）
  - **Activation**: unsupervised RL, intrinsic motivation, controllable information, empowerment, reward-free exploration, primitive behavior discovery, forward CIP, robotics pretraining

### Where-OPD: Spatially Guided On-Policy Self-Distillation of MLLMs with Synthetic Scenes
- [[where-opd-spatially-guided-self-distillation]] - MLLM特权自蒸馏新形态：文本空间引导（物体身份+坐标）替代图像裁剪特权，程序化合成场景免标注post-training，合成到真实迁移+3.23pp (arXiv: 2610.02117)
  - 教师收文本空间引导定位整合多区域证据，学生从图像+问题on-policy自蒸馏复现；合成场景特权标注自动免费，可扩展免标注
  - 计数/文档/图表理解一致提升；仅合成场景训练迁移到CVBench/V*/ZoomBench/BLINK/HR-Bench/MME-RealWorld真实基准
  - **Activation**: on-policy distillation, privileged information, MLLM perception, synthetic scenes, spatial grounding, annotation-free post-training, synthetic-to-real transfer, teacher guidance

## 2026-10-06 - Deep Learning Research (Cron Job)

### Pivot-SD: Efficient Self-Distillation for Masked Diffusion Language Models
- [[pivot-sd-masked-diffusion-self-distillation]] - dLM后训练credit assignment：信息增益选出高影响力commitment(pivot)，成功轨迹pivot用CE、失败轨迹仅pivot施加定向unlikelihood，200题×4rollouts即超SFT/RL基线 (arXiv: 2610.03665)
  - 少数commitment主导剩余mask不确定性，现有recipe不定位这些关键token
  - 失败轨迹pivot级定向unlikelihood：不学错误也不浪费有效片段；LLaDA-8B数学/代码双超预算匹配RL基线
  - **Activation**: masked diffusion LM, dLM post-training, self-distillation, credit assignment, denoising commitment, unlikelihood training, LLaDA

### Learning from Repaired Reasoning: Root-Cause-Guided On-Policy Distillation
- [[rc-opd-root-cause-repaired-distillation]] - OPSD指导信号重设计：用学生自身推理的修复版本（定位最早实质错误→局部修正→锚定有效前缀→迭代continue）替代参考解，解reasoning mismatch与蒸馏陷阱 (arXiv: 2610.03515)
  - 参考解解释"如何正确"不解释"学生为何错"——学生借结论不走，自身错误未解决
  - 双通道蒸馏：root-cause-guided监督错误段 + anchor-guided支撑有效前缀；修复预算内diagnosis-repair-continuation迭代
  - **Activation**: on-policy distillation, reasoning repair, privileged hindsight, root cause analysis, distillation trap, intermediate anchor, OPSD

### Page-EntroKV: Hardware-Aligned, Entropy-Weighted KV-Cache Eviction under GQA
- [[page-entrokv-gqa-kv-eviction]] - GQA下KV驱逐按物理组而非per-head：sink隔离Rényi-2熵池化头权重+PagedAttention页对齐，UOR恒1.0（per-head并集最高4.75x膨胀），needle召回100% vs 均值池化0% (arXiv: 2610.03135)
  - per-head独立选择迫使serving引擎保留并集，cache膨胀至组比率r；算术均值稀释retrieval head、sink head伪装13x
  - 理论：两head组UOR-分歧精确恒等式+任意组比率双侧界；严格预算保持+needle保留界（均值池化可证违反）
  - **Activation**: KV cache eviction, grouped-query attention, GQA serving, PagedAttention, long context, token importance, retrieval head, sink head, cache budget

### Divergence controls entropy in distillation
- [[divergence-entropy-distillation-control]] - 蒸馏散度=隐式熵正则器：前向KL膨胀学生熵（CE为特例，预训练/SFT定量验证）、反向KL压缩熵、插值训练平滑收敛突变；on-policy蒸馏低熵来自token级反向KL非采样方式 (arXiv: 2610.03529)
  - 实践规则：要低熵确定学生→token级反向KL；要多样学生→前向KL
  - 自蒸馏：条件化特权信息压缩熵→最优散度超参=补偿该压缩的选择；先诊断熵失衡再选散度
  - **Activation**: knowledge distillation, forward KL, reverse KL, student entropy, cross-entropy, on-policy distillation, self-distillation, entropy regularization, distillation objective design

### Contextual Flow Matching (COFLOW): Adaptive Step Selection
- [[coflow-contextual-adaptive-step-flow-matching]] - Flow Matching推理时按prompt特征自适应步数：无监督奖励在线训练步数预测器，底层生成模型冻结即插即用，图像/视频2.5x加速保质，O(1/K)离散误差界 (arXiv: 2610.03202)
  - 输入依赖难度差异被固定步数忽略——简单prompt不需要复杂prompt的步数
  - 奖励=推理效率与生成保真平衡，免人工难度标注；免蒸馏免重训
  - **Activation**: flow matching acceleration, adaptive NFE, step count selection, image generation efficiency, video generation, inference-time optimization

### ZeroMAG: Zero-Shot Multimodal Adapter Generation for EEG Foundation Models
- [[zeromag-zero-shot-multimodal-adapter]] - EEG FM零样本扩展异构多模态：冻结编码器，从无标签记录（模态-被试-任务条件）在函数约束潜空间生成adapter权重，免目标标签/目标侧优化，距监督适配仅0.50pp (arXiv: 2610.03546)
  - 配置不变adapter容忍异构伴生模态组合；直接权重回归缺函数监督会退化，表征学习与条件生成双组件缺一不可
  - 6个held-out数据集×3个EFM backbone：+7.22pp over EEG-only，+4.89pp over权重回归
  - **Activation**: EEG foundation model, multimodal adapter, zero-shot adaptation, hypernetwork, adapter generation, physiological signals, cross-dataset generalization

### Zephon: Elastic Determinism for Online, Stateful FM Data Loading
- [[zephon-elastic-determinism-data-loader]] - 基础模型训练数据管线弹性确定性：拓扑无关lane划分+顺序决策串行化/无状态计算并行+有界in-flight状态checkpoint，GPU拓扑变化/resume/后端变化下全局batch序列恒定 (arXiv: 2610.03087)
  - 在线tokenize/pack/mix是有状态n-to-m变换，破坏样本索引；离线物化对视频等模态不可行
  - 恢复成本不随训练进度增长；ablation差异可归因参数而非数据顺序噪声
  - **Activation**: deterministic data loading, foundation model training, data pipeline, checkpoint resume, GPU topology, sample packing, online tokenization, shuffle reproducibility

## 2026-10-08 - OpenAI Research (Cron Job)

### Advancing computer use with Ironclad
- [[expert-rubric-computer-use-training]] - 把真实业务工作流变成 computer-use agent 的 RL 训练任务：领域专家定义细粒度 rubric（每任务 8–50 条二值标准）+ 厂商托管沙箱练习环境 + 围绕代表性工作流的合成任务变体，rubric 分数作为 RL 奖励
  - 关键：endpoint-only 打分高估 agent 就绪度——单步全对≠产出的流程在设计场景内成立；细粒度标准给 partial credit、失败定位和稠密奖励
  - GPT-6 Astra 首个用 Ironclad 任务训练的前沿模型：11 任务均分 55.0% vs GPT-5.6 Sol 41.6%，单次尝试 19.2min vs 37.0min（内部开发模型 63.7%）
  - 合作模板：具体任务示例+失败证据、定义成功的领域专家、安全测试环境、可用于研究的数据
  - **Activation**: computer-use agents, rubric evaluation, expert-defined criteria, hosted sandbox, synthetic task generation, RL from rubric feedback, partial credit scoring, SaaS workflow automation

### Sharing AI progress in mathematics
- (Obsidian only, no skill - release announcement) - 内部前沿模型的数学成果发布实践：GitHub 仓库+修订引用协议+Lean 形式化证明（机器可检验），10 份模型推理摘要、计算量估算（平均每成果 ≈3 小时 ChatGPT Pro thinking）、尝试题目统计
  - 发布规范由 IAS 独立顾问组 AGMAI 的公开建议塑造；承诺未来改进论述与引用质量
  - **Activation**: AI mathematics, Lean formalization, proof verification, scientific disclosure practices, AGMAI

