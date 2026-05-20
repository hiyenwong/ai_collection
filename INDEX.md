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