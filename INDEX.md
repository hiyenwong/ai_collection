
## 2026-05-29 - Neuroscience Research (Cron Job)

### Misalignment Between Backpropagation and the Hierarchy of Brain Responses to Images
- [[backpropagation-brain-hierarchy-misalignment]] - 反向传播梯度能预测fMRI/MEG信号但组织方式与大脑不匹配 (arXiv: 2605.28693)
  - 反向传播梯度能预测fMRI/MEG信号但组织方式与大脑不匹配
  - 空间和时间层级均与反向传播顺序不一致
  - 深度网络与大脑使用不同学习机制
  - **Activation**: backpropagation, brain hierarchy, visual cortex, gradient alignment

### Exploratory Experience Shapes the Geometry of Predictive Representations
- [[exploratory-experience-predictive-representations]] - 探索性行为塑造更组织化的预测表征几何 (arXiv: 2605.27929)
  - 探索性行为塑造更组织化的预测表征几何
  - 利用性行为导致无组织的表征
  - 小鼠与人工agent的行为-表征对齐
  - **Activation**: exploration, predictive representations, active sensing, spatial navigation

### EEG-FM-Audit: A Systematic Evaluation and Analysis Pipeline for EEG Foundation Models
- [[eeg-fm-audit-systematic-evaluation]] - ASHA驱动的公平基准测试 (arXiv: 2605.26910)
  - ASHA驱动的公平基准测试
  - 范式级消融研究验证FM有效性
  - 神经生理学探测(NPP)揭示生理特征使用
  - **Activation**: EEG foundation model, ASHA benchmarking, neurophysiological probing, interpretability


---

     1|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics + Quantum (Cron Job)
     2|
     3|### Latent-Conditioned Parameterized Quantum Circuits as Universal Approximators for Distributions over Quantum States
     4|- [[latent-conditioned-pqc-universal-approximator]] - 量子态分布通用逼近定理：LPQC在1-Wasserstein距离下逼近任意密度算子概率分布 (arXiv: 2605.28690)
     5|  - 核心：经典神经网络将潜变量映射到PQC参数，证明量子分布设置的通用逼近定理
     6|  - MoE架构+多模态潜先验缓解barren plateau问题
     7|  - QM9分子结构集成实验验证，超越量子生成基线
     8|  - **Activation**: latent-conditioned PQC, LPQC, universal approximator quantum states, quantum generative modeling, Wasserstein distance quantum, barren plateau MoE
     9|
    10|## 2026-05-29 - Number Theory, Statistics, Advanced Mathematics (Cron Job)
    11|
    12|### Iterative maps emerging from cohomological structure of primes
    13|- [[prime-cohomological-maps]] - 素数上同构结构分析：迭代映射预测素数增长，对数积分函数为上同构方程的解 (arXiv: 2605.17622)
    14|  - 核心要点 1: 素数间隙按分离距离分组，可用迭代映射描述其主要增长
    15|  - 核心要点 2: 剩余涨落编码上同构结构，li(x)为上同构方程的解
    16|  - **Activation**: cohomological prime analysis, prime number iterative maps, 素数上同构分析, 素数迭代映射, logarithmic integral prime distribution
    17|
    18|### Module Lattice Security Part III: Structured CVP Distance on the Log-Unit Lattice
    19|- [[module-lattice-security]] (enhanced) - 模格安全性分析：L2 CVP距离收敛到Voronoi细胞内 (arXiv: 2605.17404)
    20|  - 核心要点: 随机短环元素到对数单位格的L2 CVP距离收敛到 pi/(2*sqrt(6))*sqrt(n)
    21|  - **Activation**: module lattice security, post-quantum cryptography, 模格安全
    22|
    23|### A Uniform Random-Lattice Tail Bound for the SVP Kissing-Profile Parameter
    24|- [[svp-lattice-tail-bound]] (enhanced) - SVP算法格子参数概率保证：Haar随机格尾界 (arXiv: 2605.21966)
    25|  - 核心要点: 证明gamma(L)等于2的o(n)次方对Haar-Siegel随机格以高概率成立
    26|  - **Activation**: SVP algorithm, lattice tail bound, shortest vector problem, Rogers mean value
    27|
    28|## 2026-05-28 - Systems Engineering + Quantum (Cron Job)
    29|
    30|### QuCtrl-BELL: A Compiler-Driven Sub-Microsecond Feedback Control Stack for Scalable Trapped-Ion Quantum Experiments
    31|- [[quctrl-bell-compiler-quantum-control]] - 编译器驱动量子控制栈方法论：六阶段转译管道实现亚微秒级反馈控制 (arXiv: 2605.22433)
    32|  - 控制流与硬件状态解耦，Python DSL → 六阶段编译 → 确定性硬件程序
    33|  - 跨板同步协议支持 <700ns 反馈延迟，无需主机干预
    34|  - **Activation**: compiler quantum control, QuCtrl-BELL, sub-microsecond feedback, trapped-ion control, quantum DSL
    35|
    36|### Adaptive Reinforcement Learning for Robust Open Quantum System Control
    37|- 多任务 SAC 强化学习框架：51 种哈密顿量变体下的鲁棒量子控制 (arXiv: 2605.26925)
    38|  - RIM 分析揭示 SAC 策略对脉冲扰动和退相干变异的鲁棒性优于 GRAPE
    39|  - **Activation**: adaptive quantum control, SAC RL, robustness measure, open quantum systems
    40|
    41|### Toward General Quantum Control with Physics-Informed LLMs (VF-QCTRL)
    42|- 物理信息 LLM 量子控制框架：符号推理 + 优化反馈循环 (arXiv: 2605.26021)
    43|  - QCTRL-BENCH 16 任务基准测试，训练-free 通用量子控制
    44|  - **Activation**: physics-informed LLM, VF-QCTRL, QCTRL-BENCH, analytic control ansatz
    45|
    46|### Scaling Quantum Optimization for Unit Commitment via Pauli Correlation Encoding
    47|- Pauli 相关编码优化：大规模组合优化的量子-经典混合方案 (arXiv: 2605.17145)
    48|  - Leader-follower 架构，312 二进制变量仅需 ~30 量子比特
    49|  - **Activation**: Pauli Correlation Encoding, PCE QUBO, leader-follower optimization, unit commitment
    50|
    51|