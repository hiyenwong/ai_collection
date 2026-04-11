---
name: spatiotemporal-neural-coherence
description: '时空神经一致性解码方法论。使用 EEG 和光流特征构建预测性神经动力学的时空表征。适用于视觉语言处理的神经解码、预测推理分析。触发词：神经解码、预测推理、视觉语言、EEG 分析、光流特征、neural decoding、predictive inference、visual language。'
user-invocable: true
---

# Spatiotemporal Neural Coherence - 时空神经一致性解码

## 核心思想

通过神经信号（EEG）与光流衍生运动特征的相干性，构建预测性神经动力学的时空表征，解码视觉语言处理中的预测推理机制。

**来源：** arXiv:2512.20929 (NeurIPS 2025 Workshop)
**效用：** 1.0

---

## 方法论

### 1. 数据采集

**输入信号：**
- EEG 神经信号（高时间分辨率）
- 视觉语言刺激（如手语视频）
- 光流特征（从视频提取运动信息）

**实验设计：**
- 对比条件：正常语言刺激 vs 时间反转刺激
- 被试群体：Deaf signers（经验依赖分析）

### 2. 特征提取

**光流特征：**
- 从视觉刺激提取运动向量
- 计算运动方向和速度
- 构建时序运动特征

**神经-运动相干性：**
```
coherence = |EEG_signal ⊗ optical_flow_features|
```

**频带分解：**
- Delta (1-4 Hz)
- Theta (4-8 Hz)
- Alpha (8-12 Hz)
- Beta (12-30 Hz)
- Gamma (30-100 Hz)

### 3. 熵特征选择

**核心创新：** 使用熵筛选频率特异性神经签名

**步骤：**
1. 计算每个频带-电极组合的相干性熵
2. 识别高区分度特征（正常 vs 时间反转）
3. 选择最具信息量的时空特征

**熵计算：**
```python
def entropy_feature_selection(coherence_matrix):
    """
    计算相干性特征的熵，用于特征选择
    """
    # 正常条件下的相干性分布
    p_normal = coherence_matrix['normal'] / np.sum(coherence_matrix['normal'])
    # 时间反转条件下的相干性分布
    p_reversed = coherence_matrix['reversed'] / np.sum(coherence_matrix['reversed'])
    
    # 计算KL散度作为区分度度量
    kl_divergence = np.sum(p_normal * np.log(p_normal / p_reversed + 1e-10))
    
    return kl_divergence
```

### 4. 时空表征构建

**空间维度：** 电极位置（脑区）
**时间维度：** 频带动态

**关键发现：**
- 分布式左半球一致性 → 语言理解核心
- 额叶低频相干性 → 预测处理
- 经验依赖签名与年龄相关

---

## 应用场景

### 1. 神经解码研究

- 视觉语言处理机制
- 预测推理神经基础
- 经验驱动的神经可塑性

### 2. BCI 应用

- 语言相关 BCI 特征选择
- 注意力状态监测
- 认知负荷评估

### 3. 临床应用

- 语言障碍诊断
- 神经康复评估
- 学习效果追踪

---

## 实现工具

**Python 库：**
- `mne` - EEG 信号处理
- `numpy` - 数值计算
- `scipy.signal.coherence` - 相干性分析
- `opencv` - 光流计算

**示例代码：**

```python
import mne
import numpy as np
from scipy.signal import coherence
import cv2

def compute_spatiotemporal_coherence(eeg_data, video_frames, fs=500):
    """
    计算时空神经一致性
    
    Parameters:
    -----------
    eeg_data : np.ndarray, shape (n_channels, n_samples)
        EEG 信号
    video_frames : np.ndarray, shape (n_frames, H, W)
        视频帧序列
    fs : float
        采样率
    
    Returns:
    --------
    coherence_map : np.ndarray
        时空相干性图
    """
    # 1. 提取光流特征
    motion_features = extract_optical_flow(video_frames)
    
    # 2. 频带分解
    freq_bands = {
        'delta': (1, 4),
        'theta': (4, 8),
        'alpha': (8, 12),
        'beta': (12, 30),
        'gamma': (30, 100)
    }
    
    coherence_map = {}
    for band_name, (fmin, fmax) in freq_bands.items():
        # 带通滤波
        eeg_filtered = mne.filter.filter_data(
            eeg_data, fs, fmin, fmax
        )
        
        # 计算相干性
        f, coh = coherence(
            eeg_filtered.mean(axis=0),  # 全脑平均
            motion_features,
            fs=fs,
            nperseg=1024
        )
        
        coherence_map[band_name] = coh
    
    return coherence_map

def extract_optical_flow(frames):
    """从视频帧提取光流运动特征"""
    flows = []
    prev_gray = cv2.cvtColor(frames[0], cv2.COLOR_BGR2GRAY)
    
    for frame in frames[1:]:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(
            prev_gray, gray, None,
            pyr_scale=0.5, levels=3, winsize=15,
            iterations=3, poly_n=5, poly_sigma=1.2, flags=0
        )
        # 计算运动幅值
        magnitude = np.sqrt(flow[..., 0]**2 + flow[..., 1]**2)
        flows.append(magnitude.mean())
        prev_gray = gray
    
    return np.array(flows)
```

---

## 关键参数

| 参数 | 推荐值 | 说明 |
|------|--------|------|
| 采样率 | 500 Hz | EEG 高时间分辨率 |
| 频带 | Delta-Theta | 语言预测相关 |
| 相干窗口 | 1024 samples | 平衡时频分辨率 |
| 光流金字塔层数 | 3 | 运动检测精度 |

---

## 预期结果

1. **频率特异性签名：** 识别区分语言理解的关键频带
2. **脑区定位：** 左半球和额叶作为预测处理核心
3. **经验依赖性：** 年龄/经验与神经签名强度相关

---

## 注意事项

- 需要同步采集 EEG 和视频数据
- 光流计算对视频质量敏感
- 熵特征选择需要足够的试次数量
- 考虑个体差异和经验背景

---

## 参考文献

- arXiv:2512.20929 - Decoding Predictive Inference in Visual Language Processing via Spatiotemporal Neural Coherence
- NeurIPS 2025 Workshop: Foundation Models for the Brain and Body
## Activation Keywords

- spatiotemporal-neural-coherence
- spatiotemporal-neural-coherence 技能
- spatiotemporal-neural-coherence skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 频率特异性签名：

### Step 2: 脑区定位：

### Step 3: 经验依赖性：

### Step 4: Understand the Request

### Step 5: Search for Information

## Examples

### Example 1: Basic Application

**User:** I need to apply Spatiotemporal Neural Coherence - 时空神经一致性解码 to my analysis.

**Agent:** I'll help you apply spatiotemporal-neural-coherence. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for spatiotemporal-neural-coherence?

**Agent:** Let me search for the latest research and best practices...
