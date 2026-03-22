---
name: discrete-heat-kernels-simplicial
description: 单纯复形上的离散热核方法论。将热核平滑从顶点和边扩展到环和高维结构，通过Hodge拉普拉斯算子构建离散热核。触发词：热核、单纯复形、高阶网络、拓扑数据分析、Hodge拉普拉斯、脑网络分析、环检测、heat kernel、simplicial complex、higher-order network、Hodge Laplacian。
user-invocable: true
---

# Discrete Heat Kernels on Simplicial Complexes

基于单纯复形的离散热核框架，将经典信号处理方法从顶点和边扩展到环和高维结构，用于功能脑网络分析。

## 核心方法论

### 1. 单纯复形构建

```python
import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
from scipy.sparse.linalg import expm_multiply
from itertools import combinations

class SimplicialComplex:
    """单纯复形构建与管理
    
    单纯复形包含：
    - 0-单纯形：顶点
    - 1-单纯形：边
    - 2-单纯形：三角形（填充的环）
    - k-单纯形：k维结构
    """
    
    def __init__(self):
        self.simplices = {}  # k -> set of k-simplices
        self.vertices = set()
        
    def add_simplex(self, simplex: tuple):
        """添加单纯形及其所有面
        
        Args:
            simplex: 顶点元组，如 (0, 1, 2) 表示三角形
        """
        k = len(simplex) - 1  # 维度
        
        if k not in self.simplices:
            self.simplices[k] = set()
        
        self.simplices[k].add(tuple(sorted(simplex)))
        
        # 添加所有顶点
        for v in simplex:
            self.vertices.add(v)
        
        # 递归添加所有面
        if k > 0:
            for face in combinations(simplex, k):
                self.add_simplex(face)
    
    def build_from_graph(self, edges: list, max_dim: int = 2):
        """从图边列表构建单纯复形
        
        Args:
            edges: 边列表 [(i, j), ...]
            max_dim: 最大维度（2=包含三角形）
        """
        # 添加所有边
        for edge in edges:
            self.add_simplex(edge)
        
        # 检测三角形（如果max_dim >= 2）
        if max_dim >= 2:
            # 使用邻接关系检测三角形
            edge_set = set(tuple(sorted(e)) for e in edges)
            vertices = set()
            for e in edges:
                vertices.update(e)
            
            for v1 in vertices:
                neighbors_v1 = {e[1] if e[0] == v1 else e[0] 
                               for e in edges if v1 in e}
                
                for v2, v3 in combinations(neighbors_v1, 2):
                    if tuple(sorted([v2, v3])) in edge_set:
                        # 发现三角形
                        self.add_simplex((v1, v2, v3))
    
    def get_k_simplices(self, k: int):
        """获取所有k-单纯形"""
        return list(self.simplices.get(k, set()))
    
    def n_simplices(self, k: int):
        """k-单纯形数量"""
        return len(self.simplices.get(k, set()))
```

### 2. 边界算子与Hodge拉普拉斯

