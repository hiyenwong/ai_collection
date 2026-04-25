---
name: irene-eeg-seizure-detection
version: v1.0.0
last_updated: 2026-04-18
description: "Information Bottleneck-guided EEG Seizure Detection (IRENE). Jointly learns denoised dynamic graph structures and informative spatial-temporal representations for EEG seizure detection. Addresses noisy EEG graphs, redundant connections, and inter-patient variability using IB principle and self-supervised Graph Masked AutoEncoder. Accepted at IEEE ICHI 2026."
category: neuroscience
tags:
  - eeg
  - seizure-detection
  - information-bottleneck
  - dynamic-graph
  - self-supervised-learning
  - graph-masked-autoencoder
  - spatiotemporal-representation
paper:
  title: "Optimizing EEG Graph Structure for Seizure Detection: An Information Bottleneck and Self-Supervised Learning Approach"
  authors: "Lincan Li, Rikuto Kotoge, Xihao Piao, Zheng Chen, Yushun Dong"
  arxiv: "2604.01595v1"
  published: "2026-04-02"
  url: "https://arxiv.org/abs/2604.01595"
  accepted: "IEEE ICHI 2026"
activation: "eeg seizure detection, information bottleneck EEG, dynamic graph EEG, IRENE, graph masked autoencoder EEG, seizure propagation, inter-patient variability EEG"
---

# IRENE: Information Bottleneck-guided EEG Seizure Detection

## 概述

IRENE (Information Bottleneck-guided EEG SeizuRE DetectioN via SElf-Supervised Learning) 是一种新的 EEG 癫痫检测框架，通过信息瓶颈 (IB) 原则联合学习去噪的动态图结构和信息丰富的时空表示。解决了 EEG 图结构中的噪声、冗余连接和患者间变异性问题。已被 IEEE ICHI 2026 接受。

## 来源论文

- **标题**: Optimizing EEG Graph Structure for Seizure Detection: An Information Bottleneck and Self-Supervised Learning Approach
- **作者**: Lincan Li, Rikuto Kotoge, Xihao Piao, Zheng Chen, Yushun Dong
- **arXiv**: 2604.01595v1
- **发表**: 2026-04-02
- **录用**: IEEE 14th International Conference on Healthcare Informatics (ICHI)
- **代码**: https://github.com/LabRAI/IRENE
- **PDF**: https://arxiv.org/pdf/2604.01595v1

## 核心问题

EEG 癫痫检测的三大挑战：
1. **噪声图结构**: 基于统计相关性或隐式学习的动态图包含冗余和任务无关连接
2. **癫痫传播解释**: 难以解释癫痫在大脑网络中的传播路径
3. **标签稀缺与患者间变异**: 标注数据有限且不同患者的 EEG 模式差异巨大

## 核心方法

### Information Bottleneck (IB) 原理

IB 原则：在压缩输入信息的同时，最大化对目标任务的预测能力。

```
min I(X; Z) - β·I(Z; Y)

其中:
- X: 原始 EEG 输入
- Z: 学到的表示
- Y: 癫痫标签
- β: 权衡参数
```

IRENE 将此应用于 EEG 图结构学习：学习紧凑、可靠的连接模式，同时保留癫痫检测所需的关键信息。

### 架构组件

```
EEG Signals
    ↓
┌─────────────────────────────────────┐
│  Dynamic Graph Constructor (IB)     │
│  - Accounts for EEG noise           │
│  - Produces compact connectivity    │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│  Graph Masked AutoEncoder (GMAE)    │
│  - Self-supervised pretraining       │
│  - Reconstructs masked EEG signals  │
│  - Structure-aware representations   │
└─────────────────────────────────────┘
    ↓
┌─────────────────────────────────────┐
│  Spatiotemporal Encoder              │
│  - Captures temporal dynamics        │
│  - Spatial propagation patterns      │
└─────────────────────────────────────┘
    ↓
Seizure Detection + Explanation
```

### 关键实现

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class IRENE(nn.Module):
    """Information Bottleneck-guided EEG Seizure Detection."""
    
    def __init__(self, n_channels, n_samples, hidden_dim=128, beta=0.1):
        super().__init__()
        self.n_channels = n_channels
        self.n_samples = n_samples
        self.beta = beta
        
        # IB-guided graph constructor
        self.graph_constructor = IBGraphConstructor(
            n_channels, hidden_dim, beta=beta
        )
        
        # Graph Masked AutoEncoder
        self.gmae = GraphMaskedAutoEncoder(
            n_channels, hidden_dim
        )
        
        # Spatiotemporal encoder
        self.st_encoder = SpatiotemporalEncoder(
            hidden_dim, n_classes=2
        )
    
    def forward(self, x, mask_ratio=0.3):
        """
        Forward pass with IB-guided graph learning and GMAE.
        
        Args:
            x: EEG signals (batch, n_channels, n_samples)
            mask_ratio: Fraction of channels to mask for GMAE
        """
        # Step 1: Learn IB-optimized dynamic graph
        adj, ib_loss = self.graph_constructor(x)
        
        # Step 2: Self-supervised GMAE pretraining
        x_masked, mask = self._mask_channels(x, mask_ratio)
        reconstructed = self.gmae(x_masked, adj)
        recon_loss = self._reconstruction_loss(reconstructed, x, mask)
        
        # Step 3: Spatiotemporal encoding for seizure detection
        features = self.gmae.encode(x, adj)
        seizure_pred = self.st_encoder(features, adj)
        
        return seizure_pred, ib_loss, recon_loss
    
    def _mask_channels(self, x, mask_ratio):
        """Randomly mask EEG channels for self-supervised learning."""
        batch_size, n_channels, n_samples = x.shape
        n_mask = int(n_channels * mask_ratio)
        
        # Random channel selection
        mask = torch.rand(batch_size, n_channels) < mask_ratio
        x_masked = x.clone()
        x_masked[mask] = 0  # Zero-masked channels
        
        return x_masked, mask


