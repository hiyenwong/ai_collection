---
name: griffiths-phase-brain-criticality
version: 1.0.0
description: |
  脑临界性的 Griffiths 相框架。扩展的临界区域解释个体变异，
  平衡鲁棒性与灵活性。结合结构网络模块性和区域异质性。
  触发词：脑临界性、Griffiths相、临界点、个体变异、鲁棒性与灵活性、
  brain criticality, Griffiths phase, critical point, individual variability。
---

# Griffiths Phase Brain Criticality

## 核心方法论

### 问题定义

**传统假设：** 大脑在单一临界点运作以实现最优性能

**挑战：** 无法解释神经动力学和认知功能的广泛个体变异

**解决方案：** Griffiths 相（GP）- 扩展的临界区域框架

---

## 关键概念

### 1. 脑临界性假说

**核心观点：** 大脑在临界点附近运作，实现最优信息处理

| 特性 | 临界态 | 亚临界态 | 超临界态 |
|------|--------|----------|----------|
| 信息传输 | 最优 | 局限 | 过度激活 |
| 稳定性 | 边缘 | 高 | 低 |
| 灵活性 | 高 | 低 | 高 |

### 2. Griffiths 相（GP）

**定义：** 由网络异质性协同诱导的扩展临界区域

**两种异质性：**
- **区域异质性：** 局部兴奋性差异
- **连接异质性：** 结构网络模块性

### 3. 鲁棒性-灵活性权衡

```
┌─────────────────────────────────────────────────────┐
│          Griffiths Phase 框架                       │
├─────────────────────────────────────────────────────┤
│                                                     │
│  结构网络模块性 + 区域兴奋性异质性                   │
│            ↓                                        │
│  协同作用 → Griffiths 相                           │
│            ↓                                        │
│  ┌─────────────────────────────────────┐           │
│  │  扩展的全局兴奋性范围               │           │
│  │  ┌───────────────┐                 │           │
│  │  │ 亚临界 │ GP │ 超临界 │         │           │
│  │  │  稳定   │ 最优 │ 灵活  │         │           │
│  │  └───────────────┘                 │           │
│  │      ↑ 最优点（平衡全局/局部传输）  │           │
│  └─────────────────────────────────────┘           │
│            ↓                                        │
│  个体化临界景观 → 独特认知特征                      │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 技术要点

### GP 特性

| 特性 | 说明 |
|------|------|
| **扩展范围** | 全局兴奋性范围广泛延伸 |
| **嵌入最优点** | 平衡全局/局部信息传输 |
| **个体特异性** | GP 内位置决定网络动力学 |
| **认知关联** | 功能连接配置决定认知特征 |

### 三种功能连接模式

| 模式 | 说明 | 认知功能 |
|------|------|----------|
| **分离** | 局部处理增强 | 专门化任务 |
| **整合** | 全局通信增强 | 复杂推理 |
| **平衡** | 分离与整合平衡 | 认知灵活性 |

---

## 应用场景

| 场景 | 说明 |
|------|------|
| **个体差异研究** | 解释认知功能变异 |
| **脑疾病诊断** | GP 位置偏移作为生物标志 |
| **脑网络建模** | 全脑动力学模拟 |
| **认知预测** | 从网络特征预测认知能力 |

---

## 数据验证

**Human Connectome Project 数据**

- 结构网络：DTI 纤维束追踪
- 功能连接：静息态 fMRI
- 认知测量：多维度认知测试

**发现：**
- GP 内位置与认知特征相关
- 个体化临界景观解释认知变异
- 鲁棒性-灵活性权衡的进化适应机制

---

## 技术实现

### 全脑建模

```python
import numpy as np

class GriffithsPhaseModel:
    def __init__(self, structural_network, regional_excitability):
        """
        structural_network: 结构连接矩阵
        regional_excitability: 区域兴奋性参数
        """
        self.A = structural_network
        self.h = regional_excitability
        
    def compute_gp_range(self):
        """
        计算 Griffiths 相范围
        """
        # 模块性计算
        modularity = compute_modularity(self.A)
        
        # 异质性度量
        heterogeneity = np.std(self.h)
        
        # GP 范围估计
        gp_range = self._estimate_gp_extent(modularity, heterogeneity)
        
        return gp_range
    
    def locate_in_gp(self, global_excitability):
        """
        定位全局兴奋性在 GP 中的位置
        """
        gp_range = self.compute_gp_range()
        
        # 归一化位置
        position = (global_excitability - gp_range[0]) / (gp_range[1] - gp_range[0])
        
        return np.clip(position, 0, 1)
    
    def predict_cognitive_profile(self, position):
        """
        预测认知特征
        """
        # 基于 GP 位置预测功能连接模式
        segregation = self._compute_segregation(position)
        integration = self._compute_integration(position)
        balance = segregation / (segregation + integration)
        
        return {
            'segregation': segregation,
            'integration': integration,
            'balance': balance
        }
```

---

## 与传统临界性框架对比

| 特性 | 传统临界点 | Griffiths 相 |
|------|------------|--------------|
| 假设 | 单一临界点 | 扩展临界区域 |
| 个体变异 | 视为噪声 | 核心特征 |
| 鲁棒性 | 低 | 高 |
| 解释力 | 有限 | 广泛 |

---

## 相关技能

- `time-varying-brain-connectivity` - 时变脑网络分析
- `weighted-brain-community-detection` - 加权脑网络社区检测

---

## 来源

- **论文：** Optimal Griffiths Phase in Heterogeneous Human Brain Networks: Brain Criticality Embracing Stability and Flexibility across Individuals
- **arXiv：** 2512.03409
- **效用评分：** 0.9
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
