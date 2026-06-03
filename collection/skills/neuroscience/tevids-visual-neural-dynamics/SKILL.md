---
name: te-vids---time-evolving-visual-dynamical-system
description: **来源论文：** arXiv:2408.07908 - Time-Evolving Dynamical System for Learning Latent Representations of Mouse Visual Neural Activity
---

# TE-ViDS - Time-Evolving Visual Dynamical System

**来源论文：** arXiv:2408.07908 - Time-Evolving Dynamical System for Learning Latent Representations of Mouse Visual Neural Activity
**效用评分：** 0.97
**创建时间：** 2026-03-24 20:03
**会议：** NeurIPS 2025

## 概述

TE-ViDS 是一种序列潜在变量模型，将神经活动分解为随时间演化的低维潜在表示，专门用于处理自然视觉刺激下的视觉神经活动，结合对比学习提取可解释的潜在轨迹。

## 激活关键词

- TE-ViDS
- time-evolving dynamical system
- visual neural activity
- latent representation learning
- mouse visual cortex
- contrastive learning neural
- 时间演化动力学
- 视觉神经活动

## 核心架构

```
TE-ViDS 模型结构:
┌─────────────────────────────────────────┐
│         神经活动输入                      │
│    [时间序列, 神经元]                     │
└─────────────────────────────────────────┘
                ↓
┌─────────────────────────────────────────┐
│         潜在表示分解                      │
│  ┌───────────┐  ┌───────────┐           │
│  │ 刺激相关   │  │ 时间演化   │           │
│  │ 潜在变量   │  │ 潜在变量   │           │
│  └───────────┘  └───────────┘           │
└─────────────────────────────────────────┘
                ↓
┌─────────────────────────────────────────┐
│         对比学习对齐                      │
│    + 时间演化约束                         │
└─────────────────────────────────────────┘
                ↓
┌─────────────────────────────────────────┐
│         潜在轨迹输出                      │
│    可解释的神经动力学                     │
└─────────────────────────────────────────┘
```

## 核心方法

```python
import torch
import torch.nn as nn

class TEViDS(nn.Module):
    """
    Time-Evolving Visual Dynamical System
    """
    def __init__(self, n_neurons, latent_dim, hidden_dim=256):
        super().__init__()
        
        # 编码器：神经活动 → 潜在表示
        self.encoder = nn.Sequential(
            nn.Linear(n_neurons, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, latent_dim * 2)  # 分裂为两部分
        )
        
        # 时间演化模块
        self.time_evolution = nn.GRU(latent_dim, latent_dim, batch_first=True)
        
        # 解码器：潜在表示 → 神经活动重建
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, n_neurons)
        )
        
        # 对比学习投影头
        self.contrastive_head = nn.Sequential(
            nn.Linear(latent_dim, latent_dim),
            nn.ReLU(),
            nn.Linear(latent_dim, latent_dim)
        )
    
    def encode(self, neural_activity):
        """
        编码神经活动为潜在表示
        """
        z = self.encoder(neural_activity)
        z_stim, z_time = z.chunk(2, dim=-1)  # 分裂为两部分
        return z_stim, z_time
    
    def evolve(self, z_time):
        """
        时间演化潜在表示
        """
        z_evolved, _ = self.time_evolution(z_time.unsqueeze(1))
        return z_evolved.squeeze(1)
    
    def decode(self, z_stim, z_time):
        """
        解码潜在表示重建神经活动
        """
        z_combined = z_stim + z_time
        return self.decoder(z_combined)
```

## 应用场景

- 小鼠视觉皮层神经解码
- 自然场景/电影刺激响应分析
- 脑区视觉处理差异研究
- 神经动力学可视化

## 代码仓库

https://github.com/Grasshlw/Time-Evolving-Visual-Dynamical-System

## 相关技能

- `tavrnn-neural-dynamics`
- `benediff-behavior-neural-diffusion`
- `neural-dynamics-universal-translator`

---

_此技能用于视觉神经活动的时间演化潜在表示学习_
## Description

TE-ViDS - Time-Evolving Visual Dynamical System

## Activation Keywords

- tevids-visual-neural-dynamics
- tevids-visual-neural-dynamics 技能
- tevids-visual-neural-dynamics skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Understand the Request

### Step 2: Search for Information

### Step 3: Apply the Framework

### Step 4: Provide Results

### Step 5: Verify Accuracy

## Examples

### Example 1: Basic Application

**User:** I need to apply TE-ViDS - Time-Evolving Visual Dynamical System to my analysis.

**Agent:** I'll help you apply tevids-visual-neural-dynamics. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for tevids-visual-neural-dynamics?

**Agent:** Let me search for the latest research and best practices...
