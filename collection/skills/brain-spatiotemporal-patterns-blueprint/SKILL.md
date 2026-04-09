---
arxiv_id: 2106.00637v1
utility: 0.88
tags: '[spatiotemporal patterns, coordination dynamics, EEG, brain connectivity, metastability, brain dynamics]'
created: 2026-03-31
---

# Brain Spatiotemporal Patterns Blueprint

## Activation Keywords

- 脑时空模式
- coordination dynamics
- 神经电信号分析
- 脑连接动力学
- metastability
- 神经模式分析框架

## Problem Statement

脑功能研究需要理解时空模式的挑战：
- 脑区之间的相互作用随时间演化
- 静态分析无法捕捉动态模式
- 需要研究模式化的时空交互
- 病理状态与连接异常相关

## Method Overview

Tognoli et al. (2021) 提出脑协调动力学框架：
1. 连续电生理数据分析工具集
2. 时空组织模式识别
3. 行为/认知/临床变量关联
4. 生物启发工程应用

## Tools Used

- `Component` - Analysis component
- `Coordination Dynamics` - Analysis component
- `Spatiotemporal Analysis` - Analysis component
- `Metastability` - Analysis component
- `EEG/MEG Processing` - Analysis component

## Key Concepts

### Coordination Dynamics

协调动力学研究脑区间的时空交互模式：
- **Metastability**：系统在多个吸引子间游走
- **Phase Synchrony**：相位同步模式
- **Pattern Switching**：模式切换动力学

### Spatiotemporal Organization

| Scale | Patterns | Methods |
|-------|----------|---------|
| Micro | Neuronal assemblies | Spike trains |
| Meso | Local field potentials | LFP/EEG |
| Macro | Brain networks | fMRI/MEG |

## Step-by-Step Instructions

### 脑时空模式分析框架

1. **数据准备与预处理**
   ```python
   import numpy as np
   from scipy import signal
   
   def preprocess_eeg(eeg_data, fs=256):
       """EEG 数据预处理"""
       # 带通滤波
       b, a = signal.butter(4, [1, 40], btype='band', fs=fs)
       filtered = signal.filtfilt(b, a, eeg_data, axis=0)
       
       # 去伪迹（ICA）
       # ica = FastICA(n_components=eeg_data.shape[1])
       # cleaned = ica.fit_transform(filtered)
       
       return filtered
   ```

2. **相位同步分析**
   ```python
   def compute_phase_synchrony(eeg, fs=256, freq_band='alpha'):
       """计算相位同步"""
       # 频带滤波
       bands = {'delta': (1, 4), 'theta': (4, 8), 
                'alpha': (8, 12), 'beta': (12, 30), 'gamma': (30, 40)}
       f_low, f_high = bands[freq_band]
       
       b, a = signal.butter(4, [f_low, f_high], btype='band', fs=fs)
       filtered = signal.filtfilt(b, a, eeg, axis=0)
       
       # Hilbert 变换提取相位
       analytic = signal.hilbert(filtered, axis=0)
       phase = np.angle(analytic)
       
       # 相位同步指数
       n_channels = eeg.shape[1]
       plv = np.zeros((n_channels, n_channels))
       
       for i in range(n_channels):
           for j in range(i+1, n_channels):
               phase_diff = phase[:, i] - phase[:, j]
               plv[i, j] = np.abs(np.mean(np.exp(1j * phase_diff)))
               plv[j, i] = plv[i, j]
       
       return plv
   ```

3. **Metastability 分析**
   ```python
   def metastability_index(phase_sync_series, window=100):
       """计算 metastability 指数"""
       # 滑动窗口相位同步
       sync_variance = []
       for i in range(0, len(phase_sync_series) - window, window//2):
           window_sync = phase_sync_series[i:i+window]
           sync_variance.append(np.var(window_sync))
       
       # Metastability：同步方差的方差
       return np.var(sync_variance)
   ```

4. **模式切换检测**
   ```python
   def detect_pattern_switches(sync_series, threshold=0.7):
       """检测模式切换"""
       # 同步状态变化
       sync_binary = (sync_series > threshold).astype(int)
       
       # 状态转换点
       switches = np.where(np.diff(sync_binary) != 0)[0]
       
       return switches, sync_binary
   ```

## Example Usage

```python
import numpy as np

# 加载 EEG 数据
eeg = load_eeg_recording()  # shape: (n_samples, n_channels)

# 1. 预处理
eeg_clean = preprocess_eeg(eeg)

# 2. 相位同步
plv_matrix = compute_phase_synchrony(eeg_clean, freq_band='alpha')

# 3. 时间演化
sync_series = compute_time_varying_sync(eeg_clean, window=500)

# 4. Metastability
meta_idx = metastability_index(sync_series)
print(f"Metastability index: {meta_idx:.3f}")

# 5. 模式切换
switches, states = detect_pattern_switches(sync_series)
print(f"Number of pattern switches: {len(switches)}")
```

## Clinical Applications

| Pathology | Pattern Alteration |
|-----------|-------------------|
| Schizophrenia | Reduced metastability |
| Autism | Altered synchrony patterns |
| Alzheimer's | Disrupted long-range connectivity |
| Epilepsy | Excessive synchronization |

## Description

Brain Spatiotemporal Patterns Blueprint

**Key Concepts:**
- **Metastability**：系统在多个吸引子间游走
- **Phase Synchrony**：相位同步模式
- **Pattern Switching**：模式切换动力学

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 数据准备与预处理

### Step 2: 相位同步分析

### Step 3: Metastability 分析

### Step 4: 模式切换检测

### Step 5: Understand the Request

## Examples

### Example 1: Basic Application

**User:** I need to apply Brain Spatiotemporal Patterns Blueprint to my analysis.

**Agent:** I'll help you apply brain-spatiotemporal-patterns-blueprint. First, let me understand your specific use case...

**Context:** **Metastability**：系统在多个吸引子间游走

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for brain-spatiotemporal-patterns-blueprint?

**Agent:** Let me search for the latest research and best practices...

## References

- Tognoli, E. et al. (2021). A Blueprint for the Study of the Brain's Spatiotemporal Patterns. arXiv:2106.00637.

## Related Skills

- time-varying-brain-connectivity
- bursty-persistent-brain-networks-pbm
- neural-dynamics-universal-translator