---
name: atlas-free-brain-network-transformer
description: 无图谱脑网络Transformer方法论。直接从个体fMRI数据导出个性化脑分区，避免图谱偏差。触发词：脑网络、脑图谱、个体化分区、fMRI分析、脑网络Transformer、BrainGNN、Graphormer、无图谱分析、atlas-free、brain parcellation、BNT。
user-invocable: true
---

# Atlas-free Brain Network Transformer

无需预定义图谱的脑网络Transformer，直接从个体静息态fMRI数据导出个性化脑分区，避免图谱偏差问题。

## 核心方法论

### 1. 个体化脑分区

```python
import numpy as np
from sklearn.cluster import KMeans, SpectralClustering
from sklearn.metrics.pairwise import cosine_similarity
from scipy.ndimage import gaussian_filter
import nibabel as nib

class IndividualizedParcellation:
    """个体化脑分区
    
    直接从个体fMRI数据生成个性化脑分区
    """
    
    def __init__(self, n_regions: int = 200, method: str = 'spectral'):
        self.n_regions = n_regions
        self.method = method
        
    def compute_voxel_connectivity(self, fmri_data: np.ndarray, mask: np.ndarray):
        """计算体素级功能连接
        
        Args:
            fmri_data: 4D fMRI数据 (x, y, z, time)
            mask: 脑掩模 (x, y, z)
            
        Returns:
            体素功能连接矩阵
        """
        # 提取脑内体素
        brain_voxels = fmri_data[mask > 0]  # (n_voxels, time)
        
        # 计算功能连接（皮尔逊相关）
        # 为避免内存溢出，使用分块计算
        n_voxels = brain_voxels.shape[0]
        chunk_size = 5000
        connectivity = np.zeros((n_voxels, n_voxels))
        
        for i in range(0, n_voxels, chunk_size):
            for j in range(0, n_voxels, chunk_size):
                i_end = min(i + chunk_size, n_voxels)
                j_end = min(j + chunk_size, n_voxels)
                chunk_i = brain_voxels[i:i_end]
                chunk_j = brain_voxels[j:j_end]
                connectivity[i:i_end, j:j_end] = np.corrcoef(chunk_i, chunk_j)[:i_end-i, i_end-i_end:]
        
        return connectivity
    
    def generate_parcellation(self, fmri_data: np.ndarray, mask: np.ndarray):
        """生成个体化脑分区
        
        Returns:
            分区图（与输入数据同维度）
        """
        # 计算体素功能连接
        connectivity = self.compute_voxel_connectivity(fmri_data, mask)
        
        # 聚类
        if self.method == 'kmeans':
            # 基于连接模式的K-means聚类
            clusterer = KMeans(n_clusters=self.n_regions, random_state=42, n_init=10)
            labels = clusterer.fit_predict(connectivity)
        else:
            # 谱聚类（基于相似性矩阵）
            similarity = cosine_similarity(connectivity)
            clusterer = SpectralClustering(
                n_clusters=self.n_regions,
                affinity='precomputed',
                random_state=42
            )
            labels = clusterer.fit_predict(similarity)
        
        # 将标签映射回3D空间
        parcellation = np.zeros(mask.shape, dtype=int)
        parcellation[mask > 0] = labels + 1  # 0保留为背景
        
        return parcellation, labels
    
    def compute_roi_features(self, fmri_data: np.ndarray, parcellation: np.ndarray):
        """计算ROI特征
        
        将体素级特征聚合为ROI级特征
        """
        n_timepoints = fmri_data.shape[3]
        n_regions = parcellation.max()
        roi_signals = np.zeros((n_regions, n_timepoints))
        
        for roi in range(1, n_regions + 1):
            mask_roi = parcellation == roi
            if mask_roi.sum() > 0:
                # 平均时间序列
                roi_signals[roi - 1] = fmri_data[mask_roi].mean(axis=0)
        
        return roi_signals


class VoxelFeatureSpace:
    """标准化体素特征空间
    
    将个体脑映射到标准化特征空间以实现跨个体比较
    """
    
    def __init__(self, n_features: int = 100):
        self.n_features = n_features
        self.reference_space = None
        
    def fit_reference_space(self, fmri_dataset: list):
        """从多受试者数据构建参考特征空间
        
        Args:
            fmri_dataset: fMRI数据列表，每个元素为 (x, y, z, time)
        """
        # 收集所有体素特征
        all_features = []
        for fmri in fmri_dataset:
            # 提取功能连接特征
            features = self._extract_voxel_features(fmri)
            all_features.append(features)
        
        # 合并并降维
        all_features = np.vstack(all_features)
        
        # 使用PCA构建参考空间
        from sklearn.decomposition import PCA
        self.pca = PCA(n_components=self.n_features)
        self.pca.fit(all_features)
        
    def _extract_voxel_features(self, fmri_data: np.ndarray):
        """提取体素级特征"""
        # 局部功能连接密度
        n_x, n_y, n_z, n_t = fmri_data.shape
        
        features = []
        for x in range(1, n_x - 1, 2):
            for y in range(1, n_y - 1, 2):
                for z in range(1, n_z - 1, 2):
                    voxel_ts = fmri_data[x, y, z, :]
                    # 周邻体素连接
                    neighbors = fmri_data[x-1:x+2, y-1:y+2, z-1:z+2, :].reshape(-1, n_t)
                    corr = np.corrcoef([voxel_ts], neighbors)[0, 1:]
                    features.append(corr)
        
        return np.array(features)
    
    def transform(self, fmri_data: np.ndarray):
        """将个体数据映射到参考空间"""
        features = self._extract_voxel_features(fmri_data)
        return self.pca.transform(features)
```

