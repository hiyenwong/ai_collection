---
arxiv_id: 2304.01799v1
utility: 0.88
tags: [neural acoustic, Python, data processing, auditory neuroscience, preprocessing, feature extraction]
created: 2026-03-31
---

# naplib-python Neural Acoustic Processing

## Activation Keywords

- 神经声学数据处理
- naplib-python
- auditory neuroscience Python
- neural recording preprocessing
- acoustic feature extraction
- 神经信号预处理

## Problem Statement

听觉神经科学数据处理面临的问题：
- 数据格式不统一
- 试验持续时间不同
- 多模态刺激处理复杂
- 缺乏标准化分析工具

## Method Overview

naplib-python 提供统一解决方案：
1. 直观的数据结构处理神经记录和刺激
2. 完整的预处理工具链
3. 特征提取和分析工具
4. 与现有工具箱无缝集成

## Tools Used

| Component | Function |
|-----------|----------|
| Data Structure | Unified format for neural/stimuli data |
| Preprocessing | Filtering, normalization, artifact removal |
| Feature Extraction | Spectral, temporal features |
| Analysis | Statistical and visualization tools |

## Installation

```bash
pip install naplib
```

## Key Features

### 1. 统一数据结构

```python
import naplib as nl

# 创建数据结构
data = nl.Data()

# 添加神经记录
data.add_recording('neural', neural_data, sampling_rate=1000)

# 添加刺激
data.add_stimulus('audio', audio_stimulus, sampling_rate=44100)

# 支持不同试验持续时间
data.add_trial(trial_1, duration=2.5)
data.add_trial(trial_2, duration=3.2)  # 可以不同
```

### 2. 预处理工具

```python
from naplib import preprocessing

# 滤波
filtered = preprocessing.bandpass_filter(
    data, 
    lowcut=1, 
    highcut=100, 
    fs=1000
)

# 归一化
normalized = preprocessing.zscore(filtered)

# 去除伪迹
cleaned = preprocessing.remove_artifacts(
    data, 
    threshold=5.0  # z-score 阈值
)
```

### 3. 特征提取

```python
from naplib import features

# 频谱特征
spectral = features.spectral_features(
    data,
    n_fft=512,
    hop_length=256
)

# 时域特征
temporal = features.temporal_features(data)

# 声学特征
acoustic = features.acoustic_features(
    audio_data,
    sample_rate=44100,
    features=['mfcc', 'spectral_centroid', 'zero_crossing_rate']
)
```

### 4. 分析工具

```python
from naplib import analysis

# 时间锁定分析
locked = analysis.time_lock(
    data,
    event_times=event_onsets,
    window=(-0.5, 1.0)  # 事件前后窗口
)

# 相关性分析
corr = analysis.correlation(
    neural_data,
    stimulus_features,
    method='pearson'
)

# 可视化
analysis.plot_raster(data, trial_indices=[0, 1, 2])
analysis.plot_psth(data, bin_size=0.05)
```

## Example Workflow

```python
import naplib as nl
from naplib import preprocessing, features, analysis
import numpy as np

# 1. 加载数据
data = nl.load_data('experiment_data.npz')

# 2. 预处理
# 带通滤波 1-100 Hz
filtered = preprocessing.bandpass_filter(
    data['neural'],
    lowcut=1,
    highcut=100,
    fs=1000
)

# z-score 归一化
normalized = preprocessing.zscore(filtered)

# 3. 特征提取
# 从音频刺激提取 MFCC
mfcc = features.mfcc(
    data['audio'],
    sample_rate=44100,
    n_mfcc=13
)

# 4. 时间锁定分析
# 对齐到刺激开始
aligned = analysis.time_lock(
    normalized,
    event_times=data['stimulus_onset'],
    window=(-0.2, 0.8)
)

# 5. 可视化
analysis.plot_psth(aligned, bin_size=0.02)
analysis.plot_heatmap(aligned)

# 6. 保存结果
nl.save_data(aligned, 'processed_data.npz')
```

## Data Structure Details

### Naplib Data Format

```python
class Data:
    """
    统一数据结构
    
    属性：
    - recording: 神经记录 (n_trials, n_timepoints, n_channels)
    - stimulus: 刺激数据 (n_trials, n_timepoints, n_features)
    - sampling_rate: 采样率
    - metadata: 元数据字典
    """
    
    # 示例
    data.recording.shape  # (trials, time, channels)
    data.stimulus.shape   # (trials, time, features)
    data.sampling_rate    # 1000 Hz
```

### 支持的数据类型

| 类型 | 描述 |
|------|------|
| 神经记录 | 电生理、fMRI、钙成像 |
| 音频刺激 | 声音波形、频谱图 |
| 行为数据 | 反应时间、选择 |
| 元数据 | 试验条件、受试者信息 |

## Integration with Other Tools

### 与现有工具箱集成

```python
# 导出为 NumPy
numpy_array = data.to_numpy()

# 导出为 Pandas
df = data.to_dataframe()

# 与 MNE-Python 集成
import mne
raw = mne.io.RawArray(data.recording, mne.Info(...))

# 与 SciPy 集成
from scipy import signal
spectrogram = signal.spectrogram(data.recording)
```

## API Reference

### Preprocessing Module

```python
preprocessing.bandpass_filter(data, lowcut, highcut, fs)
preprocessing.highpass_filter(data, cutoff, fs)
preprocessing.lowpass_filter(data, cutoff, fs)
preprocessing.notch_filter(data, freq, fs)
preprocessing.zscore(data)
preprocessing.remove_artifacts(data, threshold)
preprocessing.interpolate_bad_channels(data, bad_idx)
```

### Features Module

```python
features.mfcc(audio, sample_rate, n_mfcc=13)
features.spectral_features(data, n_fft, hop_length)
features.temporal_features(data)
features.acoustic_features(audio, sample_rate, features)
features.spectral_centroid(audio, sample_rate)
features.zero_crossing_rate(audio)
```

### Analysis Module

```python
analysis.time_lock(data, event_times, window)
analysis.correlation(x, y, method='pearson')
analysis.pca(data, n_components)
analysis.clustering(data, n_clusters, method='kmeans')
analysis.plot_raster(data, trial_indices)
analysis.plot_psth(data, bin_size)
analysis.plot_heatmap(data)
```

## Benefits

| 特性 | 传统方法 | naplib-python |
|------|---------|---------------|
| 数据格式 | 自定义 | 统一标准 |
| 试验时长 | 需对齐 | 自动处理 |
| 多模态 | 手动同步 | 内置支持 |
| 可复现性 | 低 | 高 |
| 学习曲线 | 陡峭 | 平缓 |

## References

- Mischler, G. et al. (2023). naplib-python: Neural Acoustic Data Processing and Analysis Tools in Python. arXiv:2304.01799.
- GitHub: https://github.com/naplab/naplib
- Documentation: https://naplib.readthedocs.io

## Related Skills

- eeg-brain-connectivity-bci
- neural-code-dynamics-analysis
- spike-timing-neuronal-assemblies