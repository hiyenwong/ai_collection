## 2026-05-21 - Neuroscience Research (Cron Job)

### FPED: Functional-Network Prior-Guided Mixture-of-Experts Framework for Interpretable Brain Decoding
- [[fped-moe-brain-decoding]] - fMRI视觉解码中基于功能网络先验引导的混合专家(MoE)框架,实现可解释的语义重建 (arXiv: 2605.19279)
  - 功能脑网络作为专门专家模块,保留大脑拓扑结构
  - 自适应路由揭示功能网络与语义处理的生物学对应关系
  - 仅0.68B参数实现高竞争力语义重建性能
  - **Activation**: fMRI decoding, Mixture-of-Experts, brain network, visual reconstruction, functional connectivity

### VENCircuit: Von Economo Neurons as Acquisition Scaffolds in Recurrent Spiking Networks
- [[vencircuit-ven-scaffold-snn]] - Von Economo神经元在脉冲神经网络中作为学习获取支架的计算模型,解释其在社交学习中的关键作用 (arXiv: 2605.17399)
  - VEN完整网络98%收敛率 vs 移除后70%,Fisher's exact p=8.7e-5
  - 形式化分析:VEN提供免疫于Jacobian不稳定性的直接梯度通路
  - 发育期缺失产生随机学习失败,类比ASD中社交技能的可变表现
  - **Activation**: Von Economo neurons, spiking neural networks, social learning, gradient pathways, autism spectrum

## 2026-05-21 - Systems Engineering + Quantum (Cron Job - Hourly)

### Unveiling Energetic Advantage in Superconducting Cat-Qubits Quantum Computation
- [[energetic-efficiency-quantum-computation]] - 超导猫量子比特计算的能量效率分析框架，从时间复杂度转向能耗分析 (arXiv: 2605.19854)
  - 能量-时间乘积(ET)作为量子计算效率综合指标
  - 猫量子比特自主错误抑制带来的能量优势
  - 全系统能耗建模：门操作、控制电子、冷却基础设施
  - **Activation**: quantum energetic efficiency, 量子能量效率, cat-qubit energetics, energy-aware quantum computing

### Universally Robust Control of Open Quantum Systems (Updated)
- [[universally-robust-quantum-control]] - 开放量子系统的噪声无关鲁棒控制框架 (arXiv: 2508.07379)
  - 动态修改系统-环境耦合实现高保真度操作
  - 无需先验噪声表征即可达到>99%保真度
  - **Activation**: robust quantum control, 鲁棒量子控制, noise-agnostic control

### Dynamic Quantum-Assisted Co-Design of Control Tuning and Lyapunov Stability Synthesis for Nonlinear Systems
- [[quantum-assisted-control-lyapunov]] - Quantum-assisted co-design of controller and Lyapunov parameters via QITE on Ising Hamiltonian surrogate (arXiv: 2605.04296)
  - Black-Hole calibration contracts search region, then QITE explores encoded Hamiltonian
  - Joint online optimization of controller gains and Lyapunov certificates
  - **Activation**: quantum-assisted control, Lyapunov synthesis, QITE optimization, Ising Hamiltonian control

### Space-Time Tradeoffs of Pauli-Based Computation in Distributed qLDPC Architectures
- [[pbc-distributed-quantum-computing]] - Large qLDPC blocks outperform surface code 10x in distributed PBC via qubit migration (arXiv: 2605.03854)
  - PBC competitive in distributed regime; establish as compilation baseline
  - Qubit migration to free nodes bypasses sequential bottleneck
  - **Activation**: pauli-based computation, PBC distributed, qLDPC architecture, quantum compilation

### Quantum Battery Optimized by Parametric Amplification
- [[quantum-battery-parametric-amplification]] - Quantum battery optimization via parametric amplification for enhanced energy storage and charging power (arXiv: 2605.14582)
  - Squeezed-state engineering increases both capacity and charging rate
  - Trade-off analysis between charging speed and energy efficiency
  - **Activation**: quantum battery, parametric amplification, quantum energy storage

### Programmable Non-Hermitian Synchronization of Light on a Silicon Photonic Processor
- [[non-hermitian-photonic-sync]] - Programmable non-Hermitian synchronization on silicon photonic chips via engineered gain/loss profiles (arXiv: 2605.14653)
  - Exceptional point control for enhanced sensing and collective dynamics
  - Reconfigurable platform for photonic network synchronization
  - **Activation**: non-hermitian synchronization, photonic processor, exceptional point photonics

