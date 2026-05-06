---
name: spiking-mode-neural-networks
description: 脉冲模式神经网络训练框架。基于Hopfield分解将循环权重矩阵分解为输入/输出模式和评分矩阵，显著降低训练成本，揭示低维吸引子结构。适用于神经形态计算、SNN训练加速、神经流形分析。触发词：脉冲模式网络、Hopfield分解、SNN训练加速、神经流形、spiking mode、Hopfield decomposition、neural manifold、attractor dynamics。
user-invocable: true
---

# 脉冲模式神经网络框架

**来源论文：** arXiv:2310.14621 - Spiking mode-based neural networks (Phys. Rev. E 110, 024306, 2024)

## 核心方法论

### 1. Hopfield 分解

将循环权重矩阵分解为三个矩阵的乘积：

\[
W = \sum_{\mu} s_\mu \phi_\mu \otimes \psi_\mu = \Phi S \Psi^T
\]

其中：
- \(\phi_\mu\) - 输入模式
- \(\psi_\mu\) - 输出模式
- \(s_\mu\) - 评分（重要性权重）

### 2. 模式-评分空间训练

**优势：**
- 显著降低空间复杂度
- 可调节模式数量
- 透明理解电路机制

### 3. 低维吸引子结构

高维神经活动投影到低维模式空间：
- 少数模式即可捕获神经流形
- 揭示动力学吸引子结构

## Python 实现

