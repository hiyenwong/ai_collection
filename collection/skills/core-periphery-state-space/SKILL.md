---
name: core-periphery-state-space
description: '核心-边缘状态空间模型方法论。使用Mamba选择性状态空间模型线性复杂度捕获脑网络长程依赖，CP-MoE专家混合学习连接模式。适用于功能连接组分类、fMRI分析。触发词：核心-边缘、状态空间模型、Mamba、功能连接、core-periphery、state space model、fMRI classification。'
user-invocable: true
---

# Core-Periphery State Space Model - 核心-边缘状态空间模型

## 核心思想

结合 Mamba 选择性状态空间模型（线性复杂度）和核心-边缘组织原则，高效捕获功能脑网络长程依赖。

**来源：** arXiv:2503.14655
**效用：** 1.0

---

## 方法论

### 1. 核心问题

| 方法 | 问题 |
|------|------|
| 传统ML | 难捕获脑区间复杂关系 |
| Transformer | 二次复杂度，长序列计算困难 |

### 2. 解决方案

**CP-SSM = Mamba + CP-MoE**

- **Mamba：** 线性复杂度的选择性状态空间模型
- **CP-MoE：** 核心-边缘引导的专家混合

### 3. 实现框架

```python
import torch
import torch.nn as nn

class CPSSM(nn.Module):
    """Core-Periphery State Space Model"""
    
    def __init__(self, d_model=256, n_experts=8, d_state=16):
        super().__init__()
        
        # Mamba SSM 层
        self.ssm = MambaBlock(d_model, d_state)
        
        # CP-MoE 专家混合
        self.experts = nn.ModuleList([
            Expert(d_model) for _ in range(n_experts)
        ])
        self.gate = nn.Linear(d_model, n_experts)
        
        # 核心-边缘路由
        self.cp_router = CorePeripheryRouter(d_model)
    
    def forward(self, x):
        """
        x: (batch, seq_len, d_model)
        """
        # SSM 处理长程依赖
        x = self.ssm(x)
        
        # CP 路由决定专家权重
        cp_weights = self.cp_router(x)
        gate_weights = torch.softmax(self.gate(x), dim=-1)
        
        # 专家混合
        expert_outputs = torch.stack([e(x) for e in self.experts], dim=-1)
        combined = torch.sum(expert_outputs * gate_weights.unsqueeze(-2), dim=-1)
        
        return combined

class MambaBlock(nn.Module):
    """简化版 Mamba SSM"""
    
    def __init__(self, d_model, d_state):
        super().__init__()
        self.proj_in = nn.Linear(d_model, d_model * 2)
        self.proj_out = nn.Linear(d_model, d_model)
        
        # 状态空间参数
        self.A = nn.Parameter(torch.randn(d_model, d_state))
        self.B = nn.Parameter(torch.randn(d_model, d_state))
        self.C = nn.Parameter(torch.randn(d_model, d_state))
    
    def forward(self, x):
        # 选择性扫描（简化实现）
        h = torch.zeros(x.shape[0], x.shape[-1], self.A.shape[1], device=x.device)
        outputs = []
        
        for t in range(x.shape[1]):
            h = self.A @ h.T + self.B @ x[:, t].T
            y = self.C @ h
            outputs.append(y.T)
        
        return self.proj_out(torch.stack(outputs, dim=1))

class CorePeripheryRouter(nn.Module):
    """核心-边缘路由器"""
    
    def __init__(self, d_model):
        super().__init__()
        self.classifier = nn.Linear(d_model, 2)  # core vs periphery
    
    def forward(self, x):
        """识别核心/边缘节点"""
        return torch.softmax(self.classifier(x.mean(dim=1)), dim=-1)

class Expert(nn.Module):
    """单个专家网络"""
    
    def __init__(self, d_model):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(d_model, d_model * 2),
            nn.GELU(),
            nn.Linear(d_model * 2, d_model)
        )
    
    def forward(self, x):
        return self.fc(x)
```

---

## 应用场景

1. **功能连接组分类：** ABIDE、ADNI 数据集
2. **神经疾病诊断：** 自闭症、阿尔茨海默病
3. **脑网络分析：** 长程依赖建模

---

## 关键参数

| 参数 | 推荐值 |
|------|--------|
| d_model | 256 |
| n_experts | 8 |
| d_state | 16 |

---

## 性能对比

| 模型 | 复杂度 | 性能 |
|------|--------|------|
| Transformer | O(n²) | 基线 |
| CP-SSM | O(n) | 更优 |

---

## 参考文献

- arXiv:2503.14655 - Core-Periphery Principle Guided State Space Model
## Activation Keywords

- core-periphery-state-space
- core-periphery-state-space 技能
- core-periphery-state-space skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 功能连接组分类：

### Step 2: 神经疾病诊断：

### Step 3: 脑网络分析：

### Step 4: Understand the Request

### Step 5: Search for Information

## Examples

### Example 1: Basic Application

**User:** I need to apply Core-Periphery State Space Model - 核心-边缘状态空间模型 to my analysis.

**Agent:** I'll help you apply core-periphery-state-space. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for core-periphery-state-space?

**Agent:** Let me search for the latest research and best practices...
