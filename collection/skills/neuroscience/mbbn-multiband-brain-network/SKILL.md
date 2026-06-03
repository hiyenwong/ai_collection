---
name: mbbn-multiband-brain-network
description: Multi-Band Brain Net (MBBN) — Transformer-based framework for frequency-specific spatiotemporal brain dynamics from fMRI. Integrates biologically-grounded frequency decomposition with multi-band self-attention for cognitive and psychiatric applications. Use when analyzing frequency-dependent brain network interactions, building fMRI-based prediction models for psychiatric disorders (depression, ADHD, ASD), or developing scale-aware neural biomarkers.
user-invocable: true
---

# Multi-Band Brain Network (MBBN)

**来源论文：** arXiv:2503.23394 (v2, 2025-06-17) - "Spatiotemporal Learning of Brain Dynamics from fMRI Using Frequency-Specific Multi-Band Attention for Cognitive and Psychiatric Applications"
**作者:** Sangyoon Bae, Junbeom Kwon, Shinjae Yoo, Jiook Cha

## 核心方法论

### 1. 问题背景

传统神经影像分析假设线性与平稳性，无法捕捉频率特异性神经计算。大脑功能动力学展现跨时间尺度的无标度和多重分形特性，需要频率感知的分析方法。

### 2. MBBN 架构

```
fMRI BOLD信号 → 频带分解 → 多频带自注意力 → 时空表征 → 预测输出
                     ↓
              5个生理相关频带:
              - Ultra-low (<0.01 Hz): 慢速全局波动
              - Low (0.01-0.027 Hz): 默认网络
              - Mid (0.027-0.073 Hz): 感觉运动网络
              - High (0.073-0.198 Hz): 注意网络
              - Ultra-high (0.198-0.25 Hz): 快速局部交互
```

### 3. 关键技术

#### 3.1 频带分解
```python
# 带通滤波分离频率成分
from scipy.signal import butter, filtfilt

def band_decompose(signal, fs, bands):
    """多频带分解"""
    decomposed = {}
    for name, (low, high) in bands.items():
        nyquist = fs / 2
        b, a = butter(4, [low/nyquist, high/nyquist], btype='band')
        decomposed[name] = filtfilt(b, a, signal, axis=0)
    return decomposed
```

#### 3.2 多频带自注意力
```python
import torch
import torch.nn as nn

class MultiBandAttention(nn.Module):
    """
    多频带自注意力机制
    每个频带独立计算注意力，然后融合
    """
    def __init__(self, n_bands, n_regions, d_model, n_heads):
        super().__init__()
        self.n_bands = n_bands
        self.band_attentions = nn.ModuleList([
            nn.MultiheadAttention(d_model, n_heads, batch_first=True)
            for _ in range(n_bands)
        ])
        self.band_weights = nn.Parameter(torch.ones(n_bands))
        self.output_proj = nn.Linear(d_model, d_model)
    
    def forward(self, band_features):
        """
        Args:
            band_features: list of [batch, seq_len, d_model], one per band
        """
        # 每个频带独立计算注意力
        attended = []
        for i, (attn, feat) in enumerate(zip(self.band_attentions, band_features)):
            out, _ = attn(feat, feat, feat)
            attended.append(out)
        
        # 频带加权融合
        weights = torch.softmax(self.band_weights, dim=0)
        fused = sum(w * a for w, a in zip(weights, attended))
        
        return self.output_proj(fused)
```

#### 3.3 时空建模
```python
class MBBN(nn.Module):
    """Multi-Band Brain Network"""
    
    def __init__(self, n_regions, n_bands=5, d_model=64, n_heads=4, n_layers=2):
        super().__init__()
        self.region_embedding = nn.Linear(1, d_model)  # 每个脑区独立嵌入
        self.temporal_position = nn.Parameter(torch.randn(100, d_model))  # 位置编码
        
        self.mbbn_layers = nn.ModuleList([
            MultiBandAttention(n_bands, n_regions, d_model, n_heads)
            for _ in range(n_layers)
        ])
        
        self.classifier = nn.Sequential(
            nn.Linear(n_regions * d_model, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 1)
        )
    
    def forward(self, band_features):
        # band_features: list of [batch, time, regions], one per band
        
        # 嵌入
        embedded_bands = []
        for feat in band_features:
            batch, time, regions = feat.shape
            # 重塑 + 嵌入
            x = feat.view(batch * time, regions, 1)
            x = self.region_embedding(x)  # [batch*time, regions, d_model]
            x = x + self.temporal_position[:time].unsqueeze(1)
            x = x.view(batch, time, regions, -1)
            embedded_bands.append(x)
        
        # 多层处理
        for layer in self.mbbn_layers:
            # 按时间步处理
            new_bands = []
            for band_data in embedded_bands:
                band_out = layer([band_data[:, t] for t in range(band_data.size(1))])
                new_bands.append(band_out)
            embedded_bands = new_bands
        
        # 池化 + 分类
        pooled = [b.mean(dim=1) for b in embedded_bands]  # 时间平均
        fused = sum(pooled) / len(pooled)
        return self.classifier(fused.view(fused.size(0), -1))
```

### 4. 关键发现

#### 4.1 疾病特异性频率签名

| 疾病 | 高频特征 | 低频特征 |
|------|----------|----------|
| ADHD | 额叶-感觉运动连接减弱 | - |
| ASD | 眶额-体感回路高频中断 | 颞顶-前额叶超低频耦合增强 |

#### 4.2 性能提升
- 在抑郁症、ADHD、ASD 分类任务中 AUROC 提升高达 52.5%
- 训练数据：49,673 人 (UK Biobank, ABCD, ABIDE)
- 特别在分类任务中表现突出

#### 4.3 动态枢纽发现
- ADHD: 盖部体感节点成为动态枢纽
- 高频连接变化比低频更具区分力

## 数据处理流程

### Step 1: 预处理
1. 标准 fMRI 预处理 (motion correction, slice timing, normalization)
2. 脑区分割 (AAL, Harvard-Oxford, 或 Schaefer atlas)
3. 提取每个脑区的 BOLD 时间序列

### Step 2: 频带分解
```python
# fMRI TR ≈ 2s, Nyquist = 0.25 Hz
bands = {
    'ultra_low': (0.0, 0.01),
    'low': (0.01, 0.027),
    'mid': (0.027, 0.073),
    'high': (0.073, 0.198),
    'ultra_high': (0.198, 0.25)
}
```

### Step 3: 模型训练
```python
# 训练配置
config = {
    'batch_size': 32,
    'learning_rate': 1e-4,
    'n_epochs': 100,
    'n_bands': 5,
    'd_model': 64,
    'n_heads': 4,
    'n_layers': 2,
    'dropout': 0.3
}
```

### Step 4: 解释分析
- 注意力权重分析 → 识别重要频带
- 梯度分析 → 识别关键脑区
- 频带重要性排序 → 发现疾病特异性频率签名

## 激活关键词
- MBBN
- multi-band brain network
- frequency-specific fMRI
- transformer brain dynamics
- fMRI psychiatric prediction
- ADHD fMRI classification
- ASD brain network
- 多频带脑网络
- 频率特异性fMRI
- 精神疾病预测

## Related Skills
- `nonequilibrium-brain-dynamics` - 非平衡脑动力学
- `fcn-llm-graph-tuning` - LLM脑功能连接图调优
- `multimodal-brain-connectivity-gnn` - 多模态脑连接GNN