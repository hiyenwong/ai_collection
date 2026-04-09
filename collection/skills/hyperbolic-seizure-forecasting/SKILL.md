# Hyperbolic Brain Network Embedding for Seizure Forecasting

**来源论文：** arXiv:2406.10184 - Hyperbolic embedding of brain networks as a tool for epileptic seizures forecasting
**效用评分：** 0.98
**创建时间：** 2026-03-24 15:03
**发表期刊：** Physical Review Research

---

## 概述

使用双曲嵌入脑网络从颅内 EEG 连接性数据中识别癫痫前期状态，实现癫痫发作预测。准确率 85%，F1-score 89%。

## 激活关键词

- hyperbolic brain network
- seizure forecasting
- epileptic prediction
- intracranial EEG connectivity
- Poincaré embedding
- preictal state detection
- 双曲脑网络
- 癫痫预测

## 核心创新

```
癫痫预测挑战:
┌─────────────────────────────────────────┐
│ 传统方法:                                │
│ • 线性特征分析                           │
│ • 欧几里得空间嵌入                       │
│ • 忽略脑网络层级结构                     │
└─────────────────────────────────────────┘
                    ↓
         双曲嵌入方法
┌─────────────────────────────────────────┐
│ • 双曲空间天然适合层级网络               │
│ • 捕捉非平凡连接模式                     │
│ • 区分发作前期 vs 发作间期               │
│ • 24小时内预测准确率 85%                 │
└─────────────────────────────────────────┘
```

## 核心方法

### 1. 双曲嵌入模型

```python
import torch
import torch.nn as nn
import numpy as np

class HyperbolicBrainEmbedding(nn.Module):
    """
    脑网络双曲嵌入模型
    
    将脑网络嵌入到 Poincaré 球中
    """
    def __init__(self, n_nodes, dim=2, c=1.0):
        """
        Args:
            n_nodes: 脑区/电极数量
            dim: 嵌入维度
            c: 曲率参数
        """
        super().__init__()
        self.n_nodes = n_nodes
        self.dim = dim
        self.c = c  # 曲率
        
        # 双曲嵌入参数
        # 使用指数映射确保在 Poincaré 球内
        self.embeddings = nn.Parameter(
            torch.randn(n_nodes, dim) * 0.01
        )
    
    def expmap0(self, v):
        """
        从原点的指数映射
        
        将切空间的向量映射到 Poincaré 球
        """
        norm_v = torch.norm(v, dim=-1, keepdim=True)
        exp_v = torch.tanh(torch.sqrt(self.c) * norm_v) * v / (norm_v + 1e-8)
        return exp_v
    
    def get_embeddings(self):
        """
        获取 Poincaré 球中的嵌入
        """
        return self.expmap0(self.embeddings)
    
    def hyperbolic_distance(self, x, y):
        """
        Poincaré 球中的双曲距离
        
        d(x,y) = arcosh(1 + 2c * ||x-y||^2 / ((1-c||x||^2)(1-c||y||^2)))
        """
        sqrt_c = np.sqrt(self.c)
        
        # 归一化
        x_norm = torch.clamp(torch.norm(x, dim=-1), max=1 - 1e-5)
        y_norm = torch.clamp(torch.norm(y, dim=-1), max=1 - 1e-5)
        
        # 距离公式
        diff = x - y
        diff_norm = torch.norm(diff, dim=-1)
        
        numerator = 2 * self.c * diff_norm ** 2
        denominator = (1 - self.c * x_norm ** 2) * (1 - self.c * y_norm ** 2)
        
        dist = torch.acosh(1 + numerator / denominator) / sqrt_c
        
        return dist
    
    def forward(self, adj_matrix):
        """
        计算嵌入损失
        
        目标：连接的节点在双曲空间中距离近
        """
        embeddings = self.get_embeddings()
        
        loss = 0
        n_pairs = 0
        
        for i in range(self.n_nodes):
            for j in range(i + 1, self.n_nodes):
                dist = self.hyperbotic_distance(embeddings[i], embeddings[j])
                
                if adj_matrix[i, j] > 0:
                    # 连接的节点应该近
                    loss += dist
                else:
                    # 不连接的节点应该远
                    loss += torch.exp(-dist)
                
                n_pairs += 1
        
        return loss / n_pairs
```

### 2. 发作预测模型