```python
class BoundaryOperators:
    """边界算子计算
    
    边界算子 ∂_k 将 k-单纯形映射到 (k-1)-单纯形
    """
    
    def __init__(self, complex: SimplicialComplex):
        self.complex = complex
        self.boundary_matrices = {}
        
    def compute_boundary_matrix(self, k: int):
        """计算k-边界矩阵 ∂_k
        
        ∂_k: C_k → C_{k-1}
        
        对于k-单纯形 (v_0, ..., v_k):
        ∂_k = Σ (-1)^i (v_0, ..., v_i^, ..., v_k)
        """
        if k in self.boundary_matrices:
            return self.boundary_matrices[k]
        
        if k == 0:
            # 0-边界是零映射
            return csr_matrix((0, self.complex.n_simplices(0)))
        
        k_simplices = self.complex.get_k_simplices(k)
        k_minus_1_simplices = self.complex.get_k_simplices(k - 1)
        
        n_k = len(k_simplices)
        n_k_minus_1 = len(k_minus_1_simplices)
        
        if n_k == 0 or n_k_minus_1 == 0:
            return csr_matrix((n_k_minus_1, n_k))
        
        # 构建稀疏边界矩阵
        B = lil_matrix((n_k_minus_1, n_k))
        
        # 创建索引映射
        simplex_to_idx = {s: i for i, s in enumerate(k_minus_1_simplices)}
        
        for j, simplex in enumerate(k_simplices):
            for i, v in enumerate(simplex):
                # 移除第i个顶点得到面
                face = tuple(sorted(simplex[:i] + simplex[i+1:]))
                if face in simplex_to_idx:
                    # 符号由位置决定
                    B[simplex_to_idx[face], j] = (-1) ** i
        
        self.boundary_matrices[k] = csr_matrix(B)
        return self.boundary_matrices[k]


class HodgeLaplacian:
    """Hodge拉普拉斯算子
    
    L_k = ∂_k^T ∂_k + ∂_{k+1} ∂_{k+1}^T
    
    性质：
    - 半正定
    - 零特征向量对应k阶同调群
    """
    
    def __init__(self, complex: SimplicialComplex):
        self.complex = complex
        self.boundary_ops = BoundaryOperators(complex)
        self.laplacians = {}
        
    def compute_laplacian(self, k: int):
        """计算k-Hodge拉普拉斯算子"""
        if k in self.laplacians:
            return self.laplacians[k]
        
        B_k = self.boundary_ops.compute_boundary_matrix(k)
        B_k_plus_1 = self.boundary_ops.compute_boundary_matrix(k + 1)
        
        # L_k = B_k^T B_k + B_{k+1} B_{k+1}^T
        L_k = B_k.T @ B_k + B_k_plus_1 @ B_k_plus_1.T
        
        self.laplacians[k] = L_k
        return L_k
    
    def get_harmonic_space(self, k: int, tol: float = 1e-10):
        """获取k阶调和空间（零特征空间）
        
        对应于k阶同调群
        """
        L_k = self.compute_laplacian(k)
        
        if L_k.shape[0] == 0:
            return np.zeros((0, 0))
        
        # 特征分解
        eigenvalues, eigenvectors = np.linalg.eigh(L_k.toarray())
        
        # 零特征值对应的特征向量
        harmonic_idx = np.abs(eigenvalues) < tol
        harmonic_vectors = eigenvectors[:, harmonic_idx]
        
        return harmonic_vectors
    
    def betti_number(self, k: int):
        """计算k阶Betti数
        
        β_k = dim(H_k) = 调和空间的维度
        """
        harmonic = self.get_harmonic_space(k)
        return harmonic.shape[1] if len(harmonic.shape) == 2 else 0
```

### 3. 离散热核