class IBGraphConstructor(nn.Module):
    """Information Bottleneck-guided dynamic graph constructor."""
    
    def __init__(self, n_channels, hidden_dim, beta=0.1):
        super().__init__()
        self.beta = beta
        
        # Learn node embeddings
        self.node_embed = nn.Sequential(
            nn.Linear(n_channels, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        # Graph attention for adjacency
        self.attn = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, 1)
        )
    
    def forward(self, x):
        """
        Construct IB-optimized adjacency matrix.
        
        Args:
            x: EEG signals (batch, n_channels, n_samples)
        """
        batch_size, n_channels, n_samples = x.shape
        
        # Extract node features (channel-wise statistics)
        node_features = self.node_embed(x.mean(dim=-1))  # (batch, n_channels, hidden)
        
        # Compute pairwise attention
        adj = torch.zeros(batch_size, n_channels, n_channels, device=x.device)
        for i in range(n_channels):
            for j in range(n_channels):
                pair = torch.cat([node_features[:, i], node_features[:, j]], dim=-1)
                adj[:, i, j] = self.attn(pair).squeeze(-1)
        
        # IB regularization: penalize overly dense graphs
        ib_loss = self.beta * torch.mean(adj ** 2)
        
        # Normalize adjacency
        adj = F.softmax(adj, dim=-1)
        
        return adj, ib_loss


class GraphMaskedAutoEncoder(nn.Module):
    """Self-supervised Graph Masked AutoEncoder for EEG."""
    
    def __init__(self, n_channels, hidden_dim):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(n_channels, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        self.decoder = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, n_channels)
        )
    
    def encode(self, x, adj):
        """Encode EEG signals with graph context."""
        # x: (batch, n_channels, n_samples)
        features = self.encoder(x.mean(dim=-1))  # (batch, n_channels, hidden)
        
        # Graph message passing
        features = torch.bmm(adj, features)  # (batch, n_channels, hidden)
        
        return features
    
    def decode(self, features, adj):
        """Reconstruct masked channels."""
        features = torch.bmm(adj, features)
        reconstructed = self.decoder(features)
        return reconstructed
    
    def forward(self, x_masked, adj):
        features = self.encode(x_masked, adj)
        reconstructed = self.decode(features, adj)
        return reconstructed
```

### 训练流程

```python
def train_irene(model, dataloader, n_epochs=100):
    """
    Train IRENE with joint supervised and self-supervised objectives.
    """
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    
    for epoch in range(n_epochs):
        for eeg_signals, seizure_labels in dataloader:
            # Forward pass
            preds, ib_loss, recon_loss = model(eeg_signals)
            
            # Supervised loss (seizure classification)
            cls_loss = F.cross_entropy(preds, seizure_labels)
            
            # Combined objective
            loss = cls_loss + ib_loss + 0.5 * recon_loss
            
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
```

## 应用场景

### 1. 癫痫检测
```python
# Detect seizures in real-time EEG
model = IRENE(n_channels=21, n_samples=256)
model.load_state_dict(torch.load('irene_checkpoint.pt'))
model.eval()

eeg_segment = load_eeg_segment()  # (1, 21, 256)
with torch.no_grad():
    pred, _, _ = model(eeg_segment)
    seizure_prob = F.softmax(pred, dim=1)[0, 1]
    is_seizure = seizure_prob > 0.5
```

### 2. 癫痫传播解释
```python
# Analyze seizure propagation patterns
adj, _ = model.graph_constructor(eeg_segment)

# Visualize learned connectivity
import networkx as nx
G = nx.from_numpy_array(adj[0].detach().cpu().numpy())
nx.draw(G, node_size=50)
```

### 3. 跨患者泛化
```python
# Self-supervised pretraining on unlabeled data from new patient
unlabeled_eeg = load_unlabeled_eeg()
for eeg_segment in unlabeled_eeg:
    _, ib_loss, recon_loss = model(eeg_segment, mask_ratio=0.3)
    loss = ib_loss + 0.5 * recon_loss
    loss.backward()
    optimizer.step()
```

## 关键创新

1. **IB 指导的图学习**: 显式考虑 EEG 噪声特性，产生紧凑可靠的连接模式
2. **GMAE 自监督**: 通过掩码重建学习结构感知表示，缓解标签稀缺
3. **可解释性**: 学到的图结构提供癫痫传播的临床洞见
4. **患者间鲁棒性**: IB 原则和自监督学习提升跨患者泛化

## 实现要点

- **IB β 参数**: 需要调优以平衡信息压缩和预测能力
- **掩码比例**: 通常 0.2-0.4 之间，过高会导致重建困难
- **通道数**: 根据 EEG 导联配置调整（常见 19-64 通道）
- **时间窗口**: 通常 1-4 秒的 EEG 片段（256-1024 样本 @ 256Hz）

## 局限性

- 图构造的计算复杂度为 O(n_channels²)
- IB 原则的 β 参数需要针对不同数据集调优
- 对极低质量 EEG（如大量伪迹）可能需要预处理

## 激活关键词

- eeg seizure detection, information bottleneck EEG, dynamic graph EEG, IRENE, graph masked autoencoder EEG, seizure propagation, inter-patient variability EEG
