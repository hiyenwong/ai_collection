---
name: chasmbrain-mamba-brain-reconstruction
description: CHASMBrain - Hierarchical Mamba architecture for image-to-fMRI brain reconstruction with coarse-to-fine strategy. Use when building brain encoding models, visual cortex modeling, or implementing Mamba-based neural decoding systems. Separates global semantic (CLS) and local spatial (patch) processing streams for anatomically-specialized predictions.
license: MIT
---

# CHASMBrain: Hierarchical Mamba for Brain Reconstruction

## Overview

**论文**: "Coarse-to-fine Hierarchical Architecture with Sequential Mamba for Brain Reconstruction" (arXiv:2606.04772)
**核心创新**: 双流 Mamba 设计分离全局语义与局部空间，粗到细分层策略预测 ROI → voxel

## 核心方法论

### 1. 问题背景

**图像到 fMRI 编码的挑战**:
- 视觉皮层层级组织复杂
- 现有模型与脑层级对应性弱
- 传统方法无法区分功能专化

**灵感**: 视觉皮层的功能分离
- **早期视觉区** (V1-V3): 位置/方向特异性 → 局部空间
- **高阶区域** (IT): 语义/物体特异性 → 全局语义

### 2. 双流 Mamba 架构

```python
import torch
import torch.nn as nn
from mamba_ssm import Mamba

class DualStreamMamba(nn.Module):
    """
    双流 Mamba: 分离 CLS (语义) 和 Patch (空间)
    
    设计原理:
    - CLS stream: 捕获全局语义 → 高阶视觉区
    - Patch stream: 捕获局部位置 → 早期视觉区
    """
    
    def __init__(self, d_model=256, n_layers=4):
        super().__init__()
        
        # CLS stream: 全局语义处理
        self.cls_mamba = nn.ModuleList([
            Mamba(d_model=d_model, d_state=16, d_conv=4, expand=2)
            for _ in range(n_layers)
        ])
        
        # Patch stream: 局部空间处理
        self.patch_mamba = nn.ModuleList([
            Mamba(d_model=d_model, d_state=16, d_conv=4, expand=2)
            for _ in range(n_layers)
        ])
        
        # 融合层
        self.fusion = nn.Linear(d_model * 2, d_model)
    
    def forward(self, cls_token, patch_tokens):
        """
        Args:
            cls_token: (B, 1, D) - 全局语义
            patch_tokens: (B, N, D) - 局部空间
        
        Returns:
            fused: (B, N+1, D) - 融合表示
        """
        # CLS stream processing
        cls_out = cls_token
        for mamba_layer in self.cls_mamba:
            cls_out = mamba_layer(cls_out)
        
        # Patch stream processing
        patch_out = patch_tokens
        for mamba_layer in self.patch_mamba:
            patch_out = mamba_layer(patch_out)
        
        # 融合
        # 注意: 不同流对应不同脑区
        return cls_out, patch_out
```

### 3. 粗到细分层策略

```python
class CHASMBrain(nn.Module):
    """
    CHASMBrain: Stage 1 (ROI-level) → Stage 2 (voxel-level)
    
    两阶段设计:
    - Stage 1: 预测去噪 ROI 级激活
    - Stage 2: Mamba-VAE 精细 voxel 级预测
    """
    
    def __init__(self, n_rois=10, n_voxels_per_roi=1000):
        super().__init__()
        
        # 视觉特征提取 (如 DINOv2)
        self.backbone = load_dino_v2()
        
        # Stage 1: ROI-level coarse prediction
        self.stage1_roi = nn.Sequential(
            DualStreamMamba(d_model=256),
            nn.Linear(256, n_rois)
        )
        
        # Stage 2: Voxel-level refinement
        self.stage2_vae = MambaVAE(
            latent_dim=128,
            n_voxels=n_voxels_per_roi
        )
    
    def forward(self, image):
        """
        Args:
            image: (B, 3, H, W)
        
        Returns:
            roi_activations: (B, n_rois)
            voxel_predictions: (B, n_voxels)
        """
        # 提取视觉特征
        cls_token, patch_tokens = self.backbone(image)
        
        # Stage 1: ROI coarse
        cls_out, patch_out = self.stage1_roi(cls_token, patch_tokens)
        roi_activations = self.aggregate_to_roi(cls_out, patch_out)
        
        # Stage 2: Voxel refinement
        voxel_predictions = self.stage2_vae(roi_activations, patch_out)
        
        return roi_activations, voxel_predictions
    
    def aggregate_to_roi(self, cls_out, patch_out):
        """
        聚合到 ROI 级
        
        关键发现:
        - patch stream → 早期视觉 ROI (V1-V3)
        - CLS stream → 高阶视觉 ROI (OTC)
        """
        # ROI-specific pooling
        roi_activations = []
        
        # Early visual ROIs: use patch stream
        early_rois = torch.mean(patch_out[:, :5, :], dim=1)
        
        # Higher-order ROIs: use CLS stream
        higher_rois = cls_out.squeeze(1)
        
        roi_activations = torch.cat([early_rois, higher_rois], dim=1)
        return roi_activations
```

### 4. Mamba-VAE 细化模块

