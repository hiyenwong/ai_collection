---
name: modularity-graph-for-brain-functional-networks
description: **来源论文：** arXiv:2406.15155 - Introducing the modularity graph: an application to brain functional networks
---

# Modularity Graph for Brain Functional Networks

**来源论文：** arXiv:2406.15155 - Introducing the modularity graph: an application to brain functional networks
**效用评分：** 0.98
**创建时间：** 2026-03-24 14:03

---

## 概述

模态图（Modularity Graph）是一种新的图特征，用于突出图社区之间的关系。结合多尺度社区检测算法，应用于EEG运动想象实验的脑功能连接网络分析，识别不同认知状态下的连接模式。

## 激活关键词

- modularity graph
- brain functional network
- community detection multiscale
- EEG motor imagery
- graph community interaction
- connectivity state analysis
- 模态图
- 脑功能网络社区

## 核心概念

```
传统社区检测                模态图方法
┌─────────────────┐          ┌─────────────────┐
│ 单一尺度        │          │ 多尺度          │
│ 节点分配到社区  │  →       │ 社区间关系图    │
│ 忽略社区交互    │          │ 量化社区连接    │
└─────────────────┘          └─────────────────┘

模态图:
- 节点 = 原图的社区
- 边权重 = 社区间的连接强度
- 捕捉网络的高阶组织结构
```

## 核心方法

### 1. 模态图构建

```python
import numpy as np
import networkx as nx

class ModularityGraph:
    """
    模态图构建器
    
    将原图转换为以社区为节点的新图
    """
    def __init__(self, resolution=1.0):
        self.resolution = resolution
        self.communities = None
        self.modularity_graph = None
    
    def detect_communities(self, G, method='louvain', n_scales=5):
        """
        多尺度社区检测
        
        Args:
            G: 原图 (NetworkX Graph)
            method: 社区检测方法
            n_scales: 尺度数量
        
        Returns:
            communities: 多尺度社区划分
        """
        from community import best_partition
        
        communities = {}
        
        # 不同分辨率参数对应不同尺度
        resolutions = np.logspace(-1, 1, n_scales)
        
        for i, res in enumerate(resolutions):
            if method == 'louvain':
                partition = best_partition(G, resolution=res)
            
            communities[f'scale_{i}'] = partition
        
        self.communities = communities
        return communities
    
    def build_modularity_graph(self, G, partition):
        """
        构建模态图
        
        Args:
            G: 原图
            partition: 社区划分 {node: community_id}
        
        Returns:
            M: 模态图 (社区为节点)
        """
        # 获取社区列表
        community_ids = list(set(partition.values()))
        n_communities = len(community_ids)
        
        # 初始化模态图
        M = nx.Graph()
        M.add_nodes_from(community_ids)
        
        # 计算社区间的连接强度
        for u, v, data in G.edges(data=True):
            weight = data.get('weight', 1.0)
            
            comm_u = partition[u]
            comm_v = partition[v]
            
            if comm_u != comm_v:
                # 社区间连接
                if M.has_edge(comm_u, comm_v):
                    M[comm_u][comm_v]['weight'] += weight
                else:
                    M.add_edge(comm_u, comm_v, weight=weight)
        
        # 添加社区内部统计
        for comm in community_ids:
            nodes_in_comm = [n for n in partition if partition[n] == comm]
            
            # 社区大小
            M.nodes[comm]['size'] = len(nodes_in_comm)
            
            # 社区内部连接数
            internal_edges = G.subgraph(nodes_in_comm).number_of_edges()
            M.nodes[comm]['internal_edges'] = internal_edges
        
        self.modularity_graph = M
        return M
    
    def compute_inter_community_strength(self, G, partition):
        """
        计算社区间连接强度
        """
        strengths = {}
        
        for u, v in G.edges():
            comm_u = partition[u]
            comm_v = partition[v]
            
            if comm_u != comm_v:
                key = tuple(sorted([comm_u, comm_v]))
                strengths[key] = strengths.get(key, 0) + 1
        
        return strengths
```

### 2. 多尺度分析

