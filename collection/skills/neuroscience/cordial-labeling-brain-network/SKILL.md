---
name: cordial-labeling-brain-network
version: 1.0.0
description: |
  脑连接网络的 Cordial 标记技术。将图论标记方法应用于脑连接图，
  解释兴奋/抑制神经元的结构平衡。
  触发词：脑连接标记、Cordial标记、图论标记、网络平衡、cordial labeling、
  brain connectivity, graph labeling, excitatory-inhibitory balance。
---

# Cordial Labeling in Brain Connectivity Network

## 核心方法论

### 问题定义

**应用：** 将图论标记方法应用于脑连接图，刻画网络结构特征

**核心概念：** Cordial 标记作为兴奋/抑制神经元相互作用的结构平衡度量

---

## 关键概念

### 1. Cordial 标记

**定义：** 图的顶点标记，使得：
- 标记 0 和 1 的顶点数之差最多为 1
- 两端标记不同的边数与两端标记相同的边数之差最多为 1

**神经科学解释：**
| 标记 | 神经含义 |
|------|----------|
| 0 | 抑制性神经元 |
| 1 | 兴奋性神经元 |

### 2. Signed Product Cordial 标记

**定义：** 扩展标记方法，反映神经动力学的合作与对抗

**应用：**
- 合作性神经动力学（同步活动）
- 对抗性神经动力学（竞争活动）

### 3. 小世界网络关联

脑网络具有小世界特性，Cordial 标记揭示其结构平衡

---

## 技术要点

### 数学框架

```
G = (V, E)  脑连接图
f: V → {0, 1}  顶点标记

Cordial 条件：
|{v : f(v) = 0}| - |{v : f(v) = 1}| ≤ 1
|{e : f 端点不同}| - |{e : f 端点相同}| ≤ 1
```

### 神经网络解释

| 图论概念 | 神经科学含义 |
|----------|--------------|
| 顶点 | 神经元/脑区 |
| 边 | 突触连接 |
| 标记 0 | 抑制性 |
| 标记 1 | 兴奋性 |
| 边标记差 | 连接类型变化 |

---

## 应用场景

| 场景 | 说明 |
|------|------|
| **E/I 平衡分析** | 兴奋/抑制神经元比例 |
| **网络结构分类** | 区分正常/病理网络 |
| **连接模式研究** | 分析脑区连接特征 |
| **图论建模** | 神经网络图论分析 |

---

## 技术实现

### Python 示例

```python
import networkx as nx

def is_cordial_labeling(G, labeling):
    """
    检查是否为有效的 cordial 标记
    """
    # 检查顶点条件
    count_0 = sum(1 for v in G.nodes() if labeling[v] == 0)
    count_1 = sum(1 for v in G.nodes() if labeling[v] == 1)
    
    if abs(count_0 - count_1) > 1:
        return False
    
    # 检查边条件
    same_label = 0
    diff_label = 0
    
    for u, v in G.edges():
        if labeling[u] == labeling[v]:
            same_label += 1
        else:
            diff_label += 1
    
    return abs(same_label - diff_label) <= 1

def find_cordial_labeling(G):
    """
    寻找图的 cordial 标记
    """
    # 尝试所有可能的标记组合
    from itertools import product
    
    for labeling_tuple in product([0, 1], repeat=G.number_of_nodes()):
        labeling = dict(zip(G.nodes(), labeling_tuple))
        if is_cordial_labeling(G, labeling):
            return labeling
    
    return None  # 无 cordial 标记
```

### 脑网络应用

```python
def analyze_ei_balance(connectivity_matrix, labeling):
    """
    分析兴奋/抑制平衡
    """
    n_neurons = len(labeling)
    excitatory = sum(labeling.values())
    inhibitory = n_neurons - excitatory
    
    balance_ratio = excitatory / inhibitory if inhibitory > 0 else float('inf')
    
    return {
        'excitatory_count': excitatory,
        'inhibitory_count': inhibitory,
        'balance_ratio': balance_ratio
    }
```

---

## 相关技能

- `weighted-brain-community-detection` - 加权脑网络社区检测
- `gp-cake-brain-connectivity` - 因果核建模

---

## 来源

- **论文：** Exploring Cordial Labeling techniques in Brain Connectivity Network
- **arXiv：** 2511.05606
- **期刊：** Techniques-Sciences-methodes, vol 9, issue 11, (2025)
- **效用评分：** 0.9
- **学习日期：** 2026-03-21

## Activation Keywords

- 脑连接标记
- Cordial标记
- 图论标记
- 网络平衡
- cordial labeling

## Tools Used

- **read**: Read skill documentation
- **exec**: Run analysis scripts
- **web_fetch**: Fetch papers

## Instructions for Agents

1. Understand cordial labeling mathematical framework
2. Apply to brain connectivity graphs
3. Interpret results in neuroscience context
4. Document findings

## Examples

```python
# Example: Analyze brain network cordial labeling
G = nx.from_numpy_array(connectivity_matrix)
labeling = find_cordial_labeling(G)
balance = analyze_ei_balance(connectivity_matrix, labeling)
```