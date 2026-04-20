---
name: brain-mgf---multimodal-graph-fusion-for-eeg-fmri
description: Skill for AI agent capabilities
---

# Brain-MGF - Multimodal Graph Fusion for EEG-fMRI

## Overview

EEG-fMRI 多模态图融合网络，用于迷幻药（psilocybin）影响下的脑连接分析。使用自适应 softmax 门控融合模态，在世界上最大的单点迷幻药数据集 PsiConnect 上验证。

**来源论文：** arXiv:2511.18325 - Brain-MGF: Multimodal Graph Fusion Network for EEG-fMRI Brain Connectivity Analysis Under Psilocybin

## 触发词

EEG-fMRI 融合、多模态图融合、Brain-MGF、psilocybin 脑连接、迷幻药脑网络、multimodal graph fusion、adaptive fusion、EEG fMRI integration

## 核心方法

### 数据集

**PsiConnect**：世界上最大的单点迷幻药数据集
- EEG + fMRI 同步记录
- 迷幻药 vs 对照条件
- 冥想和静息态任务

### 模态融合策略

1. **图构建**：偏相关边 + Pearson 特征节点
2. **图卷积**：学习主体级嵌入
3. **自适应 Softmax 门控**：样本特定权重融合

### 性能

| 任务 | 准确率 | F1 | ROC-AUC |
|------|--------|-----|---------|
| 冥想 | 74.0% | 76.5% | — |
| 静息 | 76.0% | — | 85.8% |

## 使用场景

### 适用情况

- EEG-fMRI 多模态分析
- 药物影响脑连接研究
- 意识状态分类
- 多模态融合方法验证

### 数据要求

- 同步 EEG 和 fMRI 记录
- 药物/对照条件标签
- 预处理后的连接矩阵

## 实施步骤

1. **模态图构建**
   - EEG：偏相关连接矩阵
   - fMRI：偏相关连接矩阵
   - 节点特征：Pearson 相关性

2. **图卷积嵌入**
   - 分别学习 EEG 和 fMRI 嵌入
   - 主体级表示

3. **自适应融合**
   - Softmax 门控计算模态权重
   - 样本特定融合策略

4. **分类与可视化**
   - 迷幻药 vs 对照分类
   - UMAP 可视化嵌入

## 技术细节

### 自适应门控

- 每个样本有独立的模态权重
- 捕获上下文依赖的贡献度
- 融合 vs 单模态和非自适应变体

### 图特征

- **边**：偏相关系数（去除间接连接）
- **节点**：Pearson 相关性作为特征

## 与其他方法对比

| 方法 | 多模态 | 自适应融合 | 图结构 |
|------|--------|-----------|--------|
| Brain-MGF | ✅ EEG+fMRI | ✅ 样本特定 | ✅ |
| 单模态 GNN | ❌ | ❌ | ✅ |
| 简单融合 | ✅ | ❌ 固定权重 | ⚠️ |

## 工具使用

- `exec`: 运行 PyTorch 实现
- `read`: 查看图构建配置
- `web_fetch`: 获取论文代码

## 注意事项

- 需要同步 EEG-fMRI 数据
- 预处理质量影响图构建
- 迷幻药研究需要伦理审批

## 扩展阅读

- 相关技能：`multimodal-brain-connectivity-gnn`（多模态融合）
- 相关技能：`gnn-transformer-fusion`（GNN-Transformer 融合）
- 论文链接：https://arxiv.org/abs/2511.18325
## Description

Brain-MGF - Multimodal Graph Fusion for EEG-fMRI

## Activation Keywords

- brain-mgf-multimodal-fusion
- brain-mgf-multimodal-fusion 技能
- brain-mgf-multimodal-fusion skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 图构建

### Step 2: 图卷积

### Step 3: 自适应 Softmax 门控

### Step 4: 模态图构建

### Step 5: 图卷积嵌入

## Examples

### Example 1: Basic Application

**User:** I need to apply Brain-MGF - Multimodal Graph Fusion for EEG-fMRI to my analysis.

**Agent:** I'll help you apply brain-mgf-multimodal-fusion. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for brain-mgf-multimodal-fusion?

**Agent:** Let me search for the latest research and best practices...
