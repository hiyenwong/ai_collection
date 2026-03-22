---
name: multimodal-brain-connectivity-gnn
description: 多模态脑连接分析框架，整合fMRI、DTI和sMRI数据。使用可解释图神经网络，通过掩码策略差异加权神经连接，实现跨模态数据融合。支持认知功能预测和解剖特征发现。触发词：多模态融合、脑连接、fMRI、DTI、sMRI、图神经网络、功能连接、结构连接、multimodal fusion、brain connectivity、functional connectivity、structural connectivity。
---

# Multimodal Brain Connectivity Analysis with Interpretable GNN

## 核心方法论

整合三种神经影像模态的可解释图神经网络框架：

### 1. 多模态数据整合
- **fMRI（功能磁共振）**：功能连接矩阵（FC）
- **DTI（扩散张量成像）**：结构连接矩阵（SC）
- **sMRI（结构磁共振）**：解剖特征（皮层厚度、表面积等）

### 2. 基于Atlas的配准
- **Glasser Atlas**：360个皮层区域
- 一致的区域划分确保跨模态对齐
- 区域级特征提取

### 3. 掩码策略
- **连接级掩码**：差异加权神经连接
- **可解释性**：揭示关键连接和特征
- **多尺度融合**：整合全局和局部特征

## 实现代码示例

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv, global_mean_pool, GATConv
from torch_geometric.data import Data, Batch
import numpy as np

