---
name: brain-higher-order-structures
description: 脑网络高阶结构分析方法论。使用单纯复形和持续同调研究功能脑网络中的高阶交互（四节点以上），解释为何常规分析难以检测复杂高阶结构。触发词：高阶结构、持续同调、单纯复形、脑网络拓扑、higher-order interactions、persistent homology、simplicial complex。
user-invocable: true
---

# 脑网络高阶结构分析

基于 arXiv:2503.14700 - "From Density to Void: Brain Networks and Higher-Order Structures"

## 核心方法论

### 1. 单纯复形框架

```python
import numpy as np
from scipy.spatial.distance import pdist, squareform
from itertools import combinations

class SimplicialComplex:
    """
    单纯复形构建器
    用于将脑网络转换为拓扑结构
    """
    
    def __init__(self):
        self.simplices = {0: [], 1: [], 2: [], 3: [], 4: []}
        self.filtration_values = {}
    
    def add_simplex(self, vertices, filtration_value=0):
        """添加单纯形"""
        dim = len(vertices) - 1
        if dim not in self.simplices:
            self.simplices[dim] = []
        simplex = tuple(sorted(vertices))
        if simplex not in self.simplices[dim]:
            self.simplices[dim].append(simplex)
            self.filtration_values[simplex] = filtration_value
    
    def build_from_correlation_matrix(self, corr_matrix, threshold_range=None):
        """
        从功能连接矩阵构建单纯复形
        
        参数:
            corr_matrix: 功能连接矩阵 (N x N)
            threshold_range: 持续同调的阈值范围
        """
        n_nodes = corr_matrix.shape[0]
        
        if threshold_range is None:
            threshold_range = np.linspace(0.1, 0.9, 50)
        
        # 将相关系数转换为距离
        distance_matrix = 1 - np.abs(corr_matrix)
        
        for threshold in threshold_range:
            # 构建Vietoris-Rips复形
            edges = np.where(np.triu(distance_matrix < threshold, k=1))
            
            for i, j in zip(edges[0], edges[1]):
                self.add_simplex((i, j), threshold)
            
            # 构建高维单纯形
            self._build_higher_simplices(threshold)
        
        return self
    
    def _build_higher_simplices(self, threshold):
        """构建高维单纯形（三角形、四面体等）"""
        # 2-单纯形（三角形）
        for t in combinations(range(len(self.simplices.get(0, []))), 3):
            edges = [(t[0], t[1]), (t[0], t[2]), (t[1], t[2])]
            if all(e in self.simplices[1] for e in edges):
                self.add_simplex(t, threshold)
        
        # 3-单纯形（四面体）
        for t in combinations(range(len(self.simplices.get(0, []))), 4):
            faces = list(combinations(t, 3))
            if all(f in self.simplices[2] for f in faces):
                self.add_simplex(t, threshold)
        
        # 4-单纯形及以上
        for dim in range(4, 5):
            if len(self.simplices.get(dim-1, [])) > 0:
                for t in combinations(range(len(self.simplices.get(0, []))), dim+1):
                    faces = list(combinations(t, dim))
                    if all(f in self.simplices.get(dim-1, []) for f in faces):
                        self.add_simplex(t, threshold)


def compute_betti_numbers(simplex_complex, max_dim=4):
    """
    计算Betti数
    
    Betti_k = k维空洞数量
    - Betti_0: 连通分量数
    - Betti_1: 独立环数
    - Betti_2: 空腔数
    - ...
    """
    betti = {k: 0 for k in range(max_dim + 1)}
    
    # 简化计算（实际应使用GUDHI或Ripser库）
    # Betti_0 = 连通分量数
    edges = simplex_complex.simplices.get(1, [])
    nodes = set()
    for e in edges:
        nodes.add(e[0])
        nodes.add(e[1])
    
    # 使用并查集计算连通分量
    parent = {n: n for n in nodes}
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    for e in edges:
        px, py = find(e[0]), find(e[1])
        if px != py:
            parent[px] = py
    
    components = len(set(find(n) for n in nodes))
    betti[0] = components
    
    # Betti_1 简化估计
    n_edges = len(edges)
    n_nodes = len(nodes)
    # Euler特征: chi = n_nodes - n_edges + n_triangles
    n_triangles = len(simplex_complex.simplices.get(2, []))
    chi = n_nodes - n_edges + n_triangles
    
    # Betti_1 ≈ n_edges - n_nodes + n_triangles + Betti_0
    betti[1] = max(0, n_edges - n_nodes + n_triangles + betti[0] - components)
    
    return betti
```

