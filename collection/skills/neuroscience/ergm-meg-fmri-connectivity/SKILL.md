---
name: meg-fmri-exponential-random-graph-modeling
description: **来源论文：** arXiv:1805.12005 - Combined MEG and fMRI Exponential Random Graph Modeling for inferring functional Brain Connectivity
---

# MEG-fMRI Exponential Random Graph Modeling

**来源论文：** arXiv:1805.12005 - Combined MEG and fMRI Exponential Random Graph Modeling for inferring functional Brain Connectivity
**效用评分：** 0.99
**创建时间：** 2026-03-24 10:03

---

## 概述

使用指数随机图模型（ERGM）结合 MEG 和 fMRI 神经影像数据，推断功能性脑连接网络。该方法能够捕捉功能分离和功能整合等重要脑属性。

## 激活关键词

- ERGM brain connectivity
- exponential random graph
- MEG fMRI fusion
- functional connectome modeling
- network statistical model
- small world brain
- 指数随机图模型
- 功能连接组建模

## 核心方法

### 指数随机图模型（ERGM）

```
传统相关性分析                ERGM 建模
┌─────────────────┐          ┌─────────────────┐
│ 单一连接矩阵    │          │ 统计网络模型    │
│ 静态快照        │  →       │ 生成过程建模    │
│ 噪声敏感        │          │ 网络属性推断    │
└─────────────────┘          └─────────────────┘

ERGM 核心公式:
P(Y=y) ∝ exp(θᵀg(y))

其中:
- Y: 随机图
- y: 观察到的网络
- θ: 模型参数
- g(y): 网络统计量
```

## 实现步骤

### 1. 数据准备

```python
import numpy as np
import networkx as nx

def prepare_multimodal_data(meg_data, fmri_data, atlas):
    """
    准备 MEG 和 fMRI 多模态数据
    
    Args:
        meg_data: MEG 时间序列 [n_timepoints, n_sensors]
        fmri_data: fMRI 时间序列 [n_timepoints, n_rois]
        atlas: 脑区划分
    
    Returns:
        合并的功能连接矩阵
    """
    # MEG 源定位到脑区
    meg_source = source_localization(meg_data, atlas)
    
    # 计算功能连接
    meg_fc = compute_functional_connectivity(meg_source)
    fmri_fc = compute_functional_connectivity(fmri_data)
    
    # 多模态融合
    combined_fc = fuse_multimodal_fc(meg_fc, fmri_fc)
    
    return combined_fc

def compute_functional_connectivity(timeseries):
    """
    计算功能连接矩阵
    """
    # Pearson 相关
    fc = np.corrcoef(timeseries.T)
    
    # Fisher Z 变换
    fc_z = 0.5 * np.log((1 + fc) / (1 - fc + 1e-6))
    
    return fc_z

def fuse_multimodal_fc(meg_fc, fmri_fc, weight=0.5):
    """
    融合 MEG 和 fMRI 功能连接
    """
    # 加权平均
    combined = weight * meg_fc + (1 - weight) * fmri_fc
    
    return combined
```

### 2. 构建 ERGM 模型