```python
class MambaVAE(nn.Module):
    """
    Mamba-based VAE for voxel-level refinement
    
    将粗 ROI 预测细化为 voxel 级激活
    """
    
    def __init__(self, latent_dim=128, n_voxels=1000):
        super().__init__()
        
        # Encoder: ROI → latent
        self.encoder = nn.Sequential(
            Mamba(d_model=256, d_state=16),
            nn.Linear(256, latent_dim * 2)  # mean + logvar
        )
        
        # Decoder: latent → voxels
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256),
            Mamba(d_model=256, d_state=16, expand=n_voxels // 256),
            nn.Linear(256, n_voxels)
        )
    
    def forward(self, roi_activations, spatial_context):
        """
        Args:
            roi_activations: (B, n_rois)
            spatial_context: (B, N, D) from patch stream
        
        Returns:
            voxel_predictions: (B, n_voxels)
        """
        # Encode ROI to latent
        latent_params = self.encoder(roi_activations)
        mean, logvar = latent_params.chunk(2, dim=-1)
        
        # Sample latent
        z = self.sample_latent(mean, logvar)
        
        # Decode to voxels with spatial context
        voxels = self.decoder(z)
        
        return voxels
    
    def sample_latent(self, mean, logvar):
        """VAE latent sampling"""
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mean + eps * std
```

## 实验结果

**Natural Scenes Dataset (NSD)**:

| 模型 | Pearson Correlation | MSE |
|------|-------------------|-----|
| Ridge Regression | 0.358 | 0.293 |
| DINOv2 Linear Probe | 0.391 | 0.278 |
| **CHASMBrain** | **0.429** | **0.261** |

## 关键发现：因果分支消融

**实验设计**: 分别消融 CLS stream 和 Patch stream

**核心发现**:
```
Patch Stream 消融 → 早期视觉区 (V1-V3) 性能下降
CLS Stream 消融 → 高阶区域 (OTC) 性能下降

结论: 
- Patch stream 专化于早期视觉（视网膜拓扑区）
- CLS stream 专化于高阶语义区
- 对应关系是因果性的，不仅是相关性
```

## 跨被试迁移

```python
def cross_subject_transfer(source_model, target_subject_data):
    """
    CHASMBrain 跨被试迁移
    
    发现: backbone 学到的表示是被试无关的
    只需少量 per-subject adaptation
    """
    # 加载预训练 backbone
    backbone = source_model.backbone
    
    # 目标被试少量数据
    target_images, target_fmri = target_subject_data
    
    # 最小适配
    adaptation_layer = nn.Linear(256, target_fmri.shape[1])
    
    # Fine-tune on target
    for img, fmri in zip(target_images[:50], target_fmri[:50]):
        pred = backbone(img)
        adaptation_layer(pred)
    
    return adapted_model
```

## 应用场景

### 1. 视觉皮层建模
```python
# 预测特定 ROI 的激活
model = CHASMBrain()
roi_names = ['V1', 'V2', 'V3', 'V4', 'OTC']

for roi in roi_names:
    activations = model.predict_roi(image, roi)
    visualize_roi_activation(activations, roi)
```

### 2. 脑-模型对应性分析
```python
# 消融实验分析脑区专化
cls_contribution = model.cls_stream_ablation(image)
patch_contribution = model.patch_stream_ablation(image)

# 比对真实 fMRI
correlation_cls = correlate(cls_contribution, real_fmri['OTC'])
correlation_patch = correlate(patch_contribution, real_fmri['V1-V3'])
```

### 3. 神经解码器设计
```python
# 逆向: fMRI → image reconstruction
class BrainToImageDecoder(nn.Module):
    def __init__(self):
        self.inverted_mamba = InvertedMamba()
        self.generator = DiffusionGenerator()
    
    def forward(self, fmri_activations):
        # fMRI → latent → image
        latent = self.inverted_mamba(fmri_activations)
        image = self.generator(latent)
        return image
```

## 实现要点

### 数据预处理

```python
def preprocess_nsd_data(nsd_dataset):
    """
    NSD 数据预处理
    
    Args:
        nsd_dataset: Natural Scenes Dataset
    
    Returns:
        images: 预处理图像
        fmri: 对应 fMRI voxel 激活
    """
    # 图像标准化
    images = normalize_images(nsd_dataset.images)
    
    # fMRI 去噪 + ROI 定义
    fmri = denoise_fmri(nsd_dataset.fmri)
    
    # ROI 分组
    roi_activations = {
        'early_visual': fmri[:, early_visual_mask],
        'higher_order': fmri[:, higher_order_mask]
    }
    
    return images, fmri, roi_activations
```

### 避免陷阱

**常见错误**:
1. ✗ 单流处理所有特征 → 无法区分功能专化
2. ✗ 直接预测 voxel → 计算成本高 + 噪声敏感
3. ✗ 固定 backbone → 跨被试迁移差

**正确做法**:
1. ✓ 双流分离: CLS (语义) + Patch (空间)
2. ✓ 粗到细: ROI → Voxel 分层预测
3. ✓ 共享 backbone + per-subject adaptation

## 代码资源

**Mamba SSM**: https://github.com/state-spaces/mamba

**NSD Dataset**: https://naturalscenesdataset.org

**依赖**:
- Python 3.9+
- PyTorch 2.0+
- mamba-ssm
- einops

## 扩展方向

1. **动态视觉**: 视频 → 时序 fMRI 编码
2. **多模态**: 视觉 + 语言 Mamba 融合
3. **逆向解码**: fMRI → 图像重建
4. **临床应用**: 视觉功能障碍诊断

## 关键论文引用

```bibtex
@article{vo2026chasmbrain,
  title={Coarse-to-fine Hierarchical Architecture with Sequential Mamba for Brain Reconstruction},
  author={Vo, Hoang-Son and Bui, Van-Hung and Mai-Duc, Minh-Huy and Mai, Tien-Dung and Kim, Soo-Hyung},
  journal={arXiv preprint arXiv:2606.04772},
  year={2026}
}
```

---

**Activation Keywords**: CHASMBrain, Mamba brain reconstruction, image-to-fMRI, visual cortex modeling, dual-stream Mamba, ROI voxel prediction, coarse-to-fine neural decoding, NSD dataset