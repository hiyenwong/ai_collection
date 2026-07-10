---
name: nonequilibrium-brain-dynamics
description: Nonequilibrium physics framework for brain dynamics analysis. Covers entropy production, time-irreversibility, broken detailed balance, and nonequilibrium computation in neural systems. Use when analyzing brain dynamics from nonequilibrium statistical physics perspective, measuring entropy production, studying time-irreversibility in neural data, or investigating consciousness/cognitive complexity through nonequilibrium metrics.
user-invocable: true
---

# Nonequilibrium Brain Dynamics

**来源论文：** arXiv:2504.12188 (v2, 2025-10-16) - "Nonequilibrium physics of brain dynamics"
**期刊发表：** Physics Reports (2026), Vol 1152, Pages 1-43
**DOI:** 10.1016/j.physrep.2025.10.003
**作者:** Ramón Nartallo-Kaluarachchi, Morten L. Kringelbach, Gustavo Deco, Renaud Lambiotte, Alain Goriely

## 核心方法论

### 1. 核心洞察

大脑动力学展现出**时间不可逆性 (time-irreversibility)** 和**细致平衡破缺 (broken detailed balance)**，表明大脑运行在非平衡稳态 (nonequilibrium stationary state) 中。非平衡程度（通过熵产生或不可逆性衡量）是认知复杂性和意识的关键标志。

### 2. 数学范式

#### 连续状态空间

**Langevin 动力学：**
```
dx = f(x)dt + σ dW

细致平衡条件：∇ × (f/σ²) = 0
破缺时：系统处于非平衡态
```

**熵产生率 (Entropy Production Rate)：**
```
EP = ⟨f · (σ⁻² f)⟩ - ⟨∇ · f⟩

物理意义：时间反演不对称性的量化度量
```

**时间不可逆性度量：**
```
γ_τ = ⟨x(t)[x(t+τ) - x(t-τ)]⟩

对于可逆过程 γ_τ = 0，γ_τ ≠ 0 表明非平衡
```

#### 离散状态空间

**主方程 (Master Equation)：**
```
dp_i/dt = Σ_j (W_{ij} p_j - W_{ji} p_i)

Kolmogorov 判据（细致平衡）：
对任意环 i→j→k→...→i，有 Π W_{ij} = Π W_{ji}
```

**环流 (Cycle Currents)：**
- 非零环流 → 非平衡态
- 环流大小 = 非平衡强度

### 3. 无模型方法 (Model-Free)

**不可逆性分析：**
- 从观测数据直接估计时间不可逆性
- 无需假设生成模型
- 适用于 EEG、fMRI、MEA 数据

**熵产生估计：**
- 基于轨迹概率比
- EP = k_B Σ p(x) log[p(x)/p(x̄)] 其中 x̄ 为时间反演轨迹
- 高 EP → 高认知复杂度

### 4. 基于模型方法 (Model-Based)

**全脑模型：**
- 整合结构连接 (DTI) 与局部动力学
- Hopf bifurcation model, Kuramoto model
- 量化模型预测与实证数据的不可逆性差异

**神经脉冲序列分析：**
- 将脉冲序列视为离散随机过程
- 估计脉冲间的非平衡环流
- 识别非平衡计算模式

### 5. 关键发现

| 发现 | 意义 |
|------|------|
| 意识水平 ↑ → EP ↑ | 非平衡程度与意识状态相关 |
| 静息态 ≠ 平衡态 | 大脑即使在静息时也持续消耗能量维持非平衡 |
| 不同脑区 EP 不同 | 联合皮层 EP 高于感觉皮层 |
| 病理状态 EP 改变 | 精神分裂症、癫痫等显示异常 EP 模式 |

### 6. 非平衡计算

**信息处理视角：**
- 非平衡态允许方向性信息流
- 细致平衡破缺 → 计算能力
- 平衡系统 = 有限计算能力

**Landauer 原理扩展：**
- 信息擦除需要最小能量耗散
- 大脑信息处理必然伴随非平衡

## Python 实现

