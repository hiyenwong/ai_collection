---
name: orthoreg-hybrid-symbolic-neural-dynamics
description: Orthogonal Regularization 方法论用于混合符号-神经动力系统，防止符号结构被神经网络残余吸收，实现互补分解
trigger_words:
  - hybrid modeling
  - symbolic neural
  - dynamical systems
  - orthogonal regularization
  - physics-informed
  - symbolic discovery
  - L2 regularization
  - projection argument
  - sparse discovery
  - mechanistic model
paper_id: arXiv:2606.19145
published: 2026-06-17
authors: Till Richter, Niki Kilbertus
---

# OrthoReg: Orthogonal Regularization for Hybrid Symbolic-Neural Dynamical Systems

## 核心问题

动力系统建模的持久困境：
- **符号模型**: 可解释但过于简化、误指定
- **神经方法**: 灵活但缺乏物理洞察

**混合建模的目标**: 结合两者的优势，但面临关键挑战：**神经网络可能重新学习符号部分**。

## 传统 L² 正则化的局限性

### 投影论证

标准 L² 正则化基于**投影论证**：
```
最小化 ||f_symbolic + f_neural||²
→ 约束 ||f_neural||²
```

### 核心问题

当符号结构通过**稀疏发现**从数据中学习时：
- L² 的投影论证**失效**
- 神络网络残余可能与符号结构**重叠**
- 导致**冗余且不可解释**的模型

**失败案例**: 
```python
# 传统方法
f_total = f_symbolic(discovered) + f_neural
# f_neural 可能学到 f_symbolic 已表达的部分
→ 冗余！不可解释！
```

## OrthoReg 核心创新

### 直接惩罚重叠

```python
# Orthogonal Regularization
loss = reconstruction_loss + λ * overlap_penalty

# overlap_penalty = ||⟨f_symbolic, f_neural⟩||²
# 直接测量两个组件的内积
```

### 互补分解保证

OrthoReg 确保：
- **符号部分**: 捕获库所能表达的
- **神经部分**: 捕获剩余部分
- **两者互补**: 不重叠，不冗余

## 数学框架

### 正交约束

设符号组件为 $\phi_s(x)$，神经组件为 $\phi_n(x)$：

$$
\text{OrthoReg} = \lambda \int \phi_s(x) \cdot \phi_n(x) dx
$$

### 优化目标

$$
\min_{\theta} \| \hat{y} - y \|^2 + \lambda \cdot \text{Overlap}(\phi_s, \phi_n)
$$

其中 Overlap 衡量符号与神经组件的重叠程度。

## 与 L² 正则化对比

| 方法 | 适用场景 | 稀疏发现时表现 |
|------|----------|----------------|
| L² 正则化 | 符号结构已知 | **失效（投影论证破坏）** |
| OrthoReg | 符号结构学习 | **有效（直接惩罚重叠）** |

### 关键区别

**L² 正则化**:
- 隐式假设符号结构固定
- 投影论证依赖固定基
- 稀疏发现时基变化 → 论证失效

**OrthoReg**:
- 直接测量符号-神经重叠
- 不依赖投影论证
- 稀疏发现时仍有效

## 实验结果

### 基准动力系统

在**部分库不匹配**场景下：

| 指标 | L² 正则化 | OrthoReg |
|------|-----------|----------|
| 符号恢复 | 低 | **高** |
| OOD 行为 | 不稳定 | **稳定** |
| 可解释性 | 低 | **高** |

### 关键发现

OrthoReg 在：
1. **符号发现**: 更准确地恢复物理结构
2. **分布外行为**: 更好的泛化能力
3. **模型可解释性**: 真正的互补分解

## 技术实现

### 正交性度量

```python
import torch

def orthoreg_loss(symbolic_output, neural_output):
    """
    计算符号与神经输出的正交性损失
    
    Args:
        symbolic_output: 符号模型输出
        neural_output: 神经网络残余输出
    
    Returns:
        overlap_penalty: 重叠惩罚
    """
    # 内积度量重叠
    overlap = torch.sum(symbolic_output * neural_output)
    
    # L² 形式的重叠惩罚
    overlap_penalty = overlap ** 2
    
    return overlap_penalty
```

### 训练流程

```python
class HybridDynamicalModel:
    def forward(self, x):
        # 符号组件（稀疏发现）
        symbolic = self.symbolic_library(x)
        
        # 神经残余
        residual = self.neural_net(x)
        
        # 组合输出
        return symbolic + residual
    
    def loss(self, pred, target, lambda_ortho=0.1):
        # 重构损失
        recon = F.mse_loss(pred, target)
        
        # 正交约束
        symbolic = self.symbolic_library(self.x)
        residual = self.neural_net(self.x)
        ortho = orthoreg_loss(symbolic, residual)
        
        return recon + lambda_ortho * ortho
```

## 应用场景

### 科学发现

- **物理定律发现**: 从数据中学习方程
- **生物系统建模**: 符号机制 + 神经修正
- **化学反应动力学**: 可解释的混合模型

### 工程应用

- **控制系统**: 符号控制律 + 神经自适应
- **机器人**: 物理模型 + 学习残余
- **气候建模**: 已知机制 + 学习偏差

## 理论基础

### 投影空间几何

- **符号基**: $\mathcal{B}_s = \{\phi_1, \phi_2, ..., \phi_n\}$（稀疏发现）
- **神经空间**: $\mathcal{N} = \text{span}(f_n)$
- **正交约束**: $\mathcal{B}_s \perp \mathcal{N}$

### 互补分解

$$
f_{total} = f_s + f_n
$$

其中：
- $f_s \in \text{span}(\mathcal{B}_s)$
- $f_n \perp \mathcal{B}_s$
- $\langle f_s, f_n \rangle = 0$

## 与相关方法对比

| 方法 | 符号发现支持 | 重叠预防 | 可解释性保证 |
|------|--------------|----------|--------------|
| SINDy | ✓ | 间接 | ✓ |
| L² 正则化 | ✗（投影失效） | ✗ | 低 |
| **OrthoReg** | ✓ | ✓ | ✓ |

## 参考文献

Till Richter, Niki Kilbertus. "OrthoReg: Orthogonal Regularization for Hybrid Symbolic-Neural Dynamical Systems." arXiv:2606.19145. 2026-06-17.

## Activation

- dynamical systems
- hybrid modeling
- symbolic neural
- orthogonal regularization
- physics-informed
- sparse discovery
- mechanistic learning