---
name: inexact-graph-matching-brain-networks
description: Inexact Graph Matching for Brain Networks
---

# Inexact Graph Matching for Brain Networks

## Description

基于图编辑距离的脑网络比较方法，用于解决个体化脑分割导致的网络对应问题，支持遗传性分析和个体差异追踪。

## Activation Keywords

- inexact graph matching
- brain graph comparison
- graph edit distance
- functional connectivity heritability
- individual brain network
- network correspondence

## Tools Used

- `read` - 读取脑网络数据
- `exec` - 运行 Python 图匹配脚本
- `web_fetch` - 获取论文详细内容

## Instructions for Agents

### 1. 理解问题背景

**个体化脑分割的挑战：**
- 数据驱动的脑分割能捕捉个体变异（发育、疾病）
- 但导致不同个体间的脑网络节点不对应
- 传统比较方法无法处理这种"不精确"匹配问题

**解决方案：**
- 使用图编辑距离（Graph Edit Distance）直接比较脑图
- 同时提供网络元素对应关系
- 保持局部功能连接变化的追踪能力

### 2. 技术方法

**图编辑距离（GED）：**
- 度量两个图之间的最小编辑成本
- 编辑操作：节点插入/删除/替换，边插入/删除
- 寻找最优对应关系

**应用于脑网络：**
```
输入：
- 图 G1: 个体 1 的功能连接网络（节点=脑区，边=连接强度）
- 图 G2: 个体 2 的功能连接网络

输出：
- 图编辑距离 d(G1, G2)
- 节点对应关系映射
```

### 3. 实现步骤

```python
# 1. 构建脑图
# 节点：脑区（来自个体化分割）
# 边：功能连接强度

# 2. 计算图编辑距离
import networkx as nx

def graph_edit_distance(G1, G2):
    # 定义编辑成本
    node_cost = 1.0  # 节点插入/删除成本
    edge_cost = 0.5  # 边插入/删除成本

    # 使用近似算法（精确 GED 是 NP-hard）
    from networkx.algorithms.similarity import optimal_edit_paths
    paths, cost = optimal_edit_paths(G1, G2)

    return cost, paths

# 3. 遗传性分析
# 计算同卵双胞胎 vs 异卵双胞胎的 GED 分布
# 使用统计检验评估遗传性
```

### 4. 应用场景

1. **遗传性分析** - 比较双胞胎的脑网络相似度
2. **疾病检测** - 追踪患者与对照的网络差异
3. **发育研究** - 监测个体脑网络变化

## Examples

### Example 1: 比较双胞胎的脑网络

```
User: 如何比较同卵双胞胎和异卵双胞胎的脑网络差异？

Agent: 使用 inexact-graph-matching-brain-networks 技能：

1. 对每对双胞胎计算图编辑距离
2. 分组统计：
   - MZ 组（同卵双胞胎）：GED 分布
   - DZ 组（异卵双胞胎）：GED 分布

3. 遗传性推断：
   - 如果 MZ 的 GED 显著小于 DZ，则表明功能网络有遗传性

arXiv:1703.10062 在 116 对双胞胎数据上验证了该方法：
- 发现功能连接模式具有显著的遗传性
- 网络对应关系可用于定位遗传影响的脑区
```

### Example 2: 个体化脑网络比较

```
User: 患者和健康对照的脑网络如何比较？

Agent: 使用图编辑距离方法：

1. 构建两组人群的脑图
2. 计算组内和组间的 GED
3. 识别最不匹配的节点/边

输出示例：
- 组间 GED 显著高于组内 GED
- 不匹配节点：前额叶皮层、扣带回
- 不匹配边：默认模式网络内部连接

这些差异可作为疾病生物标志物。
```

## Source

- **arXiv:** 1703.10062
- **效用:** 0.94
- **标题:** Exploring Heritability of Functional Brain Networks with Inexact Graph Matching
- **会议:** ISBI 2017

## Key Findings

1. **图编辑距离有效** - 能准确反映个体网络相似度
2. **遗传性证据** - 功能连接模式具有遗传基础
3. **对应关系** - 方法提供网络元素对应，支持局部变化追踪

## Related Skills

- `functional-connectome-fingerprint` - 功能连接指纹
- `brain-graph-augmentation-template` - 脑图增强模板
- `multimodal-brain-connectivity-gnn` - 多模态脑连接 GNN

## References

- Ktena et al. (2017) - 原始论文
- Human Connectome Project - 双胞胎数据集