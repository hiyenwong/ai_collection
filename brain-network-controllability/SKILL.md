---
name: brain-network-controllability
description: "结构脑网络可控性分析实用指南。基于网络控制理论计算平均可控性、模态可控性、最小控制能量等指标，研究脑网络状态转移能力。 触发词: brain, network, controllability, 脑网络, 可控性"
---

# 脑网络可控性分析

## 概述
结构脑网络可控性分析实用指南。基于网络控制理论计算平均可控性、模态可控性、最小控制能量等指标，研究脑网络状态转移能力。

## 核心概念

1. **网络控制理论 (Network Control Theory)**
2. **平均可控性 (Average Controllability)**
3. **模态可控性 (Modal Controllability)**
4. **控制能量 (Control Energy)**
5. **最小控制节点集 (Minimum Dominating Set)**

## 应用领域

- 脑刺激靶点优化 (TMS/tDCS)
- 神经疾病诊断和治疗
- 脑机接口 (BCI) 优化
- 认知功能网络分析

## 方法论与实现


## 核心计算方法

### 1. 平均可控性
```python
import numpy as np
from scipy.linalg import solve_discrete_are, expm

def average_controllability(A, C):
    '''
    计算脑网络的平均可控性
    A: 邻接矩阵 (N x N)
    C: 控制输入矩阵 (N x K)
    '''
    # 使用可控性格拉姆矩阵的迹
    N = A.shape[0]
    W = np.zeros((N, N))
    
    for t in range(100):  # 时间范围
        W += np.linalg.matrix_power(A, t) @ C @ C.T @ np.linalg.matrix_power(A.T, t)
    
    # 平均可控性 = trace(W^-1)
    avg_cont = np.trace(np.linalg.inv(W + 1e-6 * np.eye(N)))
    return avg_cont
```

### 2. 模态可控性
```python
def modal_controllability(A, C):
    '''
    计算模态可控性 - 评估每个特征模态的可控程度
    '''
    eigenvalues, eigenvectors = np.linalg.eig(A)
    N = A.shape[0]
    
    modal_ctrl = []
    for i, lam in enumerate(eigenvalues):
        v = eigenvectors[:, i]  # 右特征向量
        w = eigenvectors[:, i]  # 左特征向量 (简化)
        
        # 模态可控性 = |w^H C|^2
        mode_ctrl = np.abs(w.conj().T @ C)**2
        modal_ctrl.append(mode_ctrl)
    
    return np.array(modal_ctrl)
```

### 3. 最小控制能量
```python
def optimal_control_energy(A, B, x0, xf, T):
    '''
    计算从初始状态 x0 到目标状态 xf 的最小控制能量
    '''
    # 离散时间系统的最优控制
    # 使用动态规划或黎卡提方程求解
    
    N = A.shape[0]
    # 简化的能量估计
    diff = xf - np.linalg.matrix_power(A, T) @ x0
    energy = np.linalg.norm(diff)**2
    
    return energy
```

## 实践应用

### 脑刺激优化
1. 识别网络中的最优控制节点
2. 计算达到目标脑状态所需的刺激强度
3. 评估不同刺激方案的能量效率

### 神经疾病分析
- 阿尔茨海默病: 海马区控制节点受损
- 帕金森病: 基底节网络可控性降低
- 抑郁症: 默认模式网络控制异常


## 激活关键词
- brain, network, controllability, 脑网络, 可控性
- neuroscience
- brain
- neural

---
*该 skill 基于神经科学领域知识创建（arXiv API 暂时不可用）*