### Syndrome Adaptive Gain Control for Min-Sum Decoding of Quantum LDPC Codes
- [[syndrome-adaptive-gain-qldpc]] - Adaptive MS decoder gain based on unsatisfied stabilizer fraction for QLDPC codes (arXiv: 2605.10433)
  - SAGMS adapts gain online, no per-code optimization needed
  - Matches or outperforms offline optimized SMS, approaches BP performance
  - **Activation**: syndrome adaptive gain, QLDPC decoding, min-sum decoder, quantum error correction


## 2026-05-21 - Systems Engineering + Quantum (Cron Job)

### Tolerating Device Failure in Distributed Quantum Computing
- [[distributed-quantum-fault-tolerance]] - Modular distributed QEC architecture that tolerates node failure and enables hot-swappable quantum devices, with distributed system reliability exceeding component reliability (arXiv: 2605.11088)
  - QEC over modular quantum network allows device swap during operation with minimal logical error impact
  - Distributed toric code outperforms monolithic under catastrophic node failure below 0.05% physical error rate
  - Toric vs hyperbolic Floquet code selection depends on topology regularity and encoding rate needs
  - **Activation**: distributed quantum computing, fault tolerance, device failure, modular QEC, toric code, hyperbolic Floquet, hot-swappable quantum

### Risk-Averse Ensemble Control for Control-Affine Systems
- [[risk-averse-ensemble-control]] - Risk-averse optimal control for ensembles with random inputs, establishing regularity theory for infinite-dimensional optimization with applications to quantum control (arXiv: 2605.02791)
  - Beyond expectation-based optimization: accounts for worst-case outlier phenomena across ensemble
  - Control-affine structure ensures lower semi-continuity and Fréchet differentiability
  - Adjoint state of bounded variation characterizes primal-dual optimality conditions
  - **Activation**: risk-averse control, ensemble control, optimal control, quantum control, Neural ODE, distributionally robust

## 2026-05-21 - Neuroscience Research (Cron Job)

### Geometric Phase Transition Enables Extreme Hippocampal Memory Capacity
- [[hippocampal-memory-geometry-phase-transition]] - Evolution achieves >100x memory capacity by engineering neural code geometry from disorganized "mist" to rigid "crystalline" structure, not by adding neurons (arXiv: 2605.17199)
  -  Chickadee vs. finch comparison: geometric stability (Shesha 0.245 vs 0.166) and temporal coherence (0.393 vs 0.209)
  - E/I circuit motif: excitatory neurons form scaffold, inhibitory neurons provide orthogonal decorrelation
  - Double dissociation with Valiant's SMA: continuous topological organization > discrete neuron allocation
  - "Geometric tax": 169x representational redundancy needed to stabilize crystalline manifold
  - **Activation**: hippocampal memory geometry, geometric phase transition, crystalline neural coding, Shesha stability, memory capacity scaling, E/I decorrelation, topological rigidity

### Features Have Life History. And We Should Care
- [[feature-life-history-scaffold]] - Identifies ~50 sparse "carrier scaffold" features that form the representational backbone of LLMs, assembling in the first 1% of training and recruiting 64% of all active features (arXiv: 2605.18789)
  - Two-phase training: selection (first 1%, 40x faster feature turnover) → calibration (remaining 99%)
  - Joint cross-layer ablation required: per-firing single-feature methods miss the scaffold entirely
  - Function precedes direction: carrier identity predictable from onset firing patterns (4/5 accuracy)
  - **Activation**: feature life history, carrier scaffold, representational backbone, two-phase training, cross-layer ablation, sparse features, scaffold hierarchy

### BrainDyn: A Sheaf Neural ODE for Generative Brain Dynamics
- [[braindyn-sheaf-neural-ode]] - First combination of cellular sheaf theory with neural ODEs for continuous-time brain dynamics modeling on structured brain graphs, outperforming GNNs and transformers across fMRI and EEG modalities (arXiv: 2605.19324)
  - Cellular sheaves equip each edge with restriction maps that transform node features into edge-specific shared spaces before aggregation, enabling heterogeneous inter-region communication
  - Three-component architecture: LSTM temporal encoding → sheaf Laplacian message passing → neural ODE continuous-time evolution
  - Strong forecasting across fMRI (PNC) and EEG (TUSZ) with in silico perturbation prediction capability
  - **Activation**: braindyn, sheaf neural ODE, brain dynamics forecasting, sheaf Laplacian, generative brain model, continuous-time neural dynamics, in silico perturbation

### Mechanistically
