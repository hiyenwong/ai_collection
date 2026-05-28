---
name: eeg-fm-audit-systematic-evaluation
description: EEG基础模型系统评估和分析管道。提出三组件评估框架：ASHA基准测试、范式级消融研究、神经生理学探测，揭示EEG-FMs的真实性能和可解释性。Activation: EEG foundation model, systematic evaluation, ASHA benchmarking, paradigm ablation, neurophysiological probing, neural decoding, interpretability.
version: 1.0.0
author: Xianheng Wang, Yige Yang, Damien Coyle
arxiv_id: 2605.26910
created: 2026-05-28
category: neuroscience
tags:
  - eeg-foundation-model
  - systematic-evaluation
  - benchmarking
  - interpretability
  - neural-decoding
---

# EEG-FM-Audit: Systematic Evaluation Pipeline

## 核心问题

大型EEG基础模型（FMs）在跨认知任务解码中展现巨大潜力，但现有研究存在三大关键局限：
1. 监督基线调优不透明
2. 复杂学习范式的贡献未验证
3. 模型决策缺乏透明度

## 方法论框架

### 三组件评估管道

#### 1. ASHA驱动基准测试
- **目的**：通过透明优化确保公平比较
- **方法**：使用ASHA算法系统优化监督基线
- **结果**：揭示适当调优的监督基线可匹配或超越高级FMs

#### 2. 范式级消融研究
- **目的**：评估FMs学习范式的有效性
- **方法**：系统性消融不同学习范式组件
- **发现**：学习范式有效性高度依赖数据集规模和架构

#### 3. 神经生理学探测（NPP）
- **目的**：探索FMs是否利用有效的EEG时空频特性
- **维度**：
  - 时间特性探测
  - 空间特性探测
  - 频谱特性探测
- **意义**：建立更可解释的神经解码框架

## 实验验证

### 数据集
- 4个最先进EEG-FMs
- 5个代表性监督模型
- 3个公开数据集

### 关键发现

#### 1. 基线性能
- **惊人发现**：适当调优的监督基线可匹配或超越高级FMs
- **参数效率**：监督基线参数量显著更少
- **意义**：挑战"更大更好"的传统观念

#### 2. 范式依赖性
- 学习范式有效性非普适
- 数据集规模是关键因素
- 架构设计影响范式效果

#### 3. 生理特征依赖
- FMs依赖特定生理特征
- NPP揭示特征利用模式
- 提供可解释性证据

## 技术创新

### ASHA基准协议
- 透明超参数优化
- 自动化基线调优
- 可复现的比较标准

### NPP框架
- 时间特性探针
- 空间特性探针
- 频谱特性探针
- 多维度可解释性分析

### 范式消融方法
- 模块化消融设计
- 定量贡献评估
- 架构依赖分析

## 应用场景

### 1. 模型评估
- 系统评估新EEG-FMs
- 验证范式有效性
- 对比监督vs无监督

### 2. 模型改进
- 识别有效学习范式
- 优化架构设计
- 提升可解释性

### 3. 研究指导
- 建立评估标准
- 指导模型开发
- 促进领域标准化

## 启示与影响

### 对EEG-FM研究
- 提供标准化评估工具
- 揭示真实性能差距
- 促进透明研究

### 对神经解码
- 建立可解释性框架
- 验证生理合理性
- 提升模型可信度

### 对机器学习
- 范式有效性评估方法
- 基线调优重要性
- 参数效率启示

## 未来方向

1. **扩展验证**：更多数据集和任务
2. **新范式探索**：评估新兴学习范式
3. **跨模态应用**：扩展到其他神经信号
4. **自动化评估**：开发自动化评估系统

## 参考文献

arXiv:2605.26910 - EEG-FM-Audit: A Systematic Evaluation and Analysis Pipeline for EEG Foundation Models

## Activation Keywords

- EEG foundation model evaluation
- ASHA benchmarking protocol
- neurophysiological probing framework
- systematic EEG-FM audit
- paradigm ablation study
- neural decoding interpretability
