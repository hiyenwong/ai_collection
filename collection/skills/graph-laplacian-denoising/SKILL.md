---
name: graph-laplacian-denoising
description: 脑连接网络的图拉普拉斯去噪方法。用于提升功能连接估计的可靠性，增强脑状态检测和 BCI 应用的性能。触发词：脑连接去噪、图拉普拉斯、Laplacian denoising、功能连接、FC denoising、J-divergence。
user-invocable: true
---

# Graph Laplacian Denoising for Brain Connectivity

## 核心方法论

图拉普拉斯去噪方法利用图信号处理（GSP）技术，提升功能连接（FC）估计的可靠性：

1. **网络图拉普拉斯表示** - 将功能连接矩阵转换为图拉普拉斯
2. **图信号去噪** - 利用图的平滑性先验去除噪声
3. **Jensen 散度增强** - 新的 J-divergence 公式量化脑状态距离
4. **实时 BCI 应用** - 缩短连接估计所需时间窗口

### 核心优势

- 提高脑状态可区分性（J-divergence）
- 缩短估计时间窗口
- 提供节点级贡献分析
- 适用于实时 BCI 系统

## Python 代码示例

### 1. 图拉普拉斯去噪核心实现

```python
import numpy as np
from scipy import linalg
from scipy.spatial.distance import squareform

def compute_graph_laplacian(fc_matrix, normalized=True):
    """
    从功能连接矩阵计算图拉普拉斯
    
    Args:
        fc_matrix: N×N 功能连接矩阵
        normalized: 是否使用归一化拉普拉斯
    
    Returns:
        L: 图拉普拉斯矩阵
    """
    # 构建邻接矩阵（取绝对值，可设阈值）
    W = np.abs(fc_matrix)
    
    # 可选：稀疏化
    # threshold = np.percentile(W, 90)
    # W[W < threshold] = 0
    
    # 度矩阵
    D = np.diag(np.sum(W, axis=1))
    
    if normalized:
        # 归一化拉普拉斯: L = I - D^{-1/2} W D^{-1/2}
        D_inv_sqrt = linalg.fractional_matrix_power(D, -0.5)
        L = np.eye(len(W)) - D_inv_sqrt @ W @ D_inv_sqrt
    else:
        # 标准拉普拉斯: L = D - W
        L = D - W
    
    return L

def graph_laplacian_denoising(L, noise_level=0.1, n_iterations=5):
    """
    图拉普拉斯去噪
    
    Args:
        L: 图拉普拉斯矩阵
        noise_level: 噪声水平估计
        n_iterations: 迭代次数
    
    Returns:
        L_denoised: 去噪后的拉普拉斯
    """
    # 特征分解
    eigenvalues, eigenvectors = linalg.eigh(L)
    
    # 低频分量保留（图信号的平滑性先验）
    # 高频分量对应噪声
    n_eigenvectors = max(2, int(len(eigenvalues) * (1 - noise_level)))
    
    # 重构去噪拉普拉斯
    L_denoised = eigenvectors[:, :n_eigenvectors] @ np.diag(eigenvalues[:n_eigenvectors]) @ eigenvectors[:, :n_eigenvectors].T
    
    return L_denoised, eigenvalues, eigenvectors
```

### 2. Jensen 散度计算

```python
def laplacian_j_divergence(L1, L2):
    """
    计算两个拉普拉斯矩阵之间的 Jensen 散度
    
    Args:
        L1, L2: 两个图拉普拉斯矩阵
    
    Returns:
        J: Jensen 散度值
        contributions: 每个节点的贡献
    """
    n = L1.shape[0]
    
    # 计算 M = (L1 + L2) / 2
    M = (L1 + L2) / 2
    
    # 特征分解
    eig_L1 = linalg.eigh(L1)[0]
    eig_L2 = linalg.eigh(L2)[0]
    eig_M = linalg.eigh(M)[0]
    
    # Jensen 散度: J = H(M) - (H(L1) + H(L2))/2
    # H(L) = -log det(L)
    
    def entropy(L, eigenvalues=None):
        if eigenvalues is None:
            eigenvalues = linalg.eigh(L)[0]
        # 只考虑正特征值
        pos_eig = eigenvalues[eigenvalues > 1e-10]
        if len(pos_eig) == 0:
            return 0
        return -np.sum(np.log(pos_eig))
    
    H_M = entropy(M, eig_M)
    H_L1 = entropy(L1, eig_L1)
    H_L2 = entropy(L2, eig_L2)
    
    J = H_M - (H_L1 + H_L2) / 2
    
    # 节点级贡献（基于对角元素）
    contributions = np.abs(np.diag(L1) - np.diag(L2))
    contributions = contributions / np.sum(contributions) * J if np.sum(contributions) > 0 else np.zeros(n)
    
    return J, contributions
```

### 3. 完整处理流程