```python
class MultiScaleModularityAnalysis:
    """
    多尺度模态图分析
    """
    def __init__(self, n_scales=5):
        self.n_scales = n_scales
        self.modularity_graphs = {}
    
    def analyze(self, G):
        """
        多尺度模态图分析
        
        Args:
            G: 原图
        
        Returns:
            分析结果
        """
        builder = ModularityGraph()
        
        # 多尺度社区检测
        communities = builder.detect_communities(G, n_scales=self.n_scales)
        
        # 为每个尺度构建模态图
        for scale_name, partition in communities.items():
            M = builder.build_modularity_graph(G, partition)
            self.modularity_graphs[scale_name] = M
        
        # 提取特征
        features = self.extract_multiscale_features()
        
        return features
    
    def extract_multiscale_features(self):
        """
        提取多尺度特征
        """
        features = {}
        
        for scale_name, M in self.modularity_graphs.items():
            # 社区数量
            n_communities = M.number_of_nodes()
            
            # 社区间连接数
            n_inter_edges = M.number_of_edges()
            
            # 平均社区大小
            avg_size = np.mean([M.nodes[n]['size'] for n in M.nodes()])
            
            # 模态图密度
            density = nx.density(M)
            
            # 模态图聚类系数
            clustering = nx.average_clustering(M)
            
            features[scale_name] = {
                'n_communities': n_communities,
                'n_inter_edges': n_inter_edges,
                'avg_community_size': avg_size,
                'density': density,
                'clustering': clustering
            }
        
        return features
```

### 3. EEG 脑功能网络应用

```python
import mne
from scipy import signal

class EEGFunctionalConnectivity:
    """
    EEG 功能连接网络构建
    """
    def __init__(self, n_channels=64, freq_bands=None):
        self.n_channels = n_channels
        self.freq_bands = freq_bands or {
            'delta': (0.5, 4),
            'theta': (4, 8),
            'alpha': (8, 13),
            'beta': (13, 30),
            'gamma': (30, 100)
        }
    
    def compute_connectivity(self, eeg_data, method='plv'):
        """
        计算功能连接矩阵
        
        Args:
            eeg_data: [n_channels, n_timepoints]
            method: 连接性度量方法
        
        Returns:
            connectivity: [n_channels, n_channels]
        """
        if method == 'plv':
            connectivity = self.phase_locking_value(eeg_data)
        elif method == 'coherence':
            connectivity = self.coherence(eeg_data)
        elif method == 'correlation':
            connectivity = np.corrcoef(eeg_data)
        
        return connectivity
    
    def phase_locking_value(self, eeg_data):
        """
        相位锁定值
        """
        n_channels = eeg_data.shape[0]
        plv = np.zeros((n_channels, n_channels))
        
        # Hilbert 变换获取相位
        phases = np.angle(signal.hilbert(eeg_data, axis=1))
        
        for i in range(n_channels):
            for j in range(i + 1, n_channels):
                # 相位差
                phase_diff = phases[i] - phases[j]
                
                # PLV
                plv[i, j] = np.abs(np.mean(np.exp(1j * phase_diff)))
                plv[j, i] = plv[i, j]
        
        return plv
    
    def coherence(self, eeg_data):
        """
        相干性
        """
        n_channels = eeg_data.shape[0]
        coh = np.zeros((n_channels, n_channels))
        
        for i in range(n_channels):
            for j in range(i + 1, n_channels):
                f, Cxy = signal.coherence(eeg_data[i], eeg_data[j])
                coh[i, j] = np.mean(Cxy)
                coh[j, i] = coh[i, j]
        
        return coh
    
    def build_network(self, connectivity, threshold=0.3):
        """
        从连接矩阵构建网络
        """
        G = nx.Graph()
        
        n = connectivity.shape[0]
        G.add_nodes_from(range(n))
        
        # 阈值化
        for i in range(n):
            for j in range(i + 1, n):
                if connectivity[i, j] > threshold:
                    G.add_edge(i, j, weight=connectivity[i, j])
        
        return G
```

### 4. 运动想象任务分析

