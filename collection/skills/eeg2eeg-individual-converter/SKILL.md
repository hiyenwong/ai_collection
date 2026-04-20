---
name: eeg2eeg---individual-to-individual-eeg-converter
description: Skill for AI agent capabilities
---

# EEG2EEG - Individual-to-Individual EEG Converter

## Overview

个体到个体 EEG 转换器，使用生成模型将一个受试者的 EEG 信号转换为另一个受试者的 EEG 信号。解决认知和计算神经科学模型中的个体差异问题，实现跨个体神经表示映射。

**来源论文：** arXiv:2304.10736 - Generate your neural signals from mine: individual-to-individual EEG converters

## 触发词

EEG 转换器、个体间 EEG、EEG2EEG、跨个体 EEG、individual EEG converter、subject transfer EEG、EEG domain transfer

## 核心方法

### 挑战

- 训练于单个受试者的模型无法泛化到其他受试者
- 个体间神经表示差异大
- 数据稀缺问题

### 解决方案

**EEG2EEG 转换器**：
- 受计算机视觉生成模型启发
- 学习个体间 EEG 表示映射
- 生成目标受试者的 EEG 信号

### 验证

- THINGS EEG2 数据集
- 72 个独立模型（9 个受试者配对）
- 高转换性能
- 生成的 EEG 包含更清晰的视觉信息表示

## 使用场景

### 适用情况

- 跨受试者 EEG 分析
- 个体差异校正
- 数据增强
- 认知模型泛化

### 数据要求

- 多受试者 EEG 记录
- 相同任务/刺激条件
- 配对数据用于训练

## 实施步骤

1. **数据准备**
   - 收集多受试者 EEG
   - 对齐任务/刺激条件

2. **模型训练**
   - 设计生成模型架构
   - 学习源→目标映射

3. **转换生成**
   - 输入源受试者 EEG
   - 生成目标受试者 EEG

4. **评估验证**
   - 与真实 EEG 对比
   - 下游任务性能评估

## 技术细节

### 生成模型框架

- 编码器-解码器结构
- 条件生成
- 对抗训练（可选）

### 表示对齐

- 视觉信息保持
- 神经表示一致性

## 与其他方法对比

| 方法 | 个体迁移 | 数据增强 | 表示清晰度 |
|------|---------|---------|-----------|
| EEG2EEG | ✅ 直接转换 | ✅ | ✅ 更清晰 |
| 数据归一化 | ⚠️ 有限 | ❌ | — |
| 迁移学习 | ⚠️ 特征层 | ⚠️ | — |

## 工具使用

- `exec`: 运行 PyTorch 实现
- `read`: 查看 EEG 预处理配置
- `web_fetch`: 获取论文代码

## 注意事项

- 需要配对训练数据
- 转换质量依赖数据量
- 个体间差异程度影响效果

## 扩展阅读

- 相关技能：`eeg-foundation-model`（EEG 基础模型）
- 相关技能：`eeg-brain-connectivity-bci`（EEG BCI）
- 论文链接：https://arxiv.org/abs/2304.10736
## Description

EEG2EEG - Individual-to-Individual EEG Converter

## Activation Keywords

- eeg2eeg-individual-converter
- eeg2eeg-individual-converter 技能
- eeg2eeg-individual-converter skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 数据准备

### Step 2: 模型训练

### Step 3: 转换生成

### Step 4: 评估验证

### Step 5: Understand the Request

## Examples

### Example 1: Basic Application

**User:** I need to apply EEG2EEG - Individual-to-Individual EEG Converter to my analysis.

**Agent:** I'll help you apply eeg2eeg-individual-converter. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for eeg2eeg-individual-converter?

**Agent:** Let me search for the latest research and best practices...
