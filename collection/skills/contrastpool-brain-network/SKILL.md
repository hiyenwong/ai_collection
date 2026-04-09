# ContrastPool - Contrastive Graph Pooling for Brain Networks

## Overview

对比图池化方法，用于 fMRI 脑网络的可解释分类。提出对比双注意力块和可微分图池化，满足 fMRI 数据特殊需求。在帕金森、阿尔茨海默、自闭症等数据集上验证有效。

**来源论文：** arXiv:2307.11133 - Contrastive Graph Pooling for Explainable Classification of Brain Networks

## 触发词

对比图池化、ContrastPool、脑网络可解释、fMRI GNN、contrastive graph pooling、explainable brain network、dual attention GNN

## 核心方法

### 挑战

- fMRI 数据特征独特
- GNN 需要针对脑网络设计
- 可解释性要求

### 解决方案

1. **对比双注意力块**：提取有效特征
2. **可微分图池化 (ContrastPool)**：自适应池化
3. **领域可解释性**：模式匹配神经科学知识

### 验证数据集

- 5 个静息态 fMRI 数据集
- 3 种疾病（帕金森、阿尔茨海默、自闭症）

## 使用场景

### 适用情况

- fMRI 脑网络分类
- 神经退行性疾病诊断
- 可解释 GNN 应用
- 脑网络特征提取

### 数据要求

- 静息态 fMRI 脑网络
- 疾病标签

## 实施步骤

1. **脑网络构建**
   - 从 fMRI 构建功能连接图
   - 定义节点和边

2. **对比双注意力**
   - 应用双注意力机制
   - 对比学习目标

3. **图池化**
   - ContrastPool 可微分池化
   - 生成图级表示

4. **分类与解释**
   - 疾病分类
   - 分析提取的模式

## 技术细节

### 对比双注意力

- 双路径注意力机制
- 对比损失增强区分性

### ContrastPool

- 可微分池化
- 保持领域可解释性

## 与其他方法对比

| 方法 | 可解释性 | fMRI 适配 | 池化方式 |
|------|---------|----------|---------|
| ContrastPool | ✅ 匹配领域知识 | ✅ 专门设计 | ✅ 可微分 |
| 标准 GNN | ❌ 黑盒 | ⚠️ 通用 | ⚠️ 固定 |
| DiffPool | ⚠️ 有限 | ❌ | ✅ 可微分 |

## 工具使用

- `exec`: 运行 PyTorch Geometric 实现
- `read`: 查看 fMRI 预处理配置
- `web_fetch`: 获取论文代码

## 注意事项

- fMRI 预处理质量重要
- 对比学习需要合适负样本
- 池化比例需要调优

## 扩展阅读

- 相关技能：`multimodal-brain-connectivity-gnn`（多模态 GNN）
- 相关技能：`gnn-transformer-fusion`（GNN-Transformer）
- 论文链接：https://arxiv.org/abs/2307.11133
## Description

ContrastPool - Contrastive Graph Pooling for Brain Networks

## Activation Keywords

- contrastpool-brain-network
- contrastpool-brain-network 技能
- contrastpool-brain-network skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 对比双注意力块

### Step 2: 可微分图池化 (ContrastPool)

### Step 3: 领域可解释性

### Step 4: 脑网络构建

### Step 5: 对比双注意力

## Examples

### Example 1: Basic Application

**User:** I need to apply ContrastPool - Contrastive Graph Pooling for Brain Networks to my analysis.

**Agent:** I'll help you apply contrastpool-brain-network. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for contrastpool-brain-network?

**Agent:** Let me search for the latest research and best practices...