```python
class DiscreteHeatKernel:
    """离散热核
    
    H_k(t) = exp(-t L_k)
    
    用于在k-单纯形上平滑信号
    """
    
    def __init__(self, hodge_laplacian: HodgeLaplacian):
        self.hodge = hodge_laplacian
        
    def compute_kernel(self, k: int, t: float):
        """计算k维热核矩阵
        
        H_k(t) = exp(-t L_k)
        """
        L_k = self.hodge.compute_laplacian(k)
        
        if L_k.shape[0] == 0:
            return csr_matrix((0, 0))
        
        # 使用特征分解计算矩阵指数
        eigenvalues, eigenvectors = np.linalg.eigh(L_k.toarray())
        
        # H = V @ exp(-t * Λ) @ V^T
        exp_eigenvalues = np.exp(-t * eigenvalues)
        H = eigenvectors @ np.diag(exp_eigenvalues) @ eigenvectors.T
        
        return H
    
    def heat_diffusion(self, k: int, signal: np.ndarray, t: float):
        """在k-单纯形上执行热扩散
        
        Args:
            k: 单纯形维度
            signal: k-单纯形上的信号
            t: 扩散时间
            
        Returns:
            平滑后的信号
        """
        H = self.compute_kernel(k, t)
        return H @ signal
    
    def multi_scale_diffusion(self, k: int, signal: np.ndarray, t_values: list):
        """多尺度热扩散
        
        在多个时间尺度上分析信号
        """
        results = {}
        for t in t_values:
            results[t] = self.heat_diffusion(k, signal, t)
        return results


class SparseHeatKernel:
    """稀疏实现的热核（适用于大规模网络）"""
    
    def __init__(self, hodge_laplacian: HodgeLaplacian):
        self.hodge = hodge_laplacian
        
    def heat_diffusion_iterative(
        self, 
        k: int, 
        signal: np.ndarray, 
        t: float,
        n_steps: int = 100
    ):
        """使用迭代方法计算热扩散
        
        避免（稠密）矩阵指数计算
        """
        L_k = self.hodge.compute_laplacian(k)
        
        if L_k.shape[0] == 0:
            return signal
        
        # 时间步长
        dt = t / n_steps
        
        # 显式欧拉方法
        u = signal.copy()
        for _ in range(n_steps):
            u = u - dt * (L_k @ u)
        
        return u
    
    def chebyshev_heat_kernel(
        self,
        k: int,
        signal: np.ndarray,
        t: float,
        order: int = 30
    ):
        """Chebyshev多项式近似热核
        
        更高效的数值方法
        """
        L_k = self.hodge.compute_laplacian(k)
        
        if L_k.shape[0] == 0:
            return signal
        
        # 归一化拉普拉斯
        eigenvalues = np.linalg.eigvalsh(L_k.toarray())
        lambda_max = eigenvalues.max()
        lambda_min = eigenvalues.min()
        
        # 缩放到[-1, 1]
        L_scaled = (2 * L_k - (lambda_max + lambda_min) * np.eye(L_k.shape[0])) / (lambda_max - lambda_min)
        
        # Chebyshev递推
        T_prev = signal
        T_curr = L_scaled @ signal
        result = 0.5 * np.exp(-t * lambda_max) * T_prev + np.exp(-t * (lambda_max + lambda_min) / 2) * T_curr
        
        for m in range(2, order):
            T_next = 2 * L_scaled @ T_curr - T_prev
            result += np.exp(-t * lambda_max * (1 + 2 * (m - 1) / order)) * T_next
            T_prev = T_curr
            T_curr = T_next
        
        return result
```

### 4. 脑网络应用

