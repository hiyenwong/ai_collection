# BACE - Behavior-Adaptive Connectivity Estimation

## Overview

行为自适应连接估计框架，从多区域颅内局部场电位 (LFP) 直接学习相位特定的有向脑区间连接。通过可学习邻接矩阵和预测目标，生成行为相位特异性的可解释连接图。

**来源论文：** arXiv:2510.20831 - BACE: Behavior-Adaptive Connectivity Estimation for Interpretable Graphs of Neural Dynamics

## 触发词

BACE、行为自适应连接、相位特异性连接、有向脑连接、LFP 连接分析、behavior-adaptive connectivity、phase-specific connectivity、interpretable neural dynamics

## 核心方法

### 框架架构

1. **区域时间编码器**：聚合每个解剖区域内的微触点
2. **相位特定邻接矩阵**：学习每个行为相位的连接模式
3. **预测目标训练**：端到端优化

### 关键特性

- **端到端学习**：直接从原始信号学习连接
- **相位特异性**：不同行为阶段有不同的连接模式
- **有向连接**：捕获因果性影响方向
- **可解释性**：输出显式邻接矩阵

## 使用场景

### 适用情况

- 颅内 LFP 多区域记录分析
- 行为任务中脑网络动态研究
- 运动控制神经机制
- 认知任务相位分析

### 数据要求

- 多区域同步 LFP 记录
- 行为事件标记（如 cued reaching）
- 时间分辨率足够捕获相位变化

## 实施步骤

1. **数据准备**
   - 按解剖区域组织 LFP 通道
   - 标记行为相位（准备、执行、反馈等）

2. **模型配置**
   - 定义区域时间编码器结构
   - 设置行为相位数量
   - 配置邻接矩阵约束

3. **训练**
   - 使用预测目标优化
   - 学习相位特定连接

4. **分析**
   - 提取各相位邻接矩阵
   - 分析行为对齐的重配置模式

## 技术细节

### 区域聚合

- 每个区域内的微触点通过时间编码器聚合
- 捕获区域级时间特征

### 相位特定邻接

- 每个行为相位独立邻接矩阵
- 参数共享或独立可配置

### 预测目标

- 时间序列预测
- 对比学习辅助

## 与其他方法对比

| 方法 | 有向连接 | 相位特异性 | 可解释性 |
|------|---------|-----------|---------|
| BACE | ✅ | ✅ | ✅ 显式矩阵 |
| 功能连接 | ❌ | ❌ | ⚠️ 相关性 |
| 有效连接 (GC) | ✅ | ❌ | ⚠️ 间接 |
| GNN | ❌ | ⚠️ | ❌ 隐式 |

## 工具使用

- `exec`: 运行 PyTorch 实现
- `read`: 查看配置文件
- `web_fetch`: 获取论文代码链接

## 注意事项

- 需要多区域同步记录
- 行为标记质量影响结果
- 相位划分需要领域知识

## 扩展阅读

- 相关技能：`task-aware-brain-connectivity`（任务感知连接）
- 相关技能：`gp-cake-brain-connectivity`（因果核方法）
- 论文链接：https://arxiv.org/abs/2510.20831
## Description

BACE - Behavior-Adaptive Connectivity Estimation

## Activation Keywords

- bace-behavior-adaptive-connectivity
- bace-behavior-adaptive-connectivity 技能
- bace-behavior-adaptive-connectivity skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 区域时间编码器

### Step 2: 相位特定邻接矩阵

### Step 3: 预测目标训练

### Step 4: 数据准备

### Step 5: 模型配置

## Examples

### Example 1: Basic Application

**User:** I need to apply BACE - Behavior-Adaptive Connectivity Estimation to my analysis.

**Agent:** I'll help you apply bace-behavior-adaptive-connectivity. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for bace-behavior-adaptive-connectivity?

**Agent:** Let me search for the latest research and best practices...