```python
class SeizureForecaster(nn.Module):
    """
    癫痫发作预测模型
    
    结合双曲嵌入和机器学习
    """
    def __init__(self, n_electrodes, hidden_dim=128):
        super().__init__()
        
        # 双曲嵌入层
        self.hyperbolic_embed = HyperbolicBrainEmbedding(n_electrodes)
        
        # 特征提取
        self.feature_extractor = nn.Sequential(
            nn.Linear(n_electrodes * 2, hidden_dim),  # 坐标 + 双曲距离特征
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU()
        )
        
        # 分类器
        self.classifier = nn.Sequential(
            nn.Linear(hidden_dim // 2, 32),
            nn.ReLU(),
            nn.Linear(32, 2)  # 发作前期 vs 发作间期
        )
        
        # 概率估计
        self.probability_head = nn.Sequential(
            nn.Linear(hidden_dim // 2, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
            nn.Sigmoid()
        )
    
    def extract_hyperbolic_features(self, adj_matrix):
        """
        提取双曲空间特征
        """
        embeddings = self.hyperbolic_embed.get_embeddings()
        
        # 1. 嵌入坐标
        coord_features = embeddings.flatten()
        
        # 2. 双曲距离统计
        dist_matrix = self.compute_distance_matrix(embeddings)
        dist_stats = torch.stack([
            dist_matrix.mean(),
            dist_matrix.std(),
            dist_matrix.min(),
            dist_matrix.max()
        ])
        
        # 3. 径向分布（距离原点的分布）
        radii = torch.norm(embeddings, dim=-1)
        radius_stats = torch.stack([
            radii.mean(),
            radii.std(),
            torch.quantile(radii, 0.25),
            torch.quantile(radii, 0.75)
        ])
        
        # 4. 角度分布
        angles = torch.atan2(embeddings[:, 1], embeddings[:, 0])
        angle_stats = torch.stack([
            angles.mean(),
            angles.std()
        ])
        
        features = torch.cat([coord_features, dist_stats, radius_stats, angle_stats])
        
        return features
    
    def compute_distance_matrix(self, embeddings):
        """
        计算所有节点对的双曲距离矩阵
        """
        n = embeddings.size(0)
        dist_matrix = torch.zeros(n, n)
        
        for i in range(n):
            for j in range(i + 1, n):
                d = self.hyperbolic_embed.hyperbolic_distance(embeddings[i], embeddings[j])
                dist_matrix[i, j] = d
                dist_matrix[j, i] = d
        
        return dist_matrix
    
    def forward(self, adj_matrix):
        """
        预测癫痫发作概率
        """
        # 提取双曲特征
        hyperbolic_features = self.extract_hyperbolic_features(adj_matrix)
        
        # 特征提取
        features = self.feature_extractor(hyperbolic_features.unsqueeze(0))
        
        # 分类
        logits = self.classifier(features)
        
        # 发作概率
        seizure_prob = self.probability_head(features)
        
        return logits, seizure_prob
```

### 3. 连接性计算

```python
import scipy.signal as signal
from scipy.stats import pearsonr

class iEEGConnectivity:
    """
    颅内 EEG 连接性计算
    """
    def __init__(self, n_electrodes, freq_bands=None):
        self.n_electrodes = n_electrodes
        self.freq_bands = freq_bands or {
            'delta': (0.5, 4),
            'theta': (4, 8),
            'alpha': (8, 13),
            'beta': (13, 30),
            'gamma': (30, 100)
        }
    
    def compute_phase_locking_value(self, eeg_data):
        """
        相位锁定值 (PLV)
        """
        n_channels, n_timepoints = eeg_data.shape
        plv_matrix = np.zeros((n_channels, n_channels))
        
        # Hilbert 变换获取相位
        phases = np.angle(signal.hilbert(eeg_data, axis=1))
        
        for i in range(n_channels):
            for j in range(i + 1, n_channels):
                phase_diff = phases[i] - phases[j]
                plv = np.abs(np.mean(np.exp(1j * phase_diff)))
                plv_matrix[i, j] = plv
                plv_matrix[j, i] = plv
        
        return plv_matrix
    
    def compute_amplitude_envelope_correlation(self, eeg_data):
        """
        幅值包络相关性 (AEC)
        """
        # Hilbert 变换获取包络
        envelopes = np.abs(signal.hilbert(eeg_data, axis=1))
        
        # Pearson 相关
        aec_matrix = np.corrcoef(envelopes)
        
        return aec_matrix
    
    def compute_imaginary_coherence(self, eeg_data, fs):
        """
        虚相干性 (ImCoh)
        """
        n_channels = eeg_data.shape[0]
        imcoh_matrix = np.zeros((n_channels, n_channels))
        
        for i in range(n_channels):
            for j in range(i + 1, n_channels):
                f, Cxy = signal.coherence(eeg_data[i], eeg_data[j], fs=fs)
                # 取虚部
                imcoh = np.imag(Cxy)
                imcoh_matrix[i, j] = np.mean(imcoh)
                imcoh_matrix[j, i] = imcoh_matrix[i, j]
        
        return imcoh_matrix
```

### 4. 训练和评估