```python
class MotorImageryModularityAnalysis:
    """
    运动想象任务的模态图分析
    """
    def __init__(self):
        self.fc_builder = EEGFunctionalConnectivity()
        self.modularity_analyzer = MultiScaleModularityAnalysis()
    
    def analyze_task_states(self, eeg_data, labels, task_names):
        """
        分析不同任务状态下的模态图差异
        
        Args:
            eeg_data: {task: [n_trials, n_channels, n_timepoints]}
            labels: 任务标签
            task_names: 任务名称列表
        
        Returns:
            任务特异性模态图特征
        """
        results = {}
        
        for task in task_names:
            task_data = eeg_data[task]
            
            # 平均功能连接
            all_connectivity = []
            for trial in task_data:
                fc = self.fc_builder.compute_connectivity(trial)
                all_connectivity.append(fc)
            
            mean_fc = np.mean(all_connectivity, axis=0)
            
            # 构建网络
            G = self.fc_builder.build_network(mean_fc)
            
            # 多尺度模态图分析
            features = self.modularity_analyzer.analyze(G)
            
            results[task] = features
        
        # 统计检验
        statistical_results = self.statistical_comparison(results)
        
        return results, statistical_results
    
    def statistical_comparison(self, results):
        """
        统计比较不同任务间的模态图差异
        """
        from scipy import stats
        
        comparison = {}
        
        # 获取所有尺度
        scales = list(results[list(results.keys())[0]].keys())
        
        for scale in scales:
            # 提取该尺度的特征
            scale_features = {}
            for task, task_results in results.items():
                scale_features[task] = task_results[scale]
            
            # ANOVA 检验
            for feature_name in ['n_communities', 'density', 'clustering']:
                values = [
                    scale_features[task][feature_name] 
                    for task in scale_features
                ]
                
                # 如果有多个被试，可以做 ANOVA
                # f_stat, p_value = stats.f_oneway(*values)
                
                comparison[f"{scale}_{feature_name}"] = {
                    'values': values,
                    'tasks': list(scale_features.keys())
                }
        
        return comparison
```

### 5. 模态图可视化

```python
import matplotlib.pyplot as plt

def visualize_modularity_graph(M, original_G, partition, title="Modularity Graph"):
    """
    可视化模态图和原图
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # 原图（着色社区）
    ax1 = axes[0]
    pos = nx.spring_layout(original_G)
    
    # 社区颜色
    communities = set(partition.values())
    colors = plt.cm.tab20(np.linspace(0, 1, len(communities)))
    color_map = {comm: colors[i] for i, comm in enumerate(communities)}
    
    node_colors = [color_map[partition[n]] for n in original_G.nodes()]
    
    nx.draw_networkx_nodes(original_G, pos, ax=ax1, 
                          node_color=node_colors, node_size=50)
    nx.draw_networkx_edges(original_G, pos, ax=ax1, alpha=0.3)
    ax1.set_title("Original Graph (colored by community)")
    ax1.axis('off')
    
    # 模态图
    ax2 = axes[1]
    pos_M = nx.spring_layout(M)
    
    # 节点大小 = 社区大小
    node_sizes = [M.nodes[n]['size'] * 10 for n in M.nodes()]
    
    # 边宽度 = 连接强度
    edge_weights = [M[u][v]['weight'] for u, v in M.edges()]
    max_weight = max(edge_weights) if edge_weights else 1
    edge_widths = [w / max_weight * 3 for w in edge_weights]
    
    nx.draw_networkx_nodes(M, pos_M, ax=ax2, 
                          node_size=node_sizes, node_color='lightblue')
    nx.draw_networkx_edges(M, pos_M, ax=ax2, width=edge_widths)
    nx.draw_networkx_labels(M, pos_M, ax=ax2)
    ax2.set_title(title)
    ax2.axis('off')
    
    plt.tight_layout()
    return fig
```

## 应用场景

1. **运动想象分类** - BCI 任务状态识别
2. **认知状态分析** - 不同认知任务的脑网络差异
3. **神经疾病诊断** - 异常社区组织检测
4. **网络重构** - 高阶网络结构分析

## 实验验证

论文使用公开 EEG 运动想象数据：
- **任务：** 左手/右手/脚部运动想象
- **数据：** 多被试 EEG 记录
- **发现：** 不同任务状态下模态图存在显著差异

## 关键发现

| 发现 | 描述 |
|------|------|
| 多尺度差异 | 不同尺度下社区组织不同 |
| 任务特异性 | 不同运动想象任务的模态图特征不同 |
| 社区交互 | 模态图揭示社区间连接模式 |

## 相关技能

- `weighted-brain-community-detection` - 加权脑社区检测
- `eeg-brain-connectivity-bci` - EEG 脑连接 BCI
- `core-periphery-state-space` - 核心-边缘状态空间
- `time-varying-brain-connectivity` - 时变脑连接

---

_此技能基于模态图方法，用于脑功能网络的多尺度社区分析_
## Description

Modularity Graph for Brain Functional Networks

## Activation Keywords

- modularity-graph-brain-network
- modularity-graph-brain-network 技能
- modularity-graph-brain-network skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 运动想象分类

### Step 2: 认知状态分析

### Step 3: 神经疾病诊断

### Step 4: 网络重构

### Step 5: Understand the Request

## Examples

### Example 1: Basic Application

**User:** I need to apply Modularity Graph for Brain Functional Networks to my analysis.

**Agent:** I'll help you apply modularity-graph-brain-network. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for modularity-graph-brain-network?

**Agent:** Let me search for the latest research and best practices...
