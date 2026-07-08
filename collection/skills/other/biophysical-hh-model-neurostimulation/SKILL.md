---
name: biophysical-hh-model-neurostimulation
description: Learning biophysical Hodgkin-Huxley models from extracellular MEA data for precise neurostimulation prediction
tags: [hodgkin-huxley, neurostimulation, multi-electrode-array, differentiable-simulation, icml-2026]
paper: arXiv:2607.04063
date: 2026-07-08
---

# Learning Biophysical Models of Large-Scale Multineuronal Data to Enable Precise Neurostimulation

## 核心方法论

**研究问题**：如何从细胞外多电极阵列 (MEA) 数据快速推断 Hodgkin-Huxley (HH) 生物物理参数，以预测神经对电刺激的响应？

**核心创新**：
1. **可微分生物物理模拟**：结合可微分 HH 模型与基于模拟的推断
2. **细胞外数据推断**：仅从 MEA 细胞外测量推断 HH 参数（无需细胞内记录）
3. **刺激响应预测**：用几分钟记录数据训练的模型预测数小时的刺激测试

## 技术细节

### 实验设置
- **数据源**：离体猕猴视网膜
- **设备**：30 μm 间距 512 电极阵列
- **数据量**：数百小时刺激和记录数据
- **训练数据**：仅需几分钟记录

### 方法流程
```
1. 设计细胞外 MEA 测量特征
2. 利用可微分生物物理模拟
3. 基于模拟的推断 (simulation-based inference)
4. 推断 HH 参数
5. 预测未见过的多电极刺激响应
```

### 关键结果
- **预测精度**：90.6%（使用仅几分钟记录拟合的 HH 模型）
- **效率提升**：替代数小时的临床刺激测试
- **可扩展性**：高通量捕获许多神经元的几何和细胞特异性特性

## 应用价值

### 转化神经工程
- **核心目标**：预测候选神经刺激模式的神经放电响应
- **临床意义**：将原本需要数小时测量的过程缩短为几分钟
- **应用范围**：视网膜假体、深部脑刺激、脊髓刺激

### 技术优势
1. **非侵入性**：使用细胞外记录而非细胞内记录
2. **高通量**：同时处理整个神经群体
3. **生物物理可解释**：基于原理性 HH 框架
4. **预测性强**：可预测未见过的刺激模式

## 关键洞察

1. **可微分模拟的力量**：使复杂生物物理模型的参数推断成为可能
2. **数据效率**：极少训练数据即可达到高精度预测
3. **生物物理约束**：HH 模型提供原理性框架，避免黑箱
4. **临床转化潜力**：直接应用于神经假体设备优化

## 应用场景

- **视网膜假体**：优化人工视网膜刺激参数
- **深部脑刺激**：个性化帕金森病治疗
- **神经调控**：精确控制神经活动
- **基础研究**：大规模神经电路生物物理建模

## 激活关键词

Hodgkin-Huxley, neurostimulation, multi-electrode array, differentiable simulation, biophysical modeling, retina, neural prosthesis, simulation-based inference

## 相关技能链接

- [[hybrid-biophysical-neuron-neural-ode]]
- [[pinn-neuronal-parameter-estimation]]
- [[neuron-model-reconstruction]]
