---
name: graph-laplacian-denoising
description: "脑连接网络的图拉普拉斯去噪方法。用于提升功能连接估计的可靠性，增强脑状态检测和 BCI 应用的性能。 触发词: graph laplacian, denoising, brain connectivity, 图拉普拉斯, 去噪"
---

# 脑连接网络的图拉普拉斯去噪方法

## 概述
脑连接网络的图拉普拉斯去噪方法。用于提升功能连接估计的可靠性，增强脑状态检测和 BCI 应用的性能。

## 核心概念

1. **图拉普拉斯 (Graph Laplacian)**
2. **谱图理论 (Spectral Graph Theory)**
3. **功能连接去噪 (FC Denoising)**
4. **平滑正则化 (Smoothness Regularization)**
5. **脑状态检测 (Brain State Detection)**

## 应用领域

- fMRI 功能连接去噪
- EEG 连接性增强
- 脑状态分类
- BCI 性能提升

## 方法论与实现


## 理论基础

### 图拉普拉斯矩阵
```python
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh

def compute_graph_laplacian(adjacency):
    '''
    计算图拉普拉斯矩阵 L = D - A
    adjacency: 邻接矩阵 (n_nodes x n_nodes)
    '''
    # 度矩阵
    degree = np.sum(adjacency, axis=1)
    D = np.diag(degree)
    
    # 拉普拉斯矩阵
    L = D - adjacency
    
    return L

def normalized_laplacian(adjacency):
    '''
    归一化拉普拉斯 L_sym = I - D^(-1/2) A D^(-1/2)
    '''
    degree = np.sum(adjacency, axis=1)
    D_inv_sqrt = np.diag(1.0 / np.sqrt(degree + 1e-10))
    
    L_sym = np.eye(len(degree)) - D_inv_sqrt @ adjacency @ D_inv_sqrt
    return L_sym
```

## 去噪方法

### 1. 谱图去噪
```python
def spectral_graph_denoising(fc_matrix, n_eigen=20, alpha=0.5):
    '''
    基于谱图的功能连接去噪
    fc_matrix: 原始功能连接矩阵
    n_eigen: 保留的特征向量数量
    alpha: 平滑系数
    '''
    # 确保对称性
    A = (fc_matrix + fc_matrix.T) / 2
    
    # 计算拉普拉斯
    L = normalized_laplacian(np.abs(A))
    
    # 特征分解
    eigenvalues, eigenvectors = eigsh(L, k=n_eigen, which='SM')
    
    # 在谱域平滑
    # 保留低频成分（平滑信号），抑制高频（噪声）
    smoothed_fc = np.zeros_like(A)
    for i in range(n_eigen):
        coeff = eigenvectors[:, i].T @ A @ eigenvectors[:, i]
        # 低频权重更大
        weight = np.exp(-alpha * eigenvalues[i])
        smoothed_fc += weight * coeff * np.outer(eigenvectors[:, i], eigenvectors[:, i])
    
    return smoothed_fc
```

### 2. 图信号处理去噪
```python
def graph_signal_denoising(signal, adjacency, lambda_reg=0.1, iterations=100):
    '''
    图信号去噪: 最小化 ||x - y||^2 + lambda * x^T L x
    signal: 图信号 (n_nodes,)
    adjacency: 邻接矩阵
    '''
    L = compute_graph_laplacian(adjacency)
    
    # 解析解
    n = len(signal)
    denoised_signal = np.linalg.solve(
        np.eye(n) + lambda_reg * L,
        signal
    )
    
    return denoised_signal
```

### 3. 自适应图去噪
```python
def adaptive_graph_denoising(fc_matrices, alpha=0.1, beta=0.01):
    '''
    自适应图去噪: 同时学习干净图结构和去噪信号
    fc_matrices: 多个被试的功能连接 [n_subjects, n_nodes, n_nodes]
    '''
    n_subjects, n_nodes, _ = fc_matrices.shape
    
    # 初始化
    clean_fc = fc_matrices.copy()
    
    for iteration in range(50):
        # 更新图结构（平均并稀疏化）
        mean_fc = clean_fc.mean(axis=0)
        
        # 软阈值稀疏化
        threshold = np.percentile(np.abs(mean_fc), 90)
        graph_structure = mean_fc * (np.abs(mean_fc) > threshold)
        
        # 对每个被试去噪
        for i in range(n_subjects):
            L = compute_graph_laplacian(np.abs(graph_structure))
            
            # 平滑约束
            smoothness = np.trace(clean_fc[i].T @ L @ clean_fc[i])
            
            # 数据保真 + 平滑性
            clean_fc[i] = (1 - alpha) * fc_matrices[i] + alpha * (
                fc_matrices[i] - beta * (L @ fc_matrices[i] + fc_matrices[i] @ L.T)
            )
        
        # 收敛检查
        if iteration > 0 and np.linalg.norm(clean_fc - prev_fc) < 1e-6:
            break
        prev_fc = clean_fc.copy()
    
    return clean_fc
```

## BCI 应用

### 运动想象分类
```python
def enhance_motor_imagery_bci(eeg_data, labels, fs=250):
    '''
    使用图拉普拉斯去噪增强运动想象 BCI
    eeg_data: [trials, channels, time]
    '''
    n_trials, n_channels, _ = eeg_data.shape
    
    # 构建 EEG 通道空间图（基于空间邻近性）
    channel_coords = get_channel_coordinates()  # 通道空间坐标
    adjacency = build_spatial_graph(channel_coords)
    
    enhanced_data = np.zeros_like(eeg_data)
    
    for trial in range(n_trials):
        for t in range(eeg_data.shape[2]):
            signal = eeg_data[trial, :, t]
            # 图信号去噪
            enhanced_data[trial, :, t] = graph_signal_denoising(
                signal, adjacency, lambda_reg=0.05
            )
    
    # 提取 CSP 特征并分类
    features = extract_csp_features(enhanced_data, labels)
    accuracy = classify_motor_imagery(features, labels)
    
    return accuracy, enhanced_data
```

## 性能评估

```python
def evaluate_denoising(original_fc, denoised_fc, ground_truth=None):
    '''
    评估去噪效果
    '''
    metrics = {}
    
    # 信噪比提升
    if ground_truth is not None:
        noise_before = np.linalg.norm(original_fc - ground_truth, 'fro')
        noise_after = np.linalg.norm(denoised_fc - ground_truth, 'fro')
        metrics['snr_improvement'] = 20 * np.log10(noise_before / noise_after)
    
    # 平滑性（拉普拉斯二次型）
    L = compute_graph_laplacian(np.abs(denoised_fc))
    metrics['smoothness'] = np.trace(denoised_fc.T @ L @ denoised_fc)
    
    # 模块度（保留社区结构）
    metrics['modularity'] = compute_modularity(denoised_fc)
    
    return metrics
```

## 优势

1. **保持结构**: 在平滑噪声的同时保留重要的网络拓扑
2. **理论基础**: 基于谱图理论的数学保证
3. **适应性**: 可以针对不同脑区和任务调整参数
4. **可解释性**: 谱分解提供对信号成分的洞察


## 激活关键词
- graph laplacian, denoising, brain connectivity, 图拉普拉斯, 去噪
- neuroscience
- brain
- neural

---
*该 skill 基于神经科学领域知识创建（arXiv API 暂时不可用）*
