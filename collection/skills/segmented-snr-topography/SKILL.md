---
name: segmented-snr-topography
description: '分段SNR地形图可视化神经动力学方法论。结合数据驱动的噪声区间评估和高级SNR可视化，改进EEG-BCI性能。适用于P300检测、EEG信号质量评估、自适应BCI系统。触发词：SNR地形图、P300检测、EEG信号质量、噪声区间、BCI优化、signal-to-noise ratio、neural dynamics、P300。'
user-invocable: true
---

# Segmented SNR Topography - 分段SNR地形图可视化

## 核心思想

通过数据驱动的噪声区间评估和高级 SNR 可视化，解决 EEG-BCI 低信噪比和非平稳神经活动的挑战。

**来源：** arXiv:2509.18599
**效用：** 1.0

---

## 方法论

### 1. 问题背景

**EEG-BCI 挑战：**
- 低信噪比（SNR）
- 非平稳神经活动
- 噪声区间选择缺乏系统评估

### 2. 分段 SNR 地形图

**核心创新：**
- 数据驱动的噪声区间评估
- 高级 SNR 可视化
- 精确时空定位

**SNR 计算：**
```python
def compute_snr(signal_epoch, noise_interval, signal_interval):
    """计算分段SNR"""
    noise = signal_epoch[:, noise_interval[0]:noise_interval[1]]
    signal = signal_epoch[:, signal_interval[0]:signal_interval[1]]
    
    noise_power = np.mean(noise ** 2)
    signal_power = np.mean(signal ** 2)
    
    snr = 10 * np.log10(signal_power / noise_power)
    return snr
```

### 3. P300 亚成分检测

**两个关键亚成分：**
| 成分 | 位置 | 功能 |
|------|------|------|
| P3a | 额中央 | 新奇检测 |
| P3b | 顶叶 | 目标识别 |

**频带分析：**
- Delta (0.5-4 Hz) - P300 主要成分
- Theta (4-7.5 Hz) - 注意力调制
- Broadband (1-15 Hz) - 全频特征

### 4. 噪声区间敏感性

**关键发现：**
- 噪声区间选择显著影响 EEG 信号质量
- 警觉和任务参与状态调节噪声区间敏感性
- 跨会话相关性显示适应性需求

---

## 实现框架

```python
import numpy as np
from scipy import signal

class SegmentedSNRTopography:
    """分段SNR地形图分析"""
    
    def __init__(self, fs=500):
        self.fs = fs
        self.freq_bands = {
            'delta': (0.5, 4),
            'theta': (4, 7.5),
            'broadband': (1, 15)
        }
    
    def segment_snr_analysis(self, eeg_data, noise_intervals, signal_window):
        """分段SNR分析"""
        snr_topographies = {}
        
        for band_name, (fmin, fmax) in self.freq_bands.items():
            filtered = self._bandpass_filter(eeg_data, fmin, fmax)
            
            snr_maps = []
            for noise_int in noise_intervals:
                snr = self._compute_snr_map(filtered, noise_int, signal_window)
                snr_maps.append(snr)
            
            best_idx = np.argmax([np.max(s) for s in snr_maps])
            snr_topographies[band_name] = {
                'snr_map': snr_maps[best_idx],
                'best_noise_interval': noise_intervals[best_idx]
            }
        
        return snr_topographies
    
    def _bandpass_filter(self, data, fmin, fmax):
        """带通滤波"""
        b, a = signal.butter(4, 
            [fmin/(self.fs/2), fmax/(self.fs/2)], 
            btype='band')
        return signal.filtfilt(b, a, data, axis=1)
    
    def _compute_snr_map(self, data, noise_int, signal_win):
        """计算SNR地形图"""
        n_channels = data.shape[0]
        snr_map = np.zeros(n_channels)
        
        for ch in range(n_channels):
            avg_signal = np.mean(data[ch], axis=-1)
            noise = avg_signal[noise_int[0]:noise_int[1]]
            signal_seg = avg_signal[signal_win[0]:signal_win[1]]
            
            noise_power = np.mean(noise ** 2)
            signal_power = np.mean(signal_seg ** 2)
            
            snr_map[ch] = 10 * np.log10(signal_power / noise_power + 1e-10)
        
        return snr_map
```

---

## 应用场景

### 1. P300 BCI 优化
- P3a/P3b 亚成分精确检测
- SNR 导向的通道选择
- 实时信号质量监控

### 2. 临床诊断
- 神经生理异常检测
- 可解释的临床工具
- 量化指标

### 3. 自适应 BCI
- 警觉状态检测
- 任务参与度评估
- 动态噪声区间调整

---

## 关键参数

| 参数 | 推荐值 | 说明 |
|------|--------|------|
| Delta 频带 | 0.5-4 Hz | P300 主要成分 |
| Theta 频带 | 4-7.5 Hz | 注意力相关 |
| Broadband | 1-15 Hz | 全频特征 |
| 噪声区间 | 刺激前 200-500ms | 数据驱动选择 |

---

## 参考文献

- arXiv:2509.18599 - From Noise to Insight: Visualizing Neural Dynamics with Segmented SNR Topographies
## Activation Keywords

- segmented-snr-topography
- segmented-snr-topography 技能
- segmented-snr-topography skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Understand the Request

### Step 2: Search for Information

### Step 3: Apply the Framework

### Step 4: Provide Results

### Step 5: Verify Accuracy

## Examples

### Example 1: Basic Application

**User:** I need to apply Segmented SNR Topography - 分段SNR地形图可视化 to my analysis.

**Agent:** I'll help you apply segmented-snr-topography. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for segmented-snr-topography?

**Agent:** Let me search for the latest research and best practices...
