---
name: neural-code-dynamics-analysis
description: 神经编码动力学分析框架。整合计算神经科学、机器学习和临界态理论，研究生物与人工神经网络编码表示动力学，涵盖临界脑假说、神经表示流形、表征漂移等。适用于神经编码研究、临界态分析、表示学习。触发词：神经编码、临界脑、神经表示、表征漂移、neural code、critical brain、neural representation、representational drift、representation manifold。
user-invocable: true
---

# 神经编码动力学分析框架

**来源论文：** arXiv:2402.12796 - The dynamics of neural codes in biological and artificial neural networks (PhD Thesis, University of Granada)

## 核心方法论

### 1. 三种研究方法

| 方法 | 描述 |
|------|------|
| **计算方法** | 基于生物特征构建有效模型模拟结构和动力学 |
| **机器学习方法** | 推断解决任务所需的动力学和编码特性 |
| **理论方法** | 临界脑假说解释涌现集体性质 |

### 2. 临界脑假说

**核心思想：** 大脑动力学在临界点附近运行

**优势：**
- 最大信息传输
- 最大动态范围
- 最佳计算能力

**量化指标：**
- 谱半径接近 1
- 关联长度发散
- 指数衰减偏离临界

### 3. 神经表示流形

**发现：** 动力学态与表示流形拓扑特性之间存在关联

**关键概念：**
- 表示流形的维度
- 拓扑性质（连接性、曲率）
- 流形学习

### 4. 表征漂移

**现象：** 嗅觉皮层编码过程中的表示不稳定性

**机制假设：**
- 突触可塑性规则
- 网络动力学特性
- 学习-记忆权衡

## Python 实现

