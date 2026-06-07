---
name: hermes-brain-connectivity
description: HERMES脑连接分析工具箱。整合功能和有效连接分析方法，包括互相关、相干性、Granger因果、相位同步、互信息等。适用于EEG/MEG脑网络分析、神经生理信号处理。触发词：HERMES、脑连接、功能连接、有效连接、Granger因果、相位同步、brain connectivity、effective connectivity。
user-invocable: true
---

# HERMES Brain Connectivity Toolbox - 脑连接分析工具箱

## 核心思想

整合多种功能和有效连接分析方法到统一工具箱，方便神经科学研究者使用。

**来源：** arXiv:1305.2550
**效用：** 1.0

---

## 方法论

### 功能连接 (FC) 方法

| 方法 | 说明 |
|------|------|
| 互相关 | 时域线性相关 |
| 相干性 | 频域线性相关 |
| 相位同步 | 相位锁定值 |
| 互信息 | 非线性依赖 |

### 有效连接 (EC) 方法

| 方法 | 说明 |
|------|------|
| Granger因果 | 因果推断 |
| 传递熵 | 非线性因果 |
| DTF | 有向传递函数 |
| PDC | 偏有向相干 |

---

## Python 实现

```python
import numpy as np
from scipy import signal
from scipy.stats import entropy

class HERMESToolbox:
    """HERMES 脑连接分析工具箱"""
    
    def __init__(self, fs=500):
        self.fs = fs
    
    # === 功能连接 ===
    
    def cross_correlation(self, x, y, max_lag=None):
        """互相关分析"""
        if max_lag is None:
            max_lag = len(x) // 4
        
        corr = np.correlate(x - np.mean(x), y - np.mean(y), mode='full')
        lags = np.arange(-len(x) + 1, len(x))
        
        # 归一化
        corr = corr / (np.std(x) * np.std(y) * len(x))
        
        # 限制滞后范围
        mask = np.abs(lags) <= max_lag
        return lags[mask], corr[mask]
    
    def coherence(self, x, y, nperseg=256):
        """相干性分析"""
        f, Cxy = signal.coherence(x, y, fs=self.fs, nperseg=nperseg)
        return f, Cxy
    
    def phase_locking_value(self, x, y):
        """相位锁定值"""
        # Hilbert 变换
        phase_x = np.angle(signal.hilbert(x))
        phase_y = np.angle(signal.hilbert(y))
        
        # 相位差
        phase_diff = phase_x - phase_y
        
        # PLV
        plv = np.abs(np.mean(np.exp(1j * phase_diff)))
        return plv
    
    def mutual_information(self, x, y, bins=20):
        """互信息"""
        # 联合直方图
        hist_2d, _, _ = np.histogram2d(x, y, bins=bins)
        
        # 归一化
        pxy = hist_2d / np.sum(hist_2d)
        
        # 边缘分布
        px = np.sum(pxy, axis=1)
        py = np.sum(pxy, axis=0)
        
        # 互信息
        mi = 0.0
        for i in range(bins):
            for j in range(bins):
                if pxy[i, j] > 0 and px[i] > 0 and py[j] > 0:
                    mi += pxy[i, j] * np.log(pxy[i, j] / (px[i] * py[j]))
        
        return mi
    
    # === 有效连接 ===
    
    def granger_causality(self, x, y, max_lag=10):
        """Granger 因果检验"""
        from statsmodels.tsa.stattools import grangercausalitytests
        
        # 准备数据
        data = np.column_stack([y, x])
        
        # Granger 检验
        result = grangercausalitytests(data, maxlag=max_lag, verbose=False)
        
        # 提取 F 统计量
        f_stats = [result[lag][0]['ssr_ftest'][0] for lag in range(1, max_lag + 1)]
        
        return np.array(f_stats)
    
    def transfer_entropy(self, x, y, k=1, l=1):
        """传递熵（简化实现）"""
        # 离散化
        x_discrete = np.digitize(x, bins=np.linspace(x.min(), x.max(), 10))
        y_discrete = np.digitize(y, bins=np.linspace(y.min(), y.max(), 10))
        
        # 计算条件概率
        # TE = H(Y_t+1 | Y_t) - H(Y_t+1 | Y_t, X_t)
        # 简化实现
        te = self.mutual_information(y[k:], x[:-k]) - self.mutual_information(y[k:], y[:-k])
        
        return te
    
    # === 批量分析 ===
    
    def compute_connectivity_matrix(self, data, method='plv'):
        """
        计算连接矩阵
        
        Parameters:
        -----------
        data : np.ndarray, shape (n_channels, n_samples)
        method : str, one of 'plv', 'coherence', 'mi', 'granger'
        
        Returns:
        --------
        conn_matrix : np.ndarray, shape (n_channels, n_channels)
        """
        n_ch = data.shape[0]
        conn_matrix = np.zeros((n_ch, n_ch))
        
        for i in range(n_ch):
            for j in range(n_ch):
                if i != j:
                    if method == 'plv':
                        conn_matrix[i, j] = self.phase_locking_value(data[i], data[j])
                    elif method == 'coherence':
                        _, coh = self.coherence(data[i], data[j])
                        conn_matrix[i, j] = np.mean(coh)
                    elif method == 'mi':
                        conn_matrix[i, j] = self.mutual_information(data[i], data[j])
        
        return conn_matrix
```

---

## 应用场景

1. **EEG/MEG 分析** - 脑网络连接
2. **fMRI 分析** - 功能连接
3. **神经生理研究** - 因果关系推断

---

## Activation Keywords
- HERMES
- 脑连接
- 功能连接
- 有效连接
- Granger因果
- 相位同步

## Tools Used
- numpy
- scipy
- statsmodels

## Instructions for Agents
1. 选择合适的连接分析方法
2. 预处理信号（滤波、去噪）
3. 计算连接矩阵
4. 统计检验和网络分析

## Examples
分析多通道EEG数据的功能连接网络。

## 参考文献
- arXiv:1305.2550 - HERMES: towards an integrated toolbox