### 2. ROI到体素连接特征

```python
class ROIToVoxelFeatures:
    """ROI到体素连接特征
    
    在标准化体素特征空间中计算ROI-体素连接性
    """
    
    def __init__(self, parcellation_method='individualized'):
        self.parcellation_method = parcellation_method
        self.parcellator = IndividualizedParcellation()
        
    def compute_features(self, fmri_data: np.ndarray, mask: np.ndarray):
        """计算ROI-体素连接特征
        
        Returns:
            features: shape (n_rois, n_features)
            用于Transformer处理的特征矩阵
        """
        # 生成个体化分区
        parcellation, _ = self.parcellator.generate_parcellation(fmri_data, mask)
        
        # 计算ROI时间序列
        roi_signals = self.parcellator.compute_roi_features(fmri_data, parcellation)
        
        # 计算ROI功能连接
        roi_connectivity = np.corrcoef(roi_signals)
        
        # 图论特征
        graph_features = self._compute_graph_features(roi_connectivity)
        
        return roi_connectivity, graph_features
    
    def _compute_graph_features(self, connectivity: np.ndarray):
        """计算图论特征"""
        import networkx as nx
        
        # 构建图
        G = nx.from_numpy_array(np.abs(connectivity))
        
        features = {
            'degree_centrality': list(nx.degree_centrality(G).values()),
            'betweenness_centrality': list(nx.betweenness_centrality(G).values()),
            'clustering_coefficient': list(nx.clustering(G).values()),
            'local_efficiency': nx.local_efficiency(G)
        }
        
        return features
```