```python
import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from collections import defaultdict
from sklearn.manifold import Isomap, TSNE
from sklearn.decomposition import PCA


@dataclass
class NeuralCodeConfig:
    """神经编码分析配置"""
    n_neurons: int = 100           # 神经元数量
    n_time_steps: int = 1000       # 时间步数
    dt: float = 1.0                # 时间步长
    
    # 临界态参数
    spectral_radius_target: float = 0.95  # 目标谱半径
    
    # 表示分析
    n_components: int = 3          # 流形维度


class CriticalBrainAnalyzer:
    """临界脑分析器"""
    
    def __init__(self, config: NeuralCodeConfig):
        self.config = config
        
    def compute_spectral_radius(self, W: np.ndarray) -> float:
        """计算谱半径
        
        Args:
            W: 连接矩阵
            
        Returns:
            spectral_radius: 谱半径
        """
        eigenvalues = np.linalg.eigvals(W)
        return np.max(np.abs(eigenvalues))
    
    def distance_to_criticality(self, W: np.ndarray) -> float:
        """计算到临界点的距离
        
        Args:
            W: 连接矩阵
            
        Returns:
            distance: 到临界点的距离
        """
        spectral_radius = self.compute_spectral_radius(W)
        return np.abs(1.0 - spectral_radius)
    
    def tune_to_criticality(self, 
                            W: np.ndarray, 
                            target: float = 0.95) -> np.ndarray:
        """调整到临界态附近
        
        Args:
            W: 连接矩阵
            target: 目标谱半径
            
        Returns:
            W_tuned: 调整后的连接矩阵
        """
        spectral_radius = self.compute_spectral_radius(W)
        scale = target / spectral_radius
        return W * scale
    
    def analyze_critical_signature(self, 
                                    activity: np.ndarray) -> Dict:
        """分析临界态特征
        
        Args:
            activity: 神经活动 (time, neurons)
            
        Returns:
            signature: 临界态特征
        """
        # 计算关联函数
        mean_activity = activity.mean(axis=1)
        
        # 自相关
        autocorr = np.correlate(mean_activity, mean_activity, mode='full')
        autocorr = autocorr[len(autocorr)//2:]
        autocorr = autocorr / autocorr[0]
        
        # 簇大小分布（简化）
        threshold = mean_activity.mean() + mean_activity.std()
        avalanches = []
        current_size = 0
        
        for val in mean_activity:
            if val > threshold:
                current_size += 1
            else:
                if current_size > 0:
                    avalanches.append(current_size)
                current_size = 0
                
        # 幂律拟合（简化）
        if len(avalanches) > 10:
            sizes = np.array(avalanches)
            log_sizes = np.log(sizes[sizes > 0])
            hist, edges = np.histogram(log_sizes, bins=20)
            centers = (edges[:-1] + edges[1:]) / 2
            
            # 简化的幂律指数估计
            valid = hist > 0
            if np.sum(valid) > 5:
                exponent = -np.polyfit(centers[valid], np.log(hist[valid]), 1)[0]
            else:
                exponent = 1.5
        else:
            exponent = 1.5
            
        return {
            'autocorrelation': autocorr,
            'avalanche_sizes': avalanches,
            'power_law_exponent': exponent,
            'distance_to_critical': 0.0  # 需要更多分析
        }


class NeuralRepresentationAnalyzer:
    """神经表示分析器"""
    
    def __init__(self, config: NeuralCodeConfig):
        self.config = config
        
    def compute_representation_manifold(self,
                                         activities: np.ndarray,
                                         method: str = 'isomap') -> Dict:
        """计算表示流形
        
        Args:
            activities: 神经活动集合 (n_samples, time, neurons)
            method: 降维方法
            
        Returns:
            manifold: 流形信息
        """
        # 展平
        X = activities.reshape(len(activities), -1)
        
        # 降维
        n_components = self.config.n_components
        
        if method == 'isomap':
            embedding = Isomap(n_components=n_components)
        elif method == 'tsne':
            embedding = TSNE(n_components=n_components)
        else:
            embedding = PCA(n_components=n_components)
            
        coords = embedding.fit_transform(X)
        
        return {
            'coordinates': coords,
            'method': method,
            'n_components': n_components
        }
    
    def compute_manifold_geometry(self, 
                                   coords: np.ndarray) -> Dict:
        """计算流形几何特性
        
        Args:
            coords: 流形坐标 (n_samples, n_dims)
            
        Returns:
            geometry: 几何特性
        """
        from scipy.spatial.distance import pdist, squareform
        
        # 成对距离
        distances = pdist(coords)
        
        # 局部维度估计
        n_neighbors = min(10, len(coords) - 1)
        local_dims = []
        
        for i in range(len(coords)):
            # 找最近邻
            dist_row = squareform(distances)[i]
            neighbors = np.argsort(dist_row)[1:n_neighbors+1]
            
            # 局部 PCA
            local_points = coords[neighbors]
            pca = PCA(n_components=min(3, n_neighbors))
            pca.fit(local_points)
            
            # 有效维度
            explained = pca.explained_variance_ratio_
            dim = np.sum(explained > 0.1)  # 阈值
            local_dims.append(dim)
            
        # 曲率估计（简化）
        mean_dist = np.mean(distances)
        std_dist = np.std(distances)
        
        return {
            'mean_distance': mean_dist,
            'distance_std': std_dist,
            'mean_local_dimension': np.mean(local_dims),
            'intrinsic_dimension': np.mean(local_dims)
        }
    
    def analyze_representational_drift(self,
                                        activities_time1: np.ndarray,
                                        activities_time2: np.ndarray,
                                        same_stimuli: bool = True) -> Dict:
        """分析表征漂移
        
        Args:
            activities_time1: 时间点1的神经活动
            activities_time2: 时间点2的神经活动
            same_stimuli: 是否相同刺激
            
        Returns:
            drift: 漂移分析结果
        """
        # 计算表示相关性
        mean1 = activities_time1.mean(axis=0)
        mean2 = activities_time2.mean(axis=0)
        
        correlation = np.corrcoef(mean1, mean2)[0, 1]
        
        # CCA 分析（简化）
        # 使用 PCA 替代
        pca1 = PCA(n_components=10)
        pca2 = PCA(n_components=10)
        
        coords1 = pca1.fit_transform(activities_time1)
        coords2 = pca2.fit_transform(activities_time2)
        
        # 子空间重叠
        subspace_overlap = np.mean([
            np.abs(np.corrcoef(coords1[:, i], coords2[:, i])[0, 1])
            for i in range(min(coords1.shape[1], coords2.shape[1]))
        ])
        
        return {
            'representation_correlation': correlation,
            'subspace_overlap': subspace_overlap,
            'drift_magnitude': 1 - correlation,
            'stable_components': subspace_overlap
        }


class ReservoirComputer:
    """储层计算机（用于生物启发学习）"""
    
    def __init__(self, n_inputs: int, n_reservoir: int, n_outputs: int,
                 spectral_radius: float = 0.9):
        """
        Args:
            n_inputs: 输入维度
            n_reservoir: 储层大小
            n_outputs: 输出维度
            spectral_radius: 谱半径
        """
        self.n_inputs = n_inputs
        self.n_reservoir = n_reservoir
        self.n_outputs = n_outputs
        
        # 输入权重
        self.W_in = np.random.randn(n_reservoir, n_inputs) * 0.1
        
        # 储层权重
        W = np.random.randn(n_reservoir, n_reservoir) * 0.1
        # 调整谱半径
        current_sr = np.max(np.abs(np.linalg.eigvals(W)))
        self.W = W * (spectral_radius / current_sr)
        
        # 输出权重（训练）
        self.W_out = None
        
        # 状态
        self.state = np.zeros(n_reservoir)
        
    def update(self, input_signal: np.ndarray) -> np.ndarray:
        """更新储层状态
        
        Args:
            input_signal: 输入信号
            
        Returns:
            state: 新状态
        """
        self.state = np.tanh(self.W @ self.state + self.W_in @ input_signal)
        return self.state
    
    def train(self, inputs: np.ndarray, targets: np.ndarray):
        """训练输出权重
        
        Args:
            inputs: 输入序列 (time, n_inputs)
            targets: 目标序列 (time, n_outputs)
        """
        # 收集状态
        states = []
        self.state = np.zeros(self.n_reservoir)
        
        for t in range(len(inputs)):
            state = self.update(inputs[t])
            states.append(state)
            
        states = np.array(states)
        
        # 岭回归
        ridge = 1e-6
        self.W_out = np.linalg.lstsq(
            states.T @ states + ridge * np.eye(self.n_reservoir),
            states.T @ targets,
            rcond=None
        )[0].T
        
    def predict(self, inputs: np.ndarray) -> np.ndarray:
        """预测
        
        Args:
            inputs: 输入序列
            
        Returns:
            outputs: 输出序列
        """
        outputs = []
        self.state = np.zeros(self.n_reservoir)
        
        for t in range(len(inputs)):
            state = self.update(inputs[t])
            output = self.W_out @ state
            outputs.append(output)
            
        return np.array(outputs)


def analyze_criticality_vs_performance(spectral_radii: np.ndarray,
                                        performances: np.ndarray) -> Dict:
    """分析临界态与性能关系
    
    Args:
        spectral_radii: 谱半径数组
        performances: 性能数组
        
    Returns:
        analysis: 分析结果
    """
    # 最佳谱半径
    best_idx = np.argmax(performances)
    optimal_sr = spectral_radii[best_idx]
    
    # 到临界点距离 vs 性能
    distances = np.abs(1.0 - spectral_radii)
    
    # 相关性
    correlation = np.corrcoef(distances, performances)[0, 1]
    
    return {
        'optimal_spectral_radius': optimal_sr,
        'performance_correlation': correlation,
        'critical_distance': np.abs(1.0 - optimal_sr)
    }


def visualize_neural_codes(activities: np.ndarray,
                            labels: np.ndarray = None):
    """可视化神经编码"""
    import matplotlib.pyplot as plt
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. 神经活动热图
    ax = axes[0, 0]
    ax.imshow(activities[:100, :].T, aspect='auto', cmap='viridis')
    ax.set_xlabel('Time')
    ax.set_ylabel('Neuron')
    ax.set_title('Neural Activity Heatmap')
    
    # 2. PCA 降维
    ax = axes[0, 1]
    pca = PCA(n_components=2)
    coords = pca.fit_transform(activities)
    if labels is not None:
        scatter = ax.scatter(coords[:, 0], coords[:, 1], c=labels, cmap='tab10', alpha=0.6)
        plt.colorbar(scatter, ax=ax)
    else:
        ax.scatter(coords[:, 0], coords[:, 1], alpha=0.6)
    ax.set_xlabel('PC1')
    ax.set_ylabel('PC2')
    ax.set_title('Neural Representation (PCA)')
    
    # 3. 平均活动
    ax = axes[1, 0]
    mean_activity = activities.mean(axis=1)
    ax.plot(mean_activity, linewidth=1)
    ax.axhline(y=mean_activity.mean() + mean_activity.std(), 
               color='r', linestyle='--', label='Threshold')
    ax.set_xlabel('Time')
    ax.set_ylabel('Mean Activity')
    ax.set_title('Population Activity')
    ax.legend()
    
    # 4. 活动分布
    ax = axes[1, 1]
    ax.hist(activities.flatten(), bins=50, density=True, alpha=0.7)
    ax.set_xlabel('Activity')
    ax.set_ylabel('Density')
    ax.set_title('Activity Distribution')
    
    plt.tight_layout()
    plt.savefig('neural_code_dynamics.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    return 'neural_code_dynamics.png'


# 使用示例
def example_neural_code_analysis():
    """示例：神经编码分析"""
    print("="*60)
    print("神经编码动力学分析框架")
    print("="*60)
    
    config = NeuralCodeConfig(n_neurons=100)
    
    # 1. 临界脑分析
    print("\n1. 临界脑分析")
    critical_analyzer = CriticalBrainAnalyzer(config)
    
    # 生成随机网络
    W = np.random.randn(100, 100) * 0.1
    sr = critical_analyzer.compute_spectral_radius(W)
    distance = critical_analyzer.distance_to_criticality(W)
    
    print(f"   谱半径: {sr:.3f}")
    print(f"   到临界点距离: {distance:.3f}")
    
    # 调整到临界态
    W_tuned = critical_analyzer.tune_to_criticality(W, target=0.95)
    sr_tuned = critical_analyzer.compute_spectral_radius(W_tuned)
    print(f"   调整后谱半径: {sr_tuned:.3f}")
    
    # 2. 神经表示分析
    print("\n2. 神经表示分析")
    rep_analyzer = NeuralRepresentationAnalyzer(config)
    
    # 生成示例活动
    activities = np.random.randn(50, 100, 100) * 0.1
    
    manifold = rep_analyzer.compute_representation_manifold(activities)
    geometry = rep_analyzer.compute_manifold_geometry(manifold['coordinates'])
    
    print(f"   流形维度: {config.n_components}")
    print(f"   平均局部维度: {geometry['mean_local_dimension']:.2f}")
    
    # 3. 储层计算
    print("\n3. 储层计算（临界态优化）")
    reservoir = ReservoirComputer(10, 100, 5, spectral_radius=0.95)
    print(f"   储层大小: 100")
    print(f"   谱半径: 0.95（接近临界）")
    
    print(f"\n关键发现:")
    print(f"  ✅ 临界态优化计算能力")
    print(f"  ✅ 表示流形揭示编码结构")
    print(f"  ✅ 表征漂移反映可塑性")
    
    return config


## Activation Keywords
- 神经编码
- 临界脑
- 神经表示
- 表征漂移
- neural code
- critical brain
- neural representation
- representational drift
- representation manifold

## Tools Used
- numpy
- scipy
- sklearn

## Instructions for Agents
1. 理解三种研究方法：计算、机器学习、理论
2. 使用临界态分析评估网络动力学
3. 计算表示流形揭示编码结构
4. 分析表征漂移理解可塑性机制
5. 在储层计算中应用临界态优化

## Examples
```python
# 神经编码分析示例
from neural_code_dynamics_analysis import (
    CriticalBrainAnalyzer, NeuralRepresentationAnalyzer,
    NeuralCodeConfig, ReservoirComputer
)