class MultimodalBrainGNN(nn.Module):
    """
    多模态脑连接图神经网络
    
    整合 fMRI, DTI, sMRI 数据进行认知功能预测
    """
    
    def __init__(self, num_regions=360, hidden_dim=128, 
                 fmri_feat_dim=10, dti_feat_dim=5, smri_feat_dim=20,
                 output_dim=10, num_gnn_layers=3, num_heads=4):
        super().__init__()
        self.num_regions = num_regions
        self.hidden_dim = hidden_dim
        
        # 模态特定编码器
        self.fmri_encoder = nn.Sequential(
            nn.Linear(fmri_feat_dim, hidden_dim),
            nn.ELU(),
            nn.BatchNorm1d(hidden_dim),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        self.dti_encoder = nn.Sequential(
            nn.Linear(dti_feat_dim, hidden_dim),
            nn.ELU(),
            nn.BatchNorm1d(hidden_dim),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        self.smri_encoder = nn.Sequential(
            nn.Linear(smri_feat_dim, hidden_dim),
            nn.ELU(),
            nn.BatchNorm1d(hidden_dim),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        # 连接掩码学习器
        self.edge_mask_fc = nn.Sequential(
            nn.Linear(1, 16),
            nn.ELU(),
            nn.Linear(16, 1),
            nn.Sigmoid()
        )
        
        self.edge_mask_sc = nn.Sequential(
            nn.Linear(1, 16),
            nn.ELU(),
            nn.Linear(16, 1),
            nn.Sigmoid()
        )
        
        # 多模态融合层
        self.fusion = nn.Sequential(
            nn.Linear(hidden_dim * 3, hidden_dim * 2),
            nn.ELU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim * 2, hidden_dim)
        )
        
        # 图注意力网络
        self.gat_layers = nn.ModuleList([
            GATConv(hidden_dim, hidden_dim // num_heads, heads=num_heads, 
                   concat=True, dropout=0.2)
            for _ in range(num_gnn_layers)
        ])
        
        # 预测头
        self.predictor = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ELU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim // 2, output_dim)
        )
        
        # 可解释性模块
        self.importance_fc = nn.Linear(hidden_dim, 1)
        self.importance_sc = nn.Linear(hidden_dim, 1)
        self.importance_smri = nn.Linear(hidden_dim, 1)
    
    def learn_edge_mask(self, adj, mask_network):
        """学习连接掩码"""
        edge_weights = adj[adj > 0].unsqueeze(-1)
        mask = mask_network(edge_weights)
        return mask.squeeze(-1)
    
    def forward(self, fmri_data, dti_data, smri_data, 
                fc_matrix, sc_matrix, return_importance=False):
        """
        Args:
            fmri_data: [batch, num_regions, fmri_feat_dim] fMRI区域特征
            dti_data: [batch, num_regions, dti_feat_dim] DTI区域特征
            smri_data: [batch, num_regions, smri_feat_dim] sMRI区域特征
            fc_matrix: [batch, num_regions, num_regions] 功能连接矩阵
            sc_matrix: [batch, num_regions, num_regions] 结构连接矩阵
        
        Returns:
            prediction: 认知功能预测
            importance: (可选) 模态和连接重要性
        """
        batch_size = fmri_data.shape[0]
        
        # 模态特定编码
        h_fmri = self.fmri_encoder(fmri_data)  # [batch, num_regions, hidden_dim]
        h_dti = self.dti_encoder(dti_data)
        h_smri = self.smri_encoder(smri_data)
        
        # 多模态融合
        h_fused = self.fusion(torch.cat([h_fmri, h_dti, h_smri], dim=-1))
        
        # 学习连接掩码
        fc_mask = self.learn_edge_mask(fc_matrix, self.edge_mask_fc)
        sc_mask = self.learn_edge_mask(sc_matrix, self.edge_mask_sc)
        
        # 融合功能性和结构性连接
        combined_adj = 0.5 * fc_matrix * fc_mask.unsqueeze(0) + \
                       0.5 * sc_matrix * sc_mask.unsqueeze(0)
        
        # 转换为edge_index格式
        edge_index = (combined_adj > 0.1).nonzero(as_tuple=False).t()
        edge_weight = combined_adj[edge_index[0], edge_index[1]]
        
        # 图注意力网络
        h = h_fused.view(-1, self.hidden_dim)  # [batch*num_regions, hidden_dim]
        
        for gat in self.gat_layers:
            h = F.elu(gat(h, edge_index, edge_weight))
            h = F.dropout(h, p=0.2, training=self.training)
        
        # 全局池化
        h_graph = h.view(batch_size, self.num_regions, -1).mean(dim=1)
        
        # 预测
        prediction = self.predictor(h_graph)
        
        if return_importance:
            # 计算模态重要性
            imp_fc = torch.sigmoid(self.importance_fc(h_fmri.mean(dim=1)))
            imp_sc = torch.sigmoid(self.importance_sc(h_dti.mean(dim=1)))
            imp_smri = torch.sigmoid(self.importance_smri(h_smri.mean(dim=1)))
            
            importance = {
                'fmri_importance': imp_fc,
                'dti_importance': imp_sc,
                'smri_importance': imp_smri,
                'fc_mask': fc_mask,
                'sc_mask': sc_mask
            }
            return prediction, importance
        
        return prediction


class GlasserAtlasParcellation:
    """Glasser Altas区域划分工具"""
    
    # Glasser Atlas的360个区域
    REGIONS = {
        'visual': list(range(1, 31)),      # 视觉皮层
        'somatomotor': list(range(31, 66)),  # 感觉运动皮层
        'dorsal_attention': list(range(66, 95)),  # 背侧注意网络
        'ventral_attention': list(range(95, 118)),  # 腹侧注意网络
        'limbic': list(range(118, 133)),   # 边缘系统
        'frontoparietal': list(range(133, 176)),  # 额顶网络
        'default_mode': list(range(176, 181)) + list(range(230, 281)),  # 默认模式网络
    }
    
    @classmethod
    def get_network_regions(cls, network_name):
        """获取特定功能网络的区域索引"""
        return cls.REGIONS.get(network_name, [])


def extract_multimodal_features(fmri_path, dti_path, smri_path):
    """
    从原始影像数据提取多模态特征
    
    Args:
        fmri_path: fMRI数据路径
        dti_path: DTI数据路径
        smri_path: sMRI数据路径
    
    Returns:
        dict: 包含各模态特征和连接矩阵
    """
    # 实际实现需要nibabel等库
    import nibabel as nib
    from nilearn.connectome import ConnectivityMeasure
    
    # 加载并配准到Glasser Atlas
    # fMRI: 提取时间序列，计算功能连接
    # DTI: 追踪纤维，计算结构连接
    # sMRI: 分割，提取形态学特征
    
    return {
        'fmri_features': None,  # [num_regions, fmri_feat_dim]
        'dti_features': None,   # [num_regions, dti_feat_dim]
        'smri_features': None,  # [num_regions, smri_feat_dim]
        'fc_matrix': None,      # [num_regions, num_regions]
        'sc_matrix': None       # [num_regions, num_regions]
    }


def train_multimodal_gnn():
    """训练示例"""
    # 参数
    num_regions = 360
    batch_size = 16
    
    # 创建模型
    model = MultimodalBrainGNN(
        num_regions=num_regions,
        hidden_dim=128,
        output_dim=10  # 例如：预测10项认知测试分数
    )
    
    # 模拟数据
    fmri_data = torch.randn(batch_size, num_regions, 10)
    dti_data = torch.randn(batch_size, num_regions, 5)
    smri_data = torch.randn(batch_size, num_regions, 20)
    fc_matrix = torch.rand(batch_size, num_regions, num_regions)
    fc_matrix = (fc_matrix + fc_matrix.transpose(1, 2)) / 2  # 对称化
    sc_matrix = torch.rand(batch_size, num_regions, num_regions)
    sc_matrix = (sc_matrix + sc_matrix.transpose(1, 2)) / 2
    
    labels = torch.randn(batch_size, 10)
    
    # 前向传播
    prediction, importance = model(
        fmri_data, dti_data, smri_data,
        fc_matrix, sc_matrix,
        return_importance=True
    )
    
    # 计算损失
    loss = F.mse_loss(prediction, labels)
    
    # 可解释性正则化
    sparsity_loss = 0.01 * (importance['fc_mask'].mean() + importance['sc_mask'].mean())
    total_loss = loss + sparsity_loss
    
    print(f"Prediction Loss: {loss.item():.4f}")
    print(f"Sparsity Loss: {sparsity_loss.item():.4f}")
    print(f"Total Loss: {total_loss.item():.4f}")
    
    # 打印模态重要性
    print(f"\nModality Importance:")
    print(f"fMRI: {importance['fmri_importance'].mean().item():.3f}")
    print(f"DTI: {importance['dti_importance'].mean().item():.3f}")
    print(f"sMRI: {importance['smri_importance'].mean().item():.3f}")
    
    return model


if __name__ == "__main__":
    model = train_multimodal_gnn()
```

## 应用场景

1. **认知功能预测**
   - 青少年认知发展追踪
   - 神经精神疾病诊断
   - 个体差异建模

2. **生物标志物发现**
   - 识别关键解剖特征
   - 发现重要神经连接
   - 理解脑结构与功能关系

3. **临床应用**
   - 阿尔茨海默病早期检测
   - 精神分裂症分型
   - 治疗效果预测

## 数据来源

- Human Connectome Project Development Study
- 需要Glasser Altas配准
- 支持3T和7T MRI数据

## 参考文献

- arXiv:2408.14254 - Integrated Brain Connectivity Analysis with fMRI, DTI, and sMRI