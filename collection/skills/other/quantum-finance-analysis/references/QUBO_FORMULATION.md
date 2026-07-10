# QUBO Formulation for Financial Optimization

## 数学基础

QUBO（Quadratic Unconstrained Binary Optimization）形式：

```
min f(x) = x^T Q x
其中 x ∈ {0,1}^n, Q ∈ R^{n×n}
```

## Markowitz 投资组合问题

经典形式：
```
min  Σ w_i w_j σ_ij  (方差)
max  Σ w_i μ_i       (收益)
s.t. Σ w_i = 1       (预算约束)
     w_i ≥ 0          (权重约束)
```

量子映射步骤：

### Step 1: 变量离散化

将连续权重 w_i 映射到二进制：

```python
# 每个资产用 k bits 表示权重
# w_i = Σ_j b_{ij} 2^{-j}  (精度 2^{-k})
# 总变量数：n × k (n 个资产，k bits 精度)
```

### Step 2: 目标函数编码

```python
# 风险项：Σ_ij w_i w_j σ_ij → Σ_ij b_i b_j σ_ij'
# 收益项：Σ_i w_i μ_i → Σ_i b_i μ_i'
# 组合：Q = risk_matrix - λ return_vector + penalty_matrix
```

### Step 3: 约束惩罚

```python
# 预算约束 Σ w_i = 1
# 惩罚项：P (Σ w_i - 1)^2 → 加入 Q

# Sector 限制 Σ_{i∈S} w_i ≤ S_max
# 惩罚项：max(0, Σ_{i∈S} w_i - S_max)^2

# 风险上限 w^T Σ w ≤ σ_max
# 惩罚项：max(0, w^T Σ w - σ_max)^2
```

## Q 矩阵构造示例

```python
import numpy as np

def construct_qubo(mu, sigma, lambda_risk, penalty_budget, n_bits=4):
    """
    构造投资组合优化的 QUBO 矩阵
    
    参数:
    - mu: 预期收益向量
    - sigma: 协方差矩阵
    - lambda_risk: 风险权重
    - penalty_budget: 预算约束惩罚系数
    - n_bits: 权重精度位数
    """
    n_assets = len(mu)
    n_vars = n_assets * n_bits
    
    Q = np.zeros((n_vars, n_vars))
    
    # 编码权重：w_i = Σ_j b_{ij} * 2^{-j}
    scale_factors = 2.0 ** np.arange(n_bits)  # [1, 2, 4, 8] for n_bits=4
    
    for i in range(n_assets):
        for j in range(n_bits):
            idx_ij = i * n_bits + j
            
            # 收益项（负号因为最大化）
            Q[idx_ij, idx_ij] -= lambda_risk * mu[i] * scale_factors[j]
            
            # 风险项（自协方差）
            for k in range(n_assets):
                for l in range(n_bits):
                    idx_kl = k * n_bits + l
                    if idx_ij <= idx_kl:  # QUBO 对角化
                        Q[idx_ij, idx_kl] += sigma[i, k] * scale_factors[j] * scale_factors[l]
    
    # 预算约束惩罚
    # Σ_i w_i = Σ_i Σ_j b_{ij} * 2^{-j} ≈ 1
    for i in range(n_assets):
        for j in range(n_bits):
            for k in range(n_assets):
                for l in range(n_bits):
                    idx_ij = i * n_bits + j
                    idx_kl = k * n_bits + l
                    if idx_ij <= idx_kl:
                        Q[idx_ij, idx_kl] += penalty_budget * scale_factors[j] * scale_factors[l]
    
    return Q
```

## 求解方法

### Quantum Annealing (D-Wave)

```python
from dwave.system import DWaveSampler, EmbeddingComposite

def solve_qubo_dwave(Q):
    sampler = EmbeddingComposite(DWaveSampler())
    response = sampler.sample_qubo(Q, num_reads=1000)
    best_solution = response.first.sample
    return best_solution
```

### QAOA (Gate-based)

```python
from qiskit import QuantumCircuit
from qiskit.algorithms import QAOA

def solve_qubo_qaoa(Q, p=3):
    # QAOA depth p
    optimizer = COBYLA()
    qaoa = QAOA(optimizer, quantum_instance, p=p)
    result = qaoa.solve_qubo(Q)
    return result
```

## 实用考虑

1. **精度权衡**：更多 bits → 更精确权重，但变量数增加
2. **惩罚系数**：需调优确保约束满足
3. **问题规模**：当前量子硬件支持 ~100-1000 变量
4. **混合方案**：量子初始化 + 经典优化迭代