### 2. 持续同调分析

```python
import numpy as np

class PersistenceDiagram:
    """
    持续图分析
    记录拓扑特征的出现和消失
    """
    
    def __init__(self):
        self.points = []  # [(birth, death, dim), ...]
    
    def add_point(self, birth, death, dim):
        """添加持久点"""
        self.points.append((birth, death, dim))
    
    def compute_persistence_landscape(self, resolution=100):
        """
        计算持久图景观
        
        用于统计比较和机器学习
        """
        max_val = max(p[1] if p[1] < float('inf') else p[0] for p in self.points)
        t = np.linspace(0, max_val, resolution)
        
        landscapes = {}
        for dim in set(p[2] for p in self.points):
            dim_points = [(p[0], p[1]) for p in self.points if p[2] == dim]
            landscape = np.zeros(resolution)
            
            for birth, death in dim_points:
                if death == float('inf'):
                    death = max_val
                for i, ti in enumerate(t):
                    if birth <= ti <= death:
                        landscape[i] += min(ti - birth, death - ti)
            
            landscapes[dim] = landscape
        
        return t, landscapes
    
    def compute_statistics(self):
        """计算持久性统计量"""
        stats = {}
        
        for dim in set(p[2] for p in self.points):
            dim_points = [(p[0], p[1]) for p in self.points if p[2] == dim]
            persistences = [d - b for b, d in dim_points if d < float('inf')]
            
            if persistences:
                stats[dim] = {
                    'n_features': len(dim_points),
                    'mean_persistence': np.mean(persistences),
                    'max_persistence': np.max(persistences),
                    'total_persistence': np.sum(persistences)
                }
        
        return stats


def analyze_higher_order_interactions(fmri_data, n_timepoints, n_nodes, 
                                       threshold_method='percentile'):
    """
    分析功能脑网络中的高阶交互
    
    参数:
        fmri_data: fMRI时间序列 (n_timepoints x n_nodes)
        threshold_method: 阈值方法 ('percentile', 'absolute', 'adaptive')
    
    返回:
        - 高阶交互检测结果
        - 为何难以检测的解释
    """
    # 计算功能连接
    corr_matrix = np.corrcoef(fmri_data.T)
    
    # 构建单纯复形
    sc = SimplicialComplex()
    
    # 根据阈值方法确定阈值范围
    if threshold_method == 'percentile':
        thresholds = np.percentile(np.abs(corr_matrix[np.triu_indices(n_nodes, k=1)]),
                                   np.linspace(90, 99, 10))
    elif threshold_method == 'absolute':
        thresholds = np.linspace(0.3, 0.9, 10)
    else:  # adaptive
        thresholds = np.linspace(np.min(np.abs(corr_matrix)) + 0.1,
                                 np.max(np.abs(corr_matrix)) - 0.1, 10)
    
    # 在不同阈值下构建复形
    results = []
    for threshold in thresholds:
        # 应用阈值
        adj = np.abs(corr_matrix) > threshold
        
        # 计算不同维度单纯形的数量
        n_nodes = adj.shape[0]
        n_edges = np.sum(np.triu(adj, k=1))
        
        # 统计高阶单纯形
        n_triangles = 0
        n_tetrahedra = 0
        n_4_simplices = 0
        
        for i in range(n_nodes):
            for j in range(i+1, n_nodes):
                for k in range(j+1, n_nodes):
                    if adj[i,j] and adj[i,k] and adj[j,k]:
                        n_triangles += 1
                        for l in range(k+1, n_nodes):
                            if (adj[i,l] and adj[j,l] and adj[k,l]):
                                n_tetrahedra += 1
                                for m in range(l+1, n_nodes):
                                    if (adj[i,m] and adj[j,m] and 
                                        adj[k,m] and adj[l,m]):
                                        n_4_simplices += 1
        
        results.append({
            'threshold': threshold,
            'n_edges': n_edges,
            'n_triangles': n_triangles,
            'n_tetrahedra': n_tetrahedra,
            'n_4_simplices': n_4_simplices,
            'ratio_2_to_1': n_triangles / max(n_edges, 1),
            'ratio_3_to_2': n_tetrahedra / max(n_triangles, 1),
            'ratio_4_to_3': n_4_simplices / max(n_tetrahedra, 1)
        })
    
    return results


def explain_detection_failure(results):
    """
    解释为何高阶结构难以检测
    
    基于"From Density to Void"论文的核心发现
    """
    explanation = """
    高阶交互难以检测的原因：
    
    1. **稀疏性递减**：
       - 随着维度增加，单纯形数量急剧减少
       - 边 → 三角形 → 四面体 → 4-单纯形 呈指数衰减
    
    2. **阈值敏感性**：
       - 高阶结构对连接阈值极其敏感
       - 阈值变化微小可能导致高阶结构完全消失
    
    3. **时间不稳定性**：
       - 功能连接随时间波动
       - 高阶结构需要多个连接同时稳定存在
       - 概率上难以维持
    
    4. **噪声放大**：
       - 高阶结构检测需要多个低阶结构同时存在
       - 噪声逐级放大
    
    5. **维度灾难**：
       - 检测k阶结构需要O(N^k)的计算量
       - 样本量相对维度严重不足
    """
    
    # 从实际结果中提取证据
    if results:
        avg_ratios = {
            'edge_to_triangle': np.mean([r['ratio_2_to_1'] for r in results]),
            'triangle_to_tetra': np.mean([r['ratio_3_to_2'] for r in results]),
            'tetra_to_4simplex': np.mean([r['ratio_4_to_3'] for r in results])
        }
        
        evidence = f"""
        实际数据证据：
        - 边/三角形比例：{avg_ratios['edge_to_triangle']:.4f}
        - 三角形/四面体比例：{avg_ratios['triangle_to_tetra']:.4f}
        - 四面体/4-单纯形比例：{avg_ratios['tetra_to_4simplex']:.4f}
        
        维度每增加1，结构数量减少约一个数量级。
        """
        
        return explanation + evidence
    
    return explanation
```

