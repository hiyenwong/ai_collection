---
name: mesoscale-brain-organization
description: 脑组织中介尺度结构识别方法论。通过多分辨率技术提取脑连接网络的内聚结构。适用于脑网络模块化、社区检测。触发词：中介尺度、脑组织、模块化、mesoscale、community detection。
user-invocable: true
---

# Mesoscale Brain Organization

## 核心思想

使用多分辨率技术提取脑连接网络的内聚结构。

**来源：** arXiv:1312.6070
**效用：** 0.90

---

## 实现

```python
import numpy as np
import networkx as nx

def mesoscale_detection(fc, resolutions=[0.5, 1.0, 2.0]):
    G = nx.from_numpy_array(fc)
    return [nx.community.louvain_communities(G, resolution=g) for g in resolutions]
```

---

## Activation Keywords
- 中介尺度
- 脑组织
- 模块化

## Tools Used
- networkx
- numpy

## Instructions for Agents
1. 应用多分辨率阈值
2. 检测社区结构

## Examples
识别fMRI功能网络模块化。

## 参考文献
- arXiv:1312.6070