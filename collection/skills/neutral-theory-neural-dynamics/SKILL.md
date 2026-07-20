---
name: neutral-theory-neural-dynamics
description: 中性理论无标度神经动力学方法论。神经元雪崩无标度行为不源于临界性，而是来自中性漂移。适用于脑网络雪崩分析、临界性研究、神经动力学建模。触发词：中性理论、无标度、神经元雪崩、临界性、neutral theory、scale-free、neural avalanche。
user-invocable: true
---

# Neutral Theory Neural Dynamics - 中性理论神经动力学

## 核心思想

神经元雪崩的无标度行为不源于临界性，而是来自中性漂移——类似群体遗传学中性理论。

**来源：** arXiv:1703.05079
**效用：** 1.0

---

## 方法论

### 核心观点

| 传统观点 | 中性理论观点 |
|---------|-------------|
| 雪崩无标度来自临界性 | 来自中性漂移 |
| 系统处于相变边缘 | 系统远离临界点 |
| 功能优势 | 人口涨落驱动 |

### 中性漂移机制

```python
import numpy as np

class NeutralNeuralDynamics:
    """中性理论神经动力学模型"""
    
    def __init__(self, n_neurons=1000, connection_prob=0.1):
        self.n = n_neurons
        self.p = connection_prob
        
        # 随机连接矩阵
        self.W = (np.random.rand(n_neurons, n_neurons) < connection_prob).astype(float)
        self.W *= np.random.rand(n_neurons, n_neurons)  # 随机权重
        
        # 状态
        self.state = np.zeros(n_neurons)
    
    def neutral_drift(self, steps=1000):
        """中性漂移模拟"""
        activity_trace = []
        
        for _ in range(steps):
            # 人口涨落驱动的中性漂移
            perturbation = np.random.randn(self.n) * 0.1
            
            # 边际传播
            response = self.W @ self.state + perturbation
            
            # 活跃神经元
            active = response > np.percentile(response, 90)
            
            # 记录雪崩大小
            avalanche_size = np.sum(active)
            activity_trace.append(avalanche_size)
            
            # 更新状态（中性漂移）
            self.state = response * 0.1
        
        return np.array(activity_trace)
    
    def analyze_power_law(self, trace):
        """分析幂律分布"""
        sizes, counts = np.unique(trace, return_counts=True)
        probs = counts / len(trace)
        
        # 幂律拟合
        mask = (sizes > 1) & (probs > 0)
        log_sizes = np.log(sizes[mask])
        log_probs = np.log(probs[mask])
        
        # 线性拟合
        slope, intercept = np.polyfit(log_sizes, log_probs, 1)
        
        return slope  # 幂律指数
```

---

## 关键发现

1. **非临界性：** 无标度行为不依赖临界点
2. **中性漂移：** 人口涨落驱动边际传播
3. **雪崩重叠：** 雪崩可同时共存

---

## 应用场景

- 脑网络雪崩分析
- 临界性假设检验
- 神经动力学建模

---

## Activation Keywords
- 中性理论
- 无标度
- 神经元雪崩
- 临界性
- neutral theory
- scale-free

## Tools Used
- numpy
- matplotlib

## Instructions for Agents
1. 理解中性漂移机制
2. 区分临界性与中性理论
3. 分析雪崩幂律分布

## Examples
分析EEG数据中的雪崩分布，检验是否来自中性漂移而非临界性。

## 参考文献
- arXiv:1703.05079