```python
def process_eeg_connectivity(eeg_data, n_channels, method='plv', window_size=1000):
    """
    完整的 EEG 功能连接处理流程
    
    Args:
        eeg_data: (n_samples, n_channels) EEG 数据
        n_channels: 通道数
        method: 连接性度量 ('plv', 'coh', 'wpli')
        window_size: 时间窗口大小
    
    Returns:
        fc_denoised: 去噪后的功能连接
        L_denoised: 去噪后的图拉普拉斯
    """
    from scipy.signal import hilbert
    
    # 1. 计算功能连接
    if method == 'plv':
        # Phase Locking Value
        analytic_signal = hilbert(eeg_data, axis=0)
        phase = np.angle(analytic_signal)
        
        fc = np.zeros((n_channels, n_channels))
        for i in range(n_channels):
            for j in range(i+1, n_channels):
                plv = np.abs(np.mean(np.exp(1j * (phase[:, i] - phase[:, j]))))
                fc[i, j] = plv
                fc[j, i] = plv
    
    # 2. 计算图拉普拉斯
    L = compute_graph_laplacian(fc, normalized=True)
    
    # 3. 去噪
    L_denoised, eigenvalues, eigenvectors = graph_laplacian_denoising(L)
    
    # 4. 重构功能连接
    # 从拉普拉斯逆推邻接矩阵
    D_denoised = np.diag(np.sum(np.eye(n_channels) - L_denoised, axis=1))
    W_denoised = np.eye(n_channels) - L_denoised
    fc_denoised = W_denoised
    
    return fc_denoised, L_denoised, eigenvalues
```

### 4. 脑状态分类应用

```python
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

def brain_state_classification(fc_matrices_1, fc_matrices_2, use_denoising=True):
    """
    使用 Jensen 散度进行脑状态分类
    
    Args:
        fc_matrices_1: 状态 1 的功能连接矩阵列表
        fc_matrices_2: 状态 2 的功能连接矩阵列表
        use_denoising: 是否使用图拉普拉斯去噪
    
    Returns:
        accuracy: 分类准确率
    """
    features = []
    labels = []
    
    # 状态 1 样本
    for fc in fc_matrices_1:
        L = compute_graph_laplacian(fc)
        if use_denoising:
            L, _, _ = graph_laplacian_denoising(L)
        # 使用特征值作为特征
        features.append(linalg.eigh(L)[0])
        labels.append(0)
    
    # 状态 2 样本
    for fc in fc_matrices_2:
        L = compute_graph_laplacian(fc)
        if use_denoising:
            L, _, _ = graph_laplacian_denoising(L)
        features.append(linalg.eigh(L)[0])
        labels.append(1)
    
    # SVM 分类
    X = np.array(features)
    y = np.array(labels)
    
    clf = SVC(kernel='rbf')
    scores = cross_val_score(clf, X, y, cv=5)
    
    return scores.mean(), scores.std()
```

## 应用场景

1. **运动想象 BCI** - 提升运动想象状态检测
2. **静息态分析** - 增强静息态网络识别
3. **实时脑机接口** - 缩短估计窗口，实时反馈
4. **临床诊断** - 提高病理脑网络检测敏感度
5. **认知状态监测** - 注意力、警觉性状态识别

## 参数调优建议

1. **去噪强度**: `noise_level` 根据数据信噪比调整（0.05-0.2）
2. **特征保留**: 保留 80-95% 的特征值
3. **窗口大小**: 实时应用建议 500-1000 样本
4. **连接度量**: PLV 适合相位同步，wPLI 更抗体积传导干扰

## Activation Keywords
- 脑连接去噪
- 图拉普拉斯
- Laplacian denoising
- 功能连接
- FC denoising
- J-divergence
- 图信号处理
- BCI
- 脑状态分类
- EEG分析

## Tools Used
- numpy
- scipy
- sklearn

## Instructions for Agents
1. 理解图拉普拉斯表示：L = D - W 或归一化形式
2. 掌握谱去噪：保留低频分量，去除高频噪声
3. 计算Jensen散度：量化两个拉普拉斯矩阵的差异
4. 应用脑状态分类：使用谱特征进行SVM分类
5. 注意归一化拉普拉斯在脑网络分析中的优势

## Examples
```python
# 使用示例
from graph_laplacian_denoising import compute_graph_laplacian, graph_laplacian_denoising

# 1. 计算图拉普拉斯
L = compute_graph_laplacian(fc_matrix, normalized=True)

# 2. 去噪
L_denoised, eigenvalues, eigenvectors = graph_laplacian_denoising(L, noise_level=0.1)

# 3. 计算Jensen散度
from graph_laplacian_denoising import laplacian_j_divergence
J, contributions = laplacian_j_divergence(L1, L2)
print(f"Jensen散度: {J:.4f}")

# 4. 脑状态分类
accuracy, std = brain_state_classification(fc_matrices_1, fc_matrices_2, use_denoising=True)
```

## 参考文献

- Paper: arXiv:2012.11240
- IEEE Trans. Signal and Information Processing over Networks, 2021