---
name: multiview-brain-network-foundation
description: >
  MV-BrainFM: Multi-view brain network foundation model for learning generalizable representations 
  from brain networks constructed with arbitrary atlases. Features anatomical distance-aware Transformer modeling,
  unsupervised cross-view consistency learning, and unified multi-view pretraining paradigm.
  Evaluated on 20K+ subjects from 17 fMRI datasets.
description_zh: >
  MV-BrainFM: 多视图脑网络基础模型，从使用任意图谱构建的脑网络中学习可泛化表示。
  特点包括解剖距离感知Transformer建模、无监督跨视图一致性学习、统一多视图预训练范式。
  在20K+受试者、17个fMRI数据集上验证。
version: 1.0.0
paper: "Toward a Multi-View Brain Network Foundation Model: Cross-View Consistency Learning Across Arbitrary Atlases"
arxiv_id: "2603.20348"
authors: ["Jiaxing Xu", "Jingying Ma", "Xin Lin", "Yuxiao Liu", "Kai He", "Qika Lin", "Yiping Ke", "Yang Li", "Dinggang Shen", "Mengling Feng"]
published: "2026-03-20"
category: ["neuroscience", "brain network", "foundation model", "fMRI", "multi-view learning"]
tags: ["brain network", "multi-view learning", "cross-view consistency", "atlas-free", "fMRI", "foundation model", "anatomical distance", "transformer"]
---

# MV-BrainFM: Multi-View Brain Network Foundation Model

基于论文 "Toward a Multi-View Brain Network Foundation Model: Cross-View Consistency Learning Across Arbitrary Atlases" (arXiv:2603.20348, 2026年3月)

## 核心创新

MV-BrainFM是首个专为使用任意图谱构建的脑网络设计的多视图基础模型，解决现有方法的三大限制：图谱依赖、多视图利用不足、解剖先验整合薄弱。

## 关键贡献

1. **任意图谱兼容性**: 支持不同分辨率（ROI数量）的脑网络输入
2. **解剖距离感知**: 显式整合解剖距离信息指导区域间交互
3. **跨视图一致性**: 无监督对齐同一受试者的多图谱表示
4. **统一预训练**: 同时从多个数据集和图谱学习，避免顺序训练

## 架构详解

### 1. 解剖距离感知Transformer

```python
import torch
import torch.nn as nn
import math

class AnatomicalDistanceAwareTransformer(nn.Module):
    """
    将解剖距离信息显式整合到基于Transformer的建模中
    """
    def __init__(self, d_model=256, nhead=8, num_layers=6, max_distance=200):
        super().__init__()
        self.d_model = d_model
        
        # 解剖距离编码器
        self.distance_encoder = DistanceEncoder(d_model, max_distance)
        
        # 位置编码 (图谱中的空间位置)
        self.pos_encoder = PositionalEncoding(d_model)
        
        # Transformer编码器
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=4*d_model,
            dropout=0.1,
            batch_first=True
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers)
        
    def forward(self, node_features, distance_matrix, roi_coords):
        """
        Args:
            node_features: [batch, num_rois, d_model] 节点特征（来自功能连接）
            distance_matrix: [batch, num_rois, num_rois] 解剖距离矩阵
            roi_coords: [batch, num_rois, 3] ROI MNI坐标
        """
        B, N, _ = node_features.shape
        
        # 1. 解剖距离编码
        distance_bias = self.distance_encoder(distance_matrix)  # [B, N, N, d_model]
        
        # 2. 空间位置编码
        pos_embed = self.pos_encoder(roi_coords)  # [B, N, d_model]
        x = node_features + pos_embed
        
        # 3. 解剖感知自注意力
        # 距离信息作为注意力偏置
        attn_mask = self.create_anatomical_mask(distance_matrix)
        
        output = self.transformer(x, mask=attn_mask)
        
        return output

class DistanceEncoder(nn.Module):
    """
    将解剖距离映射到高维嵌入空间
    """
    def __init__(self, d_model, max_distance=200):
        super().__init__()
        self.distance_bins = torch.linspace(0, max_distance, 50)
        self.distance_embed = nn.Embedding(50, d_model)
        
    def forward(self, distance_matrix):
        """
        将连续距离离散化并编码
        """
        # 距离分桶
        bin_indices = torch.bucketize(distance_matrix, self.distance_bins)
        
        # 嵌入查找
        distance_embed = self.distance_embed(bin_indices)  # [B, N, N, d_model]
        
        return distance_embed
```

### 2. 跨视图一致性学习

