---
name: brain-graph-augmentation-template
description: 基于群体模板的脑图数据增强方法，用于改进单样本学习分类。使用连接脑模板（CBT）和图生成对抗网络（gGAN）从单一群体模板生成增强数据，提升阿尔茨海默病等疾病分类性能。触发词：脑图增强、数据增强、单样本学习、连接脑模板、CBT、图GAN、Alzheimer分类、brain graph augmentation、one-shot learning、CBT、gGAN。
---

# Population Template-Based Brain Graph Augmentation

## 核心方法论

从单一群体模板生成增强数据，改进单样本学习分类：

### 1. 连接脑模板（CBT）
- **群体指纹**：从多个受试者图生成代表性模板
- **关键连接**：捕获群体的判别性生物标志物
- **模板融合**：加权平均或学习融合

### 2. 图生成对抗网络（gGAN）
- **生成器**：从潜在空间生成脑图
- **判别器**：区分真实图和生成图
- **条件生成**：基于类别标签生成

### 3. 增强策略
- **单模板增强**：从CBT生成多样化样本
- **类别条件**：保持类别标签一致性
- **图结构保持**：确保拓扑合理性

## 实现代码示例

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv, global_mean_pool
from torch_geometric.utils import dense_to_sparse
from torch_geometric.data import Data, DataLoader
import numpy as np
from typing import List, Tuple, Optional


class ConnectionalBrainTemplate:
    """
    连接脑模板（CBT）生成器
    
    从多个受试者的脑图生成代表性群体模板
    """
    
    def __init__(self, num_nodes, fusion_method='average'):
        self.num_nodes = num_nodes
        self.fusion_method = fusion_method
    
    def compute_cbt(self, graphs: List[torch.Tensor], labels: Optional[torch.Tensor] = None):
        """
        计算连接脑模板
        
        Args:
            graphs: List of adjacency matrices [num_subjects, num_nodes, num_nodes]
            labels: Optional class labels for class-specific CBT
        
        Returns:
            cbt: Connectional Brain Template [num_nodes, num_nodes]
        """
        if self.fusion_method == 'average':
            # 简单平均
            cbt = torch.stack(graphs).mean(dim=0)
        
        elif self.fusion_method == 'weighted':
            # 基于类别的加权
            if labels is not None:
                unique_labels = labels.unique()
                cbt = torch.zeros(self.num_nodes, self.num_nodes)
                for label in unique_labels:
                    mask = labels == label
                    class_graphs = [g for g, m in zip(graphs, mask) if m]
                    class_template = torch.stack(class_graphs).mean(dim=0)
                    cbt += class_template
                cbt /= len(unique_labels)
            else:
                cbt = torch.stack(graphs).mean(dim=0)
        
        elif self.fusion_method == 'learned':
            # 学习融合权重（需要训练）
            raise NotImplementedError("Learned fusion requires training")
        
        # 对称化
        cbt = (cbt + cbt.T) / 2
        
        # 归一化到[0, 1]
        cbt = (cbt - cbt.min()) / (cbt.max() - cbt.min() + 1e-8)
        
        return cbt
    
    def extract_biomarkers(self, cbt: torch.Tensor, threshold: float = 0.7):
        """
        从CBT提取判别性生物标志物连接
        
        Args:
            cbt: Connectional Brain Template
            threshold: 连接强度阈值
        
        Returns:
            biomarkers: 强连接的边列表
        """
        # 找到超过阈值的连接
        strong_edges = (cbt > threshold).nonzero(as_tuple=False)
        # 移除对角线和重复
        mask = strong_edges[:, 0] < strong_edges[:, 1]
        biomarkers = strong_edges[mask]
        
        return biomarkers


