---
name: corsw-sliced-wasserstein-eeg-decoding
description: Correlation Sliced-Wasserstein (CorSW) framework for scale-invariant EEG decoding with improved domain generalization. Use when working with EEG signal classification, domain adaptation in BCI systems, or developing robust neural signal processing methods. Handles distribution shift in EEG datasets through manifold-based Wasserstein metrics.
license: MIT
---

# Correlation Sliced-Wasserstein for EEG Decoding

## Overview

**论文**: "A Sliced-Wasserstein Framework on Correlation Matrices for EEG Decoding" (arXiv:2606.06104, KDD 2026)
**核心创新**: Pullback Euclidean Metric Sliced Wasserstein (PEMSW) 框架处理相关矩阵流形上的分布匹配

## 核心方法论

### 1. 问题背景

**EEG解码的挑战**:
- 协方差描述符对通道尺度敏感
- 分布偏移导致跨域泛化差
- 传统方法：binning/smoothing → 丢失细节信息

**解决方案**: 全秩相关矩阵作为尺度不变表示

### 2. PEMSW框架

**数学基础**: 拉回欧几里得度量流形上的切片 Wasserstein 距离

```python
# CorSW 距离定义（两种几何）
# 1. Off-Log Metric (OLM): d_OLM(C1, C2) 
# 2. Log-Scaled Metric (LSM): d_LSM(C1, C2)

import numpy as np
from scipy.linalg import logm

def correlation_to_tangent(C, metric='OLM'):
    """
    将相关矩阵映射到切空间
    
    Args:
        C: 相关矩阵 (n_channels x n_channels)
        metric: 'OLM' 或 'LSM'
    
    Returns:
        tangent: 切空间表示
    """
    if metric == 'OLM':
        # Off-Log Metric: 对角元素偏移
        d = np.diag(C)
        offset = np.log(d)
        return logm(C) - np.diag(offset)
    elif metric == 'LSM':
        # Log-Scaled Metric: 对角缩放
        D = np.diag(np.sqrt(1.0 / np.diag(C)))
        return logm(D @ C @ D)
```

### 3. 切片 Wasserstein 实现

```python
def sliced_wasserstein_correlation(C1, C2, num_projections=1000, metric='OLM'):
    """
    计算两个相关矩阵集合间的 CorSW 距离
    
    Args:
        C1, C2: 相关矩阵数组 (N1 x n x n), (N2 x n x n)
        num_projections: 随机投影数量
        metric: 相关几何类型
    
    Returns:
        distance: SW 距离估计
    """
    # 映射到切空间
    T1 = np.array([correlation_to_tangent(c, metric) for c in C1])
    T2 = np.array([correlation_to_tangent(c, metric) for c in C2])
    
    # 随机投影 + 一维 Wasserstein
    n_channels = C1.shape[1]
    distances = []
    
    for _ in range(num_projections):
        # 随机单位向量
        theta = np.random.randn(n_channels * n_channels)
        theta = theta / np.linalg.norm(theta)
        
        # 投影
        proj1 = np.dot(T1.reshape(len(T1), -1), theta)
        proj2 = np.dot(T2.reshape(len(T2), -1), theta)
        
        # 一维 Wasserstein (排序差异)
        proj1_sorted = np.sort(proj1)
        proj2_sorted = np.sort(proj2)
        
        sw_1d = np.mean(np.abs(proj1_sorted - proj2_sorted))
        distances.append(sw_1d)
    
    return np.mean(distances)
```

### 4. 域泛化框架

```python
class CorSWDomainGeneralizer:
    """
    CorSW-based EEG 域泛化
    
    使用场景:
    - 多站点 EEG 数据集泛化
    - BCI 跨被试迁移
    - 医院间 EEG 分类器迁移
    """
    
    def __init__(self, metric='OLM', lambda_reg=0.1):
        self.metric = metric
        self.lambda_reg = lambda_reg
        
    def compute_domain_shift(self, domains):
        """
        计算多域间分布偏移
        
        Args:
            domains: 字典 {domain_name: correlation_matrices}
        
        Returns:
            shift_matrix: 域间距离矩阵
        """
        domain_names = list(domains.keys())
        n_domains = len(domain_names)
        shift_matrix = np.zeros((n_domains, n_domains))
        
        for i, d1 in enumerate(domain_names):
            for j, d2 in enumerate(domain_names):
                if i != j:
                    shift_matrix[i, j] = sliced_wasserstein_correlation(
                        domains[d1], domains[d2], 
                        metric=self.metric
                    )
        
        return shift_matrix, domain_names
    
    def align_domains(self, source_corr, target_corr):
        """
        对齐源域到目标域
        
        通过优化最小化 CorSW 距离
        """
        # 迁移学习策略
        # 1. 基于距离加权混合
        # 2. 特征空间对齐
        pass
```

