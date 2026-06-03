---
name: eeg-brain-connectivity-bci
description: EEG脑连接BCI分析方法论。通过功能连接分析理解脑网络在BCI中的机制，用于神经康复和外骨骼控制。适用于脑机接口、神经康复、步态训练。触发词：EEG、脑连接、BCI、脑机接口、功能网络、神经康复、brain-computer interface、neurorehabilitation。
user-invocable: true
---

# EEG Brain Connectivity for BCI - EEG脑连接BCI分析

## 核心思想

通过分析EEG脑连接理解功能网络涌现，改进BCI信号分析和分类，用于运动障碍患者的神经康复。

**来源：** arXiv:2007.11674
**效用：** 0.97

---

## 方法论

### 四种策略

| 策略 | 目的 |
|------|------|
| 特征提取 | 用连接特征增强分类 |
| 状态监测 | 跟踪脑网络变化 |
| 适应性控制 | 根据连接状态调整BCI |
| 神经康复 | 结合外骨骼促进恢复 |

### 实现框架

```python
import numpy as np
from scipy import signal

class EEGConnectivityBCI:
    """EEG脑连接BCI分析器"""
    
    def __init__(self, n_channels=32, fs=500):
        self.n_channels = n_channels
        self.fs = fs
    
    def compute_functional_connectivity(self, eeg_data):
        """
        计算功能连接矩阵
        
        Parameters:
        -----------
        eeg_data : np.ndarray, shape (n_channels, n_samples)
        
        Returns:
        --------
        fc_matrix : np.ndarray, shape (n_channels, n_channels)
        """
        fc_matrix = np.zeros((self.n_channels, self.n_channels))
        
        for i in range(self.n_channels):
            for j in range(i+1, self.n_channels):
                # 相位锁定值
                plv = self._phase_locking_value(eeg_data[i], eeg_data[j])
                fc_matrix[i, j] = plv
                fc_matrix[j, i] = plv
        
        return fc_matrix
    
    def _phase_locking_value(self, x, y):
        """相位锁定值"""
        phase_x = np.angle(signal.hilbert(x))
        phase_y = np.angle(signal.hilbert(y))
        return np.abs(np.mean(np.exp(1j * (phase_x - phase_y))))
    
    def extract_features(self, fc_matrix):
        """
        从连接矩阵提取特征
        
        Returns:
        --------
        features : dict
        """
        # 网络特征
        features = {
            'mean_connectivity': np.mean(fc_matrix),
            'std_connectivity': np.std(fc_matrix),
            'clustering': self._clustering_coefficient(fc_matrix),
            'path_length': self._average_path_length(fc_matrix)
        }
        
        return features
    
    def _clustering_coefficient(self, fc_matrix, threshold=0.5):
        """聚类系数"""
        binary = (fc_matrix > threshold).astype(int)
        n = len(binary)
        
        clustering = []
        for i in range(n):
            neighbors = np.where(binary[i] == 1)[0]
            if len(neighbors) > 1:
                triangles = 0
                for j in neighbors:
                    for k in neighbors:
                        if binary[j, k]:
                            triangles += 1
                clustering.append(triangles / (len(neighbors) * (len(neighbors) - 1)))
        
        return np.mean(clustering) if clustering else 0
    
    def _average_path_length(self, fc_matrix, threshold=0.5):
        """平均路径长度"""
        # 简化实现
        binary = (fc_matrix > threshold).astype(int)
        return 1.0 / (np.mean(binary) + 1e-10)
```

---

## 应用场景

1. **BCI控制** - 轮椅、外骨骼
2. **神经康复** - 步态训练
3. **状态监测** - 疲劳、注意力

---

## Activation Keywords
- EEG
- 脑连接
- BCI
- 脑机接口
- 功能网络

## Tools Used
- numpy
- scipy

## Instructions for Agents
1. 计算功能连接矩阵
2. 提取网络特征
3. 用于BCI分类或监测

## Examples
分析运动想象任务的EEG连接特征。

## 参考文献
- arXiv:2007.11674