```python
class BrainNetworkSimplicialAnalysis:
    """脑网络单纯复形分析
    
    将功能脑网络映射到单纯复形进行分析
    """
    
    def __init__(self, threshold: float = 0.5, max_dim: int = 2):
        self.threshold = threshold
        self.max_dim = max_dim
        
    def connectivity_to_simplicial(self, connectivity: np.ndarray):
        """将功能连接矩阵转换为单纯复形
        
        Args:
            connectivity: 功能连接矩阵 (n_rois, n_rois)
            
        Returns:
            SimplicialComplex对象
        """
        n = connectivity.shape[0]
        
        # 阈值化获取边
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                if np.abs(connectivity[i, j]) > self.threshold:
                    edges.append((i, j))
        
        # 构建单纯复形
        complex = SimplicialComplex()
        complex.build_from_graph(edges, max_dim=self.max_dim)
        
        return complex
    
    def analyze_higher_order_structure(self, connectivity: np.ndarray):
        """分析高阶结构
        
        Returns:
            包含各维度分析结果的字典
        """
        # 构建单纯复形
        sc = self.connectivity_to_simplicial(connectivity)
        
        # 计算Hodge拉普拉斯
        hodge = HodgeLaplacian(sc)
        
        results = {
            'n_simplices': {k: sc.n_simplices(k) for k in range(self.max_dim + 1)},
            'betti_numbers': {},
            'spectral_features': {}
        }
        
        for k in range(self.max_dim + 1):
            # Betti数
            results['betti_numbers'][k] = hodge.betti_number(k)
            
            # 谱特征
            L_k = hodge.compute_laplacian(k)
            if L_k.shape[0] > 0:
                eigenvalues = np.linalg.eigvalsh(L_k.toarray())
                results['spectral_features'][k] = {
                    'smallest_nonzero': eigenvalues[eigenvalues > 1e-10].min() if (eigenvalues > 1e-10).any() else 0,
                    'spectral_gap': eigenvalues[1] - eigenvalues[0] if len(eigenvalues) > 1 else 0
                }
        
        return results
    
    def smooth_network_signal(
        self,
        connectivity: np.ndarray,
        signal: np.ndarray,
        k: int = 0,
        t: float = 1.0
    ):
        """在网络信号上应用热核平滑
        
        Args:
            connectivity: 功能连接矩阵
            signal: 节点/边信号
            k: 单纯形维度（0=顶点，1=边）
            t: 平滑强度
        """
        sc = self.connectivity_to_simplicial(connectivity)
        hodge = HodgeLaplacian(sc)
        heat_kernel = DiscreteHeatKernel(hodge)
        
        smoothed = heat_kernel.heat_diffusion(k, signal, t)
        return smoothed
    
    def detect_coherent_architectures(self, connectivity: np.ndarray, t_values: list = [0.1, 0.5, 1.0]):
        """检测连贯解剖结构
        
        通过多尺度平滑消除虚假连接，增强连贯结构
        """
        sc = self.connectivity_to_simplicial(connectivity)
        hodge = HodgeLaplacian(sc)
        heat_kernel = DiscreteHeatKernel(hodge)
        
        # 边信号：连接强度
        edges = sc.get_k_simplices(1)
        if len(edges) == 0:
            return None
        
        edge_signal = np.array([
            connectivity[e[0], e[1]] for e in edges
        ])
        
        # 多尺度平滑
        results = {}
        for t in t_values:
            smoothed = heat_kernel.heat_diffusion(1, edge_signal, t)
            
            # 识别强化的连贯结构
            threshold = smoothed.mean() + smoothed.std()
            coherent_edges = [edges[i] for i in range(len(edges)) if smoothed[i] > threshold]
            
            results[t] = {
                'smoothed_signal': smoothed,
                'coherent_edges': coherent_edges,
                'coherence_ratio': len(coherent_edges) / len(edges)
            }
        
        return results
```

## 应用场景

### 1. 功能脑网络分析
- 高阶功能连接检测
- 拓扑特征提取
- 脑区协调模式分析

### 2. 网络信号处理
- 去噪和信号增强
- 多尺度结构分析
- 异常连接检测

### 3. 拓扑数据分析
- 持续同调计算
- Betti数估计
- 空洞结构识别

## 使用示例

```python
# 构建测试网络
n_nodes = 50
np.random.seed(42)

# 创建随机网络
adjacency = np.random.rand(n_nodes, n_nodes)
adjacency = (adjacency + adjacency.T) / 2
np.fill_diagonal(adjacency, 0)

# 创建功能连接矩阵（添加一些模块化结构）
for i in range(5):
    for j in range(10):
        for k in range(10):
            if j != k:
                adjacency[i*10+j, i*10+k] += 0.5

# 分析
analyzer = BrainNetworkSimplicialAnalysis(threshold=0.6)
results = analyzer.analyze_higher_order_structure(adjacency)

print("单纯形数量:", results['n_simplices'])
print("Betti数:", results['betti_numbers'])
print("谱特征:", results['spectral_features'])

# 信号平滑
node_signal = np.random.randn(n_nodes)
smoothed_signal = analyzer.smooth_network_signal(
    adjacency, node_signal, k=0, t=0.5
)

print(f"\n原始信号方差: {node_signal.var():.4f}")
print(f"平滑信号方差: {smoothed_signal.var():.4f}")

# 检测连贯结构
coherent = analyzer.detect_coherent_architectures(adjacency)
if coherent:
    for t, result in coherent.items():
        print(f"\nt={t}: 连贯边比例 = {result['coherence_ratio']:.2%}")
```

## 参考文献

- arXiv:2509.16908 - Discrete Heat Kernels on Simplicial Complexes and Its Application to Functional Brain Networks