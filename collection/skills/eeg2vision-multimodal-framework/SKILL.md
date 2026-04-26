---
name: eeg2vision-multimodal-framework
description: "Multimodal EEG-to-image reconstruction framework using diffusion models with LLM-guided post-processing. Supports low-density EEG configurations (24-128 channels). Activation: EEG2Vision, EEG reconstruction, brain-to-image, multimodal brain decoding."
---

# EEG2Vision: Multimodal EEG-Based Visual Reconstruction

## Description
EEG2Vision是一种模块化的端到端EEG到图像重建框架，使用条件扩散模型结合多模态大语言模型(MLLM)引导的后处理增强，实现从非侵入性EEG信号重建视觉刺激。特别针对低密度电极配置(24-128通道)进行优化。

## Core Architecture

### 1. 系统概述
```
EEG Input → Feature Extraction → Conditional Diffusion → MLLM Enhancement → Reconstructed Image
```

### 2. 主要组件

#### 2.1 EEG编码器
- 支持多分辨率输入：128, 64, 32, 24通道
- 处理低空间分辨率和高噪声
- 提取语义和结构特征

#### 2.2 条件扩散重建
- EEG条件化的扩散模型
- 生成初步视觉重建
- 保持EEG驱动的结构约束

#### 2.3 语义增强模块 (Boosting Stage)
- **MLLM语义提取**: 使用多模态大语言模型提取语义描述
- **图像到图像扩散**: 细化几何和感知一致性
- **保持EEG结构**: 在增强过程中保留EEG驱动的结构

### 3. 关键技术

#### 3.1 多分辨率支持
| 通道数 | Top-1准确率 | FID分数 | IS提升 |
|--------|-------------|---------|--------|
| 128 | 89% | 76.77 | 基准 |
| 64 | - | ~78 | 中等 |
| 32 | - | ~79 | 中等 |
| 24 | 38% | 80.51 | +9.71% |

#### 3.2 语义解码vs重建质量
- 语义解码准确率随通道减少显著下降（89%→38%）
- 重建质量(FID)下降相对较小（76.77→80.51）
- 后处理增强在所有配置下持续改善感知指标

### 4. 创新点

#### 4.1 模块化设计
- 独立的编码、重建、增强模块
- 易于扩展和替换组件
- 支持不同EEG设备配置

#### 4.2 提示引导增强
```python
# MLLM提取语义
description = mllm.describe(initial_reconstruction)

# 图像到图像扩散增强
enhanced_image = img2img_diffusion(
    initial_reconstruction,
    prompt=description,
    strength=0.7
)
```

#### 4.3 实验室外应用
- 支持低密度EEG设备
- 实时脑到图像应用潜力
- 降低硬件门槛

## Activation Keywords
- EEG2Vision
- EEG reconstruction
- brain-to-image
- 脑电重建
- multimodal brain decoding
- diffusion model EEG
- 扩散模型脑解码
- low-density EEG

## Tools Used
- **pytorch**: 深度学习框架
- **diffusers**: 扩散模型库
- **mne-python**: EEG数据处理
- **transformers**: MLLM接口

## Workflow

### Step 1: EEG预处理
```python
import mne

# 加载EEG数据
raw = mne.io.read_raw_edf('eeg_data.edf')
# 滤波
raw.filter(1, 40)
# 提取epochs
epochs = mne.Epochs(raw, events, event_id, tmin=-0.2, tmax=0.5)
```

### Step 2: 特征提取
```python
# 提取时频特征
# 或使用预训练编码器
features = eeg_encoder(epochs.get_data())
```

### Step 3: 条件扩散生成
```python
from diffusers import StableDiffusionImg2ImgPipeline

# 初始重建
initial_image = diffusion_pipeline(
    prompt="visual reconstruction",
    conditioning=features,
    strength=0.8
)
```

### Step 4: MLLM增强
```python
# 提取语义描述
description = multimodal_llm.describe(initial_image)

# 图像增强
final_image = img2img_pipeline(
    image=initial_image,
    prompt=description,
    strength=0.4
)
```

## Examples

### Example 1: 视觉刺激重建
```python
# 完整流程
eeg_data = load_eeg('subject_001.eeg')
reconstruction = eeg2vision.reconstruct(
    eeg=eeg_data,
    channels=64,  # 支持24-128
    use_boosting=True  # 启用MLLM增强
)
```

### Example 2: 对比不同通道配置
```python
for ch in [128, 64, 32, 24]:
    result = eeg2vision.reconstruct(
        eeg=downsample(eeg_full, ch),
        channels=ch
    )
    evaluate(result, ground_truth)
```

## Performance Metrics

### 定量指标
- **FID (Frechet Inception Distance)**: 76.77 (128ch) → 80.51 (24ch)
- **IS (Inception Score)**: 基准 + 9.71%提升 (boosting)
- **Top-1 Accuracy**: 89% (128ch) → 38% (24ch)

### 用户研究
- 感知偏好测试确认增强重建的优越性
- 主观质量评分显著提升

## Limitations
- 语义解码准确率随通道数减少显著下降
- 高密度EEG(128ch)效果最佳
- MLLM增强引入额外计算开销

## References
- arXiv:2604.08063v1 (2026-04-09)
- Authors: Emanuele Balloni, Emanuele Frontoni, Chiara Matti, et al.
- Categories: cs.CV

## Related Skills
- eeg2vision-multimodal-reconstruction
- eeg2vision-multimodal-eeg-based-framework-visual
- brain3d-eeg-multimodal

---
_Last updated: 2026-04-14_
