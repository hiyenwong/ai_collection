---
name: ml-latent-neural-dynamics-survey
description: Machine Learning Methods for Studying Latent Neural Activity Dynamics - IJCAI 2026 survey综述机器学习研究神经种群潜伏动力学结构的方法论，涵盖单区域潜伏动力学（LDS/RNN/Neural ODE）、多区域通信、行为对齐建模、神经基础模型（Transformer/扩散模型）
version: 1.0
author: arXiv researchers
arxiv_id: 2606.10530
paper_date: 2026-06-09
keywords: latent neural dynamics, machine learning survey, neural population, brain decoding, LVM, neural foundation model
trigger_words: neural dynamics, latent variable model, neural population decoding, brain state space, multi-region communication, behavior-aligned modeling
---

# ML方法研究潜伏神经动力学综述

## 论文定位

IJCAI 2026 survey track接受的综述论文，系统梳理机器学习方法研究大规模神经元群体潜伏结构的发展轨迹。

## 三大研究领域

### 1. 单区域潜伏动力学 Single-Region Latent Dynamics

#### 线性模型
- Linear Dynamical Systems (LDS)：经典状态空间模型
- 因子分析：降维和潜伏变量提取

#### 非线性模型
- Recurrent Neural Networks (RNN)：序列动力学建模
- Neural Ordinary Differential Equations (ODE)：连续时间动力学
- Latent Variable Models (LVM)：概率生成框架

### 2. 多区域通信 Multi-Region Communication

#### 研究重点
- 信息跨脑区传输机制
- 突触传播延迟建模
- 网络连接性分析

#### 方法论
- 概率模型：概率图模型表达区域间通信
- 子空间方法：低秩子空间分析通信模式
- 因果推断：区域间因果关系识别

### 3. 行为对齐建模 Behavior-Aligned Modeling

#### 目标
- 解耦任务相关神经活动与其他内部状态
- 行为信号引导神经表征学习

#### 方法
- 监督学习：行为标签引导潜在表征
- 对比学习：行为对比训练神经解码器
- 多任务学习：同时建模多种行为维度

## 神经基础模型 Neural Foundation Models

### Transformer架构
- 大规模预训练跨主体优化性能
- 注意力机制建模神经元间依赖
- 位置编码表达时间结构

### 扩散模型
- 生成式建模神经活动分布
- 潜伏空间扩散学习复杂动力学
- 多模态融合行为和神经数据

### 预训练策略
- 跨被试迁移学习
- 自监督神经表征学习
- 行为对齐预训练目标

## 评估框架

### 基准测试 Benchmarks
- 解码准确率：行为预测性能
- 潜伏表征质量：重建和解释性
- 跨被试泛化：迁移学习能力

### 评估标准 Evaluation Criteria
- 模型可解释性：潜伏变量语义
- 计算效率：训练和推理开销
- 数据需求：样本量敏感性

## 开放挑战 Open Challenges

### 因果链接识别
- 区域间通信方向性推断
- 潜伏变量的因果作用
- 干扰效果的因果解释

### 方向性通信 Directionality of Communication
- 信息流向估计
- 时序因果分析
- 网络拓扑推断

### 可解释性 Interpretability
- 潜伏变量神经语义
- 动力学参数可解释性
- 行为-神经映射透明度

### 可扩展性 Scalability
- 大规模神经元群体
- 长时间序列数据
- 多模态数据融合

## 方法论洞察

### 模型选择原则
- 数据规模小：线性模型或简单LVM
- 复杂动力学：Neural ODE或RNN
- 跨区域分析：多区域通信模型
- 行为指导：行为对齐建模

### 训练策略
- 监督信号充足：监督学习
- 行为数据稀缺：自监督预训练
- 多任务场景：多任务学习框架

### 计算资源考量
- 实时应用：轻量模型部署
- 离线分析：大规模基础模型
- 边缘计算：模型压缩和量化

## 应用场景

- 神经解码：从神经活动预测行为
- 脑机接口：实时神经状态估计
- 神经疾病诊断：异常动力学检测
- 认知研究：潜伏状态与认知关联

## 参考文献

- arXiv:2606.10530 原综述论文
- Latent Variable Models文献
- Neural foundation models研究