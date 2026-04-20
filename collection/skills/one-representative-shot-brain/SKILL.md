---
name: one-representative-shot-brain-connectivity-learnin
description: Skill for AI agent capabilities
---

# One Representative-Shot Brain Connectivity Learning

## Overview

使用群体驱动模板（Connectional Brain Template, CBT）实现脑连接图的单样本学习分类和演化预测。首个在单个群体模板上训练 GNN 的单样本学习范式。

**来源论文：** arXiv:2110.11238 - One Representative-Shot Learning Using a Population-Driven Template with Application to Brain Connectivity Classification and Evolution Prediction

## 触发词

单样本学习脑连接、CBT 学习、one-shot brain connectivity、population-driven template、connectional brain template、representative-shot learning

## 核心方法

### 挑战

- 深度学习需要大量数据
- 罕见疾病神经影像数据稀缺
- 低资源临床设施数据有限

### 解决方案

**群体驱动模板 (CBT)**：
- 紧凑表示群体脑图
- 捕获个体间共享的连接模式
- 类似于神经影像的脑图谱

### 创新点

- 首个在单个 CBT 上训练 GNN 的方法
- 从"数据驱动"转向"模板驱动"

## 使用场景

### 适用情况

- 罕见神经系统疾病分类
- 低资源临床环境
- 脑连接演化预测
- 数据稀缺场景

### 数据要求

- 群体脑连接图用于构建 CBT
- 单个测试样本

## 实施步骤

1. **CBT 构建**
   - 从群体脑图构建连接脑模板
   - 捕获共享连接模式

2. **GNN 训练**
   - 在单个 CBT 上训练图神经网络
   - 学习判别性特征

3. **分类/预测**
   - 对新样本进行分类
   - 预测脑连接演化

4. **迁移应用**
   - 应用于不同人群或疾病

## 技术细节

### CBT 特性

- 群体代表性
- 连接模式保持
- 可解释性

### 单样本学习策略

- 模板作为"代表性样本"
- 无需大规模训练集
- 泛化到新个体

## 与其他方法对比

| 方法 | 训练数据需求 | 适用场景 |
|------|-------------|---------|
| One Representative-Shot | 单个 CBT | 数据稀缺 |
| Few-shot GNN | 少量样本 | 中等稀缺 |
| 传统 GNN | 大量样本 | 数据充足 |

## 与数据增强的区别

| 数据增强方法 | 单样本学习方法 |
|-------------|---------------|
| 从模板生成多个样本 | 直接在模板上训练 |
| 增加数据量 | 减少数据需求 |
| 生成多样性 | 学习代表性 |

## 工具使用

- `exec`: 运行 GNN 实现
- `read`: 查看 CBT 配置
- `web_fetch`: 获取论文代码

## 注意事项

- CBT 质量影响分类性能
- 群体代表性需要验证
- 可能需要领域适配

## 扩展阅读

- 相关技能：`brain-graph-augmentation-template`（图数据增强）
- 相关技能：`federated-brain-trajectory-gnn`（联邦学习）
- 论文链接：https://arxiv.org/abs/2110.11238
## Description

One Representative-Shot Brain Connectivity Learning

## Activation Keywords

- one-representative-shot-brain
- one-representative-shot-brain 技能
- one-representative-shot-brain skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: CBT 构建

### Step 2: GNN 训练

### Step 3: 分类/预测

### Step 4: 迁移应用

### Step 5: Understand the Request

## Examples

### Example 1: Basic Application

**User:** I need to apply One Representative-Shot Brain Connectivity Learning to my analysis.

**Agent:** I'll help you apply one-representative-shot-brain. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for one-representative-shot-brain?

**Agent:** Let me search for the latest research and best practices...