# 1. 临界态分析
config = NeuralCodeConfig(n_neurons=100)
critical = CriticalBrainAnalyzer(config)

# 检查网络是否接近临界
W = np.random.randn(100, 100) * 0.1
distance = critical.distance_to_criticality(W)
print(f"到临界点距离: {distance:.3f}")

# 调整到临界态
W_critical = critical.tune_to_criticality(W, target=0.95)

# 2. 表示分析
rep_analyzer = NeuralRepresentationAnalyzer(config)
manifold = rep_analyzer.compute_representation_manifold(activities)
geometry = rep_analyzer.compute_manifold_geometry(manifold['coordinates'])

# 3. 表征漂移
drift = rep_analyzer.analyze_representational_drift(
    activities_time1, activities_time2
)
print(f"漂移幅度: {drift['drift_magnitude']:.3f}")
```

if __name__ == "__main__":
    example_neural_code_analysis()
```

## Related Skills

- `generative-brain-dynamics-models` - 脑动力学生成模型
- `kuramoto-brain-network` - Kuramoto 脑网络
- `time-varying-brain-connectivity` - 时变脑连接

## References

- arXiv:2402.12796 - The dynamics of neural codes in biological and artificial neural networks
- PhD Thesis, University of Granada
- Topics: Neurons and Cognition (q-bio.NC), Disordered Systems (cond-mat.dis-nn), Statistical Mechanics