---
name: lightweight-dynamic-brain-connectivity
description: '轻量级动态脑连接框架方法论。基于时变有向传递函数（TV-DTF）估计脑区间方向性信息流，用于压力分类和脑网络分析。适用于EEG压力检测、动态功能连接、因果脑网络分析。触发词：动态脑连接、TV-DTF、压力检测、方向性信息流、脑网络、dynamic connectivity、stress detection、directed transfer function。'
user-invocable: true
---

# Lightweight Dynamic Brain Connectivity - 轻量级动态脑连接框架

## 核心思想

通过时变有向传递函数（TV-DTF）估计脑区间方向性信息流，实现轻量级动态脑网络分析，用于压力状态分类。

**来源：** arXiv:2511.05505
**效用：** 1.0

---

## 方法论

### 1. TV-DTF 原理

**时变有向传递函数（Time-Varying Directed Transfer Function）：**
- 估计脑区间方向性信息流
- 捕获时间和因果影响
- 静态功能连接无法实现的动态分析

**数学表达：**
```
TV-DTF_ij(f,t) = |H_ij(f,t)|² / Σ_k|H_ik(f,t)|²
```
其中 H 为传递函数矩阵。

### 2. 特征提取流程

**步骤：**
1. EEG 信号预处理（32 通道）
2. 频带分解（Delta, Theta, Alpha, Beta, Gamma）
3. TV-DTF 计算
4. 动态连接矩阵构建
5. 特征向量化

**关键频带：**
- **Alpha (8-12 Hz)** - 最强判别力，89.73% 准确率
- **Beta (12-30 Hz)** - 次强判别力

### 3. 机器学习验证

**分类器对比：**
| 分类器 | 2类准确率 | 3类准确率 |
|--------|----------|----------|
| SVM | — | 89.73% |
| XGBoost | 93.69% | — |
| Random Forest | 高 | 高 |

### 4. 脑区信息流

**关键发现：**
- 额-顶叶长程信息影响主导
- 额-枕叶方向性连接显著
- 额叶区域在压力下的调节作用

---

## 实现框架

```python
import numpy as np
from scipy import signal
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import xgboost as xgb

class TVDTFClassifier:
    """时变有向传递函数压力分类器"""
    
    def __init__(self, fs=500, n_channels=32):
        self.fs = fs
        self.n_channels = n_channels
        self.freq_bands = {
            'delta': (1, 4),
            'theta': (4, 8),
            'alpha': (8, 12),
            'beta': (12, 30),
            'gamma': (30, 45)
        }
    
    def compute_tv_dtf(self, eeg_data, band_name):
        """
        计算特定频带的TV-DTF
        
        Parameters:
        -----------
        eeg_data : np.ndarray, shape (n_channels, n_samples)
            多通道EEG数据
        band_name : str
            频带名称
        
        Returns:
        --------
        dtf_matrix : np.ndarray, shape (n_channels, n_channels)
            方向性连接矩阵
        """
        # 带通滤波
        fmin, fmax = self.freq_bands[band_name]
        filtered = self._bandpass_filter(eeg_data, fmin, fmax)
        
        # 计算传递函数（简化版本）
        # 实际实现需要多变量自回归模型
        dtf_matrix = self._estimate_dtf(filtered)
        
        return dtf_matrix
    
    def _bandpass_filter(self, data, fmin, fmax):
        """带通滤波"""
        b, a = signal.butter(4, 
            [fmin/(self.fs/2), fmax/(self.fs/2)], 
            btype='band')
        return signal.filtfilt(b, a, data, axis=1)
    
    def _estimate_dtf(self, data):
        """估计DTF矩阵（简化）"""
        n_ch = data.shape[0]
        dtf = np.zeros((n_ch, n_ch))
        
        # 使用格兰杰因果简化估计
        for i in range(n_ch):
            for j in range(n_ch):
                if i != j:
                    # 计算方向性影响
                    dtf[i, j] = self._granger_causality(data[j], data[i])
        
        # 归一化
        row_sums = dtf.sum(axis=1, keepdims=True)
        dtf_normalized = dtf / (row_sums + 1e-10)
        
        return dtf_normalized
    
    def _granger_causality(self, x, y):
        """简化的格兰杰因果检验"""
        # 使用互相关作为简化度量
        corr = np.abs(signal.correlate(x, y, mode='valid'))
        return np.max(corr)
    
    def extract_features(self, eeg_data):
        """提取TV-DTF特征"""
        features = []
        
        # 提取Alpha和Beta频带特征（最强判别力）
        for band in ['alpha', 'beta']:
            dtf = self.compute_tv_dtf(eeg_data, band)
            # 展平上三角矩阵
            upper_tri = dtf[np.triu_indices(self.n_channels, k=1)]
            features.extend(upper_tri)
        
        return np.array(features)
    
    def fit(self, X, y):
        """训练XGBoost分类器"""
        self.clf = xgb.XGBClassifier(
            n_estimators=100,
            max_depth=6,
            learning_rate=0.1
        )
        self.clf.fit(X, y)
    
    def predict(self, X):
        """预测压力状态"""
        return self.clf.predict(X)
```

---

## 应用场景

### 1. 压力检测
- 实时压力状态分类
- 心理健康监测
- 工作负荷评估

### 2. 脑网络分析
- 动态功能连接
- 方向性因果推断
- 脑区交互研究

### 3. BCI 应用
- 认知状态识别
- 注意力监测
- 疲劳检测

---

## 数据集

**SAM 40 数据集：**
- 32 通道 EEG
- 心算任务试验
- 压力/放松状态标注

---

## 关键参数

| 参数 | 推荐值 | 说明 |
|------|--------|------|
| 通道数 | 32 | 标准EEG配置 |
| 采样率 | 500 Hz | 时变分析精度 |
| Alpha频带 | 8-12 Hz | 最强判别力 |
| Beta频带 | 12-30 Hz | 次强判别力 |
| 分类器 | XGBoost/SVM | 最优性能 |

---

## 预期结果

1. **压力分类：** 2类 93.69%，3类 89.73%
2. **方向性连接：** 额-顶叶、额-枕叶主导
3. **动态特征：** 优于静态功率和相位锁定

---

## 注意事项

- TV-DTF 需要多变量自回归模型
- 频带选择影响分类性能
- 个体差异需要校准
- 实时应用需优化计算效率

---

## 参考文献

- arXiv:2511.05505 - Rewiring Human Brain Networks via Lightweight Dynamic Connectivity Framework
## Activation Keywords

- lightweight-dynamic-brain-connectivity
- lightweight-dynamic-brain-connectivity 技能
- lightweight-dynamic-brain-connectivity skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 压力分类：

### Step 2: 方向性连接：

### Step 3: 动态特征：

### Step 4: Understand the Request

### Step 5: Search for Information

## Examples

### Example 1: Basic Application

**User:** I need to apply Lightweight Dynamic Brain Connectivity - 轻量级动态脑连接框架 to my analysis.

**Agent:** I'll help you apply lightweight-dynamic-brain-connectivity. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for lightweight-dynamic-brain-connectivity?

**Agent:** Let me search for the latest research and best practices...