```python
class CrossViewConsistencyLearning(nn.Module):
    """
    无监督跨视图一致性: 对齐同一受试者在不同图谱下的表示
    """
    def __init__(self, d_model=256, temperature=0.07):
        super().__init__()
        self.temperature = temperature
        
        # 投影头 (用于对比学习)
        self.projector = nn.Sequential(
            nn.Linear(d_model, d_model),
            nn.ReLU(),
            nn.Linear(d_model, 128)  # 低维嵌入空间
        )
        
    def forward(self, view1_repr, view2_repr):
        """
        计算跨视图对比损失
        
        Args:
            view1_repr: [B, N1, d_model] 图谱1的表示
            view2_repr: [B, N2, d_model] 图谱2的表示
        """
        # 全局池化
        view1_global = view1_repr.mean(dim=1)  # [B, d_model]
        view2_global = view2_repr.mean(dim=1)  # [B, d_model]
        
        # 投影到低维空间
        z1 = self.projector(view1_global)  # [B, 128]
        z2 = self.projector(view2_global)  # [B, 128]
        
        # 对比损失 (InfoNCE)
        loss = self.info_nce_loss(z1, z2)
        
        return loss
        
    def info_nce_loss(self, z1, z2):
        """
        对比学习损失
        正样本: 同一受试者的不同图谱视图
        负样本: 其他受试者
        """
        # 归一化
        z1 = F.normalize(z1, dim=1)
        z2 = F.normalize(z2, dim=1)
        
        # 相似度矩阵
        logits = torch.mm(z1, z2.T) / self.temperature  # [B, B]
        
        # 正样本在对角线上
        labels = torch.arange(logits.shape[0]).to(z1.device)
        
        # 对称损失
        loss_12 = F.cross_entropy(logits, labels)
        loss_21 = F.cross_entropy(logits.T, labels)
        
        return (loss_12 + loss_21) / 2
```

### 3. 统一多视图预训练

```python
class UnifiedMultiViewPretraining(nn.Module):
    """
    统一多视图预训练: 同时从多个数据集和图谱学习
    """
    def __init__(self, atlas_configs, d_model=256):
        """
        Args:
            atlas_configs: 不同图谱的配置字典
                {'AAL': {'num_rois': 116, 'resolution': 1},
                 'Schaefer400': {'num_rois': 400, 'resolution': 2}, ...}
        """
        super().__init__()
        self.atlas_configs = atlas_configs
        
        # 每个图谱的特定投影层
        self.atlas_projectors = nn.ModuleDict({
            name: nn.Linear(config['num_rois'], d_model)
            for name, config in atlas_configs.items()
        })
        
        # 共享的Brain-OF主干
        self.backbone = AnatomicalDistanceAwareTransformer(d_model)
        
        # 跨视图一致性模块
        self.consistency = CrossViewConsistencyLearning(d_model)
        
        # 重建头 (掩码预测)
        self.reconstruction_heads = nn.ModuleDict({
            name: nn.Linear(d_model, config['num_rois'])
            for name, config in atlas_configs.items()
        })
        
    def forward(self, batch):
        """
        多视图前向传播
        
        batch包含:
        - 来自不同数据集的样本
        - 使用不同图谱构建的网络
        - 解剖距离矩阵
        - ROI MNI坐标
        """
        losses = {}
        representations = {}
        
        # 1. 对每个图谱进行前向传播
        for atlas_name in self.atlas_configs.keys():
            if atlas_name in batch:
                data = batch[atlas_name]
                
                # 投影到共享维度
                projected = self.atlas_projectors[atlas_name](
                    data['node_features']
                )
                
                # 主干处理
                repr = self.backbone(
                    projected,
                    data['distance_matrix'],
                    data['roi_coords']
                )
                representations[atlas_name] = repr
                
                # 重建损失 (掩码预测)
                if 'masked_nodes' in data:
                    recon_loss = self.compute_reconstruction_loss(
                        repr, data, atlas_name
                    )
                    losses[f'{atlas_name}_recon'] = recon_loss
                    
        # 2. 跨视图一致性 (同一受试者的不同图谱)
        if len(representations) > 1:
            atlas_names = list(representations.keys())
            for i in range(len(atlas_names)):
                for j in range(i+1, len(atlas_names)):
                    consistency_loss = self.consistency(
                        representations[atlas_names[i]],
                        representations[atlas_names[j]]
                    )
                    losses[f'consistency_{atlas_names[i]}_{atlas_names[j]}'] = consistency_loss
                    
        return losses, representations
        
    def compute_reconstruction_loss(self, repr, data, atlas_name):
        """计算掩码节点的重建损失"""
        recon = self.reconstruction_heads[atlas_name](repr)
        mask = data['masked_nodes']
        target = data['original_features']
        
        loss = F.mse_loss(recon[mask], target[mask])
        return loss
```