### 3. Brain Network Transformer

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class BrainNetworkTransformer(nn.Module):
    """脑网络Transformer
    
    处理ROI特征并生成受试者级嵌入
    """
    
    def __init__(
        self,
        n_rois: int = 200,
        d_model: int = 128,
        n_heads: int = 8,
        n_layers: int = 6,
        d_ff: int = 512,
        dropout: float = 0.1
    ):
        super().__init__()
        
        # ROI特征嵌入
        self.roi_embedding = nn.Sequential(
            nn.Linear(n_rois, d_model),
            nn.LayerNorm(d_model),
            nn.ReLU(),
            nn.Dropout(dropout)
        )
        
        # 位置编码（基于图结构）
        self.positional_encoding = GraphPositionalEncoding(d_model)
        
        # Transformer编码器
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=n_heads,
            dim_feedforward=d_ff,
            dropout=dropout,
            batch_first=True
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=n_layers)
        
        # 受试者级嵌入
        self.subject_embedding = nn.Sequential(
            nn.Linear(d_model, d_model),
            nn.LayerNorm(d_model),
            nn.ReLU(),
            nn.Linear(d_model, d_model)
        )
        
    def forward(self, roi_features: torch.Tensor, adj_matrix: torch.Tensor = None):
        """前向传播
        
        Args:
            roi_features: (batch, n_rois, n_features) ROI特征
            adj_matrix: (batch, n_rois, n_rois) 邻接矩阵（可选）
            
        Returns:
            subject_embedding: (batch, d_model) 受试者嵌入
        """
        batch_size, n_rois, _ = roi_features.shape
        
        # ROI嵌入
        x = self.roi_embedding(roi_features)  # (batch, n_rois, d_model)
        
        # 添加位置编码
        if adj_matrix is not None:
            pos_enc = self.positional_encoding(adj_matrix)  # (batch, n_rois, d_model)
            x = x + pos_enc
        
        # Transformer处理
        x = self.transformer(x)  # (batch, n_rois, d_model)
        
        # 全局池化得到受试者嵌入
        x = x.mean(dim=1)  # (batch, d_model)
        subject_emb = self.subject_embedding(x)
        
        return subject_emb


class GraphPositionalEncoding(nn.Module):
    """基于图结构的位置编码"""
    
    def __init__(self, d_model: int):
        super().__init__()
        self.d_model = d_model
        
        # 拉普拉斯特征映射
        self.linear = nn.Linear(d_model, d_model)
        
    def forward(self, adj_matrix: torch.Tensor):
        """计算位置编码
        
        Args:
            adj_matrix: (batch, n_rois, n_rois) 邻接矩阵
        """
        batch_size, n_rois, _ = adj_matrix.shape
        
        # 计算拉普拉斯矩阵
        degree = adj_matrix.sum(dim=-1)
        degree_inv_sqrt = torch.pow(degree, -0.5)
        degree_inv_sqrt[torch.isinf(degree_inv_sqrt)] = 0.0
        
        # 归一化拉普拉斯
        identity = torch.eye(n_rois, device=adj_matrix.device).unsqueeze(0)
        L = identity - degree_inv_sqrt.unsqueeze(-1) * adj_matrix * degree_inv_sqrt.unsqueeze(-2)
        
        # 特征分解
        eigenvalues, eigenvectors = torch.linalg.eigh(L)
        
        # 取前d_model个特征向量
        pos_enc = eigenvectors[:, :, :self.d_model]
        
        return self.linear(pos_enc)
```

### 4. 训练与推理

```python
class AtlasFreeBNTTrainer:
    """无图谱BNT训练器"""
    
    def __init__(self, model: BrainNetworkTransformer, lr: float = 1e-4):
        self.model = model
        self.optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
        self.criterion = nn.CrossEntropyLoss()
        
    def train_epoch(self, dataloader, epoch: int):
        """训练一个epoch"""
        self.model.train()
        total_loss = 0
        
        for batch_idx, (roi_features, labels, adj_matrices) in enumerate(dataloader):
            self.optimizer.zero_grad()
            
            # 前向传播
            embeddings = self.model(roi_features, adj_matrices)
            
            # 分类损失
            loss = self.criterion(embeddings, labels)
            
            # 反向传播
            loss.backward()
            self.optimizer.step()
            
            total_loss += loss.item()
        
        return total_loss / len(dataloader)
    
    def evaluate(self, dataloader):
        """评估模型"""
        self.model.eval()
        correct = 0
        total = 0
        
        with torch.no_grad():
            for roi_features, labels, adj_matrices in dataloader:
                embeddings = self.model(roi_features, adj_matrices)
                predictions = embeddings.argmax(dim=1)
                correct += (predictions == labels).sum().item()
                total += labels.size(0)
        
        return correct / total


