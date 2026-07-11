---
name: functional-proximity-law-multilayer
description: "Functional Proximity Law in Multilayer Networks: Hub importance scores persist more strongly between functionally similar layers. Validated across 17 pre-registered experiments including neuroscience (r=0.777 in C. elegans connectome). Activation: multilayer networks, functional proximity, hub importance, network layers, cross-layer similarity."
---

# 多层网络功能邻近定律

> 多层网络中，中心节点(hub)的重要性分数在功能相似的层之间比功能不同的层之间表现出更强的持续性，这一普适规律在17个预注册实验中得到验证。

## Metadata
- **Source**: arXiv:2604.23639
- **Authors**: Vladi Ivanov
- **Published**: 2026-04-26
- **Category**: Social and Information Networks (cs.SI)

## Core Methodology

### 功能邻近定律定义

**定律陈述**: 
> 多层网络中，中心节点的重要性分数在功能相似的层之间比功能不同的层之间持续得更强。

**形式化表达**:
```
对于层i和层j，中心节点重要性相关性：
Corr(hub_importance_i, hub_importance_j) = f(functional_similarity(i,j))

预测: f 是单调递增函数
```

### 实验设计

#### 预注册研究(17个实验)

| 类别 | 领域 | 验证状态 |
|------|------|----------|
| 规范域 | 分子生物学 | 确认 (9/12) |
| 规范域 | 神经科学 | 确认 |
| 规范域 | 计算机系统 | 确认 |
| 规范域 | 生态学 | 确认 |
| 规范域 | 语言学 | 确认 |
| 规范域 | 其他 | 3个被拒绝 |
| 外部验证 | C. elegans连接组 | 确认 (r=0.777, p=0.004) |

#### 被拒绝的域

3个被拒绝的规范域揭示了**命名结构边界条件**，缩小了定律适用范围。

### 统计验证

#### 规范域结果

- **8个域单独达到 p < 0.05**
- **方向性不等式在9个确认的域中全部成立**

#### C. elegans外部验证

- **数据**: 独立作者的连接组数据
- **层定义**: 独立于作者的定义
- **结果**: r = 0.777 (p = 0.004)

#### 显著性

- **14/17预注册确认的随机概率**: p ~ 0.006 (二项分布)
- **Bonferroni校正后仍显著**

## Implementation Guide

### 中心节点重要性计算

```python
import networkx as nx
import numpy as np

def compute_hub_importance(G, method='betweenness'):
    """
    计算单层网络中各节点的重要性
    
    参数:
        G: NetworkX图
        method: 'betweenness', 'degree', 'eigenvector', 'pagerank'
    
    返回:
        dict: {node: importance_score}
    """
    if method == 'betweenness':
        importance = nx.betweenness_centrality(G)
    elif method == 'degree':
        importance = dict(G.degree())
    elif method == 'eigenvector':
        importance = nx.eigenvector_centrality(G)
    elif method == 'pagerank':
        importance = nx.pagerank(G)
    else:
        raise ValueError(f"Unknown method: {method}")
    
    return importance


def compute_layer_similarity(layer1, layer2, similarity_metric='jaccard'):
    """
    计算两层之间的功能相似性
    
    参数:
        layer1, layer2: 层特征向量
        similarity_metric: 'jaccard', 'cosine', 'correlation'
    """
    if similarity_metric == 'jaccard':
        intersection = np.sum((layer1 > 0) & (layer2 > 0))
        union = np.sum((layer1 > 0) | (layer2 > 0))
        return intersection / union if union > 0 else 0
    elif similarity_metric == 'cosine':
        return np.dot(layer1, layer2) / (np.linalg.norm(layer1) * np.linalg.norm(layer2))
    elif similarity_metric == 'correlation':
        return np.corrcoef(layer1, layer2)[0, 1]
```

### 功能邻近定律检验