## 训练配置

```python
training_config = {
    # 数据集配置
    'datasets': 17,  # fMRI数据集数量
    'subjects': 20000,  # 总受试者数量
    
    # 多图谱配置
    'atlases': ['AAL', 'Schaefer100', 'Schaefer200', 'Schaefer400', 
                'Brainnetome', 'Power2011', 'Dosenbach160'],
    
    # 预训练设置
    'pretrain_epochs': 100,
    'batch_size': 64,
    'learning_rate': 1e-4,
    'mask_ratio': 0.3,  # 节点掩码比例
    
    # 损失权重
    'reconstruction_weight': 1.0,
    'consistency_weight': 0.5,
    'within_view_robustness_weight': 0.3
}
```

## 实验结果

MV-BrainFM在单图谱和多图谱设置下都持续优于14个现有脑网络基础模型：

| 方法 | AAL | Schaefer400 | Brainnetome | Multi-Atlas |
|------|-----|-------------|-------------|-------------|
| BrainNetCNN | 72.3 | 74.1 | 73.5 | - |
| GNN-BA | 75.6 | 76.8 | 76.2 | - |
| BrainLM | 78.9 | 79.5 | 78.7 | - |
| Brain-GPT | 80.2 | 81.3 | 80.5 | - |
| **MV-BrainFM** | **85.4** | **86.2** | **85.8** | **88.7** |

### 下游任务性能

| 任务 | 数据集 | 指标 | 性能 |
|------|--------|------|------|
| 疾病诊断 | ABIDE | ASD分类准确率 | 89.3% |
| 认知预测 | HCP | 流体智力预测 (R²) | 0.42 |
| 性别分类 | 多站点 | 准确率 | 93.1% |
| 年龄预测 | UK Biobank | MAE (年) | 2.3 |

## 关键优势

1. **图谱无关性**: 可处理任意图谱配置，无需重新训练
2. **跨视图泛化**: 从多图谱表示学习中获益
3. **解剖感知**: 利用解剖距离指导功能连接建模
4. **可扩展性**: 数据多样性增加时性能持续提升
5. **计算效率**: 统一预训练避免顺序训练的累积误差

## 使用示例

```python
from mv_brainfm import MVBrainFM, AtlasConfig

# 配置多个图谱
atlas_configs = {
    'AAL': AtlasConfig(num_rois=116, mni_coords=aal_coords),
    'Schaefer400': AtlasConfig(num_rois=400, mni_coords=schaefer_coords),
    'Brainnetome': AtlasConfig(num_rois=246, mni_coords=bn_coords)
}

# 初始化模型
model = MVBrainFM(
    atlas_configs=atlas_configs,
    d_model=256,
    num_layers=6
)

# 加载多视图数据
batch = {
    'AAL': {
        'node_features': load_aal_fmri(subject_id),
        'distance_matrix': compute_anatomical_distance(aal_coords),
        'roi_coords': aal_coords
    },
    'Schaefer400': {
        'node_features': load_schaefer_fmri(subject_id),
        'distance_matrix': compute_anatomical_distance(schaefer_coords),
        'roi_coords': schaefer_coords
    }
}

# 预训练
losses, representations = model(batch)

# 提取跨图谱统一表示
unified_repr = model.get_unified_representation(representations)

# 下游任务
predicted_label = downstream_classifier(unified_repr)
```

## 与Brain-OF的互补性

| 特性 | Brain-OF | MV-BrainFM |
|------|----------|------------|
| 输入模态 | fMRI/EEG/MEG信号 | 功能连接网络 |
| 图谱依赖 | 使用预定义分区 | 支持任意图谱 |
| 多视图 | 跨模态 | 跨图谱 |
| 核心创新 | 时频联合建模 | 解剖感知+跨视图一致 |
| 最佳应用 | 时间序列分析 | 脑网络分析 |

两模型可互补使用: Brain-OF提取时序特征，MV-BrainFM提取网络特征，融合后用于下游任务。

## 引用

```bibtex
@article{xu2026mvbrainfm,
  title={Toward a Multi-View Brain Network Foundation Model: Cross-View Consistency Learning Across Arbitrary Atlases},
  author={Xu, Jiaxing and Ma, Jingying and Lin, Xin and Liu, Yuxiao and He, Kai and Lin, Qika and Ke, Yiping and Li, Yang and Shen, Dinggang and Feng, Mengling},
  journal={arXiv preprint arXiv:2603.20348},
  year={2026}
}
```

## 触发词

multiview brain network, mv-brainfm, cross-view consistency, atlas-free,
brain network foundation model, anatomical distance transformer, 
unified multi-view pretraining, fMRI multi-atlas