```python
import numpy as np
from typing import Tuple, Optional

def time_irreversibility(signal: np.ndarray, tau: int = 1) -> float:
    """
    计算时间不可逆性度量 γ_τ
    
    γ_τ = ⟨x(t)[x(t+τ) - x(t-τ)]⟩
    
    Args:
        signal: 时间序列 (T,)
        tau: 时间延迟
    Returns:
        不可逆性标量值
    """
    T = len(signal)
    return np.mean(
        signal[tau:T-tau] * (signal[2*tau:] - signal[:T-2*tau])
    )

def entropy_production_rate_gaussian(
    signal: np.ndarray,
    lag: int = 1
) -> float:
    """
    估计高斯过程的熵产生率
    
    基于滞后协方差的不对称性
    
    Args:
        signal: 多元时间序列 (T, D)
        lag: 时间滞后
    Returns:
        熵产生率估计
    """
    T, D = signal.shape
    
    # 计算滞后协方差矩阵
    C_fwd = np.zeros((D, D))
    C_bwd = np.zeros((D, D))
    
    for t in range(lag, T):
        C_fwd += np.outer(signal[t], signal[t-lag])
        C_bwd += np.outer(signal[t-lag], signal[t])
    
    C_fwd /= (T - lag)
    C_bwd /= (T - lag)
    
    # 对称部分和反对称部分
    C_sym = (C_fwd + C_bwd) / 2
    C_asym = (C_fwd - C_bwd) / 2
    
    # 熵产生 ≈ Tr(C_asym² C_sym⁻¹) / 2
    try:
        C_sym_inv = np.linalg.inv(C_sym)
        ep = 0.5 * np.trace(C_asym @ C_sym_inv @ C_asym.T @ C_sym_inv)
        return max(0, ep)  # EP ≥ 0
    except np.linalg.LinAlgError:
        return 0.0

def kolmogorov_criterion(transition_matrix: np.ndarray) -> Tuple[bool, float]:
    """
    检验 Kolmogorov 细致平衡判据
    
    对所有三元环检验 W_ij * W_jk * W_ki = W_ik * W_kj * W_ji
    
    Args:
        transition_matrix: 转移矩阵 (N, N)
    Returns:
        (satisfies_detailed_balance, max_violation)
    """
    N = transition_matrix.shape[0]
    max_violation = 0.0
    
    for i in range(N):
        for j in range(N):
            if i == j: continue
            for k in range(N):
                if k == i or k == j: continue
                
                fwd = transition_matrix[i,j] * transition_matrix[j,k] * transition_matrix[k,i]
                bwd = transition_matrix[i,k] * transition_matrix[k,j] * transition_matrix[j,i]
                
                if fwd + bwd > 0:
                    violation = abs(np.log(fwd + 1e-300) - np.log(bwd + 1e-300))
                    max_violation = max(max_violation, violation)
    
    return max_violation < 1e-6, max_violation

def cycle_currents(transition_matrix: np.ndarray) -> np.ndarray:
    """
    估计离散状态系统的环流
    
    J_ij = p_i * W_ij - p_j * W_ji
    
    Args:
        transition_matrix: 转移矩阵 (N, N)
    Returns:
        环流矩阵 (N, N), J_ij > 0 表示 i→j 方向净流
    """
    # 稳态分布
    eigenvalues, eigenvectors = np.linalg.eig(transition_matrix.T)
    stationary = np.real(eigenvectors[:, np.argmax(np.real(eigenvalues))])
    stationary /= stationary.sum()
    stationary = np.abs(stationary)
    stationary /= stationary.sum()
    
    N = transition_matrix.shape[0]
    J = np.zeros((N, N))
    
    for i in range(N):
        for j in range(N):
            J[i,j] = stationary[i] * transition_matrix[i,j] - \
                     stationary[j] * transition_matrix[j,i]
    
    return J
```

## 数据分析流程

### 步骤 1: 数据预处理
- 对 fMRI: 去趋势、滤波、标准化
- 对 EEG/MEA: 带通滤波、artifact rejection
- 离散化（如需要）：K-means 或 Gaussian mixture

### 步骤 2: 不可逆性估计
- 无模型：直接计算 γ_τ
- 模型：拟合动力学模型后计算 EP

### 步骤 3: 统计检验
- 置换检验：打乱时间顺序生成零分布
- 比较实证 γ_τ 与零分布

### 步骤 4: 解释
- 高 EP 区域 → 高信息处理区域
- EP 变化 → 状态转变（如意识水平变化）

## 激活关键词
- nonequilibrium brain
- entropy production brain
- time-irreversibility
- broken detailed balance
- non-equilibrium neural dynamics
- nonequilibrium statistical physics neuroscience
- 非平衡脑动力学
- 熵产生
- 时间不可逆性
- 细致平衡破缺

## Related Skills
- `generative-brain-dynamics-models` - 脑动力学生成模型
- `kuramoto-brain-network` - Kuramoto 模型
- `brain-stimulation-dynamics-state` - 脑刺激动力学