## 实验验证

**三个 EEG 数据集**:
- 低训练开销
- 无额外推理成本
- 改善分布偏移下的泛化

**关键指标**:
- 分类准确率提升
- 域间距离量化
- 不确定性估计

## 与现有方法对比

| 方法 | 尺度敏感 | 分布偏移 | 训练开销 |
|------|---------|---------|---------|
| Covariance | ✓ | 高 | 低 |
| Riemannian | 部分 | 中等 | 高 |
| **CorSW** | ✗ | **低** | **低** |

## 应用场景

### 1. BCI 跨被试迁移
```python
# 源被试 EEG → 目标新被试
source_subjects = load_correlation_matrices('train_subjects')
target_subject = load_correlation_matrices('new_subject')

# 计算域偏移
shift = sliced_wasserstein_correlation(source_subjects, target_subject)

# 基于偏移调整分类器
adjust_classifier(shift)
```

### 2. 多站点 EEG 协作
```python
# 医院 A, B, C 的 EEG 数据
hospitals = {
    'A': load_correlations('hospital_A'),
    'B': load_correlations('hospital_B'),
    'C': load_correlations('hospital_C')
}

# 域泛化训练
generalizer = CorSWDomainGeneralizer()
shift_matrix, names = generalizer.compute_domain_shift(hospitals)

# 选择最佳源域
best_source = select_min_shift_domain(shift_matrix, target='C')
```

## 实现要点

### 数据预处理
```python
def eeg_to_correlation(eeg_signals):
    """
    EEG 信号 → 全秩相关矩阵
    
    Args:
        eeg_signals: (n_trials x n_channels x n_timepoints)
    
    Returns:
        correlations: (n_trials x n_channels x n_channels)
    """
    # 去均值
    centered = eeg_signals - np.mean(eeg_signals, axis=2, keepdims=True)
    
    # 计算协方差
    cov = np.einsum('ijk,ilk->ijl', centered, centered) / eeg_signals.shape[2]
    
    # 转换为相关矩阵
    std = np.sqrt(np.diag(cov))
    corr = cov / (std[:, None] * std[None, :])
    
    return corr
```

### 避免陷阱

**常见错误**:
1. ✗ 使用协方差而非相关矩阵 → 尺度敏感
2. ✗ 欧几里得距离处理相关矩阵 → 忽略流形结构
3. ✗ 固定投影方向 → 低效估计

**正确做法**:
1. ✓ 全秩相关矩阵作为基础表示
2. ✓ OLM/LSM 几何定义切空间
3. ✓ 大量随机投影稳定估计

## 代码资源

**GitHub**: https://github.com/ChenHu-ML/CorSW

**依赖**:
- Python 3.7+
- NumPy, SciPy
- PyTorch (可选，用于优化)

## 扩展方向

1. **动态 EEG**: 时间序列相关矩阵建模
2. **多模态融合**: EEG + MEG CorSW
3. **在线适应**: 实时域偏移检测与纠正
4. **神经解码**: fMRI → EEG CorSW 迁移

## 关键论文引用

```bibtex
@article{hu2026corsw,
  title={A Sliced-Wasserstein Framework on Correlation Matrices for EEG Decoding},
  author={Hu, Chen and Wang, Rui and Zhou, Jiale and Yi, Jingjun and Jin, Shaocheng and Song, Yidong and Zheng, Yefeng},
  journal={arXiv preprint arXiv:2606.06104},
  year={2026}
}
```

---

**Activation Keywords**: CorSW, sliced-wasserstein EEG, correlation matrices, domain generalization BCI, EEG decoding, scale-invariant neural signals, PEMSW, OLM LSM metrics