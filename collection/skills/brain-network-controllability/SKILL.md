---
name: brain-network-controllability
description: 结构脑网络可控性分析实用指南。基于网络控制理论计算平均可控性、模态可控性、最小控制能量等指标，研究脑网络状态转移能力。适用于脑网络分析、神经调控研究、认知控制研究。触发词：脑网络可控性、控制理论、结构连接、控制能量、平均可控性、模态可控性、controllability、control theory、structural brain network。
user-invocable: true
---

# 结构脑网络可控性分析方法论

**来源论文：** arXiv:1908.03514 - A practical guide to methodological considerations in the controllability of structural brain networks

## 核心方法论

基于网络控制理论的脑网络可控性框架：

### 1. 线性动力学模型
\[\mathbf{x}(t+1) = \mathbf{A}\mathbf{x}(t) + \mathbf{B}\mathbf{u}(t)\]

其中：
- \(\mathbf{x}(t)\)：脑区状态向量
- \(\mathbf{A}\)：结构连接矩阵（状态转移矩阵）
- \(\mathbf{B}\)：控制输入矩阵
- \(\mathbf{u}(t)\)：控制信号

### 2. 可控性指标

**平均可控性（Average Controllability）**
- 驱动系统到附近状态的能力
- 与网络整合和扩散相关

**模态可控性（Modal Controllability）**
- 驱动系统到远距离状态的能力
- 与网络分离和专门化相关

**控制能量（Control Energy）**
- 实现状态转移所需的最小能量
- 与认知努力相关

## Python 实现

