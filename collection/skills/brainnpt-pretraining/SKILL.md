# BrainNPT - Brain Network Pre-trained Transformer

## Overview

脑网络预训练 Transformer 模型。使用 <cls> token 作为分类嵌入向量，通过预训练框架利用无标签脑网络数据学习结构信息。解决深度学习在脑影像分析中标签数据有限的问题。

**来源论文：** arXiv:2305.01666 - BrainNPT: Pre-training of Transformer networks for brain network classification

## 触发词

脑网络 Transformer、BrainNPT、脑网络预训练、Transformer 脑分类、brain network pretraining、functional network classification、脑网络迁移学习

## 核心方法

### 挑战

- 深度学习在脑影像分析受限于标签数据
- 预训练技术在脑网络分析中探索不足

### 解决方案

**BrainNPT 架构：**
1. **Transformer 主干**：处理脑网络表示
2. **<cls> Token**：分类嵌入向量
3. **预训练框架**：利用无标签数据学习结构信息

### 优势

- 无预训练已达 SOTA
- 预训练进一步提升性能
- 有效捕获脑网络表示

## 使用场景

### 适用情况

- 脑功能网络分类
- 疾病诊断（标签稀缺）
- 脑网络迁移学习
- 预训练-微调范式

### 数据要求

- 功能连接矩阵
- 无标签数据可用于预训练
- 标签数据用于微调

## 实施步骤

1. **数据准备**
   - 构建功能连接矩阵
   - 收集无标签脑网络数据

2. **预训练**
   - 使用无标签数据
   - 学习脑网络结构信息

3. **微调**
   - 在下游任务上微调
   - 使用 <cls> token 分类

4. **评估**
   - 与 SOTA 方法对比
   - 消融预训练效果

## 技术细节

### <cls> Token 机制

- 类似 BERT 的分类 token
- 聚合整个脑网络表示
- 用于下游分类任务

### 预训练目标

- 掩码重建
- 对比学习
- 结构预测

## 与其他方法对比

| 方法 | 预训练 | 标签需求 | 性能 |
|------|--------|---------|------|
| BrainNPT | ✅ | 低 | ✅ SOTA |
| 传统 CNN | ❌ | 高 | ⚠️ |
| GNN | ❌ | 中 | ⚠️ |

## 工具使用

- `exec`: 运行 PyTorch 实现
- `read`: 查看网络配置
- `web_fetch`: 获取论文代码

## 注意事项

- 预训练数据量影响效果
- 脑网络表示方式需要统一
- 下游任务需要合适的微调策略

## 扩展阅读

- 相关技能：`eeg-foundation-model`（EEG 预训练）
- 相关技能：`gnn-transformer-fusion`（GNN-Transformer 融合）
- 论文链接：https://arxiv.org/abs/2305.01666