### 3. 空洞与空腔分析

```python
def detect_voids_in_brain_network(corr_matrix, min_size=4, max_size=6):
    """
    检测脑网络中的空洞（void）
    
    空洞：节点间存在连接，但缺少高阶交互形成的"中空"结构
    """
    n_nodes = corr_matrix.shape[0]
    distance_matrix = 1 - np.abs(corr_matrix)
    
    voids = []
    
    for size in range(min_size, max_size + 1):
        for node_set in combinations(range(n_nodes), size):
            # 检查是否形成空洞
            # 空洞条件：所有边界都存在，但内部填充不存在
            is_clique = True
            for i, j in combinations(node_set, 2):
                if distance_matrix[i, j] > 0.5:  # 阈值
                    is_clique = False
                    break
            
            if is_clique:
                # 这是一个团，不是空洞
                continue
            
            # 检查边界
            boundary_exists = True
            for sub in combinations(node_set, size - 1):
                sub_clique = True
                for i, j in combinations(sub, 2):
                    if distance_matrix[i, j] > 0.5:
                        sub_clique = False
                        break
                if not sub_clique:
                    boundary_exists = False
                    break
            
            if boundary_exists:
                voids.append({
                    'nodes': node_set,
                    'size': size,
                    'type': 'void' if size >= 4 else 'cycle'
                })
    
    return voids


def compute_topological_complexity(persistence_stats):
    """
    计算拓扑复杂度指标
    
    用于量化脑网络的拓扑丰富程度
    """
    complexity = 0
    
    for dim, stats in persistence_stats.items():
        if 'total_persistence' in stats:
            complexity += stats['total_persistence'] * (dim + 1)
    
    return complexity
```

## 应用场景

### 1. 脑网络分析
- 评估功能连接的拓扑丰富程度
- 检测临界状态下的拓扑变化

### 2. 疾病标志物
- 神经精神疾病的拓扑特征变化
- 高阶结构缺失作为病理指标

### 3. 方法学研究
- 评估持续同调在脑科学中的适用性
- 开发更鲁棒的高阶交互检测方法

## 参考文献

- Chung, M.K. et al. (2025). "From Density to Void: Brain Networks and Higher-Order Structures" arXiv:2503.14700