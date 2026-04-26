---
name: neuromamba-brain-connectivity-mamba-llm
version: 1.0.0
description: End-to-end framework integrating dynamic latent graph learning, selective state-space (Mamba) temporal modeling, and LLM reasoning for fMRI functional connectivity analysis. Applied to autism classification on ABIDE dataset.
created: 2026-04-23
source: arXiv:2602.13770
authors: Torabi, Razmara, Ajorlou, Baraeinejad
title: "NeuroMambaLLM: Dynamic Graph Learning of fMRI Functional Connectivity Using Mamba and Language Model Reasoning"
tags: [fmri, functional-connectivity, mamba, LLM, dynamic-graph, autism-classification, brain-network]
activation: fMRI connectivity, Mamba state-space, LLM reasoning, dynamic graph learning, autism, brain network classification
---

# NeuroMambaLLM: Dynamic Graph + Mamba + LLM for fMRI Connectivity

## 概述
端到端框架，整合动态潜在图学习、选择性状态空间（Mamba）时间建模与大语言模型推理，应用于自闭症脑功能连接分析。

## 核心创新
1. **动态潜在图学习** — 从原始BOLD时间序列动态学习功能连接，取代固定相关性图
2. **Mamba时序建模** — 选择性状态空间模型捕获BOLD信号的长期依赖
3. **LLM推理增强** — 利用语言模型的推理能力提升分类决策
4. **端到端训练** — 图学习、时序建模和分类联合优化

## 方法论架构

### 第一阶段：动态潜在图学习
```
原始BOLD时间序列
  → 滑动窗口分割
  → 潜在空间映射
  → 自适应邻接矩阵学习
  → 动态脑图序列
```

**关键技术**:
- 不使用固定Pearson相关矩阵
- 学习自适应潜在连接，捕获非线性依赖
- 图结构随时间动态变化

### 第二阶段：Mamba时序建模
```
动态图序列
  → 图神经网络（GNN）节点嵌入
  → Mamba选择性状态空间
  → 长程时间依赖建模
  → 时序特征聚合
```

**Mamba优势**:
- 线性时间复杂度（vs Transformer的二次复杂度）
- 选择性扫描机制聚焦关键时间点
- 适合fMRI的长序列特征

### 第三阶段：LLM推理
```
时序特征
  → 特征到文本转换
  → LLM提示工程
  → 推理增强分类
  → 最终预测
```

## 与传统方法对比
| 方法 | FC构建 | 时序模型 | 分类器 |
|---|---|---|---|
| 传统GLM | 静态相关 | 线性回归 | SVM |
| GCN | 静态图 | GNN | Softmax |
| BrainGNN | 静态图 | 图池化GNN | MLP |
| **NeuroMambaLLM** | **动态潜在图** | **Mamba SSM** | **LLM** |

## 关键技术参数
- **输入**: 原始BOLD时间序列（无需预计算FC矩阵）
- **图学习**: 可学习邻接矩阵，带稀疏性约束
- **Mamba参数**: 选择性扫描 + 状态空间维度
- **LLM**: 用于推理增强的轻量级语言模型

## 应用：自闭症谱系障碍分类
- 数据集: ABIDE (Autism Brain Imaging Data Exchange)
- 任务: ASD vs TD（典型发育）分类
- 评估: 准确率、AUC、F1-score
- 优势: 捕获动态连接变化，而非静态模式

## 复现要点
1. **数据预处理**: 标准fMRI预处理管道（运动校正、空间标准化、平滑）
2. **BOLD序列**: 使用预处理的ROI时间序列
3. **图学习模块**: 可微的邻接矩阵学习层
4. **Mamba集成**: 替换Transformer注意力为选择性状态空间
5. **LLM融合**: 设计合适的提示模板将数值特征转为文本描述

## 扩展应用
- 其他脑疾病分类（ADHD、精神分裂症、阿尔茨海默症）
- 脑状态解码
- 脑年龄预测
- 多站点数据迁移学习

## 参考信息
- arXiv: 2602.13770
- 日期: 2026-02-14
- 领域: eess.IV, cs.AI, cs.LG
- 应用数据集: ABIDE
