---
name: unifying-von-neumann-hpc-neuromorphic-ebbrains
description: 统一冯诺依曼HPC与神经形态计算的EBRAINS工作流框架 - 透明跨平台执行SNN，支持异构架构无缝切换。
version: 1.0.0
author: arXiv:2606.08515 (Krishna Kant Singh et al.)
date: 2026-06-13
arxiv_id: 2606.08515
activation_keywords:
  - neuromorphic computing
  - von neumann hpc
  - ebbrains
  - heterogeneous architecture
  - snn acceleration
  - workflow orchestration
  - brain-inspired computing
  - transparent execution
---

# Unifying von-Neumann HPC and Neuromorphic Acceleration via EBRAINS Research Infrastructure

arXiv:2606.08515 - Submitted 7 June 2026

**Authors**: Krishna Kant Singh, Charl Linssen, Eric Müller, Eleni Mathioulaki, Wouter Klijn, Lena Oden

**Categories**: cs.DC

## TL;DR

提出EBRAINS研究基础设施上的统一框架，实现冯诺依曼HPC与神经形态加速器的无缝集成，支持单一科学工作流在异构架构间透明执行。

## Problem Statement

现代科学工作流日益跨越多样计算架构:
- 冯诺依曼HPC: 高精度数值模拟
- 神经形态加速器: 低功耗、实时SNN推理
- 执行单一工作流需要跨架构适配
- 缺乏统一调度和资源管理框架

## Core Contribution

**EBRAINS统一框架**:

1. **透明跨平台执行**: SNN模型自动适配不同硬件
2. **工作流编排**: 混合架构任务调度
3. **资源抽象层**: 统一API隐藏底层差异
4. **性能优化**: 架构特定优化策略

## Key Methodology

### 1. Architecture Abstraction
```
Workflow Definition
├── Task Graph (DAG)
│   ├── HPC Tasks (传统计算)
│   ├── Neuromorphic Tasks (SNN推理)
│   └── Hybrid Tasks (混合执行)
└── Resource Mapping
    ├── CPU/GPU Clusters (HPC)
    ├── SpiNNaker/BrainScaleS (神经形态)
    └── Dynamic Allocation
```

### 2. Transparent Execution Layer
- 自动任务分派
- 数据格式转换
- 异构通信管理
- 性能监控

### 3. EBRAINS Infrastructure Integration
- SpiNNaker neuromorphic boards
- BrainScaleS analog neuromorphic
- HPC cluster nodes
- Unified scheduling API

## Key Features

### Seamless SNN Deployment
```python
# Conceptual workflow
workflow = EBRAINSWorkflow()

# Define SNN model (architecture-agnostic)
snn = SpikingModel(...)

# Transparent execution
workflow.run(
    model=snn,
    backend='auto',  # Auto-select: HPC/neuromorphic
    optimization='power',  # 或 'speed', 'accuracy'
)
```

### Dynamic Resource Allocation
- 任务特征分析 (计算密集 vs 通信密集)
- 架构匹配 (神经形态 vs 冯诺依曼)
- 运行时迁移 (负载均衡)

### Performance Metrics
- 能耗效率: 神经形态优势
- 计算吞吐: HPC优势
- 实时性: 混合优化

## Implications for Neuroscience Research

### Large-Scale Brain Simulation
- 百万神经元网络模拟
- 实时行为验证
- 低功耗长期运行

### Hybrid Simulation-Experiment
- HPC预处理 + 神经形态实时推理
- 闭环神经接口
- 边缘计算部署

### Research Workflow Modernization
- 单一框架覆盖全研究生命周期
- 降低架构切换成本
- 促进跨学科协作

## Technical Details

### Supported Platforms
- **HPC**: CPU集群、GPU加速、云平台
- **Neuromorphic**: SpiNNaker2, BrainScaleS-2, Intel Loihi
- **Hybrid**: FPGA加速、边缘设备

### Data Flow Management
- 异构架构间数据传输
- 格式转换 (浮点 → 脉冲编码)
- 带宽优化 (压缩、缓存)

### Fault Tolerance
- 任务级容错
- 架构切换备用
- 结果验证机制

## Future Directions

1. 自适应架构选择 (基于任务特征)
2. 能效优化调度算法
3. 更多神经形态硬件支持
4. 实时工作流监控界面

## Related Work

- SpiNNaker neuromorphic platform
- BrainScaleS analog neuromorphic
- NEST brain simulation
-神经形态边缘计算框架

---

## References

- Singh et al. (2026). arXiv:2606.08515
- EBRAINS: https://ebrains.eu/
- SpiNNaker: https://spinnakermanchester.github.io/