```python
import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class SpikingModeConfig:
    """脉冲模式网络配置"""
    n_neurons: int = 100           # 神经元数量
    n_modes: int = 10              # 模式数量
    n_inputs: int = 784            # 输入维度
    n_outputs: int = 10            # 输出类别
    
    # 神经元参数
    tau: float = 20.0              # 时间常数 (ms)
    threshold: float = 1.0         # 发放阈值
    
    # 训练参数
    learning_rate: float = 0.01
    n_steps: int = 100             # 时间步数


class HopfieldDecomposition:
    """Hopfield 分解"""
    
    def __init__(self, n_neurons: int, n_modes: int):
        """
        Args:
            n_neurons: 神经元数量
            n_modes: 模式数量
        """
        self.n_neurons = n_neurons
        self.n_modes = n_modes
        
        # 初始化模式和评分
        self.phi = np.random.randn(n_modes, n_neurons) * 0.1  # 输入模式
        self.psi = np.random.randn(n_modes, n_neurons) * 0.1  # 输出模式
        self.scores = np.ones(n_modes)                         # 评分
        
    def reconstruct_weight(self) -> np.ndarray:
        """重建权重矩阵
        
        W = Phi^T @ diag(scores) @ Psi
        
        Returns:
            W: 重建的权重矩阵
        """
        # W = sum_mu s_mu * phi_mu @ psi_mu^T
        S = np.diag(self.scores)
        W = self.phi.T @ S @ self.psi
        return W
    
    def get_mode_contribution(self, mode_idx: int) -> np.ndarray:
        """获取单个模式的贡献
        
        Args:
            mode_idx: 模式索引
            
        Returns:
            contribution: 模式贡献矩阵
        """
        return self.scores[mode_idx] * np.outer(self.phi[mode_idx], self.psi[mode_idx])
    
    def rank_approximation(self, k: int) -> np.ndarray:
        """k 秩近似
        
        Args:
            k: 保留的模式数量
            
        Returns:
            W_k: k 秩近似权重矩阵
        """
        # 按评分排序
        sorted_indices = np.argsort(self.scores)[::-1]
        top_k = sorted_indices[:k]
        
        W_k = np.zeros((self.n_neurons, self.n_neurons))
        for idx in top_k:
            W_k += self.get_mode_contribution(idx)
            
        return W_k
    
    def compute_effective_rank(self, threshold: float = 0.95) -> int:
        """计算有效秩
        
        Args:
            threshold: 累积贡献阈值
            
        Returns:
            effective_rank: 有效秩
        """
        sorted_scores = np.sort(self.scores)[::-1]
        cumulative = np.cumsum(sorted_scores) / np.sum(sorted_scores)
        
        return np.searchsorted(cumulative, threshold) + 1


class SpikingModeNetwork:
    """脉冲模式神经网络"""
    
    def __init__(self, config: SpikingModeConfig):
        """
        Args:
            config: 网络配置
        """
        self.config = config
        
        # Hopfield 分解
        self.decomposition = HopfieldDecomposition(config.n_neurons, config.n_modes)
        
        # 输入权重
        self.W_in = np.random.randn(config.n_neurons, config.n_inputs) * 0.1
        
        # 输出权重
        self.W_out = np.random.randn(config.n_outputs, config.n_neurons) * 0.1
        
        # 状态
        self.membrane = np.zeros(config.n_neurons)
        self.spikes = np.zeros(config.n_neurons)
        
    def reset_state(self):
        """重置网络状态"""
        self.membrane = np.zeros(self.config.n_neurons)
        self.spikes = np.zeros(self.config.n_neurons)
        
    def step(self, input_current: np.ndarray) -> np.ndarray:
        """单步更新
        
        Args:
            input_current: 输入电流
            
        Returns:
            spikes: 脉冲输出
        """
        cfg = self.config
        
        # 重建循环权重
        W_rec = self.decomposition.reconstruct_weight()
        
        # 膜电位更新
        self.membrane += (-self.membrane + 
                         W_rec @ self.spikes + 
                         self.W_in @ input_current) / cfg.tau
        
        # 发放
        self.spikes = (self.membrane >= cfg.threshold).astype(float)
        
        # 重置
        self.membrane[self.spikes > 0] = 0
        
        return self.spikes
    
    def forward(self, inputs: np.ndarray) -> np.ndarray:
        """前向传播
        
        Args:
            inputs: 输入序列 (time, n_inputs)
            
        Returns:
            output: 输出
        """
        self.reset_state()
        
        # 输出累积
        output_accum = np.zeros(self.config.n_outputs)
        
        for t in range(len(inputs)):
            spikes = self.step(inputs[t])
            output_accum += self.W_out @ spikes
            
        return output_accum / len(inputs)
    
    def project_to_mode_space(self, activity: np.ndarray) -> np.ndarray:
        """投影到模式空间
        
        Args:
            activity: 神经活动 (time, n_neurons)
            
        Returns:
            mode_activity: 模式空间活动 (time, n_modes)
        """
        # 投影到输入模式
        return activity @ self.decomposition.phi.T
    
    def extract_neural_manifold(self, 
                                 activities: np.ndarray,
                                 n_components: int = 3) -> Dict:
        """提取神经流形
        
        Args:
            activities: 神经活动集合 (n_samples, time, n_neurons)
            n_components: 主成分数量
            
        Returns:
            manifold: 流形信息
        """
        # 展平
        X = activities.reshape(-1, self.config.n_neurons)
        
        # PCA
        from sklearn.decomposition import PCA
        pca = PCA(n_components=n_components)
        manifold_coords = pca.fit_transform(X)
        
        return {
            'coordinates': manifold_coords,
            'explained_variance': pca.explained_variance_ratio_,
            'components': pca.components_
        }


class ModeScoreTrainer:
    """模式-评分空间训练器"""
    
    def __init__(self, network: SpikingModeNetwork, config: SpikingModeConfig):
        """
        Args:
            network: 脉冲模式网络
            config: 配置
        """
        self.network = network
        self.config = config
        
    def compute_loss(self, output: np.ndarray, target: np.ndarray) -> float:
        """计算损失
        
        Args:
            output: 网络输出
            target: 目标
            
        Returns:
            loss: 损失值
        """
        # 交叉熵损失
        exp_output = np.exp(output - np.max(output))
        softmax = exp_output / np.sum(exp_output)
        
        return -np.log(softmax[target] + 1e-10)
    
    def train_mode_scores(self, 
                          inputs: np.ndarray, 
                          target: int,
                          n_iterations: int = 100) -> Dict:
        """训练模式评分
        
        Args:
            inputs: 输入
            target: 目标类别
            n_iterations: 迭代次数
            
        Returns:
            training_info: 训练信息
        """
        losses = []
        
        for it in range(n_iterations):
            # 前向传播
            output = self.network.forward(inputs)
            
            # 计算损失
            loss = self.compute_loss(output, target)
            losses.append(loss)
            
            # 梯度估计（简化）
            # 更新评分
            for i in range(self.config.n_modes):
                # 扰动
                delta = np.random.randn() * 0.01
                old_score = self.network.decomposition.scores[i]
                
                self.network.decomposition.scores[i] += delta
                output_perturbed = self.network.forward(inputs)
                loss_perturbed = self.compute_loss(output_perturbed, target)
                
                # 梯度近似
                grad = (loss_perturbed - loss) / delta
                
                # 恢复并更新
                self.network.decomposition.scores[i] = old_score - self.config.learning_rate * grad
                
        return {
            'final_loss': losses[-1],
            'loss_history': losses
        }
    
    def train_modes(self,
                    train_data: List[Tuple[np.ndarray, int]],
                    n_epochs: int = 10) -> Dict:
        """训练模式和评分
        
        Args:
            train_data: 训练数据 [(inputs, target), ...]
            n_epochs: 训练轮数
            
        Returns:
            training_info: 训练信息
        """
        epoch_losses = []
        
        for epoch in range(n_epochs):
            epoch_loss = 0
            
            for inputs, target in train_data:
                # 训练评分
                info = self.train_mode_scores(inputs, target, n_iterations=1)
                epoch_loss += info['final_loss']
                
            epoch_losses.append(epoch_loss / len(train_data))
            
        return {
            'final_loss': epoch_losses[-1],
            'loss_history': epoch_losses
        }


def visualize_neural_manifold(network: SpikingModeNetwork,
                               activities: np.ndarray):
    """可视化神经流形"""
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    
    # 提取流形
    manifold = network.extract_neural_manifold(activities)
    coords = manifold['coordinates']
    
    fig = plt.figure(figsize=(12, 5))
    
    # 3D 流形
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.scatter(coords[:, 0], coords[:, 1], coords[:, 2], 
                c=np.arange(len(coords)), cmap='viridis', alpha=0.6)
    ax1.set_xlabel('PC1')
    ax1.set_ylabel('PC2')
    ax1.set_zlabel('PC3')
    ax1.set_title('Neural Manifold in Mode Space')
    
    # 解释方差
    ax2 = fig.add_subplot(122)
    variance = manifold['explained_variance']
    ax2.bar(range(len(variance)), variance)
    ax2.set_xlabel('Principal Component')
    ax2.set_ylabel('Explained Variance Ratio')
    ax2.set_title('Variance Explained by Components')
    
    plt.tight_layout()
    plt.savefig('spiking_mode_manifold.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    return 'spiking_mode_manifold.png'


def compare_training_cost(config: SpikingModeConfig) -> Dict:
    """比较训练成本
    
    Args:
        config: 配置
        
    Returns:
        comparison: 比较结果
    """
    n_neurons = config.n_neurons
    n_modes = config.n_modes
    
    # 传统 SNN
    traditional_params = n_neurons * n_neurons  # 全连接循环
    
    # 模式 SNN
    mode_params = 2 * n_modes * n_neurons + n_modes  # phi, psi, scores
    
    reduction = 1 - mode_params / traditional_params
    
    return {
        'traditional_params': traditional_params,
        'mode_params': mode_params,
        'reduction': reduction,
        'compression_ratio': traditional_params / mode_params
    }


# 使用示例
def example_spiking_mode_network():
    """示例：脉冲模式网络"""
    print("="*60)
    print("脉冲模式神经网络框架")
    print("="*60)
    
    # 配置
    config = SpikingModeConfig(
        n_neurons=100,
        n_modes=10
    )
    
    # 创建网络
    network = SpikingModeNetwork(config)
    
    # 比较训练成本
    cost = compare_training_cost(config)
    print(f"\n训练成本比较:")
    print(f"  传统 SNN 参数: {cost['traditional_params']:,}")
    print(f"  模式 SNN 参数: {cost['mode_params']:,}")
    print(f"  参数减少: {cost['reduction']:.1%}")
    print(f"  压缩比: {cost['compression_ratio']:.1f}x")
    
    # Hopfield 分解
    decomp = network.decomposition
    print(f"\nHopfield 分解:")
    print(f"  模式数量: {config.n_modes}")
    print(f"  有效秩: {decomp.compute_effective_rank()}")
    
    # 重建权重
    W = decomp.reconstruct_weight()
    print(f"\n权重矩阵:")
    print(f"  形状: {W.shape}")
    print(f"  谱半径: {np.max(np.abs(np.linalg.eigvals(W))):.3f}")
    
    print(f"\n关键优势:")
    print(f"  ✅ 显著降低训练成本")
    print(f"  ✅ 透明的模式解释")
    print(f"  ✅ 低维吸引子结构")
    
    return network


## Activation Keywords
- 脉冲模式网络
- Hopfield分解
- SNN训练加速
- 神经流形
- spiking mode
- Hopfield decomposition
- neural manifold
- attractor dynamics

## Tools Used
- numpy
- sklearn

## Instructions for Agents
1. 理解 Hopfield 分解：W = Phi @ S @ Psi^T
2. 在模式-评分空间训练，而非直接训练权重
3. 使用低秩近似控制模型复杂度
4. 投影神经活动到模式空间分析流形
5. 权衡模式数量与表达能力

## Examples
```python
# 脉冲模式网络使用示例
from spiking_mode_neural_networks import (
    SpikingModeNetwork, SpikingModeConfig, ModeScoreTrainer
)

# 1. 配置
config = SpikingModeConfig(
    n_neurons=100,
    n_modes=10,    # 少量模式即可
)

# 2. 创建网络
network = SpikingModeNetwork(config)

# 3. 查看训练成本降低
from spiking_mode_neural_networks import compare_training_cost
cost = compare_training_cost(config)
print(f"参数减少: {cost['reduction']:.1%}")

# 4. 训练
trainer = ModeScoreTrainer(network, config)
trainer.train_modes(train_data, n_epochs=10)

# 5. 提取神经流形
manifold = network.extract_neural_manifold(activities)
print(f"解释方差: {manifold['explained_variance']}")
```

if __name__ == "__main__":
    example_spiking_mode_network()
```

## Related Skills

- `noisy-snn-learning` - 噪声驱动 SNN 学习
- `delay-adaptive-snn-classifier` - 延迟自适应 SNN
- `multi-plasticity-snn-training` - 多重可塑性 SNN 训练

## References

- arXiv:2310.14621 - Spiking mode-based neural networks
- Phys. Rev. E 110, 024306 (2024)
- DOI: 10.1103/PhysRevE.110.024306
- Topics: Neurons and Cognition (q-bio.NC), Disordered Systems (cond-mat.dis-nn), AI (cs.AI)