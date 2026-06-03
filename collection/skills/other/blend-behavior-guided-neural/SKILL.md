---
name: blend-behavior-guided-neural
version: 1.0.0
description: |
  行为指导的神经种群动力学建模方法论（BLEND）。通过特权知识蒸馏，
  在训练时利用行为信号，推理时仅需神经活动。
  触发词：神经种群动力学、行为建模、知识蒸馏、特权信息、BLEND、
  neural population dynamics, behavior-guided, privileged distillation。
---

# BLEND: Behavior-guided Neural Population Dynamics

## 核心方法论

### 问题定义

**挑战：** 神经活动与行为联合建模需要复杂设计或过度简化假设。现实场景中，推理时往往只有神经活动数据，没有配对的行为数据。

**解决方案：** BLEND - 行为指导的神经种群动力学建模框架

---

## 关键概念

### 1. 特权知识蒸馏

**核心思想：** 将行为视为特权信息

| 阶段 | 输入 | 模型 |
|------|------|------|
| **训练** | 神经活动 + 行为 | Teacher 模型 |
| **推理** | 仅神经活动 | Student 模型 |

### 2. 框架特点

| 特点 | 说明 |
|------|------|
| **模型无关** | 可增强现有架构，无需从头设计 |
| **无强假设** | 不预设神经-行为的特定关系 |
| **灵活蒸馏** | 多种蒸馏策略可选 |

---

## 性能提升

| 任务 | 提升幅度 |
|------|----------|
| 行为解码 | >50% |
| 神经元身份预测 | >15% |

---

## 应用场景

| 场景 | 说明 |
|------|------|
| **行为解码** | 从神经活动预测行为 |
| **神经元身份预测** | 转录组神经元类型分类 |
| **神经假体** | 实时神经解码 |
| **脑机接口** | 意图解码 |

---

## 技术实现

### PyTorch 示例

```python
import torch
import torch.nn as nn

class BLENDTeacher(nn.Module):
    def __init__(self, neural_dim, behavior_dim, hidden_dim):
        super().__init__()
        self.neural_encoder = nn.Sequential(
            nn.Linear(neural_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        self.behavior_encoder = nn.Sequential(
            nn.Linear(behavior_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        self.fusion = nn.Linear(hidden_dim * 2, hidden_dim)
        
    def forward(self, neural, behavior):
        n_feat = self.neural_encoder(neural)
        b_feat = self.behavior_encoder(behavior)
        return self.fusion(torch.cat([n_feat, b_feat], dim=-1))

class BLENDStudent(nn.Module):
    def __init__(self, neural_dim, hidden_dim):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(neural_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
    def forward(self, neural):
        return self.encoder(neural)
```

---

## 与传统方法对比

| 方法 | 推理输入 | 模型设计 | 假设 |
|------|----------|----------|------|
| 联合建模 | 神经+行为 | 复杂 | 强 |
| 单独建模 | 仅神经 | 简单 | 弱 |
| **BLEND** | 仅神经 | 模型无关 | 无 |

---

## 相关技能

- `neuron-model-reconstruction` - 神经元模型重构
- `time-varying-brain-connectivity` - 时变脑网络分析

---

## 来源

- **论文：** BLEND: Behavior-guided Neural Population Dynamics Modeling via Privileged Knowledge Distillation
- **arXiv：** 2410.13872
- **会议：** ICLR 2025
- **效用评分：** 1.0
- **学习日期：** 2026-03-21
## Activation Keywords

- 脑网络分析
- 神经科学方法
- 计算神经科学
- 脑连接建模

## Tools Used

- **read**: Read skill documentation and references
- **exec**: Run analysis scripts and data processing
- **web_fetch**: Fetch papers and resources

## Instructions for Agents

1. Read the skill documentation carefully
2. Understand the methodology and key concepts
3. Apply the techniques to the specific problem
4. Document results and insights

## Examples

```python
# Example usage of the skill methodology
# Refer to the Technical Implementation section for details
```
