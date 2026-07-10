---
name: kuramoto-brain-network
description: Kuramoto模型脑网络相位动力学分析方法论。使用振荡器同步框架研究脑网络相位耦合，分析催产素等神经调节物质对脑网络动态的影响。适用于脑网络同步性分析、神经调节研究、网络神经科学。触发词：Kuramoto模型、脑网络、相位耦合、同步性、神经调节、催产素、oxytocin、phase coupling、synchronization、brain network dynamics。
user-invocable: true
---

# Kuramoto模型脑网络相位动力学分析方法论

**来源论文：** arXiv:2105.08288 - Kuramoto model based analysis reveals oxytocin effects on brain network dynamics

## 核心方法论

使用Kuramoto振荡器模型研究脑网络相位动力学：

1. **相位动力学建模**：将脑区视为耦合振荡器
2. **网络拓扑分析**：研究同步社区结构变化
3. **耦合强度估计**：量化网络连接强度和变异性
4. **时间动态分析**：追踪耦合模式的时间演化

### Kuramoto模型基础

\[\frac{d\theta_i}{dt} = \omega_i + \sum_{j} K_{ij} \sin(\theta_j - \theta_i)\]

其中：
- \(\theta_i\)：第i个振荡器的相位
- \(\omega_i\)：固有频率
- \(K_{ij}\)：耦合强度矩阵

## Python 实现