```python
from scipy.special import logsumexp
import random

class BrainERGM:
    """
    脑网络指数随机图模型
    """
    def __init__(self, n_nodes, statistics_funcs):
        self.n_nodes = n_nodes
        self.statistics = statistics_funcs
        self.theta = np.zeros(len(statistics_funcs))
        
    def compute_statistics(self, G):
        """
        计算网络统计量
        """
        stats = []
        for func in self.statistics:
            stats.append(func(G))
        return np.array(stats)
    
    def log_likelihood(self, G):
        """
        计算对数似然
        """
        stats = self.compute_statistics(G)
        return np.dot(self.theta, stats)
    
    def fit(self, observed_networks, n_iterations=1000, learning_rate=0.01):
        """
        使用 MCMC 拟合模型参数
        
        Args:
            observed_networks: 观察到的网络列表
            n_iterations: 迭代次数
            learning_rate: 学习率
        """
        for iteration in range(n_iterations):
            # 计算观察网络的期望统计量
            observed_stats = np.mean([
                self.compute_statistics(G) 
                for G in observed_networks
            ], axis=0)
            
            # 生成模拟网络
            simulated_networks = self.simulate_networks(n_networks=100)
            simulated_stats = np.mean([
                self.compute_statistics(G) 
                for G in simulated_networks
            ], axis=0)
            
            # 更新参数（梯度上升）
            gradient = observed_stats - simulated_stats
            self.theta += learning_rate * gradient
            
            if iteration % 100 == 0:
                print(f"Iteration {iteration}: Δ = {np.linalg.norm(gradient):.4f}")
        
        return self.theta
    
    def simulate_networks(self, n_networks=1):
        """
        从模型生成网络样本
        """
        networks = []
        
        for _ in range(n_networks):
            G = self.mcmc_sample()
            networks.append(G)
        
        return networks
    
    def mcmc_sample(self, n_steps=1000, burn_in=500):
        """
        MCMC 采样生成网络
        """
        # 初始化随机网络
        G = nx.erdos_renyi_graph(self.n_nodes, 0.3)
        current_log_lik = self.log_likelihood(G)
        
        for step in range(n_steps + burn_in):
            # 提议：随机翻转一条边
            G_new = G.copy()
            i, j = random.sample(range(self.n_nodes), 2)
            
            if G_new.has_edge(i, j):
                G_new.remove_edge(i, j)
            else:
                G_new.add_edge(i, j)
            
            # 计算接受概率
            new_log_lik = self.log_likelihood(G_new)
            log_ratio = new_log_lik - current_log_lik
            
            if np.log(random.random()) < log_ratio:
                G = G_new
                current_log_lik = new_log_lik
        
        return G
```

### 3. 定义脑网络统计量

```python
def edge_count(G):
    """边数量"""
    return G.number_of_edges()

def density(G):
    """网络密度"""
    return nx.density(G)

def triangles(G):
    """三角形数量（聚类）"""
    return sum(nx.triangles(G).values()) / 3

def small_world_coefficient(G):
    """小世界系数"""
    # 聚类系数
    C = nx.average_clustering(G)
    
    # 平均路径长度
    if nx.is_connected(G):
        L = nx.average_shortest_path_length(G)
    else:
        L = float('inf')
    
    # 随机网络参考值
    n = G.number_of_nodes()
    m = G.number_of_edges()
    C_rand = m / (n * (n - 1) / 2)
    L_rand = np.log(n) / np.log(2 * m / n)
    
    # 小世界系数
    sigma = (C / C_rand) / (L / L_rand) if L_rand > 0 else 0
    
    return sigma

def modularity(G):
    """模块化系数"""
    communities = nx.community.greedy_modularity_communities(G)
    return nx.community.modularity(G, communities)

def global_efficiency(G):
    """全局效率（功能整合）"""
    return nx.global_efficiency(G)

def local_efficiency(G):
    """局部效率（功能分离）"""
    return nx.local_efficiency(G)

# 标准统计量集合
BRAIN_NETWORK_STATISTICS = [
    edge_count,
    density,
    triangles,
    small_world_coefficient,
    modularity,
    global_efficiency,
    local_efficiency
]
```

### 4. 组级分析

