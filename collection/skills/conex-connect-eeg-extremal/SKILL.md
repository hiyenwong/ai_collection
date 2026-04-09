---
arxiv_id: 2101.09352v1
utility: 0.88
tags: [EEG, epilepsy, extremal dependence, brain connectivity, seizure detection, Gamma-band]
created: 2026-03-31
---

# Conex-Connect EEG Extremal Connectivity

## Activation Keywords

- EEG 极值连接
- 癫痫脑连接
- extremal dependence
- Conex-Connect
- seizure connectivity analysis
- Gamma-band EEG

## Problem Statement

癫痫 EEG 分析的传统方法存在局限：
- 时间变化谱分析无法捕捉极端行为
- 连贯性方法忽略极值依赖
- 癫痫发作前后的连接变化难以量化

## Method Overview

Huser et al. (2021) 提出 Conex-Connect：
1. 基于极值依赖的脑连接建模
2. 条件极值关联分析
3. 发作焦点与全脑连接的关系
4. Gamma 波段高频振荡的特征提取

## Tools Used

| Component | Function |
|-----------|----------|
| Extreme Value Theory | Tail dependence modeling |
| Conditional Dependence | Reference channel conditioning |
| Spectral Decomposition | Gamma-band extraction |
| EEG Processing | Multi-channel analysis |

## Key Concepts

### Extremal Dependence

极值依赖度量两个通道同时出现极端值的概率：
- 高依赖 → 连接紧密
- 低依赖 → 独立/弱连接
- 混乱模式 → 发作后状态

### Pre vs Post-Seizure

| State | Dependence Pattern | Interpretation |
|-------|-------------------|----------------|
| Pre-seizure | Stable, high | Focal area drives network |
| Post-seizure | Weak, chaotic | Network disrupted |

## Step-by-Step Instructions

### Conex-Connect 实现

1. **EEG 预处理与频带分解**
   ```python
   import numpy as np
   from scipy import signal
   
   def extract_gamma_band(eeg, fs=256):
       """提取 Gamma 波段 (30-100 Hz)"""
       b, a = signal.butter(4, [30, 100], btype='band', fs=fs)
       gamma = signal.filtfilt(b, a, eeg, axis=0)
       return gamma
   
   def compute_hilbert_amplitude(eeg_band):
       """计算包络幅度"""
       analytic = signal.hilbert(eeg_band, axis=0)
       return np.abs(analytic)
   ```

2. **极值依赖估计**
   ```python
   def estimate_tail_dependence(x, y, threshold=0.95):
       """估计尾部依赖系数"""
       # 转换为均匀边际
       u_x = np.rank(x) / len(x)
       u_y = np.rank(y) / len(y)
       
       # 计算联合超阈值概率
       extreme_both = np.mean((u_x > threshold) & (u_y > threshold))
       extreme_x = np.mean(u_x > threshold)
       
       # 尾部依赖系数
       chi = extreme_both / extreme_x if extreme_x > 0 else 0
       return chi
   ```

3. **条件极值依赖**
   ```python
   def conex_connect(eeg_channels, reference_idx, threshold=0.95):
       """Conex-Connect 条件极值依赖"""
       ref = eeg_channels[:, reference_idx]
       n_channels = eeg_channels.shape[1]
       
       conditional_dep = np.zeros(n_channels)
       for i in range(n_channels):
           if i == reference_idx:
               conditional_dep[i] = 1.0
           else:
               # 条件于参考通道极值
               extreme_mask = ref > np.quantile(ref, threshold)
               conditional_dep[i] = estimate_tail_dependence(
                   ref[extreme_mask], 
                   eeg_channels[extreme_mask, i]
               )
       
       return conditional_dep
   ```

4. **癫痫发作分析**
   ```python
   def analyze_seizure_connectivity(eeg_pre, eeg_post, focal_idx):
       """分析发作前后连接变化"""
       # 提取 Gamma 包络
       gamma_pre = compute_hilbert_amplitude(extract_gamma_band(eeg_pre))
       gamma_post = compute_hilbert_amplitude(extract_gamma_band(eeg_post))
       
       # 计算条件极值依赖
       conn_pre = conex_connect(gamma_pre, focal_idx)
       conn_post = conex_connect(gamma_post, focal_idx)
       
       # 连接变化
       delta_conn = conn_post - conn_pre
       
       return {
           'pre_seizure': conn_pre,
           'post_seizure': conn_post,
           'change': delta_conn
       }
   ```

## Example Usage

```python
import numpy as np

# 加载 EEG 数据
eeg_data = load_eeg_recording()  # shape: (n_samples, n_channels)

# 标记发作焦点（如 T3 电极）
focal_channel = 10  # T3

# 分割发作前后
pre_seizure = eeg_data[:1000, :]  # 发作前
post_seizure = eeg_data[2000:, :]  # 发作后

# 分析连接变化
results = analyze_seizure_connectivity(pre_seizure, post_seizure, focal_channel)

print(f"Pre-seizure stability: {np.std(results['pre_seizure']):.3f}")
print(f"Post-seizure chaos: {np.std(results['post_seizure']):.3f}")
print(f"Average change: {np.mean(results['change']):.3f}")
```

## Key Findings

1. **Gamma 波段最重要** - 高频振荡最能解释极值依赖
2. **发作前稳定** - 条件依赖高且稳定
3. **发作后混乱** - 连接弱且模式混乱
4. **焦点驱动** - 癫痫焦点主导全脑连接

## References

- Huser, R. et al. (2021). Learning Patterns in Extremal Brain Connectivity From Multi-Channel EEG Data. arXiv:2101.09352.

## Related Skills

- eeg-brain-connectivity-bci
- seizure-detection-connectivity
- explainable-gnn-eeg-neurological