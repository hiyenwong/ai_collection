---
name: rnn-task-degradation-analysis
description: RNN权重初始化、解的多样性与性能退化分析框架。研究不同初始化如何收敛到不同动力学解，分析网络规模、时间间隔、连接损伤对性能的优雅退化影响。适用于计算神经科学、RNN模型分析、脑皮层建模。触发词：RNN初始化、解多样性、性能退化、网络鲁棒性、优雅退化、weight initialization、degradation analysis、RNN dynamics、graceful degradation。
user-invocable: true
---

# RNN 任务退化分析框架

**来源论文：** arXiv:1906.01094 - Exploring weight initialization, diversity of solutions, and degradation in recurrent neural networks trained for temporal and decision-making tasks

## 核心方法论

### 1. 解的多样性分析

不同初始化 → 不同动力学解 → 相同任务表现

**关键发现：**
- 多个稳定解可以解决相同的计算任务
- 解的动力学轨迹不同但功能等效
- 对生物神经网络的启示：不同神经元群体可以实现相同功能

### 2. 性能退化维度

| 维度 | 退化模式 |
|------|----------|
| 网络规模 ↓ | 性能优雅下降 |
| 时间间隔 ↑ | 时序任务精度下降 |
| 连接损伤 ↑ | 鲁棒性测试 |

### 3. 任务参数化框架

统一的任务描述框架：
- 输入时序结构
- 目标输出定义
- 时间约束条件

## Python 实现