class AtlasFreeBNTInference:
    """推理管道"""
    
    def __init__(self, model_path: str):
        self.parcellator = IndividualizedParcellation()
        self.model = torch.load(model_path)
        self.model.eval()
        
    def predict(self, fmri_data: np.ndarray, mask: np.ndarray):
        """对新受试者进行预测"""
        # 个体化分区
        parcellation, _ = self.parcellator.generate_parcellation(fmri_data, mask)
        
        # 提取ROI特征
        roi_signals = self.parcellator.compute_roi_features(fmri_data, parcellation)
        roi_connectivity = np.corrcoef(roi_signals)
        
        # 转换为张量
        features = torch.tensor(roi_connectivity, dtype=torch.float32).unsqueeze(0)
        adj = torch.tensor(np.abs(roi_connectivity) > 0.3, dtype=torch.float32).unsqueeze(0)
        
        # 推理
        with torch.no_grad():
            embedding = self.model(features, adj)
        
        return embedding.numpy()
```

## 应用场景

### 1. 性别分类
- 基于脑网络模式的性别预测
- 无需固定图谱约束

### 2. 脑龄预测
- 预测受试者的大脑年龄
- 个体化精度更高

### 3. 临床诊断
- 阿尔茨海默病早期检测
- 精神疾病分类
- 神经发育障碍识别

## 使用示例

```python
# 初始化模型
model = BrainNetworkTransformer(
    n_rois=200,
    d_model=128,
    n_heads=8,
    n_layers=6
)

# 模拟数据
batch_size = 16
n_rois = 200
roi_features = torch.randn(batch_size, n_rois, n_rois)
adj_matrix = torch.rand(batch_size, n_rois, n_rois)
adj_matrix = (adj_matrix + adj_matrix.transpose(1, 2)) / 2  # 对称化
adj_matrix = (adj_matrix > 0.5).float()

# 前向传播
embeddings = model(roi_features, adj_matrix)
print(f"受试者嵌入维度: {embeddings.shape}")  # (batch, 128)

# 训练
trainer = AtlasFreeBNTTrainer(model)
# trainer.train_epoch(dataloader, epoch=1)
```

## Activation Keywords
- 脑网络
- 脑图谱
- 个体化分区
- fMRI分析
- 脑网络Transformer
- BrainGNN
- Graphormer
- 无图谱分析
- atlas-free
- brain parcellation
- BNT

## Tools Used
- Python
- PyTorch
- NumPy
- SciPy
- scikit-learn
- NetworkX
- NiBabel

## Instructions for Agents
1. 确认任务是否为脑网络分析或fMRI数据处理
2. 从个体fMRI数据计算体素功能连接
3. 使用谱聚类或K-means生成个体化脑分区
4. 提取ROI特征并计算功能连接矩阵
5. 构建Brain Network Transformer模型
6. 进行分类或回归任务（性别、年龄、疾病诊断）

## Examples
```python
# 初始化个体化分区器
parcellator = IndividualizedParcellation(n_regions=200, method='spectral')

# 从fMRI数据生成分区（需要脑掩模）
# parcellation, labels = parcellator.generate_parcellation(fmri_data, mask)

# 初始化BNT模型
model = BrainNetworkTransformer(
    n_rois=200,
    d_model=128,
    n_heads=8,
    n_layers=6
)

# 前向传播
roi_features = torch.randn(16, 200, 200)  # batch, n_rois, n_features
adj_matrix = (torch.rand(16, 200, 200) > 0.5).float()
embeddings = model(roi_features, adj_matrix)
print(f"受试者嵌入维度: {embeddings.shape}")
```

## 参考文献

- arXiv:2510.03306 - Atlas-free Brain Network Transformer
- GitHub: https://github.com/shuai-huang/atlas_free_bnt