```python
def train_seizure_forecaster(model, train_data, val_data, epochs=100):
    """
    训练癫痫预测模型
    """
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    cls_criterion = nn.CrossEntropyLoss()
    
    best_val_acc = 0
    
    for epoch in range(epochs):
        # 训练
        model.train()
        train_loss = 0
        
        for batch in train_data:
            adj = batch['connectivity']
            label = batch['label']  # 0: 发作间期, 1: 发作前期
            
            optimizer.zero_grad()
            
            logits, prob = model(adj)
            
            # 分类损失
            loss = cls_criterion(logits, label)
            
            # Brier 分数正则化（校准概率）
            brier_loss = torch.mean((prob.squeeze() - label.float()) ** 2)
            loss += 0.1 * brier_loss
            
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()
        
        # 验证
        model.eval()
        val_correct = 0
        val_total = 0
        all_probs = []
        all_labels = []
        
        with torch.no_grad():
            for batch in val_data:
                adj = batch['connectivity']
                label = batch['label']
                
                logits, prob = model(adj)
                predicted = torch.argmax(logits, dim=1)
                
                val_correct += (predicted == label).sum().item()
                val_total += label.size(0)
                
                all_probs.append(prob.item())
                all_labels.append(label.item())
        
        val_acc = val_correct / val_total
        
        # 计算 F1-score
        f1 = compute_f1_score(all_labels, all_probs)
        
        # 计算 Brier 分数
        brier = compute_brier_score(all_labels, all_probs)
        
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), 'best_seizure_model.pt')
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch}: Loss={train_loss/len(train_data):.4f}, "
                  f"Val Acc={val_acc:.2%}, F1={f1:.2%}, Brier={brier:.4f}")

def compute_brier_score(labels, probs):
    """
    计算 Brier 分数
    
    BS = 1/N * Σ(p_i - y_i)^2
    
    越低越好
    """
    return np.mean((np.array(probs) - np.array(labels)) ** 2)

def compute_brier_skill_score(labels, probs):
    """
    计算 Brier 技能分数
    
    BSS = 1 - BS / BS_ref
    
    BS_ref 是基准模型的 Brier 分数（通常用气候频率）
    """
    bs = compute_brier_score(labels, probs)
    bs_ref = np.mean((np.mean(labels) - np.array(labels)) ** 2)
    
    return 1 - bs / bs_ref
```

### 5. 临床应用

```python
class SeizurePredictionPipeline:
    """
    癫痫预测完整流程
    """
    def __init__(self, model_path, n_electrodes):
        self.model = SeizureForecaster(n_electrodes)
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval()
        
        self.connectivity = iEEGConnectivity(n_electrodes)
    
    def predict_from_eeg(self, eeg_segment, threshold=0.7):
        """
        从 EEG 段预测癫痫发作概率
        
        Args:
            eeg_segment: [n_electrodes, n_timepoints]
            threshold: 预警阈值
        
        Returns:
            预测结果和风险等级
        """
        # 计算连接性
        adj = self.connectivity.compute_phase_locking_value(eeg_segment)
        
        # 预测
        with torch.no_grad():
            logits, prob = self.model(torch.tensor(adj))
        
        seizure_prob = prob.item()
        
        # 风险等级
        if seizure_prob > threshold:
            risk_level = "HIGH"
            alert = "Seizure likely within 24 hours"
        elif seizure_prob > threshold / 2:
            risk_level = "MEDIUM"
            alert = "Elevated seizure risk"
        else:
            risk_level = "LOW"
            alert = "Normal interictal state"
        
        return {
            'probability': seizure_prob,
            'risk_level': risk_level,
            'alert': alert
        }
```

## 实验结果

论文报告的性能指标：

| 指标 | 数值 |
|------|------|
| 分类准确率 | 85% |
| 预测准确率 | 87% |
| F1-score | 89% |
| Brier 分数 | 0.12 |
| Brier 技能分数 | 0.37 |

## 应用场景

1. **癫痫发作预测** - 24小时内预警
2. **患者监测** - 实时风险评估
3. **治疗优化** - 个性化干预时机
4. **生物标志物** - 发作前期特征

## 临床意义

- **预警系统** - 提前通知患者和家属
- **生活质量** - 减少不确定性焦虑
- **精准治疗** - 按需给药而非固定方案

## 相关技能

- `hyperbolic-brain-network-neurodegeneration` - 双曲嵌入神经退行
- `seizure-risk-forecasting` - 癫痫风险预测
- `eeg-brain-connectivity-bci` - EEG 脑连接 BCI
- `graph-laplacian-denoising` - 图拉普拉斯去噪

---

_此技能基于双曲嵌入方法，用于癫痫发作预测的生物标志物开发_
## Description
Framework from arXiv papers. See paper reference for details.
## Activation Keywords

- hyperbolic-seizure-forecasting
- hyperbolic-seizure-forecasting 技能
- hyperbolic-seizure-forecasting skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents

1. **Understand the Request**: Analyze what the user needs related to this skill's domain.
2. **Search for Information**: Use web_search to find relevant papers or documentation.
3. **Apply the Framework**: Follow the methodology described in the skill's key concepts.
4. **Provide Results**: Summarize findings and actionable recommendations.
5. **Verify Accuracy**: Cross-check key facts before presenting to user.

## Examples

### Example 1: Basic Usage

**User:** How can I apply hyperbolic-seizure-forecasting?

**Agent:** I'll help you understand and apply hyperbolic-seizure-forecasting...

### Example 2: Advanced Application

**User:** What are the key considerations for hyperbolic-seizure-forecasting?

**Agent:** Let me search for the latest research and best practices...