class GraphGenerator(nn.Module):
    """
    图生成器
    
    从潜在向量生成脑连接图
    """
    
    def __init__(self, latent_dim, num_nodes, hidden_dim=256):
        super().__init__()
        self.num_nodes = num_nodes
        self.latent_dim = latent_dim
        
        # 节点特征生成
        self.node_gen = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim, hidden_dim),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim, num_nodes * hidden_dim // 4)
        )
        
        # 边生成
        self.edge_gen = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim, hidden_dim),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim, num_nodes * (num_nodes - 1) // 2)
        )
        
        # 条件注入（类别标签）
        self.label_embed = nn.Embedding(2, latent_dim)
    
    def forward(self, z, labels=None):
        """
        Args:
            z: [batch, latent_dim] 潜在向量
            labels: [batch] 类别标签（可选）
        
        Returns:
            graphs: 生成的图 {x, edge_index, edge_attr}
        """
        batch_size = z.shape[0]
        
        # 条件注入
        if labels is not None:
            c = self.label_embed(labels)
            z = z * c  # 条件调制
        
        # 生成节点特征
        node_features = self.node_gen(z)
        node_features = node_features.view(batch_size, self.num_nodes, -1)
        
        # 生成边权重（上三角）
        edge_weights = self.edge_gen(z)
        edge_weights = torch.sigmoid(edge_weights)  # [0, 1]
        
        # 构建邻接矩阵
        adj = torch.zeros(batch_size, self.num_nodes, self.num_nodes)
        triu_indices = torch.triu_indices(self.num_nodes, self.num_nodes, offset=1)
        
        for b in range(batch_size):
            adj[b, triu_indices[0], triu_indices[1]] = edge_weights[b]
            adj[b] = adj[b] + adj[b].T  # 对称化
        
        # 转换为PyG格式
        graphs = []
        for b in range(batch_size):
            edge_index = (adj[b] > 0.1).nonzero(as_tuple=False).t()
            graphs.append(Data(
                x=node_features[b],
                edge_index=edge_index,
                edge_attr=adj[b][adj[b] > 0.1].unsqueeze(-1)
            ))
        
        return graphs