```python
import numpy as np
from scipy.integrate import odeint, solve_ivp
from scipy.signal import hilbert
from typing import Dict, Tuple, Optional, List
from dataclasses import dataclass
import networkx as nx
from sklearn.cluster import SpectralClustering


@dataclass
class KuramotoParameters:
    """Kuramoto模型参数"""
    n_oscillators: int = 50        # 振荡器数量
    K: float = 1.0                 # 全局耦合强度
    omega_mean: float = 0.0        # 平均固有频率
    omega_std: float = 1.0         # 固有频率标准差
    dt: float = 0.01               # 时间步长
    T: float = 100.0               # 总模拟时间
    noise_strength: float = 0.1    # 噪声强度


class KuramotoModel:
    """Kuramoto振荡器网络模型"""
    
    def __init__(self, params: KuramotoParameters, 
                 connectivity: Optional[np.ndarray] = None):
        """
        Args:
            params: 模型参数
            connectivity: 连接矩阵 (n x n)，None表示全连接
        """
        self.params = params
        self.n = params.n_oscillators
        
        # 初始化固有频率
        self.omega = np.random.normal(
            params.omega_mean, 
            params.omega_std, 
            self.n
        )
        
        # 设置连接矩阵
        if connectivity is None:
            self.K = np.ones((self.n, self.n)) * params.K / self.n
        else:
            self.K = connectivity * params.K
            
        # 移除自连接
        np.fill_diagonal(self.K, 0)
        
    def _derivatives(self, t: float, theta: np.ndarray) -> np.ndarray:
        """计算相位导数
        
        d theta_i / dt = omega_i + sum_j K_ij * sin(theta_j - theta_i)
        """
        dtheta = self.omega.copy()
        
        # 添加噪声
        if self.params.noise_strength > 0:
            dtheta += np.random.normal(0, self.params.noise_strength, self.n)
            
        # 计算耦合项
        for i in range(self.n):
            coupling = self.K[i, :] * np.sin(theta - theta[i])
            dtheta[i] += coupling.sum()
            
        return dtheta
    
    def simulate(self, theta0: Optional[np.ndarray] = None) -> Tuple[np.ndarray, np.ndarray]:
        """模拟振荡器动力学
        
        Args:
            theta0: 初始相位 (n,)，None则随机初始化
            
        Returns:
            t: 时间数组
            theta: 相位轨迹 (n_steps, n)
        """
        if theta0 is None:
            theta0 = np.random.uniform(0, 2 * np.pi, self.n)
            
        t_span = (0, self.params.T)
        t_eval = np.arange(0, self.params.T, self.params.dt)
        
        sol = solve_ivp(
            self._derivatives,
            t_span,
            theta0,
            t_eval=t_eval,
            method='RK45'
        )
        
        return sol.t, sol.y.T
    
    def compute_order_parameter(self, theta: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """计算序参量
        
        r(t) = |1/N * sum_j exp(i * theta_j)|
        psi(t) = arg(1/N * sum_j exp(i * theta_j))
        
        Args:
            theta: 相位数组 (n_steps, n) 或 (n,)
            
        Returns:
            r: 序参量幅值
            psi: 序参量相位
        """
        if theta.ndim == 1:
            z = np.exp(1j * theta)
            r = np.abs(z.mean())
            psi = np.angle(z.mean())
            return r, psi
        else:
            z = np.exp(1j * theta)
            r = np.abs(z.mean(axis=1))
            psi = np.angle(z.mean(axis=1))
            return r, psi


class BrainNetworkKuramotoAnalyzer:
    """脑网络Kuramoto分析器
    
    用于分析fMRI数据的相位动力学
    """
    
    def __init__(self, fmri_data: np.ndarray, 
                 connectivity_matrix: Optional[np.ndarray] = None):
        """
        Args:
            fmri_data: fMRI时间序列 (n_rois, n_timepoints)
            connectivity_matrix: 结构连接矩阵
        """
        self.fmri = fmri_data
        self.n_rois, self.n_timepoints = fmri_data.shape
        self.connectivity = connectivity_matrix
        
    def extract_phase(self) -> np.ndarray:
        """从fMRI信号提取相位
        
        使用Hilbert变换提取瞬时相位
        
        Returns:
            phase: 相位时间序列 (n_rois, n_timepoints)
        """
        phase = np.zeros_like(self.fmri)
        
        for i in range(self.n_rois):
            # Hilbert变换
            analytic_signal = hilbert(self.fmri[i, :])
            phase[i, :] = np.angle(analytic_signal)
            
        return phase
    
    def estimate_coupling_strength(self, phase: np.ndarray) -> np.ndarray:
        """估计耦合强度矩阵
        
        基于相位差统计推断耦合强度
        
        Args:
            phase: 相位时间序列 (n_rois, n_timepoints)
            
        Returns:
            K: 耦合强度矩阵 (n_rois, n_rois)
        """
        K = np.zeros((self.n_rois, self.n_rois))
        
        for i in range(self.n_rois):
            for j in range(i + 1, self.n_rois):
                # 计算相位差的同步指数
                phase_diff = phase[i, :] - phase[j, :]
                
                # 同步指数 r = |<exp(i * delta_phi)>|
                sync_index = np.abs(np.mean(np.exp(1j * phase_diff)))
                K[i, j] = sync_index
                K[j, i] = sync_index
                
        return K
    
    def compute_community_structure(self, K: np.ndarray, 
                                     n_communities: int = 2) -> Tuple[np.ndarray, Dict]:
        """检测同步社区
        
        Args:
            K: 耦合强度矩阵
            n_communities: 社区数量
            
        Returns:
            labels: 社区标签
            metrics: 社区度量
        """
        # 使用谱聚类
        clustering = SpectralClustering(
            n_clusters=n_communities,
            affinity='precomputed',
            random_state=42
        )
        
        labels = clustering.fit_predict(K)
        
        # 计算社区内/社区间同步
        intra_sync = []
        inter_sync = []
        
        for i in range(self.n_rois):
            for j in range(i + 1, self.n_rois):
                if labels[i] == labels[j]:
                    intra_sync.append(K[i, j])
                else:
                    inter_sync.append(K[i, j])
                    
        metrics = {
            'intra_sync_mean': np.mean(intra_sync),
            'intra_sync_std': np.std(intra_sync),
            'inter_sync_mean': np.mean(inter_sync),
            'inter_sync_std': np.std(inter_sync),
            'modularity': self._compute_modularity(K, labels)
        }
        
        return labels, metrics
    
    def _compute_modularity(self, K: np.ndarray, labels: np.ndarray) -> float:
        """计算模块度
        
        Q = 1/(2m) * sum_ij [A_ij - k_i k_j/(2m)] * delta(c_i, c_j)
        """
        m = K.sum() / 2
        k = K.sum(axis=1)
        
        Q = 0
        for i in range(self.n_rois):
            for j in range(self.n_rois):
                if labels[i] == labels[j]:
                    Q += K[i, j] - k[i] * k[j] / (2 * m)
                    
        return Q / (2 * m)
    
    def analyze_coupling_dynamics(self, phase: np.ndarray, 
                                   window_size: int = 20) -> Dict[str, np.ndarray]:
        """分析耦合动态变化
        
        Args:
            phase: 相位时间序列
            window_size: 滑动窗口大小
            
        Returns:
            dynamics: 耦合动态度量
        """
        n_windows = self.n_timepoints - window_size + 1
        
        r_mean = np.zeros(n_windows)
        r_std = np.zeros(n_windows)
        coupling_var = np.zeros(n_windows)
        
        for t in range(n_windows):
            window_phase = phase[:, t:t + window_size]
            
            # 窗口内的同步性
            r_t = []
            K_window = self.estimate_coupling_strength(window_phase)
            r_t = K_window[np.triu_indices(self.n_rois, k=1)]
            
            r_mean[t] = np.mean(r_t)
            r_std[t] = np.std(r_t)
            coupling_var[t] = np.var(r_t)
            
        return {
            'r_mean': r_mean,
            'r_std': r_std,
            'coupling_variance': coupling_var
        }
    
    def compare_conditions(self, phase_cond1: np.ndarray, 
                          phase_cond2: np.ndarray) -> Dict:
        """比较两种条件下的网络动态
        
        例如：催产素 vs 安慰剂
        
        Args:
            phase_cond1: 条件1的相位
            phase_cond2: 条件2的相位
            
        Returns:
            comparison: 比较结果
        """
        # 估计耦合强度
        K1 = self.estimate_coupling_strength(phase_cond1)
        K2 = self.estimate_coupling_strength(phase_cond2)
        
        # 社区检测
        labels1, metrics1 = self.compute_community_structure(K1)
        labels2, metrics2 = self.compute_community_structure(K2)
        
        # 动态分析
        dynamics1 = self.analyze_coupling_dynamics(phase_cond1)
        dynamics2 = self.analyze_coupling_dynamics(phase_cond2)
        
        return {
            'coupling_strength_diff': K2 - K1,
            'coupling_variance_change': {
                'cond1': np.var(K1[np.triu_indices(self.n_rois, k=1)]),
                'cond2': np.var(K2[np.triu_indices(self.n_rois, k=1)])
            },
            'community_metrics': {
                'cond1': metrics1,
                'cond2': metrics2
            },
            'dynamics': {
                'cond1': dynamics1,
                'cond2': dynamics2
            },
            'flexibility': {
                'cond1': np.mean(dynamics1['coupling_variance']),
                'cond2': np.mean(dynamics2['coupling_variance'])
            }
        }


def simulate_oxytocin_effect(n_rois: int = 50, 
                             n_timepoints: int = 200) -> Dict:
    """模拟催产素对脑网络的影响
    
    基于论文发现：
    - FPN同步性增加
    - DMN同步性降低
    - 耦合强度变异性增加
    - 耦合模式更灵活
    
    Returns:
        results: 模拟结果
    """
    # 创建两个模块（模拟FPN和DMN）
    n_fpn = n_rois // 2
    n_dmn = n_rois - n_fpn
    
    # 安慰剂条件
    params_placebo = KuramotoParameters(
        n_oscillators=n_rois,
        K=1.0,
        omega_std=1.0
    )
    
    # 创建模块化连接
    connectivity_placebo = np.zeros((n_rois, n_rois))
    # FPN内部强连接
    connectivity_placebo[:n_fpn, :n_fpn] = 1.5
    # DMN内部强连接
    connectivity_placebo[n_fpn:, n_fpn:] = 1.5
    # 模块间弱连接
    connectivity_placebo[:n_fpn, n_fpn:] = 0.3
    connectivity_placebo[n_fpn:, :n_fpn] = 0.3
    
    model_placebo = KuramotoModel(params_placebo, connectivity_placebo)
    t, theta_placebo = model_placebo.simulate()
    
    # 催产素条件
    # 效应：FPN同步增加，DMN同步降低，变异性增加
    connectivity_oxytocin = connectivity_placebo.copy()
    connectivity_oxytocin[:n_fpn, :n_fpn] *= 1.3  # FPN同步增加
    connectivity_oxytocin[n_fpn:, n_fpn:] *= 0.7   # DMN同步降低
    
    # 添加变异性
    noise = np.random.normal(0, 0.1, connectivity_oxytocin.shape)
    connectivity_oxytocin += noise
    connectivity_oxytocin = np.clip(connectivity_oxytocin, 0, None)
    
    params_oxytocin = KuramotoParameters(
        n_oscillators=n_rois,
        K=1.2,  # 增加全局耦合
        omega_std=1.2  # 增加频率变异性
    )
    
    model_oxytocin = KuramotoModel(params_oxytocin, connectivity_oxytocin)
    _, theta_oxytocin = model_oxytocin.simulate()
    
    # 计算同步性
    r_placebo, _ = model_placebo.compute_order_parameter(theta_placebo[-1000:])
    r_oxytocin, _ = model_oxytocin.compute_order_parameter(theta_oxytocin[-1000:])
    
    # 分析社区结构
    analyzer = BrainNetworkKuramotoAnalyzer(
        np.random.randn(n_rois, n_timepoints)  # 占位数据
    )
    
    phase_placebo = theta_placebo[-n_timepoints:]
    phase_oxytocin = theta_oxytocin[-n_timepoints:]
    
    comparison = analyzer.compare_conditions(phase_placebo, phase_oxytocin)
    
    return {
        'sync_placebo': r_placebo,
        'sync_oxytocin': r_oxytocin,
        'sync_change': r_oxytocin - r_placebo,
        'community_comparison': comparison,
        'theta_placebo': theta_placebo,
        'theta_oxytocin': theta_oxytocin
    }


# 使用示例
def example_analysis():
    """示例：脑网络Kuramoto分析"""
    # 生成模拟fMRI数据
    n_rois = 30
    n_timepoints = 200
    fmri_data = np.random.randn(n_rois, n_timepoints)
    
    # 添加一些同步信号
    shared_signal = np.sin(np.linspace(0, 10 * np.pi, n_timepoints))
    fmri_data[:15] += 0.5 * shared_signal
    
    # 创建分析器
    analyzer = BrainNetworkKuramotoAnalyzer(fmri_data)
    
    # 提取相位
    phase = analyzer.extract_phase()
    
    # 估计耦合强度
    K = analyzer.estimate_coupling_strength(phase)
    
    # 检测社区
    labels, metrics = analyzer.compute_community_structure(K, n_communities=2)
    
    print(f"检测到 {len(np.unique(labels))} 个社区")
    print(f"社区内同步: {metrics['intra_sync_mean']:.3f} ± {metrics['intra_sync_std']:.3f}")
    print(f"社区间同步: {metrics['inter_sync_mean']:.3f} ± {metrics['inter_sync_std']:.3f}")
    print(f"模块度: {metrics['modularity']:.3f}")
    
    # 分析动态
    dynamics = analyzer.analyze_coupling_dynamics(phase)
    print(f"\n耦合变异性: {np.mean(dynamics['coupling_variance']):.4f}")
    
    return analyzer, K, labels, metrics


## Activation Keywords
- Kuramoto模型
- 脑网络
- 相位耦合
- 同步性
- 神经调节
- 催产素
- oxytocin
- phase coupling
- synchronization
- brain network dynamics
- 序参量
- 社区检测

## Tools Used
- numpy
- scipy
- networkx
- sklearn

## Instructions for Agents
1. 理解Kuramoto模型：振荡器相位动力学方程
2. 计算序参量：r(t) = |1/N * sum exp(i*theta_j)|
3. 提取相位：使用Hilbert变换从fMRI信号提取瞬时相位
4. 估计耦合强度：基于相位差统计推断
5. 分析催产素效应：FPN同步增加，DMN同步降低

## Examples
```python
# 使用示例
from kuramoto_brain_network import KuramotoModel, BrainNetworkKuramotoAnalyzer

# 1. 创建Kuramoto模型
params = KuramotoParameters(n_oscillators=50, K=1.0)
model = KuramotoModel(params, connectivity_matrix)

# 2. 模拟
t, theta = model.simulate(initial_phase)

# 3. 计算序参量
r, psi = model.compute_order_parameter(theta)
print(f"同步指数: {r.mean():.4f}")

# 4. 脑网络分析
analyzer = BrainNetworkKuramotoAnalyzer(fmri_data)
phase = analyzer.extract_phase()
K = analyzer.estimate_coupling_strength(phase)
```

## 参考文献

- arXiv:2105.08288 - Kuramoto model based analysis reveals oxytocin effects on brain network dynamics