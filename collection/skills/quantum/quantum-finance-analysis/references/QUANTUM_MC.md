# Quantum Monte Carlo for Finance

## 经典蒙特卡洛瓶颈

金融蒙特卡洛模拟：
- VaR 估计：需要大量场景采样
- 衍生品定价：价格路径模拟
- 风险度量：统计量估计

经典复杂度：O(N) 采样，N = 10^6 - 10^9

## 量子加速原理

### Amplitude Estimation

量子振幅估计提供 **二次加速**：

```
经典 MC：估计精度 ε 需要 O(1/ε^2) 采样
量子 AE：估计精度 ε 需要 O(1/ε) 量子门操作

加速比：O(√N) vs O(N)
```

### 量子随机游走

```python
# 价格路径模拟
class QuantumPriceWalk:
    def __init__(self, n_steps, drift, volatility):
        self.n_steps = n_steps
        self.params = (drift, volatility)
    
    def quantum_simulate(self):
        # 量子随机游走编码价格路径
        # 所有路径并行演化
        # 振幅估计提取期望值
```

## VaR/CVaR 量子估计

### 算法框架

```python
def quantum_var_estimation(portfolio_value_distribution, confidence_level=0.99):
    """
    量子 VaR 估计
    
    步骤:
    1. 编码损失分布到量子态
    2. 振幅估计测量损失概率
    3. 提取 VaR（分位数）
    """
    
    # 1. 初始化量子态表示损失分布
    qc = initialize_loss_distribution(portfolio_value_distribution)
    
    # 2. 应用振幅估计
    amplitude_estimator = AmplitudeEstimation(accuracy_target=0.01)
    result = amplitude_estimator.estimate(qc)
    
    # 3. 从估计结果提取 VaR
    var = extract_var_from_quantum(result, confidence_level)
    
    return var
```

### QRNG 增强方案

```python
# 量子随机数生成器增强经典 MC
def qrng_enhanced_monte_carlo(n_samples, model):
    """
    QRNG + 经典 MC 混合方案
    
    优势：
    - QRNG 提供真随机性
    - 硬件已实用化
    - 提高模拟精度
    """
    from qrng import QRNG  # 假设 QRNG API
    
    qrng = QRNG()
    random_numbers = qrng.generate(n_samples)
    
    # 使用量子随机数运行经典 MC
    losses = model.simulate(random_numbers)
    
    var = np.percentile(losses, 99)
    cvar = np.mean(losses[losses >= var])
    
    return var, cvar
```

## 衍生品定价

### 期权定价量子化

```python
def quantum_option_pricing(S, K, T, r, sigma, option_type='call'):
    """
    量子期权定价
    
    使用振幅估计加速蒙特卡洛
    """
    
    # 经典 Black-Scholes 对比基准
    bs_price = black_scholes(S, K, T, r, sigma, option_type)
    
    # 量子蒙特卡洛定价
    n_qubits = int(np.log2(n_paths))
    
    # 编码价格路径
    qc = encode_price_paths(S, sigma, T, n_qubits)
    
    # 振幅估计期望值
    quantum_price = amplitude_estimate_payoff(qc, K, option_type)
    
    return {
        'classical_bs': bs_price,
        'quantum_mc': quantum_price,
        'acceleration': 'O(√N) vs O(N)'
    }
```

## 当前硬件约束

| 约束 | 影响 | 缓解方案 |
|-----|------|---------|
| 量子比特数 | 路径数限制 | 分层采样 |
| 电路深度 | 模拟精度 | 低深度算法 |
| 噪声 | 结果偏差 | 误差 mitigation |
| 连通性 | 编码效率 | Swap 网络 |

## 实用化建议

1. **QRNG 最成熟**：量子随机数生成已商业化
2. **混合方案优先**：量子初始化 + 经典迭代
3. **问题规模阈值**：小问题经典更优，大问题量子优势显现
4. **NISQ 适配**：低深度量子电路设计