```python
import numpy as np
from scipy.linalg import eig, inv, solve, svd
from scipy.integrate import solve_ivp
from typing import Dict, Tuple, List, Optional
from dataclasses import dataclass
import warnings


@dataclass
class ControllabilityConfig:
    """可控性分析配置"""
    normalize: bool = True           # 是否归一化可控性指标
    energy_horizon: float = 1.0      # 控制能量计算时间范围
    timesteps: int = 100             # 状态转移时间步数
    regularization: float = 1e-6     # 正则化参数
    eigenvalue_threshold: float = 0.99  # 特征值阈值（稳定性）


class BrainNetworkControllability:
    """脑网络可控性分析器"""
    
    def __init__(self, A: np.ndarray, config: Optional[ControllabilityConfig] = None):
        """
        Args:
            A: 结构连接矩阵 (n x n)
            config: 分析配置
        """
        self.A = A.copy().astype(float)
        self.n = A.shape[0]
        self.config = config or ControllabilityConfig()
        
        # 稳定性处理
        self._stabilize_matrix()
        
    def _stabilize_matrix(self):
        """确保系统稳定（谱半径 < 1）"""
        eigenvalues = np.linalg.eigvals(self.A)
        spectral_radius = np.max(np.abs(eigenvalues))
        
        if spectral_radius >= 1:
            # 缩放矩阵
            self.A = self.A / spectral_radius * self.config.eigenvalue_threshold
            warnings.warn(f"Matrix scaled for stability. Original spectral radius: {spectral_radius:.4f}")
            
    def gramian(self, T: int = None) -> np.ndarray:
        """计算可控性格拉姆矩阵
        
        W_c = sum_{t=0}^{T-1} A^t @ B @ B^T @ (A^t)^T
        
        Args:
            T: 时间范围
            
        Returns:
            W_c: 可控性格拉姆矩阵 (n x n)
        """
        if T is None:
            T = self.config.timesteps
            
        # 假设B = I（所有节点都是控制节点）
        B = np.eye(self.n)
        
        W_c = np.zeros((self.n, self.n))
        A_power = np.eye(self.n)
        
        for t in range(T):
            W_c += A_power @ B @ B.T @ A_power.T
            A_power = A_power @ self.A
            
        return W_c
    
    def average_controllability(self, node_indices: List[int] = None) -> np.ndarray:
        """计算平均可控性
        
        对于控制节点i，平均可控性定义为：
        AC_i = trace(W_c^{(i)})
        
        其中 W_c^{(i)} 是以节点i为控制输入的格拉姆矩阵
        
        Args:
            node_indices: 要分析的节点索引，None则分析所有节点
            
        Returns:
            ac: 每个节点的平均可控性 (n,)
        """
        if node_indices is None:
            node_indices = list(range(self.n))
            
        ac = np.zeros(len(node_indices))
        T = self.config.timesteps
        
        for idx, i in enumerate(node_indices):
            # B矩阵：只有第i列非零
            B = np.zeros((self.n, 1))
            B[i, 0] = 1
            
            # 计算格拉姆矩阵
            W_c = np.zeros((self.n, self.n))
            A_power = np.eye(self.n)
            
            for t in range(T):
                W_c += A_power @ B @ B.T @ A_power.T
                A_power = A_power @ self.A
                
            # 平均可控性 = trace(W_c)
            ac[idx] = np.trace(W_c)
            
        if self.config.normalize:
            ac = ac / ac.max() if ac.max() > 0 else ac
            
        return ac
    
    def modal_controllability(self, node_indices: List[int] = None) -> np.ndarray:
        """计算模态可控性
        
        基于特征向量计算：
        phi_i = 1 - sum_j (A_ij)^2 * lambda_j^2 / ||v_j||^2
        
        其中 lambda_j 是特征值，v_j 是特征向量
        
        Args:
            node_indices: 要分析的节点索引
            
        Returns:
            mc: 每个节点的模态可控性 (n,)
        """
        if node_indices is None:
            node_indices = list(range(self.n))
            
        # 特征分解
        eigenvalues, eigenvectors = eig(self.A)
        eigenvalues = np.real(eigenvalues)
        eigenvectors = np.real(eigenvectors)
        
        # 计算每个节点的模态可控性
        mc = np.zeros(len(node_indices))
        
        for idx, i in enumerate(node_indices):
            # 节点i的模态可控性
            # phi_i = sum_j (1 - lambda_j^2) * v_{i,j}^2
            mc[idx] = np.sum(
                (1 - eigenvalues**2) * eigenvectors[i, :]**2
            )
            
        if self.config.normalize:
            mc = mc / mc.max() if mc.max() > 0 else mc
            
        return mc
    
    def minimum_control_energy(self, x0: np.ndarray, xf: np.ndarray,
                               T: float = 1.0, 
                               controlled_nodes: List[int] = None) -> float:
        """计算最小控制能量
        
        E = integral_0^T u(t)^T u(t) dt
        
        使用最优控制理论求解
        
        Args:
            x0: 初始状态 (n,)
            xf: 目标状态 (n,)
            T: 控制时间
            controlled_nodes: 控制节点索引
            
        Returns:
            E: 最小控制能量
        """
        if controlled_nodes is None:
            controlled_nodes = list(range(self.n))
            
        # 控制矩阵B
        B = np.zeros((self.n, len(controlled_nodes)))
        for j, i in enumerate(controlled_nodes):
            B[i, j] = 1
            
        # 计算控制能量
        # 离散时间控制
        timesteps = int(T * 100)
        dt = T / timesteps
        
        # 状态转移
        def dynamics(t, x, u_func):
            u = u_func(t)
            return self.A @ x + B @ u
        
        # 最优控制：u*(t) = B^T @ exp(A^T(T-t)) @ W^{-1} @ (xf - exp(AT) @ x0)
        # 其中 W = integral_0^T exp(At) @ B @ B^T @ exp(A^T t) dt
        
        # 简化计算：使用伪逆
        delta_x = xf - np.linalg.matrix_power(self.A, timesteps) @ x0
        
        # 计算可控性格拉姆矩阵
        W = np.zeros((self.n, self.n))
        A_power = np.eye(self.n)
        
        for t in range(timesteps):
            W += A_power @ B @ B.T @ A_power.T * dt
            A_power = A_power @ self.A
            
        # 正则化
        W += self.config.regularization * np.eye(self.n)
        
        # 最优控制输入
        try:
            v = solve(W, delta_x, assume_a='pos')
        except np.linalg.LinAlgError:
            v = np.linalg.lstsq(W, delta_x, rcond=None)[0]
            
        # 计算能量
        E = delta_x.T @ v
        
        return max(0, E)
    
    def optimal_control_trajectory(self, x0: np.ndarray, xf: np.ndarray,
                                    T: float = 1.0,
                                    controlled_nodes: List[int] = None) -> Dict:
        """计算最优控制轨迹
        
        Args:
            x0: 初始状态
            xf: 目标状态
            T: 控制时间
            controlled_nodes: 控制节点
            
        Returns:
            trajectory: 包含状态和控制轨迹的字典
        """
        if controlled_nodes is None:
            controlled_nodes = list(range(self.n))
            
        n_controls = len(controlled_nodes)
        timesteps = int(T * 100)
        dt = T / timesteps
        
        # B矩阵
        B = np.zeros((self.n, n_controls))
        for j, i in enumerate(controlled_nodes):
            B[i, j] = 1
            
        # 计算格拉姆矩阵
        W = np.zeros((self.n, self.n))
        A_power = np.eye(self.n)
        
        for t in range(timesteps):
            W += A_power @ B @ B.T @ A_power.T * dt
            A_power = A_power @ self.A
            
        W += self.config.regularization * np.eye(self.n)
        
        # 状态轨迹
        t = np.linspace(0, T, timesteps + 1)
        x = np.zeros((timesteps + 1, self.n))
        x[0] = x0
        
        # 控制轨迹
        u = np.zeros((timesteps, n_controls))
        
        # 最优控制计算
        delta_x = xf - np.linalg.matrix_power(self.A, timesteps) @ x0
        
        try:
            v = solve(W, delta_x, assume_a='pos')
        except np.linalg.LinAlgError:
            v = np.linalg.lstsq(W, delta_x, rcond=None)[0]
            
        # 模拟轨迹
        A_power = np.eye(self.n)
        for i in range(timesteps):
            # 控制输入
            exp_At = np.linalg.matrix_power(self.A, timesteps - i)
            u[i] = B.T @ exp_At.T @ v
            # 更新状态
            x[i+1] = self.A @ x[i] + B @ u[i]
            
        return {
            'time': t,
            'states': x,
            'controls': u,
            'energy': np.sum(u**2) * dt
        }
    
    def radial_propagation_connectivity(self, 
                                        distances: np.ndarray) -> np.ndarray:
        """计算径向传播连接性
        
        考虑活动通过相邻组织的径向传播
        
        Args:
            distances: 脑区之间的物理距离矩阵 (n x n)
            
        Returns:
            A_radial: 径向传播连接矩阵
        """
        # 径向传播因子
        # 连接强度随距离衰减
        sigma = np.mean(distances[distances > 0]) / 2  # 特征长度
        
        A_radial = np.exp(-distances**2 / (2 * sigma**2))
        
        # 结合结构连接
        A_combined = self.A * A_radial
        
        return A_combined
    
    def energy_landscape_complexity(self, 
                                    n_samples: int = 100) -> Dict:
        """计算能量景观复杂度
        
        随机采样状态转移，分析能量分布
        
        Args:
            n_samples: 采样数量
            
        Returns:
            metrics: 能量景观度量
        """
        energies = []
        
        for _ in range(n_samples):
            # 随机初始和目标状态
            x0 = np.random.randn(self.n)
            xf = np.random.randn(self.n)
            
            # 计算最小控制能量
            E = self.minimum_control_energy(x0, xf)
            energies.append(E)
            
        energies = np.array(energies)
        
        return {
            'mean_energy': np.mean(energies),
            'std_energy': np.std(energies),
            'min_energy': np.min(energies),
            'max_energy': np.max(energies),
            'energy_range': np.max(energies) - np.min(energies),
            'energy_skewness': self._skewness(energies),
            'energy_kurtosis': self._kurtosis(energies)
        }
    
    @staticmethod
    def _skewness(x: np.ndarray) -> float:
        """计算偏度"""
        return np.mean((x - np.mean(x))**3) / np.std(x)**3
    
    @staticmethod
    def _kurtosis(x: np.ndarray) -> float:
        """计算峰度"""
        return np.mean((x - np.mean(x))**4) / np.std(x)**4 - 3
    
    def full_analysis(self, 
                      x0: np.ndarray = None,
                      xf: np.ndarray = None) -> Dict:
        """完整可控性分析
        
        Returns:
            results: 所有可控性指标
        """
        results = {}
        
        # 1. 平均可控性
        results['average_controllability'] = self.average_controllability()
        
        # 2. 模态可控性
        results['modal_controllability'] = self.modal_controllability()
        
        # 3. 可控性权衡
        results['controllability_tradeoff'] = -np.corrcoef(
            results['average_controllability'],
            results['modal_controllability']
        )[0, 1]
        
        # 4. 控制能量（如果提供了状态）
        if x0 is not None and xf is not None:
            results['minimum_energy'] = self.minimum_control_energy(x0, xf)
            results['optimal_trajectory'] = self.optimal_control_trajectory(x0, xf)
            
        # 5. 能量景观复杂度
        results['energy_landscape'] = self.energy_landscape_complexity(n_samples=50)
        
        # 6. 网络统计
        results['network_stats'] = {
            'spectral_radius': np.max(np.abs(np.linalg.eigvals(self.A))),
            'density': np.mean(self.A > 0),
            'mean_weight': np.mean(self.A[self.A > 0]) if np.any(self.A > 0) else 0
        }
        
        return results


def generate_modular_network(n_nodes: int, n_modules: int = 4,
                            p_intra: float = 0.3, p_inter: float = 0.05,
                            weight_mean: float = 0.5, weight_std: float = 0.2) -> np.ndarray:
    """生成模块化脑网络
    
    Args:
        n_nodes: 节点数量
        n_modules: 模块数量
        p_intra: 模块内连接概率
        p_inter: 模块间连接概率
        weight_mean: 连接权重均值
        weight_std: 连接权重标准差
        
    Returns:
        A: 连接矩阵
    """
    A = np.zeros((n_nodes, n_nodes))
    module_size = n_nodes // n_modules
    
    rng = np.random.default_rng(42)
    
    for i in range(n_nodes):
        for j in range(n_nodes):
            if i == j:
                continue
                
            # 确定是否在同一模块
            i_module = i // module_size
            j_module = j // module_size
            
            if i_module == j_module:
                p = p_intra
            else:
                p = p_inter
                
            # 建立连接
            if rng.random() < p:
                A[i, j] = np.clip(
                    rng.normal(weight_mean, weight_std),
                    0.1, 1.0
                )
                
    # 对称化
    A = (A + A.T) / 2
    
    return A


# 使用示例
def example_analysis():
    """示例：脑网络可控性分析"""
    # 生成模拟连接矩阵
    n_nodes = 50
    A = generate_modular_network(n_nodes, n_modules=5)
    
    # 创建分析器
    analyzer = BrainNetworkControllability(A)
    
    # 完整分析
    results = analyzer.full_analysis()
    
    print("="*60)
    print("脑网络可控性分析结果")
    print("="*60)
    
    print(f"\n网络统计:")
    print(f"  谱半径: {results['network_stats']['spectral_radius']:.4f}")
    print(f"  连接密度: {results['network_stats']['density']:.4f}")
    print(f"  平均权重: {results['network_stats']['mean_weight']:.4f}")
    
    print(f"\n可控性指标:")
    ac = results['average_controllability']
    mc = results['modal_controllability']
    print(f"  平均可控性: mean={ac.mean():.4f}, std={ac.std():.4f}")
    print(f"  模态可控性: mean={mc.mean():.4f}, std={mc.std():.4f}")
    print(f"  可控性权衡 (负相关): r={results['controllability_tradeoff']:.4f}")
    
    print(f"\n能量景观:")
    el = results['energy_landscape']
    print(f"  平均能量: {el['mean_energy']:.4f}")
    print(f"  能量标准差: {el['std_energy']:.4f}")
    print(f"  能量范围: {el['energy_range']:.4f}")
    
    # 识别高可控性节点
    print(f"\n高平均可控性节点 (前5):")
    top_ac = np.argsort(ac)[-5:][::-1]
    for i, node in enumerate(top_ac):
        print(f"  {i+1}. 节点 {node}: AC={ac[node]:.4f}")
        
    print(f"\n高模态可控性节点 (前5):")
    top_mc = np.argsort(mc)[-5:][::-1]
    for i, node in enumerate(top_mc):
        print(f"  {i+1}. 节点 {node}: MC={mc[node]:.4f}")
        
    return analyzer, results


def example_state_transition():
    """示例：状态转移控制"""
    n_nodes = 20
    A = generate_modular_network(n_nodes)
    
    analyzer = BrainNetworkControllability(A)
    
    # 定义初始和目标状态
    x0 = np.zeros(n_nodes)
    x0[0:5] = 1.0  # 前5个节点激活
    
    xf = np.zeros(n_nodes)
    xf[15:20] = 1.0  # 后5个节点激活
    
    # 计算最优轨迹
    trajectory = analyzer.optimal_control_trajectory(x0, xf, T=1.0)
    
    print("\n状态转移控制:")
    print(f"  控制能量: {trajectory['energy']:.4f}")
    print(f"  时间步数: {len(trajectory['time'])}")
    print(f"  初始状态范数: {np.linalg.norm(x0):.4f}")
    print(f"  最终状态范数: {np.linalg.norm(trajectory['states'][-1]):.4f}")
    
    return trajectory


if __name__ == "__main__":
    analyzer, results = example_analysis()
    print("\n" + "="*60)
    trajectory = example_state_transition()