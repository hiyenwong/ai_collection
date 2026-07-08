---
name: neuroscience-of-transformers
description: 使用Transformer架构建模脑数据的范式。系统化回顾Transformer在fMRI、EEG、MEG、ECoG等脑信号中的应用，识别输入表示和神经对齐策略等关键设计选择。适用于脑-文本解码、脑-图像重建、脑信号预测。触发词：neuroscience of transformers, brain signal modeling, neural alignment, brain-to-text, brain-to-image, fMRI transformer, EEG transformer
version: 1.0.0
metadata:
  hermes:
    tags: [neuroscience, transformer, brain-signal, fmri, eeg, decoding, neural-alignment]
    source_paper: "The Neuroscience of Transformers: Using transformer architectures to model the brain (arXiv:2604.18195)"
    published: "2026-04-19"
---

# Neuroscience of Transformers

## Overview

使用Transformer架构建模脑数据的系统性范式。涵盖fMRI、EEG、MEG、ECoG等多种脑信号模态的建模方法。

## Key Design Choices

### 1. Input Representation
| 模态 | 输入表示 | 空间维度 | 时间维度 |
|------|---------|---------|---------|
| fMRI | 体素时间序列 | 91×109×91 | ~1000 TRs |
| EEG | 电极时间序列 | 64-256 channels | 1000+ Hz |
| MEG | 传感器时间序列 | 306 channels | 1000+ Hz |
| ECoG | 皮层电极阵列 | 64-256 electrodes | 500-2000 Hz |

### 2. Neural Alignment Strategies

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class NeuralAlignment(nn.Module):
    """神经对齐策略实现"""
    def __init__(self, brain_dim, model_dim):
        super().__init__()
        # 线性投影：将脑信号映射到模型表示空间
        self.projection = nn.Linear(brain_dim, model_dim)
        # RSA（表征相似性分析）对齐损失
        self.alignment_weight = nn.Parameter(torch.ones(1))
    
    def rsa_loss(self, brain_repr, model_repr):
        """表征相似性分析损失"""
        # 计算两个表征的RSA矩阵
        brain_sim = F.cosine_similarity(
            brain_repr.unsqueeze(1), brain_repr.unsqueeze(0), dim=-1
        )
        model_sim = F.cosine_similarity(
            model_repr.unsqueeze(1), model_repr.unsqueeze(0), dim=-1
        )
        # MSE between similarity matrices
        return F.mse_loss(brain_sim, model_sim)
    
    def forward(self, brain_signal, model_repr):
        projected = self.projection(brain_signal)
        loss = self.rsa_loss(projected, model_repr)
        return projected, loss
```

## Task-Specific Implementations

### Brain-to-Text Decoding
```python
class BrainToTextDecoder(nn.Module):
    def __init__(self, brain_dim, vocab_size, hidden_dim=768):
        super().__init__()
        self.align = NeuralAlignment(brain_dim, hidden_dim)
        self.decoder = nn.TransformerDecoder(
            nn.TransformerDecoderLayer(hidden_dim, nhead=8),
            num_layers=6
        )
        self.vocab_proj = nn.Linear(hidden_dim, vocab_size)
    
    def decode_brain(self, brain_signal):
        aligned, _ = self.align(brain_signal, None)
        text_logits = self.vocab_proj(self.decoder(aligned))
        return text_logits
```

### Brain-to-Image Reconstruction
```python
class BrainToImageReconstructor(nn.Module):
    def __init__(self, brain_dim, image_size=256):
        super().__init__()
        self.align = NeuralAlignment(brain_dim, 768)
        # 使用扩散模型作为图像先验
        self.diffusion_prior = nn.Linear(768, image_size * image_size * 3)
    
    def reconstruct(self, brain_signal):
        aligned, _ = self.align(brain_signal, None)
        image = self.diffusion_prior(aligned)
        return image.view(-1, 3, image_size, image_size)
```

## Implementation Guidelines

1. **模态特定预处理**: 不同脑信号需要不同的预处理（fMRI需要空间标准化，EEG需要重参考）
2. **对齐策略选择**: RSA适用于语义对齐，CCA适用于跨模态对齐
3. **数据增强**: 使用噪声注入、时间扭曲等增强策略
4. **评估指标**: Pearson correlation, classification accuracy, BLEU/CLIP score

## References
- Zhang et al. (2026). The Neuroscience of Transformers. arXiv:2604.18195