```python
import numpy as np
import torch
import torch.nn as nn
from typing import Dict, List, Tuple, Optional, Callable
from dataclasses import dataclass, field
from collections import defaultdict
import matplotlib.pyplot as plt


@dataclass
class RNNConfig:
    """RNN 配置"""
    input_size: int = 1
    hidden_size: int = 100
    output_size: int = 1
    dt: float = 10.0          # 时间步长 (ms)
    tau: float = 100.0        # 时间常数 (ms)
    
    # 训练参数
    learning_rate: float = 0.01
    n_epochs: int = 500
    batch_size: int = 32
    
    # 损伤参数
    damage_fraction: float = 0.0  # 连接损伤比例


@dataclass
class TaskConfig:
    """任务配置"""
    name: str = "delay_match"
    duration: float = 1000.0     # 任务时长 (ms)
    stimulus_duration: float = 100.0
    delay_duration: float = 500.0
    response_duration: float = 200.0
    n_inputs: int = 2
    n_outputs: int = 1


class ContinuousTimeRNN(nn.Module):
    """连续时间 RNN"""
    
    def __init__(self, config: RNNConfig):
        super().__init__()
        self.config = config
        
        # 权重矩阵
        self.W_rec = nn.Parameter(
            torch.randn(config.hidden_size, config.hidden_size) * 0.1
        )
        self.W_in = nn.Parameter(
            torch.randn(config.hidden_size, config.input_size) * 0.1
        )
        self.W_out = nn.Parameter(
            torch.randn(config.output_size, config.hidden_size) * 0.1
        )
        
        # 偏置
        self.b_rec = nn.Parameter(torch.zeros(config.hidden_size))
        self.b_out = nn.Parameter(torch.zeros(config.output_size))
        
        # 时间常数
        self.alpha = config.dt / config.tau
        
    def forward(self, inputs: torch.Tensor, 
                initial_state: torch.Tensor = None) -> Tuple[torch.Tensor, torch.Tensor]:
        """
        Args:
            inputs: 输入序列 (batch, time, input_size)
            initial_state: 初始隐藏状态
            
        Returns:
            outputs: 输出序列 (batch, time, output_size)
            hidden: 最终隐藏状态
        """
        batch_size, seq_len, _ = inputs.shape
        
        if initial_state is None:
            h = torch.zeros(batch_size, self.config.hidden_size, device=inputs.device)
        else:
            h = initial_state
            
        outputs = []
        
        for t in range(seq_len):
            # 连续时间更新
            # dh/dt = -h/tau + W_rec @ tanh(h) + W_in @ u + b
            h = h + self.alpha * (
                -h + torch.tanh(h @ self.W_rec.T + self.b_rec) +
                inputs[:, t] @ self.W_in.T
            )
            
            # 输出
            out = torch.tanh(h @ self.W_out.T + self.b_out)
            outputs.append(out)
            
        outputs = torch.stack(outputs, dim=1)
        return outputs, h
    
    def apply_damage(self, fraction: float):
        """应用连接损伤
        
        Args:
            fraction: 损伤比例 (0-1)
        """
        if fraction <= 0:
            return
            
        with torch.no_grad():
            mask = torch.rand_like(self.W_rec) > fraction
            self.W_rec *= mask.float()
            
    def get_effective_size(self) -> int:
        """计算有效网络大小（非零连接）"""
        with torch.no_grad():
            return (self.W_rec.abs() > 1e-6).sum().item()


class TaskDegradationAnalyzer:
    """任务退化分析器"""
    
    def __init__(self, rnn_config: RNNConfig, task_config: TaskConfig):
        self.rnn_config = rnn_config
        self.task_config = task_config
        
    def generate_task_data(self, n_samples: int = 100) -> Tuple[torch.Tensor, torch.Tensor]:
        """生成任务数据
        
        Returns:
            inputs: 输入序列
            targets: 目标输出
        """
        task = self.task_config
        rnn = self.rnn_config
        
        n_steps = int(task.duration / rnn.dt)
        inputs = torch.zeros(n_samples, n_steps, rnn.input_size)
        targets = torch.zeros(n_samples, n_steps, task.n_outputs)
        
        for i in range(n_samples):
            # 随机选择刺激
            stimulus_channel = np.random.randint(0, task.n_inputs)
            
            # 刺激阶段
            stim_start = 0
            stim_end = int(task.stimulus_duration / rnn.dt)
            inputs[i, stim_start:stim_end, stimulus_channel] = 1.0
            
            # 延迟阶段
            delay_end = stim_end + int(task.delay_duration / rnn.dt)
            
            # 响应阶段
            response_start = delay_end
            response_end = response_start + int(task.response_duration / rnn.dt)
            
            # 目标：在响应阶段输出 1（如果匹配）
            targets[i, response_start:response_end, 0] = 1.0
            
        return inputs, targets
    
    def train_rnn(self, n_initializations: int = 5) -> List[Dict]:
        """训练多个不同初始化的 RNN
        
        Args:
            n_initializations: 初始化数量
            
        Returns:
            results: 训练结果列表
        """
        results = []
        
        for init_id in range(n_initializations):
            # 创建新 RNN
            rnn = ContinuousTimeRNN(self.rnn_config)
            optimizer = torch.optim.Adam(rnn.parameters(), 
                                         lr=self.rnn_config.learning_rate)
            
            # 生成数据
            inputs, targets = self.generate_task_data(
                n_samples=self.rnn_config.batch_size * 10
            )
            
            # 训练
            losses = []
            for epoch in range(self.rnn_config.n_epochs):
                # 随机采样
                idx = np.random.choice(len(inputs), self.rnn_config.batch_size)
                batch_inputs = inputs[idx]
                batch_targets = targets[idx]
                
                # 前向传播
                outputs, _ = rnn(batch_inputs)
                
                # 损失
                loss = nn.MSELoss()(outputs, batch_targets)
                losses.append(loss.item())
                
                # 反向传播
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                
            # 记录结果
            results.append({
                'init_id': init_id,
                'rnn': rnn,
                'final_loss': losses[-1],
                'loss_history': losses,
                'weights': {
                    'W_rec': rnn.W_rec.detach().clone(),
                    'W_in': rnn.W_in.detach().clone(),
                    'W_out': rnn.W_out.detach().clone()
                }
            })
            
        return results
    
    def analyze_diversity(self, training_results: List[Dict]) -> Dict:
        """分析解的多样性
        
        Args:
            training_results: 训练结果
            
        Returns:
            diversity_metrics: 多样性指标
        """
        n = len(training_results)
        
        # 提取权重
        weights = [r['weights']['W_rec'].numpy() for r in training_results]
        
        # 计算权重相似度
        similarity_matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                # 余弦相似度
                w_i = weights[i].flatten()
                w_j = weights[j].flatten()
                similarity_matrix[i, j] = np.dot(w_i, w_j) / (
                    np.linalg.norm(w_i) * np.linalg.norm(w_j) + 1e-8
                )
                
        # 分析动力学
        dynamics_metrics = []
        for r in training_results:
            rnn = r['rnn']
            # 计算谱半径
            with torch.no_grad():
                eigenvalues = torch.linalg.eigvals(rnn.W_rec)
                spectral_radius = torch.max(torch.abs(eigenvalues)).item()
            dynamics_metrics.append({
                'spectral_radius': spectral_radius,
                'final_loss': r['final_loss']
            })
            
        return {
            'weight_similarity': similarity_matrix,
            'dynamics_metrics': dynamics_metrics,
            'mean_similarity': similarity_matrix.mean(),
            'std_similarity': similarity_matrix.std()
        }
    
    def analyze_size_degradation(self, 
                                  size_fractions: List[float] = None) -> Dict:
        """分析网络规模退化
        
        Args:
            size_fractions: 规模比例列表
            
        Returns:
            degradation_results: 退化结果
        """
        if size_fractions is None:
            size_fractions = [1.0, 0.8, 0.6, 0.4, 0.2]
            
        results = {
            'size_fraction': [],
            'performance': [],
            'effective_size': []
        }
        
        for frac in size_fractions:
            # 调整隐藏层大小
            config = RNNConfig(
                hidden_size=int(self.rnn_config.hidden_size * frac)
            )
            
            # 训练
            training_results = self.train_rnn(n_initializations=1)
            performance = 1.0 / (training_results[0]['final_loss'] + 0.1)
            
            results['size_fraction'].append(frac)
            results['performance'].append(performance)
            results['effective_size'].append(config.hidden_size)
            
        return results
    
    def analyze_damage_degradation(self,
                                    damage_levels: List[float] = None) -> Dict:
        """分析连接损伤退化
        
        Args:
            damage_levels: 损伤水平列表
            
        Returns:
            degradation_results: 退化结果
        """
        if damage_levels is None:
            damage_levels = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
            
        # 先训练一个完整的 RNN
        training_results = self.train_rnn(n_initializations=1)
        best_rnn = training_results[0]['rnn']
        
        # 测试数据
        inputs, targets = self.generate_task_data(n_samples=50)
        
        results = {
            'damage_level': [],
            'performance': []
        }
        
        for damage in damage_levels:
            # 复制 RNN
            rnn_copy = ContinuousTimeRNN(self.rnn_config)
            rnn_copy.load_state_dict(best_rnn.state_dict())
            
            # 应用损伤
            rnn_copy.apply_damage(damage)
            
            # 评估
            with torch.no_grad():
                outputs, _ = rnn_copy(inputs)
                loss = nn.MSELoss()(outputs, targets)
                performance = 1.0 / (loss.item() + 0.1)
                
            results['damage_level'].append(damage)
            results['performance'].append(performance)
            
        return results
    
    def analyze_interval_degradation(self,
                                      intervals: List[float] = None) -> Dict:
        """分析时间间隔退化
        
        Args:
            intervals: 延迟间隔列表 (ms)
            
        Returns:
            degradation_results: 退化结果
        """
        if intervals is None:
            intervals = [200, 400, 600, 800, 1000]
            
        results = {
            'interval': [],
            'performance': []
        }
        
        for interval in intervals:
            # 创建新任务配置
            task_config = TaskConfig(
                delay_duration=interval
            )
            
            # 训练
            analyzer = TaskDegradationAnalyzer(self.rnn_config, task_config)
            training_results = analyzer.train_rnn(n_initializations=1)
            
            performance = 1.0 / (training_results[0]['final_loss'] + 0.1)
            
            results['interval'].append(interval)
            results['performance'].append(performance)
            
        return results
    
    def full_degradation_analysis(self) -> Dict:
        """完整退化分析
        
        Returns:
            full_results: 所有退化分析结果
        """
        print("Running full degradation analysis...")
        
        results = {}
        
        # 1. 解多样性
        print("\n1. Analyzing solution diversity...")
        training_results = self.train_rnn(n_initializations=5)
        results['diversity'] = self.analyze_diversity(training_results)
        
        # 2. 规模退化
        print("\n2. Analyzing size degradation...")
        results['size'] = self.analyze_size_degradation()
        
        # 3. 损伤退化
        print("\n3. Analyzing damage degradation...")
        results['damage'] = self.analyze_damage_degradation()
        
        # 4. 间隔退化
        print("\n4. Analyzing interval degradation...")
        results['interval'] = self.analyze_interval_degradation()
        
        return results


def visualize_degradation_results(results: Dict):
    """可视化退化结果
    
    Args:
        results: 退化分析结果
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. 解多样性
    ax = axes[0, 0]
    if 'diversity' in results:
        sim = results['diversity']['weight_similarity']
        im = ax.imshow(sim, cmap='RdYlBu_r', vmin=-1, vmax=1)
        ax.set_title('Weight Similarity Between Solutions')
        ax.set_xlabel('Initialization')
        ax.set_ylabel('Initialization')
        plt.colorbar(im, ax=ax, label='Cosine Similarity')
    
    # 2. 规模退化
    ax = axes[0, 1]
    if 'size' in results:
        ax.plot(results['size']['size_fraction'], 
                results['size']['performance'], 'o-', linewidth=2)
        ax.set_xlabel('Network Size Fraction')
        ax.set_ylabel('Performance')
        ax.set_title('Size Degradation')
        ax.grid(True, alpha=0.3)
    
    # 3. 损伤退化
    ax = axes[1, 0]
    if 'damage' in results:
        ax.plot(results['damage']['damage_level'], 
                results['damage']['performance'], 's-', linewidth=2, color='red')
        ax.set_xlabel('Damage Fraction')
        ax.set_ylabel('Performance')
        ax.set_title('Damage Degradation')
        ax.grid(True, alpha=0.3)
    
    # 4. 间隔退化
    ax = axes[1, 1]
    if 'interval' in results:
        ax.plot(results['interval']['interval'], 
                results['interval']['performance'], '^-', linewidth=2, color='green')
        ax.set_xlabel('Delay Interval (ms)')
        ax.set_ylabel('Performance')
        ax.set_title('Interval Degradation')
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('rnn_degradation_analysis.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    return 'rnn_degradation_analysis.png'


# 使用示例
def example_degradation_analysis():
    """示例：完整退化分析"""
    print("="*60)
    print("RNN 任务退化分析")
    print("="*60)
    
    # 配置
    rnn_config = RNNConfig(
        hidden_size=50,
        n_epochs=200
    )
    task_config = TaskConfig()
    
    # 创建分析器
    analyzer = TaskDegradationAnalyzer(rnn_config, task_config)
    
    # 运行分析
    results = analyzer.full_degradation_analysis()
    
    # 打印结果
    print("\n" + "="*60)
    print("分析结果")
    print("="*60)
    
    if 'diversity' in results:
        div = results['diversity']
        print(f"\n解多样性:")
        print(f"  平均权重相似度: {div['mean_similarity']:.3f}")
        print(f"  相似度标准差: {div['std_similarity']:.3f}")
        
    if 'size' in results:
        print(f"\n规模退化:")
        for i, (frac, perf) in enumerate(zip(
            results['size']['size_fraction'],
            results['size']['performance']
        )):
            print(f"  规模 {frac:.1f}: 性能 {perf:.3f}")
            
    if 'damage' in results:
        print(f"\n损伤退化:")
        for damage, perf in zip(
            results['damage']['damage_level'],
            results['damage']['performance']
        ):
            print(f"  损伤 {damage:.1%}: 性能 {perf:.3f}")
            
    if 'interval' in results:
        print(f"\n间隔退化:")
        for interval, perf in zip(
            results['interval']['interval'],
            results['interval']['performance']
        ):
            print(f"  间隔 {interval}ms: 性能 {perf:.3f}")
    
    # 可视化
    print("\n生成可视化图表...")
    img_path = visualize_degradation_results(results)
    print(f"图表已保存: {img_path}")
    
    return results


## Activation Keywords
- RNN初始化
- 解多样性
- 性能退化
- 网络鲁棒性
- 优雅退化
- weight initialization
- degradation analysis
- RNN dynamics
- graceful degradation
- solution diversity

## Tools Used
- numpy
- torch
- matplotlib

## Instructions for Agents
1. 训练多个不同初始化的 RNN 解决相同任务
2. 分析权重相似度和动力学差异（解多样性）
3. 测试网络规模减小对性能的影响
4. 测试连接损伤对性能的影响
5. 测试时间间隔增加对性能的影响
6. 量化"优雅退化"模式

## Examples
```python
# 退化分析示例
from rnn_task_degradation_analysis import (
    TaskDegradationAnalyzer, RNNConfig, TaskConfig
)

# 1. 配置
rnn_config = RNNConfig(hidden_size=50, n_epochs=200)
task_config = TaskConfig(delay_duration=500)

# 2. 创建分析器
analyzer = TaskDegradationAnalyzer(rnn_config, task_config)

# 3. 完整分析
results = analyzer.full_degradation_analysis()

# 4. 查看解多样性
print(f"权重相似度: {results['diversity']['mean_similarity']:.3f}")

# 5. 查看退化曲线
for frac, perf in zip(
    results['size']['size_fraction'],
    results['size']['performance']
):
    print(f"规模 {frac}: 性能 {perf:.3f}")
```

if __name__ == "__main__":
    example_degradation_analysis()
```

## Related Skills

- `lattice-rnn-pruning` - 格子RNN剪枝
- `cornn-convex-rnn-optimization` - 凸RNN优化
- `heterogeneous-synaptic-dynamics` - 异质性突触动力学

## References

- arXiv:1906.01094 - Exploring weight initialization, diversity of solutions, and degradation in RNNs
- Topics: Neurons and Cognition (q-bio.NC), Neural and Evolutionary Computing (cs.NE)