class GraphDiscriminator(nn.Module):
    """
    图判别器
    
    区分真实图和生成图
    """
    
    def __init__(self, num_nodes, hidden_dim=256, num_classes=2):
        super().__init__()
        
        # 图编码器
        self.conv1 = GCNConv(hidden_dim // 4, hidden_dim // 2)
        self.conv2 = GCNConv(hidden_dim // 2, hidden_dim)
        self.conv3 = GCNConv(hidden_dim, hidden_dim)
        
        # 判别头
        self.discriminator = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim // 2, 1)
        )
        
        # 分类头（辅助任务）
        self.classifier = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.LeakyReLU(0.2),
            nn.Linear(hidden_dim // 2, num_classes)
        )
    
    def forward(self, graphs):
        """
        Args:
            graphs: List[Data] 图列表
        
        Returns:
            validity: [batch, 1] 真实性分数
            class_logits: [batch, num_classes] 类别预测
        """
        batch_embeddings = []
        
        for graph in graphs:
            h = graph.x
            edge_index = graph.edge_index
            edge_attr = graph.edge_attr if graph.edge_attr is not None else None
            
            # 图卷积
            h = F.leaky_relu(self.conv1(h, edge_index), 0.2)
            h = F.leaky_relu(self.conv2(h, edge_index), 0.2)
            h = F.leaky_relu(self.conv3(h, edge_index), 0.2)
            
            # 全局池化
            h_global = h.mean(dim=0)
            batch_embeddings.append(h_global)
        
        batch_embeddings = torch.stack(batch_embeddings)
        
        # 判别和分类
        validity = self.discriminator(batch_embeddings)
        class_logits = self.classifier(batch_embeddings)
        
        return validity, class_logits


class GraphGAN(nn.Module):
    """
    图生成对抗网络用于脑图增强
    """
    
    def __init__(self, num_nodes, latent_dim=100, hidden_dim=256):
        super().__init__()
        self.num_nodes = num_nodes
        self.latent_dim = latent_dim
        
        self.generator = GraphGenerator(latent_dim, num_nodes, hidden_dim)
        self.discriminator = GraphDiscriminator(num_nodes, hidden_dim)
    
    def generate(self, num_samples, labels=None, device='cpu'):
        """生成增强样本"""
        z = torch.randn(num_samples, self.latent_dim).to(device)
        if labels is not None:
            labels = labels.to(device)
        return self.generator(z, labels)
    
    def discriminate(self, graphs):
        """判别图真实性"""
        return self.discriminator(graphs)


def train_graphgan(
    real_graphs: List[Data],
    labels: torch.Tensor,
    num_epochs: int = 200,
    batch_size: int = 32,
    latent_dim: int = 100,
    device: str = 'cpu'
):
    """
    训练GraphGAN
    
    Args:
        real_graphs: 真实脑图数据
        labels: 类别标签
        num_epochs: 训练轮数
        batch_size: 批大小
        latent_dim: 潜在维度
        device: 计算设备
    
    Returns:
        generator: 训练好的生成器
    """
    num_nodes = real_graphs[0].x.shape[0]
    
    # 创建模型
    model = GraphGAN(num_nodes, latent_dim).to(device)
    
    # 优化器
    g_optimizer = torch.optim.Adam(model.generator.parameters(), lr=0.0002, betas=(0.5, 0.999))
    d_optimizer = torch.optim.Adam(model.discriminator.parameters(), lr=0.0002, betas=(0.5, 0.999))
    
    # 损失函数
    adversarial_loss = nn.BCEWithLogitsLoss()
    classification_loss = nn.CrossEntropyLoss()
    
    # 数据加载器
    dataloader = DataLoader(real_graphs, batch_size=batch_size, shuffle=True)
    
    for epoch in range(num_epochs):
        for batch in dataloader:
            batch_size = batch.num_graphs
            
            # 真实标签
            real_labels = torch.ones(batch_size, 1).to(device)
            fake_labels = torch.zeros(batch_size, 1).to(device)
            
            # ========== 训练判别器 ==========
            d_optimizer.zero_grad()
            
            # 真实图
            real_validity, real_class = model.discriminator(batch.to_data_list())
            d_real_loss = adversarial_loss(real_validity, real_labels)
            
            # 生成图
            z = torch.randn(batch_size, latent_dim).to(device)
            fake_graphs = model.generator(z)
            fake_validity, _ = model.discriminator(fake_graphs)
            d_fake_loss = adversarial_loss(fake_validity, fake_labels)
            
            # 分类损失
            batch_labels = labels[:batch_size].to(device)
            c_loss = classification_loss(real_class, batch_labels)
            
            d_loss = (d_real_loss + d_fake_loss) / 2 + 0.5 * c_loss
            d_loss.backward()
            d_optimizer.step()
            
            # ========== 训练生成器 ==========
            g_optimizer.zero_grad()
            
            z = torch.randn(batch_size, latent_dim).to(device)
            fake_graphs = model.generator(z, batch_labels)
            fake_validity, fake_class = model.discriminator(fake_graphs)
            
            # 对抗损失
            g_adv_loss = adversarial_loss(fake_validity, real_labels)
            # 分类损失（让生成的图属于正确类别）
            g_class_loss = classification_loss(fake_class, batch_labels)
            
            g_loss = g_adv_loss + 0.5 * g_class_loss
            g_loss.backward()
            g_optimizer.step()
        
        if (epoch + 1) % 20 == 0:
            print(f"Epoch [{epoch+1}/{num_epochs}] "
                  f"D_loss: {d_loss.item():.4f} G_loss: {g_loss.item():.4f}")
    
    return model.generator


def augment_from_template(
    cbt: torch.Tensor,
    generator: GraphGenerator,
    num_augmented: int,
    class_label: int,
    perturbation_scale: float = 0.1,
    device: str = 'cpu'
):
    """
    从CBT模板生成增强数据
    
    Args:
        cbt: 连接脑模板 [num_nodes, num_nodes]
        generator: 训练好的图生成器
        num_augmented: 要生成的增强样本数
        class_label: 类别标签
        perturbation_scale: CBT扰动强度
        device: 计算设备
    
    Returns:
        augmented_graphs: 增强的图列表
    """
    num_nodes = cbt.shape[0]
    augmented_graphs = []
    
    # 将CBT作为条件或参考
    cbt_flat = cbt[torch.triu_indices(num_nodes, num_nodes, offset=1)]
    
    for _ in range(num_augmented):
        # 添加噪声扰动
        noise = torch.randn_like(cbt_flat) * perturbation_scale
        perturbed = torch.clamp(cbt_flat + noise, 0, 1)
        
        # 或者使用生成器
        z = torch.randn(1, generator.latent_dim).to(device)
        labels = torch.tensor([class_label]).to(device)
        
        with torch.no_grad():
            gen_graphs = generator(z, labels)
        
        augmented_graphs.extend(gen_graphs)
    
    return augmented_graphs


def one_shot_classification(
    template: torch.Tensor,
    augmented_graphs: List[Data],
    test_graph: Data,
    generator: GraphGenerator,
    k_neighbors: int = 5
):
    """
    单样本学习分类
    
    Args:
        template: 类别模板
        augmented_graphs: 增强的训练图
        test_graph: 测试图
        generator: 图生成器
        k_neighbors: KNN邻居数
    
    Returns:
        predicted_label: 预测的类别
    """
    # 简化：使用图相似度
    # 实际实现中应使用图神经网络分类器
    
    def graph_similarity(g1, g2):
        """计算图相似度（边权重的余弦相似度）"""
        adj1 = torch.zeros(g1.num_nodes, g1.num_nodes)
        adj1[g1.edge_index[0], g1.edge_index[1]] = g1.edge_attr.squeeze()
        
        adj2 = torch.zeros(g2.num_nodes, g2.num_nodes)
        adj2[g2.edge_index[0], g2.edge_index[1]] = g2.edge_attr.squeeze()
        
        # 余弦相似度
        return F.cosine_similarity(
            adj1.flatten().unsqueeze(0),
            adj2.flatten().unsqueeze(0)
        ).item()
    
    # 计算与增强图的相似度
    similarities = [graph_similarity(test_graph, aug) for aug in augmented_graphs]
    
    # 找最相似的
    best_idx = np.argmax(similarities)
    
    return best_idx, similarities[best_idx]


def evaluate_augmentation(
    real_graphs: List[Data],
    labels: torch.Tensor,
    generator: GraphGenerator,
    test_split: float = 0.2
):
    """
    评估增强效果
    
    Args:
        real_graphs: 真实图数据
        labels: 标签
        generator: 训练好的生成器
        test_split: 测试集比例
    """
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, f1_score
    
    # 划分数据集
    train_graphs, test_graphs, train_labels, test_labels = train_test_split(
        real_graphs, labels.numpy(), test_size=test_split, stratify=labels
    )
    
    print(f"Training samples: {len(train_graphs)}")
    print(f"Test samples: {len(test_graphs)}")
    
    # 生成增强数据
    num_augmented = len(train_graphs)  # 与原始数据量相同
    augmented_AD = augment_from_template(
        torch.rand(50, 50),  # 假设的AD模板
        generator,
        num_augmented // 2,
        class_label=0  # AD
    )
    augmented_LMCI = augment_from_template(
        torch.rand(50, 50),  # 假设的LMCI模板
        generator,
        num_augmented // 2,
        class_label=1  # LMCI
    )
    
    # 合并增强数据
    augmented_graphs = augmented_AD + augmented_LMCI
    augmented_labels = torch.cat([
        torch.zeros(len(augmented_AD)),
        torch.ones(len(augmented_LMCI))
    ])
    
    print(f"Augmented samples: {len(augmented_graphs)}")
    
    # 评估
    correct = 0
    for test_graph, test_label in zip(test_graphs, test_labels):
        pred_idx, _ = one_shot_classification(
            None,
            train_graphs + augmented_graphs,
            test_graph,
            generator
        )
        if pred_idx < len(train_graphs):
            pred = train_labels[pred_idx]
        else:
            pred = augmented_labels[pred_idx - len(train_graphs)]
        
        if pred == test_label:
            correct += 1
    
    accuracy = correct / len(test_graphs)
    print(f"\nAccuracy with augmentation: {accuracy:.4f}")
    
    # 基线：无增强
    correct_baseline = 0
    for test_graph, test_label in zip(test_graphs, test_labels):
        pred_idx, _ = one_shot_classification(
            None,
            train_graphs,
            test_graph,
            generator
        )
        if train_labels[pred_idx] == test_label:
            correct_baseline += 1
    
    baseline_accuracy = correct_baseline / len(test_graphs)
    print(f"Accuracy without augmentation: {baseline_accuracy:.4f}")
    print(f"Improvement: {(accuracy - baseline_accuracy) * 100:.2f}%")
    
    return accuracy, baseline_accuracy


if __name__ == "__main__":
    # 示例：AD vs LMCI分类
    print("=== Brain Graph Augmentation Demo ===\n")
    
    # 模拟数据
    num_subjects = 100
    num_nodes = 50
    
    # 生成模拟图
    real_graphs = []
    for i in range(num_subjects):
        adj = torch.rand(num_nodes, num_nodes)
        adj = (adj + adj.T) / 2
        edge_index = (adj > 0.5).nonzero(as_tuple=False).t()
        real_graphs.append(Data(
            x=torch.randn(num_nodes, 16),
            edge_index=edge_index,
            edge_attr=adj[adj > 0.5].unsqueeze(-1)
        ))
    
    # 标签：0=AD, 1=LMCI
    labels = torch.randint(0, 2, (num_subjects,))
    
    # 训练GraphGAN
    print("Training GraphGAN...")
    generator = train_graphgan(
        real_graphs, labels,
        num_epochs=100,
        batch_size=16
    )
    
    # 评估增强效果
    print("\nEvaluating augmentation...")
    evaluate_augmentation(real_graphs, labels, generator)
```

## 应用场景

1. **疾病分类**
   - Alzheimer's Disease vs Late Mild Cognitive Impairment
   - 数据稀缺场景的分类
   - 平衡类别分布

2. **单样本学习**
   - 只有一个模板时的增强
   - 快速适应新类别
   - 小样本场景验证

3. **生物标志物发现**
   - 从CBT提取判别性连接
   - 群体指纹识别
   - 疾病特异性模式

## 数据集

- AD/LMCI数据集
- 需要预构建的CBT模板
- 支持任意脑连接矩阵

## 关键优势

- **单模板增强**：从唯一模板生成多样化数据
- **类别条件**：保持标签一致性
- **图结构保持**：确保拓扑合理性
- **指标平衡**：提升整体分类性能

## 参考文献

- arXiv:2212.07790 - Population Template-Based Brain Graph Augmentation for Improving One-Shot Learning Classification