```python
def test_functional_proximity_law(multilayer_network, 
                                   functional_features,
                                   hub_method='betweenness'):
    """
    检验功能邻近定律
    
    参数:
        multilayer_network: dict {layer_name: nx.Graph}
        functional_features: dict {layer_name: feature_vector}
        hub_method: 中心节点重要性计算方法
    
    返回:
        dict: 检验结果
    """
    layers = list(multilayer_network.keys())
    n_layers = len(layers)
    
    # 1. 计算每层中心节点重要性
    hub_importance = {}
    for layer_name, G in multilayer_network.items():
        hub_importance[layer_name] = compute_hub_importance(G, hub_method)
    
    # 2. 构建重要性向量矩阵
    all_nodes = set()
    for G in multilayer_network.values():
        all_nodes.update(G.nodes())
    all_nodes = sorted(all_nodes)
    
    importance_matrix = np.zeros((n_layers, len(all_nodes)))
    for i, layer in enumerate(layers):
        for j, node in enumerate(all_nodes):
            importance_matrix[i, j] = hub_importance[layer].get(node, 0)
    
    # 3. 计算层间重要性相关性
    importance_corr = np.corrcoef(importance_matrix)
    
    # 4. 计算层间功能相似性
    n = len(layers)
    functional_sim = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                functional_sim[i, j] = compute_layer_similarity(
                    functional_features[layers[i]],
                    functional_features[layers[j]]
                )
    
    # 5. 检验定律：功能相似性 vs 重要性相关性
    correlations = []
    similarities = []
    
    for i in range(n):
        for j in range(i+1, n):
            correlations.append(importance_corr[i, j])
            similarities.append(functional_sim[i, j])
    
    # 6. 统计检验
    from scipy import stats
    
    # Spearman相关性（单调关系）
    spearman_r, spearman_p = stats.spearmanr(similarities, correlations)
    
    # Pearson相关性
    pearson_r, pearson_p = stats.pearsonr(similarities, correlations)
    
    # 方向性检验
    directional_test = np.sum(np.array(correlations) > 0) / len(correlations)
    
    return {
        'spearman_r': spearman_r,
        'spearman_p': spearman_p,
        'pearson_r': pearson_r,
        'pearson_p': pearson_p,
        'directional_consistency': directional_test,
        'layer_pairs': len(correlations),
        'importance_matrix': importance_matrix,
        'functional_sim_matrix': functional_sim
    }
```

### 神经科学应用：C. elegans连接组

```python
# C. elegans连接组分析示例

def analyze_celegans_multilayer():
    """
    秀丽隐杆线虫多层网络分析
    
    层定义示例:
    - 化学突触层
    - 电突触(间隙连接)层
    - 神经调质层
    """
    # 加载连接组数据
    chem_syn = load_celegans_chemical_synapses()
    gap_junction = load_celegans_gap_junctions()
    neuromod = load_celegans_neuromodulation()
    
    multilayer = {
        'chemical': chem_syn,
        'gap_junction': gap_junction,
        'neuromodulator': neuromod
    }
    
    # 功能特征定义
    # 例如：神经递质类型分布
    functional_features = {
        'chemical': compute_neurotransmitter_profile(chem_syn),
        'gap_junction': compute_electrical_coupling_profile(gap_junction),
        'neuromodulator': compute_modulator_profile(neuromod)
    }
    
    # 检验定律
    results = test_functional_proximity_law(
        multilayer, 
        functional_features
    )
    
    print(f"C. elegans验证结果:")
    print(f"  Spearman r = {results['spearman_r']:.3f}")
    print(f"  p-value = {results['spearman_p']:.4f}")
    
    return results
```

## Applications

- **脑网络多模态整合**: fMRI、DTI、MEG等多模态脑网络的跨层分析
- **社交网络跨平台**: 不同社交平台用户影响力的跨层一致性
- **生物分子网络**: 基因、蛋白质、代谢物多层网络的中心节点分析
- **计算机网络**: 不同协议层的节点重要性相关性

## Pitfalls

- **层定义敏感性**: 功能相似性的定义方式影响结果
- **节点对齐**: 跨层节点对应关系的确定可能困难
- **网络大小**: 不同层节点数不同时需要特殊处理
- **边界条件**: 某些网络类型(被拒绝的3个域)不适用

## Related Skills

- brain-connectivity-analysis
- hermes-brain-connectivity
- higher-order-brain-networks
- dgcl-brain-network-construction