```python
def pooled_ergm_analysis(subject_networks, conditions):
    """
    池化 ERGM 分析
    
    Args:
        subject_networks: {subject_id: {condition: network}}
        conditions: 实验条件列表
    
    Returns:
        组级 ERGM 参数和比较结果
    """
    results = {}
    
    # 为每个条件拟合池化 ERGM
    for condition in conditions:
        # 收集所有被试的网络
        condition_networks = []
        for subject_id in subject_networks:
            condition_networks.append(subject_networks[subject_id][condition])
        
        # 拟合 ERGM
        ergm = BrainERGM(
            n_nodes=condition_networks[0].number_of_nodes(),
            statistics_funcs=BRAIN_NETWORK_STATISTICS
        )
        theta = ergm.fit(condition_networks)
        
        results[condition] = {
            'theta': theta,
            'ergm': ergm
        }
    
    # 条件间比较
    comparison = compare_conditions(results, conditions)
    
    return results, comparison

def compare_conditions(results, conditions):
    """
    比较不同条件下的 ERGM 参数
    """
    from scipy import stats
    
    comparisons = {}
    
    for i, cond1 in enumerate(conditions):
        for cond2 in conditions[i+1:]:
            # 统计检验
            theta1 = results[cond1]['theta']
            theta2 = results[cond2]['theta']
            
            # 参数差异
            diff = theta1 - theta2
            
            # 显著性检验（需要多个样本）
            # t_stat, p_value = stats.ttest_ind(...)
            
            comparisons[f"{cond1}_vs_{cond2}"] = {
                'theta_diff': diff,
                'significant': np.abs(diff) > 0.5  # 阈值
            }
    
    return comparisons
```

### 5. 网络属性验证

```python
def validate_ergm_model(ergm, observed_networks):
    """
    验证 ERGM 模型是否重现重要脑网络属性
    """
    # 观察网络的统计量
    observed_stats = np.mean([
        ergm.compute_statistics(G) 
        for G in observed_networks
    ], axis=0)
    
    # 模拟网络的统计量
    simulated = ergm.simulate_networks(n_networks=100)
    simulated_stats = np.mean([
        ergm.compute_statistics(G) 
        for G in simulated
    ], axis=0)
    
    # 比较统计量
    stat_names = ['edges', 'density', 'triangles', 'small_world', 
                   'modularity', 'global_eff', 'local_eff']
    
    comparison = {}
    for i, name in enumerate(stat_names):
        comparison[name] = {
            'observed': observed_stats[i],
            'simulated': simulated_stats[i],
            'ratio': simulated_stats[i] / (observed_stats[i] + 1e-6)
        }
    
    return comparison
```

## 应用场景

1. **脑连接推断** - 从噪声数据推断真实连接
2. **组级比较** - 不同实验条件的网络差异
3. **网络生成** - 生成符合脑属性的随机网络
4. **属性验证** - 检验功能分离和整合

## 实验数据

论文使用 n-back 记忆任务数据：
- **模态：** MEG + fMRI
- **被试：** 9 名（从 32 名中筛选）
- **条件：** 0-back vs 2-back
- **发现：** 功能连接具有小世界属性

## 关键发现

- 小世界属性：所有功能连接网络都表现出小世界特性
- 功能分离 vs 整合：ERGM 成功重现这两个重要属性
- 条件区分：功能分离模型能区分 0-back 和 2-back 条件
- 多模态融合：MEG+fMRI 提供更完整的连接估计

## 相关技能

- `multimodal-brain-connectivity-gnn` - 多模态脑连接
- `graph-laplacian-denoising` - 图拉普拉斯去噪
- `brain-higher-order-structures` - 脑高阶结构
- `weighted-brain-community-detection` - 加权脑社区检测

---

_此技能基于 ERGM 方法，用于结合 MEG 和 fMRI 推断功能性脑连接_
## Description

MEG-fMRI Exponential Random Graph Modeling

## Activation Keywords

- ergm-meg-fmri-connectivity
- ergm-meg-fmri-connectivity 技能
- ergm-meg-fmri-connectivity skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 脑连接推断

### Step 2: 组级比较

### Step 3: 网络生成

### Step 4: 属性验证

### Step 5: Understand the Request

## Examples

### Example 1: Basic Application

**User:** I need to apply MEG-fMRI Exponential Random Graph Modeling to my analysis.

**Agent:** I'll help you apply ergm-meg-fmri-connectivity. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for ergm-meg-fmri-connectivity?

**Agent:** Let me search for the latest research and best practices...
