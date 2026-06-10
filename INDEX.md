# AI Collection Index

## 2026-06-11 - Neuroscience + Computational Physics (Cron Job)

### NeuroPINNs: Neuroscience Inspired Physics Informed Neural Networks
- [[neuropinns-spiking-pinn]] - 神经科学启发的 Physics-Informed Neural Networks，使用 Variable Spiking Neurons 实现能量高效的 PDE 求解，stochastic projection 方法解决 spike discontinuity 与 gradient optimization 的兼容问题 (arXiv: 2511.06081)
  - 核心创新：Variable Spiking Neurons (VSNs) 实现稀疏事件驱动通信
  - Upscaled theory 启发的 stochastic projection 方法避免系统性偏差
  - 应用验证：4个代表性 PDE 问题 + 3D 线性弹性微力学
  - Neuromorphic-ready：适合 Intel Loihi/BrainScaleS 等硬件部署
  - **Activation**: neuropinns, spiking-pinn, variable-spiking-neuron, neuromorphic-pde, energy-efficient-pde, event-driven-pinn

## 2026-06-11 - Neuroscience Research (Cron Job)

### Multifractal Space-Filling Curve Analysis for MRI Dementia Biomarker
- [[multifractal-space-filling-curve-mri-dementia]] - MFSCA方法论：空间填充曲线投影+多重分形分析，量化MRI脑结构组织，揭示老化/痴呆进展中的多重分形→单分形转变 (arXiv: 2606.10222)
  - 核心创新：Φ: R^N → R^1投影保持局部和长程空间关系
  - 多重分形谱f(α)量化空间组织异质性（Δα = α_max - α_min）
  - 临床发现：Young Control → Elderly Control → Early dementia → MCI显示Δα递减
  - **Activation**: MFSCA, multifractal MRI, space-filling curve, dementia biomarker, Hilbert curve

## 2026-06-11 - Systems Engineering + Quantum (Cron Job)

### SCOPE: A Syndrome-Driven Control Plane for QEC-Enabled Quantum Networks
- [[scope-qec-control-plane]] - 量子网络控制面从物理层保真度转向逻辑层错误率，利用QEC解码器综合征数据驱动路由决策 (arXiv: 2606.08873)
  - 核心转变：控制面基于逻辑错误综合征而非物理层指标
  - 架构组件：综合征聚合器 + 逻辑错误估计器 + 控制面接口
  - 端到端优化：逻辑错误率为真实性能指标
  - **Activation**: quantum control plane, syndrome-driven routing, QEC network, logical error rate, fault-tolerant quantum network

### Neural Network Decoder Confidence as Learned Proxy for Logical Gap
- [[neural-decoder-confidence-qec]] - 神经网络解码器置信度作为逻辑间隙的学习代理，将硬判决解码器扩展为软可靠性估计 (arXiv: 2606.08758)
  - 硬判决vs软信息：解码器输出校正+置信度
  - 置信度代理：神经网络学习估计逻辑间隙
  - 下游应用：自适应QEC、网络路由、资源分配
  - **Activation**: neural decoder confidence, logical gap proxy, QEC soft decoding, decoder reliability

### Coset Ensemble Decoder for Quantum Error Correction with Algorithm-Hardware Co-Design
- [[coset-ensemble-decoder-qec]] - 基于陪集分解的量子纠错解码器，算法-硬件协同设计实现低延迟高精度实时解码 (arXiv: 2606.11076)
  - 陪集分解：将解码问题分解为并行子问题
  - 硬件协同：专用解码器硬件优化陪集操作
  - 集成投票：多解码器共识提高准确率
  - **Activation**: coset ensemble decoder, QEC decoder, algorithm-hardware co-design, real-time QEC, syndrome decoding

### Adaptive Identification of Low-Degree Polynomials in QSVT for Nonlinear Quantum Properties Estimation
- [[qsvt-adaptive-spectral-cutoff]] - 自适应谱截断方法优化QSVT多项式度数选择，无需最坏情况边界即可估计冯·诺依曼熵和Rényi熵 (arXiv: 2606.10994)
  - 两阶段算法：搜索谱截断→自适应QSVT估计
  - 任务依赖：不同性质需要不同截断精度
  - 无需先验：不需要最小特征值或秩信息
  - **Activation**: qsvt adaptive cutoff, quantum singular value transformation, von Neumann entropy estimation, spectral cutoff, nonlinear quantum property

## 2026-06-11 - Systems Engineering + Quantum (Cron Job)

### Analog Quantum AEGNN: Event-Based Graph Neural Networks on Neutral-Atom Processors
- [[analog-quantum-event-gnn]] - 将事件驱动图神经网络映射到中性原子量子处理器，利用Rydberg哈密顿量原生执行事件图计算，混合量子经典训练优化激光参数 (arXiv: 2606.11000)
  - 核心创新：事件-原子映射 + Rydberg哈密顿量编程实现原生消息传递
  - 流式处理：异步事件到达，无需批处理同步
  - 混合训练：经典优化器调整激光脉冲振幅和失谐
  - **Activation**: analog quantum, AEGNN, neutral-atom, Rydberg Hamiltonian, event camera, quantum GNN

### Free Parametrization of L2-Bounded SSM Controllers for Nonlinear Control with Stability Guarantees
- [[l2ru-ssm-controller-stability]] - L2有界结构化状态空间模型的自由参数化方法，通过L2-Recurrent Unit保证闭环稳定性，无需额外约束优化 (arXiv: 2606.11049)
  - 核心创新：LTI系统L2增益自由参数化，小增益定理保证稳定性
  - L2RU架构：按设计强制L2约束，独立于优化参数
  - 并行扫描：高效处理长输入序列
  - **Activation**: L2-bounded controller, state-space model, nonlinear control, stability guarantee, small-gain theorem

## 2026-06-11 - Neuroscience Research (Cron Job)

### Functional Whole-Brain Models: A New Framework for Unifying Brain Structure and Cognitive Function
- [[functional-whole-brain-models-fwbm]] - 统一建模范式整合结构真实性、动力学真实性与功能能力，四项最小标准+三支柱路线图 (arXiv: 2605.18118)
  - 结构基础：经验连接组+区域生物学
  - 动力学真实性：连续时间+兴奋抑制平衡
  - 功能能力：跨认知域任务执行
  - 可映射数据：fMRI/EEG/行为数据
  - **Activation**: fWBMs, whole-brain modeling, neuroconnectionism, cognitive function, connectome

### Recovering Sparse Neural Connectivity from Partial Measurements
- [[sparse-neural-connectivity-recovery]] - 协方差方法+Granger因果精化，从部分测量恢复连接矩阵，Stein-Price identity揭示线性近似隐式正则化优势 (arXiv: 2603.18497)
  - 协方差累积：跨session成对估计
  - Granger精化：生物约束+投影梯度
  - 控制-估计权衡：刺激vs动力学保真度
  - **Activation**: neural connectivity, partial measurements, covariance method, Granger causality, Stein-Price identity
